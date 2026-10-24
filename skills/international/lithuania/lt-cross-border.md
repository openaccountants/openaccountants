---
name: lt-cross-border
description: "Hub skill for crossing the Lithuanian border in tax year 2026. Covers individual residence under GPMĮ article 4 (permanent home, centre of interests, 183 days, the 280 and 90 day two-year test, departure); companies and permanent establishments under PMĮ articles 2 and 4; tax at source on payments to foreign entities (PMĮ articles 4(4), 5, 34, 37, 37-1): 17% on dividends and real estate income, 10% on royalties and on interest to non-EEA, non-treaty lenders, 0% on interest to EEA and treaty lenders; the 10% and 12 month dividend exemption; DAS-1 and DAS-2 treaty forms and the FR0313 return; inbound dividends and foreign PE profits; foreign tax credits for companies and individuals; tax withheld from non-resident individuals (GPMĮ articles 6 and 23(7)); the corporate exit tax and its five year spread (PMĮ article 40-2); late payment interest. Includes the 2026 changes: CIT at 17%, PIT at 20, 25 and 32%, Russia and Belarus treaties no longer applied. Trigger phrases: nenuolatinis gyventojas, užsienio vienetas, DAS-1, išskaičiuojamas pelno mokestis, turto perkėlimas, exit tax Lithuania, withholding tax Lithuania, leaving Lithuania. Out of scope: lt-corporate-income-tax, lithuania-pit, lt-payroll-social, lithuania-vat-return."
jurisdiction: LT
category: international
tax_year: 2026
tier: 2
last_updated: 2026-10-24
version: 0.2
verified_by: pending
trust_label: Built by Michael Cutajar and the OpenAccountants team
---

# Lithuania: cross-border tax for people and companies (2026)

Source-cited draft: not reviewed by an accountant, not for filing.

This is the hub for the Lithuanian cross-border (XB) domain. It links rather than repeats:

- Corporate tax in general (rates for small companies, losses, advance payments): [lt-corporate-income-tax](lt-corporate-income-tax.md). That skill still carries 2025 figures; the 2026 rates below come from the law in force.
- Personal income tax for residents: [lithuania-pit](lithuania-pit.md) (2026 figures).
- Payroll and Sodra contributions: [lt-payroll-social](lt-payroll-social.md).
- VAT: [lithuania-vat-return](lithuania-vat-return.md).

The law is the Corporate Income Tax Law (Pelno mokesčio įstatymas, No. IX-675, "PMĮ"), read in the consolidated version in force from 19 May 2026 to 31 December 2026 on e-tar.lt, and the Personal Income Tax Law (Gyventojų pajamų mokesčio įstatymas, No. IX-1007, "GPMĮ"), read in the consolidated version in force from 11 June 2026 on e-tar.lt, in the State Tax Inspectorate's (VMI) commentary of 19 October 2026 and its English translation of the 2026 text. The tax authority is the VMI. Tax year: the calendar year, unless a company has VMI approval for another 12 month period (PMĮ article 6). Currency: euro.

## Who this applies to

**Individuals: who is resident.** GPMĮ article 4(1) sets the tests, applied in order. A person is a Lithuanian resident for the tax year if:

1. their permanent place of residence in the year is in Lithuania; or
2. their personal, social or economic interests are more in Lithuania than abroad; or
3. they are in Lithuania for 183 days or more in the year, in one stay or several; or
4. they are in Lithuania for 280 days or more over two consecutive years and for 90 days or more in one of those years. They are then resident in both years (unless article 4(3) applies); or
5. they are a Lithuanian citizen paid under an employment contract, or whose living costs abroad are covered, from the state or a municipal budget.

VMI's commentary lists what counts for test 2: where most of the person's property is, their bank accounts, where their family lives, citizenship, and where they work or take part in public life. Foreign diplomats and consular staff who are not Lithuanian citizens are not resident under tests 3 to 5 (article 4(2)).

