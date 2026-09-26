---
name: pa-sales-tax
description: Use this skill whenever asked about Pennsylvania sales and use tax, PA DOR filings, Pennsylvania clothing exemption, Philadelphia sales tax, Allegheny County tax, or any request involving Pennsylvania state sales and use tax compliance. Trigger on phrases like "Pennsylvania sales tax", "PA sales tax", "PA DOR", "PA-3", "Philadelphia tax", "Pennsylvania clothing exemption", or any request involving Pennsylvania sales tax. ALWAYS read this skill before touching any Pennsylvania sales tax work.
version: 2.0
jurisdiction: US-PA
tax_year: 2026
last_updated: 2026-09-25
authored_by: OpenAccountants team
review_status: pending_review
trust_label: By OpenAccountants
depends_on:
  - us-sales-tax
category: us-states
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Pennsylvania sales and use tax: 2026 collection, nexus and filing

Figures are for tax year 2026, as they stand on 25 September 2026. They come from the Pennsylvania Department of Revenue (DOR) at pa.gov. The biggest 2026 change is the local tax in Philadelphia and Allegheny County: Act 21 of 2026 moved it to destination sourcing for tax years after 31 December 2025, and DOR will begin enforcing that from 1 October 2026. A short section covers 2025 periods, when the old rule applied.

## Scope and who this is for

- Businesses that sell goods, digital products or taxable services to customers in Pennsylvania, and must decide what to charge, whether local tax applies, and how to file.
- Out-of-state sellers deciding whether they must register (remote sellers, marketplace sellers, marketplace facilitators).
- Businesses that owe use tax because no Pennsylvania sales tax was charged on their purchases.
- Sellers accepting or giving exemption certificates (REV-1220).
- Out of scope: hotel occupancy tax and booking agents, the Public Transportation Assistance (PTA) taxes and fees on tires and vehicle leases, vehicle rental tax, consumer fireworks tax, motor vehicle sales registered through PennDOT, and construction contractor rules beyond the short note below. Philadelphia's own city taxes (other than the local sales tax) are also out of scope.

## Ask the client first

