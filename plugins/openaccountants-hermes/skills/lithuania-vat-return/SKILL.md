---
name: lithuania-vat-return
description: "Use this skill for Lithuanian VAT (pridėtinės vertės mokestis, PVM) in tax year 2026. It covers the 21% standard rate, the 12% and 5% reduced rates and the end of the 9% rate on 31 December 2025 (heating, firewood, books, accommodation, transport and culture moved), the EUR 45,000 small business scheme and when VAT starts once it is passed, the EU cross-border small business scheme, the EUR 14,000 acquisitions threshold, tax periods, the FR0600 return and payment by the 25th, i.SAF invoice data by the 20th, the EU sales list (FR0564), reverse charge on services and goods from foreign suppliers and on construction work, blocked input VAT on representation and cars, fines and 0.027% a day late payment interest. Trigger on: Lithuanian VAT, PVM, FR0600, i.SAF, PVM mokėtojas, Lithuania VAT registration, 12% PVM. Out of scope: corporate income tax (lt-corporate-income-tax), personal income tax (lithuania-pit), payroll (lt-payroll-social), cross-border income tax (lt-cross-border)."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/lithuania-vat-return"
  jurisdiction: "LT"
  tax_year: "2026"
  last_updated: "2026-10-24"
  trust_label: "Built by Michael Cutajar and the OpenAccountants team"
  review_status: "pending_review"
---

# Lithuania: VAT (2026) v2.2

This skill sets out who must charge Lithuanian VAT (pridėtinės vertės mokestis, PVM), at what rate, and how to file and pay it for 2026. The law is the Law on VAT No. IX-751 (Pridėtinės vertės mokesčio įstatymas, PVMĮ), in its consolidated version in force from 1 July 2026 to 31 December 2026. Art. 19 (rates) is the same in the version in force from 1 January 2026: its last changes are laws XV-287 and XV-366 of June 2025. Fines and late payment interest come from the Law on Tax Administration No. IX-2112 (Mokesčių administravimo įstatymas, MAĮ). The tax authority is the State Tax Inspectorate (VMI).

The biggest change for 2026: the 9% reduced rate ended on 31 December 2025. From 1 January 2026, accommodation, scheduled passenger transport and culture admissions are at 12%, books are at 5%, and heating, hot water and firewood for homes are no longer on a reduced rate.

## Who this applies to

