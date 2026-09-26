---
name: ireland-vat-return
description: Use this skill whenever asked to prepare, review, or classify transactions for an Irish VAT return (VAT3 form) for a self-employed individual or small business in Ireland. Trigger on phrases like "prepare VAT return", "do the VAT", "Irish VAT", "VAT3", "ROS return", "Revenue Online", or any request involving Ireland VAT filing. Also trigger when classifying transactions for VAT purposes from bank statements, invoices, or other source data. This skill covers Ireland only and only standard VAT-registered businesses. VAT groups, Capital Goods Scheme adjustments, and complex property transactions are in the refusal catalogue. MUST be loaded alongside BOTH vat-workflow-base v0.1 or later AND eu-vat-directive v0.1 or later. ALWAYS read this skill before touching any Irish VAT work.
version: 2.0
jurisdiction: IE
tax_year: 2026
last_updated: 2026-09-25
authored_by: OpenAccountants team
review_status: pending_review
trust_label: By OpenAccountants
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Irish VAT returns (VAT3 and RTD): 2026 rates, thresholds, cash basis, reverse charge and filing

## Scope

This Guide covers preparing and checking Irish VAT3 returns and the annual VAT Return of Trading Details (RTD) for a VAT-registered sole trader, partnership or company established in Ireland. Figures are for tax year 2026 (calendar 2026, the VAT year most Irish businesses are filing now). A dated section near the end covers 2025 periods, for late or amended returns.

It does not cover: VAT groups, the Capital Goods Scheme, supplies or lettings of property, partial exemption beyond spotting it, margin schemes, the flat-rate farmer scheme, One-Stop Shop returns, or customs. Those are in "When to refuse or refer".

The law is the Value-Added Tax Consolidation Act 2010 (VATCA 2010), as amended each year by a Finance Act. Revenue's own guidance is on [revenue.ie](https://www.revenue.ie/en/vat/index.aspx); Acts are on [irishstatutebook.ie](https://www.irishstatutebook.ie/eli/2025/act/18/enacted/en/html).

## Ask the client first

- Are you registered for VAT, and from what date? What is your VAT number? If not registered, what did you sell in 2025 and so far in 2026, and is it goods, services or both?
- Which taxable period is this, and what period does ROS show for you (two-monthly, four-monthly, six-monthly or monthly)?
- Are you on the invoice basis or authorised by Revenue for the moneys received (cash) basis? Ask for the authorisation letter.
- What does the business sell, and at which rates? Any restaurant, catering, hot food, hairdressing, hotel, construction, energy or livestock supplies?
- Did any sale or purchase straddle 1 July 2026 (the hospitality and hairdressing rate change)?
- Do you make any VAT-exempt sales (for example financial, insurance, medical, education, residential letting)? If yes, how much?
- Do you buy services or goods from outside Ireland (software subscriptions, advertising, consultants, stock)? Do you import goods, or sell to customers outside Ireland? Do EU customers give you a VAT number?
- Are you in construction? Are you a principal contractor who must operate Relevant Contracts Tax (RCT), a subcontractor, or both? Are any customers or suppliers connected to you?
- Do you own or lease a car used for the business? When was it first registered, what are its CO2 emissions, and how much is business use?
- Is any return or RTD outstanding, and what is the accounting year end (it sets the RTD due date)?

## The method, step by step

1. **Confirm status and period.** Check the VAT registration, the taxable period on ROS and the basis (invoice or moneys received). If the client is not registered, test the thresholds first; if they are over, stop and deal with registration.
2. **Collect the evidence.** Sales invoices and credit notes, purchase invoices, customs documents for imports, and the bank statements for the period. A purchase with no valid VAT invoice (or customs receipt) gets no input credit.
3. **Classify every sale by rate and place of supply.** Irish sales at the standard, reduced, second reduced, livestock or zero rate, exempt sales, EU business sales (no Irish VAT, reported in E1 or ES1 and on VIES), exports and non-EU business services (no Irish VAT). Use the rate in force on the date VAT becomes due, not the payment date.
4. **Find the reverse-charge and self-accounting items.** Services bought from any supplier outside Ireland, goods bought from other EU countries, construction services received as principal contractor under RCT, construction services between connected persons, and imports under postponed accounting. Put the VAT in T1 and, where deductible, the same amount in T2. Account for received services by the earliest of invoice date, payment date or the 15th of the month after the service; for EU goods, no later than the 15th of the month after arrival.
5. **Test each purchase for input credit.** It must be used for taxable supplies or qualifying activities, carry a valid invoice, and not be on the blocked list (food, drink, accommodation, entertainment, cars except qualifying cars, petrol). Apportion shared costs; refer if exempt sales are more than incidental.
6. **Complete the VAT3.** T1 total VAT on sales plus self-accounted VAT; T2 total deductible VAT; T3 or T4 is the difference; then E1, E2, ES1, ES2 and PA1 values. Enter zero, never "nil", on an empty return.
7. **File and pay on ROS by the 23rd** of the month after the period ends (the 19th for the few who do not file on ROS). File a return even when nothing is due.
8. **At the year end**, file the final VAT3 and then the RTD by the 23rd of the month after the accounting year ends. An outstanding RTD holds up refunds.

