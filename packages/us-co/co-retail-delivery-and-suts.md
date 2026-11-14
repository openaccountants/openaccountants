---
name: co-retail-delivery-and-suts
description: >
  Colorado 2026 retail delivery fee eligibility, fiscal-year rates, separate
  DR 1786 registration/filing, refunds and collection-versus-absorption election.
  Also covers SUTS registration, participating home-rule jurisdictions and
  current GIS limitations, with ordinary sales/use tax routed to co-sales-tax.
jurisdiction: US-CO
category: state-tax
tax_year: 2026
last_updated: 2026-11-13
version: 1.0
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: vat-gst
type: situation-rules
depends_on:
  - us-sales-tax
  - co-sales-tax
---

# Colorado retail delivery fee and SUTS v1.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

Retailers and marketplace facilitators causing motor-vehicle deliveries to
Colorado locations during 2026, and retailers considering the Sales & Use Tax
System (SUTS). Retail delivery fees are a separate account and return from sales
tax. They are not filed through SUTS.

`co-sales-tax` owns sales/use rates, nexus, transaction taxability, shipping-charge
conditions and sourcing. `us-sales-tax` owns the federal framework. Income tax
routes to `co-income-tax` and `co-corporate-tax`, not a duplicated flat rate here.
Special excises, lodging, marijuana, vehicle registration, construction permits,
severance and enterprise-zone credits remain outside this skill's computations.

## Ask the client first

1. Prior/current calendar-year Colorado gross retail goods/services sales, wholesale deductions, direct/facilitated channels and all related sales/use accounts.
2. Physical/economic sales-tax nexus and which seller/facilitator collects each transaction's state tax.
3. Delivery date, destination, post-order transportation legs, taxable contents and purchaser exemption evidence.
4. Single sale versus separate subscriptions/orders, returns versus pre-shipment cancellations.
5. Existing fee account, assigned sales filing frequency and actual collection/absorption election.
6. SUTS/Revenue Online access, each home-rule jurisdiction and required use-tax/fee/amendment filings.

## Rates, bands and thresholds

| Item | Applicable period and conditions | Official source |
|---|---|---|
| Total fee | $0.28 per qualifying sale January 1-June 30, 2026 | https://tax.colorado.gov/retail-delivery-fee-rates |
| Total fee | $0.31 per qualifying sale July 1, 2026-June 30, 2027 | https://tax.colorado.gov/retail-delivery-fee-rates |
| Community access component | $0.0567 January-June 2026; $0.0792 July 2026-June 2027 | https://tax.colorado.gov/retail-delivery-fee-rates |
| Clean fleet component | $0.0589 then $0.0609 for the same two periods | https://tax.colorado.gov/retail-delivery-fee-rates |
| Clean transit component | $0.0333 then $0.0344 for the same two periods | https://tax.colorado.gov/retail-delivery-fee-rates |
| General component | $0.0933 then $0.0965 for the same two periods | https://tax.colorado.gov/retail-delivery-fee-rates |
| Bridge/tunnel component | $0.0300 then $0.0310 for the same two periods | https://tax.colorado.gov/retail-delivery-fee-rates |
| Air pollution component | $0.0078 then $0.0080 for the same two periods | https://tax.colorado.gov/retail-delivery-fee-rates |
| Qualified-business exemption | Prior-calendar-year Colorado retail sales of goods, commodities/services $500,000 or less; gross across accounts/sites minus wholesale sales | https://tax.colorado.gov/retail-delivery-fee-retailers |
| No preceding-year Colorado sales | Initially exempt, but begin at first day of first month commencing at least 90 days after current-year cumulative sales exceed $500,000; not an automatic full first-year holiday | https://tax.colorado.gov/special-topics-retail-delivery-fees |
| Return/payment | Same assigned schedule as sales tax; generally 20th following period, next business day rule; zero returns until account closed | https://tax.colorado.gov/retail-delivery-fee-reporting-and-payment |
| Erroneous prior overpayment credit | DOR refund page permits qualifying line 6 credit within three years; distinguish delivered returns from pre-shipment cancellations | https://tax.colorado.gov/retail-delivery-fee-refunds |
| New annual rate publication | By April 15 for upcoming July fiscal-year change | https://tax.colorado.gov/retail-delivery-fee-rates |

