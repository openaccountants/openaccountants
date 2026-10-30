---
name: ua-income-tax
description: "Ukrainian personal income tax (податок на доходи фізичних осіб, ПДФО) and the 5% military levy for every individual, tax year 2026, under section IV of the Tax Code of Ukraine. Covers residents and non-residents; salary and civil-law fees withheld by tax agents; the tax social benefit; interest, dividends (5% and 9%), investment profit, rent, property and car sales, gifts and inheritance; foreign income and foreign tax credit; sole proprietors on the general system (net profit, deductible expenses, depreciation, quarterly advances); independent professionals; the annual declaration due 1 May, payment by 1 August, the tax discount and refunds; penalties. Trigger on: Ukraine income tax, ПДФО, декларація про майновий стан і доходи, податкова знижка, ФОП загальна система, military levy Ukraine. Out of scope: single tax (ua-single-tax), crypto (ua-crypto-tax), ЄСВ (ua-social-contributions), employer payroll (ua-payroll), residence and treaties (ua-cross-border), companies (ua-corporate-income-tax)."
version: 0.2
jurisdiction: UA
tax_year: 2026
last_updated: 2026-10-30
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Ukraine: personal income tax and military levy (2026)

Ukraine taxes individuals under section IV of the Tax Code of Ukraine (Податковий кодекс України, Law No. 2755-VI of 2 December 2010, "TCU"). The main rate is 18% (art. 167.1). On top of it, every individual taxed under section IV pays a 5% military levy (військовий збір) on the same income (TCU section XX, subsection 10, point 16-1). Most tax is withheld at source by a tax agent: an employer, a bank, a company paying dividends, a business tenant. The individual files an annual declaration only for income nobody withheld on, for foreign income, or to claim a refund. All article numbers below are articles of the Tax Code unless another act is named. Amounts tied to the minimum wage or the subsistence minimum use the 2026 State Budget Law: minimum wage UAH 8,647 a month, subsistence minimum for able-bodied persons UAH 3,328 a month (Law No. 4695-IX, arts. 8 and 7).

## Who this applies to

- **Residents: worldwide income.** A resident is taxed on total monthly and annual taxable income, on Ukrainian-source income taxed at payment, and on foreign income (art. 163.1). Who is resident (home, centre of vital interests, citizenship, the 183-day test) is in `ua-cross-border` (art. 14.1.213).
- **Non-residents: Ukrainian-source income only** (art. 163.2), taxed at the rates for residents unless this section says otherwise (art. 170.10.1).
- **Employees and people paid under civil-law contracts.** Salary under an employment contract and fees under a civil-law contract are taxable income (art. 164.2.1, 164.2.2). The payer withholds the tax (art. 168.1.1). The employer's side (withholding, ЄСВ, reports) is in `ua-payroll`.
- **Investors, landlords, sellers of property, heirs and gift recipients.** Covered below: interest, dividends, investment profit, rent, sales of real estate and cars, gifts and inheritance (art. 164.2, 170, 172 to 174).
- **Sole proprietors (ФОП) on the general system.** Taxed on net profit at 18% (art. 177.1, 177.2), with the 5% levy. This skill carries the full computation.
- **Independent professionals** (notaries, advocates, and others registered as self-employed under art. 178.1). Net income, that is income less documented expenses needed for the activity, at 18% (art. 178.2, 178.3).
- **Out of this skill.** Sole proprietors on the single tax pay the single tax instead of PIT on that income (art. 165.1.36): see `ua-single-tax`. Virtual assets: `ua-crypto-tax`. The unified social contribution (ЄСВ): `ua-social-contributions`. Controlled foreign companies, treaties and leaving Ukraine in depth: `ua-cross-border`. Diia City gig specialists and the agricultural minimum tax liability (art. 170.14) are named here only.
- **Martial law.** The levy rates and several reliefs below are temporary rules tied to martial law, in force since 24 February 2022.

## Rates, bands and thresholds

There are no bands. Each kind of income has one flat rate.

