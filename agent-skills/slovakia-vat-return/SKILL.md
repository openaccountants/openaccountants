---
name: slovakia-vat-return
description: "Slovak VAT (DPH) for tax year 2026 under Act No. 222/2004 Coll. as in force from 1 January 2026: the 23% standard rate, the 19% rate (most food, electricity, non-alcoholic drinks served in restaurants), the 5% rate (basic food, medicines, books, restaurant meals, accommodation, sports and fitness entry), the foods moved from 19% to 23% in 2026, the monthly or quarterly return and control statement due 25 days after the period, refunds, domestic reverse charge, the 50% cap on passenger car input VAT, the EU SME scheme, fines and late-payment interest. Trigger on: Slovak VAT return, DPH priznanie, kontrolny vykaz, suhrnny vykaz, nadmerny odpocet, prenesenie danovej povinnosti, Slovakia 23% VAT. Out of scope: which registration a client needs (slovakia-vat-registration-4-7-7a), income tax (slovakia-pit, sk-corporate-income-tax), payroll (sk-payroll-social)."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/slovakia-vat-return"
  jurisdiction: "SK"
  tax_year: "2026"
  last_updated: "2026-10-23"
  trust_label: "Built by Michael Cutajar and the OpenAccountants team"
  review_status: "pending_review"
---

# Slovakia VAT return (2026)

Source-cited draft: not reviewed by an accountant. Built by Michael Cutajar and the OpenAccountants team.

This skill covers the Slovak VAT return for a business registered in Slovakia for 2026: rates, what goes into the return, the control statement, the EC sales list, refunds, penalties and interest. Every figure is taken from Act No. 222/2004 Coll. on VAT (the "VAT Act") in the version in force from 1 January 2026 to 31 December 2026, and from Act No. 563/2009 Coll. (the Tax Procedure Code). It links to the other Slovakia skills and does not repeat them:

- [slovakia-vat-registration-4-7-7a](slovakia-vat-registration-4-7-7a.md): whether a client must register under § 4, § 7 or § 7a, the EUR 50,000 and EUR 62,500 turnover tests, and what a § 7 or § 7a registrant may not deduct.
- [slovakia-pit](slovakia-pit.md) and [sk-corporate-income-tax](sk-corporate-income-tax.md): income tax of individuals and companies.
- EU rules on place of supply, intra-EU supplies and OSS are in [eu-vat-directive](../eu/eu-vat-directive.md); the general return workflow is in [vat-workflow-base](../../foundation/vat-workflow-base.md).

## Who this applies to

