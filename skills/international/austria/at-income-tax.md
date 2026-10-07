---
name: at-income-tax
description: Use this skill whenever asked about Austrian income tax (Einkommensteuer) for self-employed individuals filing form E1. Trigger on phrases like "Einkommensteuer", "ESt", "E1 Erklarung", "Gewinnfreibetrag", "Betriebsausgabenpauschale", "Absetzbetrge", "Sonderausgaben", "selbstandig Steuer Osterreich", "Austrian income tax", "self-employed tax Austria", or any question about computing or filing income tax for a self-employed person in Austria. This skill covers progressive tax brackets (0--55%), Gewinnfreibetrag, Betriebsausgabenpauschale, Sonderausgaben, aussergewohnliche Belastungen, Absetzbetrge, SV deductibility, and E1/E1a structure. ALWAYS read this skill before touching any Austrian income tax work.
version: 2.0
jurisdiction: AT
tax_year: 2026
last_updated: 2026-09-27
authored_by: Michael Cutajar and the OpenAccountants team
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Austrian income tax for individuals (Einkommensteuer): the E 1 return, the employee assessment (L 1) and prepayments

This Guide explains how Austria taxes one individual's income. It covers the seven income types, the 2026 tariff, profit rules for the self-employed (the profit allowance, the investment allowance and the flat expense rate), Werbungskosten for employees, special expenses, the tax credits including the Familienbonus Plus, the choice between the employee assessment (Arbeitnehmerveranlagung, form L 1) and the full income tax return (form E 1), deadlines, prepayments and surcharges. Figures are for tax year 2026, the calendar year, which is assessed in 2027. Each figure names its year. A short dated section covers the 2025 returns that are being filed and assessed now.

Sources are the Finance Ministry (BMF) and its business portal (USP), pages mostly updated 1 January 2026, and the BMF Steuerbuch 2026 (November 2025, explaining the 2025 assessment; its figures are labelled). The statute is the Einkommensteuergesetz 1988 (EStG). The legal database ris.bka.gv.at did not answer when this Guide was checked, so section numbers come from BMF and USP pages: check the statute before relying on one in a dispute.

## Scope

- **Who:** individuals who are fully taxable in Austria, meaning they have a home (Wohnsitz) or their habitual abode (gewöhnlicher Aufenthalt) there and are taxed on worldwide income. This includes employees, pensioners, sole traders, freelancers, freie Dienstnehmer, and landlords letting property privately.
- **What:** the income tax assessment for 2026, the tariff, credits, Werbungskosten, Sonderausgaben, extraordinary expenses, the self-employed profit rules, the L 1 and E 1 returns, prepayments, and surcharges for late payment and late filing.
- **Periods:** calendar 2026 (the current year and the prepayments being paid now), plus a dated section for 2025 returns.
- **Companion Guides:** VAT (Umsatzsteuer, the small business exemption, the U 30 and U 1 returns) belongs in `at-vat-return`. Social insurance contributions (SVS) belong in `at-svs-contributions`. Companies belong in `at-corporate-income-tax`. The map of all Austrian taxes is `at-tax-overview`.
- **Out of scope, refer:** non-residents (limited tax liability), partnerships' own returns (E 6), group taxation, farming flat rates, sector flat rates, the Kleinunternehmerpauschalierung, business sales and closures, private sales of real estate beyond the basic rate, treaty and move-abroad cases, audits and appeals, and payroll (monthly Lohnsteuer) calculations.

## Ask the client first

- Did you have a home or habitual abode in Austria in 2026, all year? If not, refer.
- Which income did you have in 2026: wages or pension, trade or freelance, letting, capital, other? The mix decides the return.
- Employees: more than one employer or pension at once? Other income, and how much? Did payroll apply the Familienbonus Plus, the Pendlerpauschale or a sole-earner credit?
- Self-employed: which activity exactly? Books or cash basis? Last year's turnover? Flat rate used before, or left within five years?
- New business assets with at least four years' life: what, when, what cost, kept four years?
- Partner (months together, their income), children (ages, who gets the family allowance, is support paid)?
- Church contributions, donations, voluntary pension insurance, adviser fees, medical or disability costs?
- Foreign accounts, shares or crypto without Austrian KESt?
- The 2025 tax notice and any prepayment notice.

## The method, step by step

