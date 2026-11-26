---
name: uk-vat-return
description: "UK VAT for a business registered in Great Britain, with general coverage at 24 October 2026 and Flat Rate Scheme and interest updates checked on 22 November 2026. VAT has no tax year: each figure carries the date it applies from. Covers the 20%, 5% and 0% rates, exempt supplies, the temporary zero rate on domestic electricity (1 October 2026 to 31 March 2027), registration at GBP 90,000, deregistration at GBP 88,000, Making Tax Digital, the nine boxes, the deadline, blocked input tax (cars, business entertainment), mobile phones, bad debt relief, the Capital Goods Scheme (GBP 600,000 from 29 July 2026), the Flat Rate, cash and annual accounting schemes, reverse charges for overseas services and construction, penalty points, late payment penalties and interest. Trigger on: VAT return, VAT100, 9 boxes, VAT threshold, MTD for VAT, reverse charge, input tax, bad debt relief, VAT penalty. Out of scope: the short routine (vat-returns-for-small-businesses-in-the-uk), Xero closes (xero-uk-vat-close), EU goods sellers (gb-vat-eu-goods-sellers)."
version: 2.5
jurisdiction: GB
tax_year: 2026
last_updated: 2026-11-26
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: vat-gst
type: filing-howto
---

# UK VAT return: rates, registration, the nine boxes, penalties (24 October 2026; FRS and interest updated 22 November 2026)

VAT is not tied to the 6 April income tax year. Rates change when the law changes, and the registration limits are set by order and have been the same since 1 April 2024. Every figure below says the date it applies from. Return periods are set by HMRC for each business (usually quarterly).

This skill is the method and the figures. It links to the other UK VAT skills and does not repeat them:

- `vat-returns-for-small-businesses-in-the-uk`: the short quarterly routine for a small business.
- `xero-uk-vat-close`: closing a quarter from Xero.
- `gb-vat-eu-goods-sellers`: EU sellers shipping goods into Great Britain.

## Who this applies to

