---
name: saudi-arabia-vat
description: Use this skill whenever asked to prepare, review, or classify transactions for a Saudi Arabia VAT return for any client. Trigger on phrases like "prepare VAT return", "Saudi VAT", "ZATCA return", "KSA VAT", "fill in VAT return", "Fatoorah", "e-invoicing Saudi", or any request involving Saudi Arabia VAT filing. Also trigger when classifying transactions for VAT purposes from bank statements, invoices, or other source data. This skill covers KSA only and only standard VAT-registered persons. VAT groups, profit margin schemes, partial exemption with significant exempt supplies, oil & gas sector special rules, and designated zone goods movement classifications are all in the refusal catalogue. MUST be loaded alongside vat-workflow-base v0.1 or later (for workflow architecture). ALWAYS read this skill before touching any KSA VAT work.
version: 2.1
jurisdiction: SA
tax_year: 2026
last_updated: 2026-11-26
source_checked: 2026-11-26
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
reviewed_by: "Mehran Habib"
reviewed_on: 2026-11-03
tier: 1
domain: vat-gst
type: filing-howto
category: VAT
tax_year_notes: "Current 2026 edition; original April 2026 cases retain their dates and undated historic cases remain undated. Historical amendment commencement requires separate confirmation."
---

# Saudi Arabia VAT

## Scope

Prepare a single Saudi VAT-registered person's return using this Guide and `vat-workflow-base` v0.1 or later. This is the **2026 edition**, with the original April **2026** examples preserved on their actual dates. Undated historical cases remain undated. A bank statement supports reconciliation; it does not establish the supply date, rate or right to deduct.

