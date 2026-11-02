---
name: ee-cross-border
description: "Estonian cross-border tax for tax year 2026, from the Income Tax Act (tulumaksuseadus) in force from 1 October 2026 and Estonian Tax and Customs Board guidance. Covers individual residence (home in Estonia or 183 days in 12 months), how non-residents are taxed on Estonian-source income, withholding on payments to non-residents (22% on wages, board fees and rent; 10% on services performed in Estonia, royalties and performers), dividends under the distribution-based 22/78 system with no withholding, permanent establishments, treaty relief and residence certificates, the foreign tax credit, and the exit tax when a company moves assets or residence abroad. Confirms the 2026 rate stayed at 22% and that the 2% security tax on income and profits does not apply. Trigger on: non-resident Estonia, Estonian withholding tax, TSD annex 2, moving to Estonia, leaving Estonia, e-resident company abroad, Estonia exit tax. Out of scope: estonia-income-tax, ee-corporate-income-tax, estonia-payroll, estonia-social-contributions, estonia-vat-return."
version: 0.2
jurisdiction: EE
tax_year: 2026
last_updated: 2026-10-24
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Estonia cross-border tax: residence, non-residents, withholding, exit (tax year 2026)

Source-cited draft: not reviewed by an accountant, not for filing.

Estonia taxes individuals on the calendar year. Companies pay income tax only when they distribute profit, monthly, on form TSD. The law is the Income Tax Act (tulumaksuseadus, TuMS); paragraph numbers below are to the Estonian consolidated text on Riigi Teataja in force from 1 October 2026 to 31 December 2026. A superscript paragraph number such as 54⁵ is written "54^5". The Estonian text is the law; the English translations are for information. The authority is the Estonian Tax and Customs Board (Maksu- ja Tolliamet, ETCB).

This skill links to its siblings instead of repeating them:

- `estonia-income-tax`: the resident's return (form A, form E), the 2026 basic exemption and FIE rules.
- `ee-corporate-income-tax`: the distribution tax in general.
- `estonia-payroll` and `estonia-social-contributions`: social tax, unemployment insurance and the II pillar.
- `estonia-vat-return`: VAT on cross-border supplies.

## Who this applies to

**Individuals.** A natural person is resident if their place of residence is in Estonia, or they stay in Estonia at least 183 days in any 12 consecutive calendar months (TuMS § 6(1)). A person who meets the 183-day test is resident from the day they arrived. An Estonian diplomat or civil servant on a long-term posting abroad, and the family members with them, are also resident. The ETCB counts arrival and departure days as full days in Estonia. A place of residence is where the person permanently or primarily lives (General Part of the Civil Code Act § 14); owning a flat in Estonia does not by itself make someone resident, and a home let to others is not the owner's residence. A person who settles abroad, keeps no Estonian residence and is not in Estonia 183 days becomes non-resident from the day after leaving. Changes of residence are reported on form R (TuMS § 6(6)).

**Companies.** A legal person is resident if it was founded under Estonian law. A European company (SE) or European cooperative (SCE) with its registered seat in Estonia is also resident (TuMS § 6(2)). There is no place-of-management test in the Act. A company founded abroad and run from Estonia is a non-resident, and may have a permanent establishment in Estonia.

**Treaties.** Where a tax treaty gives a different residence, or more favourable terms than the Act, the treaty applies (TuMS § 6(5)). The ETCB then registers the person as non-resident from that date, on the foreign residence certificate.

