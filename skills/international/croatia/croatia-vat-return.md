---
name: croatia-vat-return
description: "Croatian value added tax (porez na dodanu vrijednost, PDV) for 2026 under the Zakon o porezu na dodanu vrijednost as amended to NN 48/2026. Covers who must register (the EUR 60,000 small-business threshold in Article 90 and the EU SME scheme), the 25%, 13% and 5% rates and what each covers, the temporary 5% rate for gas and heating to 31 March 2027, input VAT and the blocked items (entertainment, 50% on passenger cars), monthly and quarterly periods, the PDV return, PDV-S and ZP all due by the last day of the following month from 2026, payment, refunds, domestic and cross-border reverse charge, Fiskalizacija 2.0 e-invoicing and e-reporting from 1 January 2026, and fines. Trigger on: Croatia VAT, PDV Hrvatska, PDV obrazac, PDV-S, Zbirna prijava, eRačun, fiskalizacija 2.0, Croatian reverse charge. Out of scope: income tax (croatia-income-tax), profit tax (hr-corporate-income-tax), payroll (croatia-payroll), contributions (croatia-social-contributions)."
jurisdiction: HR
category: international
tax_year: 2026
tier: 2
last_updated: 2026-10-23
version: 3.0
verified_by: pending
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Croatia: value added tax (PDV), 2026 (v3.0)

Source-cited draft: not reviewed by an accountant, not for filing.

The statute is the Zakon o porezu na dodanu vrijednost (ZPDV), Narodne novine (NN) 73/13 with amendments up to NN 48/26. The Tax Administration (Porezna uprava) keeps the consolidated text in its register of regulations. Article numbers below refer to it. Forms and line rules sit in the Pravilnik o porezu na dodanu vrijednost (VAT Rulebook). E-invoicing sits in a separate law, the Zakon o fiskalizaciji (NN 89/25). Interest and the limitation period sit in the Opći porezni zakon (OPZ, General Tax Act).

**What changed for 2026.**
- NN 151/25, in force 1 January 2026: the PDV return, the PDV-S and the ZP are now due by the last day of the month after the period. Before 2026 they were due by the 20th. The last 2025 period (December 2025, or October to December 2025) still followed the old law and its 20th deadline (151/25 Art. 10).
- NN 151/25 also removed the need for the buyer's consent to receive an e-invoice where the Fiscalisation Act requires one (ZPDV Art. 80(2)).
- Zakon o fiskalizaciji (NN 89/25): B2B e-invoicing, e-invoice fiscalisation and e-reporting apply from 1 January 2026 for VAT-registered businesses. Businesses outside the VAT register must issue e-invoices from 1 January 2027 (Art. 80).
- NN 32/26, in force 30 March 2026: the temporary 5% rate on gas, heating, firewood, pellets, briquettes and wood chips now runs to 31 March 2027 (Art. 38(4) and (5)).
- NN 48/26, in force the day after publication in May 2026: new Article 38.a lets the Government set, by decree and for a limited time, the VAT rate on energy products subject to excise duty.

This skill replaces version 2.0, which carried 2025 figures and some wrong rules (for example a full block on passenger cars, which is in fact a 50% block). If you used it, recheck those points.

## Who this applies to

