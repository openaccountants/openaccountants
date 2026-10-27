---
name: ie-vat-return
description: "Irish VAT for tax year 2026 under the Value-Added Tax Consolidation Act 2010 (VATCA) as revised to 1 August 2026, including Finance Act 2025. Covers the 23%, 13.5%, 9%, 4.8% and 0% rates, the move of catering, hot take-away food and hairdressing from 13.5% to 9% on 1 July 2026, the EUR 42,500 services and EUR 85,000 goods registration thresholds, the two-monthly VAT3 return and payment by the 19th (23rd on ROS), the annual Return of Trading Details (RTD), the EUR 2,000,000 cash (moneys received) basis, reverse charge on services from abroad, EU goods and RCT construction, VIES statements, blocked input credit and qualifying cars, 0.0274% daily interest and EUR 4,000 fixed and tax-geared penalties. Trigger on 'Irish VAT', 'VAT3', 'ROS VAT return', 'RTD', 'do I need to register for VAT in Ireland', 'Irish reverse charge', 'VIES Ireland'. Out of scope: income tax (ie-income-tax-form11), corporation tax (ie-corporation-tax), payroll (ie-payroll), withholding and treaties (ie-foreign-tax-and-withholding), residence (ie-cross-border); VAT groups, property, Capital Goods Scheme, margin schemes and OSS are referred."
version: 2.1
jurisdiction: IE
tax_year: 2026
last_updated: 2026-10-26
authored_by: Michael Cutajar and the OpenAccountants team
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Irish VAT returns (VAT3 and RTD), tax year 2026

> **Source-cited draft.** Drafted from the Value-Added Tax Consolidation Act 2010 as revised by the Law Reform Commission to 1 August 2026 (which includes Finance Act 2025), Finance Act 2025 Part 3, and Revenue's own VAT pages and Tax and Duty Manuals, all read on 2026-10-24. No accountant has reviewed it. Do not file from it without review by a qualified Irish professional.

Authority: the Revenue Commissioners (the Collector-General collects VAT). Returns and payments go through ROS (Revenue Online Service). Currency: euro. Section numbers below are VATCA 2010 unless another act is named. Ireland is in the EU, so EU VAT rules on intra-Community supplies, VIES and the One-Stop Shop apply.

See also: `ie-income-tax-form11`, `ie-corporation-tax`, `ie-payroll`, `ie-foreign-tax-and-withholding`, `ie-cross-border`, `ie-formation`. A second Irish VAT skill, `ireland-vat-return`, holds an older copy of this content and is due to be merged into this one.

## Who this applies to

