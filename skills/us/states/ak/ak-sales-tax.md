---
name: ak-sales-tax
description: "Alaska 2026 local sales/use tax and ARSSTC remote-seller workflow: statewide economic threshold, physical-presence separation, marketplace-only affidavit, delivery sourcing, municipal rates and caps, Juneau's 2026 cap changes, Kenai's stacked taxes, registration, returns and records. Load us-sales-tax for the federal/interstate framework."
version: "1.2"
jurisdiction: US-AK
tax_year: 2026
last_updated: 2026-11-14
depends_on:
  - us-sales-tax
category: state-tax
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: tax
type: situation-rules
tax_year_notes: "2026 local rules; rates/caps checked against the 1 November 2026 ARSSTC sheet and dated Juneau notices. The 2025 example is historical only."
---

# Alaska local sales and use tax, 2026

> **General reference only.** Source-cited draft, not approved by an accountant. Under US Treasury Circular 230 section 10.37, this is a working-paper aid. A qualified professional must review the actual facts, municipal law, period and return before filing or taking a position.

## Scope

**Answer first.** Alaska has no statewide sales tax. Cities and boroughs can tax locally, sometimes both on the same sale. Remote sellers use the Alaska Remote Seller Sales Tax Commission (ARSSTC) for adopting member jurisdictions; physical-presence sales are reported directly to the municipality. A statewide remote-sales threshold is an administration rule, not a statewide tax rate. [Alaska DCRA, sales/use explanation](https://www.commerce.alaska.gov/web/dcra/OfficeoftheStateAssessor/AlaskaSalesTaxInformation.aspx); [ARSSTC business guidance](https://arsstc.org/business-sellers/).

This skill covers ordinary goods and services, remote registration, marketplace allocation, member-jurisdiction returns and two retained municipal cases. Every municipality's use-tax return, special industry tax and exemption is not reproduced. `us-sales-tax` owns the wider interstate framework; federal income, Alaska individual-income-tax status and Permanent Fund Dividend questions belong to the pack router and relevant federal income skill, including `us-form-1040-individual-return`. No federal figure is computed here.

## Ask the client first

1. Actual delivery/service-benefit address, sale date, municipality and any nested borough; physical office, inventory, representative or equipment there?
2. Current and previous calendar-year remote Alaska gross sales, including marketplace and exempt/non-taxing-destination sales, separated from physical-presence sales?
3. All sales through a collecting marketplace, or also a website/direct channel; facilitator affidavit and collection evidence?
4. Goods/service classification, separately priced items, bundles, instalments, vehicle status, resale/exemption documents?
5. Existing local/ARSSTC registrations, assigned filing frequency, first threshold date, returns, credits, notices, sale or closure of business?

## The method, step by step

### 1. Identify the collection regime

Use the actual delivery address and member effective date. There is no single Alaska rate or exemption list. The State Assessor explains that city and borough levies can overlap and local governments determine most exemptions. Do not infer a blanket grocery, professional-service or software exemption. [DCRA](https://www.commerce.alaska.gov/web/dcra/OfficeoftheStateAssessor/AlaskaSalesTaxInformation.aspx).

- Physical presence includes an office, warehouse, storefront, inventory, service/sales agent, independent sales consultant or rented equipment. Register/report the sales in that physical-presence jurisdiction directly with it, including remote deliveries into that same jurisdiction. The remote economic threshold does not excuse local physical-presence duties.
- An Alaska business selling remotely into other member jurisdictions separates those remote receipts and files them with ARSSTC when subject to the code. Count only remote sales outside its home physical-presence jurisdictions for the remote threshold.
- A seller with no Alaska physical presence counts all Alaska remote sales, including marketplace sales. Nonmember obligations must be checked directly with the local government; the ARSSTC portal is not a return for every Alaska municipality.
- Goods/services sent out of Alaska do not fall under the ARSSTC remote code; check the destination's law separately.

Source: [ARSSTC business guidance, physical-presence and channel sections](https://arsstc.org/business-sellers/); [Uniform Code sections 010, 040 and 050](https://arsstc.org/wp-content/uploads/2024/09/Uniform-Code_2024-revisions_final_070824.pdf).

### 2. Test the threshold and marketplace route

The threshold is **at least $100,000** statewide gross remote sales of property, products or services in the current **or** previous calendar year, including marketplace sales and transactions exempt locally or delivered to non-taxing communities. It is not a per-town test. The 200-transaction prong ended on 1 January 2025. A seller delivering only to non-taxing communities need not register until it makes sales into a taxing member community; a threshold seller selling only exempt products into a taxing member community still registers/reports exempt sales. [Uniform Code sections 040 and 090](https://arsstc.org/wp-content/uploads/2024/09/Uniform-Code_2024-revisions_final_070824.pdf); [seller FAQ](https://arsstc.org/faqs-for-sellers/).

A marketplace-only seller is not required to register with ARSSTC but must submit the Commission's Marketplace Seller Affidavit. A mixed-channel seller counts marketplace sales for threshold purposes, collects/reports its own non-marketplace sales, and does not report the same platform sales again. A facilitator tests all sellers' Alaska sales and collects for sellers regardless of each seller's individual threshold. Delivery-network, transient-lodging and travel-agency marketplace exceptions have separate local reporting under code sections 040/050/090; do not generalize the ordinary-goods platform rule to them. Juneau specifically moved qualifying marketplace-facilitator reporting to ARSSTC from 1 October 2026; confirm the correct account for that period. [ARSSTC channels](https://arsstc.org/business-sellers/); [Uniform Code](https://arsstc.org/wp-content/uploads/2024/09/Uniform-Code_2024-revisions_final_070824.pdf); [Juneau 2026 changes](https://juneau.org/finance/sales-tax-info).

### Rates, bands and thresholds

| Item | Amount, period and conditions | Official source |
| --- | --- | --- |
| Statewide sales tax | None; local city/borough levies can apply together | [DCRA](https://www.commerce.alaska.gov/web/dcra/OfficeoftheStateAssessor/AlaskaSalesTaxInformation.aspx) |
| Remote threshold | $100,000 or more, current or prior calendar year, statewide gross remote sales; no transaction-count prong from 1 January 2025 | [Code section 040](https://arsstc.org/wp-content/uploads/2024/09/Uniform-Code_2024-revisions_final_070824.pdf) |
| Registration | Within 30 calendar days of meeting threshold or code effective date, whichever occurs second; an approved technical implementation extension is not automatic | [Code section 090](https://arsstc.org/wp-content/uploads/2024/09/Uniform-Code_2024-revisions_final_070824.pdf) |
| Default returns | Monthly; received by midnight Alaska Standard Time on the last day of the next month; zero returns required while registered | [Code section 100](https://arsstc.org/wp-content/uploads/2024/09/Uniform-Code_2024-revisions_final_070824.pdf) |
| Approved quarterly returns | 30 April, 31 July, 31 October, 31 January; less frequent filing requires approval, not a seller's unilateral election | [Code section 100](https://arsstc.org/wp-content/uploads/2024/09/Uniform-Code_2024-revisions_final_070824.pdf) |
| Juneau general sales rate | 5% for the 2026 examples; special goods/additional taxes may differ | [1 November 2026 sheet, General Remote Sales Tax row 25](https://arsstc.org/wp-content/uploads/2026/11/ARSSTC-Sales-Tax-Rate-Sheet-11-1-26.xlsx) |
| Juneau single-item/service cap | $15,000 from 1 January through 30 September 2026; at 5%, maximum $750 | [Juneau cap notice](https://juneau.org/wp-content/uploads/2025/12/2025-Sales-Tax-Cap-Change-HOT-TOPIC-Notice.pdf) |
| Juneau single-item/service cap | $50,000 from 1 October 2026; motor vehicles priced at $50,000 or less retain a $15,000 cap; more expensive vehicles use $50,000 | [Juneau Ordinance 2026-27(am) explanation](https://juneau.org/finance/sales-tax-info) |
| Kenai City plus Kenai Peninsula Borough | City 3% plus borough 3%; the ordinary single-item example is capped at $500 in each levy, combined maximum $30 | [1 November sheet, General rows 26-31 and Tax Caps rows 70-77](https://arsstc.org/wp-content/uploads/2026/11/ARSSTC-Sales-Tax-Rate-Sheet-11-1-26.xlsx) |
| Homer City plus borough | Ordinary general rate 4.85% plus 3%, combined 7.85%; $500 cap and $39.25 maximum shown for the listed ordinary cap categories. Food seasonal rules are separate | [1 November sheet, General row 26, Tax Caps rows 54-57 and seasonal notes](https://arsstc.org/wp-content/uploads/2026/11/ARSSTC-Sales-Tax-Rate-Sheet-11-1-26.xlsx) |
| Record retention | Sales records 3 years from the reporting return, with exemption documentation retained for 3 years | [Code section 210](https://arsstc.org/wp-content/uploads/2024/09/Uniform-Code_2024-revisions_final_070824.pdf) |

### 3. Determine base, rate, cap and exemption for the sale date

Use the Commission's address lookup linked from its business page and the sheet for the sale period; ZIP or ZIP+4 alone is not adequate. Save the lookup result, municipal code, jurisdiction code, applicable effective date and classification. For each overlapping city/borough levy calculate its own base and tax, then add the levies. Do not apply a combined rate to an assumed common cap unless both levies actually share that cap. [ARSSTC business guidance](https://arsstc.org/business-sellers/); [Code sections 030 and 260](https://arsstc.org/wp-content/uploads/2024/09/Uniform-Code_2024-revisions_final_070824.pdf).

For an ordinary single item: taxable base = min(item selling price, applicable single-item cap), where that exemption actually applies. A cap on a single item is not necessarily a cap on a whole invoice. Bundled taxable/nontaxable products need reasonable, verifiable allocation; an undivided bundle does not automatically qualify for the single-item/service cap. Instalment and separately invoiced delivery rules use the original sale/service date as specified in section 030 and the local code. [Code sections 030 and 060](https://arsstc.org/wp-content/uploads/2024/09/Uniform-Code_2024-revisions_final_070824.pdf).

**AUDIT FLASH POINT:** the 1 November sheet's Juneau vehicle row shows a general $50,000 cap. The municipality's current explanation specifies a lower $15,000 cap for motor vehicles sold for $50,000 or less. Apply the municipal condition, not the abbreviated sheet row. The old $14,300/$715 Juneau figures are 2025 history, not 2026 inputs. The December 2025 cap notice also ends with an apparent 2025 implementation-date typo; its operative text expressly makes $15,000 effective 1 January 2026. [Juneau changes](https://juneau.org/finance/sales-tax-info); [December cap notice](https://juneau.org/wp-content/uploads/2025/12/2025-Sales-Tax-Cap-Change-HOT-TOPIC-Notice.pdf).

## Boundary and exception table

| Pattern / fact | Treatment / action |
| --- | --- |
| General tangible goods | Apply the destination municipality's taxability, rate and cap; no single state levy |
| Groceries/unprepared food | Read the local exemption and seasonal notes; do not reuse the old unsupported statewide "often exempt" default |
| Professional services | Can fall within local sales tax; establish the service's benefit/delivery situs and local exemption |
| SaaS/digital products | Local classification must be established; no universal exemption or federal-state rate substitution |
| Resale | Obtain the applicable valid certificate and local exemption. A remote reseller without local presence may apply for the Commission certificate; section 190 makes it expire at calendar-year end |
| Exempt buyer | Keep authorization number, buyer/organization, date, price and tax exempted; missing documentation can invalidate the claim |
| Marketplace-only goods seller | Affidavit route; do not duplicate facilitator-reported tax |
| Physical presence plus remote channels | Separate local physical-presence and outside-home remote revenue streams; the local account is not replaced by ARSSTC |
| No-tax municipality or address | Establish jurisdiction from the actual location; Alaska's lack of a state tax is not proof of local exemption |
| Local use tax | DCRA says local use tax can accompany sales tax, equals its rate, and is levied on buyers. With proof of sales tax paid, only a positive difference may remain. Obtain the municipality's own return and rules |

Sources: [Code sections 010, 050, 100 and 190](https://arsstc.org/wp-content/uploads/2024/09/Uniform-Code_2024-revisions_final_070824.pdf); [DCRA use-tax and overlapping-levy FAQ](https://www.commerce.alaska.gov/web/dcra/OfficeoftheStateAssessor/AlaskaSalesTaxInformation.aspx).

### Defaults and red flags

No usable address, period, exemption or cap: request the missing evidence and withhold a final computation. Flag a $100,000 threshold crossing, mixed channels, a new physical location, a bundle, a high-value Juneau vehicle, inconsistent sheet/code text, and any claimed filing-frequency change. Do not call an unconfirmed rate "0%". The old Anchorage/Fairbanks examples of no general levy were not independently established in this refresh; use current municipal evidence rather than assuming from city name.

## Worked cases

### Case A: retained Juneau $20,000 item, with the correct year and vehicle branch

Assume a registered remote seller makes a taxable, unbundled $20,000 ordinary single-item sale to Juneau at 5%. The old December 2025 sheet's $14,300 cap gives $715 for a **2025** sale. From January through September 2026 the $15,000 cap gives $750. On or after 1 October 2026, the ordinary-item $50,000 cap leaves all $20,000 taxable: $1,000. A qualifying $20,000 motor vehicle retains the $15,000 cap and produces $750, a $250 difference from the ordinary item. Classification, not a seller election, decides the result. [2025 sheet](https://arsstc.org/wp-content/uploads/2025/11/ARSSTC-Sales-Tax-Rate-Sheet-12-1-25.xlsx); [January notice](https://juneau.org/wp-content/uploads/2025/12/2025-Sales-Tax-Cap-Change-HOT-TOPIC-Notice.pdf); [October change](https://juneau.org/finance/sales-tax-info).

```oa-check
name: Alaska Juneau retained item and 2026 cap decision
inputs:
  price: 20000
steps:
  - historical_2025_tax: min(price, 14300) * 0.05
  - jan_sep_2026_tax: min(price, 15000) * 0.05
  - oct_ordinary_tax: min(price, 50000) * 0.05
  - oct_vehicle_tax: min(price, 15000) * 0.05
  - classification_difference: oct_ordinary_tax - oct_vehicle_tax
expected:
  historical_2025_tax: 715
  jan_sep_2026_tax: 750
  oct_ordinary_tax: 1000
  oct_vehicle_tax: 750
  classification_difference: 250
```

### Case B: retained Kenai $800 single item and stacked caps

A taxable ordinary $800 single item delivered in Kenai City is subject to the city 3% and borough 3%, each with the listed $500 cap. Borough tax $15 plus city tax $15 = $30. Do not tax all $800 at 6%, or use only the city levy. For the same ordinary capped item in Homer, the listed city 4.85% plus borough 3% gives $39.25; this is not a statement about seasonal grocery treatment. [November 2026 rate/cap sheets](https://arsstc.org/wp-content/uploads/2026/11/ARSSTC-Sales-Tax-Rate-Sheet-11-1-26.xlsx).

```oa-check
name: Alaska retained Kenai stacked cap and Homer comparison
inputs:
  price: 800
  cap: 500
steps:
  - taxable: min(price, cap)
  - borough_tax: taxable * 0.03
  - city_tax: taxable * 0.03
  - total_tax: borough_tax + city_tax
  - homer_total: taxable * (0.0485 + 0.03)
expected:
  borough_tax: 15
  city_tax: 15
  total_tax: 30
  homer_total: 39.25
```

### Case C: own-site sales versus marketplace-only registration

Assume no Alaska physical presence, $90,000 direct and $20,000 marketplace remote Alaska gross sales in the year, and delivery into adopting taxing communities. Total $110,000 exceeds the threshold by $10,000. Register and handle the $90,000 direct channel; the $20,000 platform channel is not reported twice. If instead all $110,000 goes through a collecting marketplace, the seller uses the marketplace-only affidavit route. This example determines registration/channel responsibility, not taxable sales or tax due. [Code sections 040/090](https://arsstc.org/wp-content/uploads/2024/09/Uniform-Code_2024-revisions_final_070824.pdf); [business guidance](https://arsstc.org/business-sellers/).

```oa-check
name: Alaska threshold with marketplace sales
inputs:
  direct: 90000
  marketplace: 20000
steps:
  - threshold_sales: direct + marketplace
  - excess_over_threshold: threshold_sales - 100000
  - seller_channel: direct
expected:
  threshold_sales: 110000
  excess_over_threshold: 10000
  seller_channel: 90000
```

## When to refuse or refer

Refer disputed physical presence, unconfirmed local service/digital situs or exemption, nonmember returns, marketplace lodging/travel/delivery exceptions, transfer-of-business successor liability, audits/protests and local use-tax computations without the local law. Do not use a new municipality's rate before its code effective date. Federal income/PFD and non-Alaska taxes stay with their owners.

## Filing and payment

Register at [arsstc.munirevs.com](https://arsstc.munirevs.com/) within the section 090 deadline; retain legal name, primary address, sales-tax contact and confirmation. Start collection when required; if software cannot implement immediately, obtain an approved implementation arrangement instead of assuming an automatic grace period. Section 090 allows a granted technical extension up to 90 days. Physical-presence/local accounts remain separate.

Use the monthly jurisdiction template downloaded from the portal, reconcile gross/exempt/taxable sales and jurisdiction taxes, exclude facilitator-reported marketplace sales, review the calculated tax and any charges, then transmit the return and electronic payment. Keep filing and payment confirmations separately. File zero returns and explain why no tax is due. Returns use the same cash/accrual basis as the federal return under section 100; no federal tax amount is repeated here. [Business guidance](https://arsstc.org/business-sellers/); [Code sections 090, 100 and 120](https://arsstc.org/wp-content/uploads/2024/09/Uniform-Code_2024-revisions_final_070824.pdf).

Reduced filing requires a written request and Commission approval consistent with member rules. The business webpage says less than $100,000 taxable dollars or 12 transactions annually; its linked detailed guideline says less than $10,000 taxable sales or fewer than 12 transactions in the preceding 12 months, and allows an annual request when all gross sales were exempt. Those are inconsistent descriptions, not alternative automatic elections. Keep monthly filing until the Commission confirms the assigned frequency; this skill does not certify a numeric reduced-frequency eligibility cutoff. [Business webpage](https://arsstc.org/business-sellers/); [linked guideline](https://arsstc.org/wp-content/uploads/2021/07/Filing-Frequency-Change-Guidelines-6.22.21.pdf); [Code section 100](https://arsstc.org/wp-content/uploads/2024/09/Uniform-Code_2024-revisions_final_070824.pdf).

For ARSSTC returns, section 180 imposes $25 per late month/fraction, capped at $100; unpaid sales tax bears 15% annual interest plus 5% per late month/fraction capped at 20% of delinquent tax, with no interest on the penalty. Incomplete returns are treated as no return. A written penalty-waiver application has a 45-day delinquency deadline, payment conditions and at most one such waiver per calendar year. These are Commission rules, not every local municipality's penalties; Juneau's direct-filer interest and procedure changed separately in 2026. [Code section 180](https://arsstc.org/wp-content/uploads/2024/09/Uniform-Code_2024-revisions_final_070824.pdf); [Juneau changes](https://juneau.org/finance/sales-tax-info).

Keep sales and exemption records under section 210. Notify ARSSTC within 30 days of closure/cessation; file a final return rather than just stop filing. Transfers of a majority business interest require at least 10 business days' advance notice and a final return within 30 days under section 220; obtain specialist review of buyer liability and final-audit rules. [Business guidance](https://arsstc.org/business-sellers/); [Code sections 210/220](https://arsstc.org/wp-content/uploads/2024/09/Uniform-Code_2024-revisions_final_070824.pdf).

## Completion checklist

- Actual place, period, physical presence and member status established; local and Commission streams separated.
- Both current/prior-year threshold totals include marketplace and exempt remote receipts; no post-2024 transaction-count trigger.
- Marketplace affidavit or mixed-channel responsibilities documented.
- Each city/borough rate, cap, special classification and exemption traced to current evidence; Juneau date/vehicle conditions applied.
- Return template reconciled, correct assigned frequency, zero/final returns resolved, payment/receipt and records retained.
- No state-wide rate, automatic grocery exemption, automatic reduced filing or unsupported federal conclusion issued.

## Sources

| Source and reading scope | URL | Read on |
| --- | --- | --- |
| Alaska DCRA Sales Tax Information. Read for the local-only, overlapping city/borough, municipal exemption and use-tax credit FAQ in the web reader; direct scripted fetch returned 403. | https://www.commerce.alaska.gov/web/dcra/OfficeoftheStateAssessor/AlaskaSalesTaxInformation.aspx | 2026-11-14 |
| ARSSTC Business/Sellers. Read for physical presence, Alaska/out-of-state channels, marketplaces, registration, filing, records and lookup guidance. | https://arsstc.org/business-sellers/ | 2026-11-14 |
| ARSSTC seller FAQ. Read for statewide measurement, non-taxing/exempt deliveries and physical-presence threshold questions. | https://arsstc.org/faqs-for-sellers/ | 2026-11-14 |
| Uniform Code amended July 2024, effective 1 January 2025. Read for sections 010-100, 120, 180-190, 210-220 and 260 with neighbouring provisions; not a full protest/audit manual. | https://arsstc.org/wp-content/uploads/2024/09/Uniform-Code_2024-revisions_final_070824.pdf | 2026-11-14 |
| ARSSTC current rate index and linked 1 November 2026 workbook. Read for general rows, seasonal notes, Juneau/Kenai/Homer caps and marketplace sheet; local vehicle condition reconciled to Juneau's own explanation. | https://arsstc.org/business-sellers/tax-rates/ | 2026-11-14 |
| ARSSTC 1 November 2026 workbook. Read for exact general/cap cells for the worked examples; not a universal statewide rate range. | https://arsstc.org/wp-content/uploads/2026/11/ARSSTC-Sales-Tax-Rate-Sheet-11-1-26.xlsx | 2026-11-14 |
| Archived 1 December 2025 workbook. Read for the old Juneau $14,300/$715 and Kenai cap/rate cells to preserve and date the old cases. | https://arsstc.org/wp-content/uploads/2025/11/ARSSTC-Sales-Tax-Rate-Sheet-12-1-25.xlsx | 2026-11-14 |
| Juneau December 2025 cap notice. Read for effective date and $15,000/$750 change; noted contradictory closing-year typo. | https://juneau.org/wp-content/uploads/2025/12/2025-Sales-Tax-Cap-Change-HOT-TOPIC-Notice.pdf | 2026-11-14 |
| Juneau Sales Tax Code & Policy Changes. Read for October cap/vehicle exception and marketplace move; neighbouring direct-filer changes distinguish local procedures from ARSSTC. | https://juneau.org/finance/sales-tax-info | 2026-11-14 |
| ARSSTC filing-frequency guideline linked by current business page. Read for all criteria, approval and reversion rules; $10,000 text conflicts with webpage's $100,000. | https://arsstc.org/wp-content/uploads/2021/07/Filing-Frequency-Change-Guidelines-6.22.21.pdf | 2026-11-14 |

Not yet confirmed: numeric reduced-frequency eligibility while the official webpage and linked guideline disagree; all municipalities' use-tax returns, current nonmember rates and product-specific exemptions; unsupported old Anchorage/Fairbanks general-tax examples and grocery/professional-service defaults. The 2025 $14,300 Juneau cap is historical only. Future 2027 seasonal changes are not 2026 instructions. The obsolete registration/closure PDF links returned 404 in the web reader; use the live portal and current administrator instructions rather than those dead documents.
