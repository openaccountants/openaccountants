---
name: hr-cross-border
description: "Croatian cross-border tax for tax year 2026 (Profit Tax Act NN 177/04 as amended to NN 151/25, Personal Income Tax Act NN 115/16 as amended to NN 152/24, General Tax Act NN 115/16). Covers residence of individuals (home or habitual abode of 183 days) and companies (registered seat or place of effective management), how non-residents are taxed, permanent establishment, withholding tax under Profit Tax Act article 31 (15% interest and royalties, 10% dividends, 10% foreign performers, 25% on payments and listed services to EU-listed non-cooperative jurisdictions), EU directive exemptions, 12% tax on dividends and interest paid to non-resident individuals, treaty relief claim forms, foreign tax credit, and the company exit tax with five-period spreading. Trigger on: Croatia withholding tax, porez po odbitku, Croatian non-resident, move to Croatia, leave Croatia, exit tax Croatia, PE in Croatia. Out of scope: hr-corporate-income-tax, croatia-income-tax, croatia-payroll, croatia-social-contributions, croatia-vat-return."
jurisdiction: HR
category: international
tax_year: 2026
tier: 2
last_updated: 2026-10-23
version: 0.1
verified_by: pending
---

# Croatia cross-border tax: residence, non-residents, withholding, exit (tax year 2026)

Source-cited draft: not reviewed by an accountant, not for filing.

Croatia taxes on the calendar year for individuals and, as a rule, for companies (Profit Tax Act, art. 29(1)). The authority is the Tax Administration (Porezna uprava). Currency: euro. Article numbers below are to the Profit Tax Act (Zakon o porezu na dobit, "ZPD"), the Personal Income Tax Act (Zakon o porezu na dohodak, "ZPDoh"), the General Tax Act (Opći porezni zakon, "OPZ") and the Profit Tax Rulebook (Pravilnik o porezu na dobit). The 2026 amendments to the Profit Tax Act (NN 151/25, in force 1 January 2026) rewrote the foreign tax credit (art. 30) but did not touch the article 31 withholding rates.

This skill links to its siblings instead of repeating them:

- `hr-corporate-income-tax`: the company return. Note that it still carries 2025 text and lists a 15% withholding on market research, advisory and audit services; see "Services" below for why that no longer applies to ordinary payees.
- `croatia-income-tax`: the personal return, rates and allowances in full.
- `croatia-payroll` and `croatia-social-contributions`: payroll withholding, JOPPD and contributions.
- `croatia-vat-return`: VAT on services bought from non-residents.
- `hr-transfer-pricing`: related-party pricing, documentation and the 2026 related-party loan rate.

## Who this applies to

**Individuals.** A resident is an individual with a home (prebivalište) or habitual abode (uobičajeno boravište) in Croatia. A person without either who works in the Croatian state service and is paid for it is also resident (ZPDoh, art. 3). A non-resident is an individual with neither who earns income taxable under the Act (ZPDoh, art. 4).

- **Home:** a dwelling owned or possessed for at least 183 days without a break, in one or two calendar years. Living in it is not required (OPZ, art. 43(1)).
- **Home in Croatia and abroad:** the person has the home where the family home is. A single person, or one whose family home cannot be fixed, has it in the state from which he mainly goes to work or where he mainly stays. If the other state does not treat him as its tax resident, he has the home in Croatia (OPZ, art. 43(3) and (4), as amended by NN 106/18).
- **Habitual abode:** a continuous or connected stay of at least 183 days in one or two calendar years. Short breaks of up to one year do not count (OPZ, art. 43(5)).

A resident is taxed on worldwide income. A non-resident is taxed only on income earned in Croatia (ZPDoh, art. 6). In the year a person becomes resident or stops being resident, the tax period is split into the resident and non-resident parts (ZPDoh, art. 7(2) point 1). The Tax Administration asks for questionnaire TU on arrival (non-resident to resident) and TI on departure (resident to non-resident) (Tax Administration, residence page).

**Companies.** A legal or natural person is resident if its seat is entered in a court or other register in Croatia, or its place of effective management and supervision is in Croatia. A natural-person entrepreneur with a home or habitual abode in Croatia whose business is registered is also resident (ZPD, art. 3(1)). A resident company is taxed on profit earned in Croatia and abroad; a non-resident only on profit earned in Croatia (ZPD, art. 5(2) and (3)). A Croatian branch of a foreign business (poslovna jedinica) is itself a taxpayer (ZPD, art. 2(2) and art. 4).

