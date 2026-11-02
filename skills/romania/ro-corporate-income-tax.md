---
name: ro-corporate-income-tax
description: "Use this skill for Romanian company tax in tax year 2026 (calendar year): who pays profit tax (impozit pe profit) and who may use the micro-enterprise turnover tax (impozit pe veniturile microîntreprinderilor). Covers the 16% profit tax rate, the 1% micro tax with its EUR 100,000 revenue ceiling and one-employee rule, the minimum turnover tax (IMCA) for companies above EUR 50 million at 0.5% for 2026 and its end on 31 December 2026, the taxable base, limited and non-deductible expenses, the sponsorship credit, losses (5 years, 70% cap), the interest limit (30% of EBITDA, EUR 1 million safe harbour), quarterly payments, the D101 return due 25 June, 16% dividend tax, and interest and penalties. Trigger phrases: Romanian corporate tax, impozit pe profit, microintreprindere 2026, D101, IMCA, SRL tax Romania. Out of scope: ro-cross-border, ro-income-tax, ro-payroll-social, ro-cas-cass, ro-vat-return, ro-company-formation."
version: 0.2
jurisdiction: RO
tax_year: 2026
last_updated: 2026-10-31
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Romania company tax: profit tax and micro-enterprise tax (2026)

A Romanian company pays one of two taxes. The default is profit tax at 16% of taxable profit (Fiscal Code Title II). A small company that meets the micro-enterprise conditions may instead pay 1% of its revenue (Title III). This skill covers both, plus the minimum turnover tax for large companies, the dividend tax a company withholds, and the filing calendar.

The law is Legea 227/2015 (Codul fiscal, "the Fiscal Code") and Legea 207/2015 (Codul de procedură fiscală, "the Procedure Code"). Every article below was read on 23 October 2026 in ANAF's consolidated texts, both shown as last updated by Legea 170/2026. ANAF notes these consolidations are not an official republication. The 2026 changes read for this skill come from OUG 156/2024 (micro revenue ceiling cut to EUR 100,000 from 1 January 2026), Legea 141/2025 (dividend tax 16%), OUG 89/2025 (single 1% micro rate and the 0.5% IMCA rate for 2026, both from 1 January 2026), Ordonanța 6/2026 (repeal of the art. 25^1 cap) and OUG 8/2026 (micro rules, the D101 deadline, the first-quarter payment). Superscript article numbers are written as 18^1, 40^2 and so on.

Related skills: ro-cross-border (residence of companies, exit tax, withholding on payments abroad, EU directive relief), ro-payroll-social (employer payroll), ro-vat-return (VAT), ro-company-formation (setting up an SRL), ro-tax-overview (the whole system). There is no Romanian transfer pricing skill yet.

## Who this applies to

**Profit tax payers** (art. 13(1)):
- Romanian legal persons, such as an SRL or SA;
- foreign companies with a permanent establishment in Romania, on the profit of that establishment;
- foreign companies resident in Romania because their place of effective management is here (see ro-cross-border);
- foreign companies with the income listed in art. 12(h), such as gains on Romanian real estate or on shares in a Romanian company;
- European companies (such as an SE) with a registered office in Romania.

A resident is taxed on worldwide profit. A permanent establishment is taxed on the profit attributable to it.

**Outside profit tax** (art. 13(2)): the State Treasury, the National Bank, public institutions (except their economic activities), the Romanian Academy and listed guarantee funds. Non-profit bodies, unions and religious units have special rules in art. 15 and are not covered here.

**Micro-enterprise tax** (art. 47 and 48). The regime is optional (art. 48(1)). A Romanian legal person may opt for it for 2026 if on 31 December 2025 it met all of these (art. 47(1)):
1. 2025 revenue not above the RON equivalent of EUR 100,000, counted together with the revenue of linked enterprises (art. 47(1)(c) and (1^1); art. 54(3)). The revenue counted is turnover as defined in the accounting rules (art. 47(1^1) and art. 54(1)). The euro test uses the exchange rate at the close of the financial year in which the revenue was recorded (art. 47(1)(c));
2. its capital is held by persons other than the state and local authorities;
3. it is not in dissolution followed by liquidation;
4. it has at least one employee (art. 47(1)(g)). "Employee" means a full-time employment contract. Part-time contracts that add up to one full-time post count, and so does a director or administrator under a mandate contract paid at least the national gross minimum wage (art. 51(4));
5. any shareholder holding more than 25% has chosen this company as the only one of their companies to use the micro regime (art. 47(1)(h) and (4));
6. it filed its annual financial statements on time. For 2026, filing by 31 March 2026 counts as on time (art. 48(2)).

