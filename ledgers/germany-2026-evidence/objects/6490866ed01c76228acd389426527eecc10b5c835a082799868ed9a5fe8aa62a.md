---
name: de-payroll-benefits
description: "German payroll benefits for 2026: how an employer values and taxes benefits in kind on the payslip. Covers the EUR 50 monthly limit for benefits in kind and vouchers, company cars (1% rule, 0.03% commute charge, a quarter or a half of the list price for electric and plug-in hybrid cars, the EUR 100,000 price cap, the logbook method, user charges), meals and lodging at the 2026 official values, the 30% flat tax of § 37b EStG and the 15%, 20% and 25% flat taxes of §§ 40 and 40b, tax-free items (public transport tickets, childcare, health promotion, bikes, charging, devices, employee shares), employer pensions (8% and 4% limits, the § 100 subsidy, salary sacrifice and the 15% top-up), and the social insurance status of managing directors with the DRV status procedure. Trigger on: Sachbezug, geldwerter Vorteil, Dienstwagen, 1%-Regelung, Fahrtenbuch, Sachbezugswerte 2026, 37b, Pauschalsteuer, Jobticket, bAV, Entgeltumwandlung, Gesellschafter-Geschäftsführer, Statusfeststellung. Out of scope: the wage tax and contribution run itself (de-payroll), the employee's annual return (de-employee-income-tax), self-employed contributions (de-social-contributions)."
version: 0.2
jurisdiction: DE
tax_year: 2026
last_updated: 2026-10-29
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# German payroll benefits 2026: benefits in kind, company cars, flat taxes, employer pensions and managing directors

> **General reference only.** This skill is general tax reference material for AI-assisted work. It has not been reviewed for any specific employer's or employee's facts. A Steuerberater or payroll accountant should confirm the treatment before a real payroll run.

**Sibling skills.** The monthly wage tax and contribution run (tax classes, the 2026 PAP, rates, ceilings, Minijobs, filing and payment dates): [de-payroll](de-payroll.md). [germany-payroll](germany-payroll.md) is an older version of that run. The employee's own annual return: [de-employee-income-tax](de-employee-income-tax.md). Contributions of the self-employed: [de-social-contributions](de-social-contributions.md). Non-residents: [de-non-resident-tax](de-non-resident-tax.md).

## Who this applies to

