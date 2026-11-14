---
name: ak-sales-tax
description: "Use this skill whenever asked about Alaska sales and use tax for 2026. Alaska has no statewide sales tax, but boroughs and cities levy their own, and the Alaska Remote Seller Sales Tax Commission (ARSSTC) collects for its member communities from remote sellers and marketplace facilitators. Covers the 100,000 dollar statewide economic nexus test, destination sourcing, local rates and caps from the ARSSTC rate sheet, monthly filing, penalties and physical-presence sellers who file with the municipality. Trigger on phrases like \"Alaska sales tax\", \"AK sales tax\", \"Alaska local sales tax\", \"ARSSTC\", \"Alaska Remote Seller Sales Tax Commission\", \"Alaska economic nexus\", \"Juneau sales tax\", \"Kenai Peninsula Borough sales tax\", \"do I charge sales tax in Alaska\". ALWAYS load us-sales-tax first."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/ak-sales-tax"
  jurisdiction: "US-AK"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# Alaska sales and use tax (local only), 2026

> **Built from the law. Not yet approved.** Written by Claude. Not reviewed by an accountant. Local Alaska sales tax rules are set by each borough and city and change often. All outputs must be reviewed by a qualified professional before filing.

**Answer first.** The State of Alaska levies no sales tax. Boroughs and cities may levy their own sales and use tax after a public vote, and a borough tax and a city tax inside it add together. A seller with no physical presence in an Alaska member community collects through one place, the Alaska Remote Seller Sales Tax Commission (ARSSTC), once its statewide gross sales into Alaska reach USD 100,000 in the current or previous calendar year. A seller with a physical presence registers and files directly with that municipality.