**Scope.** A resident individual is taxed on worldwide income (TuMS § 6(1)). A non-resident is taxed only on Estonian-source income listed in TuMS § 29 (TuMS § 6(3)).

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source URL |
|---|---|---|---|
| General income tax rate (individuals, withholding, companies) | 22% | 2026 (also 2025) | https://www.riigiteataja.ee/akt/TuMS (§ 4(1)); https://www.emta.ee/en/private-client/taxes-and-payment/declaration-income/tax-rates |
| Company tax on distributions and other § 1(2) to (4) and (6) to (8) objects | Taxable amount ÷ 0.78 × 22%, so 22/78 of the net amount | 2026 | https://www.riigiteataja.ee/akt/TuMS (§ 4(1^1)) |
| Planned rise to 24% from 2026 | Cancelled; the rate stays 22% for individuals and companies | 2026 | https://www.fin.ee/uudised/2026-aastal-joustuvad-seadusemuudatused |
| Security tax of 2% on individuals' income and company profit "from the first euro" | Does not apply from 2026 | 2026 | https://www.fin.ee/uudised/riigikogu-kiitis-heaks-julgeolekumaksu-muudatused |
| Withholding on wages for work in Estonia paid to a non-resident | 22% | 2026 | https://www.riigiteataja.ee/akt/TuMS (§ 41 p 2, § 43(1) p 1) |
| Withholding on board member fees of a resident company paid to a non-resident | 22% (plus 33% social tax unless the person has an A1 certificate) | 2026 | https://www.emta.ee/en/private-client/foreigner-non-resident/non-residents/income-employment |
| Withholding on rent from property in Estonia or registered in Estonia | 22% | 2026 | https://www.emta.ee/en/private-client/foreigner-non-resident/non-residents/rental-income-and-licence-fee |
| Withholding on fees for services provided in Estonia | 10% | 2026 | https://www.riigiteataja.ee/akt/TuMS (§ 41 p 10, § 43(1) p 2) |
| Withholding on royalties (licence fees) | 10% | 2026 | https://www.riigiteataja.ee/akt/TuMS (§ 41 p 8, § 43(1) p 2) |
| Withholding on fees of non-resident performers and sportspeople for activity in Estonia | 10% | 2026 | https://www.riigiteataja.ee/akt/TuMS (§ 41 p 9, § 43(1) p 2) |
| Withholding on service fees to a company in an EU-listed non-cooperative jurisdiction, wherever the service was performed | 22% | 2026 | https://www.riigiteataja.ee/akt/TuMS (§ 29(3), § 41 p 11, § 43(1) p 1) |
| Interest paid to a non-resident | Not taxed, except interest from a fund over 50% invested in Estonian real estate with a holding of at least 10%: 22% | 2026 | https://www.riigiteataja.ee/akt/TuMS (§ 29(7)); https://www.emta.ee/en/business-client/registration-business/non-residents-e-residents/taxation-non-residents-estonian |
| Dividends paid to a non-resident (company or individual) | No withholding; the company pays 22/78 on distribution | 2026 | https://www.emta.ee/en/business-client/registration-business/non-residents-e-residents/taxation-non-residents-estonian |
| Dividend a company received (exempt under TuMS § 50(1^1)) whose underlying profit was taxed at 14/86 under former § 50^1, passed on to an individual. Not the company's own pre-2025 profit, which is taxed at 22/78 | 7% withheld (TuMS § 61(68)) | 2026 | https://www.riigiteataja.ee/akt/TuMS |
| Non-resident's gain on Estonian immovable property, Estonian-registered movables, or a 10%+ holding in an entity more than 50% in Estonian real estate | 22% of the gain | 2026 | https://www.riigiteataja.ee/akt/TuMS (§ 29(4)); https://www.emta.ee/en/business-client/registration-business/non-residents-e-residents/taxation-non-residents-estonian |
| Royalty exemption, EU or Swiss associated company | 0% if 25% held for two years or more (direct either way, or common parent); arm's-length part only | 2026 | https://www.riigiteataja.ee/akt/TuMS (§ 31(4), (5)) |
| Participation exemption on dividends received and passed on | Holding of at least 10% in the paying company | 2026 | https://www.riigiteataja.ee/akt/TuMS (§ 50(1^1)) |
| Exit tax deferral when assets or residence move within the EEA | Payable over up to five years; not for a non-EU EEA state without a recovery-assistance agreement equivalent to Directive 2010/24/EU | 2026 | https://www.riigiteataja.ee/akt/TuMS (§ 54^5(3), (4)) |
| Interest on deferred exit tax | 0.06% a day; the ETCB can cut the rate by up to 50% when it grants the schedule | 2026 | https://www.riigiteataja.ee/akt/TuMS (§ 54^5(5)); https://www.riigiteataja.ee/akt/MKS (§ 117(1), (2)) |
| Basic exemption for non-resident individuals | Only an EEA resident, on application with a residence certificate; 700 a month in 2026 | 2026 | https://www.riigiteataja.ee/akt/TuMS (§ 42(1)); https://www.emta.ee/en/private-client/foreigner-non-resident/non-residents/income-employment |
| Tax treaties | 66 in force (of 70 signed) | 2026 | https://www.fin.ee/en/double-taxation-agreements |
| Interest on late payment | 0.06% a day (21.9% a year); no claim under 10 euros; rounded to whole euros | 2026 | https://www.emta.ee/en/private-client/taxes-and-payment/payment-arrears/payment-interests |