- **VAT payers (platitel) under § 4.** A taxable person with its seat, place of business or fixed establishment in Slovakia (or, failing that, its residence or usual abode there) becomes a payer from 1 January of the year after its turnover passed EUR 50,000, or at the supply that takes turnover in the current year past EUR 62,500 (VAT Act § 4(1)(a) and (b)). Voluntary registration is allowed (§ 4(6) and (7)). The registration tests sit in the sibling skill.
- **Foreign persons registered under § 5.** A business with no seat, place of business, establishment or residence in Slovakia becomes a payer from its first taxable supply in Slovakia, unless all its Slovak supplies fall in the § 5(2) list (for example supplies where the customer accounts for the tax, or supplies covered by OSS). It applies to the Bratislava Tax Office within five working days (§ 5(1) to (3)).
- **Persons who are not payers but owe tax under § 69.** Someone registered only under § 7 or § 7a, or not registered at all, who receives a reverse-charge supply files a return only for the month the liability arose, and does not pay if the tax is EUR 5 or less (§ 78(3)).
- **Out:** a business below the § 4 thresholds that is not a payer charges no VAT and files no periodic VAT return. It must still check § 7 and § 7a.

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source URL |
|---|---|---|---|
| Standard rate | 23% (since 1 January 2025) | 2026 | https://static.slov-lex.sk/static/SK/ZZ/2004/222/20260101.html (§ 27(1)) |
| Reduced rate, goods in Annex 7 point 1: food for human consumption not in point 2, bottled drinking water without sugar or flavouring (not mains water), salt, electricity | 19% | 2026 | https://static.slov-lex.sk/pdf/prilohy/SK/ZZ/2004/222/20260101_5815198-2.pdf (§ 27(2)(a)) |
| Reduced rate, Annex 7a point 1: drinks served as restaurant and catering services (CPA 56), except alcoholic drinks over 0.5% alcohol | 19% | 2026 | https://static.slov-lex.sk/pdf/prilohy/SK/ZZ/2004/222/20260101_5747469-2.pdf (§ 27(2)(b)) |
| Reduced rate, Annex 7 points 2 and 3: listed fresh meat, freshwater fish, milk, yoghurt, butter, honey, fresh vegetables, apples and pears, fresh bread and rolls, juices with at most 5 g added sugar per 100 ml, medicines (chapter 30), listed medical aids, printed books, newspapers and periodicals (advertising at most 50%) | 5% | 2026 | https://static.slov-lex.sk/pdf/prilohy/SK/ZZ/2004/222/20260101_5815198-2.pdf (§ 27(3)(a)) |
| Reduced rate, Annex 7a point 2: accommodation (CPA 55), food served as restaurant and catering services (CPA 56), online books and audio books, entry to theatre, opera, ballet and similar events, museums, sports events, fitness centres | 5% | 2026 | https://static.slov-lex.sk/pdf/prilohy/SK/ZZ/2004/222/20260101_5747469-2.pdf (§ 27(3)(b)) |
| Reduced rate, registered social enterprises using 100% of after-tax profit for their main aim; state-supported rental housing | 5% | 2026 | https://static.slov-lex.sk/static/SK/ZZ/2004/222/20260101.html (§ 27(3)(c) to (e)) |
| Foods moved from 19% to 23% on 1 January 2026 (Acts 261/2025 and 385/2025): mainly sweets, cakes, jams, ice cream, muesli, sweetened soft drinks, salty snacks; listed dietetic foods stay at 19% | 23% | 2026 | https://www.financnasprava.sk/sk/podnikatelia/dane/dan-z-pridanej-hodnoty/sadzby-dane |
| Imported goods declared under the § 68cb low-value scheme | Not covered by § 27(2)(a) or (3)(a), so 23% | 2026 | https://static.slov-lex.sk/static/SK/ZZ/2004/222/20260101.html (§ 27(2)(a), (3)(a)) |
| Rate used when rates change | Rate in force on the day the tax liability arises | 2026 | https://static.slov-lex.sk/static/SK/ZZ/2004/222/20260101.html (§ 27(5)) |
| Registration turnover, payer from 1 January of the next year | Over EUR 50,000 in the calendar year | 2026 | https://static.slov-lex.sk/static/SK/ZZ/2004/222/20260101.html (§ 4(1)(a)) |
| Registration turnover, payer at the supply that crosses it | Over EUR 62,500 in the current calendar year | 2026 | https://static.slov-lex.sk/static/SK/ZZ/2004/222/20260101.html (§ 4(1)(b)) |
| Quarterly tax period allowed | More than 12 months since the end of the month of registration, and turnover under EUR 100,000 in the preceding 12 months | 2026 | https://static.slov-lex.sk/static/SK/ZZ/2004/222/20260101.html (§ 77(2)) |
| Passenger cars (M1, L1e, L3e) acquired, leased long term or run from 1 January 2026 to 30 June 2028 | 50% of input VAT deductible, unless an exception applies | 2026 | https://static.slov-lex.sk/static/SK/ZZ/2004/222/20260101.html (§ 85n(1) to (5)) |
| Domestic reverse charge on mobile phones and integrated circuits | Invoice tax base EUR 5,000 or more | 2026 | https://static.slov-lex.sk/static/SK/ZZ/2004/222/20260101.html (§ 69(12)(h), (i)) |
| Control statement, simplified invoices listed by supplier | When deducted VAT on simplified invoices in the period is EUR 3,000 or more | 2026 | https://static.slov-lex.sk/static/SK/ZZ/2004/222/20260101.html (§ 78a(6)) |
| EC sales list may be quarterly | Goods in § 80(1)(a) to (c) at or under EUR 50,000 in the quarter and in the four previous quarters | 2026 | https://static.slov-lex.sk/static/SK/ZZ/2004/222/20260101.html (§ 80(2)) |
| Fast refund condition: tax, customs and insurance arrears in the last 6 months | Not more than EUR 1,000 in total | 2026 | https://static.slov-lex.sk/static/SK/ZZ/2004/222/20260101.html (§ 79(2)(c)) |
| Non-payer owing reverse-charge tax: no payment due | Tax of EUR 5 or less | 2026 | https://static.slov-lex.sk/static/SK/ZZ/2004/222/20260101.html (§ 78(3)) |
| EU SME scheme, Slovak business exempt in other member states | EU turnover not over EUR 100,000 in the current and the previous calendar year | 2026 | https://static.slov-lex.sk/static/SK/ZZ/2004/222/20260101.html (§ 68g(1)) |
| EU SME scheme, business from another member state exempt in Slovakia | Slovak turnover not over EUR 62,500 this year and EUR 50,000 last year; EU turnover not over EUR 100,000 in both years | 2026 | https://static.slov-lex.sk/static/SK/ZZ/2004/222/20260101.html (§ 68f(1)) |

