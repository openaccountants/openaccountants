---
name: tn-sales-tax
description: "Apply Tennessee 2026 sales/use tax: 7% general, 4% qualifying food, local rates, single-article additional state tax, remote nexus, taxable software/digital products and exemptions. Covers TNTAP registration, filing, use tax and holiday decisions. Trigger on TN retail sales, consumer use or sales tax returns."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/tn-sales-tax"
  jurisdiction: "US-TN"
  tax_year: "2026"
  last_updated: "2026-11-13"
---

# Tennessee sales and use tax, tax year 2026

> **Source-cited draft.** Written by Codex. Not reviewed by an accountant. This skill supports a professional working paper; review the taxpayer facts and current forms before filing. Circular 230 section 10.37: this material is not a legal opinion or a substitute for reasonable factual and legal inquiry.

**Answer first.** Tennessee generally charges 7% state sales tax plus the applicable local tax. Qualifying food uses 4%; high-value single articles require an additional state tax as well as the local cap, so the ordinary combined rate alone can give the wrong answer.

## Scope and who this is for

Tennessee retail sales and consumer use tax, including physical/remote sellers and marketplace reconciliation. This skill is source-cited and usable within the identified rules; the blocked 2026 sales manual leaves specific legacy topics unconfirmed below. Multi-state allocation belongs with `us-sales-tax`; entity and payroll obligations have separate Tennessee owners.

## Ask the client first

1. What goods, services, software delivery modes, agreements and exemption uses are involved?
2. Where are the seller, inventory, workers, pickup and delivery locations; what physical presence exists?
3. What Tennessee retail sales occurred in the previous 12 months, separating resale, exempt retail, direct and facilitated sales?
4. What are the registered locations, assigned return frequency and actual current local rates?
5. What certificates, marketplace collection evidence, out-of-state tax credits and prior returns/payments support the calculation?
6. For a holiday purchase, what date, item price and personal versus business use apply?

## The method, step by step

### Rates, bands and thresholds

