---
name: me-tax-overview
description: "A one-page map of the Montenegrin tax system for tax year 2026, read from the laws published in the Official Gazette and on gov.me. Covers the calendar tax year, the euro, the Tax Administration (Poreska uprava) and its IRMS portal, who is resident, personal income tax at 0%, 9% and 15% (monthly salary bands EUR 700 and 1,000; annual business bands EUR 8,400 and 12,000), 15% on most other income and 12% on gambling winnings from 21 May 2026, the municipal surtax caps, corporate profit tax at 9%, 12% and 15% (bands EUR 100,000 and 1,500,000), withholding at 15% and 30%, VAT at 21%, 15%, 7% and 0% with EUR 30,000 registration, social contribution rates, the main filing deadlines and late-payment interest. Use for 'how does tax work in Montenegro', 'Montenegro tax overview', 'Montenegro tax rates 2026'. Detail sits in montenegro-income-tax, me-corporate-income-tax, montenegro-vat, montenegro-social-contributions, montenegro-payroll, me-cross-border, me-transfer-pricing and me-company-formation."
version: 0.2
jurisdiction: ME
category: international
tax_year: 2026
last_updated: 2026-10-30
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Montenegro Tax Overview

This is a map, not a computation skill. Each line gives the 2026 headline figure and its source, and names the skill in this pack that carries the full rules. Where a domain skill and this overview ever differ, the domain skill wins.

Several laws below are read from the Ministry of Finance's consolidated texts on gov.me. A consolidation is a working text; the official text is the one published in the Official Gazette (Službeni list Crne Gore).

## Montenegro tax system at a glance

