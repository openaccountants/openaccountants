---
name: mo-sales-tax
description: "Missouri sales/use: state and local rates, food/business tests, software delivery, remote-seller nexus, filing, consumer use and 2026 cash rounding."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/mo-sales-tax"
  jurisdiction: "US-MO"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# Missouri sales and use tax, 2026

> **General reference only.** Source-cited draft, not approved by an accountant. For US Treasury Circular 230 §10.37 purposes this is general reference material; a qualified professional must check the facts, current law and forms before filing or taking a position.

## Who this applies to

Missouri retailers, remote sellers/marketplace facilitators, and purchasers with Missouri use-tax exposure in 2026. Load `us-sales-tax` for common sales-tax concepts, then apply the Missouri rules here. Missouri has sales tax on tangible personal property and specifically enumerated services; a general assertion that all services or all Internet transactions are exempt is wrong. Register with DOR/MyTax Missouri and obtain the relevant retail sales or vendor/consumer use-tax account. Sales tax and vendor's use tax are different returns, not alternative names for the same transaction. [DOR sales filing FAQ](https://dor.mo.gov/faq/taxation/business/sales-tax-filing.html).

Economic collection began January 1,2023 under SB153; the old “last state” historical superlative is unnecessary to the filing decision. Physical presence, agents, property or other statutory nexus can require collection below the economic threshold. Missouri is not treated as an SST simplified single-rate filing jurisdiction here: use the actual Missouri rate and location system.

## Rates, bands and thresholds

