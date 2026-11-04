---
name: latvia-vat-return
description: "Latvian value added tax (pievienotās vērtības nodoklis, PVN) for tax year 2026 under the VAT Law (Pievienotās vērtības nodokļa likums) as in force from 1 January 2026. Covers who must register (EUR 50,000 domestic threshold, the EUR 5,000 tolerance, the EUR 10,000 limit for EU acquisitions), the EU small-enterprise scheme (EUR 100,000 EU turnover), the 21%, 12% and 5% rates and what sits at each, including bread, milk, poultry and eggs at 12% from 1 July 2026 to 30 June 2027, input VAT limits for cars and entertainment, the domestic reverse charges, monthly and quarterly periods, the return by the 20th and payment by the 23rd, the EU sales list, structured e-invoices, late-filing fines and 0.05% a day late interest. Trigger on: Latvia VAT, PVN deklarācija, PVN return, register for VAT in Latvia. Out of scope: corporate income tax (lv-corporate-income-tax), individuals (latvia-income-tax), payroll (latvia-payroll), cross-border hub (lv-cross-border)."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/latvia-vat-return"
  jurisdiction: "LV"
  tax_year: "2026"
  last_updated: "2026-10-24"
  trust_label: "Built by Michael Cutajar and the OpenAccountants team"
  review_status: "pending_review"
---

# Latvia: VAT (PVN) for 2026

Latvia charges VAT under the VAT Law of 29 November 2012. The version used here is the one in force from 1 January 2026; no later version had been published by 16 October 2026. The standard rate is 21%. Reduced rates are 12% and 5%. A registered business files a return for each month or quarter within 20 days after the period and pays within 23 days (VAT Law arts. 41, 118(1), 119(1)). The State Revenue Service (Valsts ieņēmumu dienests, VID) runs VAT through its Electronic Declaration System (EDS).

Load this skill with `eu-vat-directive` for the EU rules and `vat-workflow-base` for the return workflow.

## Who this applies to

