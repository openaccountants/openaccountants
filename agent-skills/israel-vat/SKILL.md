---
name: israel-vat
description: "Use this skill whenever asked to prepare, review, or classify transactions for an Israel VAT (Ma'am, מע\"מ) return or advise on Israeli VAT registration, filing, and reporting. Trigger on phrases like \"prepare Ma'am return\", \"Israeli VAT\", \"מע\"מ\", \"doch maam\", or any Israel VAT request. ALWAYS read this skill before touching any Israel Ma'am-related work."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/israel-vat"
  jurisdiction: "IL"
  tax_year: "2026"
  last_updated: "2026-11-03"
---

# Israel VAT

## Section 1: Quick reference

**Quick reference**

| Field | Value | Source |
| --- | --- | --- |
| Country | Israel (מדינת ישראל) | |
| Tax | Ma'am (מס ערך מוסף: Value Added Tax) | |
| Currency | ILS (Israeli New Shekel: ₪) | |
| Standard rate | 18% as at January 2026 (was 17% before 1 January 2025) | https://www.gov.il/BlobFolder/generalpage/income-tax-guide-knowyourright/he/Guides_IncomeTax_da-2025.pdf (PDF p.140: "as at January 2026 the VAT rate is 18%") |
| Reduced rate | unverified: 0% on exports, specific agricultural produce, tourism services to non-residents | unverified |
| Exempt | unverified: financial services, insurance, residential rent (if not commercial), medical services | unverified |
| Exempt dealer (Osek Patur) ceiling | ILS 122,833 expected annual turnover as at January 2026, updated once a year; below this a dealer can be classed "Osek Patur". Some professions (for example doctors, architects, bookkeepers, VAT Registration Regulations reg. 13) must register as Osek Murshe whatever the turnover | https://www.gov.il/BlobFolder/generalpage/income-tax-guide-knowyourright/he/Guides_IncomeTax_da-2025.pdf (PDF pp.139-140, VAT annex s.4) |
| Small business | Osek Murshe (עוסק מורשה): registered dealer filing periodic returns | |
| Tax authority | Israel Tax Authority (ITA: רשות המיסים בישראל) | |
| Filing portal | Shaam Online: https://www.misim.gov.il | |
| Return form | unverified: Doch Ma'am (דוח מע"מ: Form PCN83 / PCN874) | unverified |
| Filing frequency | Two-monthly if turnover in the determining year is up to ILS 1,775,000; monthly above ILS 1,775,000 (amount as at 1 January 2026, updated once a year) | https://www.gov.il/BlobFolder/generalpage/income-tax-guide-knowyourright/he/Guides_IncomeTax_da-2025.pdf (PDF p.141, VAT annex s.9) |
| Deadline | Within 15 days after the end of the reporting period | https://www.gov.il/BlobFolder/generalpage/income-tax-guide-knowyourright/he/Guides_IncomeTax_da-2025.pdf (PDF p.141, VAT annex s.9) |
| Tax invoices | A registered dealer may issue a Heshbonit Mase (חשבונית מס) and must do so when the customer asks. unverified: the ILS 305 figure in earlier versions | https://www.gov.il/BlobFolder/generalpage/income-tax-guide-knowyourright/he/Guides_IncomeTax_da-2025.pdf (PDF p.140, VAT annex s.7); ILS 305 unverified |
| Contributor | Open Accountants Community | |
| Validated by | Pending: requires sign-off by Israel-licensed CPA (רואה חשבון) | |
| Skill version | 2.1 | |

### Key return form fields

**Key return form fields**

