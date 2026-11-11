---
name: vietnam-vat
description: >
  Use this skill whenever asked to prepare, review, or classify
  transactions for a Vietnam VAT (thuế giá trị gia tăng / GTGT) return, classify
  transactions for Vietnamese VAT purposes, or advise on VAT registration and
  filing in Vietnam. Trigger on phrases like "thuế GTGT", "Vietnam VAT",
  "tờ khai thuế GTGT", "hóa đơn điện tử", "phương pháp khấu trừ",
  "phương pháp trực tiếp", or any Vietnam VAT request. ALWAYS read this skill
  before touching any Vietnam VAT work. It covers supplies from 1 July 2025
  under Law 48/2024/QH15, with 10%, 8%, 5% and 0% rates and the
  VND 1,000,000,000 household threshold. This Tier 2 draft supports source
  checking and reviewer questions; it does not authorise a filing, a payment
  or a tax position.
version: 2.1
jurisdiction: VN
tax_year: 2026
tax_year_notes: "VAT periods from 1 July 2025, read at 5 November 2026. VAT has no tax year: the rate and rules follow the tax point of each supply. Supplies before 1 July 2025 fall under Law 13/2008/QH12 and are not classified here. On the texts read, the 8% rate covers 1 July 2025 to 31 December 2026, and no extension was found."
last_updated: 2026-11-11
depends_on:
  - vat-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
domain: vat-gst
type: situation-rules
---

# Vietnam VAT v2.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Organisations, households and individuals that produce or trade VAT-taxable goods and services in Vietnam (Cộng hòa Xã hội Chủ nghĩa Việt Nam), importers, and Vietnamese businesses that buy services from foreign parties (VAT Law art 4), and the reviewers working with them. The tax is thuế giá trị gia tăng (GTGT, VAT), levied on goods and services used for production, trade and consumption in Vietnam (art 3). The tax authority is the Cục Thuế (Tax Department) of the Ministry of Finance, with provincial tax offices, and Customs (Hải quan) handles import VAT. Amounts are in VND (Vietnamese dong, đồng). Returns go electronically through the Hệ thống thông tin quản lý thuế (Tax Management Information System), and Decree 254/2026/ND-CP art 41.3(a) gives eTax Mobile as an example of that system.

Coverage label: VAT periods from 1 July 2025, read at 5 November 2026. VAT has no tax year: the rate and rules follow the tax point of each supply. Supplies before 1 July 2025 fall under Law 13/2008/QH12 and are not classified here. On the texts read, the 8% rate covers 1 July 2025 to 31 December 2026, and no extension was found.

### What this file is

This is a country slot file for `vat-workflow-base`, which owns the workflow, output specification, question form and self-checks. Its status is Tier 2, pending review. It was contributed by the Open Accountants Community. No qualified practitioner has reviewed or approved this text, and a sign-off by a Vietnam-licensed đại lý thuế (tax agent) or CPA is still needed.

**Operational hold.** `vat-workflow-base` Step 1 requires a regional or directive layer as well as this file. None for Vietnam was found in this repository at 5 November 2026, so Step 1 stops the workflow. Use this file as a reference only. Stop before producing a workbook, return or filing instruction until a regional layer or an approved non-EU exception exists.

Every classification is a working paper for reviewer checking. Input VAT is provisional until the document in The base is checked.

### Which law applies to which period

| Tax point or act | Governing text | Status at 5 November 2026 |
| --- | --- | --- |
| Supplies before 1 July 2025 | Law 13/2008/QH12, as amended by Laws 31/2013/QH13, 71/2014/QH13 and 106/2016/QH13 | Ceased when Law 48/2024/QH15 commenced (art 18.3). Not read and not classified here: R-VN-8 |
| Supplies from 1 July 2025 | Law 48/2024/QH15, passed 26 November 2024, in force 1 July 2025 (art 18), amended by Law 90/2025/QH15 (from 1 July 2025), Law 149/2025/QH15 (from 1 January 2026) and Law 09/2026/QH16 arts 1 to 3 (from 1 January 2026). Consolidated text 12/VBHN-VPQH is dated before Law 09/2026/QH16 | Enacted and in force. The consolidated text still prints VND 500 million in art 5.25: Law 09/2026/QH16 art 2 overrides it |
| Supplies from 1 July 2025 | Decree 181/2025/ND-CP, amended by Decree 359/2025/ND-CP (from 1 January 2026) and Decree 144/2026/ND-CP (from 20 June 2026); Circular 69/2025/TT-BTC | In force at the dates each states |
| 1 July 2025 to 31 December 2026 | Resolution 204/2025/QH15 and Decree 174/2025/ND-CP: the 8% rate | Enacted, ending on the last day of 2026. The Resolution was read as reproduced in the notes to 12/VBHN-VPQH, not as a separate file |
| From 1 January 2026, household and individual businesses | Decree 68/2026/ND-CP as amended by Decree 141/2026/ND-CP; Law 108/2025/QH15 art 13 | In force. Household declaration replaces the presumptive tax (thuế khoán) method |
| Tax administration from 1 July 2026 | Law 108/2025/QH15 (passed 10 December 2025; art 52.1), Decree 252/2026/ND-CP, Circular 89/2026/TT-BTC as corrected by Decision 2551/QD-BTC | In force. Law 38/2019/QH14 ends on that date (art 52.3) and was not read, so filings and acts before it are held |
| E-invoices from 1 July 2026 | Decree 254/2026/ND-CP (art 43.1) | In force. It repeals Decree 123/2020/ND-CP, art 1 of Decree 41/2022/ND-CP and Decree 70/2025/ND-CP (art 43.2). Those texts and Circular 78/2021/TT-BTC, which governed earlier invoices, were not read. Circular 91/2026/TT-BTC carries the detail from the same date (art 25.1) and ended Circular 32/2025/TT-BTC (art 25.2), which was not read |
| Tax and invoice penalties | Law 108/2025/QH15 arts 44 and 45, with Decree 125/2020/ND-CP as amended by Decrees 102/2021/ND-CP and 310/2025/ND-CP (from 16 January 2026), kept in force by Decree 252/2026/ND-CP art 74.4 | In force until a replacement decree |

### Refusals and boundaries

These are the country refusals for `vat-workflow-base`. If a trigger fires, stop, output the message verbatim and end, as Step 5 of the base requires. There is no partial classification.

- **R-VN-1, direct method taxpayers (phương pháp trực tiếp).** Trigger: the client calculates VAT by the direct method, on revenue under VAT Law art 12.2 or on value added for gold, silver and gemstones under art 12.1. Message: 'Direct method taxpayers pay a percentage of revenue, or for gold, silver and gemstones the VAT rate on value added. They claim no input credit in the deduction form. This workflow covers the deduction method and stops here. Confirm the method with a licensed tax agent.'
- **R-VN-2, businesses at or below VND 1 billion.** Trigger: a household or individual business with annual revenue of VND 1,000,000,000 or less, or an enterprise or cooperative below that amount that has not opted into the deduction method. Message: 'A household or individual business with annual revenue of VND 1 billion or less is not subject to VAT from 1 January 2026, but must notify its revenue. An enterprise below VND 1 billion still pays VAT, by the direct method unless it opts into the deduction method; any exemption it has is from corporate income tax, not VAT (Law 67/2025/QH15 art 4.14a, added by Law 09/2026/QH16 art 3; see `vn-corporate-income-tax`). This workflow stops here. Confirm the business type and method.'
- **R-VN-3, shared input without a ratio.** Trigger: the business makes taxable and exempt sales, cannot separate shared input VAT, and has not given revenue by class for the period. Message: 'Shared input VAT is split by accounts or, failing that, by taxable revenue over total revenue for the tax period. Without that revenue the split cannot be made. This workflow stops here. Provide revenue by class, or escalate to a licensed tax agent.'
- **R-VN-4, real estate and construction.** Trigger: the client sells real estate it developed, transfers land use rights as a business, or supplies construction or installation work. Message: 'Real estate and construction have their own tax point and price rules. This workflow stops here. Escalate to a licensed tax agent.'
- **R-VN-5, foreign contractor tax.** Trigger: the client asks to compute or file foreign contractor withholding, or a foreign party's VAT under Circular 69/2025/TT-BTC art 9 or Decree 252/2026/ND-CP arts 40 to 45. Message: 'Foreign contractor tax combines VAT and corporate income tax and is filed apart from the ordinary GTGT return. This workflow stops here. Escalate to a licensed tax agent.'
- **R-VN-6, excessive ambiguity.** This is a workflow limit set by this file for the base's excessive-ambiguity contract, not a rule of law. Trigger: more than 10 questions survive the filtering and grouping in Step 6.5. Message: 'More than 10 questions remain after the required filtering and grouping. This VAT workflow cannot complete the return. Please refer the records and unresolved questions to a qualified practitioner.'
- **R-VN-7, refund claim.** Trigger: the client asks to prepare or file a VAT refund (hoàn thuế). Message: 'A VAT refund needs a separate file, the conditions in VAT Law art 15 and the documents behind them. This workflow stops here. Escalate to a licensed tax agent.'
- **R-VN-8, supplies before 1 July 2025.** Trigger: a supply with a tax point before 1 July 2025 must be classified or corrected. Message: 'Supplies before 1 July 2025 fall under Law 13/2008/QH12, which this file has not read. This workflow stops here. Refer them to a licensed tax agent.'

### Prohibitions

- Never claim input VAT without a compliant hóa đơn điện tử (e-invoice) or, for imports and VAT paid on behalf of a foreign supplier, the tax payment document (VAT Law art 14.2(a); Decree 181/2025/ND-CP art 25).
- Never zero-rate a service without confirming foreign consumption, the contract and non-cash payment, and that the service is not on the art 9.1(d) list.
- Never apply 8% to an excluded supply, or to any supply after 31 December 2026 without a confirmed extension.
- Never use the deduction method for a direct-method taxpayer.
- Never ignore foreign contractor tax for an international service payment.
- Never present a calculation as definitive; direct it to a licensed Vietnamese tax agent (đại lý thuế).

### Required inputs

| Level | Items |
| --- | --- |
| Minimum viable | Bank statement for the period in CSV, PDF or pasted text. Confirmation of the VAT method (deduction, phương pháp khấu trừ, or direct, phương pháp trực tiếp) and the MST (mã số thuế, tax code). |
| Recommended | Hóa đơn GTGT (VAT invoices) for all purchases, electronic invoices (hóa đơn điện tử) for sales, the prior period return and the excess credit carried forward. |
| Ideal | Complete ledger, export customs declarations (tờ khai hải quan), asset register and full invoice register. |

Refusal policy: SOFT WARN where supporting documents are missing. No bank statement is a hard stop. Say: 'Input VAT credits in Vietnam require compliant hóa đơn GTGT (VAT invoices) or hóa đơn điện tử or, for imports and VAT paid on behalf of a foreign supplier, the tax payment document. All credits are provisional pending verification of the applicable invoice or tax payment document.'

The earlier version gave the MST as 10 digits. No text read fixes its length, and Decree 252/2026/ND-CP refers to issuing tax codes by personal identification number, so do not reject a tax code on length alone.

### Intake

Intake only. Under `vat-workflow-base` Step 6.5 questions come before any output: no working paper is built first with pending flags, and a fact still unanswered is Needs Input. Ask only what the data does not settle:

1. Mã số thuế (MST, tax code)?
2. Phương pháp tính thuế: khấu trừ (deduction) hay trực tiếp (direct)?
3. Kỳ khai thuế (tax period): theo tháng (monthly) hay theo quý (quarterly)?
4. Doanh thu năm trước (prior year revenue), for the method and tax period?
5. Any export sales? If yes: contract with the foreign party, non-cash payment, and for goods the customs declaration?
6. Any international services (Google, Microsoft and others)? Does the supplier issue Vietnamese invoices, or has VAT been paid on its behalf?
7. Số thuế GTGT còn được khấu trừ kỳ trước (excess credit carried forward)?
8. Any exempt sales (doanh thu không chịu thuế)?

## Rates, bands and thresholds

Each row applies to a tax point from 1 July 2025 unless it says otherwise. Revenue thresholds are not a registration threshold: no text read sets a turnover floor for a company to be a VAT taxpayer.