## The taxable base

**Non-resident individuals and companies (TuMS § 29).** Estonian-source income is:

- Wages for work in Estonia, if the employer is the Estonian state, a resident, a non-resident acting as an employer in Estonia, or a non-resident through an Estonian permanent establishment, or if the person worked in Estonia at least 183 days in 12 consecutive months (§ 29(1)). With an Estonian employer the day count does not matter. A user company in Estonia counts as the employer of an agency worker (§ 29(1^3)), and the foreign agency must withhold on the Estonian wages (§ 40(3^2)).
- Fees for serving on the management or supervisory board of a resident company, wherever the work is done (§ 29(2)).
- Income from business carried on in Estonia (§ 29(3)). A service fee is taxed only where the service is provided in Estonia, except that a company in an EU-listed non-cooperative jurisdiction is taxed on every service fee from an Estonian resident (§ 29(3), § 10^1).
- Gains on Estonian immovable property, Estonian-registered movables, timber felled in Estonia, rights tied to Estonian real estate, and holdings of at least 10% in a company or fund more than 50% made up of Estonian real estate at any time in the two years before (§ 29(4)).
- Capital reductions, buy-backs and liquidation proceeds from a resident company above the cost of the holding (§ 29(5), § 15(2) and (3)).
- Rent from property in Estonia or registered in Estonia, and royalties paid by the state, a resident or an Estonian permanent establishment (§ 29(6)).
- Interest only from a real-estate fund holding as above (§ 29(7)).
- Pensions, grants, prizes and benefits paid from Estonia, and performance fees for artists and sportspeople performing in Estonia, including fees paid to a third party for their activity (§ 29(9), (10)).

**Withholding is final.** Tax withheld at the Act or treaty rate is the non-resident's final tax on that income, unless the income belongs to an Estonian permanent establishment (TuMS § 43(4)). Payments to an Estonian-registered permanent establishment, and to an FIE entered in the Estonian business register or the register of another EEA state for business income, are paid gross (TuMS § 40(2) points 2 and 3). The unemployment insurance premium withheld is deducted before withholding (TuMS § 42(5)). An EEA resident individual can claim the monthly basic exemption on written application (TuMS § 42(1)).

**Dividends.** A resident company pays 22/78 on the net dividend when it pays it (TuMS § 50(1), § 4(1^1)). The shareholder pays nothing more, whether resident or not, so there is no withholding on dividends to a non-resident. A dividend is exempt at the paying company if it is paid out of (TuMS § 50(1^1)):

1. a dividend received from a company resident and liable to tax in an EEA state or Switzerland, holding at least 10% (not from a non-cooperative jurisdiction);
2. profit of the company's permanent establishment in an EEA state or Switzerland;
3. a dividend from a company in any other state, holding at least 10%, where tax was withheld on the dividend or the underlying profit was taxed;
4. profit of a permanent establishment in another state that was taxed there.

Exemptions 1 and 3 apply only if the paying subsidiary could not deduct the dividend (§ 50(1^3)). Only tax that was compulsory under law or treaty counts (§ 50(1^2)).

**Permanent establishment of a non-resident company (TuMS § 7, § 53).** A permanent establishment is a business unit through which a non-resident carries on permanent business in Estonia. It arises from activity in a fixed place, mobile activity, or a representative authorised to conclude contracts. Its profit is computed at arm's length, as if it were an independent taxpayer (§ 7(3)). It pays 22/78 on profit it takes out of Estonia in cash or in kind, and on fringe benefits, gifts, entertainment costs and non-business payments, the same way as a resident company (§ 53(1) to (5)). Moving its business to another country, or moving assets out, counts as taking profit out; the taxable amount is market value minus book value (§ 1(4), § 53(4^13)).

**Residents with foreign income (TuMS § 45).** A resident individual adds all foreign income to taxable income. Tax is computed separately for each country. Foreign tax is credited up to the Estonian tax on that income; any excess is not refunded. Credit needs a certificate from the foreign authority or withholding agent, and only compulsory tax counts. Wages for work abroad are exempt if the person worked abroad at least 183 days in 12 consecutive months and the income was taxable there, shown by a document stating the tax, even zero (§ 13(4)). An FIE's business income from a foreign permanent establishment is exempt on the same kind of proof (§ 14(10)). The ETCB form A puts taxable foreign income in tables 8.1 to 8.7 and exempt foreign income in table 8.8.