**Permanent establishment** (OPZ, art. 45, as replaced by NN 106/18). A fixed place of business through which a non-resident carries on business, in particular a place of management, branch, office, factory, workshop or mine. Also:

- a building site or construction or installation project lasting more than six months;
- services, including consulting, through employees or other staff, for the same or a connected project, lasting more than three months in total in any twelve-month period;
- a dependent agent who habitually concludes contracts, or plays the principal role in concluding them, for the non-resident.

Storage, display, delivery, purchasing, information gathering and other preparatory or auxiliary activities do not create a PE, unless they form part of a cohesive business with a related party in Croatia (art. 45(6) and (7)). Income from Croatian real estate can be taxed whatever the thresholds (art. 45(5)).

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| Withholding: interest and royalties (copyright and other IP, including software that carries IP rights) paid to a foreign person that is not a natural person | 15% of gross | 2026 | ZPD art. 31(4) and (6) as amended by NN 114/23: https://narodne-novine.nn.hr/clanci/sluzbeni/2023_10_114_1613.html |
| Withholding: dividends and profit shares paid to a foreign person that is not a natural person | 10% of gross | 2026 | ZPD art. 31(7), NN 114/23 |
| Withholding: fees for performances of foreign artists, entertainers and athletes paid to a foreign entity | 10% of gross; no personal income tax or contributions for the performer | 2026 | ZPD art. 31(10), NN 138/20: https://narodne-novine.nn.hr/clanci/sluzbeni/2020_12_138_2627.html |
| Withholding: all payments taxable under art. 31, plus market research, tax and business advisory and audit services, paid to persons seated or managed in a jurisdiction on the EU list of non-cooperative jurisdictions with which Croatia applies no tax treaty | 25% of gross | 2026 | ZPD art. 31(12), NN 114/23 |
| Interest exempt from withholding | commodity credits for goods used in the business; loans from a foreign bank or other financial institution; interest to foreign legal-person bondholders | 2026 | ZPD art. 31(5): https://narodne-novine.nn.hr/clanci/sluzbeni/2004_12_177_3067.html |
| EU Interest and Royalties Directive exemption | 0%: associated companies, direct holding of at least 25% either way or by a common parent, held 24 months without a break, or paid exempt before 24 months against a bank guarantee (ZPD art. 31.b(4), Rulebook art. 51.a(13)); EEA companies too, and under the Rulebook Swiss companies (Rulebook art. 51.a(11)) | 2026 | ZPD arts. 31.a, 31.b, 31.f; NN 57/06: https://narodne-novine.nn.hr/clanci/sluzbeni/2006_05_57_1354.html |
| EU Parent-Subsidiary Directive exemption on dividends | 0%: EU parent holding at least 10% of capital for 24 months without a break, or paid exempt before 24 months against a bank guarantee (Rulebook art. 51.b(4)); EEA companies too, and under the Rulebook Swiss companies (Rulebook art. 51.b(7)) | 2026 | ZPD arts. 31.e, 31.f; NN 22/12: https://narodne-novine.nn.hr/clanci/sluzbeni/2012_02_22_571.html |
| Non-resident individual: interest and dividends from Croatia (capital income) | 12%, withheld by the payer | 2026 | ZPDoh art. 70(1) and (19) as amended by NN 114/23: https://narodne-novine.nn.hr/clanci/sluzbeni/2023_10_114_1609.html |
| Capital gains on financial assets (residents; non-residents on Croatian-source gains) | 12%; no tax if held more than two years | 2026 | ZPDoh art. 67(8), art. 70(4), NN 114/23 |
| Corporate profit tax rate (non-resident PE profit, exit tax base) | 10% if revenue in the period is up to EUR 1,000,000; 18% if more than EUR 1,000,000 | 2026 | ZPD art. 28, NN 114/23 |
| Personal income tax, default where the municipality has not set rates | 20% up to EUR 60,000 a year; 30% above | 2026 | ZPDoh art. 19.a(5), NN 152/24: https://narodne-novine.nn.hr/clanci/sluzbeni/2024_12_152_2505.html |
| Range a local unit may set (Grad Zagreb) | lower rate 15% to 23%; higher rate 25% to 33% | 2026 | ZPDoh art. 19.a(2), NN 152/24 |
| Basic personal allowance, residents and non-residents (non-residents only for months with Croatian income) | EUR 600 a month | 2026 | ZPDoh arts. 14(1) and 16(1), NN 152/24 |
| PE: building site or installation project | more than 6 months | 2026 | OPZ art. 45(3), NN 106/18: https://narodne-novine.nn.hr/clanci/sluzbeni/2018_11_106_2065.html |
| PE: services through staff | more than 3 months in any 12-month period | 2026 | OPZ art. 45(4), NN 106/18 |
| Home or habitual abode test | at least 183 days in one or two calendar years | 2026 | OPZ art. 43: https://narodne-novine.nn.hr/clanci/sluzbeni/2016_12_115_2519.html |
| Tax loss carry-forward (companies) | 5 years | 2026 | ZPD art. 17(2), NN 177/04 |
| Treaty example: Cyprus (in force from 1 January 2024) | royalties 5%, interest 5%, dividends 5% | 2026 | Tax Administration, treaty table: https://porezna-uprava.gov.hr/hr/dvostruko-oporezivanje/3997 |

