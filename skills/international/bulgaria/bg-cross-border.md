---
name: bg-cross-border
description: "Bulgarian cross-border tax for tax year 2026 under the Corporate Income Tax Act (ZKPO), the Personal Income Taxes Act (ZDDFL) and the Tax and Social Security Procedure Code (DOPK). Covers tax residence of individuals (permanent address, more than 183 days in 12 months, centre of vital interests) and of companies (incorporation); Bulgarian-source income of non-residents; permanent establishment and fixed base; final withholding at 5% on dividends and 10% on interest, royalties, technical services, rents, management fees and capital gains (CITA arts. 194, 195, 200; PITA arts. 37, 38, 46); the EU/EEA dividend and interest-royalty exemptions; treaty relief (DOPK arts. 135 to 142, the EUR 255,645.94 threshold); the foreign tax credit; CFC rules; and company exit tax (CITA arts. 155 to 155g). Trigger phrases: non-resident Bulgaria, Bulgarian withholding tax, SIDDO, PE Bulgaria, exit tax Bulgaria. Out of scope: rates and returns (bulgaria-income-tax, bg-corporate-income-tax), payroll (bulgaria-payroll), social contributions (bulgaria-social-contributions), VAT (bulgaria-vat-return)."
version: 0.1
jurisdiction: BG
tax_year: 2026
last_updated: 2026-10-23
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Bulgaria cross-border tax: residence, non-residents, withholding, treaties and exit (2026)

> **Source-cited draft.** Drafted from the consolidated texts of the Corporate Income Tax Act (Закон за корпоративното подоходно облагане, ZKPO, last amended ДВ бр. 55/2026), the Personal Income Taxes Act (Закон за данъците върху доходите на физическите лица, ZDDFL, last amended ДВ бр. 85/2026) and the Tax and Social Security Procedure Code (Данъчно-осигурителен процесуален кодекс, DOPK) on lex.bg, and the National Revenue Agency (NRA, НАП) pages on treaty relief and treaties in force, all read on 2026-10-23. No accountant has reviewed it. Do not file from it without review by a qualified Bulgarian professional.

This skill is the hub for cross-border questions in the Bulgaria pack. It says who Bulgaria taxes and on what, what a Bulgarian payer must withhold when money leaves Bulgaria, how a treaty rate is claimed, how a resident gets credit for foreign tax, and what a company pays when assets or residence leave Bulgaria. For the rates and returns themselves, see `bulgaria-income-tax` (individuals) and `bg-corporate-income-tax` (companies). Those two skills still carry 2025 figures.

Tax year: the calendar year. Currency: the euro from 1 January 2026. Several lev amounts in the statutes have not been rewritten. Under the Euro Introduction Act they count as euro amounts converted at BGN 1.95583 per euro and rounded to the cent (arts. 11(2), 12, 13; § 5(1) of its transitional provisions applies this to fines and sanctions); for example BGN 500,000 is EUR 255,645.94, the figure the NRA publishes. Authority: the National Revenue Agency, nra.bg. Bulgaria is an EU member, so the Parent-Subsidiary and Interest-Royalties Directives are transposed in the CITA.

## Who this applies to

**Resident individuals** (PITA art. 4). Whatever their citizenship, an individual is resident if any one of these is met:
- (1) a permanent address (постоянен адрес) in Bulgaria; but a person with a permanent address whose centre of vital interests is not in Bulgaria is not resident (art. 4(5));
- (2) presence in Bulgaria for more than 183 days in any 12-month period; the person is resident for the year in which the 183 days are exceeded; the day of leaving and the day of arriving each count as a day in Bulgaria; days spent only for study or medical treatment do not count (art. 4(2), (3));
- (3) being sent abroad by the Bulgarian state, its bodies or organisations, or by Bulgarian enterprises, together with family members;
- (4) a centre of vital interests in Bulgaria: family, property, the place from which the person works or runs a business, and the place from which the person manages property (art. 4(4)).

Residents are taxed on income from Bulgaria and abroad (art. 6). Non-residents are taxed only on Bulgarian-source income (art. 7).

