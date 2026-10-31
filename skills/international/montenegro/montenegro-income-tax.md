---
name: montenegro-income-tax
description: "Montenegro personal income tax (porez na dohodak fizičkih lica) for tax year 2026, from the Personal Income Tax Law as amended by 160/25 (from 1 January 2026) and 70/26 (from 21 May 2026). Covers residence and scope, the monthly salary bands (0, 9 and 15% at EUR 700 and 1,000), the annual bands for a principal independent activity (0, 9 and 15% at EUR 8,400 and 12,000), the flat 15% for supplementary entrepreneurs, occasional work, rent, capital income, capital gains, sport, royalties, other receipts and internet or gaming income, and gambling winnings (progressive to 20 May, 12% from 21 May). Sets out business-profit adjustments, standard expense percentages, losses, reliefs, the municipal surtax, the GPP-FL return due by the end of April, monthly advances, withholding, lump-sum tax, fines and the foreign tax credit. Payroll, social contributions and VAT have their own skills."
version: 0.4
jurisdiction: ME
tax_year: 2026
last_updated: 2026-10-31
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Montenegro personal income tax, tax year 2026

This skill computes Montenegro personal income tax for an individual or a sole proprietor (preduzetnik) for 2026. The law is the Personal Income Tax Law (Zakon o porezu na dohodak fizičkih lica, "PIT Law"), consolidated through amendment 160/25, which applies from 1 January 2026 (160/25 art. 21), read with amendment 70/26, which changes the gambling rate from 21 May 2026 (70/26 arts. 1 and 3). The tax is run by the Tax Administration (Poreska uprava). The currency is the euro.

## Who this applies to

- **Taxpayers.** Every resident or nonresident individual who earns income from a source named in the law. Where two or more people earn income jointly, each is taxed on his or her share (PIT Law art. 2).
- **Residents.** An individual is resident if he or she has a domicile or centre of business and vital interests in Montenegro, or stays in Montenegro for more than 183 days in the tax year. An individual sent abroad to work for a Montenegrin resident person or for an international organisation is also resident (art. 3). Citizenship, a bank account or one immigration document does not decide residence.
- **Scope.** Residents are taxed on income earned in and outside Montenegro; nonresidents only on income earned in Montenegro (art. 4).
- **Tax period.** The calendar year, except where an activity starts or stops during the year (art. 7). On cessation of an independent activity, tax is computed for the part of the year in which it was carried on (art. 42(1a)).
- **Income classes.** Personal earnings (salary); independent activity, split into a principal independent activity, supplementary entrepreneurship and occasional independent work; property (rent); capital; capital gains; sport; copyright, related rights, patents, trademarks and independent cultural professionals; other receipts; internet and video games (gaming); and games of chance (art. 12(2)). Total income is the sum of these for the period (art. 12(3)).
- **Out of the tax.** Members of foreign diplomatic and consular missions and their households who are not Montenegrin citizens, UN technical-assistance officials, honorary consuls on pay from the appointing state, and officials, experts and administrative staff of international organisations who are not Montenegrin citizens or have no domicile in Montenegro (art. 6).
- **Other skills.** Monthly salary withholding and the IOPPD report are in the [payroll skill](montenegro-payroll.md); insurance status, contribution bases and the annual pension refund in the [social contributions skill](montenegro-social-contributions.md); VAT in the [VAT skill](montenegro-vat.md); companies (d.o.o., a.d.) in the [corporate income tax skill](me-corporate-income-tax.md).

## Rates, bands and thresholds

| Item | Amount | Tax year | Source |
|---|---|---|---|
| Personal earnings (salary), monthly | 0% up to EUR 700.00; 9% from EUR 700.01 to 1,000.00; 15% above EUR 1,000.00 | 2026 | [PIT Law art. 10(1)(1)][law], as restated by [160/25 art. 3][amend] |
| Principal independent activity, annual | 0% up to EUR 8,400.00; 9% from EUR 8,400.01 to 12,000.00; 15% above EUR 12,000.00 | 2026 | [PIT Law art. 10(1)(2)][law] |
| Supplementary entrepreneurship, occasional work, property, capital, capital gains, sport, royalties, other receipts, internet and gaming | 15% of the tax base | 2026 | [PIT Law art. 10(1)(3)][law] |
| Gambling winnings paid 1 January to 20 May 2026 | 0% up to EUR 50.00; 10% from EUR 50.01 to 1,500.00; 15% above EUR 1,500.00, per winning | 1 Jan to 20 May 2026 | [PIT Law art. 10(1)(4)][law], [160/25 art. 3][amend] |
| Gambling winnings paid from 21 May 2026 | 12% of each winning | from 21 May 2026 | [70/26 arts. 1 and 3][may]; [Gazette record][mayrecord] |
| Undeclared income found from the rise in net assets | 80% of the base | 2026 | [PIT Law art. 10a][law] |
| Occasional independent work, undocumented costs | standard expenses 30% of receipts | 2026 | [PIT Law art. 20(2)][law] |
| Rent, undocumented costs | standard expenses 30% | 2026 | [PIT Law art. 35(2)][law] |
| Holiday letting to tourists | standard expenses 50% if tourist tax is paid; 70% under a lease with a travel agency or local tourist organisation with average occupancy of at least 60 days a year | 2026 | [PIT Law art. 35(3)][law] |
| Depreciable fixed assets | value over EUR 200 and useful life over one year | 2026 | [PIT Law art. 23(2)][law] |
| Depreciation rates | group I 2.5% (straight line, asset by asset); II 10%; III 15%; IV 20%; V 30% (declining balance on the group) | 2026 | [PIT Law art. 23(3) to (5)][law]; [160/25 art. 7][amend] |
| Health, humanitarian, social, educational, scientific, religious, cultural, sports and environmental spending | deductible up to 3% of total income | 2026 | [PIT Law art. 24][law] |
| Representation (entertainment) | deductible up to 1% of total income | 2026 | [PIT Law art. 25][law] |
| Chamber and association memberships | deductible up to 0.1% of total income, or the amount fixed by law | 2026 | [PIT Law art. 26][law] |
| Business losses | carried forward, no longer than 5 years | 2026 | [PIT Law art. 33][law] |
| New business in an underdeveloped municipality | tax cut by 100% for the first 8 years, total relief no more than EUR 200,000; apply within 30 days of registration | 2026 | [PIT Law arts. 32 and 32a][law] |
| New hire in an underdeveloped municipality | salary tax relief for 4 years from hiring | 2026 | [PIT Law art. 32b][law] |
| Property acquisition cost that cannot be established | 80% of the sale price | 2026 | [PIT Law art. 37d(5)][law] |
| Sport income, undocumented costs | standard expenses 30%; amateur athletes 90% | 2026 | [PIT Law art. 37j][law] |
| Copyright and related income, undocumented costs | 60% fine art; 50% architecture, urban and landscape planning; 30% performers; 30% all other copyright, related rights, patents, trademarks and cultural professionals | 2026 | [PIT Law art. 37lj][law] |
| Internet income | expenses 15% of receipts | 2026 | [PIT Law art. 37p(1)][law] |
| Video-game (gaming) income, undocumented costs | standard expenses 20% | 2026 | [PIT Law art. 37p(3)][law] |
| Lump-sum tax eligibility | prior-year (or planned) turnover below EUR 30,000.01 | 2026 | [PIT Law art. 49(1)][law]; [160/25 art. 14][amend] |
| Salary from two or more payers, return required | total monthly gross above EUR 700 | 2026 | [PIT Law art. 43(4)(5)][law] |
| Municipal surtax (prirez) | up to 13% of the tax; up to 15% in the Capital City (Podgorica) and the Old Royal Capital (Cetinje); rate set by each municipality's decision | 2026 | [Local Self-Government Financing Law arts. 8 and 9][local] |
| Pension and disability contribution (PIO), employees | 10% employee, 0% employer | 2026 | [Contributions Law art. 15][contrib] |
| Unemployment contribution, employees | 0.5% employee, 0.5% employer | 2026 | [Contributions Law art. 18][contrib] |
| VAT, standard rate and registration | 21%; registration once turnover in the last 12 months, or a shorter period, exceeds EUR 30,000 | 2026 | [VAT Law arts. 24, 42 and 55][vat] |
| Fine, individual (return, payment, foreign salary, rent withholding) | EUR 500 to 2,000 | 2026 | [PIT Law art. 53v][law] |
| Fine, entrepreneur (return, advances, information return, lump sum, books) | EUR 1,000 to 6,000, plus a possible ban on the activity of 1 to 3 months | 2026 | [PIT Law art. 53a(3) and (4)][law]; [160/25 art. 18][amend] |
| Fine, legal-person payer | EUR 2,000 to 20,000; responsible person EUR 500 to 1,000 | 2026 | [PIT Law art. 53a(1) and (2)][law] |

