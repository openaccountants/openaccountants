---
name: georgia-tax-optimization
description: Use this skill whenever asked about reducing tax in Georgia (country), tax planning, or legal strategies to minimise tax for an individual entrepreneur, IT business or small company in Georgia, tax year 2026. Trigger on phrases like "reduce tax Georgia", "1% tax Georgia", "small business status", "individual entrepreneur Georgia", "micro business status", "Georgia turnover tax", "virtual zone Georgia", "international company status Georgia", "IT company tax Georgia", "save tax Georgia", "tax planning Georgia". This skill covers Small Business Status (1% of Georgian-source income, 3% above GEL 500,000), Micro Business Status (0%), the international company regime (5% profit tax, 5% on salaries, no dividend tax), the virtual zone exemption for IT supplied abroad, the standard 20% / 15% system with 5% on dividends, the VAT threshold, and the eligibility and anti-avoidance red lines, including the activities barred from the special regimes. ALWAYS read this skill before advising on any Georgian tax optimisation. Computations sit in ge-corporate-income-tax, georgia-income-tax, georgia-vat and georgia-payroll.
version: 0.2
jurisdiction: GE
tax_year: 2026
last_updated: 2026-10-31
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
category: tax-optimization
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Georgia Tax Optimization

## Georgia Tax Optimization Skill v0.2

**Tier 2. Sources: the Tax Code of Georgia (consolidated text on matsne.gov.ge, publication of 15 October 2026), Government Resolution No 415 of 29 December 2010 on special tax regimes, and the Law on Information Technology Zones, read on 31 October 2026 and listed in Sources below. Figures must agree with `ge-corporate-income-tax.md`, `georgia-income-tax.md` and `georgia-social-contributions.md`; those skills win if they differ. No Georgian tax adviser has signed this off. Aggressive positions are never advised; every suggestion must be reviewed.**

## Section 1 -- Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Georgia (country) |
| Currency | GEL (lari) |
| Headline lever | **Small Business Status: 1% on Georgian-source business income** up to GEL 500,000 a year (Tax Code art. 90(1), (3)) |
| Other levers | Micro Business Status 0% up to GEL 30,000 (arts. 84, 86); international company 5% profit tax and 5% on salaries (art. 23); virtual zone: no profit tax on IT supplied outside Georgia (art. 99(1)(p)) |
| Standard system | Personal income tax 20% (art. 81(1)); profit tax 15% on distributed profit, grossed up by 0.85 (arts. 97(10), 98(1)); 5% withheld on dividends (art. 130(1)) |
| VAT threshold | GEL 100,000 of taxable supplies in any 12 consecutive months; rate 18% (arts. 165(1), 166) |
| Anti-avoidance | Barred-activity lists (Resolution 415); two-year GEL 500,000 test; international company activity list; virtual zone covers IT supplied abroad only |

> **Georgia's headline is one of the lowest effective rates anywhere:** an individual entrepreneur with Small Business Status pays **1% of taxable income**, meaning Georgian-source income other than salary and other excluded types (art. 90(1), (3)). This is a tax on gross income, not on profit. From the month gross income exceeds GEL 500,000, the rate is 3% (art. 90(2)).

## Section 2 -- Small Business Status (1% turnover tax)

**Small Business Status feature table**

| Feature | Detail |
| --- | --- |
| Who | An entrepreneur natural person, that is a registered individual entrepreneur (Tax Code art. 88(1)). The Code sets no residence or citizenship condition. |
| Rate | **1%** of taxable income (art. 90(1)). **3%** from the start of the month in which gross income passes GEL 500,000 (GEL 700,000 for wine tourism and agro tourism operators) until the end of that calendar year (art. 90(2)) |
| Taxable income | Georgian-source income, excluding salary and the income types excluded by the Government (art. 90(3)) |
| Income not taxed under the regime and not counted toward the limit | Rent; loan income; gambling winnings; gifts; gains on real estate, vehicles and securities; inheritance; dividends; interest; royalties; debt forgiveness; gains on selling a partner's share (Resolution 415, annex 5). These are taxed under the general rules. |
| Employees | Allowed. Salaries up to GEL 6,000 in total for the year are not taxed at source if the person became a small business that year, or had gross income of no more than GEL 50,000 the year before (art. 94(4)) |
| Loss of status | If gross income exceeds GEL 500,000 (GEL 700,000 for wine and agro tourism) in each of 2 calendar years, the status ends from the start of the next year (art. 89(2)(a), (3)). It also ends for a barred activity, for 3 or more cash-register fines in a year (from the start of that year), or on the person's own request (from the next month) (art. 89(2), (3^1), (4)). |
| Reporting | Monthly return and payment by the 15th of the following month (art. 93(1^1)) |
| Records | A special book of records, kept as the Minister of Finance orders (art. 91(1)) |
| Losses | Not carried forward while the person stays in the regime (art. 91(5)) |
| VAT | A small business that crosses the VAT threshold must register. It records its stock at that moment and can deduct input VAT on it if it has the documents (art. 92) |

