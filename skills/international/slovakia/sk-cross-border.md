---
name: sk-cross-border
description: "Use this skill for Slovak cross-border income tax in 2026 (calendar year). It covers who is a Slovak tax resident (home, 183 days, seat or place of effective management), what Slovak-source income a non-resident is taxed on, when a permanent establishment exists (six months, 183 days of services, dependent agents, repeat platform letting), withholding tax at 19%, 7% on dividends to individuals and 35% for non-cooperating states, the 19% / 35% security deduction (zabezpečenie dane) on payments to non-EU/EEA non-residents, the EU interest and royalty exemption, dividends paid abroad, the treaty credit and exemption methods, and the company exit tax at 21%. Trigger on: zrážková daň, zabezpečenie dane, nerezident, stála prevádzkareň, Slovak withholding tax, paying a foreign supplier from Slovakia, moving to or leaving Slovakia, foreign tax credit Slovakia, exit tax Slovakia. Out of scope: slovakia-pit (individual return), sk-corporate-income-tax, sk-payroll-social, slovakia-vat-registration-4-7-7a and slovakia-vat-return (VAT), transfer pricing."
version: 0.1
jurisdiction: SK
tax_year: 2026
last_updated: 2026-10-23
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Slovakia: cross-border income tax (2026)

This skill covers what happens in Slovak income tax when income, people or companies cross the border. The law is the Income Tax Act, Act No. 595/2003 Coll. (zákon o dani z príjmov, "ZDP"), in the version in force from 1 January 2026 to 30 December 2026. Procedure, penalties and interest come from the Tax Procedure Code, Act No. 563/2009 Coll. (daňový poriadok). The authority is the Financial Administration (Finančná správa SR). The currency is the euro.

Detail lives in the sibling skills. Read [slovakia-pit](slovakia-pit.md) for the individual return, [sk-corporate-income-tax](sk-corporate-income-tax.md) for companies, [sk-payroll-social](sk-payroll-social.md) for payroll and social contributions, and [slovakia-vat-registration-4-7-7a](slovakia-vat-registration-4-7-7a.md) for VAT on cross-border services. Those four skills still carry 2025 figures.

**What changed for 2026.** The 2025 consolidation package, Act No. 261/2025 Coll. of 24 September 2025, did not change the withholding rules (§ 43) or the security rules (§ 44). It did change the individual rate bands to 19%, 25%, 30% and 35% for 2026 (§ 15 letter a), § 52zzzj), cut the personal allowance bands, and replaced the company minimum tax scale (§ 46b(2)). The 7% dividend rate and the 10% / 21% / 24% company rates were already in force from 2025. Set against the version in force from 1 December 2025, the 2026 text of § 2, § 13, § 16, § 17f, § 17g, § 44 and § 45 is unchanged. In § 43 only the content of the withholding notice changed (§ 43(11)): for each non-resident recipient it now gives the income type (for § 16(1)(e) points 1, 2, 4, 9 and 11), the amount, the rate, the recipient's address and its foreign tax number.

## Who this applies to

### Individuals

An individual has unlimited tax liability in Slovakia (is resident) if they have permanent residence (trvalý pobyt), a home (bydlisko), or habitually stay here (§ 2 letter d) point 1 ZDP).

- **Home.** A person has a home here if they have accommodation that is not only occasional, and their personal and economic ties show an intention to stay there permanently (§ 2 letter d) point 1a).
- **183 days.** A person habitually stays here if present for at least 183 days in the calendar year, in one stretch or several. Every day started counts (§ 2 letter d) point 1b).
- **Study or medical treatment only.** A person here only to study or for medical treatment is not resident (§ 2 letter e) point 2).
- **Treaty tie-breaker.** A person who is resident under Slovak law but resident in the other state under a tax treaty has limited liability (§ 2 letter e) point 1).

### Companies

