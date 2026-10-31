---
name: belarus-tax-optimization
description: 'Use this skill whenever asked about reducing tax in Belarus, tax planning, or legal strategies to minimise tax for an individual entrepreneur, a self-employed individual or a small company in Belarus, for tax year 2026. Trigger on phrases like "reduce tax Belarus", "individual entrepreneur Belarus", "IP vs LLC", "simplified tax Belarus", "self-employed Belarus", "professional income tax Belarus", "HTP", "High-Tech Park", "save tax Belarus", "tax planning Belarus". This skill covers the 2026 individual-entrepreneur rules (permitted activity list, three-person cap, 20% or 30% above BYN 500,000), the professional income tax for people without registration, the company simplified system (6%), the High-Tech Park (HTP) regime, the 2026 dividend and share-sale rates, and the red lines. Out of scope: the computations themselves, which sit in belarus-income-tax, by-corporate-income-tax, belarus-social-contributions and belarus-cross-border-tax, and company set-up (by-company-formation). ALWAYS read this skill before advising on any Belarusian tax optimisation.'
version: 0.2
jurisdiction: BY
tax_year: 2026
last_updated: 2026-10-31
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
category: tax-optimization
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Belarus Tax Optimization

## Belarus Tax Optimization Skill v0.2

**Tier 2, checked against the law. Sources: the Tax Code (Special and General Parts, consolidated to Law No. 127-Z of 30 December 2025), Law No. 127-Z itself (transitional rules), Law No. 365-Z of 22 April 2024, Council of Ministers Resolution No. 457 of 28 June 2024, Presidential Decree No. 12 of 22 September 2005 on the High-Tech Park and Law No. 118-Z on FSZN contributions, all read on pravo.by, plus MNS commentary pages on nalog.gov.by, on 31 October 2026. Figures must agree with [belarus-income-tax](belarus-income-tax.md), [by-corporate-income-tax](by-corporate-income-tax.md) and [belarus-social-contributions](belarus-social-contributions.md); where they differ, those skills win. NOT yet signed off by a Belarusian tax adviser. Aggressive positions are never advised; every suggestion must be reviewed. NOTE: Belarus has TIGHTENED its small-business regimes; this playbook is as much about compliance as savings.**

## Section 1 -- Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Republic of Belarus |
| Currency | BYN (Belarusian ruble) |
| Headline reality | Since 1 January 2026 every individual entrepreneur (IP) must work only in activities on the permitted list and may engage at most **three** people; the transition ended on 31 December 2025 |
| IP general tax | 20% on business income after expenses (actual, or deemed 20%; 30% for retail/transport only); **30% for the whole year** once business income exceeds BYN 500,000 |
| Professional income (no registration) | 10%; 20% on income from Belarus businesses above BYN 60,000 a year; includes the FSZN contribution |
| Company simplified system | 6% of gross revenue; at most 50 staff and BYN 3,735,000 revenue in the year |
| HTP (IT) | Residents exempt from profit tax and from VAT on domestic sales; pay 1% of revenue to the HTP administration; 9% personal income tax on staff pay and dividends |
| Dividends | Individuals 13% (25% above BYN 350,000); companies 12%; 0% after five years without distribution; the old 6% company rate is repealed |
| Share sales | No general personal income tax exemption: 13%. HTP-resident shares held 365 days or more: exempt |
| Anti-avoidance | Permitted activity list; three-person cap; 26% rate on unregistered business income |

- **IP permitted-list audit flash point**: from 1 October 2024 no IP is registered for an activity outside the list, and IPs registered earlier could continue unlisted activities only until 31 December 2025 _(Law No. 365-Z, art. 12)_. In 2026 an IP outside the list is carrying on unlawful business; income from business without registration is taxed at 26% _(Tax Code, Special Part, art. 214(7.4))_. Do not plan around the old IP regimes without checking the activity against Annex 1 to Resolution No. 457. _(AUDIT FLASH POINT)_

## Section 2 -- Individual Entrepreneur (IP), restricted