What breaks when the order is wrong: classifying purchases before checking the basis puts cash-basis clients' sales in the wrong period; skipping step 4 understates T1 and leaves an unclaimed T2, which is an error even when the net is nil; using the payment date for the rate misplaces sales around 1 July 2026.

## Registration thresholds for 2025 and 2026 ([Revenue: VAT thresholds](https://www.revenue.ie/en/vat/vat-registration/who-should-register-for-vat/vat-thresholds.aspx); [Finance Act 2024, s.78](https://www.irishstatutebook.ie/eli/2024/act/43/section/78/enacted/en/html))

Registration is obligatory when annual turnover **exceeds** the threshold. Below it, a business established in Ireland may elect to register.

| Who | Threshold (2025 and 2026) | Before 1 January 2025 |
| --- | --- | --- |
| Services only | €42,500 | €40,000 |
| Goods taxed at the reduced or standard rate that you made or produced from zero-rated materials | €42,500 | Not captured |
| Goods, or goods and services where 90% or more of turnover is from goods | €85,000 | €80,000 |
| Distance sales of goods and cross-border telecoms, broadcasting and electronic services to EU consumers (all EU States together) | €10,000 | Not captured |
| Acquisitions of goods from other EU Member States | €41,000 | Not captured |
| Services received from abroad | No threshold | No threshold |
| Business not established in Ireland supplying taxable goods or services to taxable customers in Ireland | No threshold (unless using the VAT SME Scheme) | Not captured |

