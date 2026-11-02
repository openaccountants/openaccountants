---
name: be-cross-border
description: "Belgian cross-border tax for 2026: who is a Belgian tax resident (home or seat of wealth, the National Register presumption, and the company test of main establishment or seat of management); arriving under the special tax regime for inbound taxpayers and researchers (35% cost allowance, EUR 70,000 minimum pay, changed by the law of 18 December 2025); non-resident income tax (belasting der niet-inwoners, BNI) and the 75% rule; the new 10% exit tax on financial assets from 1 January 2026 and the company exit charge on moving the seat abroad, with EU/EEA deferral; 30% withholding tax on outbound dividends, interest and royalties; treaty relief and EU social security coordination. Tax year 2026 (assessment year 2027). Trigger on: moving to Belgium, leaving Belgium, expat Belgium, impatriate, BBIB, BBIO, non-resident Belgium, BNI, exit tax Belgium, roerende voorheffing non-resident, digital nomad Belgium. Out of scope: be-income-tax, be-social-contributions, belgium-payroll, be-capital-gains, belgium-crypto-tax."
version: 0.2
jurisdiction: BE
tax_year: 2026
last_updated: 2026-11-01
authored_by: Michael Cutajar and the OpenAccountants team
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
category: cross-border
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Belgium cross-border tax: residence, inbound regime, non-residents, exit taxes and withholding (2026)

> **General reference only.** This skill is general tax reference material for AI-assisted work. It has not been reviewed for any person's facts. Do not rely on it to file, pay or take a tax position without review by a qualified professional in Belgium.

This is the cross-border hub for the Belgian pack. It covers what changes when a person or a company crosses the Belgian border, and it points to the other Belgian skills for the detail:

- Resident personal income tax computation: `be-income-tax`
- Self-employed social contributions: `be-social-contributions`
- Payroll withholding (bedrijfsvoorheffing) and employer contributions: `belgium-payroll`
- Crypto: `belgium-crypto-tax`
- Corporate income tax: `be-corporate-tax` (open as PR #553, not yet merged on 22 October 2026)

**Tax year.** Belgium taxes the calendar income year. Income year 2026 is assessment year (aanslagjaar) 2027. Figures below are for income year 2026 unless the row says otherwise.

**2026 is a year of change.** Three 2025-2026 laws matter here: the law of 18 December 2025 (inbound regime), the law of 6 April 2026 (a new tax on capital gains on financial assets, with an exit tax, from 1 January 2026) and the law of 15 July 2026 (personal income tax changes, including a part of art. 244bis for non-residents from assessment year 2027). For the capital gains tax itself (scope, exemption, step-up, rates), see `be-capital-gains`.

## Who this applies to

### Individuals

A person is a Belgian resident (rijksinwoner) if they have their home (woonplaats) in Belgium or, if they have no home in Belgium, their seat of wealth (zetel van fortuin) there (art. 2, §1, 1°, a) WIB 92). Both are judged on the facts: where the family lives, where the person's life is organised, where assets are managed.

- **The National Register presumption.** A person registered in the National Register of natural persons (Rijksregister) is presumed to have their home in Belgium. The presumption is rebuttable: the person can prove the contrary.
- **Married couples.** For married people (outside the cases in art. 126, §2), the tax home is where the household is established.
- **No day-count test.** Belgian law has no 183-day rule for residence. Days matter only under a tax treaty (for example the employment article) or for the inbound regime's pro rata.
- **No split-year statute, but a split year in practice.** A person who arrives or leaves during the year is a resident for part of the year and a non-resident for the rest. The resident part goes on the personal income tax return; Belgian-source income in the non-resident part goes on a non-resident (BNI) return. Confirm the arrival or departure date with registration and deregistration at the commune.

A resident is taxed on worldwide income. A non-resident is taxed only on income listed as Belgian-source (art. 227 and 228 WIB 92).

### Companies