- **Who may be an IP**: an IP may carry on only activities on the Council of Ministers list (Annex 1 to Resolution No. 457) and may engage no more than three individuals under employment or civil-law contracts for work, services or intellectual property _(Civil Code art. 22(1), as worded by Law No. 365-Z, art. 1; Resolution No. 457, Annex 1)_. Computer programming and related consultancy (OKED 62) is on the list.
- **General system tax rate**: 20% on business income _(Special Part, art. 214(3))_. The IP deducts documented expenses or takes deemed expenses of 20% of taxable business income (30% for an IP doing only retail and/or transport from the list) _(art. 205(10))_. Once business income since 1 January exceeds BYN 500,000, the rate is 30% for the **whole** year, not only on the excess _(art. 214(3))_. Detail: [belarus-income-tax](belarus-income-tax.md).
- **Single tax narrowed to four activities for IPs**: for an IP the single tax covers only short-stay accommodation, construction and taxi services to consumers, and retail of listed goods groups _(Special Part, art. 337(1))_. Everything else, including IT services, goes on the general 20% system.
- **No simplified system for an IP**: the 6% simplified system is open only to Belarus legal entities _(Special Part, art. 324(1))_. An IP who wants it must trade through a company (Section 4).
- **IP-to-company route**: an IP may set up a single-founder commercial organisation under the procedure annexed to Law No. 365-Z; that company has a two-year holiday from selective inspections _(Law No. 365-Z, arts. 14-15)_. A territorial tax relief that runs from registration date counts from the IP's own registration date when the company is created from 1 January 2026 _(art. 16)_. Detail: [by-company-formation](by-company-formation.md).
- **Social contributions**: an IP pays 29% pension and 6% social insurance contributions on its own income _(Law No. 118-Z, art. 5)_. The base is the income-tax base after art. 205 expenses; if that income is more than 12 December minimum wages, contributions are at least those on the monthly minimum wages for the months covered _(art. 9(3))_. The minimum wage is BYN 858 a month from 1 January 2026 _(Council of Ministers Resolution No. 612 of 06.11.2025, paras. 1, 4)_. Detail: [belarus-social-contributions](belarus-social-contributions.md).

### Worked example: the BYN 500,000 cliff

An IP on the general system with deemed expenses of 20% earns BYN 480,000 in 2026. Expenses are 96,000, the base is 384,000 and tax at 20% is 76,800. If the same IP earns BYN 520,000, the 30% rate applies to the whole year: expenses 104,000, base 416,000, tax 124,800. Earning 40,000 more costs 48,000 more tax. (Deductions and FSZN are ignored.) This is not a reason to split income across people or entities without substance (Section 7).

```oa-check
name: BY IP 2026, 20% below and 30% above BYN 500,000
inputs:
  income_low: 480000
  income_high: 520000
steps:
  - base_low: income_low - income_low * 0.20
  - tax_low: base_low * 0.20
  - base_high: income_high - income_high * 0.20
  - tax_high: base_high * 0.30
  - extra_tax: tax_high - tax_low
expected:
  tax_low: 76800
  tax_high: 124800
  extra_tax: 48000
```

## Section 3 -- Self-Employed (private person, no IP)

- **Independent professional activity**: an individual who has no employer for the activity and engages no one may work, without IP registration, in the activities on Annex 2 to Resolution No. 457 after notifying the tax authority that a special regime applies _(Civil Code art. 22(1)(2), as worded by Law No. 365-Z; Resolution No. 457, Annex 2)_. Annex 2 includes website development, software development and testing (item 63).
- **Professional income tax**: 10% of professional income; 20% on income from Belarus-registered organisations and IPs above BYN 60,000 in the calendar year _(Special Part, art. 381-2(1))_. No expense deduction. The app is used for every receipt; income without a receipt, or with a late one, is taxed at 20% _(art. 381-2(2))_. From 1 July 2026 the tax is at least BYN 45 a month, including months with no income _(art. 381-6(2), as worded by Law No. 127-Z, art. 2 item 172, in force from 1 July 2026 under art. 6)_; for pension recipients the MNS gives a minimum of BYN 18 _(MNS, "NPD from 01.07.2026")_. A registered payer who stops working should deregister, or the minimum keeps accruing.
- **FSZN contributions are included, not voluntary**: the professional income tax includes the compulsory FSZN contribution _(Special Part, art. 380(1.2))_; 60% of the tax paid goes to the FSZN, except for pensioners and people paying additional pension contributions _(Law No. 118-Z, art. 16-1(1))_. The old version of this skill said contributions were only voluntary; that does not hold for the professional income tax.
- **Single tax for non-entrepreneurs**: an individual doing an Annex 2 activity may instead pay the single tax where that activity is a single-tax object for individuals, for example website development and computer set-up for consumers _(Law No. 365-Z, art. 13; Special Part, art. 337(3.1.17))_. The monthly amounts are in Annex 24 and are not restated here.
- **Employer trap**: professional income tax does not cover work or services for the person's current employer, or for a former employer within three years _(Special Part, art. 379)_. Converting staff to "self-employed" contractors does not work.

## Section 4 -- Company simplified system

