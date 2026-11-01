---
name: nigeria-vat
description: Use this skill whenever asked to prepare, review, or classify transactions for a Nigeria VAT return or advise on Nigerian VAT registration, filing, and compliance. Trigger on phrases like "prepare Nigeria VAT return", "Nigerian VAT", "NRS VAT", "FIRS VAT", "Form 002", or any Nigeria VAT request. ALWAYS read this skill before touching any Nigeria VAT work.
version: 2.1
jurisdiction: NG
tax_year: 2026
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - vat-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Nigeria VAT

Tax year 2026. Unofficial-source warning: see Status columns and "Not yet confirmed".

## Who this applies to

Taxable persons making taxable supplies in Nigeria from 1 January 2026, and non-residents supplying into Nigeria. All NTA figures below are read from an unofficial copy and stay marked unverified until confirmed in an official document. "NTA" means the Nigeria Tax Act 2025, in force 1 January 2026 (commencement line of the Act).

For the place-of-supply tests see NTA s.145. For 2025 and earlier see the pre-2026 section.

## Rates, bands and thresholds

| Item | Rate or amount | Tax year | Law | Status and link |
|---|---|---|---|---|
| Standard rate on taxable supplies | 7.5% | 2026 | NTA s.147 | unverified: unofficial copy only, https://media.premiumtimesng.com/wp-content/files/2026/01/Final-Approved-Copy-for-Print-NIGERIA-TAX-ACT-2025.pdf |
| Zero rate list, including basic food, medical services, tuition, exported goods other than oil and gas, exported services | 0% | 2026 | NTA s.186 | unverified: unofficial copy only, https://media.premiumtimesng.com/wp-content/files/2026/01/Final-Approved-Copy-for-Print-NIGERIA-TAX-ACT-2025.pdf |
| VAT withheld, collected or self-accounted: remit by | 14th day of the following month | 2026 | NTA s.154(4) | unverified: unofficial copy only, https://media.premiumtimesng.com/wp-content/files/2026/01/Final-Approved-Copy-for-Print-NIGERIA-TAX-ACT-2025.pdf |
| Input tax claim window | within 5 years after the end of the tax period | 2026 | NTA s.155(4)(b) | unverified: unofficial copy only, https://media.premiumtimesng.com/wp-content/files/2026/01/Final-Approved-Copy-for-Print-NIGERIA-TAX-ACT-2025.pdf |

## The base

Value is the amount which, with VAT added, equals the consideration; a non-money supply or a supply between connected persons uses market value (NTA s.148). Imports add duties and charges other than VAT, plus commission, "parking" (as printed), transport and insurance to the port (s.149).

Time of supply is the earliest of invoice or receipt, delivery or availability, or payment due or received (s.146).

Exempt under s.185: oil and gas exports, crude oil and feed gas, humanitarian donor project goods, baby products, locally made sanitary products, military hardware, shared passenger road transport, agricultural equipment, zone entity supplies on approved activity, diplomatic supplies, educational plays, land and buildings, money and securities, government licences, and assistive devices. Collection on Eleventh Schedule items waits for a ministerial order (s.185(2)).

Input tax on services and fixed assets is deductible to the extent used for taxable supplies, with a proportion where supplies are mixed, within five years (s.155(4)), and only for supplies from commencement (s.155(5)). This replaces the old limit in the earlier text below. Excess input VAT carries forward, and a refund is available on request (s.155(1)(b), (2)).

The earlier text's exempt list is not 2026 law: basic food, medical products, educational materials and exported services are zero rated under s.186, so related input tax stays recoverable.

## Deadlines and filing

The VAT remittance date for a taxable person is "the due date for rendering the relevant tax return prescribed by the Nigeria Tax Administration Act" (s.155(1)); we did not open that Act. Withheld or self-accounted VAT is due by the 14th of the next month with a schedule of supplier, Tax ID, invoice and amount (s.154(3), (4)). VAT invoices need the seven items in s.152(1). E-invoicing can be directed on 30 days' notice (s.152(4)); fiscalisation is mandatory as deployed (s.157). The NRS notice of 20 July 2026 told large taxpayers to "ensure full compliance on or before 31 July 2026".