A company is a domestic company (binnenlandse vennootschap) if it has its main establishment (voornaamste inrichting) or its seat of management (zetel van bestuur of beheer) in Belgium (art. 2, §1, 5°, b) WIB 92). A company with its registered office in Belgium is presumed to have its main establishment or seat of management there. The counter-proof is accepted only if the company also shows that it is tax resident in another state under that state's law.

A foreign company with a Belgian establishment (Belgische inrichting) is taxed in Belgium under the non-resident tax for companies on the income of that establishment (art. 227, 2° and 229 WIB 92).

### Who is out of scope here

Diplomats and other Belgian state officials posted abroad are residents by special rule (art. 2, §1, 1°, b) to d)); refer them. International organisation staff (EU, NATO and others) have their own rules; refer them.

## Rates, bands and thresholds

| Item | 2026 figure | Tax year | Source |
|---|---|---|---|
| Inbound regime (BBIB): minimum gross pay | More than EUR 70,000 a calendar year, pro rata in the year of arrival or departure (was more than EUR 75,000 to 31 December 2024) | Pay from 1 January 2025 | [Art. 32/1, §3 WIB 92; Circular 2026/C/51](https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/d6fdb273-93c6-490d-8abe-67edd8373598) |
| Inbound regime (BBIB and BBIO): tax-free recurring cost allowance | Up to 35% of gross pay, no annual cap (was 30% capped at EUR 90,000) | Pay from 1 January 2025 | [Circular 2026/C/51](https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/d6fdb273-93c6-490d-8abe-67edd8373598) |
| Inbound regime: home furnishing costs | Up to EUR 1,500 (one-off, first six months) | 2026 | [Art. 32/1, §6 WIB 92](https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/d6fdb273-93c6-490d-8abe-67edd8373598) |
| Inbound regime: duration | 5 years, extendable by 3 years | 2026 | [Art. 32/1, §7 WIB 92](https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/d6fdb273-93c6-490d-8abe-67edd8373598) |
| Inbound regime: look-back | Not resident, not living within 150 km of the Belgian border, and not subject to BNI on professional income in the 60 months before starting work | 2026 | [Art. 32/1, §3 WIB 92](https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/d6fdb273-93c6-490d-8abe-67edd8373598) |
| Personal income tax scale (residents, and non-residents via art. 243 and 243/1) | 25% to EUR 16,720; 40% to EUR 29,510; 45% to EUR 51,070; 50% above | Income 2026 | [Art. 130 WIB 92 (income 2026)](https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/796a4fc5-340e-4c89-a72a-88caa804ca96) |
| Tax-free amount (residents, and qualifying non-residents under art. 243/1) | EUR 11,550 basic amount (plus EUR 2,030 if disabled), as amended by the law of 15 July 2026 (Belgian Official Gazette 29 July 2026) from assessment year 2027 | Income 2026 | [Art. 131 WIB 92 (income 2026)](https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/f3c5d665-cac4-4cbd-b714-bd287f791751) |
| Non-resident surcharge instead of municipal tax | 7 additional centimes (7% of the federal tax). The statute says 6, raised to 7 by royal decree | Income 2026 | [Art. 245 WIB 92](https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/182fc9a7-f7c6-46ef-8da9-239fd2378423); [art. 80 KB/WIB 92](https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/ff25ff26-ce91-4678-bdb5-5a1dee98e899) |
| 75% rule for non-residents | Belgian taxable professional income at least 75% of total worldwide professional income gives resident-style allowances and deductions | Income 2026 | [Art. 243/1 WIB 92 (income 2026)](https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/a32b08a8-163e-4d48-b76f-fc6b40a89daf) |
| Exit tax on financial assets (individuals leaving) | 10% of the latent gain since 31 December 2025; 1.25% to 10% if a substantial interest (at least 20% of the rights in the company, held directly) | Departures from 1 January 2026 | [Circular 2026/C/74, nos. 153 to 156](https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/7f6b62c6-1baa-487a-8f59-c883dd5485c4) |
| Capital gains basic exemption | EUR 10,000 a year (indexed amount for assessment year 2027), reduced pro rata by months when the taxable period is not a full calendar year, as in the year of departure; EUR 1 million for a substantial interest, available over 5 consecutive taxable periods and also reduced pro rata | Income 2026 | [Art. 129/1 WIB 92; Circular 2026/C/74, nos. 51, 92, 99 and 155](https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/7f6b62c6-1baa-487a-8f59-c883dd5485c4) |
| Company moving its seat or main establishment abroad | Treated as a liquidation (art. 208 and 209 apply); corporate tax at 25% (20% on the first EUR 100,000 for small companies) | Income 2026 | [Art. 210, §1, 4° WIB 92](https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/a3d38979-9797-4133-b830-bf716b9625de); [art. 215 WIB 92](https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/3fd24be9-c978-47d0-ad39-5157070d42b1) |
| Company exit charge, EU/EEA move: spread payment | One fifth within two months of the assessment notice, the rest in four equal yearly instalments | Income 2026 | [Art. 413/1, §2 WIB 92](https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/baa69120-644c-46a1-aaab-697645ea9501) |
| Withholding tax (roerende voorheffing) on dividends, interest, royalties | 30% general rate | Income 2026 | [Art. 269, §1, 1° WIB 92 (income 2026)](https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/c9acc360-8503-4b60-b2c4-9880403d1cac) |
| Withholding: copyright income | 15% on the first band (EUR 77,220 indexed) | Income 2026 | [Art. 269, §1, 4° WIB 92](https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/c9acc360-8503-4b60-b2c4-9880403d1cac) |
| Withholding: dividends of small companies on new shares (VVPR-bis) | 20% for the second financial year after a contribution made by 31 December 2025; 18% for the third and later financial years (the 18% rate applies to dividends allocated or paid from 1 July 2026, programme law of 30 May 2026) | Income 2026 | [Art. 269, §2 WIB 92](https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/c9acc360-8503-4b60-b2c4-9880403d1cac) |
| Withholding: capital gains on financial assets (art. 90, 9°, c)) | 10%, withheld only when the recipient is a Belgian resident; never on the exit tax gain. The capital gains tax does not apply in the non-resident tax (Circular 2026/C/94) | From 1 June 2026 (law of 6 April 2026, art. 35, second paragraph); the tax itself applies to gains from 1 January 2026 | [Art. 269, §1, 5° WIB 92](https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/c9acc360-8503-4b60-b2c4-9880403d1cac) |