- **Businesses established in Ireland** that make taxable supplies of goods or services. Registration is compulsory once annual turnover exceeds the goods or services threshold (s.6(1)(c) and (d)). Below it, a business may elect to register, but only from a current date; an election cannot be backdated (Revenue: elect to register).
- **The threshold test** is "annual turnover" in the **current calendar year or the previous calendar year** (s.6(1)(c), (d)). Revenue counts, excluding VAT: taxable supplies, supplies of immovable goods, certain financial transactions, and insurance and reinsurance. Leave out occasional disposals of business assets (a van, a building), transfers of goods to a non-EU country with no supply, and exempt cross-border supplies of new means of transport.
- **Which threshold:** the goods threshold applies only if at least 90% of turnover is from goods, and not from goods taxed at 13.5% or 23% that the person made wholly or mainly from zero-rated materials (s.6(1)(c)(ii)). Everyone else, including those makers, uses the services threshold (s.6(1)(d)).
- **Connected businesses:** where one person controls others that supply goods of the same class or services of the same nature, the turnover of all of them counts for each (s.6(2)(b)).
- **No threshold** applies to: a principal contractor that must operate Relevant Contracts Tax (RCT) and receives construction services from a subcontractor (Construction services TDM, para 3.1); a person who must self-account on services received from abroad (s.12), including a VAT-exempt business such as a bank, insurer or bookmaker that receives taxable services from abroad for its business (Revenue: received services); and a business not established in Ireland that supplies taxable goods or services to taxable customers in Ireland, unless it uses the EU VAT SME Scheme (Revenue: VAT thresholds).
- **Intra-EU acquisitions:** a person whose acquisitions of goods from other EU States (other than new means of transport and excise goods) exceed, or are likely to exceed, EUR 41,000 in any continuous 12 months must register (s.9(2)).
- **EU VAT SME Scheme** (s.92B, from 1 January 2025): a small business established only in Ireland can use another Member State's exemption, if it stays under that State's threshold and under the EUR 100,000 Union threshold, and registers for the scheme with Revenue.
- **Out of this skill:** VAT groups (s.15), Capital Goods Scheme and property (Part 8 Chapter 2, Part 7), margin schemes and auction schemes, flat-rate farmers (s.86), sea fishers and horse trainers, One-Stop Shop and Import One-Stop Shop returns (Chapters 6 to 8 of Part 9), customs warehousing. Refer these. Partial exemption is covered only far enough to spot it. Also refer: construction where the RCT status of the contract or a connection between the parties is unclear (check RCT status on ROS first), and any deliberate under-declaration or Revenue audit notice, before a disclosure is made.

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| Standard rate | 23% | 2025 and 2026 | VATCA s.46(1)(a), https://revisedacts.lawreform.ie/eli/2010/act/31/revised/en/html; Revenue current rates, https://www.revenue.ie/en/vat/vat-rates/search-vat-rates/current-vat-rates.aspx |
| Reduced rate (Schedule 3 goods and services: hotel and guesthouse lettings, cinema, theatre and museum admissions, amusement parks, open farms, certain printed matter, certain fuels, building services, repair, cleaning and maintenance, tour guides, short-term hire and more) | 13.5% | 2025 and 2026 | VATCA s.46(1)(c) and Sch. 3; https://www.revenue.ie/en/vat/vat-rates/what-are-vat-rates/reduced-rate-vat.aspx |
| Restaurant and catering services (not alcohol, soft drinks or bottled water), hot take-away food, hot tea and coffee, hairdressing (Sch. 3 paras 3(1), 3(3), 13(3)) | 13.5% to 30 June 2026; **9% from 1 July 2026** | 2026 | Finance Act 2025 s.71, https://www.irishstatutebook.ie/eli/2025/act/18/section/71/enacted/en/html; VATCA s.46(1)(cb) |
| Second reduced rate: periodicals and e-periodicals, sporting facilities (not non-profit), heat pump systems (Sch. 3 paras 7(a), 7A, 12, 12A) | 9% | 2025 and 2026 | VATCA s.46(1)(ca); https://www.revenue.ie/en/vat/vat-rates/what-are-vat-rates/second-reduced-rate-vat.aspx |
| Electricity, and gas for heating or lighting | 9%, 1 May 2022 to 31 December 2030 | 2026 | VATCA s.46(1)(caa) (Finance Act 2025 s.69) |
| Qualifying apartments (supply, and construction until completed) | 9%, 26 November 2025 to 31 December 2030 | 2026 | VATCA s.46(1)(cac), Sch. 3 para 9B |
| Certain qualifying apartments (supply only), for late or amended 2025 returns | 9%, 8 October 2025 to 25 November 2025 | 2025 | VATCA s.46(1)(cab), Sch. 3 para 9A |
| Livestock | 4.8% | 2025 and 2026 | VATCA s.46(1)(d) |
| Zero rate (exports, intra-EU supplies of goods to registered customers, most food, children's clothing and footwear, oral medicines, books, and the other Schedule 2 items) | 0% | 2025 and 2026 | VATCA s.46(1)(b) and Sch. 2 |
| Flat-rate addition charged by unregistered farmers | 4.5% (5.1% in 2025) | 2026 | Revenue current rates table; Finance Act 2025 s.73 |
| Services threshold (services, and goods made from zero-rated materials) | EUR 42,500 | 2025 and 2026 | VATCA s.2(1) "services threshold", s.6(1)(d); https://www.revenue.ie/en/vat/vat-registration/who-should-register-for-vat/vat-thresholds.aspx |
| Goods threshold (90% or more of turnover from goods) | EUR 85,000 | 2025 and 2026 | VATCA s.2(1) "goods threshold", s.6(1)(c) |
| Intra-EU acquisitions threshold (continuous 12 months) | EUR 41,000 | 2026 | VATCA s.9(2) |
| EU-wide distance sales and telecoms, broadcasting and electronic services to consumers | EUR 10,000 | 2026 | VATCA s.35(1); Revenue VAT thresholds |
| EU VAT SME Scheme Union threshold | EUR 100,000 | 2026 | VATCA s.92B(1) "Union threshold" |
| Cash (moneys received) basis: turnover limit, any continuous 12 months | EUR 2,000,000 (or 90% of supplies to unregistered customers) | 2026 | VATCA s.80(1); https://www.revenue.ie/en/vat/accounting-for-vat/accounting-for-vat-on-moneys-received/who-can-opt-moneys-received-basis.aspx |
| Four-monthly returns allowed if annual liability is | EUR 3,001 to EUR 14,400 | 2026 | https://www.revenue.ie/en/vat/accounting-for-vat/how-to-account-for-value-added-tax/when-vat-becomes-payable.aspx |
| Six-monthly returns allowed if annual liability is | EUR 1 to EUR 3,000 | 2026 | same page |
| VIES goods statement: quarterly allowed if intra-EU goods supplies per quarter (and in each of the last 4 quarters) do not exceed | EUR 50,000 | 2026 | VATCA s.82(1), (5) |
| Qualifying car: share of VAT deductible | 20%, if business use is at least 60% | 2026 | VATCA s.59(1), (2)(d) |
| Interest on late VAT | 0.0274% a day or part of a day | 2026 | VATCA s.114(1); https://www.revenue.ie/en/vat/interest-and-penalties/when-is-interest-applied-by-revenue/index.aspx |
| Fixed penalty (each failure) | EUR 4,000 | 2026 | VATCA s.115(1), (2), (4); https://www.revenue.ie/en/vat/interest-and-penalties/when-are-penalties-payable-to-revenue/fixed-penalties.aspx |

**Which rate applies to a sale** (s.74, s.80(2)(a)): with an invoice, the rate when the invoice is issued (or should have been issued); without one, the rate at the time of supply, or of any advance payment. On the cash basis, the rate when the goods or services were supplied, not when paid. So a function held and invoiced on 20 June 2026 is at 13.5%; the same function on 10 July 2026 is at 9%. For late or amended 2025 returns, catering, hot take-away food and hairdressing were at 13.5% for the whole of 2025.

**Items not listed here** (passenger transport, many specific goods): look them up in Revenue's VAT rates database before charging or claiming.

## The taxable base

**What is taxed.** The amount on which VAT is charged is the total consideration, including all taxes, commissions, costs and charges, but not the VAT itself (s.37). Foreign-currency amounts are converted at the latest Central Bank of Ireland or ECB selling rate when the VAT becomes due, unless Revenue agrees another method (s.37(4)).

**Two-thirds rule** (s.41; Revenue: two-thirds rule). When a service includes movable goods, compare the VAT-exclusive cost of the goods with the VAT-exclusive total price. If the goods exceed two-thirds, the whole job takes the goods rate; if not, the service rate. Revenue's example: a EUR 300 guitar repair with EUR 220 of materials takes 23% on the whole, EUR 69. The rule does not apply to repair of motor vehicles and agricultural machinery, reverse-charge construction, or construction between connected persons.

**Input credit** (s.59). You deduct VAT on goods and services used for taxable supplies or qualifying activities (for example exports of exempt financial services outside the EU), backed by a valid VAT invoice or customs document, claimed through the VAT3. No credit for costs of exempt or non-business activities; costs used for both are apportioned. Refund claims must be made within 4 years after the end of the taxable period (s.99(4)).

**Blocked even for a fully taxable business** (s.60(2)(a)):
- food, drink, accommodation or other personal services for you, your agents or employees, unless part of a taxable supply you make (qualifying conference accommodation is allowed);
- food, drink, accommodation or entertainment that forms part of an advertising service;
- entertainment;
- passenger motor vehicles, except qualifying vehicles, stock-in-trade, and cars used in a car-hire or driving-school business;
- petrol, unless stock-in-trade (diesel is not on the list);
- buying or developing immovable goods used for a purpose other than the business (s.60(2)(a)(iia));
- contract work that consists of handing over goods that are themselves blocked (s.60(2)(a)(vi));
- goods bought under a margin scheme or auction scheme (s.60(3)).

**Qualifying cars** (s.59(1), (2)(d); s.62; Revenue manual on partial recovery for cars). 20% of the VAT on buying, hiring, acquiring or importing a car is deductible if the car is used at least 60% for business, and it was first registered from 1 January 2021 with CO2 under 140g/km (or 2009 to 2020 with CO2 under 156g/km). On a lease, 20% of the VAT on each charge. If a bought car is sold, or its business use falls below 60%, within 2 years, the credit is clawed back by the formula in s.62: all of it within the first 182 days, 75% within the next 182, then 50%, then 25%. Example: EUR 4,000 VAT on a qualifying car gives a credit of EUR 800; if the car is sold after 3 months, the whole EUR 800 is paid back in the period of sale. There is no clawback for a hired or leased car. Revenue reviews business use every 6 months. Vans are not passenger cars.

**Cash (moneys received) basis** (s.80). Revenue may authorise it if turnover has not exceeded and is not likely to exceed EUR 2,000,000 in any continuous 12 months, or if at least 90% of turnover is from supplies to unregistered persons (retailers, pubs, restaurants). VAT is then due on money received in the period. It cannot be used for transactions with a connected person, construction services from a subcontractor to a principal contractor, pre-2008 long leases, intra-EU acquisitions or imports (Revenue: who may opt). Money received includes sums lodged to the supplier's account, sums received by an agent (such as a solicitor) on its behalf, Professional Services Withholding Tax and RCT withheld by the customer, sums paid to Revenue under an attachment, and debts settled by set-off (received on the date of the set-off) (Revenue: sums included). Revenue's PSWT example: a EUR 1,230 fee including EUR 230 VAT with EUR 200 PSWT withheld is treated as EUR 1,230 received, with EUR 230 VAT due. Normal invoicing rules still apply. If sales to unregistered persons fall below 90% over four consecutive months, or turnover is likely to pass EUR 2 million, tell Revenue by the end of the following month. If you do not, the authorisation is cancelled from the start of the VAT period in which you should have told Revenue (Revenue: eligibility and cancellation).

**Self-accounted VAT (reverse charge).** The customer, not the supplier, accounts for the VAT in these cases:
- services received from a supplier established outside Ireland where the place of supply is Ireland (s.12); Revenue's example: EUR 100,000 of German consultancy gives EUR 23,000 in T1 and, if deductible, EUR 23,000 in T2;
- goods acquired from other EU States (s.3(d), s.75: VAT due on the 15th of the month after the acquisition, or earlier on the supplier's invoice);
- construction operations supplied by a subcontractor to a principal contractor who must operate RCT, and construction services between connected persons (s.16(3); Construction services TDM);
- imports under postponed accounting (s.53A).
A supplier invoicing from Ireland with Irish VAT is a domestic purchase: claim the VAT in T2; there is no reverse charge.

**Construction under RCT** (Construction services TDM). The subcontractor invoices without VAT, adding "VAT on this supply to be accounted for by the principal contractor". The principal contractor puts the VAT in T1 and, if entitled, the same amount in T2 in the same return. Construction services are generally 13.5%; qualifying apartments and heat pump systems 9%; building materials sold alone and scaffolding 23%. A principal contractor always accounts for VAT on construction services from non-resident subcontractors. A builder working for a private householder charges VAT normally.

**Conservative defaults when evidence is missing.** Unknown VAT status of a purchase: not deductible. Unknown business-use share: no recovery. Unknown status of an EU customer: treat as a consumer and charge Irish VAT. Unknown whether a transaction is in scope: treat it as in scope. Unknown rate on a sale: standard rate until checked. Flag each default to the client.

**Boundary table** (Revenue: completing the VAT3):

| Transaction | Treatment | Boxes |
|---|---|---|
| Software subscription invoiced from another EU State | Self-account at the Irish rate | T1 and T2; value in ES2 |
| Software subscription invoiced from outside the EU | Self-account at the Irish rate | T1 and T2; no ES2 |
| Consultancy sold to a business in another EU State with a valid VAT number | No Irish VAT; VIES statement | ES1 |
| Consultancy sold to a business outside the EU, with proof it is a business | No Irish VAT | Not in T1 |
| Goods bought from an EU supplier | Self-account | T1 and T2; value in E2 |
| Goods sold to an EU business meeting all five zero-rate conditions | 0%; VIES statement | E1 |
| Import from Great Britain under postponed accounting | Self-account | T1 and T2; PA1 |
| Subcontractor invoice to you as RCT principal | Self-account, usually at 13.5% | T1 and T2 |
| Restaurant meal, client entertainment, hotel stay | Blocked (except qualifying conference accommodation) | None |
| Bank charges, interest, insurance, wages, PRSI, PAYE, tax payments, transfers between own accounts | No VAT; exclude | None |
| Commercial rent with VAT on the invoice | Domestic purchase | T2 |
| Residential rent | No VAT; exclude | None |

## Deadlines and filing

**Taxable period.** Two months, starting 1 January, 1 March, 1 May, 1 July, 1 September and 1 November (s.2(1)). The Collector-General may authorise longer periods, up to 12 months (s.77): four-monthly if the annual liability is EUR 3,001 to EUR 14,400, six-monthly if EUR 1 to EUR 3,000. Monthly returns are allowed for businesses usually in repayment. Check the period ROS shows for the client.

**VAT3 return and payment** (s.76(1)). File and pay within 9 days after the 10th of the month after the period ends, that is by the **19th** (Revenue's 2026 calendar for tax professionals lists the 19th). Revenue extends this to the **23rd** for those who file on ROS (Revenue: when VAT becomes payable); the RTD manual describes the 23rd as the date for those who pay and file on ROS. Interest runs from the date the tax became payable under s.76 (s.114(1)), so this skill counts days late from the 19th. For 2026 two-monthly periods on ROS: January to February by 23 March; March to April by 23 May; May to June by 23 July; July to August by 23 September; September to October by 23 November; November to December by 23 January 2027. File a return even when nothing is due, with zero (never "nil") in T1 to T4.

**VAT3 boxes** (Revenue: completing the VAT3):

| Box | What goes in it |
|---|---|
| T1 VAT on sales | VAT on your supplies, plus self-accounted VAT on EU acquisitions, imports under postponed accounting and services received from abroad |
| T2 VAT on purchases | Deductible VAT on costs, including the deductible part of the self-accounted items and the flat-rate addition |
| T3 VAT payable | T1 minus T2, when T1 is greater |
| T4 VAT repayable | T2 minus T1, when T2 is greater |
| E1 | Value of goods sent to customers in other EU States |
| E2 | Value of goods received from suppliers in other EU States |
| ES1 | Value of services supplied to customers in other EU States |
| ES2 | Value of services received from suppliers in other EU States (not non-EU) |
| PA1 | Customs value plus customs duty of goods imported under postponed accounting |

Credit notes issued or received adjust T1 and T2.

**Direct debit and annual returns** (s.77(5), s.114(3)). The Collector-General may let a trader pay an agreed schedule by monthly direct debit and file one return for the accounting period. If the balance due with that return is more than 20% of the year's liability, interest on it runs from 6 months before the return's due date.

**Return of Trading Details (RTD)** (Revenue TDM, VAT RTD, updated February 2026). Every registered person files one a year, with the final VAT3 of the year, by the **23rd of the month after the month in which the income tax or corporation tax accounting period ends** (19 days for those exempt from ROS). It shows net-of-VAT values by rate for: (1) supplies, including exempt, EU and export sales and self-accounted services; (2) EU acquisitions and postponed-accounting imports; (3) purchases for resale; (4) other deductible purchases. No negative figures; OSS sales are left out. While the previous year's RTD is outstanding, refunds under any taxhead are withheld.

**VIES statements.** Goods supplied to registered customers in other EU States: a statement for each month by the 23rd of the following month (s.82(3)); quarterly by the 23rd after the quarter if supplies do not exceed EUR 50,000 in the quarter or any of the previous 4 quarters (s.82(5)). Services where the EU customer pays the VAT: quarterly by the 23rd after the quarter, or monthly by election (s.83(3), (4)). A nil statement is needed for a period with no supplies if one was required for an earlier period.

**Repayments** go to a bank account. Revenue may withhold them while returns are outstanding and offset them against other tax owed (Revenue: repayment of VAT).

**Records** must be kept for 6 years from the date of the latest transaction they relate to (s.84(3)), and longer while a Revenue inquiry, a claim or an appeal on the matter is still open (s.84(4)).

**Method, in order.** (1) Confirm registration, period and basis. (2) Collect sales invoices, credit notes, purchase invoices, customs documents and bank statements. (3) Classify every sale by rate and place of supply, using the invoice date for the rate. (4) Find every reverse-charge item and put its VAT in T1 and, if deductible, T2. (5) Test each purchase for input credit and remove blocked items. (6) Complete T1 to T4, E1, E2, ES1, ES2 and PA1. (7) File and pay on ROS by the 23rd. (8) At the year end, file the RTD. Skipping step 4 understates T1 and leaves T2 unclaimed: an error even when the net is nil.

## Penalties and interest

**Interest** (s.114). Simple interest at **0.0274% for each day or part of a day** from the date the VAT became payable until paid. The same rate applies to a refund that was not properly due, from the date it was paid. On an assessment, Revenue charges interest from the date the original return was due.

**Fixed penalties of EUR 4,000** (s.115; Revenue: fixed penalties) include: failure to register; failure to charge and pay over VAT; failure to keep proper records; failure to meet invoicing rules; failure to file a VAT return; failure to file an RTD; failure to file a VIES statement; issuing a VAT invoice when not registered. Where a company commits the failure, the secretary is liable to a separate EUR 4,000 (s.115(4)).

**Tax-geared penalties** (s.116), as a share of the VAT underpaid or over-claimed:

| Behaviour | No cooperation | Full cooperation | Plus prompted qualifying disclosure | Plus unprompted qualifying disclosure |
|---|---|---|---|---|
| Deliberate | 100% | 75% | 50% | 10% |
| Careless, difference over 15% of the VAT properly payable | 40% | 30% | 20% | 5% |
| Careless, difference 15% or less | 20% | 15% | 10% | 3% |

A second qualifying disclosure within 5 years raises the reduced rates (s.116(13)). Using an incorrect invoice, VAT number, credit note or record carries EUR 3,000 if careless and EUR 5,000 if deliberate (s.116(8)). A company secretary faces a separate EUR 1,500 penalty, EUR 3,000 for deliberate behaviour (s.116(17)). A qualifying disclosure must be in writing, signed, with a declaration that it is complete, and paid with the tax and the interest. A prompted disclosure is one made after Revenue notifies the date an audit or inquiry will start and before it starts; once an inquiry has started and the person has been contacted, a disclosure no longer qualifies (s.116(1), (15)). An honest error that comes to light and is not fixed without unreasonable delay is treated as deliberate (s.116(9)).

## Cross-border points

- **Services sold to EU businesses.** No Irish VAT. Check the customer's VAT number on VIES, show it on the invoice, state that the reverse charge applies, and report the value in ES1 and on the VIES statement. If you treat a consumer as a business, you owe the VAT (Revenue: supplying services to business customers abroad).
- **Goods sold to EU businesses** (Revenue: intra-Community supplies). 0% only if all five conditions are met: the customer is registered in another Member State; you hold its VAT number with country prefix; both numbers are on the invoice; the goods leave Ireland; and correct VIES statements are filed. Otherwise charge Irish VAT. Value in E1.
- **Sales to EU consumers.** Irish VAT applies unless your EU-wide distance sales of goods and telecoms, broadcasting and electronic services exceed EUR 10,000 in the current or previous calendar year (s.35), or you opted for taxation in the customer's State. Above that, the customer's State's VAT applies, usually through the One-Stop Shop (referred).
- **Services bought from abroad.** Self-account at the Irish rate (s.12). Give your VAT number to EU suppliers so they do not charge their own VAT. Non-EU services go in T1 and T2 but not ES2.
- **Goods from other EU States.** Self-account in T1, reclaim in T2 if deductible, value in E2. Revenue's example: EUR 5,000 of German stock at 23% gives EUR 1,150 in T1 and T2.
- **Imports, including from Great Britain** (Postponed accounting TDM). Goods from outside the EU, including Great Britain, are imports. Under postponed accounting the VAT goes in T1 and T2 and the customs value plus duty in PA1; otherwise VAT is paid at entry and reclaimed in T2 with the customs document. Goods moving between Ireland and Northern Ireland stay inside the EU VAT regime; services do not.
- **Non-established suppliers** making supplies to taxable customers in Ireland register whatever their turnover (Revenue: VAT thresholds), unless the customer self-accounts.

## Worked examples

### Example 1: consultancy company, September to October 2026

Bray Advisory Ltd, registered, on the invoice basis, files two-monthly on ROS. In September and October 2026 it invoices Irish clients EUR 60,000 net at 23%: output VAT EUR 13,800. It invoices EUR 20,000 to a company in Germany that gave a valid VAT number: no Irish VAT, EUR 20,000 in ES1 and on the quarterly VIES statement. It pays a US software company EUR 1,000, with no VAT charged. The supplier is outside Ireland and Bray is a business, so Bray self-accounts at 23%: EUR 230 in T1 and EUR 230 in T2 (not in ES2, as the supplier is outside the EU). Its Irish purchase invoices carry EUR 2,100 of deductible VAT, after removing a client lunch (blocked).

T1 = 13,800 + 230 = EUR 14,030. T2 = 2,100 + 230 = EUR 2,330. T3 = EUR 11,700, due by 19 November 2026 (23 November on ROS). If Bray misses the ROS date and pays on 29 November, interest runs from 19 November, the date the tax became payable (s.76(1), s.114(1)): 11,700 × 0.0274% × 10 days = EUR 32.06.

```oa-check
name: Bray Advisory Ltd, Sep-Oct 2026 VAT3 with a reverse-charged US service, paid 10 days after 19 November
inputs:
  irish_sales: 60000
  eu_b2b_services: 20000
  us_software: 1000
  domestic_input_vat: 2100
  days_late: 10
steps:
  - output_vat: irish_sales * 23 / 100
  - reverse_charge_vat: us_software * 23 / 100
  - t1: output_vat + reverse_charge_vat
  - t2: domestic_input_vat + reverse_charge_vat
  - t3: t1 - t2
  - es1: eu_b2b_services
  - interest: round(t3 * 0.0274 / 100 * days_late, 2)
expected:
  output_vat: 13800
  reverse_charge_vat: 230
  t1: 14030
  t2: 2330
  t3: 11700
  es1: 20000
  interest: 32.06
```

### Example 2: restaurant after the 1 July 2026 rate change, with a careless error

The Harbour Kitchen Ltd runs a restaurant. In July and August 2026 it sells food for EUR 90,000 net and drinks (alcohol and soft drinks) for EUR 30,000 net. From 1 July 2026 the food is at 9% (Finance Act 2025 s.71); alcohol and soft drinks stay at 23%. Correct output VAT: 8,100 + 6,900 = EUR 15,000. Deductible input VAT is EUR 4,000, so the correct T3 is EUR 11,000, due by 19 September 2026 (23 September on ROS).

The till was set up wrongly and put the drinks at 9% too. The return showed EUR 10,800 of output VAT and T3 of EUR 6,800, which was paid on time. The VAT short is 30,000 × (23% − 9%) = EUR 4,200, which is 38% of the EUR 11,000 properly payable: over 15%. Revenue writes to say a compliance intervention will start on a set date. Before that date, on 23 November 2026, the company makes a prompted qualifying disclosure in writing and pays the EUR 4,200 with interest, and then cooperates fully. The careless penalty is 20% of EUR 4,200 = EUR 840 (s.116(7)(b)(I)(B)). Interest runs from 19 September, when the tax became payable (s.114(1)): 65 days to 23 November, so 4,200 × 0.0274% × 65 = EUR 74.80.

```oa-check
name: Harbour Kitchen Ltd, Jul-Aug 2026, drinks wrongly at 9%, prompted disclosure, interest from 19 September
inputs:
  food: 90000
  drinks: 30000
  input_vat: 4000
  days_late: 65
steps:
  - food_vat: food * 9 / 100
  - drinks_vat: drinks * 23 / 100
  - correct_t3: food_vat + drinks_vat - input_vat
  - declared_t3: (food + drinks) * 9 / 100 - input_vat
  - shortfall: correct_t3 - declared_t3
  - share_of_liability: round(shortfall / correct_t3, 4)
  - penalty: shortfall * 20 / 100
  - interest: round(shortfall * 0.0274 / 100 * days_late, 2)
expected:
  food_vat: 8100
  drinks_vat: 6900
  correct_t3: 11000
  declared_t3: 6800
  shortfall: 4200
  share_of_liability: 0.3818
  penalty: 840
  interest: 74.80
```

## Ask the client first

1. **Registration and turnover.** Are you registered, from what date, and on which period and basis (invoice or Revenue-authorised cash basis)? If not registered: turnover in 2025 and so far in 2026, and is it goods, services or both?
2. **What you sell.** Any catering, hot food, hairdressing, hotel, construction, energy or livestock supplies, or exempt sales (finance, insurance, medical, education, residential letting)? Did any sale straddle 1 July 2026?
3. **Who you sell to and where.** Do EU customers give you a VAT number? Do you sell goods abroad or to EU consumers online?
4. **What you buy from abroad.** Software, advertising, consultants, stock from the EU, imports from Great Britain or elsewhere.
5. **Construction.** Are you a principal contractor operating RCT, a subcontractor, or both? Are any customers or suppliers connected to you?
6. **Cars and open returns.** Any business car (first registration date, CO2, business use)? Is any VAT3, VIES statement or RTD outstanding, and when does your accounting year end?

## Sources

| Source | URL | Read on |
|---|---|---|
| Value-Added Tax Consolidation Act 2010, revised to 1 August 2026 (Law Reform Commission): ss.2, 6, 9, 12, 16, 35, 37, 41, 46, 53A, 59, 60, 62, 74, 75, 76, 77, 80, 82, 83, 84, 92B, 99, 114, 115, 116; Schs. 2 and 3 | https://revisedacts.lawreform.ie/eli/2010/act/31/revised/en/html | 2026-10-24 |
| Finance Act 2025, Part 3 (ss.67 to 77), in particular s.68 (threshold tests), s.69 (energy to 2030), s.71 (9% from 1 July 2026), s.73 (flat-rate addition), s.76 (fixed penalties for payment service providers; no change for other traders) | https://www.irishstatutebook.ie/eli/2025/act/18/enacted/en/html | 2026-10-24 |
| Finance Act 2025, s.71 | https://www.irishstatutebook.ie/eli/2025/act/18/section/71/enacted/en/html | 2026-10-24 |
| Revenue, current VAT rates (2023 to 2026) | https://www.revenue.ie/en/vat/vat-rates/search-vat-rates/current-vat-rates.aspx | 2026-10-24 |
| Revenue, second reduced rate (published 1 July 2026) | https://www.revenue.ie/en/vat/vat-rates/what-are-vat-rates/second-reduced-rate-vat.aspx | 2026-10-24 |
| Revenue, reduced rate (published 1 July 2026) | https://www.revenue.ie/en/vat/vat-rates/what-are-vat-rates/reduced-rate-vat.aspx | 2026-10-24 |
| Revenue, VAT thresholds (published 6 May 2026) | https://www.revenue.ie/en/vat/vat-registration/who-should-register-for-vat/vat-thresholds.aspx | 2026-10-24 |
| Revenue, electing to register | https://www.revenue.ie/en/vat/vat-registration/who-should-register-for-vat/elect-register-vat.aspx | 2026-10-24 |
| Revenue, EU VAT SME Scheme | https://www.revenue.ie/en/vat/vat-registration/eu-vat-sme-scheme/index.aspx | 2026-10-24 |
| Revenue, when VAT becomes payable (19th, 23rd on ROS; period options) | https://www.revenue.ie/en/vat/accounting-for-vat/how-to-account-for-value-added-tax/when-vat-becomes-payable.aspx | 2026-10-24 |
| Revenue, completing the VAT3 (published 28 July 2026) | https://www.revenue.ie/en/vat/accounting-for-vat/how-to-account-for-value-added-tax/completing-vat3-return.aspx | 2026-10-24 |
| Revenue, repayment of VAT | https://www.revenue.ie/en/vat/accounting-for-vat/how-to-account-for-value-added-tax/vat-repayment.aspx | 2026-10-24 |
| Revenue, who may opt for the moneys received basis (published 6 October 2026) | https://www.revenue.ie/en/vat/accounting-for-vat/accounting-for-vat-on-moneys-received/who-can-opt-moneys-received-basis.aspx | 2026-10-24 |
| Revenue, sums included in the moneys received basis | https://www.revenue.ie/en/vat/accounting-for-vat/accounting-for-vat-on-moneys-received/sums-included-money-received-basis.aspx | 2026-10-24 |
| Revenue, moneys received basis eligibility and cancellation | https://www.revenue.ie/en/vat/accounting-for-vat/accounting-for-vat-on-moneys-received/vat-moneys-received-basis-eligibility-cancellation.aspx | 2026-10-24 |
| Revenue, who can reclaim VAT | https://www.revenue.ie/en/vat/reclaiming-vat/who-can-reclaim-vat.aspx | 2026-10-24 |
| Revenue, two-thirds rule | https://www.revenue.ie/en/vat/vat-on-services/two-thirds-rule/index.aspx | 2026-10-24 |
| Revenue, received services | https://www.revenue.ie/en/vat/vat-on-services/exceptions-general-place-supply-rules-services/received-services/index.aspx | 2026-10-24 |
| Revenue, supplying services to business customers abroad | https://www.revenue.ie/en/vat/vat-on-services/when-is-vat-charged-on-services/vat-obligations-of-Irish-traders-supplying-services-to-business-customers-abroad.aspx | 2026-10-24 |
| Revenue, supplies of goods to businesses in the EU | https://www.revenue.ie/en/vat/goods-and-services-to-and-from-abroad/intracommunity-supplies/supplies-of-goods-to-businesses-in-the-european-union-eu.aspx | 2026-10-24 |
| Revenue, self-accounting on EU acquisitions | https://www.revenue.ie/en/vat/goods-and-services-to-and-from-abroad/acquisitions-from-other-eu-member-states/self-accounting-for-vat.aspx | 2026-10-24 |
| Revenue, calendar of key dates for tax professionals, 2026 (VAT3 and RTD on the 19th) | https://www.revenue.ie/en/tax-professionals/calendar/index.aspx | 2026-10-24 |
| Revenue, interest (published 13 October 2026) | https://www.revenue.ie/en/vat/interest-and-penalties/when-is-interest-applied-by-revenue/index.aspx | 2026-10-24 |
| Revenue, fixed penalties (published 20 April 2026) | https://www.revenue.ie/en/vat/interest-and-penalties/when-are-penalties-payable-to-revenue/fixed-penalties.aspx | 2026-10-24 |
| Tax and Duty Manual, VAT Return of Trading Details (updated February 2026) | https://www.revenue.ie/en/tax-professionals/tdm/value-added-tax/part09-obligations-accountable-persons/return/VAT-RTD-S76.pdf | 2026-10-24 |
| Tax and Duty Manual, VAT treatment of construction services (reviewed August 2026) | https://www.revenue.ie/en/tax-professionals/tdm/value-added-tax/part11-immovable-goods/construction-services/construction-servcies.pdf | 2026-10-24 |
| Tax and Duty Manual, partial recovery of VAT on qualifying passenger motor vehicles (reviewed December 2024) | https://www.revenue.ie/en/tax-professionals/tdm/value-added-tax/part03-taxable-transactions-goods-ica-services/Goods/partial-recovery-of-VAT-on-qualifying-passenger-motor-vehicles.pdf | 2026-10-24 |
| Tax and Duty Manual, postponed accounting | https://www.revenue.ie/en/tax-professionals/tdm/value-added-tax/part07-provisions-relating-to-imports-exports/postponed-accounting.pdf | 2026-10-24 |

Not yet confirmed: whether Revenue, in practice, charges interest only from the 23rd for a ROS filer who pays late (this skill follows s.76(1) and s.114(1) and counts from the 19th); the tax point for services received from abroad (the old version said the earliest of invoice, payment or the 15th of the month after the service; s.74 does not say this and the rule was not found in the law read); the legal basis for the ROS extension to the 23rd (read on Revenue's page only, not in the Taxes Consolidation Act); the monthly-return option for repayment traders (Revenue practice, no figure in s.77); the item-by-item lists of Schedules 2 and 3 beyond the paragraphs named above; the VIES statement threshold set by regulations for annual statements under s.82(4); any VAT changes in Finance Bill 2026 (Budget 2027), not enacted on 2026-10-24 and not read; the EU-goods and RTD treatment of One-Stop Shop sales beyond leaving them out of the RTD.

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