Checks: a monthly salary of EUR 1,200 bears PIT of 300 × 9% + 200 × 15% = EUR 57.00. Annual principal-business profit of EUR 8,400 bears no tax; EUR 12,000 bears EUR 324.00. The salary bands are monthly; the business bands are annual. Never apply one to the other.

## The taxable base

### How the base is built

Taxable income is total income less recognised expenses, which must be documented unless the law says otherwise (art. 13). A resident's base is the taxable income of the period less a carried-forward loss; a nonresident's base has no loss deduction (art. 8). Each income class has its own base, rate and payment route, so keep a separate schedule per class.

### Exclusions and exempt amounts

- **Not income** (art. 5): disability rights payments, child allowance, basic social-protection rights, aid for natural disasters, health-insurance benefits other than salary compensation, inheritances and gifts, organised humanitarian aid, state awards, pensions (except pensions of state and public officials), prize games, insurance of property and life, and receipts of religious officials (point 12, added by [160/25 art. 1][amend]).
- **Exempt up to set amounts** (art. 5a): for example, death solidarity aid up to EUR 2,000 (raised from 1,500 by [160/25 art. 2][amend]), illness aid up to EUR 1,000, retirement severance up to EUR 1,500, field allowance and separated-living allowance up to EUR 100 a month, student grants up to EUR 300 a month, newborn payment to an employee up to EUR 1,000, amateur athletes' food allowance up to EUR 600 a month, and jubilee awards of EUR 150 to 450.
- An inherited or gifted property's exclusion at receipt does not make its later sale tax free: the acquisition cost is then the donor's or deceased's cost (art. 37d(3)).
- An unidentified bank credit is neither an exempt gift nor automatically business revenue. If the tax authority finds undeclared income from the rise in net assets, art. 10a taxes it at 80%.

### Principal independent activity and supplementary entrepreneurship

- **Who.** A principal independent activity is a registered business, a liberal profession (health workers, vets, farmers, lawyers, notaries, auditors, engineers, architects, advisers, consultants, translators, journalists and similar) or professional and intellectual services that are the taxpayer's main activity (art. 16(2) and (3)). Supplementary entrepreneurship is business carried on by an entrepreneur as a supplementary activity under the company law (art. 16(4), added by [160/25 art. 5][amend]). Supplementary entrepreneurship is taxed at a flat 15%: it does not get the 0% and 9% bands.
- **Base.** Taxable profit is the income-statement profit adjusted under the PIT Law (art. 17). Income and expenses follow the income statement under the accounting law unless the PIT Law says otherwise (arts. 18 and 20(1)). Dividends and profit shares from other legal persons are left out of the business base (art. 19); this does not exempt an individual's private dividends, which are capital income under art. 37.
- **Not deductible** (art. 21): costs not incurred for the business, costs that cannot be documented, interest for late payment of tax and contributions, interest paid to nonresidents above the usual commercial rate, payments to a nonresident head office, profit distributions to employees or others, fines and penalties, and contributions to political organisations. Income tax and owner drawings are not expenses either.
- **Inventory.** Materials and goods sold use weighted average cost or FIFO (art. 22).
- **Depreciation.** Tax depreciation replaces book depreciation on fixed assets over EUR 200 with a life over one year, at the group rates in the table (art. 23). Right-of-use assets under operating leases and intangible assets are depreciated as booked under the accounting rules (art. 23(6) and (7)). Do not use the corporate-tax EUR 300 threshold.
- **Capped expenses.** Qualifying-purpose spending up to 3% of total income, and only if paid to bodies carrying on those activities and used only for those purposes (art. 24). Representation up to 1%, if business-related, documented and not paid to a related person (art. 25). Memberships up to 0.1%, except a membership fixed by law (art. 26). Do not use the corporate 3.5% cap.
- **Bad debts.** Deductible only if the debt was earlier included in income, is written off in the books and failed collection is proved; a later recovery goes back into income (art. 27). Reserve funds are not deductible (art. 28).
- **Related-party interest.** Deductible up to the open-market interest cost and no more than actually paid (art. 30). The difference between arm's length interest and interest actually received is added to the lender's base (art. 31).
- **Losses.** Business losses carry forward for no more than five years (art. 33). Keep a register by year of origin and use. A business loss is not set against rent, capital income or capital gains, and a capital loss is not carried forward under art. 33.
- **Mixed-use costs.** Home office, car, phone and internet costs are deductible only for the business part, since private costs are excluded (art. 21(1)) and costs must be documented (arts. 13(2) and 21(2)). The law sets no fixed home-office or car percentage: ask for floor-area or mileage evidence and deduct nothing until it is produced.
- **VAT-registered taxpayers.** Output VAT is not income and recoverable input VAT is not an expense, because the base follows the income statement (arts. 18 and 20).