## Penalties and interest

Set by the Nigeria Tax Administration Act 2025, not read. See "Not yet confirmed".

## Cross-border points

A non-resident supplying Nigeria registers and charges VAT (s.150(1)). Where it supplies from abroad, the Nigerian taxable customer withholds and remits (s.150(2)) unless an appointed collector has collected (s.150(4)). Goods bought through a non-resident platform with VAT already collected are not charged again on proof of payment (s.150(8)). Exports other than oil and gas are zero rated (s.186(n) to (p)).

## Two worked examples that recompute

Simple: month with standard-rated sales of NGN 10,000,000 before VAT and purchases of NGN 4,000,000 before VAT, all for taxable supplies.

```oa-check
name: Monthly VAT, standard-rated
inputs:
  sales: 10000000
  purchases: 4000000
steps:
  - output: sales * 0.075
  - input: purchases * 0.075
  - payable: output - input
expected:
  payable: 450000.00
```

Decision, is it better to supply zero rated or exempt? A clinic buys NGN 2,000,000 of taxable inputs. Medical services are zero rated (s.186(l)), so the NGN 150,000 of input VAT is recoverable. On an exempt supply the same NGN 150,000 would be a cost.

```oa-check
name: Input VAT, zero rated against exempt
inputs:
  inputs: 2000000
steps:
  - vat: inputs * 0.075
  - recoverable_zero: vat
  - recoverable_exempt: 0
  - difference: recoverable_zero - recoverable_exempt
expected:
  difference: 150000.00
```

## Ask the client first

1. Which period? Before 2026 uses the pre-2026 section.
2. What is supplied, and which s.185 or s.186 line fits?
3. Is the customer or supplier non-resident?
4. Any mixed taxable and non-taxable supplies?
5. Has NRS appointed the client to withhold or directed e-invoicing?

## Pre-2026 law (years of assessment to 2025)

This section keeps the earlier text so nothing is lost. It applies to years of assessment up to 2025, under the Acts repealed by NTA s.195 from 1 January 2026 (Personal Income Tax Act, Companies Income Tax Act, Capital Gains Tax Act, Value Added Tax Act and others). It was not re-read against those Acts in this update. Do not use it for 2026. Where it differs from the sections above, the sections above govern 2026 and later.



#### Section 1: Quick reference

**Quick reference**

| Field | Value | Status |
| --- | --- | --- |
| Country | Nigeria (Federal Republic of Nigeria) | unverified, earlier text not re-read |
| Tax | Value Added Tax (VAT) | unverified, earlier text not re-read |
| Currency | NGN (Nigerian Naira: ₦) | unverified, earlier text not re-read |
| Standard rate | 7.5% (effective February 2020; previously 5%) | unverified, earlier text not re-read |
| Zero rate | 0% (exports of goods and services, goods purchased by diplomats, humanitarian donor organisations) | unverified, earlier text not re-read |
| Exempt | Basic food items (unprocessed agricultural products), medical/pharmaceutical products, baby products, newspapers, educational materials, financial services, natural gas, exported services | unverified, earlier text not re-read |
| Registration threshold | NGN 25,000,000 annual turnover (from 2020); below this: no obligation to register | unverified, earlier text not re-read |
| Tax authority | Federal Inland Revenue Service (FIRS) | unverified, earlier text not re-read |
| Filing portal | FIRS TaxPro Max: https://taxpromax.firs.gov.ng | unverified, earlier text not re-read |
| Return form | VAT Form 002 (monthly return) | unverified, earlier text not re-read |
| Filing frequency | Monthly | unverified, earlier text not re-read |
| Deadline | 21st of the following month | unverified, earlier text not re-read |
| e-Invoice | FIRS e-Invoice / e-Receipt pilot: expanding from 2024 | unverified, earlier text not re-read |
| Contributor | Open Accountants Community | unverified, earlier text not re-read |
| Validated by | Live status: https://openaccountants.com/skills/nigeria-vat | unverified, earlier text not re-read |
| Skill version | 2.0 | unverified, earlier text not re-read |

