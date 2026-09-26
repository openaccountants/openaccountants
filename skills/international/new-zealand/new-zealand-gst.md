---
name: new-zealand-gst
description: Use this skill whenever asked to prepare, review, or classify transactions for a New Zealand GST return (GST101A form) for a self-employed individual or small business in New Zealand. Trigger on phrases like "prepare GST return", "do the GST", "fill in GST101A", "create the return", "New Zealand GST", "NZ GST", or any request involving New Zealand GST filing. Also trigger when classifying transactions for GST purposes from bank statements, invoices, or other source data. This skill covers standard GST-registered persons under the invoice or payments basis. Financial services elections, GST groups, non-profit bodies, and complex change-of-use adjustments on high-value mixed-use assets are in the refusal catalogue. MUST be loaded alongside vat-workflow-base v0.1 or later (for workflow architecture). ALWAYS read this skill before touching any NZ GST work.
version: 2.0
jurisdiction: NZ
tax_year: 2026
last_updated: 2026-09-25
authored_by: OpenAccountants team
review_status: pending_review
trust_label: By OpenAccountants
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# New Zealand GST: registration, rate, invoices, filing, input tax and adjustments (2026-27)

Figures are for tax year 2026, meaning the New Zealand 2026-27 income year from 1 April 2026 to 31 March 2027 (which IRD calls the 2027 income year). GST itself has no tax year. It runs by taxable period, and the rules below apply to every period until the law changes. A short dated section near the end covers returns still being filed for 2025-26. Sources are Inland Revenue (IRD) web pages read on 25 September 2026, the IR375 GST guide (March 2026 edition) and IRD interpretation statement IS 25/21 (8 October 2025). All amounts are New Zealand dollars.

## Scope and who this is for

- **Covers:** anyone who is, or may need to be, registered for New Zealand GST (sole trader, partnership, company or trust): registration and cancellation, the rate, zero-rated and exempt supplies, taxable supply information, accounting bases, filing frequency, input tax and change of use, secondhand goods, entertainment, bad debts, online marketplaces, remote services and low value imported goods, the GST101A, due dates, penalties and interest.
- **Does not cover:** GST groups, the financial services zero-rating election, the compulsory zero-rating of land between registered persons, non-profit bodies selling donated goods, mixed-use holiday homes, boats and aircraft, fringe benefit tax, and the income tax side of any item. The "When to refuse or refer" section lists where to send these.
- **Bank-statement work:** use the classification defaults below with the runbook in `vat-workflow-base`.

## Ask the client first

- Are you registered for GST? If not, what were your sales from all taxable activities in the last 12 months, and what do you expect in the next 12 months? Do you add GST to your prices?
- Which accounting basis are you on (payments, invoice or hybrid), how often do you file, and what is your balance date? If you never chose, IRD put you on the invoice basis and on 2-monthly filing matched to your balance date.
- Are you liable for provisional tax? That decides whether you file a GST101A or a GST103.
- Do you make any exempt supplies, such as residential rent, interest or other financial services?
- Do any sales go to customers overseas? Were those customers outside New Zealand when you did the work? Do you export goods?
- Do you sell ride-sharing, food and beverage delivery, or short-stay accommodation through an app or website such as Uber or Airbnb? Do you also take direct bookings?
- Do you use any asset partly for private purposes? Did you claim GST on it using the principal purpose method or the apportionment method?
- Do you buy secondhand goods from people who are not registered? Do you buy from relatives or associated companies or trusts?
- Did you spend money on business entertainment this year, and does a tax agent file your income tax return?
- Do you import goods and pay GST to Customs? Did you write off, or recover, any bad debts?

## The method, step by step