| Item | Rate or amount | Year | Source URL |
|---|---|---|---|
| PIT main rate: salary, civil-law fees, other income not listed below | 18% | 2026 | https://zakon.rada.gov.ua/laws/show/2755-17 (art. 167.1) |
| Military levy for individuals taxed under section IV | 5% of the income in art. 163 | 2026 | https://zakon.rada.gov.ua/laws/show/2755-17 (section XX, subs. 10, point 16-1, sub-point 1.3(1)) |
| Military levy after martial law | 1.5%, from 1 January of the year after the third calendar year after martial law ends | future | same, sub-point 1.3 |
| Military levy on pay of service members | 1.5% (sub-point 1.3(4)); their money allowance is exempt while martial law lasts | 2026 | same, sub-points 1.3(4) and 1.7 |
| Passive income (interest, investment profit, royalties) | 18% | 2026 | art. 167.5.1 |
| Dividends from a Ukrainian company that pays corporate income tax | 5% | 2026 | art. 167.5.2 |
| Dividends from non-residents, collective investment institutions and companies that do not pay corporate income tax | 9% (half of 18%) | 2026 | art. 167.5.4 |
| Sale of one home or qualifying land plot a year, owned more than 3 years | 0% (not taxed) | 2026 | art. 172.1 |
| Sale of a second art. 172.1 property in the year, or of the first property in the year that is not on the art. 172.1 list | 5% | 2026 | art. 172.2, 167.2 |
| Sale of a third and further art. 172.1 property in the year, a second and further property not on that list, or unfinished construction and off-plan property rights | 18%; 5% where that property was inherited | 2026 | art. 172.2, 167.1, 167.2 |
| Sale of movable property | 5%; one car, motorcycle or moped a year is not taxed | 2026 | art. 173.1, 173.2 |
| Inheritance or gift from a family member of the 1st or 2nd degree | 0% | 2026 | art. 174.2.1, 174.6 |
| Inheritance or gift from anyone else | 5% | 2026 | art. 174.2.2, 174.6 |
| Inheritance or gift from a non-resident, or received by a non-resident | 18% | 2026 | art. 174.2.3 |
| Tax social benefit (ПСП), basic | UAH 1,664 a month (50% of UAH 3,328) | 2026 | art. 169.1.1; Law 4695-IX art. 7 |
| ПСП for a parent of two or more children under 18 | 100% of the basic amount (UAH 1,664) per child | 2026 | art. 169.1.2 |
| ПСП, 150% group (single parent per child, parent of a disabled child, students, Chernobyl categories 1 and 2, others listed) | UAH 2,496 | 2026 | art. 169.1.3 |
| ПСП, 200% group (categories listed in art. 169.1.4) | UAH 3,328 | 2026 | art. 169.1.4 |
| ПСП income limit: monthly salary not above | UAH 4,660 (3,328 x 1.4 = 4,659.20, rounded to the nearest UAH 10); times the number of children for the child benefits | 2026 | art. 169.4.1 |
| Investment profit: sales proceeds a year not above | UAH 4,660 are not taxed | 2026 | art. 170.2.8 "а" |
| Tax discount: donations to non-profit organisations | up to 4% of total taxable income of the year | 2026 | art. 166.3.2 |
| Tax discount: home rent paid by an internally displaced person, a combat participant or a person disabled by the war | up to 30 minimum wages a year, UAH 259,410 | 2026 | art. 166.3.9 |
| Tax discount: own life, pension or medical insurance | up to UAH 4,660 for each month the contract ran; 50% of that per insured family member | 2026 | art. 166.3.5 |
| Fixed asset of a sole proprietor | cost above UAH 20,000 and useful life over 1 year | 2026 | art. 14.1.138, 177.4.6 |
| Minimum useful life for depreciation | buildings 10 years; machines and equipment 5 years; intangibles at least 2 years | 2026 | art. 177.4.9 |
| Minimum wage, 1 January 2026 | UAH 8,647 a month | 2026 | https://zakon.rada.gov.ua/laws/show/4695-20 (art. 8) |
| Subsistence minimum for able-bodied persons, 1 January 2026 | UAH 3,328 a month | 2026 | https://zakon.rada.gov.ua/laws/show/4695-20 (art. 7) |