##### Key VAT Form 002 lines

**Key VAT Form 002 lines**

| Line | Meaning | Status |
| --- | --- | --- |
| Line 1 | Total taxable sales (net of VAT) | unverified, earlier text not re-read |
| Line 2 | VAT on sales (Line 1 × 7.5%) | unverified, earlier text not re-read |
| Line 3 | Zero-rated sales | unverified, earlier text not re-read |
| Line 4 | Exempt sales | unverified, earlier text not re-read |
| Line 5 | Total input VAT (on purchases for taxable activities) | unverified, earlier text not re-read |
| Line 6 | Net VAT payable (Line 2 − Line 5) | unverified, earlier text not re-read |
| Line 7 | Excess input VAT carried forward | unverified, earlier text not re-read |

##### Conservative defaults

**Conservative defaults**

| Ambiguity | Default | Status |
| --- | --- | --- |
| Unknown rate on a sale | 7.5% standard | unverified, earlier text not re-read |
| Unknown whether food is processed/unprocessed | Treat as processed: 7.5% until confirmed | unverified, earlier text not re-read |
| Unknown whether pharmaceutical is exempt | 7.5% until exemption confirmed with NAFDAC registration | unverified, earlier text not re-read |
| Unknown whether export documentation complete | Treat as domestic 7.5% | unverified, earlier text not re-read |
| Unknown business-use % | 0% input credit | unverified, earlier text not re-read |
| Foreign digital service (B2B) | 7.5% reverse-charge: buyer self-assesses | unverified, earlier text not re-read |
| Unknown whether NGN 25M threshold met | Assume must file | unverified, earlier text not re-read |

##### Red flag thresholds

**Red flag thresholds**

| Threshold | Value | Status |
| --- | --- | --- |
| HIGH single transaction | NGN 10,000,000 | unverified, earlier text not re-read |
| HIGH tax delta on single conservative default | NGN 750,000 | unverified, earlier text not re-read |
| MEDIUM counterparty concentration | >40% of output or input | unverified, earlier text not re-read |
| MEDIUM conservative default count | >4 per return | unverified, earlier text not re-read |
| LOW absolute net VAT position | NGN 5,000,000 | unverified, earlier text not re-read |

#### Section 2: Required inputs and refusal catalogue

##### Required inputs

- **Required inputs before starting Nigeria VAT work**: 1. FIRS TIN (Tax Identification Number: 10 digits) and VAT registration certificate 2. Monthly bank statements in NGN (all business accounts) 3. Sales invoices with VAT registration number (VRN) printed 4. Purchase invoices from VAT-registered suppliers with their VRN 5. Prior month VAT return (for carried-forward excess input credit) 6. Export documentation (form NXP, shipping documents) for zero-rated exports 7. Details of exempt supplies (basic foodstuffs, medical goods) with product descriptions  _(unsure)_

##### Refusal catalogue

- **Refuse and escalate to a CITN-licensed tax practitioner**: VAT on imported services: complex FIRS guidance and WHT interaction; VAT grouping (rare in Nigeria); Petroleum Profit Tax (PPT): separate legislation; Real estate VAT (complex exemption rules on land vs. buildings); VAT refund claims: FIRS refund process is complex and slow; requires specialist; State-level consumption taxes (Lagos, Rivers): in addition to federal VAT; Free trade zone (FTZ) VAT treatment  _(unsure)_

#### Section 3: Supplier pattern library

##### 3.1 Banking and financial services

**Banking and financial services suppliers**