- **In.** Any employer that runs German payroll (wage tax under § 38 EStG) and gives employees anything other than cash pay: goods, services, vouchers, a car, meals, lodging, gifts, event costs, pension contributions. It also covers the employer's choice to pay a flat tax on a benefit instead of taxing it through the employee's tax class.
- **Benefits in kind are pay.** Income includes everything received in money or money's worth (§ 8(1) EStG). Non-cash income is valued at the usual end price at the place of supply, less usual discounts (§ 8(2) sentence 1 EStG), unless a special rule below applies.
- **Social insurance follows tax, with exceptions.** The social insurance value of a benefit is set by the Sozialversicherungsentgeltverordnung (SvEV). Many tax-free or flat-taxed items are also free of contributions, but only if the payroll leaves them tax-free or flat-taxed in the pay period they belong to (§ 1(1) last sentences SvEV).
- **Managing directors.** A GmbH managing director is an employee for wage tax. Whether they are also an insured employee for social insurance depends on the status test in § 7(1) SGB IV, covered below.
- **Out.** Gifts to non-employees are in only as far as § 37b EStG lets the giver pay a flat tax on them. Pensions in payment, severance pay and share option plans of listed groups are not covered.

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source URL |
|---|---|---|---|
| Benefits in kind valued at market price: tax-free if the total net benefit is not more than this a month (a cliff, not an allowance); vouchers count only if given on top of pay owed (EStG § 8(2) sentence 11) | EUR 50 a month | 2026 | https://www.gesetze-im-internet.de/estg/__8.html |
| Staff discount on the employer's own goods and services: value is the public price less 4%, then tax-free up to this amount a year (EStG § 8(3)) | 4% markdown; EUR 1,080 a year | 2026 | https://www.gesetze-im-internet.de/estg/__8.html |
| Company car, private use (EStG § 8(2) sentence 2 with § 6(1) no. 4 sentence 2) | 1% of the gross list price a month | 2026 | https://www.gesetze-im-internet.de/estg/__6.html |
| Company car, home to first place of work (EStG § 8(2) sentence 3) | 0.03% of the list price per km of one-way distance a month | 2026 | https://www.gesetze-im-internet.de/estg/__8.html |
| Company car, home trips in a double household (EStG § 8(2) sentence 5) | 0.002% of the list price per km per trip | 2026 | https://www.gesetze-im-internet.de/estg/__8.html |
| Electric car with zero CO2, bought 1 Jan 2019 to 31 Dec 2030, gross list price not over the cap: list price counted at (EStG § 6(1) no. 4 sentence 2 no. 3) | one quarter | 2026 | https://www.gesetze-im-internet.de/estg/__6.html |
| Price cap for the quarter rate: cars bought after 30 June 2025 (EStG § 6(1) no. 4 sentence 2 no. 3; § 52(12) sentence 6) | EUR 100,000 | 2026 | https://www.gesetze-im-internet.de/estg/__52.html |
| Price cap for the quarter rate: cars bought 1 Jan 2024 to 30 June 2025 (Wachstumschancengesetz art. 3; § 52(12) sentence 5) | EUR 70,000 | 2026 | https://www.recht.bund.de/bgbl/1/2024/108/VO.html |
| Price cap for the quarter rate: cars bought 1 Jan 2019 to 31 Dec 2023 (EStG § 52(12) sentence 4; BMF letter of 5 November 2021, BStBl I p. 2205, Rn. 11) | EUR 60,000 | 2026 | https://lsth.bundesfinanzministerium.de/lsth/2026/B-Anhaenge/Anhang-24/IV/IV-6/anhang-24-IV-6.html |
| Electric car over the cap, or plug-in hybrid with at most 50 g CO2/km or at least 80 km electric range, bought 1 Jan 2025 to 31 Dec 2030 (EStG § 6(1) no. 4 sentence 2 no. 5) | one half | 2026 | https://www.gesetze-im-internet.de/estg/__6.html |
| Electric car over the cap, or plug-in hybrid with at most 50 g CO2/km or at least 60 km range, bought 1 Jan 2022 to 31 Dec 2024 (EStG § 6(1) no. 4 sentence 2 no. 4) | one half | 2026 | https://www.gesetze-im-internet.de/estg/__6.html |
| Electric car over the cap, or plug-in hybrid with at most 50 g CO2/km or at least 40 km range, bought 1 Jan 2019 to 31 Dec 2021 (EStG § 6(1) no. 4 sentence 2 no. 2 with § 3(2) EmoG; BMF letter of 5 November 2021, Rn. 11) | one half | 2026 | https://www.gesetze-im-internet.de/estg/__6.html |
| List price for the 1%, 0.03% and 0.002% rules: rounded down to the full EUR 100, after any quarter or half is applied (R 8.1(9) no. 1 sentence 6 LStR; BMF letter of 5 November 2021, Rn. 12) | full EUR 100 | 2026 | https://lsth.bundesfinanzministerium.de/lsth/2026/A-Einkommensteuergesetz/II-Einkommen-2-24b/4-Ueberschuss-d-Einnahmen-ueber-die-Werbungsk-8-9a/Paragraf-8/r-8-1-9.html |
| Meals provided as benefit in kind, monthly (SvEV § 2(1)) | EUR 345: breakfast 71, lunch 137, dinner 137 | 2026 | https://www.gesetze-im-internet.de/svev/__2.html |
| Single meal (one thirtieth of the monthly value, rounded to the cent, SvEV § 2(6)) | breakfast EUR 2.37; lunch or dinner EUR 4.57 | 2026 | https://www.gesetze-im-internet.de/svev/__2.html |
| Lodging, monthly (SvEV § 2(3)); flat rate for a flat where the local rent is very hard to find (SvEV § 2(4)) | EUR 285; EUR 5.01 per m2 (EUR 4.10 basic) | 2026 | https://www.gesetze-im-internet.de/svev/__2.html |
| Meal on a business trip valued at the official value if its price is not over (EStG § 8(2) sentence 8) | EUR 60 | 2026 | https://www.gesetze-im-internet.de/estg/__8.html |
| Employer-provided flat: no benefit if the rent paid is at least two thirds of local rent and local rent is not over (EStG § 8(2) sentence 12) | EUR 25 per m2 | 2026 | https://www.gesetze-im-internet.de/estg/__8.html |
| Flat tax on non-cash gifts and incentives (EStG § 37b(1), (2)); capped at EUR 10,000 per recipient a year, excluded for a single gift over EUR 10,000 | 30% | 2026 | https://www.gesetze-im-internet.de/estg/__37b.html |
| Flat tax on canteen meals, trip meals, staff events, recreation grants, devices, chargers, bikes given outright (EStG § 40(2) sentence 1) | 25% | 2026 | https://www.gesetze-im-internet.de/estg/__40.html |
| Recreation grants, flat tax limit a year (EStG § 40(2) sentence 1 no. 3) | EUR 156 employee, EUR 104 spouse, EUR 52 per child | 2026 | https://www.gesetze-im-internet.de/estg/__40.html |
| Commuting subsidies or car commute benefit (EStG § 40(2) sentence 2 no. 1); public transport instead of tax-free (no. 2) | 15%; 25% | 2026 | https://www.gesetze-im-internet.de/estg/__40.html |
| Flat tax on a larger number of one-off payments at an average rate, on application; excluded above (EStG § 40(1)) | EUR 1,000 per employee a year | 2026 | https://www.gesetze-im-internet.de/estg/__40.html |
| Staff event: allowance per event and attending employee (companions' share included), for up to two events a year, if open to all staff (EStG § 19(1) no. 1a) | EUR 110 | 2026 | https://www.gesetze-im-internet.de/estg/__19.html |
| Solidarity surcharge on flat wage tax (SolzG §§ 3, 4) | 5.5% | 2026 | https://www.gesetze-im-internet.de/solzg_1995/__4.html |
| Tax-free: health promotion meeting SGB V §§ 20, 20b (EStG § 3 no. 34) | EUR 600 a year | 2026 | https://www.gesetze-im-internet.de/estg/__3.html |
| Tax-free: employee shares in the employer (EStG § 3 no. 39) | EUR 2,000 a year | 2026 | https://www.gesetze-im-internet.de/estg/__3.html |
| Pension ceiling (general pension insurance), base for the bAV limits (SVBezGrV 2026 § 4(1) no. 1) | EUR 101,400 a year | 2026 | https://www.recht.bund.de/bgbl/1/2025/278/regelungstext.pdf?__blob=publicationFile&v=3 |
| bAV: employer contributions to Pensionsfonds, Pensionskasse or Direktversicherung tax-free (EStG § 3 no. 63) | 8% of the ceiling = EUR 8,112 | 2026 | https://www.gesetze-im-internet.de/estg/__3.html |
| bAV: contribution-free part of those contributions (SvEV § 1(1) no. 9) | 4% of the ceiling = EUR 4,056 | 2026 | https://www.gesetze-im-internet.de/svev/__1.html |
| bAV: unfunded Pensionskasse, tax-free (EStG § 3 no. 56), less § 3 no. 63 amounts | 4% of the ceiling = EUR 4,056 | 2026 | https://www.gesetze-im-internet.de/estg/__3.html |
| bAV: old Pensionskasse flat tax and limit (EStG § 40b(1), (2)) | 20%; EUR 1,752 a year | 2026 | https://www.gesetze-im-internet.de/estg/__40b.html |
| bAV subsidy for low earners: 30% of the employer's extra contribution of at least EUR 240, capped (EStG § 100(2), (3)) | max EUR 288 a year | 2026 | https://www.gesetze-im-internet.de/estg/__100.html |
| § 100 pay limit at the time of the contribution (EStG § 100(3) no. 3) | EUR 2,575 a month; EUR 30,900 a year | 2026 | https://www.gesetze-im-internet.de/estg/__100.html |
| § 100 contribution tax-free up to (EStG § 100(6)) | EUR 960 a year | 2026 | https://www.gesetze-im-internet.de/estg/__100.html |
| § 100 from 1 January 2027: subsidy max EUR 360, tax-free up to EUR 1,200, pay limit 3% of the monthly pension ceiling (Zweites Betriebsrentenstärkungsgesetz, BGBl. 2026 I No. 14, art. 2 no. 2, art. 18(4)) | EUR 360; EUR 1,200 | 2027 | https://www.recht.bund.de/bgbl/1/2026/14/VO.html |
| Salary sacrifice: employee right up to 4% of the ceiling; employer top-up where it saves contributions (BetrAVG § 1a(1), (1a)) | 4% = EUR 4,056; top-up 15% | 2026 | https://www.gesetze-im-internet.de/betravg/__1a.html |

## The taxable base

**The EUR 50 limit.** Benefits valued at market price under § 8(2) sentence 1 EStG stay out of pay if the total net benefit in the month is not over EUR 50. It is a cliff: at EUR 50.01 the whole amount is taxable. Benefits valued by a special rule (company car, official meal values, staff discounts under § 8(3)) do not count toward it and cannot use it. Vouchers and cash cards that only buy goods or services and meet the payment-services criteria count as benefits in kind, but only if given on top of the pay already owed (§ 8(1) sentence 3 and § 8(2) sentence 11 EStG). "On top of pay owed" means no offset against pay, no pay cut in exchange, not instead of an agreed raise, and no pay rise if the benefit stops (§ 8(4) EStG). The same EUR 50 limit applies for contributions (§ 3(1) SvEV).

**Company cars.**
- **1% rule.** Private use is 1% of the domestic gross list price at first registration, plus factory extras, including VAT, each month (§ 6(1) no. 4 sentence 2 with § 8(2) sentence 2 EStG). The list price is used even for a used or leased car. It is rounded down to the full EUR 100; a car phone and a second set of tyres are left out. The full monthly amounts apply even if the car is available for only part of the month or not used (R 8.1(9) no. 1 sentences 4 and 6 LStR).
- **Commute.** If the car can also be used between home and the first place of work, add 0.03% of the list price per km of one-way distance each month (§ 8(2) sentence 3 EStG). The tax authority accepts, instead, 0.002% per km for each actual commuting day, for at most 180 days a year, if the employee declares the dates each month in writing; the employer keeps the declarations with the payroll records (BMF letter of 3 March 2022, BStBl I p. 232).
- **Electric and hybrid cars.** For a zero-emission electric car bought from 2019 to 2030 with a gross list price not over the cap, only a quarter of the list price is used. The cap is EUR 100,000 for cars bought after 30 June 2025, EUR 70,000 for cars bought in 2024 up to 30 June 2025, and EUR 60,000 for cars bought from 2019 to 2023. Above the cap, and for qualifying plug-in hybrids, half the list price is used. A plug-in hybrid bought from 2025 to 2030 qualifies with at most 50 g CO2/km or at least 80 km of electric range; one bought from 2022 to 2024 needs 50 g or 60 km; one bought from 2019 to 2021 needs 50 g or 40 km (§ 6(1) no. 4 sentence 2 nos. 2 to 5 EStG; BMF letter of 5 November 2021, BStBl I p. 2205). The quarter or half is applied first, then the result is rounded down to the full EUR 100 (same letter, Rn. 12). The reduced list price also drives the 0.03% and 0.002% amounts, because those rules refer to the same list price.
- **Logbook method.** Instead, the benefit can be the share of total car costs that falls on private and commuting trips, if the total costs are shown by receipts and the split by a proper logbook (Fahrtenbuch) (§ 8(2) sentence 4 EStG). For qualifying electric and hybrid cars the purchase cost (or similar cost) enters total costs at a quarter or a half (§ 6(1) no. 4 sentence 3 EStG).
- **User charges.** A fixed or per-km charge the employee pays reduces the benefit, down to zero but not below. Giving up cash pay in a salary sacrifice is not a user charge (BMF letter of 3 March 2022).
- **Charging and bikes.** Charging an electric or hybrid car at the employer's site, and lending a charger for private use, is tax-free if given on top of pay owed (§ 3 no. 46 EStG; applies to periods ending before 1 January 2031 under § 52(4) sentence 21). Lending a bicycle that is not a motor vehicle is tax-free on the same condition (§ 3 no. 37 EStG; also for pay periods ending before 1 January 2031 under § 52(4) sentence 12).

**Meals and lodging.** Meals and lodging use the SvEV values for both tax and contributions (§ 8(2) sentences 6 and 7 EStG). For 2026: EUR 345 a month for full board, EUR 2.37 per breakfast and EUR 4.57 per lunch or dinner, EUR 285 a month for lodging (§ 2 SvEV). The taxable amount is the official value less what the employee pays. Canteen meals, and meals on business trips valued at the official value, can be taxed at a 25% flat rate (§ 40(2) sentence 1 nos. 1 and 1a EStG). A trip meal costing up to EUR 60 is not taxed at all where the employee could claim the travel meal allowance (§ 8(2) sentences 8 and 9 EStG). Travel meal allowances paid above the tax-free flat rates can be taxed at 25% up to the same amount again (§ 40(2) sentence 1 no. 4 EStG).

**Flat taxes.**
- **§ 37b, 30%.** The employer may pay 30% income tax on all non-cash benefits granted in a business year on top of pay owed (to employees) or on top of the agreed service (to customers and business partners). The base is the employer's cost including VAT. Costs per recipient a year count only up to EUR 10,000; the excess is taxed normally. A single gift costing more than EUR 10,000 is excluded in full (§ 37b(1) sentence 3 EStG; BMF letter of 19 May 2015, Rn. 21). It does not apply to company cars, official meal values, staff discounts, items under § 40(2) or shares (§ 37b(2) sentence 2). The choice is made once for the business year, but separately for third parties and for own employees; for own employees the calendar year counts (BMF letter of 19 May 2015, BStBl I p. 468, Rn. 4). Items costing up to EUR 10 are treated as promotional giveaways and can be left out (same letter). The recipient is told the tax was paid and leaves the item out of income (§ 37b(3) EStG). For own employees the item stays subject to contributions: only gifts to third parties' employees are excluded from pay for social insurance (§ 1(1) no. 14 SvEV).
- **§ 40(2), 25% and 15%.** Canteen meals, trip meals, staff events beyond the EUR 110 allowance, recreation grants within the limits, data-processing devices and internet subsidies, chargers and bikes given outright: 25%. Commuting subsidies and the car commute benefit, up to what the employee could claim as commuting costs: 15%. Public transport benefits can also be taxed at 25% instead of being tax-free, so the employee's commuting deduction is not reduced (§ 40(2) EStG). Items taxed under § 40(2) are free of contributions (§ 1(1) no. 3 SvEV).
- **§ 40(1), average rate.** On application, the tax office can allow a flat rate worked out from the employees' average tax, for one-off payments to a larger number of employees, up to EUR 1,000 per employee a year, or for wage tax collected after an audit (§ 40(1) EStG). The rate is a net rate, since the employer bears the tax.
- **Who bears it.** The employer owes the flat tax. If it is passed on to the employee, the amount passed on is still pay and does not reduce the base. Flat-taxed pay and the flat tax are left out of the employee's own return (§ 40(3) EStG; § 37b(3) applies it). The solidarity surcharge is 5.5% of the flat tax (§§ 3, 4 SolzG). Church tax on flat tax follows state decrees (see Not yet confirmed).

**Tax-free items (on top of pay owed where marked).**
- Public transport between home and work, and local public transport in general, given as a ticket or a subsidy (Jobticket), on top of pay owed. It reduces the employee's commuting deduction (§ 3 no. 15 EStG).
- Care of children not yet of school age in kindergartens or similar, on top of pay owed, with no cap in the law (§ 3 no. 33 EStG).
- Health promotion meeting the SGB V §§ 20 and 20b standards, on top of pay owed, up to EUR 600 a year (§ 3 no. 34 EStG).
- Private use of the employer's computers, phones, accessories and software (§ 3 no. 45 EStG).
- Employee shares in the employer's company up to EUR 2,000 a year if open to all staff with one year's service (§ 3 no. 39 EStG). For companies founded not more than 20 years ago and within twice the EU SME turnover and balance-sheet limits and four times the headcount limit (now or in any of the six previous years), the rest of the benefit can be deferred until sale, 15 years, or leaving the employer (§ 19a(1), (3), (4) EStG). The 15-year and leaving triggers do not apply if the employer declares irrevocably, by the next wage tax return, that it will be liable for the tax on a later sale (§ 19a(4a) EStG). Deferred share benefits are still subject to contributions (§ 1(1) no. 1 SvEV).
- Staff events: if open to all staff, costs up to EUR 110 per event and attending employee are not pay, for up to two events a year. The cost is all the employer's costs including VAT, shared over the attendees, and the share of an employee's companions counts as the employee's (§ 19(1) no. 1a EStG). Only the excess is pay, which can be taxed at 25% (§ 40(2) sentence 1 no. 2 EStG).

**Employer pensions (bAV).**
- **Tax.** Employer contributions from the first employment to a Pensionsfonds, Pensionskasse or Direktversicherung are tax-free up to 8% of the pension ceiling: EUR 8,112 in 2026 (§ 3 no. 63 EStG; ceiling from SVBezGrV 2026). This includes amounts the employee converts from pay (Entgeltumwandlung).
- **Contributions.** Only up to 4% of the ceiling, EUR 4,056 in 2026, is free of social insurance, including converted pay (§ 1(1) no. 9 SvEV). The excess over 4% up to 8% is tax-free but contribution-liable.
- **Salary sacrifice.** The employee can demand conversion of up to 4% of the ceiling (§ 1a(1) BetrAVG). The employer must add 15% of the converted amount to the pension vehicle as far as it saves contributions by the conversion (§ 1a(1a) BetrAVG). For pay above the ceilings the saving, and so the top-up, can be smaller or nil.
- **Low-earner subsidy (§ 100).** If the employee's current pay is not over EUR 2,575 a month (EUR 30,900 a year) when the contribution is made, and the employer pays at least EUR 240 a year on top of pay owed, the employer deducts 30% of that contribution, at most EUR 288, from the wage tax it pays over. The employer contribution under § 100 is tax-free up to EUR 960 a year, in addition to § 3 no. 63 (§ 100 EStG).
- **Old contracts.** Unfunded Pensionskasse contributions are tax-free up to 4% of the ceiling, less § 3 no. 63 amounts (§ 3 no. 56 EStG), and can be flat-taxed at 20% up to EUR 1,752 a year (§ 40b EStG). Direktversicherung and Pensionskasse contracts where at least one contribution was flat-taxed under the pre-2005 § 40b before 1 January 2018 keep that 20% flat tax, and those amounts reduce the § 3 no. 63 limit (§ 52(4) sentence 23 and § 52(40) EStG).
- **Direct promise and Unterstützungskasse.** Converted pay used for these routes stays out of contributions only up to 4% of the pension ceiling (§ 14(1) sentence 2 SGB IV). Their wage tax treatment is not covered here.
- **From 2027.** The § 100 subsidy rises to at most EUR 360, the tax-free amount to EUR 1,200, and the pay limit becomes 3% of the monthly pension ceiling (Zweites Betriebsrentenstärkungsgesetz, BGBl. 2026 I No. 14, in force 1 January 2027 under art. 18(4)). For 2026 the figures above apply.

**Managing directors (Gesellschafter-Geschäftsführer).**
- **The test.** Employment is non-self-employed work, especially in an employment relationship; the signs are working under instructions and being integrated into the organisation (§ 7(1) SGB IV).
- **The share rule.** A managing director with no share in the capital is always employed. The Federal Social Court holds that a shareholder managing director is self-employed by reason of the shareholding only with at least 50% of the share capital, or, with less, a "real" blocking minority in the articles that covers all company business, not just listed matters. Agreements outside the articles (voting pacts, options) do not count (BSG, 14 March 2018, B 12 KR 13/17 R). On 23 July 2026 the court held that two 50% shareholder directors were employed because a casting-vote clause in the articles meant neither could always block resolutions (BSG, B 12 BA 10/24 R, hearing report).
- **Status procedure.** Either party can ask Deutsche Rentenversicherung Bund (DRV Bund) to decide employed or self-employed status (§ 7a(1) SGB IV). The collecting health fund must apply itself when the employer's registration shows the person is the employer's spouse, partner or descendant, or a managing shareholder of a GmbH (§ 7a(1) sentence 2 SGB IV); the registration under § 28a SGB IV carries this flag. Other insurers are bound by the DRV decision (§ 7a(2) SGB IV).
- **Effect.** If the decision is "self-employed", the director's pay is still wage income for wage tax, but no social insurance is due.

## Deadlines and filing

- **Through the payroll.** Benefits are pay of the period they are given in. Wage tax and contributions on them are filed and paid with the normal monthly run: the wage tax return (Lohnsteuer-Anmeldung) by the 10th after the period, contributions by the third-last bank working day of the month. Dates and penalties for the run: [de-payroll](de-payroll.md).
- **Flat taxes.** The § 40 and § 40b flat taxes are declared in the wage tax return; the choice to flat-tax is made by filing a return that shows the flat tax, or, for an audited period, by a declaration to the tax office until the audit assessments are final (§ 40(4) EStG; § 40b(5)). The § 37b tax counts as wage tax, goes in the wage tax return of the employer's payroll office, and is due by the 10th after the return period (§ 37b(4) EStG).
- **§ 100 subsidy.** Taken by deducting it in the next wage tax return (§ 100(1) EStG).
- **§ 19a deferral.** Applied in payroll only with the employee's consent; it cannot be claimed later in the employee's return. The employer records the untaxed value in the payroll account (§ 19a(2), (6) EStG).
- **Status procedure.** Apply to DRV Bund in writing or electronically (§ 7a(1) SGB IV). If the application is made within one month of the work starting and employment is found, insurance starts only on the day the decision is notified, if the worker agrees and had comparable health and pension cover in between (§ 7a(5) SGB IV). Contributions then fall due only when the decision is final. An objection or claim against the decision delays its effect (§ 7a(6) SGB IV). A decision before work starts is possible on application (§ 7a(4a) SGB IV; this rule runs until 30 June 2027 under § 7a(7)).

## Penalties and interest

- **Employer liability.** The employer is liable for wage tax it should have withheld on a benefit (§ 42d(1) EStG). Tax collected after an audit for many employees can be flat-taxed at a net rate under § 40(1) no. 2 EStG, which raises the cost.
- **Late payment.** 1% of the tax due, rounded down to a multiple of EUR 50, for each month started (§ 240(1) AO). Late contributions: 1% a month on arrears rounded down to EUR 50 (§ 24(1) SGB IV). Details in [de-payroll](de-payroll.md).
- **Lost contribution-free treatment.** Items that are only contribution-free when left tax-free or flat-taxed in the period's payroll become contribution-liable if the payroll misses that (§ 1(1) last sentences SvEV).
- **Managing directors.** If a director treated as self-employed is later found employed, contributions are due for the whole period, subject to limitation; the status procedure is the protection against this (§ 7a SGB IV). The July 2026 BSG case shows the size: EUR 127,833.77 in contributions and levies claimed after an audit.

## Cross-border points

- **Tax.** Benefits are part of employment income and follow the same rules as cash pay for German wage tax and for treaty allocation; see [de-non-resident-tax](de-non-resident-tax.md) and [de-payroll](de-payroll.md).
- **§ 37b and foreign givers.** A foreign business that opts for § 37b must flat-tax uniformly all gifts to recipients taxable in Germany (BMF letter of 19 May 2015).
- **Company cars.** The list price is the German domestic list price (§ 6(1) no. 4 sentence 2 EStG), also for cars bought abroad.
- **bAV.** § 3 no. 63 applies only to contributions from the first employment; the § 100 subsidy needs the pay to be subject to German wage tax in that period (§ 100(3) no. 1 EStG).
- **Social insurance.** Workers posted to or from Germany under an A1 certificate stay in their home system; benefits are then contribution-free in Germany. The status test for directors applies only where German social insurance law applies.

## Worked examples

**Example 1: company car, combustion versus electric.** An employee has a company car for private use and the commute. One-way distance 18 km. Option A: a petrol car with a gross list price of EUR 48,700. Option B: a fully electric car bought in February 2026 with a gross list price of EUR 64,050 (under the EUR 100,000 cap, so a quarter applies), and the employee pays a user charge of EUR 50 a month.

Option A: 1% of 48,700 is EUR 487.00; 0.03% x 18 km x 48,700 is EUR 262.98; monthly benefit EUR 749.98. Option B: a quarter of 64,050 is EUR 16,012.50, rounded down to the full EUR 100: EUR 16,000. 1% is EUR 160.00; 0.03% x 18 x 16,000 is EUR 86.40; total EUR 246.40; less the user charge of EUR 50, taxable benefit EUR 196.40 a month. The benefit is added to gross pay for wage tax and contributions.

```oa-check
name: DE 2026 company car, petrol vs electric, 18 km commute
inputs:
  list_petrol: 48700
  list_ev: 64050
  km: 18
  user_charge: 50
steps:
  - petrol_private: list_petrol * 0.01
  - petrol_commute: list_petrol * 0.0003 * km
  - petrol_total: petrol_private + petrol_commute
  - ev_base: floor(list_ev / 4 / 100) * 100
  - ev_private: ev_base * 0.01
  - ev_commute: ev_base * 0.0003 * km
  - ev_total: ev_private + ev_commute
  - ev_taxable: max(0, ev_total - user_charge)
expected:
  petrol_total: 749.98
  ev_base: 16000
  ev_total: 246.40
  ev_taxable: 196.40
```

**Example 2: salary sacrifice inside the 4% line, plus canteen lunches.** Pay EUR 4,000 a month, under all ceilings. The employee converts EUR 290 a month into a Direktversicherung. Because the conversion saves contributions, the employer adds 15%, EUR 43.50. Total contributions EUR 333.50 a month, EUR 4,002 a year. All of it is tax-free (under EUR 8,112) and contribution-free (under EUR 4,056), leaving EUR 54 of contribution-free room. Anything above EUR 4,056 would be tax-free but subject to contributions, and the 15% top-up is owed only as far as the employer actually saves contributions. The employee also takes 20 canteen lunches a month and pays EUR 2.50 for each. The 2026 value is EUR 4.57 (137 / 30 rounded to the cent), so the benefit is EUR 2.07 a lunch, EUR 41.40 a month. The employer flat-taxes it at 25% (EUR 10.35) plus 5.5% solidarity surcharge (EUR 0.56, fractions of a cent dropped), and the meals are then free of contributions.

```oa-check
name: DE 2026 bAV salary sacrifice 290 a month with 15% top-up, plus canteen lunches
inputs:
  sacrifice_month: 290
  ceiling: 101400
  lunches: 20
  paid_per_lunch: 2.50
  lunch_month_value: 137
steps:
  - topup_month: sacrifice_month * 0.15
  - total_year: (sacrifice_month + topup_month) * 12
  - tax_free_cap: ceiling * 0.08
  - sv_free_cap: ceiling * 0.04
  - tax_free: min(total_year, tax_free_cap)
  - sv_free: min(total_year, sv_free_cap)
  - sv_liable: total_year - sv_free
  - lunch_value: round(lunch_month_value / 30, 2)
  - meal_benefit: (lunch_value - paid_per_lunch) * lunches
  - flat_tax: meal_benefit * 0.25
  - soli: floor(flat_tax * 0.055 * 100) / 100
expected:
  total_year: 4002
  tax_free: 4002
  sv_free: 4002
  sv_liable: 0
  lunch_value: 4.57
  meal_benefit: 41.40
  flat_tax: 10.35
  soli: 0.56
```

## Ask the client first

1. For each car: gross list price at first registration, purchase date, drive type (petrol or diesel, electric, plug-in hybrid with CO2 and electric range from the certificate of conformity), commute distance, and whether a logbook is kept.
2. Is each benefit given on top of pay already owed, or does it replace pay (salary sacrifice)? This decides the EUR 50 limit for vouchers and most tax-free items.
3. Which benefits have been flat-taxed so far in the year, and has the business already chosen § 37b for employees or for third parties this business year?
4. For employer pensions: the vehicle (Direktversicherung, Pensionskasse, Pensionsfonds, Unterstützungskasse, direct promise), employer and converted amounts, and whether this is the employee's first employment.
5. For each managing director: share of capital, voting rules and any casting-vote or blocking clause in the articles, and whether a DRV status decision exists.
6. Church membership of employees, if flat taxes are used (church tax on flat tax).

## Sources

| Source | URL | Read on |
|---|---|---|
| EStG § 3 (nos. 15, 33, 34, 37, 39, 45, 46, 56, 63) | https://www.gesetze-im-internet.de/estg/__3.html | 2026-10-24 |
| EStG § 6(1) no. 4 (list price, electric and hybrid rates, logbook) | https://www.gesetze-im-internet.de/estg/__6.html | 2026-10-24 |
| EStG § 8 (benefits in kind, company car, EUR 50 limit, staff discount) | https://www.gesetze-im-internet.de/estg/__8.html | 2026-10-24 |
| EStG § 19 (staff events) and § 19a (employee shares) | https://www.gesetze-im-internet.de/estg/__19a.html | 2026-10-24 |
| EStG § 37b (30% flat tax) | https://www.gesetze-im-internet.de/estg/__37b.html | 2026-10-24 |
| EStG § 40 (flat taxes) | https://www.gesetze-im-internet.de/estg/__40.html | 2026-10-24 |
| EStG § 40b (Pensionskasse flat tax) | https://www.gesetze-im-internet.de/estg/__40b.html | 2026-10-24 |
| EStG § 52 (application dates, car price caps, § 3 no. 46) | https://www.gesetze-im-internet.de/estg/__52.html | 2026-10-24 |
| EStG § 100 (bAV subsidy) | https://www.gesetze-im-internet.de/estg/__100.html | 2026-10-24 |
| Wachstumschancengesetz, BGBl. 2024 I No. 108, art. 3 (EUR 70,000 cap) | https://www.recht.bund.de/bgbl/1/2024/108/VO.html | 2026-10-24 |
| Zweites Betriebsrentenstärkungsgesetz, BGBl. 2026 I No. 14, art. 2 and 18 (§ 100 changes from 2027) | https://www.recht.bund.de/bgbl/1/2026/14/VO.html | 2026-10-24 |
| R 8.1(9) LStR 2023 (company car list price rounding, part months; Lohnsteuer-Handbuch 2026) | https://lsth.bundesfinanzministerium.de/lsth/2026/A-Einkommensteuergesetz/II-Einkommen-2-24b/4-Ueberschuss-d-Einnahmen-ueber-die-Werbungsk-8-9a/Paragraf-8/r-8-1-9.html | 2026-10-24 |
| BMF letter of 5 November 2021 on electric and hybrid cars, BStBl I p. 2205 (Lohnsteuer-Handbuch 2026, annex 24 IV.6) | https://lsth.bundesfinanzministerium.de/lsth/2026/B-Anhaenge/Anhang-24/IV/IV-6/anhang-24-IV-6.html | 2026-10-24 |
| SGB IV § 14 (salary sacrifice into direct promise or Unterstützungskasse) | https://www.gesetze-im-internet.de/sgb_4/__14.html | 2026-10-24 |
| SvEV §§ 1, 2, 3 (2026 meal and lodging values; contribution-free items) | https://www.gesetze-im-internet.de/svev/ | 2026-10-24 |
| SVBezGrV 2026, BGBl. 2025 I No. 278 (pension ceiling EUR 101,400) | https://www.recht.bund.de/bgbl/1/2025/278/regelungstext.pdf?__blob=publicationFile&v=3 | 2026-10-24 |
| BetrAVG § 1a (salary sacrifice, 15% top-up) | https://www.gesetze-im-internet.de/betravg/__1a.html | 2026-10-24 |
| SGB IV §§ 7, 7a (employment, status procedure) | https://www.gesetze-im-internet.de/sgb_4/__7a.html | 2026-10-24 |
| SolzG §§ 3, 4 | https://www.gesetze-im-internet.de/solzg_1995/__4.html | 2026-10-24 |
| AO § 240; SGB IV § 24; EStG § 42d | https://www.gesetze-im-internet.de/ao_1977/__240.html | 2026-10-24 |
| BMF letter of 3 March 2022 on company cars for employees (Lohnsteuer-Handbuch 2026, annex 24 IV.1) | https://lsth.bundesfinanzministerium.de/lsth/2026/B-Anhaenge/Anhang-24/IV/IV-1/anhang-24-IV-1.html | 2026-10-24 |
| BMF letter of 19 May 2015 on § 37b, amended 28 June 2018 (Lohnsteuer-Handbuch 2026, annex 23a) | https://lsth.bundesfinanzministerium.de/lsth/2026/B-Anhaenge/Anhang-23a/inhalt.html | 2026-10-24 |
| Federal Social Court, 14 March 2018, B 12 KR 13/17 R | https://www.bsg.bund.de/SharedDocs/Entscheidungen/DE/2018/2018_03_14_B_12_KR_13_17_R.html | 2026-10-24 |
| Federal Social Court, 23 July 2026, B 12 BA 10/24 R (hearing report) | https://www.bsg.bund.de/SharedDocs/Verhandlungen/DE/2026/2026_07_23_B_12_BA_10_24_R.html | 2026-10-24 |

Not yet confirmed: the administrative car rules in R 8.1(9) LStR beyond the list-price rounding and part-month rule; the EUR 60 meal limit and staff-event rules in the wage tax guidelines beyond the statute; church tax rates on flat taxes (for § 37b the BMF letter, Rn. 36, points to the state decrees of 28 and 29 December 2006; the rates themselves were not read); whether a collective agreement can set aside the 15% top-up; whether a bAV top-up is owed where pay exceeds the ceilings (depends on the saving actually made); the written reasons of the 23 July 2026 BSG decision (only the hearing report was read); the wage tax treatment of the Unterstützungskasse and direct-promise routes of bAV, which is not covered here.

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