- **Rate and limits**: a Belarus legal entity on the simplified system pays 6% of gross revenue _(Special Part, art. 329)_ instead of profit tax, VAT on domestic sales and real estate tax, with listed exceptions such as dividends and share gains _(art. 326(1))_. It loses the system from the month after average staff since 1 January exceed 50 or revenue since 1 January exceeds BYN 3,735,000 _(art. 327(6.3)-(6.4))_. Entry for 2027 needs average staff of at most 50 and revenue of at most BYN 2,800,000 in the first nine months of 2026 _(art. 327(2))_; for 2026 entry the limit was BYN 2,625,000 for the first nine months of 2025 _(MNS commentary 33838)_. A company that used the simplified system in 2025 and had 2025 revenue above BYN 3,500,000 cannot use it in 2026, despite the higher 2026 limit _(Law No. 127-Z, art. 4(4))_. Detail: [by-corporate-income-tax](by-corporate-income-tax.md).
- **General system: investment deduction**: a company on the general profit tax system may expense an investment deduction of up to 20% of the initial cost of production buildings, structures and transmission devices, and up to 40% for machinery, equipment and vehicles (not ordinary passenger cars, except special-purpose, taxi and car-sharing cars) used in business, over two years from the period in which depreciation starts _(Special Part, art. 170(2.2))_. The MNS 2026 commentary says that in 2026, as in 2025, the deduction may be applied only to production buildings and structures. The Code as amended to Law No. 127-Z has no such limit: art. 170(2.2) still gives 40% for machinery and equipment, and the statute wins over the commentary. Deductions whose two-year period began before 1 January 2026 continue under the rules in force when it began _(Law No. 127-Z, art. 4(3))_.
- **Who cannot use it**: among others, companies more than 25% owned by other organisations, holding participants, banks, insurers, realtors, token businesses, and residents of the HTP and free economic zones _(art. 324(2))_.

## Section 5 -- HTP (High-Tech Park) for IT

- **The regime**: the HTP is a special legal regime that runs until 1 January 2049 _(Decree No. 12, para. 2)_. Residents (companies and IPs) must carry on the HTP's listed activities and pay the HTP administration 1% of the previous quarter's revenue from those activities _(Regulation on the HTP, para. 17)_.
- **Company taxes**: residents are exempt from profit tax (except tax withheld as agent) and from VAT on sales in Belarus. The VAT exemption does not cover exported goods (including goods taken to other EAEU states) or rent from the resident's own property _(Regulation, paras. 27-28)_. Share-sale gains, sales of securities, interest and some other income are taxed at 9% profit tax _(para. 28)_. The token-profit exemption is suspended by Law No. 47-Z of 13 December 2024 _(note to para. 27)_. Residents are also exempt from real estate tax on HTP-located property they do not let out _(para. 30)_, and their annual accounts need a mandatory audit (see [by-company-formation](by-company-formation.md)).
- **People**: employment income from a resident, the income of a resident IP, and dividends from a resident are taxed at 9% personal income tax _(Regulation, para. 31)_. A resident IP pays 9% on token transactions _(Special Part, art. 214(3-1))_. Gains on HTP-resident shares held at least 365 days are exempt _(Regulation, para. 31)_. FSZN contributions are not charged on the part of an employee's pay above one national average monthly wage; the employee may opt out of this cap _(para. 34)_.
- **Foreign owners**: dividends paid by a resident to a foreign company are taxed at 5% unless a treaty gives less; certain other payments by a resident to foreign companies, including share-sale proceeds, interest and royalties, are taxed at 0% _(Regulation, paras. 33, 36)_.
- **Route**: the company (HTP-resident company) route, not the restricted IP route, is the usual way an IT business uses the regime. HTP residents cannot also use the simplified system _(Special Part, art. 324(2.3.6))_.

## Section 6 -- Dividends & Capital Gains (2026)

- **Dividends to individuals**: 13%; dividends above BYN 350,000 for the year are taxed at 25% on the excess; 0% for a resident where the Belarus company has not distributed profit to resident participants for the five preceding calendar years in a row _(Special Part, art. 214(1.2), (6))_
- **Dividends to Belarus companies**: 12%; 0% under the same five-year condition. The former 6% clause (art. 184(7)) is repealed _(Special Part, art. 184(6)-(8))_
- **Dividends to foreign companies**: 25% before treaty relief _(Special Part, arts. 189(1.4), 192(1.4))_; 5% where paid by an HTP resident (Section 5). Detail: [belarus-cross-border-tax](belarus-cross-border-tax.md).
- **Capital gains on Belarusian company shares**: no general exemption in the Code's exemption list, so the ordinary 13% applies to the gain _(Special Part, arts. 208, 214(1.1))_. HTP-resident shares held at least 365 days are exempt (Section 5).
- **Extraction within limits**: salary above BYN 350,000 a year moves into the 25% and 30% bands, while dividends top out at 25% _(art. 214(1.2)-(1.3))_. The five-year 0% only works if no distribution at all is made to resident participants during those five years.