- **Taxable persons** who supply goods or services in Croatia for consideration, acquire goods from other EU states, or import goods (Arts. 1 to 6, 75).
- **Small business exemption.** A business established in Croatia whose domestic annual turnover was not more than **EUR 60,000** is exempt from charging VAT on domestic supplies (Art. 90(1)). It may not show VAT on invoices and may not deduct input VAT (Art. 90.g). The exemption stops at the moment the threshold is passed (Art. 90.f(2)). The business must then enter the VAT register (Art. 77(1)). If it does not, the Tax Administration enters it by decision.
- **What counts toward the EUR 60,000.** Taxable supplies, zero-rated solar supplies, exempt supplies with deduction under Arts. 41 and 45 to 49, and real estate and financial supplies unless ancillary. Sales of the business's own fixed assets are left out (Art. 90(3) and (4)).
- **Voluntary registration.** An exempt small business can ask to be taxed normally. It must then stay in the normal scheme for the current and the next calendar year. The request is treated as accepted if the Tax Administration does not decide within 8 days (Art. 90.h).
- **EU SME scheme.** A business from another member state can use the Croatian exemption if its EU-wide turnover is not more than **EUR 100,000** and its Croatian supplies are not more than EUR 60,000 (Art. 90(2)). It needs an EX number from its home state (Art. 90(5) and (6)) and files a quarterly report there within one month of each quarter (Art. 90.b).
- **Exempt small businesses still file a PDV return** when they supply services to taxable persons in other EU states or third countries where the customer accounts for the VAT (Art. 85(3)).
- **Non-established businesses.** A foreign business without a Croatian establishment that sells to a Croatian VAT-registered customer does not charge Croatian VAT. The customer pays it (Art. 75(1) point 6 and 75(2)). A foreign business that sells to consumers in Croatia registers and files monthly (Art. 84(4)), unless it uses the OSS or IOSS schemes.

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source URL |
|---|---|---|---|
| Standard rate | 25% | 2026 | https://porezna-uprava.gov.hr/hr_propisi/_layouts/15/in2.vuk2019.sp.propisi.intranet/propisi.aspx (ZPDV Art. 38(1)) |
| Reduced rate: accommodation, newspapers and magazines (other than dailies), child car seats and nappies, menstrual products, water supply, electricity, natural gas and heating, firewood and pellets, municipal waste collection, urns and coffins, certain author and performer services, preparing and serving food and desserts in catering | 13% | 2026 | https://porezna-uprava.gov.hr/hr_propisi/_layouts/15/in2.vuk2019.sp.propisi.intranet/propisi.aspx (ZPDV Art. 38(3)) |
| Reduced rate: bread, milk, specialist and educational books, approved medicines, certain disability aids, cinema, concert, sporting and cultural tickets, daily newspapers, scientific journals, baby food, edible oils and fats, butter and margarine, live animals, fresh meat, fish and shellfish, fresh vegetables, fruit and nuts, eggs, seedlings and seeds, fertilisers and pesticides, animal feed (not pet food) | 5% | 2026 | https://porezna-uprava.gov.hr/hr_propisi/_layouts/15/in2.vuk2019.sp.propisi.intranet/propisi.aspx (ZPDV Art. 38(2)) |
| Temporary rate: natural gas (from 1 April 2022), heating from heating plants, firewood, pellets, briquettes, wood chips | 5% to 31 March 2027 | 2026 | https://narodne-novine.nn.hr/clanci/sluzbeni/2026_03_32_377.html (ZPDV Art. 38(4) and (5)) |
| Supply and installation of solar panels on homes and public-interest buildings | 0% | 2026 | https://porezna-uprava.gov.hr/hr_propisi/_layouts/15/in2.vuk2019.sp.propisi.intranet/propisi.aspx (ZPDV Art. 38(6)) |
| Government power to set the rate on excise energy products by decree | rate set by decree | from May 2026 | https://narodne-novine.nn.hr/clanci/sluzbeni/2026_05_48_578.html (ZPDV Art. 38.a) |
| Small business exemption (domestic annual turnover) | EUR 60,000 | 2026 | https://narodne-novine.nn.hr/clanci/sluzbeni/2024_12_152_2508.html (ZPDV Art. 90(1)) |
| EU SME scheme, EU-wide annual turnover cap | EUR 100,000 | 2026 | https://narodne-novine.nn.hr/clanci/sluzbeni/2024_12_152_2508.html (ZPDV Art. 90(2)) |
| Quarterly periods allowed if prior-year supplies including VAT were below | EUR 110,000 | 2026 | https://porezna-uprava.gov.hr/hr_propisi/_layouts/15/in2.vuk2019.sp.propisi.intranet/propisi.aspx (ZPDV Art. 84(2)) |
| Cash accounting allowed if prior-year supplies excluding VAT were not above | EUR 2,000,000 | 2026 | https://porezna-uprava.gov.hr/hr_propisi/_layouts/15/in2.vuk2019.sp.propisi.intranet/propisi.aspx (ZPDV Art. 125.i(1)) |
| Intra-EU distance sales and e-services to consumers taxed in Croatia while EU-wide total stays at or below | EUR 10,000 | 2026 | https://porezna-uprava.gov.hr/hr_propisi/_layouts/15/in2.vuk2019.sp.propisi.intranet/propisi.aspx (ZPDV Art. 26.a) |
| Acquisition threshold for exempt businesses and non-taxable legal persons | EUR 10,000 | 2026 | https://porezna-uprava.gov.hr/hr_propisi/_layouts/15/in2.vuk2019.sp.propisi.intranet/propisi.aspx (ZPDV Art. 5(2)) |
| Input VAT blocked on passenger cars and related costs | 50% | 2026 | https://porezna-uprava.gov.hr/hr_propisi/_layouts/15/in2.vuk2019.sp.propisi.intranet/propisi.aspx (ZPDV Art. 61(2)) |
| Capital goods adjustment period: movable fixed assets / real estate | 5 years / 10 years | 2026 | https://porezna-uprava.gov.hr/hr_propisi/_layouts/15/in2.vuk2019.sp.propisi.intranet/propisi.aspx (ZPDV Art. 64(1)) |
| No capital goods adjustment if the input VAT to adjust per asset is below | EUR 135 | 2026 | https://porezna-uprava.gov.hr/hr_propisi/_layouts/15/in2.vuk2019.sp.propisi.intranet/propisi.aspx (ZPDV Art. 64(4)) |
| Refund of excess input VAT, Tax Administration deadline | 30 days from filing the return | 2026 | https://porezna-uprava.gov.hr/hr_propisi/_layouts/15/in2.vuk2019.sp.propisi.intranet/propisi.aspx (ZPDV Art. 66(2)) |