**Resident companies** (CITA art. 3). A legal entity is resident if it was incorporated under Bulgarian law, or is a European company (SE) or European cooperative (SCE) with its seat in Bulgaria and entered in a Bulgarian register. There is no place-of-management test. Residents are taxed on profits from all sources (art. 3(2)). A foreign entity is taxed on profits through a Bulgarian place of business (permanent establishment), on disposals of its assets, and on Bulgarian-source income named in the CITA (art. 4(2)). Unincorporated companies are treated as legal entities (art. 2(2)). A foreign trust, fund or similar body with no identifiable owner of the income is itself taxable on Bulgarian-source income (art. 2(3)). Reverse hybrids are covered by art. 2(4).

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| Residence by presence (individuals) | More than 183 days in any 12-month period | 2026 | PITA art. 4(1)(2), [lex.bg](https://lex.bg/laws/ldoc/2135538631) |
| Corporate income tax (resident company or PE) | 10% | 2026 | CITA art. 20, [lex.bg](https://lex.bg/laws/ldoc/2135540562) |
| Dividends and liquidation shares paid to foreign companies | 5% final withholding | 2026 | CITA arts. 194(1), 200(1) |
| Dividends paid to companies resident in another EU or EEA state | Exempt, except hidden profit distributions; no minimum holding | 2026 | CITA art. 194(3)(3) |
| Interest, royalties, technical services, franchise and factoring fees, rent of movable property, management or control fees, gains on Bulgarian financial assets and real estate, paid to foreign companies | 10% final withholding | 2026 | CITA arts. 12(2), (3), (5), (8), 195(1), 200(2) |
| Penalties and compensation paid to companies in preferential tax regimes | 10% final withholding | 2026 | CITA arts. 12(9), 195(1) |
| Interest and royalties to an associated EU company (25% held for at least 2 years, beneficial owner) | Exempt | 2026 | CITA art. 195(6)(3), (7), (12) |
| Interest on listed bonds of Bulgarian issuers, the state or municipalities (regulated market or growth market in the EU or EEA) | Exempt | 2026 | CITA art. 195(6)(1), extended to growth markets from 1 Jan 2026 |
| Disposals of financial instruments as defined in the CITA | Not withheld | 2026 | CITA art. 196 |
| Dividends to individuals (resident or non-resident) | 5% final tax | 2026 | PITA arts. 38(1), 46(3) |
| Interest, rents, royalties, technical services, management fees, artists' and sportspeople's fees, paid to non-resident individuals | 10% final tax on the gross amount | 2026 | PITA arts. 37(1)(1) to (9), 37(2), 46(1) |
| Non-resident individual, gain on Bulgarian real estate | 10% of (sale price less documented cost, less 10% for expenses) | 2026 | PITA arts. 37(1)(10), 37(3), 46(1) |
| Non-resident individual, gain on shares and other financial assets | 10% of (sale price less documented cost) | 2026 | PITA arts. 37(1)(12), 37(4), 46(1) |
| Simplified treaty relief (proof given to the payer only) | Income from one payer to one foreign person up to EUR 255,645.94 (BGN 500,000) a year | 2026 | DOPK art. 142(1), [NRA](https://nra.bg/wps/portal/nra/mezhdunarodni-deinosti/siddo/prilagane-na-SIDDO) |
| NRA opinion on a treaty request (where a check is made) | Within 60 days; silence counts as an opinion that the treaty applies | 2026 | DOPK art. 141(1) to (3) |
| Treaties listed by the NRA | 71 countries, from Austria to Japan | 2026 | [NRA treaty list](https://nra.bg/wps/portal/nra/mezhdunarodni-deinosti/siddo/spisak-sas-spogodbi) |
| CFC control test | More than 50% of votes, capital or profit, with related enterprises | 2026 | CITA art. 47в(1)(1) |
| Exit tax base (companies) | Market price less tax value of transferred assets, at the 10% rate | 2026 | CITA arts. 155, 155а |
| Exit tax deferral (transfers to EU or EEA) | Five equal annual instalments, with interest | 2026 | CITA art. 155г(1), (5) |

**Treaties.** The NRA list (read 2026-10-23) shows treaties with: Albania, Algeria, Armenia, Austria, Azerbaijan, Bahrain, Belarus, Belgium, Canada, China, Croatia, Cyprus, Czech Republic, Denmark, Egypt, Estonia, Finland, France, Georgia, Germany, Greece, Hungary, India, Indonesia, Iran, Ireland, Israel, Italy, Japan, Jordan, Kazakhstan, Kuwait, Latvia, Lebanon, Lithuania, Luxembourg, Malta, Moldova, Mongolia, Montenegro, Morocco, Netherlands (new treaty in force 31 July 2021), North Korea, North Macedonia, Norway, Pakistan, Poland, Portugal, Qatar, Romania, Russia, Saudi Arabia, Serbia, Singapore, Slovakia, Slovenia, South Africa, South Korea, Spain, Sweden, Switzerland, Syria, Thailand, Turkey, Ukraine, United Arab Emirates, United Kingdom, United States, Uzbekistan, Vietnam and Zimbabwe. For several the NRA also publishes a synthesised text showing the effect of the multilateral BEPS convention. Read the treaty for the rate: this skill does not tabulate treaty rates.

## The taxable base

**Bulgarian-source income of foreign companies** (CITA art. 12). Profits from business through a Bulgarian place of business, or from disposing of its assets; income from financial assets issued by Bulgarian companies, the state and municipalities, and from deals in them; dividends and liquidation shares from Bulgarian companies; interest (including in finance lease instalments), rent of movable property, royalties, technical services fees, franchise and factoring fees, and fees for managing or controlling a Bulgarian company, when accrued by a Bulgarian payer or a Bulgarian PE; rent of and gains on Bulgarian real estate. Where the payment is made does not matter (art. 12(10)). A payment accrued through a Bulgarian company's own PE abroad is not Bulgarian-source (art. 12(6)).

**What is withheld, and what is not.** Withholding covers only the items listed in art. 12(2), (3), (5), (8) and (9). A fee for ordinary services performed outside Bulgaria, such as marketing or legal advice, is not on the list unless it is a technical service or a management or control fee. Advance payments are not withheld (art. 195(5)). The base is the gross amount; for gains on financial assets and real estate it is sale price less documented acquisition cost (art. 199). Where the payer is not a taxable person, and for gains on financial assets and on real estate, the foreign recipient pays the tax itself (arts. 195(2), (3), 202(4)).

**Permanent establishment** (DOPK § 1, item 5, applied by CITA § 1, item 2). A place of business is: (a) a fixed place, owned, rented or otherwise used, through which a foreign person carries on business in Bulgaria wholly or partly, such as a place of management, branch, registered commercial representation, office, workshop, factory, shop, warehouse, assembly site, construction site, mine or well; (b) business carried on by persons authorised to conclude contracts in the foreign person's name, other than independent agents under the Commercial Act; (c) regular commercial transactions performed in Bulgaria, even with no permanent representative and no fixed place. Domestic law sets no minimum duration for a construction site; a treaty usually does. For individuals the equivalent is a fixed base (определена база): a place for independent personal services or a liberal profession, or providing such services in Bulgaria on a lasting basis (DOPK § 1, item 7). PE profits are taxed at 10% through the annual return.

**Bulgarian-source income of non-resident individuals** (PITA art. 8). Employment income for work done in Bulgaria and fees for services performed in Bulgaria; business income through a fixed base; dividends from Bulgarian companies; and the items in art. 8(6) accrued or paid by Bulgarian residents or Bulgarian PEs (interest, royalties, technical services, management fees, rents of movable property, insurance income, prizes and more). Most of these carry a 10% final tax under art. 37 or 5% under art. 38. Employment income and other income in the general annual base go on an annual return (art. 50(2)).

**Treaty override and the relief procedure.** A ratified treaty in force takes precedence over the CITA and the PITA (CITA art. 13, PITA art. 75). In Bulgaria treaties do not apply automatically: the foreign recipient must first prove the grounds (DOPK art. 135(2)). It shows that it is resident of the other state under the treaty, is the beneficial owner (притежател) of the income, has no Bulgarian PE or fixed base the income is effectively connected with, and meets any special treaty conditions (art. 136). Residence is certified by the foreign tax administration; beneficial ownership and the absence of a PE are declared by the recipient; special conditions are proved by official documents, never by declaration (art. 137). Contracts, invoices and dividend resolutions go with it (art. 138).
- **Up to EUR 255,645.94 a year from one payer:** the proof is given to the payer, no request goes to the NRA, and the payer applies the treaty rate at source (art. 142(1)). The payer reports the income paid and the reliefs given by 31 March of the next year (art. 142(5)).
- **Above that amount within the year:** the recipient files a request on the NRA form with the territorial directorate where the payer is registered (or NRA Sofia if the payer is not registered), for the whole amount of the income (arts. 139, 142(2)). Where the NRA makes a check, it issues an opinion within 60 days; the treaty conditions count as met from the date of a positive opinion or, if the NRA says nothing, from the end of the 60 days. Where the NRA opens an audit instead and finds the grounds met, they count as met from the request date (art. 141(1) to (3)). For long-term contracts one request is enough; dividends are not long-term income (art. 140).
- **Tax already withheld:** the treaty is claimed through a refund or offset request (art. 142(3)); the NRA page says the act is issued within 30 days unless an audit is ordered.

**EU and EEA alternatives.** A company resident in the EU or EEA may elect to recompute its Bulgarian withholding tax as if it were a Bulgarian company, by annual return to NRA Sofia by 31 December of the following year; any excess is refunded to the extent it cannot be credited at home (CITA art. 202a). An EU or EEA resident individual has the same right under PITA art. 37a, through the art. 50 annual return. Income exempt under PITA art. 13 is not taxed when paid to EU or EEA residents who give the payer a residence certificate and a declaration (art. 37(7), (8)). If exempt interest or royalties under CITA art. 195(7) were taxed, the beneficial owner can ask for a refund, paid within a year of the request (art. 195(10)). If the 25% holding is broken before two years, 10% becomes due with late interest (art. 195(9)).

**Foreign tax credit for residents.** Where no treaty provision applies, a resident company credits foreign tax similar to corporate tax, and foreign tax on the gross amount of dividends, interest, royalties, technical services fees and rents (CITA art. 14(1) to (3)). The credit is computed for each country and each type of income separately and capped at the Bulgarian tax on that income (art. 14(4)). Evidence of foreign tax goes with the annual return, except where the treaty uses exemption with progression (art. 92(6)). Resident individuals have the same per-country, per-type credit (PITA art. 76) and attach evidence to the annual return (art. 50(5), (6)). Dividends a Bulgarian company receives from EU or EEA resident companies are left out of its taxable result (CITA art. 27(1)(1)), so no credit arises on them. The exclusion does not apply to hidden profit distributions or to amounts the paying company deducted (art. 27(2)).

**CFC rule** (CITA arts. 47в, 47г). A foreign entity or foreign PE is a CFC where the Bulgarian company with its related enterprises holds more than 50% of the votes, capital or profit rights, and the corporate tax actually paid abroad is lower than the difference between the Bulgarian tax that would be due and the tax actually paid. The CFC's undistributed taxable profit is added to the Bulgarian company's result in proportion to the holding, with credit for the CFC's tax under art. 14(4). The rule does not apply where the CFC carries on a substantive economic activity with the staff, equipment, assets and premises that activity needs, which the Bulgarian company must prove (art. 47г(7)).

## Deadlines and filing

| Obligation | When | Source |
|---|---|---|
| Withholding tax return (CITA arts. 194, 195) | By the end of the month after the quarter; filed with the payer's NRA directorate | CITA art. 201(1) |
| Payment of dividend withholding | By the end of the month after the quarter in which the distribution decision was taken | CITA art. 202(1); PITA art. 65(2) |
| Payment of other withholding (interest, royalties, services) | By the end of the month after the quarter in which the income was accrued | CITA art. 202(2); PITA art. 65(1) |
| Non-resident individual's own tax on gains from real estate and shares | By the end of the month after the quarter of the disposal | PITA arts. 65(6), 67(1) |
| Payer's declaration under the simplified treaty procedure | By 31 March of the following year; electronic only if more than five recipients | DOPK art. 142(5) |
| Treaty request above EUR 255,645.94 | Filed with the payer's NRA directorate; opinion within 60 days; missing items cured within 15 days of the NRA's request | DOPK arts. 139, 141 |
| Change in treaty circumstances | Notify within 30 days | DOPK art. 140(3) |
| Election to recompute withholding (EU or EEA company) | Annual return to NRA Sofia by 31 December of the following year | CITA art. 202a(4) |
| Annual corporate return of a Bulgarian PE or resident company | 1 March to 30 June of the following year; tax paid by 30 June | CITA arts. 92(2), 93(1) |
| Annual personal income tax return | 10 January to 30 April of the following year (30 June for sole traders); tax on foreign dividends paid by 30 April | PITA arts. 53(1), 67(4), (5) |
| Exit tax deferral election | Made in the annual return for the year of the transfer | CITA art. 155г(6) |
| Event ending an exit tax deferral | Notify the NRA within 14 days | CITA art. 155г(9) |

A certificate of the tax withheld for a foreign company is issued by the NRA on request (CITA art. 201(4)).

## Penalties and interest

| Failure | Penalty | Source |
|---|---|---|
| Tax not withheld and paid | The payer is jointly liable with the recipient for the tax | CITA art. 203; DOPK art. 18(1) |
| Payer under the PITA fails to withhold or pay on time | Fine or sanction up to BGN 1,000 (EUR 511.29); repeat up to BGN 2,000 (EUR 1,022.58) | PITA art. 81 |
| Return not filed, filed late, or understating tax (CITA taxpayer, including withholding returns) | BGN 500 to 3,000 (EUR 255.65 to 1,533.88); repeat BGN 1,000 to 6,000 (EUR 511.29 to 3,067.75) | CITA art. 261 |
| Art. 142(5) treaty declaration not filed on time | BGN 500 to 5,000 (EUR 255.65 to 2,556.46); repeat BGN 1,000 to 10,000 (EUR 511.29 to 5,112.92) | DOPK art. 275 |
| Holding for the interest-royalty exemption broken before 2 years | 10% withholding on the exempted income, with late interest from the original due date | CITA art. 195(9) |
| Late payment of any tax, including withheld tax not paid | Statutory interest (законна лихва) | Law on Interest on Taxes, Fees and Other Similar State Receivables, art. 1, [lex.bg](https://lex.bg/laws/ldoc/2123675140) |

The euro figures above are the lev amounts still written in the statutes, converted at the fixed rate of BGN 1.95583 and rounded to the cent, as the Euro Introduction Act requires (arts. 11(2), 12, 13 and § 5(1)). That Act sets no separate rounding rule for fines.

## Cross-border points

- **Arriving.** An individual becomes resident for the year in which presence exceeds 183 days in a 12-month period, or from the year a centre of vital interests or permanent address (with the centre of interests) is in Bulgaria. The PITA has no split-year rule; see "Not yet confirmed".
- **Leaving: individuals.** The PITA has no exit tax on an individual's private assets or shares. Once non-resident, Bulgarian dividends carry 5%, and interest, rent and royalties 10%, withheld by the payer; gains on Bulgarian real estate and Bulgarian shares stay taxable at 10% of the gain, paid by the seller (arts. 37, 65(6), 67(1)), unless a treaty or the EU/EEA exemption applies.
- **Leaving: companies** (CITA arts. 155 to 155g). Where Bulgaria loses the right to tax a later disposal, a transfer of assets or activity is taxed as if sold at market price: from a Bulgarian head office to a PE abroad; from a Bulgarian PE to another part of the enterprise abroad; on a change of tax residence to another jurisdiction (assets that stay effectively connected with a Bulgarian PE are excluded); or a transfer of a Bulgarian PE's activity abroad (art. 155(1)). The gain is market price less tax value: tax written-down value for depreciable assets, adjusted book value for others (art. 155a(2)). Transfers of up to 12 months for securities financing, collateral or prudential capital or liquidity needs are excluded if the assets return (art. 155в). For an incidental or irregular transfer to the EU, or to EEA states with an equivalent recovery assistance agreement, the tax can be paid in five equal annual instalments, with interest under the interest law. The deferral is capped at the corporate tax due for the period (art. 155г(1), (2), (5)). The deferral ends at once if the asset is sold, moved on outside the EU, the residence moves on outside the EU, the company enters insolvency or liquidation, or an instalment is more than 12 months late (art. 155г(7)). There is no deferral where the transfer and the ending event fall in the same year (art. 155г(10)).
- **Arriving: companies.** Assets transferred into Bulgaria take market price as their tax value; where the other EU state taxed the exit under the Anti-Tax Avoidance Directive, the Bulgarian value follows that state's value, unless the NRA sets a different market price (art. 155д).
- **PE drawing on its head office.** A Bulgarian PE that accrues interest, royalties and similar items to its own head office abroad withholds 10% in the cases in art. 195(4), such as where the transfer matches the head office's ordinary dealings with third parties.
- **Transfer pricing.** Transactions with related non-residents follow the arm's length rule in CITA art. 15; methods are in DOPK § 1, item 10. A separate transfer pricing skill covers documentation.

## Worked examples

### Example 1: interest and royalties to an unrelated Swiss company, above the simplified threshold

Rila Soft OOD, a Bulgarian company, owes Alpine AG, an unrelated Swiss resident company, EUR 180,000 of loan interest and EUR 120,000 of software licence royalties in 2026, all accrued in the first quarter. Alpine has no Bulgarian PE. Rila Soft also pays its Greek parent company a dividend of EUR 50,000.

Under domestic law Rila Soft withholds 10% on both items: EUR 18,000 on the interest and EUR 12,000 on the royalties, EUR 30,000 in total, payable by 30 April 2026 (end of the month after Q1). The Greek parent is an EU resident company, so its dividend is exempt (art. 194(3)(3)) and nothing is withheld. To apply the Switzerland treaty instead, Alpine must prove the grounds. Its income from Rila Soft for the year, EUR 300,000, is EUR 44,354.06 above the EUR 255,645.94 limit, so the simplified route through the payer is closed. Alpine files a request with the NRA for the whole EUR 300,000. Until the NRA opinion (60 days) or a refund, Rila Soft withholds the domestic 10%.

```oa-check
name: Bulgarian payer, interest and royalties to Swiss company, EU dividend, 2026
inputs:
  interest: 180000
  royalties: 120000
  dividend_greece: 50000
  simplified_limit: 255645.94
steps:
  - wht_interest: interest * 0.10
  - wht_royalties: royalties * 0.10
  - wht_dividend_greece: dividend_greece * 0
  - total_wht: wht_interest + wht_royalties + wht_dividend_greece
  - income_to_alpine: interest + royalties
  - excess_over_limit: max(0, income_to_alpine - simplified_limit)
expected:
  wht_interest: 18000
  wht_royalties: 12000
  wht_dividend_greece: 0
  total_wht: 30000
  income_to_alpine: 300000
  excess_over_limit: 44354.06
```

### Example 2: exit tax on a patent moved to an EU branch, with deferral

Vitosha Labs EAD, a Bulgarian company, moves a patent from its head office in Sofia to its branch in Romania in 2026. Bulgaria loses the right to tax a later sale (art. 155(1)(1)). The patent's tax value is EUR 200,000 and its market price at the transfer is EUR 1,000,000. Its other taxable profit for 2026 is EUR 400,000.

The exit gain is EUR 800,000, adding EUR 80,000 of corporate tax at 10%. Total corporate tax for 2026 is EUR 120,000, so the EUR 80,000 is within the cap on deferral (art. 155г(1)). Romania is in the EU and the transfer is a one-off, so Vitosha can elect in its 2026 return to pay the EUR 80,000 in five equal instalments of EUR 16,000: the first by 30 June 2027 with the 2026 tax, the rest in each of the next four years, with interest. If the patent were then moved on from the Romanian branch to a branch outside the EU and EEA in 2028, the unpaid balance would become due at once (art. 155г(7)(2)). Had the patent gone to a branch outside the EU and EEA, the whole EUR 80,000 would be due by 30 June 2027 with no deferral.

```oa-check
name: Bulgarian company, patent moved to EU branch, exit tax deferral, 2026
inputs:
  market_price: 1000000
  tax_value: 200000
  other_profit: 400000
steps:
  - exit_gain: market_price - tax_value
  - exit_tax: exit_gain * 0.10
  - total_cit: (other_profit + exit_gain) * 0.10
  - deferrable: min(exit_tax, total_cit)
  - instalment: deferrable / 5
  - due_first_year: total_cit - deferrable + instalment
expected:
  exit_gain: 800000
  exit_tax: 80000
  total_cit: 120000
  deferrable: 80000
  instalment: 16000
  due_first_year: 56000
```

## Ask the client first

1. **Where the person lives and for how long.** Permanent address, days in Bulgaria in any 12 months, family, property and work decide residence under PITA art. 4. For a company: where it was incorporated (CITA art. 3).
2. **The recipient's country, legal form and residence certificate.** An EU or EEA company gets dividends free of withholding; an associated EU company (25% for two years) gets interest and royalties free; anyone else needs a treaty and the DOPK proof.
3. **What the payment is for.** Technical service, management fee, royalty, interest or rent is withheld; an ordinary service performed abroad is not.
4. **Total paid to the same foreign person in the year.** Above EUR 255,645.94 the treaty needs an NRA request, not just proof to the payer.
5. **People, sites and contract signing in Bulgaria.** A fixed place, an agent concluding contracts, or regular transactions in Bulgaria make a PE.
6. **Assets, residence or activity leaving Bulgaria.** Destination country (EU or EEA, or not), market price and tax value decide the exit tax and the deferral.

## Sources

| Source | URL | Read on |
|---|---|---|
| Corporate Income Tax Act (ZKPO), consolidated to ДВ бр. 55/2026, arts. 2, 3, 4, 12, 13, 14, 15, 20, 27, 47в, 47г, 92, 93, 155 to 155д, 194, 195, 196, 199, 200, 201, 202, 202a, 203, 261, § 1 item 2 | https://lex.bg/laws/ldoc/2135540562 | 2026-10-23 |
| Personal Income Taxes Act (ZDDFL), consolidated to ДВ бр. 85/2026, arts. 4 to 8, 37, 37a, 38, 46, 48, 50, 53, 65, 67, 75, 76, 81 | https://lex.bg/laws/ldoc/2135538631 | 2026-10-23 |
| Tax and Social Security Procedure Code (DOPK), consolidated to ДВ бр. 85/2026, arts. 18, 135 to 142, 275, § 1 items 5, 7, 10 | https://lex.bg/laws/ldoc/2135514513 | 2026-10-23 |
| Law on Interest on Taxes, Fees and Other Similar State Receivables, art. 1 | https://lex.bg/laws/ldoc/2123675140 | 2026-10-23 |
| Euro Introduction Act (Закон за въвеждане на еврото в Република България), consolidated to ДВ бр. 92/2026, arts. 11, 12, 13, § 5 | https://lex.bg/bg/laws/ldoc/2137244903 | 2026-10-23 |
| NRA, application of double tax treaties (procedure, EUR 255,645.94 threshold, refund route) | https://nra.bg/wps/portal/nra/mezhdunarodni-deinosti/siddo/prilagane-na-SIDDO | 2026-10-23 |
| NRA, list of double tax treaties | https://nra.bg/wps/portal/nra/mezhdunarodni-deinosti/siddo/spisak-sas-spogodbi | 2026-10-23 |

Not yet confirmed: treaty rates for any treaty (the NRA treaty texts are PDFs this session could not read, so no treaty rate is given); the current statutory interest rate on late tax after the euro changeover (the interest law refers to "законна лихва", whose rate is set outside that law); the withholding or advance-tax mechanics for fees a non-resident individual earns for services physically performed in Bulgaria that are not on the PITA art. 37 list; whether a split-year rule applies to an individual who arrives or leaves mid-year (PITA art. 4 states none); whether the Russia treaty is applied in practice (it is still on the NRA list); the instalment allocation formula in CITA art. 155г(4), which lex.bg shows without the formula itself.

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