| Supplier | Typical description | VAT rate | Input credit | Status |
| --- | --- | --- | --- | --- |
| Guaranty Trust Bank (GTBank) | Bank fees, transfer charges | Exempt | No | unverified, earlier text not re-read |
| Zenith Bank | Account maintenance, corporate banking | Exempt | No | unverified, earlier text not re-read |
| Access Bank | Business banking fees | Exempt | No | unverified, earlier text not re-read |
| First Bank Nigeria | Commercial banking | Exempt | No | unverified, earlier text not re-read |
| United Bank for Africa (UBA) | Pan-African banking fees | Exempt | No | unverified, earlier text not re-read |
| Stanbic IBTC | Investment banking, advisory | Exempt | No | unverified, earlier text not re-read |
| Flutterwave | Payment gateway: processing fee | 7.5% | Yes | unverified, earlier text not re-read |
| Paystack | Payment gateway: commission | 7.5% | Yes | unverified, earlier text not re-read |
| Interswitch | Card switching, POS services | 7.5% | Yes | unverified, earlier text not re-read |
| PalmPay | Mobile payments | Exempt (payment) | No | unverified, earlier text not re-read |
| Opay | Digital wallet | Exempt | No | unverified, earlier text not re-read |

##### 3.2 Electricity and utilities

**Electricity and utilities suppliers**

| Supplier | Typical description | VAT rate | Input credit | Status |
| --- | --- | --- | --- | --- |
| Eko Electricity Distribution Company (EKEDC) | Electricity: Lagos Island/mainland south | 7.5% | Yes (business) | unverified, earlier text not re-read |
| Ikeja Electric (IKEDC) | Electricity: Lagos Ikeja/mainland north | 7.5% | Yes (business) | unverified, earlier text not re-read |
| Abuja Electricity Distribution Company (AEDC) | Electricity: FCT Abuja | 7.5% | Yes (business) | unverified, earlier text not re-read |
| Lagos State Water Corporation | Water supply | 7.5% | Yes | unverified, earlier text not re-read |
| LSWC / State water boards | Water: various states | 7.5% | Yes | unverified, earlier text not re-read |
| Lagos Waste Management Authority (LAWMA) | Waste disposal | 7.5% | Yes | unverified, earlier text not re-read |

##### 3.3 Telecommunications

**Telecommunications suppliers**

| Supplier | Typical description | VAT rate | Input credit | Status |
| --- | --- | --- | --- | --- |
| MTN Nigeria | Mobile, data | 7.5% | Yes (business use) | unverified, earlier text not re-read |
| Airtel Nigeria | Mobile, broadband | 7.5% | Yes (business use) | unverified, earlier text not re-read |
| Glo (Globacom) | Mobile, data | 7.5% | Yes (business use) | unverified, earlier text not re-read |
| 9mobile (etisalat) | Mobile, business lines | 7.5% | Yes (business use) | unverified, earlier text not re-read |
| IPNX | Fiber internet: enterprise | 7.5% | Yes | unverified, earlier text not re-read |
| Spectranet | Fixed wireless broadband | 7.5% | Yes | unverified, earlier text not re-read |
| Swift Networks | Enterprise connectivity | 7.5% | Yes | unverified, earlier text not re-read |

##### 3.4 Transport and travel

**Transport and travel suppliers**

| Supplier | Typical description | VAT rate | Input credit | Status |
| --- | --- | --- | --- | --- |
| Air Peace | Domestic flights | 7.5% | Yes | unverified, earlier text not re-read |
| Ibom Air | Domestic flights | 7.5% | Yes | unverified, earlier text not re-read |
| United Nigeria Airlines | Domestic flights | 7.5% | Yes | unverified, earlier text not re-read |
| Ethiopian Airlines Nigeria | International flights | 0% (export) | No input applicable | unverified, earlier text not re-read |
| Bolt Nigeria | Ride-hailing | 7.5% | Yes (business use) | unverified, earlier text not re-read |
| Uber Nigeria | Ride-hailing | 7.5% | Yes (business use) | unverified, earlier text not re-read |
| Rensource / Tricycle services | Local transport | 7.5% | Yes | unverified, earlier text not re-read |

