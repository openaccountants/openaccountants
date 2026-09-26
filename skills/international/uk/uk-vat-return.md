---
name: uk-vat-return
description: Use this skill whenever asked to prepare, review, or classify transactions for a UK VAT return (VAT100) for a self-employed individual or very small business in Great Britain. Trigger on phrases like "prepare VAT return", "do my VAT", "classify these for VAT", "VAT100", "9-box return", "MTD", "Making Tax Digital", "flat rate scheme", "FRS", "cash accounting VAT", "input tax", "output tax", "reverse charge construction", "CIS reverse charge", "bad debt relief", "Box 1 to Box 9", "reduced rate UK", "zero-rated UK", "exempt supply UK", "de minimis VAT", "annual accounting scheme", or any question about UK VAT obligations. Covers the VAT100 9-box structure, standard/reduced/zero rates, registration threshold (GBP 90,000), Flat Rate Scheme, cash accounting scheme, annual accounting scheme, MTD requirements, input tax blocked categories, partial exemption, bad debt relief, and reverse charge for construction (CIS). MUST be loaded alongside vat-workflow-base v0.1 or later (for workflow architecture). ALWAYS read this skill before touching any UK VAT work.
version: 2.0
jurisdiction: GB
tax_year: 2026
last_updated: 2026-09-25
authored_by: OpenAccountants team
review_status: pending_review
trust_label: By OpenAccountants
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# UK VAT returns for small businesses and freelancers: 2026/27 thresholds, rates, the 9 boxes, schemes, MTD, penalties and corrections

Figures are for tax year 2026/27, as the rules stand on 25 September 2026. VAT thresholds run from 1 April, so the thresholds below apply to 1 April 2026 to 31 March 2027. Every figure links to HM Revenue and Customs (HMRC) guidance on gov.uk or to the law on legislation.gov.uk. A short section near the end covers returns for 2025/26 periods that are still being filed or corrected.

## Scope and who this is for

- Sole traders, freelancers, partnerships and small companies in Great Britain (England, Scotland and Wales) that are VAT registered, or near the threshold, and prepare their own VAT return.
- Out of scope: Northern Ireland goods trade with the EU (boxes 2, 8 and 9), VAT groups, margin and retail schemes, the Capital Goods Scheme, land and buildings, and going concern transfers. See "When to refuse or refer".

## Ask the client first

- Are you VAT registered? If so, from what date, on what return periods (monthly, quarterly, annual), and under which schemes (standard, Flat Rate, cash accounting, annual accounting)?
- If not registered: what were your taxable sales in each of the last 12 months, and do you expect any single 30-day period ahead to bring in more than the threshold on its own?
- What do you sell, to whom (UK or abroad, businesses or consumers), and at which VAT rates? Any exempt income, such as residential rent, insurance commission or financial services?
- Do you buy services from suppliers based outside the UK (software, advertising, platforms)?
- Are you in the construction industry, registered for CIS, and do you buy or sell construction services?
- Do you have valid VAT invoices for the purchases you want to reclaim? Any cars, fuel, entertaining, home office or mixed-use costs?
- Which Making Tax Digital software do you use, and are all links between your records and the software digital?
- Any late returns, penalty points, Time to Pay arrangements, errors in earlier returns, or customers unpaid for 6 months or more?

## The method, step by step