- **Taxable persons** carrying on economic activity in Latvia: companies, sole traders, permanent establishments, other legal arrangements (VAT Law arts. 3, 4).
- **Domestic businesses under EUR 50,000.** A domestic taxpayer need not register while its domestic supplies in the calendar year, net of VAT, stay at or below EUR 50,000 (art. 59(1)). The count includes taxable supplies and the exempt insurance, financial, fund management, real estate sale, residential letting and statutory land-use supplies in art. 52(1)(20), (21), (22), (24), (25) and (26). Exempt gambling (point 23) is not counted. It leaves out sales of fixed assets and intangibles, and occasional exempt deals unlike the normal business (art. 59(2), (3)).
- **No threshold** for a domestic business that supplies services to a business customer in another EU state under the general B2B rule (art. 59(8)). It must register before doing so.
- **Previous-year rule.** A business that went over EUR 50,000 in the previous calendar year cannot use the threshold this year (art. 59(10)).
- **EU acquisitions.** An unregistered business whose goods bought from other EU states reach EUR 10,000 in a calendar year must apply to register by the 15th of the following month (art. 57(1)).
- **Services bought from abroad.** An unregistered business that receives B2B services taxed in Latvia under art. 19(1) can keep the domestic threshold only by using the special registration in art. 139.2 (art. 59(9), in force from 1 July 2025).
- **Foreign businesses.** An EU business making taxable supplies in Latvia can use the EUR 50,000 threshold only while its EU-wide turnover stayed at or below EUR 100,000 in this and the previous year (art. 61(11), (12)). Non-EU businesses register under arts. 62 and 63.
- **Out:** persons with no economic activity; final consumers. The persons named in art. 3(4) have no duty to register (art. 59(12)).

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| Standard rate | 21% | 2026 | https://likumi.lv/ta/id/253451-pievienotas-vertibas-nodokla-likums (art. 41(1)(1)) |
| Reduced rate: medicines, medical devices for individual use, specialised infant food | 12% | 2026 | same, art. 42(1) to (3) |
| Reduced rate: scheduled domestic passenger transport and baggage | 12% | 2026 | same, art. 42(4) |
| Reduced rate: accommodation in tourist lodgings | 12% | 2026 | same, art. 42(10) |
| Reduced rate: firewood and heat supplied to households | 12% | 2026 | same, art. 42(11), (12) |
| Reduced rate: fresh fruit, berries and vegetables on the Annex 1 list (64 items), washed, peeled, cut or packed but not cooked, frozen, salted or dried | 12% | 2026 | same, art. 42(16)(1), Annex 1 |
| Reduced rate: bread, fresh milk, fresh poultry meat, eggs on the Annex 2 list | 12% from 1 July 2026 to 30 June 2027; 21% before | 2026 | same, art. 42(16)(2), Annex 2, transitional provision 48 |
| Reduced rate: books, printed and electronic, in Latvian, Latgalian, Livonian and listed foreign languages | 5% | 2026 | same, art. 42(5), (8) |
| Reduced rate: newspapers, magazines and other press, printed or electronic, same language rule | 5% | 2026 | same, art. 42(7), (8) |
| Zero rate: exports, intra-EU supplies of goods, listed transport and international services | 0% | 2026 | same, arts. 43 to 50 |
| Domestic registration threshold | EUR 50,000 a calendar year | 2026 | same, art. 59(1) |
| Tolerance before registration must happen in the year | EUR 5,000 over the threshold | 2026 | same, art. 59(4) |
| EU acquisitions registration threshold | EUR 10,000 a calendar year | 2026 | same, art. 57(1) |
| EU small-enterprise scheme, EU-wide turnover ceiling | EUR 100,000 | 2026 | same, arts. 61(12), 139.1(2) |
| Monthly period if taxable supplies exceed | EUR 50,000 in the previous or current year | 2026 | same, art. 115(1)(1) |
| Entertainment input VAT not deductible | 60% | 2026 | same, art. 100(1) |
| Ordinary passenger car input VAT not deductible | 50% | 2026 | same, art. 100(2) |
| Late payment interest | 0.05% of the unpaid tax a day | 2026 | https://likumi.lv/ta/id/33946-par-nodokliem-un-nodevam (art. 29(2)) |
| Fine unit | EUR 5 | 2026 | https://likumi.lv/ta/id/303007-administrativas-atbildibas-likums (art. 16(2)) |

The bread, milk, poultry and eggs rule has limits. UHT milk, condensed milk, evaporated milk, frozen poultry and pastries stay at 21% (Annex 2). Minced poultry qualifies only if added salt is at most 1%. Goods at a reduced rate keep that rate on import and on EU acquisition (art. 42.1). In a set of goods, each item takes its own rate (art. 41(2)).

## The taxable base

- **What is taxed:** supplies of goods and services for consideration in Latvia, EU acquisitions of goods, imports, and services received from abroad where the customer pays the tax (art. 5).
- **Value:** the consideration without VAT (art. 1(2), art. 34).
- **Exempt without credit (art. 52(1)):** universal postal services; medical and dental care; social care; recognised education and private tuition; listed cultural services; insurance and finance; fund management; gambling and lotteries; sales of used real estate, but new buildings and building land stay taxable; listed residential services.
- **Input VAT.** A registered business deducts VAT on purchases used for its taxable supplies (arts. 92, 93). Mixed businesses use a proportion (art. 98).
- **Entertainment:** 60% of VAT on receptions, meals, conferences and promotional items is not deductible, so 40% can be deducted (art. 100(1)).
- **Cars.** For an ordinary passenger car with up to 8 passenger seats, 50% of the VAT on purchase, lease, import, fuel and repairs is not deductible (art. 100(2)). For a car whose value meets the "representative car" level set in the corporate income tax rules, no VAT is deductible on the car, or on its running costs for 60 months (art. 100(1.1)). Neither limit applies to taxis, rental cars, car dealers, freight, driving schools, security firms, or a car used for taxable transactions where the business keeps GPS trip records (art. 100(3), (4)).
- **Domestic reverse charge.** The customer pays the VAT when both parties are registered, for: timber and timber services (art. 141); construction services, including design in a construction contract (art. 142); scrap metal, where the buyer holds the licence (art. 143); mobile phones, tablets, laptops, integrated circuit devices and game consoles (art. 143.1); grain and industrial crops such as wheat, rye, barley, oats, maize, buckwheat, triticale, soya, linseed and rapeseed (art. 143.2); raw precious metals (art. 143.3); and the semi-finished ferrous and non-ferrous metal products that the Cabinet lists (art. 143.4). The seller invoices without VAT. The buyer must pay by non-cash means.
- **Refunds.** Excess input VAT is refunded within 30 days after the return due date, subject to VID checks (art. 109(1)).

