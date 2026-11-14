---
name: illinois-sales-tax
description: "Illinois sales and use tax for 2026 on Form ST-1. Covers the Retailers' Occupation Tax and Use Tax, the Service Occupation Tax and Service Use Tax, the 6.25% State rate on general merchandise and 1% on drugs and medical appliances, the end of the State grocery tax on 1 January 2026 and the local 1% grocery tax, origin and destination sourcing, the 15% rate for undocumented destination sales, the $100,000 remote seller threshold with no transaction test from 2026, the four ways to compute Service Occupation Tax, resale certificates, filing frequency, the 1.75% retailers' discount capped at $1,000 a month, penalties and interest. Trigger on \"Illinois sales tax\", \"IL sales tax\", \"ROT\", \"Retailers Occupation Tax\", \"IDOR sales tax\", \"ST-1\", \"Illinois use tax\", \"Service Occupation Tax\", \"CRT-61\", \"Illinois grocery tax\", \"Illinois remote seller\"."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/illinois-sales-tax"
  jurisdiction: "US-IL"
  tax_year: "2026"
  last_updated: "2026-11-13"
---

# Illinois sales and use tax, 2026: rates, sourcing, remote sellers, service occupation tax and Form ST-1

> **Source-cited draft.** Built from the IDOR Form ST-1 instructions, the IDOR Retailers' Occupation Tax page, PIO-115, Informational Bulletins FY 2026-03, FY 2026-12 and FY 2026-13, Publication 103 and the IDOR interest rate page, read on 2026-11-13. No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before filing.

**Answer first.** Illinois "sales tax" is two pairs of taxes collected on one return, Form ST-1: the Retailers' Occupation Tax (ROT) with the Use Tax, and the Service Occupation Tax (SOT) with the Service Use Tax. The State rate is **6.25%** on general merchandise and **1%** on qualifying drugs and medical appliances; local taxes are added by address. From **1 January 2026** the State 1% tax on groceries ended; a local grocery tax of exactly 1% applies in the RTA and Metro-East areas and wherever a municipality or county has adopted one. A remote seller must collect once it has **$100,000** of Illinois sales of goods in the preceding 12 months; the 200-transaction test ended on 1 January 2026. Returns are due by the **20th** of the month after the period, and the **1.75%** retailers' discount (at least $5 a year, at most **$1,000 a month**) is lost if the return or payment is late.

## Scope and who this is for

In scope: retailers selling tangible personal property in Illinois or to Illinois customers, remote retailers and marketplace facilitators deciding whether to register, servicepersons that transfer goods with a service, businesses that owe Use Tax on their own purchases, and sellers and buyers using resale certificates, for 2026 periods and the 2025 periods still open.

Out of scope, and where it goes:

| Topic | Skill |
| --- | --- |
| Sales tax nexus across all states | `us-sales-tax-nexus-50-state-matrix` |
| General US sales tax concepts | `us-sales-tax` |
| Vehicles, watercraft, aircraft, trailers and mobile homes (Forms ST-556, RUT-25, RUT-50, RUT-75) | refer |
| Motor fuel and prepaid sales tax on fuel, aviation fuel (Form ST-70) | refer |
| Prepaid Wireless E911 Surcharge and ITAC Assessment (ST-1 Schedule F) | refer |
| Automobile renting, hotel operators', telecommunications and cannabis taxes | refer |
| Taxes cities and counties collect themselves (for example Chicago's own taxes) | refer to the city or county |

## Ask the client first

1. **Physical presence in Illinois**: office, warehouse, inventory, employees, agents, own delivery vehicles?
2. **If outside Illinois**: gross receipts from sales of goods to Illinois purchasers in each 12-month period ending 31 March, 30 June, 30 September and 31 December. Did it register only because of the old 200-transaction test?
3. **Marketplaces**: does a facilitator that meets the threshold collect for it, and is any inventory in a facilitator's Illinois warehouse used for its own orders too?
4. **Each sale's fulfilment**: from Illinois inventory or from outside Illinois, and the delivery address.
5. **What it sells**: general merchandise, groceries, candy or soft drinks, food prepared for immediate consumption, drugs or medical appliances, or services with parts. Does it provide seating?
6. **Servicepersons**: are parts separately stated? What is the annual cost ratio (cost of goods transferred / total service income)?
7. **Filing frequency** IDOR has assigned, and any quarter-monthly or electronic payment notice.
8. **Resale certificates or exemption numbers** on file for every untaxed sale.
9. **Late returns or payments, or an open audit.**

## The method, step by step

### Rates, bands and thresholds

| Item | Amount, 2026 | Source |
| --- | --- | --- |
| State rate, general merchandise (high rate), plus local taxes | 6.25% | [IDOR PIO-115](https://tax.illinois.gov/research/publications/pio-115.html) |
| State rate, qualifying drugs, medicines and medical appliances (low rate), plus local taxes | 1% | [IDOR PIO-115](https://tax.illinois.gov/research/publications/pio-115.html) |
| State tax on groceries from 1 January 2026 | none (State 1% eliminated by Public Act 103-0781) | [IDOR Bulletin FY 2026-03](https://tax.illinois.gov/research/publications/bulletins/fy-2026-03.html) |
| Local grocery tax a municipality or county may impose by ordinance; RTA and MED local grocery tax continues | exactly 1% | [IDOR Bulletin FY 2026-03](https://tax.illinois.gov/research/publications/bulletins/fy-2026-03.html) |
| Remote retailer and marketplace facilitator threshold: cumulative gross receipts from sales of goods to Illinois purchasers, 12-month lookback | $100,000 or more | [IDOR Bulletin FY 2026-12](https://tax.illinois.gov/research/publications/bulletins/fy-2026-12.html) |
| Transaction-count test for lookback periods after 31 December 2025 | none (200-transaction test removed by Public Act 104-0006) | [IDOR Bulletin FY 2026-12](https://tax.illinois.gov/research/publications/bulletins/fy-2026-12.html) |
| Rate on destination sales whose location the seller cannot show, from 1 January 2026 | 15% | [Form ST-1 instructions](https://tax.illinois.gov/forms/sales/salesandusetax/st-1-instructions.html) |
| Services threshold for remote servicepersons and service marketplaces | $100,000 in gross receipts from sales of service | [IDOR Bulletin FY 2026-13](https://tax.illinois.gov/research/publications/bulletins/fy-2026-13.html) |
| Retailers' discount: share of tax due, or $5 a calendar year if greater, return and payment on time | 1.75% | [Form ST-1 instructions](https://tax.illinois.gov/forms/sales/salesandusetax/st-1-instructions.html) |
| Retailers' discount cap, returns due on or after 1 January 2025 | $1,000 a month | [Form ST-1 instructions](https://tax.illinois.gov/forms/sales/salesandusetax/st-1-instructions.html) |
| Filing frequency IDOR may assign, by average monthly liability | over $200 monthly; $50 to $200 quarterly; under $50 annual | [Form ST-1 instructions](https://tax.illinois.gov/forms/sales/salesandusetax/st-1-instructions.html) |
| Quarter-monthly payments required if average monthly liability is | $20,000 or more | [IDOR ROT page](https://tax.illinois.gov/research/taxinformation/sales/rot.html) |
| Return and payment due | 20th of the month after the period | [Form ST-1 instructions](https://tax.illinois.gov/forms/sales/salesandusetax/st-1-instructions.html) |
| Late-payment penalty: 1 to 30 days late; 31 days or later | 2%; 10% | [IDOR Publication 103](https://tax.illinois.gov/research/publications/pubs/penalties-and-interest-for-illinois-taxes.html) |
| Late-filing penalty, first tier | lesser of $250 or 2% of the tax required to be shown | [IDOR Publication 103](https://tax.illinois.gov/research/publications/pubs/penalties-and-interest-for-illinois-taxes.html) |
| Interest rate on underpayments, 1 January 2025 to 31 December 2026 | 7% | [IDOR interest rates](https://tax.illinois.gov/individuals/interestrate.html) |

Local rates are not listed: they vary by address and change on 1 January and 1 July. Look up the rate for the address and period in the MyTax Illinois Tax Rate Finder (IDOR ROT page; ST-1 instructions).

### The four taxes

| Tax | Who owes it | How it works |
| --- | --- | --- |
| Retailers' Occupation Tax (35 ILCS 120) | Retailers, on gross receipts from selling goods at retail | The retailer's ROT is reimbursed by the Use Tax it collects from the customer in the same transaction (ROT page) |
| Use Tax (35 ILCS 105) | Buyers, for using goods in Illinois | Paid to the retailer, or directly to IDOR when no Illinois tax was charged |
| Service Occupation Tax (35 ILCS 115) | Servicepersons, only on goods transferred with a service | The service element is not taxed |
| Service Use Tax (35 ILCS 110) | Buyers of services, on goods received with the service | Paid to the serviceperson, or directly |

From 1 January 2025 a lease of goods (other than items titled or registered with a State agency, except certain trailers) is a sale at retail, so lessors owe ROT on lease receipts (ROT page).

### Steps

1. **Decide whether the seller must register.** Physical presence in Illinois: register and collect. A remote retailer or marketplace facilitator: register and collect once its gross receipts from sales of goods to Illinois purchasers reach $100,000 in the 12-month lookback, tested at the end of each quarter. For lookback periods ending after 31 December 2025 there is no transaction test (Bulletin FY 2026-12). IDOR's general ROT page still describes the 200-transaction test; the later bulletin governs.
2. **Classify each item** (PIO-115). General merchandise at the high rate includes candy, soft drinks, alcohol, food prepared for immediate consumption and prewritten software. Drugs and medical appliances, including products whose label makes a medicinal claim, are at the low rate. Groceries (food to be eaten off the premises, other than alcohol, cannabis-infused food, soft drinks, candy or prepared food) carry no State tax from 2026 but may carry a 1% local grocery tax.
3. **Source the sale.** A sale made from an Illinois location, or filled from Illinois inventory, takes that location's rates (origin). A sale made from outside Illinois by a retailer that must collect takes the rates of the Illinois delivery address (destination). From 1 January 2026 servicepersons with an Illinois place of business are also on destination sourcing for service sales otherwise sourced outside Illinois (Bulletin FY 2026-13). Keep the full delivery address for every destination sale, or IDOR taxes those receipts at 15% (ST-1 instructions).
4. **Look up the combined rate** for the address and period in the Tax Rate Finder, including any local grocery tax.
5. **Support every untaxed sale.** A resale needs the buyer's active Illinois registration or resale number and a resale certification, usually Form CRT-61; an exempt organisation must give its IDOR exemption number (ROT page).
6. **For services, choose the SOT base** (Bulletin FY 2026-13): (1) SOT on the separately stated selling price of goods transferred; (2) SOT on 50% of the entire bill; (3) SOT on the serviceperson's cost price, for a de minimis serviceperson registered or required to be registered under Section 2a of the ROT Act; (4) Use Tax on cost price, for a de minimis serviceperson not otherwise required to register. A serviceperson whose only Illinois presence is meeting the $100,000 services threshold cannot use method 4 if it makes any retail sales to Illinois purchasers.
7. **Accrue Use Tax** on purchases used in Illinois where no Illinois tax was paid, on the ST-1 for that period.
8. **File Form ST-1** (with Form ST-2 for multiple or destination sites) by the 20th of the month after the period, including periods with nothing to report. Take the discount only when filing and paying on time.

### Groceries from 1 January 2026 (Bulletin FY 2026-03; ST-1 instructions)

- An ordinance imposing the local 1% grocery tax must be filed with IDOR to take effect; IDOR had received more than 600 ordinances when the bulletin was published, and notifies affected retailers.
- In the RTA and MED areas the existing local grocery tax continues; where a municipality or county there also imposes a grocery tax, the rate is the total of both.
- Where a grocery tax applies: include grocery receipts on ST-1 Step 2 Lines 1 and 3 and report them on the new Line 5c. Where none applies (outside RTA and MED): include them on Line 1 and deduct them on Schedule A Line 16.
- Destination sellers collect the local grocery tax for delivery addresses where it applies.

### Food boundaries (PIO-115)

| Item | Treatment |
| --- | --- |
| Candy: sugar or sweeteners combined with chocolate, fruit, nuts or other ingredients in bars, drops or pieces | High rate |
| A preparation containing flour, or one that requires refrigeration | Not candy: groceries |
| Juice over 50% fruit or vegetable juice | Not a soft drink: groceries |
| Any food where the seller provides seating or facilities for eating on the premises | Presumed prepared food at the high rate, unless the eating area is separate and sales are recorded separately |
| Vitamins and supplements | Groceries only if the label makes no medicinal claim; otherwise low-rate drugs |

## Boundary and exception table

| Item | Status | Condition |
| --- | --- | --- |
| Sales for resale | Not taxed | Buyer's active registration or resale number and certification (CRT-61); otherwise presumed not for resale |
| Out-of-state purchaser that will resell and deliver only outside Illinois | Not taxed | CRT-61 with its other-state registration |
| Governments; exclusively charitable, religious or educational organisations | Exempt | Organisations need an IDOR exemption number |
| Sales to buyers outside Illinois (interstate commerce) | Exempt | Keep proof of out-of-state delivery |
| Manufacturing and assembling machinery and equipment; production agriculture equipment | Exempt | Primary use conditions apply |
| SNAP purchases | Exempt | Report on ST-1 Schedule A |
| Clothing and footwear | Taxable at 6.25% | No general exemption |
| Prewritten software | Taxable at 6.25% | General merchandise; SaaS and custom software: refer |
| Repair labor and other services | Not taxed | Only goods transferred with the service (SOT) |
| Remote seller with $99,999 of Illinois sales in the lookback | No collection duty | The test is $100,000 or more |
| Seller registered only under the old 200-transaction test | Review the 12 months to 31 December 2025 | Under $100,000: stop collecting ROT for remote sales from 1 January 2026 (Bulletin FY 2026-12) |
| Return with no sales | Still file | Every period, including zero returns |
| Due date on a weekend or holiday | Next business day | ST-1 instructions |

### Defaults when a fact is missing

| Missing fact | Default, and flag it |
| --- | --- |
| Delivery address for a destination sale | Do not file without it: IDOR may tax the receipts at 15% |
| Seating at a food seller | Assume seating (all food at the high rate) until shown otherwise |
| Whether the location has a local grocery tax | Check the Tax Rate Finder and IDOR's ordinance list; do not assume none |
| Resale certificate | Treat the sale as taxable |
| Serviceperson's cost ratio | Use method 1 or 2 until the ratio is computed |

### Red flags to raise with the client

| Flag | Why it matters |
| --- | --- |
| Remote seller collecting on the old 200 test | It may now be under the threshold, and over-collected tax must be refunded or reported |
| Destination sales without full addresses | 15% rate |
| Groceries charged no tax in a town with an ordinance | The 1% is owed even if not collected |
| A single "Illinois rate" quoted | There is none; the rate depends on address and period |

## Worked cases

**Case 1, a decision: must a remote seller register?** An Oregon seller with no Illinois presence made 450 sales worth $80,000 to Illinois buyers in the 12 months to 31 March 2026, and $104,000 in the 12 months to 30 June 2026. Under the 2026 rule only the $100,000 test counts, so at 31 March it has no duty (the 450 transactions no longer matter), and at 30 June it does: it must register, collect State and local ROT at each delivery address's rate and file returns. IDOR's pages read here do not state the start date after the quarter end; confirm it with IDOR before the first collection.

```oa-check
name: Illinois remote seller threshold, quarterly test (2026)
inputs:
  receipts_to_march: 80000
  receipts_to_june: 104000
  threshold: 100000
steps:
  - must_register_march: min(floor(receipts_to_march / threshold), 1)
  - must_register_june: min(floor(receipts_to_june / threshold), 1)
expected:
  must_register_march: 0
  must_register_june: 1
```

**Case 2, the discount, the cap and a late return.** A monthly filer owes $5,000 for August 2026, due 21 September 2026 (20 September is a Sunday). Filed and paid on time: discount 1.75% x $5,000 = $87.50, net $4,912.50. A filer owing $80,000 would compute $1,400, but the cap allows $1,000. If the $5,000 return is filed and paid 12 days late: no discount; late-payment penalty 2% = $100; late-filing penalty the lesser of $250 or 2% = $100; interest at 7% simple for 12 days = $11.51.

```oa-check
name: Illinois ST-1 discount, cap and late penalties (2026)
inputs:
  tax_due: 5000
  large_tax_due: 80000
  days_late: 12
steps:
  - discount: max(tax_due * 0.0175, 5)
  - net_on_time: tax_due - discount
  - large_discount: min(large_tax_due * 0.0175, 1000)
  - late_payment_penalty: tax_due * 0.02
  - late_filing_penalty: min(250, tax_due * 0.02)
  - interest: round(tax_due * 0.07 / 365 * days_late, 2)
expected:
  discount: 87.50
  net_on_time: 4912.50
  large_discount: 1000.00
  late_payment_penalty: 100.00
  late_filing_penalty: 100.00
  interest: 11.51
```

**Further examples (State rate only; add local rates from the Tax Rate Finder).**

- *Groceries, candy and drugs* (PIO-115): a shop outside RTA and MED, no seating, sells $200 of groceries, a $20 box of granola bars containing flour (groceries), a $40 box of chocolate bars without flour (candy: $2.50 State tax) and $10 of aspirin (drug: $0.10 State tax). In a town with no grocery ordinance the $220 of groceries carries no tax; with one, $2.20 is owed whether or not collected.
- *SOT methods* (Bulletin FY 2026-13): $500 labor and $300 parts separately stated: $18.75 State SOT on the parts. An $800 bill with no split: 50% = $400 base, $25.00. The selling price can never be less than cost price.
- *Use Tax on a purchase*: $2,000 of equipment bought from an out-of-state vendor that charged no Illinois tax: $125.00 Use Tax on the ST-1 for that month.

## When to refuse or refer

- **SaaS, custom software, streaming and digital downloads**: IDOR's pages read here class prewritten software as general merchandise but do not settle the others. Refer.
- **Taxes IDOR does not collect**, such as a city's own amusement or restaurant taxes. Refer to the city or county.
- **Titled or registered items, motor fuel, aviation fuel, E911 and ITAC.**
- **Audits, the 15% undetermined-location rate, and appeals** to the Illinois Independent Tax Tribunal or circuit court.
- **Exemption claims needing certificates** beyond CRT-61 and exemption numbers (manufacturing, farm, enterprise zone, high impact business).
- **A client who wants one "Illinois rate"** without an address and period.

## Filing and payment

Register through MyTax Illinois (Form REG-1). File Form ST-1, with ST-2 for multiple sites and every destination site, by the 20th of the month after the period: monthly, quarterly (20 April, 20 July, 20 October, 20 January) or annual (20 January), as IDOR assigns. A due date on a weekend or holiday moves to the next business day. File electronically through MyTax Illinois where required; electronic filers get the discount only if they file electronically and pay on time. Correct errors on Form ST-1-X. Pay quarter-monthly (7th, 15th, 22nd and last day of each month) once average monthly liability is $20,000 or more. Individuals and unregistered businesses owing Use Tax file Form ST-44. Penalties (Publication 103): late payment 2% (1 to 30 days) or 10% (31 days or more); 15% of amounts unpaid until an audit starts and 20% of amounts unpaid within 30 days of an audit-prepared return; late filing first tier the lesser of $250 or 2%, second tier (no return within 30 days of a nonfiling notice) the greater of $250 or 2%; negligence 20%; fraud 50%; failure to keep or produce books and records $1,000 then $3,000; collection fee $30 (under $1,000 unpaid) or $100. Interest is simple interest at 7% for 1 January 2025 to 31 December 2026.

### 2025 periods (amended or audited returns)

- Through 31 December 2025 qualifying food was taxed at the State 1% plus local taxes; use the pre-2026 ST-1 and ST-2 for those periods.
- For lookback periods ending on or before 31 December 2025, a remote retailer or facilitator met the threshold with $100,000 or more in gross receipts or 200 or more transactions (Bulletin FY 2026-12).
- The $1,000 monthly discount cap applies to returns due on or after 1 January 2025; interest was 7% throughout 2025.

## Completion checklist

- Physical presence checked; remote sellers tested each quarter against $100,000, with no transaction test for 2026.
- Each item classified (general merchandise, drug, grocery, prepared food; flour, refrigeration and seating tests).
- Each sale sourced and the rate taken from the Tax Rate Finder, including any local grocery tax.
- Full delivery addresses kept for every destination sale.
- SOT base chosen from the four methods.
- CRT-61 or exemption number on file for each untaxed sale.
- Use Tax accrued on untaxed purchases.
- ST-1 (and ST-2) filed by the 20th, zero returns included; 1.75% discount only when on time, capped at $1,000 a month.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| IDOR Form ST-1 instructions. Read for the grocery lines 5c and 2b, the 15% undetermined-location rate, the 20th due date, the weekend rule, the filing frequency thresholds, the 1.75% discount, $5 minimum and $1,000 cap. | https://tax.illinois.gov/forms/sales/salesandusetax/st-1-instructions.html | 2026-11-13 |
| IDOR Retailers' Occupation Tax page. Read for the four taxes, leases from 2025, resale certificates, exemptions, quarter-monthly payments at $20,000, the Tax Rate Finder, ST-1-X, ST-2, ST-44. | https://tax.illinois.gov/research/taxinformation/sales/rot.html | 2026-11-13 |
| IDOR PIO-115. Read for the 6.25% high rate and 1% low rate, the grocery definition, candy, flour, refrigeration, juice, seating and supplements. | https://tax.illinois.gov/research/publications/pio-115.html | 2026-11-13 |
| IDOR Informational Bulletin FY 2026-03. Read for the end of the State grocery tax on 1 January 2026, the local 1% grocery tax, RTA and MED, the 600 ordinances and the reporting chart. | https://tax.illinois.gov/research/publications/bulletins/fy-2026-03.html | 2026-11-13 |
| IDOR Informational Bulletin FY 2026-12. Read for the removal of the 200-transaction test (Public Act 104-0006) and the $100,000 threshold. | https://tax.illinois.gov/research/publications/bulletins/fy-2026-12.html | 2026-11-13 |
| IDOR Informational Bulletin FY 2026-13. Read for servicepersons' destination sourcing from 1 January 2026, the four SOT methods and the $100,000 services threshold. | https://tax.illinois.gov/research/publications/bulletins/fy-2026-13.html | 2026-11-13 |
| IDOR Publication 103, Penalties and Interest for Illinois Taxes. Read for the late-filing, late-payment, audit, negligence, fraud, records and collection fee amounts. | https://tax.illinois.gov/research/publications/pubs/penalties-and-interest-for-illinois-taxes.html | 2026-11-13 |
| IDOR interest rates page. Read for 7% for 1 January 2025 to 31 December 2026. | https://tax.illinois.gov/individuals/interestrate.html | 2026-11-13 |

Illinois sites refused direct connections from this machine; every page above was read through a Firecrawl fetch of the official URL on 2026-11-13.

Not yet confirmed: the de minimis serviceperson cost ratios (35%, or 75% for prescription drugs and graphic arts) carried from the earlier version (Publication 113-SOT not re-read); the record retention period of three and one-half years (record-keeping page not re-read); the Form ST-44 thresholds ($600 or less by 15 April) from the earlier version; the start date of collection after a remote seller passes the threshold; how the $1,000 monthly cap applies to quarterly and annual returns; the 2026 back-to-school sales tax holiday terms and the 2026 Remote Retailer Tax Amnesty (1 August to 31 October 2026) described in the earlier version from Bulletins FY 2026-30 and FY 2026-28, not re-read; Chicago, Springfield and Champaign combined rates in the retired `il-sales-tax` file (not used: look up the address instead); the taxability of prepaid calling arrangements (35 ILCS 120/2-25, not read).

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-13. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `illinois-sales-tax` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/illinois-sales-tax. If neither is available, confirm every figure against the official source pages cited above before relying on it.