Principal annual business PIT on taxable base B: `0.09 × max(min(B, 12000) − 8400, 0) + 0.15 × max(B − 12000, 0)`.

### Occasional independent work

Occasional work outside the taxpayer's main activity, or a work contract (ugovor o djelu) to make or repair something or perform a physical or intellectual task, if not taxed under another heading (art. 16(5)). If costs are not documented, standard expenses are 30% of receipts (art. 20(2)), so the base is 70% of the gross receipt and tax is 15% of that. A legal-person or entrepreneur payer withholds the tax at each payment; income received directly is taxed with the annual return (art. 48a).

### Classifying bank-statement lines

| Line on the statement | Class | Rule |
|---|---|---|
| Client payments, fees, platform payouts (Stripe, PayPal, Wise, Upwork) into a registered business | Principal or supplementary business income | Arts. 16 to 18 |
| ZARADA, PLATA, salary from an employer | Personal earnings, monthly bands | Arts. 10(1)(1), 14 and 15 |
| ZAKUP, KIRIJA, rent received | Property income, 15% after expenses | Arts. 34 to 36 |
| KAMATA, interest received | Capital income, 15% of gross (interest on Montenegrin government, central bank or municipal debt securities is not capital income) | Art. 37(1)(1) and (5) |
| DIVIDENDA, dividend | Capital income, 15% of gross | Art. 37(1)(4) |
| POVRAĆAJ POREZA, tax refund | Not income | Art. 42(6) |
| Own-account transfers and loan principal; output VAT remittances and recoverable input VAT | Neither income nor expense; check nonrecoverable VAT with the underlying expense or asset in the accounts-to-tax workpaper | Arts. 13, 18, 20 and 23 |
| POREZ, PRIREZ, income tax paid; drawings | Not deductible | Art. 21 |
| KAZNA, fines and penalties | Not deductible | Art. 21(7) |
| Laptop, furniture, car over EUR 200 | Fixed asset, depreciate | Art. 23 |
| DOPRINOSI, PIO, contributions | Track separately in the contribution workpaper | Contributions Law |

### Property income

Rent from movable and immovable property (art. 34). Expenses are documented actual costs or, if not documented, 30% of rent (art. 35(1) and (2)). For rooms, apartments, houses and flats let to tourists, standard expenses are 50% if tourist tax was paid, or 70% under a lease with a travel agency or local tourist organisation giving average occupancy of at least 60 days a year (art. 35(3)). The route depends on the evidence, not on the larger percentage. Taxable income is rent less expenses in the same period (art. 36). A legal-person or entrepreneur tenant withholds 15% at each payment; rent received directly is taxed with the annual return (art. 49a). A licensed holiday-letting provider files a return even with no income in the year (art. 43(5)). Tourist tax, property tax and VAT are separate.

### Capital income

Interest; the owner's private use of company assets and services; liquidation surplus above invested capital; dividends and profit shares in cash, shares or stakes; and shares that board members and employees receive or buy on preferential terms (art. 37(1) and (2), as amended by [160/25 art. 8][amend], which deleted point 2). No costs are deductible; the base is the gross amount (art. 37(3) and (4)). Interest on debt securities issued by the state, the Central Bank of Montenegro or a municipality is not capital income (art. 37(5)). The payer withholds 15% at payment (art. 50).

### Capital gains

- **What.** Gains on the sale or transfer of real estate (land, buildings, flats, business units and other structures), stakes in legal persons and shares and other equity securities. A negative difference is a capital loss (art. 37a).
- **Real estate.** Sale price is the contract price less documented reconstruction and sale costs; the tax authority sets the price if the contract price is below market, and an exchange uses market price (art. 37c). Acquisition cost is the price paid or the price the authority set on acquisition under the real-estate transfer tax law, or construction cost for a self-built property; for a gift or inheritance, the donor's or deceased's cost. It is indexed each year by retail price growth from acquisition to sale, using official statistics. Only if no cost can be established is acquisition cost 80% of the sale price (art. 37d).
- **Company stakes.** Sale and purchase values are those in the contract; the authority sets the sale value if below market; a stake acquired on founding costs the founding contribution plus increases (art. 37e).
- **Shares.** Listed shares cost the documented price paid; unlisted shares the documented price, or nominal value if no price is documented. Repeated purchases of the same issuer use FIFO. Bonus shares paid as a dividend cost the value at which they were acquired (art. 37f).
- **Exempt** (art. 37g): a property that was the taxpayer's only and main residence (domicile); transfers between spouses or life partners linked to marriage, partnership, divorce, its end or inheritance; gifts to first-order heirs.
- **Losses.** A capital loss is set only against capital gains of the same tax period (art. 37h).
- **Tax.** 15%, computed annually and paid with the annual return (art. 50a). A gain recorded in business books goes in the tax balance, not a separate return (art. 43(6a)); never report it twice.

### Sport, copyright, other receipts, internet and gaming

- **Sport** (arts. 37i to 37k): income of professional and amateur athletes, coaches and sports professionals, transfers and fees, that is not salary. Documented costs, or standard 30%; amateur athletes 90%.
- **Copyright, related rights, patents, trademarks, cultural professionals** (arts. 37l to 37m): documented costs, or standard 60% for fine art, 50% for architecture, urban and landscape planning, 30% for performers' rights and 30% for everything else.
- **Other receipts** (art. 37n): awards and payments to people not employed by the payer, officials' pensions under the officials' salary law (point 1a, added by [160/25 art. 9][amend]), receipts above art. 5a limits, pay of board and assembly members not employed by the payer, bankruptcy trustees and lay judges, severance on agreed termination, sales-agency income and all other untaxed income. Taxed on gross (art. 37n(3)).
- **Internet and video games** (arts. 37o to 37r): income from an activity carried on through the internet, if not taxed under another heading, with a fixed 15% expense; income from video-game competitions and other gaming that is not salary, with documented costs or 20% standard. These percentages are expenses; the tax rate is 15%. Do not use both actual and standard costs, and do not move salary or business income into the internet heading.

### Gambling winnings

Taxable winnings from lottery games and betting are each winning less its corresponding stake (art. 37s(2)(1) and (2)); a global jackpot uses the total accumulated prize defined in art. 37s(2)(3), without importing that stake deduction. These definitions were replaced by [160/25 art. 10][amend]. Prize games are not income (art. 5(10)). Rates: progressive bands for winnings paid to 20 May 2026; 12% for winnings paid from 21 May 2026 ([70/26][may]). The game organiser withholds at each payment or transfer (art. 50f).

### Reliefs