## Section 3 -- Micro Business Status (0%)

- **Micro Business Status eligibility and rate**: an individual with no hired staff who works independently. Gross income must not exceed GEL 30,000 in the calendar year (Tax Code art. 84(1)). The Government lists some activities to which the GEL 30,000 limit does not apply (art. 84(2); Resolution 415, annex 1). A micro business pays no income tax (art. 86). The Code says "natural person" here, not "entrepreneur natural person" as for small business (arts. 84(1), 88(1)).
- **Barred activities**: those needing a licence or permit; activities whose income could exceed GEL 30,000 a year; currency exchange; medical, architectural, advocacy or notary, audit and consulting work (including tax consultants); gambling (Resolution 415, annex 2).
- **Loss of status**: on the person's request; if a stock count shows inventory over GEL 45,000; or on VAT registration (art. 85(2)). A person who passes GEL 30,000 must apply for small business status within 15 days, or loses the status (art. 85(3)).
- **Return**: an annual return before 1 April of the following year (art. 93(1); Georgian "1 აპრილამდე", so by 31 March).
- **Effect on business customers**: a company that buys from a micro business is taxed on that cost as a cost unrelated to its business. This does not apply where the micro business is taxed under the general rule, or where a consignment note or the prescribed document is issued (art. 98^2(1)(c)). Expect business customers to ask for the document.

## Section 4 -- VAT & the Standard System

- **VAT registration threshold**: a person must apply to register within 2 business days of exceeding GEL 100,000 of VAT-taxable supplies in any 12 consecutive months. VAT is due from the transaction that crosses the threshold (Tax Code art. 165(1), (2)). The rate is 18% (art. 166). Most exempt supplies are left out of the GEL 100,000 count. Exempt supplies of financial or immovable things as the main activity, exports of goods and the art. 172(1), (2) supplies are counted (art. 165(7)). Whether a service supplied to a non-resident is a Georgian taxable supply depends on the place-of-supply rules: see [georgia-vat](georgia-vat.md).
- **Standard system rates outside the special regimes**: personal income tax 20% (art. 81(1)). Profit tax 15% on distributed profit, costs unrelated to the business, free supplies and entertainment over the cap, each divided by 0.85 (arts. 97(1), (10), 98(1)). 5% withheld on dividends (art. 130(1)). Profit kept in the company is not taxed. Detail: [ge-corporate-income-tax](ge-corporate-income-tax.md).
- **Company vs small business**: a company owner who takes profit as dividends bears 15% profit tax on the grossed-up amount plus 5% withholding. Per GEL 100 of pre-tax profit paid out, that is GEL 15 + GEL 4.25 = GEL 19.25. A small business pays 1% of gross income (up to GEL 500,000) but cannot deduct costs. The company route is better only where margins are very low or profit is kept in the business.

## Section 5 -- International company (IT and other listed activities)

- **What it is**: a Georgian enterprise that carries on activities listed by Government ordinance and earns income only from them. The Government grants the status (Tax Code art. 23(1), (2), (15)).
- **Profit tax**: 5% on the same distributed-profit base as other companies, grossed up by dividing by 0.95 (art. 23(9) to (11)). Expenses listed by the Government and borne in Georgia can reduce the taxable amount (art. 23(12)).
- **Salaries**: employees' income from working for an international company is taxed at 5% (art. 23(7)).
- **Dividends**: not taxed at source, and not included in the recipient's gross income (art. 23(8)).
- **Property tax**: exempt, except on land, for property used for the permitted activities (art. 23(13)).
- **Limits**: it cannot be set up in a Free Industrial Zone (art. 23(4)). If it carries on an activity not on the list, it loses the status from 1 January of the year that activity began (art. 23(3)).

## Section 6 -- Virtual zone person (IT supplied abroad)