"Linked enterprise" (art. 47(1^1)) covers four cases:
- the company holds more than 25% of another Romanian company;
- another Romanian company holds more than 25% of it;
- one person holds more than 25% of both;
- a shareholder holding more than 25% also runs a business as a PFA or sole trader.

The linked revenue is added in.

Banks, insurers and reinsurers, capital-market firms and their intermediaries, gambling operators, oil and gas exploration and production, and a few state funds may not use the micro regime (art. 47(3)).

A new company may opt from its first year if the shareholder conditions are met at registration and it hires an employee within 90 days (art. 48(3)).

**Leaving the micro regime in the year** (art. 52). A micro-enterprise pays profit tax from the quarter in which:
- cumulative turnover for the year goes above EUR 100,000 (art. 52(1) and art. 54(1)). If the company sells more than one fixed asset from any subgroup, or more than one plot of land, in the year, the proceeds are added to turnover for this test (art. 54(1)). The euro test uses the exchange rate at the close of the previous financial year (art. 52(5));
- it fails to file its financial statements on time (art. 52(2));
- it starts an excluded activity (art. 52(4)).

Losing the only employee moves the company to profit tax from the next quarter, unless a new employee is hired within 30 days (art. 52(3)). Profit tax is then computed on revenue and expenses from the start of that quarter (art. 52(6)).

## Rates, bands and thresholds