- **Underdeveloped municipalities** (arts. 32 and 32a): a taxpayer who starts an activity there pays no tax for the first eight years from registration, capped at EUR 200,000 in total including other state aid. Not available to someone who closed the same or a similar activity in the previous three years, to recipients of aid for firms in difficulty, or in transport, shipbuilding, steel, trade and hospitality (except primary hospitality establishments). Apply within 30 days of registration; the authority decides; a statement of other state aid goes with each annual return.
- **New hires there** (art. 32b): a permanent or at least five-year hire of a person registered with the Employment Agency for over three months and living in an underdeveloped municipality frees the salary tax for four years, if headcount rises above the 12-month average. If the employer ends the contract within five years (other than at the employee's request or for serious breach), the tax is repaid within 30 days. A person previously employed by the founder or a related person of the new employer is excluded, whether or not there was a break in employment (art. 32b(3)).
- **Expired** (art. 32c): the 2021 to 2023 new-hire relief.
- **Research and innovation; digital nomads** (art. 32d): exemption for beneficiaries of research and innovation incentives, and for income from a foreign employer earned under digital-nomad status, each under its own law.

### What sits on top of PIT

- **Municipal surtax (prirez).** A municipality can levy a surtax on the PIT on salary, independent activity, property and property rights, and capital income, at up to 13% of the tax, or up to 15% in the Capital City and the Old Royal Capital (Local Self-Government Financing Law art. 8). The actual rate is the municipality's own decision (art. 9). It is a tax on the tax, never added to the income rate: at a 13% surtax the top business rate becomes 15% × 1.13 = 16.95%; at 15% it is 17.25%. The law lists only these four bases; capital gains and gambling winnings are not among them.
- **Social contributions.** Employees pay 10% PIO and 0.5% unemployment; the employer pays 0% PIO and 0.5% unemployment (Contributions Law arts. 15 and 18). The health contribution provisions are deleted (art. 17). The annual PIO ceiling is set each year by Ministry of Finance act (art. 14(3) and (4)). Older secondary guides still show 15% employee pension and 8.5% health; those rates are out of date. Details, bases and the self-employed rules are in the [social contributions skill](montenegro-social-contributions.md).
- **VAT.** Standard rate 21% (VAT Law art. 24); a business whose turnover in the last 12 months, or a shorter period, exceeds EUR 30,000 must apply for registration by the 20th of the following month (arts. 42 and 55). A VAT-registered taxpayer cannot pay lump-sum PIT (PIT Law art. 49(12)). See the [VAT skill](montenegro-vat.md).

## Deadlines and filing

- **Annual return.** Form GPP-FL with schedules A, PPG, A1, B, B1, C, D, D1, E, E1, F, G and H ([return rulebook art. 3][return]), filed by the end of April for the previous year (PIT Law art. 43(2)). Tax is self-assessed and paid when the return is filed; advances and withholding on all sources are credited (art. 42(2), (4) and (5)). An overpayment is refunded on request or credited to the next year's advances (art. 42(6)).
- **Who files** (art. 43(4) to (6)): residents with a principal independent activity (unless on lump-sum tax), supplementary entrepreneurship, or occasional work not taxed by withholding; rent, unless the payer is a legal person or entrepreneur; capital gains; foreign income; salary from two or more payers with total monthly gross above EUR 700; sport; copyright and related income; internet and gaming income. A licensed holiday-letting provider files even with no income. A nonresident files for Montenegrin income on which no withholding is prescribed.
- **Where and how.** A resident files with the tax office of his or her domicile, a nonresident with that of his or her stay, in person, by post or electronically; the taxpayer or an authorised person signs ([return rulebook arts. 4 and 5][return]; PIT Law art. 43(7)).
- **Cessation.** A taxpayer who stops an independent activity files within 30 days of deletion from the register (art. 43(2a)).
- **Late or missing return.** The tax authority files a return on the taxpayer's behalf ex officio (art. 43(6b)).
- **Two or more employers.** The authority assesses the tax by decision within 30 days of the return, from the return and its own records (art. 43a).
- **Business advances.** Principal and supplementary business tax is paid in monthly advances of 1/12 of the previous year's tax, by the end of each month for the previous month (art. 48(1) and (2)). A new business files an information return with its estimated income within 15 days of registration (art. 48(4)).
- **Lump-sum tax** (art. 49): available on request to a principal independent activity with turnover below EUR 30,000.01. Apply by the end of January, or within five days of registration for a new activity; the authority decides within 15 days. Tax is paid monthly at 1/12 by the end of the month for the previous month; seasonal activities of up to six months pay by the 5th of the month for the current month. Turnover books must be kept. Not available for lawyers, notaries, auditors, accountants, health, consulting, design, surveying, enforcement officers and other professional and intellectual activities, hairdressing, billiards and amusement games, wholesale and retail trade, hospitality, hotels, financial intermediation, real estate, or VAT-registered taxpayers; the authority can approve lump-sum tax for trade or hospitality in a kiosk, trailer or mobile unit only where the taxpayer produces and sells only its own products (art. 49(10) and (11)). If circumstances justify it, the authority orders a change of method by decision (art. 49(7)). The scale is set by Ministry rulebook (art. 49(2)).

- **Withholding by the payer, at payment:** salary (art. 46), occasional work (art. 48a), rent paid by a legal person or entrepreneur (art. 49a), capital income (art. 50), sport and copyright income earned in Montenegro (arts. 50b(1) and 50c(1)), other receipts (art. 50d). Gambling: the organiser withholds at payment and pays by the 15th of the following month (art. 50f).
- **Paid with the annual return:** capital gains (art. 50a), internet and gaming income (art. 50e), sport and copyright income earned abroad (arts. 50b(2) and 50c(2)), and occasional work or rent received directly (arts. 48a(2) and 49a(2)).
- **Self-assessed within five days:** salary from abroad, and salary from a foreign diplomatic mission or international organisation (art. 46(6) and (7)).
- **Employer reports.** Monthly report of taxes and contributions by the 15th of the month for the previous month (art. 47(3)); annual statement of salary and tax to each employee by 31 January (art. 47(1)); payers of other personal earnings under article 14 give recipients a statement by 31 January (art. 47(5)).
- **Records.** Keep identity and residence evidence, income records, accounts and loss registers, asset, valuation and indexation evidence, relief decisions, foreign tax and treaty evidence, payer statements, advance payments, the signed return and payment records.

### Lump-sum scale, application and turnover book

First apply the principal-activity, profession, VAT and own-product gates in article 49 above. A turnover of exactly EUR 30,000 is within the statutory test of less than EUR 30,000.01; a turnover of EUR 30,000.01 is not. A group name in the rulebook does not override a statutory exclusion. For example, the rulebook's group-I list includes barbers, while the statute excludes hairdressing. Do not infer eligibility from the group list alone. The authority fixes the liability by decision. [PIT Law art. 49][law]; [Pausal Rulebook arts. 2 to 5][pausal].

The four activity groups recognise costs of I: 50%, II: 40%, III: 35%, IV: 30%. The rulebook's examples include beekeepers in I, tailors and plumbers in II, vehicle mechanics in III, and bakers in IV. Match the actual activity to the full article 3 list and obtain the decision; do not choose the largest cost percentage. Within each group the turnover ceilings are EUR 7,500, 15,000, 22,500 and 30,000. The following are the **annual scale amounts**, using the subgroup ceiling, not a calculation of costs against arbitrary actual receipts. [Pausal Rulebook arts. 3 to 5][pausal].

| Group / recognised costs | Turnover ceiling EUR | Scale taxable income EUR | Annual PIT EUR | Annual PIT + contributions EUR | Official source |
|---|---:|---:|---:|---:|---|
| I / 50% | 7,500.00 | 3,750.00 | 0.00 | 412.50 | [Pausal Rulebook art. 5][pausal] |
| I / 50% | 15,000.00 | 7,500.00 | 0.00 | 825.00 | [Pausal Rulebook art. 5][pausal] |
| I / 50% | 22,500.00 | 11,250.00 | 256.50 | 1,494.00 | [Pausal Rulebook art. 5][pausal] |
| I / 50% | 30,000.00 | 15,000.00 | 774.00 | 2,424.00 | [Pausal Rulebook art. 5][pausal] |
| II / 40% | 7,500.00 | 4,500.00 | 0.00 | 495.00 | [Pausal Rulebook art. 5][pausal] |
| II / 40% | 15,000.00 | 9,000.00 | 54.00 | 1,044.00 | [Pausal Rulebook art. 5][pausal] |
| II / 40% | 22,500.00 | 13,500.00 | 549.00 | 2,034.00 | [Pausal Rulebook art. 5][pausal] |
| II / 40% | 30,000.00 | 18,000.00 | 1,224.00 | 3,204.00 | [Pausal Rulebook art. 5][pausal] |
| III / 35% | 7,500.00 | 4,875.00 | 0.00 | 536.25 | [Pausal Rulebook art. 5][pausal] |
| III / 35% | 15,000.00 | 9,750.00 | 121.50 | 1,194.00 | [Pausal Rulebook art. 5][pausal] |
| III / 35% | 22,500.00 | 14,625.00 | 717.75 | 2,326.50 | [Pausal Rulebook art. 5][pausal] |
| III / 35% | 30,000.00 | 19,500.00 | 1,449.00 | 3,594.00 | [Pausal Rulebook art. 5][pausal] |
| IV / 30% | 7,500.00 | 5,250.00 | 0.00 | 577.50 | [Pausal Rulebook art. 5][pausal] |
| IV / 30% | 15,000.00 | 10,500.00 | 189.00 | 1,344.00 | [Pausal Rulebook art. 5][pausal] |
| IV / 30% | 22,500.00 | 15,750.00 | 886.50 | 2,619.00 | [Pausal Rulebook art. 5][pausal] |
| IV / 30% | 30,000.00 | 21,000.00 | 1,674.00 | 3,984.00 | [Pausal Rulebook art. 5][pausal] |

Column 5 of the official scale is PIT alone. Column 6 is PIT **plus mandatory social contributions**, shown as `taxable income × 11% + PIT`. For an ordinary insured principal entrepreneur this reconciles to 10% PIO plus 1% unemployment on the pausal taxable-income base (Contributions Law arts. 9(7), 11(5), 15(2) and 18(2)). Do not treat the combined column as PIT or add those contributions a second time. Municipal surtax is separate and uses the relevant municipal decision. [Pausal Rulebook art. 5][pausal]; [Contributions Law][contrib]; [2026 seasonal informator, pausal section][seasonal].

For a full-year group-II third-subgroup decision, annual PIT is EUR 549 and contributions EUR 1,485, total EUR 2,034; the corresponding monthly amounts are EUR 45.75, 123.75 and 169.50. The ordinary PIT payment is one twelfth by the end of the current month for the previous month; the special payment date for a seasonal principal activity of no more than six months is the fifth of the current month. Use the authority's actual period and decision for a seasonal or partial-year liability, rather than assuming the full annual table or a rounding method. [PIT Law art. 49(3), (6) and (8)][law]; [Pausal Rulebook art. 5][pausal].

**ZPO application.** The printed application records taxpayer identity and addresses, business details, bank accounts, year, activity and manner of working, owned/rented premises and area, owned/rented equipment, employee count, prior-year product and service receipts and their sum (7.1 + 7.2 = 7.3), planned product and service receipts and their sum (8.1 + 8.2 = 8.3), applicant details and signature/date, and lodging details. Section 11 is completed by the authority. The ordinary deadlines remain end January or five days after a new registration. For **2026 only**, the Tax Administration treated applications through **27 February 2026** as timely and required paper ZPO during the IRMS rollout. Its later 2026 seasonal informator describes electronic ZPOG/ZPOS applications in IRMS's collection module. Preserve this chronology; the printed form's diskette/email fields are not evidence that those channels operate today. [Pausal Rulebook art. 7 and ZPO attachment][pausal]; [Tax Administration notice, 5 February 2026][pausalnotice]; [2026 seasonal informator][seasonal].

**KPP turnover book.** Record name, place, activity/group and tax ID; then each transaction's serial number, chronological posting date, product receipts, service receipts and their total (columns 3 + 4 = 5). Article 6 requires the record to use turnover registered through the electronic collection device and allows the book itself to be electronic. Reconcile the product/service totals to the application and decision records. [Pausal Rulebook art. 6 and KPP attachment][pausal].

### GPP-FL: promulgated schedules and the calculation crosswalk

The Gazette download for amendment **103/2025, article 3**, contains the actual GPP-FL and all thirteen attachments, unlike the short consolidated rulebook. The crosswalk below describes those printed fields. Determine **2026** liability and the filing population under the later PIT Law first; the 2025 form does not override the 160/25 or 70/26 amendments. This crosswalk is not confirmation of every live IRMS field or acceptance rule. [103/2025 arts. 1 to 3 and attachments][gppforms]; [PIT Law arts. 10, 43, 44 and 48a][law]; [160/25][amend]; [70/26][may].

On the cover select original/amended and resident/nonresident, state the year, taxpayer ID/name and personal details, residence/contact address, business registration/activity/headcount, bank accounts, relevant attachments and notes. The taxpayer or authorised representative signs; authority receipt and processing fields are separate. [GPP-FL cover and general instructions][gppforms].

| Attachment | Workpaper and printed destination | Official source |
|---|---|---|
| A: independent-activity profit/loss | Start with accounting profit (1), add book depreciation (2) and nonallowable expenses (4), deduct tax depreciation (3) and dividends/profit shares included in the business accounts (5). Positive adjusted profit is row 6; deduct permitted PPG losses (7) to obtain row 8. Row 9 separates the taxable bands and feeds main 1.1; the annual principal-activity tax goes to main 1.2. A new business loss belongs to A10, not a PIT credit. | [103/25 art. 3, A and instructions][gppforms]; [PIT Law arts. 17 to 33][law] |
| PPG: business losses | List unused losses by origin in the previous five years. PPG1 takes A6; PPG3 uses no more than the available profit and transfers to A7. Keep capital losses out of this register. | [103/25 art. 3, PPG][gppforms]; [PIT Law arts. 33 and 37h][law] |
| A1: social contributions | Record turnover (1), contribution base (1a), PIO charge/exemption (2.1/2.2), unemployment charge/exemption (2.3/2.4), and advances by component (3.1/3.2). Compare each net component with its own advances; overpayments are 4.1/4.2 and debts 5.1/5.2. Contributions are separate from main PIT advances and foreign tax credit. | [103/25 art. 3, A1][gppforms]; [Contributions Law arts. 9, 11, 15, 18][contrib] |
| B: property income | Classify rent and apply documented costs or the qualifying standard route, not both. B4 is the base for main 3.1; B5 is withholding supported by B1 for main 5.4. Record each property's details; the instructions require extra B sheets if there are more than six properties, with income/cost amounts only on the first. The current statutory filing exception for a legal-person/entrepreneur payer still applies. | [103/25 art. 3, B][gppforms]; [PIT Law arts. 35, 36, 43 and 49a][law] |
| B1: rent payer certificate | Payer and recipient identities; gross rent, tax base and advance in rows 1, 2 and 3. The payer signs. The advance supports B5; do not duplicate the rent or infer a new annual filing obligation from the certificate. | [103/25 art. 3, B1][gppforms]; [PIT Law art. 43(4)(2)][law] |
| C: capital gains/losses | Identify the asset and buyer, sale price, property reconstruction/sale costs and acquisition basis, then separate gains and losses. C9 is the positive same-year balance, or zero, for main 3.2. Keep the statutory valuation, indexation, FIFO and exemption checks above; a gain in business books goes through the tax balance rather than being duplicated here. | [103/25 art. 3, C][gppforms]; [PIT Law arts. 37a to 37h and 43(6a)][law] |
| D: sport | Classify the sport receipt, total income (2), documented or qualifying standard costs (3/4), selected deduction (5), and base (6) for main 3.3. D7 is the advance supported by D1 for main 5.5. | [103/25 art. 3, D][gppforms]; [PIT Law arts. 37i to 37k][law] |
| D1: sport payer certificate | Payer/recipient identities, gross receipt (1), base (2) and advance (3), signed by the payer. Carry only the advance to D7. | [103/25 art. 3, D1][gppforms] |
| E: copyright and related receipts | Classify copyright, related rights, patent/trademark or cultural professional income; total at E2; documented or applicable standard costs at E3/4; selected costs at E5; base at E6 for main 3.4. E7 is the E1 advance for main 5.6. The printed instructions reserve their 50% architecture route for constructed objects and exclude sketches/plans; preserve the statutory category analysis rather than automatically assigning 50% to every architectural invoice. | [103/25 art. 3, E][gppforms]; [PIT Law art. 37lj][law] |
| E1: copyright payer certificate | Payer/recipient identities, gross receipt (1), base (2), advance (3) and payer signature. The advance supports E7. | [103/25 art. 3, E1][gppforms] |
| F: foreign income | Separate source categories and countries, showing income and foreign tax in distinct columns. F10 is foreign salary for main 2.1; F11 is occasional-work income and F12 the other listed foreign categories for main 3.5. F13 records foreign tax paid, F14 the corresponding Montenegrin tax and F15 the lower eligible credit for main 5.7, subject to the statutory foreign-country cap and the separate allocation workpaper. Do not duplicate the same foreign receipt in F and a domestic schedule. | [103/25 art. 3, F][gppforms]; [PIT Law art. 44][law] |
| G: two or more salary payers | Record payer names/IDs, annual gross earnings and annual tax by payer and totals, with OPD-2 statements. The trigger is combined monthly gross above EUR 700 in at least one month. The authority determines the additional tax by decision; do not route these domestic wages through the foreign-salary field. | [103/25 art. 3, G][gppforms]; [PIT Law arts. 43(4)(5) and 43a][law] |
| H: direct occasional work, internet and gaming | H3 less documented or 30% standard costs in H4 gives H5. H6 less the 15% internet deduction in H7 gives H8. H9 less documented or 20% gaming costs in H10 gives H11. H12 = H5 + H8 + H11 feeds main 3.6. Use occasional-work H only for receipts not subject to payer withholding under article 48a; registered business and salary keep their own class. | [103/25 art. 3, H][gppforms]; [PIT Law arts. 16, 20, 37o to 37r and 48a][law] |

**Main settlement.** The printed form separately calculates principal-business PIT (1.2) and foreign-salary PIT (2.2). Foreign salary uses the monthly salary bands on each month's receipts, not the annual business scale. The bases in main 3.1 to 3.6 sum to 3.7; the printed 15% row 3.8 produces 3.9. Main 4.1 sums 1.2 + 2.2 + 3.9. Main 5.1 to 5.7 record paid business PIT advances, approved underdeveloped-municipality and research/innovation relief, B/D/E withholding and the allowed F credit; total at 5.8. Do not enter a contribution payment as a PIT advance. A positive 4.1 minus 5.8 goes to 6.1 (due); the reverse positive difference to 6.2 (overpaid). Split an overpayment between refund requested (6.3) and next-period credit (6.4) without claiming it twice. [GPP-FL main calculation and instructions, F instructions][gppforms]; [PIT Law arts. 42 and 44][law].

**Foreign-tax evidence.** F's instructions require a certificate from the competent authority abroad showing the source, amount of income and tax paid, in the source-country language and Montenegrin with a court-certified translation. Preserve the proof and apply treaty priority and the article 44 cap; the printed aggregate credit field does not authorise unused credit from one foreign country to erase tax on another country's income. Article 44 states the cap by foreign country; a mandatory separate category basket within the same country is not established here. Also retain the Montenegro tax already paid within five days on foreign salary under article 46(7): article 42(4) credits advances, but main 5.1 is labelled business advances and F15 is foreign tax. The live return field for those Montenegro salary advances is unresolved; the printed crosswalk must not cause the same salary tax to be paid twice. [F instructions][gppforms]; [PIT Law arts. 44 and 45][law].

**Printed-instruction conflicts.** The A instructions tell the reader once to put a loss in row 9, whereas the actual form and its later instruction use row 10. A1's instruction for total contributions says `2.1 + 2.2`, even though 2.2 is a PIO exemption and unemployment has separate rows. F's prose for row 11 points to row 2 column 6 (tax), while the printed form points to row 2 column 5 (income). F's discussion of the domestic-tax cap also refers to row 13 where the actual cap is row 14. A general note says occasional work is not entered in GPP-FL, but the same promulgated amendment supplies H for nonwithheld occasional receipts; H's following-page prose also contradicts the statutory payer-withholding duty. Preserve these discrepancies in the workpaper, follow the current statute for liability, and do not present an invented portal correction as verified. [103/25 art. 3, main notes and A/A1/F/H instructions][gppforms]; [PIT Law arts. 43 and 48a][law]. The unresolved 2026 mappings and rounding are listed under Sources.

## Penalties and interest

- **Individual:** EUR 500 to 2,000 for not filing the return by the end of April (or within 30 days of cessation), wrong computation or not paying with the return; for a resident with foreign or diplomatic-mission salary not paying within five days; and for rent withholding failures (art. 53v).
- **Entrepreneur:** EUR 1,000 to 6,000 for not filing or paying the annual return, not paying advances on time, not filing the information return within 15 days of registration, not paying lump-sum tax on time, or not keeping turnover books; a ban on the activity of one to three months can be added (art. 53a(3) and (4)). For an individual, not keeping turnover books brings a EUR 200 misdemeanour order (art. 53b).
- **Legal-person payer:** EUR 2,000 to 20,000 for failing to compute, withhold or pay tax on salary, rent, capital, sport, copyright, other receipts or gambling winnings, or to give salary data or the monthly report; the responsible person EUR 500 to 1,000 (art. 53a(1) and (2)).
- **Interest, appeals, enforcement.** The PIT Law refers these to the tax procedure law (art. 53). Late-payment interest runs from the day after the due date: 0.03% a day until 17 July 2026, then 5.4% a year for 18 July to 31 December 2026 (ECB main refinancing rate plus 3 points, set each half-year) (Tax Administration Law art. 95, as amended by 104/26 arts. 20 and 26; Tax Administration decision of 24 July 2026).
- A fine follows a specific offence; an arithmetic difference is not by itself a penalty.

## Cross-border points

- **Nonresidents** are taxed only on Montenegrin income (art. 4(2)), with no loss carry-forward (art. 8). They file only for Montenegrin income on which no withholding is prescribed (art. 43(6)).
- **Foreign tax credit.** A resident who pays income tax abroad gets a credit for it, capped at the Montenegrin tax on the income earned in that foreign country (art. 44). Maintain a workpaper per foreign country and compute the corresponding domestic tax with the right class rates and bases: a principal business uses the progressive bands, not a flat 15%. Do not credit social contributions, refundable treaty excess or unproved tax. The law gives no carry-forward of unused credit.
- **Treaties** prevail over the PIT Law (art. 45(1)). The Ministry sets the form and procedure for residence certificates (art. 45(2)).
- **Foreign salary** is self-assessed and paid within five days of receipt (art. 46(7)); a nonresident organisation with a seat or permanent unit in Montenegro withholds like a local employer (art. 46(5)).
- **Foreign sport and copyright income** is taxed annually with the return (arts. 50b(2) and 50c(2)).
- **Posted workers.** An individual sent abroad by a Montenegrin resident or for an international organisation remains resident (art. 3(2)).
- **Digital nomads.** Income from a foreign employer earned under digital-nomad status is exempt under art. 32d.
- **Payments to nonresidents in a business.** Interest above the usual commercial rate and payments to a nonresident head office are not deductible (art. 21(4) and (5)).

## Worked examples

All figures are EUR for 2026. Facts are as stated; there is no surtax, social contribution, VAT or relief unless stated.

### 1. Principal business: accounts to tax, and the annual balance

Total revenue 80,000; accounting profit 25,000 after all booked costs. Add back private costs 1,200 and book depreciation above tax depreciation 800. Qualifying-purpose spending 3,000 exceeds the 3% cap (2,400) by 600; representation 1,000 exceeds 1% (800) by 200; memberships 120 exceed 0.1% (80) by 40. Adjusted profit is 27,840. An unused business loss of 3,000 within its five years brings the base to 24,840. PIT is 3,600 × 9% = 324 plus 12,840 × 15% = 1,926, total 2,250. Advances paid 1,800, so 450 is due with the return. [Arts. 17 to 33, 42 and 48][law]

```oa-check
name: Montenegro principal business annual profit and settlement
inputs:
  revenue: 80000
  accounting_profit: 25000
  private_expense: 1200
  depreciation_adjustment: 800
  qualifying_spend: 3000
  representation: 1000
  memberships: 120
  available_loss: 3000
  paid_advances: 1800
steps:
  - purpose_excess: max(qualifying_spend - revenue * 0.03, 0)
  - representation_excess: max(representation - revenue * 0.01, 0)
  - membership_excess: max(memberships - revenue * 0.001, 0)
  - adjusted_profit: accounting_profit + private_expense + depreciation_adjustment + purpose_excess + representation_excess + membership_excess
  - loss_used: min(available_loss, max(adjusted_profit, 0))
  - taxable_business: max(adjusted_profit - loss_used, 0)
  - annual_pit: max(min(taxable_business, 12000) - 8400, 0) * 0.09 + max(taxable_business - 12000, 0) * 0.15
  - settlement_due: annual_pit - paid_advances
expected:
  purpose_excess: 600
  representation_excess: 200
  membership_excess: 40
  adjusted_profit: 27840
  loss_used: 3000
  taxable_business: 24840
  annual_pit: 2250
  settlement_due: 450
```

### 2. Principal versus supplementary business

The same taxable profit of 10,000. As a principal activity, PIT is 1,600 × 9% = 144. As supplementary entrepreneurship, PIT is 15% = 1,500. The class follows the facts and registration; it is not an election. [Arts. 10, 12 and 16][law]

```oa-check
name: Montenegro principal versus supplementary income rates
inputs:
  taxable_profit: 10000
steps:
  - principal_pit: max(min(taxable_profit, 12000) - 8400, 0) * 0.09 + max(taxable_profit - 12000, 0) * 0.15
  - supplementary_pit: taxable_profit * 0.15
expected:
  principal_pit: 144
  supplementary_pit: 1500
```

The nine additional predecessor examples (occasional work, three rental routes, property gains, FIFO, internet and gaming, foreign dividend credit, fine art and amateur sport, municipal surtax and the mid-year gambling change) remain [verbatim in the evidence appendix](../../../ledgers/montenegro-income-tax-evidence/retained-examples.md). The [additional controls](../../../ledgers/montenegro-income-tax-evidence/additional-controls.md) recompute the complete pausal table and the new form crosswalk.

## Ask the client first

1. Residence: domicile, centre of vital interests, days in Montenegro in 2026, and any posting abroad or digital-nomad status.
2. Which income classes: salary (and from how many payers), registered business as main or supplementary activity, occasional contracts, rent (and whether to tourists, with a licence), interest and dividends, sales of property, stakes or shares, sport, royalties, internet or gaming income, gambling winnings.
3. For a business: accounts, fixed-asset register, unused losses by year, advances paid, VAT registration, lump-sum decision, and any underdeveloped-municipality or other relief decision.
4. Municipality of activity or residence, and its surtax decision.
5. Who paid each receipt (legal person, entrepreneur or private individual) and what tax was withheld.
6. Foreign income and foreign tax paid, with proof and the treaty country.

## Sources

| Source | URL | Read on |
|---|---|---|
| Personal Income Tax Law, consolidated through 160/25 (Ministry of Finance publication), arts. 1 to 10a, 12 to 37s, 42 to 53v, 62 | https://wapi.gov.me/download/b8465a42-2073-4894-9be0-3b965c2f7195?version=1.0 | 2026-10-31 |
| Law amending the Personal Income Tax Law, Official Gazette 160/25, arts. 1 to 21 (application from 1 January 2026, art. 21) | https://wapi.gov.me/download/47bea12c-f250-4cdc-b481-3afc30fba94f?version=1.0 | 2026-10-31 |
| Law amending the Personal Income Tax Law, Official Gazette 70/26, arts. 1 to 3 (12% gambling rate) | https://www.sluzbenilist.me/propisi/394390/download | 2026-10-31 |
| Official Gazette record for 70/26: published 20.05.2026, in force 21.05.2026 | https://www.sluzbenilist.me/propisi/394390 | 2026-10-31 |
| Ministry of Finance, notice on taxation of gambling winnings, 5 January 2026 (bands from 1 January 2026) | https://www.gov.me/clanak/jasna-pravila-oporezivanja-dobitaka-od-igara-na-srecu-zakon-se-primjenjuje-jednako-na-sve | 2026-10-30 |
| Rulebook on the form and content of the annual PIT return (GPP-FL), through 103/2025, arts. 1 to 5 | https://wapi.gov.me/download/afb50b45-7e83-4dac-b69e-2a1e280d3ffc?version=1.0 | 2026-10-31 |
| Local Self-Government Financing Law, through 149/2025, arts. 8 and 9 (surtax) | https://wapi.gov.me/download/98dd2203-4c4e-4751-bbb9-9ad1e13564bd?version=1.0 | 2026-10-31 |
| Law on Contributions for Mandatory Social Insurance, through 160/2025, arts. 14, 15, 17 and 18 | https://wapi.gov.me/download/97253561-f373-4456-a024-b15f6596a0f2?version=1.0 | 2026-10-31 |
| VAT Law, consolidated through 12/26, arts. 24, 42 and 55 | https://wapi.gov.me/download/795cb7a3-2699-44bd-baa6-b11802121045?version=1.0 | 2026-10-31 |
| Tax Administration Law, Ministry consolidation published March 2026 (before 104/26), art. 95(1) (0.03% a day) | https://wapi.gov.me/download/2dd530ac-eec4-4d0c-9d8f-0c9e7ebc5b86?version=1.0 | 2026-10-31 |
| Law amending the Tax Administration Law, Official Gazette 104/26, arts. 20 and 26 (ECB + 3 points from 18 July 2026) | https://wapi.gov.me/download/c22f3c59-7e52-4213-bbe4-3cd9d8d3a373?version=1.0 | 2026-10-31 |
| Tax Administration decision on the default interest rate for 18 July to 31 December 2026 (5.4% a year) | https://wapi.gov.me/download/6d6ec964-3dd6-4588-b81a-a5affc153f6e?version=1.0 | 2026-10-31 |

| Pausal Rulebook, consolidated through 118/2024, arts. 2 to 7, scale, KPP and ZPO (Ministry publication 1 April 2026) | https://wapi.gov.me/download/13de63a3-660e-4cb4-bb77-b0b59e456834?version=1.0 | 2026-10-31 |
| GPP-FL amendment, Gazette 103/2025, arts. 1 to 4 and all printed schedules/instructions | https://www.sluzbenilist.me/propisi/385024/download | 2026-10-31 |
| Tax Administration, 2026 seasonal-business informator (IRMS, applications, pausal and separate surtax) | https://wapi.gov.me/download/16a44be5-b5f1-431e-952a-9251f90dfdc4?version=1.0 | 2026-10-31 |
| Tax Administration notice, 5 February 2026, annual pausal request accepted through 27 February 2026 on paper ZPO | https://www.gov.me/clanak/rok-za-podnosenje-zahtjeva-za-pausalno-oporezivanje-produzen-do-27-februara-2026-godine | 2026-10-31 |

[law]: https://wapi.gov.me/download/b8465a42-2073-4894-9be0-3b965c2f7195?version=1.0
[amend]: https://wapi.gov.me/download/47bea12c-f250-4cdc-b481-3afc30fba94f?version=1.0
[may]: https://www.sluzbenilist.me/propisi/394390/download
[mayrecord]: https://www.sluzbenilist.me/propisi/394390
[return]: https://wapi.gov.me/download/afb50b45-7e83-4dac-b69e-2a1e280d3ffc?version=1.0
[local]: https://wapi.gov.me/download/98dd2203-4c4e-4751-bbb9-9ad1e13564bd?version=1.0
[contrib]: https://wapi.gov.me/download/97253561-f373-4456-a024-b15f6596a0f2?version=1.0
[vat]: https://wapi.gov.me/download/795cb7a3-2699-44bd-baa6-b11802121045?version=1.0

[pausal]: https://wapi.gov.me/download/13de63a3-660e-4cb4-bb77-b0b59e456834?version=1.0
[gppforms]: https://www.sluzbenilist.me/propisi/385024/download
[seasonal]: https://wapi.gov.me/download/16a44be5-b5f1-431e-952a-9251f90dfdc4?version=1.0
[pausalnotice]: https://www.gov.me/clanak/rok-za-podnosenje-zahtjeva-za-pausalno-oporezivanje-produzen-do-27-februara-2026-godine

Not yet confirmed: live IRMS GPP-FL fields/acceptance rules and a 2026 return mapping for supplementary entrepreneurship, Montenegro advances already paid on foreign salary, country-level foreign-credit allocations, or foreign gambling after the mid-year rate change (the printed 2025 main calculation uses 15% for its pooled foreign-income line); corrected portal instructions for the documented A/A1/F/H contradictions and any same-country category-allocation rule for foreign credits; partial-year band proration and rounding (A's example rounds 8,400/365 to 23.01 before multiplying by 302, giving 6,949.02 rather than 6,950.14 at full precision); the PIT-specific rulebook classifying assets into depreciation groups (art. 23(8)); each municipality's current surtax rate (only the 13% and 15% caps are confirmed); the 2026 PIO annual ceiling (the old EUR 68,765 was a 2024 figure); the treatment of government grants in business income; the dual net minimum wage of EUR 670 and 800 and the employer Labour Fund and Chamber levies (see the payroll skill); the list of underdeveloped municipalities; and a September 2026 Government proposal to change salary taxation from 1 January 2027, not found enacted. The pausal scale and promulgated printed schedules are now retained, so their former source-access gaps are closed; the remaining ordinary return-mapping gaps keep IT-IND partial.

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