A legal person is resident if its seat or its place of effective management is in Slovakia. The place of effective management is where the key management and business decisions for the entity as a whole are made, even if that address is not in the commercial register (§ 2 letter d) point 2). A company that a treaty treats as resident in the other state has limited liability (§ 2 letter e) point 3).

### Scope of tax

- Residents are taxed on Slovak and foreign income (§ 2 letter f)).
- Non-residents are taxed only on Slovak-source income listed in § 16 (§ 2 letter g)).

### Who acts

- **Slovak payers** (companies, sole traders, permanent establishments) paying non-residents. They withhold tax (§ 43) or a security deduction (§ 44) and they are liable if they do not (§ 43(12), § 44(6)).
- **Non-residents** with Slovak income: employees, service providers, sellers of Slovak property or shares, and foreign companies with a Slovak permanent establishment.
- **Residents** with foreign income who need double tax relief (§ 45).
- **Companies** moving assets, business or their residence out of Slovakia (§ 17f, exit tax).

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| Residence: days of presence that make an individual resident | 183 days in the calendar year, any day started counts | 2026 | https://static.slov-lex.sk/static/SK/ZZ/2003/595/20260101.html (§ 2 d) 1b) |
| Withholding tax, general rate | 19% | 2026 | https://static.slov-lex.sk/static/SK/ZZ/2003/595/20260101.html (§ 43(1)(b)) |
| Withholding tax on dividends and similar profit shares paid to individuals | 7% | 2026 | https://static.slov-lex.sk/static/SK/ZZ/2003/595/20260101.html (§ 43(1)(a), § 43(3)(r)) |
| Withholding tax on any withheld income paid to a taxpayer of a non-cooperating state | 35% | 2026 | https://static.slov-lex.sk/static/SK/ZZ/2003/595/20260101.html (§ 43(1)(c), § 2 x)) |
| Withholding on yields from Slovak and EU/EEA government bonds paid to non-business entities | 13% | 2026 | https://static.slov-lex.sk/static/SK/ZZ/2003/595/20260101.html (§ 43(1)(d), § 43(3)(v)) |
| Security deduction on payments to non-residents outside the EU/EEA | 19% of the payment | 2026 | https://static.slov-lex.sk/static/SK/ZZ/2003/595/20260101.html (§ 44(2)) |
| Security deduction on payments to a taxpayer of a non-cooperating state, or where the beneficial owner is not shown | 35% of the payment | 2026 | https://static.slov-lex.sk/static/SK/ZZ/2003/595/20260101.html (§ 44(2), § 44(7)) |
| Security deduction ordered by a tax office decision | 9.5% of the payment | 2026 | https://static.slov-lex.sk/static/SK/ZZ/2003/595/20260101.html (§ 44(1)) |
| EU interest and royalty exemption: holding | at least 25% direct holding, for at least 24 months in a row | 2026 | https://static.slov-lex.sk/static/SK/ZZ/2003/595/20260101.html (§ 13(2)(f), (h)) |
| Permanent establishment: one-off activity; building site or construction or assembly project | one-off activity: more than 6 months in any 12-month period; site or project: activity of the non-resident or its related persons over 6 months | 2026 | https://static.slov-lex.sk/static/SK/ZZ/2003/595/20260101.html (§ 16(2)) |
| Permanent establishment: services performed in Slovakia | more than 183 days in any 12-month period | 2026 | https://static.slov-lex.sk/static/SK/ZZ/2003/595/20260101.html (§ 16(2)) |
| Non-resident share sale: real-estate-rich company test | Slovak real estate over 50% of equity | 2026 | https://static.slov-lex.sk/static/SK/ZZ/2003/595/20260101.html (§ 16(1)(h)) |
| Non-resident individual: spouse allowance and PEPP and supplementary pension contributions deductible | Slovak income at least 90% of worldwide income | 2026 | https://static.slov-lex.sk/static/SK/ZZ/2003/595/20260101.html (§ 11(7)) |
| Individual rates (resident and non-resident) | 19% up to 154.8 x subsistence minimum; 25% to 212.4 x; 30% to 264 x; 35% above. A sole trader with business revenue up to EUR 100,000 pays 15% on that base | 2026 | https://static.slov-lex.sk/static/SK/ZZ/2003/595/20260101.html (§ 15 a) 1 to 3) |
| Company rates | 10% (taxable revenue up to EUR 100,000); 21%; 24% (taxable revenue over EUR 5,000,000) | 2026 | https://static.slov-lex.sk/static/SK/ZZ/2003/595/20260101.html (§ 15 b) 1) |
| Exit tax on a company's special tax base | 21% | 2026 | https://static.slov-lex.sk/static/SK/ZZ/2003/595/20260101.html (§ 15 b) 3, § 17f(5)) |
| Exit tax instalments (move to EU/EEA state with recovery agreement) | up to 5 years | 2026 | https://static.slov-lex.sk/static/SK/ZZ/2003/595/20260101.html (§ 17g(1)) |
| Exit tax instalments: no lien needed | tax up to EUR 3,000 | 2026 | https://static.slov-lex.sk/static/SK/ZZ/2003/595/20260101.html (§ 17g(5)) |
| Cooperating states (§ 2 x)): Ministry of Finance list valid from 1 January 2026 | 138 states and jurisdictions, 71 of them through a tax treaty; Russia is not on it | 2026 | https://www.mfsr.sk/files/archiv/39/Zoznam-spolupracujucich-statov-podla-2-pism-x-zakona-c-595_2003-Z-z_1.1.2026.pdf |
| Late payment interest (also on unremitted withholding and security) | 4 x ECB base rate a year, at least 15% a year, at most 4 years | 2026 | https://static.slov-lex.sk/static/SK/ZZ/2009/563/20260901.html (§ 156(1)-(2)) |