## Deadlines and filing

| What | When | Source |
|---|---|---|
| Registration once over EUR 55,000 (threshold plus tolerance) | Application by the 15th of the next month | art. 59(5) |
| Registration when the tolerance is used (over EUR 50,000 but not over EUR 55,000) | Application by 30 November; by 31 December if the threshold is crossed after 30 November | art. 59(4), (6), (7) |
| Registration for EU acquisitions over EUR 10,000 | By the 15th of the following month | art. 57(1) |
| Period | Monthly if taxable supplies exceed EUR 50,000 in the previous or current year, or if the business makes intra-EU supplies of goods, B2B services to other EU states, or call-off stock transfers; monthly for the first six months after registration; otherwise quarterly | art. 115(1), (2), (3), (5) |
| Change from monthly to quarterly | Notice by 31 January | art. 115(6)(2) |
| VAT return and its annexes, including nil returns | Within 20 days after the period ends; next working day if that is a holiday | arts. 117(2), 118(1), (7) |
| Payment | Within 23 days after the period ends; next working day if that is a holiday | art. 119(1); Law on Taxes and Fees art. 29(3.1) |
| EU sales list (annex on supplies to the EU) | For each calendar month, within the same 20 days | arts. 116(2)(2), 117(7), 118(6) |
| Annual return (proportion changes, adjustments) | By 1 May of the next year, with payment | arts. 117(5), 118(5), 119(6) |
| Tax invoice | By the 15th day after the supply or prepayment; for intra-EU supplies and reverse-charged B2B services, by the 15th of the following month | art. 131(1), (2) |

**There is no semi-annual period in the 2026 law.** Article 115 provides only for monthly and quarterly periods.

**E-invoicing.** Under the VAT Law, an electronic invoice needs the customer's agreement (art. 132(1)). Under the Accounting Law, invoices to budget institutions must be structured e-invoices. Their data has gone to VID from 1 January 2026. Structured e-invoices between Latvian businesses become compulsory from 1 January 2028 (Accounting Law art. 11(14), transitional provisions 8 to 10). In 2026 a B2B invoice can still be on paper or in a PDF.

## Penalties and interest

- **Late payment:** 0.05% of the unpaid tax for each day late (Law on Taxes and Fees art. 29(2)). For taxes paid through the single tax account, VID calculates this twice a month, on the 1st and 15th. It charges nothing if the tax arrives by the last day of the month in which it fell due (art. 29(2.1), (2.2)).
- **Late return (Law on Taxes and Fees art. 141, fine unit EUR 5):**
  - 3 to 10 days late: a warning or 5 to 14 units (EUR 25 to 70). One delay of up to five days in 12 months on a monthly or quarterly EDS return is not fined.
  - 11 to 20 days late: 15 to 30 units (EUR 75 to 150).
  - 21 to 30 days late: 31 to 56 units (EUR 155 to 280).
  - More than 30 days late, or no return: 57 to 140 units (EUR 285 to 700).
