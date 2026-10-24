---
name: sy-consumption-tax-jewellery-vehicles
description: >
  Syria consumption-expenditure tax collection for jewellery, precious-metal articles and passenger vehicles under June 2026 instructions. Covers final-consumer invoices, returned goods, first registration, engine bands and documented imported-component credits. Research draft with worked examples; not comprehensive import or country coverage.
jurisdiction: SY
category: international
tax_year: 2026
tier: 2
last_updated: 2026-10-23
version: 0.1
verified_by: pending
sources:
  - url: "https://docs.mof.gov.sy/consumption_tax_on_imports_table.pdf"
    title: "Finance Ministry Decision 938/Q.W, 29 June 2026, instructions and Table 3"
    as_of: "2026-10-23"
  - url: "https://sana.sy/economy/2515968/"
    title: "SANA: ministry announcement linking the official PDF"
    as_of: "2026-10-22"
---

# Syria: jewellery and vehicle consumption-tax collection

## Scope

Finance Ministry Decision 938/Q.W of 29 June 2026 contains special collection rules for these goods. Read instruction pages 6–8 alongside Table 3 on page 233 of the [official PDF](https://docs.mof.gov.sy/consumption_tax_on_imports_table.pdf). Jewellery is collected on final-consumer sales; covered passenger vehicles are collected at first registration. Neither should simply inherit the producer-sale collection rule used for other domestic goods.

This Guide reports the recovered instructions, not a complete consolidated tax code. The underlying legislation, later changes, territorial implementation, import restrictions and other customs/registration charges remain separate checks. Monetary instruction amounts are in new Syrian pounds (XXII, p.19); older instructions listed in XXIV, p.20 are superseded. Arabic controls.

## Jewellery and precious-metal articles

Instruction III, pp.6–7 and Table 3, p.233 distinguish:

| Category | Rate and qualification |
|---|---|
| Plain gold jewellery, gold manufactures and the stated other precious-metal manufactures | 1%, without additions under this rule |
| Jewellery such as gem-set gold, pearls, precious stones and diamonds | 5%, plus applicable statutory additions |
| Tableware and parts made from gold, silver or precious metals | 20%, plus applicable statutory additions |
| Watches and parts made from gold, silver or precious metals/platinum, within the stated chapter 91 category | 20%, plus applicable statutory additions |

Do not apply the plain-gold rate to gem-set jewellery merely because it contains gold. Statutory additions for the latter categories have not been quantified here; their base levy is not the total amount due.

For the specified plain-gold/precious-metal category, the final-consumer invoice base includes metal value, additions and making charges through manufacture and preparation for final sale, including workshop charges and wholesale/retail margins. It is not a levy on making charges alone. A person in the jewellery trade who makes a final-consumer sale becomes responsible for collection/remittance from the invoice date. The instructions treat the relevant income-tax registrants who sell to final consumers as registered with the consumption-tax office. Workshops and wholesalers/half-wholesalers issue invoices for their own stage, but those non-final-consumer invoices do not bear this final-consumer levy (p.6).

Each transaction needs an invoice or contract. The prescribed invoice format uses two identical sequentially numbered copies, commercial name and tax number, and the electronic-linkage QR identifier on each copy. Jewellery-association stamping applies; a taxpayer producing printed invoices through accounting software with the required linkage QR code is exempted from that stamping requirement. Do not interpret this as an exemption from invoicing (p.7).

The instructions allow sales returns within tax-administration limits, requiring the invoice counterfoil to record the returned item's type, weight and fineness, plus the customer's full name, national number and telephone. They nevertheless state **the consumption levy is not refunded, regardless of the reason for return** (p.6). This differs from the air-ticket refund provision; do not copy that refund treatment into jewellery.

Gold hallmarking and the QR label have separate controls: the label remains with the item until sale and is removed before final weighing/invoicing. Association and workshop records support quantity and payment checks. Confirm the operative technical instructions before implementing a point-of-sale system (p.7). [Instructions, pp.6–7; Table 3, p.233](https://docs.mof.gov.sy/consumption_tax_on_imports_table.pdf).

## Passenger vehicles: category, rate and collection point

Table 3, p.233 gives the following rates for the specified private passenger-vehicle category, excluding government vehicles. Confirm classification, propulsion and engine capacity from the vehicle documents:

| Category | Rate |
|---|---|
| Engine capacity not exceeding 1,600 cc | 10% |
| Above 1,600 cc and not exceeding 3,000 cc | 20% |
| Above 3,000 cc | 60% |
| Electric passenger vehicles | 5% |
| Hybrid passenger vehicles | 5% |

These are rates on the relevant value, not marginal tax bands. Electric/hybrid categories are separately specified; do not add an engine-band rate to the electric/hybrid rate.

For imported passenger vehicles, instruction p.8 collects the levy **once, on first registration** in the private category at the transport directorate. Government vehicles are excluded under this provision. The base is the invoice or sale-contract value for the buyer in whose name the vehicle is registered. This is not an annual levy or permission to treat customs taxes as paid.

For domestically manufactured passenger vehicles, the same first-registration/invoice-or-contract basis applies, with a deduction for consumption levy paid to Customs on imported components. Pay the remaining difference to the transport directorate. The deduction requires original receipts proving final payment to the General Authority for Ports and Customs; the assessment and customs/final receipts are copied to the tax administration for audit and final settlement. Do not treat ordinary customs duty, an estimate, an unpaid assessment or an unrelated import receipt as this credit. The instructions retrieved do not establish a refund or carryforward when claimed component levy exceeds the vehicle levy (p.8). [Instructions, p.8; Table 3, p.233](https://docs.mof.gov.sy/consumption_tax_on_imports_table.pdf).

## Filing and records

Jewellery sellers must preserve the final-consumer and preceding-stage invoice trail, returned-item details, hallmarking records and levy-payment evidence. The common declaration/payment provision V(d), p.10 requires the previous month's taxable sales declaration and payment within the first 10 days of the following month. Jewellery p.7 permits payment to the finance directorate's bank accounts through bank transfer, certified cheque or electronic payment; verify current account details directly.

Vehicle first-registration collection is the specific rule above; do not replace it with a wait-until-next-month payment instruction. Keep registration classification, engine/propulsion evidence, invoice or contract, assessment and original eligible component receipts together. Common records, exemptions and foreign-currency provisions are addressed in the [services Guide](sy-consumption-tax-services.md), with unresolved implementation points disclosed. [Instructions, pp.7–10, 16–19](https://docs.mof.gov.sy/consumption_tax_on_imports_table.pdf).

## Example 1: plain gold includes making charges

Assume a confirmed 1% category final-consumer sale: metal value 100,000 new pounds and making charges/margins 10,000. The base is 110,000 and the levy 1,100, not 100 on the making charges alone. A later qualifying goods return does not produce a levy refund under the stated jewellery rule.

```oa-check
name: Syria plain gold full invoice base and return
inputs:
  metal: 100000
  making_and_margins: 10000
  rate: 0.01
  permitted_levy_refund: 0
steps:
  - base: metal + making_and_margins
  - levy: base * rate
  - retained_levy: levy - permitted_levy_refund
expected:
  base: 110000
  levy: 1100
  retained_levy: 1100
```

## Example 2: vehicle engine boundary

Assume two non-electric, non-hybrid private passenger vehicles each have a confirmed registration base of 1,000,000 new pounds. At exactly 1,600 cc, levy is 100,000. At 1,601 cc, levy is 200,000 on the full base. These examples exclude other vehicle/import charges.

```oa-check
name: Syria passenger vehicle 1600 cc boundary
inputs:
  base: 1000000
  rate_at_1600: 0.10
  rate_at_1601: 0.20
steps:
  - levy_at_1600: base * rate_at_1600
  - levy_at_1601: base * rate_at_1601
expected:
  levy_at_1600: 100000
  levy_at_1601: 200000
```

## Example 3: local vehicle with documented component levy

Assume a qualifying locally manufactured vehicle has a 2,000,000 new-pound registration base and a confirmed 20% rate. Gross levy is 400,000. Original receipts establish 60,000 of eligible, finally paid consumption levy on its imported components. The difference payable at registration is 340,000, subject to the required audit/settlement. No general VAT input-credit mechanism is inferred.

```oa-check
name: Syria locally manufactured vehicle component levy deduction
inputs:
  registration_base: 2000000
  rate: 0.20
  eligible_component_levy_paid: 60000
steps:
  - gross_levy: registration_base * rate
  - difference_payable: gross_levy - eligible_component_levy_paid
expected:
  gross_levy: 400000
  difference_payable: 340000
```

## Gaps and sources

Unresolved: statutory additions on the 5%/20% jewellery categories, technical invoicing/hallmarking instructions, complete legislative history and later amendments, operational forms/accounts, territorial administration, other import/registration charges and negative vehicle-credit outcomes. No complete goods, imports or country coverage is claimed.

- [Finance Ministry Decision 938/Q.W and Table 3](https://docs.mof.gov.sy/consumption_tax_on_imports_table.pdf), especially pp.6–8, 10, 19–20 and 233.
- [SANA announcement with the official PDF link](https://sana.sy/economy/2515968/).

## Disclaimer

Source-cited research draft, not professionally attested. Establish the applicable law, period, location and transaction facts before collection, filing or payment.