##### 3.5 Logistics and courier

**Logistics and courier suppliers**

| Supplier | Typical description | VAT rate | Input credit | Status |
| --- | --- | --- | --- | --- |
| DHL Nigeria | International courier | 0% (export) / 7.5% (domestic) | Yes | unverified, earlier text not re-read |
| FedEx Nigeria | International courier | 0% / 7.5% | Yes | unverified, earlier text not re-read |
| GIG Logistics | Domestic courier | 7.5% | Yes | unverified, earlier text not re-read |
| ABC Cargo | Domestic freight | 7.5% | Yes | unverified, earlier text not re-read |
| Kwik Delivery | Last-mile delivery | 7.5% | Yes | unverified, earlier text not re-read |
| NIPOST | Nigerian postal service | 7.5% | Yes | unverified, earlier text not re-read |

##### 3.6 Retail and office supplies

**Retail and office supplies suppliers**

| Supplier | Typical description | VAT rate | Input credit | Status |
| --- | --- | --- | --- | --- |
| Jumia Nigeria | E-commerce marketplace | 7.5% (taxable goods) | Yes (business) | unverified, earlier text not re-read |
| Konga | E-commerce | 7.5% | Yes | unverified, earlier text not re-read |
| Shoprite Nigeria | Supermarket: food/non-food | Mixed (basic food exempt; other 7.5%) | Partial | unverified, earlier text not re-read |
| SPAR Nigeria | Supermarket | Mixed | Partial | unverified, earlier text not re-read |
| Staples Nigeria / Office supplies store | Office stationery | 7.5% | Yes | unverified, earlier text not re-read |
| Dangote Industries (cement) | Building materials | 7.5% | Yes | unverified, earlier text not re-read |
| Copy Shop / printing | Document printing | 7.5% | Yes | unverified, earlier text not re-read |

##### 3.7 Software and digital services

**Software and digital services suppliers**

| Supplier | Typical description | VAT rate | Input credit | Status |
| --- | --- | --- | --- | --- |
| Sage Nigeria | Accounting software | 7.5% | Yes | unverified, earlier text not re-read |
| VFD Tech / Mono | Fintech API | 7.5% | Yes | unverified, earlier text not re-read |
| Microsoft Nigeria (Azure, M365) | Cloud services: B2B | 7.5% (reverse-charge) | Yes | unverified, earlier text not re-read |
| Google Nigeria (Workspace, Ads) | Digital services: B2B | 7.5% (reverse-charge) | Yes | unverified, earlier text not re-read |
| Zoom Nigeria | Video conferencing: B2B | 7.5% (reverse-charge) | Yes | unverified, earlier text not re-read |
| AWS Nigeria | Cloud infrastructure: B2B | 7.5% (reverse-charge) | Yes | unverified, earlier text not re-read |
| Zoho Nigeria | Business software | 7.5% (reverse-charge if foreign) | Yes | unverified, earlier text not re-read |

##### 3.8 Professional services

**Professional services suppliers**

| Supplier | Typical description | VAT rate | Input credit | Status |
| --- | --- | --- | --- | --- |
| Chartered Accountant (ICAN/ANAN) | Audit, tax advisory | 7.5% | Yes | unverified, earlier text not re-read |
| Law firm | Legal services | 7.5% | Yes | unverified, earlier text not re-read |
| Consulting firm | Management consulting | 7.5% | Yes | unverified, earlier text not re-read |
| Advertising agency | Marketing services | 7.5% | Yes | unverified, earlier text not re-read |
| CITN-registered tax practitioner | Tax compliance | 7.5% | Yes | unverified, earlier text not re-read |

##### 3.9 Insurance

**Insurance suppliers**