## Section 7 -- Red Lines (do not cross)

- **IP activity list**: the single biggest compliance item. The transition ended on 31 December 2025; an IP outside Annex 1 is carrying on unlawful business, and unregistered business income is taxed at 26% _(Law No. 365-Z, art. 12; Special Part, art. 214(7.4))_.
- **Three-person cap**: an IP may engage at most three individuals; a business that needs more people must be a company _(Civil Code art. 22(1))_.
- **IT is not on the IP single tax**: an IT IP pays the general 20% (or 30%) system _(Special Part, art. 337(1))_.
- **Dividend rates**: do not rely on the repealed 6% company rate; the 0% rate needs five full years with no distribution to resident participants.
- **No business splitting**: do not split a business to stay under BYN 500,000, the BYN 60,000 professional-income band or the simplified-system limits without real substance.
- **HTP substance**: the HTP benefits depend on resident status and on the listed activities; income from other activities is taxed normally.

## PROHIBITIONS

- **NEVER advise IT activity under the IP single tax**: IT services are not a single-tax object for an IP (general 20% or 30% only).
- **NEVER plan around an IP activity that is not on the permitted list**: since 1 January 2026 there is no transition period left.
- **NEVER present the 6% company dividend rate as current**: it is repealed; the rates are 12% or 0%.
- **NEVER present the professional income tax as free of FSZN**: the contribution is built into the tax.
- **NEVER contradict related skill rates**: NEVER contradict the rates in `belarus-income-tax.md` / `by-corporate-income-tax.md` / `belarus-social-contributions.md`.
- **NEVER present Not yet confirmed items as confirmed**: nor optimisation as definitive advice; route to a licensed Belarusian tax adviser.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a licensed tax adviser in Belarus) before acting upon.

The most up-to-date version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

## Sources

| Source | URL | Read on |
|---|---|---|
| Tax Code, Special Part, consolidated to Law No. 127-Z of 30.12.2025: arts. 170, 184, 189, 192, 205, 208, 214, 324, 326, 327, 329, 337, 379, 380, 381-2, 381-6 | https://pravo.by/document/?guid=3871&p0=hk0900071 | 2026-10-31 |
| Law No. 365-Z of 22.04.2024 on amending laws on business activity (Civil Code art. 22): arts. 1, 12-16, 23 | https://pravo.by/document/?guid=3871&p0=H12400365 | 2026-10-31 |
| Council of Ministers Resolution No. 457 of 28.06.2024 on types of individual business activity: Annexes 1 and 2 | https://pravo.by/document/?guid=3871&p0=C22400457 | 2026-10-31 |
| Presidential Decree No. 12 of 22.09.2005 on the High-Tech Park and the Regulation on the HTP: paras. 2, 17, 27-36 | https://pravo.by/document/?guid=3871&p0=Pd0500012 | 2026-10-31 |
| Law No. 118-Z of 15.07.2021 on FSZN contributions: arts. 5, 9, 16-1 | https://pravo.by/document/?guid=3871&p0=H12100118 | 2026-10-31 |
| Law No. 127-Z of 30.12.2025 on amending tax laws: art. 2 item 172, arts. 4(3)-(4), 6 | https://pravo.by/upload/docs/op/H12500127_1767214800.pdf | 2026-10-31 |
| Council of Ministers Resolution No. 612 of 06.11.2025 (minimum wage BYN 858): paras. 1, 4 | https://pravo.by/document/?guid=12551&p0=C22500612 | 2026-10-31 |
| MNS, "NPD from 01.07.2026" (BYN 45 minimum, BYN 18 for pension recipients) | https://nalog.gov.by/actual/npd_45/ | 2026-10-31 |
| MNS commentary 33838 (simplified system limits 2026/2027) | https://nalog.gov.by/clarifications/comments/33838/ | 2026-10-31 |
| MNS commentary 33570 (profit tax 2026: investment deduction) | https://nalog.gov.by/clarifications/comments/33570/ | 2026-10-31 |

Not yet confirmed: the single-tax monthly amounts (Annex 24), the HTP activity list (Regulation para. 3) and the HTP rules for token transactions after Law No. 47-Z are not restated. Decree No. 8 of 21.12.2017 on the digital economy was saved but not used for figures.

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