## The taxable base

- **Base.** VAT is charged on the consideration for each supply, excluding the VAT itself. Discounts granted at the time of supply and early-payment discounts are left out (Art. 33).
- **Rate choice.** Use the rate for the item as listed in Art. 38. Anything not listed is 25%. Goods in Art. 38(2) points j) to z) and Art. 38(3) points g) and h) follow the Combined Nomenclature codes in the Rulebook (Art. 38(7)).
- **Exempt without deduction.** Universal postal services, hospital and medical care, education, financial and insurance services, residential and most real estate supplies, and the other public-interest supplies in Arts. 39 and 40. No input VAT is deductible on costs used for them.
- **Exempt with deduction.** Exports (Art. 45), intra-EU supplies of goods to VAT-registered customers (Art. 41) and the other supplies in Arts. 43 to 53.
- **Input VAT.** A registered business deducts VAT on purchases used for taxable supplies (Arts. 57 and 58). It cannot deduct:
  - VAT on entertainment of business partners: gifts, hospitality, holidays, sport and leisure, and hire of cars, boats, aircraft or holiday homes for them (Art. 61(1));
  - 50% of the VAT on buying or leasing passenger cars (up to 8 passenger seats) and on all related goods and services, such as fuel and servicing (Art. 61(2)). The block does not apply to cars used for driving schools, testing, servicing, carrying passengers or goods, funeral transport, rental, or bought for resale, nor to certain N1 vans (Art. 61(3)).
- **Mixed use.** A business with taxable and exempt supplies deducts a pro-rata share. The share is taxable turnover over total turnover for the year, rounded up to the next whole percent. During the year it uses last year's share and corrects in the last return of the year (Art. 62).
- **Capital goods.** If deduction conditions change within 5 years (10 for real estate), correct 1/5 (or 1/10) of the VAT per year after the change (Art. 64).
- **Cash accounting.** A business with prior-year supplies of not more than EUR 2,000,000 excluding VAT can account for VAT when paid and deduct input VAT when it pays (Art. 125.i). Its invoices must say "obračun prema naplaćenim naknadama". It does not cover intra-EU supplies of goods (Art. 125.j).

## Deadlines and filing

| What | Period | Deadline (2026) | Source |
|---|---|---|---|
| PDV return (Obrazac PDV) | month; or quarter if eligible | last day of the month after the period | ZPDV Art. 85(6) |
| Payment of VAT due | same period | last day of the month after the period | ZPDV Art. 76(1) |
| PDV-S (EU acquisitions and EU services received) | month | last day of the following month | ZPDV Art. 86(2) |
| ZP (EU sales list) | month | last day of the following month | ZPDV Art. 88(2); Rulebook |
| Notice of a bad-debt base correction | with the PDV return | same as the return | ZPDV Art. 85(11) |
| New means of transport, EU supply or acquisition | per transaction | 10 days from the supply or acquisition, to Customs | ZPDV Art. 87 |
| E-invoice fiscalisation, issuer | per invoice | when the e-invoice is issued (self-billing: 5 working days) | Zakon o fiskalizaciji Art. 48(3) |
| E-invoice fiscalisation, recipient | per invoice | within 5 working days of receipt | Zakon o fiskalizaciji Art. 48(4) |
| E-reporting of payments received on e-invoices | month | 20th of the following month | Zakon o fiskalizaciji Art. 53(1) |
| E-reporting of rejected e-invoices | month | 20th of the following month | Zakon o fiskalizaciji Art. 52(1) |