- **Late registration:** a warning or a fine. Individuals pay 10 to 42 units, legal persons 10 to 70 units (art. 136).
- **Under-declaration found in an audit (art. 32):** the tax, interest up to the audit start, and a penalty. The penalty is 20% of the shortfall if it is no more than 15% of the tax due, and 30% if it is more. The penalty is halved for a first offence by a business that filed and paid on time and cooperated (art. 32(7)).
- **VAT Law penalties:** 100% of VAT shown on an invoice issued without the right to do so (art. 146(2)). 10% of VAT not self-assessed on EU acquisitions or services received from abroad (art. 146(4)).

## Cross-border points

- **B2B services.** The general rule taxes services where the customer is established (art. 19(1)). A Latvian business buying such services from an EU or non-EU supplier accounts for the VAT itself (arts. 88(1), 89(1)). A Latvian supplier of such services to an EU business charges no Latvian VAT and lists the sale on the EU sales list.
- **Intra-EU supplies of goods** are zero-rated when the customer has a valid VAT number and the goods leave Latvia (art. 43). EU acquisitions are self-assessed by the buyer (art. 86(1)).
- **Distance sales and digital services to EU consumers.** Latvian VAT applies up to EUR 10,000 a year across the EU. Above that, the customer's state's VAT applies, through the One Stop Shop if wanted (arts. 13.1, 27, 140.3).
- **EU small-enterprise scheme.** A Latvian business can be exempt in another EU state when its sales there stay under that state's threshold and its EU-wide turnover is at most EUR 100,000. It notifies VID through EDS and gets an "EX" number (art. 139.1). EU businesses using the scheme in Latvia must stay under EUR 50,000 in Latvia and EUR 100,000 in the EU (art. 61(11), (12)).
- **Non-EU businesses** making taxable supplies in Latvia register under arts. 62 and 63. A Latvian registered business that has run continuously for over two years can register as a fiscal representative for foreign businesses (art. 65(1)).
- For permanent establishments, withholding tax and treaties, see `lv-cross-border`.

## Worked examples

**Example 1. Monthly SIA return, March 2026.** An SIA made EUR 40,000 of sales at 21% and EUR 10,000 of sales of Annex 1 fresh vegetables at 12%. It bought goods for resale for EUR 20,000 net at 21%. It spent EUR 1,000 net on a client dinner and EUR 800 net on fuel and repairs for an ordinary company car, both at 21%. Output VAT is EUR 8,400 + EUR 1,200 = EUR 9,600. Input VAT on goods is EUR 4,200. Of the EUR 210 VAT on the dinner, only 40% can be deducted, which is EUR 84 (art. 100(1)). Of the EUR 168 VAT on the car, only 50% can be deducted, which is EUR 84 (art. 100(2)). Total input VAT is EUR 4,368. The SIA files the return by 20 April 2026 and pays EUR 5,232 by 23 April 2026.

```oa-check
name: Latvian SIA, March 2026 return with entertainment and car limits
inputs:
  sales_21: 40000
  sales_12: 10000
  purchases_21: 20000
  entertainment_net: 1000
  car_costs_net: 800
steps:
  - output_21: sales_21 * 0.21
  - output_12: sales_12 * 0.12
  - output_total: output_21 + output_12
  - input_purchases: purchases_21 * 0.21
  - input_entertainment: entertainment_net * 0.21 * 0.40
  - input_car: car_costs_net * 0.21 * 0.50
  - input_total: input_purchases + input_entertainment + input_car
  - payable: output_total - input_total
expected:
  output_total: 9600
  input_entertainment: 84
  input_car: 84
  input_total: 4368
  payable: 5232
```

**Example 2. Sole trader goes over the threshold in 2026.** An unregistered sole trader's domestic sales were under EUR 50,000 in 2025. All its sales are at 21%. Its 2026 sales pass EUR 55,000 in September and reach EUR 58,000 by the end of that month. That is over EUR 50,000 plus the EUR 5,000 tolerance, so it must apply to register by 15 October 2026 (art. 59(5)). Until it is registered, VAT is due on the sales above EUR 55,000, here EUR 3,000. That amount is treated as including VAT (art. 34(10)), so the VAT is 3,000 x 21/121 = EUR 520.66, payable by 23 October 2026 (art. 119(2)). As a new registrant it files monthly for six months (art. 115(2)). In November 2026 it buys EUR 10,000 of building work from a registered subcontractor. This is under the domestic reverse charge (art. 142). The trader puts EUR 2,100 of output VAT on its November return. It deducts the same EUR 2,100 if the work is for its taxable business. The net effect is nil.