Use the Arabic regulations where the English translation differs. The linked English consolidation is dated November 2021; the Arabic tenth edition includes the April 2025 amendments. ZATCA’s [current Arabic regulations page](https://zatca.gov.sa/ar/RulesRegulations/Taxes/Pages/VATImplementingRegulations.aspx), updated in September 2026, links to that tenth edition. Use its retained operative provisions for 2026; do not apply amended wording retrospectively to earlier transactions without confirming commencement. For a 2025 transaction whose result depends on amendment commencement: **Check this point with one of our partner accountants.**

Quick reference: standard-rated Saudi supplies bear **15%**; zero-rating and exemption require the conditions below. Use the taxpayer's actual registered period and the portal's field labels. Do not create a return from guessed supplier residence, an assumed rate or a bank-name match. [ZATCA rate explanation](https://zatca.gov.sa/en/RulesRegulations/VAT/Pages/About-Vat.aspx), [Arabic regulations](https://zatca.gov.sa/ar/RulesRegulations/Taxes/Documents/Implmenting%20Regulations%20of%20the%20VAT%20Law.pdf).

## Ask the client first

Read the available records before requesting missing facts. Obtain the legal name, registration certificate and VAT number, CR if applicable, registered filing period, accounting basis, business activity, employees, taxable/exempt activities, customer/supplier establishments, invoice register, customs entries, credit notes, prior return and carried-forward credit. Obtain the actual Phase 2 notification and supporting invoices. Do not infer a VAT number's validity from its length or digits.

Resolve unknown vehicle availability for private use, legally required staff benefits, mixed-use phone/internet use, insurance type, property use and foreign-service beneficiaries. Hold an unidentified receipt, owner-named transfer, outgoing payment to an individual or cash withdrawal for explanation; do not default it to sales, salary, a loan or drawings. Missing tax documents prevent a filing-ready deduction; the old SAR 2,000 documentation cutoff is withdrawn. Article 49(7) requires evidence of the input tax; alternative commercial evidence is subject to the Authority's discretion. [IR Article 49](https://zatca.gov.sa/en/RulesRegulations/Taxes/Documents/Implmenting%20Regulations%20of%20the%20VAT%20Law_EN.pdf).

## The method, step by step

### Registration, period and amounts

| Item | Rule and operative conditions | Official source |
|---|---|---|
| Standard rate | 15% on standard-rated supplies from 1 July 2020; do not apply it to exempt or qualifying zero-rated supplies. Historical 5% contract transitions require separate dated review. | [VAT Law Article 2, ZATCA explanation](https://zatca.gov.sa/en/RulesRegulations/VAT/Pages/About-Vat.aspx) |
| Mandatory registration | Resident person's registration supplies exceed SAR 375,000 over the relevant 12 months; test both previous supplies and expected future supplies. Compute the base under Agreement Article 52: taxable supplies, received supplies on which the recipient must account for VAT (including reverse charge), and qualifying intra-GCC supplies. Exclude exempt supplies; apply the capital-asset disposal exclusion subject to IR Article 6(5), rather than counting every disposal as turnover. IR Articles 3–4 require application within 30 days of month end when their test is met. The all-zero-rated exception in Article 9 must be considered. Non-resident registration is outside this resident threshold test. | [Agreement Articles 50–52](https://www.zatca.gov.sa/ar/RulesRegulations/Taxes/Documents/GCC%20VAT%20Agreement.pdf); [IR Articles 3–9](https://zatca.gov.sa/ar/RulesRegulations/Taxes/Documents/Implmenting%20Regulations%20of%20the%20VAT%20Law.pdf); [threshold explanation, section 3.2](https://zatca.gov.sa/en/HelpCenter/guidelines/Documents/Guideline-on-Tax-Groups-under-VAT-Provisions.pdf) |
| Voluntary registration | Resident person not required to register: taxable supplies or qualifying expenses reach at least SAR 187,500 in the previous or expected next 12 months, subject to IR Article 7. | [IR Article 7](https://zatca.gov.sa/ar/RulesRegulations/Taxes/Documents/Implmenting%20Regulations%20of%20the%20VAT%20Law.pdf); [section 3.3 threshold explanation](https://zatca.gov.sa/en/HelpCenter/guidelines/Documents/Guideline-on-Tax-Groups-under-VAT-Provisions.pdf) |
| Filing period | Monthly where taxable supplies in the previous 12 months exceed SAR 40,000,000; otherwise normally three months. A smaller taxpayer may have an approved monthly period or a period directed by ZATCA. Use the registration/period notification. | [IR Article 58](https://zatca.gov.sa/en/RulesRegulations/Taxes/Documents/Implmenting%20Regulations%20of%20the%20VAT%20Law_EN.pdf) |
| Filing and payment | Both normally due by the last day of the month after the tax period ends. Article 74(1) requires returns and tax payment by the stated date even when it is not a working day; do not roll these deadlines forward. | [IR Articles 59(1), 62(1), 74(1)](https://zatca.gov.sa/ar/RulesRegulations/Taxes/Documents/Implmenting%20Regulations%20of%20the%20VAT%20Law.pdf) |
| Foreign currency | Convert to SAR at the Saudi Central Bank daily rate on the date the relevant tax becomes due, not automatically the bank settlement date. The original USD 16 / SAR 60 case stipulates SAR 60; it is not an exchange-rate rule. | [IR Article 61](https://zatca.gov.sa/ar/RulesRegulations/Taxes/Documents/Implmenting%20Regulations%20of%20the%20VAT%20Law.pdf) |

For a confirmed VAT-inclusive standard-rated amount: net = gross / 1.15; VAT = gross − net. For a VAT-exclusive amount: VAT = net × 0.15. Preserve debit/credit signs in the transaction sheet and transfer positive purchase/sales bases to the relevant return category; do not multiply every bank payment by 15%.

### Supplier patterns are search aids

The old supplier library's names remain useful for finding documents, not assigning tax. Al Rajhi/ALRAJHI/مصرف الراجحي, SNB/NCB/البنك الأهلي, Riyad Bank, SABB, BSF, ANB, Alinma, Bank AlJazira, Bank Albilad, Revolut and Wise require the actual fee or financing document. An explicit bank or payment-processing fee is not exempt merely because the supplier is a bank: Article 29(1) excludes explicit fees, commissions and commercial discounts from its financial-service exemption. Interest/implicit-margin financing and equivalent Islamic finance follow Article 29, subject to the transaction's actual nature. [IR Article 29](https://zatca.gov.sa/ar/RulesRegulations/Taxes/Documents/Implmenting%20Regulations%20of%20the%20VAT%20Law.pdf).

Use invoices for SEC, SWCC, NWC, Marafiq; STC, Mobily, Zain, Virgin Mobile; Jarir, Extra, IKEA, SACO; legal/accounting/audit and government-liaison providers. The normal deduction rule applies only to correctly incurred VAT for taxable business use, subject to restrictions. It is not automatic even for accounting fees. [IR Article 49](https://zatca.gov.sa/en/RulesRegulations/Taxes/Documents/Implmenting%20Regulations%20of%20the%20VAT%20Law_EN.pdf).

For Tawuniya, Bupa, MedGulf, Malath, Walaa and Al Rajhi Takaful distinguish life insurance from other insurance. The life-insurance/reinsurance exemption in Article 29(7) includes explicit consideration; general, motor and health insurance do not acquire that exemption from the insurer's name. Apply the input restrictions separately. [IR Article 29(7)–(8)](https://zatca.gov.sa/ar/RulesRegulations/Taxes/Documents/Implmenting%20Regulations%20of%20the%20VAT%20Law.pdf).

For Uber, Careem, Saudia, Flynas, SAR railway, DHL and Aramex, establish the actual route/service. International passenger and goods transport is zero-rated under Article 34; a domestic journey is not an export merely because the carrier also flies abroad. Distinguish a purchase from the taxpayer's own transport sale. [IR Article 34(1)–(2), (7)](https://zatca.gov.sa/ar/RulesRegulations/Taxes/Documents/Implmenting%20Regulations%20of%20the%20VAT%20Law.pdf).

Panda, Carrefour, Danube, Tamimi, Othaim, Bin Dawood, restaurants and cafes require the invoice and purpose. Apply Article 50 restrictions to consumption/entertainment, with its onward-taxable-supply exception; do not block trading stock merely because it came from a supermarket. [IR Article 50](https://zatca.gov.sa/ar/RulesRegulations/Taxes/Documents/Implmenting%20Regulations%20of%20the%20VAT%20Law.pdf).

Google, Microsoft, Adobe, Meta, LinkedIn, AWS, Notion, Anthropic, OpenAI, GitHub, Figma, Canva, Slack, Atlassian, Zoom, HubSpot, Stripe subscriptions, Shopify and Twilio require the actual invoice, supplying establishment and Saudi VAT treatment. Do not assume the billing entity from a brand. Likewise inspect Stripe, PayPal, Mada, HyperPay, Moyasar and Payfort fee invoices. Unknown residence or a VAT number alone does not settle the reverse charge.

Al Rajhi/SNB/Riyad/Revolut/Wise column layouts and Gregorian/Hijri dates must be checked against the actual export. SADAD and Mada descriptions identify a payment channel; trace the underlying bill or merchant. Arabic hints include مشتريات (purchases), مبيعات (sales), رواتب (salaries), إيجار (rent), كهرباء (electricity), مياه (water), اتصالات (telecom). Reconcile own-account transfers, WPS/salary, GOSI, end-of-service, owner drawings, dividends, loan principal, zakat/VAT/customs payments and Ministry/municipality/CITC/CMA/Absher/Muqeem/Qiwa/Mudad payments to their underlying records. A government or platform name does not establish an exclusion. For unresolved legal treatment of these items: **Check this point with one of our partner accountants.**

### Return categories

Use the separate **Amount**, **Adjustment** and **VAT Amount** columns. These are categories, not one field number for a base and the next field for its tax. The official [Submit VAT Return manual, pages 6–7](https://zatca.gov.sa/en/eServices/Documents/eServices_Manual_009.pdf) shows:

| Return category | Treatment |
|---|---|
| 1 Standard Rated Sales | Enter standard-rated sales base and output tax in its respective columns. |
| 2 Sales on which the government bears VAT | Specialist category; hold for confirmation, not a GCC-sales field. |
| 3 Zero Rated Domestic Sales; 4 Exports; 5 Exempt Sales; 6 Total Sales | Keep zero-rated domestic supplies, exports and exempt supplies distinct. |
| 7 Standard Rated Domestic Purchases | Enter the purchase base and eligible input VAT in this row's columns. |
| 8 Imports subject to VAT paid on import | Use the customs import record and eligible import VAT, not a guessed bank amount. |
| 9 Imports subject to VAT accounted for through reverse charge | Account for the reverse-charge liability and permitted input deduction; do not also claim the same tax in domestic purchases. |
| 10 Zero Rated Purchases; 11 Exempt Purchases; 12 Total Purchases | Reconcile to supporting records. |
| Total VAT screen | Reconcile current-period tax, prior credit, corrections and net VAT. Follow live labels; the old invented Fields 13–20 must not be used as an overlay. |

A taxable customer liable for a supply received from a non-resident accounts for output VAT and eligible input VAT under IR Article 47(1). For a standard-rated imported service, compute 15% output tax; equal input tax is possible only when fully deductible. Both sides remain in the working paper even when the net is zero. In the portal, category 9 assumes full input deduction and nets the two sides; restricted deduction requires the corresponding adjustment. Refer unresolved partial-recovery cases before filing. [ZATCA reverse-charge circular, section 3](https://www.zatca.gov.sa/en/MediaCenter/Publications/Documents/VAT%20Circular%20-%20RCM-EN.pdf). Establish place of supply and whether Saudi VAT has correctly been charged before applying this rule. For physical goods cleared at customs, use the import document, import VAT actually assessed and entitlement under Article 49, rather than treating them as imported services. [IR Articles 43–44, 47(1), 49](https://zatca.gov.sa/en/RulesRegulations/Taxes/Documents/Implmenting%20Regulations%20of%20the%20VAT%20Law_EN.pdf).

Credit/debit notes adjust the relevant supply category under Articles 40 and 54; they are not automatically previous-return errors. Amended Article 54(6) requires the note no later than the fifteenth day of the following month. For amended Article 63: an understatement normally requires correction of the original return within 20 days of discovery; an understatement **strictly below SAR 15,000** may instead be added in the return for the discovery period. An overstatement may be deducted in a subsequent return, within five years from the end of the calendar year containing the original period. Do not replace the law's strict threshold with an inclusive portal label. For an earlier-period error, first establish the operative amendment date; if unresolved, refer before choosing a correction route. [Arabic IR Articles 54(6), 63(1)–(5)](https://zatca.gov.sa/ar/RulesRegulations/Taxes/Documents/Implmenting%20Regulations%20of%20the%20VAT%20Law.pdf).

## Boundary and exception table

| Topic | Rule or boundary | Official source |
|---|---|---|
| Export goods | Zero-rating requires export evidence within 90 days: customs export documentation, commercial documents identifying customer/delivery, and transportation evidence of delivery/receipt outside the relevant territory. | [IR Article 32(1)–(4)](https://zatca.gov.sa/en/RulesRegulations/Taxes/Documents/Implmenting%20Regulations%20of%20the%20VAT%20Law_EN.pdf) |
| Export services | Customer must be non-resident in the relevant member-state territory. Check all amended Article 33 exclusions: special place-of-supply rules; resident customer; customer/related person's direct benefit while present in a member state where the related person cannot fully deduct; tangible services on goods there. A foreign remittance alone proves none of this. | [Arabic IR Article 33](https://zatca.gov.sa/ar/RulesRegulations/Taxes/Documents/Implmenting%20Regulations%20of%20the%20VAT%20Law.pdf) |
| GCC transactions | Article 79(6) treats a member state without VAT or without the electronic-services system with KSA as outside Council territory. Do not default every UAE/Bahrain/Oman sale to domestic 15%. Confirm the actual state, supply and operative arrangements; unresolved treatment is referred below. | [Arabic IR Article 79(6)](https://zatca.gov.sa/ar/RulesRegulations/Taxes/Documents/Implmenting%20Regulations%20of%20the%20VAT%20Law.pdf) |
| Medicines/medical equipment | Zero-rating applies to qualifying medicines/medical goods under the competent authority's classifications and any additional controls; not every medical purchase qualifies. | [IR Article 35](https://zatca.gov.sa/ar/RulesRegulations/Taxes/Documents/Implmenting%20Regulations%20of%20the%20VAT%20Law.pdf) |
| Investment metals | Article 36 covers the producer/refiner's first supply and qualifying investment rights. Qualifying metals are gold, silver or platinum; investment metal must be at least 99% pure and tradeable on the global bullion market. Purity alone does not establish every supply's treatment. | [IR Article 36](https://zatca.gov.sa/en/RulesRegulations/Taxes/Documents/Implmenting%20Regulations%20of%20the%20VAT%20Law_EN.pdf) |
| Property, including Ejar/warehouse/office/Wafi | Transfer of ownership/right to dispose as owner is VAT-exempt for commercial/residential property and land; residential lease/licence is exempt. Temporary hotel/serviced accommodation is not residential real estate. A commercial lease is subject to normal taxable-supply rules. Do not zero-rate the first SAR 1,000,000 of a property sale. RETT/first-home assistance requires separate advice. | [IR Article 30 and VAT scope](https://zatca.gov.sa/ar/RulesRegulations/Taxes/Documents/Implmenting%20Regulations%20of%20the%20VAT%20Law.pdf) |
| Deductible input VAT | Correctly incurred tax for taxable business activity, supported by Article 49(7) evidence and subject to restrictions. Direct exempt costs are not deductible under Article 51(2); private-use costs are blocked under Article 50. Do not promise full recovery on exempt real-estate sales. | [IR Articles 49–51](https://zatca.gov.sa/ar/RulesRegulations/Taxes/Documents/Implmenting%20Regulations%20of%20the%20VAT%20Law.pdf) |
| Entertainment and staff meals | Amended Article 50 blocks entertainment and hospitality/catering unless an applicable exception is established. Workplace food/hospitality has a statutory-obligation exception; a staff dinner or business discussion alone is insufficient. Onward taxable resale has its own exception. | [Arabic IR Article 50(1), (4)](https://zatca.gov.sa/ar/RulesRegulations/Taxes/Documents/Implmenting%20Regulations%20of%20the%20VAT%20Law.pdf) |
| Employee insurance/healthcare | Amended Article 50(1)(c) restricts employee/dependent insurance/healthcare, with the statutory-obligation exception. Do not extend that exception automatically to housing or childcare; resolve the actual benefit and statutory basis. | [Arabic IR Article 50(1)](https://zatca.gov.sa/ar/RulesRegulations/Taxes/Documents/Implmenting%20Regulations%20of%20the%20VAT%20Law.pdf) |
| Vehicles | Amended restricted-vehicle definition covers vehicles designed for no more than 10 people. Exceptions include exclusive economic use with no private availability, taxable resale/lease/similar activity, specified emergency vehicles and qualifying heavy equipment. Restricted-vehicle purchase/lease, insurance, repairs and fuel are blocked. The owner's occupation alone does not determine entitlement. | [Arabic IR Article 50(1)–(2)](https://zatca.gov.sa/ar/RulesRegulations/Taxes/Documents/Implmenting%20Regulations%20of%20the%20VAT%20Law.pdf) |
| Mixed-use phone/internet | Deduct only the evidenced eligible economic-use part under Article 49, subject to restrictions; do not treat all mixed use as automatically zero or fully recoverable. Taxable/exempt residual-cost apportionment is a separate Article 51 issue. | [IR Articles 49–51](https://zatca.gov.sa/ar/RulesRegulations/Taxes/Documents/Implmenting%20Regulations%20of%20the%20VAT%20Law.pdf) |

## Worked cases

These preserve all original inputs. Conditional results are usable only after the stated evidence is established; held deductions are not asserted to be zero under the law.

### Original April 2026 examples

1. **Notion:** `03.04.2026 ; NOTION LABS INC ; DEBIT ; Monthly subscription ; USD 16.00 ; SAR 60.00`. Assuming the invoice establishes the non-resident imported-service facts and fully taxable use: base SAR 60, reverse-charge output SAR 9, deductible input SAR 9, net SAR 0 in reverse-charge category 9. The brand alone is insufficient. [IR 47(1), 49](https://zatca.gov.sa/en/RulesRegulations/Taxes/Documents/Implmenting%20Regulations%20of%20the%20VAT%20Law_EN.pdf).
2. **Techcorp:** `10.04.2026 ; TECHCORP INC DELAWARE ; CREDIT ; Invoice SA-2026-018 IT consultancy March ; +25,000.00 ; SAR`. SAR 25,000 in Exports category 4 with zero output VAT only if every applicable amended Article 33 condition above is satisfied; otherwise hold, rather than infer zero-rating from a US name or receipt. [Arabic IR 33](https://zatca.gov.sa/ar/RulesRegulations/Taxes/Documents/Implmenting%20Regulations%20of%20the%20VAT%20Law.pdf).
3. **Client dinner:** `15.04.2026 ; THE GLOBE RESTAURANT RIYADH ; DEBIT ; Client dinner ; -1,800.00 ; SAR`. Client hospitality for the consultant's consumption, not onward taxable resale: deductible VAT SAR 0 under Article 50. If the invoice confirms gross SAR 1,800 includes 15%, embedded tax is SAR 234.78 and net SAR 1,565.22; the full SAR 1,800 is the unrecovered cost. Do not describe gross as VAT-exclusive net. [Arabic IR 50(1)](https://zatca.gov.sa/ar/RulesRegulations/Taxes/Documents/Implmenting%20Regulations%20of%20the%20VAT%20Law.pdf).
4. **Laptop:** `18.04.2026 ; JARIR BOOKSTORE ; DEBIT ; Invoice JR-2026-441 Laptop HP ; -5,750.00 ; SAR`. With a valid invoice and wholly eligible taxable business use: SAR 5,000 net, SAR 750 deductible VAT in domestic-purchase category 7; gross remains SAR 5,750. [IR 49](https://zatca.gov.sa/en/RulesRegulations/Taxes/Documents/Implmenting%20Regulations%20of%20the%20VAT%20Law_EN.pdf).
5. **Car lease:** `22.04.2026 ; AL JAZIRAH VEHICLES ; DEBIT ; Monthly car lease ; -4,500.00 ; SAR`. The IT-consultant occupation does not itself block recovery. Hold the claim until vehicle/private-availability facts and invoice are obtained. If a restricted vehicle, deductible VAT is zero; if exclusive economic use with no private availability is proven, normal deduction conditions apply. If SAR 4,500 includes 15%, embedded VAT is SAR 586.96 and net SAR 3,913.04; neither amount is automatically deductible. [Arabic IR 50(1)–(2)](https://zatca.gov.sa/ar/RulesRegulations/Taxes/Documents/Implmenting%20Regulations%20of%20the%20VAT%20Law.pdf).
6. **Bank fee:** `28.04.2026 ; AL RAJHI BANK ; DEBIT ; Monthly account maintenance ; -50.00 ; SAR`. An explicit maintenance fee is not the implicit-margin exemption. Obtain the invoice: if SAR 50 is VAT-inclusive at 15%, net SAR 43.48 and VAT SAR 6.52, potentially deductible under the normal conditions in category 7. If SAR 50 is exclusive, VAT is SAR 7.50 and total SAR 57.50; the bank debit alone does not settle this. [IR 29(1), 49](https://zatca.gov.sa/en/RulesRegulations/Taxes/Documents/Implmenting%20Regulations%20of%20the%20VAT%20Law_EN.pdf).

```oa-check
name: sa-original-2026-purchases
inputs:
  notion: 60
  dinner: 1800
  laptop: 5750
  lease: 4500
  bank_fee: 50
  rate: 0.15
steps:
  - notion_rc: notion * rate
  - notion_net: notion_rc - notion_rc
  - dinner_vat: round(dinner * rate / (1 + rate), 2)
  - dinner_net: round(dinner / (1 + rate), 2)
  - laptop_net: laptop / (1 + rate)
  - laptop_vat: laptop - laptop_net
  - lease_vat: round(lease * rate / (1 + rate), 2)
  - lease_net: round(lease / (1 + rate), 2)
  - bank_vat_inclusive: round(bank_fee * rate / (1 + rate), 2)
  - bank_net: round(bank_fee / (1 + rate), 2)
  - bank_vat_exclusive: bank_fee * rate
expected:
  notion_rc: 9
  notion_net: 0
  dinner_vat: 234.78
  dinner_net: 1565.22
  laptop_net: 5000
  laptop_vat: 750
  lease_vat: 586.96
  lease_net: 3913.04
  bank_vat_inclusive: 6.52
  bank_net: 43.48
  bank_vat_exclusive: 7.5
```

### Original v1.1 test cases retained

These original tests were undated. Their inputs remain unchanged; do not assign them a new tax year. Apply the corresponding operative rules above; amended-rule cases require commencement confirmation for the actual period.

| Original ID and input | Corrected result / final action | Official source |
|---|---|---|
| Test 1: domestic standard sale SAR 10,000 + 1,500 = 11,500 | Category 1 base 10,000, output 1,500; 11,500 total. | [VAT rate](https://zatca.gov.sa/en/RulesRegulations/VAT/Pages/About-Vat.aspx); [return manual](https://zatca.gov.sa/en/eServices/Documents/eServices_Manual_009.pdf) |
| Test 2: goods export to India SAR 50,000, export proof | Category 4 base 50,000, output zero only with Article 32 evidence/time conditions. | [IR 32](https://zatca.gov.sa/en/RulesRegulations/Taxes/Documents/Implmenting%20Regulations%20of%20the%20VAT%20Law_EN.pdf) |
| Test 3: office equipment SAR 5,000 + 750 = 5,750, fully taxable use | Category 7 base 5,000, eligible input 750 with valid evidence and no restriction. | [IR 49](https://zatca.gov.sa/en/RulesRegulations/Taxes/Documents/Implmenting%20Regulations%20of%20the%20VAT%20Law_EN.pdf) |
| Test 4: UK consulting, SAR 20,000, no VAT, fully taxable recipient | If taxable imported service: category 9 base 20,000, output 3,000, eligible input 3,000, net zero. | [IR 47(1), 49](https://zatca.gov.sa/en/RulesRegulations/Taxes/Documents/Implmenting%20Regulations%20of%20the%20VAT%20Law_EN.pdf) |
| Test 5: residential rent SAR 8,000/month | Exempt-sales category 5 base 8,000, output zero; directly attributable exempt costs not deductible. | [IR 30, 51(2)](https://zatca.gov.sa/en/RulesRegulations/Taxes/Documents/Implmenting%20Regulations%20of%20the%20VAT%20Law_EN.pdf) |
| Test 6: staff party catering SAR 15,000 + 2,250 VAT | Ordinary staff party, not statutory workplace provision or onward resale: input deduction zero; unrecovered total 17,250. | [Arabic IR 50](https://zatca.gov.sa/ar/RulesRegulations/Taxes/Documents/Implmenting%20Regulations%20of%20the%20VAT%20Law.pdf) |
| Test 7 / EC1: developer's first apartment sale, completed 1 year ago; SAR 1,100,000; eligible Saudi first-home buyer (EC1 described completion 2 years ago) | Under the property-transfer VAT exemption: exempt-sales category 5 base 1,100,000, VAT zero; withdraw the old SAR 1,000,000 zero-rate / SAR 100,000 taxable split and SAR 15,000 VAT. Separate RETT/assistance: Check this point with one of our partner accountants. | [IR 30(1)(a)](https://zatca.gov.sa/ar/RulesRegulations/Taxes/Documents/Implmenting%20Regulations%20of%20the%20VAT%20Law.pdf) |
| Test 8: machinery from Germany; customs value SAR 100,000; VAT SAR 15,000 paid | Category 8 uses the customs record; 15,000 input deductible only if Article 49 requirements are met. The stipulated customs assessment is not a general import-base formula. | [IR 43, 49](https://zatca.gov.sa/en/RulesRegulations/Taxes/Documents/Implmenting%20Regulations%20of%20the%20VAT%20Law_EN.pdf) |
| Test 9 / EC5: related companies; invoice SAR 10,000; market value SAR 25,000; both fully taxable | If recipient can fully deduct this supply's VAT, Article 38's recipient-ineligibility condition is absent: category 1 base 10,000, VAT 1,500. Mere VAT registration is insufficient. | [IR 38(1)](https://zatca.gov.sa/en/RulesRegulations/Taxes/Documents/Implmenting%20Regulations%20of%20the%20VAT%20Law_EN.pdf) |
| Test 10: discovered prior-period understatement SAR 8,000 | Under amended Article 63(3), 8,000 is below 15,000 and may be added in the discovery-period return. If earlier wording applies, do not use this route; confirm commencement first. | [Arabic IR 63](https://zatca.gov.sa/ar/RulesRegulations/Taxes/Documents/Implmenting%20Regulations%20of%20the%20VAT%20Law.pdf) |
| Test 11 / EC10: same-period credit note SAR 2,000 + 300 VAT | Reduce category 1 base by 2,000 and output tax by 300, total credit 2,300. A later price change and an error in an old return are distinct. | [IR 40, 54](https://zatca.gov.sa/en/RulesRegulations/Taxes/Documents/Implmenting%20Regulations%20of%20the%20VAT%20Law_EN.pdf) |
| Test 12 / EC9: laptop taken for personal use; original cost SAR 4,000; market value SAR 2,500 | HOLD: establish original deduction and whether capital-asset rules apply; withdraw automatic SAR 375 output tax on market value. Arithmetic alone: 2,500 × 15% = 375; 4,000 × 15% = 600, but neither is a filing conclusion. Check this point with one of our partner accountants. | No tax-law conclusion asserted; specialist referral. |

```oa-check
name: sa-original-v1-tests
inputs:
  sale: 10000
  equipment: 5000
  uk_service: 20000
  staff_party: 15000
  credit_note: 2000
  rate: 0.15
steps:
  - sale_vat: sale * rate
  - sale_total: sale + sale_vat
  - equipment_vat: equipment * rate
  - equipment_total: equipment + equipment_vat
  - rc_output: uk_service * rate
  - rc_input: rc_output
  - rc_net: rc_output - rc_input
  - party_vat: staff_party * rate
  - party_cost: staff_party + party_vat
  - credit_vat: credit_note * rate
  - credit_total: credit_note + credit_vat
expected:
  sale_vat: 1500
  sale_total: 11500
  equipment_vat: 750
  equipment_total: 5750
  rc_output: 3000
  rc_input: 3000
  rc_net: 0
  party_vat: 2250
  party_cost: 17250
  credit_vat: 300
  credit_total: 2300
```

## When to refuse or refer

A referral is a non-usable hold: do not insert a guessed tax result in the return. Each line below means **Check this point with one of our partner accountants.**

- **R-SA-1:** taxable/exempt residual-cost apportionment, incidental exempt transactions and annual adjustments; withdraw the oversimplified recovery fraction and old Article 50 citation. Article 51 is the relevant apportionment provision.
- **R-SA-2:** VAT group registration, eligibility, consolidation and changes.
- **R-SA-3 / EC4:** oil and gas / concession-specific supplies.
- **R-SA-4 / EC2:** special/designated zones, customs suspension and movements to the mainland; no automatic Article 39 zone treatment.
- **R-SA-5:** capital-asset adjustments, initial/actual use, disposal and private use; the old SAR 250,000 input-tax threshold and five-year movable-asset shortcut are withdrawn.
- **R-SA-6 / EC1:** first-home assistance and RETT, including the legacy SAR 1,000,000 relief topic; use only the VAT property exemption established above.
- **R-SA-7:** electronic marketplaces, deemed-supplier conditions and commencement; the old effective-date assertion is not a filing instruction.
- **EC7:** tourist refunds, participating retailers, operator eligibility and minimum spend.
- **EC8:** used-goods profit-margin eligibility, approval, calculation and record requirements.
- **EC6:** a GCC transaction whose actual transitional conditions have not been established; retain the original KSA-to-UAE goods-export topic without blanket domestic treatment.
- **EC3 and technical e-invoicing:** clearance versus reporting, deadlines, QR/TLV tags, UUID/stamps, XML/PDF formats, invoice/payment/tax-category codes, invoice validity and buyer deduction consequences. Do not infer legal validity from an open-source implementation.
- **EC11 / EC12 and other inherited boundaries:** government commercial/sovereign activity; non-resident registration/representative; deregistration; cash accounting; simplified invoices; record-retention periods; related-party facts not resolved above; deemed supplies/gifts including the old SAR 200 threshold; pre-July-2020 contracts; diplomatic supplies; penalty amounts, amnesty eligibility/expiry and excluded periods. No amount or date from the old text is current usable guidance for these points. Zakat, corporate/income tax, withholding, excise and RETT computations remain separate specialist topics.

## Filing and payment

E-invoicing generation applies from 4 December 2021 to resident VAT taxpayers and relevant parties issuing on their behalf; non-resident taxpayers are excluded. Phase 2 integration started on 1 January 2023 in waves. Obtain the actual notification; do not infer an assigned wave from the old Wave 24 summary. [ZATCA e-invoicing explanation](https://zatca.gov.sa/en/E-Invoicing/Introduction/Pages/What-is-E-invoicing.aspx).

Follow the official [Submit VAT Return manual, pages 3–9](https://zatca.gov.sa/en/eServices/Documents/eServices_Manual_009.pdf): open E-Services, choose Submit VAT Return, authenticate, select Returns → VAT and the required return, verify taxpayer details, enter sales and purchases, reconcile Total VAT, attach evidence, review the summary and have the authorized filer submit and generate the SADAD bill. Retain the submission confirmation, downloaded form, bill and payment confirmation. Reconcile prior credit rather than assuming a refund is automatic.

## Completion checklist

Keep Transactions, Field Summary and Return Form working sheets. Retain original amounts/currencies/signs, tax dates, supplier/customer evidence, category, tax incurred, deductible tax, adjustments, questions and holds. Sum actual eligible tax; never generate all purchase deductions by multiplying gross bank totals or customs payments by the standard rate. Reconcile totals to the live portal labels and prior credit. Recalculate every workbook formula, re-open cached results and check for formula errors; the old invented Fields 1–20 formulas are withdrawn. Colour conventions may follow the companion workflow.

Release a filing-ready working paper only after each hold affecting the return is resolved, evidence and computations reconcile and a qualified professional has reviewed it. This Guide is informational and computational support, not professional sign-off.

## Sources

| Source and read scope | Date read |
|---|---|
| [Current Arabic regulations page](https://zatca.gov.sa/ar/RulesRegulations/Taxes/Pages/VATImplementingRegulations.aspx): operative-document link and September 2026 update context. | 2026-11-26 |
| [Arabic VAT Implementing Regulations, tenth edition, April 2025](https://zatca.gov.sa/ar/RulesRegulations/Taxes/Documents/Implmenting%20Regulations%20of%20the%20VAT%20Law.pdf): cover/amendment list; Articles 3–9, 29–30, 32–36, 38–39, 47, 49–51, 54, 58–63, 74(1), 79(6). Amended Arabic wording controls the conflicts with the older translation. | 2026-11-26 |
| [English VAT Implementing Regulations, eighth edition, November 2021](https://zatca.gov.sa/en/RulesRegulations/Taxes/Documents/Implmenting%20Regulations%20of%20the%20VAT%20Law_EN.pdf): Articles 29–40, 43–44, 47, 49–52, 58–63; used only where applicable and not superseded. | 2026-11-26 |
| [GCC VAT Agreement](https://www.zatca.gov.sa/ar/RulesRegulations/Taxes/Documents/GCC%20VAT%20Agreement.pdf): Articles 50–52 and neighbouring definitions for registration thresholds and base; read through ZATCA’s current agreement link. | 2026-11-26 |
| [ZATCA reverse-charge circular](https://www.zatca.gov.sa/en/MediaCenter/Publications/Documents/VAT%20Circular%20-%20RCM-EN.pdf): sections 1–4, especially category 9 reporting and partial-recovery adjustment; read alongside IR Article 47(1). | 2026-11-26 |
| [ZATCA About VAT](https://zatca.gov.sa/en/RulesRegulations/VAT/Pages/About-Vat.aspx): rate change and VAT Law Article 2 explanation. | 2026-11-26 |
| [Tax Groups guideline, section 3.2–3.3](https://zatca.gov.sa/en/HelpCenter/guidelines/Documents/Guideline-on-Tax-Groups-under-VAT-Provisions.pdf): resident registration thresholds; Article 7 controls the voluntary threshold's inclusive test. | 2026-11-26 |
| [Submit VAT Return manual](https://zatca.gov.sa/en/eServices/Documents/eServices_Manual_009.pdf): pages 3–9, including visual reading of sales/purchases screenshot on page 6 and Total VAT screenshot on page 7. | 2026-11-26 |
| [ZATCA What is E-invoicing](https://zatca.gov.sa/en/E-Invoicing/Introduction/Pages/What-is-E-invoicing.aspx): scope, non-resident exclusion and phase dates. | 2026-11-26 |

Not yet confirmed: commencement of each amended provision for an affected earlier 2025 transaction; taxpayer-specific evidence and the specialist points in When to refuse or refer. These are explicit holds, not usable rates, defaults or filing conclusions. Check this point with one of our partner accountants.