- **Tax period.** The period is the calendar month (Art. 84(1)). A business whose supplies including VAT in the prior year were below EUR 110,000 uses calendar quarters, and may choose months instead (Art. 84(2)). Quarters are not available to a business that carries out intra-EU transactions (Art. 84(3)), or to a foreign business registered in Croatia (Art. 84(4)).
- **The return.** Filed electronically through ePorezna on Obrazac PDV. Part I holds exempt and non-taxable supplies, including the domestic reverse charge sales (I.1), intra-EU goods (I.3) and B2B services to other EU states (I.4). Part II holds output VAT by rate (II.1 at 5%, II.2 at 13%, II.3 at 25%), domestic reverse charge received (II.4), EU acquisitions (II.5 to II.7), EU services received (II.8 to II.10) and other reverse charge supplies from non-established suppliers (II.11 to II.13). Part III holds input VAT on the same lines. Part IV is the net amount to pay or reclaim (Rulebook Arts. 174 to 177).
- **Year-end.** The return for the last period of the year must carry all annual corrections, including the final pro-rata (Art. 85(7)).
- **Refunds.** Excess input VAT is refunded or carried forward. If a refund is asked for, the Tax Administration must pay within 30 days of the return being filed, or within 90 days of starting an audit (Art. 66).
- **E-invoicing (Fiskalizacija 2.0).** From 1 January 2026 a VAT-registered business established in Croatia must issue e-invoices to business customers for domestic transactions (Zakon o fiskalizaciji Art. 38(1) point 1 and (2)). Every business must be able to receive them (Art. 41). Both issuer and recipient fiscalise each e-invoice in the Tax Administration's system (Arts. 47 and 48). Each line carries a six-digit KPD product code (Art. 42). Income-tax and profit-tax payers outside the VAT register, and public bodies outside it, must issue e-invoices from 1 January 2027 (Art. 80). They can use the free MIKROeRAČUN application (Arts. 54 and 55). E-invoices are kept for 6 years (Art. 35).
- **Cash and card sales to consumers** stay under fiscalisation of receipts, not e-invoices (Zakon o fiskalizaciji Art. 39).

## Penalties and interest

- **VAT Act misdemeanours, Art. 131.** A fine of **EUR 260 to EUR 66,360** for the taxpayer, and EUR 130 to EUR 6,630 for the responsible person in a legal entity. It covers, among others: wrong base or rate, wrongful exemption, deducting blocked input VAT, not paying on time, not issuing an invoice, not filing the PDV return on time (Art. 85(6)), missing year-end corrections, not filing the PDV-S or ZP on time.
- **Art. 130.** A fine of **EUR 130 to EUR 26,540** for the taxpayer (EUR 60 to EUR 5,300 for the responsible person). It covers, among others: not self-assessing reverse charge VAT, not registering or not requesting a VAT number, and invoices missing required details.
- **Fiscalisation Act fines.**
  - Not issuing or receiving e-invoices, or not fiscalising them: legal persons EUR 3,980 to EUR 66,360; craftsmen and other self-employed individuals EUR 3,980 to EUR 39,810; responsible persons EUR 660 to EUR 6,630 (Art. 71).
  - Not fiscalising an e-invoice in the required way and time: legal persons EUR 2,650 to EUR 66,360; self-employed individuals EUR 1,320 to EUR 39,810 (Art. 72).
  - Late or missing e-reporting of payments or rejections, or no KPD codes: legal persons EUR 1,320 to EUR 26,540 (Art. 73).
- **Interest.** Interest runs on unpaid VAT from the due date (OPZ Art. 130(3)), at the rate set by a separate regulation (OPZ Art. 130(1)).
- **Limitation.** The right to assess and collect tax and interest expires 6 years after the end of the year in which the liability arose (OPZ, limitation article).
- **Business closure.** Where tax is unpaid, the Tax Administration can ban the business from operating until payment, by sealing its premises (ZPDV Art. 128).

## Cross-border points