## The taxable base

- **Output tax.** Tax is charged on domestic supplies at the rate in force on the day the liability arises. The return also carries the tax the payer self-assesses as customer: intra-EU acquisitions of goods, services from foreign persons under § 69(3), and domestic reverse-charge supplies under § 69(12).
- **Domestic reverse charge (§ 69(12)).** Applies only when both supplier and customer are payers registered under § 4, § 4b, § 4c or § 5. It covers metal waste and scrap; greenhouse gas emission allowances; real estate the supplier has opted to tax under § 38(8); real estate sold in a forced sale; goods supplied when a security is enforced; cereals and oilseeds in chapters 10 and 12 not normally sold for final consumption; iron and steel in chapter 72 and headings 7301, 7308 and 7314; mobile phones and integrated circuits where the invoice tax base is EUR 5,000 or more; and construction work in section F of the classification, including goods supplied with installation in section F. The supplier invoices without VAT. The customer declares the tax and, if entitled, deducts it.
- **Input tax.** A payer deducts tax on purchases used for taxable supplies. There is no deduction for hospitality and entertainment (§ 49(7)(a)). Where purchases serve both taxable and exempt supplies, the deductible share follows the coefficient in § 50.
- **Passenger cars from 1 January 2026 (§ 85n).** For an M1 car, or an L1e or L3e motorcycle, acquired as a long-term asset, leased on a contract that is not short-term, or for goods and services bought to run one, from 1 January 2026 to 30 June 2028, the payer deducts 50%. Private use then counts as neither a supply of services nor a supply of goods. The cap does not apply to vehicles used only for car rental, paid passenger transport including taxis, driving schools, or as demonstration or courtesy cars (§ 85n(4)). It also does not apply where the vehicle is used only for business and the payer keeps electronic records for each vehicle: VIN, registration number, odometer readings at the start, at each period end and at the end, and a log of every trip with the driver, date and time, business purpose, start and end place and kilometres (§ 85n(5) and (6)). The payer must notify the tax office of a § 85n(4) or (5) use by the return deadline for the period of the first deduction. That notice is not needed for vehicles acquired by 31 December 2025 (§ 85n(9)).
- **Excess deduction (nadmerny odpocet).** If deductible tax is more than tax due, the excess is first set against the next period's liability. Any part not used is refunded within 30 days of filing the next period's return (§ 79(1)). A monthly payer registered at least 12 months, with arrears of not more than EUR 1,000 in the last 6 months, can mark the return and be refunded within 30 days of the return deadline for the period itself (§ 79(2) and (3)). The refund clock stops while a request to fix the return or control statement is open (§ 79(4)).
- **Rounding.** Figures in the return are rounded to the nearest euro cent, with 0.005 rounded up (§ 78(7)).