## The taxable base

### Slovak-source income of a non-resident (§ 16(1))

A non-resident is taxed on income from:

- activity through a Slovak permanent establishment, and disposals of its property (letter a));
- employment carried out in Slovakia, or on aircraft or ships run by a Slovak resident (letter b));
- services provided in Slovakia, including commercial, technical or other advice, management, intermediation, construction and assembly, even without a permanent establishment (letter c));
- artists and sportspeople performing in Slovakia, paid directly or through an intermediary (letter d));
- payments by Slovak residents or Slovak permanent establishments of: royalties for industrial property, software, designs, plans and know-how; copyright royalties; interest on loans, deposits and similar yields (not bonds); rent for movables in Slovakia; disposals of Slovak movables, registered rights and Slovak-issued securities; directors' and board fees; prizes; pensions and annuities; dividends and liquidation shares; fees for commercial, technical or other advice, data processing, management, intermediation and marketing to the extent the payer deducts them; capital fund distributions; and crypto-asset sales (letter e) points 1 to 13);
- sale, rent or other use of Slovak real estate (letter f));
- sale of shares in a Slovak company or cooperative (letter g)), or in any company whose Slovak real estate is more than 50% of its equity (letter h)).

### Permanent establishment (stála prevádzkareň, § 16(2))

A permanent establishment is a fixed place through which the non-resident carries on its activity in Slovakia: a branch, office, workshop, worksite, point of sale, technical equipment, or a place of extraction. A place is fixed if it is used continuously or repeatedly.

- A one-off activity creates a permanent establishment only after more than six months in any 12 months. A building site or construction or assembly project is one only if the activity of the non-resident or its related persons there lasts more than six months.
- Services provided in Slovakia by the non-resident or its staff create one after more than 183 days in any 12 months.
- Repeated intermediation of transport or accommodation, including through a digital platform, counts as a fixed place.
- A dependent agent is one: a person acting on the non-resident's instructions who habitually negotiates, concludes or arranges contracts, or plays the principal role leading to contracts the non-resident concludes without material change, in the non-resident's name or for its property or services.

Income of a registered permanent establishment is not withheld at source (§ 43(2)). It is declared in a return and taxed at the normal rates.

