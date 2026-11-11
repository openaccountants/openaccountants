---
name: sr-vat-gst
description: "Suriname value added tax (Belasting over de Toegevoegde Waarde, BTW) for 2026 under the Wet Belasting over de Toegevoegde Waarde 2022 (S.B. 2022 no. 121) as amended by S.B. 2022 nos. 143 and 148 and S.B. 2023 no. 126, with the Minister's 2023 and 2025 decrees. Covers who must register (the SRD 1,000,000 turnover threshold, voluntary registration, the two-year lock), the 10% general rate, the 5% rate (water, electricity, cooking gas, domestic goods transport), the 25% rate (large or costly cars, motorcycles over 125 cc, boats, small aircraft, weapons, fireworks), the 0% rate (exports, outsourcing for foreign customers, petroleum and gold contractors, public bodies), exemptions, place of supply, reverse charge on services from abroad, input VAT and blocked items, pro rata and revision, invoices, the monthly return and payment before the 16th, refunds, the 2026 late-filing and late-payment penalty table and 6% interest. Trigger on: Suriname VAT, BTW Suriname, btw-aangifte, BTW-plichtig, SRD 1.000.000 omzetgrens, 10% BTW, BTW verlegd, Belastingdienst Suriname. Out of scope: income tax (sr-income-tax, sr-corporate-income-tax), customs duties and excise."
version: 1.0
jurisdiction: SR
tax_year: 2026
last_updated: 2026-11-11
category: international
type: computation
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: vat-gst
---

# Suriname VAT (BTW) for 2026 v1.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

Suriname has charged VAT (BTW) since 1 January 2023, in place of the old turnover tax (omzetbelasting). This skill covers the monthly VAT of a business in 2026: whether it must register, which rate applies, what input VAT it may deduct, and how to file and pay.

**Which text of the law.** The Wet Belasting over de Toegevoegde Waarde 2022 (Wet BTW), S.B. 2022 no. 121 of 12 October 2022, with the correction sheet S.B. 2022 no. 143 and the amending acts S.B. 2022 no. 148 (in force 1 January 2023) and S.B. 2023 no. 126 (5 September 2023; new annex 2 of exemptions from 1 October 2023 and new annex 4 of 5% items from 1 November 2023). The Minister's decree of 13 November 2025 (S.B. 2025 no. 140) still names S.B. 2023 no. 126 as the last amendment, and no later amendment is listed by the Suriname Tax Administration (Belastingdienst Suriname) or De Nationale Assemblée (DNA) as of 11 November 2026. Figures are in Surinamese dollars (SRD).

Linked skills: income tax of individuals in [sr-income-tax](sr-income-tax.md); companies in [sr-corporate-income-tax](sr-corporate-income-tax.md); an overview in [sr-tax-overview](sr-tax-overview.md).

## Who this applies to

