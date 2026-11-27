---
name: bc-pst
description: >
  Prepare a British Columbia Provincial Sales Tax registration and return workpaper
  for 2026. Establish seller and platform duties, local small-seller versus remote
  thresholds, goods/software/services scope, special rates, actual FIN400 boxes,
  self-assessment, commission, adjustments and filing. Preserve the original
  Q2 2025 case as conditional arithmetic with its filing outcome on hold.
version: 2.1
jurisdiction: CA-BC
tax_year: 2026
last_updated: 2026-11-27
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: vat-gst
type: computation
---

# British Columbia provincial sales tax

## Scope

Prepare a 2026 British Columbia PST registration and FIN400 return workpaper. PST is a separate retail sales tax; there is no general PST input-tax-credit system. Prepare federal GST/HST through `canada-gst-hst`, including its own registration, place, export and input-credit tests. A provincial exemption does not determine federal treatment. [BC scope and business assets](https://www2.gov.bc.ca/gov/content/taxes/sales-taxes/pst/publications/small-business-guide).

Use the supported registration, classification, calculation and filing steps below. The exception table preserves the specialist jobs; its **non-usable holds** prohibit a tax or exemption conclusion until the identified determination is resolved. No filing, payment or registration is performed by this Guide. The original Cascadia Cloud Inc. Q2 2025 facts remain in Worked cases; they are not silently moved to 2026.

| Quick reference | Entry | Official source |
|---|---|---|
| Ordinary taxable goods/software/services | 7%, subject to category, base, location and exemption tests below | [Act ss.34,105](https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/12035_03) and [software](https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/12035_04) |
| Administrator, portal and return | BC Ministry of Finance; eTaxBC; PST FIN400. Accommodation MRDT uses separate FIN401 | [Return guide](https://www2.gov.bc.ca/gov/content/taxes/sales-taxes/pst/report-pay/pst-return-guide) |
| Reporting period | The director specifies the account's period; obtain the assignment | [Act s.1, reporting period](https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/12035_01) |
| Currency | CAD; Bank of Canada daily rate for the date PST is paid or payable, whichever comes first | [Return guide](https://www2.gov.bc.ca/gov/content/taxes/sales-taxes/pst/report-pay/pst-return-guide) |

## Ask the client first

Obtain legal/trade name, seller location, business/fulfilment premises and inventory, actual account/registration dates, assigned period and primary/secondary-account status, representative authority and any prior return. Obtain invoice-level supply descriptions, due/payment/delivery dates, tax-exclusive prices, discounts, freight/customs and other charges, customer/device location and use, exemption/resale evidence, and own-use purchases or inventory withdrawals. Do not infer a classification from a vendor brand, B2B label or customer address.

For remote sellers collect solicitation, BC-origin orders, delivery and preceding/estimated-following revenue by statutory population. For platforms establish contractual role, payment collection and actual reporting. Obtain accommodation address, occupancy and charges; vehicle class, price/valuation, seller/import/gift/lease history; and refund, write-off, recovery, tax-remittance and closure records. Reconcile supported rows before requesting an authorised human's approval to transmit and pay.

## The method, step by step

### 1. Establish registration and collector

**Local sellers.** Apply the vendor/lessor requirements in s.169; an only-exempt seller is excepted under the relevant subsection. There is no universal local CAD10,000 registration exemption. A vendor ceasing to be a small seller must register by the last day of its first month as a vendor. [Act s.169](https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/12035_08#section169).

**Small seller: all conditions.** The person must be located in BC; sell eligible goods/software or provide taxable services at a sale in BC; neither maintain established business premises nor regularly make the specified retail sales/provide services from established commercial premises; have eligible retail/service gross revenue at most CAD10,000 in the previous 12 months and a reasonable estimate at most CAD10,000 for the following 12 months. It must not knowingly have made non-retail eligible goods/software sales in the previous 12 months. It must not sell vehicles, aircraft, boats, vapour products, fossil-fuel combustion systems, tobacco, other excluded goods or cannabis in the ordinary course, or liquor other than under a permit or by auction. It cannot be a lessor, independent sales contractor, specified supply-and-affix contractor, accommodation vendor within paragraph (d) of vendor, or facilitator; it must not be registered or required by ss.169–171 to register. Apply the statutory eligible-goods and vendor definitions, not just revenue. A qualifying small seller pays PST on resale purchases and must not levy or collect PST, subject to the liquor-permit exception in s.182(1). [Act s.1 definitions](https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/12035_01), [s.183](https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/12035_08#section183), [BC explanation](https://www2.gov.bc.ca/gov/content/taxes/sales-taxes/pst/publications/small-business-guide).

**Remote routes are separate.** For ordinary-course Canadian sellers outside BC, s.172(1) covers solicitation, BC-origin orders, sales for the specified BC use/consumption and delivery in BC; all those conditions apply and this route has no revenue safe harbour. Section172(1.1) covers BC-origin orders, the specified sale/use and delivery, plus the minimum-revenue test or vapour products. Section172(2.1) separately covers solicitation and BC-origin orders for software used on/through/with a device ordinarily in BC or telecommunications for the specified BC use/benefit. The relevant only-exempt-supplies exceptions apply. [Act s.172](https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/12035_08#section172).

For a seller outside BC, s.172.1(1) separately requires registration for BC-origin goods orders, the specified BC use/consumption and goods held in BC inventory when sold. Section172.1(1.1) covers BC-origin software/telecom orders, supplies in response meeting the minimum revenue, and specified BC device use/benefit; only-exempt supplies are excepted. Lease activity has its own s.169(1.1)–(2) test; do not apply a remote sales threshold to it. [Act ss.169,172.1](https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/12035_08).

| Minimum revenue for routes that expressly use s.172.2 | Population and boundary | Official source |
|---|---|---|
| Located in Canada outside BC | BC gross revenue from all retail goods sales/leases and all software/telecom sales/provisions: **greater than CAD10,000** in preceding 12 months OR reasonable estimate greater than CAD10,000 in the following 12 months | [s.172.2(1)](https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/12035_08#section172.2) |
| Located outside Canada | BC gross revenue from all software/telecom sales/provisions: **greater than CAD10,000**, with the same preceding OR reasonable-estimated-following test | [s.172.2(2)](https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/12035_08#section172.2) |

A facilitator ordinarily operates/owns/controls a marketplace, facilitates sellers' goods/software/non-legal-service transactions and collects payment; the definition also includes prescribed persons. Registration under s.172.3 covers the listed BC goods, software/device, accommodation and other taxable-service transactions, excluding legal services. It is not required if the defined gross value **made or facilitated** is CAD10,000 or less in the preceding 12 months **OR** the reasonable estimate is CAD10,000 or less in the following 12 months. The joint-platform exception requires another joint operator to be registered and collect all required tax; only-exempt facilitated supplies are also excepted. This is not the remote seller's OR trigger. [Act s.1](https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/12035_01), [s.172.3](https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/12035_08#section172.3).

Where s.179.3 applies to a registered/required-to-register facilitator, it is the collector and the seller is not; do not collect twice. The outside-Canada goods exception and possible prescribed circumstances remain. Legal services are outside this facilitator definition. The seller and facilitator have the statutory joint-and-several liability on the listed assessments, penalties and interest; obtain collector evidence rather than promising all seller obligations disappear. Marketplace-service fees to sellers require their separate s.172.4/134.3 test: **non-usable hold** on an unresolved fee/role determination. Check this point with one of our partner accountants. [Act ss.172.4,179.3](https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/12035_08).

Prepare the actual application and required information through eTaxBC or the authority's permitted application route; retain the issued account and restrictions. Registration numbers are not transferable. Do not assume an incorporation, acquisition or closure transfers the account. [Act s.168](https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/12035_08#section168).

### 2. Classify the supply, base and rate

Goods, software, related services, legal services, accommodation, telecommunications and online-marketplace services require their own category/location/exemption determination. Software includes SaaS, infrastructure as a service and APIs; a business address alone does not establish BC device use. Digital music/movies can be telecommunications; the former blanket no-PST streaming outcome is withdrawn. [Act definitions](https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/12035_01), [BC scope](https://www2.gov.bc.ca/gov/content/taxes/sales-taxes/pst/publications/small-business-guide).

| Category in 2026 | Rate and operative boundary | Official source |
|---|---|---|
| Ordinary taxable goods | 7% of statutory purchase price; exemptions and special rates take priority | [Act s.34(1)](https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/12035_03#section34) |
| Taxable software | 7% under the applicable purchase/use provision; establish device use and exemptions | [Act ss.104–107](https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/12035_04) |
| Liquor; vapour products; fossil-fuel combustion systems | Respectively 10%;20%;12% of the statutory purchase price for the applicable category | [Act s.34(2),(11),(12)](https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/12035_03#section34) |
| Taxable accommodation | 8% PST; MRDT and Major Events MRDT are separate determinations/returns | [Act s.122](https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/12035_05#section122) |
| Non-ZEV passenger vehicle within s.34(4) GST-registrant taxable-supply/import/prescribed route | Rate selected by **original purchase price**: 7% below CAD55,000;8% at 55,000–<56,000;9% at 56,000–<57,000;10% at 57,000–<125,000;15% at 125,000–<150,000;20% at 150,000+. Apply rate to the whole statutory purchase price | [s.34(4)–(6)](https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/12035_03#section34) |
| Passenger vehicle in residual/private route | Subject to s.34 exceptions:12% below original purchase price CAD125,000;15% at 125,000–<150,000;20% at 150,000+. Do not assume invoice consideration is the statutory base or original purchase price | [s.34(3)–(3.1)](https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/12035_03#section34) |
| Qualifying ZEV passenger vehicle within s.34(4) route | By original purchase price:7% below CAD75,000;8% at 75,000–<76,000;9% at 76,000–<77,000;10% at 77,000–<125,000;15% at 125,000–<150,000;20% at 150,000+ | [s.34(6.1)](https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/12035_03#section34) |
| Boats/aircraft | Residual purchase route12%; s.34(4) qualifying registrant taxable-supply/import/prescribed route7%, subject to exemptions. No vehicle-style progressive bands | [s.34(3)–(5)](https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/12035_03#section34) |

Vehicle lease tax-rate values, gifts, modifications, private-sale valuation and specific exemptions require their own determination in the exception table; the purchase-rate table is not a complete vehicle workpaper.

From 1October2026, accounting, architectural, engineering, non-residential real-estate and security services are exempt under the respective new Part5 divisions. Do not charge a budget-proposed expansion after ignoring these operative exemptions. Separately classify existing taxable components such as legal services. [B.C.Reg.161/2026, ss.82.1–82.5 and commencement](https://www.bclaws.gov.bc.ca/civix/document/id/bcgaz2/bcgaz2/v69n16_161-2026).

Determine statutory purchase/lease price, freight and other charges, discounts, credits and any valuation adjustment before applying a rate. PST generally applies before GST; GST-inclusive accommodation is not the default base. The standard timing is paid or due, whichever first, with instalment allocation and the property-transfer backstop in s.28(4)–(5); use ss.29–33 for exceptions/due-date rules. [Act price definitions](https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/12035_01), [timing](https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/12035_02), [BC tax base](https://www2.gov.bc.ca/gov/content/taxes/sales-taxes/pst/publications/small-business-guide).

For a supported mixed BC/outside-BC business software purchase under s.107, tax is7% × purchase price × estimated BC usage/estimated total usage, using a method the director considers reasonable. The prescribed estimate period is the shorter of three years from purchase (s.107(1)(b)(i)) or first mixed use ((b)(ii)), and the term of the right if only a right to use was purchased. Section108 requires the later usage determination/adjustment. Exclude s.112 small-seller purchases from s.107. Do not allocate a cloud invoice just by customer address or a guessed consumption percentage. [Act ss.107–108](https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/12035_04), [Reg.96/2013 s.29](https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/1295368594#section29).

Food/soda and electricity exemptions are BC rules: s.139 excludes soda, the specified dispenser beverages and prescribed products; electricity is exempt under s.140.1. Do not import GST grocery definitions or infer an exemption for every food-containing product. Other exemption investigations and mixed bundles are preserved as specific holds below. [Act ss.139–140.1](https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/12035_06).

### 3. Reconcile purchases and prepare actual FIN400

Self-assess supported taxable own-use purchases/leases, imports and inventory withdrawals for which PST was not paid; check location, base, prior tax and exemption first. Report the supported untaxed cost in E and tax in F. A vendor name alone does not establish software/telecom liability. [BC own-use rules](https://www2.gov.bc.ca/gov/content/taxes/sales-taxes/pst/publications/small-business-guide), [return guide](https://www2.gov.bc.ca/gov/content/taxes/sales-taxes/pst/report-pay/pst-return-guide).

| Actual FIN400 box | Transfer from workpaper | Official source |
|---|---|---|
| A | All taxable, non-taxable and exempt sales/leases **in Canada**, excluding taxes and marketplace-facilitator sales reportable by that facilitator | [BoxA](https://www2.gov.bc.ca/gov/content/taxes/sales-taxes/pst/report-pay/pst-return-guide) |
| B | PST collectable on taxable sales/leases, including charged but unpaid tax and tax collected in error; include any applicable ICE/rental tax only after its separate determination | [BoxB](https://www2.gov.bc.ca/gov/content/taxes/sales-taxes/pst/report-pay/pst-return-guide) |
| C;D | Eligible commission; then B−C | [BoxesC–D](https://www2.gov.bc.ca/gov/content/taxes/sales-taxes/pst/report-pay/pst-return-guide) |
| E;F | Untaxed taxable own-use purchase/lease cost; then its actual PST | [BoxesE–F](https://www2.gov.bc.ca/gov/content/taxes/sales-taxes/pst/report-pay/pst-return-guide) |
| G | D+F before adjustments | [BoxG](https://www2.gov.bc.ca/gov/content/taxes/sales-taxes/pst/report-pay/pst-return-guide) |
| H;I | Eligible previously remitted tax on bad-debt write-offs; eligible PST refunded/credited to customers | [BoxesH–I](https://www2.gov.bc.ca/gov/content/taxes/sales-taxes/pst/report-pay/pst-return-guide) |
| J;K | H+I; then G−J as total due. A negative total is an account credit | [BoxesJ–K](https://www2.gov.bc.ca/gov/content/taxes/sales-taxes/pst/report-pay/pst-return-guide) |

Commission requires the return and full PST payment by the due date. Use only the permitted primary account; where one return covers multiple locations, use that return's aggregate collectable PST. The actual FIN400 worksheet uses sales/lease PST in B, not self-assessed purchases or MRDT. [Actual worksheet](https://www2.gov.bc.ca/assets/gov/taxes/sales-taxes/forms/fin-400-provincial-sales-tax-return.pdf). [Return guide, BoxC](https://www2.gov.bc.ca/gov/content/taxes/sales-taxes/pst/report-pay/pst-return-guide), [Act s.185](https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/12035_08#section185).

| Eligible B / remitted sales tax for the period | Commission | Official source |
|---|---|---|
| CAD0–22 | That tax amount | [Reg.96/2013 s.74](https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/1295368594#section74) |
| CAD22.01–333.33 | CAD22 | [s.74](https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/1295368594#section74) |
| More than CAD333.33 | 6.6% of that tax, maximum CAD198; never the former1.32% formula | [s.74](https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/1295368594#section74) |

For bad debts, s.159 requires a qualifying transaction, registration at the transaction date, tax remitted as required, non-payment and a write-off within four years of remitting that tax. Deduct eligible tax in the write-off period. Under Reg.97/2013 s.134 the proportional amount is remitted tax × unpaid amount/total payable; total payable includes all applicable taxes, excludes interest, and unpaid amount excludes interest. Subsequent recoveries restore the attributable tax in B for the recovery period. If the same-period deduction is missed, the separate refund claim has the guide's four-year-from-write-off limit. Never claim twice. [Act s.159](https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/12035_07#section159), [Reg.s.134](https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/97_2013_00_multi#section134), [BoxH](https://www2.gov.bc.ca/gov/content/taxes/sales-taxes/pst/report-pay/pst-return-guide).

Customer refunds/credits in I require previously remitted tax and a legally permitted customer refund/credit. Claim in that period; a missed-period claim follows the separate refund route within four years of refunding/crediting the customer. Do not offset an unpaid disputed invoice without a qualifying adjustment. [Act s.160](https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/12035_07#section160), [BoxI](https://www2.gov.bc.ca/gov/content/taxes/sales-taxes/pst/report-pay/pst-return-guide).

### 4. File, pay and preserve evidence

Use the account's assigned period: the director's period controls. The Ministry's general ongoing-period table below describes options, not an election overriding the assignment. A person required to register who has not applied reports monthly. Liquor sellers have a separate initial/ongoing assignment process; do not use the general bands to select their period. [Act s.1](https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/12035_01), [reporting-period guide](https://www2.gov.bc.ca/gov/content/taxes/sales-taxes/pst/report-pay).

| Annual PST collectable, general ongoing table | Period options | Official source |
|---|---|---|
| More than CAD12,000 | Monthly only | [Ministry table](https://www2.gov.bc.ca/gov/content/taxes/sales-taxes/pst/report-pay) |
| More than CAD6,000 through12,000 | Monthly or quarterly | [Ministry table](https://www2.gov.bc.ca/gov/content/taxes/sales-taxes/pst/report-pay) |
| More than CAD3,000 through6,000 | Quarterly or semi-annual | [Ministry table](https://www2.gov.bc.ca/gov/content/taxes/sales-taxes/pst/report-pay) |
| CAD3,000 or less | Quarterly, semi-annual or annual | [Ministry table](https://www2.gov.bc.ca/gov/content/taxes/sales-taxes/pst/report-pay) |

The old CAD11,940 bands and automatic annual period for negative collections are withdrawn. If the assignment is unknown, hold filing. Check this point with one of our partner accountants.

For a collector with a period of one or more months, both filing and payment ordinarily fall due on the last day of the following month. A non-calendar period uses30 days after its last day. When a due date falls on a weekend or BC statutory holiday, use the first following business day; mail, bank and electronic timeliness have different rules. [Reg.96/2013 ss.72,77,82–83.1](https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/1295368594), [filing instructions](https://www2.gov.bc.ca/gov/content/taxes/sales-taxes/pst/report-pay).

eTaxBC supports filing/payment; an authorised representative needs actual account access. Mandatory electronic filing/remittance applies at CAD1.5million or more of total Canadian property/service sales or leases in the previous12months, and in director-specified circumstances. Keep return acceptance and payment receipts separately; use separate notices for assessment/fee payments. [Reg.ss.73,78](https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/1295368594), [return guide](https://www2.gov.bc.ca/gov/content/taxes/sales-taxes/pst/report-pay/pst-return-guide).

Nil returns remain necessary; for closure use eTaxBC or FIN357 and file/pay through the closure date. Retain actual name/address/business change notifications and check s.174's applicable notification/deemed-cancellation route rather than merely stopping returns. [BC closure](https://www2.gov.bc.ca/gov/content/taxes/sales-taxes/pst/publications/small-business-guide), [Act s.174](https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/12035_08#section174).

Retain sales/purchases, tax, exemption, platform, inventory, commission, refund/write-off/recovery and filing/payment records. Reg.s.93 requires five years **from record creation**, subject to authorised earlier destruction; records needed for an appeal must remain until appeals are exhausted. Preserve evidence of an ongoing exemption while it is needed. [Reg.ss.88–93](https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/1295368594).

Accommodation in an MRDT area needs separate PST and FIN401 MRDT returns; a single payment may cover both. Any Vancouver Major Events MRDT must follow its separate electronic reporting instructions. Rate/designation/occupancy and federal host/platform determinations remain the specific holds below. [Return guide](https://www2.gov.bc.ca/gov/content/taxes/sales-taxes/pst/report-pay/pst-return-guide), [BC MRDT instructions](https://www2.gov.bc.ca/gov/content/taxes/sales-taxes/pst/publications/small-business-guide).

Before finalising timing, test the s.33 earliest invoice issue/date, undue-delay and written-payment dates, including its written lease/licence exception. Deposits are not consideration until applied (with the reusable-container rule); conduit supplies, unascertainable price and statutory/written construction holdbacks have s.28(6)–(10) conditions. An unresolved special timing outcome is a **non-usable hold**. Check this point with one of our partner accountants. [Act ss.28,33](https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/12035_02).

## Boundary and exception table

Each row is a **non-usable hold on the named outcome**, not an exemption or permission to charge tax. Complete other supported BC work; separate Saskatchewan, Manitoba, Quebec and other-province returns.

| Preserved investigation | Missing determination and action |
|---|---|
| Medical/prescription products | Actual eligible product, use and documents. Check this point with one of our partner accountants. |
| Children's clothing/footwear | Actual garment/size/child eligibility and evidence; no invented price limit. Check this point with one of our partner accountants. |
| School supplies; books/publications | Qualifying items/use and documentary conditions; an ISBN or student alone does not settle it. Check this point with one of our partner accountants. |
| Private used goods; resale; production machinery; BC exports | Separate transaction, resale intent, qualifying industry/use, goods shipment/software-use outside BC and exemption evidence; registration alone does not exempt operating equipment. Check this point with one of our partner accountants. |
| First Nations/reserve; Crown/public bodies | Qualifying purchaser, statutory immunity, location/delivery and evidence. Check this point with one of our partner accountants. |
| Contractors/affixed machinery | Contract, supply-and-affix, title/use and any liability agreement; no blanket end-user or retail result. Check this point with one of our partner accountants. |
| Residential/new/used/commercial property; goodwill; business assets | Allocate land/buildings, equipment/inventory/software and goodwill; determine PST, federal GST/elections and property-transfer tax separately. Check this point with one of our partner accountants. |
| Bulk business transfer | Obtain the s.187 certificate analysis before acquisition; preserve seller tax/account evidence. No s.230 universal-successor shortcut. Check this point with one of our partner accountants. |
| Accommodation occupancy/exemptions | Original27-day long-stay and low-revenue/price investigations need the full eligible-occupant/unit/listing test; no blanket residential exemption or platform CAD2,500 trigger. Check this point with one of our partner accountants. |
| Vancouver/Victoria/Whistler/Tofino/Kelowna MRDT; Major Events MRDT; private destination fee | Actual transaction-date designation/rate, mandatory charges/base and collector. The previous Vancouver3% MRDT plus2.5% Major Events claim for February2023–January2030 and other-city3%/2% list are held, not certified; do not substitute a private2.5% fee. Check this point with one of our partner accountants. |
| Vehicle/boat/aircraft exceptions | Lease/gift/import/modification, class, valuation, ZEV definition and exemptions before using purchase rates. Check this point with one of our partner accountants. |
| Liquor/cannabis/vapour/energy sectors | Determine other levies, ICE/rental amounts and product/residential-energy exemptions separately from supported PST rates. Insurance/financial supplies need their actual tax statute. Check this point with one of our partner accountants. |
| Mixed bundles; disputed cloud/software/telecom use | Actual components, optionality, value, allocation and exemption; do not tax everything from a single invoice or default to charging/self-assessing. Check this point with one of our partner accountants. |
| Bankruptcy/receivership; audit, disclosure, appeals; penalties/interest | Actual authority, notices, periods, applicable rate/deadline and relief conditions. No universal10% penalty or unspecified current-interest figure. Check this point with one of our partner accountants. |
| Federal GST/HST; other provinces | Preserve federal export/ITC/host-platform work and each province's return; no automatic5% export tax,13% Ontario outcome or host GST collection from PST platform status. Check this point with one of our partner accountants. |

## Worked cases

### Case 1: original Q2 2025 Cascadia Cloud Inc. — filing outcome held

Cascadia Cloud Inc. is a Vancouver BC corporation. Preserve **Q2 2025** and every original input: BC SaaS CAD240,000; Ontario SaaS360,000; US SaaS500,000; hardware delivered to Burnaby12,000 without a resale certificate; Vancouver-owned condo via registered Airbnb18,000; US AWS cloud invoice40,000, with the original asserted BC allocation30,000 and no BC PST charged.

**Non-usable historical filing hold.** The current sources do not prove every Q2 2025 rule, the assigned quarter, the particular SaaS/AWS classification or usage period, exemption, platform/accommodation or federal outcome. These inputs do not establish those legal assumptions. Check this point with one of our partner accountants.

The following block only recomputes the preserved amounts **conditionally**: assume fully taxable BC SaaS/hardware, no BC use of Ontario/US SaaS, supported30,000 taxable software purchase base, accommodation correctly reported by the facilitator, Canadian sales as stated, timely eligible primary-account commission, and no adjustments. It illustrates the current FIN400 field model, not an accepted Q2 2025 return. The same arithmetic may be used for an actual2026 period only after independently establishing that period and those facts; the original year is unchanged. [Act software/base](https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/12035_04), [current FIN400 guide](https://www2.gov.bc.ca/gov/content/taxes/sales-taxes/pst/report-pay/pst-return-guide), [commission](https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/1295368594#section74).

```oa-check
name: Cascadia original Q2 2025 inputs conditional arithmetic only
inputs:
  bc_saas: 240000
  ontario_saas: 360000
  us_saas: 500000
  burnaby_hardware: 12000
  platform_accommodation: 18000
  cloud_invoice: 40000
  assumed_supported_bc_base: 30000
steps:
  - box_a: bc_saas + ontario_saas + burnaby_hardware
  - bc_saas_pst: bc_saas * 0.07
  - hardware_pst: burnaby_hardware * 0.07
  - box_b: bc_saas_pst + hardware_pst
  - box_c: min(198, round(box_b * 0.066, 2))
  - box_d: box_b - box_c
  - box_e: assumed_supported_bc_base
  - box_f: box_e * 0.07
  - box_g: box_d + box_f
  - box_j: 0
  - box_k: box_g - box_j
expected:
  box_a: 612000
  bc_saas_pst: 16800
  hardware_pst: 840
  box_b: 17640
  box_c: 198
  box_d: 17442
  box_e: 30000
  box_f: 2100
  box_g: 19542
  box_j: 0
  box_k: 19542
```

The US500,000 and platform18,000 are excluded from this conditional Canadian non-platform A population. No federal GST/HST, MRDT or Major Events amount is certified. The original BC-only A252,000 and invented B–G meanings are withdrawn; the final19,542 coincidence did not validate the old1.32% commission formula.

### Case 2: original middle-interval commission

Retain CAD200 collectable sales PST and70 supported self-assessed purchase PST, no adjustments, with timely full filing/payment by an eligible primary account. C is22, not2.64 or198; K is248. Purchase tax does not enlarge the commission base. [Reg.s.74](https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/1295368594#section74), [BoxesB–K](https://www2.gov.bc.ca/gov/content/taxes/sales-taxes/pst/report-pay/pst-return-guide).

```oa-check
name: BC original middle commission interval
inputs:
  collectable_sales_tax: 200
  self_assessed_purchase_tax: 70
steps:
  - box_c: 22
  - box_k: collectable_sales_tax - box_c + self_assessed_purchase_tax
expected:
  box_c: 22
  box_k: 248
```

## When to refuse or refer

Do not finalise an unsupported period, collector, supply/place/base, exemption, special-rate or adjustment outcome. Carry the exact unresolved facts with the applicable hold above; complete supported rows. Prepared applications, returns, journal entries or payments are not authority acceptance. Never restore a withdrawn historical claim as a fallback.

## Completion checklist

Confirm registration route and revenue population; category/base/use and source date; full Canadian A and collectable B reconciliation; supported E/F; commission eligibility; H/I and recoveries; separate accommodation/federal/other-province work; assigned period and filing/payment evidence; nil/closure/change notifications; and record retention. Every exception remains blocked until its determination is supported.

## Sources

| Official source and precise scope read | URL | Read on |
|---|---|---|
| Act Part1: seller/facilitator/software/period definitions and purchase-price/bundle provisions; no certification of every specialist valuation | https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/12035_01 | 2026-11-27 |
| Act Part2: ss.28–29,33 paid/due timing, instalments, transfer backstop, unpaid tax and invoice/due-date conditions; specialist ss.30–32 outcomes held | https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/12035_02 | 2026-11-27 |
| Act Part3: s.34 purchase-rate selection, qualifying transactions and original purchase price; lease/gift outcomes held | https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/12035_03 | 2026-11-27 |
| Act Part4: ss.104–108 software liability, BC device use, mixed usage and subsequent adjustment | https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/12035_04 | 2026-11-27 |
| Act Part5: taxable-services categories and s.122 accommodation rate; specialist outcomes remain held | https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/12035_05 | 2026-11-27 |
| Act Part6: ss.137–140.1 bundle/food/electricity boundaries; other exemptions not certified | https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/12035_06 | 2026-11-27 |
| Act Part7: ss.159–160 bad-debt qualification/write-off/recovery and customer-refund deductions | https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/12035_07 | 2026-11-27 |
| Act Part8: ss.168–175 registration; ss.179.3,183,185–187 collector, allowance and bulk-certificate provisions | https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/12035_08 | 2026-11-27 |
| Reg.96/2013: s.29 usage period; ss.72–83.1 timing, commission, electronic duties, receipts; ss.88–93 records. Consolidation says29September2026; checked Reg.114/2026 Schedule2 and161/2026: these retained provisions unchanged | https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/1295368594 | 2026-11-27 |
| Reg.97/2013: ss.78,82.1–82.5,134 occupancy/exemption boundaries and bad-debt formula; specialist occupancy outcomes held | https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/97_2013_00_multi | 2026-11-27 |
| Reg.114/2026: Schedule2 amendments to Reg.96/2013; read against subsequent repeal of its section4 | https://www.bclaws.gov.bc.ca/civix/document/id/bcgaz2/bcgaz2/v69n13_114-2026 | 2026-11-27 |
| Reg.161/2026: whole operative schedule and commencement; professional-service exemptions effective1October2026 | https://www.bclaws.gov.bc.ca/civix/document/id/bcgaz2/bcgaz2/v69n16_161-2026 | 2026-11-27 |
| Ministry small-business guide: PST categories/base, separation from GST, own-use purchases, closure, MRDT returns and records; specialist details are not certified | https://www2.gov.bc.ca/gov/content/taxes/sales-taxes/pst/publications/small-business-guide | 2026-11-27 |
| Actual FIN400: complete text of both pages including worksheet, B-based piecewise commission, remittance fields and certification; revision2017/6/8 is not a new2026 edition | https://www2.gov.bc.ca/assets/gov/taxes/sales-taxes/forms/fin-400-provincial-sales-tax-return.pdf | 2026-11-27 |
| Ministry report/pay page: general ongoing reporting bands, mandatory monthly non-registrant rule, liquor exception, assigned period, weekend/holiday extension | https://www2.gov.bc.ca/gov/content/taxes/sales-taxes/pst/report-pay | 2026-11-27 |
| Ministry return guide: FIN400 A–K, Canada/platform population, currency, adjustments, commission eligibility, due dates, filing/payment and closure | https://www2.gov.bc.ca/gov/content/taxes/sales-taxes/pst/report-pay/pst-return-guide | 2026-11-27 |

Not yet confirmed: the non-usable exception outcomes listed above, original Q2 2025 case law/account facts, filing without the account assignment, and specialised current classifications. Each is expressly referred; none supplies a usable rate, exemption, filing or payment conclusion. No new approval is added or inferred.