- **Taxable persons supplying in Lithuania.** Anyone who supplies goods or services in Lithuania must register and charge VAT (PVMĮ art. 71(1)), unless the small business scheme applies or the only supplies are ones where the buyer accounts for the VAT under art. 95(2) to (4).
- **Small business scheme (smulkiojo verslo schema).** A Lithuanian taxable person need not register or charge VAT if its domestic supplies were not above **EUR 45,000** in the previous calendar year and are not expected to pass it in the current year (art. 71(2)). A new business qualifies if it does not expect to pass EUR 45,000 in its first year.
- **Related companies are counted together.** Where one person (alone or with related persons) controls several legal persons, all of them, and that person if it carries on economic activity, must register once their combined supplies pass the limit, even if each one is below it. This does not apply if they prove that no member of their management bodies is the same person and that their activities are not of the same kind and they do not act in each other's interest (art. 71(7)).
- **Cross-border services trigger registration below EUR 45,000.** A business that buys services from a foreign supplier for which it must account for the VAT under art. 95(2) (for example advertising from Google or Facebook, or platform fees from Booking or Bolt), or that supplies B2B services taxed in another member state, must register for VAT whatever its turnover (art. 71-1(2)). It can still stay on the small business scheme while its Lithuanian supplies are within EUR 45,000 (VMI answer KM3566).
- **Businesses from other EU states.** A business established in another member state can use the Lithuanian small business scheme if its Lithuanian supplies stay within EUR 45,000 and its total EU supplies were not above **EUR 100,000** in the previous year (art. 71(2-1)). It registers for this through its home state.
- **Buyers of goods from other EU states.** A flat-rate farmer, a business whose activity gives no right to deduct VAT, or a legal person that is not a taxable person, if not registered, must register once goods bought from other member states pass **EUR 14,000** in a calendar year (art. 71-1(1) and (3)). New vehicles and excise goods are left out of the count.
- **Non-EU businesses.** A business established outside the EU, or with only a branch in some member state, registers through its Lithuanian branch, or if it has none, through a fiscal agent in Lithuania (art. 71(3)).
- **Not registering does not remove the tax.** A person who should have registered must still compute and pay the VAT (art. 71(4)).

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| Standard rate | 21% | 2026 | https://www.e-tar.lt/portal/lt/legalAct/TAR.ED68997709F5/asr (art. 2(32), 19(1)) |
| Reduced rate: accommodation under tourism law; scheduled passenger transport and baggage; admission to arts and culture venues and events | 12% (9% until 31 Dec 2025) | 2026 | https://www.e-tar.lt/portal/lt/legalAct/TAR.ED68997709F5/asr (art. 19(3)); https://www.vmi.lt/evmi/lengvatinis-9-proc.-pvm-tarifas-19-str.- |
| Reduced rate: reimbursed medicines and medical aids, prescription medicines; technical aids for disabled people and their repair; newspapers and periodicals; printed and e-books and non-periodical information publications | 5% (books 9% until 31 Dec 2025) | 2026 | https://www.e-tar.lt/portal/lt/legalAct/TAR.ED68997709F5/asr (art. 19(4)) |
| Heating energy and hot water for homes; firewood for households | Not on any reduced rate in art. 19 from 1 Jan 2026, so 21% (9% until 31 Dec 2025) | 2026 | https://www.vmi.lt/evmi/lengvatinis-9-proc.-pvm-tarifas-19-str.- |
| Zero rate: exports, intra-EU supplies of goods and other chapter VI cases | 0% | 2026 | https://www.e-tar.lt/portal/lt/legalAct/TAR.ED68997709F5/asr (art. 19(5)) |
| Small business scheme limit (domestic supplies) | EUR 45,000 a year | 2026 | https://www.e-tar.lt/portal/lt/legalAct/TAR.ED68997709F5/asr (art. 71(2)) |
| EU small business scheme: EU-wide limit | EUR 100,000 a year | 2026 | https://www.e-tar.lt/portal/lt/legalAct/TAR.ED68997709F5/asr (art. 71(2-1)) |
| Acquisitions from other EU states, registration threshold | EUR 14,000 a year | 2026 | https://www.e-tar.lt/portal/lt/legalAct/TAR.ED68997709F5/asr (art. 71-1) |
| Quarterly returns allowed (not for individuals) | Income up to EUR 300,000 in the previous year | 2026 | https://www.e-tar.lt/portal/lt/legalAct/TAR.ED68997709F5/asr (art. 84(2)) |
| Representation: input VAT not deductible | 50% where the cost is a representation cost for profit tax; 100% where it is not | 2026 | https://www.e-tar.lt/portal/lt/legalAct/TAR.ED68997709F5/asr (art. 62(2)(1)) |
| Electric M1 car: input VAT block does not apply | Value up to EUR 50,000 including VAT | 2026 | https://www.e-tar.lt/portal/lt/legalAct/TAR.ED68997709F5/asr (art. 62(2)(3)) |
| Late payment interest | 0.027% a day from 1 Aug 2026 | 2026 | https://www.vmi.lt/evmi/delspinigiai-baudos-ir-atleidimas-nuo-ju-96-100-str.-138-143-str.- |

## The taxable base

- **What is taxed.** Supplies of goods and services in Lithuania for consideration, acquisitions of goods from other member states and imports (PVMĮ art. 3). Exempt supplies (chapter IV, art. 20 to 40) carry no VAT and give no right to deduct.
- **Which rate.** 21% unless art. 19 names a lower rate. The 12% list in art. 19(3) has three items only: accommodation provided under tourism law, passenger transport on regular routes set by the Ministry of Transport or municipalities (with baggage), and admission to arts and culture venues and events. Restaurant and catering services are at 21%; their 9% rate ended on 31 December 2023 (VMI).
- **Books.** The 5% rate covers printed and electronic books and non-periodical information publications, including textbooks, maps and sheet music, but not calendars or notebooks, and not publications more than 4/5 advertising or mainly music or video (art. 19(4)(4)).
- **Input VAT.** VAT on purchases used for taxable (or zero-rated) supplies is deductible (art. 57 and 58). Mixed use is apportioned (art. 59).
- **Blocked input VAT (art. 62(2)).**
  - Representation: 50% of the VAT is not deductible where the cost counts as representation for profit tax; all of it is blocked where it does not.
  - Passenger cars for up to 8 passengers plus the driver, and off-road vehicles, and their hire: not deductible unless the car is resold, leased out or used for paid passenger transport. M1 electric cars worth up to EUR 50,000 including VAT, and special-purpose vehicles, are not blocked.
  - Taxi-type passenger transport in such cars: not deductible unless the buyer acts as an undisclosed agent.