| Field | Meaning |
| --- | --- |
| Iska (עסקה) | Output tax base: taxable supplies at 18% |
| Yetsia (יציאה) | Exports / zero-rated supplies |
| Pator (פטור) | Exempt supplies |
| Totchaot (תשומות) | Input tax on purchases |
| Maam Letashlum (מע"מ לתשלום) | Net Ma'am payable (Output − Input) |
| Yiteret Totchaot (יתרת תשומות) | Excess input tax carried forward |
| Mechira LeZar (מכירה לזר) | Sale to foreign resident (zero-rated tourism) |

### Conservative defaults

**Conservative defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown rate on a sale | 18% standard |
| Unknown whether export documentation complete | Treat as domestic 18% |
| Unknown business-use % (vehicle, phone, home) | 0% input credit |
| Unknown whether Heshbonit Mase issued | No input credit until confirmed |
| Financial service vs professional service | Treat as professional: 18% |
| Residential rent vs commercial | Treat as exempt until lease reviewed |
| Foreign digital service (B2B) | unverified: buyer self-assesses under reverse charge (see Example 4) |

### Red flag thresholds

**Red flag thresholds**

| Threshold | Value |
| --- | --- |
| HIGH single transaction | ILS 100,000 |
| HIGH tax delta on single conservative default | ILS 17,000 |
| MEDIUM counterparty concentration | >40% of output or input |
| MEDIUM conservative default count | >4 per return |
| LOW absolute net Ma'am position | ILS 250,000 |

## Section 2: Required inputs and refusal catalogue

### Required inputs

- **Required inputs before starting Israel Ma'am work**: 1. Osek number (מספר עוסק: 9-digit taxpayer ID) and registration certificate 2. Bimonthly bank statements in ILS (all business accounts) 3. Heshbonit Mase (tax invoices) from all suppliers: must include supplier's Osek number 4. Sales invoices issued (Heshbonit Mase or Heshbonit Kala for amounts below ILS 305) 5. Prior period Doch Ma'am (for carried-forward excess input credit) 6. Import documents from Customs (ASYCUDA / import declarations) for imported goods 7. Details of zero-rated tourism transactions (passports, foreign payment evidence)

### Refusal catalogue

- **Items requiring escalation to licensed CPA**: Refuse and escalate to a licensed CPA (רואה חשבון) for: - Partial exemption (Alut Yechusit: עלות יחסית): businesses with mixed exempt/taxable - Real estate Ma'am transactions (Mas Rechisha: complex exemptions on property) - Ma'am group registration (Kvutzat Osek: עוסק קבוצה) - Designated area supplies (Eilat free zone: zero-rated) - Diamond and precious metal special scheme - Ma'am on long-term contracts and construction - Retroactive registration for Osek Patur transitioning to Osek Murshe

## Section 3: Supplier pattern library

unverified: every row in this section. A supplier's name does not settle the legal treatment of a supply; the 18% figure is the standard rate as at January 2026 (rights guide, PDF p.140), but whether a given supply is exempt, zero-rated or under a reverse charge was not checked against the law for any row. Classify each supply on its facts.

### 3.1 Banking and financial services

**Banking and financial services suppliers**

| Supplier | Typical description | Ma'am rate | Input credit |
| --- | --- | --- | --- |
| Bank Hapoalim (בנק הפועלים) | Bank fees, wire charges | unverified: Exempt | No |
| Bank Leumi (בנק לאומי) | Account maintenance, loans | unverified: Exempt | No |
| Mizrahi Tefahot (מזרחי טפחות) | Mortgage, business banking | unverified: Exempt | No |
| Discount Bank (בנק דיסקונט) | Commercial banking fees | unverified: Exempt | No |
| Bank Otsar HaHayal (אוצר החייל) | Military banking | unverified: Exempt | No |
| Bit (ביט: Hapoalim app) | P2P payment transfer | unverified: Exempt | No |
| PayBox (פייבוקס: Leumi) | P2P digital wallet | unverified: Exempt | No |
| Pelecard / Creditguard | Payment processing | unverified: 18% | Yes |
| Tranzila | E-commerce payment gateway | unverified: 18% | Yes |

### 3.2 Electricity and utilities

**Electricity and utilities suppliers**

| Supplier | Typical description | Ma'am rate | Input credit |
| --- | --- | --- | --- |
| Israel Electric Corporation (חברת החשמל: IEC) | Electricity | unverified: 18% | Yes (business) |
| Mekorot (מקורות) | Water supply wholesale | unverified: 18% | Yes |
| Local municipality water (ועדה מקומית) | Water: municipal | unverified: 18% | Yes |
| Paz Gas / Supergas | Gas: cooking/heating | unverified: 18% | Yes |
| Cellcom Energy | Green electricity supply | unverified: 18% | Yes |

### 3.3 Telecommunications

**Telecommunications suppliers**

| Supplier | Typical description | Ma'am rate | Input credit |
| --- | --- | --- | --- |
| Cellcom (סלקום) | Mobile, broadband | unverified: 18% | Yes (business use) |
| Partner Communications (פרטנר) | Mobile, fiber, TV | unverified: 18% | Yes (business use) |
| Bezeq (בזק) | Fixed line, DSL internet | unverified: 18% | Yes (business use) |
| HOT (הוט) | Cable TV, internet, phone | unverified: 18% | Yes (business use) |
| 012 Mobile / 013 Netvision | MVNO, internet | unverified: 18% | Yes |
| Golan Telecom (גולן טלקום) | Discount mobile | unverified: 18% | Yes |

### 3.4 Transport and travel

**Transport and travel suppliers**

| Supplier | Typical description | Ma'am rate | Input credit |
| --- | --- | --- | --- |
| El Al (אל על) | Domestic flights (Eilat) | unverified: 18% | Yes |
| El Al | International flights | unverified: 0% | No input credit applicable |
| Arkia | Domestic flights | unverified: 18% | Yes |
| Israir | Domestic flights | unverified: 18% | Yes |
| Israel Railways (רכבת ישראל) | Train tickets | unverified: 18% | Yes |
| Egged (אגד) | Bus: intercity | unverified: 18% | Yes |
| Dan (דן) | Bus: Tel Aviv metro | unverified: 18% | Yes |
| Gett (גט) | Taxi app | unverified: 18% | Yes (business use) |
| Yango | Ride-hailing | unverified: 18% | Yes (business use) |

### 3.5 Logistics and postal

**Logistics and postal suppliers**

| Supplier | Typical description | Ma'am rate | Input credit |
| --- | --- | --- | --- |
| Israel Post (דואר ישראל) | Domestic mail, parcels | unverified: 18% | Yes |
| DHL Israel | International courier | unverified: 0% (export) / 18% (domestic) | Yes |
| UPS Israel | International courier | unverified: 0% / 18% | Yes |
| FedEx Israel | International courier | unverified: 0% / 18% | Yes |
| Ashot Logistics | Domestic delivery | unverified: 18% | Yes |

### 3.6 Retail and office supplies

**Retail and office supplies suppliers**

| Supplier | Typical description | Ma'am rate | Input credit |
| --- | --- | --- | --- |
| Shufersal (שופרסל) | Supermarket: food/non-food | unverified: 18% (food not zero-rated in IL) | Yes (business) |
| Rami Levy (רמי לוי) | Discount supermarket | unverified: 18% | Yes |
| Office Depot Israel | Office supplies | unverified: 18% | Yes |
| KSP (כ.ס.פ) | Electronics | unverified: 18% | Yes |
| SuperPharm | Pharmacy: medicines | unverified: 18% (medicines not zero-rated in IL) | Yes |
| Factory 54 / Castro | Clothing | unverified: 18% | Yes |

### 3.7 Software and digital services

**Software and digital services suppliers**

| Supplier | Typical description | Ma'am rate | Input credit |
| --- | --- | --- | --- |
| Priority Software (פריוריטי) | Israeli ERP | unverified: 18% | Yes |
| Greeninvoice (חשבונית ירוקה) | Cloud invoicing platform | unverified: 18% | Yes |
| Hashavshevet (חשבשבת) | Accounting software | unverified: 18% | Yes |
| iCount | Cloud accounting | unverified: 18% | Yes |
| Microsoft Israel (Azure, M365) | Cloud services: B2B | unverified: 18% (buyer reverse-charge) | Yes |
| Google Workspace IL | Cloud: B2B | unverified: 18% (buyer reverse-charge) | Yes |
| Salesforce Israel | CRM: B2B | unverified: 18% (buyer reverse-charge) | Yes |
| AWS Israel | Cloud infrastructure: B2B | unverified: 18% (buyer reverse-charge) | Yes |

### 3.8 Professional services

**Professional services suppliers**

| Supplier | Typical description | Ma'am rate | Input credit |
| --- | --- | --- | --- |
| Roeh Heshbon (רואה חשבון: CPA) | Accounting, audit | unverified: 18% | Yes |
| Orech Din (עורך דין: lawyer) | Legal services | unverified: 18% | Yes |
| Munahel Ishur (מנהל אישור: notary equivalent) | Document certification | unverified: 18% | Yes |
| Reklam / marketing agency | Advertising, PR | unverified: 18% | Yes |
| Building contractor (קבלן) | Construction services | unverified: 18% | Yes |

### 3.9 Insurance

**Insurance suppliers**

| Supplier | Typical description | Ma'am rate | Input credit |
| --- | --- | --- | --- |
| Harel Insurance (הראל) | Business insurance | unverified: Exempt | No |
| Menora Mivtachim (מנורה מבטחים) | Property, liability | unverified: Exempt | No |
| Clal Insurance (כלל ביטוח) | Vehicle, business | unverified: Exempt | No |
| AIG Israel | Professional indemnity | unverified: Exempt | No |

### 3.10 Healthcare

**Healthcare suppliers**

| Supplier | Typical description | Ma'am rate | Input credit |
| --- | --- | --- | --- |
| Clalit (כללית) | Health fund / Kupat Holim | unverified: Exempt | No |
| Maccabi (מכבי) | Health fund | unverified: Exempt | No |
| Meuhedet (מאוחדת) | Health fund | unverified: Exempt | No |
| Private clinic / specialist | Private medical | unverified: Exempt | No |

## Section 4: Worked examples

### Example 1: Standard Ma'am on consulting fee

**Scenario:** Tel Aviv software consulting firm issues Heshbonit Mase to Israeli corporate client.

**Bank statement line (Bank Hapoalim format):**
```
תאריך    : 15/04/2025
סוג פעולה: זיכוי - העברה בנקאית
תיאור    : TECH SOLUTIONS LTD - חשבונית 041/2025 - שכ"ט ייעוץ
סכום     : +236,000 ₪
```

**Working:**
- Heshbonit Mase: net ILS 200,000 + Ma'am 18% ILS 36,000 = ILS 236,000
- Return entry: Output Iska: ILS 200,000 | Output Ma'am: ILS 36,000

### Example 2: Import of goods (reverse-charge customs)

**Scenario:** Company imports electronics from Germany: customs clears at Ben Gurion.

**Bank statement line (Bank Leumi format):**
```
תאריך    : 10/04/2025
פעולה    : שוברי רכש - פרעון / מכס ומע"מ
תיאור    : תשלום מכס ומע"מ יבוא: ASYCUDA REF 2025-04-1234
סכום     : -92,160 ₪
```

**Working:**
- unverified: the import VAT base (CIF value plus duty). Import customs document: CIF value ILS 400,000 + customs duty ILS 112,000 = ILS 512,000 × 18% = ILS 92,160 Ma'am
- Pay at port of entry: then claim as input tax in Doch Ma'am filing
- Return entry: Input Totchaot: ILS 512,000; Input Ma'am: ILS 92,160

### Example 3: Zero-rated tourism service

**Scenario:** Hotel provides accommodation to foreign tourist paying in USD.

**Bank statement line (Mizrahi Tefahot format):**
```
תאריך    : 18/04/2025
סוג      : זיכוי מטבע חוץ
תיאור    : HOTEL BOOKING - FOREIGN GUEST - BOOKING REF TL-2025-0418
סכום     : +7,650 ₪ (USD 2,100)
```

**Working:**
- Foreign tourist: payment in foreign currency: qualifies as zero-rated tourist service
- unverified: the zero rate for this service and its documents (passport copy, foreign payment evidence, ITA Form 1345)
- Return entry: Mechira LeZar: ILS 7,650 | Ma'am: ILS 0

### Example 4: Reverse-charge on foreign digital service

**Scenario:** Company pays for Google Workspace (billed from Google Ireland).

**Bank statement line (Discount Bank format):**
```
תאריך    : 05/04/2025
פעולה    : חיוב: שירות בנקאי חו"ל
תיאור    : GOOGLE IRELAND LTD: WORKSPACE SUBSCRIPTION APR 2025
סכום     : -5,865 ₪ (USD 1,600)
```

**Working:**
- unverified: whether the Israeli business buyer must self-assess VAT on this service, and under which provision. The provision that puts the tax on an Israeli buyer of a service from a foreign supplier was not opened in an official text; confirm it before using this example.
- If the buyer must self-assess: the foreign price contains no Israeli VAT, so the tax is 18% of the consideration, not 18/118 of it. VAT is charged at a fixed rate on the transaction price agreed between the parties (rights guide, PDF p.140). ILS 5,865 x 18% = ILS 1,055.70.
- Declare the ILS 1,055.70 as output tax AND claim it as input tax (a fully taxable business that holds the document the input claim needs): net zero.
- Return entry: Reverse-charge output: base ILS 5,865, tax ILS 1,055.70 | Input Totchaot: tax ILS 1,055.70

### Example 5: Business vehicle purchase (blocked credit)

**Scenario:** Company purchases a passenger car (רכב פרטי) for a salesperson.

**Bank statement line (Hapoalim format):**
```
תאריך    : 03/04/2025
סוג פעולה: חיוב - העברה בנקאית
תיאור    : CHAMPION MOTORS LTD - רכישת רכב: חשב׳ 2025-V-041
סכום     : -177,000 ₪
```

**Working:**
- Passenger car (רכב פרטי): as a rule, no input tax may be deducted on buying a private car (VAT Regulations reg. 14, as stated in rights guide, PDF p.141). Exceptions: a car used only for driving lessons, for car hire by a car-hire business, for carrying passengers by a passenger-transport business, or for tours by a tour business; and a commercial vehicle over 3,500 kg used for the business that is not like a vehicle in the fourth schedule
- Heshbonit Mase shows: net ILS 150,000 + Ma'am ILS 27,000 = ILS 177,000
- Input credit: ILS 0 (none of the exceptions applies to a salesperson's car)
- Record as Tier 2: confirm whether vehicle classified as commercial (רכב מסחרי) or private

### Example 6: Bimonthly return summary

**Bimonthly return summary**

| Item | Net (ILS) | Ma'am (ILS) |
| --- | --- | --- |
| Software sales (domestic) | 800,000 | 144,000 |
| Export (zero-rated) | 300,000 | 0 |
| Cloud subscriptions (reverse-charge output, self-assessed) | 30,000 | 5,400 |
| Total Output | 1,130,000 | 149,400 |
| Purchases: hardware | 200,000 | 36,000 |
| Office rent | 50,000 | 9,000 |
| Cloud subscriptions (reverse-charge) | 30,000 | 5,400 |
| Total Input | 280,000 | 50,400 |
| **Net Ma'am payable** |  | **99,000** |

The reverse-charge line appears twice: once as output (5,400) and once as input (5,400), so it nets to zero and leaves the payable at 144,000 − 45,000 = 99,000. Claiming the 5,400 as input without declaring it as output understates the tax by ILS 5,400. Whether this service falls under a reverse charge at all is unverified (see Example 4).

## Section 5: Tier 1 rules (compressed)

- **Rate assignment**: - 18% standard (rights guide, PDF p.140); unverified for the lists that follow: almost all goods and services (food, clothing, electronics, professional services: all at standard rate unlike EU VAT) - 0%: exports of goods with customs declaration, services exported to foreign residents used outside Israel, tourism services to non-residents with foreign currency payment - Exempt: financial services, insurance, residential rent (non-commercial), medical services by licensed practitioners, educational services
- **Input credit** (rights guide, PDF p.141, VAT Law s.38(a)): - A dealer deducts input tax shown on a tax invoice lawfully issued to it, an import declaration or another document the Director approved, bearing the dealer's name, within six months of the document's date - Input tax is deductible only for use in a taxable transaction (full rate or zero rate), not an exempt one - From 1.1.2026 no deduction on a tax invoice above ILS 10,000 before VAT (ILS 5,000 from 1.6.2026) that lacks an allocation number under VAT Law s.47(a2)(2) - Blocked: buying a private car (רכב פרטי), VAT Regulations reg. 14, with the exceptions in Example 5 - Running costs of a business car, VAT Regulations reg. 18: up to 2/3 of the input tax if the car is mainly used for the business; up to 1/4 if it is mainly not - unverified: entertainment and other personal-expense blocks - Reverse charge (foreign services): where it applies (unverified, see Example 4), declare the output and claim the input; they net to zero for a fully taxable Osek Murshe
- **Filing mechanics** (rights guide, PDF p.141, VAT annex s.9): - Two-monthly return if turnover in the determining year is up to ILS 1,775,000; monthly above ILS 1,775,000 (as at 1 January 2026; the amount is updated once a year) - File within 15 days after the end of the reporting period - Show input tax on fixed assets separately from other input tax; the last line is output tax minus input tax; if input exceeds output, file a refund return - unverified: the ILS 305 invoice figure, refund timing for exporters, and monthly filing for new businesses

## Section 6: Tier 2 catalogue (genuinely data-unknowable items)

**Tier 2 catalogue**

| Item | Why unknowable | What to ask |
| --- | --- | --- |
| Vehicle purchase | Private (blocked credit) vs commercial (allowed) depends on registration | "Provide vehicle licence: is it רכב פרטי or רכב מסחרי?" |
| Home office | Business % of home use unknown | "What % of your home is used exclusively for business?" |
| Mobile phone | Business vs personal split | "Is this a dedicated business phone? Estimate business use %." |
| Entertainment | Must prove business purpose | "List attendees and business purpose of each entertainment expense." |
| Mixed residential/commercial property | Residential rent exempt, commercial 18% | "Is the lease for residential or commercial use? Provide lease agreement." |
| Export documentation incomplete | Zero-rate only with valid export evidence | "Provide customs export declaration or foreign payment evidence." |
| Osek Patur supplier | Unregistered supplier: no Heshbonit Mase available, no input credit | "Confirm supplier registration status: Osek Murshe or Osek Patur?" |

## Section 7: Excel working paper

**Columns:** Date | Supplier / Customer | Osek No. | Invoice No. | Net (ILS) | Ma'am Rate % | Ma'am (ILS) | In/Out | Zero-rated? | Exempt? | Tier 2 flag | Notes

**Tab structure:**
1. `Output_Sales`: all sales (domestic 18%, zero-rated exports, exempt)
2. `Input_Purchases`: all purchases with Ma'am credit
3. `ReverseCharge_Foreign`: foreign services self-assessed
4. `MaamSummary`: bimonthly return totals
5. `Tier2_Items`: awaiting client response

- **Key formula**: Net_Maam_Payable = Total_Output_Maam - Total_Input_Maam - Excess_BF

## Section 8: Bank statement reading guide

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

## Section 9: Onboarding fallback

- **Fallback when Heshbonit Mase unavailable**: When client cannot provide Heshbonit Mase for all transactions: 1. Use bank statement amounts as Ma'am-inclusive totals and back-calculate: - Net = Total ÷ 1.18 | Ma'am = Total − Net 2. Apply conservative defaults: 18% output on all unverified sales; 0% input credit without valid Heshbonit Mase 3. Flag all items without Heshbonit Mase in Tier2_Items tab 4. Issue data request listing missing invoice references 5. Warn client: ITA can disallow input credit claims without valid Heshbonit Mase from Osek Murshe supplier: risk of penalty

## Section 10: Reference material

**Reference material**

| Resource | Reference |
| --- | --- |
| ITA filing portal (Shaam Online) | https://www.misim.gov.il |
| Ma'am Law (מס ערך מוסף, 1975) | ITA website: tax law library |
| ITA official guidance (חוזרים) | taxes.gov.il/maam |
| Registration threshold updates | ITA annual circular |
| Heshbonit Mase requirements | Section 9 Ma'am Law |
| Tourist refund scheme | ITA Form 1345 guidance |

## Recomputed checks (2026)

```oa-check
name: Invoice net ILS 200,000
inputs:
  n: 200000
steps:
  - v: n*0.18
expected:
  v: 36000
```

```oa-check
name: Bimonthly net payable with reverse-charge output declared
inputs:
  sales: 800000
  rc: 30000
  hardware: 200000
  rent: 50000
steps:
  - output: (sales+rc)*0.18
  - input: (hardware+rent+rc)*0.18
  - p: output-input
expected:
  output: 149400
  input: 50400
  p: 99000
```

## Sources

| Source | URL | Read on |
|---|---|---|
| Israel Tax Authority, "Know your rights and duties" guide, tax year 2025 (published July 2026), Annex C VAT guide for a new dealer, read PDF pp.139-141 (Osek Patur ceiling ILS 122,833 as at January 2026, 18% rate as at January 2026, tax invoice, input tax under VAT Law s.38(a), allocation-number limits, VAT Regulations regs. 14 and 18 on cars, two-monthly/monthly ILS 1,775,000 as at 1/1/2026, 15-day deadline) | https://www.gov.il/BlobFolder/generalpage/income-tax-guide-knowyourright/he/Guides_IncomeTax_da-2025.pdf | 2026-11-03 |
| Israel Tax Authority, Form 1301 service page, tax year 2025 | https://www.gov.il/he/service/reporting-and-payment-2025-annual-tax-report-for-individuals | 2026-11-01 |

Not yet confirmed: the reverse-charge rule for services bought from a foreign supplier and its legal basis (no official text of the VAT Law or Regulations was opened; Examples 4 and 6 depend on it); the ILS 305 invoice figure; the zero-rate and exempt lists; refund timing for exporters and monthly filing for new businesses; the entertainment block; form names PCN83/PCN874; the supplier treatment tables in Section 3 (a supplier's name does not settle the legal treatment; each row is unverified); Form 1345 and the tourism zero rate in Example 3; the import base in Example 2.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-03. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `israel-vat` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/israel-vat. If neither is available, confirm every figure against the official source pages cited above before relying on it.