## The taxable base

**What is taxed.** Taxable income includes salary, civil-law fees, royalties, the taxable part of property sales, rent, passive income, winnings and prizes, investment profit, inheritance and gifts, fringe benefits (free housing, goods, services, a loan forgiven) and any other income not exempted by art. 165 (art. 164.2). Income in kind counts (art. 164.3). Income in foreign currency is converted at the National Bank of Ukraine rate in force when it is accrued or received (art. 164.4). Income in kind is grossed up: the base is the ordinary price times K = 100 / (100 - rate), so at 18% the factor is 100 / 82 (art. 164.5).

**Salary.** The base is accrued salary less the tax social benefit where it applies (art. 164.6). The employer withholds 18% PIT and 5% levy from each payment and pays them to the budget with the salary (art. 168.1.1, 168.1.2). Most employees owe nothing more and file no declaration (art. 179.2).

**Tax social benefit (ПСП).** It reduces the monthly salary base, at one employer only, chosen by the employee's written application (art. 169.2.1, 169.2.2). It applies only if the month's salary is not above UAH 4,660 in 2026 (art. 169.4.1). It does not apply to income other than salary, or to business income (art. 169.2.3). Because the 2026 minimum wage is UAH 8,647, a full-time employee on at least the minimum wage never gets it; it matters for part-time salaries.

**Military levy base.** The levy is charged on the income in art. 163, not on the PIT base after the ПСП or the tax discount (sub-point 1.2(1)). Income that is not included in taxable income, or is taxed at 0%, is free of the levy, except single-tax income and two items of art. 170.13-1 (sub-point 1.7). So a tax-free first home sale, a 0% family inheritance or a tax-free car sale bears no levy; a 5% second property sale bears 5% PIT plus 5% levy.

**Interest.** The bank or other payer withholds 18% when it accrues interest, and that is final (art. 170.4.1). Interest on government bonds, and on current accounts that receive only salary, pensions and social payments, is not taxed (art. 165.1.2, 165.1.41).

**Dividends.** The paying company withholds 5% or 9% (art. 170.5.1, 167.5). Foreign dividends are declared and taxed at 9% (art. 170.11.1 "а", 167.5.4).

**Investment profit** (shares, bonds, derivatives, corporate rights). Profit on each asset is the sale price less documented acquisition cost (art. 170.2.2). Gains and losses of the year are netted. A net loss carries forward without time limit against later investment profit (art. 170.2.6). Losses on wash sales within 30 days, on repurchase deals and on sales to related persons are disallowed (art. 170.2.4, 170.2.5). Proceeds of UAH 4,660 or less in the year are not taxed (art. 170.2.8). A licensed broker or bank can act as tax agent, but the individual still declares all trades (art. 170.2.2, 170.2.9). The result is declared once a year.

**Rent.** A business tenant withholds 18% from rent for real estate, on the contract rent but not less than the minimum rent set by the Cabinet of Ministers' method (art. 170.1.2, 170.1.4). If the tenant is a private individual, the landlord pays the tax himself within 40 days after each quarter and declares the year (art. 170.1.5 "а"). Real estate of a non-resident may be let only through a Ukrainian representative (art. 170.1.3).

**Sale of real estate.** One sale a year of a house, flat or part of one (with its land), or of land within the free-transfer norms, is not taxed if owned more than three years; the three-year test does not apply to inherited property (art. 172.1). The second sale in the year of an art. 172.1 property, or the first sale in the year of a property not on that list, is taxed at 5%. The third and later sales of art. 172.1 property, the second and later sales of other property, and sales of unfinished construction or of off-plan purchase rights are taxed at 18%; where that property was inherited, the rate is 5% (art. 172.2). Income is the contract price, but not less than the assessed value from the state valuation module (art. 172.3). The seller pays the tax before the notary certifies the sale (art. 172.5 "а").