| Item | Amount or rate | Rule and limit | Source |
| --- | --- | --- | --- |
| Standard rate | 10% | Goods and services not on the 0% or 5% lists, including services that foreign suppliers without a permanent establishment supply through e-commerce and digital platforms. VAT Law art 9.3 | https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/02/12-vbhn-vpqh.pdf |
| Temporary rate | 8% | 1 July 2025 to 31 December 2026, for deduction method sellers, on art 9.3 goods and services. Excluded and staying at 10%: telecoms; finance, banking, securities and insurance; real estate business; metal products; mining products other than coal (Decree 174 art 1.1(a), Annex I); goods and services subject to special consumption tax other than petrol (art 1.1(b), Annex II). Applied uniformly at import, production, processing and trade. An item exempt or at 5% under the VAT Law gets no reduction (art 1.1(c)) | https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/7/174nd.signed.pdf |
| Direct method reduction | 20% off the percentage | Same period and same goods and services, for direct method businesses, including household and individual businesses, when they invoice. So 1% becomes 0.8%, 5% becomes 4%, 3% becomes 2.4% and 2% becomes 1.6%. Decree 174 art 1.2(b). The sales invoice must note the reduction in the words of art 1.3(b) | same |
| Reduced rate | 5% | Art 9.2 only: (a) clean water for production and domestic use, not bottled or jarred drinking water or other soft drinks; (b) fertiliser, ores for making it, plant protection products and livestock growth stimulants; (c) dredging for farming, crop care and pest control, preliminary processing and storage of farm products; (d) crop, planted forest (not timber or bamboo shoots), livestock and aquatic products, unprocessed or ordinarily pre-processed, unless exempt under art 5.1; (đ) listed latex forms, fishing nets, ropes and yarn; (e) products of jute, sedge, bamboo, nứa, leaf, straw, coconut husk and shell and water hyacinth, other handicrafts made from farm by-products, carded or combed cotton, and newsprint; (g) offshore fishing vessels and specialised farm machinery; (h) medical equipment, medicines and their ingredients; (i) listed teaching aids; (k) traditional and folk performing arts; (l) children's toys, and books not exempt under art 5.15; (m) science and technology services; (n) sale, lease and hire purchase of social housing. Detail in Decree 181 art 19 | https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/02/12-vbhn-vpqh.pdf |
| Zero rate | 0% | Exported goods, exported services and the art 9.1(c) list, unless art 9.1(d) excludes them. See Cross-border points. VAT Law art 9.1; Decree 181 arts 17 and 18 | same |
| Direct method, revenue | 1%, 5%, 3%, 2% | Percentage × revenue on the sales invoice, including surcharges. 1%: distribution and supply of goods. 5%: services, and construction without materials. 3%: production, transport, services tied to goods, and construction with materials. 2%: other business. VAT Law art 12.2(b) and (c); groups in Circular 69/2025/TT-BTC art 5 and Annex I. Who uses it: enterprises and cooperatives with annual revenue under VND 1,000,000,000 that have not opted in; household and individual businesses; foreign parties without a permanent establishment and without full accounts (not art 4.4 suppliers); other organisations outside art 11.2. Art 12.2(a) | same |
| Direct method, value added | VAT rate × value added | Buying, selling and working gold, silver and gemstones, on separate accounts: selling payment less matching purchase payment. VAT Law art 12.1. Negative value added carries within the year only (Decree 181 art 22) | same |
| Household threshold | VND 1,000,000,000 | From 1 January 2026, a household or individual business with annual revenue at or under this amount is not subject to VAT (Decree 68 art 3.1, as amended). Over it, it is subject and uses the direct method (art 3.2). VAT Law art 5.25, as rewritten by Law 09/2026/QH16 art 2, leaves the amount to the Government, and Decree 141 art 1.1 sets it. Periods from 1 January 2026 only: VAT Law art 18.2. The level for 1 July to 31 December 2025 is not read | https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/4/141-ndcp.signed.pdf |
| Deduction method threshold | VND 1,000,000,000 | Businesses, other than households and individuals, with annual revenue from this amount that keep full accounts and invoices use the deduction method. Below it, they may opt in. VAT Law art 11.2. Annual revenue is self-determined from returns, stable for 2 years; new entities annualise (Decree 181 art 21.1). This row is in the Law, not the decree | https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/02/12-vbhn-vpqh.pdf |
| Non-cash evidence floor | VND 5,000,000 | Purchases from this amount including VAT need a non-cash payment document for input credit, with the exceptions under Input VAT. Decree 181 art 26 | https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/7/181nd.signed.pdf |
| Car credit cap | VND 1,600,000,000 | Cars of 9 seats or fewer: input credit only on the part of the price up to this amount excluding VAT, except transport, tourism, hotel and test-drive use. Decree 181 art 24.4 | same |
| Refund floor | VND 300,000,000 | Unclaimed input in the month or quarter, or after 12 consecutive months or 4 consecutive quarters for a business with only 5% output; with several rates, the 5% share of input follows the Decree 181 art 31 split. VAT Law art 15 | https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/02/12-vbhn-vpqh.pdf |
| Export refund cap | 10% of export revenue | In the refund period; the excess carries forward. VAT Law art 15.1(b) | same |
| Quarterly election | VND 50,000,000,000 | Taxpayer on monthly filing with revenue for the previous year at or under this amount may choose quarterly filing; monthly is the default. Circular 89 art 19.1(a), (b.1.1) | https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/7/89-btc.signed.pdf |
| Household filing split | VND 50,000,000,000 | Household or individual business: quarterly up to this annual revenue, monthly over it. Decree 68 art 10.1 | https://xdcs.cdnchinhphu.vn/446259493575335936/2026/3/6/68-2026-nd-cp-05032026-signed-17727673940151875228819.pdf |

Art 9.4: a business selling at several rates, including exempt goods, declares by rate; if it does not, tax is at the highest rate of what it sells. Art 9.5: scrap and by-products take their own item's rate.

**Household and individual businesses from 1 January 2026.** The presumptive method ended: Decree 68 art 17.5 deals with those who paid by thuế khoán up to 2025 and moved to declaration from 1 January 2026, and the tax office does not use 2026 declared revenue to reopen earlier years, unless concealment of revenue is found. Annual revenue includes revenue that others have withheld and paid on the business's behalf (art 8.1(b)).

- At or under the threshold: notify actual revenue by 31 January of the next calendar year. If revenue passes the threshold during the year, declare and pay from the quarter it passes (art 8.1(a), as amended). New businesses: arts 9.1 and 9.2 set notices by 31 July and 31 January by start date.
- Over it: declare under art 10. Where coded or cash register e-invoices are used, the tax system creates a draft return, but the business stays responsible for the return (art 8.1(b)).
- E-invoices: over VND 1,000,000,000, tax-authority-coded e-invoices or cash register e-invoices with a data link are required, with a business location code for multi-site traders; at or under, they are optional if eligible, except that a household or individual business selling an asset that must register ownership or use right needs one (Decree 254 art 6.1(d)). A new or exceeding business registers within 30 days from the last day of the tax period in which cumulative revenue passes the threshold (Decree 68 art 8.5, replaced by Decree 141 art 1.2).
- Platforms with ordering and payment functions withhold VAT from households and individuals on their platforms (VAT Law art 4.5; Decree 252 art 43).
- Those who already declared for 2026 at revenue up to VND 1,000,000,000 follow Decree 141 art 4.1, with overpaid tax dealt with under Decree 68 art 12. An overpayment of VND 50,000 or less for the whole year is offset against the next period and is not refunded (Decree 252 art 29.4(b)).

## The base

### Taxable price and timing

**Deduction method.** VAT payable is output VAT less deductible input VAT (VAT Law art 11.1(a)). Output VAT is the taxable price × rate. Where an invoice shows a VAT-inclusive payment price, output is that price less the taxable price (art 11.1(b)); the gross-to-net rule is art 7.1(k), so for a price including 8%, net = gross ÷ 1.08. Excess input carries forward (art 14.1(đ)), so the amount for the period is max(output − deductible input − credit brought forward, 0), and the credit carried on is max(credit brought forward + deductible input − output, 0).

**Taxable price.** It includes surcharges the business keeps (Decree 181 art 14.1(a)) and excludes trade discounts given (art 14.2). It excludes receipts not related to a sale: money compensation, bonuses, third-party recoveries in insurance, amounts collected for others, fees for State collection work and financial receipts (art 14.1(b)).

**Exchange, internal use, gifts and promotions.** Goods or services used for exchange, internal use or gifts take the taxable price of the same or equivalent goods or services at that time (Decree 181 art 6.1). Internal use does not cover goods or services used to continue production or business, those used to serve production or business, including self-built fixed assets, or the asset transfers in art 6.1(c). Goods or services used for a promotion under commercial law are priced at zero, except that a price cut promotion is priced at the cut price. Samples and free gifts are zero, and the value of vouchers, prizes and customer loyalty rewards stays out of the taxable price of what is sold. A sale of these kinds outside the commercial law rules on promotion is priced as a gift (art 6.2).

**Tax point (art 8).** Goods: transfer of ownership or use, or the invoice date, whether or not paid. Services: completion or the invoice date, whether or not paid. Decree 181 arts 15 and 16 set special rules for exports, imports, telecoms, insurance, electricity, water, real estate, construction and oil and gas.

**Prepayment across the end of 2026.** A Government newspaper answer of 28 October 2026, which is not law, says a deduction method company that collected in advance for an eligible service running from 1 January 2026 to 31 December 2027 applies the reduction only to the revenue of the service from 1 January 2026 to 31 December 2026. Treat the rate on the 2027 part as Needs Input.

**Invoice timing (Decree 254 art 9).**

- Goods: at transfer of ownership or use, whether or not paid. Exports: self-determined, no later than the next working day after customs clearance (art 9.1).
- Services: at completion, whether or not paid. If money is collected before or during the service, at collection, except a deposit under the Civil Code that secures performance of a service contract (art 9.2).
- Delivery in stages: each handover (art 9.3).
- Art 9.4 and 9.5 have sector cases, including retail petrol at the end of each sale; a seller without automatic invoicing software may invoice a sale in night working hours by the next working day.

### Exempt sales

VAT Law art 5 lists 26 items of non-taxable goods and services (đối tượng không chịu thuế); arts 5.27 and 5.28 are the input rule and delegation. Art 5.27: no input credit or refund on them, unless the art 9.1 zero rate applies. Arts 5.12, 5.14, 5.17 to 5.20, 5.22 to 5.24 and 5.26 are left out here: read the Law. The other items:

- Art 5.1: unprocessed farm, forest and aquatic products of the grower or catcher, and at import. Decree 359 adds Decree 181 art 4.1b for traders: between enterprises and cooperatives, no output declaration but input stays creditable; a deduction method seller to households, individuals and others charges 5%; a direct method household, individual, enterprise, cooperative, cooperative union or other economic organisation pays 1% of revenue at the trading stage (art 4.1b(c)).
- Art 5.2 to 5.4: livestock breeds and plant propagation material; animal and aquatic feed; salt.
- Art 5.5: public-owned housing sold to its tenant. Art 5.7: land use right transfers.
- Art 5.6: irrigation, ploughing, field canal dredging and harvesting services.
- Art 5.8 and Decree 181 art 4.3a (added by Decree 144): life, health and learner insurance and other person-related insurance; livestock, crop and other farm insurance; fishing vessel insurance; reinsurance; listed oil and gas works insurance.
- Art 5.9: (a) credit services (dịch vụ cấp tín dụng) and fees in Government foreign loan agreements; (b) lending by a non-credit institution; (c) securities business; (d) capital transfers, not project or asset sales; (đ) debt sales, including payables, receivables and deposit certificates, without the earlier limit to sales between taxpayers that are not credit institutions since Decree 144; (e) foreign exchange trading; (g) derivatives; (h) sale of secured assets by the State debt company.
- Art 5.10 and 5.11: listed medical and veterinary services; funeral services.
- Art 5.13: teaching and vocational training under the education laws.
- Art 5.15: listed publications. Art 5.16: public passenger transport by bus, tram and inland waterway.
- Art 5.21: technology transfer, intellectual property transfer, and software products and services (Decree 181 art 4.13).
- Art 5.25: household and individual businesses at or under the threshold; assets sold by non-business, non-taxpayer parties; State reserve sales; fees and charges under the fees law.