- **Small business scheme.** Under the scheme no VAT is charged and none is deducted. When domestic supplies pass EUR 45,000, VAT is charged from the month the limit was passed, on the supplies by which it was passed (art. 71(2)).
- **Annual adjustment.** Where the deduction must be adjusted after the year end (chapter VIII), an annual VAT return is due by 1 October of the next year (art. 87(1)).

## Deadlines and filing

- **Registration.** Apply to VMI electronically through My VMI (art. 76). Where registration is compulsory, apply without delay once the obligation arises; VMI decides within 3 working days of receiving the application (VMI answer KM0738). PVMĮ sets no fixed number of days. A voluntary applicant applies at least 3 working days before the date from which it wants to be registered (VMI). VAT is due from the month the EUR 45,000 limit was passed, whether or not registration is complete (art. 71(2) and (4)).
- **Tax period (art. 84).**
  - Default: the calendar month.
  - Quarter: on request, for a VAT payer (other than an individual) whose income from economic activity was not above EUR 300,000 last year, or a new payer expecting to stay under it. A change back is possible only after the quarter ends.
  - Half-year: the default for individuals, unless they ask for monthly periods.
- **Return: FR0600.** Due by the **25th** of the month after a monthly period, or by the 25th of the first month after a quarter or half-year (art. 85(1), (1-1) and (2)). VMI sets the form (art. 86). VMI's i.SAF service prepares a draft FR0600 from invoice data.
- **Payment.** Due by the same date as the return (art. 90(1)).
- **i.SAF invoice data.** VAT payers send the data from their issued and received invoice registers to VMI (art. 78; VMI Order VA-55). Companies send it **every month by the 20th** of the next month, even if their VAT period is a quarter. Individuals send it on their return period: by the 20th of the next month, or by the 20th of the first month of the next half-year. Payers on the small business scheme do not send it (VMI).
- **EU sales list: FR0564.** Payers supplying goods to other member states, or services taxed in another member state under the general B2B rule, file a report by the **25th** of the next month, every month (art. 88-1). Small business scheme payers file it for such services too.
- **Small business scheme payers** registered for VAT file a FR0600 only for periods in which VAT became due or they supplied B2B services to another member state (art. 85(7)).

## Penalties and interest

- **Late payment interest (delspinigiai).** Charged on VAT not paid by the due date, and on VAT found in an audit from the day after the original due date (MAĮ art. 96). The rate is set by the Minister of Finance from the 12-month government securities yield plus 7 points (MAĮ art. 99). From 1 August 2026 it is **0.027% a day** (VMI answer KM2633).
- **Fine on understated VAT.** VAT found understated in a tax audit, or a lower rate wrongly applied, carries a fine of **20% to 100%** of the shortfall (MAĮ art. 139(1)). VMI starts from the midpoint and adjusts for mitigating and aggravating circumstances (art. 140). A repeat breach of the same tax law, where a fine was already imposed within the current and five previous calendar years, doubles it (art. 139(3), 68(4)).
- **Voluntary correction.** No fine if a corrected return is filed before VMI orders an audit (MAĮ art. 139(4)).
- **Relief.** VMI can waive fines and interest in the cases in MAĮ art. 141.
- **Not registering.** The VAT is still due from the month the limit was passed (PVMĮ art. 71(2)), with late payment interest from its due date.

## Cross-border points

- **Services from foreign suppliers (reverse charge).** A taxable buyer in Lithuania accounts for VAT on general-rule B2B services from a supplier not established in Lithuania (art. 95(2)). The buyer declares the output VAT and, if entitled, deducts it on the same return.
- **Goods from foreign suppliers.** A VAT-registered buyer (including one on the small business scheme) accounts for VAT on gas, electricity, heat and cooling, and on goods installed or assembled in Lithuania, supplied by a supplier not established here (art. 95(3)).
- **Domestic reverse charge (art. 96).** The buyer, if a VAT payer, accounts for the VAT on: construction work as defined in the Construction Law; assets received as a capital contribution or on a reorganisation; transfers of major building improvements; and other cases set by the Government. The buyer shows the VAT as payable and deducts it under the normal rules (art. 96(3)).
- **Intra-EU supplies of goods.** Zero-rated under chapter VI with evidence (art. 56); reported on FR0564 (art. 88-1).
- **Acquisitions from other EU states.** Taxed in Lithuania. A non-registered buyer registers once acquisitions pass EUR 14,000 a year (art. 71-1).
- **Non-EU businesses.** Register through a Lithuanian branch or a fiscal agent (art. 71).
- **EU small business scheme.** Lithuanian businesses can use other states' schemes and foreign EU businesses can use Lithuania's, within the EUR 100,000 EU-wide limit (art. 71(2-1), 71-2, 74-1).
- **One-stop shop (OSS) and import one-stop shop.** Special schemes in PVMĮ chapter XII, sections 5 to 7, with their own return dates (art. 115-3, 115-8, 115-13). Not covered in detail here.

