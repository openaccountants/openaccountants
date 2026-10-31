---
name: ie-corporation-tax
description: "Irish corporation tax for tax year 2026 (accounting periods ending in 2026) for an Irish-resident company. Covers the 12.5% trading rate (section 21 TCA 1997), the 25% rate on passive income and excepted trades (section 21A), company gains grossed up at the 31% CGT rate for disposals from 7 October 2026 (33% before that date and on development land), the Pillar Two 15% minimum tax (Part 4A, scope only), close-company surcharges, preliminary tax, losses and group relief, start-up relief, the R&D credit (30%, or 35% for periods ending 31 December 2026 or later), the Knowledge Development Box (10% effective rate), interest limitation, and CT1 filing on ROS. Trigger on: Ireland corporation tax, CT1, 12.5% rate, preliminary CT, R&D credit Ireland, KDB, close company surcharge, Pillar Two Ireland. Out of scope: non-resident companies and Irish branches under section 25 (ie-foreign-tax-and-withholding), company exit tax (ie-cross-border), transfer pricing (ie-transfer-pricing), individuals (ie-income-tax-form11), VAT (ie-vat-return)."
version: 1.3
jurisdiction: IE
tax_year: 2026
last_updated: 2026-10-27
authored_by: Michael Cutajar and the OpenAccountants team
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Irish corporation tax (CT1): 2026 rates, preliminary tax, losses, reliefs and filing

The law is the Taxes Consolidation Act 1997 (TCA), as amended each year by a Finance Act. Revenue's guidance is on [revenue.ie](https://www.revenue.ie/en/companies-and-charities/corporation-tax-for-companies/index.aspx) and in its Tax and Duty Manuals (TDMs). Figures are for tax year 2026: accounting periods ending in 2026, for a calendar-year company the 12 months to 31 December 2026. The 2025 CT1, due by 23 September 2026 for a calendar-year company, is covered under "Deadlines and filing".

## Who this applies to

- **Irish-resident companies** that file a Form CT1: trading companies, investment and holding companies, and owner-managed close companies.
- **Non-resident companies with an Irish branch or agency.** They pay corporation tax at the same rates on the branch's trading income, on income from property or rights the branch uses or holds, and on gains on branch assets (section 25(2)). Profits are attributed to the branch under the Authorised OECD Approach for periods commencing on or after 1 January 2022 (section 25A). A non-resident company's Irish rental income is in corporation tax from 1 January 2022 (section 25(2A)). The rules for these companies, including Irish income with no branch and tax deducted at source, are in [ie-foreign-tax-and-withholding](ie-foreign-tax-and-withholding.md). Use this skill for the rates, reliefs and CT1 mechanics that apply to the branch once its profit is known.
- **Groups in Pillar Two scope** (consolidated revenue of EUR 750m or more in two of the four preceding fiscal years). This skill screens for scope only.

Not covered here, refer to a specialist: Section 110 securitisation companies; banks and insurers; REITs and IREFs; funds and ICAVs; tonnage tax; petroleum and mineral profits; the Pillar Two top-up computation; anti-hybrid rules and the outbound payments measures; foreign currency (section 402) computations; loss-buying (section 401); arrangements that may fall within the general anti-avoidance rule (section 811C) or mandatory disclosure; Revenue audits and qualifying disclosures; loans and benefits to participators; and any case where residence or a permanent establishment is in doubt. Do not apply 12.5% until the facts support a trade.