- **Taxable persons (ondernemers).** Anyone who independently carries on a business or profession in Suriname; anyone who exploits an asset for lasting income; public bodies the Minister designates (Wet BTW art. 1(1)(f)). VAT is charged on supplies of goods and services in Suriname by a business acting as such, for consideration, and on imports (art. 2).
- **Small businesses below the threshold.** A business living or established in Suriname whose taxable turnover, excluding VAT, is SRD 1,000,000 or less in a calendar year has no VAT duties and no VAT rights, in particular no right to deduct input VAT (art. 21(1)). All its activities count together (art. 21(3)). Exempt turnover (annex 2) does not count towards the threshold; 0%, 5%, 10% and 25% turnover, including exports, does (Tax Administration VAT page).
- **Fiscal unity.** Businesses resident or with a permanent establishment in Suriname that are financially, organisationally and economically intertwined can be treated as one business by the inspector's decision, from the first day of the following month (art. 1(1)(f)(4°)). This does not carry over to wage tax.
- **Foreign suppliers.** A business with no residence or permanent establishment in Suriname that supplies a Surinamese business does not charge VAT; the customer pays it under reverse charge (art. 11(2)).
- **Out of scope:** customs duties and excise; casinos and lotteries; the petroleum and gold-mining 0% regimes beyond the pointer below (they turn on contracts); the cash-accounting scheme the Minister may set (art. 24); a VAT ledger kept in a foreign currency (art. 36).

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| General rate on supplies of goods, services and imports (Wet BTW art. 4(1)) | 10% | 2026 | https://belastingdienst.sr/wp-content/uploads/2026/01/BTWS.B.-2022-no.-121-WET-BTW-2022.pdf |
| Reduced rate, annex 4 as replaced from 1 November 2023 (art. 4(3); S.B. 2023 no. 126 art. I.D and art. 68(8)): water supplied by a state enterprise or government service for household use only, and other water in packs of at least 5 gallons; electricity and related services, and cooking gas; domestic transport of goods by road, water and air | 5% | 2026 | https://belastingdienst.sr/wp-content/uploads/2026/01/BTWS.B.-2023-no.-126-nadere-wijziging-WET-BTW-5-September-2023.pdf |
| Motor petrol and diesel: on the 5% list of S.B. 2022 no. 148 until 31 October 2023, not on the new annex 4 from 1 November 2023, so the general rate applies | 10% | 2026 | same |
| Increased rate, annex 3 (art. 4(4)): passenger cars and other motor vehicles mainly for passengers over 2,500 cm3 or with a CIF value of USD 40,000 or more, except electric vehicles (S.B. 2023 no. 126 art. I.C) | 25% | 2026 | same |
| Increased rate, annex 3 continued: motorcycles over 125 cm3 (S.B. 2022 no. 148 art. I.N) | 25% | 2026 | https://belastingdienst.sr/wp-content/uploads/2026/01/BTWS.B.-2022-no.-148-nadere-wijziging-WET-BTW-30-december-2022.pdf |
| Increased rate, annex 3 continued: speedboats, jet skis, yachts, sport and pleasure craft; helicopters and aircraft for fewer than 10 persons; weapons, ammunition and parts; fireworks | 25% | 2026 | https://belastingdienst.sr/wp-content/uploads/2026/01/BTWS.B.-2022-no.-121-WET-BTW-2022.pdf |
| Zero rate (art. 4(2)(b) to (e), as amended): goods that are exported (only the exporter's own supply); international carriage of goods by aircraft and sea-going ships; services in Suriname on outgoing goods; outsourcing work done in Suriname for a customer not resident or established in Suriname | 0% | 2026 | same |
| Zero rate, annex 1 as replaced by S.B. 2023 no. 126: imports by and supplies and services to contractors and subcontractors and state enterprises under the Petroleumwet 1990 (except the blocked items of art. 14(6)); to gold-mining companies under agreements with the force of law; and to public bodies | 0% | 2026 | https://belastingdienst.sr/wp-content/uploads/2026/01/BTWS.B.-2023-no.-126-nadere-wijziging-WET-BTW-5-September-2023.pdf |
| Registration threshold: taxable turnover excluding VAT in a calendar year (art. 21(1), (2)); register at once when exceeded | More than SRD 1,000,000 | 2026 | https://belastingdienst.sr/wp-content/uploads/2026/01/BTWS.B.-2022-no.-121-WET-BTW-2022.pdf |
| Telecommunications, broadcasting and electronic services to non-business customers: place of supply is where the customer lives if gross fees in the current year exceed the threshold and it was not exceeded in the previous year (art. 9(8)); the Minister may change the threshold | More than SRD 500,000 a year | 2026 | same |
| Refund below which the inspector may order offset in a later period (art. 17(4)) | Less than SRD 1,000 | 2026 | same |
| Late-payment interest (art. 13(5); S.B. 2023 no. 32) | 6% a year on VAT not paid or paid late | 2026 | https://belastingdienst.sr/wp-content/uploads/2026/01/BTWS.B.-2023-no.-32-Beschikking-vaststelling-interest-bij-late-betaling.pdf |
| Late-filing penalty per return period (art. 37; S.B. 2025 no. 140 part II), applied from 1 January 2026; months late rounded up; also for nil and refund returns | SRD 2,500 for 1 month late, 5,000 for 2, 7,500 for 3, 10,000 from 4 months | 2026 | https://belastingdienst.sr/wp-content/uploads/2026/01/BTWS.B.-2025-no.-140-BESCHIKKING-boetebeleid-verzuim-boeten.pdf |
| Late-payment penalty (art. 38; S.B. 2025 no. 140 part III); none if the late return shows nil or a refund | 50% of the amount unpaid at the deadline, at most SRD 10,000 | 2026 | same |
| Penalty for intent or gross negligence (art. 39) | 5% to 100% of the VAT not paid on time | 2026 | https://belastingdienst.sr/wp-content/uploads/2026/01/BTWS.B.-2022-no.-121-WET-BTW-2022.pdf |
| Record keeping (art. 30(2)) | 10 years | 2026 | same |

## The base

**1. Is there a taxable supply in Suriname?**
- Goods: the place where transport starts, or where the goods are when supplied (art. 8(1)); goods sent from abroad and imported by the supplier are supplied in Suriname (art. 8(2)). Supplies include transfer of ownership, hire purchase, delivery of made goods, and the creation or transfer of rights over real estate (art. 6). Taking goods out of the business for private use is a supply if input VAT was deducted on them (art. 6(3)); small gifts and samples are not (art. 6(6)).
- Services to a business: where the customer has its seat or the permanent establishment served (art. 9(1)). Services to a non-business customer: where the supplier is established (art. 9(3)). Exceptions: real estate services and hotel accommodation where the property is; passenger and goods transport where people board or goods are loaded (art. 9(2)(b) and (4)(b) as amended by S.B. 2022 no. 148); events, restaurants and catering where they take place; short hire of transport (up to 30 days, 90 for ships) where it is made available; outsourcing work where it is done; and for royalties and licences, advertising, consultancy, legal and accounting work, data processing, financial and insurance services, staff hire, hire of movable goods, telecommunications, broadcasting and electronic services: where the customer is established or lives (art. 9(7)).
- Imports: VAT on the customs value plus import duty, excise and other import levies, collected by Customs (arts. 18 and 19).

**2. Which rate or exemption?** Check annex 3 (25%), annex 4 (5%), the 0% cases in art. 4(2) and annex 1, then the exemptions in annex 2 as replaced from 1 October 2023 (S.B. 2023 no. 126 art. I.B): casino gaming; medical, dental and paramedical services; non-profit social, cultural, charitable, sporting and religious bodies (unless competition is seriously distorted); domestic passenger transport by road and water; hospitals and medical laboratories; medical aids and appliances; medicines as listed by the Ministry of Health; local health insurance and life insurance; education by recognised bodies under the Ministry of Education, with teaching materials, school supplies and uniforms; childcare; care of the elderly and needy; ambulance transport; listed financial services (currency exchange, cheques and similar digital transactions, debt securities, shares, credit and credit broking, derivatives); fresh vegetables, fresh chicken, fresh unprocessed fish, eggs, flour, bread and cassava bread, rice, paddy, milk, soy oil, matches, contraceptives, disposable nappies, bath soap and toilet paper; domestic supply of gold to licensed gold buyers and fresh fish to licensed processors and exporters; domestic sale of works of art; animal feed and its raw materials, insecticides, fertilisers, pesticides and seeds. Anything not listed is 10%. The 0% rate for residential lettings of at least three months ended on 1 November 2023 (S.B. 2023 no. 126 art. I.G); real estate is not on the 2023 exemption list.

**3. The taxable amount** is the total charged for the supply excluding VAT (art. 10(1), (2)); between connected parties, at least market value where the customer cannot fully deduct (art. 10(5)). Foreign-currency amounts convert at the Central Bank of Suriname's last selling rate when VAT becomes due (art. 10(8)). Prices offered must include VAT (art. 10(9)).

**4. When VAT is due:** on the invoice date, or when the invoice should have been issued; otherwise on supply; and in any case when payment is received, in whole or part (art. 12).

**5. Input VAT (arts. 3 and 14 to 16).** Deduct VAT charged on a proper invoice in the period, VAT paid on imports (with the import document), and reverse-charge VAT, so far as the purchases are used for taxed supplies, including supplies abroad that would be taxed in Suriname (art. 14(1) to (3)). **Blocked, whatever the use (art. 14(6)):** food, drink and tobacco; business gifts; pay in kind and staff recreation; passenger motor vehicles and goods and services relating to them, except for car dealers, leasing companies and vehicles over 3,500 kg maximum mass. **Mixed use:** deduct in the ratio of taxed turnover to taxed plus exempt turnover (art. 15(1)(c)), on a provisional ratio for the year corrected in the last return of the year; no correction after the first year if the difference is 10% or less (art. 16(2)). Real estate is revised over the nine following years by tenths, depreciable movable assets over the four following years by fifths, unless the difference in a year is 10% or less (art. 15(3) to (5)).

**6. Other adjustments.** Transfer of a going concern is not a supply; the buyer steps into the seller's place (art. 22). VAT on unpaid, reduced or cancelled amounts is refunded on request in the return for the period the right arose; a customer who has not paid one year after the amount fell due must repay the input VAT deducted (art. 23).

**7. Threshold crossings.** A small business that goes over SRD 1,000,000 in a year pays VAT on the part of its turnover above SRD 1,000,000, and cannot use the small-business exemption for its whole turnover in the next two calendar years (art. 21(4)). A business may opt in below the threshold with the inspector's consent, and then stays in for the next two calendar years (art. 21(6)); a business that fell below may ask to leave for the next year (art. 21(5)). The inspector decides within 30 days (art. 21(7)).

## Deadlines and filing

| Step | When | Law |
|---|---|---|
| Register in the online portal (portaal.belastingdienst.sr/OPO): Chamber of Commerce (KKF) extract, contract or licence, ID for a sole trader, an email address not used for another registration; an SRD bank account for refunds is advised | At once on exceeding SRD 1,000,000 | Wet BTW art. 21(2); Tax Administration registration page and brochure |
| Monthly return (the return period is a calendar month), filed in the portal; a nil return is still required | From the 1st, and before the 16th day of the following month (by 15 February 2027 for January 2027, by 15 January 2027 for December 2026) | Arts. 1(1)(h), 13(2); Tax Administration notice of December 2025 |
| Payment, with the 18-digit payment reference (betalingskenmerk) the portal gives after filing | By the same date as the return | Art. 13(4) |
| Invoice to a business customer, and for advance payments | Within 15 days after the end of the month of supply; for an advance, before it falls due | Art. 27(1), (3) |
| Correct a filed return in the portal (Corrigeer Aangifte) | Up to the 15th; later only by objection to bezwaren@belastingdienst.sr | Tax Administration BTW-aangifte page and brochure |
| Refund of excess input VAT | Within one month of the right arising, which is the 16th of the month after the period (for a late return, the day after filing); the inspector may suspend for up to two months with written reasons | Art. 17(2), (3); S.B. 2025 no. 60 |

**Return boxes.** In rubrics 1a to 3d enter turnover separately for each rate; do not add amounts together or enter only the VAT due. Enter whole SRD only, rounded down, with no commas or points; enter 0 everywhere in a month with nothing to report. Click Voltooien to file; a confirmation email follows (Tax Administration BTW-aangifte page). The brochure's period computation follows this order: domestic supplies at 5%, 10%, 25% and 0%; exempt supplies; private use; exports of goods and services at 0%; reverse-charge purchases from abroad at 5%, 10% and 25% and services from abroad at 10% (total A); less deductible domestic input VAT and import VAT (total B); A minus B, plus or minus corrections of earlier periods, gives the amount to pay or reclaim.

**Invoices (art. 28)** show: date; sequential number; the supplier's and the customer's tax identification numbers (FIN); names and addresses; quantity and nature of goods or services; date of supply; amount by rate or exemption and unit price excluding VAT; the rate; the VAT; any exemption; for motor vehicles make, model, cylinder capacity and chassis number (and number plate for work on a vehicle); and "BTW verlegd" where the customer pays under reverse charge. A business selling to consumers may use a cash register whose receipts show the applied rate (art. 27(7) as amended). Records are kept in Dutch for 10 years (art. 30).

**Refund conditions (S.B. 2025 no. 60 part III).** No refund unless the business is registered, has filed and paid on time in earlier periods, and has filed correct returns over the last 12 periods.

## Penalties and interest

- **Late or missing return (art. 37; S.B. 2025 no. 140).** Up to SRD 10,000 per return period. From 1 January 2026 the Tax Administration applies the table: SRD 2,500 for each month or part month late, rising to SRD 10,000 from four months; a return five days late counts as one month. Nil and refund returns filed late are fined too.
- **Late or missing payment (art. 38; S.B. 2025 no. 140).** 50% of the VAT unpaid at the deadline, at most SRD 10,000; nothing if the late return shows nil or a refund.
- **No return at all.** The inspector issues an estimated assessment with both penalties at the maximum; filing the return as an objection leads to reconsideration under the table, and the payment penalty falls to nil if nothing was payable (S.B. 2025 no. 140 part IV).
- **Intent or gross negligence (art. 39).** 5% to 100% of the VAT not paid on time; not imposed if the business pays before it knows or should suspect the Tax Administration is aware (art. 45).
- **Interest.** 6% a year on VAT not paid on time (art. 13(5); S.B. 2023 no. 32). The business is owed interest if a refund is late (art. 17(6)).
- **Top-up assessments (naheffing).** Possible for five years after the end of the year, ten years for intent or gross negligence (art. 25(2), (3)); more than one per period if new facts appear (art. 25(8), added by S.B. 2023 no. 126).
- **Criminal fines** for false returns and fraud run to SRD 50,000 or more (arts. 58 to 61); refer.

## Cross-border points

- **Imports** are taxed at Customs on the customs value plus duties (art. 19); the business deducts the import VAT in its return with the import document (art. 14(1)(b)(1°)). Import reverse charge (art. 11(3)) needs a staatsbesluit, which could not come into force before 1 January 2024 (art. 11(4)); whether one is in force was not found.
- **Services and goods bought from a foreign supplier** with no Surinamese establishment by a Surinamese business: the customer accounts for the VAT in its own return and deducts it if used for taxed supplies (arts. 11(2), 14(1)(b)(2°)). The supplier's invoice should not show Surinamese VAT; the customer's return shows it under services or goods from abroad.
- **Exports** of goods are 0% only for the exporter's own supply; earlier supplies in the chain are taxed normally (art. 4(2)(b) as amended; explanatory memorandum to S.B. 2022 no. 148). Keep export documents.
- **Foreign businesses supplying consumers** are not covered by a separate registration scheme in the act. Telecommunications, broadcasting and electronic services to consumers follow the place-of-supply rule of art. 9(7) and the SRD 500,000 test of art. 9(8); the text of art. 9(8) is unclear, so refer before advising a foreign digital supplier.
- **Embassies and international relations:** the Minister may exempt supplies on conditions, for embassies on a reciprocal basis (art. 5(2) as amended).

## Two worked examples that recompute

**Example 1: monthly return of a registered trader, March 2026.** Domestic sales at 10%: SRD 900,000. Sales of motorcycles over 125 cm3 at 25%: SRD 200,000. Exports: SRD 100,000 at 0%. A foreign consultancy without a Surinamese establishment invoiced SRD 50,000 (reverse charge at 10%). Domestic purchase invoices carry SRD 60,000 of VAT, of which SRD 2,000 is on client lunches (blocked). Import VAT paid to Customs: SRD 30,000.

Output (total A): 10% of 900,000 = 90,000; 25% of 200,000 = 50,000; exports 0; reverse charge 10% of 50,000 = 5,000; total SRD 145,000. Input (total B): 60,000 - 2,000 = 58,000; import 30,000; reverse charge 5,000; total SRD 93,000. Pay SRD 52,000 with the return, before 16 April 2026.

```oa-check
name: Suriname monthly VAT return, March 2026
inputs:
  sales_10: 900000
  sales_25: 200000
  exports: 100000
  foreign_service: 50000
  input_domestic: 60000
  blocked: 2000
  import_vat: 30000
steps:
  - out_10: sales_10 * 0.10
  - out_25: sales_25 * 0.25
  - out_rc: foreign_service * 0.10
  - total_a: out_10 + out_25 + exports * 0 + out_rc
  - total_b: input_domestic - blocked + import_vat + out_rc
  - payable: total_a - total_b
expected:
  total_a: 145000.00
  total_b: 93000.00
  payable: 52000.00
```

**Example 2 (decision): opt in below the threshold, or stay out?** A business with taxable turnover of SRD 800,000 (below SRD 1,000,000) buys SRD 400,000 of supplies carrying 10% VAT (SRD 40,000). It can ask the inspector to apply the VAT rules (art. 21(6)), but then stays in for two more calendar years. The figure that decides is who its customers are.

- **Business customers, who can deduct VAT.** Staying out, the SRD 40,000 input VAT is a cost. Opting in, it charges 10% on top (SRD 80,000, which its customers deduct) and recovers the SRD 40,000. It is SRD 40,000 a year better off: opt in.
- **Consumers, at fixed VAT-inclusive prices of SRD 800,000.** Opting in, the output VAT inside the price is 800,000 × 10 / 110 = SRD 72,727.27, less SRD 40,000 recovered: SRD 32,727.27 a year worse off. Stay out.

```oa-check
name: Suriname voluntary VAT registration below SRD 1,000,000, both ways
inputs:
  turnover: 800000
  purchases: 400000
steps:
  - input_vat: purchases * 0.10
  - b2b_gain: input_vat
  - b2c_output: turnover * 10 / 110
  - b2c_gain: input_vat - b2c_output
expected:
  input_vat: 40000.00
  b2b_gain: 40000.00
  b2c_output: 72727.27
  b2c_gain: -32727.27
```

## Ask the client first

1. What was the business's taxable turnover (excluding VAT and exempt sales) in 2025, and what is expected for 2026? Above SRD 1,000,000 it must be registered.
2. What does it sell, and to whom? Check each line against annexes 1 to 4 (0%, exempt, 25%, 5%) and whether customers are businesses or consumers.
3. Does it buy services or goods from foreign suppliers with no Surinamese establishment? Those are reverse-charged.
4. Does it make exempt supplies as well as taxed ones? Then the pro rata and the revision rules apply.
5. Does it import or export goods, and does it keep the customs documents?
6. Is it part of a group that should be, or already is, a fiscal unity?

## Sources

| Source | URL | Read on |
|---|---|---|
| Wet BTW 2022, S.B. 2022 no. 121: read arts. 1 to 47 (definitions, rates, exemptions, place of supply, base, reverse charge, return, deduction, pro rata, refunds, threshold, invoices, records, penalties) and annexes 1 to 3 | https://belastingdienst.sr/wp-content/uploads/2026/01/BTWS.B.-2022-no.-121-WET-BTW-2022.pdf | 2026-11-11 |
| Correction sheet S.B. 2022 no. 143: read in full (art. 4(3) wording) | https://belastingdienst.sr/wp-content/uploads/2026/01/BTWS.B.-2022-no.-143-VERBETERBLAD-op-het-S.B.-2022-no.-121-WET-BTW.pdf | 2026-11-11 |
| Amending act S.B. 2022 no. 148: read in full (5% rate and annex 4, 25% annex 3, art. 9 transport, art. 11(4), art. 27(7), annexes 1 and 2, memorandum) | https://belastingdienst.sr/wp-content/uploads/2026/01/BTWS.B.-2022-no.-148-nadere-wijziging-WET-BTW-30-december-2022.pdf | 2026-11-11 |
| Amending act S.B. 2023 no. 126 (scanned; read in full by text recognition): new annexes 1, 2 and 4, annex 3 item a, art. 25(8), art. 68(8) and (9) dates, memorandum | https://belastingdienst.sr/wp-content/uploads/2026/01/BTWS.B.-2023-no.-126-nadere-wijziging-WET-BTW-5-September-2023.pdf | 2026-11-11 |
| Decree S.B. 2023 no. 32 on interest for late payment: read in full (6% a year) | https://belastingdienst.sr/wp-content/uploads/2026/01/BTWS.B.-2023-no.-32-Beschikking-vaststelling-interest-bij-late-betaling.pdf | 2026-11-11 |
| Decree S.B. 2025 no. 60 on VAT refunds: read in full (when the right arises, suspension, refund conditions) | https://belastingdienst.sr/wp-content/uploads/2026/01/BTWS.B.-2025-no.-60-Beschikking-Teruggaaf-BTW-art-17-lid-8.pdf | 2026-11-11 |
| Decree S.B. 2025 no. 140 on penalties for late returns and payments: read in full (tables, estimated assessments, last amendment S.B. 2023 no. 126) | https://belastingdienst.sr/wp-content/uploads/2026/01/BTWS.B.-2025-no.-140-BESCHIKKING-boetebeleid-verzuim-boeten.pdf | 2026-11-11 |
| Tax Administration, BTW page: read for the rates, the SRD 1,000,000 test and what counts as turnover, filing and payment dates, payment reference | https://belastingdienst.sr/belastingen/btw/ | 2026-11-11 |
| Tax Administration, BTW-aangifte page: read in full (whole amounts, rubrics 1a to 3d, nil returns, corrections to the 15th, filing and paying before the 16th) | https://belastingdienst.sr/btw-aangifte/ | 2026-11-11 |
| Tax Administration, notice "Maandelijkse aangifte BTW en verzuimboeten" (December 2025): read in full (file and pay by the 15th; penalty policy from 1 January 2026) | https://belastingdienst.sr/maandelijkse-aangifte-btw-en-verzuimboeten/ | 2026-11-11 |
| Tax Administration, brochure on the VAT law in outline (version 28 April 2025): read in full for registration, invoicing, the return layout and payment | https://belastingdienst.sr/wp-content/uploads/2025/06/Brochure-met-een-beschrijving-van-de-BTW-wetgeving-op-hoofdlijnen-2025.pdf | 2026-11-11 |
| Tax Administration, VAT registration page: read for the documents needed | https://belastingdienst.sr/belastingen/btw/registreren/ | 2026-11-11 |

Not yet confirmed: the box-by-box numbering of the portal return beyond "rubrics 1a to 3d by rate" (the model return annexed to S.B. 2023 no. 31 is not published as text); whether a staatsbesluit under art. 11(3) applies import reverse charge in 2026; the Minister's specification lists for annexes 2 and 3 (S.B. 2024 nos. 7 and 12, S.B. 2025 no. 128), not read item by item; any 2026 change in fuel taxation (the old version said fuel moved to 10% on 1 July 2024; the law read shows fuel leaving the 5% list on 1 November 2023, and no act or decree dated 1 July 2024 was found); how art. 9(8) applies to foreign suppliers of electronic services (the old version's "SRD 500,000 non-resident registration threshold" is not in the act as a registration rule); the Minister's maximum value for small gifts and samples (art. 6(7)).