**Sale of movable property.** 5% (art. 173.1). One car, motorcycle or moped a year is not taxed (art. 173.2).

**Gifts and inheritance.** 0% within the family of the 1st and 2nd degree, and for certain heirs such as a person with group I disability (art. 174.2.1). 5% for other heirs (art. 174.2.2). 18% where either side is a non-resident (art. 174.2.3). Gifts between individuals follow the same rules (art. 174.6). A gift from a company or a sole proprietor is a fringe benefit taxed at the general rules (art. 174.6).

**Sole proprietor on the general system (art. 177).**
- The object is net taxable income: proceeds in money and in kind less documented expenses connected with the business (art. 177.2). VAT of a VAT-registered proprietor is out of both income and expenses (art. 177.3).
- Deductible: materials and goods directly attributable to the product or service (art. 177.4.1); wages and civil-law fees paid to workers (art. 177.4.2); business taxes and the proprietor's own ЄСВ, but not PIT on business income or VAT (art. 177.4.3); travel, communications, advertising, bank charges, rent, repairs and running costs of business property, transport of goods, and services directly tied to the business (art. 177.4.4).
- Not deductible: expenses not connected with the business, undocumented expenses, and the cost of buying fixed assets and intangibles, which are depreciated instead (art. 177.4.5).
- Depreciation is optional, with separate records, straight-line, over a life the proprietor sets but not shorter than the minimum: 10 years for buildings, 5 for machines and equipment (a laptop is in this group), at least 2 for intangibles (art. 177.4.6, 177.4.7, 177.4.9). Current repairs are expensed; improvements are depreciated. Land, residential property and passenger cars are never depreciated (art. 177.4.6). A fixed asset is one costing over UAH 20,000 with a life over a year (art. 14.1.138); cheaper items are expensed when bought.
- A proprietor must keep a record of income and expenses, on paper or in the Electronic Cabinet (art. 177.10).
- Income from outside the registered business is taxed under the general rules (art. 177.6). A business paying a proprietor does not withhold if given proof of registration, unless the contract is in fact employment (art. 177.8).
- A negative result means no PIT and no levy on the business for the year. Art. 177 has no loss carry-forward.
- Computation order: (1) total proceeds; (2) less documented expenses and depreciation; (3) net income x 18% = PIT; (4) net income x 5% = levy; (5) less PIT advances paid; (6) balance with the declaration.

**Independent professionals.** Net income is income less documented expenses needed for the activity (art. 178.3). Business payers do not withhold if shown the registration certificate (art. 178.5). They keep income and expense records (art. 178.6).