Payment and bank transaction fees are not on the art 5.9 list. Treat a fee as exempt only if the invoice shows a listed service. Decree 174 Annex I lists financial transaction processing (code 6619043) under financial services, so an unlisted fee sits at 10% and not 8%.

### Input VAT

**Conditions (VAT Law art 14.2).** All of these for the purchase in question:

- (a) A VAT invoice, or the import VAT payment document, or the document for VAT paid on behalf of a foreign party (arts 4.3 and 4.4; Circular 69 art 6: a State budget payment document).
- (b) A non-cash payment document, unless a special case applies. Decree 181 art 26 sets the floor at purchases from VND 5,000,000 including VAT.
- (c) Exports also need the contract, sales invoice, non-cash payment, customs declaration, packing list, bill of lading and insurance document, if any.

Art 14.3 denies credit when a condition fails or the input comes from a prohibited act in art 13. An input that fails may go to income tax cost or asset cost, except a purchase that lacks non-cash evidence (art 14.1(e); Decree 181 art 23).

**Non-cash evidence (Decree 181 art 26).** The earlier version did not state this rule.

- Cash paid into the seller's account does not count (art 26.1).
- Accepted without a bank payment: offset under a contract with reconciliation, and third-party minutes where a third party is involved (art 26.2(a)); offset against a loan (b); third-party authorised payment in a written contract (c); shares or bonds (d); State Treasury payments (e).
- Art 26.2(đ): any balance from VND 5,000,000 after those still needs non-cash evidence.
- Deferred payment, as replaced by Decree 144 art 4 from 20 June 2026: credit is allowed until the contract due date; with no evidence at that date, reduce input in the period the payment duty arises; if evidence arrives later, claim in the period it is held (art 26.2(g)).
- No evidence needed: imports under VND 5,000,000 per time; purchases under VND 5,000,000 per invoice including VAT; gifts and samples (art 26.2(h)).
- Employee paid by non-cash means under internal rules, then reimbursed by non-cash means: accepted (art 26.2(i)).
- Several purchases on the same day from one taxpayer totalling VND 5,000,000 need non-cash evidence (art 26.3).

**Mixed use.** Input used for taxable sales is creditable in full; input for exempt sales is not. Shared input is split by separate accounts; failing that, by taxable revenue ÷ total revenue in the tax period (art 14.1(b); Decree 181 art 23.2). The earlier version said the ratio needs a full year: the text reads tax period. Total revenue includes taxable and non-taxable sales, the value added on gold, silver and gemstones where positive, and art 40.2 items (art 23.2(a), as amended by Decree 144 art 3.1); taxable revenue includes art 5.1 goods not declared (art 23.2(c)). Credit institutions, securities and insurance revenue follow their sector laws. An investment project for both taxable and non-taxable sales is the exception (art 23.2(b)): input VAT on fixed assets in the basic construction stage is credited provisionally at taxable revenue ÷ total revenue under the business plan, then adjusted to that ratio on revenue in the 3 years from the first year with revenue. If the adjustment cuts VAT already refunded, the difference is repaid, with no administrative fine on it. On hypothetical figures, VND 1,000,000,000 of input at a planned 80% gives VND 800,000,000 provisionally; a 3 year ratio of 70% takes it to VND 700,000,000. Reading the 3 years as one ratio is this guide's reading, and the period and return line for the adjustment are held.

**Timing and corrections.** Claim in the month or quarter the input arises; unused input carries to the next. An input error found before an inspection or audit decision is announced is corrected by a supplementary return to the original period if that raises tax payable or cuts a refund, paying the extra tax or refund back with late payment interest. If it lowers tax payable, or only changes the credit carried forward, declare it in the period found (art 14.1(đ)).

**Other limits.** Losses are creditable if uncompensated and proved (Decree 181 art 23.1). Gifts, promotions and advertising input is creditable (art 23.7). No credit on assets for defence, credit institutions, reinsurance, life insurance, securities, medical or training use, or aircraft and yachts not used for transport or tourism (art 23.13). Staff assets, capital contribution, authorised purchases and the car cap are in art 24.

### Invoices

**E-invoices (Decree 254).** From 1 July 2026:

- Art 6.1(a): tax-authority-coded e-invoices by default. (b) Uncoded for named sectors with qualifying systems. (c) Cash register invoices for direct-to-consumer sales. (d) A household or individual business with annual revenue over VND 1,000,000,000, or one selling an asset that must register ownership or use right, uses a coded e-invoice or a cash register e-invoice with a data link; Decree 68 sets the rest. Art 6.2: per-transaction coded invoices.
- Art 44.3: invoices printed to order by the tax office lose validity on that date. Invoices issued under the earlier decrees before that date are outside this row.
- Art 10.1 content: invoice name and symbols; number; seller's name, address and tax code; buyer's name, address and tax code, budget unit code or personal ID number; item, unit, quantity, unit price, amount before VAT, VAT rate, VAT by rate, total VAT and total payable; seller's signature (the buyer's digital signature is not needed unless agreed); date of issue; time of digital signature; the tax authority code on a coded invoice; and any fees, trade discount or promotion.
- Art 10.4: cash register invoices have a shorter list, but a deduction method economic organisation must show the price before VAT, the rate, the VAT and the total.

**VAT invoice or sales invoice.** A deduction method seller uses a VAT invoice (hóa đơn GTGT) and a direct method seller a sales invoice (hóa đơn bán hàng) (VAT Law art 16.1). If a VAT invoice omits the tax on a taxable sale, output is the payment price × rate (art 16.1(a)). Stamps, tickets and cards with a printed payment price include VAT (art 16.2).

**8% on the invoice.** The tax rate line shows '8%' and the buyer claims the VAT shown (Decree 174 art 1.3(a)). Mixed rates are listed item by item (art 1.4). An invoice at the unreduced rate is corrected under Circular 91/2026/TT-BTC art 10, then the seller and buyer adjust (art 1.5).

**Correcting an invoice (Circular 91/2026/TT-BTC art 10, from 1 July 2026 under art 25.1).** Art 10.1: (a) an error in a name, address, amount in words or other content, with no error in the tax code, invoice amount, rate, tax or goods: the seller tells the buyer, does not reissue, and notifies the tax authority on Form 04/SS-HĐĐT; (b) an error in the tax code, goods, invoice amount, rate, tax or other required content: the seller chooses an adjusting or a replacement invoice; (c) an error on a cash register e-invoice, or on an invoice for an asset that must register ownership or use, takes a replacement invoice, except in the art 10.5(c.2) case. Art 10.1(d) and the later limbs cover aviation and summary data tables. Art 10.5 sets separate handling for: (a) a change in value or quantity on payment or settlement, on a competent authority's conclusion, as art 10.5(a.1) to (a.3) list; (b) trade discounts based on quantity or sales; (c) returned or exchanged goods, insurance fee refunds and cuts, and cancelled services or property sales billed in advance, as art 10.5(c.1) to (c.4) set out; (d) refunds of payment service fees; (đ) prepaid mobile cards; (e) natural gas priced in foreign currency. Who issues differs. In (a) the seller issues a new invoice for the difference. In (b) the discount goes on the invoice for the last or next purchase, or on an adjusting invoice with a list. In (c.1) and (c.4) the seller issues an adjusting invoice, except that in (c.1) the parties may agree that the buyer issues an invoice to the seller on the return, and each then meets its tax duties as on a sale. In (c.2), where the goods are an asset that must be registered for ownership or use and the asset is already registered in the buyer's name, a buyer who uses e-invoices issues a return invoice to the seller, the return complying with the related law. In (c.3) and (e) the seller issues the adjusting invoice, in (d) the payment provider and in (đ) the telecoms enterprise. Art 10.6(d) sets the period for an adjusting invoice only: the seller declares it in the period it arises and the buyer in the period it is received. The text read gives no period or return line for a buyer-issued return invoice or an art 10.5(a) invoice: Needs Input.

### Conservative defaults

A default stands only where the law read fixes the result of the missing fact, and it names the rate only where the charge is verified. Anything else is Needs Input.

| Ambiguity | Treatment |
| --- | --- |
| Unknown rate on a sale | Needs Input. The earlier 10% default is withdrawn: an eligible supply is 8% and a seller cannot choose 10% |
| Rate on a purchase | The rate and VAT shown on the e-invoice (Decree 174 art 1.3(a)); if a supply eligible for 8% is invoiced at 10%, have the invoice corrected, then adjust input VAT (art 1.5). Art 1.5 points only to the law on invoices; taking the correction under Circular 91/2026/TT-BTC art 10.1(b) is this guide's reading |
| Unknown whether 5% applies | Needs Input. Only the art 9.2 list carries 5% |
| Unknown counterparty country | Needs Input. The earlier default of domestic Vietnam is withdrawn |
| Unknown export qualification | Needs Input. The earlier default of 10% is withdrawn: the outcome depends on which condition failed (see Cross-border points) |
| Unknown business use | Needs Input for the amount. No input credit is shown until the use is confirmed, as art 14.1 ties credit to taxable use |
| No e-invoice or tax payment document held | No input credit: art 14.2(a) requires one of them, so the law fixes this result |
| Purchase from VND 5,000,000 with no non-cash document | No input credit, unless an art 26.2 case is shown (Decree 181 art 26) |
| Unknown B2B or B2C for a cross-border sale | Needs Input. The earlier default of 10% is withdrawn |

### Red flag thresholds

Working review settings for the reviewer brief, not legal amounts.

| Threshold | Value |
| --- | --- |
| HIGH single transaction | VND 50,000,000 |
| HIGH tax delta on a single default | VND 5,000,000 |
| MEDIUM counterparty concentration | Over 40% of output or input |
| MEDIUM default count | Over 4 per period |
| LOW absolute net VAT position | VND 20,000,000 |
| Tier 2 question threshold | VND 0: no row is filtered on amount |

### Supplier discovery library

Match by case-insensitive substring on counterparty name or reference. Most specific match wins. Fall through to Transaction questions if no match. A match is a candidate, not a classification; no supplier's own status has been verified. Rates here are for supplies from 1 July 2025 to 31 December 2026. Eligibility was read from Decree 174 Annexes I and II. For a purchase, the VAT on the e-invoice governs. From 1 January 2027 no row stands at 8% without a confirmed extension: art 9.3 alone is the text read for later supplies.

**Banks: fee lines.** Credit services are exempt (art 5.9(a)). Other fees are not on that list: see Exempt sales. Use the bank's invoice. Do not treat a line as exempt because the payee is a bank.

| Pattern | Candidate | Rule and what to verify |
| --- | --- | --- |
| VIETCOMBANK, NGÂN HÀNG NGOẠI THƯƠNG, VCB | Needs Input by fee | Exempt if credit; 10% otherwise, no 8% (Annex I). Invoice governs |
| BIDV, NGÂN HÀNG ĐẦU TƯ VÀ PHÁT TRIỂN | Needs Input by fee | Same |
| VIETINBANK, NGÂN HÀNG CÔNG THƯƠNG, CTG | Needs Input by fee | Same |
| AGRIBANK, NGÂN HÀNG NÔNG NGHIỆP | Needs Input by fee | Same |
| TECHCOMBANK, TCB | Needs Input by fee | Same |
| VPBANK, NGÂN HÀNG VIỆT NAM THỊNH VƯỢNG | Needs Input by fee | Same |
| MB BANK, NGÂN HÀNG QUÂN ĐỘI | Needs Input by fee | Same |
| ACB, NGÂN HÀNG Á CHÂU | Needs Input by fee | Same |
| SACOMBANK | Needs Input by fee | Same |
| TPBANK | Needs Input by fee | Same |
| PHÍ DỊCH VỤ, FEE | Needs Input | Same |
| LÃI SUẤT, INTEREST (paid on a loan) | Exclude | Credit service, exempt under art 5.9(a); no VAT to claim. Confirm it is loan interest |
| LÃI TIỀN GỬI (deposit interest received) | Exclude | Financial receipt, outside the taxable price (Decree 181 art 14.1(b)) |