## Worked examples

### Example 1: a hotel company's monthly return for October 2026

A UAB runs a hotel and is a monthly VAT payer. In October 2026 it sells EUR 80,000 of room nights and EUR 20,000 of restaurant meals, both net of VAT. It has EUR 6,000 of deductible input VAT on purchases. It also paid EUR 400 of VAT on a client dinner that counts as a representation cost for profit tax.

1. Rooms are accommodation under tourism law: 12% (art. 19(3)(1)). 80,000 x 12% = EUR 9,600. In 2025 this would have been 9%.
2. Restaurant meals are not on any reduced list: 21%. 20,000 x 21% = EUR 4,200.
3. Output VAT: 9,600 + 4,200 = EUR 13,800.
4. Representation: half the VAT is blocked (art. 62(2)(1)), so EUR 200 is deductible.
5. Input VAT: 6,000 + 200 = EUR 6,200.
6. VAT payable: 13,800 - 6,200 = EUR 7,600. The FR0600 and payment are due by 25 November 2026 (art. 85(1), 90(1)). The i.SAF invoice data for October is due by 20 November 2026.

```oa-check
name: Hotel UAB, October 2026 return with the 12% rate and representation
inputs:
  accommodation_sales: 80000
  restaurant_sales: 20000
  input_vat: 6000
  representation_vat: 400
steps:
  - vat_accommodation: accommodation_sales * 12 / 100
  - vat_restaurant: restaurant_sales * 21 / 100
  - output_vat: vat_accommodation + vat_restaurant
  - representation_deductible: representation_vat * 50 / 100
  - total_input: input_vat + representation_deductible
  - vat_payable: output_vat - total_input
expected:
  vat_accommodation: 9600
  vat_restaurant: 4200
  output_vat: 13800
  representation_deductible: 200
  total_input: 6200
  vat_payable: 7600
```

### Example 2: a freelancer passes EUR 45,000 in September 2026

An individual designer in Lithuania had supplies of EUR 38,000 in 2025, so she started 2026 on the small business scheme. By the end of August 2026 her supplies were EUR 41,000. In September she invoices a Lithuanian client EUR 7,000, taking her to EUR 48,000; the contract says the price is net of VAT and the client pays any VAT on top. She registers. From October to December she invoices Lithuanian clients EUR 12,000, net of VAT. In October she also buys EUR 2,000 of design software services from a supplier in Ireland, used fully for her taxable work.

1. Her supplies pass EUR 45,000 in September. VAT is due from September, on the supplies by which the limit was passed: the whole September invoice of EUR 7,000 (art. 71(2)). She must apply to register without delay (VMI answer KM0738). 7,000 x 21% = EUR 1,470.
2. October to December sales: 12,000 x 21% = EUR 2,520.
3. The Irish service: she is a taxable buyer of a B2B service from a supplier not established in Lithuania, so she accounts for the VAT (art. 95(2)). Output 2,000 x 21% = EUR 420. She deducts the same EUR 420.
4. Total output VAT for the period: 1,470 + 2,520 + 420 = EUR 4,410. Input VAT: EUR 420.
5. VAT payable: EUR 3,990.
6. As an individual her tax period is the half-year (art. 84(4)). The FR0600 for July to December 2026 and the payment are due by 25 January 2027. Her i.SAF data for the half-year is due by 20 January 2027.