| Supplier | Typical description | VAT rate | Input credit | Status |
| --- | --- | --- | --- | --- |
| AIICO Insurance | Business insurance | Exempt | No | unverified, earlier text not re-read |
| Leadway Assurance | Property, liability | Exempt | No | unverified, earlier text not re-read |
| AXA Mansard | Health, motor | Exempt | No | unverified, earlier text not re-read |
| Cornerstone Insurance | All lines | Exempt | No | unverified, earlier text not re-read |
| Stanbic IBTC Insurance | Life, annuity | Exempt | No | unverified, earlier text not re-read |

##### 3.10 Basic foodstuffs and exempt goods

**Basic foodstuffs and exempt goods suppliers**

| Supplier | Typical description | VAT rate | Input credit | Status |
| --- | --- | --- | --- | --- |
| Unprocessed agricultural produce (farm direct) | Rice, yam, vegetables: unprocessed | Exempt | No | unverified, earlier text not re-read |
| Processed food manufacturers (e.g., Nestle, Cadbury) | Processed packaged food | 7.5% | Yes | unverified, earlier text not re-read |
| Baby products (Pampers, etc.) | Diapers, formula | Exempt | No | unverified, earlier text not re-read |
| Pharmaceutical manufacturers | Medicines: registered with NAFDAC | Exempt | No | unverified, earlier text not re-read |
| Newspapers / educational textbooks | Print media, school books | Exempt | No | unverified, earlier text not re-read |

#### Section 4: Worked examples

##### Example 1: Standard VAT on consulting service

**Scenario:** Lagos-based IT firm issues invoice to Nigerian corporate client.

**Bank statement line (GTBank format):**
```
Date        : 15/04/2025
Narration   : CREDIT TRANSFER: ACME CORP LTD: INV-2025-041: IT CONSULTING
Amount      : +NGN 5,375,000.00
Balance     : NGN 25,375,000.00
```

**Working:**
- Invoice: net NGN 5,000,000 + VAT 7.5% NGN 375,000 = NGN 5,375,000
- Return entry: Line 1: NGN 5,000,000 | Output VAT: NGN 375,000

##### Example 2: Exempt basic food sale

**Scenario:** Agricultural trader sells unprocessed yams to market.

**Bank statement line (Zenith Bank format):**
```
Date        : 10/04/2025
Description : PAYMENT: ALABA MARKET TRADERS: FARM PRODUCE SUPPLY
Reference   : INV-AGR-2025-010
Amount      : +NGN 2,000,000.00
```

**Working:**
- Unprocessed agricultural produce: exempt from VAT
- Return entry: Line 4 (Exempt): NGN 2,000,000 | VAT: NGN 0
- No output VAT; no input credit on related purchases

##### Example 3: Electricity bill (business premises)

**Scenario:** Company pays EKEDC electricity bill for April 2025.

**Bank statement line (Access Bank format):**
```
Date        : 25/04/2025
Narration   : EKEDC BILL PAYMENT: APRIL 2025: ACCT: 0123456789
Amount      : -NGN 2,150,000.00
```

**Working:**
- EKEDC invoice: net NGN 2,000,000 + VAT 7.5% NGN 150,000 = NGN 2,150,000
- 100% business use (office premises)
- Return entry: Line 5 (Input VAT): NGN 150,000

##### Example 4: Reverse-charge on foreign digital service

**Scenario:** Company pays for Microsoft Azure (billed from Microsoft Ireland).

**Bank statement line (First Bank format):**
```
Date        : 05/04/2025
Narration   : INTL PAYMENT: MICROSOFT IRELAND: AZURE SERVICES APR 2025
Amount      : -NGN 11,200,000.00
```

**Working:**
- Foreign digital service to Nigerian business: self-assess VAT under FIRS guidance
- Self-assess: NGN 11,200,000 × 7.5/107.5 = NGN 781,395 VAT
- Declare as output AND claim as input: net zero for fully taxable business

##### Example 5: Export of software (zero-rated)

**Scenario:** Nigerian tech company exports software license to UK client.

