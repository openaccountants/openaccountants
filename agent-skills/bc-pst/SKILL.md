---
name: bc-pst
description: "Prepare a British Columbia Provincial Sales Tax registration and return workpaper for 2026. Establish seller and platform duties, local small-seller versus remote thresholds, goods/software/services scope, special rates, actual FIN400 boxes, self-assessment, commission, adjustments and filing. Keep separate MRDT, federal GST/HST, sector-specific and disputed exemption workpapers."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/bc-pst"
  jurisdiction: "CA-BC"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# British Columbia provincial sales tax v2.0

## Scope

Use for the separate British Columbia retail sales tax under the Provincial Sales Tax Act, S.B.C.2012,c.35, as amended. PST is not a value-added tax and has no general input-tax-credit mechanism. Federal GST/HST registration, place of supply, exemptions, zero-rating and input tax credits require their own `canada-gst-hst` workpaper. Being registered for one tax does not automatically settle the other, and a PST-exempt transaction is not thereby GST-exempt. [BC general scope](https://www2.gov.bc.ca/gov/content/taxes/sales-taxes/pst/publications/small-business-guide), [CRA taxable/zero-rated distinction](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4022/general-information-gst-hst-registrants.html).

The ordinary method covers supported taxable retail sales/leases, software/services, purchases for own use, actual FIN400 preparation and reconciliation. Accommodation has separate PST and MRDT returns; vehicles, real-property/affixed machinery, industry, insolvency and Indigenous issues retain their specific investigations below. A second province's registration is not a reason to abandon the supported BC work, but the other province needs its own return and source rules.

| Quick reference | Entry |
|---|---|
| Currency | CAD; convert at the supported official exchange-date basis, not an arbitrary period average |
| Administrator | British Columbia Ministry of Finance |
| Return | Provincial Sales Tax Return, FIN400; MRDT is FIN401, not another FIN400 box |
| Account/access | Actual PST registration number and eTaxBC authority; no sign-in or filing is performed by this method |
| Registration | eTaxBC or actual permitted registration application; don't invent an account or registration based on an untested threshold |
| Original example | Cascadia Cloud Inc., Vancouver, preserved with corrected tax/form assumptions |

## Ask the client first

1. Obtain legal/trade name, seller location, actual PST account, registration dates, business/fulfilment premises, current assigned filing period, other locations/primary account and representative authority.
2. Obtain invoice-level goods/software/service type, transaction/due/payment date, price, separate taxes, discounts, shipping/customs and other charges, customer use/device/location and delivery evidence. Obtain exempt/resale and special-use documents, not just a B2B label.
3. For remote sellers, obtain Canadian versus foreign location, solicitation/orders/delivery/inventory facts, preceding and reasonably estimated following revenue using the correct statutory population. For platforms, obtain the legal role, payment collection, seller transactions and actual collection/remittance evidence; a trade name does not prove the role.
4. Reconcile taxable, exempt, outside-BC and Canadian sales; PST charged or levied but uncollected; tax collected in error; purchases and inventory withdrawals for own use; tax already paid; self-assessment; platform exclusions and adjustments.
5. Obtain accommodation address/dates, actual accommodation and MRDT/Major Events MRDT eligibility/rate, platform/host collection evidence and charges. Obtain vehicle class, purchase history, GST-registrant versus private transaction, import/gift/lease facts and original price/tax-rate value for special cases.
6. Obtain customer refunds/credits, bad-debt write-offs and subsequent recoveries, previously remitted tax, prior claims, assessments, closure/asset-sale and clearance documents. What return and settlement may an authorised human approve? Keep transmission and payment acknowledgements separate.

## The method, step by step

### Rates, bands and thresholds

| Item | Rate, amount and conditions under current law | Official source |
|---|---|---|
| Ordinary goods/software/taxable services | 7% on the statutory taxable base; not every service is taxable | [BC scope/rates](https://www2.gov.bc.ca/gov/content/taxes/sales-taxes/pst/publications/small-business-guide), [Act s.34](https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/12035_03) |
| Liquor | 10%; its own category and base, not an imported Saskatchewan liquor-tax rule | [Act s.34(2)](https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/12035_03), [BC](https://www2.gov.bc.ca/gov/content/taxes/sales-taxes/pst/publications/small-business-guide) |
| Vapour products | 20% PST; distinguish any other applicable duties | [Act s.34(11)](https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/12035_03), [BC](https://www2.gov.bc.ca/gov/content/taxes/sales-taxes/pst/publications/small-business-guide) |
| Fossil-fuel combustion systems | 12%, subject to actual defined scope/exemptions | [Act s.34(12)](https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/12035_03) |
| Short-term taxable accommodation | 8% PST, with separate applicable MRDT and any Major Events MRDT | [BC accommodation explanation](https://www2.gov.bc.ca/gov/content/taxes/sales-taxes/pst/publications/small-business-guide) |
| Ordinary non-ZEV passenger vehicle, qualifying GST-registrant/import transaction | 7% below CAD 55,000; 8% from 55,000 below 56,000; 9% from 56,000 below 57,000; 10% from 57,000 below 125,000; 15% from 125,000 below 150,000; 20% at 150,000 or more. Whole applicable price at the selected rate, not progressive slices | [Act s.34(4)-(6)](https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/12035_03) |
| Ordinary private passenger vehicle transaction | 12% below CAD 125,000; 15% from 125,000 below 150,000; 20% at 150,000 or more, subject to statutory exceptions and valuation. Not an across-the-board 7% private-sale rule | [Act s.34(3)-(3.1)](https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/12035_03) |
| Qualifying ZEV different thresholds | GST-registrant/import case uses 7/8/9/10% boundaries CAD 75,000/76,000/77,000, then 15/20% at 125,000/150,000; verify actual definition/transaction, not a universal vehicle exemption | [Act s.34(6.1)](https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/12035_03) |
| Boats/aircraft | Statutory ordinary distinction 7% versus 12%, depending on actual transaction/import/gift facts; not invented vehicle-like 7/8/10/12% bands | [Act s.34(3)-(5)](https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/12035_03) |
| Remote minimum revenue | More than CAD 10,000 preceding or reasonably estimated following 12months, **only for the statutory routes to which s.172.2 applies**; actual revenue population differs for Canada/foreign sellers | [Act ss.172-172.2](https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/12035_08) |
| Local small seller | At most CAD 10,000 previous and estimated next 12months plus all other small-seller conditions; no universal small-business exemption | [BC eligibility](https://www2.gov.bc.ca/gov/content/taxes/sales-taxes/pst/publications/small-business-guide), [registration bulletin](https://www2.gov.bc.ca/assets/gov/taxes/sales-taxes/publications/pst-001-registering-to-collect-pst.pdf) |
| Actual FIN400 commission | BoxB at most CAD 22: that amount; over 22 through 333.33:22; over 333.33:6.6% of BoxB capped CAD 198, only if timely filing/full payment and the permitted primary-account claim | [Actual FIN400](https://www2.gov.bc.ca/assets/gov/taxes/sales-taxes/forms/fin-400-provincial-sales-tax-return.pdf), [return guide](https://www2.gov.bc.ca/gov/content/taxes/sales-taxes/pst/report-pay/pst-return-guide) |

### Establish the registration and collection route

1. Apply the actual local vendor/lessor/software/service rules and exemptions. A qualifying local small seller has premises, revenue, activity and other conditions; it pays tax on its resale purchases and must not charge PST as a collector under that route. A shop does not get a universal revenue exemption. An exemption from registration is different from whether a purchaser owes PST. [Act ss.169,175,183](https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/12035_08), [BC small-seller explanation](https://www2.gov.bc.ca/gov/content/taxes/sales-taxes/pst/publications/small-business-guide).
2. For a Canadian seller outside BC, distinguish the solicitation/orders/delivery route, the separately thresholded orders route, and software/telecom routes. The solicitation route is not conditioned on the old universal revenue safe harbour. Goods held in BC inventory and leasing create their own statutory routes. For foreign sellers, don't apply the Canadian goods revenue population mechanically to software/telecom or invent the same goods-nexus test for every foreign transaction. [Act ss.172-172.2](https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/12035_08), [actual registration scenarios](https://www2.gov.bc.ca/assets/gov/taxes/sales-taxes/publications/pst-001-registering-to-collect-pst.pdf).
3. Under s.172.2 the minimum-revenue population for a Canadian remote seller includes the stated goods/leases/software/telecom receipts, while the foreign seller's stated population is software/telecom. Apply the real statutory conditions and strictly-greater boundary; do not round an exact threshold into a trigger. Other routes, including vapour, inventory, leases and specific services, can still require registration. [Act s.172.2 and adjacent routes](https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/12035_08).
4. For an online marketplace facilitator, test the statutory definition, facilitating role, payment collection and s.172.3 exemptions, including the actual preceding/following-period wording and jointly operated platform exception. The old “CAD 10,000+ on any platform” is not the full law, and the old accommodation-platform CAD 2,500 shortcut is not the current general framework. Obtain actual transaction/role evidence; don't classify a business by a platform brand. [Act ss.172.3,179.3](https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/12035_08).
5. Where the statutory facilitator rule applies, the facilitator is the collector and the seller does not collect again, subject to actual exceptions, including legal services and specified outside-Canada property. Preserve seller information and possible statutory shared liability; do not promise a platform always removes every host/seller obligation. A seller's own channels remain separately tested. [Act s.179.3](https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/12035_08), [actual return platform instructions](https://www2.gov.bc.ca/gov/content/taxes/sales-taxes/pst/report-pay/pst-return-guide).
6. Prepare the real registration application, legal/entity/contact/industry/expected sales and collection start facts. Retain the approved number and assigned period. Registration numbers are not transferable; an incorporation, asset deal or closure needs an actual account determination. Do not submit an application speculatively. [Act ss.168,174](https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/12035_08), [registration bulletin](https://www2.gov.bc.ca/assets/gov/taxes/sales-taxes/publications/pst-001-registering-to-collect-pst.pdf).

### Classify the supply, base, place and exemption

7. Identify the actual statutory category: tangible goods, software, related services, legal, accommodation, online marketplace or telecommunications. The goods base includes more than a short list of consumer products. Software/device use and telecommunications/digital-media classification need the actual access, delivery, use and location facts; a generic cloud/vendor label is not enough. **Streaming/digital media can be taxable telecommunications**; the old blanket “Netflix only GST, no PST” was wrong. [BC category definitions and examples](https://www2.gov.bc.ca/gov/content/taxes/sales-taxes/pst/publications/small-business-guide), [registration software/telecom examples](https://www2.gov.bc.ca/assets/gov/taxes/sales-taxes/publications/pst-001-registering-to-collect-pst.pdf).
8. For 2026 professional services, distinguish the enacted tax provisions from exemptions effective on the transaction date. The separately read **B.C.Reg.161/2026** exempts the specified accounting, architectural, engineering, non-residential real-estate and security services from the newly identified divisions effective 1October 2026. Do not present an earlier budget proposal or commencement provision as a current tax without that exemption. Existing taxable legal or other components still need their own test. [Actual amending regulation, sections 82.1-82.5](https://www.bclaws.gov.bc.ca/civix/document/id/bcgaz2/bcgaz2/v69n16_161-2026).
9. Establish the statutory purchase/lease/base and timing, generally paid or due earlier under the actual rules. With limited exceptions PST is calculated before GST, not on a supposed GST-inclusive accommodation base. Reconcile delivered/laid-down cost and each taxable charge, discount, credit, barter or related-party value; a tax rate does not establish the base. A business address alone does not prove that every software licence is used in BC. [BC charging, location and purchase guidance](https://www2.gov.bc.ca/gov/content/taxes/sales-taxes/pst/publications/small-business-guide), [FIN400 currency/base instructions](https://www2.gov.bc.ca/gov/content/taxes/sales-taxes/pst/report-pay/pst-return-guide).
10. Apply special product/transaction rates before computing. Vehicle rate selection depends on its legal class, original price or lease tax-rate value, acquisition history, modified/ZEV and private-versus-registrant/import facts. A high price selects a rate on the applicable whole base, not a marginal surcharge on the excess. Boats/aircraft have their own transaction rules. Get a specialist for disputed valuation or industry cases; no invented private-sale equalisation. [Act ss.34-36](https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/12035_03).
11. Preserve every original exemption investigation: food/soda, prescriptions/medical, children's clothing/footwear, school items, books, residential energy/electricity, private used goods, manufacturing/production machinery, resale, First Nations/reserve, Crown/public body, exports and residential accommodation. Test **BC's** actual definition, use and documents; federal zero-rating, an ISBN, a child's presence, customer status, government logo or any B2B invoice is not automatically the exemption. Some goods are exempt without certificates, others require defined records. [BC exemption categories and documentation distinctions](https://www2.gov.bc.ca/gov/content/taxes/sales-taxes/pst/publications/small-business-guide).
12. Contractor supply-and-affix, improvements and affixed machinery are not all the same asset/property question. The ordinary contractor pays tax on materials/inputs, but specific agreements, retail supplies, leases and affixed machinery rules can differ. A sale of land is not a licence to treat every accompanying asset as exempt. Obtain contract, installation, title/use and actual PE/property facts before the specialist determination. [BC contractor/affixed-machinery explanations](https://www2.gov.bc.ca/gov/content/taxes/sales-taxes/pst/publications/small-business-guide), [registration contractor cases](https://www2.gov.bc.ca/assets/gov/taxes/sales-taxes/publications/pst-001-registering-to-collect-pst.pdf).
13. For mixed bundles, identify the actual goods/software/services, independent optionality, prices and applicable statutory exemption/apportionment rule. The old blanket “single invoice taxes everything” and “always tax the ambiguous component” do not establish law. Retain the actual bundle workpaper; unresolved material scope is explicitly held rather than charging an invented tax.

### Purchases, GST/HST and accommodation are separate workpapers

14. Reconcile taxable business/personal-use purchases, imports, inventory withdrawals, promotional items and leases on which the supplier did not collect PST. Assess the actual location, tax-paid/exempt status and base; self-assess supported liability in FIN400 purchases. Do not assume every cloud invoice is software/telecom merely because the old example named AWS. There is no general PST input credit; a specific exemption, refund or tax-paid adjustment requires its own basis. [BC purchases/imports/inventory](https://www2.gov.bc.ca/gov/content/taxes/sales-taxes/pst/publications/small-business-guide), [return BoxesE-F](https://www2.gov.bc.ca/gov/content/taxes/sales-taxes/pst/report-pay/pst-return-guide).
15. Prepare GST/HST separately through `canada-gst-hst`; reconcile timing/place/base differences rather than forcing provincial and federal sales lines to agree. A zero-rated export has a zero federal output rate when its actual requirements are met, not “5% on US-zero-rated sales.” Federal tax on children's clothing or another provincial-exempt item must be separately classified. A nonresident customer's address alone is not export eligibility. [CRA ordinary, zero-rated and input-credit rules](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4022/general-information-gst-hst-registrants.html).
16. For accommodation, establish the actual property, continuous occupancy, exemptions, bundled/extra charges and collector. Apply the correct accommodation/MRDT and any Major Events MRDT legal period/rate, and separately the federal supply/collector rules. A registered PST marketplace facilitator's role does not prove that it also collects the host's GST. [BC accommodation/platform guidance](https://www2.gov.bc.ca/gov/content/taxes/sales-taxes/pst/publications/small-business-guide), [actual separate-return instructions](https://www2.gov.bc.ca/gov/content/taxes/sales-taxes/pst/report-pay/pst-return-guide).
17. MRDT is reported on **FIN401**, not FIN400. Vancouver's government-described Major Events MRDT is 2.5% in addition to its 3% MRDT and 8% PST for the stated February 2023-January 2030 period; it is not a merely voluntary industry destination fee. Other municipality/rate/period facts must come from the actual current designation, not the old illustrative city list. Paper Major Events returns have the electronic restriction described by the government. [BC MRDT/Major Events and filing explanation](https://www2.gov.bc.ca/gov/content/taxes/sales-taxes/pst/publications/small-business-guide).
18. Retain the original Vancouver/Victoria/Whistler/Tofino/Kelowna rate-checking job, and any actual destination marketing fee. Their current local designations and private fee/base were not all verified here; do not copy a presumed “most other places 2%” rule. A private fee and the statutory Major Events MRDT are distinct.

### Prepare the actual FIN400 and settlement

19. Obtain the actual assigned period. The current government table describes more than CAD 12,000 annual PST as monthly only; more than 6,000 through 12,000 monthly/quarterly; more than 3,000 through 6,000 quarterly/semi-annual; at most 3,000 quarterly/semi-annual/annual. Follow the account assignment and any approved variation. A business that should register but does not has the government's monthly rule. The old 11,940 boundary and “negative collections means annual” were invented. [Current reporting-period guide](https://www2.gov.bc.ca/gov/content/taxes/sales-taxes/pst/report-pay).
20. Complete the actual return worksheet and transfer its required fields, not the old fabricated A-G map. All values are CAD; use the return guide's Bank of Canada date basis for currency. Include collectable amounts even if the customer has not yet paid. Do not net an unsupported adjustment against collections. [Actual FIN400](https://www2.gov.bc.ca/assets/gov/taxes/sales-taxes/forms/fin-400-provincial-sales-tax-return.pdf), [guide](https://www2.gov.bc.ca/gov/content/taxes/sales-taxes/pst/report-pay/pst-return-guide).

| Actual FIN400 box | Workpaper |
|---|---|
| A | Total taxable, non-taxable and exempt sales/leases **in Canada**, excluding taxes and actual facilitator-reported sales under the current guide; not merely BC sales |
| B | PST collected or levied/collectable on sales/leases, including tax charged in error unless properly refunded/credited; applicable special amounts need actual classification |
| C | Permitted timely primary-account commission; use the actual piecewise worksheet, not 1.32% |
| D | B minus C, intermediate net sales tax; not a self-assessment field |
| E and F | Untaxed taxable own-use purchase/lease cost and its actual PST, respectively |
| G | D plus F, intermediate liability before supported adjustments |
| H and I | Previously remitted tax on qualified bad-debt write-offs and actual customer refunds/credits, respectively |
| J and K | H plus I; then G minus J as total due, with separate remittance/certification and any revised-return indication |

All box meanings above are from the [actual FIN400](https://www2.gov.bc.ca/assets/gov/taxes/sales-taxes/forms/fin-400-provincial-sales-tax-return.pdf) and [current return guide](https://www2.gov.bc.ca/gov/content/taxes/sales-taxes/pst/report-pay/pst-return-guide). The online entry prompts and paper worksheet are not proof of a successful submission.

21. For commission, establish on-time full filing/payment and the allowed account. It is based on sales/lease collectable tax, not self-assessed purchases or MRDT. Do not claim it for each branch independently. Reconcile refunded/corrected sales and the actual worksheet; the cap alone does not define the formula. [Actual worksheet](https://www2.gov.bc.ca/assets/gov/taxes/sales-taxes/forms/fin-400-provincial-sales-tax-return.pdf), [guide](https://www2.gov.bc.ca/gov/content/taxes/sales-taxes/pst/report-pay/pst-return-guide).
22. For bad debt, retain invoice, original tax/remittance, actual write-off and proportional eligible tax. The guide requires the adjustment in the write-off period; otherwise its separate refund route/time limit applies. Later recovery requires reinstating the attributable tax. Customer refund/credit adjustments have their own actual period and refund conditions; do not deduct unpaid disputed tax twice. [Return adjustments and formula](https://www2.gov.bc.ca/gov/content/taxes/sales-taxes/pst/report-pay/pst-return-guide).
23. Reconcile total due to approved payment, account arrears/credit allocations, bank processing cut-off and actual receipt. Do not pay an unrelated audit assessment/fee through the period return; follow its separate notice. A payment confirmation does not prove a return was filed. Retain the return, authority, accepted acknowledgement, payment and account statement. [Return/payment instructions](https://www2.gov.bc.ca/gov/content/taxes/sales-taxes/pst/report-pay/pst-return-guide), [actual form](https://www2.gov.bc.ca/assets/gov/taxes/sales-taxes/forms/fin-400-provincial-sales-tax-return.pdf).
24. Calendar the last day of the following month for ordinary calendar-month periods, with applicable extensions. The guide's approved non-calendar reporting period uses its separate 30-day rule. Mail evidence and electronic/bank evidence follow the actual timeliness rules, not an invented universal receipt/postmark rule. Nil returns remain required until the account is validly closed. [Guide filing dates and closure](https://www2.gov.bc.ca/gov/content/taxes/sales-taxes/pst/report-pay/pst-return-guide).
25. Retain sufficient sales, tax, purchases, inventory/use, commission, exemption, shipping, refund/write-off and platform records. The government describes a five-year general retention with outstanding appeal/permission and longer exemption-proof needs; don't destroy evidence solely because an age test passed. Prepare actual account changes/FIN357 closure and remaining returns when required. [Records and closure](https://www2.gov.bc.ca/gov/content/taxes/sales-taxes/pst/publications/small-business-guide), [closure](https://www2.gov.bc.ca/gov/content/taxes/sales-taxes/pst/report-pay/pst-return-guide).

### Asset sales, property, penalties and referrals

Keep the old residential/new/used/commercial property, goodwill, equipment/inventory/software and business-transfer work. Classify each asset under its own statute; a federal business-transfer election does not automatically exempt provincial taxable assets. Obtain the actual clearance certificate and tax liabilities before a business acquisition and reconcile the statutory successor/bulk obligations; the old section 230 citation was not established as the universal rule. Do not promise that a registered buyer acquires all operating equipment tax free. [BC buying/selling a business and clearance explanation](https://www2.gov.bc.ca/gov/content/taxes/sales-taxes/pst/publications/small-business-guide).

Late, non-filer, failure-to-collect and unsupported-adjustment cases can produce distinct tax, penalties, interest and loss of commission. The old universal 10% penalty and unspecified “current” interest are not certified for every failure; obtain the applicable Act/notice, period/rate and payment history. Refer audit defence, disclosure, insolvency/receivership and appeals with their actual deadlines/authority. The government disclosure route is conditional and does not waive all tax-equivalent penalties. [BC audits, appeals and voluntary disclosure conditions](https://www2.gov.bc.ca/gov/content/taxes/sales-taxes/pst/publications/small-business-guide).

## Boundary and exception table

| Original referral/default | Correct response |
|---|---|
| Contractor/property | Obtain actual supply/affix/asset and statutory agreement/exemption work; no blanket retail or no-tax result |
| Liquor/cannabis/vapour/energy | Apply actual PST category and specialist other-tax/exemption work; do not use another province's levy |
| Vehicle/boat/aircraft | Obtain actual acquisition/classification/valuation and rate history; private and GST-registrant cases differ |
| Insurance/financial services | Obtain the actual separate tax statute and supply; no automatic substitution for all PST work |
| First Nations/reserve | Obtain qualifying recipient, location/delivery and legal exemption evidence; status alone is insufficient |
| Bankruptcy/receivership/audit/disclosure/appeal | Refer the specific authorised legal/administrative issue with records and deadlines |
| Multiple provinces | Complete supported BC work and separate each other province's owner return; not a global refusal |
| Uncertain tax or location | Research actual category/base/place and isolate the gap; do not charge or self-assess simply to be “conservative” |
| Exemption/certificate | Obtain what the actual exemption requires; do not demand a certificate where law gives an unconditional goods exemption |
| Marketplace | Verify role, collector and seller evidence; prevent double collection and preserve actual exceptions/liability |

## Worked cases

### Case 1: original Cascadia Cloud Inc. facts, with explicit supported assumptions

Preserve the Vancouver corporation's original figures: BC SaaS CAD 240,000; Ontario SaaS 360,000; US SaaS 500,000; Burnaby hardware 12,000; registered-platform Vancouver accommodation 18,000; foreign cloud invoice 40,000, of which supported BC use 30,000. The original period was Q2 2025; that historic return needs its own period's law and account schedule. The following **calendar 2026 workpaper scenario** uses those figures and explicitly assumes that the SaaS and the BC-use purchased cloud component have been established to be taxable software, none of the hardware is exempt, the facilitator properly accounts for the accommodation, no adjustments, and this is one permitted on-time primary-account reporting period. It is not a determination that every current AWS product or platform service qualifies.

BC collectable PST is CAD 17,640; self-assessed purchase PST 2,100; actual commission is capped 198; net 19,542. The old result happened to reach the same cap but its 1.32% method and box meanings were wrong. BoxA Canadian non-platform sales are 612,000, not 252,000; collectable tax is BoxB, commissionC, purchase costE/taxF, final totalK. The US sale is not part of BoxA Canadian sales on these stated place-of-sale facts. Actual global legal/place facts can change the reporting population. [Actual FIN400](https://www2.gov.bc.ca/assets/gov/taxes/sales-taxes/forms/fin-400-provincial-sales-tax-return.pdf), [current BoxA platform/Canada rule](https://www2.gov.bc.ca/gov/content/taxes/sales-taxes/pst/report-pay/pst-return-guide), [BC source/use/base](https://www2.gov.bc.ca/gov/content/taxes/sales-taxes/pst/publications/small-business-guide).

```oa-check
name: BC 2026 Cascadia supported standard-rate return workpaper
inputs:
  bc_taxable_software_sales: 240000
  ontario_sales_in_canada: 360000
  bc_hardware: 12000
  supported_bc_untaxed_software_purchase: 30000
steps:
  - box_a_canadian_nonplatform_sales: bc_taxable_software_sales + ontario_sales_in_canada + bc_hardware
  - box_b_collectable: (bc_taxable_software_sales + bc_hardware) * 0.07
  - box_c_on_time_primary_commission: min(198, round(box_b_collectable * 0.066, 2))
  - box_d: box_b_collectable - box_c_on_time_primary_commission
  - box_f_self_assessed: supported_bc_untaxed_software_purchase * 0.07
  - box_k_no_adjustments: box_d + box_f_self_assessed
expected:
  box_a_canadian_nonplatform_sales: 612000
  box_b_collectable: 17640
  box_c_on_time_primary_commission: 198
  box_d: 17442
  box_f_self_assessed: 2100
  box_k_no_adjustments: 19542
```

For the accommodation, obtain actual facilitator reporting and separate MRDT return/period and applicable Major Events rate. No automatic host GST collection is assumed. For Ontario/US sales, complete the federal place-of-supply/export workpaper; no 5% output tax is imposed on a valid zero-rated export merely because the old text did so. [Separate return guide](https://www2.gov.bc.ca/gov/content/taxes/sales-taxes/pst/report-pay/pst-return-guide), [CRA zero-rating](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4022/general-information-gst-hst-registrants.html).

### Case 2: commission below the cap and no commission on self-assessment

A timely eligible primary account has CAD 200 collectable PST and CAD 70 supported self-assessed purchase PST, no adjustments. Actual BoxC is CAD 22 under the middle interval, not CAD 2.64 or 198. Net due is 248. The purchase tax does not enlarge the commission base. [Actual commission worksheet](https://www2.gov.bc.ca/assets/gov/taxes/sales-taxes/forms/fin-400-provincial-sales-tax-return.pdf).

```oa-check
name: BC actual middle commission interval
inputs:
  collectable_sales_tax: 200
  self_assessed_purchase_tax: 70
steps:
  - permitted_middle_commission: 22
  - net_due: collectable_sales_tax - permitted_middle_commission + self_assessed_purchase_tax
expected:
  permitted_middle_commission: 22
  net_due: 248
```

That case is deliberately inside the stated middle interval with its eligibility satisfied, not a complete piecewise calculator for every account. The worksheet's low and high branches must be applied when those facts differ.

## When to refuse or refer

Do not finalise an unknown period, unsupported supply/place/base/exemption, unverified collector role, material special-rate or adjustment claim, or unexplained reconciliation difference. Complete the supported rows and identify the exact unresolved determination. Do not represent registration, an export, a proposed journal or a prepared return/payment as accepted by the authority.

## Completion checklist

- Correct local/remote/platform registration route and population, not one universal revenue threshold.
- Current transaction-date category, exemption, price/use and special-rate facts established.
- Federal tax classified separately; no 5% “zero-rated” tax or automatic GST marketplace role.
- All original exempt/sector/property/asset/First Nation/referral investigations retained with specific evidence.
- Actual FIN400 boxes, collectable timing, Canada/platform sales population and own-use purchases reconciled.
- Commission eligibility/formula/account, bad debts, customer credits and recoveries supported.
- Separate FIN401/Major Events/account evidence obtained where applicable.
- Actual assigned period, deadline, nil/closure, records and accepted submission/payment evidence retained.

## Sources

| Source actually read and scope | Official URL | Read on |
|---|---|---|
| Read for current goods purchase/lease/gift rate provisions, private/registrant/ZEV vehicle distinctions and ordinary tax base scope; not every exemption or full Act | https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/12035_03 | 2026-11-14 |
| Read for registration sections 168-175, local/remote/platform routes and threshold wording, collection/platform exceptions and duties; not every later enforcement rule | https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/12035_08 | 2026-11-14 |
| Read for actual location, small-seller, contractor, remote order/solicitation/inventory/software and registration scenarios; not every linked industry bulletin | https://www2.gov.bc.ca/assets/gov/taxes/sales-taxes/publications/pst-001-registering-to-collect-pst.pdf | 2026-11-14 |
| Read for general/special scope, exemptions, GST separation, MRDT/Major Events, own-use purchases, records, clearance, refunds and disclosure distinctions | https://www2.gov.bc.ca/gov/content/taxes/sales-taxes/pst/publications/small-business-guide | 2026-11-14 |
| Read for whole current FIN400 preparation guide, box meanings, collectable timing, Canada/platform population, currency, adjustments, payment/dates and closure | https://www2.gov.bc.ca/gov/content/taxes/sales-taxes/pst/report-pay/pst-return-guide | 2026-11-14 |
| Read for actual complete FIN400 worksheet/remittance, piecewise commission and certification; dated form revision is not a new 2026 edition | https://www2.gov.bc.ca/assets/gov/taxes/sales-taxes/forms/fin-400-provincial-sales-tax-return.pdf | 2026-11-14 |
| Read for current assigned reporting-period table, commission and separate MRDT | https://www2.gov.bc.ca/gov/content/taxes/sales-taxes/pst/report-pay | 2026-11-14 |
| Read for entire B.C.Reg.161/2026 and October 2026 professional-service exemption commencement | https://www.bclaws.gov.bc.ca/civix/document/id/bcgaz2/bcgaz2/v69n16_161-2026 | 2026-11-14 |
| Read for CRA taxable versus zero-rated supplies, export conditions boundary and federal input-credit distinction; not every federal place-of-supply rule | https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4022/general-information-gst-hst-registrants.html | 2026-11-14 |

Not yet confirmed: every specialised current software/cloud/telecom product classification, bundle apportionment and exception; exact accommodation occupancy/long-stay rule and all current city MRDT designations/rates; any specific private destination fee/base; every vehicle valuation/modified/ZEV exemption case; energy/insurance/First Nation/Crown/manufacturing/contractor conditions and current penalty/interest figures. These jobs remain in scope for the stated specialised workpapers, not certified blanket outcomes. The old universal 10,000 registration rule, private-sale 7%,1.32% commission, fabricated return boxes, MRDT-on-FIN400, Netflix-no-PST and five-percent-zero-rated-export statements are corrected, not usable fallbacks. No accountant approval is added or inferred.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `bc-pst` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/bc-pst. If neither is available, confirm every figure against the official source pages cited above before relying on it.
