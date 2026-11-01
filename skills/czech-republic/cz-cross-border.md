---
name: cz-cross-border
description: "Hub skill for crossing the Czech border in tax year 2026. Covers tax residence for individuals (domicile or 183 days in the calendar year, Income Tax Act section 2) and companies (seat or place of management, section 17); arriving (no special inbound regime); leaving (no exit tax for individuals; corporate exit tax under section 23g, payable over up to 5 years inside the EU and EEA); non-residents taxed on Czech-source income (section 22); 15% withholding on dividends, interest, royalties and service fees, 35% to non-cooperative states (section 36); the 10% and 1% tax security (section 38e); treaty relief (section 38f). Tax year is the calendar year. Trigger on: moving to the Czech Republic, leaving Czechia, non-resident, expat, exit tax, digital nomad, srážková daň, zajištění daně. Out of scope: self-employed income tax (cz-income-tax), corporate tax (cz-corporate-income-tax), social and health insurance (cz-social-health), VAT (cz-vat-return)."
version: 0.2
jurisdiction: CZ
tax_year: 2026
last_updated: 2026-11-01
authored_by: Michael Cutajar and the OpenAccountants team
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
category: cross-border
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Czech Republic: cross-border tax for people and companies (2026) v0.1

> **Source-cited draft.** No accountant has reviewed this skill yet. Every figure below comes from the Income Tax Act and the Tax Code as published on zakonyprolidi.cz (versions in force for 2026), financnisprava.gov.cz, cssz.gov.cz and cnb.cz, read on 22 October 2026. It prepares working papers; it is not authority to file or pay.

This is the hub for the Czech cross-border (XB) domain. It summarises and links rather than repeating other skills:

- Self-employed income tax, expense lump sums and credits: [cz-income-tax](cz-income-tax.md).
- Corporate income tax: [cz-corporate-income-tax](cz-corporate-income-tax.md).
- Social and health insurance for the self-employed: [cz-social-health](cz-social-health.md).
- VAT: [cz-vat-return](cz-vat-return.md). Overview: [cz-tax-overview](cz-tax-overview.md). Entity choice: [cz-company-formation](cz-company-formation.md).

The law is Act No. 586/1992 Coll. on Income Taxes (zákon o daních z příjmů, "ITA") and Act No. 280/2009 Coll., the Tax Code (daňový řád). Tax year: the calendar year (ITA § 16b for individuals). Currency: Czech koruna (CZK).

## Who this applies to

**Individuals.** A person is a Czech tax resident if they have a domicile (bydliště) in the Czech Republic or habitually stay there (ITA § 2(2)).