**Services.** The Profit Tax Act once taxed market research, tax and business advisory and audit services paid abroad at 15% (original art. 31(6), NN 177/04). Before NN 114/23 that services clause was paragraph 6 and the 15% rate paragraph 7. NN 114/23 (published 4 October 2023, in force on the eighth day after; applied to tax periods from 1 January 2024: arts. 9, 13(1) and 15) replaced paragraph 6 with the general 15% rate and paragraph 7 with the 10% dividend rate, and dropped the services clause. The consolidated Act in force for 2026 lists in paragraph 4 only interest, dividends, profit shares and intellectual property rights. Those services now appear only in paragraph 12, so they bear withholding only at 25%, and only when paid to a listed non-cooperative jurisdiction with no Croatian treaty. Paid to any other non-resident, they bear no Croatian withholding. Some Tax Administration guidance pages still list these services among withholding items; the Act governs.

## The taxable base

**Withholding.** The payer is the taxpayer. The base is the gross fee the Croatian payer pays to the foreign recipient (ZPD, art. 31(2) and (3)). Where VAT is charged on a royalty, withholding is on the amount without VAT, and interest settled without a cash payment counts as paid (Rulebook, art. 49(1) and (3)). A Croatian branch that pays interest, dividends or royalties to its foreign head office withholds too. A fee that is booked as income of a Croatian branch of the foreign recipient is not subject to withholding (ZPD, art. 31(8) and (9)). Software bought for use is not a royalty; software licensed with rights to resell or develop it is (Rulebook, art. 49(6)).

**Which list.** Whether the 25% rate applies is decided by the EU list of non-cooperative jurisdictions in the Official Journal and on the Council website on the day of payment (Rulebook, art. 50(10)).

**Non-resident individuals.** Croatian-source employment, business, property, capital and other income is taxed (ZPDoh, art. 6(2)). Employment income gets the EUR 600 monthly allowance only for months with Croatian income (ZPDoh, art. 16(1)). An EU or EEA resident who earns at least 90% of world income in Croatia, exempt in the home state, may claim resident allowances for the whole year in the annual return (ZPDoh, art. 16(3)). Dividends and interest are taxed at 12% by withholding at payment. Performers paid through a foreign entity fall under the 10% profit-tax withholding instead (ZPDoh, art. 6(3)).

**Non-resident companies with a PE** pay profit tax on the PE's Croatian profit at the article 28 rate.

**Foreign tax credit, companies** (ZPD, art. 30, rewritten by NN 151/25 from 1 January 2026):

1. A foreign PE that files and pays profit tax abroad: its positive foreign base goes into the Croatian base and the foreign tax is credited in the same period. The credit is the Croatian rate (art. 28) applied to the foreign base, capped at the Croatian tax and at the foreign tax paid (art. 30(1) and (2)).
2. Foreign withholding paid under a treaty: credited in the same period, capped at the Croatian tax and at the foreign tax paid (art. 30(4)).
3. Foreign withholding with no treaty, or not covered by one: it reduces the tax base instead (art. 30(5)).
4. Only tax that cannot be refunded abroad counts, and only with a certificate from the foreign authority (art. 30(6)). Foreign tax above the creditable cap cannot be deducted from the base (Rulebook, art. 52(4), NN 39/26).

