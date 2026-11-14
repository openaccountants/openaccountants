---
name: dc-sales-tax
description: Use this skill whenever asked about District of Columbia sales tax, DC OTR filings. Trigger on phrases like "DC sales tax", "District of Columbia sales tax", "OTR". ALWAYS load us-sales-tax first.
version: "2.1"
jurisdiction: US-DC
tax_year: 2026
last_updated: 2026-11-13
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: tax
type: situation-rules
category: state-tax
---

# District of Columbia sales and use tax (2026)

**Circular 230 §10.37 disclosure:** This skill supplies general state-tax working papers from the sources below. It is not a professional approval. A qualified tax professional must review the facts, assumptions and outputs before filing.

**Answer first:** DC's general sales/use rate stays 6% throughout 2026; the general increase is postponed until October 1, 2027. Use the category's total rate: prepared meals/on-premises alcohol 10%, transient lodging 15.95%, and parking 18%. The old 14.95% lodging figure is stale. [§47-2002](https://code.dccouncil.gov/us/dc/council/code/sections/47-2002); [OTR current total rates](https://otr.cfo.dc.gov/page/taxable-and-non-taxable-services).

## Scope

District of Columbia sales/use tax, tax year 2026: goods and specified services, remote and marketplace sales, exemptions, registration, FR-800 and purchaser use tax. DC is one tax jurisdiction; do not add a Maryland or Virginia county rate. Load `us-sales-tax` for federal nexus context. Other state jobs are in `dc-income-tax`, `dc-corporate-tax` and `dc-payroll`.

## Ask the client first

1. DC physical presence, deliveries, employee/agent activity and buyer use/receipt location?
2. Current and prior calendar-year DC retail receipts and transaction counts, including exempt and marketplace transactions?
3. Item/service sold: food/drink, lodging, parking, software/data processing, professional work or goods?
4. Marketplace collection records, direct sales, exemptions and resale certificates?
5. Registered accounts, assigned filing periods and sales/purchase ledgers?
6. Untaxed purchases, other-jurisdiction tax and any amended-period/refund items?

## The method, step by step

### Rates, bands and thresholds

| Item | Amount or rule | Official source |
| --- | --- | --- |
| General taxable retail goods/services in 2026 | 6%; statutory general increase begins October 1, 2027 | [§47-2002(a)](https://code.dccouncil.gov/us/dc/council/code/sections/47-2002) |
| Prepared food/drink and on-premises alcohol | 10% total; do not substitute the bare base-tax component in §47-2002 for the total collection rate | [OTR total rate](https://otr.cfo.dc.gov/page/taxable-and-non-taxable-services) |
| Transient rooms/lodging | 15.95% total through September 30, 2027 | [OTR total rate and period](https://otr.cfo.dc.gov/page/taxable-and-non-taxable-services) |
| Parking/storage of motor vehicles/trailers | 18% | [§47-2002(a)(1)](https://code.dccouncil.gov/us/dc/council/code/sections/47-2002) |
| Soft drinks | 8% in the specified retail category | [§47-2002(a)(8)](https://code.dccouncil.gov/us/dc/council/code/sections/47-2002) |
| Economic nexus, no physical presence | More than $100,000 gross DC retail sales OR more than 200 DC retail transactions, current or previous calendar year | [OTR Remote Sellers FAQs](https://otr.cfo.dc.gov/page/sales-and-use-tax-faqs) |
| Return and payment | 20th following assigned monthly/quarterly period; annual sales-tax year ends September 30, annual due October 20 | [OTR due-date FAQ](https://otr.cfo.dc.gov/page/sales-and-use-tax-faqs) |
| Late filing with balance | 5% per month up to 25%; interest 10% annually compounded daily | [OTR penalty FAQ](https://otr.cfo.dc.gov/page/sales-and-use-tax-faqs) |

### Determine collection and taxability

Physical presence does not get the remote-seller small-volume exception. A remote seller counts exempt sales and sales through marketplaces as well as its own site. OTR explicitly starts collection at the 201st transaction where the revenue limb has not already been crossed; exactly 200 transactions alone does not cross it. Once crossed, collection continues in the following year. Register with online FR-500 on https://mytax.dc.gov and identify remote-seller status. [OTR Remote Sellers FAQs](https://otr.cfo.dc.gov/page/sales-and-use-tax-faqs).

| Legacy topic | Treatment and boundary | Source |
| --- | --- | --- |
| General tangible property and clothing | Generally taxable at the general rate unless a specific product/exemption applies | [OTR FAQ](https://otr.cfo.dc.gov/page/sales-and-use-tax-faqs) |
| Grocery food vs prepared food | Qualifying food/ingredients exempt; prepared immediate-consumption food has the category rate. Do not treat soft drinks as ordinary groceries | [§47-2005 food exemption](https://code.dccouncil.gov/us/dc/council/code/sections/47-2005); [OTR food rate](https://otr.cfo.dc.gov/page/taxable-and-non-taxable-services) |
| Liquor consumed on premises | Prepared-food/on-premises total rate; off-premises sales have a different category and licence exceptions | [OTR rates](https://otr.cfo.dc.gov/page/sales-and-use-tax-faqs) |
| Transient lodging | Use current total lodging rate; classify transient and any remarketer charges before computation | [§47-2002(a)(2)](https://code.dccouncil.gov/us/dc/council/code/sections/47-2002); [OTR period total](https://otr.cfo.dc.gov/page/taxable-and-non-taxable-services) |
| Parking | Category rate applies to storage/parking; no general-rate substitution | [§47-2002(a)(1)](https://code.dccouncil.gov/us/dc/council/code/sections/47-2002) |
| SaaS / software / digital goods | Data-processing and software services are within the taxable categories; classify the actual access/licence/service. Digital goods rules apply to delivered taxable digital products; the legacy assertion is not an exemption | [OTR data-processing definition](https://otr.cfo.dc.gov/page/taxable-and-non-taxable-services) |
| Professional services | No blanket tax on every profession, but listed taxable services can include professional work such as landscaping design or payroll/data processing. Apply the statutory category and contract, not the provider's job title | [OTR specified-services examples](https://otr.cfo.dc.gov/page/taxable-and-non-taxable-services) |
| Manufacturing equipment | Legacy blanket exemption is not confirmed. Identify the precise statutory exemption, purchaser, item and use; otherwise do not treat all manufacturing equipment as exempt | [§47-2005 exemption list](https://code.dccouncil.gov/us/dc/council/code/sections/47-2005) |
| Prescription drugs | Apply the statutory prescription/medical exemption conditions rather than a blanket exemption for all pharmacy goods | [§47-2005](https://code.dccouncil.gov/us/dc/council/code/sections/47-2005) |
| Resale | Document qualifying resale with the prescribed certificate; business use is not resale | [§47-2005 resale provisions](https://code.dccouncil.gov/us/dc/council/code/sections/47-2005) |

Use tax applies at the corresponding sales-tax category rate to taxable property bought for DC use/storage/consumption without the required tax. Document taxes paid elsewhere and the relevant statutory credit before reducing it. [OTR use-tax FAQ](https://otr.cfo.dc.gov/page/sales-and-use-tax-faqs).

A facilitator must collect on facilitated taxable sales. Seller marketplace and direct sales both count for economic nexus, but collection already performed must not be duplicated. OTR requires a separate marketplace account when the same seller also operates its own remote/traditional retail business. Agreements between seller and facilitator do not erase their statutory liability. [Marketplace Sales FAQs](https://otr.cfo.dc.gov/page/sales-and-use-tax-faqs).

### Register, file FR-800 and retain the result

1. Complete online FR-500 registration and activate the correct sales/use and, if applicable, marketplace account on MyTax.DC.gov. Filing a return alone is not registration.
2. In the logged-in Summary locate Sales and Use, choose Returns, then File Now for the correct monthly/quarterly/annual period. FR-800 appears. Answer return-information questions and enter gross sales, exempt/resale and marketplace information, then taxable amounts by rate; reconcile to the ledger and the period's displayed fields. [OTR tutorial pp.2-4](https://mytax.dc.gov/WebFiles/Documents/Tut/Bus/SUT/How_to_File_a_Sales_and_Use_Return.pdf).
3. Report purchaser use tax in the appropriate category and check that taxable/exempt/marketplace totals do not overstate gross sales. The old tutorial illustrates balance on line 19; use the current actual screen rather than assuming every form-year field is unchanged. [OTR tutorial p.4](https://mytax.dc.gov/WebFiles/Documents/Tut/Bus/SUT/How_to_File_a_Sales_and_Use_Return.pdf).
4. Review balance and select payment option. No Payment is Needed is appropriate for a genuine zero return; Pay Later submits a return without paying it. For ACH debit confirm bank details, amount and payment date; submit using the electronic signature and retain the confirmation, filed-return copy and payment reference. Reconcile the bank debit. [OTR tutorial pp.5-8](https://mytax.dc.gov/WebFiles/Documents/Tut/Bus/SUT/How_to_File_a_Sales_and_Use_Return.pdf).
5. Modern sales returns are electronic-only; OTR rejects paper returns for 2017 onward. Follow the assigned frequency and pay by the due date even when using a payroll/tax agent. Annual October filing is not the income-tax calendar-year April filing. [OTR FAQ](https://otr.cfo.dc.gov/page/sales-and-use-tax-faqs).

## Boundary and exception table

| Situation | Treatment |
| --- | --- |
| 200 transactions, receipts not over $100,000, no physical presence | Remote volume test not crossed; 201st sale crosses transaction limb |
| Marketplace-only vs direct sales too | Count both for nexus; reconcile responsibility and separate accounts |
| Bundled services/software | Classify contract components and actual benefit/receipt location; refer ambiguity |
| Exemption claimed | Retain valid certificate and facts satisfying the particular exemption |
| Rental vehicles or specialized excise categories | Not a general-rate case; current statutory October 2026 change and older FAQ rates must be reconciled before computation |

## Worked cases

**Case 1:** An ordinary taxable clothing sale is $1,000: $60 tax, total $1,060. A separate restaurant immediate-consumption sale of $1,000 gives $100 tax, total $1,100. A transient hotel charge of $1,000 gives $159.50 tax and total $1,159.50; $1,000 parking gives $180 tax and total $1,180. These are category total rates, not components to be added again.

```oa-check
name: DC distinct sales categories
inputs:
  sale: 1000
steps:
- clothing: sale * 0.06
- meals: sale * 0.10
- lodging: sale * 0.1595
- parking: sale * 0.18
expected:
  clothing: 60
  meals: 100
  lodging: 159.5
  parking: 180
```
**Case 2:** A remote seller with no presence has 200 sales of $400 each: $80,000, below the revenue limb and not more than 200 sales. The next $400 transaction is number 201, crossing the transaction limb even though receipts are only $80,400. OTR says begin collection with the 201st transaction. For ordinary taxable goods, that sale carries $24 tax. If all 200 sales had instead been $600, receipts would already be $120,000 and the revenue limb would have triggered sooner.

```oa-check
name: DC transaction threshold both sides
inputs:
  count: 200
  price: 400
  alternative_price: 600
steps:
- receipts200: count * price
- receipts201: (count + 1) * price
- tax201: price * 0.06
- alternative_receipts: count * alternative_price
expected:
  receipts200: 80000
  receipts201: 80400
  tax201: 24
  alternative_receipts: 120000
```

## When to refuse or refer

Refer uncertain software/digital bundles, professional-service category disputes, manufacturing-exemption claims, lodging remarketers, rentals affected by the October 2026 change, special events, street-vendor minimums, audits, voluntary disclosure and penalty relief. Ordinary remote nexus does not establish corporate/franchise nexus automatically.

## Filing and payment

Return and payment are separate submissions. Keep both confirmations and the account balance. An old 14.95% hotel lookup or the general-rate increase's earlier October 2026 date must not feed a 2026 calculation.

## Completion checklist

- Physical/economic nexus established using both receipt and transaction facts.
- Current category total rate and any special date selected.
- Exempt/resale and facilitator amounts reconciled with documentation.
- FR-800 correct account/period filed electronically and balance paid.

## Sources

| Source and reading scope | URL | Read on |
| --- | --- | --- |
| OTR sales/use FAQs. Read for general, remote, marketplace, use-tax, deadlines, electronic returns and penalties. | https://otr.cfo.dc.gov/page/sales-and-use-tax-faqs | 2026-11-13 |
| OTR taxable/non-taxable services. Read for service definitions, food rate and lodging total through September 2027; rental-vehicle paragraph not relied upon for post-September 2026. | https://otr.cfo.dc.gov/page/taxable-and-non-taxable-services | 2026-11-13 |
| D.C. Code §47-2002. Read for current general rate period, category base rates and October 2026 vehicle change. | https://code.dccouncil.gov/us/dc/council/code/sections/47-2002 | 2026-11-13 |
| D.C. Code §47-2005. Read for food, prescription, resale and conditional exemption list. | https://code.dccouncil.gov/us/dc/council/code/sections/47-2005 | 2026-11-13 |
| MyTax sales/use tutorial. Read for pp.2-8 account/period selection, FR-800, payment, signature and confirmation. | https://mytax.dc.gov/WebFiles/Documents/Tut/Bus/SUT/How_to_File_a_Sales_and_Use_Return.pdf | 2026-11-13 |

Not yet confirmed: the legacy blanket manufacturing-equipment exemption, precise SaaS/digital-product edge cases, current specialized rental-vehicle total rates and special-category exemptions; the legacy SST nonmembership assertion has not been independently confirmed from a state-host source. These are not treated as tax-computation inputs.