```oa-check
name: Sole trader over EUR 55,000 in 2026, then construction reverse charge
inputs:
  sales_to_september: 58000
  threshold: 50000
  tolerance: 5000
  construction_net: 10000
steps:
  - excess_gross: max(sales_to_september - threshold - tolerance, 0)
  - vat_on_excess: round(excess_gross * 21 / 121, 2)
  - rc_output: construction_net * 0.21
  - rc_input: construction_net * 0.21
  - rc_net: rc_output - rc_input
expected:
  excess_gross: 3000
  vat_on_excess: 520.66
  rc_output: 2100
  rc_net: 0
```

## Ask the client first

1. Is the business registered for VAT, and since when? What were its domestic sales in 2025 and so far in 2026?
2. Does it sell goods to EU businesses, supply B2B services abroad, or buy goods or services from abroad? Each of these forces monthly filing or registration.
3. What does it sell? Check each line against the 12% and 5% lists, especially food sold from July 2026 and accommodation.
4. Does it buy or sell timber, building work, scrap, phones and laptops, grain or metals? These fall under the domestic reverse charge.
5. Does it own or lease cars, and what is each car's value? Does it hold GPS trip records?
6. Does it make exempt supplies, such as letting, finance or medical care, alongside taxable ones?

## Sources

| Source | URL | Read on |
|---|---|---|
| VAT Law (Pievienotās vērtības nodokļa likums), version in force from 1 January 2026: arts. 1, 3, 5, 13.1, 19, 27, 34, 41, 42, 42.1, 43, 52, 57, 59, 61, 86, 88, 89, 98, 100, 109, 115 to 119, 131, 132, 139.1, 139.2, 141 to 143.4, 146; transitional provision 48; Annexes 1 and 2 | https://likumi.lv/ta/id/253451-pievienotas-vertibas-nodokla-likums | 2026-10-24 (likumi.lv refused the connection; read from the Internet Archive copy of 16 October 2026, https://web.archive.org/web/20261016213528/https://likumi.lv/ta/id/253451-pievienotas-vertibas-nodokla-likums) |
| Accounting Law (Grāmatvedības likums): art. 11(14) to (16); transitional provisions 8 to 10 | https://likumi.lv/ta/id/324249-gramatvedibas-likums | 2026-10-24 (Internet Archive copy of 16 October 2026, https://web.archive.org/web/20261016213528/https://likumi.lv/ta/id/324249-gramatvedibas-likums) |
| Law on Taxes and Fees (likums "Par nodokļiem un nodevām"): arts. 29, 32, 136, 141 | https://likumi.lv/ta/id/33946-par-nodokliem-un-nodevam | 2026-10-24 (Internet Archive copy of 18 September 2026) |
| Administrative Liability Law (Administratīvās atbildības likums): art. 16 | https://likumi.lv/ta/id/303007-administrativas-atbildibas-likums | 2026-10-24 (Internet Archive copy of 10 August 2026) |
| State Revenue Service (VID) | https://www.vid.gov.lv | 2026-10-24 (refused the connection; not read) |

Not yet confirmed: the VAT return form and its row numbers (the Cabinet regulation on the return was not read); the Cabinet list of metal products under art. 143.4; the full text of the art. 52 exemptions and the art. 98 proportion rules beyond the headings used here; any VAT Law amendment after the 16 October 2026 archive copy, including any 2027 rate changes.

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

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-10-24. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `latvia-vat-return` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/latvia-vat-return. If neither is available, confirm every figure against the official source pages cited above before relying on it.
