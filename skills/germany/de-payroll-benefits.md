---
name: de-payroll-benefits
description: "German payroll benefits for 2026: how an employer values and taxes benefits in kind on the payslip. Covers the EUR 50 monthly limit for benefits in kind and vouchers, company cars (1% rule, 0.03% commute charge, a quarter or a half of the list price for electric and plug-in hybrid cars, the EUR 100,000 price cap, the logbook method, user charges), meals and lodging at the 2026 official values, the 30% flat tax of § 37b EStG and the 15%, 20% and 25% flat taxes of §§ 40 and 40b, tax-free items (public transport tickets, childcare, health promotion, bikes, charging, devices, employee shares), employer pensions (8% and 4% limits, the § 100 subsidy, salary sacrifice and the 15% top-up), and the social insurance status of managing directors with the DRV status procedure. Trigger on: Sachbezug, geldwerter Vorteil, Dienstwagen, 1%-Regelung, Fahrtenbuch, Sachbezugswerte 2026, 37b, Pauschalsteuer, Jobticket, bAV, Entgeltumwandlung, Gesellschafter-Geschäftsführer, Statusfeststellung. Out of scope: the wage tax and contribution run itself (de-payroll), the employee's annual return (de-employee-income-tax), self-employed contributions (de-social-contributions)."
version: 0.6
jurisdiction: DE
tax_year: 2026
last_updated: 2026-11-27
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: payroll
type: computation
---

# German payroll benefits 2026: benefits in kind, company cars, flat taxes, employer pensions and managing directors

> **General reference only.** This skill is general tax reference material for AI-assisted work. It has not been reviewed for any specific employer's or employee's facts. A Steuerberater or payroll accountant should confirm the treatment before a real payroll run.

**Sibling skills.** The monthly wage tax and contribution run (tax classes, the 2026 PAP, rates, ceilings, Minijobs, filing and payment dates): [de-payroll](de-payroll.md). The employee's own annual return: [de-employee-income-tax](de-employee-income-tax.md). Contributions of the self-employed: [de-social-contributions](de-social-contributions.md). Non-residents: [de-non-resident-tax](de-non-resident-tax.md).

## Who this applies to

