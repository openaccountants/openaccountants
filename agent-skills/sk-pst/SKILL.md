---
name: sk-pst
description: "Prepare a Saskatchewan provincial sales tax workpaper for 2026: actual vendor, consumer and platform registration, limited home small-trader guidance, goods/services and own-use scope, corrected clothing treatment, tax-exclusive bases, assigned reporting, electronic versus non-electronic deadlines, exemptions, adjustments and sector-specific referrals. Keep liquor consumption, insurance premiums and federal GST/HST as separate legal jobs."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/sk-pst"
  jurisdiction: "CA-SK"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# Saskatchewan provincial sales tax v2.0

## Scope

Prepare the provincial retail-sales-tax workpaper for goods/services consumed or used in Saskatchewan under The Provincial Sales Tax Act, R.S.S.1978,c.P-34.1, as amended. Saskatchewan has its own tax and return; it is not an HST province. Ordinary PST has no general input-tax-credit mechanism. Actual resale/production exemptions, statutory refunds and corrections are distinct from federal GST/HST input credits. [Act ss.3-5,8](https://publications.saskatchewan.ca/api/v1/products/779/formats/1196/download).

`canada-gst-hst` owns the separate federal supply/place, registration, tax, zero-rating and input-credit workpaper. Other provincial owners include `bc-pst`, `mb-rst` and `qc-qst-return`; do not send a Quebec question to a nonexistent shorthand slug. Supported Saskatchewan work can continue while a specialised other-province or legal issue is referred. [CRA taxable/zero-rated distinction](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4022/general-information-gst-hst-registrants.html).

| Quick reference | Entry |
|---|---|
| Currency/administrator | CAD; Saskatchewan Ministry of Finance, Revenue Division |
| Account | Actual vendor's licence or registered consumer number, with representative authority and filing assignment |
| Portal | Saskatchewan Electronic Tax Service, SETS; paper/mail options exist under actual current instructions |
| Core return workpaper | Sales/collectable tax, supported exemption/location evidence, own-use purchases, prior tax/refund/write-off/recovery and account reconciliation |
| Preserved original example | Prairie Threads Inc., Regina, all original customer groups and amounts retained |

## Ask the client first

1. Obtain legal/entity/trade name, licence/consumer account, actual start/registration/closure, current assigned period and any variation, premises/other provinces and authorised representative. An account/payment and a filed return are different evidence.
2. Obtain dated invoices and actual goods/services, consideration, discounts, charges, GST/PST-inclusive presentation, customer/delivery and consumption/use facts. Get transaction dates for historic-rule changes rather than assuming current law applies to old periods.
3. For remote/platform sales, obtain seller/platform role, payment collection, actual platform licence/remittance evidence, orders/solicitation/delivery/consumption and direct-channel sales. No local office does not itself establish an exemption.
4. For a claimed small trader, obtain individual/home status, actual annual sales, production/service/delivery location, non-commercial customer and competition/advertising facts and tax paid on inputs. Do not apply it to a non-resident vendor or online marketplace merely because sales are small.
5. Reconcile taxable/exempt/outside-province sales, collectable tax, own-use imports/inventory withdrawals, supporting resale/exemption evidence, bad-debt/write-off/recovery/refund records and tax already remitted.
6. Obtain the actual professional-service Saskatchewan relationship, software/cloud/access/users and mixed-jurisdiction allocation, insurance category, contractor/property/security/clearance, private vehicle/value, Indigenous recipient/reserve/delivery, farm/manufacturing and other commodity-tax facts before finalising a specialist claim.

## The method, step by step

### Rates, bands and thresholds

| Item | Supported rate, amount and conditions | Official source |
|---|---|---|
| General taxable goods/services | 6% of actual taxable value, with statutory scope/exceptions | [Act s.5](https://publications.saskatchewan.ca/api/v1/products/779/formats/1196/download), [current government](https://www.saskatchewan.ca/business/taxes-licensing-and-reporting/provincial-taxes-policies-and-bulletins) |
| Ordinary taxable passenger vehicle | General 6% framework, subject to actual private/used, fair-value, trade-in and specific valuation/exemption rules; not a blanket exemption for used goods | [Act s.5 and vehicle provisions](https://publications.saskatchewan.ca/api/v1/products/779/formats/1196/download) |
| Taxable insurance contracts | 6% under the separate PST insurance provisions, category/exemptions and actual fee base; distinct from tax paid by an insurer under another statute | [Act s.5.9](https://publications.saskatchewan.ca/api/v1/products/779/formats/1196/download), [PST-73](https://sets.saskatchewan.ca/rptp/wcm/connect/b9fd728b-b4fc-4a9e-a59e-c542fb87d6f1/PST.073%2BInsurance%2BContracts.pdf?CACHEID=ROOTWORKSPACE-b9fd728b-b4fc-4a9e-a59e-c542fb87d6f1-oVY6hcZ&MOD=AJPERES) |
| Beer/wine/spirits | Separate 10% Liquor Consumption Tax where applicable; not a special PST rate replacing every other tax | [Act s.8(1)(d)](https://publications.saskatchewan.ca/api/v1/products/779/formats/1196/download), [government tax catalogue](https://www.saskatchewan.ca/business/taxes-licensing-and-reporting/provincial-taxes-policies-and-bulletins) |
| Registration | No general revenue safe harbour for nonresident vendors, but actual marketplace-only and limited home small-trader rules can change obligations | [Act ss.3.1,4](https://publications.saskatchewan.ca/api/v1/products/779/formats/1196/download), [PST-5](https://sets.saskatchewan.ca/rptp/wcm/connect/559aa7c9-984d-405a-8ddf-c91848dd8dd7/PST.005%2BRegistration%2Band%2BReporting%2BRequirements.pdf?CACHE=NONE&CONTENTCACHE=NONE&MOD=AJPERES&attachment=true) |
| Small-trader administrative guideline | Annual sales **less than** CAD 10,000 plus the actual home/non-commercial/tax-paid and other restrictions; not a universal small-supplier threshold | [PST-5 sectionC](https://sets.saskatchewan.ca/rptp/wcm/connect/559aa7c9-984d-405a-8ddf-c91848dd8dd7/PST.005%2BRegistration%2Band%2BReporting%2BRequirements.pdf?CACHE=NONE&CONTENTCACHE=NONE&MOD=AJPERES&attachment=true) |
| Filing frequency guide | Annual tax 0throughCAD 4,800: annual;4,800through 12,000: quarterly;over 12,000: monthly. Government summary overlaps at exactly 4,800; follow actual account assignment and hold any unresolved boundary rather than choose it | [Current government table](https://www.saskatchewan.ca/business/taxes-licensing-and-reporting/provincial-taxes-policies-and-bulletins/provincial-sales-tax/file-your-pst-return) |
| Electronic return and payment | Last day of the month following period end where **both** filing and payment are electronic | [Government filing instruction](https://www.saskatchewan.ca/business/taxes-licensing-and-reporting/provincial-taxes-policies-and-bulletins/provincial-sales-tax/file-your-pst-return), [PST-5](https://sets.saskatchewan.ca/rptp/wcm/connect/559aa7c9-984d-405a-8ddf-c91848dd8dd7/PST.005%2BRegistration%2Band%2BReporting%2BRequirements.pdf?CACHE=NONE&CONTENTCACHE=NONE&MOD=AJPERES&attachment=true) |
| Non-electronic filing or payment | Twentieth of the month following period end; using only one electronic leg does not give the later deadline | [Government filing instruction](https://www.saskatchewan.ca/business/taxes-licensing-and-reporting/provincial-taxes-policies-and-bulletins/provincial-sales-tax/file-your-pst-return), [PST-5](https://sets.saskatchewan.ca/rptp/wcm/connect/559aa7c9-984d-405a-8ddf-c91848dd8dd7/PST.005%2BRegistration%2Band%2BReporting%2BRequirements.pdf?CACHE=NONE&CONTENTCACHE=NONE&MOD=AJPERES&attachment=true) |

### Establish the actual vendor, consumer, remote or platform route

1. Apply the statutory vendor/licence and taxable retail-sale requirements before accepting a collection position. The definition reaches the actual Saskatchewan consumption/relationship and remote supplier, not just an office address. A person purchasing untaxed goods/services for own use can have a consumer/self-assessment obligation even without retail output sales. [Act ss.3-5,14](https://publications.saskatchewan.ca/api/v1/products/779/formats/1196/download), [PST-5 vendor/consumer instructions](https://sets.saskatchewan.ca/rptp/wcm/connect/559aa7c9-984d-405a-8ddf-c91848dd8dd7/PST.005%2BRegistration%2Band%2BReporting%2BRequirements.pdf?CACHE=NONE&CONTENTCACHE=NONE&MOD=AJPERES&attachment=true).
2. General remote taxable-sales obligations do not have a universal dollar safe harbour, but “every sale by anyone must register” is also too broad. Examine actual retail/non-business facts and the statutory marketplace-only exception and limited administrative small-trader guideline. A single private sale can still have buyer tax or a special vehicle registration collection route. [Act ss.4-5](https://publications.saskatchewan.ca/api/v1/products/779/formats/1196/download), [PST-5](https://sets.saskatchewan.ca/rptp/wcm/connect/559aa7c9-984d-405a-8ddf-c91848dd8dd7/PST.005%2BRegistration%2Band%2BReporting%2BRequirements.pdf?CACHE=NONE&CONTENTCACHE=NONE&MOD=AJPERES&attachment=true).
3. Under the limited home small-trader guidance, an individual producing and selling small-scale/non-commercial goods from the residence has specific annual sales, location and tax-paid input conditions. The guidance extends specified home services to non-commercial customers. It excludes outside-home/marketplace/commercial-customer/competitive-advertising cases and nonresident vendors. Treat it as a bounded administrative guideline, not an automatic exemption for any company below the amount. Preserve the actual evidence and ruling if facts are near the boundary. [PST-5 sectionC](https://sets.saskatchewan.ca/rptp/wcm/connect/559aa7c9-984d-405a-8ddf-c91848dd8dd7/PST.005%2BRegistration%2Band%2BReporting%2BRequirements.pdf?CACHE=NONE&CONTENTCACHE=NONE&MOD=AJPERES&attachment=true).
4. A marketplace facilitator or online accommodation platform can be a deemed vendor where the actual statutory facilitation/payment conditions apply, whether or not it operates physically in the province. A seller retailing exclusively through the appropriately licensed platform has the stated licence exception; own direct sales and its own untaxed consumption remain separate. Obtain actual licence/collection/remittance evidence, not just a marketplace brand. [Act ss.3.1,4(2.1)](https://publications.saskatchewan.ca/api/v1/products/779/formats/1196/download), [PST-5 platform instructions](https://sets.saskatchewan.ca/rptp/wcm/connect/559aa7c9-984d-405a-8ddf-c91848dd8dd7/PST.005%2BRegistration%2Band%2BReporting%2BRequirements.pdf?CACHE=NONE&CONTENTCACHE=NONE&MOD=AJPERES&attachment=true).
5. Prepare the actual SETS/registration application or permitted paper route with real business identity, activities, location and dates. A vendor licence and registered consumer account are not interchangeable. The actual bulletin says businesses are **not required** to state their vendor licence number on all sales invoices; that old universal invoice requirement was false. Preserve any licence display/inspection and valid resale evidence duties separately. [Act s.4](https://publications.saskatchewan.ca/api/v1/products/779/formats/1196/download), [PST-5 actual licence/invoice instructions](https://sets.saskatchewan.ca/rptp/wcm/connect/559aa7c9-984d-405a-8ddf-c91848dd8dd7/PST.005%2BRegistration%2Band%2BReporting%2BRequirements.pdf?CACHE=NONE&CONTENTCACHE=NONE&MOD=AJPERES&attachment=true).
6. Notify actual business/entity/location/ownership/closure changes and complete outstanding periods through valid cancellation. A licence is not automatically transferred with a corporation/asset sale. Obtain the specific current account determination rather than treating a changed trading name as new or closed without evidence. [PST-5 account duties](https://sets.saskatchewan.ca/rptp/wcm/connect/559aa7c9-984d-405a-8ddf-c91848dd8dd7/PST.005%2BRegistration%2Band%2BReporting%2BRequirements.pdf?CACHE=NONE&CONTENTCACHE=NONE&MOD=AJPERES&attachment=true).

### Classify the supply, Saskatchewan relationship and taxable base

7. Start from the actual statutory tangible-property, service and insurance categories. The Act's service list includes accounting, advertising, architectural, engineering, legal, commercial cleaning, employment placement and real-property services in addition to other defined services. Telecommunication/computer/software/accommodation, repair/install, lawn/garden, veterinary, laundry, credit-reporting/collection, admissions and insurance each need their actual source, definition and current exceptions. This guide retains all original category investigations but does not certify every industry transaction from a list alone. [Act s.3 definitions and s.5](https://publications.saskatchewan.ca/api/v1/products/779/formats/1196/download), [official bulletin catalogue](https://sets.saskatchewan.ca/rptp/portal/footer/taxinformation/provincial-sales-tax/).
8. For accounting, obtain the actual service and Saskatchewan relationship. PST-62 includes financial statements/bookkeeping/payroll/tax documents/audit and directly related consulting, but also has exempt service/disbursement and mixed-jurisdiction rules. Do not tax every accountant's charge simply by job title, or treat every out-of-province client as exempt without checking its actual local connection. [PST-62 bounded scope and relationship](https://sets.saskatchewan.ca/rptp/wcm/connect/b764c11e-b557-4dfa-a25b-9e59797533d0/PST.062%2BAccounting.pdf?MOD=AJPERES).
9. Software/cloud, downloaded versus accessed product, services, subscriptions, telecom and digital platform fees require actual customer/use/device/service facts and current definitions. Do not import Manitoba's2026 start date or BC's software test into Saskatchewan. Where current product-specific classification was not established, keep the question and amount explicit instead of defaulting all services to taxable.
10. Compute the actual value including statutory taxable delivery/service/processing and other consideration, less supported discounts and exclusions. GST is excluded under the stated parallel-tax rules; GST-inclusive displayed prices require removing the federal component before the correct PST calculation. Do not calculate PST on a post-GST total or apply a rounded conversion factor where an exact supported base is available. [Act consideration/value provisions](https://publications.saskatchewan.ca/api/v1/products/779/formats/1196/download), [PST-5 invoice/base instructions](https://sets.saskatchewan.ca/rptp/wcm/connect/559aa7c9-984d-405a-8ddf-c91848dd8dd7/PST.005%2BRegistration%2Band%2BReporting%2BRequirements.pdf?CACHE=NONE&CONTENTCACHE=NONE&MOD=AJPERES&attachment=true).
11. Collect and account for tax at the applicable transaction time; reconcile credit sales, bundled charges, price adjustments, related-party/noncash values and any actual approved special method. Unknown documentation does not justify a highest-tax guess. An invoice tax charged in error requires proper correction/remittance handling, not unilateral retention of the customer's money. [Act collection/refund provisions](https://publications.saskatchewan.ca/api/v1/products/779/formats/1196/download), [PST-5](https://sets.saskatchewan.ca/rptp/wcm/connect/559aa7c9-984d-405a-8ddf-c91848dd8dd7/PST.005%2BRegistration%2Band%2BReporting%2BRequirements.pdf?CACHE=NONE&CONTENTCACHE=NONE&MOD=AJPERES&attachment=true).
12. Retain the original out-of-province delivery and goods-use investigation. A customer's mailing address or IP log alone is not the complete legal supply/location determination. Obtain actual shipment/common-carrier/use evidence and allocate multi-jurisdiction services on an appropriate documented basis. Do not require all federal and provincial sales lines to agree when their scope legitimately differs. [Act s.8(1)(jj) and scope](https://publications.saskatchewan.ca/api/v1/products/779/formats/1196/download), [accounting mixed-jurisdiction instructions](https://sets.saskatchewan.ca/rptp/wcm/connect/b764c11e-b557-4dfa-a25b-9e59797533d0/PST.062%2BAccounting.pdf?MOD=AJPERES).

### Exemptions, clothing, own-use and industry boundaries

13. Apply actual statutory exemptions rather than federal assumptions or an old province comparison. Preserve the original groceries, prescription/medical, farm/fertilizer/seed/feed, books/reading material, residential rent/property, manufacturing/direct agents/raw materials, resale and export work. Each needs its actual product/use/recipient and certificate/document conditions; a federal zero-rated item, ISBN, business account or verbal intended use is not automatically sufficient. [Act s.8](https://publications.saskatchewan.ca/api/v1/products/779/formats/1196/download), [official subject catalogue](https://sets.saskatchewan.ca/rptp/portal/footer/taxinformation/provincial-sales-tax/).
14. **Children's clothing:** the old blanket Saskatchewan exemption is wrong. Current Act general retail tax and its exemption list do not supply the old exemption, and the official current-hosted tax notice explicitly taxes adult **and children's** clothing. Historical 2011 material described an earlier exemption and is not a current rule. Preserve child/product classification and any genuine specialised medical/other exemption, but do not exempt an ordinary garment just by the purchaser's age. [Act ss.5,8](https://publications.saskatchewan.ca/api/v1/products/779/formats/1196/download), [official current-hosted notice](https://sets.saskatchewan.ca/rptp/wcm/connect/008a66cd-3674-42f3-824c-e7525bfa0f32/IN%2B2017-09%2BTradeshows.pdf?MOD=AJPERES&attachment=true&id=1701375168654).
15. **Private used goods:** do not claim all non-business used goods are exempt. The actual vendor guidance describes a limited deduction for eligible used personal goods and exclusions for vehicles/commercial use; actual valuation/trade-in/registration rules need the current vehicle or used-goods workpaper. A tax-paid input history does not automatically mean no tax on its next retail sale. [Act s.5](https://publications.saskatchewan.ca/api/v1/products/779/formats/1196/download), [PST-5 used goods instructions](https://sets.saskatchewan.ca/rptp/wcm/connect/559aa7c9-984d-405a-8ddf-c91848dd8dd7/PST.005%2BRegistration%2Band%2BReporting%2BRequirements.pdf?CACHE=NONE&CONTENTCACHE=NONE&MOD=AJPERES&attachment=true).
16. **Manufacturing, farm and packaging:** a qualifying resale/raw-material/direct-agent exemption does not exempt every business input. Obtain actual transformation/use, customer transfer, disposable versus returnable packaging, separately sold versus retained item, certificate and supplier tax. The old rule that all packaging is a final cost unless separately resold is too broad. Keep a potentially mischarged tax as an exemption/refund investigation, not a general input credit. [Act s.8(1)(kk),(2)-(3)](https://publications.saskatchewan.ca/api/v1/products/779/formats/1196/download), [official manufacturing/used-goods catalogue](https://sets.saskatchewan.ca/rptp/portal/footer/taxinformation/provincial-sales-tax/).
17. **Own-use imports:** where the supplier did not collect applicable PST, self-assess the supported taxable value for actual local use, including actual laid-down/foreign-currency charges where required. Examine inventory withdrawals, promotions, business assets, untaxed repairs/services and prior tax. A purchase for a taxable business does not automatically create resale relief; tax properly paid is not a GST-style credit. [Act s.5(5),(9)-(11)](https://publications.saskatchewan.ca/api/v1/products/779/formats/1196/download), [PST-5 own-use/consumer rules](https://sets.saskatchewan.ca/rptp/wcm/connect/559aa7c9-984d-405a-8ddf-c91848dd8dd7/PST.005%2BRegistration%2Band%2BReporting%2BRequirements.pdf?CACHE=NONE&CONTENTCACHE=NONE&MOD=AJPERES&attachment=true).
18. **Real property/contractors:** a sale of land and services relating to its construction/alteration/repair are separate questions. Saskatchewan's statute expressly taxes defined real-property services and has specific supply/install, builder, security and clearance requirements; do not apply the BC ordinary contractor-input treatment blindly. Obtain contract date, total charges, materials, PE/site and actual clearance/security facts for the specialist. [Act ss.3(1)(k),5(6)-(6.3),29-29.01](https://publications.saskatchewan.ca/api/v1/products/779/formats/1196/download).
19. **Indigenous/reserve:** obtain the actual qualifying recipient, location/service connection, delivery and documentation, applying the particular exemption/ruling. Neither status alone nor any reserve-address billing is an automatic result. Keep the old referral with the actual legal gap and records. [Official First Nations subject route](https://sets.saskatchewan.ca/rptp/portal/footer/taxinformation/provincial-sales-tax/).
20. **Commodity/insurance:** beer/wine/spirits are exempt from PST where the separate Liquor Consumption Tax applies; that remains a separate 10%tax and return, not renamed PST. Tobacco/fuel/cannabis/vapour and their other taxes need actual category-specific interaction, not a blanket replacement assertion. PST on taxable insurance contracts differs from the insurer's Insurance Premiums Tax; policy/category/exemption and fees require the actual law/bulletin. [Act ss.5.9,8(1)(d)](https://publications.saskatchewan.ca/api/v1/products/779/formats/1196/download), [government tax catalogue](https://www.saskatchewan.ca/business/taxes-licensing-and-reporting/provincial-taxes-policies-and-bulletins), [PST-73](https://sets.saskatchewan.ca/rptp/wcm/connect/b9fd728b-b4fc-4a9e-a59e-c542fb87d6f1/PST.073%2BInsurance%2BContracts.pdf?CACHEID=ROOTWORKSPACE-b9fd728b-b4fc-4a9e-a59e-c542fb87d6f1-oVY6hcZ&MOD=AJPERES).
21. **Mixed bundles:** identify the taxable/exempt components and actual value and rule; a single price does not make every possible supply taxable by an invented default. The current grocery/gift-package guidance uses the taxable portion's actual value and distinguishes disposable packaging from a valuable decorative container. Refer the actual unresolved bundle, not a universal all-or-nothing rule. [Official bundle guidance](https://sets.saskatchewan.ca/rptp/wcm/connect/94a41317-34b9-46bf-9758-c27b18ee4b31/PST.002%20Grocery%2C%20Convenience%20and%20Drug%20Stores.pdf?MOD=AJPERES).

### Filing, adjustments, payments and records

22. Obtain the actual assigned period and tax population. The current public table replaces the old approximate 1,200/7,200bands with 4,800/12,000bands, but its summary overlaps at exactly 4,800. Use the actual account assignment and obtain the controlling regulation/variation for a disputed exact boundary; don't choose one by guess. [Current filing table](https://www.saskatchewan.ca/business/taxes-licensing-and-reporting/provincial-taxes-policies-and-bulletins/provincial-sales-tax/file-your-pst-return).
23. Registered nil periods still need a nil return. Both return and payment must be electronic to use the government's later month-end deadline. A paper return with online banking, or an electronic return with non-electronic payment, falls under the stated earlier twentieth rule. Paper filing is still listed, so a blanket all-SETS-only requirement is wrong. Obtain applicable weekend/holiday/receipt and operational bank timing for the actual due date, not an unexplained default. [Current filing methods and dates](https://www.saskatchewan.ca/business/taxes-licensing-and-reporting/provincial-taxes-policies-and-bulletins/provincial-sales-tax/file-your-pst-return), [PST-5](https://sets.saskatchewan.ca/rptp/wcm/connect/559aa7c9-984d-405a-8ddf-c91848dd8dd7/PST.005%2BRegistration%2Band%2BReporting%2BRequirements.pdf?CACHE=NONE&CONTENTCACHE=NONE&MOD=AJPERES&attachment=true).
24. Reconcile actual Saskatchewan gross sales, taxable/exempt/place rows and tax collectable, purchases for own use, supported previous remittance, refunds/credit and bad-debt/recovery work. The bulletin says actual return BoxA is total Saskatchewan taxable **and exempt** sales. Use the actual account form/portal fields and adjustment instructions; don't invent a universal net-remittance field or commission. [PST-5 return instructions](https://sets.saskatchewan.ca/rptp/wcm/connect/559aa7c9-984d-405a-8ddf-c91848dd8dd7/PST.005%2BRegistration%2Band%2BReporting%2BRequirements.pdf?CACHE=NONE&CONTENTCACHE=NONE&MOD=AJPERES&attachment=true).
25. The old description promised a vendor commission without a source or usable current formula. No such entitlement is established by the current sources read here. Do not deduct a guessed amount; keep any claimant-specific asserted commission for a controlling-law determination. This is not a claim that all historic collection schemes have been researched or repealed.
26. For tax paid in error, establish the actual purchaser/amount, source, invoice and overpayment time. The statutory refund rules and current official catalogue describe a four-year claim window and refund scope. Preserve bad-debt/write-off evidence, prior remittance, actual proportion and later recovery, checking the applicable legal method and period before claiming. A GST input credit or a tax-paid business input is not sufficient. [Act s.8.11](https://publications.saskatchewan.ca/api/v1/products/779/formats/1196/download), [current official refund guidance](https://sets.saskatchewan.ca/rptp/portal/footer/taxinformation/provincial-sales-tax/), [accounting bad-debt subject](https://sets.saskatchewan.ca/rptp/wcm/connect/b764c11e-b557-4dfa-a25b-9e59797533d0/PST.062%2BAccounting.pdf?MOD=AJPERES).
27. Preserve tax/interest/penalty, licence, director and enforcement investigations but obtain the actual failure type, notice and current legal rate. A blanket late fine or promised relief is not established here. The Act's collection/enforcement cross-reference to The Revenue and Financial Services Act is not a substitute for reading an actual disputed penalty. Refer audit, voluntary disclosure and ruling work with authority, facts and deadlines. [Act ss.8.1,43.2](https://publications.saskatchewan.ca/api/v1/products/779/formats/1196/download).
28. Keep sufficient invoices, prices/taxes, own-use purchases, licence/exemption/registry checks, delivery/use/allocation, platform evidence, refund/debt/recovery and actual filing/payment records. A record-age or account closure does not authorise deleting evidence needed for an unresolved claim/audit. Obtain the exact statutory retention and any direction for the case; no unverified number is inserted here.
29. Complete the return only after reconciling tax and account balances. Obtain authorised sign-off, accepted return acknowledgement and actual payment/credit receipt; bank payment alone does not prove the return was filed. Keep the separate federal return and other provincial statements. This method prepares work for a human; it does not register, submit or pay.

## Boundary and exception table

| Original refusal/default | Correct response |
|---|---|
| R-SK-1 other provincial tax | Use `bc-pst`, `mb-rst` or `qc-qst-return` for that jurisdiction, not a nonexistent Quebec shorthand |
| R-SK-2 federal tax | Use `canada-gst-hst`, retain separate classification, place and input-credit mechanics |
| R-SK-3 commodity taxes | Keep liquor/tobacco/fuel/cannabis/vapour actual separate-statute interaction and rates |
| R-SK-4 property/construction | Obtain actual statutory service, materials, date, security/clearance and specialist work |
| R-SK-5 Indigenous/reserve | Obtain recipient, actual land/delivery/service connection and controlling exemption, not status alone |
| R-SK-6 insurance premiums tax | Distinguish insurer tax from PST on a taxable contract and its actual exemption/base |
| R-SK-7 audit/disclosure/ruling | Preserve the authorised legal/administrative referral with records and deadlines |
| R-SK-8 historic years | Use actual period's law; no universal current 2017-plus shortcut or retroactive new rule |
| Unknown registration | Apply actual vendor/consumer/platform and bounded small-trader tests; no speculative signup |
| Unknown service/location | Research actual category/use and isolate unresolved rows; no default overcharge |
| Untaxed input | Assess supported liability only; no invented input credit or tax-on-every-uncertain-purchase default |
| Rate/period | Current official amount and actual assignment; don't claim a fresh portal read that was not performed |
| Exempt sale | Obtain actual required evidence and law; do not preserve a retired child-clothing exemption |
| Marketplace | Verify role/licence/payment/collection evidence; direct/own-use jobs remain separate |

## Worked cases

### Case 1: ordinary parallel-tax sale

For a supported ordinary taxable CAD 100sale with federal standard 5% and provincial 6% both applicable to the stated tax-exclusive base, federal tax 5and PST 6give total 111. This is a stated classification, not a rule that all Saskatchewan supplies bear both taxes. If the selling price already includes GST/PST, back out the appropriate components instead of compounding them. [PST-5 parallel-tax instruction](https://sets.saskatchewan.ca/rptp/wcm/connect/559aa7c9-984d-405a-8ddf-c91848dd8dd7/PST.005%2BRegistration%2Band%2BReporting%2BRequirements.pdf?CACHE=NONE&CONTENTCACHE=NONE&MOD=AJPERES&attachment=true), [CRA](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4022/general-information-gst-hst-registrants.html).

```oa-check
name: Saskatchewan supported ordinary parallel taxes
inputs:
  tax_exclusive_price: 100
steps:
  - pst: tax_exclusive_price * 0.06
  - federal_gst_given_standard_scope: tax_exclusive_price * 0.05
  - total: tax_exclusive_price + pst + federal_gst_given_standard_scope
expected:
  pst: 6
  federal_gst_given_standard_scope: 5
  total: 111
```

### Case 2: preserve Prairie Threads Inc., correct children's clothing

The original Regina business **Prairie Threads Inc.** has the same original Q2 2025records: children's clothing 40,000of which 5,000Saskatchewan/35,000elsewhere; adult clothing 60,000of which 10,000Saskatchewan/50,000elsewhere; inventory-app SaaS 20,000of which 3,000Saskatchewan/17,000elsewhere; untaxed Alberta office supplies 2,000; Saskatchewan packaging 4,000with 240tax charged. The original child's exemption was already unsupported for that stated period; preserve the actual historical return and correct its law rather than default it to an old 2011exemption. [Actual current-hosted tax notice includes child clothing](https://sets.saskatchewan.ca/rptp/wcm/connect/008a66cd-3674-42f3-824c-e7525bfa0f32/IN%2B2017-09%2BTradeshows.pdf?MOD=AJPERES&attachment=true&id=1701375168654), [Act general rate/exemption list](https://publications.saskatchewan.ca/api/v1/products/779/formats/1196/download).

For a **calendar 2026 workpaper using those figures**, explicitly assume ordinary taxable clothing, a supported taxable Saskatchewan software/service component, actual outside-Saskatchewan delivery/use on the other rows, taxable untaxed office supplies, no supported other adjustment and one actual assigned period. Saskatchewan taxable output base is 18,000, not 13,000: PST on child clothing 300, adult 600, software 180, total 1,080; own-use tax 120; total liability 1,200before any actual separately supported adjustment. No source-supported commission is assumed. [Act](https://publications.saskatchewan.ca/api/v1/products/779/formats/1196/download), [PST-5 base/own-use instructions](https://sets.saskatchewan.ca/rptp/wcm/connect/559aa7c9-984d-405a-8ddf-c91848dd8dd7/PST.005%2BRegistration%2Band%2BReporting%2BRequirements.pdf?CACHE=NONE&CONTENTCACHE=NONE&MOD=AJPERES&attachment=true).

```oa-check
name: Saskatchewan 2026 Prairie Threads corrected taxable clothing
inputs:
  sk_children_clothing: 5000
  sk_adult_clothing: 10000
  supported_sk_taxable_software: 3000
  untaxed_taxable_office_supplies: 2000
steps:
  - taxable_sales: sk_children_clothing + sk_adult_clothing + supported_sk_taxable_software
  - children_tax: sk_children_clothing * 0.06
  - adult_tax: sk_adult_clothing * 0.06
  - software_tax: supported_sk_taxable_software * 0.06
  - collectable: children_tax + adult_tax + software_tax
  - own_use: untaxed_taxable_office_supplies * 0.06
  - liability_before_supported_adjustments: collectable + own_use
expected:
  taxable_sales: 18000
  children_tax: 300
  adult_tax: 600
  software_tax: 180
  collectable: 1080
  own_use: 120
  liability_before_supported_adjustments: 1200
```

Keep the original packaging expense and 240tax-paid facts. Determine actual packaging transfer/use and exemption before treating it as final cost or seeking a specific correction; there is no general 240PST input credit. Likewise, ordinary children's clothing is **not federally zero-rated solely because it is for a child**. CRA describes clothing as taxable and some provinces' specific provincial HST rebates separately; any temporary historic relief needs its actual dates. Prepare the federal workpaper on those facts rather than omitting the child's whole national sales stream. [CRA taxable and point-of-sale rebate distinction](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4022/general-information-gst-hst-registrants.html).

## When to refuse or refer

Do not finalise an unsupported material registration, supply/base/place, exemption, platform or adjustment result. Preserve and continue supported rows, naming the actual missing law/evidence. Refer the original eight specialist/historic issues as above. Don't charge, self-assess, register or promise a credit merely because a broad conservative default sounded safer.

## Completion checklist

- Actual vendor/consumer/platform and bounded home-small-trader route, not an unconditional first-dollar or revenue slogan.
- Actual transaction date, Saskatchewan connection and current service/product/base determined.
- Clothing, private used goods, resale/production/packaging and other exemption jobs correctly tested.
- Own-use tax, marketplace collector, bad debt/refund/recovery and account records reconciled.
- Separate liquor/insurance/commodity/property/Indigenous and federal workpapers retained.
- Actual period and both electronic legs considered; exact ambiguous filing-band boundary held rather than guessed.
- No fictional commission or general PST input credit.
- Human authority, accepted return and actual payment/statement kept separate.

## Sources

| Source actually read and scope | Official URL | Read on |
|---|---|---|
| Read for statutory definitions/service list, vendor/platform/licence, general rate/own-use, property, insurance, exemption list, collection/refund and security/clearance provisions; not every regulation or enforcement rule | https://publications.saskatchewan.ca/api/v1/products/779/formats/1196/download | 2026-11-14 |
| Read for current reporting table, actual electronic/non-electronic dates, nil requirement and paper/electronic methods; exact 4,800 summary overlap retained as gap | https://www.saskatchewan.ca/business/taxes-licensing-and-reporting/provincial-taxes-policies-and-bulletins/provincial-sales-tax/file-your-pst-return | 2026-11-14 |
| Read for actual PST-5 vendor/consumer, nonresident, platform and small-trader conditions, invoices, own-use and return/deadline instructions; direct download failed, official web text was read | https://sets.saskatchewan.ca/rptp/wcm/connect/559aa7c9-984d-405a-8ddf-c91848dd8dd7/PST.005%2BRegistration%2Band%2BReporting%2BRequirements.pdf?CACHE=NONE&CONTENTCACHE=NONE&MOD=AJPERES&attachment=true | 2026-11-14 |
| Read for current government programme/bulletin catalogue and general refund/application conditions, not every linked industry bulletin | https://sets.saskatchewan.ca/rptp/portal/footer/taxinformation/provincial-sales-tax/ | 2026-11-14 |
| Read for bounded accounting services, relationship/partial allocation and preserved exemption/disbursement/debt subject routes | https://sets.saskatchewan.ca/rptp/wcm/connect/b764c11e-b557-4dfa-a25b-9e59797533d0/PST.062%2BAccounting.pdf?MOD=AJPERES | 2026-11-14 |
| Read for official current-hosted notice's explicit ordinary adult/child clothing tax statement and separate liquor/period distinctions; not a new 2026amending Act | https://sets.saskatchewan.ca/rptp/wcm/connect/008a66cd-3674-42f3-824c-e7525bfa0f32/IN%2B2017-09%2BTradeshows.pdf?MOD=AJPERES&attachment=true&id=1701375168654 | 2026-11-14 |
| Read for bounded PST-73 taxable insurance premium/fee base and unlicensed supplier's own-use payment route; not a complete policy exemption audit | https://sets.saskatchewan.ca/rptp/wcm/connect/b9fd728b-b4fc-4a9e-a59e-c542fb87d6f1/PST.073%2BInsurance%2BContracts.pdf?CACHEID=ROOTWORKSPACE-b9fd728b-b4fc-4a9e-a59e-c542fb87d6f1-oVY6hcZ&MOD=AJPERES | 2026-11-14 |
| Read for current general PST and separate liquor/insurance/commodity tax catalogue; rates not copied across regimes | https://www.saskatchewan.ca/business/taxes-licensing-and-reporting/provincial-taxes-policies-and-bulletins | 2026-11-14 |
| Read for taxable versus zero-rated clothing/exports, federal input credits and specific provincial point-of-sale rebate distinction | https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4022/general-information-gst-hst-registrants.html | 2026-11-14 |
| Read for actual gift-package taxable portion/decorative versus disposable-container discussion and liquor separation | https://sets.saskatchewan.ca/rptp/wcm/connect/94a41317-34b9-46bf-9758-c27b18ee4b31/PST.002%20Grocery%2C%20Convenience%20and%20Drug%20Stores.pdf?MOD=AJPERES | 2026-11-14 |

Not yet confirmed: controlling filing regulation/assignment at exactly CAD 4,800 annual tax, which overlaps in the current government summary; any claimant-specific current commission entitlement, all specialised software/cloud, vehicle/value, contractor/property, Indigenous, insurance, medical/farm/manufacturing/direct-agent/packaging and mixed-bundle determinations; exact current record-retention direction, failure-specific penalty/interest and holiday/receipt rules. The old approximate 1,200/7,200 filing bands, universal 20th electronic deadline, compulsory invoice licence number, blanket child-clothing/private-used exemption, speculative commission, federal zero-rating of all child clothing and automatic all-services tax defaults are corrected. The official consolidation read lists amendments through 2025; no claim is made that every subsequently proposed industry rule was reviewed. No accountant approval is added or inferred.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `sk-pst` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/sk-pst. If neither is available, confirm every figure against the official source pages cited above before relying on it.
