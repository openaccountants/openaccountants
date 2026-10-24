---
name: uk-vat-return
description: "UK VAT for a business registered in Great Britain, as the law stands on 24 October 2026. VAT has no tax year: each figure carries the date it applies from. Covers the 20%, 5% and 0% rates and exempt supplies, the temporary zero rate on domestic electricity (1 October 2026 to 31 March 2027), registration at GBP 90,000 on the rolling 12-month and 30-day tests, deregistration at GBP 88,000, Making Tax Digital, the nine boxes of the return, the deadline of one month and 7 days, the Flat Rate, cash and annual accounting schemes, reverse charges for overseas services and construction (CIS), penalty points, late payment penalties, interest at base rate plus 4%, and a partial exemption pointer. Trigger on: VAT return, VAT100, 9 boxes, VAT threshold, MTD for VAT, reverse charge, VAT penalty. Out of scope: the short routine (vat-returns-for-small-businesses-in-the-uk), Xero closes (close-the-uk-vat-quarter-from-xero, xero-uk-vat-close), EU goods sellers (gb-vat-eu-goods-sellers)."
version: 2.1
jurisdiction: GB
category: international
tax_year: 2026
last_updated: 2026-10-24
authored_by: Michael Cutajar and the OpenAccountants team
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# UK VAT return: rates, registration, the nine boxes, penalties (position at 24 October 2026)

Source-cited draft: not reviewed by an accountant. Built by Michael Cutajar and the OpenAccountants team.

VAT is not tied to the 6 April income tax year. Rates change when the law changes, and the registration limits are set by order and have been the same since 1 April 2024. Every figure below says the date it applies from. Return periods are set by HMRC for each business (usually quarterly).

This skill is the method and the figures. It links to the other UK VAT skills and does not repeat them:

- `vat-returns-for-small-businesses-in-the-uk`: the short quarterly routine for a small business.
- `close-the-uk-vat-quarter-from-xero` and `xero-uk-vat-close`: closing a quarter from Xero.
- `gb-vat-eu-goods-sellers`: EU sellers shipping goods into Great Britain.

## Who this applies to