**Companies with foreign income (TuMS § 54(5)).** A resident company, or an Estonian permanent establishment, can deduct foreign tax paid on income it received from abroad from the 22/78 it owes when it distributes that income, if the § 50(1^1) exemption does not apply. Records are kept country by country.

**Exit of a company (TuMS § 54^5, § 50(2^2)).** A resident company that moves assets to its permanent establishment in another EU state or a third country is taxed on market value minus book value of those assets at the time they leave Estonia (§ 54^5(1)). A resident company that is deleted from the register is taxed on the market value of its assets, including liquidation distributions, above the cash and in-kind contributions to equity not yet paid back (§ 50(2^2)). That charge does not apply if the business carries on in Estonia through another company or through a non-resident's permanent establishment. Both are § 1(3) objects, so the 22/78 method applies (§ 4(1^1)). Payment can be spread over up to five years if the assets go to a permanent establishment in an EEA state, or the company becomes resident in another EEA state (§ 54^5(3)). This does not apply to a non-EU EEA state that has no agreement with Estonia or the EU on recovery assistance equivalent to Directive 2010/24/EU (§ 54^5(4)). The ETCB can ask for security where there is good reason to doubt payment, and interest on the deferred tax runs under the Taxation Act (§ 54^5(5)): 0.06% a day, which the ETCB can cut by up to 50% from the date of the scheduling decision (Taxation Act § 117(1), (2)). The deferral ends and the tax falls due if the assets or the business are sold, the assets are moved on to a third country, the company's residence or the permanent establishment's business moves to a third country, the company goes bankrupt or is liquidated, or it misses instalments and does not fix it within 12 months (§ 54^5(6)). Securities financing and collateral returned within 12 months are excluded (§ 54^5(2)). Assets coming into Estonia take the value set by the state they came from, or market value if that value is not a market value (§ 50(2), § 53(4^12)).

**Individuals leaving.** The exit charge in § 54^5 is written for resident companies. A person who leaves stops being taxed on worldwide income from the day after departure, once the residence tests above are no longer met.

## Deadlines and filing

| What | Deadline | Source |
|---|---|---|
| Withholding on payments to non-residents: pay and file form TSD (annex 2) | 10th of the month after the payment | TuMS § 40(4), (5) |
| Company tax on distributions, PE profit taken out, exit tax: file TSD and pay | 10th of the month after the distribution or transfer | TuMS § 54(2), (4) |
| Residence certificate for treaty rates | Filed with the TSD, unless already in the ETCB register | TuMS § 43(2) |
| Non-resident's own return where no tax was withheld (for example rent from a natural person, or a property gain, which the ETCB says goes in table 3.1 of form V1) | 30 April of the following year | TuMS § 44(1); https://www.emta.ee/en/business-client/registration-business/non-residents-e-residents/taxation-non-residents-estonian |
| Tax due on that return | 1 October of the year the return is filed | TuMS § 46(3) |
| Change of residence (form R) | As soon as possible; on leaving, at the first opportunity | https://www.emta.ee/en/private-client/foreigner-non-resident/tax-residency/determining-residency |

The ETCB does not send a tax notice to non-residents (TuMS § 46(1)). A payment covered by a treaty exemption is still reported on TSD annex 2. The ETCB states that a legal person's residence certificate is valid for 36 months unless it says otherwise, and can then be used for all payments by all payers.

## Penalties and interest

- **Interest.** Unpaid tax carries interest from the day after the due date up to and including the day of payment (Taxation Act § 115(1)). The rate is 0.06% a day, 21.9% a year. The ETCB does not claim interest under 10 euros and rounds to whole euros.
- **Late or missing return.** Failing to file a tax return on time is a misdemeanour: a fine of up to 300 fine units (2,400 euros) for an individual, up to 3,200 euros for a legal person (Taxation Act § 154). A fine unit is 8 euros from 1 January 2025 (Penal Code § 47(1)).
- **Intentionally false or missing information that cuts tax or withholding, or raises a refund claim.** Up to 300 fine units (2,400 euros) for an individual, up to 32,000 euros for a legal person (Taxation Act § 153^1).
- **Board members.** A legal representative who breaks the taxpayer's duties wilfully or through gross negligence is jointly liable for the resulting tax debt (Taxation Act § 40(1)).