## The taxable base

**Residents: worldwide income.** Belgium has no remittance basis and no non-domiciled status. A resident reports worldwide income. Foreign professional income that a treaty exempts gets the reduction for foreign income (art. 155 WIB 92): it is left out of the tax but counts for the rate.

**Non-residents: Belgian-source income only (art. 228 WIB 92).** The common cases are Belgian real estate income, pay for work done in Belgium, director's fees from a Belgian company, profits of a Belgian establishment, and Belgian dividends and interest (usually settled by withholding). The tax is computed on the art. 130 scale plus 7 additional centimes (art. 245 and art. 80 KB/WIB 92). Two cases:

- **Standard non-resident (art. 243).** The scale applies, but the resident tax-free amount does not. Some reductions apply on the basis of total Belgian and foreign income.
- **Qualifying non-resident (art. 243/1, the 75% rule).** If Belgian taxable professional income is at least 75% of all professional income, Belgian and foreign, earned in the year, the non-resident is taxed almost like a resident: the tax-free amount, the family allowances and most reductions apply, worked out on total income. Check the 75% test on professional income only, not on rent or investment income.

**Inbound regime (BBIB for employees and directors, BBIO for researchers; art. 32/1 and 32/2 WIB 92).** The person stays a Belgian resident taxed on worldwide income. The benefit is that the employer can pay, on top of salary, recurring costs of the move and the Belgian posting as a tax-free reimbursement of the employer's own costs, up to 35% of gross pay, with no cap from 1 January 2025. One-off costs are also tax-free: the move itself, home furnishing up to EUR 1,500, and school fees at a private or international school for children of school age. Conditions:

1. Recruited directly abroad by a company registered in the Crossroads Bank for Enterprises, or seconded by a foreign group company to a Belgian group company or establishment.
2. In the 60 months before starting work in Belgium: not a Belgian resident, not living within 150 km of the Belgian border, and not subject to BNI on professional income.
3. BBIB only: gross Belgian taxable pay from that employer of more than EUR 70,000 a calendar year, pro rata for the year of arrival or departure by the days of the employment in Belgium. The test is applied when the application is filed. Researchers (BBIO) have no pay threshold but need a qualifying master's or doctorate (or 10 years' relevant experience) and must spend at least 80% of their working time on research.
4. Directors who founded the company or own 30% or more of its capital cannot use BBIB.
5. The tax administration must approve the employer's application.

**Exit tax on financial assets (from 1 January 2026).** When a resident who owns financial assets stops being a Belgian resident by moving their home and seat of wealth abroad, the latent gain on those assets is taxed as if they had been sold (art. 92, §2, 2° WIB 92). The "price" is the value of each asset on the day the person leaves. Gains that arose before 1 January 2026 are exempt: for assets bought before that date, the gain is measured from the value on 31 December 2025 (the "snapshot"). The rate is 10%, or the substantial-interest rate of 1.25% to 10% if the person held a substantial interest of at least 20% (art. 90, 9°, b)). The basic exemption of EUR 10,000 (or the EUR 1 million substantial-interest exemption) applies, reduced pro rata by months because the resident taxable period ends on departure (art. 129/1 WIB 92; Circular 2026/C/74, nos. 99 and 155). Each calendar month whose 15th day falls in the resident period counts as a full month. No withholding tax is due on the exit gain, so it must be reported on the resident return for the year of departure (Circular 2026/C/74, no. 120). A usufructuary who leaves does not trigger a gain for the bare owner. A person who becomes resident takes the assets at their value on the first day of residence (art. 102, §3 WIB 92), so pre-arrival gains are not taxed. Exception: a person who returns within 24 months of leaving, so that the deferred exit tax lapses, keeps the original acquisition value (Circular 2026/C/74, nos. 150 and 151).

**Company exit.** Moving a Belgian company's main establishment or seat of management abroad is treated as a liquidation (art. 210, §1, 4° WIB 92). Latent gains and untaxed reserves become taxable, and the part of the net assets treated as a distributed dividend falls under art. 208 and 209. For operations from 29 July 2025, that deemed dividend is also a taxable dividend for the shareholders, to the extent it relates to assets no longer used or kept in Belgium (art. 18, first paragraph, 2°quater WIB 92, programme law of 18 July 2025). If the company does not support it with individual forms (fiches), the separate assessment of art. 219 applies. For operations from 29 July 2025 to 31 December 2025, the administration does not require the forms and does not apply art. 219, but the dividend stays taxable for the shareholder (Circular 2026/C/70). A Belgian establishment of a foreign company that moves assets out is taxed on the gain (art. 228, §2, 3°bis). The 25% corporate rate applies (art. 215). For a move to an EU or EEA state with a recovery assistance agreement, the tax on those gains can be paid in five yearly parts (art. 413/1). See `be-corporate-tax` once merged for the computation.

## Deadlines and filing