**Leaving.** A person who was resident for at least three years in a row and leaves for good in the fourth year, spending fewer than 183 days in Lithuania that year, is resident only until the day they leave (article 4(3)). Before leaving they file the departure return and pay tax on that year's income to the departure date (GPMĮ article 29). We found no deemed-sale (exit) charge on an individual's assets in the GPMĮ.

**Scope.** A resident is taxed on worldwide income. A non-resident is taxed on Lithuanian-source income. Where a treaty applies and limits Lithuania's taxing right, the treaty wins (Law on Tax Administration, article 5, as cited in VMI's PMĮ commentary on article 34).

**Companies.** A "Lithuanian entity" is a legal person registered under Lithuanian law, a Lithuanian collective investment undertaking without legal personality, or a Lithuanian hybrid entity (PMĮ article 2(2)). It is taxed on income from Lithuania and abroad (PMĮ article 4(1)). A foreign entity is taxed only on Lithuanian-source income: through a permanent establishment, or at source on the payments listed in article 4(4).

**Permanent establishment.** A foreign entity has a PE in Lithuania if it carries on activity there on a permanent basis, acts through a dependent agent, uses a building site or construction, assembly or installation project, or uses equipment or structures (including wells and ships) to explore or extract natural resources (PMĮ article 2(22)). The Government sets the "permanent" and agent tests.

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| Corporate income tax, Lithuanian entities and PEs | 17% (16% in 2025) | 2026 | [PMĮ art. 5(1)(1)](https://www.e-tar.lt/portal/lt/legalAct/TAR.A5ACBDA529A9/asr), amended by Law XV-285 |
| Dividends paid to a foreign entity | 17% at source, paid by the 15th of the month after payment | 2026 | PMĮ art. 34(1) |
| Dividend exemption for a foreign parent | 0% if it holds at least 10% of the voting shares for 12 months without a break, including the distribution date, and is not in a target territory | 2026 | PMĮ art. 34(2) |
| Interest paid to a foreign entity registered in the EEA or a treaty state | 0% | 2026 | PMĮ art. 5(1)(2) |
| Interest paid to any other foreign entity | 10% of the gross amount | 2026 | PMĮ art. 5(1)(2) |
| Interest not taxed at source in any case | Government securities, deposit interest, qualifying subordinated loans | 2026 | PMĮ art. 4(4)(1) |
| Royalties and compensation for breach of copyright, paid to a foreign entity | 10% of the gross amount | 2026 | PMĮ art. 5(1)(2), 4(4)(3) and (5) |
| Royalties to an associated EU company | 0% if a 25% direct holding (either way, or a common EU parent) has run without a break for at least 2 years up to the payment and the recipient is the beneficial owner | 2026 | PMĮ art. 37-1(1) to (3) |
| Lithuanian real estate income (sale or rent), performers' and sports income, supervisory board payments, paid to a foreign entity | 17% of the gross amount | 2026 | PMĮ art. 5(1)(2), 4(4)(4), (6), (7) |
| Foreign dividends received by a Lithuanian entity | Exempt from an EEA entity taxed on its profits; exempt from another taxed entity outside target territories after a 10% holding for 12 months; otherwise 17% | 2026 | PMĮ art. 35(1) to (3) |
| Profits of a Lithuanian entity's PE in the EEA or a treaty state | Not taxed in Lithuania if taxed there | 2026 | PMĮ art. 4(1) |
| Exit tax on assets moved abroad | Market value less tax cost, taxed at 17%; the gain can be spread in equal parts over 5 years for moves within the EEA | 2026 | PMĮ art. 40-2(2) and (4) |
| Personal income tax on annual income up to 36 average wages (EUR 83,237.40) | 20% | 2026 | [GPMĮ art. 6(1)](https://www.vmi.lt/evmi/documents/20142/391224/GPM+aktualus+komentaras+(aktuali+redakcija+2026-10-13)+.pdf/541c2138-7e9c-3e99-33bf-fc547c5cdc28?t=1791918859615); figures from the VMI commentary |
| Personal income tax, 36 to 60 average wages (EUR 83,237.40 to 138,729) | 25% | 2026 | GPMĮ art. 6(1) |
| Personal income tax above 60 average wages (EUR 138,729) | 32% | 2026 | GPMĮ art. 6(1) |
| Non-employment income up to 12 average wages (EUR 27,745.80) | 15% | 2026 | GPMĮ art. 6(2) |
| Dividends received by an individual | 15% | 2026 | GPMĮ art. 6(6)(1) |
| Interest, royalties and Lithuanian real estate sale income paid to a non-resident individual (withheld by the payer) | 15% on the first EUR 27,745.80 of the payment; 20% on the part up to EUR 83,237.40; 25% up to EUR 138,729; 32% above. The bands apply to that one payment alone | 2026 | [GPMĮ](https://www.e-tar.lt/portal/lt/legalAct/TAR.C677663D2202/asr) art. 6(1), (2) and (11), 23(7) |
| Residence day counts | 183 days in the year; or 280 days over two years with 90 in one | 2026 | GPMĮ art. 4(1)(3), (4) |
| Treaties no longer applied | Russia and Belarus, from 1 January 2026 | 2026 | VMI GPMĮ commentary, art. 37 |
| Late payment interest (delspinigiai) | 0.027% a day from 1 August 2026 | 2026 | [VMI, late payment interest](https://www.vmi.lt/evmi/delspinigiai-baudos-ir-atleidimas-nuo-ju-96-100-str.-138-143-str.-) |
| Fine on tax found short in an audit (including a lower rate applied without grounds) | 20% to 100% of the shortfall | 2026 | [Law on Tax Administration](https://www.e-tar.lt/portal/lt/legalAct/TAR.3EB34933E485/asr) art. 139(1) |

## The taxable base

**Tax at source on a foreign entity's income.** PMĮ article 4(4) lists the Lithuanian-source income of a foreign entity that has no PE here:

1. interest (except on government securities, deposit interest, and qualifying subordinated loans);
2. distributed profits (dividends), except a foreign entity's income from Lithuanian collective investment undertakings when it is not in a target territory;
3. royalties (and some software licences, article 4(5));
4. income from selling, transferring or renting Lithuanian real estate;
5. compensation for breach of copyright or related rights;
6. income from performers' and sports activity in Lithuania;
7. payments for supervisory board work.

The payer (a Lithuanian entity, a PE, or a resident individual) withholds the tax from the full amount, with no deductions (PMĮ articles 5(1)(2) and 37). Income is recognised when paid (article 37, cash basis under article 8(1)). Income that is not on the list, such as a service fee, is not taxed at source.

**Interest and intermediaries.** Where interest goes to EEA or treaty lenders through a bank or broker, the payer can pay it gross only if it holds the intermediary's list naming the beneficial owners (name, ID, address, state). Otherwise it withholds 10% (VMI PMĮ commentary on article 5(1)(2), point 5). Interest paid to an EEA or treaty PE of a company based in a non-EEA, non-treaty state is taxed at 10% (point 6).

**Treaty rates at source.** The payer may apply a treaty rate below the PMĮ rate only if it holds the recipient's DAS-1 form (FR0021) when it pays. Without it, the payer withholds the domestic rate and the recipient claims the difference back on form DAS-2 (FR0022) (VMI PMĮ commentary on articles 4(4) and 34(1); VMI order No. 159 of 27 June 2001). VMI's own example: the Lithuania-Slovakia treaty caps tax on dividends to an 8% Slovak shareholder at 10%.

A tax authority that does not sign DAS-1 can issue its own residence certificate, attached to the DAS-1. VMI names the US form 6166 as the example (VMI commentary on PMĮ article 52).

**Inbound dividends.** A Lithuanian entity does not include foreign dividends in income; it pays 17% on them separately unless an exemption in article 35 applies. The exemptions do not apply where the paying company deducted the dividend from its own taxable profit (article 35(5)).

**Foreign PEs: exemption, then credit.** Profits of a Lithuanian entity's PE in an EEA or treaty state are left out of the Lithuanian base if that state taxes them (article 4(1)). The costs of earning them are not deductible. For other foreign income (a PE elsewhere, royalties or interest taxed abroad), Lithuania taxes it and credits the foreign tax. The credit is capped at the Lithuanian tax on that income (PMĮ article 55(1) and (2)).

**Individuals: exemption, then credit.** For a resident (GPMĮ article 37):

- Income from a treaty state, other than interest, dividends and royalties, is exempt if tax was paid on it there. The person must show proof of the income and the tax.
- Interest, dividends and royalties from a treaty state are taxed, and the treaty-state tax is credited.
- Tax paid in a non-treaty state is credited if the foreign tax authority certifies the income and the tax. No credit is given for a state on the Minister of Finance's list of target territories.
- The credit never exceeds the Lithuanian tax on that income (article 37(4)), and is worked out country by country (article 37(5)).

The 2026 PIT rates apply to the whole annual income. VMI's example shows that treaty-exempt foreign pay still counts towards the 36 average wage band: the bands are applied pro rata to the share of income taxed in Lithuania (VMI commentary on GPMĮ article 6(1)).

**Exit tax (turto perkėlimas).** Article 40-2(1) taxes a transfer of assets out of Lithuania when:

1. a Lithuanian entity allocates assets to its foreign PE, keeping ownership;
2. a foreign entity's Lithuanian PE allocates assets to its business in another state;
3. a Lithuanian entity moves its business abroad, except where the assets keep being used by a Lithuanian PE;
4. a foreign entity's Lithuanian PE moves its business abroad.

The gain is market value at the transfer date less acquisition cost. Acquisition cost is reduced by the depreciation or amortisation already deducted (article 40-2(2) and (3)). A loss counts in that year's result (VMI commentary). VMI's commentary says servers kept in Lithuania but allocated to a foreign PE count too. A transfer for less than 12 months is not taxed where the assets back a securities financing deal, serve as collateral, or are moved to meet prudential capital or liquidity needs (article 40-2(5)); any other temporary transfer is taxed.

**The five year spread.** For a move to an EEA state with an EU-standard tax recovery agreement, the company can bring the gain into income in equal parts over 5 years from the transfer (article 40-2(4)). VMI's commentary says only Liechtenstein had no such agreement on 1 January 2020. The rest of the gain is taxed at once in the year that:

1. the asset is sold or transferred;
2. the asset moves on, within the 5 years, to a state outside the EEA or without a recovery agreement;
3. bankruptcy or liquidation starts; or
4. the company has not met its CIT obligations for 12 months after the article 53 payment dates.

Note that Lithuania spreads the income, not the tax.

## Deadlines and filing

- **Tax withheld from payments to foreign entities:** the payer files the FR0313 return and pays the tax within 15 days after the end of the month of payment (PMĮ articles 52(2) and 53(2)). An FR0313 is still filed when a treaty means no tax is withheld, with zeros in the rate and tax boxes (VMI commentary on article 52).
- **Dividends to foreign entities:** tax paid by the 15th of the month after payment (PMĮ article 34(1)). VMI's example: dividends paid on 9 April 2026, tax due by 15 May 2026.
- **Dividends received from abroad and taxable:** the Lithuanian entity pays by the 15th of the month after receipt (PMĮ article 35(1)).
- **DAS-1:** must be held before payment. The payer gives VMI its copy when asked (VMI commentary on article 34). VMI's commentary on article 52 says the forms go in with the annual financial statements and CIT return.
- **Refund of tax withheld where article 37-1 applied:** the foreign entity applies in writing with proof within 2 years of the payment. VMI refunds within one year of the claim (PMĮ article 53(2)).
- **Withholding from individuals (A class income, including non-residents' interest and real estate sale income):** tax on income paid by the 15th of a month is due by the 15th; on income paid later in the month, by the last day of the month (GPMĮ article 23(3)). The payer files monthly returns by the 15th of the next month and an annual return by the 15th of the second month after year end (GPMĮ article 24(2)).
- **Non-resident's other income (B class):** the non-resident works out the tax, pays it and files within 25 days of receiving the income (GPMĮ article 31(1)).
- **Non-resident with a fixed base:** annual return and payment by 1 May of the next year (GPMĮ article 30).
- **Residents' annual return:** by 1 May of the next year (GPMĮ article 27(1)), so 1 May 2027 for 2026.
- **Leaving Lithuania for good:** the departure return is filed and the tax paid before departure (GPMĮ article 29).
- **Exit tax:** shown on the annual CIT return for the year of transfer, where the company ticks whether it brings the gain in at once, spreads it over 5 years, or stops a spread (VMI commentary on article 40-2(4)).

## Penalties and interest

- **Late payment interest (delspinigiai):** 0.027% for each day late from 1 August 2026, set by the Minister of Finance (Law on Tax Administration articles 96 and 99, VMI page). The Minister resets the rate each quarter from the yield on 12 month government securities plus 7 percentage points, divided by 365.
- **Fines:** where a tax audit finds that the taxpayer did not calculate or declare tax, or applied a lower rate without grounds, and so paid too little, VMI assesses the shortfall and a fine of 20% to 100% of it (Law on Tax Administration article 139(1)). A second fine for a breach of the same tax law within the limitation period doubles (article 139(3)). No fine is imposed when the taxpayer corrects the return before VMI orders an audit (article 139(4)).
- **Missing DAS-1:** with no DAS-1 when it pays, the payer must withhold the domestic rate. If it paid gross and covered the tax itself, it can reclaim once the DAS-1 arrives, filing a corrected FR0313 (VMI commentary on article 52).
- **Exit tax spread:** missing CIT obligations for 12 months after the payment dates ends the spread and brings the rest into income (PMĮ article 40-2(4)(4)).
- **Small-company 0% rate claimed wrongly:** the 0% rate for the first two tax periods applies only where every shareholder is an individual, and only if over three periods in a row the business is not suspended, liquidated or reorganised and no shares pass to new shareholders (PMĮ article 5(2)). If that fails, the 0% rate is lost for those periods. This matters where a foreign buyer acquires a young Lithuanian company.

## Cross-border points

- **Dividends to a foreign parent:** 0% with a 10% holding for 12 months. The 12 months can be completed after the payment if the shares are then kept (VMI commentary on article 34(2)). Otherwise 17%, or the treaty rate with DAS-1. Target territories never get the exemption.
- **Dividends to a foreign individual:** 15% (GPMĮ article 6(6)(1)), or the treaty rate.
- **Interest to EEA and treaty lenders:** 0%. To others: 10%. Interest to a non-resident individual is A class income (GPMĮ article 22(2)(1)): the payer withholds 15% on the first EUR 27,745.80 of the payment, and the article 6(1) bands above that, looking at that payment alone (GPMĮ article 23(7)), or the treaty rate with DAS-1.
- **Royalties:** 10%, or 0% under article 37-1 for EU associated companies, or the treaty rate.
- **Real estate:** a foreign entity's Lithuanian rent or sale proceeds suffer 17% of the gross amount. A non-resident individual selling Lithuanian property has tax withheld by a Lithuanian buyer and can ask VMI to recalculate it on the gain, with proof of cost (GPMĮ article 32).
- **Hiring a foreign service provider:** service fees are not on the article 4(4) list, so no CIT is withheld, unless the provider has a PE in Lithuania.
- **Treaties:** VMI lists the treaties applied (VMI GPMĮ commentary, article 37). Russia and Belarus are no longer applied from 1 January 2026.
- **Transfer pricing on cross-border flows:** see [lt-transfer-pricing](lt-transfer-pricing.md).

## Worked examples

### Example 1: a EUR 200,000 dividend to an 8% Slovak shareholder

A Lithuanian UAB pays a dividend of EUR 200,000 in April 2026 to a Slovak company holding 8% of its shares. The 10% participation exemption does not apply because the holding is under 10%. The Lithuania-Slovakia treaty caps the tax at 10% for a beneficial owner resident in Slovakia (VMI's example under PMĮ article 34).

- **With a DAS-1 in hand at payment:** the UAB withholds 10%, EUR 20,000.
- **Without one:** it withholds 17%, EUR 34,000. The Slovak company can claim back EUR 14,000 on DAS-2.
- **Payment:** by 15 May 2026, with the FR0313 return.

If the Slovak company had held at least 10% of the voting shares for 12 months, the dividend would be exempt.

```oa-check
name: EUR 200,000 dividend to an 8% Slovak corporate shareholder, 2026
inputs:
  dividend: 200000
steps:
  - domestic_rate: 17 / 100
  - treaty_rate: 10 / 100
  - tax_without_das1: dividend * domestic_rate
  - tax_with_das1: dividend * treaty_rate
  - das2_refund_claim: tax_without_das1 - tax_with_das1
  - net_to_shareholder: dividend - tax_with_das1
expected:
  tax_without_das1: 34000
  tax_with_das1: 20000
  das2_refund_claim: 14000
  net_to_shareholder: 180000
```

### Example 2: a trademark moved to a Latvian branch, with the five year spread broken in year 3

A Lithuanian UAB allocates a trademark to its new permanent establishment in Latvia in 2026. Market value at the transfer: EUR 500,000. Acquisition cost: EUR 200,000. Amortisation already deducted for CIT: EUR 50,000.

- **Tax cost:** acquisition cost less amortisation deducted: 200,000 less 50,000 = EUR 150,000 (PMĮ article 40-2(3)).
- **Gain:** 500,000 less 150,000 = EUR 350,000.
- **Taken at once:** CIT at 17% is EUR 59,500 for 2026.
- **Spread over 5 years** (Latvia is in the EEA with a recovery agreement): EUR 70,000 of income a year, EUR 11,900 of CIT a year at the 2026 rate.
- **Edge case:** the branch sells the trademark in the third year. The spread stops. The two parts not yet included (years 4 and 5) come into income in year 3: EUR 140,000 on top of that year's EUR 70,000, so EUR 210,000 in year 3.
- **Tax in years 1 to 3:** at 17%, the total is EUR 59,500, the same as paying at once, only later.

```oa-check
name: Exit tax on a trademark moved to a Latvian PE, 5 year spread stopped in year 3, 2026 rate
inputs:
  market_value: 500000
  acquisition_cost: 200000
  amortisation_deducted: 50000
  spread_years: 5
  years_already_included: 2
steps:
  - cit_rate: 17 / 100
  - tax_cost: acquisition_cost - amortisation_deducted
  - gain: market_value - tax_cost
  - tax_if_taken_at_once: gain * cit_rate
  - yearly_income_part: gain / spread_years
  - yearly_tax_part: yearly_income_part * cit_rate
  - income_in_year_3: gain - yearly_income_part * years_already_included
  - tax_years_1_to_3: (yearly_income_part * years_already_included + income_in_year_3) * cit_rate
expected:
  tax_cost: 150000
  gain: 350000
  tax_if_taken_at_once: 59500
  yearly_income_part: 70000
  yearly_tax_part: 11900
  income_in_year_3: 210000
  tax_years_1_to_3: 59500
```

## Ask the client first

1. For a person: days in Lithuania in 2026 and 2025, where their home and family are, citizenship, and whether another state also treats them as resident. Are they leaving Lithuania for good, and when?
2. For a payment abroad: what is it (dividend, interest, royalty, rent, service fee), who receives it, where is the recipient registered and is it the beneficial owner?
3. Does the payer hold this year's DAS-1 (or a foreign residence certificate) before paying? Is the recipient in a target territory?
4. For dividends: the recipient's voting stake, and the date it reached 10%.
5. For royalties to an EU company: the direct holding between payer and recipient, and the date it reached 25%.
6. For a company: is it moving assets, a branch's business, or its whole business abroad? To which state, on what date, and at what market value and tax cost?

## Sources

| Source | URL | Read on |
|---|---|---|
| PMĮ (Law No. IX-675 on Corporate Income Tax), consolidated version 2026-05-19 to 2026-12-31, arts. 2, 4, 5, 34, 35, 37, 37-1, 40-2, 52, 53, 55, and its list of amendments (Law XV-488 changes arts. 12 and 30 only, from 2027-01-01); Register of Legal Acts (e-tar) | https://www.e-tar.lt/portal/lt/legalAct/TAR.A5ACBDA529A9/asr | 2026-10-23 |
| VMI, commentary on the PMĮ (link labelled 2026-09-28; the file served is titled current as of 2026-10-23), arts. 2, 4, 5, 34, 37-1, 40-2, 52, 53, 55 | https://www.vmi.lt/evmi/documents/20142/751579/Pelno+mokes%C4%8Dio+komentaras+(aktualus+2026-09-28).pdf/c9688bd6-8557-df3a-c0a3-e4032cfff2b6?t=1790570493065 | 2026-10-24 |
| VMI, tax on income paid to a foreign entity (PMĮ arts. 37, 53(2), 54) | https://www.vmi.lt/evmi/pelno-mokestis-nuo-pajam%C5%B3-sum%C5%B3-i%C5%A1mok%C4%97t%C5%B3-u%C5%BEsienio-vienetui-37-str.-53-str.-2-d.-54-str.- | 2026-10-23 |
| GPMĮ (Law No. IX-1007 on Personal Income Tax), consolidated version 2026-06-11 to 2026-12-31, arts. 4, 6, 22, 23, 24, 27, 29, 30, 31, 32, 37; Register of Legal Acts (e-tar) | https://www.e-tar.lt/portal/lt/legalAct/TAR.C677663D2202/asr | 2026-10-24 |
| Law on Tax Administration (No. IX-2112), consolidated version from 2026-07-01, art. 139; Register of Legal Acts (e-tar) | https://www.e-tar.lt/portal/lt/legalAct/TAR.3EB34933E485/asr | 2026-10-24 |
| VMI, commentary on the GPMĮ (Law No. IX-1007 on Personal Income Tax), 2026-10-19 edition, arts. 4, 6, 22, 37 | https://www.vmi.lt/evmi/documents/20142/391224/GPM+aktualus+komentaras+(aktuali+redakcija+2026-10-13)+.pdf/541c2138-7e9c-3e99-33bf-fc547c5cdc28?t=1791918859615 | 2026-10-23 |
| VMI, GPMĮ in English (unofficial translation), version 2026-01-01 to 2026-12-31, arts. 6, 23, 24, 27, 29, 30, 31, 32, 37 | https://www.vmi.lt/evmi/documents/20142/390999/GPM%C4%AE+angl%C5%B3+kalba+2026-01-01-2026-12-31.pdf/648a3aaa-6e7f-27d8-7aec-73f091a2a12f?t=1770030676856 | 2026-10-23 |
| VMI, personal income tax page (links to the law, translation and commentary) | https://www.vmi.lt/evmi/gyventoju-pajamu-mokestis | 2026-10-23 |
| VMI, late payment interest, fines and relief (Law on Tax Administration arts. 88, 96 to 100, 138 to 143), KM2633 and KM0584 | https://www.vmi.lt/evmi/delspinigiai-baudos-ir-atleidimas-nuo-ju-96-100-str.-138-143-str.- | 2026-10-23 |
| Seimas register, PMĮ (direct page; behind a human check on 2026-10-23, not read) | https://e-seimas.lrs.lt/portal/legalAct/lt/TAD/TAIS.157066/asr | 2026-10-23: not read |

Not yet confirmed: whether DAS-1 forms go to VMI with the annual financial statements and CIT return or only on request (VMI's PMĮ commentary says the first under article 52 and the second under article 34; VMI order No. 159 was not read); the rate and interest charged when the small-company 0% rate is lost under PMĮ article 5(2); the current list of target territories (Minister of Finance order No. 344) and VMI's own treaty list page (the PMĮ commentary's treaty lists still name Russia and Belarus; the GPMĮ commentary of 2026-10-19 marks both as no longer applied from 2026-01-01); the CFC rules (PMĮ article 39), which this skill does not cover.
