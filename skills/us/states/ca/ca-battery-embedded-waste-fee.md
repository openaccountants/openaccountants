---
name: ca-battery-embedded-waste-fee
description: >
  California covered battery-embedded (CBE) waste recycling fee for 2026 and
  the change from 1 January 2027. Covers which products count (a battery the
  user cannot easily remove with household tools) and which do not (medical
  devices, video display devices that carry the eWaste fee instead, energy
  storage systems, e-cigarettes, products with tool-free removable batteries,
  power banks), the 1.5% rate with its USD 15 cap in 2026 falling to USD 1 in
  2027, who collects (retailers, lessors, marketplace facilitators) and who
  pays directly, the 3% retailer reimbursement, the separate receipt line,
  leases, refunds, out-of-state shipments, sales for resale, the quarterly
  CDTFA return, and the rule that the fee is outside the sales tax base.
  Trigger on "CBE fee", "battery-embedded fee", "California battery fee 2026",
  "SB 1215 fee", "CDTFA battery recycling fee", "1.5 percent battery fee".
version: 0.1
jurisdiction: US-CA
category: state-tax
tax_year: 2026
tax_year_notes: "2026-27"
last_updated: 2026-11-21
tier: 2
domain: tax
type: computation
---

# California covered battery-embedded waste recycling fee, 2026 and 2027 v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

> **Source-cited draft.** Built from Public Resources Code sections 42463 and 42464 as published in the CDTFA law guide, CDTFA special notices L-1000 (October 2025), L-1026 (April 2026) and L-1047 (November 2026), the CDTFA Covered Electronic Waste Recycling Fees Guide and its Industry Topics page, and the CalRecycle Q&A for Covered Battery-Embedded Products (updated 15 May 2026), read on 2026-11-21. No accountant has reviewed it.

**Answer first.** Since 1 January 2026, a consumer who buys or leases a new or refurbished product with a battery that cannot easily be removed with household tools (a typical smartphone, for example) pays a recycling fee of **1.5% of the retail sales price**, collected by the retailer and sent to the CDTFA on a separate quarterly return. In 2026 the fee is capped at **USD 15** per product. From **1 January 2027** the rate stays 1.5% but the cap falls to **USD 1** per product, so any product priced at USD 66.67 or more pays the flat USD 1. The retailer may keep up to 3% of what it collects, must show the fee as its own line on the receipt, and leaves it out of the sales tax calculation.