- Finance Act 2024 section 78 raised the goods threshold from €80,000 to €85,000 and the services threshold from €40,000 to €42,500 **with effect from 1 January 2025**. Finance Act 2025 did not change these amounts; the same figures apply for 2026.
- **How turnover is measured:** Revenue says to total, excluding VAT, "in a calendar year" your taxable supplies, supplies of immovable goods, certain financial transactions and insurance services. Leave out occasional disposals of business assets (such as a van), transfers of goods to a non-EU country with no supply, and exempt cross-border supplies of new means of transport.
- **Services received from abroad have no threshold** ([received services](https://www.revenue.ie/en/vat/vat-on-services/exceptions-general-place-supply-rules-services/received-services/index.aspx)). An unregistered business, or one making only exempt supplies, that buys taxable services from abroad for business may have to register just for that.
- **Construction:** a principal contractor who must operate RCT and receives construction services from a subcontractor must register and account for VAT whatever its turnover ([construction services manual](https://www.revenue.ie/en/tax-professionals/tdm/value-added-tax/part11-immovable-goods/construction-services/construction-servcies.pdf)).
- **Electing to register** cannot be backdated: "You can only elect to register for VAT from a current date" ([Revenue: electing](https://www.revenue.ie/en/vat/vat-registration/who-should-register-for-vat/elect-register-vat.aspx)).
- **EU VAT SME Scheme** (from 1 January 2025) lets a small Irish business use another Member State's exemption threshold, if it is established only in Ireland, stays under that State's threshold and under the Union threshold of €100,000, and registers for the scheme with Revenue ([Revenue: EU VAT SME Scheme](https://www.revenue.ie/en/vat/vat-registration/eu-vat-sme-scheme/index.aspx)).

## Rates in force in 2026 ([Revenue: current VAT rates](https://www.revenue.ie/en/vat/vat-rates/search-vat-rates/current-vat-rates.aspx); [second reduced rate](https://www.revenue.ie/en/vat/vat-rates/what-are-vat-rates/second-reduced-rate-vat.aspx))

| Rate | Main supplies (examples only: check each item) | Dates |
| --- | --- | --- |
| 23% standard | Most goods and services, for example solicitor and consultancy services, furniture, motor vehicles, tyres, batteries | In force throughout 2025 and 2026 |
| 13.5% reduced | Hotel and guesthouse lettings, cinema, theatre and museum admissions, amusement parks, open farms, certain printed matter (not books), certain fuels, certain building services, repair, cleaning and maintenance services, short-term hire, tour guides, greyhounds | In force; catering and hairdressing left this rate on 30 June 2026 |
| 9% second reduced | Periodicals and certain e-periodicals; sporting facilities (not non-profit); electricity; gas for heating or lighting; catering and restaurant supplies (not alcohol, soft drinks or bottled water); hot take-away food and hot tea and coffee; hairdressing; construction of qualifying apartments | Catering, hot food and hairdressing from 1 July 2026; electricity and gas 1 May 2022 to 31 December 2030; qualifying apartments 26 November 2025 to 31 December 2030 |
| 4.8% livestock | Livestock generally, and horses normally used for food production or farming | In force |
| 0% zero | Exports; intra-EU supplies of goods to VAT-registered customers; certain food and drink; certain oral and non-oral medicines and sanitary products; certain books, e-books, audiobooks, newspapers and e-newspapers; certain animal feed, fertilisers, seeds and plants; solar panels on private dwellings and schools; clothing and footwear for children under 11 | In force |
| 4.5% flat-rate addition | Charged by unregistered flat-rate farmers (5.1% in 2025) | From 1 January 2026 |

Sources for each line: [standard rate](https://www.revenue.ie/en/vat/vat-rates/what-are-vat-rates/standard-rate-vat.aspx), [reduced rate](https://www.revenue.ie/en/vat/vat-rates/what-are-vat-rates/reduced-rate-vat.aspx), [zero rate](https://www.revenue.ie/en/vat/vat-rates/what-are-vat-rates/zero-rate-vat.aspx), [livestock rate](https://www.revenue.ie/en/vat/vat-rates/what-are-vat-rates/livestock-rate-vat.aspx), [restaurant and catering](https://www.revenue.ie/en/vat/vat-on-services/restaurant-catering-and-canteen-services/index.aspx), [Finance Act 2025 s.71 (hospitality from 1 July 2026)](https://www.irishstatutebook.ie/eli/2025/act/18/section/71/enacted/en/html), [s.69 (energy to 2030)](https://www.irishstatutebook.ie/eli/2025/act/18/section/69/enacted/en/html), [s.73 (flat-rate addition)](https://www.irishstatutebook.ie/eli/2025/act/18/section/73/enacted/en/html).

- **The hospitality change is dated.** Catering and restaurant supplies (excluding alcohol, soft drinks and bottled water), hot take-away food, hot tea and coffee, and hairdressing were at the reduced rate from 1 September 2023 to 30 June 2026, and are at the second reduced rate from 1 July 2026. Hotel and guesthouse lettings stay at the reduced rate.
- **Which rate applies to a sale** ([when is VAT due](https://www.revenue.ie/en/vat/accounting-for-vat/when-is-vat-due/index.aspx)): with an invoice, the rate in force when you issue it (or should have issued it); without an invoice, the rate on the date of supply or of any advance payment. On the moneys received basis, use the rate when the goods or services were supplied, not when paid ([cash basis rates](https://www.revenue.ie/en/vat/accounting-for-vat/accounting-for-vat-on-moneys-received/vat-rates-moneys-received-basis.aspx)).
- **Items not on these lists** (passenger transport, taxis and many specific goods): look them up in Revenue's VAT rates database before charging or claiming. Until confirmed, do not claim input VAT unless a valid VAT invoice shows it.

## The VAT3 boxes ([Revenue: completing the VAT3](https://www.revenue.ie/en/vat/accounting-for-vat/how-to-account-for-value-added-tax/completing-vat3-return.aspx))

| Box | What goes in it |
| --- | --- |
| T1 VAT on sales | VAT due on your supplies of goods and services, plus VAT you self-account on intra-EU acquisitions of goods, imports under postponed accounting, and services received from abroad |
| T2 VAT on purchases | VAT you are entitled to reclaim on costs for your taxable supplies and qualifying activities, including the deductible part of the self-accounted items above and the flat-rate addition |
| T3 VAT payable | T1 minus T2, when T1 is greater |
| T4 VAT repayable | T2 minus T1, when T2 is greater |
| E1 | Value of goods sent to customers in other EU countries |
| E2 | Value of goods received from suppliers in other EU countries |
| ES1 | Value of services supplied to customers in other EU countries |
| ES2 | Value of services received from suppliers in other EU countries |
| PA1 | Customs value plus customs duty of goods imported under postponed accounting |

- Credit notes issued or received adjust T1 and T2.
- A period with nothing payable or repayable still needs a return, with zero in T1 to T4. Do not write "nil".
- Services bought from outside the EU go in T1 and T2 but not in ES2 (ES2 is EU suppliers only).

## Periods, filing and payment for 2026 ([Revenue: when VAT becomes payable](https://www.revenue.ie/en/vat/accounting-for-vat/how-to-account-for-value-added-tax/when-vat-becomes-payable.aspx))

| Period type | Who | Condition |
| --- | --- | --- |
| Two-monthly (standard) | Everyone unless authorised otherwise | Periods start 1 January, March, May, July, September and November |
| Four-monthly | Authorised by the Collector-General | Annual VAT liability between €3,001 and €14,400 |
| Six-monthly | Authorised by the Collector-General | Annual liability between €1 and €3,000 |
| Monthly | Authorised by Revenue on request | Generally for businesses in a constant repayment position |

- **Deadline:** file and pay by the 19th of the month after the period ends; for ROS filers the time limit is extended to the 23rd. For 2026 two-monthly periods on ROS: January–February by 23 March, March–April by 23 May, May–June by 23 July, July–August by 23 September, September–October by 23 November, November–December by 23 January 2027.
- **Payment** is made through ROS or myAccount ([how do you pay VAT](https://www.revenue.ie/en/vat/accounting-for-vat/how-do-you-pay-vat/index.aspx)).
- **Repayments** go to a bank account; Revenue may withhold them if returns are outstanding and may offset them against other tax owed ([repayment of VAT](https://www.revenue.ie/en/vat/accounting-for-vat/how-to-account-for-value-added-tax/vat-repayment.aspx)).

## The Return of Trading Details (RTD) ([Tax and Duty Manual: VAT RTD](https://www.revenue.ie/en/tax-professionals/tdm/value-added-tax/part09-obligations-accountable-persons/return/VAT-RTD-S76.pdf))

- **Who:** every VAT-registered person, once a year, from the ROS inbox with the final VAT3 of the year.
- **When:** the 23rd of the month after the month in which the accounting period (for income tax or corporation tax) ends. Accounting year to 31 August means RTD by 23 September. Businesses exempt from ROS filing have 19 days.
- **What:** net-of-VAT values for the year, by Irish rate, in four sections: (1) supplies of goods and services, including exempt sales, EU and export sales, and services bought from outside the EU on a self-accounting basis; (2) acquisitions from the EU and imports under postponed accounting (the items in E2, ES2 and PA1); (3) goods and services bought for resale; (4) other deductible goods and services (overheads). Items in section 2 also go in section 3 or 4. No negative figures. EU sales to consumers taxed under the One-Stop Shop are left out.
- **If it is late:** refund claims under any taxhead are withheld while the previous year's RTD is outstanding, and failure to file an RTD carries a fixed penalty of €4,000 ([fixed penalties](https://www.revenue.ie/en/vat/interest-and-penalties/when-are-penalties-payable-to-revenue/fixed-penalties.aspx)).

## Moneys received (cash) basis ([Revenue: who may opt](https://www.revenue.ie/en/vat/accounting-for-vat/accounting-for-vat-on-moneys-received/who-can-opt-moneys-received-basis.aspx))

- **Eligibility (either test):** turnover that does not exceed, and is not likely to exceed, €2,000,000 in any continuous 12 months; **or** at least 90% of supplies made to customers who are unregistered or cannot claim full VAT deduction (retailers, pubs, restaurants and similar).
- **Revenue must authorise it.** A new registrant ticks the box on the registration form; a registered business applies in writing with its turnover and the share of sales to unregistered persons ([how to apply](https://www.revenue.ie/en/vat/accounting-for-vat/accounting-for-vat-on-moneys-received/how-apply-moneys-received-basis.aspx)). It takes effect from the start of the period in which Revenue issues approval, or a later date given.
- **Not allowed for:** transactions with a connected person; construction services from a subcontractor to a principal contractor; certain pre-2008 long leases; intra-EU acquisitions; imports.
- **What counts as received:** money lodged to your account, money received by an agent (such as a solicitor) on your behalf, Professional Services Withholding Tax and RCT withheld by the customer, set-offs, and payments made under a Revenue attachment ([sums included](https://www.revenue.ie/en/vat/accounting-for-vat/accounting-for-vat-on-moneys-received/sums-included-money-received-basis.aspx)). Revenue's example: a €1,230 fee including €230 VAT, with €200 PSWT withheld, is treated as €1,230 received and the full €230 VAT is due.
- **Invoices:** normal invoicing rules still apply.
- **Losing eligibility** ([eligibility and cancellation](https://www.revenue.ie/en/vat/accounting-for-vat/accounting-for-vat-on-moneys-received/vat-moneys-received-basis-eligibility-cancellation.aspx)): if sales to unregistered persons fall below 90% over four consecutive months, or turnover is likely to exceed €2,000,000 in a continuous 12 months, notify Revenue by the end of the following month. If you do not notify, the authorisation is cancelled from the start of the period in which you should have notified.

## Input credit: what you can and cannot reclaim ([Revenue: who can reclaim VAT](https://www.revenue.ie/en/vat/reclaiming-vat/who-can-reclaim-vat.aspx))

- **Conditions:** the cost is used for your taxable supplies or qualifying activities; you hold a valid VAT invoice or relevant customs receipt; the claim is made through the VAT3. No credit for costs of exempt supplies or non-business activities; costs used for both are apportioned.
- **Time limit:** four years for claiming a repayment.
- **Blocked even for fully taxable businesses:** food, drink or other personal services for you, agents or employees (unless part of a taxable supply of services); accommodation (except qualifying conference accommodation); food, drink, accommodation or entertainment forming part of the cost of advertising services; entertainment; passenger motor vehicles (except qualifying vehicles or stock-in-trade); petrol (unless stock-in-trade); goods bought under a margin scheme; property costs used for a non-business purpose.
- **Qualifying cars** ([Tax and Duty Manual: partial recovery](https://www.revenue.ie/en/tax-professionals/tdm/value-added-tax/part03-taxable-transactions-goods-ica-services/Goods/partial-recovery-of-VAT-on-qualifying-passenger-motor-vehicles.pdf)): up to 20% of the VAT on buying, hiring, acquiring or importing the car is deductible if the car is used at least 60% for business for 2 years or more, and it was first registered from 1 January 2021 with CO2 under 140g/km (or registered 2009 to 2020 with CO2 under 156g/km). On a lease, 20% of the VAT on each monthly charge. If a car bought is sold within 2 years, part or all of the credit is paid back: all within 6 months, 75% at 6 to 12 months, 50% at 12 to 18 months, 25% at 18 to 24 months. The same scale applies if, within 2 years, business use stops or falls below 60%; the use is reviewed every 6 months. No adjustment for hired or leased cars. Vans are not passenger motor vehicles.
- **Diesel** is not on the blocked list; petrol is.

## Reverse charge and cross-border ([general place of supply](https://www.revenue.ie/en/vat/vat-on-services/when-is-vat-charged-on-services/general-place-of-supply-rules-for-services.aspx); [received services](https://www.revenue.ie/en/vat/vat-on-services/exceptions-general-place-supply-rules-services/received-services/index.aspx))

- **Services bought from abroad (EU or non-EU) for business:** place of supply is Ireland; you self-account at the Irish rate in T1 and reclaim in T2 if deductible. Give your VAT number to EU suppliers, or you may be charged their VAT. Revenue's example: €100,000 German consultancy at 23% gives €23,000 in T1 and, if deductible, €23,000 in T2.
- **Read the invoice, not the brand.** A supplier invoicing from Ireland with Irish VAT is a domestic purchase: claim the VAT in T2, no reverse charge. Only a supplier established outside Ireland triggers self-accounting.
- **Goods bought from other EU countries** ([self-accounting](https://www.revenue.ie/en/vat/goods-and-services-to-and-from-abroad/acquisitions-from-other-eu-member-states/self-accounting-for-vat.aspx)): the supplier zero-rates; you account for Irish VAT in T1, reclaim in T2 if deductible, and put the value in E2. Revenue's example: €5,000 of goods at 23% gives €1,150 in T1 and T2.
- **Services sold to EU businesses:** no Irish VAT. Get and check the customer's VAT number, put it on the invoice, say the reverse charge applies, report the value in ES1 and on the VIES return ([obligations when supplying abroad](https://www.revenue.ie/en/vat/vat-on-services/when-is-vat-charged-on-services/vat-obligations-of-Irish-traders-supplying-services-to-business-customers-abroad.aspx)). If you misidentify a consumer as a business, you owe the VAT.
- **Goods sold to EU businesses** ([zero rate on ICS](https://www.revenue.ie/en/vat/goods-and-services-to-and-from-abroad/intracommunity-supplies/supplies-of-goods-to-businesses-in-the-european-union-eu.aspx)): zero-rated only if all five conditions hold: customer registered in another Member State; you keep its VAT number with country prefix; both numbers on the invoice; goods leave Ireland; correct VIES returns filed. Otherwise charge Irish VAT. Value in E1.
- **Sales to EU consumers:** Irish VAT unless your EU-wide distance sales and electronic services exceed the €10,000 threshold ([VAT thresholds](https://www.revenue.ie/en/vat/vat-registration/who-should-register-for-vat/vat-thresholds.aspx)), or you opted for destination taxation or the One-Stop Shop.
- **Imports** ([postponed accounting manual](https://www.revenue.ie/en/tax-professionals/tdm/value-added-tax/part07-provisions-relating-to-imports-exports/postponed-accounting.pdf)): goods from outside the EU, including Great Britain, are imports. Under postponed accounting the VAT goes in T1 and T2 and the customs value plus duty in PA1; otherwise VAT is paid at entry and reclaimed in T2 with the customs receipt. Goods moving between Ireland and Northern Ireland stay within the EU VAT regime; services do not.

## Construction: the RCT reverse charge ([construction services manual](https://www.revenue.ie/en/tax-professionals/tdm/value-added-tax/part11-immovable-goods/construction-services/construction-servcies.pdf))

- **When it applies:** construction services supplied by a subcontractor to a principal contractor where RCT must be operated (public bodies can be principal contractors), and construction services between connected persons.
- **Subcontractor:** invoices without VAT, showing everything a VAT invoice shows except the rate and amount, with its VAT number and the words "VAT on this supply to be accounted for by the principal contractor". Its T1 is nil for those supplies; it still reclaims its own input VAT in T2.
- **Principal contractor:** pays the subcontractor without VAT, works out RCT on the VAT-exclusive amount, puts the VAT in T1 for the period of the supply (or of an advance payment), and claims it in T2 in the same return if entitled. Must register whatever its turnover. A principal contractor must always account for VAT on construction services from non-resident subcontractors.
- **Rate:** the reduced rate generally applies to construction services; the second reduced rate to qualifying apartments (26 November 2025 to 31 December 2030) and heat pump systems; the standard rate to building materials sold alone and to scaffolding ([Revenue: construction services](https://www.revenue.ie/en/vat/vat-on-property-and-construction/construction-fixtures-fittings-solar-panels/construction-services.aspx); heat pumps and scaffolding: [construction services manual](https://www.revenue.ie/en/tax-professionals/tdm/value-added-tax/part11-immovable-goods/construction-services/construction-servcies.pdf)).
- **Not reverse charge:** a builder working for a private householder, or for a business that is not its principal contractor for RCT, charges VAT normally.
- The two-thirds rule does not apply to reverse-charge construction or to services between connected parties.
- The cash basis cannot be used for subcontractor-to-principal construction supplies.

## Two-thirds rule ([Revenue: two-thirds rule](https://www.revenue.ie/en/vat/vat-on-services/two-thirds-rule/index.aspx))

When a service includes goods, compare the VAT-exclusive **cost** of the goods with the VAT-exclusive total price. If the cost of goods **exceeds** two-thirds of the price, the goods rate applies to the whole job; if it does not exceed two-thirds, the service rate applies. It does not apply to repair and maintenance of motor vehicles and agricultural machinery, reverse-charge construction, or construction between connected parties.

## Boundary and exception table ([Revenue: completing the VAT3](https://www.revenue.ie/en/vat/accounting-for-vat/how-to-account-for-value-added-tax/completing-vat3-return.aspx))

| Transaction | Treatment | Boxes |
| --- | --- | --- |
| Software subscription invoiced from another EU State | Self-account at the Irish rate | T1 and T2; value in ES2 |
| Software subscription invoiced from outside the EU | Self-account at the Irish rate | T1 and T2; no ES2 |
| Supplier invoice from an Irish entity showing Irish VAT | Domestic purchase | T2 only |
| Consultancy sold to a business in another EU State with a valid VAT number | No Irish VAT; VIES | ES1 |
| Consultancy sold to a business outside the EU, with proof it is a business | No Irish VAT | Not in T1 |
| Goods bought from an EU supplier | Self-account | T1 and T2; value in E2 |
| Goods sold to an EU business meeting all five conditions | Zero rate; VIES | E1 |
| Import from Great Britain under postponed accounting | Self-account | T1 and T2; PA1 |
| Subcontractor invoice to you as RCT principal | Self-account, usually at the reduced rate | T1 and T2 |
| Restaurant meal, client entertainment, hotel stay | Blocked (except qualifying conference accommodation) | None |
| Petrol | Blocked unless stock-in-trade | None |
| Qualifying car bought or leased | Part of the VAT, if all conditions met | T2 (part) |
| Bank charges, loan interest, insurance premiums, wages, PRSI, PAYE, tax payments, transfers between own accounts | No VAT to reclaim; exclude | None |
| Commercial rent with VAT on the invoice | Domestic purchase | T2 |
| Residential rent | No VAT; exclude | None |

**Conservative defaults when evidence is missing:** unknown VAT status of a purchase = not deductible; unknown business-use share = no recovery; unknown customer status for an EU sale = consumer, charge Irish VAT; unknown whether a transaction is in scope = in scope; unknown rate on a sale = standard rate until checked. Flag every default to the client.

## Penalties and interest ([fixed penalties](https://www.revenue.ie/en/vat/interest-and-penalties/when-are-penalties-payable-to-revenue/fixed-penalties.aspx); [interest](https://www.revenue.ie/en/vat/interest-and-penalties/when-is-interest-applied-by-revenue/index.aspx))

- **Interest** on late VAT is 0.0274% per day or part of a day, from the due date until paid. It also applies to a refund received in excess of the amount due, from the date received.
- **Direct debit payers:** if 80% or more of the annual liability was paid, interest runs on the balance from the due date of the year-end return; if less than 80%, it is backdated to six months before the final filing date of the annual return.
- **Fixed penalties** of €4,000 each include: failure to register; failure to charge and pay over VAT; failure to keep proper records; failure to meet invoicing rules; failure to file a VAT return; failure to file an RTD; failure to file a VIES statement; issuing a VAT invoice when not registered.
- **Tax-geared penalties** ([tax-geared penalties](https://www.revenue.ie/en/vat/interest-and-penalties/when-are-penalties-payable-to-revenue/tax-penalties.aspx); [Code of Practice](https://www.revenue.ie/en/tax-professionals/documents/code-of-practice-revenue-compliance-interventions.pdf)) apply to deliberately or carelessly incorrect returns or claims, or failure to file, as a percentage of the tax underpaid. For a first qualifying disclosure: careless without significant consequences 20%, reduced to 10% (prompted disclosure) or 3% (unprompted); careless with significant consequences 40%, 20% or 5%; deliberate 100%, 50% or 10%. "Significant consequences" means the default is more than 15% of the liability. Higher rates apply for second and later disclosures. A company secretary may face a separate €1,500 penalty (€3,000 for deliberate behaviour).

## Worked cases ([received services](https://www.revenue.ie/en/vat/vat-on-services/exceptions-general-place-supply-rules-services/received-services/index.aspx); [construction services manual](https://www.revenue.ie/en/tax-professionals/tdm/value-added-tax/part11-immovable-goods/construction-services/construction-servcies.pdf))

**Case 1: registration (services).** A web designer, established in Ireland, sells services only. Her 2026 sales reach €43,000 by September. That exceeds the €42,500 services threshold, so she must register. Had she stayed at or under €42,500 she could still elect, but only from a current date.

**Case 2: restaurant rate change.** A caterer invoices a business event: €2,000 food (net) plus €500 wine. Event and invoice on 20 June 2026: food at 13.5% = €270, wine at 23% = €115. Event and invoice on 10 July 2026: food at 9% = €180, wine at 23% = €115. The date of the invoice (or supply, if none) decides the rate, not the date of payment.

**Case 3: services from abroad.** ABC Ltd, fully taxable, buys €100,000 of consultancy from a German business: T1 includes €23,000, T2 includes €23,000, ES2 includes €100,000. It also pays a US software company €200 a month: self-account 23% = €46 in T1 and €46 in T2 each month, with nothing in ES2.

**Case 4: EU goods.** A trader buys €5,000 of stock from Germany for resale: T1 €1,150, T2 €1,150, E2 €5,000, net nil. The same value goes in the RTD sections for EU acquisitions and for purchases for resale.

**Case 5: construction.** Subcontractor B does €600,000 of building work for A Ltd, which must operate RCT. B's invoice shows no VAT. A Ltd accounts for VAT at 13.5% = €81,000 in T1 and claims €81,000 in T2. B puts nothing in T1 for this job and reclaims its own €13,000 input VAT in T2, so B is due a €13,000 repayment in T4.

**Case 6: qualifying car.** A fully taxable business buys a qualifying car (registered 2026, under 140g/km, at least 60% business use) with €4,000 VAT: it may claim 20% = €800. If it sells the car after 3 months, all €800 is paid back in the period of sale.

**Case 7: two-thirds rule and late payment.** A guitar repair is quoted at €300 net: materials cost €220 and labour and profit €80. Materials exceed two-thirds of the price, so the goods rate applies to the whole: €300 at 23% = €69. Separately, a business pays €10,000 of VAT, paid 30 days late: daily interest at 0.0274% on €10,000 for 30 days comes to €82.20.

## When to refuse or refer

- VAT groups: consolidated filing; refer.
- Capital Goods Scheme adjustments, supplies or lettings of property, option to tax, and developers: refer to a property VAT specialist.
- Partial exemption where exempt supplies are more than incidental: the apportionment needs agreement with Revenue; refer.
- Margin schemes (second-hand goods, art, antiques, travel agents): refer.
- Flat-rate farmers, sea fishers and horse trainers: special rules; refer.
- One-Stop Shop and Import One-Stop Shop returns, and customs warehousing: out of scope.
- Construction where it is unclear whether RCT applies to the contract, or whether parties are connected: get the RCT status on ROS or refer before choosing the treatment.
- Qualifying apartments, heat pumps and other property-linked second-reduced-rate supplies: refer unless the contract is clearly within Revenue's guidance.
- Any question of deliberate under-declaration, or a Revenue audit notice: refer to a tax adviser before a disclosure.

## 2025 periods (for late or amended 2025 returns) ([current VAT rates](https://www.revenue.ie/en/vat/vat-rates/search-vat-rates/current-vat-rates.aspx); [Finance Act 2024, s.78](https://www.irishstatutebook.ie/eli/2024/act/43/section/78/enacted/en/html))

- Rates in 2025: 23%, 13.5%, 9%, 4.8% and 0%, as in 2026, except catering, hot take-away food and hairdressing were at 13.5% for all of 2025, and the flat-rate addition was 5.1%.
- Thresholds in 2025: €42,500 services and €85,000 goods, from 1 January 2025.
- Qualifying apartments: the supply of certain qualifying apartments was at the second reduced rate from 8 October 2025 to 25 November 2025, and the supply and construction until completed of qualifying apartments from 26 November 2025 ([second reduced rate](https://www.revenue.ie/en/vat/vat-rates/what-are-vat-rates/second-reduced-rate-vat.aspx)).
- The 2025 RTD for a 31 December 2025 year end was due on 23 January 2026; if it is still outstanding, refunds are being withheld.
- Interest on late 2025 VAT runs at 0.0274% per day from the original due date.

## Completion checklist ([Revenue: completing the VAT3](https://www.revenue.ie/en/vat/accounting-for-vat/how-to-account-for-value-added-tax/completing-vat3-return.aspx); [records](https://www.revenue.ie/en/vat/vat-records-invoices-credit-notes/vat-records-to-be-kept/how-long-keep-records.aspx))

- Registration, period and basis confirmed; cash basis authorisation on file if used.
- Every sale has a rate or a zero, exempt or outside-scope reason, using the right date for the rate (1 July 2026 changes checked).
- Every foreign purchase checked for self-accounting; T1 and T2 both carry the self-accounted VAT.
- EU customer VAT numbers checked on VIES; E1 and ES1 match the VIES return; E2, ES2 and PA1 entered.
- Every T2 amount backed by a valid invoice or customs receipt; blocked items removed; car claims limited and conditions recorded.
- Construction invoices checked for RCT status; principal-contractor reverse charge in T1 and T2.
- T3 or T4 equals the difference between T1 and T2; zeros, not "nil", on an empty return.
- Filed and paid on ROS by the 23rd; RTD diary date set for the 23rd of the month after the year end.
- Records kept (claim-related records for six years or until the matter is finalised); defaults and open questions listed for the client.

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