| Event | What to do | When | Source |
|---|---|---|---|
| Arriving | Register at the commune (gemeente/commune) of residence; this puts you in the National Register | On arrival | Art. 2, §1, 1° WIB 92 (presumption) |
| Inbound regime application | Employer applies electronically, with an attestation signed by the employee | Within three months of starting work in Belgium; time limit is strict (op straffe van verval) | [Art. 32/1, §8 WIB 92](https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/d6fdb273-93c6-490d-8abe-67edd8373598) |
| Administration decision | Written decision to employer and employee | Within three months of receiving the application | Art. 32/1, §8 WIB 92 |
| Inbound regime extension (3 years) | Employer applies electronically | No later than three months after the first five-year period ends | Art. 32/1, §8 WIB 92 |
| Change of employer under the regime | New employer files a new application | Within three months of the new start | Art. 32/1, §9 WIB 92 |
| Employer reporting | Gross pay and the two kinds of cost reimbursements on the 281.10 form | With the annual tax forms | Art. 32/1, §10 WIB 92 |
| Leaving | Deregister at the commune; file the resident return for the resident part of the year and, if there is Belgian income after departure, a BNI return | In the normal filing season for the income year | Art. 227 to 248 WIB 92 |
| Non-resident return (BNI) for income 2025 | File through MyMinfin or on the paper form | Within the period printed on the form, which must be at least one month from sending the form or making the electronic return available. The date for income 2025 is under "Not yet confirmed" in Sources | [Art. 308, §1, second paragraph WIB 92](https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/182821e5-122a-4948-867e-297c16371fe1) |
| Exit tax on financial assets, move to EU/EEA or a treaty state with information exchange and recovery assistance | Automatic payment deferral. Send a yearly attestation confirming the assets were not sold or pledged | Yearly; the deferral and the tax lapse 24 months after departure if the assets are not sold in that time or the person returns within 24 months | [Art. 413/1, §6 WIB 92](https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/baa69120-644c-46a1-aaab-697645ea9501) |
| Exit tax, move elsewhere | Deferral only on request and only with adequate security. It ends if the assets are sold or pledged | Art. 413/1, §6 sets no time limit for the request | Art. 413/1, §6, third and fourth paragraphs |
| Company exit charge, EU/EEA | Choose spread payment by express request to the collector, using the official form | Within two months of the assessment notice; then a signed form each year by each due date | [Art. 413/1, §§2 and 4](https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/baa69120-644c-46a1-aaab-697645ea9501) |

**When the spread payment ends early (company).** The balance falls due at the end of the month after: a move of tax residence outside the EU/EEA, a sale or a move outside the EU/EEA of all or part of the assets, dissolution (except tax-neutral mergers and divisions), insolvency, a missed instalment, a missing yearly form, or failure to provide security when asked (art. 413/1, §3).

## Penalties and interest