**Government and statutory.**

| Pattern | Candidate | Rule and what to verify |
| --- | --- | --- |
| TỔNG CỤC THUẾ, CỤC THUẾ, TAX AUTHORITY | Exclude | Tax payment. Older narratives may keep the earlier name |
| THUẾ GTGT, THUẾ TNDN, THUẾ TNCN | Exclude | Tax remittance. A payment of VAT on behalf of a foreign party supports input: see art 14.2(a) |
| BẢO HIỂM XÃ HỘI, BHXH, SOCIAL INSURANCE | Exclude | Social insurance |
| BẢO HIỂM Y TẾ, BHYT | Exclude | Health insurance |
| BHTN, BẢO HIỂM THẤT NGHIỆP | Exclude | Unemployment insurance |
| HẢI QUAN, CUSTOMS | Exclude the duty | Import VAT in the payment is input if the art 14.2(a) document is held. Split the line |

**Utilities.**

| Pattern | Candidate | Rule and what to verify |
| --- | --- | --- |
| EVN, TẬP ĐOÀN ĐIỆN LỰC, ĐIỆN LỰC | Input 8% | Electricity is not excluded from the reduction |
| CÔNG TY ĐIỆN LỰC (regional utilities) | Input 8% | Regional electricity distribution |
| SAWACO, HAWACO, CẤP NƯỚC (water company) | Input 5% | Clean water, art 9.2(a) |
| VIETTEL TELECOM | Input 10% | Telecoms excluded from 8% |
| VNPT, VIỄN THÔNG VIỆT NAM | Input 10% | Telecoms excluded from 8% |
| MOBIFONE | Input 10% | Telecoms excluded from 8% |
| VIETNAMOBILE | Input 10% | Telecoms excluded from 8% |
| GMOBILE | Input 10% | Telecoms excluded from 8% |

**Transport and logistics.**

| Pattern | Candidate | Rule and what to verify |
| --- | --- | --- |
| VIETNAM AIRLINES, VNA, HÀNG KHÔNG VIỆT NAM | Check route | International 0% (art 9.1(c)); domestic 8% |
| VIETJET AIR, VIETJET | Check route | Same |
| BAMBOO AIRWAYS | Check route | Same |
| VIETRAVEL AIRLINES | Check route | Same |
| ĐƯỜNG SẮT VIỆT NAM, VNR, RAILWAY | Input 8% | Rail is taxable and not in Annex I or II |
| GRAB VIETNAM | Input 8% | Ride-hailing; use the invoice, as the seller's method decides the VAT shown |
| BE (taxi app), BEE TAXI | Input 8% | Same |
| GIAO HÀNG TIẾT KIỆM, GHTK | Input 8% | Courier, not in Annex I or II |
| GIAO HÀNG NHANH, GHN | Input 8% | Same |
| VIETTEL POST | Input 8% | Same |
| VIETNAM POST, BƯU ĐIỆN (parcel) | Input 8% | Same |
| VIETNAM POST, BƯU ĐIỆN (stamps) | Input 8% | Postal services are not in the art 5 list. Stamps include VAT (VAT Law art 16.2) |
| J&T EXPRESS VIETNAM | Input 8% | Courier, not in Annex I or II |
| NINJA VAN VIETNAM | Input 8% | Same |

**Food, retail, restaurants and hotels.**

| Pattern | Candidate | Rule and what to verify |
| --- | --- | --- |
| WINMART, VINMART, WINCOMMERCE | By invoice line | Mixed basket: lines may be exempt, 5%, 8% or 10%. Check each line's stated rate against eligibility; if an eligible line shows 10%, have the invoice corrected, then adjust input VAT (Decree 174 arts 1.4 and 1.5) |
| BIG C VIỆT NAM (now GO!) | By invoice line | Same |
| AEON VIỆT NAM | By invoice line | Same |
| CO.OPMART, SAIGON CO.OP | By invoice line | Same |
| LOTTE MART VIỆT NAM | By invoice line | Same |
| BÁN LẺ (retail), NHÀ HÀNG (restaurant) | By invoice line | Alcohol and tobacco stay at 10%, as do, from 1 January 2026, soft drinks under the national standard (TCVN) with more than 5g sugar per 100ml; other soft drinks can qualify for 8% (Annex II part II item 1(k)) |
| KHÁCH SẠN, HOTEL | By invoice line | Not in Annex I or II as hotels. The Annex II service lines are dance halls, massage, karaoke, casinos and prize electronic games, betting, golf and lottery |
| PHÂN BÓN, THUỐC TRỪ SÂU (fertilisers and pesticides) | Input 5% | Art 9.2(b) |

**Fuel, office supplies, coworking and insurance.**

| Pattern | Candidate | Rule and what to verify |
| --- | --- | --- |
| XĂNG, DẦU, CÂY XĂNG | By invoice line | Petrol is carved back into the reduction (art 1.1(b)). Other fuels: confirm the Annex I code. Fuel for a car: see Transaction questions |
| VĂN PHÒNG PHẨM, OFFICE SUPPLIES | By invoice line | Books may be exempt or 5%; metal products are Annex I |
| COWORKING, VĂN PHÒNG CHIA SẺ | By invoice | Leasing from a real estate business sits at 10%; a serviced office is Needs Input |
| BẢO HIỂM (other than social insurance) | By invoice | Art 5.8 lines are exempt; others are 10%, as insurance is excluded from 8% |

**Software and cloud, local.**

| Pattern | Candidate | Rule and what to verify |
| --- | --- | --- |
| MISA, PHẦN MỀM MISA | Check invoice | Software products and services are exempt (art 5.21); no input VAT if the invoice shows none |
| FAST ACCOUNTING | Check invoice | Same |
| VIETTEL CLOUD | Needs Input | The classification is held: software is exempt (VAT Law art 5.21), telecoms is 10%, and another taxable service is 8%. Confirm the product, the invoice and Decree 181 art 4.13 |
| VNPT CLOUD | Needs Input | Same |

**Payment processors.** Fees are not on the art 5.9 list. Candidate 10%, no 8%; the invoice governs. The earlier version treated VNPAY, MOMO, ZALOPAY and PAYOO fees as exempt and VTC PAY as 10%. No text read separates them.

| Pattern | Candidate | Rule and what to verify |
| --- | --- | --- |
| VNPAY (phí giao dịch) | Input 10% | Decree 174 Annex I code 6619043. Invoice governs |
| MOMO (phí) | Input 10% | Same |
| ZALOPAY (phí) | Input 10% | Same |
| PAYOO (phí) | Input 10% | Same |
| VTC PAY | Input 10% | Same |

**International suppliers.** The rules are under Cross-border points. All rows are Needs Input until the document is held: no input credit without an invoice or a tax payment document.

| Pattern | Candidate | Rule and what to verify |
| --- | --- | --- |
| GOOGLE (Workspace, Ads, Cloud) | Needs Input | Does it charge Vietnamese VAT under its own registration, or must the buyer withhold? |
| MICROSOFT (365, Azure) | Needs Input | Check if a Vietnam entity invoices |
| META, FACEBOOK ADS | Needs Input | Same question as Google |
| ZOOM, SLACK, NOTION, OPENAI | Needs Input | Same question |
| AWS | Needs Input | Same question |
| ADOBE, APPLE, DROPBOX, LINKEDIN, ATLASSIAN, ANTHROPIC | Needs Input | Same question |

**Internal transfers and exclusions.**

| Pattern | Candidate | Rule and what to verify |
| --- | --- | --- |
| CHUYỂN KHOẢN NỘI BỘ, INTERNAL | Exclude | Internal movement |
| VAY VỐN, TRẢ NỢ, LOAN | Exclude | Loan principal |
| LƯƠNG, TIỀN LƯƠNG, SALARY | Exclude | Wages carry no VAT invoice and are no sale of the business |
| CỔ TỨC, DIVIDEND | Exclude | Financial receipt |
| ĐẶT CỌC, DEPOSIT | Needs Input | A Civil Code deposit securing a service contract is outside the invoice timing rule (Decree 254 art 9.2). An advance for a service is invoiced at collection. The label does not decide it |
| RÚT TIỀN, ATM | Needs Input | Ask what the cash paid for. If it paid a purchase from VND 5,000,000, input credit fails |

### Bank exports and language cues

Column layouts are working notes from the earlier version, not checked against any bank. Test them against the export held.

| Bank | Key columns | Date format | Amount |
| --- | --- | --- | --- |
| Vietcombank VCB | Ngày GD, Nội dung, Phát sinh nợ (debit), Phát sinh có (credit), Số dư | DD/MM/YYYY | VND, no decimals typically |
| BIDV | Ngày, Mô tả, Số tiền ghi nợ, Số tiền ghi có, Số dư | DD/MM/YYYY | VND |
| Vietinbank | Ngày giao dịch, Nội dung, Số tiền, Số dư | DD/MM/YYYY | VND |
| Techcombank | Thời gian, Mô tả giao dịch, Số tiền ghi nợ, Số tiền ghi có, Số dư | DD/MM/YYYY | VND |
| MB Bank | Ngày, Nội dung giao dịch, Phát sinh, Số dư | DD/MM/YYYY | VND |

| Vietnamese | Meaning | Hint |
| --- | --- | --- |
| Nhận chuyển khoản | Incoming wire transfer | Potential revenue |
| Thanh toán / Chuyển khoản | Outgoing payment | Potential expense |
| Nhận ngoại tệ | Foreign currency receipt | Potential export |
| Lãi tiền gửi | Deposit interest | Financial receipt, excluded |
| Phí dịch vụ | Service fee | Needs Input by fee |
| Số dư | Balance | Running balance, ignore |
| Nội dung | Transaction description or narrative | Key classification field |
| Thuế GTGT | VAT | Tax payment, exclude |
| Rút tiền ATM | ATM withdrawal | Needs Input |
| Thanh toán tự động | Auto-payment | Subscription or utility |

### Transaction questions

Each item is Needs Input until answered. The question goes on the base's form at Step 6.5.

| Item | What is missing | Treatment | Question |
| --- | --- | --- | --- |
| Foreign contractor tax on an international service | Whether the foreign supplier registered in Vietnam directly, or the buyer must withhold | No input credit until status and document are confirmed | 'Has this foreign supplier registered for VAT in Vietnam? Does it issue Vietnamese electronic invoices? If not, has VAT been withheld and paid on its behalf?' |
| Export qualification for services | Foreign buyer, consumption abroad, contract, non-cash payment | Needs Input. See Cross-border points for each failure | 'Was this service entirely consumed outside Vietnam? Is the client a foreign entity? Is there a contract and a non-cash payment record?' |
| Reduced rate confirmation | The specific product | Needs Input on a sale. The invoice governs on a purchase | 'What exactly was purchased? Is it on the 5% list (clean water, fertiliser, medical equipment, books and so on)? If not, does the e-invoice show 8% or 10%?' |
| Partial exemption | Revenue by class for the tax period | Needs Input. No credit is shown on shared cost until the ratio is known. R-VN-3 applies if it stays unknown | 'What proportion of your sales are taxable and exempt in this tax period? Provide the revenue breakdown.' |
| Vehicle expenses | Taxable business use, seat count and price | Needs Input. No credit is shown until confirmed; the car cap applies | 'Is this vehicle registered in the company's name and used only for business? How many seats does it have, and what did it cost before VAT?' |

### Excel working paper

Working paper only. Layout for Sheet 'Box Summary' under `vat-workflow-base`, kept for use once the Operational hold lifts. The return form governs each return. Column H of Sheet 'Transactions' takes one code per row (base Check 5). For a deduction method filer the codes are the Form 01/GTGT value lines: [23] for a domestic purchase, [23a] for imported goods, then [26], [29], [30], [32], [32a], [32b] and [34a]. On the form [23a] is part of [23], so an import is coded [23a] alone. Sheet 'Box Summary' computes line [23] as SUMIFS on code [23] plus SUMIFS on code [23a], and line [23a] as SUMIFS on code [23a]. Lines [24] and [24a] do the same on column F, and [31] and [33] take column F for codes [30] and [32]. [32b] is entered as a positive amount and the form subtracts it: [27] = [29] + [30] + [32] + [32a] − [32b]. Form note 3 says what [32b] holds but not whether that value also sits in a rate line, so a [32b] row is Needs Input. Lines [27], [28], [34] and [35] are formulas and [25] is working paper line B8; none is a code. For a direct method filer the codes are the Form 04/GTGT lines [21a], [21b], [22], [24], [26] and [28]. A sale at 8% has no valid code until the hold in '8% on the return' is settled: Needs Input.