| Field | Value | Source |
| --- | --- | --- |
| State sales tax | None | [DCRA, Sales Tax](https://www.commerce.alaska.gov/web/dcra/localgovernmentresourcedesk/taxationassessment/salestax.aspx) |
| Local sales tax | Boroughs and cities, by ordinance approved by voters | [DCRA, Sales Tax](https://www.commerce.alaska.gov/web/dcra/localgovernmentresourcedesk/taxationassessment/salestax.aspx) |
| Remote-seller administrator | ARSSTC, filing portal arsstc.munirevs.com | [ARSSTC, Business sellers](https://arsstc.org/business-sellers/) |
| Rules for remote sales | ARSSTC Remote Seller Sales Tax Code (Uniform Code), amended July 2024 | [Uniform Code](https://arsstc.org/wp-content/uploads/2024/09/Uniform-Code_2024-revisions_final_070824.pdf) |
| Current rate sheet | ARSSTC rate sheet as of 11/1/2026 (rates, seasonal rates, caps, alcohol and bed taxes) | [Rate sheet 11/1/2026](https://arsstc.org/wp-content/uploads/2026/11/ARSSTC-Sales-Tax-Rate-Sheet-11-1-26.xlsx) |

## Scope

Sales and use tax on sales delivered into Alaska in 2026: whether a seller must collect, where to register, how to source and rate a sale, local caps, filing, payment and penalties. It covers remote sellers and marketplace facilitators under the ARSSTC Uniform Code, and points physical-presence sellers to the municipality's own code.

Out of scope, with the skill or source that handles it:

- The general US sales tax method (nexus after Wayfair, marketplace rules in other states, exemption certificate practice): `us-sales-tax`.
- Alaska has no individual income tax (DOR: "The State of Alaska currently does not have an individual income tax"). Federal income tax, including on the Permanent Fund Dividend, belongs to the federal skills. Alaska corporate income tax: `ak-corporate-tax`. Alaska payroll and unemployment insurance: `ak-payroll`.
- Each non-member municipality's own code (rate, base, exemptions, return form and due dates). This skill names the facts to get; it does not hold those codes.
- Local bed (transient lodging), alcohol, tobacco, fuel and other excise taxes, beyond flagging the ones on the ARSSTC rate sheet.

## Ask the client first

1. **Physical presence.** Does the seller have an office, warehouse, storefront, inventory, service or sales agent, independent sales consultants, or equipment or property rented out in any Alaska community? If yes, which communities?
2. **Gross sales into Alaska** for 2025 and for 2026 to date, split into own sales (website, phone, wholesale) and sales through each marketplace. Include exempt sales and sales to exempt buyers.
3. **Delivery addresses.** Where goods are delivered (street address, post office box, carrier pickup) and, for electronic services, the billing address.
4. **What is sold.** Goods, services, digital or electronic services, alcohol, lodging, vehicles, jewelry, groceries; and the selling price of single items and services (caps depend on it).
5. **Marketplace.** Does a registered marketplace facilitator collect for these sales? Is the seller itself a marketplace (and if so, is it a delivery network, lodging or travel marketplace)?
6. **Buyers.** Resale or exempt buyers, and whether the seller holds their exemption certificates.

## The method, step by step

### Rates, bands and thresholds

| Item and condition | 2026 figure | Official source |
| --- | --- | --- |
| State sales tax rate | None. "At present, the State of Alaska does not levy a sales tax" | [DCRA, Sales Tax](https://www.commerce.alaska.gov/web/dcra/localgovernmentresourcedesk/taxationassessment/salestax.aspx) |
| Remote-seller economic nexus | Statewide gross sales delivered into Alaska, including the seller's marketplace facilitator's sales, of USD 100,000 or more in the current or previous calendar year (Uniform Code section 040(A)(1)) | [Uniform Code](https://arsstc.org/wp-content/uploads/2024/09/Uniform-Code_2024-revisions_final_070824.pdf) |
| 200-transaction test | Repealed effective January 1, 2025; the dollar test is the only test | [ARSSTC, Repeal of Transaction Thresholds](https://arsstc.org/wp-content/uploads/2024/09/Threshold-Change-for-Sellers.pdf) |
| Registration deadline | Within 30 calendar days of meeting the threshold (section 090(C)) | [Uniform Code](https://arsstc.org/wp-content/uploads/2024/09/Uniform-Code_2024-revisions_final_070824.pdf) |
| Member combined rates, general sales tax | 0% to 7.85% on the 11/1/2026 sheet; most members 2% to 7%; highest is Homer City 4.85% plus Kenai Peninsula Borough 3% | [Rate sheet 11/1/2026](https://arsstc.org/wp-content/uploads/2026/11/ARSSTC-Sales-Tax-Rate-Sheet-11-1-26.xlsx) |
| City and Borough of Juneau | 5% | [Rate sheet 11/1/2026](https://arsstc.org/wp-content/uploads/2026/11/ARSSTC-Sales-Tax-Rate-Sheet-11-1-26.xlsx) |
| Juneau cap on a single item or single service | Sales on or after October 1, 2026: tax only the first USD 50,000 (maximum tax USD 2,500), CBJ 69.05.040(21) and (22) as amended by Serial No. 2026-22, eff. 10-1-2026. Rate sheets for January to September 2026: first USD 15,000 (maximum USD 750). Jewelry is not capped. No cap on a whole transaction | [Rate sheet 11/1/2026](https://arsstc.org/wp-content/uploads/2026/11/ARSSTC-Sales-Tax-Rate-Sheet-11-1-26.xlsx); [CBJ 69.05.040](https://library.municode.com/ak/juneau/codes/code_of_ordinances?nodeId=COLABOJUALVOII_TIT69RETA_CH69.05UNSATA_69.05.040EX); [Rate sheet 9/1/2026](https://arsstc.org/wp-content/uploads/2026/08/ARSSTC-Sales-Tax-Rate-Sheet-9-1-26.xlsx) |
| Juneau motor vehicle | Selling price USD 50,000 or less: tax only the first USD 15,000. Over USD 50,000: tax only the first USD 50,000 (CBJ 69.05.040(21)(c)) | [CBJ 69.05.040](https://library.municode.com/ak/juneau/codes/code_of_ordinances?nodeId=COLABOJUALVOII_TIT69RETA_CH69.05UNSATA_69.05.040EX) |
| Kenai Peninsula Borough | 3% borough rate; cities add: Homer 4.85% (total 7.85%), Kenai 3% (6%), Seldovia 2% (5%), Seward 4% (7%), Soldotna 3% (6%) | [Rate sheet 11/1/2026](https://arsstc.org/wp-content/uploads/2026/11/ARSSTC-Sales-Tax-Rate-Sheet-11-1-26.xlsx) |
| Kenai Peninsula Borough cap | Tax only the first USD 500 of a single item, transaction or service (maximum borough tax USD 15; Kenai City combined maximum USD 30; Homer combined maximum USD 39.25) | [Rate sheet 11/1/2026, Tax Caps tab](https://arsstc.org/wp-content/uploads/2026/11/ARSSTC-Sales-Tax-Rate-Sheet-11-1-26.xlsx) |
| Seasonal rates (summer / winter) | Sitka 6% Apr to Sep, 5% Oct to Mar; Haines Townsite 7% / 4.5%; Haines Rural 5% / 3%; Skagway 5% / 3%; Ketchikan City 5.5% / 3% (plus borough 2.5%); Craig 7% / 6%; Seldovia City 6.5% / 2%; Excursion Inlet 4.5% / 2.5%; Pelican 6% May to Sep, 4% Oct to Apr; Chignik 2% May to Oct, 0% Nov to Apr | [Rate sheet 11/1/2026](https://arsstc.org/wp-content/uploads/2026/11/ARSSTC-Sales-Tax-Rate-Sheet-11-1-26.xlsx) |
| Seasonal grocery rates | Kenai Peninsula Borough 3% and Homer 4.85% on groceries, June to August only | [Rate sheet 11/1/2026](https://arsstc.org/wp-content/uploads/2026/11/ARSSTC-Sales-Tax-Rate-Sheet-11-1-26.xlsx) |
| Bed taxes collected with sales tax by marketplaces | Juneau 9% bed tax plus 5% sales tax (14%), Tenakee Springs 6% plus 2% (8%), Cordova 13% special lodging rate | [Rate sheet 11/1/2026, Marketplaces tab](https://arsstc.org/wp-content/uploads/2026/11/ARSSTC-Sales-Tax-Rate-Sheet-11-1-26.xlsx) |
| Reduced filing frequency | May be approved for sellers with less than USD 100,000 taxable sales or 12 transactions a year statewide | [ARSSTC, Business sellers](https://arsstc.org/business-sellers/) |
| Late filing fee | USD 25 per month or fraction, to a maximum of USD 100 (section 180(A)) | [Uniform Code](https://arsstc.org/wp-content/uploads/2024/09/Uniform-Code_2024-revisions_final_070824.pdf) |
| Late payment penalty | 5% of delinquent tax per month or fraction, to a maximum of 20%; the penalty bears no interest (section 180(C)) | [Uniform Code](https://arsstc.org/wp-content/uploads/2024/09/Uniform-Code_2024-revisions_final_070824.pdf) |
| Interest | 15% a year on delinquent tax until paid (section 180(B)) | [Uniform Code](https://arsstc.org/wp-content/uploads/2024/09/Uniform-Code_2024-revisions_final_070824.pdf) |
| False or concealed information | USD 500 penalty | [ARSSTC, FAQs for sellers](https://arsstc.org/faqs-for-sellers/) |
| Credit card payments | 3% processing fee | [ARSSTC, FAQs for sellers](https://arsstc.org/faqs-for-sellers/) |

There is no single Alaska rate. Never compute tax with a rate or cap not read from the ARSSTC rate sheet in force for the month of sale, or from the municipality's own code.

1. **Is there physical presence?** Physical presence comes from an office, warehouse, storefront, inventory, a service or sales agent, contracted independent sales consultants, or rental of equipment or property in a community. A seller with physical presence registers with that municipality and reports its local sales there (Uniform Code section 050(A)). Physical-presence sales are left out of the ARSSTC threshold count and are never remitted through ARSSTC.
2. **Measure the threshold.**
   - Out-of-state seller with no Alaska presence: count ALL sales delivered into Alaska, including marketplace sales, whatever the destination community and whether or not the sale or buyer is taxable.
   - Alaska-based seller: count only remote sales sent outside its home community or communities, including marketplace sales.
   - Marketplace facilitator: count all sales into Alaska from all sellers on the platform.
   - The test is statewide, not per community, and is met if either the current or the previous calendar year reaches USD 100,000.
3. **Decide who collects.** A marketplace facilitator is treated as the remote seller for sales it facilitates and collects on them (section 050(E)). A seller that sells only through registered marketplaces does not need to register and files the Marketplace Seller Affidavit (from the ARSSTC administrator). A seller that sells both on marketplaces and on its own site counts both for the threshold and collects on its own non-marketplace sales.
4. **Register** on the ARSSTC portal (arsstc.munirevs.com) within 30 calendar days of meeting the threshold, and turn on collection for deliveries into member communities. A seller that cannot start at once must agree a start date with ARSSTC.
5. **Source each sale to the point of delivery.** Goods are taxed where delivered: delivery to a post office box in a taxing community is taxed there; goods shipped by private carrier to a residence outside the taxing community are not taxed by it. Electronic services are treated as delivered to the billing address. See ARSSTC Code Interpretation 2020-05.
6. **Rate the sale.** Use the borough rate plus the city rate for the delivery address, the seasonal rate for the month, and any alcohol or bed tax that applies. A community that joins ARSSTC starts collection on the first day of the month after 30 days from adoption; there is no retroactive collection.
7. **Apply caps and exemptions** from the rate sheet's Tax Caps tab and the member's code. Exemptions are construed narrowly (section 010(C)). Accept exemption only on a certificate the buyer gives, and keep one for every exempt sale.
8. **File and pay** each period on the ARSSTC upload template (see Filing and payment).

## Boundary and exception table

| Facts | Decision |
| --- | --- |
| Remote seller under USD 100,000 into Alaska in both 2025 and 2026 to date | No ARSSTC registration required; recheck monthly in 2026 |
| Remote seller reached USD 100,000 in 2025 | Collect for all of 2026 (previous-year test), registration within 30 days of meeting the threshold |
| Seller registered before 2025 only because of the old 200-transaction test, with no more than USD 100,000 into Alaska in 2024 | May close the ARSSTC account with the Account Closure Form, or stay registered; must keep collecting until the closure is processed |
| Sells only through a registered marketplace | Marketplace collects; seller files the Marketplace Seller Affidavit instead of registering |
| Delivery network, transient lodging or travel marketplace | Excluded from ARSSTC collection (section 040(C)); reports to the member community under its code (section 050(F)) |
| Physical presence in a community, remote sales delivered to another member community | Local sales to the municipality, remote sales to ARSSTC (section 050(B)) |
| Physical presence, remote sale delivered into the same community | Report to that municipality, not ARSSTC (section 050(C)) |
| Delivery to a community that levies no general sales tax or is not an ARSSTC member | No ARSSTC tax; a non-member community's own code may still apply to a seller present there |
| Municipality of Anchorage | Listed on the cap tab with no general rate; the rate sheet shows no Anchorage general sales tax |
| City and Borough of Juneau, single item over the cap | Tax the first USD 50,000 for sales from October 1, 2026; first USD 15,000 for January to September 2026; jewelry is taxed in full |
| Kenai Peninsula Borough community, item over USD 500 | Borough and city tax apply only to the first USD 500 |
| Groceries delivered in the Kenai Peninsula Borough or Homer | Taxed at the seasonal grocery rate June to August only |
| Seasonal-rate community | Use the summer or winter rate for the month of sale, not the annual rate |
| Remote seller buying for resale with no physical presence in a member community | Use the ARSSTC Remote Reseller Certificate of Exemption; it expires at the end of the calendar year (section 190(B)) |
| No sales in the period | File a zero return anyway (section 100(E)) |
| Return filed but tax not paid in full | Treated as no return filed (section 180(E)) |
| Seller sells or transfers the business | Final return within 30 days of the transfer; notice to ARSSTC at least 10 business days before completion |
| Buyer brings goods bought elsewhere into a taxing municipality | Use tax may apply at the same rate as the sales tax, levied on the buyer only, with credit for sales tax paid elsewhere (DCRA, AS 29.45.650(b)) |

### Red flags

| Pattern | Why it matters |
| --- | --- |
| "Alaska has no sales tax" said to a remote seller over the threshold | Local tax applies through ARSSTC once USD 100,000 is reached |
| Using a single statewide Alaska rate | There is none; rates are per community and per season |
| Applying the 200-transaction test to 2025 or 2026 | Repealed from January 1, 2025 |
| Counting only taxable sales toward the threshold | The test is gross sales, including exempt sales and marketplace sales |
| Using last year's cap for Juneau | Juneau raised its single item and service cap to USD 50,000 from October 1, 2026 |
| Uploading an old filing template | The portal accepts only the current template; download it fresh for each filing |

### Defaults to verify against the member's code

| Pattern | Typical treatment | Notes |
| --- | --- | --- |
| General tangible goods | Taxable at the local rate | Only where a local tax exists |
| Grocery or unprepared food | Often exempt | Kenai Peninsula Borough and Homer tax it June to August |
| Professional and other services | Often taxable | Several Alaska municipalities tax services; check caps on a single service |
| SaaS and digital goods | Check locally | Electronic services sourced to the billing address |
| Resale | Exempt with a certificate | Remote Reseller Certificate for remote sellers |
| Sales above a price cap | Partly exempt | Many members cap the taxable amount per item, transaction or service; see the Tax Caps tab |

## Worked cases

Rates and caps below are from the ARSSTC rate sheets named and CBJ 69.05.040. Sellers are invented.

**Case 1 (decision): must the seller register with ARSSTC?** Seller A, an Oregon online retailer with no Alaska presence, had 2025 sales into Alaska of USD 64,000 on its own site and USD 41,000 through a marketplace. Seller B had USD 58,000 and USD 39,000. Both counts include marketplace sales. Seller A totals USD 105,000, which meets the USD 100,000 test, so it must register within 30 days and collect on its own-site sales for 2026 (the marketplace keeps collecting on its sales). Seller B totals USD 97,000, so it need not register on the 2025 figures, but must recheck its 2026 running total each month.

```oa-check
name: AK ARSSTC 100,000 statewide threshold, two sellers
inputs:
  threshold: 100000
  a_direct: 64000
  a_marketplace: 41000
  b_direct: 58000
  b_marketplace: 39000
steps:
  - a_total: a_direct + a_marketplace
  - a_over: max(a_total - threshold, 0)
  - a_must_register: min(floor(a_total / threshold), 1)
  - b_total: b_direct + b_marketplace
  - b_over: max(b_total - threshold, 0)
  - b_must_register: min(floor(b_total / threshold), 1)
expected:
  a_total: 105000
  a_over: 5000
  a_must_register: 1
  b_total: 97000
  b_over: 0
  b_must_register: 0
```

**Case 2: Juneau single item before and after the October 2026 cap change.** A registered remote seller ships a USD 20,000 boat engine (not jewelry, not a vehicle) to a buyer in the City and Borough of Juneau at 5%. Sold in March 2026, the cap on the rate sheet was USD 15,000, so tax is 5% of 15,000 = USD 750. Sold in November 2026, the cap is USD 50,000, so the whole USD 20,000 is taxed: USD 1,000.

```oa-check
name: AK Juneau 5% with the single-item cap, March vs November 2026
inputs:
  price: 20000
  cap_march: 15000
  cap_november: 50000
steps:
  - taxable_march: min(price, cap_march)
  - tax_march: pct(taxable_march, 5)
  - taxable_november: min(price, cap_november)
  - tax_november: pct(taxable_november, 5)
expected:
  taxable_march: 15000
  tax_march: 750.00
  taxable_november: 20000
  tax_november: 1000.00
```

**Case 3: Kenai City plus Kenai Peninsula Borough, USD 500 cap.** A USD 800 single item shipped to the City of Kenai. The borough (3%) and Kenai City (3%) each tax only the first USD 500. Tax = 15 + 15 = USD 30, the combined maximum on the cap tab.

```oa-check
name: AK Kenai City plus Kenai Peninsula Borough, 500 cap
inputs:
  price: 800
  cap: 500
steps:
  - taxable: min(price, cap)
  - borough_tax: pct(taxable, 3)
  - city_tax: pct(taxable, 3)
  - total_tax: borough_tax + city_tax
expected:
  borough_tax: 15.00
  city_tax: 15.00
  total_tax: 30.00
```

**Case 4: late return.** A monthly filer's March 2026 return shows USD 2,000 of tax, due April 30, 2026. It is filed and paid on June 15, 2026: one full month and part of a second, so two months late. Late filing fee 2 x USD 25 = USD 50. Penalty 2 x 5% = 10% of USD 2,000 = USD 200. Interest at 15% a year on the USD 2,000 is added by the portal and is not worked here.

```oa-check
name: AK ARSSTC late filing fee and penalty, two months late
inputs:
  tax: 2000
  months_late: 2
steps:
  - filing_fee: min(25 * months_late, 100)
  - penalty_rate: min(5 * months_late, 20)
  - penalty: pct(tax, penalty_rate)
  - fee_and_penalty: filing_fee + penalty
expected:
  filing_fee: 50
  penalty_rate: 10
  penalty: 200.00
  fee_and_penalty: 250.00
```

## When to refuse or refer

- Refer a seller with physical presence in a community for that community's own code, return form and due dates; this skill does not hold non-ARSSTC local codes.
- Refer transient lodging, alcohol, tobacco, fuel and other excise questions to the member's code beyond the rates flagged above.
- Refer audits, estimated assessments, protests (30 days from the written notice), repayment plans and penalty waiver requests to a professional with the ARSSTC correspondence.
- Refuse to give a rate or cap for a period without the ARSSTC rate sheet in force for that month, or to state that a sale is exempt without the member's code or a valid certificate.

## Filing and payment

| Step | What to do | Source |
| --- | --- | --- |
| Frequency | Monthly unless ARSSTC approves quarterly or less frequent filing (section 100(B)) | [Uniform Code](https://arsstc.org/wp-content/uploads/2024/09/Uniform-Code_2024-revisions_final_070824.pdf) |
| Monthly due date | Last day of the following month, by midnight Alaska Standard Time (March is due April 30) | [Uniform Code](https://arsstc.org/wp-content/uploads/2024/09/Uniform-Code_2024-revisions_final_070824.pdf) |
| Quarterly due dates | Q1 April 30, Q2 July 31, Q3 October 31, Q4 January 31 | [Uniform Code](https://arsstc.org/wp-content/uploads/2024/09/Uniform-Code_2024-revisions_final_070824.pdf) |
| Return | The portal opens the return on the first day of the month it is due. Download a fresh Excel Upload Template each time, fill the Upload Data tab with sales for every member location (enter 0 where none), upload, review, submit | [How to File, March 2026](https://arsstc.org/wp-content/uploads/2026/03/ARSSTC-How-to-File-Sales-Tax-Returns_Mar2026.pdf) |
| What the portal works out | Tax per community, timely filing compensation, late fees, penalties and interest | [ARSSTC, Business sellers](https://arsstc.org/business-sellers/) |
| Payment | One electronic payment to ARSSTC, which distributes to the communities; no paper returns or checks; ACH credit is set up outside the portal; cards carry a 3% fee | [ARSSTC, FAQs for sellers](https://arsstc.org/faqs-for-sellers/) |
| Zero returns | Required every period while registered | [Uniform Code](https://arsstc.org/wp-content/uploads/2024/09/Uniform-Code_2024-revisions_final_070824.pdf) |
| Amendments | Within one year of the original due date, started in the portal | [ARSSTC, FAQs for sellers](https://arsstc.org/faqs-for-sellers/) |
| Records | Keep sales and exemption records for three years | [ARSSTC, Business sellers](https://arsstc.org/business-sellers/) |
| Return to quarterly after being moved to monthly for non-compliance | Six consecutive on-time filings with full payment (section 100(G)) | [Uniform Code](https://arsstc.org/wp-content/uploads/2024/09/Uniform-Code_2024-revisions_final_070824.pdf) |

Physical-presence sellers file the municipality's own return; DCRA: "you must get the form from the municipality in which you conducted your business and owe the tax."

## Completion checklist

- [ ] Physical presence established or ruled out for every Alaska community
- [ ] 2025 and 2026 gross sales into Alaska totalled, with marketplace sales, against USD 100,000
- [ ] Registration (or Marketplace Seller Affidavit) within 30 days of meeting the threshold
- [ ] Each sale sourced to its delivery or billing address
- [ ] Borough plus city rate, seasonal rate and caps read from the rate sheet for the month of sale
- [ ] Exemption certificates on file for every exempt sale
- [ ] Return filed on the current template by the last day of the following month, zero returns included
- [ ] Payment made electronically in full

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| ARSSTC Remote Seller Sales Tax Code (Uniform Code), amended July 2024. Read for sections 010, 040, 050, 090, 100, 180 and 190 | https://arsstc.org/wp-content/uploads/2024/09/Uniform-Code_2024-revisions_final_070824.pdf | 2026-11-14 |
| ARSSTC, Remote Sales: Repeal of Transaction Thresholds, effective January 1, 2025. Read for the repeal and account closure | https://arsstc.org/wp-content/uploads/2024/09/Threshold-Change-for-Sellers.pdf | 2026-11-14 |
| ARSSTC, Business sellers. Read for physical presence, threshold counting, registration, filing, reduced frequency and records | https://arsstc.org/business-sellers/ | 2026-11-14 |
| ARSSTC, FAQs for sellers. Read for due date, penalties, sourcing, payment, amendments and exemption certificates | https://arsstc.org/faqs-for-sellers/ | 2026-11-14 |
| ARSSTC, How to File Sales Tax Returns, March 2026. Read for the upload template and payment deadline | https://arsstc.org/wp-content/uploads/2026/03/ARSSTC-How-to-File-Sales-Tax-Returns_Mar2026.pdf | 2026-11-14 |
| ARSSTC rate sheet as of 11/1/2026. Read for rates, seasonal rates, caps, alcohol and bed taxes | https://arsstc.org/wp-content/uploads/2026/11/ARSSTC-Sales-Tax-Rate-Sheet-11-1-26.xlsx | 2026-11-14 |
| ARSSTC rate sheets as of 1/1/2026 to 9/1/2026 (9/1/2026 linked). Read for the Juneau cap of USD 15,000 before October 2026 | https://arsstc.org/wp-content/uploads/2026/08/ARSSTC-Sales-Tax-Rate-Sheet-9-1-26.xlsx | 2026-11-14 |
| ARSSTC, Tax rates (index of rate sheets). Read for the current sheet | https://arsstc.org/business-sellers/tax-rates/ | 2026-11-14 |
| City and Borough of Juneau Code 69.05.040 (exemptions). Read for (21) and (22), single item and service caps, vehicles, jewelry, and the Serial No. 2026-22 history note | https://library.municode.com/ak/juneau/codes/code_of_ordinances?nodeId=COLABOJUALVOII_TIT69RETA_CH69.05UNSATA_69.05.040EX | 2026-11-14 |
| Alaska DCCED, Division of Community and Regional Affairs, Sales Tax. Read for no state sales tax, local levy by vote, borough plus city, use tax (AS 29.45.650, 29.45.700) | https://www.commerce.alaska.gov/web/dcra/localgovernmentresourcedesk/taxationassessment/salestax.aspx | 2026-11-14 |
| Alaska Department of Revenue, Personal Income. Read for no individual income tax | https://tax.alaska.gov/programs/programs/index.aspx?10001 | 2026-11-14 |

Not yet confirmed: the codes of members other than Juneau (rates and caps here are as the ARSSTC rate sheet states them, not re-read in each code); the amount of ARSSTC timely filing compensation (the portal computes it; no rate was found on the pages read); whether the Municipality of Anchorage and the City of Fairbanks levy any general sales tax on physical-presence sellers (the rate sheet shows none, and the DCRA page is dated July 2013); the "Defaults to verify" table, which depends on each member's code.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `ak-sales-tax` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/ak-sales-tax. If neither is available, confirm every figure against the official source pages cited above before relying on it.