- **B2B services received from abroad.** The general place of supply is the customer's seat (Art. 17(1)). A Croatian VAT-registered customer self-assesses VAT at the Croatian rate. EU services go in II.8 to II.10 and the PDV-S. Non-EU services and goods from non-established suppliers go in II.11 to II.13. The matching input VAT goes in Part III if the business has full deduction. The VAT is treated as paid when it is reported in the return (Art. 76(4)).
- **B2B services supplied abroad.** No Croatian VAT under Art. 17(1). Report EU customers in I.4 and in the ZP.
- **Intra-EU goods.** Supplies to VAT-registered customers in other EU states are exempt with deduction (Art. 41) and go in I.3 and the ZP. Acquisitions are self-assessed (Art. 75(1) point 3).
- **Domestic reverse charge (Art. 75(3)).** The Croatian VAT-registered customer pays the VAT on construction services (including supplied staff doing construction work), used materials and waste, real estate where the seller opted to tax, real estate sold in enforcement, greenhouse gas emission allowances, and rebar steel and products made from it.
- **Imports.** Import VAT is paid to Customs. A registered business with full deduction can instead report it in the return (II.15 and III.14) if it requests this on the customs declaration (Art. 76(8)).
- **Distance sales and e-services to EU consumers.** Croatian VAT applies while EU-wide sales stay at or below EUR 10,000. Above that, the customer's state taxes them, and the OSS can be used (Art. 26.a).
- **E-invoicing scope.** The e-invoice rules cover domestic transactions only (Zakon o fiskalizaciji Art. 33(3)).

## Worked examples

### Example 1: monthly return for July 2026 with blocked costs and an EU service

A Zagreb d.o.o. files monthly. In July 2026 it invoices domestic customers EUR 40,000 net at 25% and EUR 8,000 net of catering at 13%. Its domestic purchase invoices show EUR 6,000 of input VAT. That includes EUR 250 of VAT on a client dinner, which is entertainment and fully blocked (Art. 61(1)). It also includes EUR 400 of VAT on leasing a passenger car used by a director, of which 50% is blocked (Art. 61(2)). It buys EUR 2,000 of advertising from Google Ireland. It self-assesses 25% in II.10 and deducts the same in III.10, and reports the service in the PDV-S. The return, the PDV-S and the payment are all due by 31 August 2026.

```oa-check
name: Example 1, monthly PDV return July 2026 with blocked entertainment, 50% car block and EU reverse charge
inputs:
  sales_25: 40000
  sales_13: 8000
  input_vat_domestic: 6000
  entertainment_vat: 250
  car_vat: 400
  eu_services: 2000
steps:
  - output_25: sales_25 * 0.25
  - output_13: sales_13 * 0.13
  - reverse_charge_vat: eu_services * 0.25
  - total_output: output_25 + output_13 + reverse_charge_vat
  - car_vat_blocked: car_vat * 0.5
  - deductible_domestic: input_vat_domestic - entertainment_vat - car_vat_blocked
  - total_input: deductible_domestic + reverse_charge_vat
  - vat_payable: total_output - total_input
expected:
  output_25: 10000
  output_13: 1040
  reverse_charge_vat: 500
  total_output: 11540
  car_vat_blocked: 200
  deductible_domestic: 5550
  total_input: 6050
  vat_payable: 5490
```

### Example 2: quarterly filer with domestic reverse charge and a refund

A building contractor (obrt) in Split had 2025 supplies of EUR 85,000 net, all at 25%. Including VAT that is EUR 106,250, below EUR 110,000, and it makes no intra-EU transactions, so it files quarterly in 2026 (Art. 84(2) and (3)). In January to March 2026 it invoices EUR 18,000 net of work to private homeowners at 25%. A subcontractor does EUR 20,000 of construction work for it. That falls under the domestic reverse charge (Art. 75(3)(a)). The contractor self-assesses 25% in II.4 and deducts it in III.4. It also buys a concrete mixer for EUR 30,000 plus EUR 7,500 VAT. Input VAT is higher than output VAT, so it asks for a refund in the return. The return is due by 30 April 2026. Under the old law it would have been 20 April. The Tax Administration must pay the refund within 30 days of filing (Art. 66(2)).

```oa-check
name: Example 2, quarterly PDV return Q1 2026 with construction reverse charge and refund
inputs:
  supplies_2025_net: 85000
  quarterly_limit: 110000
  sales_25: 18000
  construction_received: 20000
  equipment_vat: 7500
steps:
  - supplies_2025_gross: supplies_2025_net * 1.25
  - headroom_quarterly: quarterly_limit - supplies_2025_gross
  - output_sales: sales_25 * 0.25
  - reverse_charge_vat: construction_received * 0.25
  - total_output: output_sales + reverse_charge_vat
  - total_input: equipment_vat + reverse_charge_vat
  - net_position: total_output - total_input
  - refund: max(total_input - total_output, 0)
expected:
  supplies_2025_gross: 106250
  headroom_quarterly: 3750
  output_sales: 4500
  reverse_charge_vat: 5000
  total_output: 9500
  total_input: 12500
  net_position: -3000
  refund: 3000
```