```oa-check
name: Freelancer crosses EUR 45,000 in September 2026 with a reverse charge service
inputs:
  sales_to_august: 41000
  september_invoice: 7000
  sales_oct_dec: 12000
  irish_service: 2000
  threshold: 45000
steps:
  - total_supplies: sales_to_august + september_invoice + sales_oct_dec
  - over_threshold_in_september: sales_to_august + september_invoice - threshold
  - vat_september: september_invoice * 21 / 100
  - vat_oct_dec: sales_oct_dec * 21 / 100
  - reverse_charge_output: irish_service * 21 / 100
  - reverse_charge_input: reverse_charge_output
  - output_vat: vat_september + vat_oct_dec + reverse_charge_output
  - vat_payable: output_vat - reverse_charge_input
expected:
  total_supplies: 60000
  over_threshold_in_september: 3000
  vat_september: 1470
  vat_oct_dec: 2520
  reverse_charge_output: 420
  output_vat: 4410
  vat_payable: 3990
```

## Ask the client first

1. What were your supplies in Lithuania in 2025, and in 2026 so far, month by month? Did you pass EUR 45,000, and in which month? Do you or your owners control other companies with the same kind of activity?
2. What do you sell, exactly? Accommodation, transport, culture admissions, books, medicines, heating or firewood each need a rate check against the 2026 art. 19 list.
3. Are you a company or an individual, and is your income from economic activity above EUR 300,000? This sets the monthly, quarterly or half-yearly period.
4. Do you buy services or goods from suppliers outside Lithuania, or construction work from Lithuanian contractors?
5. Do you supply goods or services to businesses in other EU states, or sell to consumers there?
6. Do you have client entertainment, passenger cars or mixed exempt and taxable activity?

## Sources

| Source | URL | Read on |
|---|---|---|
| Law on VAT No. IX-751, consolidated version from 1 July 2026 to 31 December 2026: art. 2(32), 19, 62(2), 71, 71-1, 71-2, 74-1, 76, 78, 84, 85, 86, 87(1), 88-1, 90(1), 95, 96 | https://www.e-tar.lt/portal/lt/legalAct/TAR.ED68997709F5/asr | 2026-10-24 |
| VMI, reduced 9% VAT rate, "relevant until 2025-12-31", with the 2026 rates for each item | https://www.vmi.lt/evmi/lengvatinis-9-proc.-pvm-tarifas-19-str.- | 2026-10-24 |
| VMI, i.SAF data submission and correction | https://www.vmi.lt/evmi/duomenu-teikimas-tikslinimas | 2026-10-24 |
| VMI, VAT payers: answers KM0738 (when to apply for registration; decision within 3 working days) and KM3566 (registration when buying services from foreign platforms) | https://www.vmi.lt/evmi/pvm-moketojai | 2026-10-24 |
| VMI, VAT payer registration, deregistration and data changes | https://www.vmi.lt/evmi/pvm-moketojo-registravimas-isregistravimas-duomenu-keitimas | 2026-10-24 |
| Law on Tax Administration No. IX-2112, consolidated version from 1 July 2026: art. 68(4), 96, 99, 139 to 141 | https://www.e-tar.lt/portal/lt/legalAct/TAR.3EB34933E485/asr | 2026-10-24 |
| Law on VAT No. IX-751, list of consolidated versions (2026-01-01, 2026-07-01 and 2027-01-01 versions and the amending laws) | https://www.e-tar.lt/portal/lt/legalActEditions/TAR.ED68997709F5 | 2026-10-24 |
| VMI, late payment interest, answer KM2633 (0.027% a day from 1 August 2026) | https://www.vmi.lt/evmi/delspinigiai-baudos-ir-atleidimas-nuo-ju-96-100-str.-138-143-str.- | 2026-10-24 |

Not yet confirmed: how VAT is computed on a supply that crossed the EUR 45,000 limit where the price was agreed without VAT and cannot be increased (on top of, or within, the price); the rate for accommodation booked and paid in 2025 but supplied in 2026 (VMI answer KM3670, title only read); the late payment interest rate after 31 October 2026 (it is reset each quarter); any administrative fine for filing FR0600, FR0564 or i.SAF late (Code of Administrative Offences, not read); the Government list of extra domestic reverse charge cases under art. 96(1)(4); the exemptions in art. 20 to 40 and the zero-rate evidence rules (not read in detail); the OSS and IOSS rules and the EUR 10,000 distance sales limit; VAT refunds to foreign businesses (art. 116 to 119); and the PVMĮ version in force from 1 January 2027 (law XV-1036 of 18 June 2026 changes art. 78, 88-1 and others from 2027; not read in detail).

> Contributed by Michael Cutajar.

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

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-10-24. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `lithuania-vat-return` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/lithuania-vat-return. If neither is available, confirm every figure against the official source pages cited above before relying on it.
