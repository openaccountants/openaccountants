---
name: ee-tax-overview
description: "A one-page map of the Estonian tax system for tax year 2026, from the Income Tax Act, Social Tax Act, Value-Added Tax Act, Taxation Act and Commercial Code as consolidated on Riigi Teataja, and Estonian Tax and Customs Board (EMTA) pages. Covers the tax year, the authority, who is resident, the flat 22% income tax (the planned 24% rise and the security tax were both cancelled before 2026), the EUR 8,400 basic exemption, the distributed-profit company tax at 22/78, social tax 33%, unemployment premiums, the II pillar, VAT at 24%, 13% and 9% with the EUR 40,000 registration threshold, and the main filing deadlines. Use for 'how does tax work in Estonia', 'Estonia tax overview', 'Estonian tax rates 2026'. It points to the pack's domain skills for the detail: estonia-income-tax, ee-corporate-income-tax, estonia-vat-return, estonia-social-contributions, estonia-payroll, ee-transfer-pricing, ee-cross-border, ee-company-formation, estonia-tax-optimization."
jurisdiction: EE
category: international
tax_year: 2026
last_updated: 2026-10-30
version: 0.2
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Estonia Tax Overview

## Estonia Tax Overview v0.2

This is a map, not a computation skill. Each line gives the 2026 headline figure and its source, and names the skill in this pack that carries the full rules. Where a domain skill and this overview ever differ, the domain skill wins.

## The Estonian tax system at a glance

Estonia's tax system is run by the Estonian Tax and Customs Board (Maksu- ja Tolliamet, EMTA). Returns are filed in the e-MTA portal. The best-known feature is the company tax: a resident company pays no income tax on profit it keeps, and pays only when it distributes profit or makes payments treated as distributions.