**Foreign tax credit, individuals.** Tax paid abroad is credited item by item, only with a foreign authority certificate, and not where it was paid against the terms of an applicable treaty (ZPDoh, art. 80(2) to (4)).

**Leaving Croatia: companies (exit tax).** The taxpayer adds to its base the difference between market value and tax value of assets when it (ZPD, art. 30.d, added by NN 121/19, in force 1 January 2020):

- transfers assets to its PE in another EU state or third country, and Croatia loses the right to tax them;
- transfers assets from a Croatian PE to its head office or another PE abroad, and Croatia loses the right to tax them;
- transfers the business of a Croatian PE abroad;
- transfers its tax residence abroad. Assets that stay connected with a Croatian PE are excluded (art. 30.d(2)).

Assets due to return within 12 months, and transfers for securities financing, collateral, prudential capital or liquidity management, are excluded (art. 30.d(4)). On a transfer to an EU state, or an EEA state with a recovery-assistance agreement, the amount can be included in the base over five tax periods, with a suitable guarantee and with interest (art. 30.d(6)).

**Leaving Croatia: individuals.** The Personal Income Tax Act has no exit charge on individuals. The year of departure is split: resident to the date of the change, non-resident after it (ZPDoh, art. 7(2)).

## Deadlines and filing

| Step | Deadline | Source |
|---|---|---|
| Profit-tax withholding (art. 31): calculate, withhold and pay | when the fee is paid | ZPD art. 31(11); Rulebook art. 50(4) |
| List of all fees paid to non-residents (recipient, date, amount, tax, rate) | with the profit tax return | Rulebook arts. 49(5) and 51(11) |
| Profit tax return (PD; PD-NN for 2026 periods) and payment | four months after the end of the tax period | ZPD art. 35(1) and (2); Rulebook as amended by NN 39/26: https://narodne-novine.nn.hr/clanci/sluzbeni/2026_04_39_469.html |
| Parent-Subsidiary exemption used: evidence of residence, holding and form to the Tax Administration | within 15 days of each payment | Rulebook art. 51.b(1) |
| Interest and Royalties exemption: Tax Administration certificate | applied for per contract; issued within 3 months; valid 1 year; refund claim within 2 years of payment | Rulebook art. 51.a(3) to (7) |
| Treaty claim form certified by the foreign authority | before payment; for each payment, or for frequent payments at the first payment and then every 12 months | Rulebook art. 51(5): https://narodne-novine.nn.hr/clanci/sluzbeni/2005_08_95_1885.html |
| Treaty refund after domestic rate was withheld | within 3 years from the end of the year of payment, to the Zagreb Regional Office | Rulebook art. 51(9) |
| Exit event (move of PE business or of tax residence): notify the Tax Administration | within 8 days | ZPD art. 30.d(5) |
| Resident with foreign income without a domestic payer (INO-DOH): calculate, pay and report | within 30 days of receipt | ZPDoh art. 81(1) |
| Resident taxed abroad during the year, or posted abroad: report income and foreign tax | notify within 8 days of the first receipt in the year; report by 31 January of the next year | ZPDoh art. 81(3) and (4) |
| Capital gains tax on financial assets | by the last day of February of the next year | ZPDoh art. 70(4) |

**Treaty claim forms** (Rulebook, art. 51(3)). Four forms, one per type of payment, each titled "Zahtjev ... prema Ugovoru o izbjegavanju dvostrukog oporezivanja između Republike Hrvatske i [state]":

1. reduction or refund of tax on dividends;
2. refund of tax on interest;
3. reduction, exemption or refund of tax on licence fees (royalties);
4. reduction, exemption or refund of tax on fees for activity performed in Croatia.

The non-resident has the form certified by its own tax authority and gives two copies to the Croatian payer. The payer sends one to the Tax Administration at payment and keeps one (art. 51(6)). Where the treaty removes withholding altogether, a certificate of residence from the foreign authority is enough instead of the form (art. 51(4)). If the payer holds neither at the time of payment, it must withhold at the domestic rate (art. 51(8)).

## Penalties and interest

