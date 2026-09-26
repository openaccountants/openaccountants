---
name: iceland-income-tax
description: Use this skill whenever asked about Iceland (Ísland) personal income tax for self-employed individuals and employees. Trigger on phrases like "how much tax do I pay in Iceland", "skattframtal", "RSK 1.01", "income tax return Iceland", "staðgreiðsla", "reiknað endurgjald", "calculated remuneration", "persónuafsláttur", "personal tax credit", "útsvar", "municipal tax", "tryggingagjald", "lífeyrissjóður pension", "capital income tax 22%", "VSK / VAT registration", "Skatturinn", or any question about filing or computing income tax for a self-employed (sjálfstætt starfandi) or employed individual resident in Iceland. Also trigger when preparing or reviewing an annual return (skattframtal) or business income statement (rekstrarframtal RSK 4.11), computing deductible expenses, or advising on monthly withholding (staðgreiðsla). This skill covers the 3-bracket combined state + municipal income tax, personal tax credit, capital income tax, mandatory occupational pension, tryggingagjald, calculated remuneration, penalties, and interaction with VAT (VSK). ALWAYS read this skill before touching any Icelandic income tax work.
version: 0.1
jurisdiction: IS
tax_year: 2026
last_updated: 2026-09-25
authored_by: OpenAccountants team
review_status: pending_review
trust_label: By OpenAccountants
depends_on:
  - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Iceland income tax — employees and self-employed individuals, 2026

This method covers a resident individual's employment income, sole-trader income and ordinary private capital income for calendar 2026. Amounts are ISK. A return filed in 2026 normally reports 2025 income; the return for 2026 income is filed in 2027. Keep those periods separate. The published 2026 filing deadline is 13 March 2026 for the earlier income year; a 2027 filing deadline is not established by that notice. [Official source](https://www.skatturinn.is/english/individuals/filing-a-tax-return/)

## Ask the client first