**Bank statement line (UBA format):**
```
Date        : 20/04/2025
Narration   : SWIFT CREDIT: UK TECH LTD: SOFTWARE LICENSE Q1 2025
Amount      : +NGN 15,000,000.00 (USD 9,000)
```

**Working:**
- Export of service to non-resident: zero-rated
- Requires: contract, foreign bank transfer evidence, NXP form
- Return entry: Line 3 (Zero-rated): NGN 15,000,000 | VAT: NGN 0

##### Example 6: Monthly return summary

**Monthly return summary: Manufacturing company, April 2025**

| Item | Net (NGN) | VAT (NGN) | Status |
| --- | --- | --- | --- |
| Domestic taxable sales | 50,000,000 | 3,750,000 | unverified, earlier text not re-read |
| Export sales (0%) | 20,000,000 | 0 | unverified, earlier text not re-read |
| Exempt sales (basic food) | 10,000,000 | 0 | unverified, earlier text not re-read |
| Total Output | 80,000,000 | 3,750,000 | unverified, earlier text not re-read |
| Input on taxable purchases | 30,000,000 | 2,250,000 | unverified, earlier text not re-read |
| **Net VAT payable** |  | **1,500,000** | unverified, earlier text not re-read |

#### Section 5: Tier 1 rules (compressed)

##### Rate assignment

- **Rate assignment rules**: 7.5% standard: all goods and services not specifically exempt or zero-rated. 0%: exports of goods and services with proper documentation, diplomatic purchases, goods for humanitarian organisations. Exempt: basic unprocessed food items, medical/pharmaceutical products (NAFDAC-registered), baby products, financial services, insurance, educational materials (not stationery), newspapers, natural gas (domestic), exported services  _(unsure)_

##### Input credit

- **Input credit rules**: Credit allowed on VAT paid on purchases used for taxable activities. Must have valid VAT invoice from VAT-registered supplier (with their VRN). No credit on exempt purchases or purchases unrelated to taxable activities. No credit if supplier is below the NGN 25M registration threshold (they should not be charging VAT). Reverse-charge on foreign digital services: output and input net to zero for fully taxable businesses  _(unsure)_

##### Filing mechanics

- **Filing mechanics rules**: File VAT Form 002 monthly via FIRS TaxPro Max by 21st of following month. Also file WHT returns if subject to withholding: separate form. Excess input VAT carries forward; FIRS refunds are slow: expect 90+ days. Remit VAT collected from customers to FIRS monthly (not annual)  _(unsure)_

#### Section 6: Tier 2 catalogue (genuinely data-unknowable items)

**Tier 2 catalogue**

| Item | Why unknowable | What to ask | Status |
| --- | --- | --- | --- |
| Food product classification | Processed (7.5%) vs unprocessed/basic (exempt) depends on product detail | "Is this raw agricultural produce or processed/packaged food? NAFDAC registration?" | unverified, earlier text not re-read |
| Pharmaceutical exemption | Only NAFDAC-registered medicines exempt | "What is the product? Provide NAFDAC registration number." | unverified, earlier text not re-read |
| Export documentation | Zero-rate requires NXP form, shipping docs | "Provide export documentation: NXP form and freight evidence." | unverified, earlier text not re-read |
| Foreign digital service | B2B (reverse-charge) vs B2C | "Is the Nigerian entity VAT-registered? Does supplier have your TIN?" | unverified, earlier text not re-read |
| Real estate transaction | Land (exempt) vs building services (7.5%) | "Is this land only, or construction/building services?" | unverified, earlier text not re-read |
| Sub-NGN 25M supplier | Should not be charging VAT: no input credit | "Confirm supplier's annual turnover and VAT registration status." | unverified, earlier text not re-read |

#### Section 7: Excel working paper

**Columns:** Date | Supplier/Customer | VRN | Invoice No. | Net (NGN) | VAT Rate % | VAT (NGN) | In/Out | Zero-rated? | Exempt? | Tier 2 flag | Notes