| 2026 item | Rule | Official source |
| --- | --- | --- |
| General state sales/use rate | 4.225%, plus applicable local **sales or use** tax | [DOR sales/use tax](https://dor.mo.gov/taxation/business/tax-types/sales-use/); [2026 rate tables](https://dor.mo.gov/taxation/business/tax-types/sales-use/rate-tables/2026/) |
| Qualifying food state rate | 1.225%, plus applicable local tax; not a grocery exemption | [12 CSR10-110.990](https://dor.mo.gov/resources/official-final-rules/documents/12_CSR_10-110_990_Tax-Sales_of_Food.pdf) |
| Other food / full-rate category | 4.225% state plus local, subject to business/transaction classification | [Food rule](https://dor.mo.gov/resources/official-final-rules/documents/12_CSR_10-110_990_Tax-Sales_of_Food.pdf) |
| Local/combined rate | Actual transaction address and effective date; never assume a local rate or a statewide maximum | [2026 rate tables](https://dor.mo.gov/taxation/business/tax-types/sales-use/rate-tables/2026/) |
| Remote seller / facilitator threshold | **Exceeds 100,000** gross receipts from taxable deliveries of TPP into Missouri; statutory quarter-close preceding 12-month test | [144.605(2)(e)](https://revisor.mo.gov/main/OneSection.aspx?bid=49987&section=144.605); [remote FAQ](https://dor.mo.gov/faq/taxation/business/remote-seller-and-marketplace-facilitator.html) |
| Regular monthly return assignment | State tax 500 or more/month; local tax excluded from assignment calculation | [Sales filing FAQ](https://dor.mo.gov/faq/taxation/business/sales-tax-filing.html) |
| Annual return assignment | State tax less than 200/quarter; otherwise quarterly below monthly boundary | [Sales filing FAQ](https://dor.mo.gov/faq/taxation/business/sales-tax-filing.html) |
| Consumer use-tax filing | Annual cumulative taxable untaxed purchases exceeding 2,000; threshold is not an exemption from the first 2,000 | [Use filing FAQ](https://dor.mo.gov/faq/taxation/business/use-tax-filing.html) |
| Timely sales-tax allowance | 2% of tax due if return and payment timely; no consumer-use allowance | [Sales FAQ](https://dor.mo.gov/faq/taxation/business/sales-tax-filing.html); [use FAQ](https://dor.mo.gov/faq/taxation/business/use-tax-filing.html) |

DOR's filing-frequency FAQ uses the 4% regular/1% food **state component** for frequency assignment, rather than local tax or the whole combined rate, and its adjacent monthly/quarterly sentences overlap at exactly 500. Use the account's DOR-assigned frequency; request correction rather than self-switching. Accelerated large-seller remittance is a separate unresolved rule, not waived by this ordinary table.

## The base

Taxable sales generally include TPP unless a specific exemption applies. Retain invoices, adjustments, location codes and exemption certificates. Resale is an exemption when supported by actual resale facts and the proper certificate; nonprofit federal status alone is not Missouri sales-tax exemption. Manufacturing exemptions require qualifying machinery/materials/use and statutory scope, not simply a manufacturer's name on the invoice. Prescription drugs qualifying under the pharmacist/practitioner rule are exempt; over-the-counter products and medical devices have specific distinctions. [Taxability/exemptions FAQ](https://dor.mo.gov/faq/taxation/business/sales-use-tax-exemptions.html).

| Transaction | Missouri treatment / boundary | Official source |
| --- | --- | --- |
| General TPP and ordinary clothing | Taxable absent an applicable specific exemption/holiday | [Sales FAQ](https://dor.mo.gov/faq/taxation/business/sales-tax-filing.html) |
| Qualifying home-consumption food | Reduced 1.225% state rate, not exempt; assess retailer eligibility | [Food rule](https://dor.mo.gov/resources/official-final-rules/documents/12_CSR_10-110_990_Tax-Sales_of_Food.pdf) |
| Hot food ready for immediate consumption, alcohol, tobacco | Not qualifying reduced-rate food | [Food rule](https://dor.mo.gov/resources/official-final-rules/documents/12_CSR_10-110_990_Tax-Sales_of_Food.pdf) |
| Bakery food, including still warm from baking; qualifying vending food | Can qualify under the food rule | [Food rule](https://dor.mo.gov/resources/official-final-rules/documents/12_CSR_10-110_990_Tax-Sales_of_Food.pdf) |
| Canned software on CD/USB/physical medium | Taxable | [Software FAQ](https://dor.mo.gov/faq/taxation/business/sales-use-tax-exemptions.html) |
| Digitally delivered canned software or custom software | Not taxable; old downloaded-software taxable row corrected | [Software FAQ](https://dor.mo.gov/faq/taxation/business/sales-use-tax-exemptions.html) |
| Pure software access/subscription without tangible delivery | Analyze contract and any taxable bundled components; no universal “never taxable SaaS” prohibition | [Software FAQ](https://dor.mo.gov/faq/taxation/business/sales-use-tax-exemptions.html); [DOR ruling 8408, fact-specific](https://dor.mo.gov/rulings/show/8408) |
| Mandatory installation/maintenance/upgrades/training under software agreement | Can be taxable under the stated agreement rule | [Software FAQ](https://dor.mo.gov/faq/taxation/business/sales-use-tax-exemptions.html) |
| Separately stated repair labour / fabrication labour | Repair labour not taxable; fabrication/production labour taxable even separately stated | [Taxability FAQ](https://dor.mo.gov/faq/taxation/business/sales-use-tax-exemptions.html) |
| Professional services | Usually outside general TPP tax, but test enumerated services, TPP and bundles | [Sales tax scope](https://dor.mo.gov/faq/taxation/business/sales-tax-filing.html) |
| Manufacturing equipment / prescription drugs / resale | Exemption only when the applicable conditions and documentation are met | [Exemptions FAQ](https://dor.mo.gov/faq/taxation/business/sales-use-tax-exemptions.html) |

The food rule also tests the business: prepared-for-immediate-consumption receipts must be 80% or less of total receipts for its qualifying-food sales to receive the reduced state rate. Amusement/entertainment/recreation food generally uses full rate, with specified vending/campground-general-store exceptions. Food trucks use the full rate at their selling location. A single “all groceries versus all prepared food” rule loses these exceptions. [Food rule](https://dor.mo.gov/resources/official-final-rules/documents/12_CSR_10-110_990_Tax-Sales_of_Food.pdf); [food-truck FAQ](https://dor.mo.gov/faq/taxation/business/sales-use-tax-exemptions.html).

Compute tax on the correct receipts/base, including the exact treatment of discounts, refunds, freight, fabrication, taxable services and exemptions. For tax-included receipts, divide by 1+the applicable combined rate to recover taxable sales; do not multiply the tax-inclusive total by the rate. The use-tax statute excludes usual/customary separately stated delivery charges, but do not apply that isolated use-tax definition as a universal sales-tax freight rule. [Sales FAQ](https://dor.mo.gov/faq/taxation/business/sales-tax-filing.html); [144.605(8)](https://revisor.mo.gov/main/OneSection.aspx?bid=49987&section=144.605).

Beginning August 28,2026, cash totals may be rounded to the nearest five cents **after** all items, discounts and taxes. Credit/debit/noncash totals cannot use this rule. Exact tax reporting/remittance remains unchanged. Ending cents 01/02/06/07 round down;03/04/08/09 round up. Do not round taxable receipts first or claim cash rounding as a tax reduction. [Current sales FAQ](https://dor.mo.gov/faq/taxation/business/sales-tax-filing.html).

## Deadlines and filing

File through MyTax Missouri or the appropriate current form:53-1 sales,53-V vendor's use,53-C consumer's use. Individual nonbusiness consumer use uses 4340; the verified 2025-2026 cycle form is due April 15,2026, while final 2026 individual form instructions remain pending. Do not use the individual annual form for a business account. Active sales-license accounts file assigned zero returns even with no sales. [Sales FAQ](https://dor.mo.gov/faq/taxation/business/sales-tax-filing.html); [use FAQ](https://dor.mo.gov/faq/taxation/business/use-tax-filing.html); [2025 individual booklet](https://dor.mo.gov/forms/MO-1040%20Instructions_2025.pdf).

Ordinary monthly returns are due the last day of the following month; quarterly returns the last day of the month after quarter-end; annual returns January 31 following. Closed-day deadlines move to the next business day. Thus ordinary 2026 Q3 is due November 2,2026 and Q4/annual February 1,2027. Apply the actual assigned frequency and accelerated instructions where relevant. Consumer business-use accounts generally file quarterly; do not import employer MO-941 deadlines. [Sales/use filing FAQs](https://dor.mo.gov/faq/taxation/business/sales-tax-filing.html); [use FAQ](https://dor.mo.gov/faq/taxation/business/use-tax-filing.html).

Report each location's gross receipts, permitted adjustments and taxable receipts at its actual rate; do not report negative taxable sales for a location. Prior-period excess credits need an amended return and Form 472S refund/credit procedure rather than arbitrary negative current sales. A copy of the original return marked amended can be used as instructed. Reconcile books, POS, marketplace reports and tax paid. [Sales FAQ](https://dor.mo.gov/faq/taxation/business/sales-tax-filing.html).

## Penalties and interest

DOR's sales FAQ gives 5% late payment, or 5% for each late-filing month up to 25% where no return is filed. It calculates interest on unpaid tax, excluding the additions-to-tax amount, using the published annual rate and days/365 or 366. The calendar 2026 rate is 7% in the current DOR2026 tax publications; do not copy the FAQ's illustrative 4% as a current rate or assume 7% for 2027. Consumer use does not receive the 2% timely allowance. [Sales FAQ](https://dor.mo.gov/faq/taxation/business/sales-tax-filing.html); [2026 employer booklet, interest](https://dor.mo.gov/forms/4282_2026.pdf); [use FAQ](https://dor.mo.gov/faq/taxation/business/use-tax-filing.html).

## Cross-border points

Sales from an in-state Missouri selling location generally use that sales location; out-of-state deliveries subject to vendor's use tax use the Missouri destination/use location and **use-tax** local rate. The two local rates need not match. Multi-location order acceptance, drop shipments, leases, contractors and mobile sales have special sourcing facts; the old origin/destination shorthand is not a substitute for those rules. Export title passing outside Missouri can differ from title passing inside. [Sales FAQ](https://dor.mo.gov/faq/taxation/business/sales-tax-filing.html); [taxability FAQ, leases/exports/food trucks](https://dor.mo.gov/faq/taxation/business/sales-use-tax-exemptions.html).

For remote economic nexus,144.605(2)(e) first describes previous/current calendar-year receipts but then expressly requires checking the **preceding 12 months after each quarter closes**. This operational rule agrees with DOR's detailed example and resolves the FAQ opening's calendar-year shorthand. If taxable receipts exceed 100,000 for that period, begin collection within three months after quarter-close; collect for at least 12 months and continue while statutory nexus persists. No 200-transaction alternative is asserted. Include marketplace receipts when testing the seller's total; a seller solely through a collecting facilitator need not duplicate collection. Direct sales in addition to facilitator sales can require seller registration and direct-sales collection. Retain evidence the facilitator collected. [Statute](https://revisor.mo.gov/main/OneSection.aspx?bid=49987&section=144.605); [remote FAQ](https://dor.mo.gov/faq/taxation/business/remote-seller-and-marketplace-facilitator.html).

A purchaser may owe consumer use tax where a seller did not collect. Once the annual 2,000 filing threshold is exceeded, tax applies to **all** taxable untaxed purchases, not just the excess; exemptions and eligible tax-already-paid credits still matter. State publications differ at exactly 2,000 (“exceeds” versus some business handouts' “equal to”), so the exact-boundary treatment remains flagged below; examples deliberately exceed it. Equipment brought across state borders, vehicles/aircraft, contractors, holidays, specialized products and municipal use-tax adoption need their own current facts. [Use FAQ](https://dor.mo.gov/faq/taxation/business/use-tax-filing.html).

## Two worked examples that recompute

**Food classification decision.** Invented qualifying grocery business sells 200 of qualifying home food and 200 of full-rate nonfood goods before tax. Assume the official address/date lookup gives an applicable local sales rate 2% for both classes. Food tax is 200 x (1.225%+2%)=6.45; nonfood tax is 200 x (4.225%+2%)=12.45; total tax 18.90, invoice 418.90. Treating both classes at full rate would overcharge 6.00. The 2% is an invented location input for arithmetic, not a claimed current city rate; replace it with actual DOR lookup.

```oa-check
name: Missouri qualifying food classification decision
inputs:
  food: 200
  nonfood: 200
  validated_local_rate: 0.02
steps:
  - food_tax: food * (0.01225 + validated_local_rate)
  - nonfood_tax: nonfood * (0.04225 + validated_local_rate)
  - tax: round(food_tax + nonfood_tax, 2)
  - overcharge: round(food * (0.04225 - 0.01225), 2)
  - invoice: food + nonfood + tax
expected:
  tax: 18.9
  overcharge: 6
  invoice: 418.9
```

**Consumer-use threshold.** Invented purchaser has 3,000 of taxable untaxed purchases for Missouri use and no exemption or eligible tax-paid credit. Assume validated local use rate 2%. Entire 3,000 is taxable:186.75. Taxing only the 1,000 above the filing threshold would underpay 124.50. No 2% consumer-use timely discount is taken.

```oa-check
name: Missouri consumer use threshold is not exclusion
inputs:
  taxable_purchases: 3000
  filing_threshold: 2000
  validated_local_use_rate: 0.02
steps:
  - rate: 0.04225 + validated_local_use_rate
  - tax: round(taxable_purchases * rate, 2)
  - incorrect_excess_only: round((taxable_purchases - filing_threshold) * rate, 2)
  - underpayment: tax - incorrect_excess_only
expected:
  tax: 186.75
  incorrect_excess_only: 62.25
  underpayment: 124.5
```

## Ask the client first

1. Seller/purchaser role, physical presence, agents/inventory, exact transaction dates and Missouri selling/delivery/use addresses?
2. Quarterly trailing 12-month taxable receipts, direct versus facilitator channels, facilitator collection evidence and registration date?
3. Products/services, software delivery medium, bundles, food business receipts mix and exemption/resale certificates?
4. Gross/tax-inclusive receipts, discounts, refunds, separately stated charges and tax paid to other jurisdictions?
5. DOR-assigned frequency, account/location codes, outstanding returns/payments and any accelerated-remittance instruction?

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| 2026 state/local rate tables. Read for general state rate and effective-period location lookup; no approximate statewide maximum. | https://dor.mo.gov/taxation/business/tax-types/sales-use/rate-tables/2026/ | 2026-11-13 |
| Sales filing FAQ. Read for scope, forms, ordinary frequency/dates, zero returns, amendments, allowance, penalties and 2026 cash rounding. | https://dor.mo.gov/faq/taxation/business/sales-tax-filing.html | 2026-11-13 |
| Use filing FAQ. Read for vendor/consumer distinctions, threshold and no consumer-use allowance. | https://dor.mo.gov/faq/taxation/business/use-tax-filing.html | 2026-11-13 |
| Taxability and exemptions FAQ. Read for software delivery/services, leases/exports, labour, manufacturing, drugs, exemption documentation and food trucks. | https://dor.mo.gov/faq/taxation/business/sales-use-tax-exemptions.html | 2026-11-13 |
| Food rule 12 CSR10-110.990. Read for 1.225%/4.225%,80% business test, qualifying food, hot/bakery/vending and amusement exceptions. | https://dor.mo.gov/resources/official-final-rules/documents/12_CSR_10-110_990_Tax-Sales_of_Food.pdf | 2026-11-13 |
| 144.605. Read for quarter-close 12-month nexus test, collection period, physical nexus and use-tax base. | https://revisor.mo.gov/main/OneSection.aspx?bid=49987&section=144.605 | 2026-11-13 |
| Remote-seller/facilitator FAQ. Read for direct versus facilitated sales, threshold receipts and collection start. | https://dor.mo.gov/faq/taxation/business/remote-seller-and-marketplace-facilitator.html | 2026-11-13 |
| Software subscription ruling 8408. Read for fact-specific software-access analysis, not universal exemption of bundles. | https://dor.mo.gov/rulings/show/8408 | 2026-11-13 |
| 2026 employer tax booklet. Read for calendar 2026 DOR interest rate only. | https://dor.mo.gov/forms/4282_2026.pdf | 2026-11-13 |
| Final 2025 individual booklet. Read for 2025-2026 individual consumer-use filing cycle, distinct from business accounts. | https://dor.mo.gov/forms/MO-1040%20Instructions_2025.pdf | 2026-11-13 |

Not yet confirmed: exact 2,000 consumer-use boundary where official wording conflicts, accelerated large-seller remittance, final 2026 individual 4340 form, exact address/date local rates and local use-tax adoption, detailed multi-location/drop-ship/lease/contractor/freight/vehicle/aircraft/holiday/special-product rules and 2027 interest. Examples use assumed validated local inputs, never approximate statewide maxima.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `mo-sales-tax` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/mo-sales-tax. If neither is available, confirm every figure against the official source pages cited above before relying on it.