1. **Test registration.** Add up supplies from all the person's taxable activities for the last 12 months, and estimate the next 12 months. Compare each with the registration line in the registration table below. Registration is compulsory if either test is passed, or if the person adds GST to their prices. Check the provisos before telling someone they must register, and refer a client sitting at exactly the line.
2. **Fix the basis and period.** Confirm the accounting basis and filing frequency, and check the person still qualifies for them using the limits in the tables below. The basis decides which period each transaction falls in.
3. **Classify each sale.** Each sale is standard-rated (15%, [What GST is](https://www.ird.govt.nz/gst/what-gst-is)), zero-rated, exempt, or outside GST. Exempt and out-of-scope items stay off the return. Zero-rated sales go in Box 5 and again in Box 6. Marketplace listed services sold by a registered seller are zero-rated.
4. **Classify each purchase.** Claim GST only on purchases used to make taxable supplies, only where the taxable supply information for the size band is held, and only to the extent of taxable use. No GST charged means no claim, unless the secondhand goods rule applies.
5. **Work out the adjustments.** Debit adjustments go in Box 9 and credit adjustments in Box 13 (see the box table).
6. **Complete the return.** Enter GST-inclusive totals in Boxes 5 and 11, and apply the tax fraction. Box 15 is GST to pay or a refund.
7. **File and pay by the due date.** File every period, including nil periods. Payment is due the same day as the return.
8. **Keep the records** for 7 years.

## Figures and rules for 2026-27

### Rate and tax fraction ([What GST is](https://www.ird.govt.nz/gst/what-gst-is); [Charging GST](https://www.ird.govt.nz/gst/charging-gst))

| What | Value | Note |
| --- | --- | --- |
| Standard rate | 15% | The only positive rate. There are no reduced rates. |
| Zero rate | 0% | "Zero-rated supplies are supplies that have GST charged at 0% where certain requirements are met." |
| GST inside a GST-inclusive price | 3/23 | IRD example: $115 including GST contains $15 GST. |
| GST to add to a GST-exclusive price | 15% | IRD example: $100 plus GST is $115. |

### Registration ([Registering for GST](https://www.ird.govt.nz/gst/registering-for-gst); [IR375](https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir300---ir399/ir375/ir375.pdf); [IS 25/21](https://www.taxtechnical.ird.govt.nz/-/media/project/ir/tt/pdfs/interpretation-statements/2025/is-25-21.pdf?modified=20251023203446))

| What | Value | Note |
| --- | --- | --- |
| Registration line, past 12 months | $60,000 | Supplies from all taxable activities, including certain imported services received |
| Registration line, next 12 months | $60,000 | Supplies expected in the next 12 months |
| Voluntary registration | below $60,000 | Needs a taxable activity |

- **Who.** An entity that carries on a taxable activity. A taxable activity is one "carried on continuously or regularly" that involves supplying goods or services to another person for consideration (IR375). Starting a business does not by itself mean registering.
- **"At least" or "over".** The IRD web page says turnover "was at least $60,000 in the last 12 months" or is expected to be "at least $60,000 in the next 12 months". IR375 says "was over $60,000" or "is expected to go over $60,000". IS 25/21 says section 51(1) applies when supplies are "exceeding $60,000 in a 12-month period (looking backwards under section 51(1)(a) or looking forwards under section 51(1)(b))". The difference matters only at exactly $60,000. Refer that case.
- **Adding GST to prices.** Anyone who carries on a taxable activity and adds GST to their prices must register, whatever their turnover.
- **Provisos (IS 25/21).**
  - Registration is not required if the past 12 months passed the line but IRD "is satisfied that the value of supplies in the next 12-month period will not exceed $60,000". This covers one-off sales.
  - Registration is not required where IRD is satisfied that the line will be passed only because an activity is ending (including ending early) or being substantially and permanently reduced in size. This does not cover a subdivision where the sale proceeds are the expected result of the activity: refer.
  - Registration is not required where IRD is satisfied that the line will be passed only because plant or another capital asset used in the activity is replaced.
- **Voluntary registration** is allowed below the line. The person then must add GST, file regularly and faces penalties for lateness ([Registering voluntarily](https://www.ird.govt.nz/gst/registering-for-gst/registering-for-gst-voluntarily)).

### Cancelling registration ([When to cancel](https://www.ird.govt.nz/gst/gst-cancellation/when-to-cancel-your-gst-registration))

- **Must cancel** within 21 days if the person stops their taxable activity and does not intend to start a new one within the next 12 months.
- **May cancel** if turnover for the next 12 months will be under $60,000, or if they have filed nil returns for more than 12 months.
- **Cannot cancel** while GST is included in their prices, even if annual turnover is under $60,000.

### Taxable supply information ([How taxable supply information works](https://www.ird.govt.nz/gst/tax-invoices-for-gst/how-taxable-supply-information-for-gst-works); [Taxable supply information for GST](https://www.ird.govt.nz/gst/tax-invoices-for-gst))

From 1 April 2023, tax invoices were replaced by a duty to provide and keep **taxable supply information** (TSI). Invoices, bank statements, agreements and contracts can hold it together; a document still headed "tax invoice" complies. Debit and credit notes are now **supply correction information**.

| Supply value (including GST) | Seller must give it to a registered buyer? | What the records must show |
| --- | --- | --- |
| $200 or less | No; both sides still keep records | Seller name, date, description, the consideration |
| More than $200 and up to $1,000 | Yes, within 28 days of a request | As above, plus the seller's GST number and either (a) the GST-exclusive amount, the GST amount and the GST-inclusive amount, or (b) the GST-inclusive amount and a statement that GST is included |
| More than $1,000 | Yes, within 28 days of a request | As the middle band, plus the buyer's name and one identifier (address, phone, email, trading name, NZBN or website) |
| Secondhand goods from an unregistered seller | Buyer keeps the record | Seller name and address, date supplied, description, quantity or volume, the consideration |

A buyer claims input tax only when they hold the TSI for the band.

### Accounting bases ([Which accounting basis and filing frequency](https://www.ird.govt.nz/gst/registering-for-gst/which-gst-accounting-basis-and-filing-frequency-should-i-use); [Changing your accounting basis](https://www.ird.govt.nz/gst/changing-your-filing-frequency-or-accounting-basis/changing-your-gst-accounting-basis); [Special supplies](https://www.ird.govt.nz/gst/charging-gst/special-supplies))

| Basis | Who may use it | Sales go in the period when | Purchases go in the period when |
| --- | --- | --- | --- |
| Payments | Total sales of $2 million or less in the last 12 months, or likely to be $2 million or less in any 12-month period beginning on the first day of a month | You are paid | You pay, if you hold TSI |
| Invoice | Anyone. This is the default if no basis was chosen at registration (IR375) | You invoice; if the customer pays any amount before you invoice, return the full sale price then | You are invoiced or pay, if you hold TSI, even if not fully paid |
| Hybrid | Anyone | Invoice basis | Payments basis |

- **Leaving the payments basis.** A person on the payments basis must change basis if annual sales increase to more than $2 million.
- **Large single supplies.** A supply of goods and services for more than $225,000 must be accounted for on the invoice basis whatever the person's basis. The exception is a short-term agreement, where settlement or performance happens within 365 days of the agreement.
- **Hire purchase.** Hire purchase sales and purchases go in the period the agreement is entered into, on every basis.

### Filing frequency ([Which accounting basis and filing frequency](https://www.ird.govt.nz/gst/registering-for-gst/which-gst-accounting-basis-and-filing-frequency-should-i-use))

| Frequency | Who may use it |
| --- | --- |
| Monthly | Anyone. Compulsory if sales are over $24 million in any 12-month period |
| 2-monthly | Sales under $24 million in any 12-month period. This is the default if no period was chosen (IR375) |
| 6-monthly | Sales under $500,000 in any 12-month period |

- **GST groups.** For a GST group, each limit applies to the group as a whole.
- **Balance date.** Periods align with the income tax balance date. With a 31 March balance date, 2-monthly periods end in odd months (May, July, September, November, January, March), and 6-monthly periods end 30 September and 31 March.
- **Changing** frequency or basis: ask in myIR and wait for IRD to confirm.

### Input tax, apportionment and change of use ([Claiming GST](https://www.ird.govt.nz/gst/claiming-gst); [Change-in-use adjustments](https://www.ird.govt.nz/gst/gst-adjustments/change-in-use-adjustments-for-gst))

GST can be claimed only to the extent goods and services are used to make taxable supplies. There is no claim for private use or for making exempt supplies.

| GST-exclusive cost | Method | Adjustment periods |
| --- | --- | --- |
| $10,000 or less | Principal purpose (all the GST if the main purpose is taxable use, none if not) or apportionment | None |
| $10,001 to $20,000 | Apportionment | 2 |
| $20,001 to $500,000 | Apportionment | 5 |
| Over $500,000, or land of any value | Apportionment | 10 |

- **Apportionment lock-in.** A person who chooses apportionment for a purchase of $10,000 or less must use it for all such purchases for a minimum of 24 months (IR375).
- **Adjustment periods.** The first runs from acquisition to the end of the current income year, or to the end of the income year at least 12 months after acquisition (the person chooses). Each later period is an income year. At the end of each, compare actual taxable use with the use already claimed. The adjustment goes in the first return after balance date.
- **No adjustment needed if any of these applies:**
  - the GST-exclusive cost is $10,000 or less;
  - the change in taxable use is less than 10% and the adjustment is under $1,000 (web page) or $1,000 or less (IR375), refer an adjustment of exactly $1,000;
  - the person makes taxable and exempt supplies, and exempt supplies in the adjustment period are less than both $90,000 and 5% of total taxable and exempt supplies.
- **Permanent change (wash-up).** Adjustment = (full GST x new percentage) minus GST already claimed. Make it in the period the use permanently changes, even inside the 10% or $1,000 threshold. Annual adjustments then stop.
- **Sale of a partly-claimed asset.** Final adjustment = 3/23 x sale price (GST-inclusive) x (1 minus previous taxable use). This is a credit.
- **Mixed-use holiday homes, boats and aircraft** follow separate rules. Refer.
- **Non-taxable election.** Land, dwellings and vehicles acquired mainly for private use can be elected to be non-taxable, so no GST arises on a later sale. Conditions apply (IR375). Refer before making it.

### Entertainment ([IR375](https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir300---ir399/ir375/ir375.pdf))

| What | Value |
| --- | --- |
| Share of business entertainment usually deductible for income tax | 50% |
| Annual GST adjustment on the GST-exclusive non-deductible amount | 15% |

- **Private entertainment.** No GST claim.
- **Business entertainment.** Show the full cost in purchases during the year, then make one debit adjustment a year for the part not deductible for income tax.
- **When to make the adjustment:**
  - no tax agent: the return covering the earlier of the income tax return's due date and its filing date;
  - tax agent, no extension of time: the earlier of filing and 31 March after the due date;
  - tax agent with an extension of time: the return covering the filing date.
- **Exemption.** Bodies not liable for income tax, such as charities, make no adjustment.
- **Which items are limited** is an income tax question (IRD guide IR268).

### Online marketplaces and listed services ([GST for drivers, deliverers and accommodation owners](https://www.ird.govt.nz/sharing-economy/sellers-of-listed-services/gst-for-listed-services); [Flat-rate credit scheme](https://www.ird.govt.nz/sharing-economy/listing-intermediary-rules/flat-rate-credit-scheme))

From 1 April 2024, an online marketplace must collect and pay GST on **listed services** performed, provided or received in New Zealand, whether or not the seller is registered. Listed services are ride-sharing, food and beverage delivery, and short-stay and visitor accommodation. Short-stay means guests staying up to 4 consecutive weeks at a time. Closely connected services charged through the platform, such as a cleaning fee, are included.

| What | Value |
| --- | --- |
| GST the marketplace collects on listed services | 15% |
| Part the marketplace pays to IRD for an unregistered seller | 6.5% |
| Flat-rate credit passed to an unregistered seller | 8.5% |

- **Unregistered seller.** Keeps the flat-rate credit, and may treat it as assessable or excluded income for income tax. Marketplace income still counts towards the registration line ([Short-stay accommodation](https://www.ird.govt.nz/sharing-economy/sellers-of-listed-services/short-stay-accommodation)).
- **Registered seller.** Reports sales of listed services made through a GST-registered online marketplace as **zero-rated** supplies. Can still claim GST on costs. A flat-rate credit received while registered must be paid back as a debit adjustment. The seller must tell the marketplace they are registered.
- **Outside the platform.** Direct bookings through the seller's own website, and services that do not go through a marketplace, follow the normal rules.
- **Selling assets.** A registered seller generally returns GST on the sale of a vehicle or property used for listed services, unless a non-taxable election applies.
- **Not a marketplace.** A platform that supplies the service itself and hires the driver as an employee or contractor is not a marketplace for these rules.

### Remote services and low value imported goods ([Supplying remote services](https://www.ird.govt.nz/gst/gst-for-overseas-businesses/supplying-remote-services-into-new-zealand); [Low value imported goods](https://www.ird.govt.nz/gst/gst-for-overseas-businesses/supplying-low-value-imported-goods))

| What | Value |
| --- | --- |
| Overseas supplier must register when supplies to NZ customers were more than, or are expected to be more than | $60,000 |
| Low value good (physical good, excluding GST) | NZ$1,000 or less |

- **Remote services** (digital content, apps, software, legal, accounting or consultancy services) supplied by an overseas business to NZ-resident consumers: the supplier, or a marketplace such as an app store, registers above the line, charges GST and files quarterly.
- **Business customers.** No registration is needed if the supplier supplies only GST-registered NZ businesses for business use. It treats a customer as unregistered unless the customer says it is registered or gives a GST number or NZBN, so a registered business should give its GST number.
- **Low value goods.** An overseas seller, marketplace or redeliverer may have to charge GST on goods of NZ$1,000 or less sold to a **consumer**. A consumer is anyone not registered, or a registered person using the goods only privately. Goods over NZ$1,000 have GST charged at the border by Customs.
- **Buyer's side.** NZ GST charged by an overseas supplier on a business purchase is claimable only with TSI. No NZ GST on the invoice means no claim.

### Penalties and interest ([Late filing penalties](https://www.ird.govt.nz/managing-my-tax/penalties-and-interest/penalties-and-debt/late-filing-penalties); [Late payment penalties](https://www.ird.govt.nz/managing-my-tax/penalties-and-interest/penalties-and-debt/late-payment-penalties); [Interest](https://www.ird.govt.nz/managing-my-tax/penalties-and-interest/interest-on-overpayments-and-underpayments))

| What | Value |
| --- | --- |
| Late filing, payments basis (basis when the return is due) | $50 |
| Late filing, invoice or hybrid basis | $250 |
| Late payment, day after the due date | 1% |
| Late payment, 7th day after the due date, on remaining tax including penalties | 4% |
| Monthly late payment penalty | Does not apply to GST |
| Interest IRD charges on underpaid tax, from 16 January 2026 | 8.97% |
| Interest IRD pays on overpaid tax, from 16 January 2026 | 2.25% |
| No interest on amounts under | $100 |

- **First late payment.** If it is the first late payment in a 2-year period, IRD may give a grace period before charging penalties.
- **Late filing penalty due date.** It is usually due on the 28th of the month after the return was due. A penalty that would fall due on 28 December is due 15 January, and one that would fall due on 28 May is due 7 June.
- **Interest** is daily, not compounding, and the rates change: read the newest row of IRD's table.

## GST101A and GST103 boxes ([IR375](https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir300---ir399/ir375/ir375.pdf))

File a GST101A if not liable for provisional tax, and a form in the GST103 series if liable. The sales and purchases boxes are the same. All amounts are GST-inclusive on every basis. The basis decides only which period an item falls in.

| Box | What goes in it |
| --- | --- |
| 5 | Total sales and income for the period, including GST and including zero-rated supplies |
| 6 | Zero-rated supplies included in Box 5 |
| 7 | Box 5 minus Box 6 |
| 8 | Box 7 x 3 / 23 |
| 9 | Debit adjustments from the calculation sheet (IR372): entertainment, flat-rate credits received while registered, bad debts recovered, exported secondhand goods, change of use, insurance payments received, barter |
| 10 | Box 8 plus Box 9: total GST collected |
| 11 | Total purchases and expenses, including GST, **excluding imported goods**. Only items with TSI |
| 12 | Box 11 x 3 / 23 |
| 13 | Credit adjustments: bad debts written off, GST paid to Customs on imported goods, change of use |
| 14 | Box 12 plus Box 13: total GST credit |
| 15 | Difference between Box 10 and Box 14. Box 10 larger: GST to pay. Box 14 larger: refund. Equal: nil return, still filed |

## Boundaries and exceptions ([Zero-rated supplies](https://www.ird.govt.nz/gst/charging-gst/zero-rated-supplies); [Exempt supplies](https://www.ird.govt.nz/gst/charging-gst/exempt-supplies); [Special supplies](https://www.ird.govt.nz/gst/charging-gst/special-supplies); [Other GST credit adjustments](https://www.ird.govt.nz/gst/gst-adjustments/other-gst-credit-adjustments))

| Item | Treatment | Condition or exception |
| --- | --- | --- |
| Exported goods | Zero-rated | Goods entered for export must leave within 28 days of the time of supply unless IRD extends it. Items under $1,000 with no export entry qualify if export is proved |
| Services to a non-resident | Zero-rated | Only if the non-resident is outside New Zealand when the service is performed. Further conditions are in the Act (check against section 11A before relying on it for a large supply) |
| Remote services to non-residents; services performed outside NZ | Zero-rated | Remote services need evidence the customer is not NZ resident: the supplier's own systems, or any 2 of billing address, IP address, bank details, SIM country code, landline location |
| International passenger transport | Zero-rated | Domestic legs too if part of the same international booking |
| Sale of a going concern | Zero-rated | Registered seller to registered buyer; the whole or a stand-alone part of the activity; all goods and services needed to keep it running; both parties agree in writing that it is a going concern and intend the buyer can carry it on; the business is operating up to transfer |
| Land between registered persons | Compulsorily zero-rated | Buyer registered, buying for taxable supplies, not as a home for the buyer or a relative, at settlement. Refer |
| Listed services sold through a GST-registered online marketplace, registered seller | Zero-rated | See the marketplace section |
| Financial services (interest, loans, bank fees, shares, currency exchange) | Exempt | Zero-rating election for some business-to-business supplies: refer |
| Renting a residential dwelling | Exempt | No GST claim on the dwelling's costs. Commercial dwellings (hotels, motels, boarding houses) are taxable |
| Residential accommodation under a head lease | Exempt | If the property is for the principal purpose of residential accommodation. Taxable only if all three apply: the parties agree the exemption does not apply, the lease was entered into before 16 May 2000, and earlier supplies were treated as taxable |
| Sale of a dwelling rented for at least 5 years | Exempt | If sold as part of a taxable activity |
| Sale of a registered person's private assets | Generally not taxable; not in the return | Unless the asset was used in the taxable activity |
| Penalty interest on overdue accounts | Exempt | Statutory fines and parking penalties are outside GST |
| Donated goods sold by a non-profit | Exempt | Refer |
| Secondhand goods from an unregistered seller | Credit may be claimed | Must pay before claiming, on any basis. Keep the secondhand goods TSI record. Not secondhand goods: new goods, unused primary produce, leased or rented goods, livestock, fine metal. Purchases from associated persons: refer. Box: the previous version of this Guide claimed it with purchases in Box 11; IRD's pages read for this Guide do not name the box (check) |
| Exporting secondhand goods on which a credit was claimed | Debit adjustment of 3/23 of the full purchase price | Zero-rating also needs the goods entered for export, export within 28 days and a no-reimport declaration |
| GST paid to Customs on imported goods | Credit adjustment (Box 13), not Box 11 | Claimable in full if the goods are used solely to make taxable supplies ([Claiming GST](https://www.ird.govt.nz/gst/claiming-gst)); apportion otherwise. Invoice basis: earlier of invoice or payment. Payments or hybrid basis: when paid |
| Imported services, taxable use under 95% | Reverse charge: return 15% GST on the price | Applies where intended or actual taxable use is less than 95%. Can also push turnover past $60,000 |
| Supplies to an associated person who cannot claim | GST on the greater of market value and the price | |
| Bad debt written off (GST already returned) | Credit adjustment of 3/23 of the amount written off | Keep a record of recovery steps. Payments basis: no claim, except hire purchase and door-to-door sales. Partly-taxed supplies use (written off / total consideration) x GST included |
| Bad debt recovered | Debit adjustment of 3/23 of the amount recovered | |
| Insurance payout relating to the taxable activity | Debit adjustment for the GST content | |

## Classifying bank-statement lines: conservative defaults

| Unknown | Default |
| --- | --- |
| Rate on a sale | Standard rate |
| GST status of a purchase, or no TSI | No claim |
| Business-use share of a vehicle, phone or home office | No claim until a percentage is evidenced |
| Personal or business | Personal, no claim |
| Customer overseas, evidence missing | Standard rate |
| Restaurant, cafe or bar | No claim until business purpose is confirmed |
| Bank fees, interest, loan principal, tax payments, ACC levies, wages, drawings, transfers, residential rent | Exclude |
| Marketplace payouts to a registered seller | Zero-rated sale (Boxes 5 and 6) |
| Sale of the owner's private goods | Exclude |

## Worked cases

### Case 1: registration on the forward test ([Registering for GST](https://www.ird.govt.nz/gst/registering-for-gst); [IS 25/21](https://www.taxtechnical.ird.govt.nz/-/media/project/ir/tt/pdfs/interpretation-statements/2025/is-25-21.pdf?modified=20251023203446))

A landscaper's sales for the 12 months to 31 August 2026 were $52,000. On 1 September 2026 he signs a contract, and he now expects $75,000 over the next 12 months.

- The past test is not met ($52,000 is under $60,000).
- The forward test is met ($75,000 is over $60,000), so he must register.
- If instead the only reason for passing the line had been selling his old trailer and mower when replacing them, he would not be liable if IRD is satisfied that replacing the assets is the only reason (the capital-asset proviso).

### Case 2: claiming GST on a purchase ([How taxable supply information works](https://www.ird.govt.nz/gst/tax-invoices-for-gst/how-taxable-supply-information-for-gst-works); [Calculating GST](https://www.ird.govt.nz/gst/filing-and-paying-gst-and-refunds/calculating-your-gst))

A registered plumber on the payments basis buys tools for $920 including GST, and pays in the period.

- The supply is more than $200 and up to $1,000. The record must show the seller's name and GST number, the date, a description, and the amounts (or the inclusive amount with a GST-included statement).
- GST inside the price: $920 x 3/23 = $120.
- $920 goes in Box 11. Box 12 picks up the $120.
- Unpaid at period end: on the payments basis it waits until paid. On the invoice basis it is claimed now.

### Case 3: zero-rated services to an overseas client ([Zero-rated supplies](https://www.ird.govt.nz/gst/charging-gst/zero-rated-supplies))

An Auckland consultant invoices a Sydney company $8,500 for advice. The company has no New Zealand presence and its staff were in Australia throughout.

- This is a service supplied to a non-resident outside New Zealand when performed. It is zero-rated.
- $8,500 goes in Box 5 and in Box 6. No GST is collected.
- GST on the consultant's related costs can still be claimed.
- If the client's staff attended workshops in Auckland, zero-rating may fail: refer.

### Case 4: short-stay accommodation through a marketplace ([GST for listed services](https://www.ird.govt.nz/sharing-economy/sellers-of-listed-services/gst-for-listed-services); [Flat-rate credit scheme](https://www.ird.govt.nz/sharing-economy/listing-intermediary-rules/flat-rate-credit-scheme))

A host rents a sleep-out for 3-night stays through a marketplace. The value of the accommodation in the period is $2,000.

- **Host not registered.** The marketplace collects 15% of $2,000 = $300. It pays 6.5% of $2,000 = $130 to IRD and passes 8.5% of $2,000 = $170 to the host as a flat-rate credit.
- **Host registered.** The marketplace still collects the GST. The host reports the $2,000 as a zero-rated supply (Boxes 5 and 6) and claims GST on costs. Any flat-rate credit the platform paid in error goes back as a debit adjustment (Box 9).
- **Direct bookings.** Stays booked directly through the host's own website are standard-rated under the normal rules.

### Case 5: selling a partly-claimed vehicle ([Change-in-use adjustments](https://www.ird.govt.nz/gst/gst-adjustments/change-in-use-adjustments-for-gst))

A registered builder claimed 70% of the GST on a van. He sells it for $23,000 including GST.

- Previous taxable use was 70%, so the unclaimed share is 30%.
- Final adjustment: 3/23 x $23,000 x (1 minus 0.7) = $900, a credit adjustment in Box 13.
- The full $23,000 sale goes in Box 5.

### Case 6: annual entertainment adjustment ([Other GST debit adjustments](https://www.ird.govt.nz/gst/gst-adjustments/other-gst-debit-adjustments))

A company spent $2,300 including GST on business client dinners during 2026-27, all claimed in Box 11 as incurred. The dinners are 50% deductible for income tax.

- GST-exclusive cost: $2,300 x 20/23 = $2,000.
- Non-deductible part: 50% of $2,000 = $1,000.
- Adjustment: 15% of $1,000 = $150, a debit adjustment in Box 9. It goes in the return set by the timing rules in the entertainment section.

### Case 7: bad debt and late payment ([Other GST credit adjustments](https://www.ird.govt.nz/gst/gst-adjustments/other-gst-credit-adjustments); [Late payment penalties](https://www.ird.govt.nz/managing-my-tax/penalties-and-interest/penalties-and-debt/late-payment-penalties))

An invoice-basis trader returned GST on a $1,150 sale. The customer is now insolvent and the debt is written off.

- Credit adjustment: $1,150 x 3/23 = $150 in Box 13 in the period of the write-off.
- If $1,150 is later recovered, $150 goes back as a debit adjustment.
- **Late payment.** Separately, the trader's $4,000 of GST for the period ending 30 September 2026 is due 28 October 2026 and is not paid on time.
  - A 1% penalty ($40) is added on 29 October.
  - On the 7th day after the due date, 4% of $4,040 = $161.60 is added.
  - Interest runs from the day after the due date.
  - No monthly penalty follows, because GST is excluded.

## Returns being filed now for 2025-26 ([Filing GST](https://www.ird.govt.nz/gst/filing-and-paying-gst-and-refunds/filing-gst); [Late filing penalties](https://www.ird.govt.nz/managing-my-tax/penalties-and-interest/penalties-and-debt/late-filing-penalties))

Periods ending on or before 31 March 2026 use the same rate (15%), the same $60,000 registration line, and the same bases and frequencies. Points that differ:

- **Due date.** The 2-monthly or 6-monthly period ending 31 March 2026 was due 7 May 2026. A return filed now is late: the late filing penalty is $50 on the payments basis or $250 on the invoice or hybrid basis, plus late payment penalties.
- **Interest.** IRD charged 9.89% and paid 3.27% from 8 May 2025 until the change on 16 January 2026 ([Interest](https://www.ird.govt.nz/managing-my-tax/penalties-and-interest/interest-on-overpayments-and-underpayments)).
- **Entertainment.** The adjustment for 2025-26 business entertainment is timed by the 2025-26 income tax return, under the timing rules in the entertainment section.
- **Change of use and errors.** Adjustments for the period ending at a 31 March 2026 balance date go in the first return after it. Correct 2025-26 errors under the rules in "Filing and payment".

## When to refuse or refer

- The client is in a GST group, or asks about the financial services zero-rating election.
- Land is bought or sold between registered persons (compulsory zero-rating), or a sale may be a going concern.
- A non-profit sells donated goods or services.
- A mixed-use holiday home, boat or aircraft, or any asset over $500,000 or land ([Change-in-use adjustments](https://www.ird.govt.nz/gst/gst-adjustments/change-in-use-adjustments-for-gst)) with changing use.
- An asset is being elected non-taxable, or a large accommodation owner is opting out of the marketplace rules.
- A business that makes exempt supplies receives services from overseas (reverse charge).
- Secondhand goods are bought from an associated person, or supplies are made to associated persons.
- Turnover is at exactly $60,000 ([Registering for GST](https://www.ird.govt.nz/gst/registering-for-gst)), or a change-of-use adjustment is exactly $1,000. IRD's own documents word these tests differently.
- Zero-rating of services where the non-resident's staff or goods were in New Zealand.
- A non-resident's NZ registration.
- A default assessment, audit, dispute, or an error too large to correct in a later return.
- The income tax side of any item (entertainment limits, vehicle logbooks, provisional tax): send to the matching income tax Guide.

## Filing and payment ([Filing GST](https://www.ird.govt.nz/gst/filing-and-paying-gst-and-refunds/filing-gst); [Paying GST](https://www.ird.govt.nz/gst/filing-and-paying-gst-and-refunds/paying-gst); [IR375](https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir300---ir399/ir375/ir375.pdf))

- **Due date.** The 28th of the month after the period ends. The two exceptions are a period ending 31 March (due 7 May) and a period ending 30 November (due 15 January). If the due date falls on a weekend or public holiday, it moves to the next working day.
- **Payment** is due the same day as the return.
- **Every period** needs a return, even a nil one. There is no extension of time to file.
- **How to file:** in myIR, through accounting software that files with IRD, or on paper.
- **No return filed.** IRD may issue a default assessment, usually higher than the real amount. The return must still be filed.
- **Errors.** An error can be corrected in the next return, instead of amending the original, where the total discrepancy is $1,000 or less, or where it is no more than the lower of $10,000 and 2% of the GST collected (and the delay is not deliberate). An unclaimed input tax deduction can be included in a later return if it is within 2 years of when it was left out, or, with no time limit stated in IR375, if the delay was caused by one of the reasons IR375 lists (for example, no invoice could be obtained, the amount was disputed, or a clear mistake or simple oversight). Otherwise amend the return in myIR, or use the disputes process (Notice of proposed adjustment IR770 within 4 months of the return's due date) where a chosen tax position is being changed.
- **Records.** Keep them for 7 years: TSI, supply correction information, bank statements and the cashbook.

## Completion checklist

- [ ] Registration tested on the past and forward 12 months, provisos considered, exact-line cases referred.
- [ ] Basis and frequency confirmed and still available; large single supplies checked.
- [ ] Every sale classified, with evidence for each zero-rating.
- [ ] Every claim backed by TSI for its band; private and exempt use removed.
- [ ] Secondhand goods paid for and fully recorded.
- [ ] Adjustments worked out and put in Box 9 or Box 13.
- [ ] Boxes 5 to 15 complete, GST101A or GST103 as appropriate, amounts GST-inclusive.
- [ ] Filed and paid by the due date, moved to the next working day if needed.
- [ ] Records kept for 7 years.

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