1. **Check registration.** At the end of every month, test taxable turnover for the last 12 months, and whether the next 30 days alone will go over the threshold ([Register for VAT](https://www.gov.uk/register-for-vat)).
2. **Fix the period and scheme.** Confirm the return period dates and any schemes in use. The scheme changes which figures go in boxes 1, 4, 6 and 7 ([VAT Notice 700/12](https://www.gov.uk/guidance/how-to-fill-in-and-submit-your-vat-return-vat-notice-70012)).
3. **Classify each sale.** Standard, reduced, zero-rated, exempt, or outside the scope of UK VAT (for example, business services to an overseas business customer). Use the tax point to place each sale in the right period, unless cash accounting applies.
4. **Classify each purchase.** Is it for the business? Is there a valid VAT invoice or other evidence? Is the VAT blocked (cars, business entertainment, non-business use)? Does it relate to exempt supplies (partial exemption)? Is it a reverse charge supply?
5. **Account for reverse charges.** Services bought from overseas suppliers and CIS construction services go in box 1 and box 4, with the values in the boxes set out below.
6. **Build the 9 boxes** from the digital records in Making Tax Digital software. Check box 3 = box 1 + box 2 and box 5 = box 3 minus box 4.
7. **Add adjustments.** Bad debt relief, fuel scale charges, errors from earlier periods that are within the error correction limit, and any partial exemption annual adjustment.
8. **Check before you submit.** If all sales are standard-rated, box 1 should be about 20% of box 6 ([VAT Notice 700/12, 7.1](https://www.gov.uk/guidance/how-to-fill-in-and-submit-your-vat-return-vat-notice-70012)). You cannot amend a return after submission; errors are corrected later.
9. **Submit and pay** by 1 month and 7 days after the period end, allowing time for the payment to clear.

## Figures and rules for 2026/27

### Registration and deregistration ([Register for VAT](https://www.gov.uk/register-for-vat); [cancel your registration](https://www.gov.uk/register-for-vat/cancel-your-registration); [VAT Notice 700/1 supplement](https://www.gov.uk/government/publications/vat-notice-7001-should-i-be-registered-for-vat/vat-notice-7001-supplement--2); [VATA 1994 Sch 1 para 1](https://www.legislation.gov.uk/ukpga/1994/23/schedule/1/paragraph/1); [para 4](https://www.legislation.gov.uk/ukpga/1994/23/schedule/1/paragraph/4))

| Test | 2026/27 rule | Deadline and effective date |
| --- | --- | --- |
| Backward look (rolling 12 months) | Must register if taxable turnover for the last 12 months goes over £90,000. The law says "has exceeded", so exactly £90,000 does not trigger registration | Register within 30 days of the end of the month in which you went over. Effective date: first day of the second month after you went over |
| Forward look (next 30 days) | Must register if you expect taxable turnover in the next 30 days alone to go over £90,000 | Register by the end of that 30-day period. Effective date: the date you realised, not the date turnover went over |
| Temporary excess | You may apply for exception from registration if you can show HMRC that taxable supplies in the next 12 months will not go over the deregistration threshold | HMRC decides; if refused, you are registered |
| Voluntary registration | Allowed below £90,000 | VAT is owed from the date HMRC register you |
| Non-established taxable persons | No threshold: register if you make any taxable supplies in the UK | |
| Voluntary deregistration | You can ask to cancel if HMRC are satisfied taxable supplies in the next year will not exceed £88,000 (gov.uk says "falls below £88,000"). Not available if the fall is because you will stop making taxable supplies or suspend them for 30 days or more | You cannot backdate cancellation because turnover fell |
| Compulsory cancellation | You stop trading or making taxable supplies, or join a VAT group | Cancel within 30 days of becoming ineligible |

- Taxable turnover includes zero-rated and reduced-rated sales, services from abroad that you reverse charge, domestic reverse charge supplies, and building work over £100,000 your business did for itself. It excludes exempt and out-of-scope sales.
- An unregistered UK business that buys general rule services from overseas suppliers must add their value to its own taxable supplies when testing the threshold ([VAT Notice 741A, 5.7](https://www.gov.uk/guidance/vat-place-of-supply-of-services-notice-741a)).
- After cancellation, submit a final return up to and including the cancellation date. Account for stock and assets on hand if you reclaimed (or could have reclaimed) VAT on them and the VAT due on them is over £1,000. Keep VAT records for 6 years.
- Late registration: VAT is due on sales since the date you should have registered, and a penalty may apply.

### Rates ([VAT rates](https://www.gov.uk/vat-rates); [rates on different goods and services](https://www.gov.uk/guidance/rates-of-vat-on-different-goods-and-services))

| Rate | 2026/27 | Examples and traps |
| --- | --- | --- |
| Standard | 20% | Most goods and services. Always standard-rated food: catering, alcoholic drinks, confectionery, crisps and savoury snacks, hot food, hot takeaways, ice cream, soft drinks and mineral water, sports drinks |
| Reduced | 5% | Home energy (gas and heating oil for domestic use), children's car seats, smoking cessation products such as nicotine patches and gum |
| Zero | 0% | Most food, children's clothes and footwear, books and newspapers, water supplied to households (water to industrial customers is standard-rated), sanitary protection products, passenger transport in vehicles carrying at least 10 passengers, energy-saving materials installed in residential accommodation (0% until 31 March 2027), exports of goods |
| Exempt | No VAT, and no input tax on related costs | Postage stamps, financial and property transactions, insurance, most residential lettings, health services by registered professionals |
| Outside the scope | Not a supply for UK VAT | Wages, statutory fees such as vehicle licence duty and local authority rates, money you put in, loans and dividends, B2B services supplied to customers who belong outside the UK |

**Temporary changes in 2026 ([SI 2026/987](https://www.legislation.gov.uk/uksi/2026/987/made); [SI 2026/576](https://www.legislation.gov.uk/uksi/2026/576/made))**

- **Domestic electricity, 1 October 2026 to 31 March 2027:** electricity for domestic use (or non-business use by a charity) in England, Wales and Scotland is zero-rated. If at least 60% of a supply is for qualifying use, all of it qualifies; otherwise apportion. Northern Ireland domestic electricity and domestic gas stay at the reduced rate; business electricity is usually standard-rated. A supply to premises of not more than 1,000 kilowatt hours a month (from the same supplier) is deemed to be for domestic use. A home-office electricity bill for supplies from 1 October 2026 carries no VAT to reclaim.
- **Children's meals and family attractions, 25 June 2026 to 1 September 2026:** a temporary reduced rate of 5% (the Schedule 7A reduced rate, [VATA 1994 s 29A](https://www.legislation.gov.uk/ukpga/1994/23/section/29A)) applied to certain children's meals eaten on the premises and certain children's, family and attraction admissions. Returns covering those dates use it for qualifying sales; it has ended.

### The 9 boxes ([VAT Notice 700/12](https://www.gov.uk/guidance/how-to-fill-in-and-submit-your-vat-return-vat-notice-70012))

| Box | What goes in it |
| --- | --- |
| 1 | Output VAT on sales, postponed import VAT, reverse charge VAT, fuel scale charges, goods taken for private use, gifts of goods costing more than £50 excluding VAT, sales of business assets, less VAT on credit notes you issue |
| 2 | VAT due on acquisitions of goods brought into Northern Ireland from EU member states only. For a Great Britain business this is 0.00 |
| 3 | Box 1 plus box 2 |
| 4 | Deductible input VAT backed by a proper VAT invoice, import VAT, reverse charge VAT, bad debt relief, less VAT on credit notes you receive. Not VAT on personal use or business entertainment |
| 5 | Box 3 minus box 4. Positive: you pay. Negative: HMRC repay. No minus sign on a paper return |
| 6 | All sales excluding VAT: standard, reduced, zero-rated and exempt sales, exports, supplies outside the scope under the place of supply rules, reverse charge values where required. Not money you put in, loans, dividends or insurance claims |
| 7 | All purchases excluding VAT, including imports and reverse charge values. Not wages, PAYE and National Insurance, drawings, loans, dividends, MOT certificates, vehicle licence duty, local authority rates or other out-of-scope items |
| 8 | Supplies of goods from Northern Ireland to EU member states only (also included in box 6). Exports from Great Britain are not entered here |
| 9 | Acquisitions of goods into Northern Ireland from EU member states only (also included in box 7). Imports into Great Britain are not entered here |

### Flat Rate Scheme ([who can join](https://www.gov.uk/vat-flat-rate-scheme/who-can-join); [work out your flat rate](https://www.gov.uk/vat-flat-rate-scheme/how-much-you-pay); [if your circumstances change](https://www.gov.uk/vat-flat-rate-scheme/if-your-circumstances-change); [VAT Notice 733](https://www.gov.uk/guidance/flat-rate-scheme-for-small-businesses-vat-notice-733--2))

| Rule | 2026/27 |
| --- | --- |
| Join | VAT registered and expect VAT taxable turnover of £150,000 or less (excluding VAT) in the next 12 months |
| Cannot join | Left the scheme or committed a VAT offence in the last 12 months; VAT group or division in the last 24 months; closely associated with another business; margin or capital goods scheme |
| Must leave | On the anniversary of joining, income in the last 12 months was more than £230,000 including VAT, or you expect it to be in the next 12 months; or you expect income in the next 30 days alone to be more than £230,000 |
| Stay despite a one-off | You may stay only with HMRC's agreement: apply in writing and show that VAT-inclusive turnover in the coming year will not exceed £191,500 and that the increase came from unexpected business activity which has not occurred before and is not expected to recur |
| How VAT is worked out | Flat rate percentage x VAT-inclusive turnover, including zero-rated and exempt income. Charge normal VAT on your invoices |
| Limited cost business | If relevant goods (including VAT) cost less than 2% of flat rate turnover, or more than 2% but less than £1,000 a year (£250 for a quarterly return), the rate is 16.5% whatever the sector. Test every return; the rate can change between periods |
| First-year reduction | 1% off your flat rate until the day before the first anniversary of your VAT registration (not of joining the scheme). Not available if you registered 12 months or more after you were required to |
| Capital goods | Reclaim VAT outside the scheme (box 4) on a single purchase of capital expenditure goods costing £2,000 or more including VAT. No claim for services or for several purchases each under £2,000 |
| Cash accounting | Cannot be combined; the scheme has its own cash-based turnover method |
| After leaving | Wait 12 months before rejoining |

**Relevant goods** for the limited cost test are goods used exclusively for the business. They exclude: vehicle costs including fuel (unless you are in the transport sector using your own or a leased vehicle); food or drink for you or your staff; capital expenditure goods of any value; goods for resale, leasing, letting or hiring out unless that is your main business activity; goods for disposal such as promotional items, gifts or donations; and any services.

**Selected sector rates** (use the sector that most closely describes what the business will do in the coming year):

| Sector | Flat rate |
| --- | --- |
| Accountancy or book-keeping; computer and IT consultancy or data processing; lawyer or legal services | 14.5% |
| Labour-only building or construction services (materials less than 10% of turnover for those services) | 14.5% |
| Management consultancy | 14% |
| Hairdressing or other beauty treatment services | 13% |
| Any other activity not listed elsewhere; business services not listed elsewhere | 12% |
| Advertising; photography; publishing | 11% |
| Secretarial services | 13% |
| Social work | 11% |
| Computer repair services | 10.5% |
| Transport or storage, including couriers, freight, removals and taxis | 10% |
| General building or construction services | 9.5% |
| Limited cost business (any sector) | 16.5% |

**FRS boxes:** box 1 = flat rate VAT plus any VAT outside the scheme (reverse charges, postponed import VAT added after the flat rate, sales of capital goods you reclaimed on). Box 4 = VAT on qualifying capital goods, bad debt relief, reverse charge input VAT. Box 6 = the turnover you applied the flat rate to, **including VAT**, plus any supplies accounted for outside the scheme. Box 7 = usually blank, except qualifying capital goods, box 9 amounts and reverse charge values. Since 1 June 2022, imports under postponed VAT accounting are left out of flat rate turnover.

### Cash accounting and annual accounting ([cash accounting eligibility](https://www.gov.uk/vat-cash-accounting-scheme/eligibility); [VAT Notice 731](https://www.gov.uk/guidance/vat-cash-accounting-scheme-notice-731); [annual accounting eligibility](https://www.gov.uk/vat-annual-accounting-scheme/eligibility); [annual accounting deadlines](https://www.gov.uk/vat-annual-accounting-scheme/return-and-payment-deadlines))

| | Cash Accounting Scheme | Annual Accounting Scheme |
| --- | --- | --- |
| Join | Estimated VAT taxable turnover of £1.35 million or less in the next 12 months; returns and payments up to date; no VAT offence in the last 12 months; not on the Flat Rate Scheme | Estimated VAT taxable turnover of £1.35 million or less in the next 12 months; not in a VAT group or division; returns and payments up to date; not insolvent; not left the scheme in the last 12 months |
| Leave | Taxable supplies in the 12 months to the end of a VAT period more than £1.6 million (leave at the end of that period; a one-off increase may be ignored if the next 12 months will be below £1.35 million) | Turnover is, or is likely to be, more than £1.6 million at the end of the annual accounting year |
| How it works | VAT on sales when paid; input tax when you pay. No need to tell HMRC you use it | One return a year; advance payments of 10% of the estimated bill monthly (months 4 to 12) or 25% quarterly (months 4, 7 and 10), then a balancing payment |
| Exclusions | Not for invoices with payment terms of 6 months or more, invoices raised in advance, hire purchase, lease purchase, conditional or credit sale, importing goods into Northern Ireland from the EU, moving goods outside a customs warehouse, or reverse charge supplies | Only 1 refund a year, so poor for repayment traders |
| On leaving | Account for all outstanding VAT, whether or not customers have paid, either in that period or, if you choose, over the next 6 months. The 6-month option is not available if HMRC withdrew the scheme from you, or if taxable supplies went over £1.6 million and supplies in the previous 3 months totalled more than £1.35 million | Account in the usual way from the leaving date HMRC confirm; wait 12 months to rejoin |
| Return deadline | Normal (1 month and 7 days) | 2 months after the end of the accounting period (1 month if the period is less than 4 months) |

### Making Tax Digital ([VAT Notice 700/22](https://www.gov.uk/government/publications/vat-notice-70022-making-tax-digital-for-vat/vat-notice-70022-making-tax-digital-for-vat); [exemptions](https://www.gov.uk/guidance/apply-for-an-exemption-from-making-tax-digital-for-vat))

- All VAT-registered businesses must keep VAT records digitally and file returns using compatible software, whatever their turnover (this has applied to businesses below the threshold since 1 April 2022). HMRC have signed up remaining businesses automatically.
- Links between software (for example a spreadsheet plus bridging software) must be digital: file import and export, automated transfer or API. Copy and paste, or re-keying, is not a digital link.
- Exempt automatically: insolvency procedures, and a final return after cancellation. Others may apply if using computers or the internet is not reasonable or practical (for example age, health, disability, location, religious objection).

### Input tax: conditions and blocked items ([VAT Notice 700](https://www.gov.uk/guidance/vat-guide-notice-700); [business entertainment, Notice 700/65](https://www.gov.uk/guidance/business-entertainment-and-vat-notice-70065); [motoring, Notice 700/64](https://www.gov.uk/guidance/vat-on-motoring-expenses-notice-70064))

Conditions to reclaim:

- The goods or services are supplied to you and used for your business, and relate to taxable (or equivalent) supplies.
- You hold valid evidence, normally a VAT invoice. A simplified invoice is allowed for supplies of £250 or less. With cash accounting you must also have paid.
- Claim on the return for the period in which you were first entitled. A missed claim is an error to be corrected, within 4 years from the due date of that return.
- Before registration: goods still held (bought up to 4 years before) and services (up to 6 months before) can be reclaimed.

Blocked or restricted:

| Item | Treatment |
| --- | --- |
| Goods and services not used for the business | Not input tax. Apportion mixed-use costs (for example a home office) on a fair and reasonable basis |
| Cars | VAT on buying a car is blocked unless it is used exclusively for business and not available for private use, or bought primarily for taxis, self-drive hire or driving instruction. Leasing a qualifying car for business: 50% of the VAT is blocked, unless you intend to use the car primarily for hire with a driver (taxi), self-drive hire or driving instruction, or exclusively for the business with no private use by anyone (then all the lease VAT is recoverable, [Input Tax Order art 7](https://www.legislation.gov.uk/uksi/1992/3222/article/7)). HMRC also accept that the block does not apply to a car hired for no more than 10 days specifically for business use where you do not have a company car. Vans and other commercial vehicles follow normal rules |
| Road fuel | Four options: claim all VAT (only where there is no private use), claim all and apply the fuel scale charge, use detailed mileage records to separate business from private mileage, or claim nothing |
| Business entertainment | Blocked for UK business contacts and non-UK contacts who are not customers. Entertaining only directors, partners or sole proprietors is not input tax; staff entertainment is recoverable. Overseas customers: may be recoverable if reasonable in scale and character, but a private benefit triggers an output tax charge (a restaurant meal very likely does), so you may treat the VAT as non-deductible |
| Mobile phones provided to employees | Phone and line rental VAT is input tax even with private use; calls fully only if private use is insignificant and controlled, otherwise apportion |
| Costs of exempt supplies | Not recoverable, subject to partial exemption de minimis |
| Margin scheme purchases; going concern assets; VAT charged in error | Not input tax |

### Reverse charge ([VAT Notice 741A](https://www.gov.uk/guidance/vat-place-of-supply-of-services-notice-741a); [construction reverse charge](https://www.gov.uk/guidance/vat-domestic-reverse-charge-for-building-and-construction-services); [technical guide](https://www.gov.uk/guidance/vat-reverse-charge-technical-guide))

**Services bought from overseas suppliers.** The reverse charge applies where the place of supply is the UK, the supplier belongs outside the UK (EU and non-EU alike, even if it has a UK VAT number), you belong in the UK, and the supply is not exempt. It covers almost all B2B general rule services such as software, advertising and consultancy. Enter output tax in box 1, input tax in box 4, and the full value in box 6 and box 7. A fully taxable business has no net cost; a partly exempt business may bear the VAT.

**Services you sell to overseas business customers.** B2B general rule services are supplied where the customer belongs: outside the scope of UK VAT (not zero-rated). Box 6 only; keep evidence the customer is in business abroad. B2C services generally carry UK VAT, with exceptions.

**Construction (CIS domestic reverse charge).**

| Condition | Rule |
| --- | --- |
| Services covered | Standard and reduced-rated construction services reported within CIS (building, alteration, repair, demolition, installing heating, lighting, drainage and similar systems, painting and decorating, site preparation and completion) |
| Parties | Supplier and customer both VAT registered and CIS registered |
| Not covered | Zero-rated work (for example most new-build housing); customers who are end users or intermediary suppliers and confirm this in writing; stand-alone services of architects and surveyors; making or delivering materials; installing security systems |
| 5% disregard | If the reverse charge element of a single supply is 5% or less of its value it can be disregarded, but only where supplier and customer agree, from the start of the contract, that it applies on the basis of the overall contract values. It does not apply where there is a single supply and the predominant element is zero-rated (for example a new-build block of flats with a small commercial element) |
| Supplier's return | Value in box 6 only; invoice states that the customer must account to HMRC for the VAT |
| Customer's return | VAT in box 1 and box 4; value in box 7 only (not box 6) |
| Schemes | Cannot use cash accounting for reverse charge supplies. Flat Rate Scheme users account for reverse charge purchases outside the flat rate and exclude reverse charge sales from flat rate turnover |

### Partial exemption, summary only ([VAT Notice 706](https://www.gov.uk/guidance/partial-exemption-vat-notice-706))

- If you make both taxable and exempt supplies, input tax directly attributable to exempt supplies, plus the exempt share of residual (overhead) input tax, is normally not recoverable. The standard method apportions residual input tax by the value of supplies; a special method needs HMRC approval.
- De minimis: you can treat yourself as fully taxable for a period if exempt input tax is **both** not more than £625 per month on average **and** not more than half of total input tax. Blocked input tax is left out of "total input tax".
- HMRC's simplified Test One and Test Two (each using £625 a month and exempt supplies not more than 50% of all supplies) allow provisional recovery, with a year-end review.
- An annual adjustment is made at the end of each longer period (usually the partial exemption year). Refer anyone who fails the de minimis tests.

## Boundary and exception table ([Register for VAT](https://www.gov.uk/register-for-vat); [VAT Notice 733](https://www.gov.uk/guidance/flat-rate-scheme-for-small-businesses-vat-notice-733--2); [VAT Notice 700/45](https://www.gov.uk/guidance/how-to-correct-vat-errors-and-make-adjustments-or-claims-vat-notice-70045); [late payment penalties](https://www.gov.uk/guidance/how-late-payment-penalties-work-if-you-pay-vat-late))

| Situation | Outcome |
| --- | --- |
| Rolling 12-month taxable turnover exactly £90,000 | Not over the threshold; no duty to register yet |
| Next 12 months expected at exactly £88,000 | Voluntary deregistration possible ("will not exceed") |
| FRS relevant goods exactly 2% of flat rate turnover, or exactly £250 in a quarter | HMRC's wording ("less than 2%", "more than 2% but less than £1,000") does not cover exact equality; check with HMRC before relying on the sector rate |
| FRS income on anniversary exactly £230,000 | Not "more than £230,000"; may stay |
| Net earlier-period error exactly £10,000 | Correct on the current return (method 1) |
| Payment 15 days overdue | Interest only; the first penalty starts at 16 days |
| Exempt input tax exactly £625 a month on average, and no more than half of input tax | De minimis ("not more than") |
| CIS reverse charge element exactly 5% of a single supply | Can be disregarded, if both parties agreed from the start of the contract on the basis of overall contract values, and the predominant element is not zero-rated |

## Worked cases ([VAT Notice 700/12](https://www.gov.uk/guidance/how-to-fill-in-and-submit-your-vat-return-vat-notice-70012); [VAT Notice 733](https://www.gov.uk/guidance/flat-rate-scheme-for-small-businesses-vat-notice-733--2); [VAT Notice 741A](https://www.gov.uk/guidance/vat-place-of-supply-of-services-notice-741a); [late payment penalties](https://www.gov.uk/guidance/how-late-payment-penalties-work-if-you-pay-vat-late); [VAT Notice 700/45](https://www.gov.uk/guidance/how-to-correct-vat-errors-and-make-adjustments-or-claims-vat-notice-70045); [Register for VAT](https://www.gov.uk/register-for-vat))

**Case 1: registration timing.** A freelance designer checks at the end of each month. Taxable turnover for the 12 months to 31 May 2026 is £91,200. That is more than £90,000, so she must register by 30 June 2026 (30 days after the end of May). Her effective date of registration is 1 July 2026, the first day of the second month after she went over. Had the 12-month figure been exactly £90,000, she would not yet be liable.

**Case 2: Flat Rate Scheme, limited cost test (quarterly).** An IT consultant, registered for more than a year, has flat rate turnover of £30,000 for the quarter (£25,000 of fees plus £5,000 VAT charged). Relevant goods bought: £400 including VAT. 2% of £30,000 is £600. £400 is less than £600, so he is a limited cost business: VAT due is £30,000 x 16.5% = £4,950, compared with £5,000 of output VAT he charged. If he had bought £700 of relevant goods (more than £600 and more than £250), the IT consultancy rate of 14.5% would apply: £30,000 x 14.5% = £4,350. In both cases box 6 is £30,000 (VAT-inclusive), not £25,000.

**Case 3: reverse charges.** A UK consultant pays a US software company £1,000 with no VAT. She enters £200 in box 1 and £200 in box 4, and £1,000 in both box 6 and box 7. Separately, a VAT and CIS registered plastering subcontractor invoices a building contractor £10,000 for work on a commercial refurbishment. The subcontractor enters £10,000 in box 6 and no output VAT. The contractor enters £2,000 in box 1, £2,000 in box 4 and £10,000 in box 7, but nothing in box 6.

**Case 4: late payment (HMRC's own example).** A return is filed on time but £15,000 of VAT is paid 51 days late. First late payment penalty: 3% of £15,000 at day 15 (£450) plus 3% of £15,000 at day 30 (£450) = £900. Second late payment penalty: £15,000 x 10% x 21 ÷ 365 days = £86.30 (day 31 to day 51). Total penalties £986.30. Late payment interest is charged in addition, from the day after the due date until payment, at base rate plus 4%.

**Case 5: correcting an earlier error.** A business finds it under-declared output VAT by a net £12,000 in an earlier quarter. Box 6 for the current return is £1,500,000, so 1% is £15,000. £12,000 is between £10,000 and £50,000 and not more than £15,000, so it can be corrected in box 1 of the current return (method 1). If the current box 6 were £900,000, 1% would be £9,000; the error would exceed it, so the business must notify HMRC separately (method 2).
## When to refuse or refer

- Partial exemption beyond de minimis, a special method, or an annual adjustment: refer to a qualified adviser.
- Transfer of a business as a going concern, VAT groups, divisional registration.
- Margin schemes for second-hand goods and the Tour Operators' Margin Scheme; retail schemes.
- Northern Ireland businesses moving goods to or from the EU (boxes 2, 8 and 9, acquisitions, dispatches).
- Construction reverse charge cases where end-user or intermediary status, zero-rated new-build work or mixed supplies are unclear.
- Land and buildings: option to tax, commercial property, and the Capital Goods Scheme. From 29 July 2026 the scheme no longer covers computers, and land and buildings are capital items only from £600,000 (previously £250,000) of VAT-bearing expenditure; the same £600,000 test applies to civil engineering works. These changes do not apply to a capital item if the owner incurred any relevant expenditure on it (goods or services supplied, goods imported or acquired) before 29 July 2026, so existing items stay in the scheme ([SI 2026/765](https://www.legislation.gov.uk/uksi/2026/765/made)).
- B2C services to overseas customers, digital services to consumers, and imports needing customs advice.
- Deliberate errors, HMRC investigations, penalty appeals, insolvency, or long-overdue registration.

## Filing and payment

### Deadlines and payment ([VAT Return deadlines](https://www.gov.uk/vat-returns/deadlines); [VAT Notice 700/12](https://www.gov.uk/guidance/how-to-fill-in-and-submit-your-vat-return-vat-notice-70012); [annual accounting deadlines](https://www.gov.uk/vat-annual-accounting-scheme/return-and-payment-deadlines))

- Returns are usually quarterly. You can ask for monthly returns if you normally reclaim; HMRC can require them.
- Submit and pay by 1 calendar month and 7 days after the end of the period. Payment must reach HMRC's account by then, even if the deadline falls on a weekend or bank holiday.
- A return is required even if there is nothing to pay or reclaim. Annual accounting: 2 months after the year end.

### Late submission penalty points ([penalty points](https://www.gov.uk/guidance/penalty-points-and-penalties-if-you-submit-your-vat-return-late); [removing points](https://www.gov.uk/guidance/remove-penalty-points-youve-received-after-submitting-your-vat-return-late))

- Applies to periods starting on or after 1 January 2023, including nil and repayment returns.
- One point per late return until the threshold: annual 2, quarterly 4, monthly 5. At the threshold, a £200 penalty for that return and for each further late return.
- Below the threshold, each point expires on the last day of the month 24 months after the month of the missed deadline (25 months if the deadline was the last day of a month).
- At the threshold, points reset only when both conditions are met: a period of compliance (annual 24 months, quarterly 12 months, monthly 6 months, all returns on time) and all returns due in the previous 24 months submitted.
- Not covered: the first return after registering, the final return, and one-off returns of non-standard length.

### Late payment penalties and interest ([late payment penalties](https://www.gov.uk/guidance/how-late-payment-penalties-work-if-you-pay-vat-late); [late payment interest](https://www.gov.uk/guidance/late-payment-interest-if-you-do-not-pay-vat-or-penalties-on-time); [HMRC interest rates](https://www.gov.uk/government/publications/rates-and-allowances-hmrc-interest-rates-for-late-and-early-payments/rates-and-allowances-hmrc-interest-rates))

| Days overdue | Penalty |
| --- | --- |
| 1 to 15 | None |
| 16 to 30 | First penalty: 3% of the VAT outstanding at day 15 |
| 31 or more | First penalty: 3% of the amount outstanding at day 15 plus 3% of the amount outstanding at day 30; second penalty: a daily rate of 10% a year on the outstanding balance from day 31 until paid |

- Penalties apply to VAT on returns, amendments and assessments, but not to payments on account or annual accounting instalments.
- Asking for Time to Pay by day 15 (or day 30) avoids the next stage; breaking it can reinstate penalties.
- Late payment interest runs from the first day overdue until paid, at Bank of England base rate plus 4% (from 6 April 2025; previously plus 2.5%). HMRC's table shows 7.75% from 9 January 2026; check the table for any later change. Interest also runs on unpaid penalties. You cannot appeal interest, only object in limited cases.
- Penalties can be cancelled for a reasonable excuse; ask for a review or appeal to the tax tribunal.

### Correcting errors ([VAT Notice 700/45](https://www.gov.uk/guidance/how-to-correct-vat-errors-and-make-adjustments-or-claims-vat-notice-70045))

- Method 1 (adjust on the current return, boxes 1 and 4): net value of errors not more than £10,000, or between £10,000 and £50,000 but not more than 1% of box 6 for the return in which you discover the errors.
- Method 2 (separate error correction notification to HMRC): net errors between £10,000 and £50,000 that are more than 1% of box 6, net errors over £50,000, or any deliberate error. You may use method 2 for any error.
- Time limit: 4 years from the end of the period in which the error occurred (output tax and over-claimed input tax), or from the due date of that period's return (under-claimed input tax).
- Careless or deliberate errors can be penalised; disclosure before HMRC find out reduces the penalty.

### Bad debt relief ([VAT Notice 700/18](https://www.gov.uk/guidance/relief-from-vat-on-bad-debts-notice-70018))

- Conditions: you accounted for and paid the output VAT; the debt is written off in your VAT accounts and moved to a separate bad debt account; the price was not more than the customary selling price; the debt has not been sold or factored; and it has been unpaid for 6 months after the later of the payment due date and the date of supply.
- Claim in box 4 of the return covering the date the conditions are met, within 4 years and 6 months of the later of the due date and the supply date. Repay the relief if the customer later pays.
- A customer who has not paid a supplier within 6 months of the relevant date must repay the input tax it claimed.

## Returns for 2025/26 periods ([VAT Notice 700/1 supplement](https://www.gov.uk/government/publications/vat-notice-7001-should-i-be-registered-for-vat/vat-notice-7001-supplement--2); [HMRC interest rates](https://www.gov.uk/government/publications/rates-and-allowances-hmrc-interest-rates-for-late-and-early-payments/rates-and-allowances-hmrc-interest-rates))

- Thresholds were the same for 1 April 2025 to 31 March 2026: registration £90,000, deregistration £88,000.
- HMRC's guidance says the value of late payment penalties has been increased but does not say from which date, so for an older period check the rate that applied with HMRC before relying on the rates above. Interest has been at base rate plus 4% since 6 April 2025. For interest on 2025/26 payments, use the dated rates in HMRC's table (the rate changed several times).

## Completion checklist ([VAT Notice 700/12](https://www.gov.uk/guidance/how-to-fill-in-and-submit-your-vat-return-vat-notice-70012))

- Registration position checked on both the 12-month and 30-day tests; effective date confirmed.
- Period dates, return frequency and schemes confirmed; Flat Rate limited cost test run for this period.
- Every sale classified, using the temporary 2026 rates for the dates they apply.
- Purchases backed by valid invoices; blocked items excluded; mixed use apportioned.
- Reverse charges for overseas services (boxes 1, 4, 6, 7) and CIS construction (boxes 1, 4, 7) entered.
- Partial exemption de minimis tested if any exempt income.
- Boxes 2, 8 and 9 zero unless Northern Ireland goods trade with the EU; box 3 and box 5 arithmetic checked; box 1 roughly 20% of box 6 where all sales are standard-rated.
- Bad debt relief and earlier-period errors within the method 1 limit included; larger errors notified separately.
- Filed through Making Tax Digital software with digital links only.
- Submitted and paid, with cleared funds, by 1 month and 7 days after the period end.

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