Test on hypothetical figures. An import of VND 100,000,000 with VAT of 10,000,000, code [23a], and a domestic purchase of VND 50,000,000 with VAT of 4,000,000, code [23], give [23] 150,000,000, [23a] 100,000,000, [24] 14,000,000 and [24a] 10,000,000, with the import in one row only. A sale of VND 200,000,000 with VAT of 20,000,000, code [32], and a VND 5,000,000 row, code [32b], give [32] 200,000,000, [32b] 5,000,000, [27] 195,000,000 and [28] 20,000,000.

```
VIETNAM VAT WORKING PAPER: BẢNG TÍNH THUẾ GTGT
Kỳ khai thuế (Period): ____________  MST: ____________

A. THUẾ ĐẦU RA (OUTPUT VAT)
  A1. Doanh thu chịu thuế 10% (net)           ___________
  A2. Thuế đầu ra 10% (A1 × 10%)              ___________
  A2a. Doanh thu chịu thuế 8% (net)           ___________
  A2b. Thuế đầu ra 8% (A2a × 8%)              ___________
  A3. Doanh thu chịu thuế 5% (net)            ___________
  A4. Thuế đầu ra 5% (A3 × 5%)                ___________
  A5. Xuất khẩu 0% (net)                      ___________
  A6. Doanh thu không chịu thuế (net)         ___________
  A7. Tổng thuế đầu ra (A2 + A2b + A4)        ___________

B. THUẾ ĐẦU VÀO (INPUT VAT)
  B1. Mua hàng chịu thuế 10% (net)            ___________
  B2. Thuế đầu vào 10% (B1 × 10%)             ___________
  B2a. Mua hàng chịu thuế 8% (net)            ___________
  B2b. Thuế đầu vào 8% (B2a × 8%)             ___________
  B3. Mua hàng chịu thuế 5% (net)             ___________
  B4. Thuế đầu vào 5% (B3 × 5%)               ___________
  B5. Thuế nhập khẩu đã nộp                   ___________
  B6. Tổng thuế đầu vào (B2+B2b+B4+B5)        ___________
  B7. Thuế đầu vào không được khấu trừ        ___________
  B8. Thuế đầu vào được khấu trừ (B6−B7)      ___________

C. THUẾ PHẢI NỘP
  C1. Chênh lệch thuế (A7 − B8, may be negative)       ___________
  C2. Thuế còn được khấu trừ kỳ trước                  ___________
  C3. Thuế GTGT phải nộp: max(C1 − C2, 0)              ___________
  C4. Thuế còn được khấu trừ chuyển kỳ sau:
      max(C2 − C1, 0)                                  ___________

REVIEWER FLAGS:
  [ ] Hóa đơn điện tử confirmed for all input credits?
  [ ] Non-cash evidence held for every purchase from VND 5,000,000?
  [ ] Export evidence available for zero-rated sales?
  [ ] Foreign contractor status confirmed for all international service payments?
  [ ] 5% rate items correctly identified?
  [ ] 8% applied only to eligible supplies dated to 31 December 2026, and Annex III form prepared?
  [ ] Mixed-use ratio calculated for any exempt supplies?
```

### Known gaps and checks before filing

Topics the earlier version sent to a specialist stay there: foreign contractor computation (R-VN-5); real estate and construction (R-VN-4); non-commercial import VAT and agricultural cooperative special rules, which this draft does not state beyond art 5.1 and Decree 181 art 4.1b. Mixed use now has its rule in Input VAT; R-VN-3 covers the case with no ratio.

Before filing, once the Operational hold lifts:

- All hóa đơn điện tử (e-invoices) for sales issued and sent as Decree 254 requires.
- All input credits supported by compliant electronic invoices or tax payment documents, with non-cash evidence.
- Export zero-rating supported by contracts and payment evidence, and customs papers for goods.
- Foreign contractor position flagged for all international service payments.
- 5%, 8% and 10% rates correctly applied by supply and date.
- Form 01 of Annex III of Decree 174 filed for 8% supplies and reductions.
- Prior period excess credit correctly carried forward.

## Deadlines and filing

Filing rests on Law 108/2025/QH15, Decree 252/2026/ND-CP and Circular 89/2026/TT-BTC for filings from 1 July 2026; earlier filings rested on texts not read. Circular 89 commenced on 1 July 2026 (art 99.1) and repealed Circular 80/2021/TT-BTC (art 99.3(h)). It lists the electronic systems for tax transactions as the Cổng Dịch vụ công quốc gia (National Public Service Portal), the Hệ thống thông tin quản lý thuế (tax management information system) and connected T-VAN providers (art 8.2). For electronic tax payment it adds the online public service systems of other competent agencies and the electronic payment services of payment service providers, payment intermediaries and other service organisations connected to the tax management information system (art 8.2(d)).

**Tax period.** VAT is declared monthly unless a quarterly or per transaction case below applies (Circular 89 art 19.1(a)). Quarterly is an election: a taxpayer at or under VND 50,000,000,000 does not move to it automatically. The articles read state no transition for a taxpayer already filing quarterly on 1 July 2026, so confirm the period on its record.

- **Quarterly election.** A taxpayer with sales revenue for the previous year of VND 50,000,000,000 or less may choose quarterly filing. Revenue is the total on the VAT returns for the calendar year and, where filing is centralised at head office, includes dependent units and business locations (art 19.1(b.1.1)).
- **New business.** It may choose quarterly. If first year revenue is VND 50,000,000,000 or less, then after 12 full months of operation, from the calendar year after the year the 12 months are complete, revenue of the previous full calendar year decides the period. If revenue of the first calendar year is over that amount, even for a year under 12 months, it files monthly from the next calendar year (art 19.1(b.1.2)).
- **Who decides.** The taxpayer works out which period applies (art 19.1(b.1.3)), and the choice holds for the whole calendar year (art 19.1(b.2.1)).
- **Moving from monthly to quarterly.** Send Form 01/ĐK-TĐKTT of Annex I to the managing tax authority by 31 January of the first quarterly year. Quarterly filing starts once the authority issues its notice of acceptance (art 19.1(b.2.2)).
- **Not eligible for quarterly.** Whether the taxpayer or the tax authority finds this, the taxpayer moves to monthly from the first month of the next quarter, refiles monthly returns for the earlier quarters, and works out and pays late payment interest. The refiling and interest do not apply to a quarterly return on which the authority has issued a refund decision, or to a case the authority found by inspection at the taxpayer's premises. No late filing penalty applies to returns refiled for this reason, and they replace the quarterly returns (art 19.1(b.2.3)).
- **Per transaction** (art 19.1(c)), each limb:
  - c.1: a taxpayer that need not file under Decree 252 art 11, or a direct method taxpayer, with VAT on a real estate transfer.
  - c.2: irregular VAT of a direct method taxpayer.
  - c.3: a taxpayer asking the tax authority to issue an e-invoice per transaction.
  - c.4: a deduction method taxpayer with construction of a work valued at VND 1,000,000,000 or more including VAT, other than construction in a non-tariff zone, consulting, survey, design, accounting and insurance, or with a real estate transfer in a province other than that of its head office. Art 100.2 applies this limb until 31 December 2026 only.
  - c.5: a withholding organisation or an organisation filing on another's behalf under Decree 252 arts 22.1(c) and 22.2(c.1), (d) and (k).
  - Under c.2, c.4 and c.5, several transactions in a month may be declared monthly.

| Filing | Due | Source |
| --- | --- | --- |
| Monthly return, the default | 20th of the month after the month the tax arises | Decree 252 art 10.2; Circular 89 art 19.1(a) |
| Quarterly return, by election | Last day of the first month of the next quarter: 30 April, 31 July, 31 October, 31 January | Decree 252 art 10.3; Circular 89 art 19.1(b) |
| Per transaction return | 10th day after the day the tax arises, except that a household or individual business not required to use e-invoices, and an enterprise, economic organisation or other organisation that wants one, declare and pay before the tax authority issues a coded e-invoice for that transaction | Decree 252 art 10.1; Law 108 art 26.3(b); Circular 89 art 19.1(c) |
| Household or individual business | As above by period, except that monthly returns for January to March 2026 fell due by 20 April 2026; revenue notice by 31 January of the next year | Decree 68 arts 8.1(a), 8.3 and 18.1; Decree 252 art 10.9 |
| Foreign supplier registered directly | Monthly if regular; per transaction if irregular | Decree 252 art 40.2(a) |
| Payment | Last day of the filing period for the return | Law 108 art 14.1(a); Decree 68 art 8.3(e) for households |

The earlier version gave the quarterly date as the 30th, which is wrong for 3 quarters of 4. It also listed an annual settlement on 31 March. Circular 89 art 19 sets monthly, quarterly and per transaction periods and provides no VAT settlement, whilst art 21 provides one for corporate income tax. Decree 252 art 10.5 sets a due date for taxes declared by settlement without naming VAT. No text read provides a VAT settlement, so that row is withdrawn; this is an absence in the texts read, not proof.

A due date falling on a ngày nghỉ (non-working day) under the rules moves to the next working day (Decree 252 art 3.7). The text read does not define the term, so where the date falls on a Saturday file by the previous working day.

**Extensions and corrections.** Force majeure can extend filing by up to 30 days, or 60 days for a settlement (Law 108 art 12.4). A supplementary return may be filed within 5 years from the filing deadline of the period in error, in these cases: (a) before a tax authority or other competent body announces an inspection or audit decision; (b) for a return outside the scope or period of that decision; (c) where an investigating body has not asked that the return stay unamended (art 12.5(a) to (c)). If an error found within an inspected scope or period raises tax or cuts relief, a refund, credit or overpayment, the taxpayer may add an explanation file for the tax authority to review (art 12.5(d)). Payment extensions are in art 14.7 and Decree 252 art 25.

**No return due.** Decree 252 art 11 lists cases, including a taxpayer with only activity outside tax, other than a household or individual business under Decree 141 (item 1), export processing enterprises with only that activity (item 3) and suspension (item 4). Check the item before relying on it.

**8% supplies.** File Form 01 of Annex III of Decree 174 with the VAT return (art 1.6). It lists 8% purchases in [05] and [06], reduced sales in [07] and [08], and the difference [09] = [08] − [06]. Sales column (5) is column (4) × 80% and column (6) is (3) × [(4) − (5)].

### Return form

Forms are in Annex I of Circular 89. A return for a tax period before 1 July 2026 uses the form in force before that date (art 100.1), which was not read, so the lines below serve periods from 1 July 2026. Captions come from the page images of the signed scan.

| Form | Use |
| --- | --- |
| 01/GTGT | Deduction method, business activity, with its allocation annexes where they apply |
| 02/GTGT | Deduction method, investment project eligible for refund |
| 03/GTGT | Direct method on value added: gold, silver and gemstones |
| 04/GTGT | Direct method on revenue; also withholding organisations and organisations filing on another's behalf |
| 05/GTGT | Construction and out of province real estate transfers |
| 01/ĐK-TĐKTT | Request to change the tax period from monthly to quarterly |

Annex I also carries Form 01/TKN-CNKD for household and individual businesses (art 99.5 as corrected by Decision 2551/QD-BTC). That form, Form 02/GTGT and Form 05/GTGT were not read line by line.

**Form 01/GTGT lines.**