| Item and conditions | Amount / treatment | Official source |
| --- | --- | --- |
| Ordinary retail sale / ordinary local maximum | 7% state; applicable local up to 2.75%; ordinary combined maximum 9.75% | [official text](https://revenue.support.tn.gov/hc/en-us/articles/360058139672-SUT-13-Sales-and-Use-Tax-Rates-Overview) |
| Qualifying food and food ingredients | 4% state plus local; maximum 6.75% at 2.75% local | [official text](https://revenue.support.tn.gov/hc/en-us/articles/360058680751--SUT-53-Food-and-Food-Ingredients-Definition-and-Tax-Rate) |
| Single independent article | 7% all price + local on first $1,600 + additional 2.75% state on next $1,600 (maximum $44 additional state) | [official text](https://revenue.support.tn.gov/hc/en-us/articles/360058138992-SUT-6-Single-Article-Tax-Overview-and-Application) |
| Specified digital audio/video/books | 7% state plus fixed 2.5% local, without single-article limitation | [official text](https://revenue.support.tn.gov/hc/en-us/articles/360058688471-SUT-65-Specified-Digital-Products) |
| Remote seller economic threshold | More than $100,000 Tennessee retail sales in previous 12 months; exempt retail included, resale excluded; no transaction-count test | [official text](https://revenue.support.tn.gov/hc/en-us/articles/360057680592-RS-3-How-to-Apply-Sales-Threshold) |
| Marketplace facilitator threshold | Combine own and facilitated retail sales; more than $100,000 in previous 12 months | [official text](https://revenue.support.tn.gov/hc/en-us/articles/360058083371-MF-8-How-to-Calculate-100-000-Threshold) |
| Annual personal-use holiday limits | Clothing/school and art supplies $100 or less each; computers $1,500 or less | [official text](https://revenue.support.tn.gov/hc/en-us/articles/360057399112-STH-2-Sales-Tax-Holiday-Qualifying-Items) |
| Delinquency penalty | 5% per month or part, maximum 25%, minimum $15; interest additional | [official text](https://revenue.support.tn.gov/hc/en-us/articles/360057121372-GEN-16-Penalties-and-Interest) |

### Establish nexus and register

Physical presence (locations, inventory, employees or other activities) requires its own analysis. A remote seller exceeds the economic threshold only when Tennessee retail sales are **more than $100,000** during the previous 12 months, without a transaction-count alternative. Include exempt retail sales, exclude resale sales. The current threshold began October 1, 2020; the earlier October 2019 regime used a different threshold. Marketplace facilitators combine their own and facilitated sales. Reconcile marketplace collection separately; do not collect tax twice or assume facilitated sales discharge direct-sale obligations. Sources: [official text](https://revenue.support.tn.gov/hc/en-us/articles/360057680592-RS-3-How-to-Apply-Sales-Threshold), [official text](https://revenue.support.tn.gov/hc/en-us/articles/360058083371-MF-8-How-to-Calculate-100-000-Threshold).

Register the sales/use account through **TNTAP**, choosing **Register a New Business** where applicable, and obtain the certificate before filing. Registration is free. Do not mistake the agency's registration test based on average monthly **gross sales** for a filing-frequency test based on monthly tax. Source: [official text](https://revenue.support.tn.gov/hc/en-us/articles/360058139252-SUT-10-Sales-and-Use-Tax-Account-Registering-for-an-Account).

### Classify the transaction and source it

Retail tangible goods, including ordinary clothing and footwear, are generally taxable. Food ingredients qualify for the reduced rate only under the food definition; prepared food, candy, supplements, alcohol and tobacco do not. Human prescription drugs can be exempt, **including an OTC product actually prescribed**; an ordinary unprescribed OTC purchase is taxable. Sources: [official text](https://revenue.support.tn.gov/hc/en-us/articles/360058139672-SUT-13-Sales-and-Use-Tax-Rates-Overview), [official text](https://revenue.support.tn.gov/hc/en-us/articles/360058680751--SUT-53-Food-and-Food-Ingredients-Definition-and-Tax-Rate), [official text](https://revenue.support.tn.gov/hc/en-us/articles/360058688011-SUT-125-Sales-of-Prescription-Drugs).

Taxable services include repairs of tangible property/software, installation of property that remains tangible property, software installation, parking, laundry, telecommunications/video services and short lodging stays. Check the service-specific rule rather than applying a blanket tax to every service. Charges for delivery forming part of a taxable sale remain in the taxable price even if separately stated. Repair of property shipped into Tennessee and then shipped out has an interstate exception. General professional/personal services, real-property construction, waste handling and utilities need their specific definitions; do not treat this as a universal exemption list. Sources: [official text](https://revenue.support.tn.gov/hc/en-us/articles/360058683911-SUT-115-Services-Services-Subject-to-Sales-and-Use-Tax), [official text](https://revenue.support.tn.gov/hc/en-us/articles/360058176172-SUT-37-Repair-Services-on-Property-Shipped-into-Tennessee-for-Repair).

Custom and prewritten software are taxable regardless of physical or electronic delivery. Remotely accessed software used in Tennessee is taxable, with specific exclusions for genuine data processing, payroll/payment processing, billing/collection and certain digital/Internet services. A prewritten module/application can be a single article, including remotely accessed software: apply the limitation to the **whole service agreement**, not afresh to every installment. Custom software does not receive that limit. Specified digital audio/video/books, including qualifying streaming products, use the fixed 2.5% local rate on the full taxable price, not the ordinary local single-article rule. Sources: [official text](https://revenue.support.tn.gov/hc/en-us/articles/360058683491-SUT-61-Computer-Software-Custom-Software), [official text](https://revenue.support.tn.gov/hc/en-us/articles/360057266092-RAS-1-Remotely-Accessed-Software-Overview), [official text](https://revenue.support.tn.gov/hc/en-us/articles/360058681571-SUT-57-Computer-Software-Single-Article-Tax-Application), [official text](https://revenue.support.tn.gov/hc/en-us/articles/360058688471-SUT-65-Specified-Digital-Products).

For in-state sellers, the agency describes local sourcing to the business location; remote sellers shipping from outside Tennessee use the destination. Establish the actual location rate and any special sourcing before calculation. Do not label an illustrative city rate as a verified 2026 rate. Sources: [official text](https://revenue.support.tn.gov/hc/en-us/articles/360058174652-SUT-29-Online-Sales-by-In-State-Sellers), [official text](https://revenue.support.tn.gov/hc/en-us/articles/360058623411-SUT-30-Online-Sales-by-Out-of-State-Sellers).

### Compute sales or use tax

For an ordinary single independent article with price P and local rate L: **0.07 P + L x min (P,1,600) + 0.0275 x min (max (P - 1,600,0),1,600)**. The additional state tax is distinct from the general state tax and the local tax. Separate independent items do not become one article merely because they are sold in a set or bundle. The limit does not generally apply to services, admissions, warranty/service contracts, custom software or specified digital products. Source: [official text](https://revenue.support.tn.gov/hc/en-us/articles/360058138992-SUT-6-Single-Article-Tax-Overview-and-Application).

Use tax applies to taxable use, storage or consumption where sufficient sales tax was not collected; the state/local single-article calculation also applies where appropriate. Reconcile seller-collected tax and any allowable other-state credit before paying, rather than assuming the same nominal rate means no use tax. Source: [official text](https://revenue.support.tn.gov/hc/en-us/articles/360057569011-CUT-3-Consumer-Use-Tax-Rate).

### Exemption evidence and holiday

Obtain the applicable resale, manufacturer, agricultural or governmental/nonprofit evidence, match the purchaser and actual use, and retain it with the transaction. Manufacturing requires the specific industrial-machinery qualification and authorization; energy/water treatment is conditional. Agriculture requires an eligible exemption certificate, not merely a buyer saying the goods will be used on a farm. The old unconditional 51%-use, all-manufacturing-utilities and unverified form-code claims are not a filing basis. Sources: [official text](https://revenue.support.tn.gov/hc/en-us/articles/360058700311-SUT-80-Industrial-Machinery-Exemption-for-Manufacturers), [official text](https://revenue.support.tn.gov/hc/en-us/articles/360058677991-SUT-91-Agricultural-Exemption-Overview).

The annual holiday runs from 12:01 a.m. the last Friday in July through 11:59 p.m. Sunday. That calendar rule gives **July 31 to August 2, 2026**. Eligible personal-use clothing, school/art supplies and computers within the limits are exempt from state and local tax; purchases for a business do not qualify. Above-limit items are fully taxable, not just the excess. Sources: [official text](https://revenue.support.tn.gov/hc/en-us/articles/360057875471-STH-1-Date-of-Sales-Tax-Holiday), [official text](https://revenue.support.tn.gov/hc/en-us/articles/360057399112-STH-2-Sales-Tax-Holiday-Qualifying-Items), [official text](https://revenue.support.tn.gov/hc/en-us/articles/360057876891-STH-4-Sales-Tax-Holiday-Which-Merchants-Participate).

## Boundary and exception table

| Situation | Treatment |
| --- | --- |
| Industrial machinery / farm equipment | Confirm eligibility and current certificate; do not give a blanket exemption. |
| Residential gas/electricity | The utility FAQ describes gas/propane/electricity taxation for **non-residential** use. The former full-rate residential statement is withdrawn; exact residential exemption and water treatment need the underlying rules. |
| Human OTC drug prescribed | Can qualify for the prescription-drug exemption; ordinary unprescribed OTC remains taxable. |
| Software and digital bundle | Identify prewritten versus custom software, genuine excluded services and specified digital products before applying any cap. |
| Short rental / hotel / admission | Sales tax can apply; special occupancy levies, facilitator treatment and nonprofit-event exclusions require their own rule. Do not apply the equipment cap to the entire service invoice. |
| Marketplace plus direct sales | Obtain facilitator collection evidence and separately reconcile direct sales and registration. |
| No individual income tax | Sales/use, entity franchise/excise, gross-receipts business tax and employer UI can still apply; see `tn-corporate-tax` and `tn-payroll`. |

Sources: [official text](https://revenue.support.tn.gov/hc/en-us/articles/360058700311-SUT-80-Industrial-Machinery-Exemption-for-Manufacturers), [official text](https://revenue.support.tn.gov/hc/en-us/articles/360058677991-SUT-91-Agricultural-Exemption-Overview), [official text](https://revenue.support.tn.gov/hc/en-us/articles/360058703911-SUT-137-Utilities-Water-Natural-Gas-Propane-and-Electricity), [official text](https://revenue.support.tn.gov/hc/en-us/articles/360058688011-SUT-125-Sales-of-Prescription-Drugs), [official text](https://revenue.support.tn.gov/hc/en-us/articles/360058138992-SUT-6-Single-Article-Tax-Overview-and-Application), [official text](https://revenue.support.tn.gov/hc/en-us/articles/360058683911-SUT-115-Services-Services-Subject-to-Sales-and-Use-Tax), [official text](https://revenue.support.tn.gov/hc/en-us/articles/360058083371-MF-8-How-to-Calculate-100-000-Threshold), [official text](https://revenue.support.tn.gov/hc/en-us/articles/360057595051-GEN-34-Income-Tax-Withholding).

## Worked cases

**Case 1.** At an assumed verified local rate of 2.75%, a $50,000 boat owes $3,500 general state + $44 local + $44 additional state = **$3,588**. The old $3,544 omitted the additional state tax. A $100,000 equipment article similarly owes **$7,088**, not $7,044. Ten separate $500 items owe **$487.50**, since each is below the article limits.

```oa-check
name: TN single article versus separate items
inputs:
  boat: 50000
  equipment: 100000
  item_price: 500
  items: 10
  local_rate: 0.0275
steps:
- boat_tax: boat*0.07 + min(boat,1600)*local_rate + min(max(boat-1600,0),1600)*0.0275
- equipment_tax: equipment*0.07 + min(equipment,1600)*local_rate + min(max(equipment-1600,0),1600)*0.0275
- separate_items_tax: items*item_price*(0.07+local_rate)
expected:
  boat_tax: 3588
  equipment_tax: 7088
  separate_items_tax: 487.5
```

**Case 2, eligibility decision.** During the qualifying 2026 holiday, a personal-use $90 shirt qualifies, while $120 boots exceed the limit and are fully taxable. At an assumed 2.25% local rate, shirt tax is **$0**, boots tax **$11.10**. The same $90 shirt purchased for business owes **$8.325** before transaction rounding; this is not a holiday exemption.

```oa-check
name: TN personal-use holiday eligibility branches
inputs:
  shirt: 90
  boots: 120
  shirt_exempt: 1
  boots_exempt: 0
  business_exempt: 0
  rate: 0.0925
steps:
- shirt_tax: shirt*rate*(1-shirt_exempt)
- boots_tax: boots*rate*(1-boots_exempt)
- business_shirt_tax: shirt*rate*(1-business_exempt)
expected:
  shirt_tax: 0
  boots_tax: 11.1
  business_shirt_tax: 8.325
```

**Preserved former examples, with location rates treated as inputs:** $200 shoes at 7% + assumed 2.25% local produce $18.50 tax; $300 qualifying groceries at 4% + assumed 2.25% local produce $18.75. A $500 month-to-month taxable software agreement at the same local rate produces $46.25; an annual agreement paid monthly needs the article calculation on the whole agreement. A remote-only seller with $90,000 of relevant retail sales and 400 transactions does not exceed the economic test, assuming no physical presence; 400 transactions alone do not trigger it. A relocating business must consider sales/use, entity and business taxes and UI even though individual wage withholding is absent.


## When to refuse or refer

Refer audit/assessment, voluntary disclosure, penalty abatement, ambiguous bundled software/services, industrial eligibility, multi-state nexus and unconfirmed legacy topics. Keep an unsupported exemption out of the final return until resolved.

## Filing and payment

File and pay electronically through [TNTAP](https://tntap.tn.gov/eservices/), selecting the correct sales/use account and period. Reconcile gross sales, exempt sales, state tax, local jurisdiction detail and business use purchases; save acceptance and payment confirmation. File required zero returns. Follow the **assigned** frequency: monthly returns are due the 20 th of the following month, quarterly returns the 20 th after quarter-end, and annual returns January 20; a weekend/holiday moves the due date to the next business day. Sources: [official text](https://revenue.support.tn.gov/hc/en-us/articles/360058589831-SUT-8-Sales-and-Use-Tax-Online-Filing), [official text](https://revenue.support.tn.gov/hc/en-us/articles/360058589911-SUT-9-Sales-and-Use-Tax-Filing-Filing-Due-Dates).

The old automatic $400 monthly-tax quarterly threshold and denial of annual filing are not supported by these opened pages. The TACIR report says Tennessee no longer provides general vendor compensation apart from very limited exceptions; do **not** deduct the old generic 2%/$50 credit. That report is a verified **2025-2026 filing cycle** baseline; any special 2026 allowance requires confirmation. Source: [official text](https://www.tn.gov/content/dam/tn/tacir/2025publications/2025_VendorComp.pdf).

Delinquency generally incurs 5% per month/part, maximum 25%, minimum $15, plus interest. Do not use the old approximate 7.25% interest rate: GEN 16's 11.50% statement applies only through June 30, 2026, so later-period interest remains unconfirmed. Fraud and collection assessments require separate authority and professional review. Source: [official text](https://revenue.support.tn.gov/hc/en-us/articles/360057121372-GEN-16-Penalties-and-Interest).

## Completion checklist

- Confirm nexus, registration, taxability, actual local rate and independent-article status.
- Reconcile direct versus facilitator collection and consumer use tax.
- Retain exemption support and accepted return/payment references.
- Resolve listed gaps before using any omitted legacy rule.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| DOR SUT 13. Read for general and local maximum rates. | https://revenue.support.tn.gov/hc/en-us/articles/360058139672-SUT-13-Sales-and-Use-Tax-Rates-Overview | 2026-11-13 |
| DOR SUT 6. Read for single-article formula, additional state tax, independent units and exceptions. | https://revenue.support.tn.gov/hc/en-us/articles/360058138992-SUT-6-Single-Article-Tax-Overview-and-Application | 2026-11-13 |
| DOR SUT 53. Read for food definition and 4% rate. | https://revenue.support.tn.gov/hc/en-us/articles/360058680751--SUT-53-Food-and-Food-Ingredients-Definition-and-Tax-Rate | 2026-11-13 |
| DOR CUT 3. Read for consumer use and single-article state/local treatment. | https://revenue.support.tn.gov/hc/en-us/articles/360057569011-CUT-3-Consumer-Use-Tax-Rate | 2026-11-13 |
| DOR RS 3. Read for strictly more than $100,000, rolling 12 months and included/excluded sales. | https://revenue.support.tn.gov/hc/en-us/articles/360057680592-RS-3-How-to-Apply-Sales-Threshold | 2026-11-13 |
| DOR MF 8. Read for combined facilitator sales measurement. | https://revenue.support.tn.gov/hc/en-us/articles/360058083371-MF-8-How-to-Calculate-100-000-Threshold | 2026-11-13 |
| DOR SUT 10. Read for TNTAP registration, free certificate and distinction from filing frequency. | https://revenue.support.tn.gov/hc/en-us/articles/360058139252-SUT-10-Sales-and-Use-Tax-Account-Registering-for-an-Account | 2026-11-13 |
| DOR SUT 29/30. Read for local sourcing for in-state sellers. | https://revenue.support.tn.gov/hc/en-us/articles/360058174652-SUT-29-Online-Sales-by-In-State-Sellers | 2026-11-13 |
| DOR SUT 30. Read for destination for out-of-state shipment. | https://revenue.support.tn.gov/hc/en-us/articles/360058623411-SUT-30-Online-Sales-by-Out-of-State-Sellers | 2026-11-13 |
| DOR SUT 115. Read for enumerated taxable services and delivery in sales price. | https://revenue.support.tn.gov/hc/en-us/articles/360058683911-SUT-115-Services-Services-Subject-to-Sales-and-Use-Tax | 2026-11-13 |
| DOR SUT 37. Read for interstate repair exception. | https://revenue.support.tn.gov/hc/en-us/articles/360058176172-SUT-37-Repair-Services-on-Property-Shipped-into-Tennessee-for-Repair | 2026-11-13 |
| DOR RAS 1. Read for remote software and excluded service categories. | https://revenue.support.tn.gov/hc/en-us/articles/360057266092-RAS-1-Remotely-Accessed-Software-Overview | 2026-11-13 |
| DOR SUT 57. Read for prewritten single-article agreement treatment and custom exception. | https://revenue.support.tn.gov/hc/en-us/articles/360058681571-SUT-57-Computer-Software-Single-Article-Tax-Application | 2026-11-13 |
| DOR SUT 61. Read for custom/prewritten software across delivery modes. | https://revenue.support.tn.gov/hc/en-us/articles/360058683491-SUT-61-Computer-Software-Custom-Software | 2026-11-13 |
| DOR SUT 65. Read for specified digital products, fixed 2.5% local and no article cap. | https://revenue.support.tn.gov/hc/en-us/articles/360058688471-SUT-65-Specified-Digital-Products | 2026-11-13 |
| DOR SUT 125. Read for prescribed human OTC versus unprescribed OTC. | https://revenue.support.tn.gov/hc/en-us/articles/360058688011-SUT-125-Sales-of-Prescription-Drugs | 2026-11-13 |
| DOR SUT 80. Read for industrial machinery qualification and utility distinctions. | https://revenue.support.tn.gov/hc/en-us/articles/360058700311-SUT-80-Industrial-Machinery-Exemption-for-Manufacturers | 2026-11-13 |
| DOR SUT 91. Read for agricultural certificate requirement. | https://revenue.support.tn.gov/hc/en-us/articles/360058677991-SUT-91-Agricultural-Exemption-Overview | 2026-11-13 |
| DOR SUT 137. Read for enumerated utility charges and non-residential distinction. | https://revenue.support.tn.gov/hc/en-us/articles/360058703911-SUT-137-Utilities-Water-Natural-Gas-Propane-and-Electricity | 2026-11-13 |
| DOR STH 1. Read for last Friday July to Sunday holiday calendar. | https://revenue.support.tn.gov/hc/en-us/articles/360057875471-STH-1-Date-of-Sales-Tax-Holiday | 2026-11-13 |
| DOR STH 2. Read for holiday qualifying item limits. | https://revenue.support.tn.gov/hc/en-us/articles/360057399112-STH-2-Sales-Tax-Holiday-Qualifying-Items | 2026-11-13 |
| DOR STH 4. Read for business purchases excluded. | https://revenue.support.tn.gov/hc/en-us/articles/360057876891-STH-4-Sales-Tax-Holiday-Which-Merchants-Participate | 2026-11-13 |
| DOR SUT 8. Read for mandatory electronic returns and zero returns. | https://revenue.support.tn.gov/hc/en-us/articles/360058589831-SUT-8-Sales-and-Use-Tax-Online-Filing | 2026-11-13 |
| DOR SUT 9. Read for monthly/quarterly/annual due dates and next business day. | https://revenue.support.tn.gov/hc/en-us/articles/360058589911-SUT-9-Sales-and-Use-Tax-Filing-Filing-Due-Dates | 2026-11-13 |
| DOR GEN 16. Read for 5% delinquency, $15 minimum and interest only through June 2026. | https://revenue.support.tn.gov/hc/en-us/articles/360057121372-GEN-16-Penalties-and-Interest | 2026-11-13 |
| TACIR vendor-compensation report (2025-2026 filing cycle). Read for absence of a general vendor allowance, subject to narrow exceptions. | https://www.tn.gov/content/dam/tn/tacir/2025publications/2025_VendorComp.pdf | 2026-11-13 |
| DOR GEN 34. Read for no earned-income tax withholding and Hall repeal. | https://revenue.support.tn.gov/hc/en-us/articles/360057595051-GEN-34-Income-Tax-Withholding | 2026-11-13 |

Not yet confirmed: The August 2026 sales manual could not be read (403). Current city/county rates; assigned-frequency thresholds; exact 2026 SLS 450 screen/line mapping and individual consumer-use filing route; special vendor compensation; post-June interest; fraud penalty; certificate form names ST-14/F-13/ST-18/SSTCE, acceptance protection and three-years-from-last-transaction retention are unconfirmed. So are durable medical equipment, motor-fuel exemption boundaries, raw materials, residential utilities/water rates, legal/accounting/personal services and real-property contractor detail, commercial/residential waste collection, occupancy levies/short-rental facilitator mechanics, nonprofit admission exclusions and Streamlined member/program status. These old topics remain visible here, not approved as current rules.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-13. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `tn-sales-tax` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/tn-sales-tax. If neither is available, confirm every figure against the official source pages cited above before relying on it.
