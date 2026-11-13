---
name: canada-gst-hst
description: Prepare or review a Canadian regular-method GST/HST return, classify sales and purchases, establish input tax credits, reconcile transaction records, and map figures to the actual return fields. Covers Canadian businesses including sole proprietors and corporations, with entity-specific capital rules and Quebec federal administration. Use for GST return, HST filing, GST34, input tax credits, invoice evidence, imports, exports and bank reconciliation. Load vat-workflow-base for workpaper structure; this Canadian method controls legal treatment and evidence. Separate QST/PST/RST, Quick Method and specialist regimes require the stated companion or referral.
version: 2.1
jurisdiction: CA
tax_year: 2026
last_updated: 2026-11-13
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: vat-gst
category: international
type: filing-howto
depends_on:
  - vat-workflow-base
---

# Canada GST/HST return, regular method, 2026

## Scope

Prepare a supported regular-method GST/HST calculation for a Canadian business, reconcile it to its books and evidence, and explain the fields to enter and the separate filing/payment steps. This method covers federal GST and the full harmonized HST. It does not turn a bank statement into a substantiated return by guessing missing facts.

**Approval of this version: Not yet approved.** Version 2.0 carried Nathan Wiebe's approval dated 3 November 2026. That historical approval is not approval of these substantive corrections. The source audit is separate from an accountant accepting this version professionally. Original authorship and earlier text remain in Git history.

Read `vat-workflow-base` for the work sequence, source trace, workbook and reviewer brief. This Canadian method overrides any generic merchant classifier, assumed taxpayer profile, tax status, rate, election, blocked-input rule or foreign reverse-charge rule in that companion. EU rules do not determine Canadian GST/HST. No merchant recognition rule authorizes a legal conclusion without the underlying facts.

This Guide supplies both the Canadian legal framework and country method; **no additional regional/directive layer is required**. Use the question and artifact tools actually available in the user's AI runtime, or ordinary questions when no special UI tool exists. Do not halt solely because a Claude-specific `ask_user_input_v0` tool is absent. Resolve missing facts before finalizing the calculation, without treating a missing interface as a missing tax rule.

The sources were read on **13 November 2026**, in the portions listed below. The Justice consolidation inspected is current to 19 October 2026; this is not a claim to have checked later unpublished amendments. The actual CRA working-copy form is an unyearlabelled preparation aid, not a 2026 filing form. Earlier-period returns require the rules, rates, elections and reporting periods for those periods; do not move a 2025 item into 2026 just because it is found now.

### Quick reference

| Item | Rule and conditions | Official source |
|---|---|---|
| Federal GST | 5% on ordinary taxable supplies where only the federal component applies; zero-rating and exemptions must be tested first. | [CRA rates and place of supply](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/charge-collect-place-supply.html) |
| Full HST | Ontario 13%; Nova Scotia 14% from 1 April 2025; New Brunswick, Newfoundland and Labrador, Prince Edward Island 15%. Determine the place and relevant date of each supply. | [CRA rates](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/charge-collect-place-supply.html) |
| Ordinary small supplier | CAD 30,000 worldwide taxable consideration, including associates, with the statutory exclusions and separate single-quarter/four-quarter timing below. Public service bodies have a separate CAD 50,000 test and special rules. | [ETA 148](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-148.html) |
| Assigned reporting period | Ordinary annual threshold up to CAD 1.5 million; quarterly above CAD 1.5 million through CAD 6 million; monthly above CAD 6 million. The threshold base, associates, elections and entity exceptions matter. Read the account's assigned period. | [RC4022, reporting periods](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4022/general-information-gst-hst-registrants.html) |
| Ordinary filing | Monthly/quarterly: within one month after period end. Annual: within three months after fiscal year end, except qualifying calendar-year individual businesses and specified institutions. | [ETA 238](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-238.html) |
| Qualifying annual individual business | Calendar-year individual carrying on business whose income-tax filing date is 15 June: GST/HST filing 15 June following the year; payment 30 April. This is not a rule for every individual. | [ETA 238(1)(a)(ii)](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-238.html), [228(2)(a)](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-228.html) |
| Currency | CAD; use the actual statutory tax point or a Minister-accepted conversion method consistently, with the source and date recorded. | [ETA 159](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-159.html), [CRA memorandum 3-6](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/3-6/conversion-foreign-currency.html) |
| Administration and filing | CRA account/eligible GST/HST NETFILE route for CRA-administered accounts. Revenu Québec generally administers federal GST/HST for businesses physically located in Quebec, with SLFI exceptions. Use the assigned authority and account, not a universal GST34 paper route. | [RC4022](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4022/general-information-gst-hst-registrants.html) |

## Ask the client first

Search the supplied books, prior returns, account records, invoices, contracts and notes first. Ask only for facts still missing. Record the source beside each confirmed fact.

| Fact | Evidence to read | If missing |
|---|---|---|
| Entity and legal recipient | Incorporation/partnership records or proprietor's identity, legal invoice recipient and any agency arrangement. A name ending in Inc is a clue only. | Keep entity-specific decisions pending, especially passenger vehicles and benefits. |
| Normal registration | Actual BN/account, effective dates and legal person. Example format: `123456789RT0001`; a plausible format is not validation. Asking for a return is not proof of registration. | Resolve whether registration/collection is required; do not create ITCs for an unconfirmed registrant. |
| Place and activities | Business premises, taxable/zero-rated/exempt activities, contracts, goods delivery, obtained recipient addresses, relevant service performance and IP rights/use. | Hold the affected rate or status decision; do not default to Ontario or the registration province. |
| Period and method | Account-assigned dates/frequency, fiscal year end, prior filing, regular versus Quick Method or another election. | Date coverage of a CSV and silence about an election are not proof. |
| Sales and adjustments | Full sales journal, unpaid invoices, receipts, credit/debit notes, export evidence, write-offs, marketplace/processor reports and previous reporting. | A bank-only result is preliminary. Identify unpaid/accrued sales, deposits and missing adjustments. |
| Purchases and ITCs | Purchase journal, invoices/receipts, supplier's actual registration regime, recipient, tax paid/payable, business purpose, commercial-use records and relevant restrictions. | Pending ITCs are not entered as established claims; show the evidence gap and affected amount. |
| Reconciliation | Full-period bank/card/processor records, opening and closing balances, cash records and transfer matches. Accept CSV, PDF or pasted records from any bank where legible. | An absent bank file does not invalidate otherwise sufficient books, but unexplained reconciliation differences prevent a supported completion. |
| Prior account position | Previous return, statement of account, instalments/payments/refunds, prior ITCs and credits claimed elsewhere. | Read those records before asking. A prior account balance is not automatically a current-return adjustment. |
| Special facts | Employees/benefits, vehicle logs, home work space, exempt activities, related entities, property transactions, non-resident/simplified registration and relief claims. | Apply the relevant branch or specialist referral below. |

RBC, TD, Scotiabank, BMO, CIBC, National Bank, Desjardins, Tangerine, Simplii, EQ Bank, Revolut Business, Wise Business and other bank exports can support reconciliation. The invoice and statutory evidence rules apply at all amounts. The old CAD 400 invoice trigger was only an internal triage amount, not a documentation exemption.

## The method, step by step

### Rates, bands and thresholds

#### Province and territory routing

These are ordinary general rates, not a statement that every item sold in a province is taxable. Determine the actual place of supply first. Separate provincial taxes do not become federal ITCs.