**Tab structure:**
1. `Output_Sales`: all sales by type (taxable/zero-rated/exempt)
2. `Input_Purchases`: all purchases with VAT credit
3. `ReverseCharge_Foreign`: foreign services
4. `VAT_Summary`: monthly Form 002 totals
5. `Tier2_Items`: awaiting client response

#### Section 8: Bank statement reading guide

##### GTBank format

```
Date        : 15/04/2025
Narration   : CREDIT TRANSFER: COMPANY NAME: INV-2025-041: DESCRIPTION
Amount      : +NGN 5,375,000.00
Balance     : NGN 25,375,000.00
```

##### Zenith Bank format

```
15/04/2025  |  TRF FROM ACME CORP  |  +5,375,000.00  |  BAL: 25,375,000.00
```

##### Key patterns:

- **NGN number format:** Comma = thousands; period = decimal (NGN 5,375,000.00)
- **INTL PAYMENT / SWIFT:** Foreign payment: check for export zero-rate or reverse-charge
- **BILL PAYMENT:** Utility payments: usually include VAT; request invoice
- **CREDIT TRANSFER:** Domestic wire: match to issued invoice for output VAT

#### Section 9: Onboarding fallback

- **Onboarding fallback procedure when client cannot provide VAT invoices for all transactions**: 1. Use bank statement amounts as VAT-inclusive totals and back-calculate: Net = Total ÷ 1.075 | VAT = Total − Net 2. Apply conservative defaults: 7.5% output on all unverified taxable sales; 0% input credit without valid VRN invoice 3. Flag all items without VRN invoices in Tier2_Items tab 4. Issue data request listing missing invoice references 5. Warn client: FIRS can disallow input credit claims without valid VAT invoices from registered suppliers  _(unsure)_

#### Section 10: Reference material

**Reference material**

| Resource | Reference | Status |
| --- | --- | --- |
| FIRS TaxPro Max (filing portal) | https://taxpromax.firs.gov.ng | unverified, earlier text not re-read |
| FIRS main portal | https://www.firs.gov.ng | unverified, earlier text not re-read |
| VAT Act (as amended by Finance Act 2019/2020) | FIRS website: legislation | unverified, earlier text not re-read |
| Finance Act 2020: VAT rate increase to 7.5% | Official Gazette | unverified, earlier text not re-read |
| VAT registration threshold guidance | FIRS circular 2020 | unverified, earlier text not re-read |
| FIRS e-Invoice pilot | FIRS announcements: 2024 | unverified, earlier text not re-read |



## Sources

| Source | URL | Read on |
|---|---|---|
| Nigeria Tax Act 2025, Act No. 7, Official Gazette No. 117, 26 June 2025. UNOFFICIAL COPY hosted by Premium Times, not an official host. Sections read: ss.143 to 157, 185 to 188 | https://media.premiumtimesng.com/wp-content/files/2026/01/Final-Approved-Copy-for-Print-NIGERIA-TAX-ACT-2025.pdf | 2026-11-01 |
| NRS notice of 20 July 2026 on e-invoicing (read by an earlier pass; official) | https://www.nrs.gov.ng/ | 2026-11-01 |

NRS guides at https://www.nrs.gov.ng/taxpayer-services/tax-guides-and-manuals could not be read: a page shell loaded, then other NRS pages showed a CAPTCHA, so no cross-check was done.

Not yet confirmed: every NTA figure in this skill. Each comes from an unofficial press-hosted copy and was not confirmed in an official document, because nrs.gov.ng showed a CAPTCHA on 2026-11-01 and it was not touched. Also unconfirmed: all filing dates, forms, portals and penalties under the Nigeria Tax Administration Act 2025, whose text we did not open; the VAT registration threshold (no figure appears in the NTA text read); capital allowance rates for ordinary trades; and all earlier text in the pre-2026 section. Lost content restored: 0, nothing removed.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network — accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at
[openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Meet the accountants: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
