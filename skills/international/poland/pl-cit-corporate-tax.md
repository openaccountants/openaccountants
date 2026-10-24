---
name: pl-cit-corporate-tax
description: "Polish corporate income tax (CIT, podatek dochodowy od osób prawnych) for tax year 2026: resident companies (sp. z o.o., S.A., P.S.A., limited partnerships taxed as companies) and Polish permanent establishments of foreign companies. Covers the 19% rate, the 9% rate for small taxpayers and start-ups (revenue limit PLN 8,431,000 for a 2026 calendar year), the 2026 bank rates, Estonian CIT (ryczałt od dochodów spółek, 10% or 20%), the 10% minimum tax, tax on shifted income, losses (five years, 50% a year or PLN 5m once), tax capital groups (PGK), the PLN 3m or 30% interest limit, CIT-8 filing, monthly, quarterly and simplified advances, late payment interest, outbound withholding (19%, 20%, pay-and-refund above PLN 2m), CFC and exit tax. Trigger on: CIT Poland, Polish corporate tax, CIT-8, mały podatnik, 9% CIT, estoński CIT, CIT-8E, podatek minimalny, PGK. Out of scope: individuals (pl-income-tax, pl-capital-gains), VAT (pl-vat-return), ZUS (pl-zus-contributions), e-invoicing (poland-einvoice)."
version: 0.1
jurisdiction: PL
tax_year: 2026
last_updated: 2026-10-23
authored_by: Ryan Duguid
review_status: pending_review
trust_label: Accountant-authored
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Polish corporate income tax (CIT): tax year 2026

> **General reference only.** This skill is general tax reference material for AI-assisted work. It has not been reviewed for any specific company's facts. Do not rely on it to file, pay or take a position without review by a qualified professional in Poland.

**Tax year (art. 8).** The tax year is the calendar year unless the company's articles choose another period of 12 consecutive calendar months. "2026" here means the calendar year 2026, with the return filed in 2027.

**Which text of the law.** Article numbers are those of the CIT Act (ustawa z dnia 15 lutego 1992 r. o podatku dochodowym od osób prawnych), consolidated text Dz.U. 2026 poz. 554, as amended by Dz.U. 2026 poz. 779, 846, 912 and 1123. The Sejm's unified text read on 2026-10-22 includes all of these. A further amendment, Dz.U. 2026 poz. 1371 (in force from November 2026, parts from 1 January 2027), changes transfer pricing information returns and cash-payment cost rules; it does not change any rate below.

**Sibling skills.** Individuals and sole traders: [pl-income-tax](pl-income-tax.md). Investment income of individuals: [pl-capital-gains](pl-capital-gains.md). VAT: [pl-vat-return](pl-vat-return.md). Social contributions: [pl-zus-contributions](pl-zus-contributions.md). KSeF e-invoicing: [poland-einvoice](poland-einvoice.md).

## Who this applies to

**Taxpayers (art. 1).** CIT is charged on legal persons and capital companies in organisation. It also applies to:
- limited partnerships (spółka komandytowa) and limited joint-stock partnerships (S.K.A.) with their seat or management in Poland (art. 1(3)(1));
- general partnerships (spółka jawna) with a seat or management in Poland where not all partners are individuals and the partnership has not filed the required information on its partners (art. 1(3)(1a)), or where a family foundation is a partner (art. 1(7));
- foreign entities without legal personality that their home state taxes as companies on worldwide income (art. 1(3)(2)).

**Residence (art. 3(1) and (1a)).** A company with its seat (siedziba) or its management (zarząd) in Poland is taxed on its worldwide income. Management is in Poland where the company's current affairs are run there in an organised and continuous way, in particular under a contract, a court decision or other founding document, powers of attorney, or links with related parties.

**Non-residents and permanent establishments (art. 3(2)-(3)).** A company with neither seat nor management in Poland is taxed only on income earned in Poland. That includes business carried on through a Polish permanent establishment (zagraniczny zakład, defined in art. 4a pkt 11), Polish real estate, shares in Polish real-estate-rich companies, and payments made by Polish payers (art. 3(3)(5)).

**Out of scope here.**
- Individuals and sole traders (PIT): see [pl-income-tax](pl-income-tax.md).
- Family foundations, the IP Box (5%), the holding company regime (art. 24m and following), special economic zones and investment-support decisions, insurers and investment funds. Refer these.
- Banks and credit unions: their rates are listed below, but their bases are not covered.

## Rates, bands and thresholds