- Where is the business located? Does it have any physical presence in Pennsylvania: staff, an office, inventory (including stock held in a fulfillment center), or property?
- If it is outside Pennsylvania: what were its gross sales into Pennsylvania in the previous calendar year, counting all channels and both taxable and nontaxable sales?
- Does it sell through a marketplace facilitator? Does that facilitator collect Pennsylvania tax on its behalf?
- What exactly does it sell? Goods, clothing (everyday, formal, sporting), food (grocery or ready-to-eat), canned software, SaaS, custom software, digital downloads or streaming, or services such as building cleaning, lawn care, pest control, staffing or repair?
- Where does each customer receive the goods or service? In particular, is the delivery address in Philadelphia or in Allegheny County?
- Does it hold a Sales, Use and Hotel Occupancy Tax License, and what filing frequency has DOR assigned (monthly, quarterly, semi-annual, or monthly with prepayments)?
- Does it use a Certified Service Provider (CSP)?
- Does it sell to exempt buyers (resellers, charities, government, manufacturers) and does it hold a properly completed REV-1220 for each?
- Has it bought anything taxable for use in Pennsylvania without paying Pennsylvania sales tax?
- Were any returns filed or paid late, and does it make payments of $1,000 or more ([REV-717](https://www.pa.gov/content/dam/copapwp-pagov/en/revenue/documents/formsandpublications/formsforbusinesses/sut/documents/rev-717.pdf))?

## The method, step by step

1. **Decide whether the seller must be licensed and collect.** A business with physical presence in Pennsylvania must get a license before making taxable sales. A business with no physical presence must collect if its gross sales into Pennsylvania in the previous calendar year passed the $100,000 economic presence threshold ([DOR online retailers](https://www.pa.gov/agencies/revenue/resources/tax-types-and-information/sales-use-and-hotel-occupancy-tax/online-retailers); see below). A business with neither has no Pennsylvania sales tax obligation.
2. **Classify each sale.** Is it tangible personal property (which includes canned software and digital products), or one of the enumerated taxable services? Then check exemptions: most clothing, grocery food, candy and gum, prescription drugs, textbooks, residential heating fuels, sales for resale, and sales to exempt buyers with a certificate.
3. **Find the rate.** The state rate is 6% everywhere. Add 1% for delivery to a customer in Allegheny County, or 2% for delivery in Philadelphia ([DOR sales tax page](https://www.pa.gov/agencies/revenue/resources/tax-types-and-information/sales-use-and-hotel-occupancy-tax)).
4. **Collect tax on the full purchase price.** No deduction is allowed for labor, shipping, handling, delivery or installation. A separately stated deposit for returnable containers is not taxed.
5. **Check your own purchases.** Accrue use tax on any taxable purchase used in Pennsylvania on which no Pennsylvania sales tax was paid.
6. **File the return in myPATH by the 20th** after the period ends, even if you had no sales. Pay in full on time to keep the vendor discount. Payments of $1,000 or more must be made electronically ([REV-717](https://www.pa.gov/content/dam/copapwp-pagov/en/revenue/documents/formsandpublications/formsforbusinesses/sut/documents/rev-717.pdf)).
7. **Keep every exemption certificate for at least four years** from the date of the exempt sale.

## Rates and thresholds for 2026

### Rates ([DOR sales, use and hotel occupancy tax](https://www.pa.gov/agencies/revenue/resources/tax-types-and-information/sales-use-and-hotel-occupancy-tax))

| Item | 2026 value | Source |
| --- | --- | --- |
| State sales and use tax | 6% | [DOR sales tax page](https://www.pa.gov/agencies/revenue/resources/tax-types-and-information/sales-use-and-hotel-occupancy-tax): "The Pennsylvania sales tax rate is 6 percent." |
| Allegheny County local tax | 1% (combined 7%) | Same page: "a 1 percent local tax is added to purchases made in Allegheny County" |
| Philadelphia local tax | 2% (combined 8%) | Same page: "2 percent local tax is added to purchases made in Philadelphia" |
| Use tax | Same as sales tax: 6% plus 1% (Allegheny) or 2% (Philadelphia) | [DOR use tax](https://www.pa.gov/agencies/revenue/resources/tax-types-and-information/sales-use-and-hotel-occupancy-tax/use-tax) |

Only Allegheny County and Philadelphia levy a local sales tax. The highest combined rate is therefore 8%, in Philadelphia.

### Local tax sourcing from 2026 ([DOR local sales tax](https://www.pa.gov/agencies/revenue/resources/tax-types-and-information/sales-use-and-hotel-occupancy-tax/local-sales-tax))

- **The rule.** Act 21 of 2026 requires vendors that already collect the 6% state tax to collect Philadelphia's 2% and Allegheny County's 1% on taxable sales to customers in those counties.
- **Destination, not origin.** Before the change, local tax was generally based on the point of sale, meaning where the vendor was located. It is now based on the point of destination, where the product or service is delivered.
- **Dates.** The Act became law on 12 July 2026, with a retroactive effective date of tax years after 31 December 2025. DOR will not begin enforcing the new rules until 1 October 2026.
- **January to September 2026.** The law is retroactive, but DOR has said it will not enforce before 1 October 2026. For sales in that window where local tax was not collected under the old origin rule, the buyer still owes local use tax. DOR's page does not say how the January to September 2026 periods will be treated. Confirm the position with DOR (717-787-1064) before changing any filed 2026 return.
- **Use tax is unchanged.** If sales tax is not collected, a buyer who uses taxable items or services in Philadelphia or Allegheny County owes local use tax.
- **Finding the county.** DOR points vendors to public ZIP code and USPS address tools.

DOR's Retailer's Information booklet (REV-717, revised 02-26) still describes the old origin rule and voluntary collection. The DOR local sales tax page reflects Act 21 and is the later source; follow it.

### Who must be licensed and collect ([DOR online retailers](https://www.pa.gov/agencies/revenue/resources/tax-types-and-information/sales-use-and-hotel-occupancy-tax/online-retailers))

| Seller | Rule |
| --- | --- |
| Any business with physical presence (office, staff, inventory, property) | Must be licensed and collect. Inventory in a Pennsylvania fulfillment center counts ([DOR tax obligations for online retailers](https://www.pa.gov/agencies/revenue/resources/tax-types-and-information/tax-obligations-for-online-retailers)). |
| Remote seller (no physical presence) | Must register, collect and remit if its Pennsylvania gross sales in the previous calendar year were more than $100,000. |
| Marketplace facilitator with no physical presence | Counts both facilitated sales and its own direct sales against the $100,000 threshold. Once over it, it collects on all sales it facilitates into Pennsylvania, including for sellers that have no nexus themselves. |
| Marketplace seller with no physical presence | Counts only its direct sales plus sales through a facilitator that does **not** collect Pennsylvania tax for it. Sales on which the facilitator collects are left out. |
| Business with neither physical nor economic presence | No Pennsylvania sales tax obligation. Its Pennsylvania customers owe use tax. |

How the threshold works:

- **Amount.** DOR's guidance describes the threshold as gross sales of "greater than $100,000" (online retailers page), "more than $100,000" ([Bulletin 2019-01](https://www.pa.gov/content/dam/copapwp-pagov/en/revenue/documents/taxlawpoliciesbulletinsnotices/taxbulletins/sut/documents/st_bulletin_2019-01.pdf) and REV-717), and sales that "exceed $100,000 in the prior year". The same online retailers page also says "at least $100,000" in one sentence. DOR's formal guidance (Bulletin 2019-01 and REV-717) says "more than", so sales of exactly $100,000 most likely do not trigger collection. Because the web page also says "at least", get written confirmation from DOR before relying on that.
- **What counts.** All channels, taxable and nontaxable sales alike. There is no transaction-count test.
- **Lookback period.** The previous calendar year, reviewed year by year. DOR: "The sales threshold of $100,000 will be measured by calendar year. After the first year, collection will begin in the second quarter."
- **Collection window.** Calendar year 2025 sales decide whether a remote seller collects from 1 April 2026 through 31 March 2027. Calendar year 2026 sales decide the window from 1 April 2027 through 31 March 2028.
- **No mid-year trigger.** A remote seller that passes $100,000 partway through 2026 is not required by this test to start collecting until 1 April 2027. It must still register earlier if it gains physical presence.
- **Start dates.** Economic presence and marketplace facilitator collection both started on 1 July 2019 (Act 13 of 2019). The election to send customers use tax notices instead of collecting is no longer available to a seller with economic presence.
- **Certified Service Provider option.** A vendor with no physical presence may use a DOR-approved CSP instead. While it keeps using the CSP, it does not need its own Pennsylvania license or returns. DOR lists Avalara, Sovos and TaxCloud.
- **Marketplace sellers with inventory here.** A seller with inventory in Pennsylvania must collect on its direct sales. It must also collect on sales through a marketplace facilitator if that facilitator does not collect.

### Filing frequency ([REV-717](https://www.pa.gov/content/dam/copapwp-pagov/en/revenue/documents/formsandpublications/formsforbusinesses/sut/documents/rev-717.pdf) and [2026 REV-819](https://www.pa.gov/content/dam/copapwp-pagov/en/revenue/documents/formsandpublications/formsforbusinesses/sut/documents/2026_rev-819.pdf))

DOR assigns the frequency from the licensee's actual tax liability. The thresholds are:

| Frequency | Actual tax liability | Return due |
| --- | --- | --- |
| Monthly with prepayment, AST Level 2 | $100,000 or more for the third calendar quarter of the preceding year | Prepayment by the 20th of the current month; return by the 20th of the following month |
| Monthly with prepayment, AST Level 1 | At least $25,000 but less than $100,000 for the third calendar quarter of the preceding year | Same as Level 2 |
| Monthly | Less than $25,000 but greater than $600 per quarter | 20th of the following month |
| Quarterly | Less than $600 per quarter but greater than $300 annually | 20th of the month after the quarter |
| Semi-annual | $300 or less annually | 20 August (January to June) and 20 February (July to December) |

Boundary points:

- **Exactly $600 a quarter** falls between DOR's "greater than $600" (monthly) and "less than $600" (quarterly) wording. Follow the frequency DOR has assigned to the account.
- **Exactly $25,000** is AST Level 1, because the test reads "$25,000 but less than $100,000".
- **Exactly $100,000** is AST Level 2.
- **What the prepayment is.** AST Level 1 may pay either 50% of the liability for the same month of the prior year, or at least 50% of the actual liability for the current month. AST Level 2 must pay 50% of the liability for the same month of the prior year, with no alternative ([DOR AST prepayments](https://www.pa.gov/agencies/revenue/resources/tax-types-and-information/sales-use-and-hotel-occupancy-tax/accelerated-sales-tax-ast-prepayments)). The current month's prepayment and the prior month's liability are separate payments.

## What is taxable: boundary and exception table

### Goods, food and clothing ([DOR sales tax page](https://www.pa.gov/agencies/revenue/resources/tax-types-and-information/sales-use-and-hotel-occupancy-tax); [REV-717](https://www.pa.gov/content/dam/copapwp-pagov/en/revenue/documents/formsandpublications/formsforbusinesses/sut/documents/rev-717.pdf))

DOR: "Major items exempt from the tax include food (not ready-to-eat); candy and gum; most clothing; textbooks; pharmaceutical drugs; sales for resale; and residential heating fuels such as oil, electricity, gas, coal and firewood."

| Item | Treatment | Condition or exception |
| --- | --- | --- |
| Tangible personal property in general | Taxable | Unless a specific exemption applies |
| Everyday clothing and shoes | Exempt | Includes work clothes, everyday boots and shoes, sneakers, lingerie, T-shirts |
| Formal day or evening apparel | Taxable | For example tuxedos, prom dresses, bridal apparel, formal ties, formal shoes |
| Fur articles | Taxable | When real, imitation or synthetic fur is worth more than three times the next most valuable component |
| Sporting clothing and goods | Taxable | Clothing normally worn only for sport (for example uniforms, swimsuits, ballet shoes); running shoes, gym suits and warm-up suits are exempt |
| Accessories and ornamental wear | Taxable | For example umbrellas, costumes, corsages |
| Clothing repair, alteration, dry cleaning | Exempt | Services on taxable items other than clothing and shoes are taxable |
| Grocery food | Exempt | "Food (not ready-to-eat)" |
| Candy and gum | Exempt | Listed as nontaxable by DOR |
| Soft drinks, sports drinks, flavored water, hot coffee, sandwiches, hot food, self-service salad bars | Taxable | Even when sold by a grocery, deli or convenience store |
| Plain water, milk, coffee beans, cold bottled coffee, tea (except hot tea) | Exempt | When sold from a grocery or similar store |
| Food and drink from a restaurant, caterer or other ready-to-eat establishment | Taxable | Covers consumption on or off the premises, take-out and delivery, unless specifically exempt |
| Prescription drugs and medical supplies | Exempt | See REV-717 Category 19 for detail |
| Textbooks | Exempt | Only when sold by a school or an authorized book store. Other books, including e-books, are taxable |
| Residential heating fuels, electricity, gas, basic phone service | Exempt | The same fuels and services for commercial use are taxable |
| Property used directly and predominately in manufacturing, processing, farming, dairying, mining, printing or a public utility service | Exempt | Motor vehicles that must be registered are excluded. The buyer gives a REV-1220 |
| Sales for resale | Exempt | With a REV-1220 showing the buyer's License ID |

### Canned software, SaaS and digital products ([DOR canned software and digital goods](https://www.pa.gov/agencies/revenue/resources/tax-types-and-information/sales-use-and-hotel-occupancy-tax/canned-computer-software-digital-goods); [DOR digital products Q&A](https://www.pa.gov/content/dam/copapwp-pagov/en/revenue/documents/taxtypes/sut/documents/digital_products_tax_qa.pdf))

- **Canned software is taxable.** This applies whether it comes on a disc, by download, by streaming, or through a SaaS agreement. Act 84 of 2016 put in the statute "canned software, notwithstanding the function performed, including support, except separately invoiced help desk or call center support". DOR adds a condition: separately stated help desk or call center charges are non-taxable only "where the vendor does not access the software". Support where the vendor does access the software is taxable.
- **Custom software is not taxable.** Neither are services related to it. Custom software is "designed, created and developed for and to the specifications of an original purchaser." The exemption is tied to that original purchaser.
- **Services on canned software are taxable.** Configuring or modifying canned software is a taxable alteration of tangible personal property, whether or not it is sold with the software. Labor or services needed to make canned software work are part of the taxable purchase price.
- **Labels do not change the answer.** Calling canned software a "service" does not make it nontaxable. DOR looks at invoices, contracts and statements of work. If a bill mixes taxable and nontaxable parts, the records must show which is which.
- **Digital products are taxable.** Examples are e-books, streamed or downloaded video and music, apps and in-app purchases, games, photographs, e-greeting cards, satellite radio and streaming subscriptions.
- **Sourcing.** For state tax, a digital product is sourced to the customer's billing address on file. Digital products delivered to customers outside Pennsylvania are not taxed.
- **Exemptions.** Digital products get the same exemptions as physical goods, for example resale or purchases by a qualifying charity.
- **Licenses used outside Pennsylvania.** Remotely accessed software is taxed where the user is. If the billing address is in Pennsylvania, all users are presumed to be in Pennsylvania. The buyer can rebut this on REV-1220 (reason 7), giving the number of licenses and the number of users outside Pennsylvania, but only under these conditions:
  - Only licenses for the buyer's own employees who use the software exclusively outside Pennsylvania can be allocated out. DOR: "the purchaser may only allocate licenses to out-of-state users if the users are employees of the purchaser."
  - Users who are contractors, customers or employees of another entity cannot be allocated out; the buyer is treated as the end user (unless it actually resells the licenses).
  - Licenses bought in excess of the number of users, with a Pennsylvania billing address, stay taxable as unallocated licenses.

### Enumerated taxable services ([REV-717, Additional Services Subject to Tax](https://www.pa.gov/content/dam/copapwp-pagov/en/revenue/documents/formsandpublications/formsforbusinesses/sut/documents/rev-717.pdf))

Most services are not taxable in Pennsylvania. The services below are taxable, generally when the service is delivered or benefits a customer in Pennsylvania. The buyer owes use tax if the vendor does not collect.

| Service | Condition |
| --- | --- |
| Repairing, altering, cleaning or installing parts on tangible personal property | Not for clothing or shoes, and not for work on real estate |
| Lobbying services | Delivery or benefit in Pennsylvania |
| Adjustment, collection and credit reporting services | Collection is taxable when the creditor does business in Pennsylvania and the debtor is here; credit reports when delivered here. Debt counseling for individuals is not taxable |
| Secretarial and editing services | Editing, proofreading, resume writing, typing, word processing. Court reporting and stenography are not taxable |
| Employment agency services | Temporary or permanent placement where the employee reports to or is assigned to work in Pennsylvania |
| Help supply services | Temporary staff supervised by the buyer, including employee leasing. Farm labor and human health-related services are excluded |
| Disinfecting and pest control services | On Pennsylvania real property, or on goods here (unless delivered out of state) |
| Building maintenance and cleaning services | Janitorial and routine maintenance in Pennsylvania. Building repair services are not taxable |
| Lawn care services | Mowing, fertilizing, applying herbicides, raking in Pennsylvania |
| Self-storage services | Self-storage located in Pennsylvania. Warehouses, safe deposit boxes and public lockers are excluded |
| Premium cable services | Delivered to a Pennsylvania location |
| Catering | Food and rentals used in the catering are taxable, even if separately stated |
| Telephone and cellphone services | Basic telephone service is exempt only for residential use |

### Construction contractors ([REV-717](https://www.pa.gov/content/dam/copapwp-pagov/en/revenue/documents/formsandpublications/formsforbusinesses/sut/documents/rev-717.pdf))

Contractors generally pay tax on all materials and equipment they furnish and install. The exception is "building machinery and equipment" transferred under a contract with an exempt entity, such as a purely public charity or a government body. For that, the contractor gives the vendor a certificate naming the exempt entity and its exemption number, with a list of the qualifying property attached. Refer anything beyond this.

## Use tax ([DOR use tax for businesses](https://www.pa.gov/agencies/revenue/resources/tax-types-and-information/sales-use-and-hotel-occupancy-tax/use-tax/use-tax-for-businesses))

- **When it is owed.** On any taxable goods or services delivered into or used in Pennsylvania where the seller did not charge Pennsylvania sales tax, for example internet, catalog or out-of-state purchases.
- **Rate.** Same as sales tax: 6%, plus 1% in Allegheny County or 2% in Philadelphia.
- **Base.** The whole purchase price, including shipping and handling charged by the seller.
- **Licensed businesses** report use tax on line 6 of their sales and use tax return. No vendor discount is allowed on use tax.
- **Other businesses** can file the online PA-1 Use Tax Return in myPATH. It is due, with payment, by the 20th of the month after the month of purchase. REV-717 puts it as the first 20 days of the month after the month of first taxable use in Pennsylvania.
- **Individuals** can report use tax annually on the PA-40 personal income tax return.
- **Late payment.** Use tax found on audit is assessed with penalty and interest.

## Exemption certificates: REV-1220 ([form REV-1220](https://www.pa.gov/content/dam/copapwp-pagov/en/revenue/documents/formsandpublications/formsforbusinesses/sut/documents/rev-1220.pdf); [REV-717](https://www.pa.gov/content/dam/copapwp-pagov/en/revenue/documents/formsandpublications/formsforbusinesses/sut/documents/rev-717.pdf))

- **Form types.** Use a unit certificate for one transaction, or a blanket certificate for repeat purchases from the same seller.
- **Common reasons.**
  - Direct and predominant use in manufacturing, farming or another listed operation.
  - An exempt organization holding an exemption number. Charities' numbers start with 75.
  - Resale under a License ID.
  - Public utility use.
  - Exempt wrapping supplies.
  - Canned software used outside Pennsylvania.
  - Other, explained in detail.
- **Good faith.** The seller is protected only if it accepts the certificate in good faith, which means all four of these:
  1. The certificate is completed properly.
  2. The seller has it within 60 days of the sale.
  3. It contains no information the seller knows is false.
  4. The property or service matches the exemption claimed.

  An invalid certificate can leave the seller liable for the tax.
- **When no certificate is needed.** Sales to governmental entities, sales of nontaxable property or services, and sales delivered outside Pennsylvania. The seller must still keep documentary evidence for these.
- **Records.** Keep each certificate for at least four years from the date of the exempt sale. Do not send it to DOR.
- **Exempt organizations** use REV-1220 with REV-1715 for purchases of $200 or more.
- **Wholesale certificate holders** may give a supplier REV-1220 for items they will resell. It does not cover items they consume.

## Worked cases ([DOR sales tax page](https://www.pa.gov/agencies/revenue/resources/tax-types-and-information/sales-use-and-hotel-occupancy-tax))

Rates are 6% state, plus 1% in Allegheny County or 2% in Philadelphia. Amounts are illustrative.

1. **Delivered sale into Philadelphia.** A Harrisburg retailer ships a $1,000 laptop to a customer in Philadelphia on 5 November 2026, after DOR's enforcement date. Destination sourcing applies. State tax is $1,000 × 6% = $60.00, local tax is $1,000 × 2% = $20.00, and the total is $80.00. If the customer instead collects it at the Harrisburg store, only state tax applies: $60.00.
2. **Clothing boundary in Pittsburgh (Allegheny County).** A $200 everyday jacket is exempt, so no tax is due. A $300 tuxedo is formal apparel and taxable at 7%: $300 × 7% = $21.00.
3. **Remote marketplace seller.** An Ohio seller has no physical presence in Pennsylvania. In calendar year 2025 its Pennsylvania sales were $120,000. Of that, $30,000 went through a marketplace facilitator that collects Pennsylvania tax for it, and $90,000 were direct sales (including exempt clothing). It counts only the $90,000 of direct sales. That is not more than $100,000, so it does not have to collect from 1 April 2026. If all $120,000 had been direct sales, it would be over the threshold and must collect from 1 April 2026 through 31 March 2027 (or use a CSP). The exempt clothing sales still count toward the threshold.
4. **SaaS and custom software.** A business outside Philadelphia and Allegheny County subscribes to canned SaaS for $500 a month: $500 × 6% = $30.00 a month. A separately invoiced help desk contract under which the vendor does not access the software is not taxable; if the vendor's staff log in to the software to fix problems, the support is taxable. $50,000 paid for software developed to that business's specifications is custom software, so no tax is due. A $4,000 charge to configure a canned package is taxable: $4,000 × 6% = $240.00.
5. **Vendor discount.**
   - A monthly filer collects $4,000 of tax for October 2026 and files and pays by 20 November 2026. 1% is $40.00, so the discount is limited to $25.
   - A quarterly filer collects $5,000 for the third quarter and files on time. 1% is $50.00, which is less than $75, so it keeps $50.00.
   - Filed late, neither gets any discount.
6. **Late return.** A monthly filer owes $2,000 for September 2026, due 20 October 2026. It files and pays on 1 December 2026. That is one full month plus a fraction of a month late, so two months count. The addition is 2 × 5% = 10% of $2,000 = $200.00, and the discount is lost. Interest at 7% for 2026 is charged daily: $2,000 × 42 days × 0.000192 = $16.13.
7. **Business use tax.** A Philadelphia business buys $3,000 of computers from a website that charges no Pennsylvania tax, delivered to its Philadelphia office. It owes $3,000 × 8% = $240.00 use tax, on line 6 of its sales tax return, with no discount.
8. **Resale certificate.** A Pittsburgh retailer buys stock for resale and gives its supplier a blanket REV-1220 showing its License ID. The supplier holds the certificate within 60 days and keeps it for four years, so it need not charge tax. If the retailer later takes some of that stock for its own use, it owes use tax on it.

## When to refuse or refer

- Audits, assessments and appeals. DOR generally has three years after a return is filed to assess, and longer for fraud or a failure to file. A petition for reassessment must be filed with the Board of Appeals within 60 days of the assessment's mailing date. Refer these to a Pennsylvania CPA, EA or tax attorney.
- Refund claims. A refund petition generally has to be filed within three years of the payment date. Refer.
- Construction contracts, building machinery and equipment, and Keystone Opportunity Zone exemptions.
- Mixed software deals that bundle canned and custom software with implementation services. The taxable share depends on the contracts.
- Sales made in Philadelphia or Allegheny County between 1 January and 30 September 2026 that were not taxed under the old origin rule. DOR's guidance does not address those periods directly; confirm the position with DOR.
- A remote seller whose prior-year Pennsylvania sales were exactly $100,000 ([DOR online retailers](https://www.pa.gov/agencies/revenue/resources/tax-types-and-information/sales-use-and-hotel-occupancy-tax/online-retailers)).
- Hotel occupancy, booking agents, vehicle leases and rentals, tires, and fireworks.
- A client with unfiled past periods. DOR runs voluntary compliance programs that may limit the lookback and waive penalties; refer before filing anything.

## Filing and payment

### License ([DOR sales tax page](https://www.pa.gov/agencies/revenue/resources/tax-types-and-information/sales-use-and-hotel-occupancy-tax); [REV-717](https://www.pa.gov/content/dam/copapwp-pagov/en/revenue/documents/formsandpublications/formsforbusinesses/sut/documents/rev-717.pdf))

- **Who needs one.** Any business that sells taxable items or performs taxable services needs a Sales, Use and Hotel Occupancy Retail Tax License before its first taxable sale. Register through the Pennsylvania Online Business Tax Registration in myPATH. Failing to be licensed can lead to a fine.
- **Conditions.** The license is issued or renewed only if all Pennsylvania returns are filed and all taxes paid. It renews automatically every five years if there are no outstanding filings or liabilities. A copy must be displayed at each place of business.
- **Related registrations.** A wholesaler that only sells to retailers holds a Wholesale Certificate and has no filing obligation. Out-of-state sole proprietors or partnerships selling in person in Pennsylvania without a permanent location need a Transient Vendor Certificate and must notify DOR in writing at least thirty days before entering.

### Due dates for 2026 ([2026 REV-819](https://www.pa.gov/content/dam/copapwp-pagov/en/revenue/documents/formsandpublications/formsforbusinesses/sut/documents/2026_rev-819.pdf))

Returns are due the 20th of the month after the period. If the 20th is a weekend or holiday, they are due the next business day. Returns must be filed even if there were no taxable sales.

| Filer | Periods and due dates |
| --- | --- |
| Monthly | January due 20 Feb 2026; May due 22 Jun 2026; August due 21 Sep 2026; September due 20 Oct 2026; October due 20 Nov 2026; November due 21 Dec 2026; December due 20 Jan 2027 |
| Monthly with prepayment | Prepayment due the 20th of the current month: for example September prepayment due 21 Sep 2026, December prepayment due 21 Dec 2026 |
| Quarterly | Q1 due 20 Apr 2026; Q2 due 20 Jul 2026; Q3 due 20 Oct 2026; Q4 due 20 Jan 2027 |
| Semi-annual | January to June due 20 Aug 2026; July to December due 22 Feb 2027 |

### How to file and pay ([REV-717](https://www.pa.gov/content/dam/copapwp-pagov/en/revenue/documents/formsandpublications/formsforbusinesses/sut/documents/rev-717.pdf))

- **Filing.** File and pay in myPATH (mypath.pa.gov), which is free. TeleFile (1-800-748-8299) is only for filers DOR has approved on a TeleFile Request Form. PA-3 paper forms cannot be downloaded.
- **Electronic payment.** Payments of $1,000 or more must be made by electronic funds transfer (ACH debit, ACH credit or credit card). Failing to do so can cost a penalty of 3% of the tax due, up to $500.
- **Credit sales.** Tax on credit sales must be remitted within 30 days of the date of sale.

### Vendor discount ([REV-717](https://www.pa.gov/content/dam/copapwp-pagov/en/revenue/documents/formsandpublications/formsforbusinesses/sut/documents/rev-717.pdf); [DOR sales tax discount Q&A](https://www.pa.gov/content/dam/copapwp-pagov/en/revenue/documents/taxtypes/sut/documents/sales_tax_discount_qa.pdf))

- **The cap.** For returns filed and paid on time, the discount is the lesser of 1% of tax collected or $25 for a monthly filer, $75 for a quarterly filer, or $150 for a semi-annual filer. These caps apply to periods ending after 1 August 2016. They add up to a $300 annual cap, so changing frequency does not raise the discount.
- **When it is lost.** No discount is given on a late return or payment, or on use tax.
- **Apportionment.** Where the cap applies, the discount is shared between state and local tax in proportion to the tax due for each.

### Penalties and interest ([REV-717](https://www.pa.gov/content/dam/copapwp-pagov/en/revenue/documents/formsandpublications/formsforbusinesses/sut/documents/rev-717.pdf); [REV-1611](https://www.pa.gov/content/dam/copapwp-pagov/en/revenue/documents/formsandpublications/otherforms/documents/rev-1611.pdf))

| Charge | 2026 rule |
| --- | --- |
| Late return (addition) | 5% of the tax due for each month or fraction of a month the return stays unfiled, up to 25% of the tax for the period. It is never less than $2 |
| Interest | 7% a year for 2025 and 2026, charged daily at 0.000192. Interest = late or unpaid tax × days late × daily rate |
| EFT failure | 3% of the tax due, up to $500 |
| Unpaid tax | If tax, interest and additions are not paid, DOR issues an assessment |
| Failure to collect | The seller is assessed for tax it should have collected, plus interest and penalties |

DOR sets the interest rate each 1 January at the rate set by the U.S. Secretary of the Treasury. Earlier years' rates differ (for example 8% for 2024), so use the year the tax was due. DOR has an online penalty and interest calculator.

## 2025 periods (for amended or audited 2025 returns) ([REV-717](https://www.pa.gov/content/dam/copapwp-pagov/en/revenue/documents/formsandpublications/formsforbusinesses/sut/documents/rev-717.pdf))

- **Unchanged from 2026.** The state rate (6%), the local rates (1% and 2%), the $100,000 economic presence test, the filing frequency thresholds, the discount caps and the late-return additions.
- **Local tax sourcing.** For 2025, local tax followed the old point-of-sale rule. Vendors located in Allegheny County or Philadelphia had to collect local tax. Vendors located elsewhere could collect it voluntarily, and buyers who received taxable items in those areas without local tax owed local use tax. Sales delivered out of state were not subject to local tax.
- **Remote seller window.** Calendar year 2024 sales decided whether a remote seller collected from 1 April 2025 through 31 March 2026.
- **Interest** on tax due in 2025 is 7%.

## Completion checklist ([DOR sales tax page](https://www.pa.gov/agencies/revenue/resources/tax-types-and-information/sales-use-and-hotel-occupancy-tax))

- [ ] Nexus decided: physical presence, or more than $100,000 of prior calendar year gross sales (all channels, taxable and nontaxable), with marketplace sales handled correctly.
- [ ] Licensed through myPATH before the first taxable sale (or a CSP engaged).
- [ ] Each product or service classified: clothing exceptions, food exceptions, canned vs custom software, enumerated services.
- [ ] Delivery address checked for Philadelphia (2%) or Allegheny County (1%) on sales from 1 October 2026, and the January to September 2026 position noted.
- [ ] Tax charged on the full purchase price, including delivery and labor.
- [ ] REV-1220 held for every exempt sale, received within 60 days, kept for four years.
- [ ] Use tax accrued on untaxed purchases and reported on line 6.
- [ ] Filing frequency confirmed against DOR's assignment; AST prepayments made if required.
- [ ] Return filed and paid by the 20th (or the next business day), including zero returns.
- [ ] Payments of $1,000 or more made electronically.
- [ ] Vendor discount taken only on timely returns and within the $25, $75 or $150 cap.
- [ ] Any late period costed: 5% per month up to 25% (at least $2) plus 7% interest.

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