- **Who**: a legal person engaged in IT activities that holds virtual zone status (Tax Code art. 8(35); Law on Information Technology Zones art. 2(b)). IT means the study, support, development, design, production and introduction of computer information systems that produce software products (Law on IT Zones art. 2(c)). An individual cannot hold the status.
- **Relief**: no profit tax on profit, or its distribution, from IT the company developed and supplied outside Georgia (Tax Code art. 99(1)(p); Law on IT Zones art. 3(2)(a)). Profit from IT supplied inside Georgia is taxed under the general rules. Costs are split between the two in proportion to income (Law on IT Zones art. 3(3)).
- **Status**: granted by a person the Government designates, within 10 working days of the application. An electronic certificate follows within 2 working days (Law on IT Zones art. 5).
- **Not covered**: the relief is for profit tax on qualifying exports. Dividends paid to individuals or non-residents still bear 5% withholding (Tax Code art. 130(1)); Article 130 has no virtual zone exception. Employees' salaries are taxed at 20% (art. 81(1)).

## Section 7 -- Red Lines (do not cross)

- **Prohibited activities**: Small Business Status is barred for:
  - activities that need a licence or permit;
  - activities that need significant investment (production of excisable goods);
  - currency exchange;
  - medical, architectural, advocacy or notary, audit and consulting work, including tax consultants;
  - gambling;
  - staffing (provision of personnel);
  - production of excisable goods.
  
  (Resolution 415, annex 4; Tax Code arts. 88(2), 89(2)(c).) Carrying on a barred activity ends the status from the start of the year and draws a GEL 500 fine (arts. 89(4), 288). AUDIT FLASH POINT.
- **Genuine self-employment**: salary is not taxable income under Small Business Status (art. 90(3)). If a single-client contract is in substance employment, the income is salary taxed at 20% (art. 81(1)). Check the facts.
- **Two-year cap manipulation**: do not move income between years or between related people to stay under GEL 500,000. The rate rises to 3% from the month the GEL 500,000 is passed in any year (art. 90(2)), and the status ends after two such years (art. 89(2)(a)).
- **Monthly filing**: a small business files and pays monthly by the 15th (art. 93(1^1)). A late return costs 5% of the tax due for each month or part month, capped at 30%. More than 2 months late, the fine is 10%. There is no fine where the tax due is zero (art. 274). Late payment carries penalty interest of 0.05% a day (art. 272(4)).
- **International company and virtual zone scope**: income from activities outside the international company list costs the status for the whole year (art. 23(3)). Virtual zone relief does not cover IT supplied inside Georgia.

## PROHIBITIONS

- **Assume Small Business Status without checking prohibited list/cap**: NEVER assume Small Business Status applies without checking the Resolution 415 lists (consulting is barred) and the GEL 500,000 limit.
- **1% on profit misrepresentation**: NEVER present the 1% as applying to profit. It is on gross Georgian-source income.
- **Ignore VAT trigger**: NEVER ignore the GEL 100,000 VAT registration trigger. Check the place of supply of each service before leaving it out of the count.
- **Contradict other skill rates**: NEVER contradict the rates in `ge-corporate-income-tax.md`, `georgia-income-tax.md` or `georgia-social-contributions.md`.
- **Present research gaps as confirmed**: NEVER present the items on the "Not yet confirmed" line as confirmed, nor optimisation as definitive advice. Route to a licensed Georgian tax adviser.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a licensed tax adviser in Georgia) before acting upon.

The most up-to-date version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

## Sources

| Source | URL | Read on |
|---|---|---|
| Tax Code of Georgia, consolidated English text, publication of 15 October 2026 (arts. 8(35), 23, 81, 84 to 94, 97, 98, 98^2, 99, 130, 165, 166, 272, 274, 288) | https://matsne.gov.ge/en/document/view/1043717?publication=247 | 2026-10-31 |
| Tax Code of Georgia, Georgian original, same publication (art. 90(2) 3% period; art. 93(1) "before 1 April") | https://matsne.gov.ge/ka/document/view/1043717?publication=247 | 2026-10-31 |
| Government of Georgia Resolution No 415 of 29 December 2010, On special tax regimes (consolidated, annexes 1, 2, 4, 5) | https://matsne.gov.ge/ka/document/view/1164635?publication=14 | 2026-10-31 |
| Law of Georgia on Information Technology Zones No 4064 (arts. 2, 3, 5) | https://matsne.gov.ge/en/document/view/1152405 | 2026-10-31 |

Not yet confirmed: the Government ordinance listing international company activities and its conditions (not read); which body now grants virtual zone status (the Law says a person the Government designates); whether a small business must file a nil return in a month with no income (the old version said yes, and its "GEL 100 fine per declaration" was not found in the Code: art. 274 fines are a percentage of the tax due); the place-of-supply rules for services to non-residents (see georgia-vat); funded pension contributions for individual entrepreneurs (see georgia-social-contributions).

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