- **Standard tax year.** Companies: the tax period is the financial year, which "je kalendarska godina", except on liquidation, a status change or a start of business during the year _(Corporate Profit Tax Law, art. 39(1)-(2))_. Individuals: income is taxed by calendar year, and the annual return covers "prethodnu godinu" _(PIT Law, art. 43(2))_. Detail: `me-corporate-income-tax`, `montenegro-income-tax`.
- **Currency.** Euro (EUR). The tax laws state their amounts in euros; for example the first corporate band is "do 100.000,00 eura" _(Corporate Profit Tax Law, art. 28(2))_.
- **Tax authority.** The Tax Administration (Poreska uprava) _(Tax Administration decision of 24 July 2026 on the late-payment interest rate, issued as "Crna Gora, Poreska uprava")_. Since 12 January 2026 returns are filed in its IRMS portal (https://irms.tax.gov.me/); the old CRPS and TAXIS portals closed on 31 December 2025 _(Tax Administration IRMS notice, 30 December 2025)_. The same authority keeps the business register (CRPS) and the register of beneficial owners: see `me-company-formation`.
- **Who is resident (individuals).** A person with a domicile or a centre of business and vital interests in Montenegro, or who stays in Montenegro more than 183 days in the tax year. A person sent abroad to work for a Montenegrin resident or for an international organisation is also resident _(PIT Law, art. 3)_. Detail: `montenegro-income-tax`.
- **Who is resident (companies).** A legal person incorporated in Montenegro, or with its seat of actual management and control in Montenegro _(Corporate Profit Tax Law, art. 3(1))_. A non-resident is taxed through a permanent establishment _(art. 3(2))_. Detail: `me-corporate-income-tax`, `me-cross-border`.
- **Basis of taxation.** Residents are taxed on income earned "u Crnoj Gori i izvan Crne Gore" (in and outside Montenegro); non-residents only on income earned in Montenegro _(PIT Law, art. 4; Corporate Profit Tax Law, art. 4(1)-(2))_.
- **Personal income tax on salary.** 0% on monthly taxable income up to EUR 700, 9% from EUR 700.01 to EUR 1,000, 15% above EUR 1,000 _(PIT Law, art. 10(1), point 1)_. Detail: `montenegro-payroll`.
- **Personal income tax on a principal independent activity.** 0% up to EUR 8,400 a year, 9% from EUR 8,400.01 to EUR 12,000, 15% above EUR 12,000 _(PIT Law, art. 10(1), point 2)_. Detail: `montenegro-income-tax`.
- **Personal income tax on other income.** 15% of the base for supplementary self-employment, property, property rights, capital income, capital gains and the other classes in art. 12(2) points 3 to 9 _(PIT Law, art. 10(1), point 3)_. Gambling winnings: progressive (0% to EUR 50, 10% to EUR 1,500, 15% above) up to 20 May 2026; a flat 12% from 21 May 2026 _(PIT Law, art. 10(1), point 4; amending law, Official Gazette 70/26, arts. 1 and 3)_. Detail: `montenegro-income-tax`.
- **Municipal surtax (prirez).** A municipality may add a surtax on the personal income tax of up to 13% of the tax, or up to 15% in the Capital City (Podgorica) and the Old Royal Capital (Cetinje). Each municipality sets its own rate _(Local Self-Government Financing Law, arts. 8 and 9)_. Detail: `montenegro-payroll`.
- **Corporate profit tax.** Progressive: 9% on taxable profit up to EUR 100,000; EUR 9,000 plus 12% of the excess from EUR 100,000.01 to EUR 1,500,000; EUR 177,000 plus 15% of the excess above EUR 1,500,000 _(Corporate Profit Tax Law, art. 28)_. The amendments in Official Gazette 104/26 apply from 1 January 2027, so they do not change 2026. Detail: `me-corporate-income-tax`.
- **Withholding tax on payments to non-residents.** 15% of the gross amount on dividends, interest, royalties, capital gains, rent and listed service fees; 30% where the recipient is from a listed low-tax territory; a treaty can reduce the rate _(Corporate Profit Tax Law, art. 29(4)-(7))_. Detail: `me-cross-border`.
- **VAT (PDV).** Standard rate 21% _(VAT Law, art. 24)_. Reduced rates of 7% and 15% on listed goods and services _(art. 24a(1)-(2))_. 0% on exports and the other supplies listed in art. 25 _(art. 25(1))_. Detail: `montenegro-vat`.
- **VAT registration.** A person whose supplies in the last 12 months, or a shorter period, exceed EUR 30,000 must apply for VAT registration by the 20th of the following month _(VAT Law, art. 55(1))_. Detail: `montenegro-vat`.
- **Social contributions.** Pension and disability insurance: employee 10%, employer 0% _(Law on Compulsory Social Insurance Contributions, art. 15(1))_. Unemployment insurance: employee 0.5% and employer 0.5% _(art. 18(1))_. Labour Fund: employer 0.2% _(Ministry of Finance payroll Instruction, art. 5)_. See `montenegro-social-contributions` for the bases, entrepreneurs and the annual pension ceiling, and `montenegro-payroll` for the employer charges.
- **Corporate tax return and payment.** Within three months after the end of the tax period, so by 31 March 2027 for calendar year 2026. The tax shown in the return is paid in the same time _(Corporate Profit Tax Law, art. 40(3))_. The balance sheet and income statement go with the return _(art. 40(4))_. Detail: `me-corporate-income-tax`.
- **Annual personal income tax return (GPP-FL).** By the end of April of the current year for the previous year, so by 30 April 2027 for 2026 income _(PIT Law, art. 43(2))_. Detail: `montenegro-income-tax`.
- **VAT return and payment.** Monthly. The return is filed electronically by the 15th of the month after the tax period, even when no VAT is due _(VAT Law, art. 35(1)-(3))_. Payment is due on the 15th of the month after the period _(art. 36(1))_. Detail: `montenegro-vat`.
- **Payroll reporting (IOPPD).** The employer files the monthly report on income tax and contributions by the 15th of the current month for the previous month _(PIT Law, art. 47(3))_. Detail: `montenegro-payroll`.
- **Late-payment interest.** 0.03% a day from 1 January to 17 July 2026 _(Tax Administration Law, art. 95(1), text before 104/26)_. From 18 July to 31 December 2026: 5.4% a year _(Tax Administration Law, art. 95, as changed by Official Gazette 104/26; Tax Administration decision of 24 July 2026)_.

## Which skill to use

| Question | Skill |
|---|---|
| A resident's or non-resident's income tax, business profit, rent, capital income, gambling, the GPP-FL return | `montenegro-income-tax` |
| Company profit tax, depreciation, losses, incentives, the PD return | `me-corporate-income-tax` |
| VAT rates, registration, the monthly return, reverse charge, refunds | `montenegro-vat` |
| Pension and unemployment contributions, entrepreneurs, the annual ceiling | `montenegro-social-contributions` |
| Gross to net, surtax, Chamber dues, the IOPPD report | `montenegro-payroll` |
| Withholding on payments abroad, permanent establishments, treaties, foreign tax credit | `me-cross-border` |
| Related-party prices and documentation | `me-transfer-pricing` |
| d.o.o. or a.d., share capital, CRPS registration, annual accounts | `me-company-formation` |
| Lawful ways to lower the tax bill | `montenegro-tax-optimization` |

## Sources

| Source | URL | Read on |
|---|---|---|
| Personal Income Tax Law (Zakon o porezu na dohodak fizičkih lica), Ministry of Finance consolidation through 160/25, arts. 3, 4, 10, 43, 47 | https://wapi.gov.me/download/b8465a42-2073-4894-9be0-3b965c2f7195?version=1.0 | 2026-10-30 |
| Law amending the Personal Income Tax Law, Official Gazette 70/26 (gambling winnings 12%) | https://www.sluzbenilist.me/propisi/394390/download | 2026-10-30 |
| Corporate Profit Tax Law (Zakon o porezu na dobit pravnih lica), Ministry of Finance consolidation through 88/24, arts. 3, 4, 28, 29, 39, 40 | https://wapi.gov.me/download/8826962a-3806-4619-afa4-0029b0a57afb?version=1.0 | 2026-10-30 |
| Law amending the Corporate Profit Tax Law, Official Gazette 104/26 (applies from 1 January 2027) | https://wapi.gov.me/download/8951908b-625c-4219-aefe-0c86501ddaf8?version=1.0 | 2026-10-30 |
| VAT Law (Zakon o porezu na dodatu vrijednost), Ministry of Finance consolidation through 12/26, arts. 24, 24a, 25, 35, 36, 55 | https://wapi.gov.me/download/795cb7a3-2699-44bd-baa6-b11802121045?version=1.0 | 2026-10-30 |
| Law on Compulsory Social Insurance Contributions, Ministry of Finance publication through 160/25, arts. 15, 18 | https://wapi.gov.me/download/97253561-f373-4456-a024-b15f6596a0f2?version=1.0 | 2026-10-30 |
| Ministry of Finance Instruction on payroll calculation, art. 5 (Labour Fund 0.2%) | https://wapi.gov.me/download/f73befc2-975e-42d9-af00-4d5de0a3172d?version=1.0 | 2026-10-30 |
| Local Self-Government Financing Law, through 149/2025, arts. 8 and 9 (surtax) | https://wapi.gov.me/download/98dd2203-4c4e-4751-bbb9-9ad1e13564bd?version=1.0 | 2026-10-30 |
| Tax Administration Law, text before 104/26, art. 95 (0.03% a day) | https://wapi.gov.me/download/2dd530ac-eec4-4d0c-9d8f-0c9e7ebc5b86?version=1.0 | 2026-10-30 |
| Law amending the Tax Administration Law, Official Gazette 104/26, arts. 20 and 26 | https://wapi.gov.me/download/c22f3c59-7e52-4213-bbe4-3cd9d8d3a373?version=1.0 | 2026-10-30 |
| Tax Administration decision on the late-payment interest rate for 18 July to 31 December 2026 (24 July 2026) | https://wapi.gov.me/download/6d6ec964-3dd6-4588-b81a-a5affc153f6e?version=1.0 | 2026-10-30 |
| Tax Administration notice on the start of the IRMS system (30 December 2025) | https://www.gov.me/clanak/vazno-obavjestenje-u-vezi-sa-pocetkom-primjene-novog-integrisanog-it-sistema-poreske-uprave-irms | 2026-10-30 |

Not yet confirmed: each municipality's 2026 surtax rate (only the 13% and 15% caps are confirmed); the art. 49 lump-sum tax scale for small entrepreneurs; the 2026 annual pension contribution ceiling (not published by 30 October 2026); and treaty withholding rates by country.

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
