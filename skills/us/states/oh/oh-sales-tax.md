---
name: oh-sales-tax
description: "Ohio sales and use tax for 2026: registration and marketplace nexus, taxable goods and services, sourcing, exemption certificates, UST-1 filing and discounts, use tax and late payments. Trigger on Ohio sales tax, OH sales tax, UST-1, vendor license, STEC B, economic nexus and sales tax holiday. Use oh-cat-tax for commercial activity tax."
version: "3.1"
jurisdiction: US-OH
tax_year: 2026
last_updated: 2026-11-27
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: vat-gst
type: situation-rules
---

# Ohio sales and use tax, tax year 2026

Ohio's state rate is **5.75%**; apply the county and transit rate for the legally sourced address and transaction date. Remote economic nexus is presumed above **$100,000** of Ohio receipts **or at 200 transactions** in the current or preceding calendar year. Monthly UST-1 returns and payment are ordinarily due on the **23rd**. The timely discount is **0.75%**, with the non-motor-vehicle cap of **$750 per license per month covered** for returns required from 1 January 2026. Sources: [R.C. 5739.02(A)](https://codes.ohio.gov/ohio-revised-code/section-5739.02), [5741.01(I)](https://codes.ohio.gov/ohio-revised-code/section-5741.01), [5739.12](https://codes.ohio.gov/assets/laws/revised-code/authenticated/57/5739/5739.12/9-30-2025/5739.12-9-30-2025.pdf), [ST 2025-02](https://tax.ohio.gov/business/ohio-business-taxes/sales-and-use/information-releases/st2025-02_vendor_timely_filing_discount_dec_2025).

## Scope and who this is for

Ohio vendors, remote sellers, marketplace facilitators, exemption-certificate users and buyers with untaxed purchases. For CAT use `oh-cat-tax`; for individual income tax use `oh-income-tax`; for payroll use `oh-payroll`; for other states use `us-sales-tax`. Special transaction and enforcement holds appear below. No missing client fact is supplied by assumption. Internet-access-only, cable/website-creation and provider-specific digital-service classifications require the special-case review below; do not infer their treatment from the hosted-CRM example.

## Ask the client first

Obtain the transaction dates and years; Ohio premises, employees, inventory and delivery arrangements; Ohio receipts and transaction counts for both calendar years; direct versus facilitated sales; product descriptions, contracts and business/personal use; order-receipt records and delivery/first-use addresses; exemptions and certificates; licenses and account filing schedule; prior returns, payments and annual liabilities; untaxed purchases and tax paid elsewhere; and notices or prior Department contact. Confirm these before calculating or filing.

## The method, step by step

### Registration and nexus