The component rows add to the stated total for each period. Do not compute a
calendar year using one fiscal year's rate or round each component separately.
The fee is excluded from state and state-administered local sales-tax bases;
self-collecting home-rule cities may tax it under their own rules.

## The method, step by step

### A. Establish who is liable and whether the delivery qualifies

1. Start with the retailer/facilitator that is liable to collect state sales/use
   tax on the goods. No state nexus means no fee obligation on that basis;
   use `co-sales-tax` for the actual nexus test. If a qualified facilitator
   collects tax on its sale, it is responsible for that sale's delivery fee,
   not the marketplace seller. Direct-sale obligations remain distinct.
2. Apply the qualified-business test to the prior year's Colorado retail goods,
   commodities and services, not nationwide turnover and not deliveries alone.
   DOR computes across gross sales reported for all sites/accounts minus
   wholesale sales. Do not substitute sales tax's direct-only marketplace nexus
   test for this different threshold. The precise treatment of facilitated
   turnover in a mixed-channel seller's fee exemption remains reserved below.
3. For no prior Colorado sales, monitor the current-year crossing and commencement
   date. DOR's retailer page variously says first filing period and first month;
   the detailed publication says first month after the 90th day. Use that
   month-based rule and obtain account-specific confirmation if a nonmonthly
   assignment creates a conflict. Exactly the exemption threshold is included.
4. A qualifying sale must include at least one item subject to state sales/use
   tax, delivered by motor vehicle to a Colorado location after the order.
   Mixed taxable/exempt contents still qualify. Entirely exempt sales or
   exempt purchasers do not, if supported by valid documents.
5. Any post-order motor-vehicle leg in Colorado counts, including USPS,
   third-party or purchaser-hired carrier. Free shipping does not remove the
   fee. Customer pickup at the retailer's business location does not qualify;
   a delivery to a Colorado locker or PO box can qualify. Out-of-state
   destinations do not qualify merely because the purchaser lives in Colorado.
6. One retail sale produces one fee even if shipped in several parcels. Apply
   a consistent reasonable documented shipment-to-sale attribution. A prepaid
   subscription with one order/payment is one sale; cancellable recurring
   orders with separate payments are separate sales. For short-term leases,
   lessor acquisition/lease-tax treatment determines who has the retail sale;
   do not automatically assess every instalment.
7. Repair/diagnosis service calls and sell-and-install transactions differ.
   The primary purpose controls; lump-sum contractors normally consume rather
   than resell materials. The retailer delivering goods to the contractor
   may still have a qualifying sale. Direct-pay permit purchasers remit under
   their permit conditions. Free warranty exchanges/replacements create no
   additional fee without another retail sale.

Sources: https://tax.colorado.gov/special-topics-retail-delivery-fees;
https://tax.colorado.gov/retail-delivery-fee-retailers;
https://tax.colorado.gov/retail-delivery-fee-marketplace-sales;
https://tax.colorado.gov/retail-delivery-fee-faqs.

### B. Choose collection or absorption and register the separate account

Elect consistently to collect the fee or pay it for customers; the detailed
publication makes the election with the first qualifying sale. Collection uses
a separate Retail Delivery Fee line distinct from price/tax/other charges.
Absorption does not require a customer fee line. Either method leaves the
retailer responsible for remittance. There is no vendor service allowance.

Revenue Online > More > Other Registrations > Retail Delivery Fee Registration >
Commence Date. A missing link may mean auto-registration; check the account
before creating a duplicate. Filing DR 1786 can also establish the account.
New Revenue Online logins require account information/Letter ID; request a
Letter ID through Additional Services if needed. Fee-account closure uses
Additional Actions > Cease Account and the actual closure date, with returns
through closure. Source: https://tax.colorado.gov/retail-delivery-fee-accounts.

