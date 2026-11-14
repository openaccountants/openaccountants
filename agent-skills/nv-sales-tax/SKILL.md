---
name: nv-sales-tax
description: "Use this skill whenever asked about Nevada sales and use tax. Trigger on phrases like \"Nevada sales tax\", \"NV sales tax\", \"NRS 372\". ALWAYS load us-sales-tax first."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/nv-sales-tax"
  jurisdiction: "US-NV"
  tax_year: "2026"
  last_updated: "2026-11-13"
---

# Nevada sales and use tax, 2026

## Scope

2026 Nevada retail sales and complementary use tax. Load `us-sales-tax` for the federal interstate framework, then apply Nevada taxability, sourcing and registration here. The statewide minimum combined rate is 6.85%; county additions produce Clark 8.375% and Washoe 8.265%. These are current posted schedules read 2026-11-13, not a promise that every location/transaction has the same rate. [Official source](https://tax.nv.gov/news-publications/sales-use-tax-publications/).

**Circular 230 §10.37 disclosure:** This skill supplies general state-tax working papers from the sources below. It is not a professional approval. A qualified tax professional must review the facts, assumptions and outputs before filing.

## Ask the client first

1. Physical business/inventory/staff presence, delivery locations and registration/assigned frequency?
2. Current/prior calendar-year Nevada retail sales dollars and transaction count, direct plus marketplace channels?
3. Product/service, software delivery medium, food/preparation, drugs and any mixed or bundled charges?
4. Resale/exemption certificate or approved abatement, customer identity and use of the purchase?
5. Invoice separately stated shipping, handling, installation/repair versus fabrication charges?
6. Untaxed purchases, inventory withdrawals, other-state tax paid, returns, payments and notices?

## The method, step by step

1. **Establish registration.** Physical-presence obligations are separate from the remote small-seller exception. A remote seller must register when previous/current calendar-year retail sales into Nevada exceed $100,000 **or** reach 200 separate retail transactions. Register/collect by the first day of the calendar month beginning at least 30 days after crossing. Exactly $100,000 and 199 transactions does not cross this remote test; 200 transactions does. Register through Nevada or Streamlined registration, then use My Nevada Tax. [Official source](https://tax.nv.gov/faqs/marketplace-facilitator-seller-faqs/remote-sellers-wayfair-decision/).
2. **Separate marketplace channels.** Determine who collects each sale, retain facilitator evidence, and aggregate direct/marketplace sales when testing the seller's threshold as the state FAQ directs. Do not collect twice where the facilitator remits. The marketplace FAQ's “more than 200” wording differs from the remote FAQ's “200 or more”; for a boundary case apply the legal marketplace definition and obtain confirmation instead of silently changing the remote rule. [Official source](https://tax.nv.gov/faqs/marketplace-facilitator-seller-faqs/).
3. **Classify the transaction.** General tangible goods and clothing are taxable absent a named exemption. Unprepared human food is exempt; prepared immediate-consumption food, alcohol, pet food, tonics/vitamins are not that exemption. Qualifying prescribed medicine is exempt; retain prescription/product evidence. Ordinary professional consulting without a goods sale is not taxable, but services necessary to complete a taxable goods sale and fabrication labour are included. [Official source](https://tax.nv.gov/faqs/sales-tax-faqs/); [§372.283/284](https://www.leg.state.nv.us/NRS/NRS-372.html).
4. **Correct software/equipment treatment.** Electronically delivered software is not Nevada sales/use taxable; prewritten software on physical media is taxable. Pure remotely accessed software with no tangible transfer follows the electronic/service analysis; bundled hardware, licensing and other deliverables require facts. The old absolute “NEVER tax SaaS” is replaced by this fact-dependent rule. The old downloaded-canned-software taxable row was wrong. The old blanket manufacturing-equipment exemption was also unsupported:ordinary equipment is taxable unless a specific exemption or approved GOED abatement applies. A manufacturing label is not an approval. [Official source](https://tax.nv.gov/faqs/sales-tax-faqs/); [Official source](https://goed.nv.gov/incentives/).
5. **Build price and rate.** For delivered retail goods, use the Nevada delivery destination/county; over-the-counter goods use receipt location. Check special lease/vehicle rules separately. Separately stated end-user shipping/transport/postage is excluded; handling, packaging/crating and inbound freight remain taxable. Separately stated installation, repair/reconditioning labour is excluded; fabrication is taxable. Apply the current county rate to the taxable base. Keep a valid resale certificate; own use of resale inventory triggers use tax at cost. [Official source](https://tax.nv.gov/faqs/sales-tax-faqs/); [Official source](https://tax.nv.gov/wp-content/uploads/2024/05/Sales-and-Use-Tax-GeneraI-Info-1.pdf).
6. **Accrue use tax** where tangible goods are used/stored in Nevada and the seller did not collect the tax. Apply the appropriate local rate and allowable other-state sales/use tax credit, never below zero; do not assume an internet order is exempt. Reconcile taxable sales, exempt sales and purchases to books and the return by county. [Official source](https://tax.nv.gov/faqs/sales-tax-faqs/); [Official source](https://tax.nv.gov/wp-content/uploads/2024/05/Sales-and-Use-Tax-GeneraI-Info-1.pdf).

### Rates, bands and thresholds

| Item | Amount or rule | Official source |
| --- | --- | --- |
| Statewide minimum combined | 6.85%; not a further addition to the county combined rate | [Official source](https://tax.nv.gov/news-publications/sales-use-tax-publications/) |
| Clark County | 8.375% combined | [Official source](https://tax.nv.gov/news-publications/sales-use-tax-publications/) |
| Washoe County | 8.265% combined | [Official source](https://tax.nv.gov/news-publications/sales-use-tax-publications/) |
| Posted minimum-to-maximum county range | 6.85%-8.375%; local additions 0%-1.525% | [Official source](https://tax.nv.gov/wp-content/uploads/2024/05/ADM-T047-State-Sales-Tax-Map.pdf) |
| Remote economic threshold | >$100,000 retail sales OR>=200 retail transactions, current/prior calendar year | [Official source](https://tax.nv.gov/faqs/marketplace-facilitator-seller-faqs/remote-sellers-wayfair-decision/) |
| Quarterly filing eligibility | Taxable sales not exceeding $10,000 monthly, subject to assigned frequency | [Official source](https://tax.nv.gov/faqs/marketplace-facilitator-seller-faqs/remote-sellers-wayfair-decision/) |
| Sales/use due | 20th of month after assigned reporting period | [Official source](https://tax.nv.gov/wp-content/uploads/2024/05/Sales-and-Use-Tax-GeneraI-Info-1.pdf) |
| Late-payment penalty | 2% days 1-10; 4%11-15; 6%16-20; 8%21-30; 10%31+ | [Official source](https://tax.nv.gov/wp-content/uploads/2024/05/Sales-and-Use-Tax-GeneraI-Info-1.pdf) |
| Interest | 0.75% per month or fraction | [Official source](https://tax.nv.gov/wp-content/uploads/2024/05/Sales-and-Use-Tax-GeneraI-Info-1.pdf) |

| Old transaction pattern | 2026 treatment | Official source |
| --- | --- | --- |
| General goods/clothing | Taxable at applicable combined rate | [Official source](https://tax.nv.gov/faqs/sales-tax-faqs/) |
| Grocery versus prepared food | Unprepared qualifying food exempt; prepared immediate-consumption food taxable | [§372.284](https://www.leg.state.nv.us/NRS/NRS-372.html) |
| SaaS/electronic software | Pure electronic/service delivery generally no sales/use tax; tangible bundles need review | [Official source](https://tax.nv.gov/faqs/sales-tax-faqs/) |
| Canned software downloaded | Not taxable electronically; physical disk taxable | [Official source](https://tax.nv.gov/faqs/sales-tax-faqs/) |
| Professional services | No tax on ordinary standalone consulting; taxable goods-related work distinguished | [Official source](https://tax.nv.gov/faqs/sales-tax-faqs/) |
| Manufacturing equipment | No blanket exemption; document approved relief | [Official source](https://goed.nv.gov/incentives/) |
| Prescription medicine | Qualifying prescribed medicine exempt | [§372.283](https://www.leg.state.nv.us/NRS/NRS-372.html) |
| Resale | Certificate and resale intent required; own-use withdrawal taxable | [Official source](https://tax.nv.gov/faqs/sales-tax-faqs/); [Official source](https://tax.nv.gov/wp-content/uploads/2024/05/Sales-and-Use-Tax-GeneraI-Info-1.pdf) |

## Worked cases

**Case 1:** Clark delivery:$1,000 goods, $50 taxable handling, $100 separate installation, $40 separate outbound shipping. Taxable $1,050 x 8.375%=$87.94; invoice total $1,277.94. If installation/shipping were not properly separated, the exclusion would need rechecking.

```oa-check
name: NV Clark taxable price
inputs:
  goods: 1000
  handling: 50
  installation: 100
  shipping: 40
steps:
- base: goods + handling
- tax: round(base * 0.08375, 2)
- invoice: base + installation + shipping + tax
expected:
  base: 1050
  tax: 87.94
  invoice: 1277.94
```

**Case 2:** The same $2,000 prewritten software delivered only electronically gives $0 Nevada sales tax. Supplied on a physical disk to Washoe, it is tangible:$2,000 x 8.265%=$165.30. Sales tax treatment does not remove Commerce Tax or other business obligations.

```oa-check
name: NV software delivery decision
inputs:
  price: 2000
steps:
- electronic_tax: price * 0
- physical_tax: price * 0.08265
expected:
  electronic_tax: 0
  physical_tax: 165.3
```

## When to refuse or refer

Refer disputed remote/marketplace boundaries, leases/vehicles, contractors, medical-item classification, bundled software, food definitions and claimed manufacturing abatements without approval. National Guard/veteran and special event exemptions require their own state conditions. This skill does not supply a universal SaaS exemption for every contract. The old “NEVER compute any number” instruction is retired; source-backed arithmetic is required.

## Filing and payment

Obtain a seller permit and use assigned monthly, quarterly or annual period; do not change frequency unilaterally. Quarterly eligibility generally applies when taxable sales do not exceed $10,000 monthly; CSP remote reporting is monthly. Special annual eligibility needs state confirmation. Returns/payments are due the 20th of the following month, with the actual return's weekend/holiday date. File zero returns while registered, report sales/use separately and retain certificates, invoices, county rate evidence and confirmations. My Nevada Tax accepts filing/payment; the current general sheet provides graduated late penalty and 0.75% monthly interest. [Official source](https://tax.nv.gov/faqs/marketplace-facilitator-seller-faqs/remote-sellers-wayfair-decision/); [Official source](https://tax.nv.gov/wp-content/uploads/2024/05/Sales-and-Use-Tax-GeneraI-Info-1.pdf); [Official source](https://tax.nv.gov/tax-types/sales-tax-use-tax/).

## Sources

| Source and reading scope | URL | Read on |
| --- | --- | --- |
| DOR sales FAQ. Read for goods, services, shipping, electronic software, use tax and resale. | https://tax.nv.gov/faqs/sales-tax-faqs/ | 2026-11-13 |
| DOR rate publications. Read for current statewide minimum and county schedules. | https://tax.nv.gov/news-publications/sales-use-tax-publications/ | 2026-11-13 |
| State county map. Read for county range and address/county checking. | https://tax.nv.gov/wp-content/uploads/2024/05/ADM-T047-State-Sales-Tax-Map.pdf | 2026-11-13 |
| DOR remote seller FAQ. Read for threshold boundary, registration start and filing frequency. | https://tax.nv.gov/faqs/marketplace-facilitator-seller-faqs/remote-sellers-wayfair-decision/ | 2026-11-13 |
| DOR marketplace FAQ. Read for channel collection and threshold aggregation. | https://tax.nv.gov/faqs/marketplace-facilitator-seller-faqs/ | 2026-11-13 |
| DOR general information. Read for tax base, zero returns, due 20th, penalty and interest. | https://tax.nv.gov/wp-content/uploads/2024/05/Sales-and-Use-Tax-GeneraI-Info-1.pdf | 2026-11-13 |
| NRS 372. Read for human-food and medicine exemptions; read through web. | https://www.leg.state.nv.us/NRS/NRS-372.html | 2026-11-13 |
| GOED incentives. Read for approval-based abatements rather than blanket equipment exemption. | https://goed.nv.gov/incentives/ | 2026-11-13 |
| DOR sales/use page. Read for current filing and registration links. | https://tax.nv.gov/tax-types/sales-tax-use-tax/ | 2026-11-13 |

Not yet confirmed: contract-specific SaaS/bundled treatment, marketplace 200 transaction wording conflict, medical/prepared-food edge cases, special abatements and annual filing eligibility without an account assignment. No blanket manufacturing exemption or unconditional SaaS rule is established.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-13. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `nv-sales-tax` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/nv-sales-tax. If neither is available, confirm every figure against the official source pages cited above before relying on it.