| Item | Rate or amount | Tax year | Source |
|---|---|---|---|
| Standard CIT rate | 19% of the tax base | 2026 | [CIT Act art. 19(1)(1)](https://isap.sejm.gov.pl/isap.nsf/DocDetails.xsp?id=WDU20260000554) |
| Reduced rate, small taxpayers and start-ups | 9% of the base, on income other than capital gains (capital gains stay at 19%) | 2026 | art. 19(1)(2), (1a)-(1e) |
| Revenue limit for the 9% rate, in the tax year | EUR 2,000,000 at the NBP rate on the first working day of the tax year: PLN 8,431,000 for a calendar year 2026 (EUR 1 = PLN 4.2156 on 2 January 2026). Prorated for a tax year longer or shorter than 12 months, from 2026 | 2026 | art. 19(1)(2)(a)-(b); [podatki.gov.pl, CIT rates and limits](https://www.podatki.gov.pl/podatki-firmowe/cit/cit-klasyczny/stawki-i-limity); [NBP table 001/A/NBP/2026](https://api.nbp.pl/api/exchangerates/rates/a/eur/2026-01-02/?format=json) |
| Small taxpayer (mały podatnik) limit | Prior-year sales revenue including VAT not above EUR 2,000,000 at the NBP rate on the first working day of October of the prior year: PLN 8,517,000 for 2026 (EUR 1 = PLN 4.2586 on 1 October 2025) | 2026 | art. 4a pkt 10; [podatki.gov.pl, CIT rates and limits](https://www.podatki.gov.pl/podatki-firmowe/cit/cit-klasyczny/stawki-i-limity) |
| Banks (excluding cooperative banks), and a PGK on the share of its income from a member bank | 30% for a tax year starting in 2026; 26% in the following year; 23% after that | 2026 | art. 19(1)(3) and art. 38aa, added by [Dz.U. 2025 poz. 1658](https://isap.sejm.gov.pl/isap.nsf/DocDetails.xsp?id=WDU20250001658) |
| Cooperative banks and SKOKs | 27% for a tax year starting in 2026; 23% in the following year; 21% after that | 2026 | art. 19(1)(4) and art. 38ab (as corrected by Dz.U. 2026 poz. 779) |
| Banks and SKOKs that meet the 9% rate conditions | 17% for a tax year starting in 2026; 13% in the following year; 11% after that | 2026 | art. 19(1)(5) and art. 38ac |
| Estonian CIT (ryczałt od dochodów spółek) | 10% for a small taxpayer or a start-up; 20% otherwise | 2026 | art. 28o(1); [podatki.gov.pl, Estonian CIT rates](https://www.podatki.gov.pl/podatki-firmowe/cit/cit-estonski/stawki-i-limity-w-estonskim-cit) |
| Minimum income tax (podatek minimalny) | 10% of a special base, for companies with a loss or a profitability ratio of 2% or less | applies to 2026 (it was suspended only for 2022 and 2023, art. 38ec) | art. 24ca |
| Tax on shifted income (podatek od przerzuconych dochodów) | 19% | 2026 | art. 24aa(1) |
| Interest limitation safe harbour | PLN 3,000,000 a year, or 30% of tax EBITDA if higher | 2026 | art. 15c(1) |
| Losses | Five tax years; at most 50% of the loss in any one year, or once up to PLN 5,000,000 | 2026 | art. 7(5) |
| One-off depreciation, small taxpayers and start-ups | Up to EUR 50,000 a year: PLN 213,000 for 2026 | 2026 | art. 16k(7); [podatki.gov.pl, CIT rates and limits](https://www.podatki.gov.pl/podatki-firmowe/cit/cit-klasyczny/stawki-i-limity) |
| Low-value assets | Initial value up to PLN 10,000 may be expensed at once | 2026 | art. 16f(3) |
| Passenger car value cap for depreciation | PLN 225,000 electric or hydrogen; PLN 150,000 if CO2 below 50 g/km; PLN 100,000 if 50 g/km or more (cars entered in the asset register before 1 January 2026 keep the 2025 caps) | 2026 | art. 16(1)(4); [podatki.gov.pl, CIT rates and limits](https://www.podatki.gov.pl/podatki-firmowe/cit/cit-klasyczny/stawki-i-limity) |
| Tax capital group (PGK) | At least PLN 250,000 average share capital per company; parent holds at least 75% directly | 2026 | art. 1a(2) |
| Late payment interest (odsetki za zwłokę) | 10.50% a year (reduced 5.25%) | from 5 March 2026 | [MF notice, M.P. 2026 poz. 269](https://isap.sejm.gov.pl/isap.nsf/DocDetails.xsp?id=WMP20260000269); Tax Ordinance art. 56 |
| Pillar Two | 15% global and domestic minimum tax for groups with consolidated revenue of at least EUR 750,000,000; in force from 1 January 2025 | 2026 | [Dz.U. 2024 poz. 1685](https://isap.sejm.gov.pl/isap.nsf/DocDetails.xsp?id=WDU20240001685) |

**Who can use 9%.** All of these must hold (art. 19(1)(2), (1a)-(1e)):
1. The company is a small taxpayer (prior-year gross sales up to PLN 8,517,000 for 2026), or it is in its first year of business.
2. Its revenue in 2026 does not exceed PLN 8,431,000 (calendar year).
3. It was not created by a restructuring: transformation, merger or division (except one company changing into another company form), conversion of a sole trader or partnership, or a contribution of a business or assets worth more than EUR 10,000 (art. 19(1a)). This bar lasts for the year business starts and the following year.
4. It is not a PGK or a family foundation (art. 19(1b)), and it has not itself been divided or contributed its business elsewhere in that year or the year before (art. 19(1c)).

The 9% rate applies only to income from the "other sources" basket. Income in the capital gains basket (zyski kapitałowe, art. 7b) is taxed at 19%.

**Estonian CIT (art. 28c to 28t).** A company that opts in pays no CIT while profit stays in the business. It pays ryczałt when profit is distributed, and on hidden profits, expenses unrelated to the business, undisclosed transactions, and on retained profit when it leaves the regime. Rates: 10% (small taxpayer or start-up) or 20% (art. 28o). Conditions (art. 28j and 28k):
- legal form: sp. z o.o., S.A., P.S.A., spółka komandytowa or S.K.A., whose shareholders are only individuals (with limits on trusts and foundations, but family foundations are allowed);
- less than 50% of the prior year's revenue (with VAT) is passive: debts, interest, leasing interest, guarantees, IP rights, financial instruments, low-value-added related-party deals;
- at least 3 full-time employees who are not shareholders for 300 days a year, or equivalent pay to 3 non-shareholders under other contracts (a small taxpayer needs only 1 in its first ryczałt year; a start-up builds up by one post a year);
- the company holds no shares in other companies, units in funds, or partnership interests;
- it does not prepare IFRS accounts;
- it is not a financial undertaking, not in a special economic zone or an investment-support decision, and not in liquidation or bankruptcy.

The company files notice ZAW-RD by the end of the first month of the first ryczałt year (art. 28j(1)(7)). The election runs for four years and renews automatically (art. 28f). Losses from before the election are lost from the first ryczałt year, apart from a limited acceleration into the two years before entry (art. 7(7)-(8)). The shareholder also pays personal income tax on the dividend; how much of the ryczałt they can credit is set in the PIT Act and is not covered here.

**Minimum income tax (art. 24ca), 2026.** It applies to resident companies and PGKs that, in the "other sources" basket, either make a loss or have income of no more than 2% of revenue. The test is run on income as defined in art. 7(1). Loss relief is a separate deduction under art. 7(5), so on the wording of the Act the test uses income before losses brought forward; we found no Ministry of Finance explanations (objaśnienia podatkowe) on the point. The test leaves out costs of acquiring and using fixed assets (including depreciation and leasing fees), some regulated-price transactions, receivables sold to factoring institutions, the rise in energy costs over the prior year, some excise and similar charges, and 20% of employee pay costs (art. 24ca(2)). The base is 1.5% of "other sources" revenue, plus related-party debt financing costs above 30% of tax EBITDA, plus some intra-group service and royalty costs above PLN 3,000,000 plus 5% of tax EBITDA (art. 24ca(3)). Instead, a company can elect a simplified base of 3% of that revenue (art. 24ca(3a)). The tax is 10%. It is reduced by the year's ordinary CIT (art. 24ca(12)), and minimum tax paid can be credited against ordinary CIT in the next three years (art. 24ca(13)). Exempt (art. 24ca(14)): small taxpayers; the year business starts and the next two (not for a company created by a restructuring, art. 24ca(16)); financial undertakings; revenue down by at least 30% on the prior year; a company whose ratio was at least 2% in one of the three prior tax years; companies in bankruptcy, liquidation or restructuring proceedings; companies owned only by individuals that hold no more than 5% in other companies; some shipping, mining, healthcare and regulated-price businesses; municipal service companies; parties to a cooperative compliance agreement; and members of a 75% group whose combined ratio is above 2%. The rules apply in the same way to a Polish permanent establishment (art. 24ca(17)).

**Tax on shifted income (art. 24aa), in one line.** 19% on deductible costs paid to a related foreign entity whose income from those payments is taxed below 14.25% (or exempt), which earns at least 50% of its revenue from such payments and passes on at least 10% of it, subject to the other conditions and exclusions in art. 24aa.

## The taxable base

**Two baskets (art. 7).** Taxable income is revenue less tax-deductible costs, computed separately for capital gains (zyski kapitałowe: dividends received, share disposals, contributions in kind and similar items listed in art. 7b) and for all other sources. A loss in one basket cannot be set against income in the other (art. 7(3)(2a)). The tax base is the total income, less deductions under art. 18, rounded to whole złoty (Tax Ordinance art. 63).

**From the accounts.** Start from profit before tax in the statutory accounts (ustawa o rachunkowości), then reverse items the CIT Act treats differently. Main items not deductible (art. 16(1)) include:
- CIT itself (art. 16(1)(15));
- representation costs, in particular restaurant services, food and drink (art. 16(1)(28));
- fines and penalties from criminal, fiscal, administrative or petty-offence proceedings, and interest on them (art. 16(1)(18));
- interest accrued but not paid (art. 16(1)(11));
- depreciation of a passenger car on the part of its value above the cap: PLN 225,000, 150,000 or 100,000 (art. 16(1)(4));
- 25% of running costs of a passenger car also used privately (art. 16(1)(51));
- debt financing costs above the art. 15c limit (below).

**Depreciation (art. 16a to 16m).** Fixed assets with an initial value above PLN 10,000 are depreciated at the statutory rates (art. 16f(3), 16h-16i). Small taxpayers and start-ups may write off group 3-8 assets at once, excluding passenger cars, up to PLN 213,000 of write-offs in 2026 (art. 16k(7)).

**Interest limitation (art. 15c).** Net debt financing costs (all costs of obtaining and using outside funding, net of taxable interest income) are deductible up to the higher of PLN 3,000,000 or 30% of tax EBITDA. Tax EBITDA is total taxable revenue less interest revenue, minus tax costs excluding depreciation and debt financing costs. For a tax year that is not 12 months, the PLN 3,000,000 becomes PLN 250,000 times the months started (art. 15c(1a)). The disallowed amount carries forward for five tax years (art. 15c(18)). Financial undertakings are outside the rule (art. 15c(14)). In a PGK the PLN 3,000,000 applies to the group as a whole (art. 15c(15)).

**Dividends received.** Dividends from Polish companies are exempt if the recipient is a company taxed on worldwide income in Poland or the EU/EEA, holds directly at least 10% and does so for an uninterrupted two years; the two years can be completed after the payment (art. 22(4)-(4b)). Dividends from EU/EEA companies are exempt on the same 10% and two-year conditions (art. 20(3)). Gains on selling shares fall in the capital gains basket and are taxed at 19% unless the holding company regime applies (not covered).

**Losses (art. 7(5)).** A loss from a basket can be set against income from the same basket in the next five tax years, by one of two methods:
1. up to 50% of the loss in any one year; or
2. once, up to PLN 5,000,000 in a single year of the five. Anything left is used in the remaining years, again at most 50% of the loss in any one year.

There is no carry-back. Losses are lost on a transformation, merger or division (other than one company becoming another company form), and where the company takes over a business or receives a contribution and, as a result, its main activity changes or at least 25% of its shares pass to new holders (art. 7(3)(4) and (7)). Losses on virtual currencies cannot be carried forward (art. 7(6)).

**Tax capital group, PGK (art. 1a, 7a).** Two or more Polish sp. z o.o., P.S.A. or S.A. companies can form a PGK. Conditions: average share capital of at least PLN 250,000 per company; the parent holds directly at least 75% of each subsidiary; no arrears in state-budget taxes; a written agreement for at least three tax years, registered by the head of the tax office. Filing deadline for the agreement: at least 45 days before the group's first tax year. The group's income, per basket, is the excess of the members' income over their losses (art. 7a(1)). A member's loss from before the group was formed can reduce group income only against that member's own income in the same basket, within the five-year window and at most 50% of the loss a year (art. 7a(3)-(5)). The parent computes and pays the tax and the advances (art. 1a(7)). If a condition is broken, the group loses taxpayer status and the members must recompute their own tax for the earlier years (art. 1a(10)-(10c)). The 9% rate is not available to a PGK.

## Deadlines and filing

| Step | Deadline, calendar-year company | Rule |
|---|---|---|
| Monthly advances (zaliczki) for 2026 | 20th of each following month; December advance by 20 January 2027, not due if the return is filed and the tax paid before then | art. 25(1)-(1a) |
| Quarterly advances (small taxpayers, and start-ups in their first year) | 20th of the month after each quarter; Q4 advance by 20 January 2027, with the same exception | art. 25(1b)-(1c) |
| Simplified advances (option) | Monthly, each 1/12 of the tax shown in the return filed in the previous year (the 2024 return, filed in 2025, for 2026 advances); if it showed no tax, the return from two years earlier | art. 25(6)-(7a) |
| CIT-8 return and final payment for 2026 | 31 March 2027 (end of the third month after year end) | art. 27(1) |
| Estonian CIT declaration CIT-8E | End of the third month of the following year | art. 28r(1) |
| Accounting books in JPK_CIT format | End of the seventh month after year end: 31 July 2027 for calendar 2026. The Act said the third month until Dz.U. 2026 poz. 779 changed it from 1 July 2026; for tax years that began after 31 December 2024 and ended before 1 April 2026 (calendar 2025: 31 July 2026) the same deadline was set by MF regulation Dz.U. 2026 poz. 188 | art. 9(1c) |

- **Form and channel.** CIT-8 is the return of a single company; a PGK files CIT-8AB; an Estonian CIT company files CIT-8E with attachment CIT/EZ. Minimum tax is shown on attachment CIT/M. Returns are filed only electronically (art. 27(1c)), for example through e-Urząd Skarbowy ([podatki.gov.pl, CIT forms](https://www.podatki.gov.pl/podatki-firmowe/cit/formularze-cit)).
- **Who sends JPK_CIT, and from which year.** Books are sent first for the tax year that begins after 31 December 2024 for PGKs and companies whose prior-year revenue exceeded EUR 50 million; after 31 December 2025 for companies that file JPK_VAT; after 31 December 2026 for all others (art. 66(2) of Dz.U. 2021 poz. 2105, as amended by Dz.U. 2023 poz. 1059). So a VAT-registered calendar-year company sends its 2026 books by 31 July 2027, and a company that files no JPK_VAT sends books first for 2027. Companies exempt under art. 6(1), those in art. 27a and those keeping simplified records do not send books (art. 9(1d)).
- **Simplified advances of banks.** Banks and SKOKs paying simplified advances increase or reduce them by the percentages in art. 38aa(2), 38ab(2) and 38ac(2) (for example plus 57.9% in a year taxed at 30%).
- **The 9% rate in advances.** Advances are normally computed at 19% even by a company that expects 9% (art. 25(1f)). Small taxpayers and start-ups in their first year may compute them at 9% for the months or quarters in which their cumulative revenue from the start of the year has not passed PLN 8,431,000; from the next period they use 19% (art. 25(1g)).
- **Choice of method.** The company states in the CIT-8 that it paid quarterly or simplified advances (art. 25(1e), (7a)). Simplified advances apply for the whole year (art. 25(7)) and are not available to a company that first started business in the tax year or the year before (art. 25(8)).
- **Minimum tax.** It is paid by the CIT-8 deadline (art. 24ca(12)).

## Penalties and interest

**Late payment interest (Tax Ordinance art. 56 and 56a).** Arrears of tax and of advances carry interest at 200% of the NBP lombard rate plus 2 percentage points, with a floor of 8%. With the lombard rate at 4.25% from 5 March 2026 the rate is 10.50% a year ([MF notice of 6 March 2026, M.P. 2026 poz. 269](https://isap.sejm.gov.pl/isap.nsf/DocDetails.xsp?id=WMP20260000269); [NBP base rates](https://static.nbp.pl/dane/stopy/stopy_procentowe.xml)). The rate is half (5.25%) if the company files a valid correction within six months of the filing deadline and pays the arrears within seven days of the correction (art. 56a § 1). The raised rate of 150% (15.75%) applies only to VAT and excise, not to CIT (art. 56b). Interest is rounded to whole złoty (art. 63).

**Fiscal Penal Code, in one line.** Not filing, or concealing the tax base, is an offence under KKS art. 54, a false return under art. 56, and persistent late payment a petty fiscal offence under art. 57, punished by fines in daily rates and, for the offences, possibly imprisonment ([KKS, Dz.U. 2025 poz. 633](https://isap.sejm.gov.pl/isap.nsf/DocDetails.xsp?id=WDU20250000633)). Refer these cases to a Polish tax adviser.

## Cross-border points

**Withholding on payments to non-residents (art. 21, 22, 26).** The Polish payer withholds on the day of payment and pays the tax to the tax office by the 7th of the following month (art. 26(1), (3)). A treaty rate can be used only with the recipient's certificate of residence, and the payer must take due care to check the conditions (art. 26(1)).

| Payment to a non-resident | Domestic rate | Source |
|---|---|---|
| Dividends and other profit shares | 19% | art. 22(1) |
| Interest, royalties (copyright, patents, trademarks, know-how, use of equipment) | 20% | art. 21(1)(1) |
| Advisory, accounting, market research, legal, advertising, management, data processing, recruitment, guarantees and similar services | 20% (unless a treaty gives Poland no taxing right) | art. 21(1)(2a), (2) |
| Dividends to an EU/EEA parent | Exempt if the parent is taxed on worldwide income in the EU/EEA, holds directly at least 10% for two uninterrupted years and is not itself exempt; 25% holding for Swiss parents | art. 22(4)-(4c) |
| Interest and royalties to an associated EU/EEA company | Exempt if there is a direct 25% holding either way (or a common 25% parent) held for two uninterrupted years, and the recipient is the beneficial owner | art. 21(3)-(5) |

**Pay-and-refund above PLN 2,000,000 (art. 26(2e)).** Where dividends, interest or royalties paid to the same related party exceed PLN 2,000,000 in the payer's tax year, the payer must withhold at the domestic rate (19% or 20%) on the excess, ignoring treaty rates and exemptions. The recipient then claims a refund (art. 28b). This does not apply to payments to Polish resident companies (art. 26(2eb)). It also does not apply if:
- the payer's head of entity files a statement that it holds the required documents and, after checking, knows of nothing that rules out the relief; the statement is filed by the end of the second month after the month the threshold was passed (art. 26(7a)-(7c)); or
- the payer holds an opinion on applying the preference issued by the tax authority (art. 26b).

**CFC rules (art. 24a), in one paragraph.** A Polish company pays 19% on its share of a controlled foreign company's income. A foreign entity is a CFC if it is in a listed tax haven or a state with no information-exchange agreement. It is also a CFC if all three of these hold: the Polish company, alone or with related parties, holds over 50% of capital, votes or profit rights, or controls it in fact; at least 33% of its revenue is passive (dividends, share disposals, debts, interest, royalties, financial income, rents, certain services and low-value-added related-party deals); and the tax it actually pays is at least 25% lower than Polish CIT at 19% would be. Rules for passive holding entities are in art. 24a(3)(4). The rules do not apply to a CFC taxed in the EU/EEA that carries on a substantial genuine business there (art. 24a(16)).

**Exit tax (art. 24f).** 19% on unrealised gains when a company moves assets abroad and Poland loses the right to tax their disposal, or moves its seat or management abroad, including by cross-border conversion.

**Transfer pricing.** Related-party transactions must be at arm's length (art. 11c). Documentation duties are in art. 11k to 11t. See [pl-transfer-pricing](pl-transfer-pricing.md).

## Worked examples

### Example 1: a trading sp. z o.o. at 19%

Facts (invented): Alfa sp. z o.o. trades electronics. Its tax year is calendar 2026. Its 2025 sales were PLN 20 million, so it is not a small taxpayer and pays 19%. It has no losses brought forward, no capital-gains income and no interest above PLN 3,000,000. Profit before tax in the 2026 accounts is PLN 1,000,000. That figure already includes:
- PLN 20,000 of restaurant and hospitality spend for clients;
- a PLN 5,000 administrative fine;
- PLN 45,000 of depreciation on a petrol company car worth PLN 250,000 (CO2 above 50 g/km), first entered in the asset register in January 2026.

Monthly advances paid for 2026 total PLN 185,000.

Walk-through:
1. Add back representation: 20,000 (art. 16(1)(28)).
2. Add back the fine: 5,000 (art. 16(1)(18)).
3. Car cap for a car entered in 2026 with CO2 of 50 g/km or more is PLN 100,000. The non-deductible share of depreciation is (250,000 - 100,000) / 250,000 = 60%. Add back 45,000 x 60% = 27,000 (art. 16(1)(4)).
4. Tax base: 1,000,000 + 20,000 + 5,000 + 27,000 = 1,052,000.
5. CIT at 19%: 199,880.
6. Less advances of 185,000: balance of 14,880, payable with the CIT-8 by 31 March 2027.
7. Minimum tax: profitability is far above 2%, so it does not apply.

```oa-check
name: Alfa sp. z o.o., 2026, CIT at 19% with add-backs
inputs:
  profit_before_tax: 1000000
  representation: 20000
  fine: 5000
  car_value: 250000
  car_cap: 100000
  car_depreciation: 45000
  advances_paid: 185000
steps:
  - car_nondeductible_share: (car_value - car_cap) / car_value
  - car_addback: car_depreciation * car_nondeductible_share
  - tax_base: profit_before_tax + representation + fine + car_addback
  - cit: round(tax_base * 0.19)
  - balance_due: cit - advances_paid
expected:
  car_addback: 27000
  tax_base: 1052000
  cit: 199880
  balance_due: 14880
```

### Example 2: a small taxpayer at 9% with losses brought forward

Facts (invented): Beta sp. z o.o. was set up in cash in 2021, not by any restructuring. Its 2025 sales including VAT were PLN 6,150,000, below the PLN 8,517,000 limit, so it is a small taxpayer in 2026. Its 2026 revenue is PLN 5,000,000, below the PLN 8,431,000 limit, so it can use 9%. All its income is in the "other sources" basket. Income for 2026 before loss relief is PLN 900,000. It has an unused loss of PLN 1,200,000 from 2024 in the same basket.

Walk-through:
1. Minimum tax: Beta is a small taxpayer, so it is outside the minimum tax anyway (art. 24ca(14)(7)). The ratio would also pass: income of 900,000 over revenue of 5,000,000 is 18%, well above 2%, measured before loss relief.
2. Method 1 (art. 7(5)(1)): the most Beta can deduct is 50% of the loss, 600,000. Base: 900,000 - 600,000 = 300,000. CIT at 9%: 27,000. Loss left: 600,000.
3. Method 2 (art. 7(5)(2)): a one-off deduction up to PLN 5,000,000, limited here by income. Beta deducts 900,000. Base: 0. CIT: 0. Loss left: 300,000, usable in 2027 to 2029 at no more than 600,000 (50% of the loss) in any one year.
4. Method 2 saves 27,000 in 2026. Beta can use the one-off option only once for this loss, so it should check that 2026 is the best year for it.

```oa-check
name: Beta sp. z o.o., 2026, 9% rate, loss relief by both methods
inputs:
  income_before_losses: 900000
  revenue: 5000000
  loss_bf: 1200000
  one_off_cap: 5000000
steps:
  - profitability: income_before_losses / revenue
  - used_m1: min(loss_bf * 0.5, income_before_losses)
  - base_m1: income_before_losses - used_m1
  - cit_m1: round(base_m1 * 0.09)
  - left_m1: loss_bf - used_m1
  - used_m2: min(loss_bf, one_off_cap, income_before_losses)
  - base_m2: income_before_losses - used_m2
  - cit_m2: round(base_m2 * 0.09)
  - left_m2: loss_bf - used_m2
  - saving: cit_m1 - cit_m2
expected:
  profitability: 0.18
  used_m1: 600000
  cit_m1: 27000
  left_m1: 600000
  used_m2: 900000
  cit_m2: 0
  left_m2: 300000
  saving: 27000
```

## Ask the client first

1. **Status for the 9% rate.** Prior-year gross sales (with VAT), current-year revenue, the tax year dates, and how the company was formed (any conversion, merger, division or contribution of a business in this year or the last).
2. **Regime.** Classic CIT, Estonian CIT (when ZAW-RD was filed, who the shareholders are, headcount, passive income share) or a PGK.
3. **Losses.** The loss schedule by year and basket, how much has been used, whether the one-off PLN 5m option has been used for each loss, and any change of ownership or activity.
4. **Financing and related parties.** Net debt financing costs and tax EBITDA; related-party costs for services, royalties and financing, for the minimum tax and shifted-income tests.
5. **Payments abroad.** Dividends, interest, royalties and services paid to non-residents in 2026, the totals per related party against PLN 2,000,000, and the residence certificates and beneficial-ownership documents held.
6. **Advances.** The method used in 2026 (monthly, quarterly, simplified) and the amounts paid.

## Sources

| Source | URL | Read on |
|---|---|---|
| CIT Act, consolidated text Dz.U. 2026 poz. 554 (ISAP record) | https://isap.sejm.gov.pl/isap.nsf/DocDetails.xsp?id=WDU20260000554 | 2026-10-22 |
| CIT Act, Sejm unified text including Dz.U. 2026 poz. 554, 779, 846, 912, 1123 (arts. 1, 1a, 3, 4a, 7, 7a, 8, 9, 15c, 16, 16f, 16k, 19, 20, 21, 22, 24a, 24aa, 24ca, 24f, 25, 26, 27, 28c-28t, 38aa-38ad, 38ec) | https://api.sejm.gov.pl/eli/acts/DU/2026/554/text/U/D20260554Lj.pdf | 2026-10-22 |
| Amending act Dz.U. 2025 poz. 1658 (bank rates, 9% revenue test, from 1 January 2026) | https://api.sejm.gov.pl/eli/acts/DU/2025/1658/text.pdf | 2026-10-22 |
| Amending act Dz.U. 2026 poz. 779 (JPK_CIT deadline, from 1 July 2026; corrects art. 38ab(1)(2)(b)) | https://api.sejm.gov.pl/eli/acts/DU/2026/779/text.pdf | 2026-10-22 |
| MF regulation Dz.U. 2026 poz. 188 (seventh-month JPK_CIT deadline for tax years ending before 1 April 2026) | https://api.sejm.gov.pl/eli/acts/DU/2026/188/text.pdf | 2026-10-22 |
| Act Dz.U. 2021 poz. 2105, art. 66 (JPK_CIT phase-in), as amended by Dz.U. 2023 poz. 1059 | https://api.sejm.gov.pl/eli/acts/DU/2023/1059/text.pdf | 2026-10-22 |
| Amending act Dz.U. 2026 poz. 1371 (transfer pricing information, cash payments) | https://api.sejm.gov.pl/eli/acts/DU/2026/1371/text.pdf | 2026-10-22 |
| Act on top-up taxation (Pillar Two), Dz.U. 2024 poz. 1685 | https://api.sejm.gov.pl/eli/acts/DU/2024/1685/text.pdf | 2026-10-22 |
| Tax Ordinance, Sejm unified text of Dz.U. 2026 poz. 622 (arts. 56, 56a, 56b, 63) | https://api.sejm.gov.pl/eli/acts/DU/2026/622/text/U/D20260622Lj.pdf | 2026-10-22 |
| Fiscal Penal Code, Sejm unified text of Dz.U. 2025 poz. 633 (arts. 54, 56, 57) | https://api.sejm.gov.pl/eli/acts/DU/2025/633/text/U/D20250633Lj.pdf | 2026-10-22 |
| MF notice on late payment interest rates, M.P. 2026 poz. 269 | https://api.sejm.gov.pl/eli/acts/MP/2026/269/text.pdf | 2026-10-22 |
| podatki.gov.pl, classic CIT rates and limits (2026 limits: PLN 8,517,000, 8,431,000, 213,000; car caps; bank rates) | https://www.podatki.gov.pl/podatki-firmowe/cit/cit-klasyczny/stawki-i-limity | 2026-10-22 |
| podatki.gov.pl, Estonian CIT rates and limits | https://www.podatki.gov.pl/podatki-firmowe/cit/cit-estonski/stawki-i-limity-w-estonskim-cit | 2026-10-22 |
| podatki.gov.pl, Estonian CIT basic information (conditions, ZAW-RD, CIT-8E) | https://www.podatki.gov.pl/podatki-firmowe/cit/cit-estonski/informacje-podstawowe-cit-estonski | 2026-10-22 |
| podatki.gov.pl, CIT forms (CIT-8 (34), CIT-8AB (9), CIT-8E (4), CIT/M) | https://www.podatki.gov.pl/podatki-firmowe/cit/formularze-cit | 2026-10-22 |
| NBP, EUR mid rate 2 January 2026 (4.2156) and 1 October 2025 (4.2586) | https://api.nbp.pl/api/exchangerates/rates/a/eur/2026-01-02/?format=json and https://api.nbp.pl/api/exchangerates/rates/a/eur/2025-10-01/?format=json | 2026-10-22 |
| NBP base interest rates (lombard 4.25% from 5 March 2026) | https://static.nbp.pl/dane/stopy/stopy_procentowe.xml | 2026-10-22 |

The ISAP pages (isap.sejm.gov.pl) served a browser check to scripted requests on 2026-10-22, so the law texts were read from the Sejm's own ELI service (api.sejm.gov.pl), which serves the same documents.

Not yet confirmed: Ministry of Finance explanations on whether the minimum tax ratio is measured before loss relief (none found; the skill follows the wording of art. 24ca(1) and art. 7(1)); how much of the Estonian CIT ryczałt a shareholder can credit against personal income tax on a dividend (PIT Act); treaty withholding rates; whether exit tax can be paid in instalments. The late payment interest rate of 10.50% was still current on 2026-10-22 (NBP lombard rate unchanged since 5 March 2026); it moves with any later NBP change.

> Contributed by Ryan Duguid.

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