### Withholding tax (zrážková daň, § 43)

The payer withholds tax from the gross amount (§ 43(4)) when it pays, remits or credits the income. Setting off mutual claims counts as payment (§ 43(10)).

Paid to a non-resident (§ 43(2)), withholding applies to:

- services in Slovakia and artists or sportspeople (§ 16(1)(c) and (d));
- royalties, rent of movables, advisory, management, data processing and marketing fees, and capital fund distributions (§ 16(1)(e) points 1, 2, 4, 10 and 12);
- interest and other yields on loans, and derivative income;
- paid-out revaluation differences on a company conversion (§ 16(1)(k));
- dividends only when the recipient is a taxpayer of a non-cooperating state.

Paid to anyone (§ 43(3)), withholding also applies to bank interest, fund yields, lottery winnings, and dividends paid to individuals (point r), among others.

The rates are 19% as the rule, 7% for dividends to individuals, and 35% for any of this income paid to a taxpayer of a non-cooperating state (§ 43(1)). If the payer cannot show who the beneficial owner of a non-resident's Slovak-source income is, it withholds 35% (§ 43(25)).

**Withholding as final tax or as an advance.** Withholding settles the tax (§ 43(6)). A non-resident from an EU or EEA state may instead treat tax withheld on services, royalties, rent of movables, advisory fees and interest as an advance, file a Slovak return, and claim back any excess. A non-resident artist or sportsperson from any state may do the same for § 16(1)(d) income (§ 43(6)(a) and (b), § 43(7)).

### Security deduction (zabezpečenie dane, § 44)

This catches Slovak-source income of a non-resident that is not withheld under § 43 and is not employment income. Examples are the sale of Slovak shares, real estate or movables, income of a Slovak permanent establishment, and a non-resident partner's share in a Slovak v.o.s. or k.s. (§ 16(3)).

- It applies only where the recipient is outside the EU and EEA (§ 44(2)). Payments to EU and EEA residents are not subject to it.
- The payer deducts 19% of the gross payment, or 35% if the recipient is a taxpayer of a non-cooperating state (§ 44(2)) or the beneficial owner is not shown (§ 44(7)).
- The deduction is a prepayment, not the final tax. The non-resident files a return and credits it. If the non-resident files no return, the tax office may treat the security as settling the tax (§ 44(5)).
- If the non-resident shows a tax office certificate that it pays Slovak tax advances (§ 34 or § 42), the payer does not deduct (§ 44(4)).
- Separately, a tax office may order any payer by decision to deduct 9.5% from payments to a named taxpayer (§ 44(1)).

### Non-cooperating states (§ 2 letter x))

A taxpayer of a non-cooperating state is one whose permanent residence or seat is not in a state on the list published by the Ministry of Finance. The Ministry lists states with a tax treaty, a tax information exchange agreement, or a multilateral exchange agreement with Slovakia. It removes states on the EU list of non-cooperative jurisdictions as at 1 January, and states with no corporate income tax or a zero rate.