**The tax discount (податкова знижка).** A resident with a tax number can reduce taxable salary (and dividends from 166.3.10 share purchases) by expenses actually paid during the year (art. 166.3, 166.4.1):
- part of interest on a mortgage for a home (art. 166.3.1, 175);
- donations to non-profit organisations on the official register, up to 4% of total taxable income (art. 166.3.2);
- tuition at Ukrainian pre-school, school, vocational and higher education institutions for the taxpayer or a 1st-degree relative (art. 166.3.3);
- treatment at health institutions for the taxpayer or a 1st-degree relative, except cosmetic and other listed treatments (art. 166.3.4);
- life, non-state pension and medical insurance with resident insurers, within the monthly limits above (art. 166.3.5);
- assisted reproduction (up to one third of the year's salary) and state fees for adoption (art. 166.3.6);
- conversion of a car to biofuel or gas (art. 166.3.7);
- affordable housing (art. 166.3.8);
- home rent paid by an internally displaced person, a combat participant or a person disabled by the war, who (with 1st-degree family) has no habitable home outside occupied territory and gets no budget housing payments, up to UAH 259,410 (art. 166.3.9).
The discount cannot exceed the year's salary (art. 166.4.2). Documents must back each expense (art. 166.2). An unused right lapses at the end of the following year (art. 166.4.3). The discount refunds PIT only; the levy is charged on income before the discount (sub-point 1.2(1)).

## Deadlines and filing

| What | Deadline (2026 income) | Source |
|---|---|---|
| Tax withheld by an employer or other agent | with the payment of the income | art. 168.1.2 |
| Income in kind or cash from the agent's till | within 3 operational days after the payment | art. 168.1.4 |
| Income accrued but not paid | within the deadline for a monthly period | art. 168.1.5 |
| Rent from a private tenant: landlord pays | within 40 days after each quarter | art. 170.1.5 "а" |
| Tax on a property sale | before the notary certifies the contract | art. 172.5 "а" |
| Sole proprietor, PIT advances for Q1, Q2, Q3 | by 20 April, 20 July, 20 October 2026; no advance for Q4; no payment if the quarter's result is negative | art. 177.5.1 |
| Annual declaration (декларація про майновий стан і доходи) | by 1 May of the next year; 1 May 2027 is a Saturday, so Monday 3 May 2027 | art. 49.18.4, 49.20 |
| Tax shown on an individual's declaration | by 1 August 2027 | art. 179.7 |
| Declaration claiming only the tax discount | by 31 December 2027 | art. 166.1.2 |
| Refund after a discount claim | credited within 60 days after the declaration arrives | art. 179.8 |
| Resident leaving for permanent residence abroad | declaration no later than 60 days before departure | art. 179.3 |

**Who must file.** Anyone with income from a person who is not a tax agent (a non-resident, or a private individual who is not a registered entrepreneur), or with foreign income, must declare it and pay the tax (art. 168.2.1, 168.2.2). Sole proprietors on the general system and independent professionals file every year, showing all their other income too (art. 177.11, 178.4). No declaration is needed if all income came from tax agents, was tax-free or taxed at 0%, or was a property sale or inheritance on which tax was paid at the notary (art. 179.2). Minors fully supported by others, and people in custody, wanted, in captivity or on conscript service at year end, do not file (art. 179.4).

**How.** Through the Electronic Cabinet of the State Tax Service, on the single declaration form with annexes for each kind of income (art. 179.9). A sole proprietor's declaration also shows the quarterly advances (art. 177.5). The final settlement is the year's tax less tax already paid, proved by payment documents (art. 177.5.3).

**Foreign tax documents.** If the taxpayer lacks documents proving foreign income or foreign tax paid, he applies to move the declaration deadline to 31 December (art. 170.11.2).

## Penalties and interest

| Breach | Penalty | Source |
|---|---|---|
| Declaration not filed or filed late | UAH 340; UAH 1,020 if fined for the same breach in the past year | art. 120.1 |
| Agreed tax paid late, up to 30 days | 5% of the debt paid | art. 124.1 |
| Agreed tax paid late, more than 30 days | 10% of the debt paid | art. 124.1 |
| Tax assessed by the tax authority (understatement) | 10% of the assessed amount; 25% if intentional | art. 123.1, 123.2 |
| Tax agent fails to withhold or pay the tax | 10%; 25% if intentional; 50% if repeated within 1,095 days; 75% the third time; the agent also owes the tax | art. 125-1 |
| Penalty interest (пеня) on late payment | 120% a year of the National Bank of Ukraine discount rate, for each day late | art. 129.4 |

**Martial law.** A taxpayer who cannot file or pay on time because of martial law is released from liability, but must meet the obligation within six months after martial law ends (section XX, subsection 10, point 69.1). A taxpayer who can file and pay on time does not get this relief.

## Cross-border points

- **Non-residents.** Ukrainian-source income is taxed at the resident rates (art. 170.10.1). A Ukrainian company or self-employed person paying a non-resident individual is the tax agent and withholds (art. 170.10.3). The tax discount is for residents only (art. 166.4.1).
- **Foreign income of residents.** Declared and taxed at 18%, or 9% for foreign dividends (art. 170.11.1). Foreign tax paid is credited only under a treaty ratified by the Verkhovna Rada, and only up to the Ukrainian tax on that income (art. 170.11.2, 170.11.4). Capital taxes, property taxes and indirect taxes are not credited (art. 170.11.3). Detail and residence certificates: `ua-cross-border`.
- **Controlled foreign companies.** A resident who controls a foreign company declares its profit (art. 170.13). Rules: `ua-cross-border`.
- **Inheritance and gifts across the border.** 18% where the giver or the heir is a non-resident (art. 174.2.3).
- **Leaving Ukraine.** File the declaration at least 60 days before departing for permanent residence abroad (art. 179.3).
- **Foreign entrepreneurs.** Foreigners registered as sole proprietors in Ukraine are residents for art. 177 and file the annual declaration (art. 177.12).

## Worked examples

**Example 1. Employee claims the tax discount.** An employee earns UAH 30,000 a month at one employer, UAH 360,000 for 2026. The employer withholds PIT of UAH 64,800 and levy of UAH 18,000. In 2026 she paid UAH 40,000 university tuition for her son, UAH 10,000 for treatment at a clinic, and gave UAH 20,000 to a registered charity. Donations count only up to 4% of taxable income, UAH 14,400 (art. 166.3.2). Her discount is 40,000 + 10,000 + 14,400 = UAH 64,400, below her salary (art. 166.4.2). She files a declaration with the payment documents by 31 December 2027 and gets back 18% of the discount, UAH 11,592, within 60 days (art. 166.1.2, 179.8). The levy is not refunded.

```oa-check
name: Employee tax discount refund, 2026
inputs:
  monthly_salary: 30000
  tuition: 40000
  medical: 10000
  donation: 20000
steps:
  - annual_salary: monthly_salary * 12
  - pit_withheld: annual_salary * 0.18
  - levy_withheld: annual_salary * 0.05
  - donation_cap: annual_salary * 0.04
  - donation_allowed: min(donation, donation_cap)
  - discount: min(tuition + medical + donation_allowed, annual_salary)
  - refund: discount * 0.18
expected:
  annual_salary: 360000
  pit_withheld: 64800
  levy_withheld: 18000
  donation_cap: 14400
  donation_allowed: 14400
  discount: 64400
  refund: 11592
```

**Example 2. General-system sole proprietor with a laptop.** A sole proprietor on the general system receives UAH 3,300,000 in 2026, evenly over the year. Documented expenses: subcontractors UAH 400,000, software UAH 60,000, rent UAH 120,000, bank charges UAH 15,000. In December 2025 she bought and started using a laptop for UAH 45,000. It costs more than UAH 20,000, so it is a fixed asset: she cannot expense it, and the minimum life for machines and equipment is 5 years, so 2026 depreciation is UAH 9,000 (art. 177.4.5, 177.4.9). Her ЄСВ is 22% of her net taxable income, capped at the maximum base of UAH 172,940 a month (Law 2464-VI art. 7.1.2, 7.3, 8.5; Budget Law 4695-IX art. 32). Her profit is above the cap in every month whether or not the ЄСВ itself is deducted first, so her ЄСВ is the maximum, UAH 456,561.60 for the year, which she paid during 2026 and deducts (art. 177.4.3). Net income is UAH 2,239,438.40. PIT at 18% is UAH 403,098.91 and the levy at 5% is UAH 111,971.92. She paid PIT advances of UAH 290,000 by 20 April, 20 July and 20 October and no levy during the year, so with the declaration due 3 May 2027 she owes UAH 113,098.91 PIT and UAH 111,971.92 levy, UAH 225,070.83 in total. Her proceeds also pass UAH 1,000,000, so she checks VAT registration in `ukraine-vat`.

```oa-check
name: General-system FOP net profit with laptop depreciation and capped ЄСВ, 2026
inputs:
  proceeds: 3300000
  subcontractors: 400000
  software: 60000
  rent: 120000
  bank_charges: 15000
  minimum_wage: 8647
  laptop_cost: 45000
  minimum_life_years: 5
  advances_paid: 290000
steps:
  - depreciation: laptop_cost / minimum_life_years
  - profit_before_esv: proceeds - subcontractors - software - rent - bank_charges - depreciation
  - max_base_month: minimum_wage * 20
  - own_esv: round(max_base_month * 0.22 * 12, 2)
  - net_income: profit_before_esv - own_esv
  - net_income_month: round(net_income / 12, 2)
  - pit: round(net_income * 0.18, 2)
  - levy: round(net_income * 0.05, 2)
  - pit_balance: pit - advances_paid
  - due_with_declaration: pit_balance + levy
expected:
  depreciation: 9000
  profit_before_esv: 2696000
  max_base_month: 172940
  own_esv: 456561.60
  net_income: 2239438.40
  net_income_month: 186619.87
  pit: 403098.91
  levy: 111971.92
  pit_balance: 113098.91
  due_with_declaration: 225070.83
```

## Ask the client first

1. Were you a Ukrainian tax resident in 2026, and did you leave or plan to leave Ukraine for good?
2. What income did you have, and from whom: employer, civil-law clients, a bank, a broker, tenants, buyers of property, a foreign payer? Was tax withheld on each?
3. Are you registered as a sole proprietor or independent professional? On the general system or the single tax (`ua-single-tax`)?
4. For a proprietor: your record of income and expenses, documents for each expense, any purchase over UAH 20,000, and the advances paid.
5. Did you sell real estate, a car or securities, or receive a gift or inheritance? From whom, and how long had you owned the property?
6. Did you pay tuition, treatment, insurance, mortgage interest, donations, or home rent as a displaced person, combat participant or person disabled by the war, in 2026, and do you have the payment documents?

## Sources

| Source | URL | Read on |
|---|---|---|
| Tax Code of Ukraine (Податковий кодекс України), Law No. 2755-VI, consolidated text with amendments up to Law No. 4967-IX of 3 Sep 2026: arts. 14.1.138, 14.1.213, 49.18.4, 49.20, 57.1, 69.1 (subs. 10), 120.1, 123, 124.1, 125-1, 129.4, 163 to 179; section XX, subsection 10, point 16-1 | https://zakon.rada.gov.ua/laws/show/2755-17 | 2026-10-30 (zakon.rada.gov.ua timed out from our network; official text read via web.archive.org capture of 12 Oct 2026, https://web.archive.org/web/20261012050950/https://zakon.rada.gov.ua/laws/show/2755-17/print) |
| Law "On the State Budget of Ukraine for 2026", No. 4695-IX of 3 Dec 2025, arts. 7 and 8 | https://zakon.rada.gov.ua/laws/show/4695-20 | 2026-10-30 (via web.archive.org capture of 4 Jan 2026) |
| State Tax Service of Ukraine | https://tax.gov.ua | 2026-10-30 (refused automated access with HTTP 403; not read) |

Not yet confirmed: whether a sole proprietor's balance on the annual declaration is due within 10 days after the filing deadline (art. 57.1) or by 1 August (art. 179.7), so pay by the earlier date; whether the 1 August 2027 payment date, a Sunday, moves to the next working day; the taxation of state pensions (art. 167.4 refers to art. 164.2.19, which has been deleted); the full list of 150% and 200% social benefit categories; the National Bank discount rate for penalty interest in 2026; whether a general-system proprietor must also pay the military levy in quarterly advances with the PIT advances (sub-point 1.4 applies the section IV order; art. 177.5.1 names only PIT); whether a proprietor's ЄСВ base is net income before or after deducting that ЄСВ, and whether ЄСВ for the fourth quarter paid in January counts in the year it is for or the year it is paid; the Cabinet of Ministers minimum rent method; the cost-of-goods matching rule and cash-basis timing for proprietors (in the Ministry of Finance record-keeping order, not read); Diia City gig-specialist rates; any amendment after the 12 October 2026 archive capture.

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