All rows come from the [ANAF consolidated Fiscal Code](https://static.anaf.ro/static/10/Anaf/legislatie/Cod_fiscal_norme_2023.htm) unless another source is named.

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| Profit tax rate | 16% of taxable profit | 2026 | art. 17, ANAF consolidated Fiscal Code |
| Night bars, night clubs, discos, casinos | the higher of 16% of profit and 5% of the revenue from these activities | 2026 | art. 18, same page |
| Minimum turnover tax (IMCA), companies with prior-year turnover above EUR 50,000,000 | 0.5% x (total revenue minus listed revenue minus new fixed-asset investment minus depreciation on assets from 2024); paid where higher than profit tax | 2026 (the rule ends 31 December 2026) | art. 18^1(1), (3), (16) and (17), same page; [OUG 89/2025, art. I point 1 (ANAF copy)](https://static.anaf.ro/static/10/Anaf/legislatie/OUG_89_2025.pdf) |
| Bank turnover tax, on top of profit tax | 4% of listed revenue (2% for banks below 0.2% market share) | 2026 | art. 46^1(1)(b) and (c), same page |
| Micro-enterprise tax rate | 1% of revenue | 2026 | art. 51(1), same page; [OUG 89/2025, art. I points 4 and 5, in force 1 January 2026 (art. II(1))](https://static.anaf.ro/static/10/Anaf/legislatie/OUG_89_2025.pdf) |
| Micro-enterprise revenue ceiling | EUR 100,000 (RON equivalent), linked enterprises included | 2026 | art. 47(1)(c), art. 52(1) and art. 54(3), same page; [OUG 156/2024 (ANAF copy)](https://static.anaf.ro/static/10/Anaf/legislatie/OUG_156_2024.pdf) set EUR 250,000 for 2025 and EUR 100,000 from 1 January 2026; [OUG 8/2026, art. 6 points 15 and 20 (ANAF copy)](https://static.anaf.ro/static/10/Anaf/legislatie/OUG_8_2026.pdf) restated it |
| Tax loss carry-forward | 5 years, set against at most 70% of each year's taxable profit | 2026 | art. 31(1) and (8), same page |
| Interest limit: deductible exceeding borrowing costs | EUR 1,000,000 a year (EUR 500,000 for affiliated-party debt not financing listed assets), plus 30% of tax EBITDA; excess carried forward without time limit | 2026 | art. 40^2(1), (4) and (7), same page |
| Sponsorship credit | sponsorship deducted from profit tax up to the lower of 0.75% of turnover and 20% of profit tax | 2026 | art. 25(4)(i), same page |
| Protocol (entertainment) expenses | deductible up to 2% of accounting profit plus profit tax and protocol expenses | 2026 | art. 25(3)(a), same page |
| Social expenses | deductible up to 5% of salary costs | 2026 | art. 25(3)(b), same page |
| Cars not used only for business (up to 3,500 kg, up to 9 seats) | 50% of running costs deductible | 2026 | art. 25(3)(l), same page |
| Legal reserve | deductible up to 5% of accounting profit before profit tax, until it reaches one fifth of share capital | 2026 | art. 26(1)(a), same page |
| Depreciable fixed asset threshold | tax value of RON 5,000 or more | 2026 | art. 28(2)(b), same page |
| Dividend tax withheld on dividends paid to a Romanian company | 16% on dividends distributed from 1 January 2026 (10% stays on dividends distributed in 2025, including interim dividends). Nil where the recipient has held at least 10% for one full year and both companies pay profit tax | 2026 | art. 43(2) and (4), same page; [Legea 141/2025, art. II point 1 and art. VII(1)(a) and (2) (ANAF copy)](https://static.anaf.ro/static/10/Anaf/legislatie/L_141_2025.pdf) |
| Dividend tax on dividends paid to resident individuals | 16%, final, on dividends distributed from 1 January 2026 | 2026 | art. 97(7), same page; Legea 141/2025 art. VII(1)(c) |
| Withholding on dividends paid to non-residents | 16% | 2026 | art. 224(4)(b), same page |
| Late-payment interest | 0.02% a day | 2026 | Procedure Code art. 174(5), [ANAF consolidated Procedure Code](https://static.anaf.ro/static/10/Anaf/cod_procedura/Cod_Procedura_Fiscala_2023.htm) |
| Late-payment penalty | 0.01% a day | 2026 | Procedure Code art. 176(2), same page |
| Under-declaration penalty | 0.08% a day on tax set by ANAF that was not declared or declared wrongly | 2026 | Procedure Code art. 181(1), same page |

## The taxable base

**Profit tax** (art. 19(1)). Start from accounting revenue minus accounting expenses. Subtract non-taxable income and tax deductions. Add back non-deductible expenses. Subtract losses brought forward. The result is computed quarterly or yearly, cumulative from the start of the year (art. 19(2)). Transactions between affiliated persons must be at market value (art. 19(6)).

**The tax year** is the calendar year (art. 16(1)). A company with a different financial year may opt for a matching tax year, notified within 15 days of its start (art. 16(5)).

**Main non-taxable income** (art. 23 and 24):
- dividends from a Romanian company (art. 23(a));
- dividends from a company in a treaty state outside the EU, where at least 10% is held for an unbroken year (art. 23(b));
- dividends from an EU subsidiary under the Parent-Subsidiary Directive conditions (art. 24);
- gains on selling or revaluing shares, and liquidation proceeds, where at least 10% has been held for an unbroken year in a Romanian company or one in a treaty state (art. 23(i) and (j));
- reversals of expenses and provisions that were not deducted (art. 23(d)).

**Deductible expenses** are those incurred for the business (art. 25(1)), including salaries (art. 25(2)).

**Limited deductions** (art. 25(3)), the main ones:
- protocol, at 2%;
- social expenses, at 5% of salaries;
- 50% of the running costs of cars not used only for business. Depreciation is not part of this limit. Costs are fully deductible for vehicles used only for emergency, security or courier services, by sales and purchasing agents, for paid passenger transport including taxis, for paid services including rental and driving schools, or held as goods for sale. Managers' cars are limited to one car per person (art. 25(3)(m));
- 50% of the running costs of a registered office in a private home also used privately (art. 25(3)(k));
- provisions, within art. 26. For example, 30% of a trade-debt allowance where the conditions are met (art. 26(1)(c));
- interest, within art. 40^2;
- depreciation, within art. 28.

**Non-deductible expenses** (art. 25(4)), the main ones:
- profit tax itself, foreign profit tax, and tax the company should have withheld from non-residents but did not;
- interest, late-payment penalties and fines owed to Romanian or foreign authorities;
- missing or damaged stock and assets not charged to anyone, unless the listed conditions apply;
- expenses linked to non-taxable income;
- management, consultancy and similar services from a state with no exchange-of-information instrument, where the transaction is artificial;
- transactions without an economic purpose with a state on the EU list of non-cooperative jurisdictions;
- sponsorship (handled as a credit, below);
- invoices from a taxpayer declared inactive;
- dues to non-governmental and professional bodies above EUR 4,000 a year;
- the minimum turnover tax and the bank and oil-and-gas turnover taxes (art. 25(4)(u) and (v)).

**The art. 25^1 cap is gone in 2026.** Art. 25^1 used to cap certain costs, including intra-group ones. Ordonanța 6/2026 repealed it. Costs that fell under it follow the general art. 25 rules from the first quarter of 2026 (OG 6/2026 art. V, as noted in the consolidated text).

**Sponsorship credit** (art. 25(4)(i)). Sponsorship and patronage are not deducted as expenses. Instead the company takes the amount off its profit tax, up to the lower of 0.75% of turnover and 20% of the profit tax due. A gift to a non-profit body or religious unit counts only if the recipient was on ANAF's register of eligible entities when the contract was signed (art. 25(4)(i) and (4^1)). Where the limit is not used in full, the company may redirect profit tax to sponsorship by the D101 deadline (art. 42(4)). It must also file an information return on the recipients (art. 42(3)). Micro-enterprises no longer get a sponsorship credit: 2023 was the last year carried-forward amounts could be used (art. 56(25)).

**Losses** (art. 31). A tax loss from 2024 onwards is carried forward for 5 consecutive years. Each year it can use up at most 70% of that year's taxable profit, oldest loss first. Losses from before 2024 that were still open on 31 December 2023 keep the rest of their 7 years, but also under the 70% cap (art. 31(7)). Both kinds share one 70% cap (art. 31(8)). The law gives no carry-back. Losses pass on mergers and divisions in proportion to the assets moved (art. 31(2)). A company coming back from the micro regime recovers its earlier profit-tax losses under the same rules (art. 31(5)).

**Interest limit** (art. 40^2). "Exceeding borrowing costs" are interest and similar costs minus interest and similar income. They are deductible up to EUR 1,000,000 a year. Above that, the extra is deductible up to 30% of the tax EBITDA base (art. 40^2(1), (2) and (4)). Two points:
- within the EUR 1,000,000, net costs from affiliated-party debt that does not finance the listed assets are capped at EUR 500,000;
- a standalone company (not in a consolidated group, with no associated enterprise and no permanent establishment) deducts all of it (art. 40^2(5)).

What is not deducted carries forward without time limit (art. 40^2(7)).

**Reinvested profit** (art. 22). Profit invested in new technological equipment, production assets, computers, cash registers and software is exempt, up to the profit tax due for the period the assets are put into use. The exempt amount must go to reserves (art. 22(5)).

**Research and development** (art. 20 and 20^1). Either an extra 50% deduction of eligible R&D costs, or a tax credit of 10% of eligible R&D costs taken off profit tax (art. 20^1(2), inserted by OUG 8/2026), not both.

**Super-accelerated depreciation for 2026** (art. 28(8^1)). New technological equipment, machines and tools (subgroup 2.1) and animals and plantations (subgroup 2.4) bought or made and put into use in 2026 may be depreciated up to 65% of their tax value in the first year.

**Minimum turnover tax (IMCA)** (art. 18^1). A company whose turnover in the previous year was above EUR 50,000,000 compares its profit tax with IMCA = 0.5% x (VT - Vs - I - A) for 2026:
- VT is total revenue;
- Vs is the listed revenue taken out: non-taxable income, stock and work-in-progress movements, own-built assets, subsidies, insurance payouts for stock and assets, and excise duties;
- I is fixed assets under construction recorded from 2024;
- A is accounting depreciation on assets acquired from 2024.

If the profit tax (after sponsorship) is lower, the company pays IMCA. Payers of advance quarterly instalments compare IMCA with those instalments in quarters I to III (art. 18^1(6)). Sponsorship can reduce IMCA within the same 0.75% and 20% limits (art. 18^1(10)). Energy distributors and suppliers with more than 95% of revenue from that business are outside IMCA (art. 18^1(14)). IMCA itself is not deductible.

**The IMCA rule ends on 31 December 2026** (or on the last day of a modified year ending in 2027) (art. 18^1(17), inserted by OUG 89/2025 art. I point 1). The oil-and-gas turnover tax in art. 46^2 ends on the same date (art. 46^2(10)).

**Micro-enterprise base** (art. 53). Revenue from any source, minus:
- stock and work-in-progress movements;
- own-built assets;
- subsidies;
- reversals of provisions not deducted;
- insurance payouts for stock and assets;
- foreign-exchange gains and gains on FX-indexed balances;
- discounts granted after invoicing;
- dividends from a Romanian company or a qualifying EU subsidiary;
- foreign income already taxed under a treaty.

Discounts received after invoicing are added back. In the fourth quarter, net FX gains for the year are added back. Some released reserves are added back too (art. 53(2)). A micro-enterprise still keeps tax depreciation records and withholds dividend tax (art. 57).

**Tax groups** (art. 42^1 to 42^11). Romanian companies with at least 75% common ownership, held for an unbroken year, may opt to consolidate their profit tax for 5 years. The application is filed at least 60 days before the start (art. 42^3). Micro-enterprises cannot join (art. 42^3(2)(e)).

## Deadlines and filing

| Obligation | Deadline | Form | Source |
|---|---|---|---|
| Quarterly profit tax (default system) | 25th of the month after each of quarters I to III (25 April, 25 July, 25 October 2026); the year is settled by the D101 deadline | D100 | art. 41(1); [ANAF form 100 page](https://static.anaf.ro/static/10/Anaf/Declaratii_R/100.html) |
| Annual system with advance payments (optional, at least 2 years; notified by 31 January) | advance payments by the 25th after quarters I to III, and the fourth by 25 December. Each is one quarter of last year's profit tax, uprated by the CPI. From 2026 the quarter I payment is 16% of the quarter I accounting profit | D100 | art. 41(2), (3), (8) and (10^1) |
| Annual profit tax return and final payment for 2026 | 25 June 2027 (modified year: the 25th of the sixth month after year end) | D101 | art. 42(1) and (2); art. 45(21^4) |
| Sponsorship information return and redirection form | by the D101 deadline | ANAF forms | art. 42(3) and (4) |
| Opting into the micro regime | by 31 March 2026 | registration mention | art. 55(2) |
| Micro-enterprise tax | 25th of the month after each quarter (25 April, 25 July, 25 October 2026, 25 January 2027) | D100 | art. 56(1) and (2) |
| Leaving the micro regime | notify under the Procedure Code; on exit by option or for failing art. 47, by 31 March of the next year | registration mention | art. 55(1), (3) and (5) |
| Dividend tax withheld | 25th of the month after the dividend is paid; dividends approved but unpaid by year end, by 25 January of the next year | D100 | art. 43(2) and (3); art. 97(7) |

Banks must use the annual system with advance payments (art. 41(4)). A company that in the previous year was newly set up, had a tax loss or owed no profit tax, was dormant, or paid micro tax must use the quarterly system that year (art. 41(6)). A company dissolved with liquidation files and pays by the date it files its financial statements (art. 41(16)).

Returns are filed electronically with ANAF. The D101 model for years ending in 2024 or later is approved by OPANAF 206/2025 ([ANAF form 101 page](https://static.anaf.ro/static/10/Anaf/Declaratii_R/101.html)).

## Penalties and interest

From the [ANAF consolidated Procedure Code](https://static.anaf.ro/static/10/Anaf/cod_procedura/Cod_Procedura_Fiscala_2023.htm):

- **Late-payment interest:** 0.02% for each day late, from the day after the due date to the day of payment (art. 174(1) and (5)). For annual taxes, interest on unpaid quarterly or advance amounts runs to the end of the tax year. From 1 January of the next year it runs on the shortfall against the annual tax (art. 175(1)).
- **Late-payment penalty:** 0.01% for each day late, on top of interest (art. 176(1) to (3)). It does not apply where the under-declaration penalty applies (art. 176(4)).
- **Under-declaration penalty:** 0.08% a day on tax that was undeclared or wrongly declared and later set by ANAF in an assessment (art. 181(1)). It is cut by 75% if the assessed tax is paid by its due date or put on an instalment plan (art. 181(2)). It is doubled where judicial bodies find tax evasion (art. 181(3)). It is not charged below RON 50 (art. 181(6)).
- **Late filing fine:** filing a return late is a contravention (art. 336(1)(b)). The fine is RON 1,000 to 5,000 for medium and large taxpayers and RON 500 to 1,000 for other companies (art. 336(2)(d)).
- **Transfer pricing file:** not preparing it, or not producing it on request, costs RON 12,000 to 14,000 for medium and large taxpayers and RON 2,000 to 3,500 for others (art. 336(1)(e) and (2)(c)).

## Cross-border points

- **Residence and permanent establishments.** A foreign company managed from Romania is resident and taxed on worldwide profit. A foreign company with a Romanian permanent establishment is taxed on that establishment's profit (art. 13(1)(b) and (c); art. 36 and 37). The residence tests are in ro-cross-border.
- **Foreign dividends and share gains** are exempt under the 10% and one-year tests above (art. 23(b), (i), (j); art. 24). Foreign tax on other foreign income is credited against profit tax where a treaty applies (art. 39(1) and (2)).
- **Outbound dividends.** A Romanian company withholds 16% on dividends to non-residents (art. 224(4)(b)). The rate is nil for an EU parent holding at least 10% for an unbroken year (art. 229(1)(c)). A treaty rate applies where it is lower and the paperwork is in place. Interest, royalties and service fees paid abroad, the 50% rate, and the relief paperwork are in ro-cross-border.
- **Exit tax** (art. 40^3). Moving assets, residence or a permanent establishment's business out of Romania is taxed at 16% on market value minus tax value. Within the EU and EEA, payment can be spread over five years. Details are in ro-cross-border.
- **Anti-abuse.** The general anti-abuse rule (art. 40^4) and the controlled foreign company rules (art. 40^5) apply to profit tax.
- **Withholding not made.** Tax the company should have withheld on a payment to a non-resident, but did not, is not deductible (art. 25(4)(a)).
- **Treaties.** Where a tax treaty conflicts with the Fiscal Code, the treaty prevails (art. 1(3)).

## Worked examples

### Example 1: SRL on profit tax, with protocol, car costs, a loss and sponsorship (2026)

Facts: Alfa SRL pays profit tax on the quarterly system. For 2026 its accounting profit before profit tax is RON 1,000,000 and its turnover is RON 10,000,000. The accounts include:
- protocol expenses of RON 30,000;
- a fine of RON 5,000 from ANAF;
- RON 40,000 of running costs for a car also used privately;
- RON 15,000 of sponsorship to a non-profit on ANAF's register;
- a dividend of RON 100,000 received from a Romanian subsidiary.

It has a tax loss of RON 600,000 from 2024. Its turnover is far below EUR 50 million, so IMCA does not apply.

1. **Protocol limit.** The 2% applies to accounting profit plus profit tax expense plus protocol, which is 1,000,000 + 30,000 = 1,030,000. The limit is RON 20,600. The excess of RON 9,400 is added back (art. 25(3)(a)).
2. **Car.** 50% of RON 40,000 is not deductible. RON 20,000 is added back (art. 25(3)(l)).
3. **Fine and sponsorship.** Both are added back in full: RON 5,000 (art. 25(4)(b)) and RON 15,000 (art. 25(4)(i)).
4. **Dividend.** RON 100,000 is taken out as non-taxable (art. 23(a)).
5. **Profit before losses:** 1,000,000 + 9,400 + 20,000 + 5,000 + 15,000 - 100,000 = RON 949,400.
6. **Loss.** The cap is 70% of 949,400 = RON 664,580. The whole RON 600,000 loss fits, so taxable profit is RON 349,400 (art. 31(1)).
7. **Profit tax** at 16% is RON 55,904 (art. 17).
8. **Sponsorship credit.** The credit is the lowest of three amounts: 0.75% of turnover (RON 75,000), 20% of profit tax (RON 11,180.80) and the sponsorship paid (RON 15,000). That is RON 11,180.80 (art. 25(4)(i)).
9. **Profit tax payable** is RON 44,723.20, less the quarterly payments made. The balance is due by 25 June 2027 with the D101.

```oa-check
name: Romanian SRL on profit tax 2026, protocol, car, loss and sponsorship
inputs:
  accounting_profit: 1000000
  turnover: 10000000
  protocol: 30000
  fine: 5000
  car_costs: 40000
  sponsorship: 15000
  dividend_ro: 100000
  loss_2024: 600000
steps:
  - protocol_limit: (accounting_profit + protocol) * 0.02
  - protocol_addback: max(protocol - protocol_limit, 0)
  - car_addback: car_costs * 0.5
  - profit_before_losses: accounting_profit + protocol_addback + car_addback + fine + sponsorship - dividend_ro
  - loss_cap: profit_before_losses * 0.70
  - loss_used: min(loss_2024, loss_cap)
  - taxable_profit: profit_before_losses - loss_used
  - profit_tax: taxable_profit * 0.16
  - sponsorship_credit: min(sponsorship, turnover * 0.0075, profit_tax * 0.20)
  - tax_payable: profit_tax - sponsorship_credit
expected:
  protocol_limit: 20600.00
  protocol_addback: 9400.00
  profit_before_losses: 949400.00
  loss_cap: 664580.00
  loss_used: 600000.00
  taxable_profit: 349400.00
  profit_tax: 55904.00
  sponsorship_credit: 11180.80
  tax_payable: 44723.20
```

### Example 2: micro-enterprise that crosses EUR 100,000 in the third quarter (2026)

Facts: Beta SRL has one full-time employee and opted for the micro regime for 2026. Its 2026 revenue (all turnover) is RON 120,000 in quarter I, RON 150,000 in quarter II and RON 300,000 in quarter III. Its quarter III expenses are RON 220,000. It has no linked enterprises and no deductions from the micro base.

The euro test uses the exchange rate at the close of 2025 (art. 52(5)). This example uses RON 5.00 to the euro to keep the numbers round. For a real file, use the official rate for 31 December 2025. At RON 5.00 the ceiling is RON 500,000.

1. **Quarter I.** Cumulative revenue is RON 120,000, under the ceiling. Micro tax at 1% is RON 1,200, due 25 April 2026.
2. **Quarter II.** Cumulative revenue is RON 270,000, still under. Micro tax is RON 1,500, due 25 July 2026.
3. **Quarter III.** Cumulative revenue reaches RON 570,000, above RON 500,000. From quarter III, Beta pays profit tax (art. 52(1)). It is computed on quarter III revenue and expenses only (art. 52(6)).
4. **Quarter III profit tax.** With no adjustments, profit is 300,000 - 220,000 = RON 80,000. At 16% that is RON 12,800, due 25 October 2026.
5. **After that.** Beta stays on profit tax for the rest of 2026 and files a D101 for 2026 by 25 June 2027. It cannot use the micro regime in 2027, because its 2026 revenue is above EUR 100,000 (art. 47(1)(c)).

The edge case: had Beta been linked to another company through a common shareholder holding more than 25%, that company's turnover would be added to the test (art. 52(5^1)). The switch would then come sooner.

```oa-check
name: Romanian micro-enterprise crossing EUR 100,000 in Q3 2026
inputs:
  eur_rate: 5
  ceiling_eur: 100000
  rev_q1: 120000
  rev_q2: 150000
  rev_q3: 300000
  exp_q3: 220000
steps:
  - ceiling_ron: ceiling_eur * eur_rate
  - cum_q2: rev_q1 + rev_q2
  - cum_q3: cum_q2 + rev_q3
  - micro_q1: rev_q1 * 0.01
  - micro_q2: rev_q2 * 0.01
  - over_ceiling_q2: cum_q2 - ceiling_ron
  - over_ceiling_q3: cum_q3 - ceiling_ron
  - profit_tax_q3: (rev_q3 - exp_q3) * 0.16
  - total_2026_to_q3: micro_q1 + micro_q2 + profit_tax_q3
expected:
  ceiling_ron: 500000.00
  cum_q2: 270000.00
  cum_q3: 570000.00
  micro_q1: 1200.00
  micro_q2: 1500.00
  over_ceiling_q2: -230000.00
  over_ceiling_q3: 70000.00
  profit_tax_q3: 12800.00
  total_2026_to_q3: 15500.00
```

## Ask the client first

1. Is the company on profit tax or micro tax for 2026? If micro: what was the 2025 revenue, including that of every company or PFA linked through a holding above 25%? Does it have a full-time employee, or a mandate contract paid at least the minimum wage?
2. What was the 2025 turnover? Above EUR 50 million brings in IMCA for 2026.
3. Which payment system does it use, quarterly or annual with advance payments? What was the 2025 profit tax?
4. Are there tax losses from earlier years, and from which years?
5. Interest, dividends or share sales: what is the net interest cost, is any owed to affiliates, and which holdings (percentage and since when) produced dividends or gains?
6. Any sponsorship, protocol, cars used privately, fines, or payments to related parties abroad?

## Sources

| Source | URL | Read on |
|---|---|---|
| Fiscal Code, Legea 227/2015, ANAF consolidated text (last update Legea 170/2026), art. 1, 13, 16 to 31, 36, 37, 39, 40^2 to 40^5, 41 to 43, 45, 46^1, 47 to 57, 97, 224, 229 | https://static.anaf.ro/static/10/Anaf/legislatie/Cod_fiscal_norme_2023.htm | 2026-10-23 |
| Fiscal Procedure Code, Legea 207/2015, ANAF consolidated text (last update Legea 170/2026), art. 174 to 176, 181, 336 | https://static.anaf.ro/static/10/Anaf/cod_procedura/Cod_Procedura_Fiscala_2023.htm | 2026-10-23 |
| OUG 156/2024, ANAF copy (micro ceiling EUR 250,000 for 2025, EUR 100,000 from 2026) | https://static.anaf.ro/static/10/Anaf/legislatie/OUG_156_2024.pdf | 2026-10-23 |
| OUG 89/2025, ANAF copy (single 1% micro rate; IMCA 0.5% for 2026 and its end date) | https://static.anaf.ro/static/10/Anaf/legislatie/OUG_89_2025.pdf | 2026-10-23 |
| Legea 141/2025 privind unele măsuri fiscal-bugetare, ANAF copy (dividend tax 16%) | https://static.anaf.ro/static/10/Anaf/legislatie/L_141_2025.pdf | 2026-10-23 |
| OUG 8/2026, ANAF copy (micro rules, D101 deadline, quarter I payment) | https://static.anaf.ro/static/10/Anaf/legislatie/OUG_8_2026.pdf | 2026-10-23 |
| Ordonanța 6/2026, ANAF copy (repeal of art. 25^1) | https://static.anaf.ro/static/10/Anaf/legislatie/OG_6_2026.pdf | 2026-10-23 |
| ANAF, form 101 (annual profit tax return) | https://static.anaf.ro/static/10/Anaf/Declaratii_R/101.html | 2026-10-23 |
| ANAF, form 100 (payment obligations to the state budget) | https://static.anaf.ro/static/10/Anaf/Declaratii_R/100.html | 2026-10-23 |

Not yet confirmed:
- the D101 deadline for the 2025 return (OUG 8/2026 applies the rewritten art. 42 from the 2026 return);
- how long unused sponsorship carries forward (art. 25(4)(ț) refers to amounts carried forward without giving a period);
- the official RON/EUR rate at 31 December 2025 for the micro and IMCA tests;
- the Pillar Two minimum tax for large groups, which this skill does not cover.

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