## Ask the client first

1. What was your domestic turnover in 2025 and so far in 2026, and on what date did it pass EUR 60,000? Are you in the VAT register, and since when?
2. Were your 2025 supplies including VAT below EUR 110,000, and do you buy or sell goods or services across EU borders? This decides monthly or quarterly filing.
3. What exactly do you sell? Check each item against the 5% and 13% lists, and say whether you make exempt supplies (financial, medical, education, residential property).
4. Do you buy construction work, scrap, rebar or property from other Croatian VAT payers, or services and goods from foreign suppliers?
5. Do you have passenger cars, entertainment costs or mixed-use assets on the books?
6. Are you issuing and receiving e-invoices through an information intermediary or MIKROeRAČUN, and are payment and rejection reports filed by the 20th?

## Sources

| Source | URL | Read on |
|---|---|---|
| Zakon o porezu na dodanu vrijednost, consolidated text NN 73/13 to 32/26 (in force from 30 March 2026), Tax Administration register of regulations, Porezi > Porez na dodanu vrijednost | https://porezna-uprava.gov.hr/hr_propisi/_layouts/15/in2.vuk2019.sp.propisi.intranet/propisi.aspx | 2026-10-23 |
| Zakon o izmjenama i dopunama ZPDV, NN 152/2024 (EUR 60,000 threshold, EU SME scheme, from 1 January 2025) | https://narodne-novine.nn.hr/clanci/sluzbeni/2024_12_152_2508.html | 2026-10-23 |
| Zakon o izmjenama i dopunama ZPDV, NN 151/2025 (deadlines moved to the last day of the month, from 1 January 2026) | https://narodne-novine.nn.hr/clanci/sluzbeni/2025_12_151_2262.html | 2026-10-23 |
| Zakon o izmjeni ZPDV, NN 32/2026 (5% on gas and heating extended to 31 March 2027) | https://narodne-novine.nn.hr/clanci/sluzbeni/2026_03_32_377.html | 2026-10-23 |
| Zakon o dopuni ZPDV, NN 48/2026 (Article 38.a, energy rate by decree) | https://narodne-novine.nn.hr/clanci/sluzbeni/2026_05_48_578.html | 2026-10-23 |
| Pravilnik o porezu na dodanu vrijednost, consolidated text to NN 11/26 (Obrazac PDV lines, Arts. 174 to 178; ZP deadline), Tax Administration register | https://porezna-uprava.gov.hr/hr_propisi/_layouts/15/in2.vuk2019.sp.propisi.intranet/propisi.aspx | 2026-10-23 |
| Pravilnik o izmjeni Pravilnika o PDV-u, NN 35/2026 | https://narodne-novine.nn.hr/clanci/sluzbeni/2026_04_35_427.html | 2026-10-23 |
| Zakon o fiskalizaciji, NN 89/2025 (e-invoicing, e-reporting, fines, start dates) | https://narodne-novine.nn.hr/clanci/sluzbeni/2025_06_89_1233.html | 2026-10-23 |
| Tax Administration, Fiskalizacija 2.0 / eRačun (non-VAT-registered issue e-invoices from 1 January 2027) | https://porezna-uprava.gov.hr/hr/fiskalizacija-2-0-eracun/8073 | 2026-10-23 |
| Opći porezni zakon, consolidated text to NN 151/25 (interest, limitation), Tax Administration register, Porezni postupak | https://porezna-uprava.gov.hr/hr_propisi/_layouts/15/in2.vuk2019.sp.propisi.intranet/propisi.aspx | 2026-10-23 |

Not yet confirmed: whether the Government has issued any decree under Article 38.a setting a different rate on fuels (none found by title in NN issues 1 to 120 of 2026); the rate of late-payment interest on tax debts for 2026 (the OPZ points to a separate regulation that was not read); whether receiving EU services alone counts as an "intra-EU transaction" that rules out quarterly filing under Article 84(3); the exact treatment of the single supply that takes a small business over EUR 60,000 (Article 90.f(2) says the exemption stops "from the moment" the threshold is passed); the Rulebook amendments in NN 11/26 beyond the PDV form lines, which were not read in full.