- Obtain arrival/departure dates, foreign residence certificates, municipality, age, marital/cohabitation status and the spouse's income and credit use. Ordinary unlimited liability includes worldwide income; residence and treaty outcomes require facts, not an Icelandic bank account. [Official source](https://www.skatturinn.is/english/individuals/tax-liability/)
- Collect payslips, taxable benefits, employer statements, pension certificates and withholding records from every payer. A net bank salary is not gross taxable salary. [Official source](https://www.skatturinn.is/english/individuals/tax-liability/)
- For business, collect invoices and credit notes, platform gross-sales/fees reports, bank and card statements, cash sales, receivables/payables, inventory, VAT registration/returns, asset register, pension/payroll returns and prior losses. Establish whether the relationship is employment or independent business. [Official source](https://www.skatturinn.is/atvinnurekstur/ad-hefja-rekstur/stofna-rekstur/)
- Obtain domestic and foreign interest/dividend statements, investment purchase and disposal costs, year-end balances, capital tax withheld, rental contracts/registration and property use. Confirm whether securities qualify for the listed-market allowance. [Official source](https://www.skatturinn.is/einstaklingar/skattar-og-gjold/fjarmagnstekjuskattur/)

## The method, step by step

1. **Fix the taxpayer and period.** A stay of six months or more in a twelve-month period generally gives unlimited liability from arrival; shorter stays normally produce limited liability on Icelandic-source income. A former resident can remain liable for three years unless the foreign-tax-liability condition is proved. Check treaty residence and relief before calculating a cross-border final return. The full-year examples below assume ordinary unlimited liability throughout 2026. [Official source](https://www.skatturinn.is/english/individuals/tax-liability/)
2. **Build a reconciled income ledger.** Classify each receipt from its legal source and supporting document. Match invoices to gross platform sales, refunds, fees and net settlements. Identify transfers between own accounts, loans and capital contributions separately; a merchant name or bank description does not determine tax treatment. Reconcile opening cash/bank, movements and closing balances, then reconcile unpaid invoices and business liabilities. Establish the tax treatment of each grant or reimbursement from its conditions. [Official source](https://www.skatturinn.is/atvinnurekstur/ad-hefja-rekstur/stofna-rekstur/)
3. **Prepare the business result where applicable.** Start from business revenue, exclude collected VAT where applicable, and deduct substantiated business costs and permitted depreciation. Recoverable input VAT is not an income-tax expense; nonrecoverable VAT follows the underlying cost or asset. Calculate own remuneration separately, deduct it and employer costs in the business result, and carry remuneration plus the remaining taxable profit to the personal return. Do not tax turnover and profit again as additional personal income. [Income Tax Act, Articles 31 and 61](https://www.althingi.is/lagas/nuna/2003090.html) [Official source](https://www.skatturinn.is/atvinnurekstur/ad-hefja-rekstur/framtalsskil/)
4. **Compute personal earned-income tax.** Combine taxable employment benefits, calculated remuneration, taxable pensions/other income and business profit in their proper categories. Deduct eligible personal pension contributions once. Apply the annual state bands and actual municipal rate, then eligible credit. Reconcile withholding as a payment, not an expense. [Official source](https://www.skatturinn.is/einstaklingar/tekjur-og-fradraettir/idgjald-i-lifeyrissjodi/) [Official source](https://www.skatturinn.is/einstaklingar/helstutolur/2026)
5. **Compute capital income separately.** Distinguish private capital from business income, calculate gains from documented proceeds and tax basis, apply the specific allowance/exemption and reconcile capital withholding. Do not apply the personal credit to 2026 capital tax. [Official source](https://www.skatturinn.is/einstaklingar/skattar-og-gjold/fjarmagnstekjuskattur/) [Official source](https://www.stjornarradid.is/efst-a-baugi/frettir/stok-frett/2025/12/23/Skattabreytingar-a-arinu-2026/)
6. **Complete, submit and reconcile.** Check prefilled amounts against evidence, attach the correct business schedules, report foreign items and year-end assets/debts, submit and retain the acknowledgement. Compare the assessment with the return, withholding and approved relief; investigate differences before accepting the balance. [Official source](https://www.skatturinn.is/english/individuals/filing-a-tax-return/) [Official source](https://www.skatturinn.is/atvinnurekstur/ad-hefja-rekstur/framtalsskil/) [Official source](https://www.skatturinn.is/einstaklingar/framtal-og-alagning/alagningarsedill-og-forsendur/2026)

## Rates, personal credit and pension deductions

### Monthly withholding for 2026

The combined withholding rates include average municipal tax of 14.94%. They are not a promise that the final assessment uses that municipality's rate. Subtract qualifying pension contributions before applying the bands. Coordinate multiple employers so the lower band and personal credit are not used twice. [Official source](https://www.skatturinn.is/einstaklingar/stadgreidsla/stadgreidsla/2026) [Official source](https://www.skatturinn.is/english/individuals/tax-liability/)

| Monthly taxable income slice | Combined rate |
|---|---:|
| Up to 498,122 | 31.49% [Source](https://www.skatturinn.is/einstaklingar/stadgreidsla/stadgreidsla/2026) |
| Above 498,122 through 1,398,450 | 37.99% [Source](https://www.skatturinn.is/einstaklingar/stadgreidsla/stadgreidsla/2026) |
| Above 1,398,450 | 46.29% [Source](https://www.skatturinn.is/einstaklingar/stadgreidsla/stadgreidsla/2026) |

Source for the table: [Official source](https://www.skatturinn.is/einstaklingar/stadgreidsla/stadgreidsla/2026).

At assessment the municipal tax (útsvar) is charged at the rate of the municipality of legal domicile, on the same base as state income tax. The law allows a municipal rate of no more than 14.97% and no less than 12.44%, so a final bill can be higher or lower than the 14.94% withheld. A person domiciled in more than one municipality during the year pays municipal tax to each in proportion to the time lived there. [Act 4/1995, Articles 20, 21 and 23](https://www.althingi.is/lagas/nuna/1995004.html) [Official source](https://www.skatturinn.is/einstaklingar/stadgreidsla/stadgreidsla/2026)

The monthly personal credit is 72,492. Use the credit available for the taxpayer and period, accounting for other employers and earlier use. The credit is available to individuals domiciled in Iceland aged 16 or over; a person who turns 16 during the year gets the full credit for the whole year. Credit not used in one month accumulates and can be used later in the same year, but unused credit does not carry to the next year. [Official source](https://www.skatturinn.is/einstaklingar/stadgreidsla/personuafslattur/)

Mandatory employee pension contributions are deductible up to 4% of the contribution base, and qualifying regularly paid additional private-pension contributions up to another 4%. Both deductions require the contributions to be paid regularly. These deductions also apply to qualifying own remuneration; employer pension payments are a separate business cost. The employer withholding form calculates an employer counter-contribution of 11.5% against the 4% employee contribution; a different agreed rate can be entered. No contributions are due for an employee aged 70 or over, and children aged 15 or younger do not pay into a pension fund. [Official source](https://www.skatturinn.is/einstaklingar/stadgreidsla/stadgreidsla/2026) [Official source](https://www.skatturinn.is/einstaklingar/tekjur-og-fradraettir/idgjald-i-lifeyrissjodi/) [Employer notice 1/2026](https://www.skatturinn.is/media/2026/rsk_0601_1_2026.is.pdf)

### Annual 2026 computation

Use annual thresholds of 5,977,470 and 16,781,397, with state rates of 16.55%, 23.05% and 31.35% on successive slices; add the actual applicable municipal tax. The published annual personal credit is 869,898. Do not multiply rounded monthly thresholds or the monthly credit to manufacture annual figures. The annual credit is not a cash entitlement beyond the tax it can offset under the statutory ordering: it is deducted first from state income tax; any excess pays the same person's municipal tax; for jointly taxed spouses anything still unused is added to the other spouse's credit; whatever then remains lapses. [Official source](https://www.skatturinn.is/einstaklingar/helstutolur/2026) [Official source](https://www.skatturinn.is/media/2026/rsk_0601_1_2026.is.pdf) [Act, Articles 66–67](https://www.althingi.is/lagas/nuna/2003090.html) [Assessment rules](https://www.skatturinn.is/einstaklingar/framtal-og-alagning/alagningarsedill-og-forsendur/2026)

Unused personal credit transfers only between jointly taxed spouses. In 2026, 100% of a spouse's unused credit may be used in withholding, provided the employer is told. Married spouses living together are jointly taxed. Cohabiting partners are jointly taxed only if both ask the tax authority in writing, and their cohabitation is registered (or can be registered) in the national registry and they have or expect a child together or have lived together continuously for at least one year. Without joint taxation there is no transfer. From income year 2026 there is no transfer of unused middle-band capacity between spouses, and unused personal credit no longer reduces capital-income tax. Do not carry the old assessment-year 2026 rules into income year 2026. [Official source](https://www.skatturinn.is/einstaklingar/stadgreidsla/stadgreidsla/2026) [Official source](https://www.stjornarradid.is/efst-a-baugi/frettir/stok-frett/2025/12/23/Skattabreytingar-a-arinu-2026/) [Act, Articles 62, 66–67](https://www.althingi.is/lagas/nuna/2003090.html)

For a person resident for only part of the year, Article 69 sets the method: divide the tax base by the days resident and multiply by 365; calculate tax and personal credit as for a full-year resident; then divide the result by 365 and multiply by the days resident. Do not give a part-year resident the full annual credit, and check any treaty first. [Act, Article 69](https://www.althingi.is/lagas/nuna/2003090.html)

Children born in 2011 or later pay 6% on employment income above 300,000 in 2026 and receive no personal credit. Other child income generally belongs with the relevant parent's taxable income under the statutory rules; it is not automatically covered by this employment exemption. A child turning sixteen in the year enters the ordinary regime. [Official source](https://www.skatturinn.is/einstaklingar/helstutolur/2026) [Official source](https://www.skatturinn.is/einstaklingar/stadgreidsla/stadgreidsla/2026) [Official source](https://www.skatturinn.is/english/individuals/tax-liability/)

## Sole traders: remuneration, expenses and losses

Own remuneration (reiknað endurgjald) reflects the salary an unrelated person would receive for comparable work. Select the published 2026 occupation, staffing and work-scope category, record the facts and calculate the appropriate benchmark. It is not simply the cash drawn from the business. For example, category B5 for qualifying general business outside the specialist categories, run alone or with the stated small staffing complement, shows 933,000 monthly / 11,196,000 annually for the full-time benchmark. Do not apply B5 to a specialist covered by category A. [Official source](https://www.skatturinn.is/atvinnurekstur/stadgreidsla-og-reiknad-endurgjald/reiknad-endurgjald/2026)

Check these conditions on the benchmark before using it:
- **Start-up category.** Groups A to E each have a lower "starting activity" category (for example B9: 681,000 monthly / 8,172,000 annually) only for a person starting independent activity for the first time, working alone or with one employee, and only for one year from the start. A second business or a second year does not qualify. [Source](https://www.skatturinn.is/atvinnurekstur/stadgreidsla-og-reiknad-endurgjald/reiknad-endurgjald/2026)
- **Another salaried job.** A person who also holds another permanent paid job may reduce the benchmark by the amount by which the pay from that other job exceeds 50% of the benchmark, but never below 25% of the benchmark. This is permitted, not automatic. [Source](https://www.skatturinn.is/atvinnurekstur/stadgreidsla-og-reiknad-endurgjald/reiknad-endurgjald/2026)
- **Floor.** Own remuneration of a person selling their own or employees' work may never be lower than the pay of an employee in the business with comparable education, experience and work input. [Source](https://www.skatturinn.is/atvinnurekstur/stadgreidsla-og-reiknad-endurgjald/reiknad-endurgjald/2026)
- **Spouses.** Where jointly taxed spouses run a business together, each sets their own remuneration and the profit is split in proportion to those remunerations. Where only one runs it and the other works in it, the other's work is remunerated at arm's length and the profit belongs to the one running the business. [Source](https://www.skatturinn.is/atvinnurekstur/stadgreidsla-og-reiknad-endurgjald/reiknad-endurgjald/2026)
[Official source](https://www.skatturinn.is/atvinnurekstur/stadgreidsla-og-reiknad-endurgjald/reiknad-endurgjald/2026) [Act, Article 62](https://www.althingi.is/lagas/nuna/2003090.html)

A lower amount than the benchmark needs written explanations and supporting documents, and Skatturinn may depart from the minimum only on that basis. If Skatturinn does not accept a lower figure and raises it, the increase may not create a loss in the business beyond the year's ordinary depreciation; for an old-age or disability pensioner with their own business it may not create a loss at all. Benefits are added to the benchmark at their assessed value. [Official source](https://www.skatturinn.is/atvinnurekstur/stadgreidsla-og-reiknad-endurgjald/reiknad-endurgjald/2026)

Own remuneration of less than 700,000 a year falls outside withholding, and the startup guidance says an individual whose own remuneration does not exceed 700,000 for a full year need not register on the employer register. The remuneration still goes on the return and income and municipal tax are charged at assessment; the threshold is not an income-tax exemption. The two Skatturinn pages word the boundary differently ("less than" and "does not exceed"), so at exactly 700,000 confirm the treatment with Skatturinn. Separately, if the approved remuneration is so low that no withholding arises, the person may apply to file the own-remuneration return once a year; if approved, the personal credit must not be used against other income. [Official source](https://www.skatturinn.is/atvinnurekstur/stadgreidsla-og-reiknad-endurgjald/reiknad-endurgjald/2026) [Official source](https://www.skatturinn.is/atvinnurekstur/ad-hefja-rekstur/stofna-rekstur/)

Otherwise register the business and the applicable employer/VAT obligations before starting; the startup guidance requires notification at least eight days before commencement. Monthly payroll withholding has a due date on the first day of the following month and final payment date on the fifteenth. Check the actual registered filing arrangement and any applicable special rule. [Official source](https://www.skatturinn.is/atvinnurekstur/ad-hefja-rekstur/stofna-rekstur/)

General social security tax is 6.35% and its base includes wages/own remuneration plus employer pension contributions and taxable remuneration components under the rules. It is a business expense, not an employee pension deduction. [Employer-pension inclusion in the base](https://www.skatturinn.is/atvinnurekstur/ad-hefja-rekstur/stofna-rekstur/) For work in one's own business the base is the remuneration set for withholding, but Skatturinn's page states it may not be lower than 748,224 in annual income for full-time work. Wages of fishermen on fishing vessels carry an extra 0.65%, so 7.00% in total. If own remuneration and wages paid to others together stay below 504,000 in the year, the charge may be filed and paid once a year as if for December. Foreign social-security coverage or an A1 certificate requires applying the specific coverage decision and charge components; the page gives a reduced 0.293% rate for A1 workers for 2025 but no 2026 figure, so confirm the current rate, and do not set every employer charge to zero automatically. [Official source](https://www.skatturinn.is/atvinnurekstur/skattar-og-gjold/tryggingagjald)

Deduct only costs of earning, securing and maintaining business income supported by evidence, incurred from the start of the business until it ends. Costs that arise whether or not the person runs a business are private, even with occasional business use: own food, own clothing, a private phone and the owner's own housing costs are examples. [Act, Articles 31, 33–42 and 50](https://www.althingi.is/lagas/nuna/2003090.html) [Official source](https://www.skatturinn.is/atvinnurekstur/ad-hefja-rekstur/stofna-rekstur/)

- **Own home.** A sole trader cannot deduct rent for using their own residential property in the business, and a floor-area percentage of household rent, heating or electricity is not the test. Only a proven additional cost caused by the business (for example extra electricity or phone cost) may be deducted, and Skatturinn notes such amounts are usually small. [Source](https://www.skatturinn.is/atvinnurekstur/ad-hefja-rekstur/stofna-rekstur/)
- **Own car.** For a privately owned car used in the business, deduct the share of its running costs equal to business kilometres divided by total kilometres for the year. Keep all car-cost evidence and a record of total and business kilometres; without it there is no deduction. [Source](https://www.skatturinn.is/atvinnurekstur/ad-hefja-rekstur/stofna-rekstur/)
- **Travel.** A sole trader may not deduct per-diem (dagpeningar) amounts for their own business trips in Iceland; travel costs are deducted from invoices. For trips abroad, instead of deducting other costs besides accommodation and meals abroad from invoices, a fixed amount of 30% of the non-accommodation part of the official per diem may be deducted. [Source](https://www.skatturinn.is/atvinnurekstur/ad-hefja-rekstur/stofna-rekstur/)
- **Courses.** Courses that maintain skills in the person's current trade are deductible if the link to the income is explained. Basic education, general education, further study or study to gain a professional qualification is private. [Source](https://www.skatturinn.is/atvinnurekstur/ad-hefja-rekstur/stofna-rekstur/)
- **Gifts.** Gifts to organisations on Skatturinn's public-benefit register are deductible up to 1.5% of business income in the year given, and only if the recipient was registered when the gift was made. [Act, Article 31](https://www.althingi.is/lagas/nuna/2003090.html)
- Owner drawings and personal income tax do not become business expenses through the business bank account. A software or travel merchant match alone proves neither business connection nor the amount deductible. Capital equipment belongs in the asset register unless a specific immediate-expensing rule applies. [Source](https://www.skatturinn.is/atvinnurekstur/ad-hefja-rekstur/stofna-rekstur/)
[Official source](https://www.skatturinn.is/atvinnurekstur/ad-hefja-rekstur/stofna-rekstur/) [Act, Article 31](https://www.althingi.is/lagas/nuna/2003090.html)

For ordinary office equipment, the statutory depreciation range is 20–35%, normally on the reducing written-down value, beginning in the year first used to earn income. Passenger cars for fewer than nine people, other than taxis, use a different range: at least 10% and at most 20%. Other vehicles and other movable assets not listed elsewhere use 20–35%. In the year a business ends or is sold, its assets may not be depreciated and Article 39 immediate expensing is not available. A qualifying individual asset or asset group costing **less than 600,000** may be expensed immediately under Article 39; exactly 600,000 is not below that boundary. Do not split an asset group to evade the threshold. For the tangible assets covered by Article 42, scheduled depreciation must leave at least 10% of original cost as residual value. Apply the separate disposal rules; proceeds from an already fully expensed asset are income. Keep acquisition date, cost, recoverable VAT, first-use date, classification, chosen rate, opening value, depreciation and disposal evidence. [Act, Articles 33–42](https://www.althingi.is/lagas/nuna/2003090.html)

A sole trader's business loss does not reduce unrelated salary merely because both are on one return. Article 31 permits unused losses from the ten years preceding the income year, provided the loss and remaining balance were adequately reported when incurred. A substantial change in the business can prevent use unless justified by normal business purposes. Maintain a schedule by originating year, amounts used and remaining expiry; do not deduct an unsupported opening loss. [Act, Articles 31 and 61](https://www.althingi.is/lagas/nuna/2003090.html) [Official source](https://www.skatturinn.is/atvinnurekstur/ad-hefja-rekstur/framtalsskil/)

## Capital income, investments and rental receipts

Ordinary private capital income is taxed at 22% in 2026. The combined annual exemption of 300,000 for an individual (600,000 for eligible jointly assessed spouses) applies first to interest, then eligible dividends and then eligible share gains meeting the regulated-market conditions. It is not a blanket exemption for every private-company dividend or every gain. Preserve statements proving listing/market eligibility, basis, expenses, proceeds and withholding. Business investment income remains in the business regime where the law requires it. Capital income carries no municipal tax and does not push earned income into a higher band. Banks and paying companies withhold 22% from interest and dividends without applying the allowance; the allowance is given at assessment, which can produce a refund. Capital gains and rent have no withholding and are paid after assessment. For jointly taxed spouses, capital income is added together and taxed with the spouse whose employment income is higher. [Official source](https://www.skatturinn.is/einstaklingar/skattar-og-gjold/fjarmagnstekjuskattur/) [Act, Articles 62 and 66](https://www.althingi.is/lagas/nuna/2003090.html) [Official source](https://www.skatturinn.is/english/individuals/tax-liability/)

For qualified residential letting outside business, 25% of gross rent is exempt in 2026, so 75% is taxed at 22%. The conditions include a housing-law lease registered in the housing register and no more than two separately identified residential properties under the nonbusiness rule. Ordinary operating costs are not additionally deducted from this gross-rent basis. A specific offset for rent paid on the owner's own residence can apply where the rented-out property was originally acquired for own use; establish the conditions and use the rental schedule rather than subtracting all housing costs. [Official source](https://www.skatturinn.is/einstaklingar/fjarmagnstekjur/leigutekjur/) [Act, Articles 58a and 66](https://www.althingi.is/lagas/nuna/2003090.html)

Home accommodation must be registered with the district commissioner and have a registration number. It must concern the individual’s legal residence or one additional owned property used personally; ownership is not required for the legal residence itself. The two properties together may be let for no more than 90 days in the calendar year, with no more than five rooms or space for ten guests. Confirm the combined-day count, personal use, capacity and registration before applying capital treatment. [Official conditions](https://www.skatturinn.is/einstaklingar/fjarmagnstekjur/leigutekjur/)

Qualifying home accommodation within the 2,000,000 gross-receipts limit across the owners is a separate regime: capital tax applies to gross income without the residential-rent exemption. Failure of the applicable conditions can put the whole year's activity into business taxation. Commercial-premises letting and other business rental activity need the business computation. Do not grant the housing exemption solely because a platform calls a stay residential. [Official source](https://www.skatturinn.is/einstaklingar/fjarmagnstekjur/leigutekjur/) [Act, Article 58a](https://www.althingi.is/lagas/nuna/2003090.html)

Foreign income is not omitted because no Icelandic withholding occurred. Report the corresponding foreign income, year-end asset and foreign tax with documentary exchange-rate and treaty-relief support. A private asset disposal needs its own gain/exemption classification; this guide does not establish a universal exemption for property, cryptocurrency or private-company transactions. [Official source](https://www.skatturinn.is/english/individuals/tax-liability/) [Published return layout](https://www.skatturinn.is/media/rsk01/rsk_0110_2026.en.pdf)

## Filing schedules and assessment

Use the current year's live form instructions. The dedicated business-filing guidance currently specifies:

- RSK 4.10 only for small incidental activity with turnover below 2,000,000, no VAT registration, no depreciable business assets and no car-cost deduction. [Source](https://www.skatturinn.is/atvinnurekstur/ad-hefja-rekstur/framtalsskil/)
- RSK 4.11 for turnover from 2,000,000 through 30,000,000; VAT-registered activity below the lower threshold also uses the business statement. [Source](https://www.skatturinn.is/atvinnurekstur/ad-hefja-rekstur/framtalsskil/)
- RSK 1.04 above 30,000,000; smaller businesses may choose it. Agriculture has its separate schedule. [Source](https://www.skatturinn.is/atvinnurekstur/ad-hefja-rekstur/framtalsskil/)
- Conflict to resolve: Skatturinn's startup guidance still says that a sole trader whose business revenue exceeds 20,000,000 must file annual accounts and RSK 1.04 instead of the business statement. For turnover between 20,000,000 and 30,000,000, confirm the current requirement with Skatturinn or the live form instructions before choosing RSK 4.11. [Source](https://www.skatturinn.is/atvinnurekstur/ad-hefja-rekstur/stofna-rekstur/)
- RSK 4.05 reconciles remuneration, profit, assets, debts and prior losses into the personal return RSK 1.01. RSK 4.01 maintains depreciable assets. [Official source](https://www.skatturinn.is/atvinnurekstur/ad-hefja-rekstur/framtalsskil/)

Check the return sections for gross wages/benefits, own remuneration, business profit, pension deductions, foreign income, withholding, interest, dividends, disposal gains, rent, assets and debts. Reconcile gross earnings less personal pension deductions to the taxable base, business schedules to the ledger, and all payment credits to statements. The published 2026 form is a useful layout for **2025 income**; do not assume its field numbers or annual values remain unchanged for the 2027 return. [Official source](https://www.skatturinn.is/media/rsk01/rsk_0110_2026.en.pdf) [Official source](https://www.skatturinn.is/english/individuals/filing-a-tax-return/)

Obtain access through the tax portal with electronic identification or the appropriate web key; inspect and correct prefilled information, submit and keep the receipt. A bank-only estimate is not a completed return where gross income, expenses, basis or withholding remains unproved. Taxpayer and preparer must resolve those gaps before representing the return as complete. [Official source](https://www.skatturinn.is/english/individuals/filing-a-tax-return/) [Official source](https://www.skatturinn.is/atvinnurekstur/ad-hefja-rekstur/framtalsskil/)

On assessment, distinguish income/municipal/capital tax, payments on account, social charges and separate assessed fees or means-tested benefits. The published assessment for 2026 concerns 2025 income: its 2.5% adjustment, collection schedule and fee/benefit parameters must not be treated as a forecast of the 2027 assessment. Reconcile the actual assessment notice and collector's payment schedule. Benefits and housing-interest relief require their own household and assessment-year conditions; the ministry states that interest relief (vaxtabætur) is paid for the last time in 2026. [Official source](https://www.skatturinn.is/einstaklingar/framtal-og-alagning/alagningarsedill-og-forsendur/2026) [Official source](https://www.stjornarradid.is/efst-a-baugi/frettir/stok-frett/2025/12/23/Skattabreytingar-a-arinu-2026/)

Under the 2026 assessment rules (2025 income):
- The 2.5% adjustment applies both ways: to a refund of over-withheld tax and to unpaid income tax, municipal tax and capital-income tax. [Source](https://www.skatturinn.is/einstaklingar/framtal-og-alagning/alagningarsedill-og-forsendur/2026)
- A remaining balance is spread over seven due dates, 1 June to 1 December (the broadcasting fee over three), with no instalment below 5,000; the taxpayer may instead choose to settle everything on 1 June. Unpaid income tax on a self-employed person's own remuneration is already due before 1 June. [Source](https://www.skatturinn.is/einstaklingar/framtal-og-alagning/alagningarsedill-og-forsendur/2026)
- Two flat levies sit outside withholding: the broadcasting fee (útvarpsgjald) of 22,200 and the Senior Citizens' Construction Fund fee of 14,614, each charged on a person with a base (tax base plus capital-income base, with jointly taxed spouses each counting half the joint capital base) above 2,617,618. Only people aged 16 to 69 in the income year pay them; those 70 or over at the end of the income year, and old-age or disability pensioners living in care homes, are exempt. [Source](https://www.skatturinn.is/einstaklingar/framtal-og-alagning/alagningarsedill-og-forsendur/2026)
- These amounts belong to the 2026 assessment. Skatturinn ties the levy threshold to each year's tax-free threshold, which the ministry gives as 2,762,458 for 2026; the fee amounts for the 2027 assessment (2026 income) are not yet published, so check them before quoting a 2027 bill. [Source](https://www.stjornarradid.is/efst-a-baugi/frettir/stok-frett/2025/12/23/Skattabreytingar-a-arinu-2026/)
[Official source](https://www.skatturinn.is/einstaklingar/framtal-og-alagning/alagningarsedill-og-forsendur/2026) [Official source](https://www.skatturinn.is/einstaklingar/skattar-og-gjold/utvarpsgjald/) [Official source](https://www.stjornarradid.is/efst-a-baugi/frettir/stok-frett/2025/12/23/Skattabreytingar-a-arinu-2026/)

An individual may appeal within three months of the announced completion of assessment. A late return within the appeal period can be treated as an appeal. After the ordinary period, the authority can consider an amendment request reaching up to six years back from the request year, subject to new information/material-interest conditions; this is not an automatic six-year entitlement. Skatturinn's power to raise tax reaches the income of the six years before the year of reassessment, but only two years back if the taxpayer's return and attachments gave adequate information for a correct assessment. Preserve the original return, correction, documents, explanation and submission receipt. [Official source](https://www.skatturinn.is/einstaklingar/kaerur-og-malsmedferd/ferill-agreiningsmala)

Late or defective returns carry statutory surcharges on the tax base, not a flat fine. A person who files no return is assessed on an estimate set high enough not to understate the income, and Skatturinn may add up to 15% to the estimated bases. A return received after the deadline but before assessment is finished may carry only 0.5% per day of delay, capped at 10%. Defective or wrongly reported items may carry 25%, reduced to at most 15% if the taxpayer corrects them before assessment. The surcharge is cancelled if the taxpayer shows they were not at fault or were prevented by circumstances beyond their control. Intentional or grossly negligent understatement is a separate offence with fines of at least twice and up to ten times the tax evaded. [Act, Articles 96, 108 and 109](https://www.althingi.is/lagas/nuna/2003090.html) [Official source](https://www.skatturinn.is/einstaklingar/kaerur-og-malsmedferd/ferill-agreiningsmala)

Business accounting books and supporting records, including electronic records, are retained for seven years from the end of the relevant accounting year; annual accounts for twenty-five years. Preserve records supporting continuing asset values or disputed assessments as long as they remain needed. [Official retention guidance](https://www.skatturinn.is/atvinnurekstur/ad-hefja-rekstur/stofna-rekstur/)

## Worked cases

All amounts below are explicit hypothetical facts, not client data. Calculations retain decimals to show the method; use the portal's required rounding for filing.

### A — monthly salary and withholding

Gross salary 800,000; regularly paid deductible mandatory pension 32,000; no additional pension; full unused monthly credit. Taxable salary is 768,000. Tax is 498,122 × 31.49% + (768,000 − 498,122) × 37.99% − 72,492 = **186,893.27**. Net cash before other deductions is 800,000 − 32,000 − 186,893.27 = **581,106.73**. Do not report that net deposit as gross salary. [Official source](https://www.skatturinn.is/einstaklingar/stadgreidsla/stadgreidsla/2026) [Official source](https://www.skatturinn.is/einstaklingar/tekjur-og-fradraettir/idgjald-i-lifeyrissjodi/)

### B — annual salary, separate annual thresholds

Assume full-year taxable earned income of 9,216,000 after eligible pension deductions, actual municipal rate 14.94%, full annual credit and no other items. State tax is 5,977,470 × 16.55% + (9,216,000 − 5,977,470) × 23.05% = **1,735,752.45**. Municipal tax is **1,376,870.40**. Less annual credit 869,898 gives **2,242,724.85** before payment credits. Actual withholding, rather than twelve times an illustrative rounded month, is reconciled against this amount. [Official source](https://www.skatturinn.is/einstaklingar/helstutolur/2026) [Official source](https://www.skatturinn.is/media/2026/rsk_0601_1_2026.is.pdf)

### C — business income without double counting

Assume 20,000,000 revenue excluding VAT, 4,000,000 other deductible costs, 11,196,000 properly selected full-year B5 remuneration, and employer pension of 1,287,540 under the taxpayer's documented pension arrangement. Social tax is (11,196,000 + 1,287,540) × 6.35% = **792,704.79**. Residual business profit is **2,723,755.21**. Personal income before the employee pension deduction is remuneration plus residual profit = **13,919,755.21**. Deduct qualifying employee pension once; do not add the 20,000,000 turnover again. The assumed employer pension is a case input, not a universal rate determination. [Employer-pension base](https://www.skatturinn.is/atvinnurekstur/ad-hefja-rekstur/stofna-rekstur/) [Official source](https://www.skatturinn.is/atvinnurekstur/stadgreidsla-og-reiknad-endurgjald/reiknad-endurgjald/2026) [Official source](https://www.skatturinn.is/atvinnurekstur/skattar-og-gjold/tryggingagjald) [Act, Articles 31 and 61](https://www.althingi.is/lagas/nuna/2003090.html)

### D — interest, eligible listed dividends and an ineligible dividend

Single person: interest 200,000, eligible listed dividends 180,000 and private-company dividends 100,000. The 300,000 allowance absorbs the interest and 100,000 of eligible dividends. Taxable capital is 80,000 + 100,000 = **180,000**; tax is **39,600**. Reconcile capital withholding separately. Unused earned-income personal credit cannot erase this 2026 capital tax. [Official source](https://www.skatturinn.is/einstaklingar/skattar-og-gjold/fjarmagnstekjuskattur/) [Act, Articles 66–67](https://www.althingi.is/lagas/nuna/2003090.html) [Official source](https://www.stjornarradid.is/efst-a-baugi/frettir/stok-frett/2025/12/23/Skattabreytingar-a-arinu-2026/)

### E — qualified residential rent

Gross rent 2,400,000 from a qualifying registered nonbusiness residential lease; no special rent-paid offset. Taxable rent is 2,400,000 × 75% = **1,800,000**, and tax is **396,000**. Maintenance of 100,000 does not produce an extra deduction in this gross-rent calculation. [Official source](https://www.skatturinn.is/einstaklingar/fjarmagnstekjur/leigutekjur/) [Act, Article 66](https://www.althingi.is/lagas/nuna/2003090.html)

### F — child employment boundary

A child born in 2011 earns 500,000 from employment in 2026. Tax is (500,000 − 300,000) × 6% = **12,000**, with no personal credit. Employment earnings exactly at the 300,000 exemption give zero under this rule. Bank interest still requires the separate parent/child income rules. [Official source](https://www.skatturinn.is/einstaklingar/helstutolur/2026) [Official source](https://www.skatturinn.is/english/individuals/tax-liability/)

### G — asset boundary and depreciation

A qualifying business asset costing 599,999 may use Article 39 immediate expensing. A qualifying office asset costing exactly 600,000 does not satisfy that less-than threshold. If first used in this year and the taxpayer chooses the permitted 20% ordinary depreciation rate, the first depreciation is **120,000** and closing tax value **480,000**, before any other applicable adjustments. [Act, Articles 33–42](https://www.althingi.is/lagas/nuna/2003090.html)

### H — platform settlement reconciliation

Invoices total 1,000,000 excluding VAT; a platform retains documented business fees of 30,000 and remits 970,000. Record gross revenue **1,000,000** and eligible expense **30,000**, not revenue 970,000 plus a second fee deduction. A separate 200,000 transfer between the taxpayer's own accounts is reconciled as a transfer, not a new sale. Classification must agree with invoices, platform reports and both bank entries. [Act, Article 31](https://www.althingi.is/lagas/nuna/2003090.html) [Official source](https://www.skatturinn.is/atvinnurekstur/ad-hefja-rekstur/stofna-rekstur/)

### I — form selection and correction boundary

An incidental activity below 2,000,000 turnover that owns depreciable business equipment fails the conditions for RSK 4.10. Prepare the appropriate fuller business statement and asset register. An omitted foreign-interest statement discovered after assessment requires recomputing the affected income and payment credits and submitting an appeal/correction through the applicable route; changing a spreadsheet alone does not amend the assessed return. [Official source](https://www.skatturinn.is/atvinnurekstur/ad-hefja-rekstur/framtalsskil/) [Official source](https://www.skatturinn.is/einstaklingar/kaerur-og-malsmedferd/ferill-agreiningsmala)

### J — home-accommodation boundaries

Assume registered personally used accommodation, four rooms/eight guests, combined letting of 90 days across the permitted properties and exactly 2,000,000 annual gross receipts across all owners. Subject to the other stated conditions, this meets the stated day/receipts ceilings; capital tax on gross receipts is **440,000**, without the residential-rent exemption. A ninety-first combined letting day fails the home-accommodation conditions. Receipts above the ceiling likewise put the whole year into business taxation, even where each co-owner individually receives less than the ceiling. [Official conditions](https://www.skatturinn.is/einstaklingar/fjarmagnstekjur/leigutekjur/)

### K — ordinary depreciation floor

Assume a tangible office asset with original cost 600,000, opening tax value 65,000 and a chosen 20% annual depreciation rate. The uncapped charge is 13,000, but the 10% original-cost floor is 60,000. Permitted ordinary depreciation is therefore **5,000**, leaving **60,000**; this is a continuing-use example, not an asset disposal. [Act, Articles 37 and 42](https://www.althingi.is/lagas/nuna/2003090.html)

### L — loss vintage

For income year 2026, the ordinary ten-preceding-years window covers losses originating in 2016 through 2025. A 2015 loss is outside that window. A 2016 loss needs the original reporting, unused-balance and business-continuity conditions; its age alone does not prove deductibility. [Act, Article 31(8)](https://www.althingi.is/lagas/nuna/2003090.html)

### M — working from the owner's own flat

A sole trader works from a room in the flat they own and proposes to deduct a notional rent of 480,000 for the room. That rent is not deductible, and neither is a floor-area share of household heating. The documented extra electricity caused by the business, 36,000, is deductible. The deduction is **36,000**, not 480,000. [Official source](https://www.skatturinn.is/atvinnurekstur/ad-hefja-rekstur/stofna-rekstur/)

### N — no return, or a late return

No return is filed and Skatturinn estimates the earned-income tax base at 9,000,000. It may add up to 15%, giving an estimated base of up to **10,350,000** before tax is calculated. If the return had instead arrived 8 days after the deadline but before assessment was finished, the surcharge could be at most 8 × 0.5% = **4%** of the bases (never more than 10%), and none if the taxpayer shows they were not at fault. [Act, Article 108](https://www.althingi.is/lagas/nuna/2003090.html)

### O — transferring a spouse's unused credit

Married spouses living together; one has no income in 2026 and uses no credit. The earning spouse may tell the employer to use 100% of the other spouse's credit as well, so the credit used in monthly withholding can be up to 72,492 × 2 = **144,984**, limited to the tax calculated. At assessment the non-earning spouse's unused annual credit of 869,898 is added to the earning spouse's credit. Had they been unregistered cohabitants who never asked for joint taxation, there would be no transfer. [Official source](https://www.skatturinn.is/einstaklingar/stadgreidsla/stadgreidsla/2026) [Act, Articles 62 and 67](https://www.althingi.is/lagas/nuna/2003090.html)

### P — own remuneration with another salaried job

A sole trader in category B5 (benchmark 11,196,000) also holds a permanent salaried job paying 8,000,000 a year. Half the benchmark is 5,598,000, so the permitted reduction is 8,000,000 − 5,598,000 = 2,402,000 and the reduced benchmark is **8,794,000**. The floor, 25% of the benchmark, is 2,799,000, so the floor does not bite here. The reduction is optional and needs the facts documented. [Official source](https://www.skatturinn.is/atvinnurekstur/stadgreidsla-og-reiknad-endurgjald/reiknad-endurgjald/2026)

### Q — cars

A privately owned car has running costs of 900,000 in the year and the log shows 6,000 business kilometres out of 20,000 in total. The business share is 30%, so the deduction is **270,000**; with no kilometre record the deduction is nil. A passenger car held as a business asset is depreciated at 10–20%, not the 20–35% used for office equipment. [Official source](https://www.skatturinn.is/atvinnurekstur/ad-hefja-rekstur/stofna-rekstur/) [Act, Article 37](https://www.althingi.is/lagas/nuna/2003090.html)

## When to refuse or refer

- Do not give a final filing figure when residence, the municipality, gross remuneration, pension eligibility, prior losses or investment basis is missing. Identify the exact missing evidence and continue the supported parts.
- Obtain specialist resolution for conflicting treaty residence, foreign social-security coverage, cross-border business establishments, business incorporation/cessation, special pension arrangements or disputed remuneration classification.
- Refer a foreign expert who may qualify for the Article 30 relief (a deduction of 25% of employment income for the first three years; it needs an employer based in Iceland, no residence in Iceland in the previous 60 months, scarce expertise, and a written application to the approving committee no later than three months after starting work); this guide does not apply it. [Act, Article 30](https://www.althingi.is/lagas/nuna/2003090.html)
- Do not apply ordinary private-capital or rental shortcuts to a transaction whose business, property, crypto or exemption classification is unproved. Preserve the transaction and calculate the established ordinary categories while resolving that branch.
- Do not submit an estimate as a complete reconciled return or call an AI/source review professional attestation.

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