### C. Compute, file and reconcile DR 1786

1. Count qualifying **sales**, not units, parcels, shipping invoices or customer
   addresses. Split counts across the midyear rate change, using actual sale/
   delivery records. The rate ownership here does not determine ordinary
   delivery-charge taxability, which belongs to `co-sales-tax`.
2. One DR 1786 covers all locations for an account. It is statewide, not a
   separate jurisdiction line per city. Apply the period's rate and reconcile
   fee liability, collected fees and retailer-paid fees.
3. Excess collected and not refunded goes on line 4 and must be remitted.
   Do not keep an overcollection because the business is exempt.
4. File through Revenue Online or the current paper DR 1786; SUTS does not
   receive this return. Follow the sales account's assigned monthly/quarterly/
   annual schedule, not an invented threshold based on fee receipts. Active
   accounts file zero returns too. Annual filers must split the rate periods.
5. Save return confirmation and separately verify payment is posted to the
   correct fee account/period. DOR does not automatically reallocate a payment
   sent to the wrong account. Request a written transfer through Revenue Online.

Sources: https://tax.colorado.gov/retail-delivery-fee-reporting-and-payment;
https://tax.colorado.gov/DR1786. Complete final 2026 PDF line mapping beyond the
actually read online instructions remains pending, not invented.

### D. Distinguish returned goods, cancellations and erroneous fees

Once a qualifying delivery happened, returning all goods and refunding their
price/sales tax does **not** refund the delivery fee. The return journey is not
a new retail sale, so it creates no additional fee. A sale canceled **before
shipment**, with full price, sales tax and fee refunded, can support the DOR's
credit procedure. An erroneously collected fee on an exempt transaction is
also distinct from a valid fee on later-returned goods.

Use the actual refund instructions: DR 0137E for fee overpayments, DR 0137B
when combined with sales tax, or the permitted prior-overpayment line 6 credit
with its conditions. Keep cancellation/refund dates, original transaction,
period and proof. Do not carry forward the old whole-return blanket credit.
Sources: https://tax.colorado.gov/retail-delivery-fee-refunds and
https://tax.colorado.gov/retail-delivery-fee-faqs.

### E. SUTS: verify participating jurisdictions and the current service scope

SUTS is optional consolidated filing/payment for state-administered taxes and
**participating** self-collecting home-rule jurisdictions. Participation does
not make their tax bases/exemptions identical. Do not assume all home-rule
cities participate or repeat the old approximate city count.

1. Have the state sales-tax account/licences and Revenue Online administrative
   access first. Separately register SUTS, verify email and connect the account.
   Check the actual SUTS jurisdiction list for each city. Denver, Boulder,
   Aurora, Colorado Springs, Fort Collins and Greeley appear in the read list;
   this is not a complete or permanent participation guarantee.
2. Use exact address/product/date lookup. **Since September 29, 2026, bulk
   address-spreadsheet lookup is paused**, with restart scheduled January 1,
   2027. Single-address GIS lookup and SUTS filing/payment remain active and
   free. Do not promise a bulk lookup workflow during the pause.
3. Prepare the consolidated return with each site's relevant jurisdiction and
   tax-base classifications. Match state and city sales, deductions and tax;
   home-rule participants follow the state filing frequency under DOR's FAQ.
   Review, submit and save acceptance; verify payment allocation and receipts.
4. File directly with any nonparticipating city as its law requires. A business
   with no delivery may still have sales/home-rule obligations.
5. State consumer use tax DR 0251/DR 0252, delivery fees and other state fees are
   outside SUTS. Some participating home-rule combined returns include local
   use tax. Amendments also proceed outside SUTS with DOR/the relevant city.
   Do not use obsolete DR 0104US; `co-sales-tax` owns that correction.