| Line | Meaning |
| --- | --- |
| [21] | No purchases or sales in the period (mark X) |
| [22] | VAT credit brought forward from the previous period |
| [23], [24] | Purchases in the period: value, VAT |
| [23a], [24a] | Of which imported goods: value, VAT |
| [25] | Input VAT deductible this period |
| [26] | Sales not subject to VAT |
| [27], [28] | Sales subject to VAT: [27] = [29] + [30] + [32] + [32a] − [32b]; [28] = [31] + [33] |
| [29] | Sales at 0% |
| [30], [31] | Sales at 5%: value, VAT |
| [32], [33] | Sales at 10%: value, VAT |
| [32a] | Sales not declared for tax (không kê khai tính nộp thuế) |
| [32b] | Sales not counted in the taxable price |
| [34a] | Sales outside the VAT law. The form note points to Decree 181 art 40.2, which leaves the detail to the Ministry of Finance. Circular 69 arts 1 to 10 do not define the line, so its scope is held |
| [34], [35] | Total sales and VAT: [34] = [26] + [27] + [34a]; [35] = [28] |
| [36] | VAT arising in the period: [35] − [25] |
| [37] | Downward adjustment of credit from earlier periods. A buyer receiving an adjusting or replacement invoice in a Circular 91/2026/TT-BTC art 10.5 case enters it in [37] or [38] for the period of receipt, with no supplementary return (form note 5) |
| [38] | Upward adjustment of credit from earlier periods, and art 10.5 invoices as at [37] |
| [39a] | Transferred VAT deductible in the period |
| [40a] | VAT payable on business activity: [36] − [22] + [37] − [38] − [39a], where that is 0 or more |
| [40b] | Investment project input VAT offset against [40a], not over [40a] |
| [40] | VAT still payable: [40a] − [40b] |
| [41] | VAT not yet credited: the same sum as [40a], where that is 0 or less |
| [42] | Refund claimed, not over [41] |
| [43] | Credit carried forward: [41] − [42] |

The form states [41] as a sum of 0 or less. Read it as the size of that amount: this is an inference from [42] ≤ [41] and [43] = [41] − [42].

The earlier version's line table does not match this form. On the form, 10% sales and VAT are [32] and [33], not [26] and [27]; 5% are [30] and [31], not [28] and [29]; zero-rated sales are [29], not [30]; sales not subject to VAT are [26], not [31]; total output VAT is [28] and [35], not [32]; deductible input VAT is [25], not [33] or [35]. No line carries non-deductible input VAT. [42] is the refund claimed, not net payable after credit, and [43], not [41], is the amount carried forward. Rows A1 to C4 of the Excel working paper are working rows, not form lines.

**8% on the return: held.** Form 01/GTGT has rows for 0%, 5% and 10% and none for 8%. Neither the form, its notes nor Form 01 of Annex III of Decree 174 says which row carries 8% sales. The 8% entry may sit on a page of Circular 89 that was not searched. Treat the entry as Needs Input and confirm it on the form in the Hệ thống thông tin quản lý thuế or with the tax office. Do not place 8% sales on a line by assumption. Form 04/GTGT likewise shows only 1%, 5%, 3% and 2%, and the text read does not say how it shows the 20% cut, so that entry is held too.

**Form 04/GTGT lines.** Revenue and VAT by group: [22], [23] at 1%; [24], [25] at 5%; [26], [27] at 3%; [28], [29] at 2%; totals [30], [31]. Below them: revenue not subject to VAT [21a]; revenue at 0% [21b]; taxable revenue [30a] = [21b] + [30]; total revenue [32] = [21a] + [30a]. Part B, lines [33] to [37], covers amounts collected for the State, withholding organisations and organisations filing on another's behalf.

### Refunds

R-VN-7 applies to any claim. Conditions, for orientation only. Art 15.9 opens with a business establishment (cơ sở kinh doanh) in a refund case under the article. The cases in arts 15.1 to 15.4 need the deduction method, books and a bank account under the tax code (VAT Law art 15.9(a)). On this guide's reading, a business establishment in any art 15 case needs input meeting art 14.2 and not within art 14.3 (art 15.9(b)). Arts 15.5, 15.6 and 15.7 and the treaty limb of art 15.8 name claimants in other terms. Whether art 15.9(b) binds a claimant that is not a business establishment is held: Needs Input.

| Case | Rule | Source |
| --- | --- | --- |
| Exports | Unclaimed input from VND 300,000,000 in the month or quarter, except goods imported then exported to another country. With domestic sales: split by accounts or ratio, offset against domestic payable first, remainder from VND 300,000,000, capped at 10% of export revenue in the refund period, excess carried forward | Art 15.1; Decree 181 art 29; Circular 69 art 7 and Annex II |
| Investment projects | From VND 300,000,000 after offset; up to 1 year after completion; exclusions in art 15.2 | Art 15.2 |
| 5% goods and services | Only 5% output: from VND 300,000,000 after 12 consecutive months or 4 consecutive quarters. Several rates: input for the 5% output is taken from separate accounts; shared input that cannot be separated goes by 5% production revenue ÷ total taxable revenue of the refund period; the amount left after offset against VAT payable is refundable from VND 300,000,000 | Art 15.3; Decree 181 art 31, from 1 July 2025 (art 39.2); Circular 69 art 8 and Annex II |
| Dissolution or bankruptcy | Per art 15.4 | Art 15.4 |
| Foreign travellers, ODA and aid, diplomats, competent decisions and treaties | Per arts 15.5 to 15.8 | Arts 15.5 to 15.8 |

**Refund file for periods from 1 July 2026.** Exports and the 5% case: Form 01/GTGT with the refund claimed in [42], and Annex 01-8/GTGT (Circular 89 art 46.1(a) and (c)). Investment projects: Form 02/GTGT with the refund claim, Annex 01-8/GTGT and the project papers in art 46.1(b.3) to (b.7), which are needed only for a first claim or on a change (art 46.1(b.8)).

Art 15.9(c), which required that the seller had declared and paid, was repealed by Law 149/2025/QH15 from 1 January 2026. Decree 181 art 37.3 was repealed in step by Decree 359 art 1.2, which saves files received before 1 January 2026 (art 2.2).

The process runs under Law 108 art 18. The tax office answers within 3 working days of receipt (Decree 252 art 31.1), decides in 6 working days of its notice for a refund paid first (art 31.2(a)), or 10 working days of its inspection conclusion or penalty decision for an inspected case (art 31.2(b)). Inspection comes first for: a first refund per project or case; a claim within 2 years of an evasion penalty; a high risk claim; and dissolution or bankruptcy (art 30.1).

## Penalties and interest

**Which Act reaches which duty.** The VAT Law has no penalty article. It prohibits acts in art 13 and denies credit or refund under art 14.3, which are VAT consequences, not fines. Fines reach VAT filing, payment, declarations and invoices through the tax administration Act: Law 108 arts 44 and 45 for tax administration breaches, including tax procedures, invoices and e-documents (art 45.1), with amounts in Decree 125/2020/ND-CP as amended. A filing or act before 1 July 2026 fell under Law 38/2019/QH14, not read, and the Decree 125 amounts were set under it. Late payment interest is not a fine. Criminal liability rests on the Criminal Code, not read (Law 108 art 44.6).

Amounts in Decree 125 arts 13 and 24 are for organisations (art 7.4(a)). A household or individual pays half (Law 108 art 44.4), except that wrong declaration and evasion have no such split. The fine for a procedure or invoice breach, or an art 19 act, is the midpoint of the band. One mitigating factor takes off 10% of the midpoint and one aggravating factor adds 10% of it. 2 or more mitigating factors give the band minimum, and 2 or more aggravating factors the band maximum (art 7.4(d), as replaced by Decree 310 art 1.5(c)). One mitigating factor cancels one aggravating factor (art 7.4(b)), and a factor already used to set the band is not counted again (art 7.4(c)). An act that ended before 16 January 2026 follows the text in force when it was done; an act still running at that date and found after it follows Decree 310; a complaint over a fine imposed before that date follows the text in force at the act (Decree 310 arts 3.1 to 3.3 and 4.1).

| Breach | Consequence | Source |
| --- | --- | --- |
| Late return, 1 to 5 days, with a mitigating factor | Warning | Decree 125 art 13.1 |
| Late return, 1 to 30 days, otherwise | VND 2,000,000 to 5,000,000 | Art 13.2 |
| Late return, 31 to 60 days | VND 5,000,000 to 8,000,000 | Art 13.3 |
| Late return, 61 to 90 days; or 91 days or more with no tax payable; or no return with no tax payable | VND 8,000,000 to 15,000,000 | Art 13.4(a) to (c) |
| Late return over 90 days with tax payable, tax and interest paid before an inspection announcement or the violation record | VND 15,000,000 to 25,000,000, capped at the tax on the return, or the total tax on the returns within art 5.3(b), but not below the art 13.4 midpoint, VND 11,500,000 | Art 13.5, as replaced by Decree 310 art 1.10 |
| No return, or return over 90 days late, causing tax short, outside the art 45.4(l) carve-out | Evasion, below | Law 108 art 45.4(a) and (l) |
| Late payment | 0.03% a day on the late tax (tiền chậm nộp). The Government may adjust it | Law 108 arts 16.2(a) and 16.6 |
| Wrong declaration, booked in full | 20% of the tax short or excess refund | Law 108 arts 44.3(b) and 45.2; Decree 125 art 16.1 |
| Same, corrected and paid before an inspection announcement or detection | No fine; late payment interest still runs | Law 108 arts 44.2(a) and 16.1(e) |
| Tax evasion | 1 to 3 times the tax evaded: 1× with one or more mitigating factors, 1.5× with no mitigating or aggravating factor, 2×, 2.5× and 3× with 1, 2 and 3 or more aggravating factors | Law 108 arts 44.3(c) and 45.4; Decree 125 art 17 |
| Invoice issued at the wrong time, on a sale | 1 invoice VND 500,000 to 1,500,000; 2 to under 10, 2,000,000 to 5,000,000; 10 to under 20, 5,000,000 to 15,000,000; 20 to under 50, 15,000,000 to 30,000,000; 50 to under 100, 30,000,000 to 50,000,000; 100 or more, 50,000,000 to 70,000,000 | Decree 125 art 24.2, as replaced by Decree 310 art 1.14 |
| No invoice on a sale | 1 invoice VND 1,000,000 to 2,000,000; 2 to under 10, 2,000,000 to 10,000,000; 10 to under 20, 10,000,000 to 30,000,000; 20 to under 50, 30,000,000 to 50,000,000; 50 or more, 60,000,000 to 80,000,000. Forced issue of the invoice | Decree 125 art 24.3 and 24.6, as replaced by Decree 310 art 1.14 |
| No invoice and no declaration, or invoice value below the price paid | Evasion | Law 108 art 45.4(c) |
| False or illegal invoices used to cut tax or raise credit or refund | Evasion, plus VAT Law art 14.3 denial; criminal law may apply | Law 108 art 45.4(d); VAT Law art 13 |
| Giving or selling invoices | VND 20,000,000 to 50,000,000 | Decree 125 art 22.2, as replaced by Decree 310 art 1.13 |

Bands in Decree 310 for promotional and gift invoices differ: read art 1.14 if they apply. Decree 125 art 7.1(b), as replaced by Decree 310 art 1.5(a), states no amount for the maximum fine on one tax procedure or invoice breach: it sends that maximum to the law on administrative violations, which was not read.

**One fine for several acts (Decree 125 art 5.3, as amended by Decree 310 art 1.3).** Each act is fined apart, except: (a) wrong entries on tax returns on one day, in the procedure class: one breach, at the highest band. (b) several late returns of the same tax on one day: one breach, at the highest band, with any return amounting to evasion fined apart. (c) several late invoice notices or reports of one kind on one day: one breach, at the highest band. (d) illegal invoice use fined under art 16 or 17 is not fined again under art 28. (đ) several invoices issued at the wrong time, and (e) several failures to issue, still within the time limit and fined in one case: one breach, at the art 24 band for the number of invoices. (g) several wrong entries on one return: one breach at the highest band, or one breach under art 16 or 17 where the entries also fall there.

**Time limits.** Procedure breaches: 2 years. Evasion below the criminal level and wrong declaration: 5 years (Law 108 art 44.7). After that, no fine, but tax and interest stay due for 10 years back from discovery, and for all periods if the taxpayer never registered (art 44.8). Invoice breaches: held. Decree 125 art 8.1(a) says 1 year; Law 108 art 44.7 says 2 years for 'vi phạm thủ tục thuế', and art 45.1, which reads 'vi phạm thủ tục thuế, hóa đơn, chứng từ điện tử', does not settle whether that reaches invoices.