## Deadlines and filing

| Obligation | Deadline | Source |
|---|---|---|
| Tax period | Calendar month. A calendar quarter if § 77(2) is met and the change is notified within 25 days after the end of the month the conditions were met; it takes effect from the next calendar quarter | VAT Act § 77 |
| VAT return and payment, Slovak payer | 25 days after the end of each tax period; tax paid in the same time | VAT Act § 78(1), (2)(a) |
| Deadline falling on a Saturday, Sunday or public holiday | Moves to the next working day | Tax Procedure Code § 27(4) |
| First return when the VAT number arrives after that deadline | Five working days from delivery of the registration decision | VAT Act § 78(2)(a)(1) |
| VAT return and payment, foreign payer | 25 days after the end of a period in which tax was due, exempt intra-EU or export supplies were made, exempt goods were acquired, or a deduction is claimed | VAT Act § 78(2)(b) |
| Non-payer liable under § 69 | 25 days after the end of the month the liability arose; no payment if EUR 5 or less | VAT Act § 78(3) |
| Control statement (kontrolny vykaz) | Electronically, in XML, for every period with a return, 25 days after the period. Not due if the return reports no supplies, or only exempt § 43 or § 47 supplies with no deduction (or only a § 49(2)(d) deduction) | VAT Act § 78a(1), (16) |
| Answer to a tax office request on the control statement | Five working days from delivery of the request | VAT Act § 78a(13) |
| EC sales list (suhrnny vykaz) | Monthly, 25 days after the period; quarterly if § 80(2) is met; a § 7 or § 7a registrant supplying § 15(1) services files for each quarter in which it supplied them | VAT Act § 80 |
| EU SME scheme quarterly report (Slovak business using the scheme abroad) | End of the month after the quarter | VAT Act § 68g(8) |

The control statement lists, invoice by invoice, every invoice issued for domestic taxable supplies or for domestic reverse-charge supplies under § 69(12)(f) to (j) (not simplified invoices) and every invoice received where the payer is the customer liable under § 69(2), (3), (6), (7) and (9) to (12), or deducts tax charged by another payer. Each line shows the counterparty's VAT number, invoice number, date of supply, tax base, tax, rate and deducted tax (§ 78a(2) and (4)). Simplified invoices received are given as totals, split by supplier once deducted VAT on them reaches EUR 3,000 in the period (§ 78a(6)). Retail sales are given as eKasa totals by rate (§ 78a(8)). A corrective statement replaces the original before the deadline; after the deadline, a supplementary statement carries only the changed lines (§ 78a(12)).

A payer that failed to register must file every missed return and control statement in date order, starting from the first period (§ 78(9), § 78a(14)).

## Penalties and interest

| Breach | Consequence | Source |
|---|---|---|
| Return not filed on time | Fine EUR 100 to 30,000; EUR 100 to 60,000 if not filed by the date in a tax office request (only one of the two is imposed) | Tax Procedure Code § 154(1)(a), § 155(1)(a), (b), (3) |
| Registration not made on time | Fine EUR 100 to 30,000 | § 155(1)(c) |
| First breach, fines set within a range | The tax office does not impose a fine set within a range for a first breach | § 155(4) |
| Tax under-declared, found by the tax office | 3 times the ECB base rate a year (at least 10% a year) on the extra tax, counted daily from the deadline; at least 1% of the assessed sum and at most the sum itself. Two thirds of that fine if the assessment is paid within 15 days | § 155(1)(f), (2), (5), (17) |
| Supplementary return raising tax | ECB base rate a year (at least 3%); twice the ECB rate (at least 7%) if filed after an audit has started | § 155(1)(g), (h), (5) |
| Control statement missing, late, incomplete or wrong, or defects not fixed by the requested date | Fine up to EUR 10,000; up to EUR 100,000 for repeated breaches | VAT Act § 78a(15) |
| Fast refund obtained on false data | Fine up to 1.3% of the refund | VAT Act § 79(8) |
| Late payment | Interest at 4 times the ECB base rate, at least 15% a year, counted daily from the day after the due date, for at most four years; not charged if EUR 5 or less | Tax Procedure Code § 156(2), (6)(b) |
| Fines of EUR 5 or less | Not imposed | § 155(11) |