- A business that belongs in the UK and makes taxable supplies in Great Britain (England, Scotland, Wales): sole traders, partnerships and companies.
- **Must register** if, at the end of any month, taxable turnover for the last 12 months has gone over GBP 90,000, or if at any time there are reasonable grounds to expect taxable turnover in the next 30 days alone to go over GBP 90,000 ([VATA 1994 Sch 1 para 1](https://www.legislation.gov.uk/ukpga/1994/23/schedule/1/paragraph/1)). "Has exceeded" means exactly GBP 90,000 does not trigger registration.
- **12-month test:** register within 30 days of the end of the month you went over. You are registered from the first day of the second month after you went over. HMRC's example: over on 15 July, register by 30 August, registered from 1 September ([gov.uk: when you must register](https://www.gov.uk/register-for-vat)).
- **30-day test:** register by the end of that 30-day period. You are registered from the date you realised, not the date turnover went over.
- **Temporary excess:** HMRC can except the retrospective 12-month registration test if satisfied taxable supplies in the next 12 months will not exceed GBP 88,000 (Sch 1 para 1(3)). This does not excuse liability under the separate forward 30-day test.
- **Taxable turnover** includes zero-rated and reduced-rated sales. It leaves out exempt and outside-the-scope income. A UK business that is not registered must add the value of business services it buys from overseas suppliers under the general rule ([VAT Notice 741A, 5.7](https://www.gov.uk/guidance/vat-place-of-supply-of-services-notice-741a)).
- **Voluntary registration** is allowed below GBP 90,000.
- **Non-established taxable persons** (no UK business establishment) have no monetary threshold. Establish whether the actual supply creates a registration duty: supplies for which the UK recipient accounts under the reverse charge and other registration exclusions require separate treatment. Solely zero-rated supplies can support an exemption application; that is not a monetary threshold ([VAT Notice 700/1 supplement, 2.1](https://www.gov.uk/government/publications/vat-notice-7001-should-i-be-registered-for-vat/vat-notice-7001-supplement--2); [HMRC VATREG37200](https://www.gov.uk/hmrc-internal-manuals/vat-registration-manual/vatreg37200); [VATREG37250](https://www.gov.uk/hmrc-internal-manuals/vat-registration-manual/vatreg37250)). See `gb-vat-eu-goods-sellers`.
- **Deregistration:** you can ask to cancel if HMRC are satisfied taxable supplies in the next 12 months will not exceed GBP 88,000, unless the fall is because you will stop or suspend taxable supplies for 30 days or more ([Sch 1 para 4](https://www.legislation.gov.uk/ukpga/1994/23/schedule/1/paragraph/4); [gov.uk: cancel registration](https://www.gov.uk/register-for-vat/cancel-your-registration)).
- Northern Ireland goods trade with the EU (boxes 2, 8 and 9), VAT groups, margin and retail schemes, and land and property options are outside this skill.

## Rates, bands and thresholds

| Item | Rate or amount | From (in force on 24 Oct 2026) | Source URL |
|---|---|---|---|
| Standard rate (VATA 1994 s 2(1)) | 20% | 4 January 2011 | https://www.legislation.gov.uk/ukpga/1994/23/section/2 |
| Reduced rate, Schedule 7A supplies (s 29A), for example home energy other than GB domestic electricity, children's car seats | 5% | in force | https://www.legislation.gov.uk/ukpga/1994/23/section/29A |
| Zero rate (Schedule 8), for example most food, children's clothes, books, exports of goods | 0% | in force | https://www.gov.uk/vat-rates |
| Domestic electricity in England, Wales and Scotland (new Sch 8 Group 24; at least 60% qualifying use means the whole supply qualifies; up to 1,000 kWh a month is deemed domestic) | 0% | 1 October 2026 to 31 March 2027 (SI 2026/987) | https://www.legislation.gov.uk/uksi/2026/987/made |
| Qualifying children's meals eaten on the premises; qualifying child and family admissions to shows, exhibitions, theatres, concerts and cinemas; admissions to circuses, fairs, amusement and adventure parks, soft-play centres, zoos, observation and farm attractions, nature reserves and museums (temporary Sch 7A Groups 17 and 18) | 5%, only after checking the child-meal marketing, exempt-supply exclusions and admission-date/multi-date conditions; the activity label alone does not establish eligibility | 25 June 2026 to 1 September 2026 only; ended (SI 2026/576 arts 2 to 4) | https://www.legislation.gov.uk/uksi/2026/576/made |
| Registration threshold, 12-month and 30-day tests (Sch 1 para 1) | GBP 90,000 | 1 April 2024 (SI 2024/307); unchanged since | https://www.legislation.gov.uk/ukpga/1994/23/schedule/1/paragraph/1 |
| Deregistration and temporary-excess limit (Sch 1 paras 1(3) and 4) | GBP 88,000 | 1 April 2024 (SI 2024/307); unchanged since | https://www.legislation.gov.uk/ukpga/1994/23/schedule/1/paragraph/4 |
| Flat Rate Scheme: join | Expected VAT taxable turnover GBP 150,000 or less (excluding VAT) in the next 12 months, subject to the associated-business, re-entry and other eligibility exclusions; passing the turnover test alone is insufficient | in force | https://www.gov.uk/vat-flat-rate-scheme/who-can-join |
| Flat Rate Scheme: turnover exit tests | At the joining anniversary, total VAT-inclusive income in the year then ending exceeds GBP 230,000; or there are reasonable grounds to expect income in the next 30 days alone to exceed GBP 230,000. Exclude capital-asset disposals. At the annual check only, HMRC can allow retention if satisfied that coming-year income will not exceed GBP 191,500. Notice 733, section 11.2 requires an unexpected, non-recurring increase from genuine commercial activity and a written application to HMRC. This exception cannot override the 30-day test. Measure income using the business's chosen FRS turnover method (regulations 55M(4) and 55G(1)); the cash method tests receipts. Other exit conditions and effective dates are in section 12.2 | in force | https://www.legislation.gov.uk/uksi/1995/2518/regulation/55M ; https://www.gov.uk/guidance/flat-rate-scheme-for-small-businesses-vat-notice-733--2 |
| Flat Rate Scheme: limited cost business rate | 16.5% where VAT-inclusive spending on relevant goods in the return period is below the higher of 2% of VAT-inclusive flat-rate turnover and GBP 1,000 apportioned to the period (GBP 250 for a quarter). Relevant goods must be exclusively for the business and not fall within the exclusions in regulation 55A(4)(a); test each return period | in force | https://www.legislation.gov.uk/uksi/1995/2518/regulation/55A ; https://www.legislation.gov.uk/ukpga/1994/23/section/26B ; https://www.gov.uk/guidance/flat-rate-scheme-for-small-businesses-vat-notice-733--2 |
| Flat Rate Scheme: first-year discount | 1 percentage point off in the first year of VAT registration | in force | https://www.gov.uk/vat-flat-rate-scheme/how-much-you-pay |
| Cash accounting: join / must leave | GBP 1.35 million or less expected / over GBP 1.6 million, subject to eligibility and transaction exclusions in the scheme summary below | in force | https://www.gov.uk/vat-cash-accounting-scheme/eligibility |
| Annual accounting: join / must leave | GBP 1.35 million or less expected / over GBP 1.6 million, subject to eligibility and the short-period rules below | in force | https://www.gov.uk/vat-annual-accounting-scheme/eligibility |
| Partial exemption de minimis | Exempt input tax not more than GBP 625 a month on average and not more than half of all input tax | in force | https://www.gov.uk/guidance/partial-exemption-vat-notice-706 |
| Input tax on buying a car (VAT (Input Tax) Order 1992 art 7(1), (2), (2E) to (2G)) | Blocked subject to the qualifying-car and dealer/manufacturer stock exceptions; exclusive-business/no-private-availability, taxi, self-drive hire and driving-instruction cases require their particular conditions below | in force (unchanged on 24 Oct 2026) | https://www.legislation.gov.uk/uksi/1992/3222/article/7 |
| Input tax on leasing or hiring a car that does not meet those conditions (art 7(2H)) | One half of the tax blocked (art 7(2H) words it "one half of the tax") | in force | https://www.legislation.gov.uk/uksi/1992/3222/article/7 |
| Business entertainment (Input Tax Order art 5) | 100% blocked, except reasonable entertainment of overseas customers | in force | https://www.legislation.gov.uk/uksi/1992/3222/article/5 |
| Bad debt relief (VATA 1994 s 36; VAT Regs 1995 regs 165A and 172(1A)) | Debt written off at least 6 months after the later of supply and due date; claim within 4 years and 6 months | in force | https://www.legislation.gov.uk/ukpga/1994/23/section/36 |
| Customer's input tax on supplies unpaid 6 months after the later of supply and due date (VATA 1994 s 26A) | Repay to HMRC | in force | https://www.legislation.gov.uk/ukpga/1994/23/section/26A |
| Capital Goods Scheme: land, buildings, civil engineering works (VAT Regs 1995 regs 113(4)(a), 114(3)(a)) | VAT-bearing capital expenditure of GBP 600,000 or more; adjusted over 10 intervals | 29 July 2026 (SI 2026/765); GBP 250,000 where any relevant expenditure on the item was incurred before 29 July 2026 | https://www.legislation.gov.uk/uksi/1995/2518/regulation/113 ; https://www.legislation.gov.uk/uksi/2026/765/made |
| Capital Goods Scheme: aircraft, ships, boats and other vessels (regs 113(4)(b), 114(3)(b)) | GBP 50,000 or more; adjusted over 5 intervals | in force | https://www.legislation.gov.uk/uksi/1995/2518/regulation/113 |
| Capital Goods Scheme: computers (previously GBP 50,000 or more, 5 intervals) | Removed from the scheme | 29 July 2026 (SI 2026/765 reg 2(2)(a)); items with any relevant expenditure before that date stay in | https://www.legislation.gov.uk/uksi/2026/765/made ; https://www.legislation.gov.uk/uksi/1995/2518/regulation/113 |
| Late submission penalty (FA 2021 Sch 24) | GBP 200 at the points threshold: annual 2, quarterly 4, monthly 5 points | periods starting on or after 1 January 2023 | https://www.gov.uk/guidance/penalty-points-and-penalties-if-you-submit-your-vat-return-late |
| Late payment penalties (FA 2021 Sch 26 paras 5 and 8) | 3% of VAT unpaid at day 15, plus 3% of VAT unpaid at day 30, plus 10% a year from day 31 | VAT periods starting on or after 1 April 2025 (SI 2025/589); earlier periods 2%, 2%, 4% | https://www.legislation.gov.uk/ukpga/2021/26/schedule/26 |
| Late payment interest | Bank of England base rate plus 4%: 7.75% through 23 November 2026; 8.00% from 24 November 2026 | plus 4% since 6 April 2025; 7.75% from 9 January 2026; announced successor 8.00% from 24 November 2026 | https://www.gov.uk/government/publications/rates-and-allowances-hmrc-interest-rates-for-late-and-early-payments/rates-and-allowances-hmrc-interest-rates |
| Error correction on the current return (method 1) | Net errors up to GBP 10,000, or up to GBP 50,000 if not more than 1% of box 6 | in force | https://www.gov.uk/guidance/how-to-correct-vat-errors-and-make-adjustments-or-claims-vat-notice-70045 |

For the Flat Rate Scheme turnover tests, the statute controls; Notice 733 agrees. The short GOV.UK "if your circumstances change" page also mentions expected income in the next 12 months, but regulation 55M does not create that additional exit test.

Exempt supplies carry no VAT and give no right to reclaim VAT on related costs. Examples: postage stamps, financial and insurance services, most residential lettings ([gov.uk VAT rates](https://www.gov.uk/vat-rates)). Outside the scope: wages, money you put in, loans, dividends, and qualifying B2B general-rule services sold to customers who belong outside the UK. Establish customer status and the applicable place-of-supply rule before treating a service as outside the scope; the customer's overseas address alone is insufficient ([VAT Notice 741A](https://www.gov.uk/guidance/vat-place-of-supply-of-services-notice-741a)).

## The taxable base

**Output VAT (box 1).** VAT on every taxable supply in the period at its rate. Also: postponed import VAT, reverse charge VAT, fuel scale charges, goods taken for private use, gifts of goods costing more than GBP 50 excluding VAT, sales of business assets. Deduct VAT on credit notes you issue ([VAT Notice 700/12, 3.2](https://www.gov.uk/guidance/how-to-fill-in-and-submit-your-vat-return-vat-notice-70012)).

**Input VAT (box 4).** VAT on purchases used for taxable business supplies, backed by a proper VAT invoice (or import VAT certificate). Also: reverse charge VAT, postponed import VAT, bad debt relief. Never: VAT on goods wholly for personal use, business entertainment, margin scheme purchases. A partly exempt business recovers only under the partial exemption rules ([VAT Notice 700/12, 3.5](https://www.gov.uk/guidance/how-to-fill-in-and-submit-your-vat-return-vat-notice-70012)).

**Blocked and restricted input tax.**

| Item | Treatment |
|---|---|
| Goods and services not used for the business | Not input tax. Apportion mixed-use costs on a fair and reasonable basis |
| Buying a car | Apply the block and exceptions in [Input Tax Order art 7](https://www.legislation.gov.uk/uksi/1992/3222/article/7), including dealer/manufacturer stock and the qualifying-car condition for the relevant business-use exceptions. Those include intended exclusive business use, or primarily taxi, self-drive hire or driving instruction (art 7(2E), (2F)). "Exclusively" fails if the car is available to anyone, including the owner or a partner, for private use (art 7(2G)). Establish the actual vehicle and exception before reclaiming. A payload of one tonne or more is outside the art 2 motor-car definition; the 12-or-more-seat exclusion additionally requires the applicable Schedule 6 construction/use conditions, not seat count alone ([art 2](https://www.legislation.gov.uk/uksi/1992/3222/article/2)) |
| Leasing or hiring a car | Where the purchase block would apply, 50% of the VAT on the hire charge is blocked (art 7(2H)). If the car qualifies (exclusive business use, or primarily taxi, self-drive hire or instruction), all of it is input tax. HMRC accept the 50% block does not apply to a car hired for no more than 10 days specifically for business use where you do not have a company car; it does apply from day 1 to a car replacing an off-road company car ([VAT Notice 700/64, 4.4](https://www.gov.uk/guidance/vat-on-motoring-expenses-notice-70064)) |
| Road fuel with private use | Four options: claim all and apply the fuel scale charge, keep detailed mileage records and claim the business share, claim all only where there is no private use, or claim nothing (VAT Notice 700/64, 9.1) |
| Business entertainment | Blocked ([Input Tax Order art 5](https://www.legislation.gov.uk/uksi/1992/3222/article/5)), except entertainment of an overseas customer that is reasonable in scale and character. Even then a private benefit to the guest brings an output tax charge that cancels the recovery ([VAT Notice 700/65, 2.6](https://www.gov.uk/guidance/business-entertainment-and-vat-notice-70065)). Staff entertainment (parties, outings) is input tax and not blocked. Entertaining only directors or partners is not input tax at all (Notice 700/65, 3.2) |
| Mobile phones provided to employees | VAT on buying or leasing a phone for business use and on line rental is input tax even if private use is allowed. For calls/packages, HMRC accepts an enforced private-use ban and also insignificant private use; business add-ons need a business purpose. Otherwise apportion free private use, or charge the employee and account for output tax on that charge. A contract taken out by the employee gives the business no input tax ([VAT Notice 700, 12.3](https://www.gov.uk/guidance/vat-guide-notice-700)) |
| Costs of exempt supplies | Not recoverable, subject to the partial exemption de minimis test |

**Bad debt relief** ([VATA 1994 s 36](https://www.legislation.gov.uk/ukpga/1994/23/section/36); [VAT Regulations 1995 Part XIX](https://www.legislation.gov.uk/uksi/1995/2518/part/XIX); [VAT Notice 700/18](https://www.gov.uk/guidance/relief-from-vat-on-bad-debts-notice-70018)). A supplier can reclaim the output VAT on an unpaid debt if:

- it accounted for and paid the VAT on the supply (s 36(1)(a));
- the debt is written off in its accounts and entered in a separate refunds-for-bad-debts account, no earlier than 6 months after the payment fell due (reg 172(1A)), and at least 6 months have passed since the date of supply (s 36(1)(c));
- the price was not more than the open market value (s 36(4)(a));
- the debt is not still assigned to a factor. An absolute assignment prevents relief; where reassignment is permitted, relief becomes available only once the debt has actually been reassigned and the other conditions are met (Notice 700/18, 3.12).

Claim the VAT in box 4 of the return for the period in which the conditions are first met, or a later one (reg 166), within 4 years and 6 months of the later of the due date and the date of supply (reg 165A). If the customer later pays, put the VAT element of the payment in box 1 for that period (Notice 700/18, 3.14). The customer's side: input tax claimed on a supply still unpaid 6 months after the later of the supply date and the due date must be repaid to HMRC ([VATA 1994 s 26A](https://www.legislation.gov.uk/ukpga/1994/23/section/26A)), subject to the insolvency rule in s 26AA.

**Capital Goods Scheme, summary** ([VAT Regulations 1995 Part XV](https://www.legislation.gov.uk/uksi/1995/2518/part/XV); [VAT Notice 706/2](https://www.gov.uk/guidance/capital-goods-scheme-notice-7062)). The VAT recovered on a capital item is adjusted over its period of adjustment if taxable use changes. Capital items: land, buildings and civil engineering works with VAT-bearing capital expenditure of GBP 600,000 or more (10 intervals), and aircraft and ships, boats or other vessels of GBP 50,000 or more (5 intervals) (regs 113 and 114). From 29 July 2026 computers are no longer capital items and the land and buildings limit rose from GBP 250,000 to GBP 600,000. Neither change applies to an item if the owner incurred any relevant expenditure on it before 29 July 2026, so those items stay in the scheme under the old rules ([SI 2026/765 regs 1(3) and 2](https://www.legislation.gov.uk/uksi/2026/765/made)). The adjustments interact with partial exemption: refer anyone with a capital item and changing exempt use.

**The nine boxes** ([VAT Notice 700/12, section 3](https://www.gov.uk/guidance/how-to-fill-in-and-submit-your-vat-return-vat-notice-70012)):

| Box | What goes in it |
|---|---|
| 1 | Output VAT due in the period, as above |
| 2 | VAT on goods acquired into Northern Ireland from the EU. For a Great Britain business: 0.00 |
| 3 | Box 1 plus box 2 |
| 4 | Input VAT reclaimed in the period |
| 5 | Box 3 minus box 4. Positive: you pay. Negative: HMRC repay. No minus sign |
| 6 | All sales and other outputs excluding VAT: standard, reduced, zero-rated and exempt sales, exports, outside-the-scope services, reverse charge values where required. Not money put in, loans, dividends or insurance claims |
| 7 | All purchases excluding VAT, including imports and reverse charge values. Not wages, PAYE and NIC, drawings, loans, dividends, MOT, vehicle licence duty or business rates |
| 8 | Goods supplied from Northern Ireland to the EU only (also in box 6) |
| 9 | Goods acquired into Northern Ireland from the EU only (also in box 7) |

**Reverse charges** ([VAT Notice 700/12, 4.6](https://www.gov.uk/guidance/how-to-fill-in-and-submit-your-vat-return-vat-notice-70012)):

| Reverse charge | Supplier enters | Customer enters |
|---|---|---|
| Taxable general-rule B2B services bought from a supplier who belongs outside the UK, after establishing UK place of supply and any use-and-enjoyment adjustment; exempt services do not trigger this charge | Box 6 | Box 1 (output VAT), box 4 (legally deductible input VAT), box 6 and box 7 (value) |
| Construction services reported within CIS, between VAT and CIS registered businesses | Box 6 only; invoice says the customer accounts for the VAT | Box 1, box 4 and box 7; nothing in box 6 |

The construction reverse charge covers standard and reduced-rate construction operations within CIS. It does not apply when the customer is an end user or intermediary supplier and tells the supplier in writing, to zero-rated work, or to stand-alone services such as architects, surveyors, delivering materials or installing security systems. A reverse charge element of 5% or less of a single supply can be disregarded only if both parties agree it from the start on overall contract values ([gov.uk: when to use the construction reverse charge](https://www.gov.uk/guidance/vat-domestic-reverse-charge-for-building-and-construction-services); [technical guide](https://www.gov.uk/guidance/vat-reverse-charge-technical-guide)). Services you sell to business customers abroad under the general rule are outside the scope: box 6 only.

**Schemes, in summary.**

- **Flat Rate Scheme:** pay a fixed percentage of VAT-inclusive turnover (including zero-rated and exempt income). Charge normal VAT on invoices. Ordinary input tax is restricted, but this is not a blanket bar: qualifying capital goods in a single purchase costing GBP 2,000 or more including VAT, eligible pre-registration input tax and overseas reverse-charge purchases have their own conditions. Do not extend the capital-goods exception to services or other excluded purchases; establish the actual purchase under [Notice 733, sections 7, 15 and 16](https://www.gov.uk/guidance/flat-rate-scheme-for-small-businesses-vat-notice-733--2). Box 6 holds the flat rate turnover including VAT. Sector rates include 14.5% for accountancy and for IT consultancy and 12% for activities not listed elsewhere; the limited cost rate is 16.5% ([gov.uk: how much you pay](https://www.gov.uk/vat-flat-rate-scheme/how-much-you-pay)). Test the limited cost rule on every return.
- **Cash accounting:** account for output VAT when the customer pays and reclaim eligible input VAT when you pay. Turnover alone does not establish eligibility: returns/payments must be up to date and a VAT offence in the last 12 months excludes entry. Cannot be used with the Flat Rate Scheme or for reverse charge supplies. Transaction exclusions also include invoice terms of 6 months or more, advance invoices, lease/hire purchase, conditional/credit sales, the specified Northern Ireland acquisitions and goods moving outside a customs warehouse ([eligibility](https://www.gov.uk/vat-cash-accounting-scheme/eligibility)).
- **Annual accounting:** ordinarily one return a year. For an accounting period of 4 to 12 months, the return is due 2 months after its end; for a period under 4 months, it is due 1 month after its end. Advance payments are normally 10% of the estimated bill monthly or 25% quarterly for 4-to-12-month periods; no advance payments for a period under 4 months ([deadlines](https://www.gov.uk/vat-annual-accounting-scheme/return-and-payment-deadlines)). Eligibility excludes a departure from the scheme in the preceding 12 months, VAT-registered groups/divisions, overdue returns/payments and insolvency ([eligibility](https://www.gov.uk/vat-annual-accounting-scheme/eligibility)).

**Partial exemption, pointer only.** A business making taxable and exempt supplies cannot recover input VAT used for exempt supplies, or the exempt share of overheads, unless it passes the de minimis test in the rates table. Apply the standard method or an approved special method, with an annual adjustment ([VAT Notice 706](https://www.gov.uk/guidance/partial-exemption-vat-notice-706)). Refer anyone who fails de minimis.

## Deadlines and filing

- **Return periods:** usually quarterly, on dates in your registration certificate. Monthly on request; annual under annual accounting.
- **Return and payment:** online, one calendar month and 7 days after the period ends. The payment must reach HMRC's account by then, even if the deadline is a weekend or bank holiday ([gov.uk: VAT return deadlines](https://www.gov.uk/vat-returns/deadlines)). The regulation sets the last day of the following month ([VAT Regulations 1995 reg 25](https://www.legislation.gov.uk/uksi/1995/2518/regulation/25)); HMRC's online deadline adds the 7 days.
- **A return is due even if nothing is payable** (nil or repayment returns).
- **Annual accounting:** return 2 months after a period of 4 to 12 months, or 1 month after a period under 4 months.
- **Making Tax Digital:** VAT-registered businesses generally keep digital records and file through compatible software. Links between programs must be digital; copy and paste is not a digital link. Exemptions include digital impracticality (for example age, disability, location, religious objection), insolvency and the final return after deregistration. Follow HMRC's instructions while an exemption application is pending; do not assume that a pending request itself grants permanent exemption ([VAT Notice 700/22](https://www.gov.uk/government/publications/vat-notice-70022-making-tax-digital-for-vat/vat-notice-70022-making-tax-digital-for-vat)).
- **Corrections:** a return cannot be amended once sent. Net errors within the method 1 limit go on the current return; larger or deliberate errors are notified to HMRC separately (method 2). The ordinary time limit is 4 years, with the specific adjacent-period tax-point exception and deliberate-error rule in Notice 700/45 section 4.7; see step 8 below ([VAT Notice 700/45](https://www.gov.uk/guidance/how-to-correct-vat-errors-and-make-adjustments-or-claims-vat-notice-70045)).

### How to file and pay a VAT return, step by step

**What you need first:** your 9-digit VAT registration number, access to your VAT online account, software compatible with Making Tax Digital, digital records for the period, VAT invoices for every reclaim, and the period dates and due date.

1. **Find the due date.** Sign in to the VAT online account, which shows when returns are due and when payment must clear ([GOV.UK: when to do a VAT Return](https://www.gov.uk/vat-returns), read 2026-10-31).
2. **Fill in boxes 1 to 9 in the software.** Use the box rules under "The taxable base". Enter 0.00 in any box that does not apply; every box is completed, and a return is due even with nothing to pay or reclaim ([VAT Notice 700/12, 3.1 and 7.2](https://www.gov.uk/guidance/how-to-fill-in-and-submit-your-vat-return-vat-notice-70012), read 2026-10-31).
3. **Deal with past errors before submitting.** Net errors within the method 1 limit go on this return. Otherwise see step 8 ([VAT Notice 700/45](https://www.gov.uk/guidance/how-to-correct-vat-errors-and-make-adjustments-or-claims-vat-notice-70045), read 2026-10-31).
4. **Submit from the software.** The online account form is only for a business that does not have to use software. A paper return applies only to a business approved to send one, and it must reach HMRC by the due date ([GOV.UK: how to send your VAT Return](https://www.gov.uk/vat-returns/how-to-send-your-vat-return), read 2026-10-31; [VAT Notice 700/12, 1.2 and 5](https://www.gov.uk/guidance/how-to-fill-in-and-submit-your-vat-return-vat-notice-70012), read 2026-10-31).
5. **Check it arrived.** The VAT online account shows that HMRC has received the return ([GOV.UK: when to do a VAT Return](https://www.gov.uk/vat-returns), read 2026-10-31).
6. **Pay so the money clears by the deadline: 1 calendar month and 7 days after the period ends.** There are three common routes ([GOV.UK: pay your VAT bill](https://www.gov.uk/pay-vat/print), read 2026-10-31):
   - Direct Debit: first establish eligibility. This route is unavailable for an overseas account, an insolvency practitioner, payments on account, paper returns or a bill over GBP 20 million. If eligible, set it up in the VAT online account at least 3 working days before submitting. HMRC collects 3 working days after the deadline. If it is set up later, the first payment goes another way.
   - Bank transfer: sort code 08 32 00, account 11963155, name HMRC VAT, reference the 9-digit VAT number with no spaces. Faster Payments usually arrive the same or next day, including weekends and bank holidays. CHAPS usually arrives the same working day. Bacs usually takes 3 working days.
   - Overseas bank account: CHAPS to IBAN GB36 BARC 2005 1773 1523 91, BIC BARCGB22.
7. **If box 5 is a repayment,** HMRC credits the account and repays the balance, subject to any enquiries ([VAT Notice 700/12, 3.6](https://www.gov.uk/guidance/how-to-fill-in-and-submit-your-vat-return-vat-notice-70012), read 2026-10-31). Money goes to the bank account in the VAT registration details; with no account there, HMRC sends a cheque. Direct Debit details are not used for repayments ([GOV.UK: pay your VAT bill](https://www.gov.uk/pay-vat/print), read 2026-10-31).
8. **To correct a sent return,** you cannot amend it. Method 1: net errors up to GBP 10,000, or up to GBP 50,000 if within 1% of box 6 for the return in which you find them, go on the current return. Method 2: anything above that, any deliberate error, or any error by choice is reported on the [HMRC online form](https://www.tax.service.gov.uk/submissions/new-form/notification-errors-vat-returns), or in writing with the VAT number to VAT Error Correction Team, BT VAT, HMRC, BX9 1WR. The ordinary limit is 4 years from the end of the period for output tax and over-claimed input tax, and from the return's due date for under-claimed input tax. Section 4.7 also excepts a tax-point error where VAT was declared on the immediately preceding or following return, provided the later return is within the 4-year limit. The 4-year limit does not apply to deliberate errors ([VAT Notice 700/45](https://www.gov.uk/guidance/how-to-correct-vat-errors-and-make-adjustments-or-claims-vat-notice-70045), original read 2026-10-31; section 4.7 checked 2026-11-26).
9. **If you cannot pay,** file on time anyway, because a late return and a late payment are separate failures. Contact HMRC to ask for a payment plan; HMRC checks that it is affordable, and if none is agreed it asks for the full amount ([GOV.UK: if you cannot pay your tax bill](https://www.gov.uk/difficulties-paying-hmrc), read 2026-10-31).

**Stop and get a professional when:** an error was deliberate; net errors are over GBP 50,000; the business has exempt income and partial exemption applies; or HMRC has opened an enquiry into the period.

## Penalties and interest

**Late submission (points).** A covered late return earns one point until the threshold: annual returns 2, quarterly 4, monthly 5. The first return after new registration, final return after deregistration and one-off returns covering a period other than a month, quarter or year are excluded. At the threshold you pay GBP 200, and GBP 200 again for each further covered late return while at the threshold. Applies to periods starting on or after 1 January 2023, including covered nil and repayment returns ([gov.uk: penalty points](https://www.gov.uk/guidance/penalty-points-and-penalties-if-you-submit-your-vat-return-late); [FA 2021 Sch 24](https://www.legislation.gov.uk/ukpga/2021/26/schedule/24)).

**Late payment penalties** ([gov.uk](https://www.gov.uk/guidance/how-late-payment-penalties-work-if-you-pay-vat-late); [FA 2021 Sch 26](https://www.legislation.gov.uk/ukpga/2021/26/schedule/26)):

| Days overdue | Penalty (VAT periods starting on or after 1 April 2025) |
|---|---|
| 1 to 15 | None |
| 16 to 30 | First penalty: 3% of the VAT unpaid at day 15 |
| 31 or more | First penalty: 3% at day 15 plus 3% of the VAT still unpaid at day 30. Second penalty: 10% a year, daily, on the unpaid balance from day 31 until paid |

- They do not apply to payments on account or annual accounting instalments.
- A Time to Pay proposal made by day 15 (or by day 30) can prevent the corresponding next penalty stage only if HMRC ultimately agrees the arrangement and it is kept. A request alone or rejected proposal does not establish relief. If a breached arrangement is cancelled, both penalties can be charged as if it never existed. Interest continues while VAT is outstanding.
- For VAT periods that began before 1 April 2025 the percentages were 2%, 2% and 4% a year ([SI 2025/589 reg 1(3)](https://www.legislation.gov.uk/uksi/2025/589/made)).

**Late payment interest** runs from the first day the payment is overdue until it is paid in full, at Bank of England base rate plus 4% ([gov.uk: late payment interest](https://www.gov.uk/guidance/late-payment-interest-if-you-do-not-pay-vat-or-penalties-on-time)). HMRC's table, read on 22 November 2026, gives 7.75% from 9 January through 23 November 2026 and 8.00% from 24 November 2026. Bank Rate rose from 3.75% to 4% on 5 November 2026; the next decision is due on 17 December 2026. Use HMRC's effective dates when splitting interest, and recheck its table after each base rate decision.

**Errors.** Careless or deliberate inaccuracies can be penalised; telling HMRC before they find out reduces the penalty (VAT Notice 700/45).

## Cross-border points

- **Services bought from abroad:** first establish a taxable UK supply under the applicable place-of-supply rule, including any use-and-enjoyment adjustment; an exempt service does not reverse charge. Then use the box routing above (Notice 741A sections 5.5–5.6). The supplier may be EU or non-EU.
- **Services sold abroad:** B2B general rule services to customers who belong outside the UK are outside the scope of UK VAT. Keep evidence that the customer is in business abroad. B2C services generally carry UK VAT, with exceptions in Notice 741A.
- **Exports of goods:** zero-rated with evidence of export ([VAT Notice 700/12, 3.2](https://www.gov.uk/guidance/how-to-fill-in-and-submit-your-vat-return-vat-notice-70012)).
- **Imports:** postponed VAT accounting puts import VAT in box 1 and box 4 of the same return.
- **Overseas sellers:** a non-established business has no threshold. See `gb-vat-eu-goods-sellers`.
- **Northern Ireland:** goods trade with the EU uses boxes 2, 8 and 9 and is out of scope here.

## Worked examples

**Example 1: a standard quarterly return.** A design studio in Leeds files quarterly. For the quarter to 30 September 2026 it has standard-rated sales of GBP 60,000 net, zero-rated sales (exported printed books) of GBP 5,000, standard-rated UK purchases of GBP 20,000 net with VAT invoices, and a GBP 1,000 software subscription from a US supplier with no VAT. The US service is reverse charged: GBP 200 goes in box 1 and box 4, and GBP 1,000 in box 6 and box 7. Box 1 is GBP 12,000 plus GBP 200. Box 4 is GBP 4,000 plus GBP 200. Box 5 is GBP 8,000 to pay by 7 November 2026.

```oa-check
name: Quarterly return to 30 Sep 2026 with an overseas software reverse charge
inputs:
  std_sales: 60000
  zero_sales: 5000
  std_purchases: 20000
  overseas_service: 1000
  rate: 20
steps:
  - rc_vat: overseas_service * rate / 100
  - box1: std_sales * rate / 100 + rc_vat
  - box2: 0
  - box3: box1 + box2
  - box4: std_purchases * rate / 100 + rc_vat
  - box5: box3 - box4
  - box6: std_sales + zero_sales + overseas_service
  - box7: std_purchases + overseas_service
expected:
  rc_vat: 200
  box1: 12200
  box3: 12200
  box4: 4200
  box5: 8000
  box6: 66000
  box7: 21000
```

**Example 2: paying 51 days late.** A company files its return for the quarter to 30 September 2026 on time, showing GBP 15,000 to pay by 7 November 2026. It pays nothing until 28 December 2026, day 51, and never asked for Time to Pay. The period started on or after 1 April 2025, so the 3%, 3% and 10% percentages apply. First penalty: 3% of GBP 15,000 at day 15 plus 3% at day 30, GBP 900. Second penalty: 10% a year for 21 days (day 31 to day 51), GBP 86.30. Interest at 7.75% for 51 days: GBP 162.43. This is a constant-rate arithmetic illustration, not the bill using HMRC's announced rates. Total cost on that hypothetical assumption is GBP 1,148.73 on top of the VAT. Using the rates announced by 22 November, and assuming no further changes before payment, interest would instead be 16 days at 7.75% plus 35 days at 8.00%: GBP 166.03, making the total GBP 1,152.33. Recompute if HMRC's rate changes again before payment. A Time to Pay proposal by day 15 would have prevented both penalties only if HMRC ultimately agreed it and the arrangement was kept; a request alone would not establish relief.

```oa-check
name: GBP 15,000 VAT paid 51 days late, interest at 7.75%
inputs:
  vat: 15000
  days_late: 51
  pen_rate_1: 3
  pen_rate_2: 10
  interest_rate: 7.75
steps:
  - first_penalty: vat * pen_rate_1 / 100 + vat * pen_rate_1 / 100
  - second_days: days_late - 30
  - second_penalty: round(vat * pen_rate_2 / 100 * second_days / 365, 2)
  - interest: round(vat * interest_rate / 100 * days_late / 365, 2)
  - total: first_penalty + second_penalty + interest
expected:
  first_penalty: 900
  second_days: 21
  second_penalty: 86.30
  interest: 162.43
  total: 1148.73
```

**Example 3: which should I use, the Flat Rate Scheme or standard VAT accounting?** An IT consultancy past its first year of registration sells GBP 100,000 net to UK businesses at 20% and expects to stay there, so it passes the turnover test (limit GBP 150,000 excluding VAT). Joining also requires the other eligibility conditions above. VAT-inclusive turnover is GBP 120,000. The flat rate is charged on that inclusive figure ([GOV.UK: Flat Rate Scheme](https://www.gov.uk/vat-flat-rate-scheme/print), read 2026-10-31).

For this comparison, the goods figures are VAT-inclusive spending on relevant goods, and spending and turnover are assumed to arise in the same proportions in each return period. Test the actual figures for each return separately; annual spending alone does not establish the rate for a quarterly return ([VAT Regulations 1995 reg 55A(4)](https://www.legislation.gov.uk/uksi/1995/2518/regulation/55A), read 2026-11-22).

- Worked one way, standard accounting: pay output VAT of GBP 20,000 less input VAT.
- Worked the other way, with goods of GBP 3,000 a year: this is above 2% of turnover and above GBP 1,000, so the sector rate of 14.5% applies and the payment is GBP 17,400.
- The deciding figure: standard accounting wins once reclaimable input VAT passes GBP 20,000 - 17,400 = GBP 2,600. With input VAT of GBP 3,500 it pays GBP 16,500, which is GBP 900 less. With input VAT of GBP 1,500 the flat rate is GBP 1,100 cheaper.
- If goods are only GBP 1,500, the business is a limited cost business at 16.5%, pays GBP 19,800, and the break-even falls to GBP 200. Standard accounting then wins for almost any business with costs.
- The test goes with the goods spend first, then the input VAT. To join, apply to HMRC online or by post; confirmation comes through the VAT online account or by post.

```oa-check
name: Flat Rate Scheme against standard accounting, IT consultancy
inputs:
  net_sales: 100000
  input_vat: 3500
  sector_rate: 0.145
  limited_rate: 0.165
steps:
  - output_vat: net_sales * 0.20
  - gross: net_sales + output_vat
  - flat_sector: gross * sector_rate
  - flat_limited: gross * limited_rate
  - standard: output_vat - input_vat
  - breakeven_sector: output_vat - flat_sector
  - breakeven_limited: output_vat - flat_limited
  - standard_saves: flat_sector - standard
expected:
  flat_sector: 17400
  flat_limited: 19800
  standard: 16500
  breakeven_sector: 2600
  breakeven_limited: 200
  standard_saves: 900
```

## Ask the client first

1. Are you VAT registered? From what date, on which return periods, and under which schemes (Flat Rate, cash, annual)? If not: your taxable turnover month by month for the last 12 months, and any single 30 days ahead that could go over GBP 90,000.
2. What do you sell, to whom (UK or abroad, business or consumer), and at which rates? Any exempt income (rents, insurance, financial services)? If yes, partial exemption applies.
3. Do you buy services from suppliers outside the UK, or construction services within CIS?
4. Do you hold VAT invoices for everything you reclaim? Any cars, fuel, entertaining, mobile phones or mixed-use costs? Any customer debts unpaid 6 months after they fell due? Any land or building spend of GBP 600,000 or more (or GBP 250,000 or more begun before 29 July 2026)?
5. Which MTD software do you use, and are all links digital?
6. Any late returns, penalty points, unpaid VAT, Time to Pay arrangement or errors in earlier returns?

## Sources

| Source | URL | Read on |
|---|---|---|
| VATA 1994 s 2 (standard rate 20%) | https://www.legislation.gov.uk/ukpga/1994/23/section/2 | 2026-10-24 |
| VATA 1994 s 29A (reduced rate 5%) | https://www.legislation.gov.uk/ukpga/1994/23/section/29A | 2026-10-24 |
| VATA 1994 Sch 1 para 1 (registration GBP 90,000, temporary excess GBP 88,000; SI 2024/307 from 1.4.2024; no outstanding effects) | https://www.legislation.gov.uk/ukpga/1994/23/schedule/1/paragraph/1 | 2026-10-24 |
| VATA 1994 Sch 1 para 4 (deregistration GBP 88,000) | https://www.legislation.gov.uk/ukpga/1994/23/schedule/1/paragraph/4 | 2026-10-24 |
| VAT (Supplies of Domestic Electricity) Order 2026, SI 2026/987 | https://www.legislation.gov.uk/uksi/2026/987/made | 2026-10-24 |
| VAT (Reduced Rate) (Hospitality and Tourism) Order 2026, SI 2026/576 | https://www.legislation.gov.uk/uksi/2026/576/made | 2026-10-24 |
| VAT Regulations 1995 reg 25 (returns) | https://www.legislation.gov.uk/uksi/1995/2518/regulation/25 | 2026-10-24 |
| Finance Act 2021 Sch 24 (late submission penalties) | https://www.legislation.gov.uk/ukpga/2021/26/schedule/24 | 2026-10-24 |
| Finance Act 2021 Sch 26 paras 5 and 8 (late payment penalties 3%, 3%, 10%) | https://www.legislation.gov.uk/ukpga/2021/26/schedule/26 | 2026-10-24 |
| SI 2025/589 (increase in Sch 26 percentages; application) | https://www.legislation.gov.uk/uksi/2025/589/made | 2026-10-24 |
| HMRC, VAT rates | https://www.gov.uk/vat-rates | 2026-10-24 |
| HMRC, Register for VAT and when you must register | https://www.gov.uk/register-for-vat | 2026-10-24 |
| HMRC, Cancel your VAT registration | https://www.gov.uk/register-for-vat/cancel-your-registration | 2026-10-24 |
| HMRC, VAT Notice 700/1 supplement (thresholds) | https://www.gov.uk/government/publications/vat-notice-7001-should-i-be-registered-for-vat/vat-notice-7001-supplement--2 | 2026-10-24 |
| HMRC, VAT Notice 700/12 (filling in the return) | https://www.gov.uk/guidance/how-to-fill-in-and-submit-your-vat-return-vat-notice-70012 | 2026-10-24 |
| HMRC, VAT Notice 700/22 (Making Tax Digital) | https://www.gov.uk/government/publications/vat-notice-70022-making-tax-digital-for-vat/vat-notice-70022-making-tax-digital-for-vat | 2026-10-24 |
| HMRC, VAT Return deadlines | https://www.gov.uk/vat-returns/deadlines | 2026-10-24 |
| HMRC, Penalty points for late VAT returns | https://www.gov.uk/guidance/penalty-points-and-penalties-if-you-submit-your-vat-return-late | 2026-10-24 |
| HMRC, How late payment penalties work | https://www.gov.uk/guidance/how-late-payment-penalties-work-if-you-pay-vat-late | 2026-10-24 |
| HMRC, Late payment interest on VAT | https://www.gov.uk/guidance/late-payment-interest-if-you-do-not-pay-vat-or-penalties-on-time | 2026-10-24 |
| HMRC, interest rates for late and early payments | https://www.gov.uk/government/publications/rates-and-allowances-hmrc-interest-rates-for-late-and-early-payments/rates-and-allowances-hmrc-interest-rates | 2026-10-24 |
| Bank of England, Bank Rate (3.75%, held 17 September 2026) | https://www.bankofengland.co.uk/monetary-policy/the-interest-rate-bank-rate | 2026-10-24 |
| HMRC, Flat Rate Scheme: who can join, how much you pay, if circumstances change | https://www.gov.uk/vat-flat-rate-scheme/how-much-you-pay | 2026-10-24 |
| VAT Regulations 1995 reg 55M(1) to (4), turnover exit tests, retention and capital-asset exclusion; operative text read | https://www.legislation.gov.uk/uksi/1995/2518/regulation/55M | 2026-11-22 |
| VAT Regulations 1995 reg 55A(4), limited-cost definition, relevant-goods exclusions and proportional annual floor; operative text read | https://www.legislation.gov.uk/uksi/1995/2518/regulation/55A | 2026-11-22 |
| VATA 1994 s 26B(2)(c), relevant turnover includes VAT on taxable supplies and exempt supplies; operative text read | https://www.legislation.gov.uk/ukpga/1994/23/section/26B | 2026-11-22 |
| VAT Regulations 1995 reg 55G(1), basic, cash and retailer turnover methods; operative text read | https://www.legislation.gov.uk/uksi/1995/2518/regulation/55G | 2026-11-22 |
| HMRC interest table, updated 6 November 2026: VAT is included in the main tax table, with 7.75% from 9 January and 8.00% from 24 November; entries read | https://www.gov.uk/government/publications/rates-and-allowances-hmrc-interest-rates-for-late-and-early-payments/rates-and-allowances-hmrc-interest-rates | 2026-11-22 |
| Bank of England: 5 November decision, Bank Rate 4% and next decision 17 December 2026; relevant passages read | https://www.bankofengland.co.uk/monetary-policy/the-interest-rate-bank-rate | 2026-11-22 |
| HMRC, VAT Notice 733, sections 4.4 to 4.6 and 11.2 to 12.3; threshold conditions and exit dates read | https://www.gov.uk/guidance/flat-rate-scheme-for-small-businesses-vat-notice-733--2 | 2026-11-22 |
| HMRC, Cash Accounting Scheme eligibility | https://www.gov.uk/vat-cash-accounting-scheme/eligibility | 2026-10-24 |
| HMRC, Annual Accounting Scheme eligibility and deadlines | https://www.gov.uk/vat-annual-accounting-scheme/return-and-payment-deadlines | 2026-10-24 |
| HMRC, Construction domestic reverse charge | https://www.gov.uk/guidance/vat-domestic-reverse-charge-for-building-and-construction-services | 2026-10-24 |
| HMRC, VAT reverse charge technical guide | https://www.gov.uk/guidance/vat-reverse-charge-technical-guide | 2026-10-24 |
| HMRC, VAT Notice 741A (place of supply of services) | https://www.gov.uk/guidance/vat-place-of-supply-of-services-notice-741a | 2026-10-24 |
| HMRC, VAT Notice 706 (partial exemption) | https://www.gov.uk/guidance/partial-exemption-vat-notice-706 | 2026-10-24 |
| HMRC, VAT Notice 700/45 (correcting errors) | https://www.gov.uk/guidance/how-to-correct-vat-errors-and-make-adjustments-or-claims-vat-notice-70045 | 2026-10-24 |
| VATA 1994 s 26A (customer repays input tax on unpaid supplies) | https://www.legislation.gov.uk/ukpga/1994/23/section/26A | 2026-10-24 |
| VATA 1994 s 36 (bad debt relief) | https://www.legislation.gov.uk/ukpga/1994/23/section/36 | 2026-10-24 |
| VAT Regulations 1995 Part XIX, regs 165A, 166 and 172(1A) (bad debt relief claims) | https://www.legislation.gov.uk/uksi/1995/2518/part/XIX | 2026-10-24 |
| VAT Regulations 1995 Part XV, regs 113 and 114 (Capital Goods Scheme, as amended from 29 July 2026) | https://www.legislation.gov.uk/uksi/1995/2518/part/XV | 2026-10-24 |
| VAT (Amendment) Regulations 2026, SI 2026/765 (Capital Goods Scheme changes) | https://www.legislation.gov.uk/uksi/2026/765/made | 2026-10-24 |
| VAT (Input Tax) Order 1992, SI 1992/3222, arts 2, 5 and 7 (motor car, business entertainment, cars) | https://www.legislation.gov.uk/uksi/1992/3222/article/7 | 2026-10-24 |
| HMRC, VAT Notice 700, section 12.3 (mobile phones; updated 25 June 2026) | https://www.gov.uk/guidance/vat-guide-notice-700 | 2026-10-24 |
| HMRC, VAT Notice 700/64 (motoring expenses), 4.4 and 9.1 | https://www.gov.uk/guidance/vat-on-motoring-expenses-notice-70064 | 2026-10-24 |
| HMRC, VAT Notice 700/65 (business entertainment), 2.6 and 3.2 | https://www.gov.uk/guidance/business-entertainment-and-vat-notice-70065 | 2026-10-24 |
| HMRC, VAT Notice 700/18 (bad debt relief), 3.12 and 3.14 | https://www.gov.uk/guidance/relief-from-vat-on-bad-debts-notice-70018 | 2026-10-24 |
| HMRC, VAT Notice 706/2 (Capital Goods Scheme; updated 29 July 2026) | https://www.gov.uk/guidance/capital-goods-scheme-notice-7062 | 2026-10-24 |
| GOV.UK, how to send your VAT Return | https://www.gov.uk/vat-returns/how-to-send-your-vat-return | 2026-10-31 |
| GOV.UK, when to do a VAT Return | https://www.gov.uk/vat-returns | 2026-10-31 |
| GOV.UK, pay your VAT bill (Direct Debit, bank details, timing, repayments) | https://www.gov.uk/pay-vat/print | 2026-10-31 |
| GOV.UK, VAT Notice 700/12 (updated 19 December 2025; boxes, submission, repayment) | https://www.gov.uk/guidance/how-to-fill-in-and-submit-your-vat-return-vat-notice-70012 | 2026-10-31 |
| GOV.UK, VAT Notice 700/45 (methods, limits, where to send) | https://www.gov.uk/guidance/how-to-correct-vat-errors-and-make-adjustments-or-claims-vat-notice-70045 | 2026-10-31 |
| GOV.UK, if you cannot pay your tax bill | https://www.gov.uk/difficulties-paying-hmrc | 2026-10-31 |
| GOV.UK, Flat Rate Scheme, all parts | https://www.gov.uk/vat-flat-rate-scheme/print | 2026-10-31 |

Not yet confirmed: The statutory instrument that adds the 7 days to the online return deadline was not read; the deadline is from HMRC's page. The legal basis for Making Tax Digital for VAT (VAT Regulations 1995 Part V) and for late payment interest (Finance Act 2009 s 101) was not read; those rules are from HMRC's notices. The VAT Notice 700/1 supplement threshold table ends at 31 March 2026; the GBP 90,000 figure for later dates rests on the statute, which shows no outstanding changes. What the software itself shows as a submission receipt varies by product and was not read.