## Cross-border points

**Zero rate, goods (art 9.1(a)).** Goods sold to a foreign party and consumed abroad; sold to an organisation in a non-tariff zone, consumed there and serving export production directly; sold in the isolation area to individuals who have completed exit formalities; sold in a duty free shop; on-the-spot export (xuất khẩu tại chỗ).

**Zero rate, services (art 9.1(b)).** A service supplied directly to a foreign party and consumed outside Vietnam, or to an organisation in a non-tariff zone, consumed there and serving export production directly. For a foreign individual, the person must be outside Vietnam during the service (Decree 181 art 17.2(a)).

**Other zero rate items (art 9.1(c)).** International transport; hire of transport used outside Vietnam; aviation and maritime services for international transport; construction abroad or in a non-tariff zone; digital content for a foreign party with evidence of use abroad; spare parts for a foreign party used abroad; onward processing for export; and non-taxable goods and services when exported, except art 9.1(d). Decree 181 art 17.3 defines these terms.

**Never zero (art 9.1(d); Decree 181 art 17.4).** Technology transfer and intellectual property transfer abroad; reinsurance abroad; credit services; capital transfer; derivatives; postal and telecoms services; art 5.23 raw resource exports; tobacco, alcohol and beer imported then exported; domestic petrol and oil sold to businesses in a non-tariff zone; and cars sold to a party in a non-tariff zone.

Decree 181 art 17.4 adds 2 more limbs:

- (k) Services supplied in Vietnam to foreign parties: sports competition, performing arts, culture, entertainment, conferences, hotels, training, advertising and tour services; services tied to selling, distributing or consuming goods in Vietnam; and non-cash payment services.
- (l) Services to parties in a non-tariff zone: renting homes, halls, offices, hotels and warehouses; transport of workers; and food and drink, except industrial catering and food and drink within the zone.

**Conditions (Decree 181 art 18).**

- Goods: contract, non-cash payment and customs declaration.
- Services: contract and non-cash payment.
- International transport: contract and non-cash payment; for passengers a ticket, with direct payment by individuals accepted.
- Aviation and maritime services have their own limbs. Arts 27 and 28 give the detail, including export entrustment, sales through foreign e-commerce sites, bonded warehouses, trade fairs and digital content, and art 27 has carve-outs from the payment rule.
- Circular 69 art 4.2: produce the file when an authority asks.

**When a condition fails (Decree 181 art 28.9).**

| Failure | Input | Output |
| --- | --- | --- |
| Goods with customs confirmation, other papers missing | No credit | No output VAT |
| Onward processing with papers missing | As domestic | Tax as domestic sale |
| Export service failing the non-cash condition | No credit | No output VAT |

So a failed export is not automatically 10%. A service that fails a different limb, such as consumption in Vietnam, is simply not within art 9.1 and is taxed under art 9.3, at 8% if eligible. No text read deals with goods that lack customs confirmation altogether, so that case is Needs Input.

**Foreign suppliers (purchases).**

- Art 4.3: a business in Vietnam buying services from a foreign party without a permanent establishment is the taxpayer, unless art 4.4 or 4.5 applies. The price and rate rules are in Decree 181 art 13 and Circular 69 art 9, and R-VN-5 applies to the computation. Art 9.2 lists exclusions, for example services carried out and consumed abroad.
- Art 4.4: a foreign supplier selling through e-commerce or digital platforms registers and files itself through the tax system (Decree 252 art 40), or a platform operator withholds. A Vietnamese organisation on the deduction method buying from it withholds and pays at the time of payment (arts 43.3 and 44.1(a)). If the item cannot be identified, withholding uses the highest rate (art 44.2(b)). If all its Vietnam revenue is withheld, the supplier need not register (art 40.1(a)). These details took effect from 1 July 2026.
- Input credit then rests on the tax payment document (art 14.2(a); art 11.1(c); Circular 69 art 6). Whether 8% applies to a foreign supplier's service was not stated in the text read: Needs Input.

**Imports.** Import VAT is collected at Customs, and its tax point is the import duty tax point (Decree 181 art 15.2). The payment document supports input (art 14.2(a)).

## Two worked examples that recompute

All names and bank lines are hypothetical. Dates are in 2026, after 1 July, so Decrees 252 and 254 apply.

### Example 1: a deduction month, with an overseas fee tested 4 ways

An IT consultant company in Ho Chi Minh City, on the deduction method and a monthly period, has these July 2026 items, with VND 3,000,000 of credit brought forward:

| Item | Gross VND | Treatment | Output or input VND |
| --- | --- | --- | --- |
| Domestic IT consulting received, VAT invoice | 108,000,000 | 8%, not software, not in Annex I or II | 8,000,000 output |
| Clean water, e-invoice | 2,100,000 | 5% | 100,000 input |
| Courier, e-invoice | 10,800,000 | 8% | 800,000 input |
| Telecoms, e-invoice | 2,200,000 | 10%, excluded from 8% | 200,000 input |
| Subcontractor on the overseas job, e-invoice, paid by transfer | 54,000,000 | 8% | 4,000,000 input |
| Printer, e-invoice, paid in cash | 6,480,000 | 8%, but from VND 5,000,000 with no non-cash document | 480,000 not creditable |
| Consulting fee from a US company, for work completed and invoiced in July 2026 | 125,000,000 | Depends on the facts | See cases |

The printer's VND 480,000 also cannot go to income tax cost (art 14.1(e)). The fee's tax point is July, as the service was completed and invoiced then, whenever the money arrives (VAT Law art 8.1(b)).

| Case | Facts | VAT for the month, VND | Paid after credit, VND | Credit carried on, VND |
| --- | --- | --- | --- | --- |
| A, zero rate | Foreign buyer, consumed abroad, contract, bank payment | 2,900,000 | 0 | 100,000 |
| B, domestic, fee excludes VAT | Consumed in Vietnam, so 8% on VND 125,000,000 is VND 10,000,000 | 12,900,000 | 9,900,000 | 0 |
| C, domestic, fee includes VAT | Same, but 125,000,000 ÷ 1.08 × 8% is VND 9,259,259 | 12,159,259 | 9,159,259 | 0 |
| D, cash payment | Export service fails the non-cash condition: no output, and the VND 4,000,000 subcontractor input tied to it is lost (Decree 181 art 28.9) | 6,900,000 | 3,900,000 | 0 |

The same fee moves the month's payment from nil to VND 9,900,000. The earlier version's 10% default would have given VND 12,500,000 of output tax on the fee, which matches no case. The July return is due on 20 August 2026 (Decree 252 art 10.2). VAT is rounded to the dong here for the example; no rounding rule was read.

```oa-check
name: VN deduction month with an overseas fee tested four ways
inputs:
  domestic_gross: 108000000
  fee: 125000000
  water_gross: 2100000
  courier_gross: 10800000
  telecom_gross: 2200000
  subcontract_gross: 54000000
  printer_gross: 6480000
  credit_brought: 3000000
steps:
  - domestic_net: round(domestic_gross / 1.08, 0)
  - output_domestic: domestic_gross - domestic_net
  - water_input: water_gross - round(water_gross / 1.05, 0)
  - courier_input: courier_gross - round(courier_gross / 1.08, 0)
  - telecom_input: telecom_gross - round(telecom_gross / 1.10, 0)
  - subcontract_input: subcontract_gross - round(subcontract_gross / 1.08, 0)
  - printer_barred: printer_gross - round(printer_gross / 1.08, 0)
  - general_input: water_input + courier_input + telecom_input
  - input_total: general_input + subcontract_input
  - case_a: output_domestic - input_total
  - case_b: output_domestic + round(fee * 8 / 100, 0) - input_total
  - case_c: output_domestic + round(fee / 1.08 * 8 / 100, 0) - input_total
  - case_d: output_domestic - general_input
  - paid_a: max(case_a - credit_brought, 0)
  - carried_a: max(credit_brought - case_a, 0)
  - paid_b: max(case_b - credit_brought, 0)
  - paid_c: max(case_c - credit_brought, 0)
  - paid_d: max(case_d - credit_brought, 0)
expected:
  domestic_net: 100000000
  output_domestic: 8000000
  water_input: 100000
  courier_input: 800000
  telecom_input: 200000
  subcontract_input: 4000000
  printer_barred: 480000
  general_input: 1100000
  input_total: 5100000
  case_a: 2900000
  case_b: 12900000
  case_c: 12159259
  case_d: 6900000
  paid_a: 0
  carried_a: 100000
  paid_b: 9900000
  paid_c: 9159259
  paid_d: 3900000
```

### Example 2: the household threshold, quarter by quarter

A household business supplying services without materials, eligible for the reduction, has 2026 revenue of VND 300,000,000 in the first quarter and VND 350,000,000 in the second. R-VN-2 stops the workflow while it stays at or under the threshold and R-VN-1 stops it once it is over, so this example is for the reviewer.

| Case | Third quarter revenue, VND | Cumulative, VND | Result |
| --- | --- | --- | --- |
| A | 340,000,000 | 990,000,000 | Not over VND 1,000,000,000. No VAT so far. Notify actual revenue by 31 January 2027, a Sunday, if the year ends at or under the threshold |
| B | 400,000,000 | 1,050,000,000 | Over the threshold in the third quarter. Declare and pay from that quarter, and move to coded e-invoices within 30 days from the end of the quarter |

In case B, the percentage is 5%, cut by 20% to 4% on invoices noting the reduction. Tax on third quarter revenue is VND 16,000,000. Without the reduction noted, the same revenue gives VND 20,000,000 until the invoices are corrected under Decree 174 art 1.5.

Decree 68 art 8.1(a) says to declare 'from the quarter' revenue passes the threshold, and art 3.2 taxes a business with annual revenue over the threshold. It does not say whether earlier quarters' revenue comes in. On the whole year, with the 20% cut, itself unproven on those quarters, tax would be VND 42,000,000. That is a difference of VND 26,000,000 on a single reading: Needs Input, for a reviewer.

The third quarter return would be due on 31 October 2026, a Saturday. File by Friday 30 October unless the reviewer confirms the Decree 252 art 3.7 move to Monday 2 November.

```oa-check
name: VN household threshold by quarter with reduced percentage
inputs:
  q1: 300000000
  q2: 350000000
  q3_low: 340000000
  q3_high: 400000000
  threshold: 1000000000
  percentage: 5
  cut_percent: 20
steps:
  - total_low: q1 + q2 + q3_low
  - total_high: q1 + q2 + q3_high
  - over_low: min(floor(total_low / (threshold + 1)), 1)
  - over_high: min(floor(total_high / (threshold + 1)), 1)
  - reduced_percentage: percentage * (100 - cut_percent) / 100
  - tax_low: round(over_low * q3_low * reduced_percentage / 100, 0)
  - tax_quarter: round(over_high * q3_high * reduced_percentage / 100, 0)
  - tax_quarter_no_cut: round(over_high * q3_high * percentage / 100, 0)
  - tax_whole_year: round(over_high * total_high * reduced_percentage / 100, 0)
  - reading_gap: tax_whole_year - tax_quarter
expected:
  total_low: 990000000
  total_high: 1050000000
  over_low: 0
  over_high: 1
  reduced_percentage: 4
  tax_low: 0
  tax_quarter: 16000000
  tax_quarter_no_cut: 20000000
  tax_whole_year: 42000000
  reading_gap: 26000000
```

### Bank line classifications

Six classifications from a hypothetical bank statement of the Example 1 company, in the Vietcombank (VCB) transaction history format. All are dated July 2026, inside the 8% period, and each stays Tier 2 until its document is checked.

**1. Domestic B2B revenue.** `15/07/2026  Nhận chuyển khoản  CÔNG TY TNHH ABC TECHNOLOGY  ND: HD GTGT SO 001/2026  +108,000,000  VND`. IT consulting is not in Annex I or II of Decree 174, so 8% applies; confirm it is not a software service, which is exempt (art 5.21). Gross VND 108,000,000 includes VAT: net VND 100,000,000 (doanh thu chịu thuế) plus VND 8,000,000 output GTGT. An electronic VAT invoice showing 8% must be issued. Report on the return and on Form 01 of Annex III.