1. **Decide the return route.** An employee whose only income is wages or a pension usually files the L 1 by choice, or receives an automatic assessment. Anyone with business income, or with wages plus more than a small amount of other income, files the E 1. The tests are in the filing-duty table below ([BMF, employee assessment](https://www.bmf.gv.at/themen/steuern/arbeitnehmerveranlagung/verfahren-arbeitnehmerinnenveranlagung/arbeitnehmerinnenveranlagung.html)).
2. **Sort the income into the seven types.** The three business types (farming, self-employed work, trade) are taxed on profit. The four non-business types (employment, capital, letting, other) are taxed on the surplus of receipts over Werbungskosten ([BMF, Einkommensbegriff](https://www.bmf.gv.at/themen/steuern/fuer-unternehmen/einkommensteuer/einkommensbegriff.html)).
3. **Take final-taxed income out.** Austrian capital income taxed by KESt, and private real estate gains taxed by ImmoESt, are normally final. Leave them out unless an option applies or no tax was withheld.
4. **For business income:** start from receipts minus expenses, or use the flat expense rate if the client qualifies. Deduct social insurance, then the Gewinnfreibetrag as the last expense, and the investment allowance where it applies.
5. **For employment income:** start from the payslip data (Lohnzettel), which already reflect social insurance and the Werbungskostenpauschale. Add Werbungskosten above the pauschale, and the commuter allowance if the employer did not apply it.
6. **Add up all income types**, offsetting losses within the year where this is allowed. Deduct Sonderausgaben (including loss carry-forwards) and extraordinary expenses above the Selbstbehalt. The result is the Einkommen.
7. **Apply the 2026 tariff** to the Einkommen, slice by slice. Then subtract the credits (Absetzbeträge), such as the Familienbonus Plus and the sole-earner credit. Credits reduce tax, not income.
8. **Subtract wage tax already withheld and 2026 prepayments.** File by the deadline and check the new prepayment notice. Appeal within one month if the notice is wrong.

## Figures for 2026, with years

### The seven income types ([BMF, Einkommensbegriff](https://www.bmf.gv.at/themen/steuern/fuer-unternehmen/einkommensteuer/einkommensbegriff.html))

| Type | Examples | How it is taxed |
| --- | --- | --- |
| Land- und Forstwirtschaft | Farmers, gardeners, foresters, beekeepers | Profit; E 1 |
| Selbständige Arbeit | Freelance professions (architects, lawyers, notaries, tax advisers), supervisory board members, GmbH managers holding more than a quarter of the shares | Profit; E 1 |
| Gewerbebetrieb | All other independent, lasting activity beyond managing own assets | Profit; E 1 |
| Nichtselbständige Arbeit | Employees and pensioners | Wage tax (Lohnsteuer) by the employer; L 1 or E 1 afterwards |
| Kapitalvermögen | Interest, dividends, fund distributions, gains on shares, derivatives and crypto | Austrian KESt, normally final: 25% on bank deposits, 27.5% on all other capital income; foreign income at the same rates through the return |
| Vermietung und Verpachtung | Letting land, buildings, flats, including subletting | Surplus; schedule E 1b |
| Sonstige Einkünfte | Private real estate sales (30%, collected as ImmoESt), speculative sales of other private assets within one year, occasional services, some annuities | Surplus; E 1, except final-taxed real estate gains |

Gains outside the seven types, such as lottery wins, gifts and inheritances, are not taxed (§ 2 EStG).

### Tariff for 2026 ([USP, Tarifstufen](https://www.usp.gv.at/themen/steuern-finanzen/einkommensteuer-ueberblick/weitere-informationen-est/tarifstufen.html))

For 2026 the band limits were raised by two thirds of the 2.6% inflation rate, which is 1.7333%. This is the yearly adjustment for "cold progression" (kalte Progression). The EUR 1,000,000 step is not indexed. Each person is taxed alone; there is no joint filing.

| Taxable income (Einkommen), 2026 | Marginal rate |
| --- | --- |
| Up to and including EUR 13,539 | 0% |
| Over EUR 13,539 up to EUR 21,992 | 20% |
| Over EUR 21,992 up to EUR 36,458 | 30% |
| Over EUR 36,458 up to EUR 70,365 | 40% |
| Over EUR 70,365 up to EUR 104,859 | 48% |
| Over EUR 104,859 up to EUR 1,000,000 | 50% |
| Over EUR 1,000,000 | 55%, limited to the years up to 2029, then 50% |

Official example for 2026: a taxable income of EUR 40,000 gives tariff tax of EUR 7,447.20 before credits. The slices are EUR 8,453 at 20% (EUR 1,690.60), EUR 14,466 at 30% (EUR 4,339.80) and EUR 3,542 at 40% (EUR 1,416.80).

For 2025 (returns being filed now) the limits were EUR 13,308, EUR 21,617, EUR 35,836, EUR 69,166 and EUR 103,072. The official 2025 example on EUR 40,000 is EUR 7,593.10. Never apply one year's bands to another year.

The tariff above is the basic case. Half-rate income, temporary unemployment benefit and foreign income subject to progression make the calculation more complex. Refer those cases.

### Credits (Absetzbeträge), 2026 ([USP, Steuerabsetzbeträge](https://www.usp.gv.at/themen/steuern-finanzen/einkommensteuer-ueberblick/weitere-informationen-est/steuerabsetzbetraege.html))

The sole-earner, single-parent and child-support credits, the traffic and pensioner credits, and their phase-out limits were raised by 1.7333% for 2026. The Kinderabsetzbetrag and the family allowance are not adjusted in 2026 and 2027.

| Credit, per year unless stated | 2026 | Condition |
| --- | --- | --- |
| Alleinverdiener- or Alleinerzieherabsetzbetrag, one child | EUR 612 | Needs the Kinderabsetzbetrag for a child for more than six months of the year |
| The same, two children | EUR 828 | |
| Each further child | EUR 273 | |
| Familienbonus Plus, child under 18 | EUR 2,000.16 | Only where Austrian family allowance is paid for the child |
| Familienbonus Plus, child 18 or over while family allowance is paid | EUR 700.08 | |
| Kindermehrbetrag, per child | EUR 700 | Low incomes only; conditions below |
| Kinderabsetzbetrag | EUR 70.90 per month per child | Paid with the family allowance (2025 to 2027) |
| Unterhaltsabsetzbetrag | EUR 38 to EUR 75 per month per child | For a parent paying statutory child support |
| Verkehrsabsetzbetrag | EUR 496 | Every employee |
| Verkehrsabsetzbetrag with a Pendlerpauschale, income up to EUR 15,069 | EUR 853 | Phases down to EUR 496 between EUR 15,069 and EUR 16,056 |
| Zuschlag zum Verkehrsabsetzbetrag | EUR 804 | Assessment only; full up to EUR 19,761 income, falling to nil at EUR 30,259 |
| Pensionistenabsetzbetrag | EUR 1,020 | With phase-out rules |
| Erhöhter Pensionistenabsetzbetrag | EUR 1,502 | Pension income at most EUR 24,616, spouse income at most EUR 2,720, no sole-earner credit |
| Pendlereuro | EUR 6 a year per km of one-way distance | Only with a Pendlerpauschale; it was EUR 2 up to 2025 |

In 2025 the same credits were EUR 601 / EUR 813 / EUR 268 (sole earner), EUR 487 (traffic), EUR 790 (supplement), EUR 1,002 and EUR 1,476 (pensioner).

Sole earner: the partner may earn at most EUR 7,411 in 2026, and the couple must be married, in a registered partnership, or living together for more than six months of the year ([Steuerbuch 2026, 2025 assessment, which prints the 2026 limit](https://www.bmf.gv.at/dam/jcr:436f8c01-38e0-41bf-b904-c0e62a862bf1/251117_Steuerbuch2026_DE_BF.pdf)). Single parent: no partner for more than six months. Both credits must be claimed in the assessment, even if the employer already applied them.

### Familienbonus Plus and Kindermehrbetrag, 2026 ([BMF, Familienbonus Plus](https://www.bmf.gv.at/themen/steuern/arbeitnehmerveranlagung/steuertarif-steuerabsetzbetraege/familienbonus-plus.html))

- For 2024 to 2026 it is EUR 166.68 a month per child under 18 and EUR 58.34 a month per child over 18 while family allowance is paid (the USP yearly totals above). It is tested month by month, applies at most once in full per child, and **reduces tax to zero at most**; it is never paid out.
- The family-allowance recipient and their partner (or the parent paying support who gets the Unterhaltsabsetzbetrag) split it half and half, or one takes all. If they claim too much, each gets half. If support was not paid in full, use schedule L 1k-bF.
- The employer can apply it (form E 30), but the assessment **must claim it again** on schedule L 1k (one per child), or a back payment may follow.
- **Kindermehrbetrag 2026** (for people with little or no tax to pay): taxable business or employment income on at least 30 days in 2026, or childcare benefit, maternity benefit (Wochengeld) or care leave pay for the whole year. Income may be at most EUR 17,038 with one child (tax before credits under EUR 700), EUR 20,538 with two (under EUR 1,400), EUR 23,356 with three (under EUR 2,100) and EUR 25,689 with four (under EUR 2,800). Add EUR 700 of tax for each further child. The person must also get the sole-earner or single-parent credit, or have a partner who is also under these limits; in that partner case only the parent receiving the family allowance gets it. The claimant must confirm on the return that the conditions are met (point 5.2 of form L 1, point 4.2 of form E 1).

### Werbungskosten and commuting for employees ([BMF, Werbungskosten](https://www.bmf.gv.at/themen/steuern/arbeitnehmerveranlagung/was-kann-ich-geltend-machen/werbungskosten/werbungskosten-ueberblick.html))

- Every active employee gets a Werbungskostenpauschale of EUR 132 a year. It is built into the wage tax tables, so actual Werbungskosten only help where together they exceed EUR 132. Compulsory social insurance, chamber levies and the e-card fee are already deducted through payroll.
- Common items: work clothing, tools, training, computers, double housekeeping and trips home, literature, travel, phone and internet share. Keep receipts seven years; do not attach them.
- The Pendlerpauschale (commuter allowance, from 20 km one way, or shorter where public transport is unreasonable) is claimed from the employer on form L 34 EDV or later in the assessment. The amount comes from the BMF Pendlerrechner; the Steuerbuch prints only the 2025 table.
- Telearbeitspauschale (called the Homeoffice-Pauschale until 2024): the employer may pay up to EUR 3 per telework day, for at most 100 days, tax free. If the employer paid less, the difference is a Werbungskosten deduction in the assessment ([BMF, telework FAQ](https://www.bmf.gv.at/themen/steuern/arbeitnehmerveranlagung/was-kann-ich-geltend-machen/werbungskosten/home-office-pauschale.html)).
- Computer used for work: the BMF worked example writes it off over three years, with half a year's depreciation in the first and last year, and applies a 40% private share where private use is not documented ([Steuerbuch 2026, 2025 example](https://www.bmf.gv.at/dam/jcr:436f8c01-38e0-41bf-b904-c0e62a862bf1/251117_Steuerbuch2026_DE_BF.pdf)).

### Special expenses and extraordinary expenses ([USP, Sonderausgaben und außergewöhnliche Belastungen](https://www.usp.gv.at/themen/steuern-finanzen/einkommensteuer-ueberblick/weitere-informationen-est/sonderausgaben-und-aussergewoehnliche-belastungen.html))

| Item | Limit | Note |
| --- | --- | --- |
| Compulsory church contributions | EUR 600 a year | EUR 400 up to 2023 |
| Private cash donations to listed bodies | 10% of the total of the year's income | Donations from business assets are business expenses instead |
| Voluntary continued insurance and buying back periods in the statutory pension scheme | No cap printed | |
| Tax adviser fees | No cap printed | Only where they are not a business expense or Werbungskosten |
| Annuities and permanent burdens; the loss deduction | | |

Church contributions, donations and voluntary pension payments are reported by the receiving body and applied automatically. An item that is a business expense or Werbungskosten is deducted as that, not as a Sonderausgabe.

Extraordinary expenses (außergewöhnliche Belastungen, schedule L 1ab), such as illness costs, only count above an income-based Selbstbehalt. Disability costs have none. Rates for the 2025 assessment ([Steuerbuch 2026](https://www.bmf.gv.at/dam/jcr:436f8c01-38e0-41bf-b904-c0e62a862bf1/251117_Steuerbuch2026_DE_BF.pdf)):

| Income | Selbstbehalt |
| --- | --- |
| Up to EUR 7,300 | 6% |
| More than EUR 7,300 | 8% |
| More than EUR 14,600 | 10% |
| More than EUR 36,400 | 12% |

The rate falls by one point each if the sole-earner or single-parent credit applies, and for each child for whom the child or child-support credit applies for more than six months.

### Losses ([BMF, Verlustverwertung](https://www.bmf.gv.at/themen/steuern/fuer-unternehmen/einkommensteuer/verlustverwertung.html))

- Losses are normally set against other income of the same year. Exceptions include loss-making models (§ 2 Abs 2a EStG) and private real estate losses, which only offset real estate gains; 60% of any remainder can be spread over 15 years against letting income.
- Business losses (the three business types) that cannot be used in the year carry forward **without time limit** as a Sonderausgabe. For cash-basis accounts this applies to losses from 2013 onwards.
- Losses from letting and other surplus income do **not** carry forward. A hobby activity (Liebhaberei) produces no tax loss at all.

### Gewinnfreibetrag (profit allowance), business years from 2024 ([USP, Gewinnfreibetrag](https://www.usp.gv.at/themen/steuern-finanzen/steuerliche-gewinnermittlung/weitere-informationen-zur-steuerlichen-gewinnermittlung/betriebseinnahmen-und-ausgaben/gewinnfreibetrag.html))

It is deducted as the last business expense from the provisional profit (§ 10 EStG).

| Profit band | Rate | Note |
| --- | --- | --- |
| First EUR 33,000 (Grundfreibetrag) | 15% | No investment needed; at most EUR 4,950; once per person, even with several businesses; also available with any flat-rate method |
| Next EUR 145,000 | 13% | Investment-based: must be covered by qualifying investments |
| Next EUR 175,000 | 7% | Investment-based |
| Next EUR 230,000 | 4.5% | Investment-based |
| Profit above EUR 583,000 | None | Maximum total allowance EUR 46,400 |

- The investment-based part is capped at the cost of qualifying assets bought or made in the year: new depreciable fixed assets with at least four years' life, or securities under § 14 Abs 7 Z 4 EStG dedicated to the business for four years. Not cars (taxis and driving-school cars excepted), used assets or low-value assets expensed at once.
- An asset leaving within four years (day by day) is taxed back, except by force majeure. Not with any flat rate, not on sale or closure gains. List covered assets in the asset register.
- Official example (case 1): profit EUR 40,000 and qualifying investment EUR 6,000 give EUR 4,950 plus EUR 910 (EUR 7,000 at 13%), so the allowance is EUR 5,860 and the final profit is EUR 34,140.

### Investitionsfreibetrag (investment allowance) ([USP, Investitionsfreibetrag](https://www.usp.gv.at/themen/steuern-finanzen/steuerliche-gewinnermittlung/weitere-informationen-zur-steuerlichen-gewinnermittlung/betriebseinnahmen-und-ausgaben/investitionsfreibetrag.html))

| Cost falling | Rate | Green assets under the Öko-IFB-VO |
| --- | --- | --- |
| From 1 November 2025 to 31 December 2026 | 20% | 22% |
| Otherwise (from 2023) | 10% | 15% |

- A business expense on top of depreciation, only in the year of purchase or completion (§ 11 EStG), on at most EUR 1 million of cost per business year, for assets with at least four years' life in an Austrian business.
- Not on: assets used for the investment-based Gewinnfreibetrag; buildings (heat pumps and similar excepted); cars (taxis, driving-school cars and zero-emission vehicles excepted); low-value assets expensed at once; used assets; most intangibles outside digitalisation, ecology and health; fossil-fuel plant. Not with any flat rate; taxed back if the asset leaves within four years.

### Basispauschalierung (flat expense rate), 2026 ([USP, Basispauschalierung](https://www.usp.gv.at/themen/steuern-finanzen/steuerliche-gewinnermittlung/weitere-informationen-zur-steuerlichen-gewinnermittlung/pauschalierung-weitere-infos/basispauschalierung-einkommensteuer.html))

| What | 2026 | 2025 |
| --- | --- | --- |
| Prior-year turnover limit ([USP news](https://www.usp.gv.at/aktuelles/newsliste/basispauschalierung-hoehere-grenzen-ab-2025-und-2026.html)) | EUR 420,000 | EUR 320,000 |
| Rate for commercial or technical consulting, asset managers, supervisory board members, shareholder-employees with a stake over 25%, lecturers, scientists, writers, teaching and educational work | 6%, at most EUR 25,200 | 6%, at most EUR 19,200 |
| Rate for all other § 22 and § 23 activities | 15%, at most EUR 63,000 | 13.5%, at most EUR 43,200 |

- The rate applies to turnover under § 125 Abs 1 BAO and covers depreciation, rent, phone, fuel, energy, advertising, advice, non-social insurance, car and travel costs, and the investment-based Gewinnfreibetrag.
- On top, at actual paid cost: goods and materials for resale, wages and payroll costs, outside labour going directly into the service, social insurance and self-employed pension contributions, fully reimbursed travel (which also reduces the turnover base), the Arbeitsplatzpauschale, 50% of a public transport pass used for business, VAT under the gross method, and the Grundfreibetrag.
- Leaving the flat rate locks it out for five business years.
- Only for people who neither must nor voluntarily keep double-entry books (§ 17 EStG; RIS unreadable today). An April 2026 BMF press release says higher bookkeeping thresholds were fixed: check them before confirming eligibility.

### Depreciation (AfA) ([USP, gesetzliche AfA-Sätze](https://www.usp.gv.at/themen/steuern-finanzen/steuerliche-gewinnermittlung/weitere-informationen-zur-steuerlichen-gewinnermittlung/betriebseinnahmen-und-ausgaben/gesetzliche-afa-saetze.html))

| What | Rule |
| --- | --- |
| Business buildings | 2.5% a year |
| Business buildings let for housing | 1.5% a year |
| Goodwill of a trade or farm | 15 years; a freelance practice is judged case by case |
| Cars and estate cars | 8 years (not driving-school cars or taxis) |
| Other assets | Normal useful life (straight line), or declining balance at up to 30% a year ([USP, GWG](https://www.usp.gv.at/themen/steuern-finanzen/steuerliche-gewinnermittlung/weitere-informationen-zur-steuerlichen-gewinnermittlung/betriebseinnahmen-und-ausgaben/geringwertige-wirtschaftsgueter.html)) |
| Low-value asset (GWG) | Costing not more than EUR 1,000 (from business years starting 1 January 2023): expensed at once; net of VAT if input VAT is deductible, gross for a VAT-exempt small business |

Half-year rule: an asset used for six months or less in its first year gets half a year's depreciation. The Steuerbuch example applies it; the statute (§ 7 Abs 2 EStG) could not be read on RIS today. Only buildings, goodwill and cars have lives set by law. For other assets use the normal useful life and document it.

### Cars ([USP, Besteuerung von Kfz](https://www.usp.gv.at/aktuelles/newsreihen/steuerrechtsreihe/steuerrechtsreihe-teil-7-besteuerung-von-kfz.html))

| What | Value |
| --- | --- |
| Highest recognised cost of a car or estate car (Angemessenheitsgrenze) | EUR 40,000 |
| Highest yearly depreciation | EUR 5,000 (EUR 40,000 over 8 years) |
| Running costs are business costs only if business trips exceed | 50% of the year's kilometres |

Other value-based costs (comprehensive insurance, financing, the matching share of a lease) are cut in the same proportion as the cost above the limit (Luxustangente). The private share is then removed. Keep a logbook.

### Travel, self-employed (domestic) ([USP, Reisekosten](https://www.usp.gv.at/themen/steuern-finanzen/steuerliche-gewinnermittlung/weitere-informationen-zur-steuerlichen-gewinnermittlung/betriebseinnahmen-und-ausgaben/reisekosten.html))

| What | Value |
| --- | --- |
| Tagesgeld (daily allowance) per 24 hours; after three hours one twelfth per started hour, the full rate after 11 hours | EUR 30 (EUR 26.40 up to 2024) |
| Night flat rate including breakfast, instead of the bill | EUR 17 |
| Kilometre rate for a private car used for business less than half the time | EUR 0.50 (EUR 0.42 up to 2024) |

A trip counts as a "Reise" only where the person is at least 25 km from the centre of their activity.

### Not deductible ([USP, nichtabzugsfähige Ausgaben](https://www.usp.gv.at/themen/steuern-finanzen/steuerliche-gewinnermittlung/weitere-informationen-zur-steuerlichen-gewinnermittlung/betriebseinnahmen-und-ausgaben/nichtabzugsfaehige-ausgaben.html))

- Private living costs; representation costs such as gifts to business friends.
- Business meals are **half** deductible, only where shown to serve advertising with the business reason far outweighing; purely social meals not at all.
- Voluntary payments (donations under §§ 4a ff EStG up to 10% of profit excepted); income tax and prepayments; fines.
- A study in the home and its furniture, unless it is the centre of the whole activity (self-employed may claim the Arbeitsplatzpauschale instead since 2022).
- Costs linked to tax-free income or to income at the 25%, 27.5% or 30% special rates; cash over EUR 500 per job to construction subcontractors; car cost above EUR 40,000.

## Boundary and exception table ([USP, Einkommensteuererklärung](https://www.usp.gv.at/themen/steuern-finanzen/einkommensteuer-ueberblick/weitere-informationen-est/einkommensteuererklaerung.html))

| Situation | Treatment | Watch for |
| --- | --- | --- |
| Income exactly at a band limit | That amount is taxed at the lower rate: the bands read "up to and including" and "over" | Use the bands of the correct year |
| Employee with only one wage or pension, no other income | No return needed; file an L 1 for deductions or refunds, or wait for the automatic assessment | See Returns and deadlines |
| Employee with other income | Mandatory return only if the other income totals more than the limit **and** total income is over the limit (filing table below) | Final-taxed capital income does not count toward the other-income limit |
| Cash-basis business | Schedule E 1a lists receipts and expenses; no separate paper accounts | Bookkeepers attach accounts instead |
| Loss year | Filing is recommended, so the loss is set by notice for carry-forward | Only business losses carry forward |
| Flat expense rate and actual expenses | Never both, except the items allowed on top | Five-year lock after leaving the flat rate |
| Investment-based Gewinnfreibetrag and investment allowance on the same asset | Not allowed; pick one per asset | Neither is available with any flat rate |
| Familienbonus Plus larger than the tax | Tax falls to zero; the rest is lost | The Kindermehrbetrag may apply to low incomes |
| Asset for private and business use | Deduct only the business share | Without documents the BMF example uses a 40% private share for a home computer |
| Payment due on a weekend or public holiday | Due the next working day | Bank transfers get a three-day grace period |

### Bank-statement patterns

| Pattern | Treatment |
| --- | --- |
| Client transfer, HONORAR, STRIPE or PAYPAL payout | Business receipt, net of VAT under the net method (`at-vat-return`) |
| GEHALT, LOHN, PENSION | Already on the Lohnzettel; do not add twice |
| MIETE received | Letting, schedule E 1b |
| ZINSEN, DIVIDENDE | Capital income; final if Austrian KESt was deducted |
| SVS, SELBSTÄNDIGENVORSORGE | Business expense, also with the flat rate |
| RESTAURANT | Half, only with proof of advertising purpose |
| KIRCHENBEITRAG, SPENDE | Sonderausgabe within limits |
| KREDITZINSEN on a business loan | Business expense (deductible) |
| USt ZAHLUNG | Exclude under the net method; an expense under the gross method |
| ESt VORAUSZAHLUNG, FINANZAMT refund, PRIVATENTNAHME, loan principal | Exclude |

## Worked cases ([USP, Tarifstufen](https://www.usp.gv.at/themen/steuern-finanzen/einkommensteuer-ueberblick/weitere-informationen-est/tarifstufen.html))

Hypothetical amounts are labelled; every rate and limit is the 2026 figure cited above.

**Case 1: freelancer on the flat expense rate (2026).** A graphic designer (trade income, cash basis, no books, prior-year turnover under the limit) has hypothetical 2026 turnover of EUR 60,000, actual expenses of EUR 8,000 and SVS contributions of EUR 9,000. The flat rate of 15% gives EUR 9,000, which is more than the actual EUR 8,000, so the flat rate is better (check the five-year lock). Provisional profit is EUR 60,000 minus EUR 9,000 (flat rate) minus EUR 9,000 (SVS on top) = EUR 42,000. The Grundfreibetrag is 15% of the first EUR 33,000 = EUR 4,950, so the taxable profit is EUR 37,050. There is no other income and no Sonderausgaben. Tariff: EUR 1,690.60 on the 20% slice plus EUR 4,339.80 on the 30% slice plus EUR 592 at 40% (EUR 236.80) = EUR 6,267.20 before credits. There is no investment-based allowance and no investment allowance, because both are barred with a flat rate.

**Case 2: employee with a child and the Familienbonus Plus (2026).** An employee with hypothetical 2026 income of EUR 32,000 (after social insurance and the Werbungskostenpauschale) has one child aged 10 and receives the family allowance. She claims the full bonus; her partner claims none. Tariff: EUR 1,690.60 plus EUR 10,008 at 30% (EUR 3,002.40) = EUR 4,693.00. Minus the Familienbonus Plus EUR 2,000.16 and the Verkehrsabsetzbetrag EUR 496 = EUR 2,196.84. The supplement is nil because income is above EUR 30,259. The assessment compares this with the wage tax withheld. If the parents split the bonus, each claims EUR 1,000.08.

**Case 3: expensive car in the business (2026).** A self-employed consultant buys a new car for a hypothetical EUR 60,000 and uses it 70% for business (logbook). Depreciation is at most EUR 5,000 a year (EUR 40,000 over 8 years), and the business share is 70% of that = EUR 3,500. Running costs count because business use exceeds 50%. Value-based costs such as comprehensive insurance are first cut to EUR 40,000 / EUR 60,000 of their amount, then to the business share. The car gets neither the investment-based Gewinnfreibetrag nor the investment allowance (it is not zero-emission).

**Case 4: church contribution over the cap (2026).** A hypothetical EUR 800 church contribution is paid. Only EUR 600 is a Sonderausgabe. The church reports it, so it is applied automatically.

**Case 5: employee with a small side income (2026).** An employee with one employer and hypothetical freelance income of EUR 700 has other income that does not exceed EUR 730, so this ground creates no duty to file, whatever the wages. If the side income were more than EUR 730 and total income were over EUR 14,769, an E 1 would be mandatory.

**Case 6: late prepayment (2026).** The fourth 2026 prepayment of a hypothetical EUR 2,500 falls on 15 November 2026, a Sunday, so it is due Monday 16 November 2026. Paid by bank transfer, it is on time if it reaches the tax office account within the three-day grace period. If it is later than that, the first late-payment surcharge is 2% = EUR 50. It is waived only if the delay is not more than five days and every tax in the last six months was paid on time.

**Case 7: 2025 return not yet filed (as at 25 September 2026).** A sole trader with 2025 income of a hypothetical EUR 20,000 (no wages) is over the 2025 limit of EUR 13,308, so he must file. The FinanzOnline deadline of 30 June 2026 has passed. Unless an extension was granted or a tax adviser holds a longer deadline, file now. A late-filing surcharge of up to 10% of the tax is possible if the delay is not excusable. Interest on a 2025 balance runs from 1 October 2026 (with a EUR 50 exemption limit), so a voluntary payment of the expected balance before then avoids it.

## When to refuse or refer

- Companies (GmbH, AG): `at-corporate-income-tax`. VAT and the small business exemption: `at-vat-return`. SVS contributions: `at-svs-contributions`. All Austrian taxes: `at-tax-overview`.
- People without an Austrian home or habitual abode, people moving in or out during the year, treaty cases, and requests for unlimited tax liability as an EU or EEA citizen: refer.
- Partnerships (OG, KG, GesbR): the partnership files a separate return (E 6), and each partner files an E 11. Refer.
- Farming, sector flat rates, the Kleinunternehmerpauschalierung, business sales or closures, private real estate sales beyond the basic ImmoESt case, crypto held abroad with complex histories, start-up employee shares, profit-sharing above the tax-free amounts, audits, appeals and criminal tax matters (self-disclosure): refer.
- Monthly payroll and the Lohnsteuer on the 13th and 14th salaries: payroll specialists.
- Never present a result as final. The tax office's notice is the only binding figure.
- Never apply one year's bands or credits to another year. Never allow both the flat rate and actual expenses, except for the items allowed on top. Never give the investment-based allowance without confirmed qualifying investments.

## Filing and payment

### Who must file, 2026 ([USP, Einkommensteuererklärung](https://www.usp.gv.at/themen/steuern-finanzen/einkommensteuer-ueberblick/weitere-informationen-est/einkommensteuererklaerung.html))

| Test (2026) | Limit |
| --- | --- |
| Asked by the tax office to file | Always file |
| Income with no wage-taxed income | More than EUR 13,539 |
| Wage-taxed income plus other income | Other income more than EUR 730 **and** total income more than EUR 14,769 |
| Two or more employments or pensions at the same time, not taxed together | Income more than EUR 14,769 |
| Capital income at the 27.5% special rate with no KESt (for example foreign) | File, whatever the amount |
| Private real estate gain without ImmoESt | File |
| Business owner keeping books | File, whatever the income |

The BMF employee page also lists as triggers for a mandatory L 1 or E 1: a Familienbonus Plus or credit given without entitlement, an unreported change in commuting, an exemption notice (Freibetragsbescheid) used by payroll, too high a tax-free telework allowance, and more than EUR 3,000 of tax-free profit share ([BMF, employee assessment](https://www.bmf.gv.at/themen/steuern/arbeitnehmerveranlagung/verfahren-arbeitnehmerinnenveranlagung/arbeitnehmerinnenveranlagung.html)).

### Returns and deadlines

- **E 1 with schedules:** E 1a (cash-basis business), E 1b (letting), E 1kv (capital income), L 1k or L 1k-bF (children), L 1ab (extraordinary expenses), L 1i (foreign wages without wage tax), L 1d (special Sonderausgaben). Bookkeepers attach accounts. Do not attach the Lohnzettel, because the employer sends it.
- **Deadline for 2026 returns:** 30 April 2027 on paper, or 30 June 2027 through FinanzOnline. E-filing is the rule. Paper filing is allowed without internet access, or for a self-filer whose prior-year turnover does not exceed EUR 55,000 ([USP, Einreichen von Steuererklärungen](https://www.usp.gv.at/themen/steuern-finanzen/steuerliche-rechte-und-pflichten/weitere-informationen-zu-steuerlichen-rechten-und-pflichten-als-unternehmen/einreichen-von-steuererklaerungen.html)); the [BMF deadlines page](https://www.bmf.gv.at/themen/steuern/fristen-verfahren/fristen-faelligkeiten.html) still states EUR 35,000, so confirm with the tax office before relying on paper filing. An extension can be requested with reasons, including through FinanzOnline. Tax advisers get longer deadlines under the quota system (§ 134a BAO).
- **Employee assessment (L 1) by choice:** within five years after the year ends, so for 2026 by 31 December 2031. Receipts are not attached, but keep them for seven years.
- **Automatic assessment:** in the second half of the following year. It happens if no return has arrived by 30 June, the file shows only wage-taxed income, the refund is at least five euros, and no further deductions are expected. A return filed within five years replaces it. After two years with no assessment, a refund is always paid out automatically ([BMF, automatic assessment](https://www.bmf.gv.at/themen/steuern/arbeitnehmerveranlagung/verfahren-arbeitnehmerinnenveranlagung/antragslose-arbeitnehmerinnenveranlagung.html)).
- **Appeal (Beschwerde):** within one month of the notice being delivered.

### Prepayments and interest ([USP, Einkommensteuervorauszahlungen](https://www.usp.gv.at/themen/steuern-finanzen/einkommensteuer-ueberblick/weitere-informationen-est/einkommensteuervorauszahlungen.html))

- Due 15 February, 15 May, 15 August and 15 November. A date on a weekend or holiday moves to the next working day. The tax office sends a reminder about a month before.
- In the first year they are based on an estimate of profit. After that, each notice sets them for the current and later years; the current year's amounts change only if the notice is issued by 30 September.
- A reduction can be requested, with reasons, until 30 September. Prepayments and wage tax are credited in the assessment.
- A balance for the year is charged interest (Anspruchszinsen) from 1 October of the following year, with an exemption limit of EUR 50. Refunds also earn interest from that date. Paying the expected balance in advance avoids the interest. A balance set by the notice is due within one month of the notice being served (§ 210 Abs 1 BAO, per the [BMF filing-duty page](https://www.bmf.gv.at/themen/steuern/fuer-unternehmen/einkommensteuer/einkommensteuererklaerungspflicht.html)).

### Surcharges ([USP, Fristen und Fälligkeiten](https://www.usp.gv.at/themen/steuern-finanzen/steuerliche-rechte-und-pflichten/weitere-informationen-zu-steuerlichen-rechten-und-pflichten-als-unternehmen/fristen-und-faelligkeiten.html))

| What | Rate |
| --- | --- |
| First late-payment surcharge (Säumniszuschlag) | 2% of the unpaid tax |
| Second and third, if still unpaid three and six months after enforceability | 1% each |
| Late filing (Verspätungszuschlag), if the delay is not excusable | Up to 10% of the tax assessed |

The first surcharge is waived if the delay is not more than five days and all taxes were paid on time in the previous six months. On request, it is reduced where there was no gross fault. Bank transfers get three days' grace.

### 2025 returns (dated section, as at 25 September 2026) ([BMF, Einkommensteuererklärungspflicht](https://www.bmf.gv.at/themen/steuern/fuer-unternehmen/einkommensteuer/einkommensteuererklaerungspflicht.html))

- 2025 filing limits: EUR 13,308 without wages; with wages, other income over EUR 730 and total income over EUR 14,517. Use the 2025 bands and credits cited above.
- The 2025 deadlines (30 April and 30 June 2026) have passed, unless an extension was granted or a tax adviser holds a longer deadline. File now to limit any late-filing surcharge.
- Interest on 2025 balances starts 1 October 2026. A 2025 employee assessment (L 1) can be filed until 31 December 2030, and automatic 2025 assessments are issued in the second half of 2026.

## Completion checklist

- [ ] Residence confirmed, and every income type identified and sorted into the seven types.
- [ ] Final-taxed capital income and real estate gains left out, or declared where no KESt or ImmoESt applied.
- [ ] Profit method chosen (actual, flat rate, or books); flat-rate eligibility and five-year lock checked.
- [ ] Social insurance deducted; Grundfreibetrag applied; any investment-based allowance and investment allowance matched to listed assets held for four years.
- [ ] Car cost capped, business share and logbook checked; meals halved only with proof.
- [ ] Werbungskosten above the pauschale, commuter allowance and telework difference claimed for employees.
- [ ] Sonderausgaben within limits; extraordinary expenses above the Selbstbehalt; loss carry-forward applied.
- [ ] 2026 bands applied; credits (Familienbonus Plus split, sole earner, traffic, pensioner, Kindermehrbetrag) checked against their conditions.
- [ ] Correct return (L 1 or E 1 with schedules), filed by the deadline, with the prepayment notice checked.
- [ ] Output labelled as a draft for review by a Steuerberater or other licensed adviser before filing.

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