| Place of supply | Federal return tax | Separate provincial route | Official source |
|---|---|---|---|
| Alberta (AB) | 5% GST | No general provincial sales tax in this routing table. | [CRA](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/charge-collect-place-supply.html) |
| British Columbia (BC) | 5% GST | General PST 7%, subject to exemptions/special rates; use `bc-pst` for a separate provincial job. | [CRA](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/charge-collect-place-supply.html), [BC PST Act 34(1)](https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/12035_03) |
| Manitoba (MB) | 5% GST | General RST 7%, subject to its own taxable base; use `mb-rst`. | [CRA](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/charge-collect-place-supply.html), [Manitoba bulletin 030](https://www.manitoba.ca/finance/taxation/pubs/bulletins/030.pdf) |
| New Brunswick (NB) | 15% HST | Full HST on federal return. | [CRA](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/charge-collect-place-supply.html) |
| Newfoundland and Labrador (NL) | 15% HST | Full HST on federal return. | [CRA](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/charge-collect-place-supply.html) |
| Northwest Territories (NT) | 5% GST | No general provincial sales tax in this routing table. | [CRA](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/charge-collect-place-supply.html) |
| Nova Scotia (NS) | 14% HST from 1 April 2025; previously 15% | Retain the date transition for historical adjustments; do not apply today's rate to every old invoice. | [CRA](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/charge-collect-place-supply.html) |
| Nunavut (NU) | 5% GST | No general provincial sales tax in this routing table. | [CRA](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/charge-collect-place-supply.html) |
| Ontario (ON) | 13% HST | Full HST on federal return. | [CRA](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/charge-collect-place-supply.html) |
| Prince Edward Island (PE) | 15% HST | Full HST on federal return. | [CRA](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/charge-collect-place-supply.html) |
| Quebec (QC) | 5% GST | QST 9.975% is separate; use `qc-qst-return` and the assigned RQ filing route. Quebec does not make federal GST analysis inapplicable. | [RQ current rates](https://www.revenuquebec.ca/en/businesses/consumption-taxes/gsthst-and-qst/basic-rules-for-applying-the-gsthst-and-qst/tables-of-gst-and-qst-rates/), [RC4022](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4022/general-information-gst-hst-registrants.html) |
| Saskatchewan (SK) | 5% GST | General PST 6% on its own specified supplies; use `sk-pst`. | [CRA](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/charge-collect-place-supply.html), [SK Finance, Provincial Sales Tax](https://www.saskatchewan.ca/government/government-structure/ministries/finance) |
| Yukon (YT) | 5% GST | No general provincial sales tax in this routing table. | [CRA](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/charge-collect-place-supply.html) |

#### Invoice information bands

Under [Input Tax Credit Information Regulations 3](https://laws-lois.justice.gc.ca/eng/regulations/SOR-91-45/section-3.html), test the **total paid/payable shown on the supporting documentation for all its supplies**, not just the tax-exclusive price of one item. Current bands took effect on 20 April 2021: [CRA enacted-change notice](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/news118/news118-excise-gst-hst-news-no-118.html). The former CAD 30/150 tiers are obsolete.

| Total paid/payable on the document | Required information | Official source |
|---|---|---|
| Less than CAD 100 | Supplier/intermediary business or trading name; invoice date or, without an invoice, date tax is paid/payable; total paid/payable. Substantive tax, recipient and commercial-use entitlement still must exist. | [Regulation 3(a)](https://laws-lois.justice.gc.ca/eng/regulations/SOR-91-45/section-3.html) |
| CAD 100 to less than CAD 500 | Above plus supplier/intermediary GST/HST registration number and prescribed tax amount or tax-inclusive/rate information; mixed taxable/exempt documents need the required status and tax detail. | [Regulation 3(b)](https://laws-lois.justice.gc.ca/eng/regulations/SOR-91-45/section-3.html) |
| CAD 500 or more | Above plus purchaser's business/trading name or authorized agent/representative name; terms of payment; description sufficient to identify each supply. Purchaser address is not a prescribed field in this provision. | [Regulation 3(c)](https://laws-lois.justice.gc.ca/eng/regulations/SOR-91-45/section-3.html) |

For tax-inclusive documentation, apply the actual 3(b) alternatives: separately shown tax for supplies, or the permitted statements/rates allowing tax to be determined. A lower information band does not make a bank debit proof that GST/HST was actually charged. Obtain required documentation **before filing the return claiming the ITC**, subject to a real Minister-authorized exception, not an AI-created exemption: [ETA 169(4)–(5)](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-169.html).

### 1. Establish registration, period and authority

For the ordinary small-supplier test, count worldwide taxable consideration, including zero-rated supplies and associates, before expenses. Exclude supplies of financial services, **sales** of capital property and the specified goodwill consideration. Do not exclude all income earned using capital property, such as ordinary equipment rentals. Exact equality with CAD 30,000 does not exceed the ordinary threshold. [ETA 148](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-148.html).

* A single-calendar-quarter breach ends small-supplier treatment on the sale that exceeds the threshold; tax applies to that triggering sale, with registration effective no later than that day.
* If the previous four or fewer consecutive quarters exceed the threshold without a single-quarter breach, small-supplier status continues through the month following that quarter. Registration is effective no later than the first supply after that status ends.
* Register within 29 days of the effective date. Below-threshold voluntary normal registration is possible. Taxi/commercial ride-sharing and some non-resident cases do not follow the ordinary optional-registration rule. Public service bodies and charities require their own tests. [CRA registration dates and examples](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/when-register-charge.html).

Confirm the account's actual reporting period and any election. The ordinary reporting threshold is not the registration threshold: it includes associates and domestic taxable/zero-rated revenue but excludes zero-rated exports, outside-Canada supplies, exempt/financial supplies, capital real-property sales and goodwill as described in [RC4022, Reporting periods](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4022/general-information-gst-hst-registrants.html). A business may elect a more frequent period, using the applicable account process/GST20. Never infer annual filing from low bank deposits alone.

Confirm CRA versus RQ administration. A Quebec business generally files federal GST/HST and QST with RQ; do not send its figures to the wrong account or refuse all federal analysis. SLFIs have separate administration and attribution rules. [RC4022, GST/HST and Quebec](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4022/general-information-gst-hst-registrants.html).

### 2. Reconcile complete records without confusing cash with tax points

Assign each source document and transaction a unique ID. Reconcile bank/card openings, movements and closings, ledger sales/purchases, unpaid items and processor payouts. Match both sides of own-account transfers; identify owner contributions, draws, dividends, loan principal, remittances and refunds separately. A label is a lead until supported by matching records.

GST/HST generally becomes payable at the earlier of payment and consideration becoming due, with statutory special rules. Include collectible tax on unpaid invoices in the correct period; do not add it again when cash arrives. A genuine deposit is not consideration until applied as consideration under [ETA 168(1),(2),(9)](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-168.html). A forfeited amount needs the separate [ETA 182(1)–(3)](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-182.html) analysis: a breach, modification or termination concerning a registrant's Canadian taxable non-zero-rated supply can deem tax included in the forfeiture. Check the agreement and statutory exceptions; do not treat every lost deposit as untaxed or apply tax on top automatically. This is not permission to elect cash-basis GST/HST from a bank export.

Reconcile processor gross sales, refunds, chargebacks, taxes, withheld fees and net payouts. A Stripe/PayPal deposit is not the gross taxable sale, and a fee is not automatically exempt. Split invoice components and actual business/personal use. Keep unresolved items in a separate schedule; never silently force them to taxable sales, personal spending or zero tax to balance the account.

### 3. Decide supply status and place before choosing a rate

First establish whether the supply is made in Canada under [ETA 142](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-142.html), including goods delivery, IPP use/relationship and service-performance tests. The non-resident deeming rule and its Canadian-business, normal-registration, qualifying-goods and admission exceptions are in [ETA 143](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-143.html). Foreign currency, a foreign payer or a vendor's headquarters does not settle this.

Then classify the actual supply, not the industry name:

| Supply family | Decision and retained conditions | Official source |
|---|---|---|
| Zero-rated | Qualifying prescription drugs, medical/assistive devices, basic groceries, agriculture/fishing, exports of goods/services, international transportation and specified non-resident financial services each have their own statutory tests. Zero-rated sales are taxable supplies at 0%; related inputs can support ITCs when all other conditions are met. | [Schedule VI Parts I–V, VII and IX](https://laws-lois.justice.gc.ca/eng/acts/E-15/page-121.html) |
| Exempt | Listed residential rent/condominium, health, education, childcare, legal-aid, public-sector and financial supplies are conditional exemptions. A supplier's profession or government status does not exempt all its supplies. Ordinary inputs attributable to exempt activity do not earn ITCs; mixed activities require supportable allocation. | [Schedule V Parts I–VII](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-sched200860.html), [ETA 169](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-169.html) |
| Residential/property | Ordinary qualifying long-term residential rent and qualifying residential condominium supplies may be exempt. Short accommodation, new housing, changes of use and builder self-supply require their actual exceptions and specialist property analysis. Do not apply an unconditional one-month shortcut. | [Schedule V Part I](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-sched200860.html), [ETA 191](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-191.html) |
| Financial services/processor charges | Apply the financial-service definition and exclusions, including advisory, management, professional, preparatory, debt-collection and payment-card-network services. The prescribed acquirer/issuer/settlement exceptions to paragraph (r.6) are specific; they do not exempt every merchant charge. Separate hardware, subscriptions and ancillary services according to the actual supply/contract. | [ETA 123, financial service](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-123.html), [SOR/91-26 3.2](https://laws-lois.justice.gc.ca/eng/regulations/SOR-91-26/section-3.2.html) |
| Transit, air, postage | Qualifying municipal transit is **exempt**, not zero-rated. Airline international branding alone does not establish zero-rating. Canada Post stamps/letters are not categorically exempt; product, delivery and international-mail conditions matter. | [Schedule V VI24](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-sched200860.html), [Schedule VI VII/IX](https://laws-lois.justice.gc.ca/eng/acts/E-15/page-121.html), [CRA rates/postage](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/charge-collect-place-supply.html) |

For a Canadian taxable supply, establish the province under [SOR/2010-117](https://laws-lois.justice.gc.ca/eng/regulations/SOR-2010-117/FullText.html) and the relevant Schedule IX rule:

* Goods sold ordinarily follow delivery/making available, including the actual shipment arrangement; goods leased or licensed have different rules.
* General services prioritize the recipient's Canadian home/business address obtained in the ordinary course: only one such address, or the one most closely connected if several; otherwise use the connected Canadian address. With no obtained Canadian address, use the regulation's Canadian-performance/participating-province tests. Do not substitute supplier headquarters.
* Real-property services, services relating to tangible property, personal services, transport, telecommunications/computer-related services and IPP have special rules. For IPP, identify rights, where they may be used, related property and the applicable value/address conditions. The general service-address rule is not universal.
* Consulting to an actual non-resident may be zero-rated under **Schedule VI Part V 23**, subject to its Canadian real-property, tangible-property, Canadian-litigation and agency exclusions. Part V 5 concerns agency; Part V 7 expressly excludes advisory/consulting/professional services. Read the correct clause and keep non-residence and contract evidence. [Schedule VI Part V](https://laws-lois.justice.gc.ca/eng/acts/E-15/page-121.html).
* For air-containing continuous journeys, test Schedule VI Part VII 3: origin outside Canada but in the taxation area; an origin/termination/stopover outside that area; all origins/termination/stopovers outside Canada; or the separate all-air-embarkation/disembarkation condition. The taxation area means Canada, the United States except Hawaii, and Saint Pierre and Miquelon. A Canada-to-US journey within that taxation area is not automatically zero-rated simply because it crosses a border. Through tickets, separate tickets and stopovers matter. [Schedule VI VII1–3](https://laws-lois.justice.gc.ca/eng/acts/E-15/page-121.html), [CRA travel guide, international passenger transportation](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/charge-collect-specific-situations/gst-hst-information-travel-convention-industry.html).

### 4. Establish ITC entitlement, evidence and time limit

Use [ETA 169](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-169.html): the claimant must be the eligible registrant acquiring/importing the input, tax must be paid or payable as required, and the input must have a commercial nexus. Commercial activity includes taxable and zero-rated supplies; exempt activities are different. Do not claim another person's purchase or tax merely because money passed through this bank account. Check supplier/recipient records and prevent duplicate claims, refunded tax and amounts claimed in another period. Follow the invoice bands above.

| Ordinary non-financial-institution input | Treatment after evidence and other restrictions | Official source |
|---|---|---|
| Most operating expenses, at least 90% commercial use | Generally full ITC under substantially-all deeming. | [CRA eligibility chart](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/calculate-prepare-report/input-tax-credit/calculate-eligibility-percentage.html), [ETA 141](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-141.html) |
| Most operating expenses, more than 10% but less than 90% commercial use | Fair, reasonable and consistently applied commercial-use allocation, then applicable input restriction. | [CRA chart](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/calculate-prepare-report/input-tax-credit/calculate-eligibility-percentage.html), [ETA 169](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-169.html) |
| Most operating expenses, 10% or less commercial use | Generally no ITC under the non-commercial substantially-all rule. Do not apply this ordinary-business chart to financial institutions or all real-property cases. | [CRA chart](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/calculate-prepare-report/input-tax-credit/calculate-eligibility-percentage.html), [ETA 141](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-141.html) |
| Ordinary capital personal property | More than 50% intended commercial use generally gives full initial ITC; 50% or less gives none, subject to entity/property exceptions below. It is not ordinary expense pro-rating. | [ETA 199](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-199.html) |

Use the actual [ETA 225(4)–(4.1)](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-225.html) deadline. For a non-specified person, the return claiming the credit must be filed by the due date of the last reporting period ending within four years after the period the ITC arose. A specified person generally uses the due date of the last period ending within two years after the fiscal year containing that period. Specified status includes listed FIs and the statutory over-CAD-6-million two-year threshold, with charity/substantially-all-taxable-supply exceptions. There are special late-billed/other-person-claim/assessed-supplier branches. Do not collapse these to “four years from invoice” or deny every large taxable business the ordinary window. [CRA time-limit table](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/calculate-prepare-report/input-tax-credit.html).

### 5. Apply restrictions and entity-specific capital rules

**Meals, entertainment and tips.** Ordinary business food/beverage/entertainment ITCs are normally limited to 50%, not automatically blocked. Eligible long-haul driver consumption during the defined eligible travel period uses the 80% income-tax treatment and corresponding GST/HST adjustment. The individual's principal business or employment duty must be driving a qualifying freight truck/tractor with gross vehicle weight rating **over 11,788 kg**. The driver must be away from the municipality/metropolitan area of the statutory specified place for **at least 24 continuous hours**, to transport goods to or from a location **beyond a 160 km radius** of that place. Exactly 160 km, or merely driving that total distance, is insufficient. The specified place is the employer establishment ordinarily reported to, or the qualifying self-employed driver's residence. [ETA 236](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-236.html), [ITA 67.1(1),(1.1),(5)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-67.1.html).

Qualifying full-treatment exceptions require their actual conditions: ordinary food/entertainment business resale; registered-charity fundraising; a reasonable reimbursement specifically identified in writing to the payer; relevant taxable employee benefits and defined remote/construction work-site cases; or qualifying all-employee special events within the statutory annual limit. A client reimbursing a bundled invoice, any fundraiser or any remote meal is not enough. **Convention meals are not automatically exempt from the restriction**: unitemized non-incidental food in a qualifying convention fee generally attracts the statutory CAD 50/day allocation before applying the meal rule. [ITA 67.1(2)–(3)](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-67.1.html).

Choose and document the permitted method: claim the allowable fraction in each period, or claim otherwise eligible full tax and make the required annual adjustment in the appropriate period under ETA 236. Do not both halve the claim and reverse half again. A voluntary employee gratuity is not taxed; a taxable invoiced service charge is different. Split it before extraction. [RC4022, Meals and entertainment](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4022/general-information-gst-hst-registrants.html), [CRA travel guide, Gratuities](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/charge-collect-specific-situations/gst-hst-information-travel-convention-industry.html).

**Club, personal and home costs.** Dining/recreation/sport club memberships are restricted, with the actual resale exception. Personal benefit and reasonableness rules have their statutory conditions. Home work space must be the principal place of business **or** be used exclusively to earn business income and regularly/continuously to meet clients/customers/patients. Exclusive space alone is not the only qualifying route. Apply reasonable supported use/time allocation after eligibility, avoiding prohibited personal portions. [ETA 170](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-170.html). There is no general CAD 50 customer-gift block in that section; qualifying promotional gifts/free samples can support ITCs when acquired to facilitate taxable sales, subject to other restrictions. [RQ promotional-gift guidance](https://www.revenuquebec.ca/en/businesses/consumption-taxes/gsthst-and-qst/special-cases-gsthst-and-qst/promotional-gifts-and-free-samples/). Employee gifts, food and appropriations are not resolved by that short rule.

**Ordinary capital personal property.** Establish capital character from the asset and use, not a universal CAD 1,000 threshold. Under [ETA 199](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-199.html), the ordinary non-FI acquisition primarily for commercial activities is deemed exclusive for the initial ITC; otherwise the initial ITC is blocked. Financial institutions, prescribed registrants and an individual's/partnership's passenger vehicle or aircraft are exceptions. A computer at 60% qualifying commercial use is not treated like an operating phone bill at 60%.

On beginning primarily commercial use, the ordinary capital credit uses **basic tax content**, not a universal current-FMV-times-rate formula. On ceasing primarily commercial use, [ETA 200](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-200.html) can deem tax collected equal to basic tax content. The definition in [ETA 123](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-123.html) incorporates actual historical tax/recoveries and the capped value factor. Keep original acquisition, prior ITCs/rebates, improvements, value and use-change dates; refer special classes/real property. A sale when last used otherwise than primarily commercially follows the actual 200(3) conditions, not “all asset sales taxable.”

**Passenger vehicles, aircraft, leases and operating costs.** Keep four questions separate: entitlement, commercial use, applicable acquisition/lease ceiling, and operating costs.

* Corporations generally apply the primarily-commercial capital rule, subject to the acquisition tax cap and exceptions. Individuals/partnerships generally need exclusive commercial use for the ordinary initial passenger-vehicle/aircraft ITC. For non-exclusive use, [ETA 202(4)](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-202.html) provides the relevant year-end deemed-tax route tied to CCA **actually deducted for commercial activities**, subject to its benefit conditions. Do not calculate every purchase ITC as invoice GST/HST times driving percentage. Exactly 50% use is not an unregulated gap because a summary chart skips that row.
* [ETA 201](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-201.html) caps acquisition tax using the applicable ITA 13(7)(g)–(i)/[ITR 7307](https://laws-lois.justice.gc.ca/eng/regulations/C.R.C.,_c._945/section-7307.html) amount. The 2025 ordinary passenger limit is CAD 38,000 before taxes. Finance's 14 January 2026 announcement says CAD 39,000 for vehicles acquired from 1 January 2026; the inspected consolidated 7307 still says CAD 38,000 after 2024. Record that enactment-text gap and confirm the operative amendment before a final 2026 cap-dependent claim. The old CAD 37,000 claim for both years is wrong.
* The official announcement retains CAD 61,000 for qualifying zero-emission passenger vehicles and CAD 1,100 monthly leasing ceiling before tax; the actual formula, vehicle qualification and acquisition/lease date still matter. Do not treat every electric vehicle as ordinary Class 10.1 or turn a monthly ceiling into an automatic ITC. [Finance 2026 announcement](https://www.canada.ca/en/department-finance/news/2026/01/government-announces-the-2026-automobile-deduction-limits-and-expense-benefit-rates-for-businesses.html), [ITR 7307](https://laws-lois.justice.gc.ca/eng/regulations/C.R.C.,_c._945/section-7307.html).
* Fuel, repairs and other operating expenses follow their own commercial-use and documentation rules. A loan-principal repayment is not a second vehicle purchase or ITC. Actual lease restrictions and taxable-benefit calculations require their separate facts.

### 6. Test imported services/IPP and the supplier's registration regime

Do not impose a Canadian version of EU reverse charge automatically. A foreign supplier, foreign currency or invoice without GST/HST is not sufficient.

1. Identify the actual legal supplier, service versus IPP versus goods, supply location, normal/simplified registration, Canadian-business connection, resident recipient, consideration and commercial/provincial use.
2. Apply **ETA 217's definition before 218**. Ordinary non-FI services/IPP acquired exclusively for commercial activities are excluded from the relevant imported-taxable-supply definition. “Exclusive” generally means all or substantially all for non-FIs, treated as at least 90% in CRA guidance; FIs require all. Other foreign-use, property, transport, litigation and IP-use exclusions must also be tested. Special goods/drop-shipment and FI branches are different. [ETA 217](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-217.html), [123, exclusive](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-123.html), [CRA imports](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/charge-collect-imports-exports.html).
3. For an actual imported taxable supply under this ordinary branch, federal tax is 5% of consideration under [ETA 218](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-218.html). Provincial HST components need the separate residency and use tests in [218.1](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-218.1.html) and [SOR/2010-151 7](https://laws-lois.justice.gc.ca/eng/regulations/SOR-2010-151/FullText.html). The imported service/IPP prescribed provincial-use threshold is **at least 10%**, not more than 10%. Calculate each actual participating-province component from the statutory consideration × provincial rate × relevant use proportion; do not simply impose the business's full HST rate everywhere.
4. A registrant reports applicable self-assessed tax on **405** and claims only its independently entitled ITC on **106**. Partial commercial use can leave real net tax, not an automatic equal offset. A fully commercial ordinary import excluded at step 2 has neither fictional 405 tax nor a fictional import ITC. Non-registrants use the applicable GST59 route rather than this normal registrant return. Goods imported through customs require actual importer-of-record/tax documents, not this service calculation. [CRA imports](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/charge-collect-imports-exports.html).
5. For a **simplified-framework** supplier, a normal registrant should give its normal registration information so the supplier does not charge under that framework. GST/HST charged under simplified registration is **not an ordinary ITC or rebate**. Seek correction/refund from the supplier under the applicable process; do not post it to 106 merely because a tax number appears. Verify normal versus simplified status using the actual supplier's account/registry. [CRA simplified-account verification and buyer rules](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/digital-economy-gsthst/confirming-simplified-gst-hst-account-number.html).

### 7. Account for bad debts, notes and other adjustments

For a bad-debt deduction, verify an actual taxable non-zero-rated sale to an arm's-length person, genuine bad-debt write-off in the books, tax previously reported, and remittance prerequisites. Deduction = tax on the original supply × unpaid amount written off (including relevant GST/HST/PST) ÷ original total (including those taxes). Claim on 107 if entitled, within four years **after the due date of the return for the write-off period**. Mere overdue status is not a write-off. Later recovery gives the proportionate addition, normally 104. [ETA 231(1),(1.1),(3),(4)](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-231.html), [CRA return instructions](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/calculate-prepare-report/instructions-preparing-return.html).

Distinguish excess tax from a price reduction. [ETA 232](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-232.html) generally allows excess-tax adjustment/refund within two years after it was charged/collected; a later consideration reduction has its separate four-year period measured from the end of the reduction period. Issue/receive the prescribed credit/debit note within a reasonable time. Supplier deduction and recipient ITC reversal follow the actual note period and amounts already reported/claimed. Do not refund and claim the same tax twice. Use the current account correction route for an already filed return; do not arbitrarily dump an old error into current 104/107. [RC4022, changing a return](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4022/general-information-gst-hst-registrants.html).

### 8. Map the calculation to the actual return

Use [CRA's line instructions](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/calculate-prepare-report/instructions-preparing-return.html) and the actual [CRA working-copy form](https://www.canada.ca/content/dam/cra-arc/migration/cra-arc/tx/bsnss/tpcs/gst-tps/bspsbch/rtrns/wrkngcp-eng.pdf). This is the ordinary regular-method flow; do not import Quick Method 101 rules.

| Field | What to include and control | Official source |
|---|---|---|
| 101 | Own sales and other revenue, including taxable/zero-rated and exempt revenue, **excluding GST/HST and PST** under regular method; report as instructed to the nearest dollar. Not all bank credits and not gross-inclusive. | [CRA 101](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/calculate-prepare-report/instructions-preparing-return.html) |
| Optional electronic 90/91/102 | 90: domestic taxable sales, including domestic zero-rated but excluding zero-rated exports. 91: exempt, zero-rated exports and other specified revenue, including relevant outside-Canada supplies. Own 101 = 90 + 91. 102 is associates' information, not an addition to own 101. | [CRA optional sales breakdown](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/calculate-prepare-report/instructions-preparing-return.html) |
| 103 / 104 / 105 | 103 tax collected/collectible for period; 104 adding adjustments such as qualified bad-debt recovery. 105 = 103 + 104. Do not put every self-assessed import into 103/104. | [CRA 103–105](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/calculate-prepare-report/instructions-preparing-return.html) |
| 106 / 107 / 108 | 106 eligible ITCs; 107 deducting adjustments such as eligible bad-debt deduction and appropriate credit-note adjustments. 108 = 106 + 107. 107 is not simply “recapture”: an adjustment that increases net tax does not become a deduction. | [CRA 106–108](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/calculate-prepare-report/instructions-preparing-return.html) |
| 109 | Net tax = 105 − 108. This is not necessarily the final payment/refund because other credits/debits follow. | [CRA 109](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/calculate-prepare-report/instructions-preparing-return.html) |
| 110 / 111 | 110 qualifying instalments/annual-filer payments; 111 eligible rebates with the required application/process. Do not insert every old account credit or unsupported rebate. | [CRA 110–111](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/calculate-prepare-report/instructions-preparing-return.html) |
| 205 | Tax payable directly on qualifying real-property/emission-allowance transactions under the actual conditions; refer the specialist property branch. | [CRA 205](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/calculate-prepare-report/instructions-preparing-return.html), [ETA 228(4)](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-228.html) |
| 405 | Applicable other self-assessed GST/HST after the import/brought-in rules are satisfied, including the actual provincial component where required. This is an additional debit in the final balance. | [CRA 405](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/calculate-prepare-report/instructions-preparing-return.html) |
| Paper 112 / 113A / 113B / 113C | 112 = 110 + 111; 113A = 109 − 112; 113B = 205 + 405; 113C = 113A + 113B. | [Actual working copy](https://www.canada.ca/content/dam/cra-arc/migration/cra-arc/tx/bsnss/tpcs/gst-tps/bspsbch/rtrns/wrkngcp-eng.pdf) |
| Final 114 / 115 | Negative final balance: refund on 114, as a positive magnitude. Positive balance: owing on 115. Zero: neither a positive refund nor payment. Electronic 112/113A/B/C do not appear; software still calculates the final result including 205/405. | [CRA final fields](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/calculate-prepare-report/instructions-preparing-return.html) |

Ordinary electronic instructions use 103/104 and 106/107 as inputs and automatically calculate 105/108/109. GST/HST TELEFILE has a different combined-line presentation. Do not generalize an older working-copy footnote about electronic 108 to the current ordinary NETFILE screen. [CRA electronic/paper/TELEFILE distinctions](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/calculate-prepare-report/instructions-preparing-return.html).

Schedule B recaptured ITCs is not applicable to periods beginning on or after 1 April 2021. Historical RITC reconciliation is a dated specialist question; do not label all recapture “expired 2018” or invent a current 107 deduction. [CRA schedule instructions](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/calculate-prepare-report/instructions-preparing-return.html).

### 9. File, retain confirmation and pay through the right account

The workpaper is a calculation, not a filing authorization. Before submission, obtain the taxpayer/authorized representative's actual sign-off and confirm the live account, period, authority, method and unresolved-item schedule.

1. Sign in to the relevant CRA business/representative account or authorized GST/HST NETFILE route; for an RQ-administered account use its federal/QST service. Choose the correct BN/program account and period, then the appropriate return. Never create an account, authorize a representative or submit a return merely to test this method.
2. Use the electronic field meanings above, including nil returns and optional sales breakdown where chosen. Transfer the approved figures, verify computed totals and ensure other debits/credits match the workpaper. Electronic filing is generally mandatory for ordinary non-charity registrants for periods beginning from 1 January 2024. Selected listed FIs and conditional charity cases have their own routes. [CRA enacted notice](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/news118/news118-excise-gst-hst-news-no-118.html), [SOR/2010-150 2](https://laws-lois.justice.gc.ca/eng/regulations/SOR-2010-150/FullText.html).
3. Review the return before submitting. Save the confirmation/reference, exact submitted figures, account/period and supporting workpaper. A generated workbook or green validation check is not a submission receipt. If paper is actually permitted, use the correct personalized GST34-2 or non-personalized GST62 process. **Do not mail/file the working-copy PDF.** [CRA return instructions](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/calculate-prepare-report/instructions-preparing-return.html).
4. Pay separately through the authorized payment route for the correct account and period, preserving the payment confirmation and checking its account allocation. Filing does not itself pay the tax. Read the statement of account for old balances and later processing, rather than assuming the current return settles everything.
5. Retain complete records, generally six years after the end of the year to which they relate, including electronically readable records. Objection/appeal and Minister-required retention can extend this. [ETA 286](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-286.html).

### 10. Confirm deadlines, instalments and late charges

| Item | Conditions and method | Official source |
|---|---|---|
| Monthly/quarterly filing and payment | Ordinary due date one month after period end; check the account and recognized holiday/weekend adjustment. | [ETA 238](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-238.html), [228](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-228.html), [CRA deadlines](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/file-gst-hst-return/reporting-requirements-deadlines.html) |
| Annual ordinary / exceptions | Ordinary three months; qualifying calendar-year individual business files 15 June but pays 30 April following the year. Listed financial institutions described in the provision have a six-month filing rule, not an ordinary-business extension. | [ETA 238(1)(a)](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-238.html), [228(2)](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-228.html) |
| Annual instalments | Base is generally the lesser current/prior annualized net tax under 237(2); if below CAD 3,000, deemed nil. Otherwise each quarterly instalment is one quarter of base, due within one month after fiscal-quarter end. Short periods require actual 365/day adjustments and special SLFI cases differ. Do not use revenue or an unverified rebate to erase an obligation. | [ETA 237(1)–(3)](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-237.html) |
| Late filing | A = 1% of amounts for the period unpaid by the filing deadline; add 25% of A for each complete overdue month, maximum 12. Nil/refund returns do not attract this ordinary owing-balance penalty, but still must be filed. | [ETA 280.1](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-280.1.html), [CRA penalties](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/file-gst-hst-return/reporting-requirements-deadlines/gst-hst-filing-penalties.html) |
| Required electronic filing not used | CAD 100 first failure; CAD 250 subsequent failures, independently of the ordinary late-filing balance rule. | [SOR/2010-150 3](https://laws-lois.justice.gc.ca/eng/regulations/SOR-2010-150/FullText.html) |
| Late-payment/instalment interest | Applicable prescribed quarterly rate, from the day after payment due through payment, compounded daily; instalment offsets/limits have their own rules. Fetch actual rates for the affected quarters before calculating. No fixed yearly interest rate is asserted here. | [ETA 280](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-280.html), [124](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-124.html) |

For ordinary 2026 calendar-quarter returns/payments, the dates are 30 April 2026, 31 July 2026, **2 November 2026** (31 October is Saturday) and **1 February 2027** (31 January is Sunday), subject to an actual CRA-recognized holiday/account exception. These can also be calendar-year annual instalment dates, not the annual return deadline. A qualifying 2026 individual annual business pays 30 April 2027 and files 15 June 2027. [CRA deadline/weekend rule](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/file-gst-hst-return/reporting-requirements-deadlines.html).

## Transaction evidence and supplier recognition

### Missing facts remain missing

| Uncertainty in the old workflow | Action now |
|---|---|
| Unknown sale rate or province | Trace actual supply/place/date; keep unresolved. Do not insert Ontario 13% or the registration province. |
| Unknown purchase tax or normal/simplified status | Obtain invoice and account evidence; keep pending, not a claimed ITC. |
| Unknown commercial-use percentage | Seek reasonable actual use records and quantify the possible effect; do not assert 0% as a fact. |
| Unknown personal/business purpose or restriction | Preserve the question and conditional result. Confirmed personal/restricted inputs follow their actual rule; uncertainty does not prove personal use. |
| Unknown scope/nature | Trace contract, counterparty and ledger; do not classify all incoming cash as sales or all outgoing cash as purchases. |

**Reviewer triage only, not law:** retain the previous workflow's CAD 5,000 transaction and CAD 400 possible-tax-difference high-attention flags; over-40% counterparty concentration and more-than-four unresolved assumptions medium flags; CAD 10,000 absolute-net-tax attention marker. These are legacy internal prompts, not legal thresholds, evidence exemptions or permission to ignore smaller issues. A potential error below a flag is still an error. The old CAD 1,000 purchase prompt is likewise only a capital-review reminder. No review marker proves accuracy or supplies a missing fact.

### Fifteen judgment categories

| Transaction question | Evidence and decision |
|---|---|
| Vehicle costs: Petro-Canada, Shell, Esso, Canadian Tire auto, car payments | Identify fuel/repair/lease/acquisition/loan, actual invoice tax, entity and supported commercial travel. Missing log evidence remains pending; acquisition and fuel use different rules. |
| Meals: restaurants, Tim Hortons, Starbucks, The Keg | Purpose, participants, itemized receipt, voluntary tip/service charge and any actual exception. Ordinary supported client meal can have 50% ITC; do not assume personal from merchant. |
| Home office | Principal-place or exclusive-use-plus-regular-meetings test, area/time/use records and invoices; separate private/home capital costs. |
| Round incoming owner-name amounts | Trace customer payment, capital contribution or loan using both accounts and agreement. Roundness does not prove owner capital. |
| Incoming private-name payments | Identify what was supplied, whether consideration and its tax point/status/place; then 101/103 if appropriate. |
| Interprovincial receipts | Delivery, obtained recipient addresses, actual service/IP rights and special rules; a different counterparty province is a lead only. |
| Large/durable purchases | Establish capital nature and specific asset/entity rules; no universal CAD 1,000 capitalization or automatic current-expense treatment. |
| Mixed phone/internet: Rogers, Bell, Telus | Actual use allocation and statutory deeming/restrictions. A dedicated business line is not the only route to a credit. |
| Outgoing private-name payments | Contractor, wages, refund, transfer or personal payment; obtain invoice, employment/agency and recipient facts. Do not default to drawings. |
| ATM/cash | Trace cash book and actual spending evidence; withdrawal alone creates no purchase ITC but is not proof the cash was personal. |
| Rent | Lease, occupancy, supplier registration, actual tax and recipient/use; residential/short accommodation/commercial rules differ. |
| Amazon.ca/AMZN | Actual marketplace seller, items, invoice, normal/simplified status and tax breakdown. Brand/site address does not establish domestic taxable status. |
| Stripe/PayPal receipts | Reconcile gross customer sales, refunds/chargebacks, tax, platform fees and net settlement; identify actual supplier/agent arrangement. |
| Tips/gratuities | Separate voluntary gratuity from taxable service charge before extracting tax. |
| USD/other foreign currency | Record original amount/currency, CAD amount, tax point, source/day and consistently applied accepted method; not always daily Bank of Canada or bank settlement date. |

### Supplier patterns are evidence prompts

Use case-insensitive recognition and the most specific matching description only to find the appropriate question. No pattern certifies a present billing entity, residence, registration, tax rate or ITC. The full original 94 pattern rows remain below, grouped into the same 15 families. Supplier ownership and billing locations were not independently verified and are not asserted.

#### 1. Banking and financial descriptions

Read the actual financial-service contract, tax treatment and any distinct fee; apply ETA 123, Schedule V VII and the specific SOR/91-26 3.2 exceptions.

| Pattern ID | Original recognition patterns |
|---|---|
| P001 | RBC, ROYAL BANK OF CANADA |
| P002 | TD, TORONTO-DOMINION, TD CANADA TRUST |
| P003 | SCOTIABANK, BANK OF NOVA SCOTIA |
| P004 | BMO, BANK OF MONTREAL |
| P005 | CIBC, CANADIAN IMPERIAL |
| P006 | NATIONAL BANK, BNC, BANQUE NATIONALE |
| P007 | DESJARDINS, CAISSE POPULAIRE |
| P008 | TANGERINE, SIMPLII, EQ BANK |
| P009 | REVOLUT, WISE, N26 (fee lines) |
| P010 | INTEREST, INTERET |
| P011 | MORTGAGE, HYPOTHEQUE, LOAN |

#### 2. Government and statutory payments

Identify the actual levy/contribution versus a separate supplied service; distinguish principal/remittance from fees and taxable transactions.

| Pattern ID | Original recognition patterns |
|---|---|
| P012 | CRA, CANADA REVENUE AGENCY, RECEIVER GENERAL |
| P013 | REVENU QUEBEC |
| P014 | CPP, CANADA PENSION PLAN |
| P015 | EI, EMPLOYMENT INSURANCE |
| P016 | WSIB, WCB, CNESST |
| P017 | SERVICE CANADA, SERVICE ONTARIO |
| P018 | CITY OF, VILLE DE, MUNICIPAL |

#### 3. Utilities and telecommunications

Read the actual utility/telecom supply, invoice tax, place/date and supported commercial use; no headquarters or full-business-use default.

| Pattern ID | Original recognition patterns |
|---|---|
| P019 | HYDRO ONE, TORONTO HYDRO, BC HYDRO, HYDRO-QUEBEC |
| P020 | ENBRIDGE, FORTISBC, ATCO GAS |
| P021 | TELUS |
| P022 | ROGERS, ROGERS COMMUNICATIONS |
| P023 | BELL, BELL CANADA, BELL MOBILITY |
| P024 | SHAW, COGECO, VIDEOTRON |
| P025 | FIDO, KOODO, VIRGIN PLUS, FREEDOM MOBILE |

#### 4. Insurance descriptions

Identify the actual insurance/financial service and separate advisory, administrative or other supplies; the company name does not exempt everything.

| Pattern ID | Original recognition patterns |
|---|---|
| P026 | MANULIFE, SUN LIFE, GREAT-WEST LIFE, CANADA LIFE |
| P027 | INTACT, AVIVA, DESJARDINS ASSURANCE |
| P028 | CO-OPERATORS, WAWANESA, ECONOMICAL |
| P029 | INSURANCE, ASSURANCE |

#### 5. Postage and couriers

Check the actual postal/courier product, delivery/destination and invoice tax; letters/stamps are not universally exempt.

| Pattern ID | Original recognition patterns |
|---|---|
| P030 | CANADA POST, POSTES CANADA |
| P031 | CANADA POST (courier, Xpresspost, Priority) |
| P032 | PUROLATOR |
| P033 | FEDEX CANADA, UPS CANADA, DHL CANADA |
| P034 | CANPAR, DICOM, LOOMIS |

#### 6. Passenger transport and car rental

Check municipal-transit exemption, actual journey/continuous-ticket conditions, ride-share supply or rental terms; carrier branding is not proof.

| Pattern ID | Original recognition patterns |
|---|---|
| P035 | VIA RAIL |
| P036 | GO TRANSIT, TTC, STM, TRANSLINK, OC TRANSPO |
| P037 | UBER CANADA |
| P038 | LYFT |
| P039 | AIR CANADA (international) |
| P040 | AIR CANADA (domestic) |
| P041 | WESTJET (international) |
| P042 | WESTJET (domestic) |
| P043 | ENTERPRISE, HERTZ, AVIS, BUDGET (car rental) |

#### 7. Food, groceries and retail

Itemize taxable/zero-rated goods, actual business purpose, meal restriction/exception and tips; no automatic personal-use block.

| Pattern ID | Original recognition patterns |
|---|---|
| P044 | TIM HORTONS, TIMS |
| P045 | STARBUCKS, MCDONALDS, SUBWAY, A&W |
| P046 | LOBLAWS, NO FRILLS, REAL CANADIAN, SUPERSTORE |
| P047 | METRO, SOBEYS, SAFEWAY, IGA, SAVE-ON-FOODS |
| P048 | COSTCO, WALMART (grocery) |
| P049 | CANADIAN TIRE (non-food) |

#### 8. Digital subscriptions often paid abroad

Obtain the actual legal billing supplier, normal/simplified registration, service/IPP and supply/use evidence; test ETA 217 before any 218/218.1 tax.

| Pattern ID | Original recognition patterns |
|---|---|
| P050 | GOOGLE (Ads, Workspace, Cloud) |
| P051 | MICROSOFT (365, Azure) |
| P052 | ADOBE |
| P053 | META, FACEBOOK ADS |
| P054 | NOTION |
| P055 | ANTHROPIC, CLAUDE |
| P056 | OPENAI, CHATGPT |
| P057 | FIGMA |
| P058 | CANVA |
| P059 | SLACK |
| P060 | ZOOM |
| P061 | ATLASSIAN |
| P062 | DROPBOX |

#### 9. Software and other platform suppliers

Check the actual supplier, subscription/hardware/financial service, normal/simplified registration, place and invoice tax; do not infer province from headquarters.

| Pattern ID | Original recognition patterns |
|---|---|
| P063 | SHOPIFY |
| P064 | STRIPE PAYMENTS CANADA |
| P065 | WEALTHSIMPLE |
| P066 | FRESHBOOKS |
| P067 | WAVE FINANCIAL |
| P068 | HOOTSUITE |

#### 10. Payment processing

Apply the actual financial-service inclusion/exclusion and prescribed PCNO exceptions; distinguish separate hardware, software and service components.

| Pattern ID | Original recognition patterns |
|---|---|
| P069 | STRIPE (transaction fees) |
| P070 | PAYPAL (transaction fees) |
| P071 | SQUARE, MONERIS, GLOBAL PAYMENTS |
| P072 | INTERAC |

#### 11. CRA and program descriptions

Match the actual tax remittance/refund, loan, grant/subsidy or distinct supply to its documents; no purchase ITC merely from a tax-payment string.

| Pattern ID | Original recognition patterns |
|---|---|
| P073 | CRA GST PAYMENT, RECEIVER GENERAL GST |
| P074 | CRA INCOME TAX, INSTALMENT PAYMENT |
| P075 | CRA REFUND, GST REFUND |
| P076 | CRA CEBA, CEWS, CERS |

#### 12. Professional services

Check legal recipient, business purpose, actual normal registration and tax, and any specific legal-aid exemption; professional title does not make every fee creditable.

| Pattern ID | Original recognition patterns |
|---|---|
| P077 | CPA, CHARTERED PROFESSIONAL ACCOUNTANT |
| P078 | LAWYER, LAW OFFICE, BARRISTERS |
| P079 | NOTARY, NOTAIRE |
| P080 | CONSULTANT, CONSULTING |

#### 13. Payroll and contributions

Separate wages, remittances and principal from the payroll provider’s own fee; its taxable service is not a wage payment.

| Pattern ID | Original recognition patterns |
|---|---|
| P081 | PAYROLL, SALARY, WAGES |
| P082 | CPP CONTRIBUTION |
| P083 | EI PREMIUM |
| P084 | CERIDIAN, ADP, PAYWORKS |

#### 14. Property and rent

Read the lease, occupancy/condominium status, actual supplier tax and commercial use; distinguish the original municipal levy from a landlord’s supplied/recharged amount.

| Pattern ID | Original recognition patterns |
|---|---|
| P085 | RENT, LOYER (commercial) |
| P086 | RENT, LOYER (residential) |
| P087 | CONDO FEES, STRATA FEES |
| P088 | PROPERTY TAX, MUNICIPAL TAX |

#### 15. Transfers, capital and cash

Match both sides and underlying owner/loan/dividend records before exclusion; ATM cash needs spending evidence, not a fabricated personal-use finding.

| Pattern ID | Original recognition patterns |
|---|---|
| P089 | TRANSFER, E-TRANSFER (own accounts) |
| P090 | INTERAC E-TRANSFER (to self) |
| P091 | DIVIDEND |
| P092 | LOAN REPAYMENT |
| P093 | ATM WITHDRAWAL |
| P094 | OWNER DRAW, SHAREHOLDER LOAN |


For government payments, separate the actual statutory levy/contribution, loan principal, grant/refund and any distinct taxable supply/service. For property tax versus rent reimbursement, read the actual transaction rather than treating every municipal string the same. For bank/insurance fees, apply the financial-service definition to the actual service; NSF or “monthly fee” is not a blanket company exemption. Match both sides before excluding transfers, and keep supporting cash evidence for ATM spending.

## Worked cases

Amounts are illustrative CAD facts, not a claim that a named vendor currently bills this way. Examples use normal registration, ordinary non-FI regular-method status and valid evidence unless stated otherwise. Round money half up to cents using the actual invoice's tax amounts; preserve full precision while deriving a new invoice split. Do not recompute a real tax amount differently merely to match a formula. The six original transaction families are retained and corrected below.

### Example 1: foreign SaaS with no automatic self-assessment

On 3 April, a Notion invoice is USD 16; the supported CAD consideration is 21.89. In this example the actual outside-Canada service/IPP is acquired wholly for the normal registrant's commercial activities, the supplier charges no Canadian tax, and no special FI/other branch applies. ETA 217 excludes this ordinary exclusive-commercial acquisition: 405 is **0.00** and there is **no invented 2.85 ITC** on 106. The 21.89 is recorded/reconciled as an expense consideration, not a Canadian GST/HST invoice. If registration/supply/use facts are absent, the classification remains pending. [ETA 217](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-217.html), [CRA imports](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/charge-collect-imports-exports.html).

Separate edge case: an Ontario resident normal registrant acquires an actual imported taxable service for **1,000.00**, with no relevant exclusion, all provincial use in Ontario and **80%** qualifying commercial use. Federal 5% = **50.00**; Ontario provincial component 8% × 100% = **80.00**; 405 = **130.00**. Independently eligible operating ITC = 130 × 80% = **104.00** on 106, leaving **26.00** net tax. This is a conditional fact pattern, not every foreign subscription. [ETA 218](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-218.html), [218.1](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-218.1.html), [169](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-169.html).

```oa-check
name: GST HST source audit arithmetic
steps:
  - result_1: round(1000*0.05,2)
  - result_2: round(1000*0.08,2)
  - result_3: 50+80
  - result_4: round(130*0.8,2)
  - result_5: 130-104
expected:
  result_1: 50
  result_2: 80
  result_3: 130
  result_4: 104
  result_5: 26
tolerance: 0.001
```

### Example 2: verified Shopify invoice

On 10 April, an actual normal-registration supplier invoice for a wholly commercial subscription shows **49.00 including Ontario 13% HST**, with place/status and invoice evidence established. Tax = 49 × 13 ÷ 113 = **5.64**; net = **43.36**; eligible 106 = **5.64**. The conclusion comes from the actual supply/invoice, not Shopify headquarters. If the actual invoice is under simplified registration, the simplified-tax ITC prohibition changes the result. [ETA 169](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-169.html), [CRA simplified-buyer rule](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/digital-economy-gsthst/confirming-simplified-gst-hst-account-number.html).

```oa-check
name: GST HST source audit arithmetic
steps:
  - result_1: round(49*13/113,2)
  - result_2: round(49-5.64,2)
expected:
  result_1: 5.64
  result_2: 43.36
tolerance: 0.001
```

### Example 3: supported client dinner and invoice rounding

On 15 April, The Keg's actual itemized receipt shows net **252.21**, HST **32.79**, total **285.00**, with no voluntary tip included in that total. The participants/business purpose are documented and no full-treatment exception applies. Under the per-period allowable-fraction method, 106 = 32.79 × 50% = 16.395, rounded half up to **16.40**. Do not call this personal without checking its known business purpose, or halve an independently re-extracted unrounded amount and replace the actual invoice tax. Confirmed personal spending gives no ITC; missing purpose stays pending. [ETA 236](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-236.html), [ITA 67.1](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-67.1.html).

```oa-check
name: GST HST source audit arithmetic
steps:
  - result_1: round(285*13/113,2)
  - result_2: round(285-32.79,2)
  - result_3: 252.21+32.79
  - result_4: floor(32.79*0.5*100+0.5)/100
expected:
  result_1: 32.79
  result_2: 252.21
  result_3: 285
  result_4: 16.4
tolerance: 0.001
```

### Example 4: MacBook, ordinary capital personal property

On 18 April, a supported ordinary capital computer purchase is **3,729.00 including 13% HST**: net = **3,300.00**, HST = **429.00**. It is not an “over CAD 30,000” purchase. For an ordinary non-FI registrant acquiring it wholly for commercial use, eligible 106 = **429.00**. At a supported 60% intended commercial use, the ordinary primarily-commercial capital rule still gives full initial ITC, subject to the actual exceptions; at exactly 50% it gives **0.00**. Do not multiply 429 by 60% as though it were ordinary operating expenditure, or apply this computer example to an individual's passenger car. [ETA 199](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-199.html).

```oa-check
name: GST HST source audit arithmetic
steps:
  - result_1: round(3729/1.13,2)
  - result_2: round(3729-3300,2)
  - result_3: 3300+429
expected:
  result_1: 3300
  result_2: 429
  result_3: 3729
tolerance: 0.001
```

### Example 5: consulting export, not a foreign-name shortcut

On 22 April, Acme Corp USA pays **5,500.00** for consulting. For this example, actual non-resident recipient status, the Canadian supply and all Part V 23 zero-rating conditions are established, with none of its Canadian-property/litigation/agency exclusions. Sales revenue = **5,500.00**, 103 tax = **0.00**. Regular 101 includes that revenue; if the optional electronic sales breakdown is used, the zero-rated export goes to 91, not domestic 90. The phrase USA alone would not prove this. Check whether the tax point was already in a prior period before recording an April receipt a second time. [Schedule VI V23](https://laws-lois.justice.gc.ca/eng/acts/E-15/page-121.html), [CRA 90/91/101](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/calculate-prepare-report/instructions-preparing-return.html).

### Example 6: fuel with supported use, or an unresolved log

On 28 April, a Petro-Canada invoice shows **92.00**, comprising net **81.42** and HST **10.58**, for an ordinary fuel operating expense. With documented 60% commercial use and no other restriction, 106 = 10.58 × 60% = **6.35**. Without the use evidence, keep the proposed credit pending and explain the missing log/use proof; do not state that actual business use was 0%. This does not calculate the passenger-vehicle acquisition ITC. [CRA operating-use chart](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/calculate-prepare-report/input-tax-credit/calculate-eligibility-percentage.html).

```oa-check
name: GST HST source audit arithmetic
steps:
  - result_1: round(92*13/113,2)
  - result_2: round(92-10.58,2)
  - result_3: round(10.58*0.6,2)
expected:
  result_1: 10.58
  result_2: 81.42
  result_3: 6.35
tolerance: 0.001
```

### Example 7: full return bridge, including 405

An Ontario normal registrant has net domestic taxable sales **10,000.00**, qualifying zero-rated exports **5,500.00**, and no other sales. 101 = **15,500**; optional 90 = **10,000**, 91 = **5,500**; associates' 102 is separately evidenced and not added to 101. Output tax 103 = **1,300.00**. A qualified earlier bad-debt recovery adds **13.00** on 104; 105 = **1,313.00**. Independently supported ITCs, including any entitled import ITC, total **700.00** on 106; qualified deducting adjustments total **26.00** on 107; 108 = **726.00**; 109 = **587.00**.

Qualifying instalments on 110 = **100.00**, no rebate on 111: 112 = **100.00**, 113A = **487.00**. No real-property tax on 205 and the actual imported-service tax from Example 1 on 405 = **130.00**: 113B = **130.00**; final 113C = **617.00**, owing on 115. Electronic intermediate fields are computed rather than entered, but omitting 405 would understate the payment by **130.00**. If the only change is qualifying instalments of **800.00**, final balance = **−83.00**, so refund 114 = **83.00**, not a negative payment. [CRA instructions](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/calculate-prepare-report/instructions-preparing-return.html), [actual working copy](https://www.canada.ca/content/dam/cra-arc/migration/cra-arc/tx/bsnss/tpcs/gst-tps/bspsbch/rtrns/wrkngcp-eng.pdf).

```oa-check
name: GST HST source audit arithmetic
steps:
  - result_1: 10000+5500
  - result_2: 10000*0.13
  - result_3: 1300+13
  - result_4: 700+26
  - result_5: 1313-726
  - result_6: 587-100
  - result_7: 0+130
  - result_8: 487+130
  - result_9: 587-800+130
expected:
  result_1: 15500
  result_2: 1300
  result_3: 1313
  result_4: 726
  result_5: 587
  result_6: 487
  result_7: 130
  result_8: 617
  result_9: -83
tolerance: 0.001
```

## Workpaper output and completion

### Three-sheet workbook

Keep the `vat-workflow-base` three-sheet structure with a Canadian overlay. A workpaper is required only when the user's job calls for one; do not manufacture a spreadsheet instead of answering a bounded question.

**Transactions.** Preserve an A–L core: A source/transaction ID, B date/tax point, C counterparty/description, D gross CAD, E net consideration CAD, F actual tax CAD, G role (sale, ITC, adjustment, self-assessment, transfer or pending), H return line code, I established rate (including 0% for actual zero-rating), J commercial-use/eligible-credit calculation, K evidence/status/reason, L currency conversion/source/date. Add separate columns for eligible ITC versus invoice tax, sales breakdown, original currency and actual document IDs when needed. The same imported supply can need a 405 debit and separately entitled 106 credit; use linked posting rows with distinct amounts, not one ambiguous tax cell counted twice. All unresolved facts remain visible.

**Line Summary.** Sum only classified eligible posting amounts by line; no blanket sum of bank credits for 101. Use a supported own-revenue column and distinct tax posting column. At minimum, calculate 103/104/105, 106/107/108, 109, 110/111/112, 205/405, paper bridge and final refund/owing. Named ranges below are workbook-defined ranges of equal length, not claims that these names exist in a source CSV:

```text
Sales101 = SUM(OwnRevenueFor101)
Line103 = SUMIFS(PostingAmount, LineCode, "103")
Line104 = SUMIFS(PostingAmount, LineCode, "104")
Line105 = Line103 + Line104
Line106 = SUMIFS(PostingAmount, LineCode, "106")
Line107 = SUMIFS(PostingAmount, LineCode, "107")
Line108 = Line106 + Line107
Line109 = Line105 - Line108
Line110 = SUMIFS(PostingAmount, LineCode, "110")
Line111 = SUMIFS(PostingAmount, LineCode, "111")
Line112 = Line110 + Line111
Line205 = SUMIFS(PostingAmount, LineCode, "205")
Line405 = SUMIFS(PostingAmount, LineCode, "405")
Line113A = Line109 - Line112
Line113B = Line205 + Line405
Line113C = Line113A + Line113B
Line114 = MAX(-Line113C, 0)
Line115 = MAX(Line113C, 0)
```

**Return Form.** Show the approved figures in the correct CRA/RQ electronic or permitted paper layout, with field definitions, account/period/method, unresolved items and sign-off status. Use the actual instruction for nearest-dollar sales reporting and cents for tax. A working-copy rendering must say it is a preparation aid, not a submitted return. Do not present line 109 alone as the final payable balance.

Recalculate and cache every formula using an available spreadsheet engine, then reopen/read back the resulting workbook and check formulas, amounts and error cells. If using LibreOffice, use a distinct output directory/file to avoid an ineffective conversion onto the input itself. The prior literal machine-specific `soffice` path is not a universal requirement. Do not say the workbook was recalculated or tested in the filing portal unless that actually happened.

### Bank parsing and source trace

The old bank-specific formats remain **illustrative parser hints**, not verified current vendor specifications. Inspect each real file's headings, date examples, currency, debit/credit signs and balance movement first. Do not silently swap day/month or combine CAD/USD columns.

| Previous parser example | What to inspect in the actual export |
|---|---|
| RBC: Account Type, Account Number, Transaction Date, Cheque Number, Description 1/2, CAD$, USD$; formerly described as MM/DD/YYYY with signed amounts | Confirm actual headers/date order, which currency column applies and sign direction; retain both descriptions and account trace. |
| TD: Date, Transaction Description, Debit, Credit, Balance; formerly MM/DD/YYYY | Verify date convention and separate debit/credit meaning; POS W/D and PREAUTH PYMT are transaction clues only. |
| Scotiabank: Date, Description, Withdrawals, Deposits, Balance; formerly DD/MM/YYYY | Confirm actual date examples instead of borrowing RBC/TD assumptions. |
| BMO: Transaction Date, Description, Amount; formerly a single signed column | Test sign against balance movements and actual source entries. |
| CIBC CSV/QFX: Date, Description, Debit, Credit; formerly YYYY-MM-DD | Inspect real headers/QFX structure, dates and signs. |

| Description hint | Reconciliation meaning, not tax proof |
|---|---|
| POS / POS W/D / POS PURCHASE | Possible card purchase; obtain the actual receipt/supply. |
| PREAUTH / PREAUTH PYMT / PAP | Possible preauthorized debit; identify the underlying payment. |
| INTERAC E-TRANSFER / FROM / TO | Receipt/payment; establish sale, contractor, refund, loan, owner or own-account movement. |
| ONLINE BANKING TRANSFER / TFR | Possible internal movement; match both accounts/IDs before exclusion. |
| DIRECT DEPOSIT / DIR DEP | Incoming funds, not automatically sales. |
| CRA FED / RECEIVER GENERAL | Possible tax payment/refund; establish account, period and nature. |
| NSF / NSF FEE / MONTHLY FEE / SERVICE CHARGE | Possible financial charge; determine the actual service/contract and tax. |
| INTL PURCHASE / FX FEE | Separate underlying purchase, currency conversion and any fee; do not infer import tax. |
| ABM W/D / ATM | Cash withdrawal; trace cash spending before any expense/ITC claim. |

For a verified wholly taxable tax-inclusive **113.00 at 13%**, tax = 113 × 13/113 = **13.00** and net **100.00**. This algebra does not establish that an arbitrary bank amount includes tax, and cannot be applied to an untaxed gratuity, exempt component, loan or mixed-rate invoice. [CRA rates](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/charge-collect-place-supply.html), [ITC evidence rules](https://laws-lois.justice.gc.ca/eng/regulations/SOR-91-45/section-3.html).

For foreign currency, [ETA 159](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-159.html) uses the tax-payable date or another Minister-acceptable day. [Memorandum 3-6 paragraphs 3–15](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/3-6/conversion-foreign-currency.html) permits stated alternatives including payment/acquisition dates and monthly averages, with consistency and documentation. Sources may include actual conversion, usual conversion source, a Canadian chartered bank, Bank of Canada or CBSA as applicable. Record the chosen method/rate/date in L and supporting evidence; do not always force daily Bank of Canada or the bank settlement date.

### Completion checklist

Return a clear status: supported draft ready for authorized review, or incomplete with the exact unresolved items and their tax effect. Confirm all of these before calling the calculation complete:

1. Actual taxpayer, normal registration, effective dates, assigned authority/period and method established.
2. Full source coverage and bank/ledger/processor reconciliation, with transfers, draws, loans and cash traced.
3. Accrual tax points and prior-period reporting checked, including unpaid invoices, deposits and duplication.
4. Supply status, actual province/date and zero-rating/exemption evidence supported.
5. Correct current invoice bands, legal recipient and supplier regime; required documents obtained before ITC claim.
6. Commercial allocation, capital/entity rules, meal/tip, home, club and personal restrictions applied with conditions.
7. Actual imported-supply definition tested; simplified tax not claimed as ordinary ITC; 405 included where required.
8. Bad debts, recoveries, notes, time windows and prior claims reconciled without duplication.
9. Own 101 tax-exclusive and, if used, 90/91/102 correctly separated.
10. Complete paper/electronic final-balance bridge, not just 109, including 205/405 and supported 110/111.
11. All original supplier/judgment families considered where present, with no name-based legal defaults.
12. Workpaper formulas recalculated/read back when a workbook was actually produced; uncertainties and triage flags visible.
13. Filing and payment deadlines/instalments distinguished and calendar-adjusted; no invented interest rate.
14. Accountant approval and taxpayer filing authorization stated honestly; no simulated receipt presented as a filing.
15. Actual submission/payment confirmations and record retention handled only when that separate authorized work is performed.

## When to refuse or refer

Preserve the original eight specialist routes. Explain which part can still be answered and what fact or separate method is needed; a referral is not a reason to invent a figure or abandon unrelated supported work.

| Route | Trigger and handoff | Official source |
|---|---|---|
| R-CA-1: QST/Quebec | Separate QST computation/filing: `qc-qst-return` and RQ. Federal GST/HST can still be analysed here; confirm RQ administration. | [RC4022 Quebec](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4022/general-information-gst-hst-registrants.html), [RQ rates](https://www.revenuquebec.ca/en/businesses/consumption-taxes/gsthst-and-qst/basic-rules-for-applying-the-gsthst-and-qst/tables-of-gst-and-qst-rates/) |
| R-CA-2: BC/SK/MB tax | Separate PST/RST liability, exemptions, registration and returns: `bc-pst`, `sk-pst`, `mb-rst`. Not federal GST34 ITCs. | [BC Act](https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/12035_03), [SK Finance](https://www.saskatchewan.ca/government/government-structure/ministries/finance), [MB bulletin](https://www.manitoba.ca/finance/taxation/pubs/bulletins/030.pdf) |
| R-CA-3: Quick Method | Actual valid election/eligibility and effective dates. Use its distinct remittance method and GST74/online election evidence; ordinary operating ITCs differ but some capital ITCs can remain. This audit does not supply a complete quick-rate engine. | [RC4058](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4058/quick-method-accounting-gst-hst.html) |
| R-CA-4: charities/NPOs/PSBs | Determine the actual entity, charity net-tax calculation/election, special quick method and public-service-body rebate rules. Not every NPO uses one universal simplified method. | [RC4022](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4022/general-information-gst-hst-registrants.html), [CRA eligibility notes](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/calculate-prepare-report/input-tax-credit/calculate-eligibility-percentage.html) |
| R-CA-5: First Nations relief | Actual statutory person/status, reserve/delivery/service facts and prescribed documents; do not infer relief from a name or postal address. Use CRA's relief route and a suitably qualified professional for unresolved cases. | [CRA First Nations guidance](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/charge-collect-indigenous-peoples.html) |
| R-CA-6: closely related election | Actual qualifying group/specified members, jointly filed election, scope/exclusions and effective dates under 156. Related ownership alone is not a blanket intercompany exemption or consolidated return. | [ETA 156](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-156.html) |
| R-CA-7: non-resident simplified business | If the client is the simplified registrant, its own registration/return regime is outside this regular method. If it is a normal Canadian buyer, apply the buyer/import tests above rather than refusing the entire return. | [CRA simplified-account rules](https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/digital-economy-gsthst/confirming-simplified-gst-hst-account-number.html) |
| R-CA-8: real property | Land/buildings, builder self-supply, occupancy, changes of use and housing rebates require the actual property method. Determine whether direct tax belongs on 205 under 228(4); do not reuse a personal-capital FMV shortcut. | [ETA 191](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-191.html), [228(4)](https://laws-lois.justice.gc.ca/eng/acts/E-15/section-228.html) |

Refer material financial-institution, passenger benefit/lease, mixed-special-regime or disputed tax-cap questions with the exact unresolved facts and source discrepancy. Do not claim any professional has approved or filed the result merely because a previous version had their name.

## Sources

Read date for each successful row: **13 November 2026**. The scope column identifies the actual portions read, not a claim to read entire Acts/large guides or to audit every special regime. Source identifiers are evidence references, not extra legal authority. Quotes are short source locators. The actual unyearlabelled working-copy PDF was downloaded, text-extracted and visually inspected; no taxpayer return/account was submitted during this audit.

| Source and actual portion read | Official URL | Read on |
|---|---|---|
| G01: Current federal rates; delivered goods; postage; read for Rates; sale of goods; postage stamps and postage meter: “14% HST rate” | https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/charge-collect-place-supply.html | 2026-11-13 |
| G02: Province rules; read for ss5–13;13(1)–(2);14–17; transportation/special-case headings: “General rule for services” | https://laws-lois.justice.gc.ca/eng/regulations/SOR-2010-117/FullText.html | 2026-11-13 |
| G03: Canada/outside-Canada place; read for 142(1)(a),(c),(g);(2): “performed in whole or in part in Canada” | https://laws-lois.justice.gc.ca/eng/acts/E-15/section-142.html | 2026-11-13 |
| G04: Non-resident deeming; read for 143(1)(a)–(c): “Supply by non-resident” | https://laws-lois.justice.gc.ca/eng/acts/E-15/section-143.html | 2026-11-13 |
| G05: Definitions; read for commercial activity; exclusive; financial service(a)–(t); basic tax content: “all or substantially all” | https://laws-lois.justice.gc.ca/eng/acts/E-15/section-123.html | 2026-11-13 |
| G06: Exempt categories; read for Schedule V Parts I–VII, especially I6/13, VI1/24 and VII1: “a municipal transit service” | https://laws-lois.justice.gc.ca/eng/acts/E-15/section-sched200860.html | 2026-11-13 |
| G07: Zero-rated categories and exports; read for Schedule VI Parts I–V; V1/7/8/10/10.1/12/23; VII1–3;IX: “advisory, professional or consulting service” | https://laws-lois.justice.gc.ca/eng/acts/E-15/page-121.html | 2026-11-13 |
| G08: ITC entitlement and evidence; read for 169(1),(4),(5): “Required documentation” | https://laws-lois.justice.gc.ca/eng/acts/E-15/section-169.html | 2026-11-13 |
| G09: Actual invoice bands/fields; read for 3(a),(b),(c): “$100 or more and less than $500” | https://laws-lois.justice.gc.ca/eng/regulations/SOR-91-45/section-3.html | 2026-11-13 |
| G10: Invoice transition and e-filing effective date; read for Changes to documentary requirements; Mandatory electronic filing: “effective April 20, 2021” | https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/news118/news118-excise-gst-hst-news-no-118.html | 2026-11-13 |
| G11: ITC type/use chart; read for Operating, meal, club, capital personal property/passenger charts and notes: “More than 50%” | https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/calculate-prepare-report/input-tax-credit/calculate-eligibility-percentage.html | 2026-11-13 |
| G12: ITC time windows and invoice table; read for Time limit; two examples; records table: “Records you need to support your claim” | https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/calculate-prepare-report/input-tax-credit.html | 2026-11-13 |
| G13: Substantially-all use deeming; read for 141(1)–(5): “Use in commercial activities” | https://laws-lois.justice.gc.ca/eng/acts/E-15/section-141.html | 2026-11-13 |
| G14: Restricted inputs and home office; read for 170(1)(a),(a.1),(b),(c);(2): “principal place of business” | https://laws-lois.justice.gc.ca/eng/acts/E-15/section-170.html | 2026-11-13 |
| G15: Meal adjustment statute; read for 236(1),(1.1),(1.2),(2): “Food, beverages and entertainment” | https://laws-lois.justice.gc.ca/eng/acts/E-15/section-236.html | 2026-11-13 |
| G16: Meal exceptions and convention rule; read for 67.1(1),(1.1),(2)(a)–(f),(3),(5): “Fees for convention, etc.” | https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-67.1.html | 2026-11-13 |
| G17: Capital personal property purchase; read for 199(1)–(4): “use primarily in commercial activities” | https://laws-lois.justice.gc.ca/eng/acts/E-15/section-199.html | 2026-11-13 |
| G18: Capital personal property change/disposal; read for 200(1)–(3): “basic tax content” | https://laws-lois.justice.gc.ca/eng/acts/E-15/section-200.html | 2026-11-13 |
| G19: Passenger acquisition tax cap; read for 201(a),(b),A/B/C: “Value of passenger vehicle” | https://laws-lois.justice.gc.ca/eng/acts/E-15/section-201.html | 2026-11-13 |
| G20: Individual/partnership passenger route; read for 202(1)–(4), especially(4)A/B: “Non-exclusive use of passenger vehicle or aircraft” | https://laws-lois.justice.gc.ca/eng/acts/E-15/section-202.html | 2026-11-13 |
| G21: Consolidated vehicle ceilings; read for 7307(1)(b)A(ix);(1.1);(3): “after 2024, $38,000” | https://laws-lois.justice.gc.ca/eng/regulations/C.R.C.,_c._945/section-7307.html | 2026-11-13 |
| G22: 2026 official vehicle announcement; read for January14,2026 release; changes/unchanged bullets: “from $38,000 to $39,000” | https://www.canada.ca/en/department-finance/news/2026/01/government-announces-the-2026-automobile-deduction-limits-and-expense-benefit-rates-for-businesses.html | 2026-11-13 |
| G23: Imported taxable supply definition; read for imported taxable supply(a)(i)–(vi),(c)(i)–(iii); other limbs inspected: “other than a zero-rated or prescribed supply” | https://laws-lois.justice.gc.ca/eng/acts/E-15/section-217.html | 2026-11-13 |
| G24: Import federal tax; read for 218 operative provision: “at the rate of 5%” | https://laws-lois.justice.gc.ca/eng/acts/E-15/section-218.html | 2026-11-13 |
| G25: Import provincial tax; read for 218.1(1)(a),A/B/C;(1)(b);FI provisions inspected: “resident in a participating province” | https://laws-lois.justice.gc.ca/eng/acts/E-15/section-218.1.html | 2026-11-13 |
| G26: Prescribed import use and special branches; read for Part5 Division2,s7;7.01;Part4s5: “an extent of at least 10%” | https://laws-lois.justice.gc.ca/eng/regulations/SOR-2010-151/FullText.html | 2026-11-13 |
| G27: Imports/exports practical route; read for Imported goods; imported services/IPP: “less than 90%” | https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/charge-collect-imports-exports.html | 2026-11-13 |
| G28: Simplified supplier verification; read for Requirements to charge GST/HST; normal registry link: “cannot claim input tax credits” | https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/digital-economy-gsthst/confirming-simplified-gst-hst-account-number.html | 2026-11-13 |
| G29: PCNO prescribed exceptions; read for 3.2(2)(a)–(d): “in its capacity as the acquirer” | https://laws-lois.justice.gc.ca/eng/regulations/SOR-91-26/section-3.2.html | 2026-11-13 |
| G30: Small supplier enacted base; read for 148(1),(2),(4): “made inside or outside Canada” | https://laws-lois.justice.gc.ca/eng/acts/E-15/section-148.html | 2026-11-13 |
| G31: Registration effective dates; read for Most businesses table and Examples2–4; taxis/nonresidents headings: “within 29 days” | https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/when-register-charge.html | 2026-11-13 |
| G32: General guide bounded practical portions; read for Quebec; Reporting periods; gifts; instalments; record and correction headings: “Revenu Québec generally administers the GST/HST” | https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4022/general-information-gst-hst-registrants.html | 2026-11-13 |
| G33: Accrual/payability; read for 168(1),(2),(9): “earlier of the day” | https://laws-lois.justice.gc.ca/eng/acts/E-15/section-168.html | 2026-11-13 |
| G34: Net tax and ITC windows; read for 225(1),(2),(3),(3.1),(4),specified-person provisions: “all amounts that became collectible” | https://laws-lois.justice.gc.ca/eng/acts/E-15/section-225.html | 2026-11-13 |
| G35: Bad debt; read for 231(1),(1.1),(3),(4): “dealing at arm’s length” | https://laws-lois.justice.gc.ca/eng/acts/E-15/section-231.html | 2026-11-13 |
| G36: Credit/debit notes; read for 232(1),(2),(3)(a)–(d): “Credit or debit notes” | https://laws-lois.justice.gc.ca/eng/acts/E-15/section-232.html | 2026-11-13 |
| G37: Return fields and final-balance route; read for Line-by-line101,90/91/102,103–115,205/405; schedule notes: “Do not mail us your working copy.” | https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/calculate-prepare-report/instructions-preparing-return.html | 2026-11-13 |
| G38: Return due dates enacted; read for 238(1)(a)(i)–(iii),(b),(4): “within three months” | https://laws-lois.justice.gc.ca/eng/acts/E-15/section-238.html | 2026-11-13 |
| G39: Payment due dates enacted; read for 228(1),(2),(3);(4) inspected: “on or before April 30” | https://laws-lois.justice.gc.ca/eng/acts/E-15/section-228.html | 2026-11-13 |
| G40: Calendar and deadline guide; read for Due dates; monthly/quarterly; annual exceptions: “on the next business day” | https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/file-gst-hst-return/reporting-requirements-deadlines.html | 2026-11-13 |
| G41: Instalments enacted; read for 237(1)–(3): “less than $3,000” | https://laws-lois.justice.gc.ca/eng/acts/E-15/section-237.html | 2026-11-13 |
| G42: Electronic filing law/penalty; read for 2(a)–(d);3(a),(b): “for the first failure” | https://laws-lois.justice.gc.ca/eng/regulations/SOR-2010-150/FullText.html | 2026-11-13 |
| G43: Late filing enacted; read for 280.1(a),(b): “number of complete months” | https://laws-lois.justice.gc.ca/eng/acts/E-15/section-280.1.html | 2026-11-13 |
| G44: Late-payment interest; read for 280(1),(2),(3),(4.1): “interest at the prescribed rate” | https://laws-lois.justice.gc.ca/eng/acts/E-15/section-280.html | 2026-11-13 |
| G45: Daily compounding; read for 124(1),(2): “shall be compounded daily” | https://laws-lois.justice.gc.ca/eng/acts/E-15/section-124.html | 2026-11-13 |
| G46: Filing penalty practice; read for Late/electronic penalties: “You have $0 owing” | https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/file-gst-hst-return/reporting-requirements-deadlines/gst-hst-filing-penalties.html | 2026-11-13 |
| G47: CAD statutory basis; read for 159 operative: “Value in Canadian currency” | https://laws-lois.justice.gc.ca/eng/acts/E-15/section-159.html | 2026-11-13 |
| G48: CAD permitted methods; read for paras3–15; acceptable sources13–15: “the source used for an actual conversion” | https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/3-6/conversion-foreign-currency.html | 2026-11-13 |
| G49: Tips and travel; read for Gratuities; domestic/international passenger services: “Gratuities that customers voluntarily give” | https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/charge-collect-specific-situations/gst-hst-information-travel-convention-industry.html | 2026-11-13 |
| G50: Promotional gifts; read for Promotional gifts and free samples: “promote or facilitate your taxable sales” | https://www.revenuquebec.ca/en/businesses/consumption-taxes/gsthst-and-qst/special-cases-gsthst-and-qst/promotional-gifts-and-free-samples/ | 2026-11-13 |
| G51: Quick method scope/election; read for How to elect; claiming ITCs; scope/Quebec: “Form GST74” | https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4058/quick-method-accounting-gst-hst.html | 2026-11-13 |
| G52: First Nations relief referral; read for Paying/charging; documentary and delivery examples: “Documents you need for GST/HST relief” | https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/charge-collect-indigenous-peoples.html | 2026-11-13 |
| G53: Closely related election referral; read for 156(1),(1.1); election provision: “qualifying group” | https://laws-lois.justice.gc.ca/eng/acts/E-15/section-156.html | 2026-11-13 |
| G54: Real-property self-supply referral; read for 191(1),(3) operative conditions: “Self-supply of single unit residential complex” | https://laws-lois.justice.gc.ca/eng/acts/E-15/section-191.html | 2026-11-13 |
| G55: Records; read for 286(1),(3),(3.1),(4): “Keeping books and records” | https://laws-lois.justice.gc.ca/eng/acts/E-15/section-286.html | 2026-11-13 |
| G56: BC separate PST rate; read for 34(1); currentNovember10,2026: “7% of the purchase price” | https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/12035_03 | 2026-11-13 |
| G57: Manitoba separate RST; read for RST030 revisedJuly2026,section1: “rate of 7 per cent” | https://www.manitoba.ca/finance/taxation/pubs/bulletins/030.pdf | 2026-11-13 |
| G58: Saskatchewan separate PST; read for Programs and services,Provincial Sales Tax: “a 6% sales tax” | https://www.saskatchewan.ca/government/government-structure/ministries/finance | 2026-11-13 |
| G59: Quebec separate QST and federal rate; read for Present rates table: “January 1, 2013 – present” | https://www.revenuquebec.ca/en/businesses/consumption-taxes/gsthst-and-qst/basic-rules-for-applying-the-gsthst-and-qst/tables-of-gst-and-qst-rates/ | 2026-11-13 |
| G60: actual CRA working copy, read for complete one-page text and rendered fields 101–115 including 205/405; “Do not use this working copy to file your return” | https://www.canada.ca/content/dam/cra-arc/migration/cra-arc/tx/bsnss/tpcs/gst-tps/bspsbch/rtrns/wrkngcp-eng.pdf | 2026-11-13 |
| G61: deposit forfeiture, read for ETA 182(1)–(3), deemed-tax conditions and exceptions; “Forfeiture, extinguished debt, etc.” | https://laws-lois.justice.gc.ca/eng/acts/E-15/section-182.html | 2026-11-13 |

Not yet confirmed: operative consolidated amendment implementing the announced 2026 CAD 39,000 passenger cap; do not finalize a cap-dependent 2026 claim from the announcement alone. Current vendor billing entities/ownership/registration and universal bank export formats are not established by recognition strings. Actual taxpayer invoices, legal status, use, elections, export and tax-point facts remain case-specific. This is not an end-to-end audit of Quick Method, charity/PSB rebates, Indigenous relief, related elections, real property, SLFIs or separate QST/PST/RST engines. Their scoped referral routes remain above. Current filing-portal screens were not exercised, no live submission/payment was made, and no workbook was generated/recalculated merely to write these instructions. Quarterly interest rates must be fetched for an actual interest calculation. The shared workflow's generic legal defaults are not re-audited or repaired by this Canadian change.

### Version history

* **2.1, 13 November 2026:** source audit, 2026 regular-method refresh, invoice thresholds/evidence, imports/simplified registration, capital/entity restrictions, meals, actual return bridge, deadlines and evidence-first recognition corrected. All 94 original supplier rows, 15 judgment categories, six original example families, three-sheet workpaper, bank hints, ten onboarding topics and eight referrals preserved with corrected conditions. No historical accountant approval carried into the revised version.
* **2.0, April 2026:** supplier library, six examples, rules/judgment catalogue, workbook, bank parsing and onboarding structure introduced. Duplicate version-history boilerplate consolidated; historical text and approvals remain in Git.
