---
name: north-macedonia-vat
description: "Use this skill for North Macedonia value added tax, DDV, for calendar year 2026. Trigger on Macedonian VAT registration, DDV-04, input VAT, reverse charge, exports, imported services, foreign supplier representative or VAT deregistration. It covers ordinary taxable persons, the registration turnover test, standard and reduced statutory rates, place of supply, output and input tax, blocked input tax, mixed use, capital-asset corrections, filing periods, payments and refunds. It explains the current post-2024 service-location rules and foreign-person registration distinction. Product classification and special schemes require the specific current decisions. This is a tier 2 skill, checked against the law, for working-paper preparation, with two recomputing controls and no licensed accountant’s sign-off."
jurisdiction: MK
tax_year: 2026
last_updated: 2026-10-30
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
version: 2.1
category: international
---

# North Macedonia VAT v2.1

**Tax year: 2026. Checked against the law, tier 2.** Amounts are MKD unless stated otherwise. Professional review remains outstanding.

## Who this applies to

[VAT Law arts. 2 and 9][vat] cover independent economic activity and taxable domestic supplies for consideration; imports are separately taxable. Registered persons calculate output less deductible input tax. Resident small persons below the registration condition do not charge VAT or deduct input tax unless registered voluntarily (art. 51(3)-(4)). The domestic registration threshold is not an import exemption.

Foreign persons without a local seat/branch making taxable local supplies use art. 9-b registration and a representative, except supplies governed by recipient reverse charge under art. 32(4). The foreign-person threshold exception is explicit in art. 9-b(2). This skill covers ordinary business VAT; tourist, margin, investment-gold, state-aid, donor and other special schemes require their specific provisions.

## Rates, bands and thresholds

| Item | Amount | Tax year | Official provision |
|---|---|---|---|
| Standard rate | 18% | 2026 | [VAT arts. 28-29][vat] |
| Reduced rate | 5% for specified art. 30 supplies | 2026 | [VAT art. 30][vat], with current classification decisions |
| Intermediate rate | 10% for art. 30-a food/beverage service and specified other food products | 2026 | [VAT art. 30-a][vat] |
| Resident mandatory registration | Total annual turnover exceeding 2,000,000 | 2026 | [VAT art. 51(1)-(2)][vat] |
| Quarterly period | Prior-year turnover not exceeding 25,000,000; otherwise monthly | 2026 | [VAT art. 39(1)][vat] |
| Normal minimum registration | 3 calendar years, subject to statutory exceptions | 2026 | [VAT art. 51(8)-(14)][vat] |
| Capital-input correction period | 5 years; real estate 10 years | 2026 | [VAT art. 37][vat] |
| Return/payment | Within 25 days after period-end | 2026 | [VAT arts. 41, 43][vat] |
| Requested excess-input refund | 30 days after return, subject to taxpayer-caused control delay and debt setoff | 2026 | [VAT art. 45][vat] |
| Late-filing surcharge | Up to 10% of the tax assessed by law | 2026 | [Tax Procedure Law art. 55][procedure] |
| Late interest | 0.03% per day | 2026 | [Tax Procedure Law arts. 3, 123, 180][procedure]; VAT art. 44 is expressly inoperative |

**Art. 30(1)-(2) 5% list (summary):** basic foodstuffs; drinking water from public systems and irrigation water; books, e-textbooks, newspapers and periodicals (not mainly advertising); seeds, fertilisers, plant protection, agricultural film and machinery; medicines, including veterinary; menstrual products; computers and their software; solar thermal systems; disability aids for personal use; crude oil for food production; first supply of housing within five years of construction; animal feed and live animals; listed baby products; listed school supplies; pellets, pellet stoves and boilers; heat energy for heating; passenger transport; public cleaning and waste removal; accommodation; and listed repairs and hairdressing by registered craftspeople. **Art. 30-a 10%:** serving food and drink for consumption on the premises and catering (alcoholic drinks excluded), and food products that are not basic foodstuffs.

**Art. 23 exemptions without deduction (summary):** housing supplies other than a first supply within five years, residential lettings, postage stamps and Macedonian Post postal services, banking and financial transactions, insurance and reinsurance, games of chance, specified non-profit cultural, broadcasting, health, social-care, childcare, medical-profession, patient-transport, blood/organ, education and research, funeral services, international passenger transport and road tolls/fees, each on its statutory conditions.