**2. Export service.** `22/07/2026  Nhận ngoại tệ  ACME CORPORATION USA  Technical consulting 07/2026  +USD 5,000 (VND 125,000,000)`. Needs Input: see Example 1. The fee is in July because the work was completed and invoiced in July, and the receipt date does not move it. With both dates in an earlier period, the fee belongs to that period. If the 2 dates fall in different periods, art 8.1(b) names both without ranking them: Needs Input (VAT Law art 8.1(b)). Zero-rated only if supplied directly to a foreign entity and consumed outside Vietnam, with a contract and a non-cash payment document (Decree 181 art 18.2). Output VAT is then nil. The bank credit shows a transfer, not the rest.

**3. Water utility.** `30/07/2026  Thanh toán tự động  SAWACO - CẤP NƯỚC SAIGON  Tiền nước tháng 7/2026  -2,100,000  VND`. Clean water at 5%. Net VND 2,000,000 plus VND 100,000 input VAT, claimable on the e-invoice.

**4. Domestic courier.** `31/07/2026  Thanh toán  GIAO HÀNG NHANH GHN  Phí vận chuyển tháng 7/2026  -10,800,000  VND`. Not in Annex I or II, so 8%. Net VND 10,000,000 plus VND 800,000 input VAT, pending invoice verification. The bank transfer is the non-cash evidence.

**5. Deposit interest.** `31/07/2026  Lãi tiền gửi  Vietcombank  Lãi tháng 7/2026  +250,000  VND`. A financial receipt, outside the taxable price (Decree 181 art 14.1(b)). Exclude from the GTGT return. The text does not class it as a sale of the business, so it is not put in the art 23.2 ratio; if the business has significant financial receipts, ask the reviewer.

**6. International software.** `05/07/2026  Thanh toán quốc tế  GOOGLE IRELAND LIMITED  Google Workspace July 2026  -3,300,000  VND`. Needs Input. A deduction method buyer on an e-commerce or digital platform purchase withholds at payment unless the supplier has already dealt with the tax (see Cross-border points). The tax payment document then supports input VAT, if art 14 is met. Do not claim input credit until registration status and that document are confirmed. Whether 8% applies is not settled by the text read.

## Ask the client first

1. Business type, VAT method and tax period: enterprise, cooperative, household or individual; deduction or direct; monthly or quarterly; prior year revenue; the MST.
2. What was sold: goods or services by name, any exempt or 5% lines, and how each sale was invoiced.
3. Where the buyer and use are: any foreign buyer or supplier, who consumed the service, and the contract, payment and customs papers held.
4. Which invoice or tax payment document is held for each purchase, how it was paid, and what it was used for.
5. Any credit brought forward, revenue by class for shared costs, and any refund, real estate, construction or foreign contractor position.

Ask these under `vat-workflow-base` Step 6.5, before any output. What stays unanswered is Needs Input.

## Sources

Read on means the date read for this conversion. All texts are official and in Vietnamese; English terms are working translations. Scanned texts were read by OCR, which drops some diacritics; numerals and structure read well, except that OCR dropped a zero from 2 Decree 310 amounts. Those amounts, and the wording of Decree 125 arts 5.3, 7, 8.1 and 13.5 as amended, were checked by eye on page images of Decree 310 pages 3, 4, 7, 9 and 10 and Decree 125 pages 6 and 8. Also checked by eye: Circular 91 pages 17, 18, 19 (lower half), 20, 21 and 22 (upper half) for art 10; Decree 181 page 27 (lower half) and page 28 (upper half) for art 23.2; Decree 174 page 2 (lower half) for art 1.5; the consolidated VAT Law pages 6, 9 and 18 for arts 5.21, 8 and 15.9; and Circular 89 pages 241 and 242 for Form 01/GTGT. Limits follow each source.

| Source | URL | Read on |
| --- | --- | --- |
| Law 48/2024/QH15 consolidated by 12/VBHN-VPQH of 6 February 2026, arts 1 to 18, with Resolution 204/2025/QH15 in its notes, read in full | https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/02/12-vbhn-vpqh.pdf | 2026-11-05 |
| Law 48/2024/QH15 as passed, arts 17 and 18 read for commencement | https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/01/luat48.pdf | 2026-11-05 |
| Law 09/2026/QH16, arts 1 to 5 read | https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/5/09-qh.signed.pdf | 2026-11-05 |
| Decree 174/2025/ND-CP, arts 1 and 2, Annex II parts I and II and the Annex III form read; Annex I searched by sector | https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/7/174nd.signed.pdf | 2026-11-05 |
| Decree 181/2025/ND-CP, arts 4 to 6, 12 to 19, 21 to 31 and 37 to 40 read | https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/7/181nd.signed.pdf | 2026-11-05 |
| Decree 359/2025/ND-CP, arts 1 and 2 read | https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/01/359-nd.signed.pdf | 2026-11-05 |
| Decree 144/2026/ND-CP, arts 1 to 6 read | https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/4/144-ndcp.signed.pdf | 2026-11-05 |
| Decree 68/2026/ND-CP, arts 3, 4, 8 to 13 and 17 to 19 read | https://xdcs.cdnchinhphu.vn/446259493575335936/2026/3/6/68-2026-nd-cp-05032026-signed-17727673940151875228819.pdf | 2026-11-05 |
| Decree 141/2026/ND-CP, arts 1 to 4 read | https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/4/141-ndcp.signed.pdf | 2026-11-05 |
| Circular 69/2025/TT-BTC, arts 1 to 10 read; annexes not read closely | https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/7/69-btc.signed.pdf | 2026-11-05 |
| Law 108/2025/QH15, arts 4, 12 to 16, 18, 26, 44, 45 and 52 read | https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/01/108-qh15.signed.pdf | 2026-11-05 |
| Decree 252/2026/ND-CP, arts 3, 9 to 11, 25, 29 to 31, 40 to 46 and 74 read | https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/7/252-ndcp.signed.pdf | 2026-11-05 |
| Circular 89/2026/TT-BTC, arts 8, 17 to 19, 46.1(a) to (c), 99 and 100, the Annex I list of VAT forms, and Forms 01/GTGT, 01-8/GTGT, 03/GTGT and 04/GTGT with notes read; art 18 and the opening of art 21 read for filing limits; OCR extracted pages 1 to 50, 100 to 122, 181 to 209 and 241 to 266 only, and the other pages of 839 were never searched | https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/7/89-btc.signed.pdf | 2026-11-05 |
| Decision 2551/QD-BTC correcting Circular 89 art 99.5, read in full; no VAT content | https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/9/dinh-chinh-tt-89-2026-btc.signed.pdf | 2026-11-05 |
| Decree 254/2026/ND-CP, arts 6 to 11, 41, 43 and 44 read | https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/7/254-ndcp.signed.pdf | 2026-11-05 |
| Circular 91/2026/TT-BTC, arts 1, 10, 24 and 25 read; searched for 8%; the other articles and the annexes not read | https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/7/91-btc.signed.pdf | 2026-11-05 |
| Decree 125/2020/ND-CP, arts 5, 7, 8.1, 13, 16, 17, 22 and 24 read | https://datafiles.chinhphu.vn/cpp/files/vbpq/2020/10/125.signed.pdf | 2026-11-05 |
| Decree 102/2021/ND-CP, searched for changes to arts 13, 16, 17 and 24; none to those amounts found | https://datafiles.chinhphu.vn/cpp/files/vbpq/2021/11/102.signed.pdf | 2026-11-05 |
| Decree 310/2025/ND-CP, art 1 items 1 to 14 and arts 2 to 4 read | https://datafiles.chinhphu.vn/cpp/files/vbpq/2025/12/310-cp.signed.pdf | 2026-11-05 |
| Decree 291/2026/ND-CP, art 19a addition read; not used here | https://datafiles.chinhphu.vn/cpp/files/vbpq/2026/7/291_2026_nd-cp_21072026-signed.signed.pdf | 2026-11-05 |
| Báo Chính phủ question and answer of 28 October 2026 on prepaid services, read in full; Government news, not law | https://baochinhphu.vn/thu-truoc-tien-dich-vu-den-het-2027-tinh-giam-thue-gtgt-the-nao-102261028112800628.htm | 2026-11-05 |
| Resolution 43/2026/QH16 full text, read for any VAT change; income tax only | https://xaydungchinhsach.chinhphu.vn/toan-van-nghi-quyet-so-43-2026-qh16-ve-giam-thue-thu-nhap-ca-nhan-thue-thu-nhap-doanh-nghiep-119260830184758301.htm | 2026-11-05 |
| phapluat.gov.vn national legal portal, tried for Resolution 43/2026/QH16 | https://phapluat.gov.vn/legal-documents/187347 | 2026-11-05: not read, 403 to a plain request, not retried |

Not yet confirmed: a regional layer or approved non-EU exception for `vat-workflow-base`; the Form 01/GTGT row that carries 8% sales and how Form 04/GTGT shows the 20% cut; the return forms and period rules for tax periods before 1 July 2026; any extension of the 8% rate past 31 December 2026, where no text was found at 5 November 2026 and that absence is not proof, so a later supply rests on art 9.3 alone on the text read; whether 8% applies to a service bought from a foreign supplier under VAT Law art 4.3 or 4.4, and the VAT and corporate income tax components of that charge, noting that Circular 89 art 99.3(b) repealed Circular 103/2014/TT-BTC from 1 July 2026 and Circular 69 art 10 had already repealed its arts 6, 9, 12 and 15; Circular 103/2014/TT-BTC itself for periods before 1 July 2026; Law 13/2008/QH12 for supplies before 1 July 2025; the household revenue level for 1 July to 31 December 2025, as VAT Law art 18.2 starts the art 5.25 level on 1 January 2026; Law 38/2019/QH14, Decrees 126/2020/ND-CP, 123/2020/ND-CP and 70/2025/ND-CP and Circular 78/2021/TT-BTC for filings, invoices and acts before 1 July 2026, including the earlier version's 1 July 2022 e-invoice date; the Criminal Code; whether a Saturday is a ngày nghỉ under Decree 252 art 3.7; whether a household crossing the threshold pays on earlier quarters' revenue; the treatment of exported goods with no customs confirmation; Circular 91/2026/TT-BTC beyond arts 1, 10, 24 and 25; the maximum fine under the law on administrative violations, to which Decree 125 art 7.1(b) now points; whether 1 year or 2 years limits an invoice breach; the scope of Form 01/GTGT line [34a]; whether a value in line [32b] also sits in a rate line; the period and return line for a Decree 181 art 23.2(b) adjustment; the period and return line for a buyer-issued return invoice or a Circular 91 art 10.5(a) invoice; whether VAT Law art 15.9(b) binds a refund claimant that is not a business establishment; the address of the filing portal; the length of the MST; the scope of Decree 181 art 4.13 by product and whether a cloud service is telecoms; the scope of 'financial receipts' in Decree 181 art 14.1(b); and the date the Tổng cục Thuế became the Cục Thuế.

### Version history

| Version | Date | Change |
| --- | --- | --- |
| 2.1 | 2026-11-05 | Converted to the upstream template with coverage from 1 July 2025. Corrected the filing period, quarterly due date, annual settlement, tax authority, return lines, bank and payment fee treatment, mixed-use ratio, deposit interest, and penalty and e-invoice citations against primary text. Added the non-cash rule, refund and export failure rules, foreign supplier rules from Decree 252, and household rules from Decrees 68 and 141. Replaced conservative defaults with Needs Input, made refusals full stops, added R-VN-6 to R-VN-8 and added an Operational hold. |
| 2.0 | 31 October 2026 | Legacy: added the temporary 8% rate; rebased on VAT Law 48/2024/QH15 and its decrees; moved the examples to April 2026. |
| 2.0 | April 2026 | Legacy: full v2.0 rewrite with pattern library, worked examples and foreign contractor note. |
| 1.0 | 2024 | Legacy: initial release. |

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes. All outputs must be reviewed by a qualified professional before filing.
