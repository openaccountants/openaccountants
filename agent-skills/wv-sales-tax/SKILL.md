---
name: wv-sales-tax
description: "Use this skill whenever asked about West Virginia sales tax, WV use tax, West Virginia Tax Division filing, West Virginia SaaS tax, West Virginia service taxation, or West Virginia sales tax compliance. Trigger on phrases like \"West Virginia sales tax\", \"WV sales tax\", \"W.Va. Code §11-15\", \"WV Tax Division\", \"West Virginia SaaS\", \"West Virginia SST\", or any request involving West Virginia state and local sales and use tax compliance. ALWAYS load us-sales-tax first for federal context."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/wv-sales-tax"
  jurisdiction: "US-WV"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# West Virginia sales and use tax (2026)

**Circular 230 §10.37 disclosure:** This skill supplies general state-tax working papers from the sources below. It is not a professional approval. A qualified tax professional must review the facts, assumptions and outputs before filing.

**Answer first:** West Virginia generally taxes goods and services at 6%, with an additional 1% in listed municipalities. Exemptions matter: recognized professional services, qualifying capital-improvement contracting and prescription medicines are exempt; nonprescription medicines are taxable. [Municipal rate page](https://tax.wv.gov/business/salesandusetax/municipalsalesandusetax/pages/municipalsalesandusetax.aspx); [TSD 300](https://tax.wv.gov/Documents/TSD/tsd300.pdf).

## Scope

West Virginia consumers sales/service tax and use tax in 2026: physical and remote sellers, marketplace sellers and purchasers with untaxed purchases. Load `us-sales-tax` for the federal constitutional/nexus framework; use this skill for WV rules. This is not the special district excise-tax return, motor-fuel or DMV tax computation. Municipal B&O can apply separately.

## Ask the client first

1. Locations, staff, inventory, delivery addresses and first-use locations in West Virginia?
2. Gross WV sales and transaction counts for the current and preceding calendar years, including exempt sales?
3. Actual contracts: goods, recognized professional services, software/data processing, repair or capital improvement?
4. Marketplace collection reports, direct sales and documentation of facilitator-remitted tax?
5. Exemption certificates, direct-pay permits and the purchaser's actual use?
6. Registration, assigned filing frequency, purchases without tax and prior-period adjustments?

## The method, step by step

### Rates, bands and thresholds

| Item | Amount or rule | Official source |
| --- | --- | --- |
| General state rate | 6% on taxable sales and corresponding use-tax base | [CST-200CU instructions, Part 3](https://tax.wv.gov/Documents/CST/cst200cu.instructions.pdf) |
| Municipal rate | 1% in adopting municipalities; 7% combined general rate; test boundary and effective date | [Municipal table](https://tax.wv.gov/business/salesandusetax/municipalsalesandusetax/pages/municipalsalesandusetax.aspx) |
| Remote small-seller exception | Annual gross WV sales $100,000 or less AND fewer than 200 separate transactions; physical presence/voluntary collection excluded | [Remote-seller FAQ, small-seller determination](https://tax.wv.gov/Business/SalesAndUseTax/ECommerce/RemoteSellers/Pages/RemoteSellersAndWestVirginiaTax.aspx) |
| Return/payment due date | 20th after period; monthly unless an authorized less frequent filing applies | [CST-200CU instructions p.1](https://tax.wv.gov/Documents/CST/cst200cu.instructions.pdf) |
| Quarterly eligibility | Annual aggregate $3,000 or less | [CST-200CU instructions p.1](https://tax.wv.gov/Documents/CST/cst200cu.instructions.pdf) |
| Annual eligibility | Annual aggregate $600 or less | [CST-200CU instructions p.1](https://tax.wv.gov/Documents/CST/cst200cu.instructions.pdf) |
| E-file requirement in current linked return instructions | Prior-year tax paid more than $25,000; also more than 10 municipalities | [CST-200CU instructions pp.1-2](https://tax.wv.gov/Documents/CST/cst200cu.instructions.pdf) |
| Records | At least 3 years, and longer while period is open for assessment/refund | [TSD 345 p.2](https://tax.wv.gov/Documents/TSD/tsd345.pdf) |

The remote-seller FAQ contains conflicting introductory AND/OR wording and a boundary reference to reaching $100,000. Its specific "How is the small-seller exception determined?" answer uses $100,000 or less AND fewer than 200 transactions; use that explicit test and refer a seller exactly on the dollar boundary for written confirmation. It includes taxable and nontaxable sales. Re-test the preceding calendar year and the current year; after a threshold is met, the FAQ requires collection on sales after that day. A seller making only nontaxable sales need not register to collect sales tax solely because of the threshold. [Remote-seller FAQ](https://tax.wv.gov/Business/SalesAndUseTax/ECommerce/RemoteSellers/Pages/RemoteSellersAndWestVirginiaTax.aspx).

### Taxability and exceptions

| Old topic retained | 2026 treatment and condition | Source |
| --- | --- | --- |
| Tangible goods and clothing | Generally taxable unless a specific exemption applies; retail clothing is not categorically exempt | [TSD 345 p.1](https://tax.wv.gov/Documents/TSD/tsd345.pdf) |
| Grocery food, prepared food, candy, soft drinks | Qualifying food/ingredients are exempt, including candy and dietary supplements meeting the food definition; prepared food, vending-machine food and soft drinks remain taxable. Apply the statutory definitions, including seller heating/mixing/utensil tests and exceptions | [§11-15-3a](https://code.wvlegislature.gov/11-15-3a/), [§11-15-3b](https://code.wvlegislature.gov/11-15-3b/), [§11-15B-2(b)](https://code.wvlegislature.gov/11-15B-2/) |
| Prescription medicines, DME, mobility aids and prosthetics | Exempt when dispensed on a qualifying prescription for diagnosis/cure/mitigation/treatment/prevention; insulin also exempt. No blanket exemption for all equipment | [TSD 300 pp.1-2](https://tax.wv.gov/Documents/TSD/tsd300.pdf) |
| OTC drugs and supplements | Nonprescription medications are taxable; distinguish a drug from a qualifying dietary supplement/food. Illustration (derived, invented inputs, not from the pages): a $25 OTC medicine plus a $20 qualifying supplement; $25 is taxable, state-only tax at 6% is $1.50, total $46.50 | [TSD 300 p.2](https://tax.wv.gov/Documents/TSD/tsd300.pdf); [TSD 345 p.2, pharmacy sales](https://tax.wv.gov/Documents/TSD/tsd345.pdf) |
| Lawyers, CPA accounting, engineers, architects and doctors | Recognized professional services are per-se exempt; the professional's own business purchases generally remain taxable. The old legal and tax-preparation examples incorrectly charged tax | [TSD 300 p.2](https://tax.wv.gov/Documents/TSD/tsd300.pdf) |
| Haircuts, manicures, massage | Personal services to the person exempt; ordinary physical-fitness programs generally are not, while personalized fitness services are exempt | [TSD 300 p.2](https://tax.wv.gov/Documents/TSD/tsd300.pdf) |
| Repairs, maintenance, cleaning, security, web/IT services and consulting | Taxable-services presumption applies, but determine professional, personal, data-processing and other exemptions before taxing a contract. Never characterize every consultant as a recognized professional | [TSD 300; TSD 345](https://tax.wv.gov/Documents/TSD/tsd300.pdf) |
| Custom software | Explicitly included in CST-200CU reporting; classify with any related exempt data-processing service before concluding | [CST-200CU p.1](https://tax.wv.gov/Documents/CST/cst200cu.instructions.pdf) |
| SaaS, canned software, digital downloads and streaming | The legacy blanket taxable rule is not sufficiently confirmed for every delivery model. Data-processing services and related software have a specific exemption. Contract-by-contract review required; see unconfirmed list | [TSD 300 p.4](https://tax.wv.gov/Documents/TSD/tsd300.pdf) |
| Manufacturing equipment/materials/utilities | Direct-use equipment, supplies, materials and services can qualify; incidental/convenient uses do not. Follow the applicable certificate, refund or direct-pay procedure; no blanket business-input exemption | [TSD 300 p.3](https://tax.wv.gov/Documents/TSD/tsd300.pdf) |
| Agriculture: machinery, feed, seed, fertilizer, breeding livestock | Commercial-production purchases can qualify; construction/permanent real-property improvements are excluded from that general category. Verify direct production purpose and documentation | [TSD 300 p.2](https://tax.wv.gov/Documents/TSD/tsd300.pdf) |
| Government, nonprofits, schools and financial institutions | Status alone is not enough. Government billing/payment and nonprofit statutory conditions matter. Credit unions are separately identified; do not assume every bank or nonprofit is exempt | [TSD 300 pp.1,4](https://tax.wv.gov/Documents/TSD/tsd300.pdf) |
| Advertising and media buying | Listed broadcast time, preprinted circulars, outdoor space and newspaper/magazine advertising are per-se exempt. Agency consulting, digital-advertising and bundled services need separate classification; old all-advertising-taxable assertion withdrawn | [TSD 300 p.1](https://tax.wv.gov/Documents/TSD/tsd300.pdf) |
| Transportation and telecommunications | Regulated public services and interstate passenger transport have specified exemptions; mobile/paging and unregulated services are not automatically exempt | [TSD 300 p.2](https://tax.wv.gov/Documents/TSD/tsd300.pdf) |
| Educational services | Schools/camp tuition and qualifying organizations have specific exemptions; the old all-nonprofit-education assertion needs the actual transaction conditions | [TSD 300 pp.1,4](https://tax.wv.gov/Documents/TSD/tsd300.pdf) |

### Construction classification before charging tax

A capital improvement substantially adds value or prolongs useful life, becomes permanently part of the real property so removal causes material damage, and is intended to remain permanently/indefinitely. Such contracting charges are exempt, while the contractor generally pays tax on its inputs. Non-capital-improvement repair, maintenance or installation is taxable on labor and materials; physically transferred resale parts/materials may qualify for resale. [TSD 310 p.1](https://tax.wv.gov/Documents/TSD/tsd310.pdf).

The old $200,000 Charleston renovation case cannot be taxed without that classification. If it is a qualifying capital improvement, no tax is collected on the contract; inputs are generally taxable. If it is taxable repair and no exemption applies, $200,000 x 7% = $14,000. The July 2026 TSD 310 also identifies a new July 1, 2026 public-school-facility exemption for directly used/consumed services and building materials, with F0003 or CST-240 procedure. It is not an exemption for every contractor purchase. [TSD 310 p.1](https://tax.wv.gov/Documents/TSD/tsd310.pdf).

### Sourcing, registration and marketplace sales

Source to receipt of the goods or first use of the service under the destination hierarchy, including customer pickup when receipt occurs at the shop. Check the municipal boundary and transaction date rather than relying on postal city/ZIP alone. The read municipal table names future 2027 changes too; do not apply them in 2026. Use the state boundary/rate files for the period. [Remote FAQ sourcing answer](https://tax.wv.gov/Business/SalesAndUseTax/ECommerce/RemoteSellers/Pages/RemoteSellersAndWestVirginiaTax.aspx); [municipal page](https://tax.wv.gov/business/salesandusetax/municipalsalesandusetax/pages/municipalsalesandusetax.aspx).

Register a physical-presence seller or remote seller required to collect through the state's online business-registration process, then activate the sales/use account in MyTaxes at https://mytaxes.wvtax.gov. WV participates in Streamlined Sales Tax registration and certified-provider filing; the state remote FAQ describes both routes. Registration is separate from classifying each sale. A qualifying facilitator collects for facilitated transactions; retain its reports and reconcile the marketplace deduction without omitting direct sales. The current return instructions explicitly include marketplace sales in gross sales and provide a deduction on Schedule D Part 1 line 14. Detailed facilitator eligibility thresholds are not confirmed here. [Remote FAQ](https://tax.wv.gov/Business/SalesAndUseTax/ECommerce/RemoteSellers/Pages/RemoteSellersAndWestVirginiaTax.aspx); [CST-200CU pp.3-5](https://tax.wv.gov/Documents/CST/cst200cu.instructions.pdf).

### The return, payment and use tax

1. Reconcile invoices and marketplace statements to gross WV sales. On CST-200CU line 1 column A enter gross sales including exempt and facilitator sales; line 1B deductions from Schedule D Part 1; 1C net taxable base; 1E tax.
2. Line 2 reports untaxed purchases for WV use, with allowed deductions in Schedule D Part 2. Credit lawfully paid other-state sales/use tax in Schedule D Part 3 up to the WV state liability on the same taxable purchase; municipal credits are separately limited to municipal use tax. Do not claim a credit on a WV-exempt item merely because another state charged tax.
3. Prepare Schedule M by municipality and FIPS code. Transfer municipal sales/use totals to return lines 3/4. Retain the period's actual form because the instructions' Schedule M column labels differ between narrative and transfer references; follow the current displayed form and reconcile totals.
4. Line 5 includes excess tax collected; lines 6/7 interest/additions; line 8 total; line 9 prior payment; lines 10/11 permitted credits; line 12 balance/credit. Negative use tax is not accepted. For prior sales adjustments/refunds/bad debts use the prescribed S/U/BD supplemental schedules and request review rather than netting unsupported refunds.
5. File for each assigned period, including zero periods (enter zero as instructed on lines 8/12). Pay by ACH debit/credit or an authorized method, save acceptance and payment confirmation, and reconcile the bank debit. Do not assume a timely-vendor discount: the read return gives no ordinary discount field. Retain returns, invoices, certificates and calculation workpapers. [CST-200CU pp.1-6](https://tax.wv.gov/Documents/CST/cst200cu.instructions.pdf).

The current CST instructions say annual returns are due the 20th; a remote FAQ answer says 30th. Use the current return's 20th-day instruction, which is earlier and agrees with its general answer, and flag the stale FAQ sentence. The old quarterly $150/$600 frequency bands are not supported by the current instructions.

## Boundary and exception table

| Situation | Action |
| --- | --- |
| Recognized professional service vs taxable IT consulting | Document actual work, professional status and separate goods/services |
| Exempt sale | Retain per-se proof or valid F0003/direct-pay documentation; never assume government/nonprofit status alone suffices |
| Exempt customer's contractor | Customer exemption does not automatically pass through; apply the specified construction exceptions |
| Untaxed remote purchase | Purchaser use tax remains even when the seller is a small seller |
| Manufacturer or agricultural business | Separate direct-use/production items from administration, construction and incidental inputs |
| Audit, voluntary disclosure, abatement or ambiguous bundled service | Stop final output and refer with the contract and primary-source issue |

## Worked cases

**Case 1:** Charleston furniture $1,000 x 7% = $70; total $1,070. Separately, Morgantown legal services by a recognized lawyer at $2,000 are exempt, tax $0, total $2,000. The exemption changes the outcome despite both cities imposing municipal tax. The old legal-services case overstated tax by $140.

```oa-check
name: WV taxable goods and exempt professional service
inputs:
  furniture: 1000
  legal: 2000
steps:
- goods_tax: furniture * 0.07
- goods_total: furniture + goods_tax
- legal_tax: legal * 0
- legal_total: legal + legal_tax
expected:
  goods_tax: 70
  goods_total: 1070
  legal_tax: 0
  legal_total: 2000
```
**Case 2:** A registered business brings $10,000 of taxable equipment into a 1% municipality. It lawfully paid $400 state and $150 local tax elsewhere on the same equipment. WV state use tax is $600 less $400 = $200; municipal use tax is $100 less a capped $100 credit = $0. Total additional tax is $200. If neither tax was paid elsewhere, both credits are zero and $700 is due; retain payment evidence before choosing that branch.

```oa-check
name: WV input use tax and credit ceiling
inputs:
  cost: 10000
  state_paid: 400
  local_paid: 150
steps:
- state_gross: cost * 0.06
- municipal_gross: cost * 0.01
- state_net: state_gross - min(state_gross, state_paid)
- municipal_net: municipal_gross - min(municipal_gross, local_paid)
- net: state_net + municipal_net
- without_credit: state_gross + municipal_gross
expected:
  state_gross: 600
  municipal_gross: 100
  state_net: 200
  municipal_net: 0
  net: 200
  without_credit: 700
```


Legacy fact patterns retained for review: the $5,000 IT consulting/$10,000 custom-development/$3,000 canned-software bundle totals $18,000, but each component now requires classification rather than assuming all taxable. If all three are independently taxable, tax is $1,080 state-only or $1,260 at 7%; otherwise remove only the exempt components. Similarly the $5,000 development plus $500 SaaS and the $15,000 custom-software cases need the software/data-processing determination; if taxable at 6%, results remain $300/$30 and $900 respectively. A taxable $8,000 Morgantown consulting service would give $560 and total $8,560; recognized professional exemption changes this to zero. A remote firm with $120,000 prior-year WV receipts fails the sales-value small-seller exception, but exempt professional-only sales do not thereby become taxable. The old $200 qualifying unprepared-grocery case is exempt, tax $0 and total $200; a prepared/vending/soft-drink item is not covered by that result.

## When to refuse or refer

Refer software/SaaS and mixed professional-service contracts until classified, food-definition and special medical products, specialized manufacturing/direct-pay claims, complex multi-state nexus, special districts, refund disputes, audits and abatement. Do not send an unsupported legacy example to a filing system.

## Filing and payment

Use MyTaxes for the assigned return and account, retaining the submission and bank confirmation. Late filing/payment additions and period interest require the actual delinquent period's notice; the old 5%/0.5%/25% assertions have not been re-verified for sales/use and remain unconfirmed below.

## Completion checklist

- Nexus determined independently of whether a particular sale is exempt.
- Actual product/service exemption and evidence recorded.
- Period-specific municipality, boundary and rate selected.
- Gross sales, marketplace deductions, taxable sales and untaxed purchases reconciled.
- Filed return, payment and any refund/adjustment schedules retained.

## Sources

| Source and reading scope | URL | Read on |
| --- | --- | --- |
| CST-200CU current linked instructions. Read for pp.1-6: rate, frequencies, return fields, credits and supplemental schedules. | https://tax.wv.gov/Documents/CST/cst200cu.instructions.pdf | 2026-11-13 |
| TSD 300, January 2026. Read for pp.1-4: per-se exemptions, prescriptions/OTC, professions, agriculture, manufacturing and data processing. | https://tax.wv.gov/Documents/TSD/tsd300.pdf | 2026-11-13 |
| TSD 310, July 2026. Read for pp.1-3: capital-improvement test, materials/resale, public-school change and pass-through exceptions. | https://tax.wv.gov/Documents/TSD/tsd310.pdf | 2026-11-13 |
| Municipal sales/use page. Read for rate/effective-date table, boundaries, sourcing and municipal credit limits; examples containing older city status not treated as current. | https://tax.wv.gov/business/salesandusetax/municipalsalesandusetax/pages/municipalsalesandusetax.aspx | 2026-11-13 |
| Remote-seller FAQ. Read for small-seller computation, registration, sourcing and inconsistent introductory/due-date text. | https://tax.wv.gov/Business/SalesAndUseTax/ECommerce/RemoteSellers/Pages/RemoteSellersAndWestVirginiaTax.aspx | 2026-11-13 |
| TSD 345. Read for pp.1-3: collection responsibilities, documentation and retention. | https://tax.wv.gov/Documents/TSD/tsd345.pdf | 2026-11-13 |
| West Virginia Code §§11-15-3a and 3b. Read for food-tax cessation and neighboring taxable exceptions; section 3b also read at https://code.wvlegislature.gov/11-15-3b/. | https://code.wvlegislature.gov/11-15-3a/ | 2026-11-13 |
| West Virginia Code §11-15B-2. Read for food/ingredients, candy, supplements and prepared-food definitions. | https://code.wvlegislature.gov/11-15B-2/ | 2026-11-13 |
| West Virginia Code §11-15-9(a)(21). Read for electronic-data-processing definition and related-software exemption. | https://code.wvlegislature.gov/11-15-9/ | 2026-11-13 |
| Marketplace facilitator page. Read for facilitator collection, registration and municipal sourcing. | https://tax.wv.gov/Business/SalesAndUseTax/ECommerce/MarketplaceFacilitators/Pages/MarketplaceFacilitators.aspx | 2026-11-13 |

Not yet confirmed: current holiday exceptions; SaaS, canned/custom software and digital/streaming classification in every delivery model; financial-intermediation and broad education exemptions; current facilitator definition/thresholds; sales/use penalty rates, interest and statutory vendor-discount prohibition. These were legacy subjects, not silently removed. TSD 300 confirms exempt data processing and related software, so the old blanket software/service rules must not be reused.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `wv-sales-tax` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/wv-sales-tax. If neither is available, confirm every figure against the official source pages cited above before relying on it.