**Tax year.** Calendar 2026 and 2027 (the 2027 rate was published in November 2026). CalRecycle sets the rate and maximum by 1 October each year for the next calendar year ([CDTFA L-1047](https://cdtfa.ca.gov/formspubs/l1047.pdf)).

**Circular 230 disclosure.** This material is general information, not written advice on a specific transaction under 31 CFR 10.37. It is not intended to be used, and cannot be used, to avoid penalties.

## Scope and who this is for

In scope: retailers and lessors that sell or lease covered battery-embedded products for use in California, by any channel (store, mail order, internet), including manufacturers selling direct and marketplace facilitators; consumers and businesses that buy such products without paying the fee; retailers that take CBE products out of inventory for their own use; and vendors that collect the fee from a retailer-lessor ([CDTFA L-1000](https://cdtfa.ca.gov/formspubs/l1000.pdf); [CDTFA CBE return instructions](https://cdtfa.ca.gov/online-filing-instructions/Covered-Battery-Embedded-CBE-Waste-Recycling-Fee-Return.htm)).

Out of scope, and where it goes:

| Topic | Skill |
| --- | --- |
| The eWaste fee on covered video display devices (TVs, monitors, laptops, tablets) | refer (separate CDTFA program) |
| Sales and use tax on the product itself | `california-sales-tax` |
| Manufacturer labelling, reporting and take-back duties under SB 1215 | refer (CalRecycle) |
| Loose batteries, power banks | not covered by this fee |

## Ask the client first

- What products do you sell or lease into California that contain a battery? For each, has the manufacturer said whether it is a covered battery-embedded product?
- Is any of them a video display device (such as a laptop, tablet or monitor) that already carries the eWaste fee?
- How do you sell: own store, website, a marketplace (which one), leases? Do you ship to customers outside California?
- Do you have a CDTFA CBE fee account, separate from your seller's permit and any eWaste account? Which quarters have been filed?
- Does your point-of-sale system add the fee on its own line and keep it out of sales tax? Has it been updated for the USD 1 cap from 1 January 2027?

## The method, step by step

### Rates, bands and thresholds

| Item | Figure | Conditions | Source |
| --- | --- | --- | --- |
| Fee rate, 2026 | 1.5% of the retail sales price | Each CBE product sold or leased for use in California; from 1 January 2026 | [CDTFA L-1000](https://cdtfa.ca.gov/formspubs/l1000.pdf) |
| Maximum per product, 2026 | USD 15 | same | same; [CDTFA L-1026](https://cdtfa.ca.gov/formspubs/l1026.pdf) |
| Fee rate, 2027 | 1.5% | From 1 January 2027 to 31 December 2027 | [CDTFA L-1047](https://cdtfa.ca.gov/formspubs/l1047.pdf) |
| Maximum per product, 2027 | USD 1 | same; products priced at USD 66.67 or more pay the flat USD 1 | same |
| Retailer reimbursement | up to 3% of the fee | Kept for collection costs; the return computes it | [PRC 42464(d)](https://www.cdtfa.ca.gov/lawguides/vol4/cewrf/cewrf-42464.html); [CDTFA L-1026](https://cdtfa.ca.gov/formspubs/l1026.pdf) |
| Return due date | last day of the month after each quarter | Weekends and state holidays move it to the next business day; a zero return is required for a quarter with no sales | [CDTFA L-1000](https://cdtfa.ca.gov/formspubs/l1000.pdf); [CDTFA L-1026](https://cdtfa.ca.gov/formspubs/l1026.pdf) |
| Records | at least 4 years from when the fee is due | Unless CDTFA authorizes earlier destruction in writing | [CDTFA Industry Topics](https://cdtfa.ca.gov/taxes-and-fees/covered-electronic-waste-recycling-fee/industry-topics.htm) |
| Late return or payment | 10% of amount due; interest applies to late payments for each month or fraction of a month | Late return or late payment; see the CBE filing instructions and RTC section 55042 | [CDTFA CBE return instructions](https://cdtfa.ca.gov/online-filing-instructions/Covered-Battery-Embedded-CBE-Waste-Recycling-Fee-Return.htm) |

### Steps

1. **Is it a CBE product?** It contains a battery that is not designed to be easily removed by the user with no more than commonly used household tools ([PRC 42463(f)(1)](https://www.cdtfa.ca.gov/lawguides/vol4/cewrf/cewrf-42463.html)). Excluded: certain medical devices (21 USC 321(h)), covered electronic devices that carry the eWaste fee, energy storage systems (Pub. Util. Code 2835(a)) and electronic nicotine delivery systems (15 USC 375(7)) ([PRC 42463(f)(2)](https://www.cdtfa.ca.gov/lawguides/vol4/cewrf/cewrf-42463.html)). A battery that can be taken out by hand without tools does not make a CBE product, and power banks count as loose batteries ([CalRecycle Q&A](https://www2.calrecycle.ca.gov/Docs/Web/137908)).
2. **Who decides.** The manufacturer decides whether its product is a CBE product; the CDTFA does not. A product missing from CalRecycle's lists still owes the fee if it meets the definition, and a retailer never told by the manufacturer must still charge it ([CDTFA Industry Topics](https://cdtfa.ca.gov/taxes-and-fees/covered-electronic-waste-recycling-fee/industry-topics.htm); [CalRecycle Q&A](https://www2.calrecycle.ca.gov/Docs/Web/137908)).
3. **Laptops and tablets.** A covered video display device with an embedded battery pays the eWaste fee only, not both fees ([CalRecycle Q&A](https://www2.calrecycle.ca.gov/Docs/Web/137908)).
4. **Is the sale subject to the fee?** It applies to the retail sale or lease of a new or refurbished CBE product. It does not apply to sales for resale, sales to Native Americans on Indian country, or products shipped directly to a location outside California where the sale is not subject to California sales or use tax; if the buyer takes possession in California, the fee applies ([CDTFA L-1000](https://cdtfa.ca.gov/formspubs/l1000.pdf)). Sales to the federal government are not exempt unless otherwise exempt ([CDTFA Industry Topics](https://cdtfa.ca.gov/taxes-and-fees/covered-electronic-waste-recycling-fee/industry-topics.htm)).
5. **Determine bundle treatment, then compute the fee per product.** For a manufacturer-packaged bundle containing a covered video display device (VDD) and a CBE product, the VDD fee generally applies; if the retailer itemizes the devices separately on the invoice, both fees may apply. For a retailer-created bundle containing a VDD and CBE product, apply the VDD fee to the VDD and the CBE fee to the CBE portion using its unbundled or fair retail selling price. For a CBE product packaged with a non-CBE item, calculate the CBE fee on the unbundled or fair retail selling price of the CBE portion ([CalRecycle bundle decision tree](https://calrecycle.ca.gov/electronics/embeddedbatteries/noticeguide/)). Then compute each CBE fee as the lower of 1.5% of its applicable retail sales price and the cap for the year of sale (USD 15 in 2026, USD 1 in 2027). Example from the CDTFA: an USD 800 product carries USD 12.00 in 2026, and a USD 2,000 product is capped at USD 15.00 ([CDTFA L-1026](https://cdtfa.ca.gov/formspubs/l1026.pdf)).
6. **Show it on the receipt,** as a separate line ([PRC 42464(f)](https://www.cdtfa.ca.gov/lawguides/vol4/cewrf/cewrf-42464.html)). A retailer may instead pay the fee itself and say so on the receipt; then the retailer is liable and the customer is not ([CDTFA Industry Topics](https://cdtfa.ca.gov/taxes-and-fees/covered-electronic-waste-recycling-fee/industry-topics.htm)).
7. **Keep it out of sales tax.** The fee is not part of the measure of sales or use tax ([CDTFA Industry Topics](https://cdtfa.ca.gov/taxes-and-fees/covered-electronic-waste-recycling-fee/industry-topics.htm)). Compute sales tax on the price only.
8. **File quarterly.** On the CBE return through CDTFA online services, separate from the sales and use tax return and any eWaste return; report sales by registered retail location; keep up to 3%; pay the rest ([CDTFA L-1026](https://cdtfa.ca.gov/formspubs/l1026.pdf)). A fee collected in excess must be refunded to the customer, or reported and paid to the CDTFA.

## Boundary and exception table

| Situation | Treatment | Source |
| --- | --- | --- |
| Lease | The lessor collects from the lessee, measured by rental payments; a lease renewal is not subject to the fee unless a new or refurbished product is provided | [CDTFA Industry Topics](https://cdtfa.ca.gov/taxes-and-fees/covered-electronic-waste-recycling-fee/industry-topics.htm) |
| Retailer-lessor buys from a registered vendor | The retailer may pay the fee to the vendor instead of collecting it; the vendor needs a valid seller's permit and must state the fee separately on its invoice, and then owes the fee to the state | [PRC 42464(e)](https://www.cdtfa.ca.gov/lawguides/vol4/cewrf/cewrf-42464.html) |
| Marketplace sale | A registered marketplace facilitator is treated as the retailer for fee purposes | [CalRecycle Q&A](https://www2.calrecycle.ca.gov/Docs/Web/137908) |
| Out-of-state seller with no CBE account sells to a California customer | The customer pays the fee directly to the CDTFA | [CDTFA Industry Topics](https://cdtfa.ca.gov/taxes-and-fees/covered-electronic-waste-recycling-fee/industry-topics.htm) |
| Bundle transaction | Treatment depends on whether the bundle is manufacturer-packaged, retailer-created, or combines a CBE product with a non-CBE item; use the appropriate component price and do not assume the CBE fee applies to the entire bundle | [CalRecycle bundle decision tree](https://calrecycle.ca.gov/electronics/embeddedbatteries/noticeguide/) |
| Full refund of the product | Refund the fee too; a credit is claimed if the fee was reported on an earlier return, the refund was given in the same reporting period, and returns were filed on time | [CDTFA Industry Topics](https://cdtfa.ca.gov/taxes-and-fees/covered-electronic-waste-recycling-fee/industry-topics.htm) |
| Customer never pays (bad debt) | No exemption or credit for bad debts | same |
| Retailer takes a CBE product out of inventory for its own use | The retailer registers and pays the fee as a consumer | [CDTFA L-1000](https://cdtfa.ca.gov/formspubs/l1000.pdf) |

**AUDIT FLASH POINT** The product test turns on the manufacturer's design, not on a list. A retailer that skips the fee because a product is not on a CalRecycle list, or because the manufacturer never said, is still liable for it.

## Worked cases

Both cases are made up for illustration; the rates come from CDTFA L-1026 and L-1047.

**Case 1: the same three products in 2026 and in 2027.** A retailer sells a USD 40 fitness band, an USD 800 phone and a USD 2,000 camera, each a CBE product, once in June 2026 and again in January 2027.

- 2026: band USD 0.60 (1.5% of 40); phone USD 12.00; camera USD 15.00 (USD 30.00 capped). Total USD 27.60.
- 2027: band USD 0.60 (under USD 66.67, so 1.5% still applies); phone USD 1.00; camera USD 1.00. Total USD 2.60.
- The maximum 3% reimbursement on these totals is USD 0.828 in 2026 and USD 0.078 in 2027 before any currency rounding; the official sources read do not specify how the online return rounds fractional-cent amounts.

```oa-check
name: CBE fee per product, 2026 cap USD 15 against 2027 cap USD 1
inputs:
  band: 40
  phone: 800
  camera: 2000
steps:
  - band_2026: min(band * 0.015, 15)
  - phone_2026: min(phone * 0.015, 15)
  - camera_2026: min(camera * 0.015, 15)
  - total_2026: band_2026 + phone_2026 + camera_2026
  - band_2027: min(band * 0.015, 1)
  - phone_2027: min(phone * 0.015, 1)
  - camera_2027: min(camera * 0.015, 1)
  - total_2027: band_2027 + phone_2027 + camera_2027
expected:
  band_2026: 0.60
  phone_2026: 12.00
  camera_2026: 15.00
  total_2026: 27.60
  band_2027: 0.60
  phone_2027: 1.00
  camera_2027: 1.00
  total_2027: 2.60
```

**Case 2: one quarter's return, Q1 2027.** A store sells 400 phones at USD 800 and 1,000 fitness bands at USD 40 in January to March 2027, all in California and all CBE products. It also sells a laptop (a video display device, so eWaste fee only). Sales tax is figured on the prices alone.

- Fees collected: 400 x USD 1.00 + 1,000 x USD 0.60 = USD 1,000.00.
- Assuming the retailer takes the full 3% reimbursement: USD 30.00. Paid to the CDTFA: USD 970.00, due 30 April 2027.
- The laptop adds nothing to this return.

```oa-check
name: Q1 2027 CBE return with 3% reimbursement
inputs:
  phones: 400
  phone_price: 800
  bands: 1000
  band_price: 40
  cap_2027: 1
steps:
  - phone_fee: min(phone_price * 0.015, cap_2027)
  - band_fee: min(band_price * 0.015, cap_2027)
  - fees_collected: phones * phone_fee + bands * band_fee
  - reimbursement: fees_collected * 0.03
  - remit: fees_collected - reimbursement
expected:
  phone_fee: 1.00
  band_fee: 0.60
  fees_collected: 1000.00
  reimbursement: 30.00
  remit: 970.00
```

## When to refuse or refer

- Whether a particular product is a CBE product: refer to the manufacturer, as the CDTFA and CalRecycle say; do not decide it from a product photo.
- Medical devices, energy storage systems and vaping devices near the exclusion lines: refer.
- Manufacturer duties (labelling, notices to retailers, collection programs): refer to CalRecycle.
- Unpaid past quarters or a CDTFA notice: refer to a California practitioner.

## Filing and payment

- Register for a CBE fee account through CDTFA online services; out-of-state retailers with no California location call 1-800-400-7115 ([CDTFA L-1026](https://cdtfa.ca.gov/formspubs/l1026.pdf)).
- File and pay electronically each quarter by the last day of the following month; for 2027: 30 April, 31 July, 31 October and 31 January 2028, moved to the next business day where one falls on a weekend or holiday. File a zero return for a quarter with no sales.
- A late return or late payment incurs a 10% penalty on the amount due for the period; interest applies to late payments for each month or fraction of a month ([CDTFA CBE return instructions](https://cdtfa.ca.gov/online-filing-instructions/Covered-Battery-Embedded-CBE-Waste-Recycling-Fee-Return.htm); RTC section 55042).
- The CBE account is separate from the seller's permit and from any eWaste account.

## Completion checklist

- [ ] Each battery product classified with the manufacturer's determination on file.
- [ ] Video display devices routed to the eWaste fee, not this fee.
- [ ] Point of sale charges 1.5% with the right cap for the sale date (USD 15 in 2026, USD 1 from 1 January 2027).
- [ ] Fee on its own receipt line and excluded from sales tax.
- [ ] Resale, out-of-state shipment and Indian country sales excluded with records.
- [ ] Quarterly return filed by the last day of the next month, 3% kept, records held for 4 years.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Public Resources Code 42463 (CDTFA law guide). Read for (f)(1) the CBE product definition, (f)(2) the exclusions, and the definitions of retailer, retail sale and vendor. | https://www.cdtfa.ca.gov/lawguides/vol4/cewrf/cewrf-42463.html | 2026-11-21 |
| Public Resources Code 42464 (CDTFA law guide). Read for (b) the consumer's fee and CalRecycle rate-setting by 1 October, (c) collection, (d) the 3% reimbursement, (e) retailer or vendor paying for the consumer, (f) separate statement and (h) the review by 1 August 2027. | https://www.cdtfa.ca.gov/lawguides/vol4/cewrf/cewrf-42464.html | 2026-11-21 |
| CDTFA Special Notice L-1000, Registering for a CBE Waste Recycling Fee Account (October 2025). Read for the 1.5% rate, the USD 15 cap, who registers, quarterly returns and the non-subject sales. | https://cdtfa.ca.gov/formspubs/l1000.pdf | 2026-11-21 |
| CDTFA Special Notice L-1026, New CBE Waste Recycling Fee Return (April 2026). Read for filing, due dates, the zero return, the USD 800 and USD 2,000 examples, the 3% and excess collections. | https://cdtfa.ca.gov/formspubs/l1026.pdf | 2026-11-21 |
| CDTFA Special Notice L-1047, Changes to the CBE Waste Recycling Fee Rate Effective January 1, 2027 (November 2026). Read for the 1.5% rate, the USD 1 cap and CalRecycle's 1 October rate-setting (14 CCR 18660.40(d)). | https://cdtfa.ca.gov/formspubs/l1047.pdf | 2026-11-21 |
| CDTFA, Covered Electronic Waste Recycling Fees Guide, Industry Topics. Read for imposition, retailer paying for the customer, the sales tax exclusion, leases, internet sales, refunds, bad debts, federal government sales, out-of-state shipments and the 4-year record rule. | https://cdtfa.ca.gov/taxes-and-fees/covered-electronic-waste-recycling-fee/industry-topics.htm | 2026-11-21 |
| CDTFA, Covered Battery-Embedded Waste Recycling Fee Return, online filing instructions. Read for who files (retailers and lessors, any channel), the 10% late return/payment penalty, and interest on late payments. | https://cdtfa.ca.gov/online-filing-instructions/Covered-Battery-Embedded-CBE-Waste-Recycling-Fee-Return.htm | 2026-11-22 |
| CalRecycle, Guidance for Manufacturers and Retailers, VDD and CBEP classification and fee decision tree. Read for manufacturer-packaged bundles, retailer-created bundles, and CBE products packaged with non-CBE items. | https://calrecycle.ca.gov/electronics/embeddedbatteries/noticeguide/ | 2026-11-22 |
| CalRecycle, Q&A for Covered Battery-Embedded Products (updated 15 May 2026). Read for laptops and tablets (eWaste fee only), manufacturer determinations, tool-free removable batteries, power banks, refurbished products and marketplace facilitators. | https://www2.calrecycle.ca.gov/Docs/Web/137908 | 2026-11-21 |

Not yet confirmed: which date determines the cap for a transaction initiated in 2026 but completed in 2027 (the official pages read do not resolve this); how the online return rounds fractional-cent amounts for the optional 3% reimbursement; or how unusual bundle arrangements outside CalRecycle’s decision tree should be treated. Follow the applicable statute and regulations and seek written CDTFA guidance where needed.