1. For taxable retail business at a fixed Ohio location, obtain the county vendor's license before selling: **$50 for each fixed place**. A qualifying transient vendor may instead obtain the **$50** transient license for counties without its fixed business location. These are application fees, not annual renewal charges. The increase from $25 took effect **9 April 2025**. [R.C. 5739.17(A), (C), (D)](https://codes.ohio.gov/ohio-revised-code/section-5739.17); [ODT registration](https://tax.ohio.gov/business/sales-and-use-tax/sales-and-use-tax).
2. Physical-presence nexus and other statutory contacts are separate from economic thresholds. A remote seller's nexus is presumed if Ohio gross receipts **exceed $100,000** or separate Ohio transactions **equal or exceed 200**, in either the current or preceding calendar year. Exactly $100,000 alone does not meet the receipts test. A seller with substantial nexus registers under **R.C. 5741.17**, subject to that section's exceptions; disputed nexus or rebuttal requires referral. [R.C. 5741.01(I)(2)-(3)](https://codes.ohio.gov/ohio-revised-code/section-5741.01); [5741.17](https://codes.ohio.gov/ohio-revised-code/section-5741.17).
3. Register through **OH|TAX eServices** after establishing the user account, or the Streamlined Sales Tax registration system. For a business located outside the US, ODT directs use of **UT 1000**. The out-of-state seller's license, consumer's use tax account and direct pay permit have **no fee**. An out-of-state seller making only marketplace sales for which the facilitator collects and pays Ohio tax does not need that seller's license. Check any physical presence or direct sales separately. [ODT registration](https://tax.ohio.gov/business/sales-and-use-tax/sales-and-use-tax); [nexus guidance](https://tax.ohio.gov/business/sales-and-use-tax).
4. A marketplace facilitator owns, operates or controls a marketplace and meets the facilitation activities in **5741.01(Q), (T)**; advertising alone is excluded. It aggregates its own and facilitated Ohio receipts/transactions for the same **over $100,000 / at least 200** tests. Its seller obligations start on the **first day of the first month beginning at least 30 days after nexus arises**. Maintain separate accounts for its own and facilitated sales as ODT directs. [R.C. 5741.01(E), (I)(4), (Q), (T)](https://codes.ohio.gov/ohio-revised-code/section-5741.01); [ODT facilitator guidance](https://tax.ohio.gov/business/sales-and-use-tax).

### Rates, bands and thresholds

| Item | Value and condition | Official source |
| --- | --- | --- |
| State component | 5.75% on taxable retail sales; use tax has the same state component | [R.C. 5739.02(A)(1)](https://codes.ohio.gov/ohio-revised-code/section-5739.02); [5741.02(A)(1)](https://codes.ohio.gov/ohio-revised-code/section-5741.02) |
| Q4 2026 combined rates | Cuyahoga 8.00%; Franklin 8.00%; Hamilton 7.80%; Lucas 7.75%; Montgomery 7.50%; Summit 6.75%; Stark 6.50% | [ODT 1 October–31 December 2026 table](https://tax.ohio.gov/business/sales-and-use-tax/rate-tables/by-county-q4-2026) |
| Transit districts | Licking (COTA) 8.25%; Delaware (COTA) 8.00%; Fairfield (COTA) 7.75%. Do not substitute the county's non-transit rate | [Q4 2026 table](https://tax.ohio.gov/business/sales-and-use-tax/rate-tables/by-county-q4-2026) |
| Warren change | 6.75% before 1 October 2026; 7.25% from that date | [ODT rate change notice](https://tax.ohio.gov/business/sales-and-use-tax/sales-and-use-tax) |

Look up the exact address and date in [The Finder](https://tax.ohio.gov/help-center/the-finder/the-finder). A remembered city rate or five-digit ZIP is not an address determination. Split a return when a rate changes during its period. For 2025 use the 2025 quarter's table; do not carry a 2026 local rate backwards.

### Sourcing and taxable price

| Transaction | Rule and exception | Official source |
| --- | --- | --- |
| Non-leased goods or digital goods: order and customer receipt in Ohio | Order-received location only if the vendor's system captures it when received and the receipt location falls under (C)(2)-(4). It is where the necessary order information initially arrives, not subsequent acceptance, fulfilment or shipping origin | [R.C. 5739.033(B)(1), (3)](https://codes.ohio.gov/ohio-revised-code/section-5739.033) |
| Other ordinary sales, including services and remote sales | Receipt at vendor's business first; otherwise known delivery/first-use location; then good-faith customer address in business records; then address obtained in the sale/payment instrument; finally shipping origin/service-provision address. Special statutory sourcing overrides this hierarchy | [R.C. 5739.033(C)](https://codes.ohio.gov/ohio-revised-code/section-5739.033) |
| Goods plus taxable service in one transaction | If in a single contract/transaction on the same invoice and the origin rule would split jurisdictions, (B)(4) places the transaction at the order-received location. Do not automatically source the service separately | [R.C. 5739.033(B)(4)](https://codes.ohio.gov/ohio-revised-code/section-5739.033) |
| Facilitated marketplace sales | Customer receipt location, then the good-faith address hierarchy in 5741.05(B). Titled vehicles, watercraft and outboards are excluded from this rule | [R.C. 5741.05(B)](https://codes.ohio.gov/ohio-revised-code/section-5741.05) |
| Consumer's further liability | For a qualifying goods/digital-goods sale under (B), payment of the invoiced tax at either order or receipt rate removes further Ohio tax, penalty and interest liability. Do not extend that relief to standalone services | [R.C. 5739.033(B)(2)](https://codes.ohio.gov/ohio-revised-code/section-5739.033) |

Include delivery and installation in taxable price where applicable. Vendor-funded discounts allowed and taken reduce price; third-party reimbursement can be included under the statutory conditions. Avoid a blanket statement that every mixed invoice is taxable: identify the components and apply the relevant rule; disputed bundles are held below. [R.C. 5739.01(H)](https://codes.ohio.gov/ohio-revised-code/section-5739.01).

### Exemption documents and use tax

Obtain the reason for an exemption and the prescribed certificate where required. Certificates are **not required** where the buyer's identity or item makes the transaction never taxable, or for interstate commerce. A missing certificate after **90 days** creates a tax presumption; the statute permits proof or a good-faith completed certificate within **120 days after written intent-to-assess notice**. Do not treat every incomplete certificate as an irreparable loss of exemption. [R.C. 5739.03(B)(1)-(5)](https://codes.ohio.gov/ohio-revised-code/section-5739.03).

Use **STEC U** for one purchase and **STEC B** for continuing purchases from the same seller. The SST certificate substitutes for the specified Ohio forms; MTC is limited to resale or incorporation into a product for sale. **STEC CC** involves contractor and exempt contractee certification; **STEC CO** protects the vendor, not the contractor. Direct-pay authority must be documented. [ODT certificate instructions](https://tax.ohio.gov/business/sales-and-use-tax/exemption-certificates).

For a business consumer's concurrently used digital good, software or service, **STEC MPU** shifts payment to the consumer and requires reasonable, consistent apportionment supported by contemporaneous records; software received in person at the vendor's business and direct-pay permit holders have different rules. [R.C. 5739.033(D)](https://codes.ohio.gov/ohio-revised-code/section-5739.033).

Accrue use tax on taxable Ohio use not already discharged by sales tax, including untaxed online purchases and taxable diversion from inventory. Apply the location-of-use rate and any exemption. Credit legally levied sales/use tax paid to another jurisdiction only to the permitted extent, excluding refundable/creditable amounts; pay any Ohio difference. Temporary use, produced inventory and property brought into Ohio have special valuation rules. [R.C. 5741.02(A)-(C)](https://codes.ohio.gov/ohio-revised-code/section-5741.02); [5741.01(G)](https://codes.ohio.gov/ohio-revised-code/section-5741.01).

For regular untaxed business purchases use the **consumer's use tax account / UUT-1**; individuals and infrequent purchases follow ODT's use-tax payment route. Do not simply place a business's purchases on an individual's return or assume they belong on UST-1. [ODT use tax instructions](https://tax.ohio.gov/business/sales-and-use-tax/use-streamlined-vda).

### Filing, discount and late payment

Monthly filing is the default; file nil returns while the account remains open. Use the assigned account frequency. ODT may authorize semi-annual vendor/seller filing for liability **under $1,200 per six months** and quarterly direct-pay/consumer use filing for liability **under $15,000 per quarter**. The ordinary deadline is the **23rd after the period**: semi-annual January–June is due **23 July**, July–December **23 January**; quarterly use periods are due **23 January, April, July and October**. Follow the Department's calendar for weekend/holiday extensions. [R.C. 5739.12(A), (C)(2)](https://codes.ohio.gov/assets/laws/revised-code/authenticated/57/5739/5739.12/9-30-2025/5739.12-9-30-2025.pdf); [ODT filing schedule](https://tax.ohio.gov/business/ohio-business-taxes/sales-and-use/license/).

File **UST-1** electronically through OH|TAX eServices, the Business Gateway or an authorized electronic method; pay electronically unless excused by the Commissioner. Enter gross sales including exempt sales on **line 1**, exemptions on **line 2**, and reconcile taxable sales and tax by jurisdiction. Retain the submitted return, confirmation and payment evidence. [R.C. 5739.12(A)(1)-(2)](https://codes.ohio.gov/assets/laws/revised-code/authenticated/57/5739/5739.12/9-30-2025/5739.12-9-30-2025.pdf); [ODT UST-1 instructions](https://tax.ohio.gov/business/sales-and-use-tax/sales-tax-holiday).

For timely filed and fully paid returns: discount = **min(tax due × 0.0075, $750 × licenses × months covered)** for non-motor-vehicle tax. The cap applies to returns **required on/after 1 January 2026**, including December 2025 monthly and July–December 2025 semi-annual returns. Sales/leases of motor vehicles are outside the cap. A certified service provider's monetary allowance disqualifies the vendor from the discount under (B)(2); less-frequent filing also has the CSP exclusion in (C)(2). [R.C. 5739.12(B), (C)](https://codes.ohio.gov/assets/laws/revised-code/authenticated/57/5739/5739.12/9-30-2025/5739.12-9-30-2025.pdf); [ST 2025-02](https://tax.ohio.gov/business/ohio-business-taxes/sales-and-use/information-releases/st2025-02_vendor_timely_filing_discount_dec_2025).

**Accelerated payments:** annual tax **at least $75,000** triggers accelerated monthly payments in the **second ensuing tax year** and succeeding years. Aggregate locations/licenses as required by 5739.12(G). Pay **75% of anticipated current-month tax by its 23rd**, and settle the preceding month's balance by the next 23rd. Two consecutive years below $75,000 release the requirement for the following year; a good-cause excuse may be granted. A short payment may attract up to **5% of the unpaid amount**, but not if the advance was at least **75% of the same month's reported liability in the preceding year**. [R.C. 5739.122(A)-(D)](https://codes.ohio.gov/ohio-revised-code/section-5739.122).

**Late charges:** failure to file or pay as prescribed may attract an additional charge **not exceeding the greater of $50 or 10%** of period tax; this is a discretionary maximum, not an automatic minimum. Assessment penalties may be up to **50%** for failure to collect/remit or collected tax not remitted, and up to **15%** in other assessments, with a **50%** maximum under that section. [R.C. 5739.12(D)](https://codes.ohio.gov/assets/laws/revised-code/authenticated/57/5739/5739.12/9-30-2025/5739.12-9-30-2025.pdf); [5739.133(A)](https://codes.ohio.gov/ohio-revised-code/section-5739.133).

Interest on unpaid sales/use tax follows **5739.132** and the certified annual rate: **7% in 2026**, **8% in 2025**, **7% certified for 2027**. Compute by days in each rate year, not by compounding a rounded monthly rate. Penalty/assessment cases require referral. [R.C. 5739.132](https://codes.ohio.gov/ohio-revised-code/section-5739.132); [ODT interest table and formula](https://tax.ohio.gov/researcher/interest-rates).

## Boundary and exception table

| Product/service | Treatment and limits | Official source |
| --- | --- | --- |
| Goods, electronics, furniture, office equipment, pet food/supplies, ordinary clothing | Presumed taxable unless an exemption applies. Clothing holiday exception below | [R.C. 5739.01(B)(1), (WW)](https://codes.ohio.gov/ohio-revised-code/section-5739.01); [5739.02(C)](https://codes.ohio.gov/ohio-revised-code/section-5739.02) |
| Prewritten software | Taxable whether personal/business use or delivered on media/electronically; reasonable separately stated customer-specific modification is excluded from prewritten software | [R.C. 5739.01(WW), (BBB)](https://codes.ohio.gov/ohio-revised-code/section-5739.01) |
| Hosted CRM, data processing, computer/information services | Taxable when within statutory definitions, for business use, and true object is the computer/information service. Personal/professional work with incidental computing is excluded; do not assume all SaaS or subscriptions are identical. Affiliated-group exception applies to qualifying transactions | [R.C. 5739.01(B)(3)(e), (Y)](https://codes.ohio.gov/ohio-revised-code/section-5739.01) |
| Digital movie/music/book, including less-than-permanent access | Specified digital products are sales; separate cable/video-provider and other statutory exemptions can apply. Provider qualification disputes are held | [R.C. 5739.01(B)(12), (OOO)](https://codes.ohio.gov/ohio-revised-code/section-5739.01); [5739.02(B)(53)-(54)](https://codes.ohio.gov/ohio-revised-code/section-5739.02) |
| Accounting, legal, consulting and other professional/personal services | Inconsequential goods without separate charge do not turn these into taxable sales. Separately sold taxable goods/services remain taxable. Employment/staffing and placement services ceased being taxable as such from October 2021 | [R.C. 5739.01(B), (Y)(2)](https://codes.ohio.gov/ohio-revised-code/section-5739.01); [ODT repeal alert](https://tax.ohio.gov/professional/ohtaxalert/taxalertsarchive/salesuse) |
| Landscaping/lawn care; mechanized snow removal | Each service has its own **less than $5,000 calendar-year sales** exclusion; exactly $5,000 is outside that exclusion. Transition invoices and retrospective liabilities are held below | [R.C. 5739.01(DD), (B)(3)(r)](https://codes.ohio.gov/ohio-revised-code/section-5739.01) |
| Janitorial/building cleaning | Same less-than-$5,000 calendar-year exclusion. Necessary sanitation for the specified federal meat-inspection establishments is excluded. ODT says collection continues once the threshold is reached; do not use that sentence to override the statute's annual wording | [R.C. 5739.01(II)](https://codes.ohio.gov/ohio-revised-code/section-5739.01); [ST 2002-04](https://tax.ohio.gov/business/ohio-business-taxes/sales-and-use/information-releases/st2002-04-updated04.2025) |
| Repair/installation; pest control; fitness/sports-club memberships | Listed taxable services. Repair/installation exemptions depend on the underlying property; installation into a public-utility system has a separate exclusion | [R.C. 5739.01(B)(3)(a)-(b), (k)-(m)](https://codes.ohio.gov/ohio-revised-code/section-5739.01) |
| Personal care | Listed skin care, nails, hair removal, tattoos, piercings, tanning and massage are included; hair cutting/coloring/styling and services by/on order of the listed licensed practitioners are excluded | [R.C. 5739.01(B)(3)(o)](https://codes.ohio.gov/ohio-revised-code/section-5739.01) |
| Car wash; laundry/dry cleaning; storage; towing/security; lodging; in-state passenger transport | Listed services with category-specific definitions and exemptions. Self-service laundry differs from a merely automated car wash. Apply the relevant subsection, not a universal coin-operated exemption; uncertain category cases are held | [R.C. 5739.01(B)(2)-(3), (B)(9), (M)-(N), (BB)](https://codes.ohio.gov/ohio-revised-code/section-5739.01); [5739.02(B)(43)](https://codes.ohio.gov/ohio-revised-code/section-5739.02) |
| Human food off premises | Exempt, including ordinary candy, chewing gum, breath mints and chocolate-covered pretzels; flour is not Ohio's dividing test. Alcohol, dietary supplements, soft drinks and tobacco are excluded from food. Catering follows the food/premises distinction; restaurant food is not universally exempt | [R.C. 5739.02(B)(2)](https://codes.ohio.gov/ohio-revised-code/section-5739.02); [5739.01(CCC)](https://codes.ohio.gov/ohio-revised-code/section-5739.01) |
| Soft drinks | Sweetened nonalcoholic beverages; excludes milk/milk substitutes and drinks over 50% fruit/vegetable juice. Do not infer tax from sweetness alone | [R.C. 5739.01(CCC)(2)(b)](https://codes.ohio.gov/ohio-revised-code/section-5739.01) |
| Human prescription-only drugs; medical equipment | Prescription-only human drugs exempt; ordinary OTC drugs generally taxable absent another exemption. Prescribed human prosthetic/mobility equipment and durable medical equipment for home use have specific conditions | [R.C. 5739.02(B)(18)-(19)](https://codes.ohio.gov/ohio-revised-code/section-5739.02) |
| Feminine hygiene products | Exempt for the statutory products; grooming/hygiene products are not included in that definition | [R.C. 5739.02(B)(48)](https://codes.ohio.gov/ohio-revised-code/section-5739.02); [5739.01(RR)](https://codes.ohio.gov/ohio-revised-code/section-5739.01) |
| Manufacturing/resale | Exemption depends on actual statutory use, not possession of STEC B alone. Qualifying production machinery primarily used to manufacture goods for sale is covered; office/administrative equipment and other exclusions remain taxable | [R.C. 5739.02(B)(42)(g)](https://codes.ohio.gov/ohio-revised-code/section-5739.02); [5739.011(B)-(D)](https://codes.ohio.gov/ohio-revised-code/section-5739.011); [5739.01(E)](https://codes.ohio.gov/ohio-revised-code/section-5739.01) |
| Exempt entities | Ohio/political subdivisions, reciprocal states and qualifying charitable/church buyers have statutory exemptions. Obtain evidence of the actual buyer and qualifying use; a nonprofit label alone is insufficient | [R.C. 5739.02(B)(1), (12)](https://codes.ohio.gov/ohio-revised-code/section-5739.02) |

**2026 holiday:** **7–9 August**, qualifying general-use clothing **$75 or less per item**; listed school supplies and instructional material **$20 or less per item**. Business purchases and excluded categories do not qualify; items above the limit are taxable in full. There was no expanded $500 holiday in 2026. Apply discounts, separate pricing and order/payment timing under the Department's holiday instructions. Do not reuse these limits for 2025. [R.C. 5739.02(B)(55)](https://codes.ohio.gov/ohio-revised-code/section-5739.02); [5739.41](https://codes.ohio.gov/ohio-revised-code/section-5739.41); [ODT 2026 instructions](https://tax.ohio.gov/business/sales-and-use-tax/sales-tax-holiday).

## Worked cases

**1. Canton order, Cleveland delivery (Q4 2026).** Original $800 television, Stark 6.50%, Cuyahoga 8.00%. With the order captured at the Canton store and the statutory origin conditions met: tax **$52**, versus **$64** at delivery, a **$12** difference; the customer who paid the invoiced origin tax owes no further tax under (B)(2). A standalone repair first used in Cleveland follows the service hierarchy; same-invoice goods/service transactions need (B)(4). [R.C. 5739.033(B)-(C)](https://codes.ohio.gov/ohio-revised-code/section-5739.033); [Q4 rates](https://tax.ohio.gov/business/sales-and-use-tax/rate-tables/by-county-q4-2026).

```oa-check
name: Ohio vendor sourcing, order-received rate against delivery rate (Q4 2026)
inputs:
  price: 800
  stark_rate: 0.065
  cuyahoga_rate: 0.08
steps:
  - tax_order_received: price * stark_rate
  - tax_delivery: price * cuyahoga_rate
  - difference: tax_delivery - tax_order_received
expected:
  tax_order_received: 52.00
  tax_delivery: 64.00
  difference: 12.00
```

**2. Consolidated discount (2026).** Original **$400,000 tax, three licenses, one month**, timely, non-motor-vehicle and no disqualifying CSP: uncapped **$3,000**; cap **$2,250**; remittance **$397,750**. [R.C. 5739.12(B)](https://codes.ohio.gov/assets/laws/revised-code/authenticated/57/5739/5739.12/9-30-2025/5739.12-9-30-2025.pdf).

```oa-check
name: Ohio vendor discount cap, three licenses, one month (2026)
inputs:
  tax_due: 400000
  licenses: 3
  months: 1
steps:
  - discount_uncapped: tax_due * 0.0075
  - cap: 750 * licenses * months
  - discount: min(discount_uncapped, cap)
  - remit: tax_due - discount
expected:
  discount_uncapped: 3000.00
  cap: 2250.00
  discount: 2250.00
  remit: 397750.00
```

The following original scenarios retain their amounts and years; apply the stated conditions, not the rejected historic conclusion:

- **Oregon remote seller:** **210 transactions, $60,000 in 2025**, no Ohio presence: the preceding-year transaction test applies in 2026; an ordinary direct **$500** sale received in Cuyahoga at **8%** gives **$40** tax. [R.C. 5741.01(I)](https://codes.ohio.gov/ohio-revised-code/section-5741.01); [Q4 rates](https://tax.ohio.gov/business/sales-and-use-tax/rate-tables/by-county-q4-2026).
- **Hosted CRM:** Cleveland business **$300/month**, true object is qualifying electronic information service, Cuyahoga **8%**: **$24/month**. Hosted household personal-finance service is outside the business-use rule; downloaded prewritten software is different. [R.C. 5739.01(B)(3)(e), (WW)](https://codes.ohio.gov/ohio-revised-code/section-5739.01).
- **Single-license cap:** **$120,000 March 2026 tax, due 23 April 2026**: **$900** uncapped, **$750** allowed, **$119,250** remitted. The original **November 2025**, due **23 December 2025**, comparison allows **$900**, remittance **$119,100**; **December 2025**, due **23 January 2026**, uses the cap. [ST 2025-02](https://tax.ohio.gov/business/ohio-business-taxes/sales-and-use/information-releases/st2025-02_vendor_timely_filing_discount_dec_2025).
- **Semi-annual case:** original one license, **$1,500 January–June 2026 tax**, filed/paid **23 July 2026**: assuming that filing schedule was authorized, discount **$11.25**, cap **$4,500**, remittance **$1,488.75**. The amount itself does not establish eligibility for semi-annual filing. [R.C. 5739.12(B), (C)](https://codes.ohio.gov/assets/laws/revised-code/authenticated/57/5739/5739.12/9-30-2025/5739.12-9-30-2025.pdf).
- **Holiday:** **8 August 2026**, Franklin **8%**, **$70 jacket / $80 shoes**, qualifying personal purchases: jacket exempt, shoes fully taxable, tax **$6.40**. [ODT holiday](https://tax.ohio.gov/business/sales-and-use-tax/sales-tax-holiday).
- **Janitorial start-up:** original offices billed until calendar-year sales reach **$5,000**. The statutory less-than exclusion no longer applies at that amount. Exact transition invoices and the Department's later-year continuation position are **non-usable pending advice**. Check this point with one of our partner accountants. [R.C. 5739.01(II)](https://codes.ohio.gov/ohio-revised-code/section-5739.01).
- **Late payment:** original **$10,000 March 2026 tax**, due **23 April**, paid **30 days late**: no timely discount; **$10,000 × 7% × 30 / 365 = $57.53** interest, before any applicable charge/assessment. [ODT formula](https://tax.ohio.gov/researcher/interest-rates).
- **Earlier Columbus electronics / origin cases:** original **$800**, assumed **7.50%**, produced **$60 tax / $860 total**. That assumed rate is **not usable as a 2026 Franklin rate**. At Q4 2026 **8%**, the same $800 gives **$64 / $864**. The Columbus-to-Cleveland origin case needs order capture and the other sourcing conditions even where both rates now coincide. [Q4 rates](https://tax.ohio.gov/business/sales-and-use-tax/rate-tables/by-county-q4-2026); [5739.033(B)](https://codes.ohio.gov/ohio-revised-code/section-5739.033).
- **Earlier discount test:** **$20,000** timely non-motor-vehicle tax, one license/month, no disqualifying CSP: **$150 discount / $19,850 remittance**, below the cap. [5739.12(B)](https://codes.ohio.gov/assets/laws/revised-code/authenticated/57/5739/5739.12/9-30-2025/5739.12-9-30-2025.pdf).
- **Earlier food tests:** **$150 Cleveland bread/milk/produce**, **$5 Columbus chocolate bar without flour** (old assumed **7.50%**), and **$5 chocolate-covered pretzels with flour**: each gives **$0** when ordinary human food for off-premises consumption. The original **$0.38 candy tax** is rejected; flour does not decide Ohio food exemption. [5739.02(B)(2)](https://codes.ohio.gov/ohio-revised-code/section-5739.02); [5739.01(CCC)](https://codes.ohio.gov/ohio-revised-code/section-5739.01).
- **Earlier threshold-date examples:** original **$100,000 reached on 15 October 2024**, first return **23 November 2024**, does not establish nexus on receipts alone; the Department's actual example was **$80,000 with the 200th sale on 15 October 2024**. Facilitator example: **200th transaction on 15 December 2019**, collection **1 February 2020**, first return **23 March 2020**, under its separate timing rule. [ODT nexus examples](https://tax.ohio.gov/business/sales-and-use-tax).
- **Earlier nexus test:** **$120,000 / 50 transactions in the past year**: confirm “past year” means the current or preceding calendar year; on that condition receipts exceed the threshold. A rolling twelve-month fact alone cannot resolve the test. [5741.01(I)](https://codes.ohio.gov/ohio-revised-code/section-5741.01).
- **Earlier staffing tests:** **$8,000/month**, old Columbus assumption **7.50%**, and **$6,000/month**, old Hamilton assumption **7.55%**. The old **$600 / $453 tax** outcomes are rejected for employment services as such in 2026; tax is **$0** absent a separately taxable supply. [ODT repeal alert](https://tax.ohio.gov/professional/ohtaxalert/taxalertsarchive/salesuse).
- **Earlier manufacturing test:** **$75,000 production-line equipment**, primarily manufacturing for sale, STEC B: **$0** only if the actual equipment/use meets **5739.011**, including exclusions. A certificate alone does not prove it. [5739.011](https://codes.ohio.gov/ohio-revised-code/section-5739.011).
- **Earlier use-tax test:** Cleveland business, **$4,000 office furniture from New Hampshire**, no tax collected, **8%** rate and no exemption/credit: **$320** use tax; follow the business consumer use-tax route. [5741.02](https://codes.ohio.gov/ohio-revised-code/section-5741.02).
- **Earlier edge cases:** **$50 gym membership** is within taxable fitness services; rate depends on sourcing. **$14.99 digital movie** is a specified digital product subject to applicable exemption checks. **$2,000/month landscaping** requires the separate calendar-year threshold test. Cloud analytics needs the true-object/business-use facts. A supposed missed **28 February annual license renewal / $25 annual fee** is rejected; check actual license status. [5739.01(B), (DD), (KK), (OOO)](https://codes.ohio.gov/ohio-revised-code/section-5739.01); [5739.17](https://codes.ohio.gov/ohio-revised-code/section-5739.17).

## When to refuse or refer

These are **non-usable holds**, not alternative tax conclusions:

| Point | Action |
| --- | --- |
| Audits, assessments, appeals, penalty abatement, private rulings and Habitual Offender Program/suspension cases | Check this point with one of our partner accountants. |
| Past non-compliance / voluntary disclosure, including the previous 36-month lookback, 10% collected-tax penalty and 60-day completion claims | Do not apply those figures without an agreement-specific review. Check this point with one of our partner accountants. |
| Leases, titled vehicles/watercraft/outboards, dealer trade-ins, construction contracts/CC-CO liability, resort/lodging levies and 9-1-1 fees | Check this point with one of our partner accountants. |
| Disputed bundles, multi-location allocation, true-object litigation and provider-specific streaming/cable exemptions, internet-access-only and website-creation contracts | Check this point with one of our partner accountants. |
| Janitorial later-year continuation, exactly-at-threshold invoices, retrospective collection and special sanitation facts | Check this point with one of our partner accountants. |
| Interstate delivery with uncertain receipt, temporary-use valuation, special medical/manufacturing equipment or reciprocal/exempt-entity status | Check this point with one of our partner accountants. |
| 2025 holiday claims and unsupported past local rates | Keep the transaction's original year and inputs. Check this point with one of our partner accountants. |

For refund/amended-return questions use the Department's current procedure; do not treat UST-1-X, ST AR or an old limitation-period statement as permission to adjust a different period. Check this point with one of our partner accountants.

Keep a working paper linking sales, exemptions, sourced jurisdictions/rates, tax due, discount eligibility/cap, payments/accelerated credits and separate use-tax purchases to the filed return. Treat bank descriptions as leads only: reconcile ODT payments to liabilities, marketplace settlements to collection reports, and processor payouts to gross receipts/fees; do not classify BWC from narration as sales tax.

US professional-use disclosure (Circular 230 §10.37): general reference for the stated facts and year; establish the facts, apply the cited law and obtain qualified professional review before filing or acting. No approval is asserted here.

## Sources

Read on **2026-11-27**, limited to the operative provisions described. Where Department summaries conflict with statute, the statute controls; unresolved applications are held above.

| Source and material read | URL | Read on |
| --- | --- | --- |
| Sales definitions: B, E, H, Y, DD, II, RR, WW, BBB, CCC, OOO; business-use, services, food, software and price | https://codes.ohio.gov/ohio-revised-code/section-5739.01 | 2026-11-27 |
| Sales levy A; exemptions B(1),(2),(12),(18),(19),(42),(43),(48),(53)-(55); presumption C | https://codes.ohio.gov/ohio-revised-code/section-5739.02 | 2026-11-27 |
| Manufacturing: production equipment, exclusions and primary use B-D | https://codes.ohio.gov/ohio-revised-code/section-5739.011 | 2026-11-27 |
| Certificates B(1)-(6), including exceptions and cure | https://codes.ohio.gov/ohio-revised-code/section-5739.03 | 2026-11-27 |
| Sourcing B-D and special-rule context | https://codes.ohio.gov/ohio-revised-code/section-5739.033 | 2026-11-27 |
| Monthly returns, electronic filing, discount/CSP, late charges, aggregation A-G, authenticated operative text | https://codes.ohio.gov/assets/laws/revised-code/authenticated/57/5739/5739.12/9-30-2025/5739.12-9-30-2025.pdf | 2026-11-27 |
| Accelerated threshold, timing, release, payments and shortfall A-D | https://codes.ohio.gov/ohio-revised-code/section-5739.122 | 2026-11-27 |
| Unpaid-tax interest A, read through official chapter rendering | https://codes.ohio.gov/ohio-revised-code/chapter-5739 | 2026-11-27 |
| Assessment penalty categories A | https://codes.ohio.gov/ohio-revised-code/section-5739.133 | 2026-11-27 |
| Fixed/transient licensing A-D | https://codes.ohio.gov/ohio-revised-code/section-5739.17 | 2026-11-27 |
| Holiday designation and conditional expanded holiday | https://codes.ohio.gov/ohio-revised-code/section-5739.41 | 2026-11-27 |
| Use definitions E, G, I, Q, T; nexus and marketplace rules | https://codes.ohio.gov/ohio-revised-code/section-5741.01 | 2026-11-27 |
| Use liability, exemptions and foreign-tax credit A-C | https://codes.ohio.gov/ohio-revised-code/section-5741.02 | 2026-11-27 |
| Marketplace receipt hierarchy B | https://codes.ohio.gov/ohio-revised-code/section-5741.05 | 2026-11-27 |
| Remote registration and exceptions A-B | https://codes.ohio.gov/ohio-revised-code/section-5741.17 | 2026-11-27 |
| County/transit combined rates, Q4 2026 | https://tax.ohio.gov/business/sales-and-use-tax/rate-tables/by-county-q4-2026 | 2026-11-27 |
| Application fees, registration and Warren change | https://tax.ohio.gov/business/sales-and-use-tax/sales-and-use-tax | 2026-11-27 |
| Nexus, registration systems and marketplace timing/accounts | https://tax.ohio.gov/business/sales-and-use-tax | 2026-11-27 |
| Less-frequent filing eligibility and due dates | https://tax.ohio.gov/business/ohio-business-taxes/sales-and-use/license/ | 2026-11-27 |
| Certificate form uses and limitations | https://tax.ohio.gov/business/sales-and-use-tax/exemption-certificates | 2026-11-27 |
| Statutory janitorial exclusion versus continuation summary | https://tax.ohio.gov/business/ohio-business-taxes/sales-and-use/information-releases/st2002-04-updated04.2025 | 2026-11-27 |
| Discount cap applicability and consolidated examples | https://tax.ohio.gov/business/ohio-business-taxes/sales-and-use/information-releases/st2025-02_vendor_timely_filing_discount_dec_2025 | 2026-11-27 |
| Holiday dates, qualifying categories/limits, business exclusion and UST-1 lines | https://tax.ohio.gov/business/sales-and-use-tax/sales-tax-holiday | 2026-11-27 |
| 2025/2026/2027 rates and daily formula | https://tax.ohio.gov/researcher/interest-rates | 2026-11-27 |
| Business consumer use-tax account route | https://tax.ohio.gov/business/sales-and-use-tax/taxability | 2026-11-27 |
| Employment-service repeal alert entry dated 30 August 2021 | https://tax.ohio.gov/professional/ohtaxalert/taxalertsarchive/salesuse | 2026-11-27 |

Not yet confirmed: only the specifically identified non-usable holds; no held conclusion is authorized for computation or filing. The historical 3%/8.75% ceiling summary is omitted because an actual address/date rate determines the charge, not a theoretical maximum.
