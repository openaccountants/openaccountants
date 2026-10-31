---
name: new-jersey-sales-tax
description: Use this skill whenever asked about New Jersey sales and use tax. Trigger on phrases like "New Jersey sales tax", "NJ sales tax", "NJ Division of Taxation", "UEZ", "NJ clothing exemption". ALWAYS load us-sales-tax first.
jurisdiction: US-NJ
tax_year: 2026
last_updated: 2026-10-16
authored_by: Michael Cutajar and the OpenAccountants team
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# New Jersey Sales and Use Tax

This skill covers New Jersey Sales and Use Tax for sellers and buyers: the rate, the Urban Enterprise Zone and Salem County reduced rates, what is taxable, the main exemptions, registration, remote sellers and marketplaces, returns and due dates, Use Tax and exemption certificates. Figures are for tax year 2026. Read `us-sales-tax` first for the multi-state framework. Every figure below sits in a table that links the New Jersey Division of Taxation page that prints it.

## Section 1 -- Quick reference

| Item | Value | Note (verbatim from the page) |
| --- | --- | --- |
| Source | all figures below | https://www.nj.gov/treasury/taxation/businesses/salestax/index.shtml |
| State Sales Tax rate | 6.625% | "New Jersey assesses a 6.625% Sales Tax on sales of most tangible personal property, specified digital products, and certain services unless specifically exempt under New Jersey law." |

| Item | Value | Note (verbatim from the page) |
| --- | --- | --- |
| Source | all figures below | https://www.nj.gov/treasury/taxation/businesses/salestax/uez-over.shtml |
| Urban Enterprise Zone reduced rate (certified sellers only) | 3.3125% | "The current Sales Tax rate in UEZs is 3.3125%" |

Other quick facts, each proven in the sections below:

- Tax authority: New Jersey Division of Taxation, https://www.nj.gov/treasury/taxation/
- Local sales taxes: the Division's pages describe one State rate. The only reduced rates they describe are the Urban Enterprise Zone rate and the Salem County rate (Section 2).
- Streamlined Sales Tax: New Jersey is a full member of the Streamlined Sales and Use Tax Governing Board, per https://www.nj.gov/treasury/taxation/remotesellers.shtml
- Clothing: most clothing and footwear is exempt, but not all (Section 3).

## Section 2 -- Reduced rates: Urban Enterprise Zones and Salem County

**Urban Enterprise Zones (UEZ).** The Division's UEZ page (https://www.nj.gov/treasury/taxation/businesses/salestax/uez-over.shtml ) says certified sellers may apply "a partial Sales Tax exemption to most taxable sales of tangible personal property that occur in the UEZ" and that the exemption "allows businesses to charge half the State Sales Tax rate on exempt sales". The rate is in the table in Section 1. The reduced rate is not open to every business in a zone:

- WHO: only a business that the Urban Enterprise Zone Authority has certified. The S&U-4 Sales Tax Guide (https://www.nj.gov/treasury/taxation/pdf/pubs/sales/su4.pdf) says qualified businesses "that have a UZ-2 certificate may charge Sales Tax at half of the regular rate on sales of tangible personal property qualified for the reduced rate".
- WHAT: tangible personal property only. Services are not covered by the reduced rate on that page.
- WHERE (both tests in S&U-4): the purchaser places the order in person at the seller's place of business in the zone, AND either the purchaser accepts delivery at that place of business OR the seller delivers from its business location in the zone, "not from another location".
- Certification: the business applies online through the UEZ Business Certification System, files an annual report, and applies for recertification every three years (UEZ page).
- Returns: UEZ businesses "must file the UEZ Sales and Use Tax return, UZ-50, monthly, by the 20th day of the following month", moved to the next business day when the due date falls on a weekend or holiday (UEZ page).
- Qualified UEZ businesses may also buy "items (except motor vehicles and energy) and most services (except telecommunications and utility services) without paying Sales Tax" (UEZ page). Purchase limitations apply; see the UEZ notices.

**Salem County.** S&U-4 (revision dated 07/22, https://www.nj.gov/treasury/taxation/pdf/pubs/sales/su4.pdf ) says "Certain sales made by businesses located in Salem County are subject to Sales Tax at half of the regular rate." It applies solely to retail sales of tangible personal property made in person from a place of business regularly operated by the seller for retail sales, with delivery at the seller's Salem County place of business or from the seller's Salem County location. Not eligible: motor vehicles; alcoholic beverages; cigarettes; mail-order, catalog or internet sales; sales of services; prepared food, meals and beverages; and other listed items. No current Division web page on Salem County was found; confirm the programme is still running before applying it (see Section 9).

## Section 3 -- What is taxable, and the main exemptions

Per S&U-4 (https://www.nj.gov/treasury/taxation/pdf/pubs/sales/su4.pdf), the Sales and Use Tax Act "imposes a tax on the receipts from every retail sale of tangible personal property, specified digital products, and the sale of certain services, except as otherwise provided in the Act." Tangible personal property "can include prewritten computer software delivered electronically." Most services performed on tangible personal property and specified digital products are taxable unless specifically exempted.

| Pattern | Treatment | Condition or limit (S&U-4 unless stated; S&U-6 is linked in Section 6) |
| --- | --- | --- |
| General tangible personal property | Taxable | Unless a specific exemption applies |
| Clothing and footwear for human use | Exempt | Not "fur clothing; accessories or equipment; sport or recreational equipment, or protective equipment (unless the protective equipment is necessary for the daily work of the user)". Those items are taxable; work-required protective equipment stays exempt. |
| Grocery food | Exempt | "most food sold as grocery items" |
| Prepared food (heated, combined by the seller, or sold with utensils) | Taxable | Includes beverages |
| Prescription drugs and over-the-counter drugs (for human use) | Exempt | OTC drugs only "if there is a label identifying the product as a drug, such as a 'Drug Facts' panel or a statement of active ingredients" (S&U-4) |
| Disposable paper products for household use | Exempt | Listed among exempt items |
| Specified digital products (digital audio-visual works, digital audio works, digital books) transferred electronically | Taxable | When billed to a New Jersey address. Products streamed or accessed but not delivered electronically are not taxable. |
| Prewritten computer software delivered electronically | Taxable when "Sold to individuals" (S&U-4) | Exempt per S&U-6 when "used directly and exclusively in the conduct of the purchaser's business, trade, or occupation". "This exemption does not apply to software delivered by the 'load and leave' method or to the purchase of software-related services." |
| Software accessed remotely (SaaS) | Not settled here | The live Guide said taxable. No saved page settles it; see Section 9 |
| Purchases for resale | Exempt | With a Resale Certificate, Form ST-3 (Section 6) |
| Professional services (doctor, lawyer, accountant) | Exempt | S&U-4 services list: "Professional Services (doctor, lawyer, etc.) ... E"; "Accounting Services: Professional Services ... E" |
| Production machinery and equipment | Exempt | S&U-6: "used directly and primarily in the production of goods by manufacturing, assembling, processing, and refining are exempt"; also "parts with a useful life of more than one year". Not "supplies or ... tools that are simple, hand-held, manually operated instruments". Claimed on Form ST-4. |

## Section 4 -- Registration, remote sellers and marketplaces

**Registration.** Any person or organisation engaged in business in New Jersey must file a Business Registration Application, Form NJ-REG, "at least 15 business days before starting business or opening an additional place of business in this State" (S&U-4, https://www.nj.gov/treasury/taxation/pdf/pubs/sales/su4.pdf). Seasonal or occasional sellers at events such as flea markets or craft shows must also register (https://www.nj.gov/treasury/taxation/su_12.shtml).

| Item | Value | Note (verbatim from the page) |
| --- | --- | --- |
| Source | all figures below | https://www.nj.gov/treasury/taxation/remotesellers.shtml |
| Remote seller gross revenue threshold | USD 100,000 | "exceeds $100,000" (gross revenue from sales delivered into New Jersey during the current or prior calendar year) |
| Maximum delay a marketplace facilitator may request | 180 days | "for a period not to exceed 180 days with a written request" |

**Remote sellers.** For sales on and after November 1, 2018, a remote seller must register, collect and remit if it meets EITHER test, measured over the current OR prior calendar year: gross revenue from sales of tangible personal property, specified digital products or taxable services delivered into New Jersey that is MORE THAN the amount in the table above (exceeds, not equals); OR 200 or more separate transactions delivered into New Jersey. The transaction test still appears on the page (last updated 04/24/25). A remote seller that meets neither test does not have to register.

**Marketplaces.** The marketplace facilitator must collect and remit on all marketplace transactions, "regardless of whether the marketplace seller is above or below either of the economic thresholds." A remote seller over the threshold that sells only through marketplaces must still register, but may ask to be placed on a non-reporting basis by mailing Form C-6205-ST to the Division of Revenue and Enterprise Services. Remote sellers may register through the Division of Revenue and Enterprise Services ("Register as Remote Seller Only") or through the Streamlined Sales Tax Registration System. Guidance: Technical Bulletin TB-83.

## Section 5 -- Returns, payments and due dates

| Item | Value | Note (verbatim from the page) |
| --- | --- | --- |
| Source | all figures below | https://www.nj.gov/treasury/taxation/su_12.shtml |
| Prior-year collections that trigger monthly payments | USD 30,000 | "Collected more than $30,000 in Sales and Use Tax in New Jersey during the prior calendar year; and" |
| Collections in month 1 or 2 of the quarter that trigger a monthly payment | USD 500 | "Collected more than $500 in the first and/or second month of the current calendar quarter." |

- Every registered seller files a quarterly return, Form ST-50, for each quarter, even if no tax is due and no sales were made.
- Monthly payments apply only if BOTH conditions in the table hold (AND, and both are "more than"). They are made with "Form Type: Monthly Voucher" in the New Jersey Tax Portal. The page no longer names Form ST-51 for this; a Monthly Voucher is payment only and cannot be filed for zero.
- A seller that collected the prior-year amount or less makes no payment for the first or second month, "no matter how much tax is due for that particular month."
- Due date: on or before the 20th day of the month after the end of the filing period (quarterly ST-50 due April 20, July 20, October 20 and January 20; monthly vouchers due the 20th of the following month). A weekend or legal holiday moves it to the next business day.
- Filing and payment are electronic, through the New Jersey Tax Portal (e-check, electronic funds transfer, or credit card with fees).
- Errors on a monthly payment may be corrected on the ST-50 only if found in the same calendar quarter; after that, file an amended return (S&U-4).

## Section 6 -- Exemption certificates

Per S&U-4 (https://www.nj.gov/treasury/taxation/pdf/pubs/sales/su4.pdf):

- The most common certificates are the Resale Certificate (Form ST-3), the Exempt Use Certificate (Form ST-4) and the Exempt Organization Certificate (Form ST-5). The Streamlined certificate, Form ST-SST, is also accepted.
- The seller accepting a certificate must be registered with New Jersey, and should accept it only if fully completed.
- When the purchaser completes and gives the certificate, the seller is relieved of collecting the tax, even if the purchaser later proves not to be eligible.
- One certificate covers later purchases of the same general type. Keep it for at least four years from the date of the last purchase it covers.
- Fuller rules: S&U-6, https://www.nj.gov/treasury/taxation/pdf/pubs/sales/su6.pdf

| Item | Value | Note (verbatim from the page) |
| --- | --- | --- |
| Source | all figures below | https://www.nj.gov/treasury/taxation/pdf/pubs/sales/su4.pdf |
| Government sale at or below which an ST-4 may replace a purchase order | USD 150 | "When the amount of the transaction is $150 or less, a fully completed Exempt Use Certificate (Form ST‑4) form can be issued instead; and" ... "Payment must be made by the agency’s check or voucher or with a GSA SmartPay 2 credit card that has 0, 6, 7, 8, or 9 as the sixth digit" |
| Use Tax rate (same as Sales Tax) | 6.625% | "The Use Tax rate is the same as the Sales Tax rate, which is 6.625%." |

## Section 7 -- Use Tax

The Use Tax FAQ (https://www.nj.gov/treasury/taxation/su_10.shtml ) says a New Jersey resident or business owes Use Tax on a taxable item or service bought outside New Jersey if no sales tax of any kind was paid, OR sales tax was paid to another jurisdiction at a lower rate. In the second case only the difference is due. S&U-4 adds that no credit is allowed for sales tax paid to a foreign country. The rate is in the table above.

| Item | Value | Note (verbatim from the page) |
| --- | --- | --- |
| Source | all figures below | https://www.nj.gov/treasury/taxation/su_10.shtml |
| Average annual Use Tax ceiling for Form ST-18B | USD 2,000 | "Averaged less than $2,000 in annual Use Tax liability in the last three years; and" |

- Businesses may use Form ST-18B only if ALL three hold: they did not sell taxable goods or services or lease taxable property in the tax year; their average annual Use Tax was less than the amount above over the last three years; and they owe Use Tax for the current year. Otherwise they must register for quarterly or monthly Sales Tax filing.
- Individuals report Use Tax on Form NJ-1040, or with Form ST-18.

## Section 8 -- Penalties and interest

The Division's penalties page is linked from the Sales and Use Tax filing information page; it is written for income tax filers, so confirm it applies to the return in question.

| Item | Value | Note (verbatim from the page) |
| --- | --- | --- |
| Source | all figures below | https://www.nj.gov/treasury/taxation/njit19.shtml |
| Late filing penalty, per month or part month | 5% | "The Late Filing Penalty is 5% of the tax due for each month (or part of a month) the return is late." |
| Late filing penalty cap | 25% | "The maximum penalty for late filing is 25% of the balance due." |
| Additional late filing charge per month | USD 100 | "We also may charge $100 for each month the return is late." |
| Late payment penalty | 5% | "Late Payment Penalty of 5% of the tax due." |

Interest runs for every month or part month the tax is unpaid at the prime rate plus three points, compounded annually (same page; see Technical Bulletin TB-21(R)). Penalties may be abated for reasonable cause.

## The method, step by step

1. Decide whether the seller must collect. A business in New Jersey registers on Form NJ-REG at least 15 business days before starting (S&U-4, https://www.nj.gov/treasury/taxation/pdf/pubs/sales/su4.pdf). A remote seller applies the revenue OR transaction test in Section 4 (https://www.nj.gov/treasury/taxation/remotesellers.shtml).
2. Take marketplace sales out. The marketplace facilitator collects on them whatever the seller's size (https://www.nj.gov/treasury/taxation/remotesellers.shtml).
3. Classify each item with S&U-4 and Section 3 (https://www.nj.gov/treasury/taxation/pdf/pubs/sales/su4.pdf). Check the clothing carve-outs and the digital product rules.
4. Check for a valid exemption certificate, ST-3, ST-4, ST-5 or ST-SST, fully completed (https://www.nj.gov/treasury/taxation/pdf/pubs/sales/su6.pdf).
5. Pick the rate: the State rate, or the UEZ rate only for a certified seller meeting all the in-person and delivery tests (https://www.nj.gov/treasury/taxation/businesses/salestax/uez-over.shtml). Salem County only after confirming the programme is current.
6. Calculate tax to the third decimal and round half a cent or more up, or use the Form ST-75 bracket (https://www.nj.gov/treasury/taxation/ratechange/su-calculatingthetax.shtml).
7. File the quarterly ST-50 and any Monthly Vouchers by the 20th through the New Jersey Tax Portal (https://www.nj.gov/treasury/taxation/su_12.shtml). UEZ sellers file UZ-50 monthly.
8. For purchases, assess Use Tax where no or lower sales tax was paid (https://www.nj.gov/treasury/taxation/su_10.shtml).

## Ask the client first

- Do you have any physical presence in New Jersey (office, staff, inventory)?
- If remote: what were your gross sales and number of transactions delivered into New Jersey this year and last year?
- Do you sell through a marketplace, directly, or both?
- What exactly do you sell: goods, clothing (including fur, sport or protective items), food, digital products, software (downloaded or accessed remotely), services?
- Are you a certified UEZ business, or located in Salem County, and do your sales meet the in-person and delivery tests?
- How much New Jersey Sales Tax did you collect last calendar year?

## When to refuse or refer

- SaaS or remote software access, information services, or bundled digital offerings: refer, because no saved page here settles them.
- Salem County reduced rate claims: refer until a current Division page confirms the programme.
- UEZ certification, recertification, purchase limitations or energy exemptions for UEZ manufacturers: refer to the Department of Community Affairs and the UEZ notices.
- Audits, assessments, voluntary disclosure or penalty abatement requests: refer to a New Jersey practitioner.
- Hotel occupancy, motor vehicle, alcohol and cigarette taxes and fees: outside this skill.

## Section 10 -- Prohibitions

- Never treat all clothing as exempt. Fur clothing, accessories or equipment, and sport or recreational equipment are taxable. Protective equipment is taxable unless it "is necessary for the daily work of the user" (S&U-4).
- Never apply the UEZ reduced rate to a seller without a UZ-2 certificate, to services, or to sales that fail the in-person and delivery tests.
- Never compute a number outside the method above; use the published rate and the rounding rule.

## Sources

- Sales and Use Tax: https://www.nj.gov/treasury/taxation/businesses/salestax/index.shtml
- Urban Enterprise Zone: https://www.nj.gov/treasury/taxation/businesses/salestax/uez-over.shtml
- Remote Sellers: https://www.nj.gov/treasury/taxation/remotesellers.shtml
- Filing and Remitting Sales and Use Tax: https://www.nj.gov/treasury/taxation/su_12.shtml
- New Jersey Sales Tax Guide S&U-4: https://www.nj.gov/treasury/taxation/pdf/pubs/sales/su4.pdf
- Sales Tax Exemption Administration S&U-6: https://www.nj.gov/treasury/taxation/pdf/pubs/sales/su6.pdf
- Use Tax FAQ: https://www.nj.gov/treasury/taxation/su_10.shtml
- Calculating the Tax: https://www.nj.gov/treasury/taxation/ratechange/su-calculatingthetax.shtml
- Penalties, Interest, and Collection Fees: https://www.nj.gov/treasury/taxation/njit19.shtml

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

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