- **Tax year.** The calendar year, 1 January to 31 December. The annual return covers the calendar-year taxable period and is due by 30 April of the following year _(Income Tax Act (tulumaksuseadus, TuMS) § 44(1))_.
- **Currency.** Euro (EUR). All amounts in the tax acts are in euros _(TuMS § 23(1))_.
- **Tax authority.** Estonian Tax and Customs Board (Maksu- ja Tolliamet, EMTA) _(Taxation Act (maksukorralduse seadus, MKS); [emta.ee](https://www.emta.ee/en))_.
- **Who is resident (individuals).** A person whose home (elukoht) is in Estonia, or who stays in Estonia at least 183 days in 12 consecutive calendar months. Residence starts from the day of arrival _(TuMS § 6(1))_.
- **Who is resident (companies).** A legal person founded under Estonian law, and an SE or SCE registered in Estonia _(TuMS § 6(2))_.
- **Residence basis of taxation.** A resident individual pays income tax on all income, from Estonia and abroad _(TuMS § 6(1))_. Anyone not resident under § 6(1) or (2) is a non-resident _(TuMS § 6(3))_ and is taxed in Estonia only on the Estonian-source income the Act lists. Detail: `ee-cross-border`.
- **Personal income tax rate.** Flat 22% _(TuMS § 4(1))_. The rise to 24% that had been enacted for 2026 was cancelled before it took effect; the rate stays 22% for individuals and companies _(Ministry of Finance, 2026 law changes)_. Detail: `estonia-income-tax`.
- **Basic exemption (maksuvaba tulu).** EUR 8,400 a year (EUR 700 a month), the same for everyone whatever their income. The income taper that applied up to 2025 is gone. From the year a person reaches pensionable age: EUR 9,312 a year (EUR 776 a month) _(TuMS § 23(1), § 23^5(1), § 42(1); EMTA tax rates page)_.
- **Security tax (julgeolekumaks).** Does not apply in 2026. Parliament changed the plan in June 2025 so that from 2026 neither company profit nor personal income is taxed under it _(Ministry of Finance, 18.06.2025)_. Detail: `ee-corporate-income-tax`.
- **Company income tax.** 0% on retained profit. When profit is distributed (dividends, other profit distributions) or treated as distributed (fringe benefits, gifts and donations, entertainment costs, non-business expenses, transfer pricing adjustments), the company pays 22% of the gross amount. In practice that is 22/78 of the net payment, because the taxable amount is divided by 0.78 before the 22% is applied _(TuMS § 4(1), § 4(1^1), § 50(1))_. The reduced 14/86 rate on regular dividends was abolished from 1 January 2025 _(TuMS § 4(4) repealed; EMTA tax rates page)_. Banks pay an 18% advance tax on quarterly profit _(TuMS § 4(5))_. Detail: `ee-corporate-income-tax`.
- **Dividends in the hands of an individual.** A dividend from an Estonian company is not part of the individual's taxable income; the company has already paid the tax _(TuMS § 12(2))_. Exception: 7% is withheld when a company passes on to an individual an exempt dividend whose underlying profit was taxed at the old 14/86 rate _(TuMS § 61(68))_.
- **Participation exemption.** A resident company does not pay tax again on a dividend it passes on, if it received that dividend from a company in which it held at least 10% of the shares or votes when the dividend was received, and the other conditions of § 50(1^1) are met _(TuMS § 50(1^1))_. Detail: `ee-corporate-income-tax`.
- **Social tax (sotsiaalmaks).** 33%, paid by the employer on wages and board fees. It is charged on the pay for the month, but not on less than the monthly minimum base, which in 2026 is EUR 886, so the minimum social tax is EUR 292.38 a month _(Social Tax Act (sotsiaalmaksuseadus, SMS) § 7(1), § 2(2); EMTA tax rates page; Ministry of Finance, 2026 law changes)_. Detail: `estonia-social-contributions`.
- **Unemployment insurance premiums.** 1.6% withheld from the employee, 0.8% paid by the employer _(EMTA tax rates page)_. Detail: `estonia-payroll`.
- **Funded pension (II pillar).** 2% of the member's pay, or 4% or 6% if the member chooses; a chosen rate holds for at least a calendar year _(Funded Pensions Act (kogumispensionide seadus, KoPS) § 9(1) and (2))_. Detail: `estonia-social-contributions`.
- **Minimum wage.** EUR 886 a month to 31 March 2026; EUR 946 a month (EUR 5.67 an hour) from 1 April 2026 _(EMTA tax rates page)_.
- **Self-employed (FIE).** Taxed each year on business income: 22% income tax on the annual return, and social tax of 33% on business income after allowed deductions, with an annual minimum of 12 × EUR 886 × 33% = EUR 3,508.56 and a maximum of EUR 36,867.60 in 2026 _(SMS § 2(5), § 7(1); EMTA, social tax of self-employed persons)_. Detail: `estonia-income-tax`, `estonia-social-contributions`.
- **Entrepreneur account (ettevõtluskonto).** An individual can take payments for services and goods into a special bank account. The bank holds back 20% of every receipt (22%, 24% or 26% if the person is in the II pillar at 2%, 4% or 6%), with no expenses and no return to file. The 20% splits 22/55 income tax and 33/55 social tax. Above EUR 40,000 of receipts in a calendar year the person must register as an FIE or a company and for VAT. EMTA says only LHV Pank offers the account _(Simplified Business Income Taxation Act (ettevõtlustulu lihtsustatud maksustamise seadus) § 4, § 8(2); EMTA, entrepreneur account)_. Detail: `estonia-income-tax`.
- **VAT (käibemaks).** Standard rate 24% from 1 July 2025; it was 22% in the text in force from 1 January to 30 June 2025. Reduced rates: 13% on accommodation (with or without breakfast) and 9% on books, educational literature, listed medicines and medical devices, and press publications. 0% on exports and intra-Community supplies of goods _(Value-Added Tax Act (käibemaksuseadus, KMS) § 15(1), (1^1), (2), (3), and § 15(1) of the text in force 01.01.2025 to 30.06.2025; EMTA tax rates page)_. Detail: `estonia-vat-return`.
- **VAT registration threshold.** EUR 40,000 of taxable supplies with place of supply in Estonia from the start of the calendar year. The duty to register arises on the day that amount is passed _(KMS § 19(1))_.
- **VAT return (KMD) deadline.** Monthly. The return and its annex are due by the 20th day of the month after the period _(KMS § 27(1))_.
- **Annual individual income tax return.** By 30 April of the year after the tax year. EMTA pre-fills the return for residents. Any extra tax is due, and refunds are paid, by 1 October of that year _(TuMS § 44(1), § 44(1^1), § 46(3), § 46(6))_. An FIE must file even when no tax is due _(TuMS § 44(6^1))_.
- **Monthly employer and company return (TSD) deadline.** By the 10th day of the month after the month. The income tax on distributions, fringe benefits and other company tax objects is due by the same day _(TuMS § 54(1), (2), (4))_. Banks file the quarterly advance-tax return by the 10th day of the third month of each quarter _(TuMS § 54(2^1))_.
- **Annual report (financial statements).** The management board of an OÜ (private limited company) or an AS (public limited company) files the approved annual report with the commercial register within six months of the end of the financial year, so by 30 June for a calendar-year company _(Commercial Code (äriseadustik, ÄS) § 179(4) for an OÜ, § 334(2) for an AS)_. Detail: `ee-company-formation`.
- **Late payment interest.** 0.06% a day on tax paid late _(MKS § 117(1))_.
- **Transfer pricing.** Where a related-party price differs from market value, the difference is taxed as if distributed _(TuMS § 50(4))_. Detail: `ee-transfer-pricing`.

## Which skill to use

| Question | Skill |
|---|---|
| A resident individual's return, form A, an FIE's form E, the entrepreneur account | `estonia-income-tax` |
| Tax on dividends, deemed distributions, fringe benefits, the participation exemption | `ee-corporate-income-tax` |
| The monthly KMD return, rates, registration | `estonia-vat-return` |
| Social tax, unemployment premiums, II pillar, FIE social tax | `estonia-social-contributions` |
| Gross to net, withholding, the TSD for employees and board members | `estonia-payroll` |
| Related-party prices and documentation | `ee-transfer-pricing` |
| Residence, non-residents, withholding on payments abroad, treaties, exit tax | `ee-cross-border` |
| OÜ, FIE or entrepreneur account: which to choose | `ee-company-formation` |
| Lawful ways to lower the tax bill | `estonia-tax-optimization` |

## Sources

| Source | URL | Read on |
|---|---|---|
| Tulumaksuseadus (Income Tax Act), consolidated text in force 01.10.2026 to 31.12.2026, §§ 4, 6, 12, 23, 23^5, 42, 44, 46, 50, 54, 61 | https://www.riigiteataja.ee/et/akt/109072026066 | 2026-10-30 |
| Sotsiaalmaksuseadus (Social Tax Act), consolidated text in force from 26.10.2026, §§ 2, 7 | https://www.riigiteataja.ee/et/akt/116102026014 | 2026-10-30 |
| Käibemaksuseadus (Value-Added Tax Act), consolidated text in force from 01.10.2026, §§ 15, 19, 27 | https://www.riigiteataja.ee/et/akt/130062026129 | 2026-10-30 |
| Käibemaksuseadus, consolidated text in force 01.01.2025 to 30.06.2025, § 15(1) | https://www.riigiteataja.ee/et/akt/111122024009 | 2026-10-30 |
| Maksukorralduse seadus (Taxation Act), consolidated text in force from 26.10.2026, § 117 | https://www.riigiteataja.ee/et/akt/116102026010 | 2026-10-30 |
| Kogumispensionide seadus (Funded Pensions Act), consolidated text in force 01.06.2025 to 31.10.2026, § 9 | https://www.riigiteataja.ee/et/akt/103122024016 | 2026-10-30 |
| Ettevõtlustulu lihtsustatud maksustamise seadus (Simplified Business Income Taxation Act), consolidated text in force from 01.01.2026, §§ 4, 8 | https://www.riigiteataja.ee/et/akt/118122025016 | 2026-10-30 |
| Äriseadustik (Commercial Code), consolidated text in force from 01.03.2024 (the text Riigi Teataja lists as in force on 30.10.2026), §§ 179, 334 | https://www.riigiteataja.ee/et/akt/106072023131 | 2026-10-30 |
| EMTA, tax rates (2024 to 2026) | https://emta.ee/en/business-client/taxes-and-payment/income-and-social-taxes/tax-rates | 2026-10-30 |
| EMTA, entrepreneur account | https://www.emta.ee/en/private-client/taxes-and-payment/taxable-income/entrepreneur-account | 2026-10-30 |
| EMTA, social tax of self-employed persons | https://www.emta.ee/en/business-client/registration-business/businesses/self-employed-persons/social-tax | 2026-10-30 |
| Ministry of Finance, law changes in force in 2026 | https://www.fin.ee/uudised/2026-aastal-joustuvad-seadusemuudatused | 2026-10-30 |
| Ministry of Finance, Riigikogu approved the security tax changes (18.06.2025) | https://www.fin.ee/uudised/riigikogu-kiitis-heaks-julgeolekumaksu-muudatused | 2026-10-30 |

Not yet confirmed: nothing outstanding for this overview.

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