- A business that belongs in the UK and makes taxable supplies in Great Britain (England, Scotland, Wales): sole traders, partnerships and companies.
- **Must register** if, at the end of any month, taxable turnover for the last 12 months has gone over GBP 90,000, or if at any time there are reasonable grounds to expect taxable turnover in the next 30 days alone to go over GBP 90,000 ([VATA 1994 Sch 1 para 1](https://www.legislation.gov.uk/ukpga/1994/23/schedule/1/paragraph/1)). "Has exceeded" means exactly GBP 90,000 does not trigger registration.
- **12-month test:** register within 30 days of the end of the month you went over. You are registered from the first day of the second month after you went over. HMRC's example: over on 15 July, register by 30 August, registered from 1 September ([gov.uk: when you must register](https://www.gov.uk/register-for-vat)).
- **30-day test:** register by the end of that 30-day period. You are registered from the date you realised, not the date turnover went over.
- **Temporary excess:** no registration if HMRC are satisfied taxable supplies in the next 12 months will not exceed GBP 88,000 (Sch 1 para 1(3)).
- **Taxable turnover** includes zero-rated and reduced-rated sales. It leaves out exempt and outside-the-scope income. A UK business that is not registered must add the value of business services it buys from overseas suppliers under the general rule ([VAT Notice 741A, 5.7](https://www.gov.uk/guidance/vat-place-of-supply-of-services-notice-741a)).
- **Voluntary registration** is allowed below GBP 90,000.
- **Non-established taxable persons** (no UK business establishment) have no threshold: any taxable supply in the UK means registering ([VAT Notice 700/1 supplement, 2.1](https://www.gov.uk/government/publications/vat-notice-7001-should-i-be-registered-for-vat/vat-notice-7001-supplement--2)). See `gb-vat-eu-goods-sellers`.
- **Deregistration:** you can ask to cancel if HMRC are satisfied taxable supplies in the next 12 months will not exceed GBP 88,000, unless the fall is because you will stop or suspend taxable supplies for 30 days or more ([Sch 1 para 4](https://www.legislation.gov.uk/ukpga/1994/23/schedule/1/paragraph/4); [gov.uk: cancel registration](https://www.gov.uk/register-for-vat/cancel-your-registration)).
- Northern Ireland goods trade with the EU (boxes 2, 8 and 9), VAT groups, margin and retail schemes, and land and property options are outside this skill.

## Rates, bands and thresholds

| Item | Rate or amount | From (in force on 24 Oct 2026) | Source URL |
|---|---|---|---|
| Standard rate (VATA 1994 s 2(1)) | 20% | 4 January 2011 | https://www.legislation.gov.uk/ukpga/1994/23/section/2 |
| Reduced rate, Schedule 7A supplies (s 29A), for example home energy other than GB domestic electricity, children's car seats | 5% | in force | https://www.legislation.gov.uk/ukpga/1994/23/section/29A |
| Zero rate (Schedule 8), for example most food, children's clothes, books, exports of goods | 0% | in force | https://www.gov.uk/vat-rates |
| Domestic electricity in England, Wales and Scotland (new Sch 8 Group 24; at least 60% qualifying use means the whole supply qualifies; up to 1,000 kWh a month is deemed domestic) | 0% | 1 October 2026 to 31 March 2027 (SI 2026/987) | https://www.legislation.gov.uk/uksi/2026/987/made |
| Children's meals eaten on the premises, children's and family admissions to shows, attractions and museums (temporary Sch 7A Groups 17 and 18) | 5% | 25 June 2026 to 1 September 2026 only; ended (SI 2026/576) | https://www.legislation.gov.uk/uksi/2026/576/made |
| Registration threshold, 12-month and 30-day tests (Sch 1 para 1) | GBP 90,000 | 1 April 2024 (SI 2024/307); unchanged since | https://www.legislation.gov.uk/ukpga/1994/23/schedule/1/paragraph/1 |
| Deregistration and temporary-excess limit (Sch 1 paras 1(3) and 4) | GBP 88,000 | 1 April 2024 (SI 2024/307); unchanged since | https://www.legislation.gov.uk/ukpga/1994/23/schedule/1/paragraph/4 |
| Flat Rate Scheme: join | Expected VAT taxable turnover GBP 150,000 or less (excluding VAT) in the next 12 months | in force | https://www.gov.uk/vat-flat-rate-scheme/who-can-join |
| Flat Rate Scheme: must leave | Over GBP 230,000 (including VAT) in the last 12 months at the anniversary of joining, or expected in the next 12 months, or in the next 30 days alone | in force | https://www.gov.uk/vat-flat-rate-scheme/if-your-circumstances-change |
| Flat Rate Scheme: limited cost business rate | 16.5% if goods cost less than 2% of turnover, or more than 2% but less than GBP 1,000 a year | in force | https://www.gov.uk/vat-flat-rate-scheme/how-much-you-pay |
| Flat Rate Scheme: first-year discount | 1 percentage point off in the first year of VAT registration | in force | https://www.gov.uk/vat-flat-rate-scheme/how-much-you-pay |
| Cash accounting: join / must leave | GBP 1.35 million or less expected / over GBP 1.6 million | in force | https://www.gov.uk/vat-cash-accounting-scheme/eligibility |
| Annual accounting: join / must leave | GBP 1.35 million or less expected / over GBP 1.6 million | in force | https://www.gov.uk/vat-annual-accounting-scheme/eligibility |
| Partial exemption de minimis | Exempt input tax not more than GBP 625 a month on average and not more than half of all input tax | in force | https://www.gov.uk/guidance/partial-exemption-vat-notice-706 |
| Late submission penalty (FA 2021 Sch 24) | GBP 200 at the points threshold: annual 2, quarterly 4, monthly 5 points | periods starting on or after 1 January 2023 | https://www.gov.uk/guidance/penalty-points-and-penalties-if-you-submit-your-vat-return-late |
| Late payment penalties (FA 2021 Sch 26 paras 5 and 8) | 3% of VAT unpaid at day 15, plus 3% of VAT unpaid at day 30, plus 10% a year from day 31 | VAT periods starting on or after 1 April 2025 (SI 2025/589); earlier periods 2%, 2%, 4% | https://www.legislation.gov.uk/ukpga/2021/26/schedule/26 |
| Late payment interest | Bank of England base rate plus 4%: 7.75% (base rate 3.75%) | plus 4% since 6 April 2025; 7.75% since 9 January 2026 | https://www.gov.uk/government/publications/rates-and-allowances-hmrc-interest-rates-for-late-and-early-payments/rates-and-allowances-hmrc-interest-rates |
| Error correction on the current return (method 1) | Net errors up to GBP 10,000, or up to GBP 50,000 if not more than 1% of box 6 | in force | https://www.gov.uk/guidance/how-to-correct-vat-errors-and-make-adjustments-or-claims-vat-notice-70045 |

Exempt supplies carry no VAT and give no right to reclaim VAT on related costs. Examples: postage stamps, financial and insurance services, most residential lettings ([gov.uk VAT rates](https://www.gov.uk/vat-rates)). Outside the scope: wages, money you put in, loans, dividends, and business services sold to customers who belong outside the UK.

## The taxable base

**Output VAT (box 1).** VAT on every taxable supply in the period at its rate. Also: postponed import VAT, reverse charge VAT, fuel scale charges, goods taken for private use, gifts of goods costing more than GBP 50 excluding VAT, sales of business assets. Deduct VAT on credit notes you issue ([VAT Notice 700/12, 3.2](https://www.gov.uk/guidance/how-to-fill-in-and-submit-your-vat-return-vat-notice-70012)).

**Input VAT (box 4).** VAT on purchases used for taxable business supplies, backed by a proper VAT invoice (or import VAT certificate). Also: reverse charge VAT, postponed import VAT, bad debt relief. Never: VAT on goods wholly for personal use, business entertainment, margin scheme purchases. A partly exempt business recovers only under the partial exemption rules ([VAT Notice 700/12, 3.5](https://www.gov.uk/guidance/how-to-fill-in-and-submit-your-vat-return-vat-notice-70012)).

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
| Services bought from a supplier who belongs outside the UK (general rule B2B services, such as software, advertising, consultancy) | Box 6 | Box 1 (output VAT), box 4 (input VAT), box 6 and box 7 (value) |
| Construction services reported within CIS, between VAT and CIS registered businesses | Box 6 only; invoice says the customer accounts for the VAT | Box 1, box 4 and box 7; nothing in box 6 |

The construction reverse charge covers standard and reduced-rate construction operations within CIS. It does not apply when the customer is an end user or intermediary supplier and tells the supplier in writing, to zero-rated work, or to stand-alone services such as architects, surveyors, delivering materials or installing security systems. A reverse charge element of 5% or less of a single supply can be disregarded only if both parties agree it from the start on overall contract values ([gov.uk: when to use the construction reverse charge](https://www.gov.uk/guidance/vat-domestic-reverse-charge-for-building-and-construction-services); [technical guide](https://www.gov.uk/guidance/vat-reverse-charge-technical-guide)). Services you sell to business customers abroad under the general rule are outside the scope: box 6 only.

**Schemes, in summary.**

- **Flat Rate Scheme:** pay a fixed percentage of VAT-inclusive turnover (including zero-rated and exempt income). Charge normal VAT on invoices. No input VAT except capital goods costing GBP 2,000 or more including VAT. Box 6 holds the flat rate turnover including VAT. Sector rates include 14.5% for accountancy and for IT consultancy and 12% for activities not listed elsewhere; the limited cost rate is 16.5% ([gov.uk: how much you pay](https://www.gov.uk/vat-flat-rate-scheme/how-much-you-pay)). Test the limited cost rule on every return.
- **Cash accounting:** account for output VAT when the customer pays and reclaim input VAT when you pay. Cannot be used with the Flat Rate Scheme or for reverse charge supplies ([gov.uk](https://www.gov.uk/vat-cash-accounting-scheme/eligibility)).
- **Annual accounting:** one return a year, due 2 months after the year end, with advance payments of 10% of the estimated bill monthly or 25% quarterly ([gov.uk](https://www.gov.uk/vat-annual-accounting-scheme/return-and-payment-deadlines)).

**Partial exemption, pointer only.** A business making taxable and exempt supplies cannot recover input VAT used for exempt supplies, or the exempt share of overheads, unless it passes the de minimis test in the rates table. Apply the standard method or an approved special method, with an annual adjustment ([VAT Notice 706](https://www.gov.uk/guidance/partial-exemption-vat-notice-706)). Refer anyone who fails de minimis.

## Deadlines and filing

- **Return periods:** usually quarterly, on dates in your registration certificate. Monthly on request; annual under annual accounting.
- **Return and payment:** online, one calendar month and 7 days after the period ends. The payment must reach HMRC's account by then, even if the deadline is a weekend or bank holiday ([gov.uk: VAT return deadlines](https://www.gov.uk/vat-returns/deadlines)). The regulation sets the last day of the following month ([VAT Regulations 1995 reg 25](https://www.legislation.gov.uk/uksi/1995/2518/regulation/25)); HMRC's online deadline adds the 7 days.
- **A return is due even if nothing is payable** (nil or repayment returns).
- **Annual accounting:** return 2 months after the end of the accounting period.
- **Making Tax Digital:** all VAT-registered businesses keep digital records and file through compatible software. Links between programs must be digital; copy and paste is not a digital link. Exemption only where digital records are not practical (for example age, disability, location, religious objection) or for insolvency ([VAT Notice 700/22](https://www.gov.uk/government/publications/vat-notice-70022-making-tax-digital-for-vat/vat-notice-70022-making-tax-digital-for-vat)).
- **Corrections:** a return cannot be amended once sent. Net errors within the method 1 limit go on the current return; larger or deliberate errors are notified to HMRC separately (method 2). Time limit: 4 years ([VAT Notice 700/45](https://www.gov.uk/guidance/how-to-correct-vat-errors-and-make-adjustments-or-claims-vat-notice-70045)).

## Penalties and interest

**Late submission (points).** Each late return earns one point until the threshold: annual returns 2, quarterly 4, monthly 5. At the threshold you pay GBP 200, and GBP 200 again for each further late return while at the threshold. Applies to periods starting on or after 1 January 2023, including nil and repayment returns ([gov.uk: penalty points](https://www.gov.uk/guidance/penalty-points-and-penalties-if-you-submit-your-vat-return-late); [FA 2021 Sch 24](https://www.legislation.gov.uk/ukpga/2021/26/schedule/24)).

**Late payment penalties** ([gov.uk](https://www.gov.uk/guidance/how-late-payment-penalties-work-if-you-pay-vat-late); [FA 2021 Sch 26](https://www.legislation.gov.uk/ukpga/2021/26/schedule/26)):

| Days overdue | Penalty (VAT periods starting on or after 1 April 2025) |
|---|---|
| 1 to 15 | None |
| 16 to 30 | First penalty: 3% of the VAT unpaid at day 15 |
| 31 or more | First penalty: 3% at day 15 plus 3% of the VAT still unpaid at day 30. Second penalty: 10% a year, daily, on the unpaid balance from day 31 until paid |

- They do not apply to payments on account or annual accounting instalments.
- A Time to Pay request by day 15 (or by day 30) stops the next stage. Breaking the arrangement brings back both penalties as if it never existed.
- For VAT periods that began before 1 April 2025 the percentages were 2%, 2% and 4% a year ([SI 2025/589 reg 1(3)](https://www.legislation.gov.uk/uksi/2025/589/made)).

**Late payment interest** runs from the first day the payment is overdue until it is paid in full, at Bank of England base rate plus 4% ([gov.uk: late payment interest](https://www.gov.uk/guidance/late-payment-interest-if-you-do-not-pay-vat-or-penalties-on-time)). On 24 October 2026 base rate is 3.75% (held 17 September 2026; next decision 5 November 2026), so the rate is 7.75%, as in HMRC's table from 9 January 2026. Recheck HMRC's table after each base rate decision.

**Errors.** Careless or deliberate inaccuracies can be penalised; telling HMRC before they find out reduces the penalty (VAT Notice 700/45).

## Cross-border points

- **Services bought from abroad:** reverse charge as in the table above (Notice 741A). The supplier may be EU or non-EU.
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

**Example 2: paying 51 days late.** A company files its return for the quarter to 30 September 2026 on time, showing GBP 15,000 to pay by 7 November 2026. It pays nothing until 28 December 2026, day 51, and never asked for Time to Pay. The period started after 1 April 2025, so the 2025 percentages apply. First penalty: 3% of GBP 15,000 at day 15 plus 3% at day 30, GBP 900. Second penalty: 10% a year for 21 days (day 31 to day 51), GBP 86.30. Interest at 7.75% for 51 days: GBP 162.43. This assumes base rate stays at 3.75% to 28 December; if it changes on 5 November, split the interest at the change date. Total cost GBP 1,148.73 on top of the VAT. A Time to Pay request by day 15 would have stopped both penalties.

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

## Ask the client first

1. Are you VAT registered? From what date, on which return periods, and under which schemes (Flat Rate, cash, annual)? If not: your taxable turnover month by month for the last 12 months, and any single 30 days ahead that could go over GBP 90,000.
2. What do you sell, to whom (UK or abroad, business or consumer), and at which rates? Any exempt income (rents, insurance, financial services)? If yes, partial exemption applies.
3. Do you buy services from suppliers outside the UK, or construction services within CIS?
4. Do you hold VAT invoices for everything you reclaim? Any cars, fuel, entertaining or mixed-use costs?
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
| HMRC, Cash Accounting Scheme eligibility | https://www.gov.uk/vat-cash-accounting-scheme/eligibility | 2026-10-24 |
| HMRC, Annual Accounting Scheme eligibility and deadlines | https://www.gov.uk/vat-annual-accounting-scheme/return-and-payment-deadlines | 2026-10-24 |
| HMRC, Construction domestic reverse charge | https://www.gov.uk/guidance/vat-domestic-reverse-charge-for-building-and-construction-services | 2026-10-24 |
| HMRC, VAT reverse charge technical guide | https://www.gov.uk/guidance/vat-reverse-charge-technical-guide | 2026-10-24 |
| HMRC, VAT Notice 741A (place of supply of services) | https://www.gov.uk/guidance/vat-place-of-supply-of-services-notice-741a | 2026-10-24 |
| HMRC, VAT Notice 706 (partial exemption) | https://www.gov.uk/guidance/partial-exemption-vat-notice-706 | 2026-10-24 |
| HMRC, VAT Notice 700/45 (correcting errors) | https://www.gov.uk/guidance/how-to-correct-vat-errors-and-make-adjustments-or-claims-vat-notice-70045 | 2026-10-24 |

Not yet confirmed: HMRC's interest rate table was last updated 23 December 2025; the 7.75% figure is confirmed only by adding 4% to the Bank of England rate shown on 24 October 2026. The statutory instrument that adds the 7 days to the online return deadline was not read; the deadline is from HMRC's page. The legal basis for Making Tax Digital for VAT (VAT Regulations 1995 Part V) and for late payment interest (Finance Act 2009 s 101) was not read; those rules are from HMRC's notices. The VAT Notice 700/1 supplement threshold table ends at 31 March 2026; the GBP 90,000 figure for later dates rests on the statute, which shows no outstanding changes.

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
