---
name: israel-vat
description: Use this skill whenever asked to prepare, review, or classify transactions for an Israel VAT (Ma'am, מע"מ) return or advise on Israeli VAT registration, filing, and reporting. Trigger on phrases like "prepare Ma'am return", "Israeli VAT", "מע"מ", "doch maam", or any Israel VAT request. ALWAYS read this skill before touching any Israel Ma'am-related work.
version: 2.2
jurisdiction: IL
tax_year: 2026
last_updated: 2026-11-14
depends_on:
  - vat-workflow-base
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: vat-gst
type: filing-howto
---

# Israel: VAT registration, transaction review and returns

## Scope

Prepare a documented Israeli Ma'am working paper for review by an Israel-licensed CPA. This covers ordinary dealers outside Eilat in 2026, not an authorization to file. Distinguish Osek Murshe, Osek Patur, financial institution and non-profit status before classifying supplies. The latest complete guidance read is the 2025 rights guide's VAT annex, explicitly updated for several January/June 2026 figures; other annual forms/extensions remain subject to current notices.

| Quick reference | Condition | Official source |
|---|---|---|
| Standard VAT | 18% from 1 January 2025, subject to place, liability and tax point | ITA Interpretation01/2025, https://www.gov.il/BlobFolder/policy/vat_11/he/vat_represent-info-051224-2.pdf |
| Osek Patur | Turnover across all businesses does not exceed NIS 122,833 in 2026; compulsory Murshe professions under registration reg.13 override turnover | VAT Law s.1 and rights guide reg.13 explanation, https://www.btl.gov.il/Laws1/00_0022_000000.pdf |
| Input-document time limit | Generally 6 months from lawful invoice, import declaration or approved document; statutory conditions apply | VAT Law s.38(a), https://www.btl.gov.il/Laws1/00_0022_000000.pdf |
| Invoice allocation | No input deduction for an invoice above NIS 10,000 before VAT from 1 January 2026, above NIS 5,000 from 1 June 2026, without the required allocation number | Rights guide VAT annex s.8; VAT Law ss.38/47, https://www.gov.il/BlobFolder/generalpage/income-tax-guide-knowyourright/he/Guides_IncomeTax_da-2025.pdf |

## Ask the client first

Obtain the registration certificate and taxpayer/Osek number, assigned reporting periods, all business bank statements, issued sales invoices/credit notes, suppliers' lawful tax invoices and registration status, prior return and assessment/credit position, customs import declarations in the dealer's name, export releases, service contracts and actual beneficiaries, tourist status/stay records, property leases and vehicle licences/use logs. Ask for foreign invoices, currency conversion evidence, fixed-asset records and mixed/private use. A bank narration or payment currency is evidence to match, not a tax classification.

## The method, step by step

### Establish registration, place and tax point

Register by business commencement; identify the correct status and any compulsory Murshe profession, including doctors, architects, technicians and bookkeepers under reg.13. A Patur is registered, generally exempt from periodic VAT payments/returns, but s.31(3) excludes its real-estate sales and specified equipment sales where input tax was deducted; review those before using the ordinary exemption. It cannot issue a tax invoice or deduct input VAT, and reports the preceding calendar year's turnover by 31 January. Seek reclassification if turnover exceeds the ceiling. Patur is not an income-tax exemption ([rights guide VAT annex](https://www.gov.il/BlobFolder/generalpage/income-tax-guide-knowyourright/he/Guides_IncomeTax_da-2025.pdf)).

A service is treated as supplied in Israel under s.15 where the supplier's business is in Israel, the recipient is a defined Israeli resident/entity, or it concerns Israeli property. Determine the statutory tax point rather than using bank date alone. Issued tax invoices must be included even if consideration has not arrived where the applicable reporting rule requires it. Do not assume every cash receipt is VAT-inclusive taxable turnover ([VAT Law ss.15, 22-29, 69](https://www.btl.gov.il/Laws1/00_0022_000000.pdf); rights guide VAT annex).

### Classify each supply

The standard rate, zero rating and exemption have different input-tax consequences. Under s.30(a)(1), goods exports, excluding s.33 goods, need a released export declaration or Director-approved document. Section 30(c) defines the relevant foreign resident as outside Israel with no business or activity in Israel. Under s.30(a)(5), a foreign customer does not establish zero rating if the contracted service is actually also supplied to an Israeli resident/entity; the customs-value exception refers to Customs Ordinance ss.129-133T and prescribed exclusions require review. Hotel accommodation of a statutory tourist falls under s.30(a)(8)(a), including only the prescribed incidental services. Regulation12 requires transaction price/payment method/currency recorded in the books, a written agreement or other document confirming details, and for tourist supplies the tourist's name, permanent address, passport number and an invoice detailing the service. Foreign payment or a passport copy alone does not prove all tourist/document conditions. International travel rights have s.30(a)(10), rather than a blanket rate for every airline bill ([VAT Law s.30](https://www.btl.gov.il/Laws1/00_0022_000000.pdf)).

Residential letting for no more than 25 years is exempt under s.31(1), except hotel accommodation; review actual residential use and tenant/entity circumstances. Do not label all financial, insurance, medical or educational suppliers exempt: the supplier's statutory registration and the particular supply matter. Private doctors can be compulsorily Murshe even below the turnover ceiling. Specific agricultural produce, Eilat, diamonds/precious metals and special schemes need their operative rules before use ([VAT Law s.31](https://www.btl.gov.il/Laws1/00_0022_000000.pdf); rights guide reg.13 explanation).

### Compute import VAT and foreign-service liability

For ordinary goods imports, s.11(a) uses the customs value under Customs Ordinance ss.129-134A plus customs duty and other applicable import taxes/levies, with the special s.11(b)/(c) cases separately checked. Use the accepted customs declaration, valuation and currency basis; this is import VAT paid through customs, not an automatic service reverse charge ([VAT Law s.11](https://www.btl.gov.il/Laws1/00_0022_000000.pdf)).

ITA's published Position 02/2016, reproduced in its 2024 positions list, explains that imported services with an Israeli consumption/property link are taxable under s.15(a). Under VAT reg.6D, the buyer pays unless it holds an invoice for the transaction. A foreign supplier's brand/local marketing name does not settle invoice issuer or liability. Input deduction is separately subject to ss.38/41 and is not allowed merely because output tax is self-assessed; the position specifically excludes deduction for service imports consumed in Eilat. Obtain CPA confirmation of invoice/self-invoicing mechanics and actual use before filing ([ITA position 02/2016](https://www.gov.il/BlobFolder/policy/tax-report-station-2024/he/IncomeTax_ReportStation_IncomeTax_ReportStation_2024_5.pdf)).

### Substantiate the input claim

Use a lawful tax invoice, import declaration or approved document in the dealer's name, within the statutory time limit and for taxable business supplies, including zero-rated supplies; exempt/private use does not qualify. Check required allocation numbers and credit-note adjustments. Section 38(a2) can deny input after the specified penalized cash-law violation unless the Director is satisfied lawful tax was paid. Sections 40/40A have a documented pre-registration setup exception, not a blanket pre-registration credit. Separate fixed-asset input VAT from other inputs ([VAT Law ss.38, 41, 43](https://www.btl.gov.il/Laws1/00_0022_000000.pdf)).

Private passenger-car purchase input VAT is generally blocked under reg.14, even for a salesperson. Regulation 14(b)(2)(a) separately permits qualifying vehicle-dealer inventory where the main business is vehicle sales and the car is unused/not intended for use except sale. Other exceptions require exclusive qualifying driving-school, vehicle-hire, passenger-transport or tour-business use. A commercial vehicle over 3,500 kg must also be outside the private/similar-fourth-schedule exclusion. Running costs differ: regulation 18 generally uses actual taxable-use proportion or the Director-determined ratio. Only where mixed use is indeterminate and the Director has not determined the ratio do the fallback fractions apply: 2/3 where mainly business, 1/4 where mainly non-business. Verify registration/use, not the invoice label. Regulation 15 blocks specified mixed residential-home purchase/build/service inputs; regulation 15A separately governs employee-benefit inputs; regulation 16 blocks hospitality except hospitality of a person from abroad. Home office, phones, entertainment and mixed property need their applicable block/exception conditions and evidence, not merely a guessed business percentage ([rights guide VAT annex s.8](https://www.gov.il/BlobFolder/generalpage/income-tax-guide-knowyourright/he/Guides_IncomeTax_da-2025.pdf)).

Under ss.45-47, distinguish the transaction invoice from a tax invoice. A Murshe may issue a tax invoice for a taxable supply and must do so on buyer request, subject to s.47(a1): where the tax point is receipt of payment, the buyer cannot demand it before payment of consideration or part. Section 46 generally requires invoice issue within 14 days of the tax point; apply the actual transaction/exception rules. These rights do not permit a Patur tax invoice.

### Build and reconcile the working paper

Use columns Date, Supplier/Customer, Osek number, Invoice number, Net ILS, Rate, VAT, In/Out, Zero-rated, Exempt, Unresolved and Notes/source. Keep Output_Sales, Input_Purchases, ReverseCharge_Foreign, MaamSummary and Tier2_Items tabs. Reconcile sales, exempt/zero-rated turnover, foreign-service output, admissible inputs and customs VAT to documents and the assigned period. Match prior credits to the authority account before deducting them; excess inputs require a refund return, not an unsupported automatic carryforward formula.

The old internal screening flags remain optional review priorities, **not legal thresholds**: single transaction NIS 100,000, tax delta NIS 17,000, counterparty concentration above 40%, more than 4 unresolved defaults, and absolute net position NIS 250,000. Do not turn a missing classification into the old defaults of 18% output, exempt residential rent, or 0% credit as a final conclusion. Missing input evidence means no supported claim yet; missing output classification means an unresolved filing item.

## Worked cases

### Consulting invoice and a documented import

Retain TECH SOLUTIONS LTD's old NIS 236,000 receipt, invoice 041/2025 dated 15 April 2025: assuming an ordinary taxable consulting supply, net NIS 200,000 plus VAT NIS 36,000. Interpretation01/2025 confirms 18% for tax points from 1 January 2025; the historical case still requires its actual supply/tax-point facts. For the old Germany electronics import through Ben Gurion dated 10 April 2025, assume the accepted customs value is NIS 400,000 and actual duty NIS 112,000, no other import tax/levy or special valuation case: import base NIS 512,000 and VAT NIS 92,160. The duty is an assumed assessment, **not a verified tariff rate**. The old Bank Leumi line/ASYCUDA REF 2025-04-1234 is matching evidence, not proof of input eligibility. Claim only with the qualifying import document and taxable use.

```oa-check
name: Consulting invoice and assessed customs base
inputs:
  consulting_net: 200000
  customs_value: 400000
  assessed_duty: 112000
steps:
  - consulting_vat: consulting_net*0.18
  - receipt: consulting_net+consulting_vat
  - import_base: customs_value+assessed_duty
  - import_vat: import_base*0.18
expected:
  consulting_vat: 36000
  receipt: 236000
  import_base: 512000
  import_vat: 92160
```

### Hotel, foreign software and passenger car

Retain HOTEL BOOKING, FOREIGN GUEST, BOOKING REF TL-2025-0418, 18 April 2025: NIS 7,650 (old USD 2,100 narration). Conditional on statutory tourist hotel accommodation and all documents, output VAT is zero. The narration/currency does not establish that condition, and Form 1345 concerns reportable opinions, not tourism documentation.

Retain GOOGLE IRELAND LTD, WORKSPACE SUBSCRIPTION APR 2025, 5 April 2025: NIS 5,865 (old USD 1,600 narration). If the imported-service buyer liability applies, VAT is NIS 5,865 x 18% = NIS 1,055.70, not a gross-price extraction. Only a fully eligible taxable use/document claim offsets the same amount as input. Neither USD illustration supplies a verified exchange rate.

Retain CHAMPION MOTORS LTD, invoice 2025-V-041, 3 April 2025: salesperson's private car net NIS 150,000, VAT NIS 27,000, gross NIS 177,000. On the stated facts with no qualifying reg.14 exception, purchase credit is zero, regardless of business sales use. Running costs require their separate test.

```oa-check
name: Foreign service both sides and blocked private car
inputs:
  foreign_service: 5865
  car_net: 150000
steps:
  - reverse_output: foreign_service*0.18
  - eligible_service_input: reverse_output
  - service_net_vat: reverse_output-eligible_service_input
  - car_vat: car_net*0.18
  - car_gross: car_net+car_vat
  - car_input_allowed: 0
expected:
  reverse_output: 1055.70
  service_net_vat: 0
  car_vat: 27000
  car_gross: 177000
  car_input_allowed: 0
```

### Period return with foreign services on both sides

Assume the dealer's assigned period is bimonthly; all input conditions, export evidence and service-import liability are satisfied. Domestic software net NIS 800,000 gives NIS 144,000 output, exports NIS 300,000 give zero, foreign cloud net NIS 30,000 gives NIS 5,400 output. Hardware net NIS 200,000 gives NIS 36,000 input, office rent NIS 50,000 gives NIS 9,000, cloud gives NIS 5,400. Total output NIS 149,400, input NIS 50,400, payable NIS 99,000. Service-import consideration is not sales turnover; the old NIS 1,130,000 mixed total must not be reported as customer sales. No prior credit is assumed. Omitting reverse output would understate liability by NIS 5,400.

```oa-check
name: Return reconciliation with paired reverse charge
inputs:
  domestic_sales: 800000
  exports: 300000
  foreign_service: 30000
  hardware: 200000
  office_rent: 50000
steps:
  - sales_turnover: domestic_sales+exports
  - output: (domestic_sales+foreign_service)*0.18
  - input: (hardware+office_rent+foreign_service)*0.18
  - payable: output-input
expected:
  sales_turnover: 1100000
  output: 149400
  input: 50400
  payable: 99000
```

## When to refuse or refer

Escalate mixed exempt/taxable allocations, real estate VAT, group registration, Eilat, diamonds/precious metals, long-term contracts/construction, retrospective Patur-to-Murshe registration, uncertain imported services, tourist status/documents and any unsupported rate or credit. Mas Rechisha is a separate purchase tax; do not use its name as a VAT provision. Obtain all material evidence and an Israeli CPA's review before filing.

## Filing and payment

Use the authority-assigned monthly/bimonthly cycle, not an inferred frequency. The guide gives the determining-year turnover figure NIS 1,775,000 as at 1 January 2026, but the recovered text renders both frequency branches monthly; the low-turnover branch remains unresolved. The guide's baseline is within 15 days after period end; online payment is permitted through the 19th and detailed reporting/payment through the 23rd under its specified route. Check live extensions, holidays, registration and detailed-reporting duty before calendaring. File zero and refund returns on time too ([rights guide VAT annex s.9](https://www.gov.il/BlobFolder/generalpage/income-tax-guide-knowyourright/he/Guides_IncomeTax_da-2025.pdf)).

In the Tax Authority personal/Shaam service, select the assigned period, enter reconciled sales/output and separated input categories, validate and obtain approval, submit and retain receipt, then confirm payment separately. Filing codes PCN83/PCN874 are not verified here. Excess-input refunds are subject to VAT Law s.39 review/investigation and compliance conditions; do not promise exporter refund timing from a generic estimate.

## Completion checklist

Confirm status, period and tax point; match every bank line to invoices; check invoice issuer, allocation number and lawful document; verify place/rate/zero-rating conditions; separate taxable/exempt/private use and fixed assets; reconcile import and service-import tax; resolve prior credits, complete CPA review and retain return/payment acknowledgments.

## Sources

| Source | URL | Read on |
|---|---|---|
| Consolidated VAT Law; Read for ss.7, 11 price/import base, 15 place, 30 exports/foreign services/tourists/travel, 31 residential letting, 38/41 input conditions, 43 adjustment and 45-47 invoices, 39 refund conditions | https://www.btl.gov.il/Laws1/00_0022_000000.pdf | 2026-11-14 |
| Official VAT General Regulations; Read for regs.6D imported services, 14 car/dealer exceptions, 15/15A/16 home/employee/hospitality blocks and 18 mixed-use proportion/fallback conditions | https://www.btl.gov.il/Laws1/02_0022_100000.pdf | 2026-11-14 |
| Official VAT Registration Regulations; Read for regs.2/13 registration and compulsory Murshe professions | https://www.btl.gov.il/Laws1/02_0022_100001.pdf | 2026-11-14 |
| ITA Interpretation01/2025; Read for introduction giving standard18% on Israeli transactions and goods imports with tax point from1January2025 under the2024 amending order | https://www.gov.il/BlobFolder/policy/vat_11/he/vat_represent-info-051224-2.pdf | 2026-11-14 |
| ITA 2025 rights guide, 2025-2026 filing cycle; Read for VAT annex registration/Patur/reg.13, invoice fields and Form1345 reportable-opinion purpose, input limits/allocation numbers, regs.14/18 vehicles, periodic/zero/refund returns and 15/19/23-day routes; guide expressly labels January/June 2026 figures | https://www.gov.il/BlobFolder/generalpage/income-tax-guide-knowyourright/he/Guides_IncomeTax_da-2025.pdf | 2026-11-14 |
| ITA 2024 reportable positions list; Read for Position 02/2016 service imports, reg.6D buyer liability/invoice exception and separate ss.38/41 input conditions, Eilat exclusion | https://www.gov.il/BlobFolder/policy/tax-report-station-2024/he/IncomeTax_ReportStation_IncomeTax_ReportStation_2024_5.pdf | 2026-11-14 |

Not yet confirmed: low-turnover frequency branch at NIS 1,775,000 from the recovered guide; all live extensions, new-business automatic monthly filing, exporter refund timing, PCN83/PCN874, the old NIS 305 invoice cutoff, tourist document checklist and all tourism ancillary-service conditions, agricultural/Eilat/special-scheme details, entertainment/private-expense blocks and the brand-based classifications below. The old unknown-sale 18%, financial-as-professional, residential-as-exempt defaults and blanket bank gross-up are withdrawn as filing instructions. A gross/1.18 calculation is only a provisional arithmetic estimate after independently establishing an 18% VAT-inclusive amount; it cannot create a lawful input invoice.

### Bank-document matching cues retained from the earlier version

These illustrative layouts do not establish tax treatment or authority approval. Preserve the distinction between credit/inflow and debit/outflow, foreign currency and customs/VAT payments.

### Bank Hapoalim format

```
תאריך    : 15/04/2025
סוג פעולה: זיכוי - העברה בנקאית
תיאור    : TECH SOLUTIONS - חשבונית 041/2025
סכום     : +236,000 ₪
יתרה     : 1,236,000 ₪
```
Fields: תאריך (date) | סוג פעולה (transaction type) | תיאור (description) | סכום (amount, ILS)

### Bank Leumi format

```
15.04.2025  |  זיכוי  |  TECH SOLUTIONS  |  +236,000.00  |  יתרה: 1,236,000.00
```

### Key patterns:

- **ILS number format:** Comma = thousands separator; period = decimal (ILS 236,000.00)
- **זיכוי (credit):** Money in: match to issued Heshbonit Mase
- **חיוב (debit):** Money out: match to received Heshbonit Mase for input credit
- **מטבע חוץ (foreign currency):** Foreign payment: check for zero-rated export or reverse-charge
- **מכס ומע"מ:** Customs and Ma'am: import duty + import Ma'am payment



### Legacy supplier matching library: unresolved treatments

Every old supplier/description and proposed treatment below is retained for traceability, **not usable rate or input-credit guidance**. Apply the operative rules above to the actual invoice, supplier status, transaction and use. This boundary includes all banks/payment apps, utilities, telecoms, travel, logistics, retail, software, professionals, insurers and healthcare. A row saying “Yes” does not authorize a credit; a row saying “Exempt” does not establish exemption.

### Banking and financial services

**Banking and financial services suppliers**

- Bank Hapoalim (בנק הפועלים); Bank fees, wire charges. Old unconfirmed proposal: unverified: Exempt; input credit No.
- Bank Leumi (בנק לאומי); Account maintenance, loans. Old unconfirmed proposal: unverified: Exempt; input credit No.
- Mizrahi Tefahot (מזרחי טפחות); Mortgage, business banking. Old unconfirmed proposal: unverified: Exempt; input credit No.
- Discount Bank (בנק דיסקונט); Commercial banking fees. Old unconfirmed proposal: unverified: Exempt; input credit No.
- Bank Otsar HaHayal (אוצר החייל); Military banking. Old unconfirmed proposal: unverified: Exempt; input credit No.
- Bit (ביט: Hapoalim app); P2P payment transfer. Old unconfirmed proposal: unverified: Exempt; input credit No.
- PayBox (פייבוקס: Leumi); P2P digital wallet. Old unconfirmed proposal: unverified: Exempt; input credit No.
- Pelecard / Creditguard; Payment processing. Old unconfirmed proposal: unverified: 18%; input credit Yes.
- Tranzila; E-commerce payment gateway. Old unconfirmed proposal: unverified: 18%; input credit Yes.

### 3.2 Electricity and utilities

**Electricity and utilities suppliers**

- Israel Electric Corporation (חברת החשמל: IEC); Electricity. Old unconfirmed proposal: unverified: 18%; input credit Yes (business).
- Mekorot (מקורות); Water supply wholesale. Old unconfirmed proposal: unverified: 18%; input credit Yes.
- Local municipality water (ועדה מקומית); Water: municipal. Old unconfirmed proposal: unverified: 18%; input credit Yes.
- Paz Gas / Supergas; Gas: cooking/heating. Old unconfirmed proposal: unverified: 18%; input credit Yes.
- Cellcom Energy; Green electricity supply. Old unconfirmed proposal: unverified: 18%; input credit Yes.

### 3.3 Telecommunications

**Telecommunications suppliers**

- Cellcom (סלקום); Mobile, broadband. Old unconfirmed proposal: unverified: 18%; input credit Yes (business use).
- Partner Communications (פרטנר); Mobile, fiber, TV. Old unconfirmed proposal: unverified: 18%; input credit Yes (business use).
- Bezeq (בזק); Fixed line, DSL internet. Old unconfirmed proposal: unverified: 18%; input credit Yes (business use).
- HOT (הוט); Cable TV, internet, phone. Old unconfirmed proposal: unverified: 18%; input credit Yes (business use).
- 012 Mobile / 013 Netvision; MVNO, internet. Old unconfirmed proposal: unverified: 18%; input credit Yes.
- Golan Telecom (גולן טלקום); Discount mobile. Old unconfirmed proposal: unverified: 18%; input credit Yes.

### 3.4 Transport and travel

**Transport and travel suppliers**

- El Al (אל על); Domestic flights (Eilat). Old unconfirmed proposal: unverified: 18%; input credit Yes.
- El Al; International flights. Old unconfirmed proposal: unverified: 0%; input credit No input credit applicable.
- Arkia; Domestic flights. Old unconfirmed proposal: unverified: 18%; input credit Yes.
- Israir; Domestic flights. Old unconfirmed proposal: unverified: 18%; input credit Yes.
- Israel Railways (רכבת ישראל); Train tickets. Old unconfirmed proposal: unverified: 18%; input credit Yes.
- Egged (אגד); Bus: intercity. Old unconfirmed proposal: unverified: 18%; input credit Yes.
- Dan (דן); Bus: Tel Aviv metro. Old unconfirmed proposal: unverified: 18%; input credit Yes.
- Gett (גט); Taxi app. Old unconfirmed proposal: unverified: 18%; input credit Yes (business use).
- Yango; Ride-hailing. Old unconfirmed proposal: unverified: 18%; input credit Yes (business use).

### 3.5 Logistics and postal

**Logistics and postal suppliers**

- Israel Post (דואר ישראל); Domestic mail, parcels. Old unconfirmed proposal: unverified: 18%; input credit Yes.
- DHL Israel; International courier. Old unconfirmed proposal: unverified: 0% (export) / 18% (domestic); input credit Yes.
- UPS Israel; International courier. Old unconfirmed proposal: unverified: 0% / 18%; input credit Yes.
- FedEx Israel; International courier. Old unconfirmed proposal: unverified: 0% / 18%; input credit Yes.
- Ashot Logistics; Domestic delivery. Old unconfirmed proposal: unverified: 18%; input credit Yes.

### 3.6 Retail and office supplies

**Retail and office supplies suppliers**

- Shufersal (שופרסל); Supermarket: food/non-food. Old unconfirmed proposal: unverified: 18% (food not zero-rated in IL); input credit Yes (business).
- Rami Levy (רמי לוי); Discount supermarket. Old unconfirmed proposal: unverified: 18%; input credit Yes.
- Office Depot Israel; Office supplies. Old unconfirmed proposal: unverified: 18%; input credit Yes.
- KSP (כ.ס.פ); Electronics. Old unconfirmed proposal: unverified: 18%; input credit Yes.
- SuperPharm; Pharmacy: medicines. Old unconfirmed proposal: unverified: 18% (medicines not zero-rated in IL); input credit Yes.
- Factory 54 / Castro; Clothing. Old unconfirmed proposal: unverified: 18%; input credit Yes.

### 3.7 Software and digital services

**Software and digital services suppliers**

- Priority Software (פריוריטי); Israeli ERP. Old unconfirmed proposal: unverified: 18%; input credit Yes.
- Greeninvoice (חשבונית ירוקה); Cloud invoicing platform. Old unconfirmed proposal: unverified: 18%; input credit Yes.
- Hashavshevet (חשבשבת); Accounting software. Old unconfirmed proposal: unverified: 18%; input credit Yes.
- iCount; Cloud accounting. Old unconfirmed proposal: unverified: 18%; input credit Yes.
- Microsoft Israel (Azure, M365); Cloud services: B2B. Old unconfirmed proposal: unverified: 18% (buyer reverse-charge); input credit Yes.
- Google Workspace IL; Cloud: B2B. Old unconfirmed proposal: unverified: 18% (buyer reverse-charge); input credit Yes.
- Salesforce Israel; CRM: B2B. Old unconfirmed proposal: unverified: 18% (buyer reverse-charge); input credit Yes.
- AWS Israel; Cloud infrastructure: B2B. Old unconfirmed proposal: unverified: 18% (buyer reverse-charge); input credit Yes.

### 3.8 Professional services

**Professional services suppliers**

- Roeh Heshbon (רואה חשבון: CPA); Accounting, audit. Old unconfirmed proposal: unverified: 18%; input credit Yes.
- Orech Din (עורך דין: lawyer); Legal services. Old unconfirmed proposal: unverified: 18%; input credit Yes.
- Munahel Ishur (מנהל אישור: notary equivalent); Document certification. Old unconfirmed proposal: unverified: 18%; input credit Yes.
- Reklam / marketing agency; Advertising, PR. Old unconfirmed proposal: unverified: 18%; input credit Yes.
- Building contractor (קבלן); Construction services. Old unconfirmed proposal: unverified: 18%; input credit Yes.

### 3.9 Insurance

**Insurance suppliers**

- Harel Insurance (הראל); Business insurance. Old unconfirmed proposal: unverified: Exempt; input credit No.
- Menora Mivtachim (מנורה מבטחים); Property, liability. Old unconfirmed proposal: unverified: Exempt; input credit No.
- Clal Insurance (כלל ביטוח); Vehicle, business. Old unconfirmed proposal: unverified: Exempt; input credit No.
- AIG Israel; Professional indemnity. Old unconfirmed proposal: unverified: Exempt; input credit No.

### 3.10 Healthcare

**Healthcare suppliers**

- Clalit (כללית); Health fund / Kupat Holim. Old unconfirmed proposal: unverified: Exempt; input credit No.
- Maccabi (מכבי); Health fund. Old unconfirmed proposal: unverified: Exempt; input credit No.
- Meuhedet (מאוחדת); Health fund. Old unconfirmed proposal: unverified: Exempt; input credit No.
- Private clinic / specialist; Private medical. Old unconfirmed proposal: unverified: Exempt; input credit No.