A rate is applied only after mapping the product/service to the statute and operative classification decision. No blanket 5% rate for all food, electricity or residential property is asserted. Historical electricity art. 30-b only applied in its dated 2023 period; crisis rates under art. 30-v require an operative government decision.

## The base

**Supplies and tax point:** arts. 16-22 use the consideration excluding VAT, including directly related consideration, incidental charges and applicable taxes other than VAT. Discounts/returns/bad-debt circumstances require the statutory base/invoice correction and corresponding input adjustment, not a unilateral reduction in the bank receipt. Special own-use, related-party and in-kind supplies use art. 19's prescribed valuation. Art. 22 import base starts with customs value plus customs duties, other import charges and incidental costs to the statutory destination, excluding the VAT itself.

Art. 31 generally triggers VAT when goods are supplied/dispatch begins or services are completed; advance payments trigger VAT to the extent received. Periodic supplies use invoice date or earlier receipt. Imports follow the customs-charge/release event. Record the tax point separately from cash-book classification.

**Place of supply:** goods use art. 13's location/dispatch/installation rules. Use the **current art. 14 effective since 1 January 2024**, not the superseded version retained earlier in the consolidation. General B2B services follow the business recipient's seat/receiving branch; general B2C services follow the supplier. Art. 14(4)-(6) overrides for property, transport, admission/events, catering, vehicle hire and listed B2C intangible/consulting/electronic services. A customer abroad alone does not establish an export of a locally situated property service.

**Output less input:** separate taxable, exempt-with-deduction and exempt-without-deduction supplies. Domestic exemptions without input deduction are listed in art. 23 (including specified health, education, financial and property transactions with their conditions). Exports and other art. 24 supplies are exempt **with** deduction; keep art. 26 customs/export evidence. Do not describe every exempt invoice as zero-rated with deduction.

Arts. 33-34 require business use, a compliant VAT invoice or qualifying fiscal receipt/import declaration and accounting entry before input deduction. Art. 34 allows a fiscal receipt only within its **6,000 total-turnover** limit. Input tax on reverse-charged services requires the correct taxable-business/deduction basis; reverse charging does not automatically grant deduction.

Art. 35 blocks input on exempt-without-deduction activities, specified passenger vehicles and related fuel/maintenance/rental, entertainment, administrative furnishings listed there, passenger transport, hotels and meals, subject to the stated vehicle-business and film-production exceptions. A business purpose alone does not override a specific block. For mixed taxable/exempt activities, allocate only the part attributable to deduction-entitled supplies under art. 36; retain the allocation evidence and make the final annual adjustment required by art. 40(3).

Under art. 37, changed use of investment assets adjusts input by **one fifth** annually, or **one tenth for real estate**, within the respective five-/ten-year period. Disposal or own-use conversion can require correction of the remaining period. Ordinary excess input is a refund/carryforward under art. 45, not an income-tax loss. Maintain output, input, credit-note, import and reverse-charge reconciliations under arts. 52-56.

## Deadlines and filing

**Resident registration:** art. 51 includes taxable turnover plus VAT, excluding exempt-without-deduction turnover; annualise actual turnover for a partial operating year. Test prior-year total, predicted total at start and actual crossing during the year. Prior-year threshold/voluntary registration application: **15 January**. Starting a qualifying activity: **within 15 days of commencement**. Crossing during the year: **by the 15th of the following month**, with registration after the crossing month under art. 51(7). Use the UJP registration application and its registration decision; do not wait until annual accounts.

**Deregistration:** after the normal three-calendar-year period, request removal where third-year turnover does not exceed the threshold; application by **15 January of the year removal is sought**. Art. 51(14) provides an earlier requested removal route for each of the two preceding years below threshold with no input deduction in either. Other art. 51(9)-(10) removal conditions remain separate. Submit a final return and settle stock/asset implications; a stopped business is not excused from final VAT.

**Foreign suppliers:** art. 9-b requires registration **before** taxable local supply and one qualifying tax representative, without the resident 2 million threshold. Recipient reverse-charge supplies are excluded from that representative obligation. Preserve supply and recipient-status evidence.

**Returns/payments:** file DDV-04 electronically for the UJP-assigned monthly/quarterly period by the **25th day after period-end**, including nil returns (arts. 39-41). Pay by the same deadline (art. 43). Cessation return is within **25 days after the calendar month of cessation**, even for a quarterly filer (art. 41(4)). Assessment debt is due within **15 days after service** (art. 43(3)). Import VAT follows customs payment (art. 43(5)-(9)).