- **Withholding not calculated in time or not paid in full** (art. 31(11)): fine of EUR 260 to EUR 26,540 for the company; EUR 260 to EUR 2,650 for the responsible person; for a repeat offence EUR 390 to EUR 39,810 and EUR 390 to EUR 3,980 (ZPD, art. 38(1) point 2, (2) and (3), amounts from NN 114/22: https://narodne-novine.nn.hr/clanci/sluzbeni/2022_10_114_1679.html).
- **Late profit tax or advance payments:** the same fine ranges (ZPD, art. 38(1) points 3 and 4).
- **Late payment interest:** runs from the due date of the tax, at the rate set by the special law (OPZ, art. 130(1) and (3)). Where an audit finds more tax, interest runs from the day the tax should have been paid (art. 130(7)).
- **Exit tax spread over five periods:** interest is charged for the deferral (ZPD, art. 30.d(6)).
- **No treaty paperwork at payment:** the payer must withhold at the domestic rate (Rulebook, art. 51(8)). The payer is the taxpayer for withholding (ZPD, art. 31(2)), so tax it fails to withhold is its own liability.

## Cross-border points

- **Treaties take priority** over domestic law in computing a resident's foreign income (ZPDoh, art. 80(1)). For withholding, the payer applies the treaty only if it holds the certified form or residence certificate at payment (Rulebook, art. 51(7) and (8)).
- **Treaty network.** The Tax Administration publishes the treaties in force with their royalty, interest and dividend rates. Treaties with the United States, Australia and New Zealand are signed but await ratification, so a payment to a US company in 2026 bears domestic withholding (Tax Administration, treaty page).
- **Dual residence of individuals.** Settled by the treaty tie-breaker (home, centre of vital interests, habitual abode, nationality, then mutual agreement), using the TU and TI questionnaires (Tax Administration, residence page).
- **Anti-abuse.** Treaty and directive benefits are denied for arrangements that are not genuine and whose main purpose, or one of them, is the tax benefit (ZPD, art. 5.a, NN 50/16 and 138/20; and arts. 31.d(3) and 31.e(3) for the directives).
- **Hybrids and CFCs.** Rules against profit shifting are in ZPD arts. 30.a to 30.i. Refer them.
- **Mutual agreement procedure.** The Tax Administration publishes MAP guidelines (updated August 2024) on its double taxation page.
- **Transfer pricing.** Related-party prices with non-residents must be at arm's length (ZPD, art. 13). See `hr-transfer-pricing`.

## Worked examples

### Example 1: payments abroad by a Croatian company in March 2026

Adria d.o.o., a Croatian resident company, makes five payments:

1. A royalty of EUR 50,000 to an unrelated US company for a trademark licence. The US treaty is not in force, so domestic law applies: 15%, EUR 7,500.
2. A dividend of EUR 200,000 to its German parent, which has held 100% for four years. Article 31.e exempts it. Adria sends evidence to the Tax Administration within 15 days.
3. Interest of EUR 30,000 on a loan from a foreign bank. Exempt under article 31(5) point 2.
4. A tax advisory fee of EUR 20,000 to a US firm. No withholding: advisory services are no longer in article 31 except at 25% for listed jurisdictions.
5. A business consulting fee of EUR 40,000 to a company seated in a jurisdiction on the EU Annex I list on the payment date, with no Croatian treaty. Article 31(12) applies: 25%, EUR 10,000.

Adria withholds EUR 17,500 in total at the time of payment and lists every payment with its PD return by 30 April 2027.

```oa-check
name: Adria d.o.o., five payments to non-residents, March 2026
inputs:
  royalty_us: 50000
  dividend_de_parent: 200000
  bank_interest: 30000
  advisory_us: 20000
  consulting_listed: 40000
steps:
  - royalty_wht: royalty_us * 0.15
  - dividend_wht: dividend_de_parent * 0
  - interest_wht: bank_interest * 0
  - advisory_wht: advisory_us * 0
  - consulting_wht: consulting_listed * 0.25
  - total_withheld: royalty_wht + dividend_wht + interest_wht + advisory_wht + consulting_wht
  - net_royalty: royalty_us - royalty_wht
  - net_consulting: consulting_listed - consulting_wht
expected:
  royalty_wht: 7500
  dividend_wht: 0
  interest_wht: 0
  advisory_wht: 0
  consulting_wht: 10000
  total_withheld: 17500
  net_royalty: 42500
  net_consulting: 30000
```

### Example 2: a company moves its tax residence to Austria (exit tax)

Lika d.o.o. completes a cross-border conversion and moves its registered seat and management to Austria on 30 June 2026. It becomes Austrian resident. On that date its assets have a market value of EUR 2,500,000 and a tax value of EUR 1,100,000. A warehouse with market value EUR 600,000 and tax value EUR 300,000 stays in a Croatian PE. Revenue in the short period to 30 June is above EUR 1,000,000, so the rate is 18%.

Exit base: the total difference of EUR 1,400,000 less the EUR 300,000 difference on the warehouse, which stays connected with the Croatian PE (art. 30.d(2)). That leaves EUR 1,100,000. Tax at 18%: EUR 198,000. Lika notifies the Tax Administration within 8 days.

Edge case: the move is to an EU state, so with a suitable guarantee Lika can include the EUR 1,100,000 over five tax periods, EUR 220,000 a period. That is EUR 39,600 of tax a period at 18%, plus interest on the deferral (art. 30.d(6)). The rate each period is set by that period's revenue; this example assumes 18% throughout.

```oa-check
name: Lika d.o.o., exit to Austria 30 June 2026, five-period spreading
inputs:
  market_value_all: 2500000
  tax_value_all: 1100000
  market_value_pe: 600000
  tax_value_pe: 300000
  rate: 0.18
  periods: 5
steps:
  - difference_all: market_value_all - tax_value_all
  - difference_pe: market_value_pe - tax_value_pe
  - exit_base: difference_all - difference_pe
  - exit_tax: exit_base * rate
  - base_per_period: exit_base / periods
  - tax_per_period: base_per_period * rate
expected:
  difference_all: 1400000
  difference_pe: 300000
  exit_base: 1100000
  exit_tax: 198000
  base_per_period: 220000
  tax_per_period: 39600
```

## Ask the client first

1. For a payment abroad: what is it for (interest, dividend, licence, software, services, performance), who is the recipient (company or individual), where is it seated and managed, and does it have a Croatian branch the income is booked to? (Decides whether art. 31 applies, and at what rate.)
2. Is the recipient's state on the EU Annex I list on the payment date, and does Croatia apply a treaty with it? (Decides the 25% rate.)
3. Do you hold the certified treaty form or residence certificate before payment, and for directive cases the holding percentage and how long it has been held? (Decides treaty or directive relief at source.)
4. For an individual: days in Croatia this year and last, any dwelling owned or rented here and for how long, where the family lives. (Decides residence under OPZ art. 43.)
5. For a foreign business working in Croatia: how long the site, project or service presence lasts, and whether anyone here signs contracts for it. (Decides PE.)
6. For a company moving assets, a PE or its residence abroad: which assets, market and tax values, which assets stay with a Croatian PE, and the destination state. (Decides exit tax and spreading.)

## Sources

| Source | URL | Read on |
|---|---|---|
| Profit Tax Act, NN 177/04 (original text, arts. 3, 5, 17, 31) | https://narodne-novine.nn.hr/clanci/sluzbeni/2004_12_177_3067.html | 2026-10-23 |
| Profit Tax Act amendment NN 57/06 (arts. 31.a to 31.d, Interest and Royalties Directive) | https://narodne-novine.nn.hr/clanci/sluzbeni/2006_05_57_1354.html | 2026-10-23 |
| Profit Tax Act amendment NN 22/12 (art. 31.e, Parent-Subsidiary Directive) | https://narodne-novine.nn.hr/clanci/sluzbeni/2012_02_22_571.html | 2026-10-23 |
| Profit Tax Act amendment NN 50/16 (art. 5.a anti-abuse) | https://narodne-novine.nn.hr/clanci/sluzbeni/2016_06_50_1336.html | 2026-10-23 |
| Profit Tax Act amendment NN 106/18 (art. 31(10) and (12)) | https://narodne-novine.nn.hr/clanci/sluzbeni/2018_11_106_2061.html | 2026-10-23 |
| Profit Tax Act amendment NN 121/19 (art. 3(2), art. 30.d exit tax, in force 1 January 2020) | https://narodne-novine.nn.hr/clanci/sluzbeni/2019_12_121_2382.html | 2026-10-23 |
| Profit Tax Act amendment NN 138/20 (art. 31(7) and (10) to 10%) | https://narodne-novine.nn.hr/clanci/sluzbeni/2020_12_138_2627.html | 2026-10-23 |
| Profit Tax Act amendment NN 114/22 (fines in euro, art. 38) | https://narodne-novine.nn.hr/clanci/sluzbeni/2022_10_114_1679.html | 2026-10-23 |
| Profit Tax Act amendment NN 114/23 (art. 28 threshold EUR 1,000,000; art. 31(6), (7), (12); art. 31.f; art. 35) | https://narodne-novine.nn.hr/clanci/sluzbeni/2023_10_114_1613.html | 2026-10-23 |
| Profit Tax Act amendment NN 151/25 (art. 30 foreign tax credit, in force 1 January 2026) | https://narodne-novine.nn.hr/clanci/sluzbeni/2025_12_151_2261.html | 2026-10-23 |
| Profit Tax Rulebook NN 95/05 (art. 51, treaty forms and procedure) | https://narodne-novine.nn.hr/clanci/sluzbeni/2005_08_95_1885.html | 2026-10-23 |
| Profit Tax Rulebook amendment NN 39/26 (art. 52, new PD and PD-NN forms for 2026) | https://narodne-novine.nn.hr/clanci/sluzbeni/2026_04_39_469.html | 2026-10-23 |
| Personal Income Tax Act NN 115/16 (arts. 3, 4, 6, 7, 16, 80, 81) | https://narodne-novine.nn.hr/clanci/sluzbeni/2016_12_115_2525.html | 2026-10-23 |
| Personal Income Tax Act amendment NN 114/23 (art. 70: 12% on interest, dividends and capital gains) | https://narodne-novine.nn.hr/clanci/sluzbeni/2023_10_114_1609.html | 2026-10-23 |
| Personal Income Tax Act amendment NN 152/24 (EUR 600 allowance; art. 19.a rate ranges, in force 1 January 2025) | https://narodne-novine.nn.hr/clanci/sluzbeni/2024_12_152_2505.html | 2026-10-23 |
| General Tax Act NN 115/16 (art. 43 home and habitual abode; art. 130 interest) | https://narodne-novine.nn.hr/clanci/sluzbeni/2016_12_115_2519.html | 2026-10-23 |
| General Tax Act amendment NN 106/18 (art. 43(3) and (4); art. 45 permanent establishment) | https://narodne-novine.nn.hr/clanci/sluzbeni/2018_11_106_2065.html | 2026-10-23 |
| Profit Tax Act, Tax Administration consolidated text to NN 151/25 (arts. 3, 17, 28, 30, 30.d, 31 to 31.f, 35, 38) | https://porezna-uprava.gov.hr/hr_propisi/_layouts/15/in2.vuk2019.sp.propisi.intranet/propisi.aspx#id=pro19 | 2026-10-23 |
| Profit Tax Rulebook, Tax Administration consolidated text to NN 39/26 (arts. 49 to 52) | https://porezna-uprava.gov.hr/hr_propisi/_layouts/15/in2.vuk2019.sp.propisi.intranet/propisi.aspx#id=pro23 | 2026-10-23 |
| Personal Income Tax Act and General Tax Act, Tax Administration consolidated texts (ZPDoh to NN 152/24; OPZ to NN 151/25, arts. 43, 45 and 130 unchanged) | https://porezna-uprava.gov.hr/Propisi | 2026-10-23 |
| Tax Administration, double taxation: treaties in force and rates | https://porezna-uprava.gov.hr/hr/dvostruko-oporezivanje/3997 | 2026-10-23 |
| Tax Administration, treaty network (treaties awaiting ratification) | https://porezna-uprava.gov.hr/hr/ugovori-o-izbjegavanju-dvostrukog-oporezivanja/7559 | 2026-10-23 |
| Tax Administration, determining tax residence (TU and TI questionnaires) | https://porezna-uprava.gov.hr/hr/utvrdjivanje-rezidentnosti-u-porezne-svrhe/3998 | 2026-10-23 |
| Tax Administration, non-resident capital income | https://porezna-uprava.gov.hr/hr/4-primici-nerezidenta-od-kapitala/4284 | 2026-10-23 |

Not yet confirmed: which jurisdictions are on the EU Annex I list on a given payment date (the Council list was not read for this skill); the late-payment interest rate for 2026 (the special law setting it was not read); the footnotes to the Tax Administration treaty table (rates shown with footnote marks, such as Austria and Belgium dividends, were not used); the Rulebook arts. 49 to 52 were read in the Tax Administration consolidated text to NN 39/26, not against each amending rulebook; whether the art. 28 rate applied to an exit base spread over five periods follows each later period's revenue.