Sources: https://tax.colorado.gov/SUTS-info;
https://tax.colorado.gov/SUTS-FAQ;
https://tax.colorado.gov/SUTS-Jurisdictions.

## Worked cases

### AcmeGoods, Indianapolis remote seller: separate channel responsibility

Preserve AcmeGoods' $4 million national direct website sales, including $400,000
Colorado, plus $6 million national Amazon sales, including $700,000 Colorado.
Colorado total is $1.1 million. A qualifying facilitator handles the $700,000
channel's tax/fee. The previous claim that $400,000 direct turnover conclusively
exempts the seller from delivery fees is withdrawn: direct-only nexus and the
fee exemption are different tests. Confirm the mixed-channel fee-threshold
basis before deciding the seller's direct fee liability.

For transparent arithmetic, assume exactly 1,000 qualifying **direct sales**
delivered each month, 6,000 in each half year. This replaces the former mutually
inconsistent order counts/average order value. If the seller is fee-liable,
calendar 2026 fee is $3,540. If exemption is established, direct fee is zero.
Collecting versus absorbing the $3,540 changes customer charges/employer expense,
not the amount remitted. Amazon-handled deliveries are not counted a second time.

```oa-check
name: Colorado AcmeGoods conditional fee and absorption
inputs:
  first_half_sales: 6000
  second_half_sales: 6000
steps:
  first_half_fee: first_half_sales * 0.28
  second_half_fee: second_half_sales * 0.31
  liable_fee: first_half_fee + second_half_fee
  exempt_fee: liable_fee * 0
  collected_retailer_expense: liable_fee * 0
  absorbed_retailer_expense: liable_fee
  expense_difference: absorbed_retailer_expense - collected_retailer_expense
expected:
  first_half_fee: 1680
  second_half_fee: 1860
  liable_fee: 3540
  exempt_fee: 0
  expense_difference: 3540
```

### Mountain Mug Co., Bozeman: small seller

Preserve the Etsy/website case: $180,000 national Etsy sales, $9,000 Colorado;
$45,000 direct national sales, $3,000 Colorado. Total Colorado sales $12,000 is
below the fee exemption threshold whether both channels or only direct sales
are tested, assuming this is the relevant prior-year total and no other accounts.
The old contradictory mug-count projection is not used. Direct sales-tax nexus
still requires a physical-presence check; low turnover alone does not settle it.
A qualifying facilitator remains responsible for its facilitated sales.

```oa-check
name: Colorado Mountain Mug qualified business
inputs:
  facilitated_colorado: 9000
  direct_colorado: 3000
steps:
  colorado_sales: facilitated_colorado + direct_colorado
  headroom: 500000 - colorado_sales
  direct_fee: colorado_sales * 0
expected:
  colorado_sales: 12000
  headroom: 488000
  direct_fee: 0
```

### Larimer Outfitters, Denver: midyear rates and returned goods

Preserve the retailer with $1.4 million in-store sales, $600,000 national online
sales including $200,000 Colorado deliveries. Relevant Colorado sales are
$1.6 million, above exemption. Assume 4,000 qualifying deliveries split equally
between halves of 2026: fee $1,180, not the old $1,160 based on one obsolete rate.
Returning a delivered order does not reduce that fee. One July sale canceled
before shipment with full qualifying refund can support a $0.31 credit, subject
to the actual credit conditions. The old Denver combined rate/breakdown was
inconsistent and is not retained as current; `co-sales-tax` owns local-rate work.
Use SUTS only for participating sales-tax jurisdictions; file DR 1786 separately.

```oa-check
name: Colorado Larimer midyear delivery fee
inputs:
  january_june_sales: 2000
  july_december_sales: 2000
steps:
  fee: january_june_sales * 0.28 + july_december_sales * 0.31
  returned_after_delivery_credit: 0
  qualifying_preshipment_credit: 0.31
  fee_after_valid_credit: fee - qualifying_preshipment_credit
expected:
  fee: 1180
  returned_after_delivery_credit: 0
  fee_after_valid_credit: 1179.69
```