The list valid from 1 January 2026 was built from the EU list published in the Official Journal on 17 October 2025 (C/2025/5613). It has 138 entries. A state with a Slovak tax treaty can still be non-cooperating: Russia has a treaty with Slovakia but is not on the list, so a payment to a Russian resident carries 35%. Check the list in force on the day of payment (https://www.mfsr.sk/files/archiv/39/Zoznam-spolupracujucich-statov-podla-2-pism-x-zakona-c-595_2003-Z-z_1.1.2026.pdf).

### Dividends paid abroad

- **To a non-resident individual:** 7% withholding (§ 43(1)(a), § 43(3)(r)), unless a lower treaty rate applies.
- **To a non-resident company:** not subject to Slovak tax, to the extent the dividend was not a deductible expense of the payer (§ 12(7)(c)).
- **To a taxpayer of a non-cooperating state:** 35% (§ 12(7)(c) point 1, § 16(1)(e) point 9, § 43(1)(c)).

### EU interest and royalty exemption (§ 13(2)(f) and (h))

Interest and royalties paid by a Slovak company (or an EU company's Slovak permanent establishment) to an EU company are exempt if the recipient is the beneficial owner and, for at least 24 months in a row up to the payment date, one of these holds:

1. the payer holds at least 25% of the recipient directly;
2. the recipient holds at least 25% of the payer directly; or
3. a third EU company holds at least 25% of both directly.

If the 24 months are completed after the payment, the payer withholds, and the recipient may claim the tax back from the first day after the 24 months end (§ 43(21)).

### Double tax relief for residents (§ 45)

- **Treaty state, credit method.** Foreign tax is credited up to the lower of (a) the tax the treaty allows the other state to charge and (b) the Slovak tax on the foreign income. The limit is Slovak tax times the foreign base as a percentage of the total base. For an individual the total base is taken before the § 11 personal allowances. Only tax on income included in this year's base can be credited (§ 45(1)).
- **Treaty state, exemption method.** The foreign base is left out of the Slovak base (§ 45(1)).
- **Employment income.** It is exempt if taxed abroad and it comes from a non-treaty state, from EU institutions, or from a treaty state where exemption gives a better result than the treaty method (§ 45(3)).
- **Different foreign tax year.** If the foreign tax receipt is not available by the filing deadline, the return shows the expected foreign income and tax (§ 45(2)).

§ 45 gives no other unilateral relief. Foreign income from a non-treaty state that is not employment income gets no credit under § 45.

### Exit tax (§ 17f and § 17g)

This applies to companies only (§ 2 letter d) point 2, and non-resident companies with a Slovak permanent establishment). The special tax base, taxed at 21%, is:

- **Transfer of assets** from Slovak head office to a foreign permanent establishment, or from a Slovak permanent establishment abroad: fair value at the time of transfer minus the tax value (§ 17f(1)).
- **Move of residence or business:** fair value of the assets and liabilities that are no longer connected with a Slovak permanent establishment, worked out as § 17a sets out (§ 17f(2)).

The total special base cannot be negative (§ 17f(3)). Temporary transfers for securities financing, collateral, prudential capital or liquidity that return within 12 months are excluded (§ 17f(4)). On a move to an EU or EEA state with a recovery assistance agreement, the tax can be paid in instalments over five years, with interest, on request in the return (§ 17g). A company arriving in Slovakia takes a step-up to the value taxed on exit abroad, capped at fair value (§ 17f(8)).

There is no exit tax for individuals in the ZDP.

## Deadlines and filing

- **Withholding tax:** the payer pays it to the tax office by the 15th of each month for the previous month, and files the notice of withholding (oznámenie o zrazení a odvedení dane) by the same date (§ 43(11)).
- **Security deduction:** paid by the 15th of each month for the previous month, with the notice on the official form (§ 44(3)).
- **Income tax return:** within three months after the end of the tax period, so 31 March 2027 for 2026. The tax is due by the same date (§ 49(2)).
- **Extension:** a notice filed before the deadline extends it by up to three whole months, or up to six whole months if the income includes foreign-source income. The tax is then due by the new date (§ 49(3)(a) and (b)).
- **Exit tax:** due with the return, or in instalments if allowed (§ 17g(1) to (3)).
- **Recipient's challenge:** a recipient who doubts a withholding may ask the payer for an explanation within 12 months; the payer has 30 days to reply and correct it (§ 43a(1)).

## Penalties and interest

All from the Tax Procedure Code, Act No. 563/2009 Coll.

- **Late return:** a fine of EUR 100 to EUR 30,000 (§ 155(1)(a)). A tax office does not impose a fine set within a range for the first breach (§ 155(4)).
- **Late notice or other reporting duty:** EUR 100 to EUR 10,000 (§ 155(1)(d) and (e)).
- **Under-declared tax found by the tax office:** a fine of 3 x the ECB base rate a year, at least 10% a year, on the extra tax, counted per day from the original deadline, at least 1% of the extra tax and at most the extra tax (§ 155(1)(f), (2) and (5)). Paid within 15 days, it drops to two thirds (§ 155(17)).
- **Own correction by supplementary return:** 1 x the ECB base rate a year, at least 3% a year; 2 x, at least 7%, if filed after a tax audit is announced (§ 155(1)(g), (h) and (5)).
- **Late payment interest:** 4 x the ECB base rate a year, at least 15% a year, for each day late, for at most four years (§ 156(2)). It applies to unremitted withholding tax and unremitted security (§ 156(1)(e) and (f)).
- **Payer liability:** a payer that does not withhold, withholds too little or pays late is pursued for the tax as if it were its own (§ 43(12), § 44(6)).

## Cross-border points

- **Treaties override domestic rates.** A treaty can lower or remove Slovak withholding (§ 1(2)). The Ministry of Finance list valid from 1 January 2026 names 71 states with a Slovak tax treaty, including Kyrgyzstan, whose treaty applies from 1 January 2026. Read the treaty in force for the year of payment for the rate.
- **Beneficial owner.** The beneficial owner is the person who receives the income for its own benefit and can use it freely, or its permanent establishment. An intermediary is not (§ 2 letter af)). A payer that cannot show the beneficial owner applies 35% (§ 43(25), § 44(7)).
- **Reporting the recipient.** The withholding notice names each non-resident recipient, with its address and foreign tax number, and splits royalties, rent of movables, dividends and similar income by type (§ 43(11)(b)).
- **Social security, payroll and VAT** are not in this skill. Posted workers and A1 certificates go with [sk-payroll-social](sk-payroll-social.md). VAT on services bought from abroad goes with [slovakia-vat-registration-4-7-7a](slovakia-vat-registration-4-7-7a.md).
- **Transfer pricing** between related parties, including a head office and its permanent establishment (§ 2 letter r)), is out of scope here.