Related skills: residence and the company exit tax are in [ie-cross-border](ie-cross-border.md); transfer pricing in [ie-transfer-pricing](ie-transfer-pricing.md); individuals in [ie-income-tax-form11](ie-income-tax-form11.md); employer PRSI in [ie-payroll](ie-payroll.md).

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| Trading income (Cases I and II) | 12.5% | 2026 | https://www.revenue.ie/en/companies-and-charities/corporation-tax-for-companies/corporation-tax/basis-of-charge.aspx |
| Non-trading income (rent, interest, other passive income) and excepted trades | 25% | 2026 | https://www.revenue.ie/en/companies-and-charities/corporation-tax-for-companies/corporation-tax/basis-of-charge.aspx |
| CGT rate used to gross up company gains, disposals on or after 7 October 2026 | 31% (Financial Resolution No. 3 of 6 October 2026, statutory effect under the Provisional Collection of Taxes Act 1927) | 2026 | https://www.revenue.ie/en/companies-and-charities/capital-gains-for-companies/index.aspx |
| CGT rate used to gross up company gains, disposals up to 6 October 2026 | 33% (section 28(3)) | 2026 | https://www.revenue.ie/en/companies-and-charities/capital-gains-for-companies/index.aspx |
| Development land gains (outside CT profits, taxed under CGT rules) | 33% (section 649A) | 2026 | https://www.revenue.ie/en/tax-professionals/tdm/income-tax-capital-gains-tax-corporation-tax/part-22/22-02-03.pdf |
| Pillar Two minimum effective rate | 15%; groups with consolidated revenue of EUR 750m or more in two of the four preceding fiscal years | 2026 | https://www.revenue.ie/en/companies-and-charities/pillar-two/what-is/index.aspx |
| Small company for preliminary tax | Previous period's CT not above EUR 200,000 | 2026 | https://www.revenue.ie/en/companies-and-charities/corporation-tax-for-companies/corporation-tax-payment-and-filing/preliminary-ct.aspx |
| Close-company surcharge on undistributed estate and investment income (section 440) | 20%, after a 7.5% reduction for trading companies; none if the excess is EUR 2,000 or less | 2026 | https://www.revenue.ie/en/companies-and-charities/corporation-tax-for-companies/close-companies/surcharge.aspx |
| Service-company surcharge (section 441) | 15% on half of undistributed trading income, plus 20% on undistributed estate and investment income | 2026 | https://www.revenue.ie/en/tax-professionals/tdm/income-tax-capital-gains-tax-corporation-tax/part-13/13-02-06.pdf |
| R&D corporation tax credit (sections 766C and 766D) | 30% for periods commencing on or after 1 January 2024; 35% where the specified return date is on or after 23 September 2027 (in general, periods ending 31 December 2026 or later) | 2026 | https://www.revenue.ie/en/tax-professionals/tdm/income-tax-capital-gains-tax-corporation-tax/part-29/29-02-03.pdf |
| R&D credit, first instalment | Greater of EUR 75,000 (EUR 87,500 at the 35% rate), or the credit if lower, and 50% of the credit | 2026 | https://www.revenue.ie/en/tax-professionals/tdm/income-tax-capital-gains-tax-corporation-tax/part-29/29-02-03.pdf |
| Knowledge Development Box (Part 29, Chapter 5) | Deduction of 20% of qualifying profits, an effective rate of 10%, from 1 October 2023 | 2026 | https://www.revenue.ie/en/companies-and-charities/reliefs-and-exemptions/knowledge-development-box-kdb/index.aspx |
| Plant and machinery wear and tear | 12.5% a year over eight years | 2026 | https://www.revenue.ie/en/companies-and-charities/corporation-tax-for-companies/corporation-tax/capital-allowances-and-deductions.aspx |
| Industrial buildings | 4% a year over 25 years | 2026 | https://www.revenue.ie/en/companies-and-charities/corporation-tax-for-companies/corporation-tax/capital-allowances-and-deductions.aspx |
| Interest limitation de minimis | Exceeding borrowing costs of EUR 3,000,000 for a 12-month period | 2026 | https://www.revenue.ie/en/tax-professionals/tdm/income-tax-capital-gains-tax-corporation-tax/part-35d/35D-01-01.pdf |
| Start-up relief (section 486C) | Full relief where total CT is EUR 40,000 or less; marginal relief above EUR 40,000 and below EUR 60,000; capped at qualifying PRSI (EUR 5,000 per employee, EUR 1,000 per director's Class S, EUR 40,000 overall) | 2026 | https://www.revenue.ie/en/tax-professionals/tdm/income-tax-capital-gains-tax-corporation-tax/part-15/15-03-03.pdf |
| iXBRL exclusion | All three: assets under EUR 4.4 million, turnover under EUR 8.8 million, 50 or fewer employees | 2026 | https://www.revenue.ie/en/companies-and-charities/corporation-tax-for-companies/submitting-financial-statements/who-submit.aspx |
| Late payment interest | 0.0219% a day | 2026 | https://www.revenue.ie/en/companies-and-charities/corporation-tax-for-companies/corporation-tax-payment-and-filing/payment-and-filing.aspx |
| Late filing surcharge (section 1084) | 5% up to EUR 12,695 within two months; 10% up to EUR 63,485 after | 2026 | https://www.revenue.ie/en/companies-and-charities/corporation-tax-for-companies/corporation-tax-payment-and-filing/payment-and-filing.aspx |

No change has been made to the 12.5% or 25% rates for 2025 or 2026. If a rate changes inside an accounting period, profits are apportioned on a time basis. An accounting period cannot be longer than 12 months, so a longer set of accounts is split into two CT periods ([Revenue: basis of charge](https://www.revenue.ie/en/companies-and-charities/corporation-tax-for-companies/corporation-tax/basis-of-charge.aspx)).

**The 31% CGT rate is in force, but provisionally.** Financial Resolution No. 3, carried by the Dáil on 6 October 2026, substitutes 31% for 33% in section 28(3) for disposals made on or after 7 October 2026, with statutory effect under the Provisional Collection of Taxes Act 1927. Section 36 of the Finance (No. 2) Bill 2026 (Bill 98 of 2026, published 19 October 2026, not yet enacted) makes the same change. The 1927 Act covers capital gains tax (section 1, definition of "tax", as substituted by section 160 of the Finance Act 2010). Under section 4 the resolution lapses if the Bill's provisions are rejected, if the Bill is not read a second time in time, or if no Act containing the change comes into operation within four months of 7 October 2026, so a gain computed at 31% must be revisited if that happens. Revenue's company gains page already uses 31%. Development land is taxed at 33% under section 649A, which the resolution does not touch.

## The taxable base

**Start from the accounts profit.** Add back depreciation, business entertainment, capital expenditure, CT itself, fines and penalties, and interest on late tax. Deduct capital allowances instead of depreciation. Expenses are deductible only if they are revenue in nature and incurred wholly and exclusively for the trade. Pre-trading expenses of the three years before trading starts are deductible. A donation to an approved charity of at least EUR 250 in a 12-month period reduces CT.

**Split the profits.** Trading income is taxed at 12.5%. Rent, deposit interest and other passive income, and income of an excepted trade (for example dealing in or developing land), are taxed at 25%, even inside a trading company. When the split is unclear, gather the facts first (TDM Part 02-02-06 on classifying activities as trading).

**Chargeable gains.** A company's gains on assets other than development land go into CT profits, grossed up so that CT at 12.5% equals CGT at the CGT rate ([Revenue: capital gains for companies](https://www.revenue.ie/en/companies-and-charities/capital-gains-for-companies/index.aspx)):

1. Work out the CGT on the gain at the rate for the disposal date: 31% from 7 October 2026, 33% before.
2. Divide that tax by 12.5%. The result is the adjusted gain, reported in the capital gains section of the CT1.

A gain of EUR 150,000 on a disposal from 7 October 2026 gives tax of EUR 46,500 and an adjusted gain of EUR 372,000. The same gain on 6 October 2026 gives EUR 49,500 and EUR 396,000, the figures in Revenue's own example of a disposal in October 2025 at 33%. Development land gains stay outside CT profits: they are reported in the Capital Gains (Development Land) section of the CT1 and follow CGT pay and file dates. A loss on development land can be set against gains on all other assets; a loss on other assets only against gains on non-development land assets (same Revenue page). Disposals of shares in trading subsidiaries may be exempt under section 626B; check the conditions in TDM Part 20-01-14.

**Capital allowances.**

| Asset | Allowance |
|---|---|
| Plant and machinery | 12.5% a year over eight years, if in use at the end of the period |
| Most industrial buildings | 4% a year over 25 years |
| Energy-efficient equipment, gas and electric vehicles, refuelling equipment, an employee creche or gym (equipment) | 100% in the first year of use |
| Building used as an employee creche or gym | 15% a year over seven years |
| Specified intangible assets (section 291A) | Amortisation charged in the accounts, or an election for 7% a year over 15 years and 2% in the final year |

Allowances are cut for a short period or part non-trade use. Revenue's example: a machine costing EUR 25,000 gives EUR 3,125 a year. Intangible allowances (with related interest) cannot exceed 80% of the relevant trade's income for expenditure from 11 October 2017; Finance Act 2025 extends the ring-fence and the cap to balancing allowances on events from 8 October 2025. Cars are restricted by cost and CO2 emissions: check TDM Part 11-00-01 before claiming.

**Losses** ([Revenue: trading losses](https://www.revenue.ie/en/companies-and-charities/corporation-tax-for-companies/corporation-tax/trading-losses.aspx)):

1. **Same and preceding period (section 396A).** Set a 12.5% trading loss euro for euro against trading income of the same period, then of the immediately preceding period of the same length. This offset is against trading income only, not rent, interest or gains. The preceding period counts only if the company carried on the trade in it; where periods differ in length, profits are apportioned ([Notes for guidance, TCA Part 12](https://www.revenue.ie/en/tax-professionals/documents/notes-for-guidance/tca/part12.pdf)).
2. **Value basis (section 396B).** Any loss left reduces the CT on non-trading income and gains of the same or preceding period, at 12.5% of the loss: a EUR 100,000 loss saves EUR 12,500.
3. **Carry forward (section 396(1)).** Unused losses carry forward without time limit against the first profits of the same trade.
4. **Excepted trades (section 396(2))** set losses against total profits of the same and preceding period.
5. **Terminal loss (section 397).** A loss in the last 12 months of a discontinued trade that cannot be relieved otherwise carries back against income of the same trade in the three preceding years, later periods first (Notes for guidance, Part 12).
6. **Change of ownership (section 401).** Losses carried forward are lost where, within three years, there is both a change in ownership and a major change in the nature or conduct of the trade, or where ownership changes when the trade has become small or negligible (Notes for guidance, Part 12). Refer any such case.

**Group relief** ([Revenue: group relief](https://www.revenue.ie/en/companies-and-charities/reliefs-and-exemptions/group-relief/index.aspx)). Companies are grouped where one is a 75% subsidiary of the other, or both are 75% subsidiaries of a third, measured on ordinary share capital, distributable profits and assets on a winding up. Current-year trading losses, excess charges, excess management expenses and Case V excess capital allowances can be surrendered. The claimant uses them against its trading income, on a value basis against its CT, or against total profits of an excepted trade. Relief is time-apportioned where accounting periods do not match or a company joins or leaves the group, and is restricted if either company files late. The claim is made within two years of the end of the surrendering company's period, with its written consent. Consortium relief (section 412) is separate: refer it.

**Interest limitation (Part 35D).** Exceeding borrowing costs are limited to 30% of tax-adjusted EBITDA, but only where they exceed EUR 3,000,000 for a 12-month period (reduced for a shorter period, applied once per interest group). A company wholly owned by one individual is not a standalone entity, so for most owner-managed companies the de minimis is the test ([TDM Part 35D-01-01](https://www.revenue.ie/en/tax-professionals/tdm/income-tax-capital-gains-tax-corporation-tax/part-35d/35D-01-01.pdf)). Other points from the same manual:
- The rule applies to accounting periods commencing on or after 1 January 2022.
- A standalone entity is outside the rule: an Irish-resident company that is not in a worldwide group, has no associated enterprises and has no permanent establishment outside Ireland.
- A group ratio or an equity ratio election (not both) can be made on the CT1 by the return date. Legacy debt, agreed before 17 June 2016, is excluded. Refer these.
- A disallowed amount carries forward as "deemed borrowing cost" to later periods with spare capacity.

**Start-up relief (section 486C).** For a company incorporated on or after 14 October 2008 that set up and began a qualifying trade between 1 January 2009 and 31 December 2026, for five years from the start of trading ([Revenue](https://www.revenue.ie/en/starting-a-business/initiatives-startup-businesses-smes/tax-relief-for-new-startup-companies/can-you-claim-for-tax-relief-for-your-start-up-company.aspx)). Excluded: trades taken over from another person, land development, petroleum and minerals, section 441 service company activities, certain primary production, and an associated company's trade. Relief covers only CT on the qualifying trade and its gains, is full where total CT is EUR 40,000 or less, marginal between EUR 40,000 and EUR 60,000 (CT on the trade reduced to the greater of 3 x (T - 40,000) x ((A + B) / T) and the CT less qualifying PRSI), and never exceeds the qualifying PRSI. Revenue's example: CT of EUR 25,000 and qualifying PRSI of EUR 10,500 (employer PRSI EUR 9,000, plus directors' Class S of EUR 500 and EUR 1,200, the second capped at EUR 1,000) gives relief of EUR 10,500, leaving CT of EUR 14,500 on the qualifying trade. Unused relief from the first five years (trades started on or after 1 January 2018) can be carried forward; in a later year it cannot exceed the PRSI paid in that year ([Revenue: how the relief is calculated](https://www.revenue.ie/en/starting-a-business/initiatives-startup-businesses-smes/tax-relief-for-new-startup-companies/how-is-the-relief-calculated.aspx)). Claim it on the CT1.

**R&D corporation tax credit** ([TDM Part 29-02-03](https://www.revenue.ie/en/tax-professionals/tdm/income-tax-capital-gains-tax-corporation-tax/part-29/29-02-03.pdf)). The credit is 30% of qualifying expenditure for periods commencing on or after 1 January 2024, and 35% for periods whose specified return date is on or after 23 September 2027 (Finance Act 2025, sections 766C(1) and 766D(1)). In general the 35% rate applies to periods ending 31 December 2026 or later; a period ending 30 November 2026 has an August 2027 return date and stays at 30%. It is not set against the period's CT: it is paid in three instalments, the first as in the table, the second three fifths of the balance, the third the rest. Each instalment is offset or repaid, at the company's election. The first instalment is specified on the CT1 for the period in which the expenditure was incurred, the second on the CT1 for the next period, the third on the one after. Example: EUR 400,000 spent in calendar 2026 gives EUR 140,000; first instalment EUR 87,500, second EUR 31,500, third EUR 21,000. The same spend in calendar 2025 at 30% gives EUR 120,000; first instalment EUR 75,000 (greater than 50%, EUR 60,000), second EUR 27,000, third EUR 18,000. The R&D must be systematic, investigative or experimental work in science or technology, carried out in Ireland, the EEA or the UK, that seeks scientific or technological advancement and involves resolving scientific or technological uncertainty. Subcontracted work and agency staff count as outsourcing and are subject to limits. The claim is due within 12 months of the period end (31 December 2027 for calendar 2026). A company claiming for the first time, or that has not claimed in its previous three periods, must notify Revenue at least 90 days before claiming.

**Knowledge Development Box** ([Revenue: KDB](https://www.revenue.ie/en/companies-and-charities/reliefs-and-exemptions/knowledge-development-box-kdb/index.aspx)). From 1 October 2023 a qualifying company deducts 20% of qualifying profits, an effective rate of 10%. The 50% deduction (6.25% effective) applied only up to 30 September 2023: never use 6.25% for 2026. Qualifying assets are computer programs, patented inventions and, for small companies, certified patentable IP. The KDB applies to periods commencing before 1 January 2027 (section 769Q). The nexus fraction and tracking of R&D spend make every claim technical: refer it.

**Close-company surcharges** ([Revenue: surcharge](https://www.revenue.ie/en/companies-and-charities/corporation-tax-for-companies/close-companies/surcharge.aspx)). A close company is controlled by five or fewer participators or by its directors. Under section 440, take estate and investment income less the CT on it, deduct 7.5% for a trading company, deduct distributions made within 18 months of the period end, and if the excess is above EUR 2,000 charge 20% on it. Irish dividends received count: Revenue's example is a non-trading close company with EUR 50,000 of Irish dividends with nothing paid out, giving a surcharge of EUR 10,000. Where one close company pays a distribution to another, both can jointly elect to disregard it for the surcharge; each includes the election on its CT1. The surcharge is collected with the next period's CT and reported on that CT1; leaving it out makes the return incorrect. Service companies under section 441 pay 15% on half of undistributed trading income as well; refer marginal cases.

**Pillar Two (Part 4A TCA)** ([Revenue: Pillar Two](https://www.revenue.ie/en/companies-and-charities/pillar-two/what-is/index.aspx)). In-scope groups pay at least 15% in each jurisdiction. Ireland's domestic top-up tax (a qualified domestic top-up tax) and the IIR apply for fiscal years commencing on or after 31 December 2023; the UTPR from fiscal years commencing on or after 31 December 2024. Revenue states Ireland's domestic top-up tax has transitional qualified status with the OECD. The OECD Side-by-Side package of 5 January 2026 changes some rules and is acknowledged by the European Commission (Notice C/2026/253). Screen for scope and refer the computation. Example: consolidated revenue of EUR 700m (2022), EUR 760m (2023), EUR 720m (2024) and EUR 800m (2025) reaches EUR 750m in two of the four preceding years, so the group is in scope for 2026.

**Foreign dividends: participation exemption** ([Revenue](https://www.revenue.ie/en/companies-and-charities/reliefs-and-exemptions/exemption-foreign-distributions/index.aspx)). For distributions from 1 January 2025, an Irish company holding at least 5% for a continuous 12 months can elect to exempt dividends from foreign subsidiaries resident in an EU or EEA state or treaty country (three-year look-back for 2026 distributions, five years for 2025). From 2026 a non-treaty country that charges withholding tax on cross-border distributions also counts, where that tax is paid on the full distribution and not refunded. The subsidiary must not be on the EU list of non-cooperative jurisdictions and must not be generally exempt from tax. The distribution must be income chargeable under Case III (not trading income) and must not be deductible abroad. The election is claimed on the CT1 through ROS and covers every relevant distribution for the period, not dividend by dividend.

## Deadlines and filing

**Mandatory e-filing.** Every company pays and files through ROS: preliminary tax by its due date, then a CT1 and Form 46G (Company) and the balance of tax by the return date ([Revenue: payment and filing](https://www.revenue.ie/en/companies-and-charities/corporation-tax-for-companies/corporation-tax-payment-and-filing/payment-and-filing.aspx)).

**The return date** ([TDM Part 47-06-08](https://www.revenue.ie/en/tax-professionals/tdm/income-tax-capital-gains-tax-corporation-tax/part-47/47-06-08.pdf)). Nine months after the period ends, by the 21st of that month, or the 23rd when filed and paid on ROS: 23 September 2027 for a 31 December 2026 year end. A period ending before the 21st of a month is due on the same day of the ninth month (a period ending 5 December is due 5 September).

**Preliminary tax, 2026 periods** ([Revenue](https://www.revenue.ie/en/companies-and-charities/corporation-tax-for-companies/corporation-tax-payment-and-filing/when-is-preliminary-ct-due.aspx)):

| Company | Amount | Due (calendar 2026 period) |
|---|---|---|
| Small (previous period's CT not above EUR 200,000, excluding surcharges and section 239 income tax; annualise a short period) | At least the lower of 100% of the previous period's CT and 90% of this period's CT | 31 days before the period ends, by the 23rd: 23 November 2026 |
| Large, period longer than seven months | Instalment 1: 50% of previous CT or 45% of current CT | 23rd of the sixth month: 23 June 2026 |
| | Instalment 2: brings the total to 90% of current CT | 23rd of the eleventh month: 23 November 2026 |
| Large, period of less than seven months | 90% in one instalment | See TDM Part 41A-07-02 |
| New company, first period, CT less than EUR 200,000 (excluding surcharge, including section 239 income tax) | None | Whole CT with the CT1 |
| New company, first period, CT of EUR 200,000 or more | As a large company, but only the 45% of current CT test applies to instalment 1 (no previous period) ([Notes for guidance, TCA Part 41A](https://www.revenue.ie/en/tax-professionals/documents/notes-for-guidance/tca/part41a.pdf)) | As above |

Example, large company: CT for 2025 of EUR 900,000, expected 2026 CT of EUR 1,200,000. First instalment by 23 June 2026: EUR 450,000 (50% of 2025). Second by 23 November 2026: EUR 630,000, bringing the total to EUR 1,080,000 (90% of 2026). Balance EUR 120,000 with the CT1. Groups can apply to Revenue's Debt Management Task Force for notional allocation of preliminary tax.

**iXBRL.** Financial statements are filed in iXBRL with the CT1 unless the company meets all three small tests in the rates table; Large Corporates Division and High Wealth and Financial Services Division cases and Section 110 companies always file iXBRL ([Revenue](https://www.revenue.ie/en/companies-and-charities/corporation-tax-for-companies/submitting-financial-statements/who-submit.aspx)). A company filing iXBRL skips the CT1 "Extracts from Accounts" panel but must still tag the mandatory items ([Revenue: iXBRL](https://www.revenue.ie/en/companies-and-charities/corporation-tax-for-companies/submitting-financial-statements/index.aspx)).

**Pillar Two** ([Revenue: key dates](https://www.revenue.ie/en/companies-and-charities/pillar-two/dates/index.aspx)). Register on ROS within 12 months after the end of the first fiscal year in scope (entities with a first year ending in 2024 had until 28 February 2026). File the Top-up Tax Information Return within 15 months of each fiscal year end, 18 months for the first year. The first TIR and pay and file deadline was 30 June 2026; for a group first in scope for calendar 2025, the first TIR is due 30 June 2027.

**The 2025 CT1.** For a 31 December 2025 year end the CT1 was due by 23 September 2026. Filed within two months of the return date: 5% surcharge and a 25% relief restriction. Later: 10% and 50%. The R&D rate for 2025 is 30% and the claim is due by 31 December 2026. 2025 is the first year directors' Class S PRSI counts for start-up relief.

**Proposals in the Finance (No. 2) Bill 2026, not yet law** ([Bill 98 of 2026, as initiated](https://data.oireachtas.ie/ie/oireachtas/bill/2026/98/eng/initiated/b9826d.pdf)):
- small company limit for preliminary tax raised from EUR 200,000 to EUR 350,000, and a top-up within four months of the period end where at least 80% was paid, for periods commencing on or after 1 January 2027 (section 74);
- start-up relief extended to trades begun by 31 December 2030 (section 30);
- KDB extended to periods commencing before 1 January 2032 (section 32);
- R&D first instalment at the 35% rate raised from EUR 87,500 to EUR 105,000 for return dates on or after 23 September 2028 (section 25).
Apply none of these until the Act is passed.

**Checklist before filing:** period of 12 months or less; trading, passive and gains split; add-backs and capital allowances; losses in statutory order and group relief consents; interest limitation de minimis; start-up relief within the CT bands and PRSI cap; R&D rate, instalment and notification; the previous period's close-company surcharge included; Pillar Two scope; preliminary tax tested; iXBRL tested.

## Penalties and interest

- **Late payment interest:** 0.0219% a day on tax paid late or short, including a preliminary tax shortfall measured against the final liability. It cannot be appealed or reduced.
- **Late filing surcharge (section 1084):** 5% of the tax, up to EUR 12,695, if the CT1 is filed within two months of the due date; 10%, up to EUR 63,485, after that. It applies even if the tax was paid on time, and the surcharge carries interest. A careless or deliberate incorrect return is treated as late unless corrected before the due date ([TDM Part 47-06-08](https://www.revenue.ie/en/tax-professionals/tdm/income-tax-capital-gains-tax-corporation-tax/part-47/47-06-08.pdf)).
- **Restriction of reliefs (section 1085):** a late CT1 cuts excess capital allowances, loss relief under sections 396(2), 396A(3), 396B(2) and 399(2), and group relief: by 25% (maximum EUR 31,740) if less than two months late, by 50% (maximum EUR 158,715) if two months or more ([TDM Part 47-06-04](https://www.revenue.ie/en/tax-professionals/tdm/income-tax-capital-gains-tax-corporation-tax/part-47/47-06-04.pdf)).
- **Example:** CT of EUR 150,000 for 2025, CT1 due 23 September 2026. Filed 20 October 2026: surcharge EUR 7,500. Filed 15 December 2026: surcharge EUR 15,000.
- **Time limit (section 959AA):** with full and true disclosure, Revenue cannot assess more than four years after the end of the chargeable period. No limit for fraud, neglect or no return.

## Cross-border points

- **Non-resident company with an Irish branch:** taxed at 12.5% on branch trading profits and 25% on non-trading branch income, with profits attributed under section 25A. Charge, credit for tax deducted at source (section 25(3)) and assessment through a representative (sections 1034 and 1035) are in [ie-foreign-tax-and-withholding](ie-foreign-tax-and-withholding.md). Branch-to-head-office dealings follow [ie-transfer-pricing](ie-transfer-pricing.md).
- **Group relief across borders:** Irish branches of foreign companies can be group members; an Irish parent can claim, in limited cases, the final losses of a 75% subsidiary resident in an EU or EEA treaty state.
- **Foreign tax on company income:** credit relief under Schedule 24, unilateral relief and pooling are in [ie-foreign-tax-and-withholding](ie-foreign-tax-and-withholding.md). The participation exemption above is an alternative for qualifying foreign dividends.
- **Withholding on payments out** (dividends 25%, interest and royalties 20%) and treaty rates: [ie-foreign-tax-and-withholding](ie-foreign-tax-and-withholding.md).
- **Company migration and exit tax:** [ie-cross-border](ie-cross-border.md).
- **Pillar Two:** the domestic top-up tax collects Irish top-up first; foreign IIR or UTPR may otherwise apply to Irish entities.

## Worked examples

### Example 1: small close trading company with rent, calendar 2026

Hill Ltd is a close trading company. In 2026 it has trading profit of EUR 400,000 and net rental profit of EUR 40,000. Its CT for 2025 was EUR 48,000. It pays dividends of EUR 20,000 within 18 months of 31 December 2026.

- CT for 2026: EUR 400,000 at 12.5% is EUR 50,000; EUR 40,000 at 25% is EUR 10,000. Total EUR 60,000.
- It is a small company: 2025 CT of EUR 48,000 is not above EUR 200,000. By 23 November 2026 it pays at least the lower of EUR 48,000 (100% of 2025) and EUR 54,000 (90% of 2026), so EUR 48,000.
- The balance of EUR 12,000 is due with the CT1 by 23 September 2027.
- Surcharge: rent EUR 40,000 less CT EUR 10,000 is EUR 30,000. Less the 7.5% trading company reduction gives EUR 27,750. Less dividends of EUR 20,000 leaves EUR 7,750, above EUR 2,000, so the surcharge is 20% of EUR 7,750, EUR 1,550, collected with the 2027 CT.

```oa-check
name: Hill Ltd, trading EUR 400,000 and rent EUR 40,000, calendar 2026
inputs:
  trading: 400000
  rent: 40000
  prior_ct: 48000
  dividends: 20000
steps:
  - ct_trading: trading * 0.125
  - ct_rent: rent * 0.25
  - ct_total: ct_trading + ct_rent
  - prelim_minimum: min(prior_ct, ct_total * 0.90)
  - balance_with_ct1: ct_total - prelim_minimum
  - distributable: (rent - ct_rent) * (1 - 0.075)
  - excess: distributable - dividends
  - surcharge: excess * 0.20
expected:
  ct_total: 60000.00
  prelim_minimum: 48000.00
  balance_with_ct1: 12000.00
  distributable: 27750.00
  excess: 7750.00
  surcharge: 1550.00
```

### Example 2: gain after 7 October 2026, sheltered by a trading loss

Atlas Ltd has a calendar 2026 period. It has a trading loss of EUR 100,000 and no other trading income in 2026 or 2025. On 15 November 2026 it sells a building (not development land) at a chargeable gain of EUR 150,000.

- The disposal is on or after 7 October 2026, so the CGT rate is 31%: tax EUR 46,500.
- Adjusted gain for the CT1: EUR 46,500 divided by 12.5% is EUR 372,000. CT at 12.5% on that is EUR 46,500.
- The loss has no trading income to absorb it this year or last, so it is used on a value basis: EUR 100,000 at 12.5% is EUR 12,500.
- CT payable: EUR 46,500 less EUR 12,500 is EUR 34,000.
- The edge case: had Atlas sold on 6 October 2026, the rate would be 33%: tax EUR 49,500, adjusted gain EUR 396,000, CT payable EUR 37,000. One day changes the bill by EUR 3,000. If the Finance (No. 2) Bill 2026 does not carry the 31% rate into law, recompute at 33%.

```oa-check
name: Atlas Ltd, gain EUR 150,000 on 15 November 2026 with trading loss EUR 100,000
inputs:
  gain: 150000
  loss: 100000
  cgt_rate_new: 0.31
  cgt_rate_old: 0.33
  ct_rate: 0.125
steps:
  - cgt_new: gain * cgt_rate_new
  - adjusted_gain_new: cgt_new / ct_rate
  - ct_on_gain_new: adjusted_gain_new * ct_rate
  - value_relief: loss * ct_rate
  - ct_payable_new: ct_on_gain_new - value_relief
  - cgt_old: gain * cgt_rate_old
  - adjusted_gain_old: cgt_old / ct_rate
  - ct_payable_old: cgt_old - value_relief
  - difference: ct_payable_old - ct_payable_new
expected:
  cgt_new: 46500.00
  adjusted_gain_new: 372000.00
  ct_on_gain_new: 46500.00
  value_relief: 12500.00
  ct_payable_new: 34000.00
  adjusted_gain_old: 396000.00
  ct_payable_old: 37000.00
  difference: 3000.00
```

## Ask the client first

1. The accounting period dates, and whether the company is Irish resident or a non-resident trading through an Irish branch.
2. What the income is: trading, rent, interest, dividends, or an excepted trade; and any assets sold, with the disposal dates (before or from 7 October 2026) and whether any is development land.
3. The CT for the previous period and its length, and the preliminary tax already paid.
4. Who owns it: a close company or service company, 75% group links, and whether group revenue reaches EUR 750m.
5. Losses brought forward or from group companies, R&D or patent income, and net interest expense.
6. Whether any CT1 or payment is late, and whether the accounts meet the three iXBRL tests.

## Sources

| Source | URL | Read on |
|---|---|---|
| Revenue, basis of charge (12.5% and 25%) | https://www.revenue.ie/en/companies-and-charities/corporation-tax-for-companies/corporation-tax/basis-of-charge.aspx | 2026-10-23 |
| Revenue, capital gains for companies (31% gross-up) | https://www.revenue.ie/en/companies-and-charities/capital-gains-for-companies/index.aspx | 2026-10-23 |
| Dáil Éireann, 6 October 2026, Financial Resolution No. 3: Capital Gains Tax (carried 95 to 64) | https://data.oireachtas.ie/akn/ie/debateRecord/dail/2026-10-06/debate/mul@/main.xml | 2026-10-23 |
| Finance (No. 2) Bill 2026 (Bill 98 of 2026), as initiated, sections 25, 30, 32, 36, 72, 74 | https://data.oireachtas.ie/ie/oireachtas/bill/2026/98/eng/initiated/b9826d.pdf | 2026-10-23 |
| Oireachtas, Finance (No. 2) Bill 2026 status | https://www.oireachtas.ie/en/bills/bill/2026/98/ | 2026-10-23 |
| Provisional Collection of Taxes Act 1927, section 4 | https://www.irishstatutebook.ie/eli/1927/act/7/section/4/enacted/en/html | 2026-10-23 |
| Finance Act 2010, section 160 (capital gains tax within the 1927 Act) | https://www.irishstatutebook.ie/2010/en/act/pub/0005/sec0160.html | 2026-10-23 |
| TDM Part 22-02-03, development land rate of charge | https://www.revenue.ie/en/tax-professionals/tdm/income-tax-capital-gains-tax-corporation-tax/part-22/22-02-03.pdf | 2026-10-23 |
| TDM Part 29-02-03, R&D corporation tax credit (updated April 2026) | https://www.revenue.ie/en/tax-professionals/tdm/income-tax-capital-gains-tax-corporation-tax/part-29/29-02-03.pdf | 2026-10-23 |
| Revenue, Knowledge Development Box | https://www.revenue.ie/en/companies-and-charities/reliefs-and-exemptions/knowledge-development-box-kdb/index.aspx | 2026-10-23 |
| Revenue, what is Pillar Two | https://www.revenue.ie/en/companies-and-charities/pillar-two/what-is/index.aspx | 2026-10-23 |
| Revenue, UTPR top-up tax (fiscal years commencing on or after 31 December 2024) | https://www.revenue.ie/en/companies-and-charities/pillar-two/what-is/uptr-top-up-tax.aspx | 2026-10-23 |
| Revenue, domestic top-up tax | https://www.revenue.ie/en/companies-and-charities/pillar-two/what-is/domestic-top-up-tax.aspx | 2026-10-23 |
| Revenue, Pillar Two key dates | https://www.revenue.ie/en/companies-and-charities/pillar-two/dates/index.aspx | 2026-10-23 |
| Revenue, preliminary CT | https://www.revenue.ie/en/companies-and-charities/corporation-tax-for-companies/corporation-tax-payment-and-filing/preliminary-ct.aspx | 2026-10-23 |
| Revenue, when is preliminary CT due | https://www.revenue.ie/en/companies-and-charities/corporation-tax-for-companies/corporation-tax-payment-and-filing/when-is-preliminary-ct-due.aspx | 2026-10-23 |
| Revenue, CT payment and filing | https://www.revenue.ie/en/companies-and-charities/corporation-tax-for-companies/corporation-tax-payment-and-filing/payment-and-filing.aspx | 2026-10-23 |
| TDM Part 47-06-08, late filing surcharge (updated July 2025) | https://www.revenue.ie/en/tax-professionals/tdm/income-tax-capital-gains-tax-corporation-tax/part-47/47-06-08.pdf | 2026-10-23 |
| TDM Part 47-06-04, restriction of reliefs | https://www.revenue.ie/en/tax-professionals/tdm/income-tax-capital-gains-tax-corporation-tax/part-47/47-06-04.pdf | 2026-10-23 |
| Revenue, close company surcharge | https://www.revenue.ie/en/companies-and-charities/corporation-tax-for-companies/close-companies/surcharge.aspx | 2026-10-23 |
| TDM Part 13-02-06, service company surcharge | https://www.revenue.ie/en/tax-professionals/tdm/income-tax-capital-gains-tax-corporation-tax/part-13/13-02-06.pdf | 2026-10-23 |
| Revenue, capital allowances and deductions | https://www.revenue.ie/en/companies-and-charities/corporation-tax-for-companies/corporation-tax/capital-allowances-and-deductions.aspx | 2026-10-23 |
| Revenue, trading losses | https://www.revenue.ie/en/companies-and-charities/corporation-tax-for-companies/corporation-tax/trading-losses.aspx | 2026-10-23 |
| Revenue, group relief | https://www.revenue.ie/en/companies-and-charities/reliefs-and-exemptions/group-relief/index.aspx | 2026-10-23 |
| TDM Part 35D-01-01, interest limitation (updated December 2025) | https://www.revenue.ie/en/tax-professionals/tdm/income-tax-capital-gains-tax-corporation-tax/part-35d/35D-01-01.pdf | 2026-10-23 |
| Revenue, start-up relief: can you claim | https://www.revenue.ie/en/starting-a-business/initiatives-startup-businesses-smes/tax-relief-for-new-startup-companies/can-you-claim-for-tax-relief-for-your-start-up-company.aspx | 2026-10-23 |
| Revenue, start-up relief: how it is calculated | https://www.revenue.ie/en/starting-a-business/initiatives-startup-businesses-smes/tax-relief-for-new-startup-companies/how-is-the-relief-calculated.aspx | 2026-10-23 |
| TDM Part 15-03-03, start-up relief | https://www.revenue.ie/en/tax-professionals/tdm/income-tax-capital-gains-tax-corporation-tax/part-15/15-03-03.pdf | 2026-10-23 |
| Revenue, who must submit iXBRL | https://www.revenue.ie/en/companies-and-charities/corporation-tax-for-companies/submitting-financial-statements/who-submit.aspx | 2026-10-23 |
| Revenue, participation exemption for foreign distributions | https://www.revenue.ie/en/companies-and-charities/reliefs-and-exemptions/exemption-foreign-distributions/index.aspx | 2026-10-23 |
| Revenue, Notes for Guidance TCA 1997, Part 2 (sections 25, 25A) | https://www.revenue.ie/en/tax-professionals/documents/notes-for-guidance/tca/part02.pdf | 2026-10-23 |
| Revenue, Notes for Guidance TCA 1997, Part 12 (sections 396, 396A, 397, 401) | https://www.revenue.ie/en/tax-professionals/documents/notes-for-guidance/tca/part12.pdf | 2026-10-27 |
| Revenue, iXBRL financial statements | https://www.revenue.ie/en/companies-and-charities/corporation-tax-for-companies/submitting-financial-statements/index.aspx | 2026-10-27 |
| Taxes Consolidation Act 1997 | https://www.irishstatutebook.ie/eli/1997/act/39/enacted/en/html | 2026-10-23 |

Not yet confirmed: whether the Finance (No. 2) Bill 2026 enacts the 31% CGT rate as in Financial Resolution No. 3 (if it does not, gains on disposals from 7 October 2026 go back to 33%); the other Bill proposals listed under "Deadlines and filing"; the preliminary tax due date for a large company with a period of less than seven months (Revenue's page gives none; see TDM Part 41A-07-02); the current car cost limit for capital allowances (TDM Part 11-00-01 not re-read); the earlier version's R&D condition that the spending must not be deductible abroad (not found in TDM Part 29-02-03 as read on 27 October 2026); the earlier version's point that a 2025 CT1 filed on exactly 23 November 2026 gets the 5% surcharge but the 50% relief restriction (section 1084 was not read in full; TDM Part 47-06-04 gives only "less than two months" and "two months or more").

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