For excess input, elect refund on the return or carry forward as an advance. Art. 45 sets the 30-day refund period, delays where the taxpayer prevents inspection, and setoff against other tax/interest debts. Reconcile to the UJP ledger and retain submission and payment evidence. The prescribed electronic filing form is available through UJP; bank account movement alone does not establish VAT turnover or deduction.

## Penalties and interest

[VAT arts. 59-60][vat] cover late/non-registration, missing returns, incorrect records, defective invoices and failures to retain evidence. Legal-person ranges: micro **EUR 300-1,000**, small **600-2,000**, medium **1,800-6,000**, large **3,000-10,000**, in MKD equivalent. Responsible-person ranges are respectively **EUR 50-250**, **100-500**, **150-500**, **200-500**; sole traders/self-employed **EUR 100-250**, ordinary individuals **EUR 50-250** for the listed offences. UJP can assess absent/inaccurate returns under art. 42.

A late return can also carry a separate late-filing surcharge of up to **10%** of the tax ([Tax Procedure Law art. 55][procedure]). Use [Tax Procedure Law art. 123][procedure] for **0.03% daily** interest from the day after maturity. The consolidation still prints historical VAT art. 44's 0.05%, but expressly notes that it ceased under Tax Procedure Law art. 180 from 1 April 2006. It is not a current alternative rate.

## Cross-border points

Art. 32(4) makes the qualifying local recipient liable for local supplies from a supplier without seat/branch; file/pay even where the recipient does not have ordinary input-deduction rights. Foreign-representative supplies follow arts. 9-b and 32(6). Domestic construction/scrap and specified enforcement transfers can use art. 32-a reverse charge between qualifying registered persons; confirm the transaction and implementing classification first.

Exports require physical/customs evidence under arts. 24 and 26. Imported goods follow customs VAT. Cross-border services use the operative art. 14, not EU membership assumptions or a universal foreign-customer exemption. Income-tax treaty relief does not remove VAT obligations.

## Two worked examples that recompute

**Simple: domestic standard-rated business.** Net sales 1,000,000 produce 180,000 output VAT. Fully deductible standard-rated purchases 400,000 produce 72,000 input VAT. DDV-04 payable is 108,000 (arts. 29, 33-35, 40).

```oa-check
name: MK 2026 ordinary VAT period
inputs:
  sales: 1000000
  purchases: 400000
steps:
  - output_tax: sales * 0.18
  - input_tax: purchases * 0.18
  - payable: output_tax - input_tax
expected:
  output_tax: 180000
  input_tax: 72000
  payable: 108000
```

**Edge: imported service with restricted deduction.** A local business receives 100,000 of standard-rated imported B2B services subject to art. 32(4), wholly attributable to activities with an evidenced 60% deduction allocation. It accounts for 18,000 output tax, deducts 10,800, and bears 7,200 net. This is an assumed substantiated allocation under art. 36, not a statutory 60% safe harbour.

```oa-check
name: MK 2026 reverse charge restricted deduction
inputs:
  service: 100000
  deductible_fraction: 0.60
steps:
  - reverse_output: service * 0.18
  - deductible_input: reverse_output * deductible_fraction
  - payable: reverse_output - deductible_input
expected:
  reverse_output: 18000
  deductible_input: 10800
  payable: 7200
```

## Ask the client first

- What are current/prior-year turnover, commencement date and UJP registration/period decisions?
- What goods/services, supply dates and current classification decisions apply?
- Where are supplier, recipient and any receiving branch, and what is the recipient's business status?
- Which invoices/import evidence support deductions, and are inputs blocked or mixed-use?
- Are exports, asset changes, credit notes, cessation or refund claims involved?

## Sources

| Official source | URL | Read on |
|---|---|---|
| VAT Law, consolidated through Gazette 267/2025 | https://www.ujp.gov.mk/files/attachment/0000/0986/______________________________________.____________267____30.12.2025.pdf | 2026-10-24; 2026-10-30 (web.archive.org copy, UJP site offline) |
| Tax Procedure Law, through Gazette 3/2025 | https://www.ujp.gov.mk/files/attachment/0000/0900/_________________________.pdf | 2026-10-24; 2026-10-30 (web.archive.org copy, UJP site offline) |

[vat]: https://www.ujp.gov.mk/files/attachment/0000/0986/______________________________________.____________267____30.12.2025.pdf
[procedure]: https://www.ujp.gov.mk/files/attachment/0000/0900/_________________________.pdf

Not yet confirmed: None within the stated scope.

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