## Worked examples

### Example 1: royalty paid by a Slovak s.r.o. to a foreign company

A Slovak s.r.o. pays a software licence fee of EUR 8,000 in March 2026 to a non-EU company resident in a state on the Ministry's list. The company has no Slovak permanent establishment. The client has no residence certificate from the recipient, so no treaty rate is applied at payment. Software licence fees are § 16(1)(e) point 1 income, so the payer withholds 19% (§ 43(1)(b), § 43(2)). It withholds EUR 1,520, pays EUR 6,480 to the recipient, and pays the EUR 1,520 to the tax office with the notice by 15 April 2026.

If the recipient were a taxpayer of a non-cooperating state, the rate would be 35%: EUR 2,800 withheld. If the recipient were an EU company that had held 25% of the payer directly for 24 months and was the beneficial owner, the fee would be exempt (§ 13(2)(h)).

```oa-check
name: SK royalty to a foreign company, 19% and 35% withholding (2026)
inputs:
  royalty: 8000
steps:
  - wht_19: pct(royalty, 19)
  - net_paid: royalty - wht_19
  - wht_35_noncooperating: pct(royalty, 35)
expected:
  wht_19: 1520.00
  net_paid: 6480.00
  wht_35_noncooperating: 2800.00
```

### Example 2: foreign tax credit capped at the treaty rate

A Slovak company has taxable revenue of EUR 3,000,000 in 2026, so its rate is 21% (§ 15 letter b) point 1b). Its tax base is EUR 400,000. That includes EUR 50,000 of royalties from a treaty state with no related expenses. The other state withheld 15% (EUR 7,500), but the treaty lets it charge only 10% (EUR 5,000) and uses the credit method.

Slovak tax is EUR 84,000. The foreign share of the base is 12.5%, so the credit limit is EUR 10,500. The credit is the lowest of the tax paid (EUR 7,500), the treaty maximum (EUR 5,000) and the limit (EUR 10,500): EUR 5,000 (§ 45(1)). Tax payable is EUR 79,000. The extra EUR 2,500 is not credited in Slovakia; the company must claim it back from the other state.