## Cross-border points

- **Services from abroad.** A Slovak business receiving a § 15(1) service from a foreign supplier accounts for the tax as customer (§ 69(3)). A non-payer receiving such a service from a supplier in another member state must first register under § 7a and then has no right to deduct; see the registration skill.
- **Intra-EU supplies of goods** are exempt under § 43 and go on the EC sales list. Exports are exempt under § 47.
- **Imports.** Import VAT assessed by customs is due on the customs timetable and is not part of the return's own tax liability (§ 78(1)). The § 68cb scheme for consignments of EUR 150 or less is a customs procedure for the person presenting the goods.
- **Foreign businesses** register under § 5 at the Bratislava Tax Office within five working days of becoming a payer. EU sellers to Slovak consumers can use OSS (§ 68a to 68c) instead.
- **EU SME scheme (from 1 January 2025).** A Slovak small business whose EU turnover stays at or under EUR 100,000 in the current and previous year can notify the Slovak tax office in advance and use small-business exemptions in other member states with an EX number (§ 68g). It files a quarterly report by the end of the following month. A business from another member state is exempt in Slovakia if its Slovak turnover stays at or under EUR 62,500 this year and EUR 50,000 last year and its EU turnover at or under EUR 100,000 (§ 68f). It loses the exemption from the supply that takes Slovak turnover past EUR 62,500 or EU turnover past EUR 100,000 (§ 68f(6)).
- **E-invoicing.** The version of the VAT Act in force from 1 January 2027 (Act 385/2025) changes invoicing and reporting. It is outside this 2026 skill.

## Worked examples

**Example 1: a restaurant company, monthly return, March 2026.** Cafe Dunaj s.r.o. is a monthly payer. In March 2026 it sells EUR 40,000 net of goods and services at 23% (alcoholic drinks and takeaway sweets), EUR 10,000 net of restaurant meals at 5%, and EUR 2,000 net of non-alcoholic drinks served at the tables at 19%. Its domestic purchase invoices carry EUR 4,600 of deductible VAT. Output tax is 40,000 x 23% = 9,200, plus 10,000 x 5% = 500, plus 2,000 x 19% = 380, a total of 10,080. It deducts 4,600 and pays 5,480. The 25-day deadline ends on Saturday 25 April 2026, so the return, the control statement and the payment are due on Monday 27 April 2026 (Tax Procedure Code § 27(4)). Every invoice it issued (other than simplified invoices) and every full purchase invoice it deducts goes into the control statement line by line; simplified purchase invoices go in as totals and till sales as eKasa totals by rate.

```oa-check
name: Cafe Dunaj s.r.o., March 2026 return
inputs:
  sales_23: 40000
  meals_5: 10000
  drinks_19: 2000
  input_vat: 4600
steps:
  - out_23: sales_23 * 0.23
  - out_5: meals_5 * 0.05
  - out_19: drinks_19 * 0.19
  - output_vat: out_23 + out_5 + out_19
  - payable: output_vat - input_vat
expected:
  output_vat: 10080
  payable: 5480
```