- **In.** Any employer that runs German payroll (wage tax under § 38 EStG) and gives employees anything other than cash pay: goods, services, vouchers, a car, meals, lodging, gifts, event costs, pension contributions. It also covers the employer's choice to pay a flat tax on a benefit instead of taxing it through the employee's tax class.
- **Benefits in kind are pay.** Income includes everything received in money or money's worth (§ 8(1) EStG). Non-cash income is valued at the usual end price at the place of supply, less usual discounts (§ 8(2) sentence 1 EStG), unless a special rule below applies.
- **Social insurance has separate gates.** The social insurance value of a benefit is set by the Sozialversicherungsentgeltverordnung (SvEV). Many tax-free or flat-taxed items are also free of contributions, but only if the payroll leaves them tax-free or flat-taxed in the pay period they belong to (§ 1(1) last sentences SvEV).
- **Managing directors.** Determine wage-tax treatment and social-insurance status separately; do not infer either solely from the job title or share percentage. The employment test and case holds are below.
- **Out.** Gifts to non-employees are in only as far as § 37b EStG lets the giver pay a flat tax on them. Pensions in payment, severance pay and share option plans of listed groups are not covered.

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source URL |
|---|---|---|---|
| Benefits in kind valued at market price: tax-free if the total net benefit is not more than this a month (a cliff, not an allowance); vouchers count only if given on top of pay owed (EStG § 8(2) sentence 11) | EUR 50 a month | 2026 | https://www.gesetze-im-internet.de/estg/__8.html |
| Qualifying staff discount under § 8(3): goods/services not predominantly produced, distributed or provided for staff and not flat-taxed under § 40; applicable public end price less 4%, less employee payment, then remaining annual allowance | 4% markdown; EUR 1,080 a year in aggregate | 2026 | https://www.gesetze-im-internet.de/estg/__8.html |
| Company car, private use (EStG § 8(2) sentence 2 with § 6(1) no. 4 sentence 2) | 1% of the gross list price a month | 2026 | https://www.gesetze-im-internet.de/estg/__6.html |
| Company car, home to first place of work (EStG § 8(2) sentence 3) | 0.03% of the list price per km of one-way distance a month | 2026 | https://www.gesetze-im-internet.de/estg/__8.html |
| Company car, home trips in a double household for which the deduction specified in § 9(1) no. 5 sentences 5 and 6 would not be available; the deductible-trip exception and corresponding logbook alternative apply (EStG § 8(2) sentence 5) | 0.002% of the list price per km per trip | 2026 | https://www.gesetze-im-internet.de/estg/__8.html |
| Electric car with zero CO2, bought 1 Jan 2019 to 31 Dec 2030, gross list price not over the cap: list price counted at (EStG § 6(1) no. 4 sentence 2 no. 3) | one quarter | 2026 | https://www.gesetze-im-internet.de/estg/__6.html |
| Price cap for the quarter rate: cars bought after 30 June 2025 (EStG § 6(1) no. 4 sentence 2 no. 3; § 52(12) sentence 6) | EUR 100,000 | 2026 | https://www.gesetze-im-internet.de/estg/__52.html ; https://www.gesetze-im-internet.de/estg/__6.html |
| Price cap for the quarter rate: cars bought 1 Jan 2024 to 30 June 2025 (Wachstumschancengesetz art. 3; § 52(12) sentence 5) | EUR 70,000 | 2026 | https://www.recht.bund.de/bgbl/1/2024/108/regelungstext.pdf?__blob=publicationFile&v=2 |
| Price cap for the quarter rate: cars bought 1 Jan 2019 to 31 Dec 2023 (EStG § 52(12) sentence 4; BMF letter of 5 November 2021, BStBl I p. 2205, Rn. 11) | EUR 60,000 | 2026 | https://lsth.bundesfinanzministerium.de/lsth/2026/B-Anhaenge/Anhang-24/IV/IV-6/anhang-24-IV-6.html |
| Electric car over the cap, or plug-in hybrid with at most 50 g CO2/km or at least 80 km electric range, bought 1 Jan 2025 to 31 Dec 2030 (EStG § 6(1) no. 4 sentence 2 no. 5) | one half | 2026 | https://www.gesetze-im-internet.de/estg/__6.html |
| Electric car over the cap, or plug-in hybrid with at most 50 g CO2/km or at least 60 km range, bought 1 Jan 2022 to 31 Dec 2024 (EStG § 6(1) no. 4 sentence 2 no. 4) | one half | 2026 | https://www.gesetze-im-internet.de/estg/__6.html |
| Electric car over the cap, or plug-in hybrid with at most 50 g CO2/km or at least 40 km range, bought 1 Jan 2019 to 31 Dec 2021 (EStG § 6(1) no. 4 sentence 2 no. 2 with § 3(2) EmoG; BMF letter of 5 November 2021, Rn. 11) | one half | 2026 | https://www.gesetze-im-internet.de/estg/__6.html |
| List price for the 1%, 0.03% and 0.002% rules: rounded down to the full EUR 100, after any quarter or half is applied (R 8.1(9) no. 1 sentence 6 LStR; BMF letter of 5 November 2021, Rn. 12) | full EUR 100 | 2026 | https://lsth.bundesfinanzministerium.de/lsth/2026/A-Einkommensteuergesetz/II-Einkommen-2-24b/4-Ueberschuss-d-Einnahmen-ueber-die-Werbungsk-8-9a/Paragraf-8/r-8-1-9.html |
| Meals provided as benefit in kind, monthly (SvEV § 2(1)) | EUR 345: breakfast 71, lunch 137, dinner 137 | 2026 | https://www.gesetze-im-internet.de/svev/__2.html |
| Single meal (one thirtieth of the monthly value, rounded to the cent, SvEV § 2(6)) | breakfast EUR 2.37; lunch or dinner EUR 4.57 | 2026 | https://www.gesetze-im-internet.de/svev/__2.html |
| Lodging, unreduced full month; apply the statutory reductions/daily rule below (SvEV § 2(3)); exceptional dwelling proxy only where finding local rent presents extraordinary difficulties (SvEV § 2(4)) | EUR 285; EUR 5.01 per m2 (EUR 4.10 basic) | 2026 | https://www.gesetze-im-internet.de/svev/__2.html |
| Meal on a business trip valued at the official value if its price is not over (EStG § 8(2) sentence 8) | EUR 60 | 2026 | https://www.gesetze-im-internet.de/estg/__8.html |
| Employer-provided flat: no benefit if the rent paid is at least two thirds of local rent and local rent is not over (EStG § 8(2) sentence 12) | EUR 25 per m2 | 2026 | https://www.gesetze-im-internet.de/estg/__8.html |
| Flat tax on non-cash gifts and incentives (EStG § 37b(1), (2)); capped at EUR 10,000 per recipient a year, excluded for a single gift over EUR 10,000 | 30% | 2026 | https://www.gesetze-im-internet.de/estg/__37b.html |
| Subject to the precise gates below: flat tax on canteen meals, trip meals, staff events, recreation grants, devices, chargers, bikes given outright (EStG § 40(2) sentence 1) | 25% | 2026 | https://www.gesetze-im-internet.de/estg/__40.html |
| Recreation grants, flat tax limit a year (EStG § 40(2) sentence 1 no. 3) | EUR 156 employee, EUR 104 spouse, EUR 52 per child | 2026 | https://www.gesetze-im-internet.de/estg/__40.html |
| Commuting subsidies or car commute benefit (EStG § 40(2) sentence 2 no. 1); public transport instead of tax-free (no. 2) | 15%; 25% | 2026 | https://www.gesetze-im-internet.de/estg/__40.html |
| Flat tax on a larger number of one-off payments at an average rate, on application; excluded above (EStG § 40(1)) | EUR 1,000 per employee a year | 2026 | https://www.gesetze-im-internet.de/estg/__40.html |
| Staff event: allowance per event and attending employee (companions' share included), for up to two events a year, if open to all staff of the business or a business unit (EStG § 19(1) no. 1a) | EUR 110 | 2026 | https://www.gesetze-im-internet.de/estg/__19.html |
| Solidarity surcharge on flat wage tax (SolzG §§ 3, 4) | 5.5% | 2026 | https://www.gesetze-im-internet.de/solzg_1995/__4.html |
| Tax-free: health promotion meeting SGB V §§ 20, 20b (EStG § 3 no. 34) | EUR 600 a year | 2026 | https://www.gesetze-im-internet.de/estg/__3.html |
| Tax-free: qualifying employee holdings under the instrument and offer gates below (EStG § 3 no. 39) | EUR 2,000 a year | 2026 | https://www.gesetze-im-internet.de/estg/__3.html |
| Pension ceiling (general pension insurance), base for the bAV limits (SVBezGrV 2026 § 4(1) no. 1) | EUR 101,400 a year | 2026 | https://www.recht.bund.de/bgbl/1/2025/278/regelungstext.pdf?__blob=publicationFile&v=3 |
| bAV: qualifying ordinary annual first-employment contributions, subject to the payout/election and special-route conditions below; employer contributions to Pensionsfonds, Pensionskasse or Direktversicherung tax-free (EStG § 3 no. 63) | 8% × EUR 101,400 = EUR 8,112 (computed) | 2026 | https://www.gesetze-im-internet.de/estg/__3.html ; https://www.recht.bund.de/bgbl/1/2025/278/regelungstext.pdf?__blob=publicationFile&v=3 |
| bAV: aggregate contribution-free part, including qualifying § 100(6) contributions (SvEV § 1(1) no. 9) | 4% × EUR 101,400 = EUR 4,056 (computed) | 2026 | https://www.gesetze-im-internet.de/svev/__1.html ; https://www.recht.bund.de/bgbl/1/2025/278/regelungstext.pdf?__blob=publicationFile&v=3 |
| bAV subsidy for low earners: 30% of the employer's extra contribution of at least EUR 240, capped (EStG § 100(2), (3)) | max EUR 288 a year | 2026 | https://www.gesetze-im-internet.de/estg/__100.html |
| § 100 pay limit at the time of the contribution (EStG § 100(3) no. 3) | EUR 2,575 a month; EUR 30,900 a year | 2026 | https://www.gesetze-im-internet.de/estg/__100.html |
| § 100 contribution tax-free up to (EStG § 100(6)) | EUR 960 a year | 2026 | https://www.gesetze-im-internet.de/estg/__100.html |
| § 100 from 1 January 2027: subsidy max EUR 360, tax-free up to EUR 1,200, monthly-pay-period limit 3% of the annual pension ceiling (Zweites Betriebsrentenstärkungsgesetz, BGBl. 2026 I No. 14, art. 2 no. 2, art. 18(4)) | EUR 360; EUR 1,200 | 2027 | https://www.recht.bund.de/bgbl/1/2026/14/regelungstext.pdf?__blob=publicationFile&v=2 |
| Salary sacrifice: statutory default subject to collective agreements; employee right up to 4% of the ceiling; employer top-up where it saves contributions (BetrAVG § 1a(1), (1a)) | 4% × EUR 101,400 = EUR 4,056 (computed); top-up 15% | 2026 | https://www.gesetze-im-internet.de/betravg/__1a.html ; https://www.gesetze-im-internet.de/betravg/__19.html ; https://www.recht.bund.de/bgbl/1/2025/278/regelungstext.pdf?__blob=publicationFile&v=3 |

## The taxable base

**The EUR 50 limit.** Benefits valued at market price under § 8(2) sentence 1 EStG stay out of pay if the total net benefit in the month is not over EUR 50. It is a cliff: at EUR 50.01 the whole amount is taxable. Benefits valued by a special rule (company car, official meal values, staff discounts under § 8(3)) do not count toward it and cannot use it. Cash reimbursements, earmarked cash and money substitutes are cash income. Vouchers/cards are non-cash only if exclusively exchangeable for goods/services and meeting § 2(1) no. 10 ZAG; the monthly exemption additionally requires them to be given on top of pay owed (§ 8(1), (2) EStG). "On top of pay owed" means no offset against pay, no pay cut in exchange, not instead of an agreed raise, and no pay rise if the benefit stops (§ 8(4) EStG). SvEV § 3(1) also applies the EUR 50 monthly cliff for contribution valuation.

**Qualifying staff discounts.** Under § 8(3), use the end price offered to unrelated final consumers in ordinary commerce by the employer or the customer nearest the place of supply, reduced by 4%. The goods/services must not be predominantly produced, distributed or provided for employees and must not be taxed under § 40. Subtract the employee's payment, then the unused part of the EUR 1,080 annual allowance for benefits from that employment: taxable benefit = max(0, 96% of that applicable public end price − employee payment − remaining annual allowance). Track annual aggregation; do not also use the monthly EUR 50 cliff. At public price EUR 2,000/payment EUR 500, benefit before allowance is EUR 1,420; with the full annual allowance remaining, taxable benefit is EUR 340.

**Company cars.** For a purchased car the acquisition date selects the cohort below. For leasing or first employee provision, establish the relevant date under the BMF letter of 5 November 2021, Rn. 21–22; a change of driver does not by itself start a new cohort. If those dates differ, do not select the cheaper cohort from the acquisition date alone. Check this point with one of our partner accountants.
- **1% rule.** Private use is 1% of the domestic gross list price at first registration, plus factory extras, including VAT, each month (§ 6(1) no. 4 sentence 2 with § 8(2) sentence 2 EStG). The list price is used even for a used or leased car. It is rounded down to the full EUR 100; a car phone and a second set of tyres are left out. The full monthly amounts apply even if the car is available for only part of the month or not used (R 8.1(9) no. 1 sentences 4 and 6 LStR).
- **Commute.** If the car can also be used between home and the first place of work, add 0.03% of the list price per km of one-way distance each month (§ 8(2) sentence 3 EStG). The tax authority accepts, instead, 0.002% per km for each actual commuting day, for at most 180 days a year, if the employee declares the actual dates, vehicle by vehicle, each month in writing; the employer keeps the declarations with the payroll records. Count a day only once; the 180-day annual limit is shared across all employer cars, with no 15-day monthly cap. Choose the monthly or individual commute method consistently for the calendar year; a whole-year correction remains possible before the wage certificate is issued (BMF letter of 3 March 2022, BStBl I p. 232).
- **Electric and hybrid cars.** For a zero-emission electric car bought from 2019 to 2030 with a gross list price not over the cap, only a quarter of the list price is used. The cap is EUR 100,000 for cars bought after 30 June 2025, EUR 70,000 for cars bought in 2024 up to 30 June 2025, and EUR 60,000 for cars bought from 2019 to 2023. Above the cap, and for qualifying plug-in hybrids, half the list price is used. A plug-in hybrid bought from 2025 to 2030 qualifies with at most 50 g CO2/km or at least 80 km of electric range; one bought from 2022 to 2024 needs 50 g or 60 km; one bought from 2019 to 2021 needs 50 g or 40 km (§ 6(1) no. 4 sentence 2 nos. 2 to 5 EStG; BMF letter of 5 November 2021, BStBl I p. 2205). The quarter or half is applied first, then the result is rounded down to the full EUR 100 (same letter, Rn. 12). The reduced list price also drives the 0.03% and 0.002% amounts, because those rules refer to the same list price.
- **Logbook method.** Instead, the benefit can be the share of total car costs that falls on private and commuting trips, if the total costs are shown by receipts and the split by a proper logbook (Fahrtenbuch) (§ 8(2) sentence 4 EStG). For qualifying electric/hybrid cars, reduce the depreciation basis or comparable acquisition/lease costs by the applicable fraction, not all running costs (§ 6(1) no. 4 sentence 3 EStG; BMF letter of 5 November 2021, Rn. 15–18). Choose the valuation method for the calendar year and car; no in-year switch, subject to a permitted whole-year payroll correction before the wage certificate is issued (R 8.1(9) no. 3 LStR).
- **User charges.** A fixed or per-km charge the employee pays reduces the benefit, down to zero but not below. Giving up cash pay in a salary sacrifice is not a user charge (BMF letter of 3 March 2022).
- **Charging and bikes.** Charging an electric or hybrid car at a fixed business facility of the employer or an affiliated company, and lending a charger for private use, is tax-free if given on top of pay owed (§ 3 no. 46 EStG; applies to periods ending before 1 January 2031 under § 52(4) sentence 21). Lending a bicycle that is not a motor vehicle is tax-free on the same condition (§ 3 no. 37 EStG; also for pay periods ending before 1 January 2031 under § 52(4) sentence 12).

**Meals and lodging.** Meals and lodging use the SvEV values for both tax and contributions (§ 8(2) sentences 6 and 7 EStG). For 2026: EUR 345 a month for full board, EUR 2.37 per breakfast and EUR 4.57 per lunch or dinner, EUR 285 a month for lodging (§ 2 SvEV). The taxable amount is the official value less what the employee pays. Canteen meals, and meals on business trips valued at the official value, can be taxed at a 25% flat rate (§ 40(2) sentence 1 nos. 1 and 1a EStG). A trip meal costing up to EUR 60 is not taxed at all where the employee could claim the travel meal allowance (§ 8(2) sentences 8 and 9 EStG). Travel meal allowances paid above the tax-free flat rates can be taxed at 25% up to the same amount again (§ 40(2) sentence 1 no. 4 EStG). Lodging is distinct from a dwelling. Apply each relevant § 2(3) reduction to the EUR 285 lodging value: 15% for admission to the employer's household or community lodging; 15% for under-18s or apprentices; and 40% for two employees sharing, 50% for three, or 60% for more than three. Two otherwise ordinary adult occupants give EUR 171 each for a full month before payments. Where the ordinary lodging value is inequitable in the actual case, use the statutory local-rent alternative. A dwelling normally uses local rent, taking account of impairment from its location relative to the business and applicable statutory rent limits, with § 8(2) sentence 12 EStG applied correspondingly. Only if local rent is extraordinarily difficult to establish may the statutory EUR 5.01/m² monthly proxy apply, or EUR 4.10/m² for basic equipment without central heating or without a bath/shower. Value energy, water and other ancillary costs at the usual local price. For shorter periods use 1/30 per day, applying the relevant percentage reductions to the daily value; perform calculations at two decimal places, rounding up where the third digit is 5–9 (§ 2(3)–(6) SvEV).

**Flat taxes.**
- **§ 37b, 30%.** For benefits that give the recipient taxable income in Germany (not tax-exempt or non-taxable receipts), the employer may pay 30% income tax on qualifying non-cash benefits granted in a business year on top of pay owed (to employees) or on top of the agreed service (to customers and business partners). The base is the giver's cost including VAT; for employees of affiliated companies, it is at least the value under § 8(3) sentence 1 EStG. Costs per recipient a year count only up to EUR 10,000; the excess is taxed normally. A single gift costing more than EUR 10,000 is excluded in full (§ 37b(1) sentence 3 EStG; BMF letter of 19 May 2015, Rn. 21). It does not apply to company cars, official meal values, staff discounts, items under § 40(2) or shares (§ 37b(2) sentence 2). The election is uniform for the relevant year and all domestic payroll establishments, but separate elections are permitted for third parties and own employees; for own employees the calendar year counts (BMF letter of 19 May 2015, BStBl I p. 468, Rn. 4). The EUR 10 promotional-giveaway shortcut, including its VAT-input-tax interaction, is not a usable rule here. Check this point with one of our partner accountants. The recipient is told the tax was paid and leaves the item out of income (§ 37b(3) EStG). For own employees the item stays subject to contributions: the third-party employee exclusion from social-insurance pay applies only where those employees are not employed by a company affiliated with the giver; affiliation does not itself establish a separate identical social assessment (§ 1(1) no. 14 SvEV).
- **§ 40(2), 25% and 15%.** Canteen meals, trip meals, staff events beyond the EUR 110 allowance, recreation grants within the limits, data-processing devices and internet subsidies, chargers and bikes given outright: 25%. Commuting subsidies and the car commute benefit, up to what the employee could claim as commuting costs: 15%. Public transport benefits can also be taxed at 25% instead of being tax-free, so the employee's commuting deduction is not reduced (§ 40(2) EStG). Items taxed under § 40(2) are free of contributions (§ 1(1) no. 3 SvEV). Apply the actual branch conditions: canteen meals must not be agreed wage components; for recreation grants, the employer must ensure recreational use and aggregate the earlier grants in the same year against the employee/spouse/child caps. Transfers of data-processing devices/accessories/internet access, internet-use subsidies, charger transfers/subsidies and outright transfers of non-motor bicycles require additionality to pay already owed. The 15% cash commuting subsidy also requires additionality, and amounts taxed under that 15% route reduce the employee's commuting deduction. The alternative 25% public-transport election instead covers all relevant § 3 no. 15 benefits of that calendar year uniformly, may apply without additionality, and does not reduce the commuting deduction. Staff-event allowance and the stated 25% route require access for all staff of the business or a business unit.
- **§ 40(1), average rate.** On application, the tax office can allow a flat rate worked out from the employees' average tax, for one-off payments to a larger number of employees, up to EUR 1,000 per employee a year, or for wage tax collected after an audit (§ 40(1) EStG). The rate is a net rate, since the employer bears the tax.
- **Who bears it.** The employer owes the flat tax. If it is passed on to the employee, the amount passed on is still pay and does not reduce the base. Flat-taxed pay and the flat tax are left out of the employee's own return (§ 40(3) EStG; § 37b(3) applies it). The solidarity surcharge is 5.5% of the flat tax (§§ 3, 4 SolzG). Church tax on flat tax follows state decrees (see Not yet confirmed).

**Tax-free items (on top of pay owed where marked).**
- Public transport between home and work, and local public transport in general, given as a ticket or a subsidy (Jobticket), on top of pay owed. It reduces the employee's commuting deduction (§ 3 no. 15 EStG).
- Care of children not yet of school age in kindergartens or similar, on top of pay owed, with no cap in the law (§ 3 no. 33 EStG).
- Health promotion meeting the SGB V §§ 20 and 20b standards, on top of pay owed, up to EUR 600 a year (§ 3 no. 34 EStG).
- Private use of business computers/telecommunications devices and accessories, associated services, and system/application software also used in the employer’s business (§ 3 no. 45 EStG).
- Employee shares: qualifying holdings in the employer or a group company, valued at fair value, are exempt up to EUR 2,000 in total per calendar year under § 3 no. 39 EStG. The offer must be open at least to all current employees with a year of uninterrupted service when announced. The instrument must fall within the incorporated § 2(1) no. 1(a), (b), (f)–(l), (2)–(5) 5. VermBG categories; do not assume every option or award qualifies. Check this point with one of our partner accountants for an uncertain instrument.
- **Employee-share deferral hold (§ 19a).** This Guide does not establish eligibility, SME/group thresholds, the age of the company, additionality, employee consent, payroll-only election/records, deferral triggers, employer liability election, reduced-value/buyback treatment or contribution consequences. Preserve the original case: deferred benefit EUR 8,000, later value EUR 5,000, original employee payment EUR 1,000; the arithmetic 5,000 − 1,000 = EUR 4,000 is not an authorised taxable outcome. The historic 15-year/20-year/six-prior-year inputs are not instructions. Check this point with one of our partner accountants.
- Staff events: if open to all staff of the business or a business unit, costs up to EUR 110 per event and attending employee are not pay, for up to two events a year. The cost is all the employer's costs including VAT, shared over the attendees, and the share of an employee's companions counts as the employee's (§ 19(1) no. 1a EStG). Only the excess is pay, which can be taxed at 25% (§ 40(2) sentence 1 no. 2 EStG).

**Employer pensions (bAV).**
- **Tax.** Employer contributions from the first employment to a Pensionsfonds, Pensionskasse or Direktversicherung are tax-free up to 8% of the pension ceiling: EUR 8,112 in 2026 (§ 3 no. 63 EStG; ceiling from SVBezGrV 2026). This includes amounts the employee converts from pay (Entgeltumwandlung). The promised pension/disability/survivor payout must meet § 82(2) sentence 2, and § 3 no. 63 does not apply to the extent the employee has made the § 1a(3) BetrAVG election for § 10a/section XI support. Special termination/catch-up routes are held: the original two-year illustration (101,400 × 4% × 2 = EUR 8,112) is arithmetic only, not an additional entitlement; do not add the ordinary and special routes. Check this point with one of our partner accountants.
- **Contributions.** The aggregate SvEV § 1(1) no. 9 limit covers tax-free ordinary § 3 no. 63 contributions and § 100(6) contributions together: up to 4% of the ceiling, EUR 4,056 in 2026, including converted pay (§ 1(1) no. 9 SvEV). Ordinary qualifying § 3 no. 63 amounts above that limit up to 8% remain tax-free, but this exemption does not remove them from contribution pay; actual contributions still depend on insurance status and ceilings.
- **Salary sacrifice.** The employee can demand conversion of up to 4% of the ceiling (§ 1a(1) BetrAVG). The employer must add 15% of the converted amount to the pension vehicle as far as it saves contributions by the conversion (§ 1a(1a) BetrAVG). For pay above the ceilings the saving, and so the top-up, can be smaller or nil. This is the statutory default: a collective agreement may vary § 1a, including where incorporated for non-tariff-bound parties (BetrAVG § 19). The conversion right requires at least 1/160 of the SGB IV § 18 reference amount annually, is excluded insofar as a conversion-financed pension already exists, and may be implemented in equal monthly amounts if the employer requires it (§ 1a(1), (2)).
- **Low-earner subsidy (§ 100).** If the employee's current pay is not over EUR 2,575 for a monthly pay period or EUR 30,900 for an annual pay period when the contribution is made, and the employer pays at least EUR 240 a year on top of pay owed, the employer deducts 30% of that contribution, at most EUR 288, from the wage tax it pays over. The employer contribution under § 100 is tax-free up to EUR 960 a year, in addition to § 3 no. 63 (§ 100 EStG). This requires the first employment, an eligible Pensionsfonds/Pensionskasse/Direktversicherung with the payout arrangement required by § 82(2) sentence 2, German wage-tax treatment in the contribution period, and the same percentage distribution-cost charge on each contribution (a permitted recalculation cannot exceed the original percentage). Test the pay limit at the contribution date; later changes ordinarily do not alter entitlement. If this employer already made an additional contribution in 2016, cap the subsidy at the amount paid above that 2016 contribution: for qualifying current EUR 700 and 2016 EUR 600, min(EUR 210, EUR 288, EUR 100) gives EUR 100. If a funded entitlement later lapses and money returns to the employer, repay the subsidy to the extent attributable to that repayment by adding it to wage tax in the return for the receipt period (§ 100(1)–(4)).
- **Unfunded/old-contract pension hold.** Do not use the former § 3 no. 56 / § 40b shortcuts as a complete entitlement. First-employment/payout conditions, reductions for § 3 no. 63 amounts, pooled contributions, termination multipliers, the pre-2005 treatment gate (a qualifying flat-taxed contribution before 2018), and the separate SvEV contribution additions require case review. The original EUR 1,752 / EUR 2,148 and 20% figures are identifiers of the held routes, not usable calculations. Check this point with one of our partner accountants.
- **Direct promise / Unterstützungskasse hold.** Neither tax nor social-insurance treatment is established here; do not apply the external pension-vehicle exemptions to these routes. Check this point with one of our partner accountants.
- **From 2027.** The § 100 subsidy rises to at most EUR 360, the tax-free amount to EUR 1,200, and for a monthly pay period the pay limit becomes 3% of the annual pension assessment ceiling (not 3% of its monthly amount); scale that pay limit by 1/30 for daily, 7/30 for weekly, and 12 for annual pay periods (Zweites Betriebsrentenstärkungsgesetz, BGBl. 2026 I No. 14, in force 1 January 2027 under art. 18(4)). For 2026 the figures above apply.

**Managing directors (Gesellschafter-Geschäftsführer).**
- **The test.** Employment is non-self-employed work, especially in an employment relationship; the signs are working under instructions and being integrated into the organisation (§ 7(1) SGB IV).
- **Shareholding/case hold.** No status conclusion follows here for a non-shareholder director, a 50% director, or a minority director with purported blocking rights. Read the actual articles, voting/casting-vote clauses and arrangements. The historical case of two 50% directors, BSG B 12 BA 10/24 R (23 July 2026), and EUR 127,833.77 claimed after audit is retained as an unverified case identifier, not a holding or a liability estimate. The 2018 blocking-minority decision also supplies no automatic answer for this employer. Check this point with one of our partner accountants.
- **Status procedure.** Parties may apply in writing/electronically to DRV Bund under § 7a(1) SGB IV unless a collecting body/insurer has already begun an employment-insurance proceeding. The collecting body must apply where registration identifies the employer's spouse, life partner, descendant or managing shareholder of a GmbH. DRV decides on all circumstances; other insurers are bound for that relationship (§ 7a(2)).
- **Timing/effect hold.** Advance decisions, the one-month application protection, equivalent interim cover/consent, finality of contribution liability, objections, group opinions and the 30 June 2027 sunset require individual review. Neither a self-employed finding nor a pending application establishes a universal social-insurance exemption or a wage-tax classification. Check this point with one of our partner accountants.

## Deadlines and filing

- **Flat taxes.** Exercise the § 40 election in a wage-tax return showing the flat tax; an audited period instead permits a written/electronic declaration before the audit assessments become final (§ 40(4)). § 37b tax is declared as wage tax and paid by the tenth day after the applicable return period (§ 37b(4)); § 100 is deducted separately in the next return (§ 100(1)).
- **Normal payroll and liability hold.** Use [de-payroll](de-payroll.md) for return periods, the ordinary payment timetable and actual contribution calculations. This Guide does not establish the receipt/allocation period of every benefit, an employer-liability exception, audit recovery or the § 40b filing procedure. Check this point with one of our partner accountants.

## Penalties and interest

- Late tax: 1% per started month on the debt rounded down to EUR 50; no default before assessment/declaration, and no surcharge for up to three days' delay except the statutory cash/cheque category (§ 240 AO). Actual relief and dates remain case-specific.
- Late contributions: 1% per started month on arrears rounded down to EUR 50; below EUR 150 do not levy if separately demanded. For a retroactive assessment, exclude the surcharge insofar as the debtor credibly shows no-fault ignorance of the obligation (§ 24 SGB IV).
- SvEV § 1(1)'s listed exemptions require the benefit to be left tax-free or flat-taxed in the payroll for the relevant period; do not assume every tax exemption or every flat tax eliminates contributions.

## Cross-border points

Keep the German domestic list-price basis for car valuation. Before applying any other rule here, establish German tax and social-insurance jurisdiction. Treaty allocation, foreign givers under § 37b, and the direction/validity of an A1 certificate are held for review, including the distinction between German-law outgoing certificates and certificates establishing another state's law. An A1 alone is not an instruction to exempt every benefit. See [de-non-resident-tax](de-non-resident-tax.md) and [de-social-contributions](de-social-contributions.md). Check this point with one of our partner accountants.

## Worked examples

**Example 1: company car, combustion versus electric.** An employee has a company car for private use and the commute, using the monthly method throughout 2026. For this calculation, assume both employer cars were first provided for private use in February 2026; no earlier provision or other special valuation applies. One-way distance 18 km. Option A: a petrol car with a gross list price of EUR 48,700. Option B: a fully electric car bought in February 2026 with a gross list price of EUR 64,050 (under the EUR 100,000 cap, so a quarter applies), and the employee pays a user charge of EUR 50 a month.

Option A: 1% of 48,700 is EUR 487.00; 0.03% x 18 km x 48,700 is EUR 262.98; monthly benefit EUR 749.98. Option B: a quarter of 64,050 is EUR 16,012.50, rounded down to the full EUR 100: EUR 16,000. 1% is EUR 160.00; 0.03% x 18 x 16,000 is EUR 86.40; total EUR 246.40; less the user charge of EUR 50, taxable benefit EUR 196.40 a month. Include the benefit in the applicable wage-tax and contribution bases; this is not a calculation of contributions or net pay.

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

**Example 2: salary sacrifice inside the 4% line, plus canteen lunches.** Pay EUR 4,000 a month, under all ceilings. Assume the ordinary first-employment § 3 no. 63 payout/election conditions are met, no competing § 100 contributions or other contributions use the annual limit, no collective agreement varies the default, and payroll applies the exemptions in the relevant period. The employee converts EUR 290 a month into a Direktversicherung. Assuming the employer saves at least 15% of the converted amount in contributions, the employer adds 15%, EUR 43.50. Total contributions EUR 333.50 a month, EUR 4,002 a year. All of it is tax-free (under EUR 8,112) and contribution-free (under EUR 4,056), leaving EUR 54 of contribution-free room. An otherwise qualifying ordinary § 3 no. 63 contribution above EUR 4,056 but within EUR 8,112 remains in contribution pay, and the 15% top-up is owed only as far as the employer actually saves contributions. The employee also takes 20 canteen lunches a month and pays EUR 2.50 for each. The 2026 value is EUR 4.57 (137 / 30 rounded to the cent), so the benefit is EUR 2.07 a lunch, EUR 41.40 a month. Assume these meals are not agreed wage components. The employer flat-taxes it at 25% (EUR 10.35) plus 5.5% solidarity surcharge (EUR 0.56, fractions of a cent dropped), and the meals are then excluded from contribution pay if flat-taxed with that period’s payroll. Church tax is excluded from this illustration; its actual treatment is held. Check this point with one of our partner accountants.

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
| EStG § 8: market value, cash/cards, cliff, discount, car and meal valuation | https://www.gesetze-im-internet.de/estg/__8.html | 2026-11-27 |
| EStG § 6(1) no. 4: car fractions | https://www.gesetze-im-internet.de/estg/__6.html | 2026-11-27 |
| EStG § 52: operative dates and cohorts | https://www.gesetze-im-internet.de/estg/__52.html | 2026-11-27 |
| Wachstumschancengesetz Article 3: earlier EV cap | https://www.recht.bund.de/bgbl/1/2024/108/regelungstext.pdf?__blob=publicationFile&v=2 | 2026-11-27 |
| BMF: employee company cars, Rn. 13–14 and 52–56 | https://lsth.bundesfinanzministerium.de/lsth/2026/B-Anhaenge/Anhang-24/IV/IV-1/anhang-24-IV-1.html | 2026-11-27 |
| BMF: electric/hybrid fractions, Rn. 11–12, 15–18, 21–22 | https://lsth.bundesfinanzministerium.de/lsth/2026/B-Anhaenge/Anhang-24/IV/IV-6/anhang-24-IV-6.html | 2026-11-27 |
| LStR R 8.1(9): list price, monthly values, method | https://lsth.bundesfinanzministerium.de/lsth/2026/A-Einkommensteuergesetz/II-Einkommen-2-24b/4-Ueberschuss-d-Einnahmen-ueber-die-Werbungsk-8-9a/Paragraf-8/r-8-1-9.html | 2026-11-27 |
| SvEV §§ 1–3: contribution gates and valuation | https://www.gesetze-im-internet.de/svev/ | 2026-11-27 |
| EStG § 37b: non-cash flat tax | https://www.gesetze-im-internet.de/estg/__37b.html | 2026-11-27 |
| BMF § 37b guidance: taxable receipts and election | https://lsth.bundesfinanzministerium.de/lsth/2026/B-Anhaenge/Anhang-23a/inhalt.html | 2026-11-27 |
| EStG § 40: flat-tax branches, payer, election | https://www.gesetze-im-internet.de/estg/__40.html | 2026-11-27 |
| EStG § 19(1) no. 1a: staff events | https://www.gesetze-im-internet.de/estg/__19.html | 2026-11-27 |
| EStG § 3: tax-free benefits and pensions | https://www.gesetze-im-internet.de/estg/__3.html | 2026-11-27 |
| EStG § 82(2): pension payout gate | https://www.gesetze-im-internet.de/estg/__82.html | 2026-11-27 |
| EStG § 100: 2026 subsidy and recovery | https://www.gesetze-im-internet.de/estg/__100.html | 2026-11-27 |
| BetrAVG §§ 1a, 19: conversion and collective agreements | https://www.gesetze-im-internet.de/betravg/__1a.html | 2026-11-27 |
| BetrAVG § 19 | https://www.gesetze-im-internet.de/betravg/__19.html | 2026-11-27 |
| SVBezGrV 2026 § 4(1) no. 1, reused ceiling proof | https://www.recht.bund.de/bgbl/1/2025/278/regelungstext.pdf?__blob=publicationFile&v=3 | 2026-11-27 |
| Zweites Betriebsrentenstärkungsgesetz Articles 2, 18(4): 2027 subsidy | https://www.recht.bund.de/bgbl/1/2026/14/regelungstext.pdf?__blob=publicationFile&v=2 | 2026-11-27 |
| SGB IV §§ 7, 7a: employment and status application | https://www.gesetze-im-internet.de/sgb_4/__7a.html | 2026-11-27 |
| SolzG §§ 3, 4: flat-tax surcharge | https://www.gesetze-im-internet.de/solzg_1995/__4.html | 2026-11-27 |
| AO § 240 and SGB IV § 24: reused surcharge proof | https://www.gesetze-im-internet.de/ao_1977/__240.html | 2026-11-27 |

Not yet confirmed: the following are explicit non-usable case holds. Church tax on flat tax, administrative car exceptions beyond the stated ordinary rules, travel-allowance reductions and staff-event valuation disputes are not resolved by this Guide. Check this point with one of our partner accountants.

> Contributed by OpenAccountants.