```oa-check
name: SK company, credit for foreign royalty tax capped at treaty rate (2026)
inputs:
  tax_base: 400000
  foreign_base: 50000
  foreign_tax_paid: 7500
steps:
  - sk_tax: pct(tax_base, 21)
  - foreign_share_pct: foreign_base / tax_base * 100
  - credit_limit: sk_tax * foreign_share_pct / 100
  - treaty_max: pct(foreign_base, 10)
  - credit: min(foreign_tax_paid, treaty_max, credit_limit)
  - tax_payable: sk_tax - credit
  - not_creditable: foreign_tax_paid - credit
expected:
  sk_tax: 84000.00
  foreign_share_pct: 12.50
  credit_limit: 10500.00
  credit: 5000.00
  tax_payable: 79000.00
  not_creditable: 2500.00
```

## Ask the client first

1. Where does the recipient (or the client) have its home, seat and place of effective management, and how many days was the person in Slovakia in 2026?
2. What exactly is the payment for (service done in Slovakia or abroad, royalty, interest, dividend, sale of shares or property), and when is it paid or credited?
3. Is the recipient in the EU or EEA, in a state on the Ministry of Finance's list, or in a non-cooperating state, and do you hold its residence certificate and beneficial owner evidence?
4. Does the recipient have a registered Slovak permanent establishment, or staff or a site in Slovakia for more than six months or 183 days?
5. For related-party interest or royalties within the EU: what are the direct holdings, and since when?
6. For a company: is it moving assets, business or its seat abroad in 2026?

## Sources

| Source | URL | Read on |
|---|---|---|
| Act No. 595/2003 Coll. on income tax, version in force 1 Jan 2026 to 30 Dec 2026 (§ 1, § 2, § 11, § 12, § 13, § 15, § 16, § 17f, § 17g, § 43, § 43a, § 44, § 45, § 49, § 52zzzj) | https://static.slov-lex.sk/static/SK/ZZ/2003/595/20260101.html | 2026-10-23 |
| Act No. 261/2025 Coll. (2025 consolidation package), as published | https://static.slov-lex.sk/static/SK/ZZ/2025/261/vyhlasene_znenie.html | 2026-10-23 |
| Act No. 563/2009 Coll., Tax Procedure Code, version in force from 1 Sep 2026 (§ 154, § 155, § 156) | https://static.slov-lex.sk/static/SK/ZZ/2009/563/20260901.html | 2026-10-23 |
| Financial Administration, international taxation legislation page | https://www.financnasprava.sk/sk/financna-sprava/legislativa/dane/priame-dane/dan-z-prijmov/medzinarodne-zdanenie | 2026-10-23 |
| Ministry of Finance, list of cooperating states under § 2 x), valid from 1 Jan 2026 (with the treaty or agreement for each state) | https://www.mfsr.sk/files/archiv/39/Zoznam-spolupracujucich-statov-podla-2-pism-x-zakona-c-595_2003-Z-z_1.1.2026.pdf | 2026-10-23 |
| Financial Directorate, list of Slovak tax treaties in force (1/MZ/2022/IM, as at 1 Jan 2022; shows the Russia treaty) | https://www.financnasprava.sk/_img/pfsedit/Dokumenty_PFS/Zverejnovanie_dok/Aktualne/DP/Medzinarodne_zdanovanie/2022/2021.01.05_1_MZ_2022_IM.pdf | 2026-10-23 |

Not yet confirmed: treaty withholding rates for individual states; the subsistence minimum (životné minimum) at 1 January 2026, so the 2026 individual bands are given here as multiples only; the ECB base rate used for interest and fines on a given date; the text of a later version of Act No. 595/2003 in force from 31 December 2026 (Act No. 406/2025 Coll.), which is not covered here.

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