**Example 2: a consultancy with a reverse charge and a new car, April 2026.** Tatra Consulting s.r.o., a monthly payer, invoices Slovak clients EUR 30,000 net at 23%. It buys EUR 2,000 of advertising from an Irish company (a § 15(1) service), with no VAT on the invoice. In April it also buys an M1 passenger car for EUR 25,000 plus EUR 5,750 VAT. The car is used for business and private trips and no trip log is kept, so § 85n(1) limits the deduction to 50%. A client lunch carries EUR 69 VAT, which is not deductible (§ 49(7)(a)). Other purchases carry EUR 1,150 of deductible VAT. Output tax is 30,000 x 23% = 6,900 plus the self-assessed 2,000 x 23% = 460, a total of 7,360. Input tax is the 460 reverse charge, plus 5,750 x 50% = 2,875 on the car, plus 1,150, a total of 4,485. The lunch VAT is left out. The company pays 2,875. The Irish invoice goes into the control statement as a received invoice where the company is the customer liable for the tax.

```oa-check
name: Tatra Consulting s.r.o., April 2026 return
inputs:
  sales_23: 30000
  eu_ads: 2000
  car_vat: 5750
  lunch_vat: 69
  other_input: 1150
steps:
  - out_sales: sales_23 * 0.23
  - rc: eu_ads * 0.23
  - car_input: car_vat * 0.5
  - lunch_input: lunch_vat * 0
  - output_vat: out_sales + rc
  - input_vat: rc + car_input + lunch_input + other_input
  - payable: output_vat - input_vat
expected:
  output_vat: 7360
  input_vat: 4485
  payable: 2875
```

## Ask the client first

1. Which registration do you hold (§ 4, § 5, § 7 or § 7a), and since when? This decides whether you file every period and whether you can deduct at all.
2. Are you on monthly or quarterly periods, and did turnover in any 12-month run reach EUR 100,000?
3. What do you sell, and at which rate? Food and restaurant clients need the 2026 split between 23%, 19% and 5%.
4. Did you buy, lease or run an M1 car or an L1e or L3e motorcycle in 2026, and do you keep the § 85n trip log?
5. Did you receive services from foreign suppliers, or buy construction work, scrap, steel, cereals, or phones and chips at EUR 5,000 or more from Slovak payers?
6. Do you make exempt supplies (financial, insurance, housing rental) as well as taxable ones?

## Sources

| Source | URL | Read on |
|---|---|---|
| Act No. 222/2004 Coll. on VAT, version in force 1 January 2026 to 31 December 2026 (§ 4, 5, 7a, 27, 49, 68cb, 68f, 68g, 69, 77, 78, 78a, 79, 80, 85n, 85o) | https://static.slov-lex.sk/static/SK/ZZ/2004/222/20260101.html | 2026-10-23 |
| VAT Act Annex 7, goods at reduced rates (version from 1 January 2026) | https://static.slov-lex.sk/pdf/prilohy/SK/ZZ/2004/222/20260101_5815198-2.pdf | 2026-10-23 |
| VAT Act Annex 7a, services at reduced rates (version from 1 January 2026) | https://static.slov-lex.sk/pdf/prilohy/SK/ZZ/2004/222/20260101_5747469-2.pdf | 2026-10-23 |
| Act No. 563/2009 Coll., Tax Procedure Code, version in force from 1 September 2026 (§ 27, 154, 155, 156; same text of § 154 to 156 in the version from 1 January 2026) | https://static.slov-lex.sk/static/SK/ZZ/2009/563/20260901.html | 2026-10-23 |
| Financna sprava, Sadzby dane (VAT rates and the 1 January 2026 changes) | https://www.financnasprava.sk/sk/podnikatelia/dane/dan-z-pridanej-hodnoty/sadzby-dane | 2026-10-23 |

Not yet confirmed: the row numbers of the 2026 VAT return form and the control statement layout (the official forms were not read, so this skill names no boxes); the ECB base rate on any given date, which sets the fine and interest percentages above the floors; whether the first-breach rule in Tax Procedure Code § 155(4) also covers the control statement fine in VAT Act § 78a(15); the detail of the § 50 coefficient (rounding and de minimis), which was not re-read for this version.

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

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-10-23. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `slovakia-vat-return` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/slovakia-vat-return. If neither is available, confirm every figure against the official source pages cited above before relying on it.