## Checks before finalising

- Determine tax collector, fee exemption and channel responsibility separately.
- Split fiscal-year rates; reconcile six components to the total, once per sale.
- Keep consistent collection/absorption election and supporting invoice records.
- Distinguish delivered returns from canceled-before-shipment transactions.
- Match fee account/period, zero returns, payment receipts and closure date.
- Check SUTS city participation and current GIS pause; fees/amendments remain outside.

## When to refuse or refer

Refer unresolved mixed-channel exemption basis, account commencement conflicts,
lease/contractor/direct-pay exceptions and home-rule taxability. Do not default
to charging a fee merely because uncertain; obtain the missing rule/facts.
Do not present sales tax as VAT/reverse charge or duplicate income-tax figures.

## Sources

| Source | URL | Reading scope | Read on |
|---|---|---|---|
| DOR delivery publication | https://tax.colorado.gov/special-topics-retail-delivery-fees | Read for all transaction/transport/exemption, subscription, lease, contractor, election, return/cancellation and filing sections | 2026-11-13 |
| DOR rates | https://tax.colorado.gov/retail-delivery-fee-rates | Read for every component and total in both 2026 periods and home-rule tax-base caveat | 2026-11-13 |
| DOR retailer eligibility | https://tax.colorado.gov/retail-delivery-fee-retailers | Read for prior/current-year thresholds, gross-minus-wholesale across accounts and commencement wording | 2026-11-13 |
| DOR marketplace | https://tax.colorado.gov/retail-delivery-fee-marketplace-sales | Read for facilitator liability and marketplace-seller nonliability on facilitated sales; not a mixed-channel threshold ruling | 2026-11-13 |
| DOR fee accounts | https://tax.colorado.gov/retail-delivery-fee-accounts | Read for actual Revenue Online registration, Letter ID, commencement and cessation steps | 2026-11-13 |
| DOR reporting/payment | https://tax.colorado.gov/retail-delivery-fee-reporting-and-payment | Read for schedule, one-account return, line 4 excess, active zero returns and payment allocation | 2026-11-13 |
| DOR DR 1786 landing | https://tax.colorado.gov/DR1786 | Read for qualification, no-prior-year rule, single-sale counting and zero returns; complete PDF fields not read | 2026-11-13 |
| DOR refunds | https://tax.colorado.gov/retail-delivery-fee-refunds | Read for DR0137E/0137B, line 6 prior overpayments and three-year conditions | 2026-11-13 |
| DOR FAQs | https://tax.colorado.gov/retail-delivery-fee-faqs | Read for free shipping, repair/contractor distinctions and delivered return versus pre-shipment cancellation | 2026-11-13 |
| DOR SUTS current notice | https://tax.colorado.gov/SUTS-info | Read for September 29, 2026 bulk-lookup pause, scheduled 2027 restart and continuing single lookup/filing | 2026-11-13 |
| DOR SUTS FAQ | https://tax.colorado.gov/SUTS-FAQ | Read for registration/access, state frequency, consumer-use exclusions, fees and amendments outside SUTS | 2026-11-13 |
| DOR SUTS jurisdictions | https://tax.colorado.gov/SUTS-Jurisdictions | Read for actual participating city entries; no total city-count assertion | 2026-11-13 |

Not yet confirmed: mixed-channel seller's facilitated-turnover treatment in the fee exemption, nonmonthly no-prior-year commencement conflict, complete current DR 1786 field mapping, full record-retention/penalty provisions, specific home-rule fee taxability and every jurisdiction's current participation/rate. All preexisting broader sales/nexus/sourcing topics are routed to co-sales-tax; old counts, speculative indexed rates and unsupported local combined rates are not current facts.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon. The most up-to-date version of this skill is maintained at https://www.openaccountants.com.