- **Tax increase (art. 444 WIB 92).** Not filing, filing late, or filing an incomplete or wrong return adds 10% to 200% of the tax on the undeclared or late income, on a scale set by royal decree. No increase is charged for a first offence in good faith, and good faith is presumed for a first offence. The increase applies only if the undeclared or late income reaches EUR 2,500, and tax plus increase cannot exceed the undeclared income itself. ([Art. 444 WIB 92, income 2026](https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/5095859f-8ffb-42f9-b535-3197a7c3dbe0))
- **Inbound regime ends.** If, during the regime, the employer conditions or the pay threshold are no longer met, the regime ends (art. 32/1, §4 WIB 92). Only reimbursements within the limits of art. 32/1, §§5 and 6 are the employer's own costs; anything above them is not covered by the regime.
- **Late payment interest (art. 414 WIB 92)** runs on tax paid late, per calendar month, on the amount still due rounded down to a multiple of EUR 10. It is not charged if it is less than EUR 5 a month. The rate for calendar year 2026 is 4% (art. 2, §2/1 of the law of 5 May 1865; notice in the Belgian Official Gazette of 1 July 2025, [Numac 2025004733](https://www.ejustice.just.fgov.be/cgi/article.pl?language=nl&sum_date=2025-07-01&lg_txt=n&numac_search=2025004733)). The notice of 2 July 2026 also sets 4% for 2027.
- **Administrative fines (art. 445, §1 WIB 92).** EUR 50 to EUR 1,250 for each breach of the Code, including late or missing returns, on a scale set by royal decree. ([Art. 445 WIB 92, income 2026](https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/f9f2e45e-5e3b-4642-a5e3-31ad4ca7f25f))

## Cross-border points

**Treaty tie-breaker.** Belgium has a wide treaty network. Where a person is resident in Belgium and in another state under each state's law, the treaty's residence article decides: permanent home, then centre of vital interests, then habitual abode, then nationality, then mutual agreement. The Belgian National Register presumption does not override a treaty tie-breaker. Read the specific treaty.

**Exemption or credit.** For professional income (salary, self-employed profits) that a treaty lets the other state tax, Belgium generally exempts it with progression through the art. 155 reduction. For dividends, interest and royalties, relief depends on the treaty. Check each treaty.

**Withholding on outbound payments.** A Belgian payer withholds 30% on dividends, interest and royalties paid abroad (art. 269, §1, 1°). The rate can be reduced or removed by a tax treaty (usually through a reduced-rate claim at source or a refund) or by domestic exemptions that implement the EU Parent-Subsidiary and Interest and Royalties Directives (in the KB/WIB 92). The conditions sit with the corporate skill: see `be-corporate-tax` once merged.

**Non-residents with Belgian employment.** Belgian payroll withholding applies to pay for work done in Belgium. See `belgium-payroll`. Frontier and multi-state workers need the treaty with their residence state.

**EU social security coordination.** Social security follows Regulation (EC) 883/2004, not tax residence. A person is insured in one member state only. As a rule that is the state where they work. A worker posted to Belgium by an employer that normally operates in another member state stays in the home system if the posting is expected to last no more than 24 months and they are not replacing another posted worker (art. 12, A1 certificate). A person who normally works in two or more member states is insured in the state of residence if they do a substantial part of their work there (art. 13). The inbound tax regime does not decide social security; check the separate position of the National Social Security Office (RSZ/ONSS) on the cost allowance. Self-employed cases: see `be-social-contributions`.

## Worked examples

### Example 1: an engineer recruited abroad, starts 1 March 2026 under BBIB

Facts: a German engineer living in Munich (more than 150 km from the Belgian border) and never taxed in Belgium is hired directly by a Brussels company registered in the Crossroads Bank for Enterprises. He starts on 1 March 2026. His contract gives gross pay of EUR 90,000 a year. The employer also pays recurring posting costs (housing, home leave) of 35% of gross pay. The employer files the BBIB application within three months of 1 March 2026.

1. Days of the Belgian employment in 2026: 1 March to 31 December = 306 days out of 365.
2. Pro rata threshold for 2026: EUR 70,000 x 306 / 365 = EUR 58,684.93.
3. Gross pay paid in 2026: EUR 90,000 x 10 / 12 = EUR 75,000. This is above the pro rata threshold, so the pay test is met.
4. Tax-free recurring cost allowance: 35% x EUR 75,000 = EUR 26,250. No cap applies from 2025.
5. Taxable pay stays EUR 75,000 (plus any other benefits). The EUR 26,250 is not taxable, and moving costs plus up to EUR 1,500 of home furnishing can also be reimbursed tax-free.

```oa-check
name: BBIB arrival 1 March 2026, gross pay EUR 90,000 a year
inputs:
  annual_gross: 90000
  months_worked: 10
  days_in_belgium: 306
  days_in_year: 365
  threshold: 70000
  allowance_rate: 0.35
steps:
  - prorata_threshold: round(threshold * days_in_belgium / days_in_year, 2)
  - gross_2026: annual_gross * months_worked / 12
  - margin_over_threshold: gross_2026 - prorata_threshold
  - tax_free_allowance: gross_2026 * allowance_rate
expected:
  prorata_threshold: 58684.93
  gross_2026: 75000
  margin_over_threshold: 16315.07
  tax_free_allowance: 26250
```

He is a Belgian resident from 1 March 2026 and taxed on worldwide income from that date. His German income for January and February is not Belgian taxable. Compute the tax itself with `be-income-tax`.

### Example 2: leaving Belgium with a share portfolio, exit tax on financial assets

Facts: a Belgian resident moves her home and seat of wealth to Lisbon, Portugal, on 30 September 2026. She owns a listed share portfolio (no substantial interest) bought years ago. It was worth EUR 400,000 on 31 December 2025 and EUR 460,000 on the day she leaves. She realised no other capital gains in 2026.

1. Deemed gain: EUR 460,000 - EUR 400,000 = EUR 60,000. The gain before 2026 is exempt by the 31 December 2025 snapshot.
2. Months as a resident in 2026: January to September = 9 (15 September falls in the resident period, so September counts).
3. Basic exemption: EUR 10,000 x 9 / 12 = EUR 7,500 (art. 129/1 WIB 92; Circular 2026/C/74, no. 99).
4. Taxable gain: EUR 60,000 - EUR 7,500 = EUR 52,500.
5. Exit tax at 10%: EUR 5,250. It goes on her 2026 resident return; no withholding tax is deducted from it.
6. Portugal is an EU member state, so payment is deferred automatically (art. 413/1, §6). She must send the yearly attestation. If she does not sell or pledge the shares in the 24 months after 30 September 2026, or returns to Belgium within 24 months, the obligation lapses. If she sells some of them within the 24 months, the deferral ends for the tax on those shares.

```oa-check
name: Exit tax on financial assets, departure 30 September 2026
inputs:
  value_at_departure: 460000
  value_31_dec_2025: 400000
  full_year_exemption: 10000
  resident_months: 9
  rate: 0.10
steps:
  - deemed_gain: value_at_departure - value_31_dec_2025
  - basic_exemption: full_year_exemption * resident_months / 12
  - taxable_gain: max(deemed_gain - basic_exemption, 0)
  - exit_tax: taxable_gain * rate
expected:
  deemed_gain: 60000
  basic_exemption: 7500
  taxable_gain: 52500
  exit_tax: 5250
```

Edge cases to check: the pro rata rounds down to the lower multiple of EUR 10 where the result is not a round figure (Circular 2026/C/74, no. 100, example 5). If she had a substantial interest, the 1.25% to 10% scale and the EUR 1 million exemption, also reduced pro rata, would apply instead (no. 51).

## Ask the client first

1. Exact arrival or departure date, and the commune registration or deregistration date. Where is the family home, and where are the main assets managed?
2. For arrivals: who hires you (a Belgian entity directly, or a secondment from a foreign group company)? Gross annual pay? Where did you live, and were you taxed in Belgium, in the last 60 months? Are you a founder or 30% shareholder?
3. For departures: what financial assets do you hold (shares, funds, bonds, crypto, life insurance), and their value on 31 December 2025? Any substantial interest in a company? Which country are you moving to?
4. For non-residents: what Belgian income do you have (pay for days worked in Belgium, director's fees, rent, a Belgian establishment)? What is your worldwide professional income, for the 75% test?
5. For companies: is the seat or main establishment moving abroad, or are assets moving out of a Belgian establishment? To which state?
6. Which social security system covers you now, and do you have an A1 certificate?

## Sources

All read on 2026-10-22.

- FPS Finance, Circular 2026/C/51 on the changes to the special tax regimes for inbound taxpayers and inbound researchers (1 April 2026), with the consolidated text of art. 32/1 and 32/2 WIB 92 and art. 17 of the law of 18 December 2025: https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/d6fdb273-93c6-490d-8abe-67edd8373598
- FPS Finance, special tax regime for inbound taxpayers and researchers (application forms page): https://finance.belgium.be/en/node/14643
- Fisconetplus, art. 2 WIB 92 (income 2026), residence of individuals and companies: https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/2bfeec21-7e5f-4828-a283-cb99c56d41a1
- Fisconetplus, art. 130 WIB 92 (income 2026), indexed tax scale: https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/796a4fc5-340e-4c89-a72a-88caa804ca96
- Fisconetplus, art. 131 WIB 92 (income 2026), tax-free amount, read 2026-10-23: https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/f3c5d665-cac4-4cbd-b714-bd287f791751
- Fisconetplus, art. 243 WIB 92 (income 2026): https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/629ac5c1-967e-40e9-8511-7ad5b1cbfe40
- Fisconetplus, art. 243/1 WIB 92 (income 2026), the 75% rule: https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/a32b08a8-163e-4d48-b76f-fc6b40a89daf
- Fisconetplus, art. 244bis WIB 92 (income 2026), changed by the law of 15 July 2026: https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/36447522-376d-4cb1-b5bf-8243bc16ae93
- Fisconetplus, art. 245 WIB 92 (income 2026), additional centimes: https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/182fc9a7-f7c6-46ef-8da9-239fd2378423
- Fisconetplus, art. 80 KB/WIB 92 (income 2026), 7 additional centimes: https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/ff25ff26-ce91-4678-bdb5-5a1dee98e899
- FPS Finance, Circular 2026/C/74 on the tax on capital gains on financial assets (22 July 2026), including the exit tax: https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/7f6b62c6-1baa-487a-8f59-c883dd5485c4
- Fisconetplus, art. 413/1 WIB 92 (income 2026), spread payment and exit tax deferral: https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/baa69120-644c-46a1-aaab-697645ea9501
- Fisconetplus, art. 210 WIB 92 (income 2026), seat transfer treated as liquidation: https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/a3d38979-9797-4133-b830-bf716b9625de
- Fisconetplus, art. 215 WIB 92 (income 2026), corporate tax rate: https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/3fd24be9-c978-47d0-ad39-5157070d42b1
- Fisconetplus, art. 269 WIB 92 (income 2026), withholding tax rates: https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/c9acc360-8503-4b60-b2c4-9880403d1cac
- Fisconetplus, art. 444 WIB 92 (income 2026), tax increases: https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/5095859f-8ffb-42f9-b535-3197a7c3dbe0
- Fisconetplus, art. 445 WIB 92 (income 2026), administrative fines: https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/f9f2e45e-5e3b-4642-a5e3-31ad4ca7f25f
- Fisconetplus, art. 308 WIB 92 (income 2026), return filing periods: https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/182821e5-122a-4948-867e-297c16371fe1
- Fisconetplus, law of 5 May 1865 on interest-bearing loans, art. 2, §2/1, with the yearly rates (4% for 2026 and 2027): https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/da7e0caf-3428-43aa-ab80-30410a15beca
- Belgian Official Gazette, notice of 1 July 2025 setting the 2026 rate at 4% (Numac 2025004733): https://www.ejustice.just.fgov.be/cgi/article.pl?language=nl&sum_date=2025-07-01&lg_txt=n&numac_search=2025004733
- FPS Finance, Circular 2026/C/70 on the separate assessment for the exit tax dividend of art. 18, first paragraph, 2°quater WIB 92 (30 June 2026): https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/09089595-7dba-4d67-9ea6-2a65554e5efc
- FPS Finance, Circular 2026/C/94 on withholding tax on capital gains on financial assets (20 October 2026): https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/a64fb047-7cc0-4c60-81ca-35a4ab745e55
- Regulation (EC) No 883/2004, consolidated text, art. 12 and 13: https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:02004R0883-20190731
- Justel, list of 2025 and 2026 laws amending the WIB 92: https://www.ejustice.just.fgov.be/cgi_loi/change_lg.pl?language=nl&la=N&cn=1992041032&table_name=wet

Not yet confirmed: the filing date printed on the 2026 non-resident return for income 2025 (art. 308 WIB 92 leaves the date to the form; FPS Finance pages at fin.belgium.be were behind a human-verification check and could not be read, and the form model in the royal decree of 22 June 2026 does not print it; secondary references give 20 November 2026); the conditions of the domestic withholding exemptions for EU parent companies and associated companies (KB/WIB 92); whether municipal surcharges apply to the exit tax in the year of departure; the RSZ/ONSS treatment of the 35% inbound cost allowance.

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