## Cross-border points

1. **Treaty rate needs a certificate before the payment.** The Act rate applies unless the payer files the recipient's residence certificate with the TSD, or the data is already in the ETCB register (TuMS § 43(2)). With no valid certificate, withhold at 10% or 22%.
2. **Services: where performed.** A foreign contractor's fee is taxed only for services provided in Estonia. Remote services from abroad carry no withholding, unless the recipient is in an EU-listed non-cooperative jurisdiction, where 22% applies to the whole fee.
3. **A permanent establishment changes the regime.** Payments to a registered Estonian PE are paid gross; the PE pays tax on profit it takes out (§ 53). An e-resident's company run from abroad stays an Estonian resident company (§ 6(2)). The country where its manager works may treat it as resident there or as having a PE there; check that country's rules and the treaty.
4. **Rent is not reduced by treaties.** The ETCB states that treaties do not limit Estonia's right to tax rent from Estonian real estate.
5. **Dividends abroad: Estonia taxes at the company, not the shareholder.** Check whether the shareholder's country gives credit for the 22/78 company tax; this skill does not cover foreign rules.
6. **Social tax follows EU rules.** A1 certificates and Regulation (EC) 883/2004 decide where social tax is paid; see `estonia-social-contributions`.

## Worked examples

### Example 1: an Estonian OÜ pays three non-residents in March 2026

Tamm OÜ, resident in Estonia, pays in March 2026: a Finnish company 20,000 euros for consulting work done at Tamm's Tallinn office; a non-resident individual 5,000 euros in royalties for software; and a Latvian individual 1,000 euros rent for a Tallinn flat. None of the recipients has an Estonian PE and no residence certificates are on file, so the Act rates apply. Consulting performed in Estonia: 10%, 2,000 euros. Royalty: 10%, 500 euros. Rent: 22%, 220 euros. Tamm files TSD annex 2 and pays 2,720 euros by 10 April 2026. If Tamm pays 30 days late, interest is 2,720 × 0.06% × 30 = 48.96, rounded to 49 euros. That is over 10 euros, so the ETCB claims it.

```oa-check
name: Tamm OUe, March 2026 payments to non-residents, no certificates, paid 30 days late
inputs:
  consulting_fee: 20000
  royalty: 5000
  rent: 1000
  days_late: 30
steps:
  - wht_consulting: consulting_fee * 0.10
  - wht_royalty: royalty * 0.10
  - wht_rent: rent * 0.22
  - total_withheld: wht_consulting + wht_royalty + wht_rent
  - interest_exact: total_withheld * 0.0006 * days_late
  - interest_claimed: round(interest_exact, 0)
expected:
  wht_consulting: 2000.00
  wht_royalty: 500.00
  wht_rent: 220.00
  total_withheld: 2720.00
  interest_exact: 48.96
  interest_claimed: 49
```

### Example 2: dividend to a German parent, then assets moved to a Finnish branch

Kask OÜ is owned by a German GmbH. In June 2026 it pays a net dividend of 78,000 euros. Of that, 30,000 euros comes from a dividend Kask received from its 60%-owned Latvian subsidiary, which is resident and liable to tax in Latvia and could not deduct it. That part is exempt under § 50(1^1) point 1. The taxed part is 78,000 − 30,000 = 48,000 euros. Company tax is 48,000 ÷ 0.78 × 22% = 13,538.46 euros, due with the June TSD by 10 July 2026. The German parent receives 78,000 with no withholding.

In September 2026 Kask moves software and equipment to its new branch in Finland. Market value is 500,000 euros and book value 200,000 euros. The taxable amount is 300,000 (§ 54^5(1)). Applying § 4(1^1): 300,000 ÷ 0.78 × 22% = 84,615.38 euros. Finland is an EEA state, so Kask can apply to spread payment over up to five years (§ 54^5(3)). If it agrees five equal annual instalments, each is 16,923.08 euros. Interest on the deferred tax runs at 0.06% a day, or less if the ETCB cuts the rate in its scheduling decision (Taxation Act § 117); it depends on the schedule the ETCB grants and is not computed here.