- **Domicile** means a place where the person has a permanent home in circumstances showing they intend to stay there permanently (ITA § 2(4)).
- **Habitual stay** means being in the Czech Republic for at least 183 days in the calendar year, in one block or several. Every started day counts (ITA § 2(4)).
- A person who stays only to study or for medical treatment is a non-resident even past 183 days (ITA § 2(3)).
- A treaty can make someone a non-resident (ITA § 2(3)). Financial Administration guidance says that where a double tax treaty is in force, residence is decided under the treaty article ([Finanční správa, general information](https://financnisprava.gov.cz/cs/dane/dane/dan-z-prijmu/fyzicke-osoby/obecne-informace)).

A resident is taxed on worldwide income. A non-resident is taxed only on Czech-source income listed in ITA § 22 (ITA § 2(2) and (3)).

**Part year.** The ITA has no split-year rule. The tests apply to the calendar year: a person who arrives in March and sets up a permanent home is resident for 2026 under domestic law. Where the other country also treats them as resident for the months before arrival, the treaty tie-breaker decides who taxes which income.

**Companies.** A body is Czech resident if its seat or its place of management (the address from which it is managed) is in the Czech Republic. A resident is taxed on worldwide income; a non-resident only on Czech-source income (ITA § 17(3) and (4)).

**Permanent establishment.** A non-resident has a Czech permanent establishment through a fixed place such as a workshop, office or site. A building site, an assembly project, or services and professional activity in Czechia become a permanent establishment if they last more than 6 months in any 12 consecutive months. A dependent agent who habitually concludes binding contracts also creates one (ITA § 22(2)).

## Rates, bands and thresholds

| Item | 2026 figure | Source |
|---|---|---|
| Individual income tax, base up to 36 times the average wage | 15% | [ITA § 16(1)](https://www.zakonyprolidi.cz/cs/1992-586) |
| Individual income tax, base above 36 times the average wage | 23% | ITA § 16(1) |
| Average wage for 2026 (tax purposes use the social insurance figure, ITA § 21g(2)) | CZK 48,967 (general assessment base 2024 of CZK 46,278 × coefficient 1.0581, rounded up) | [Act 589/1992 § 23b(4)](https://www.zakonyprolidi.cz/cs/1992-589); [Government Regulation 365/2025 § 1](https://www.zakonyprolidi.cz/cs/2025-365) |
| 23% threshold for 2026 | CZK 1,762,812 (36 × 48,967) | computed from the two rows above |
| Basic taxpayer credit (sleva na poplatníka), residents and non-residents | CZK 30,840 a year | ITA § 35ba(1)(a) and (2); [Finanční správa](https://financnisprava.gov.cz/cs/dane/dane/dan-z-prijmu/fyzicke-osoby/obecne-informace) |
| Spouse credit, disability credits, ZTP/P credit and child benefit for a non-resident | Only if resident in the EU or EEA and at least 90% of world income is Czech-source | ITA § 35ba(2) (credits), § 35c(5) (child benefit); Finanční správa |
| Special inbound regime for new arrivals | None in the ITA; arrivals are taxed under the normal rules | ITA (no such provision) |
| Exit tax, individuals | None | ITA § 23g applies to corporate taxpayers only |
| Corporate income tax rate (also applies to the corporate exit charge) | 21% | [ITA § 21(1)](https://www.zakonyprolidi.cz/cs/1992-586) |
| Withholding tax on dividends and other profit shares paid to a non-resident | 15% | ITA § 36(1)(b) and (2) |
| Withholding tax on interest paid to a non-resident | 15% | ITA § 36(1)(b) |
| Withholding tax on royalties, services in Czechia, independent professional and artists' fees, board fees paid to a company | 15% | ITA § 36(1)(a)(1), with § 22(1)(c), (f) and (g)(1), (2), (6) |
| Board fees paid to a non-resident individual | Not under § 36: taxed as employment income through payroll; a return is required if they exceed 36 times the average wage | ITA § 22(1)(g)(15), § 38g(6) |
| Withholding on the above to a resident of a state outside the EU and EEA with no tax treaty and no tax information exchange agreement in force | 35% | ITA § 36(1)(c) |
| Withholding on finance lease payments | 5% | ITA § 36(1)(d) |
| Tax security (zajištění daně) on other Czech-source income of non-EU and non-EEA residents | 10% of the payment | ITA § 38e(1)(c) and (2)(c) |
| Tax security on bond redemptions, sales of investment instruments and payments on assigned receivables | 1% | ITA § 38e(1)(a), (b) and (2)(a), (b) |
| Rental expense lump sum (individuals) | 30% of rent, at most CZK 600,000 | ITA § 9(4) |
| Late payment interest (úrok z prodlení) | CNB repo rate on the first day of the half-year plus 8 points: 11.50% for 1 January to 30 June 2026 (repo 3.50%), 11.75% for 1 July to 31 December 2026 (repo 3.75% from 19 June 2026) | [Tax Code § 252(4) and § 251a(5)](https://www.zakonyprolidi.cz/cs/2009-280); [Government Regulation 351/2013 § 2](https://www.zakonyprolidi.cz/cs/2013-351); [CNB repo history](https://www.cnb.cz/cs/faq/vyvoj_repo_historie.txt) |

The tax is computed on the base after deductions, rounded down to whole hundreds of CZK, as the sum of each slice times its rate (ITA § 16(2)).

## The taxable base

**Residents: worldwide income.** There is no remittance basis. Foreign income goes into the return and double taxation is then relieved under ITA § 38f (see Cross-border points).

**Non-residents: Czech-source income only** (ITA § 22(1)). The main items:

- income through a Czech permanent establishment;
- employment income for work done in the Czech Republic;
- fees for services, consulting, management and agency work provided in Czechia, and independent professional income from work done there;
- sale of Czech real estate and rent from Czech real estate;
- when paid by a Czech resident or a Czech permanent establishment: royalties, dividends, interest, board fees, and certain other items;
- sale of shares in a company with its seat in the Czech Republic.

How the tax is collected depends on the income:

- **Final withholding at 15% or 35%** applies to the § 36 items (dividends, interest, royalties, service fees, board fees paid to a company). The base is the gross payment with no deductions (ITA § 36(3)). The withholding is final unless the rules below allow a return.
- **Return with a tax security.** Other Czech-source income of a non-resident from outside the EU and EEA (for example rent from a business tenant, or the sale of a share in a Czech s.r.o.) is taxed on a return at normal rates. The payer withholds a 10% security (1% for bonds, investment instruments and assigned receivables) as an advance (ITA § 38e). There is no security on retail sales or on rent paid by individuals for a home to live in (ITA § 38e(4)).
- **Employment income** is taxed through payroll advances like a resident's.
- **EU and EEA residents** can include most withheld-income items (not dividends) in a Czech return; the withholding is then credited and any excess refunded (ITA § 36(7)).

**Arriving.** There is no expat or impatriate regime. Someone who becomes resident is taxed on worldwide income at 15% and 23% from the start of residence, with the same credits as any resident. Social and health insurance follow the EU rules (see Cross-border points) and [cz-social-health](cz-social-health.md).

**Leaving: individuals.** No exit charge applies to individuals. After they become non-resident, only Czech-source income stays taxable here: Czech rent, sale of Czech property, and sale of shares in a Czech company (ITA § 22(1)(d), (e), (h)).

**Leaving: companies (exit tax).** Moving an asset abroad without a change of owner is treated as a sale to itself at arm's length price. The gain is added to the corporate tax base (ITA § 23g(1)). This covers three cases (ITA § 23g(2)):

- a Czech resident company moves the asset to its foreign permanent establishment, where the treaty uses exemption;
- a non-resident moves an asset from its Czech permanent establishment abroad, so Czechia loses the right to tax a later sale;
- a company moves its tax residence abroad, with the same result.

Temporary transfers for securities financing, collateral or capital requirements are excluded if the assets are expected back within 12 months (ITA § 23g(3)). An asset arriving from another EU state that taxed the exit is valued at arm's length price on arrival (ITA § 23g(5)).

## Deadlines and filing

- **Individual return.** It is due within 3 months after the end of the year (Tax Code § 136(1)). This becomes 4 months if filed electronically after the 3-month date, and 6 months if filed by a tax adviser or advocate or where an audit is compulsory (§ 136(2)). For the 2025 return the dates were 1 April 2026, 4 May 2026 (electronic) and 1 July 2026. Tax is due on the last day for filing ([Finanční správa](https://financnisprava.gov.cz/cs/dane/dane/dan-z-prijmu/fyzicke-osoby/obecne-informace)).
- **Who must file.** Anyone whose taxable income was more than CZK 50,000, ignoring exempt income and income taxed by final withholding (ITA § 38g(1)). Employees with one employer, a signed tax declaration and no more than CZK 20,000 of other income need not file (§ 38g(2)). A **non-resident must file** to claim the spouse credit, disability credits, child benefit or deductions (§ 38g(2)). A non-resident whose board fees under § 22(1)(g)(15) exceed 36 times the average wage must file (§ 38g(6)).
- **Corporate return.** The same Tax Code § 136 periods apply. A company that moves assets or residence abroad and owes exit tax can ask for the tax on the exit gain to be paid in instalments over **up to 5 years from the due date**, where the assets go to another EU state or an EEA state with a recovery assistance agreement. The tax office may ask for security. Permission lapses if the asset is sold or moved again outside those states (ITA § 38zg).
- **Withholding tax** must be paid to the payer's tax office by the end of the month after the month of withholding (ITA § 38d(3)). For dividends, it is withheld on payment and no later than the end of the third month after the month in which the accounts were approved and the profit distribution decided (§ 38d(2)).
- **Tax security** is paid to the payer's tax office by the end of the month after the month the duty arose, with a report on the security withheld (ITA § 38e(6)). The security is credited on the non-resident's return. If the non-resident does not file, the tax office may treat the security as the final tax (§ 38e(7)). The tax office can reduce or waive the security on request (§ 38e(8)).

## Penalties and interest

- **Late return (pokuta za opožděné tvrzení daně).** If the return is more than 5 working days late, the penalty is 0.05% of the tax for each further day, capped at 5% of the tax (Tax Code § 250(1)(a)). The rate is 0.01% a day, capped at 5%, on a tax loss (§ 250(1)(c)). Other rules:
  - A penalty under CZK 1,000 is not charged (§ 250(3)).
  - If the return is never filed, the penalty is the full cap and at least CZK 500 (§ 250(4)).
  - The maximum is CZK 300,000 (§ 250(5)).
  - The penalty is halved if the return is filed within 30 days of the deadline and there was no other late filing that year (§ 250(7)).
- **Withholding agents** pay 0.05% a day, capped at 0.5% of the tax, for late reports or statements (§ 250(2)).
- **Penalty on additional tax assessed by the tax office (penále).** 20% of the extra tax, or 1% of a reduced loss (§ 251(1)). It does not arise on tax disclosed in a voluntary supplementary return (§ 251(4)).
- **Late payment interest (úrok z prodlení).** It runs from the fourth day after the due date until payment (§ 252(2)). The rate is the CNB repo rate on the first day of the half-year plus 8 points (§ 252(4); Government Regulation 351/2013 § 2). For 2026 that is 11.50% a year for January to June and 11.75% for July to December. Interest of CZK 1,000 or less per tax and period is not charged (§ 251a(2)). A withholding agent or payer that fails to withhold the tax security is assessed the amount directly (ITA § 38e(9)).

## Cross-border points

- **Treaty tie-breaker.** Where both states treat a person as resident, the treaty decides. Treaties based on the OECD model use, in order, permanent home, centre of vital interests, habitual abode and nationality. Czech law then follows: a person the treaty makes resident elsewhere is a Czech non-resident (ITA § 2(3)). The same applies to companies (§ 17(4)).
- **Relief for residents.** The method in the treaty applies (ITA § 38f(1)). Under simple credit, foreign tax is credited up to the Czech tax on that income, worked out country by country (§ 38f(2) and (8)). Under exemption with progression, the foreign income is removed but the rate is set on the total (§ 38f(7)). Employment income taxed in a treaty state, paid by an employer resident there or charged to a permanent establishment there, is exempt in Czechia, with progression; the taxpayer may instead use the treaty method if that is better (§ 38f(4)). Foreign tax is proved by a certificate from the foreign tax office (§ 38f(5)).
- **Outbound dividends, interest and royalties within the EU.** Several payments are exempt from Czech withholding if the conditions in ITA § 19 are met, including the 12-month holding test and beneficial ownership:
  - dividends to a parent company in another EU state holding at least 10% for 12 months (§ 19(1)(ze) and (3));
  - interest and royalties to an associated company in another EU state (§ 19(1)(zj), (zk)).
  Otherwise the treaty rate caps the 15%. Read the conditions in § 19 and the treaty before applying a lower rate.
- **Controlled foreign companies.** Low-taxed passive income of a controlled foreign company is taxed in the hands of the Czech parent (ITA § 38fa). The corporate detail is in [cz-corporate-income-tax](cz-corporate-income-tax.md).
- **EU social security.** Inside the EU, EEA and Switzerland, Regulation (EC) 883/2004 means only one country's social security law applies. Normally that is the country where the work is done. A worker or self-employed person posted temporarily to another state stays in the sending state's system for a posting expected to last no more than 24 months, proved by an A1 certificate (Art. 12). A longer stay needs an Article 16 agreement requested in advance ([ČSSZ, posted workers](https://www.cssz.gov.cz/vyslani-pracovnici)). Czech contributions for the self-employed are in [cz-social-health](cz-social-health.md).

## Worked examples

### Example 1: an engineer moves to Prague on 1 March 2026

He moves from Spain, rents a flat in Prague on a 3-year lease and works for a Czech employer from 1 March. Gross salary is CZK 180,000 a month, so CZK 1,800,000 for March to December. He has no other income in 2026 and no Czech deductions.

1. Residence: he has a permanent home in Czechia and will be there more than 183 days in 2026, so he is resident under ITA § 2. Spain may also treat him as resident for January and February; the Spain treaty tie-breaker splits the year. Here we assume his only income is the Czech salary.
2. Base: CZK 1,800,000, already a whole hundred.
3. Tax at 15% on the first CZK 1,762,812: CZK 264,421.80.
4. Tax at 23% on the excess of CZK 37,188: CZK 8,553.24.
5. Tax before credits: CZK 272,975.04. Less the basic credit of CZK 30,840 (a full year's credit; only credits b to e are pro-rated by month): CZK 242,135.04 before final rounding. His employer's monthly advances are credited against this.

There is no special regime for new arrivals, so nothing reduces the base.

```oa-check
name: Arrival 1 March 2026, Czech salary CZK 1,800,000 (2026 bands)
inputs:
  base: 1800000
  threshold: 1762812
  credit: 30840
steps:
  - tax_15: min(base, threshold) * 0.15
  - tax_23: max(base - threshold, 0) * 0.23
  - tax_before_credit: tax_15 + tax_23
  - tax_after_credit: tax_before_credit - credit
expected:
  tax_15: 264421.80
  tax_23: 8553.24
  tax_before_credit: 272975.04
  tax_after_credit: 242135.04
```

### Example 2: a UK resident lets a Prague office to a Czech company

She lives in London, is not Czech resident, and owns a small office in Prague. She lets it to a Czech s.r.o. for CZK 40,000 a month: CZK 480,000 for 2026. The United Kingdom is outside the EU and EEA.

1. Rent from Czech real estate is Czech-source income (ITA § 22(1)(e)). It is taxed on a return, not by final withholding (§ 9(3)).
2. The tenant is a company, not an individual renting a home, so it must withhold a 10% tax security from each payment: CZK 48,000 for the year (§ 38e(1)(c)). It pays this to its tax office by the end of the following month.
3. She claims the 30% lump-sum expenses: CZK 144,000, which is under the CZK 600,000 cap (§ 9(4)). Base: CZK 336,000.
4. Tax at 15%: CZK 50,400. She is a non-resident, but she may still claim the basic credit of CZK 30,840 (§ 35ba(2) restricts only credits b to e). Tax: CZK 19,560.
5. The security of CZK 48,000 is credited, giving an overpayment of CZK 28,440. She must file by the § 136 deadline to get it back. If she does not file, the tax office may treat the CZK 48,000 as her final tax (§ 38e(7)).
6. Under the UK treaty, rent from immovable property may be taxed where the property is. She claims credit for the Czech tax in the UK.

```oa-check
name: Non-resident rent CZK 480,000 with 10% tax security (2026)
inputs:
  rent: 480000
  credit: 30840
steps:
  - security: rent * 0.10
  - lump_sum: min(rent * 0.30, 600000)
  - base: rent - lump_sum
  - tax: base * 0.15 - credit
  - refund: security - tax
expected:
  security: 48000
  lump_sum: 144000
  base: 336000
  tax: 19560
  refund: 28440
```

## Ask the client first

1. The exact arrival or departure date, whether a home is kept in Czechia, and the days spent there in the calendar year.
2. Which other country treats the person as resident, and which treaty applies.
3. For a non-resident: what Czech income they have (work days in Czechia, Czech property, Czech company shares, fees from Czech payers), and their country of residence (EU or EEA or not, treaty or not). This sets the withholding rate, the tax security and which credits are available.
4. For a non-resident in the EU or EEA: what share of world income is Czech-source. At 90% or more, the extra credits are available.
5. For a company: where the seat is and where the business is actually managed from, whether assets or residence are moving abroad, and to which country.
6. For payments abroad: who the recipient is, where they are resident, whether they are the beneficial owner, and the holding percentage and period for dividends, interest and royalties.

## Sources

| Source | URL | Read on |
|---|---|---|
| Act No. 586/1992 Coll., Income Taxes Act, version in force 1 August to 31 December 2026: §§ 2, 9, 16, 16b, 17, 19, 21, 21g, 22, 23g, 35ba, 35c, 36, 38d, 38e, 38f, 38fa, 38g, 38zg | https://www.zakonyprolidi.cz/cs/1992-586 | 2026-10-22 |
| Act No. 280/2009 Coll., Tax Code, version in force from 1 January 2026: §§ 136, 137, 250, 251, 251a, 252, 253 | https://www.zakonyprolidi.cz/cs/2009-280 | 2026-10-22 |
| Act No. 589/1992 Coll., social security premiums, § 23b(4) (average wage) | https://www.zakonyprolidi.cz/cs/1992-589 | 2026-10-22 |
| Government Regulation No. 365/2025 Coll., § 1 (general assessment base 2024 and coefficient) | https://www.zakonyprolidi.cz/cs/2025-365 | 2026-10-22 |
| Government Regulation No. 351/2013 Coll., § 2 (late payment interest: repo plus 8 points) | https://www.zakonyprolidi.cz/cs/2013-351 | 2026-10-22 |
| Finanční správa, Fyzické osoby: obecné informace (residence, filing dates, credits for non-residents) | https://financnisprava.gov.cz/cs/dane/dane/dan-z-prijmu/fyzicke-osoby/obecne-informace | 2026-10-22 |
| Czech National Bank, two-week repo rate history | https://www.cnb.cz/cs/faq/vyvoj_repo_historie.txt | 2026-10-22 |
| ČSSZ, Vyslaní pracovníci (posting, A1, Regulation 883/2004) | https://www.cssz.gov.cz/vyslani-pracovnici | 2026-10-22 |

Not yet confirmed: the exact filing dates for the 2026 return (in 2027), which the Financial Administration had not published on the page read; registration duties for an arriving self-employed person or a foreign company (Tax Code § 125 and following, not read); the rounding of the final tax to whole koruna (Tax Code § 146, not read); the 25% ownership threshold and other conditions for the EU interest and royalty exemption in ITA § 19 (only summarised here); individual treaty rates and relief methods.

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