```oa-check
name: Kask OUe, June 2026 dividend with participation exemption, September 2026 exit to Finnish PE
inputs:
  net_dividend: 78000
  exempt_part: 30000
  market_value: 500000
  book_value: 200000
  instalments: 5
steps:
  - taxed_part: net_dividend - exempt_part
  - cit_dividend: taxed_part / 0.78 * 0.22
  - exit_gain: market_value - book_value
  - exit_tax: exit_gain / 0.78 * 0.22
  - instalment: exit_tax / instalments
expected:
  taxed_part: 48000.00
  cit_dividend: 13538.46
  exit_gain: 300000.00
  exit_tax: 84615.38
  instalment: 16923.08
```

## Ask the client first

1. Where does the individual live, and how many days were they in Estonia in each rolling 12-month period? Any form R filed, or a foreign residence certificate? (Decides residence under § 6 and the treaty tie-breaker.)
2. For each payment to a non-resident: what was paid for, and where was the work or service performed? (Decides 22%, 10% or nothing.)
3. Does the recipient have a valid residence certificate in the ETCB register, and is it a company or an individual? (Decides whether a treaty rate applies.)
4. Does the foreign party have an office, staff or a dependent agent in Estonia? (Decides a permanent establishment under § 7.)
5. For a dividend: what share does the company hold in each subsidiary whose dividends it is passing on, and where are they resident? (Decides the § 50(1^1) exemption.)
6. For a company moving assets or leaving: which assets, their market and book values, and the destination state. (Decides § 54^5 and the five-year deferral.)

## Sources

| Source | URL | Read on |
|---|---|---|
| Income Tax Act (tulumaksuseadus), consolidated text in force 01.10.2026 to 31.12.2026 (RT I, 09.07.2026, 66), §§ 1, 4, 6, 7, 13, 14, 29, 31, 40 to 43, 45, 46, 50, 53, 54, 54^5 | https://www.riigiteataja.ee/akt/TuMS | 2026-10-23 |
| Taxation Act (maksukorralduse seadus), consolidated text in force from 17.10.2026, §§ 40, 115, 117, 153^1, 154 | https://www.riigiteataja.ee/akt/MKS | 2026-10-23 |
| Penal Code (karistusseadustik), consolidated text in force 01.10.2026 to 31.12.2026, § 47 (fine unit 8 euros) | https://www.riigiteataja.ee/akt/KarS | 2026-10-24 |
| ETCB, Tax rates (2025 and 2026) | https://www.emta.ee/en/private-client/taxes-and-payment/declaration-income/tax-rates | 2026-10-23 |
| ETCB, Taxation of non-resident's Estonian income (updated 29.04.2026) | https://www.emta.ee/en/business-client/registration-business/non-residents-e-residents/taxation-non-residents-estonian | 2026-10-23 |
| ETCB, Non-residents: rental income and licence fee (updated 14.02.2025) | https://www.emta.ee/en/private-client/foreigner-non-resident/non-residents/rental-income-and-licence-fee | 2026-10-23 |
| ETCB, Non-residents: income from employment (updated 14.11.2025) | https://www.emta.ee/en/private-client/foreigner-non-resident/non-residents/income-employment | 2026-10-23 |
| ETCB, Determining residency (updated 13.03.2026) | https://www.emta.ee/en/private-client/foreigner-non-resident/tax-residency/determining-residency | 2026-10-23 |
| ETCB, Income derived in a foreign state (updated 02.12.2025) | https://www.emta.ee/en/private-client/taxes-and-payment/taxable-income/income-derived-foreign-state | 2026-10-23 |
| ETCB, Payment of interest | https://www.emta.ee/en/private-client/taxes-and-payment/payment-arrears/payment-interests | 2026-10-23 |
| Ministry of Finance, 2026 law changes (23.12.2025): 24% rise cancelled, rate stays 22% | https://www.fin.ee/uudised/2026-aastal-joustuvad-seadusemuudatused | 2026-10-23 |
| Ministry of Finance, Riigikogu approves security tax changes (18.06.2025) | https://www.fin.ee/uudised/riigikogu-kiitis-heaks-julgeolekumaksu-muudatused | 2026-10-23 |
| Ministry of Finance, Double taxation agreements (updated 07.04.2026) | https://www.fin.ee/en/double-taxation-agreements | 2026-10-23 |

Out of scope: treaty withholding rates for individual countries; use the treaty text on the Ministry of Finance list.

Not yet confirmed: the number of the act that cancelled the 24% rate. The Ministry of Finance confirms the cancellation, and the consolidated § 4(1) in force for 2026 still carries the 22% wording from RT I, 30.06.2023, 107; the cancelling act itself was not read.

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
