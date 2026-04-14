---
name: israel-vat
description: Use this skill whenever asked to prepare, review, or classify transactions for an Israel VAT (Ma'am — מע"מ) return or advise on Israeli VAT registration, filing, and reporting. Trigger on phrases like "prepare Ma'am return", "Israeli VAT", "מע"מ", "doch maam", or any Israel VAT request. ALWAYS read this skill before touching any Israel Ma'am-related work.
version: 2.0
jurisdiction: IL
tax_year: 2025
category: international
depends_on:
  - vat-workflow-base
---

# Israel VAT (Ma'am — מע"מ) Skill v2.0

---

## Section 1 — Quick reference

| Field | Value |
|---|---|
| Country | Israel (מדינת ישראל) |
| Tax | Ma'am (מס ערך מוסף — Value Added Tax) |
| Currency | ILS (Israeli New Shekel — ₪) |
| Standard rate | 17% (effective January 2025; was 17% restored after temporary 18% in 2024) |
| Reduced rate | 0% (exports, specific agricultural produce, tourism services to non-residents) |
| Exempt | Financial services, insurance, residential rent (if not commercial), medical services |
| Registration threshold | ILS 120,000 annual turnover (2025 threshold); below this — "Osek Patur" (exempt dealer) |
| Small business | Osek Murshe (עוסק מורשה) — registered dealer filing periodic returns |
| Tax authority | Israel Tax Authority (ITA — רשות המיסים בישראל) |
| Filing portal | Shaam Online — https://www.misim.gov.il |
| Return form | Doch Ma'am (דוח מע"מ — Form PCN83 / PCN874) |
| Filing frequency | Bimonthly (most businesses); Monthly (turnover > ILS 1.5M) |
| Deadline | 15th of the month following the reporting period |
| Tax invoices | Heshbonit Mase (חשבונית מס) required for all B2B transactions above ILS 305 |
| Contributor | Open Accountants Community |
| Validated by | Pending — requires sign-off by Israel-licensed CPA (רואה חשבון) |
| Skill version | 2.0 |

### Key return form fields

| Field | Meaning |
|---|---|
| Iska (עסקה) | Output tax base — taxable supplies at 17% |
| Yetsia (יציאה) | Exports / zero-rated supplies |
| Pator (פטור) | Exempt supplies |
| Totchaot (תשומות) | Input tax on purchases |
| Maam Letashlum (מע"מ לתשלום) | Net Ma'am payable (Output − Input) |
| Yiteret Totchaot (יתרת תשומות) | Excess input tax carried forward |
| Mechira LeZar (מכירה לזר) | Sale to foreign resident (zero-rated tourism) |

### Conservative defaults

| Ambiguity | Default |
|---|---|
| Unknown rate on a sale | 17% standard |
| Unknown whether export documentation complete | Treat as domestic 17% |
| Unknown business-use % (vehicle, phone, home) | 0% input credit |
| Unknown whether Heshbonit Mase issued | No input credit until confirmed |
| Financial service vs professional service | Treat as professional — 17% |
| Residential rent vs commercial | Treat as exempt until lease reviewed |
| Foreign digital service (B2B) | Buyer self-assesses under reverse charge |

### Red flag thresholds

| Threshold | Value |
|---|---|
| HIGH single transaction | ILS 100,000 |
| HIGH tax delta on single conservative default | ILS 17,000 |
| MEDIUM counterparty concentration | >40% of output or input |
| MEDIUM conservative default count | >4 per return |
| LOW absolute net Ma'am position | ILS 250,000 |

---

## Section 2 — Required inputs and refusal catalogue

### Required inputs

Before starting any Israel Ma'am work, obtain:

1. Osek number (מספר עוסק — 9-digit taxpayer ID) and registration certificate
2. Bimonthly bank statements in ILS (all business accounts)
3. Heshbonit Mase (tax invoices) from all suppliers — must include supplier's Osek number
4. Sales invoices issued (Heshbonit Mase or Heshbonit Kala for amounts below ILS 305)
5. Prior period Doch Ma'am (for carried-forward excess input credit)
6. Import documents from Customs (ASYCUDA / import declarations) for imported goods
7. Details of zero-rated tourism transactions (passports, foreign payment evidence)

### Refusal catalogue

Refuse and escalate to a licensed CPA (רואה חשבון) for:
- Partial exemption (Alut Yechusit — עלות יחסית) — businesses with mixed exempt/taxable
- Real estate Ma'am transactions (Mas Rechisha — complex exemptions on property)
- Ma'am group registration (Kvutzat Osek — עוסק קבוצה)
- Designated area supplies (Eilat free zone — zero-rated)
- Diamond and precious metal special scheme
- Ma'am on long-term contracts and construction
- Retroactive registration for Osek Patur transitioning to Osek Murshe

---

## Section 3 — Supplier pattern library

### 3.1 Banking and financial services

| Supplier | Typical description | Ma'am rate | Input credit |
|---|---|---|---|
| Bank Hapoalim (בנק הפועלים) | Bank fees, wire charges | Exempt | No |
| Bank Leumi (בנק לאומי) | Account maintenance, loans | Exempt | No |
| Mizrahi Tefahot (מזרחי טפחות) | Mortgage, business banking | Exempt | No |
| Discount Bank (בנק דיסקונט) | Commercial banking fees | Exempt | No |
| Bank Otsar HaHayal (אוצר החייל) | Military banking | Exempt | No |
| Bit (ביט — Hapoalim app) | P2P payment transfer | Exempt | No |
| PayBox (פייבוקס — Leumi) | P2P digital wallet | Exempt | No |
| Pelecard / Creditguard | Payment processing | 17% | Yes |
| Tranzila | E-commerce payment gateway | 17% | Yes |

### 3.2 Electricity and utilities

| Supplier | Typical description | Ma'am rate | Input credit |
|---|---|---|---|
| Israel Electric Corporation (חברת החשמל — IEC) | Electricity | 17% | Yes (business) |
| Mekorot (מקורות) | Water supply wholesale | 17% | Yes |
| Local municipality water (ועדה מקומית) | Water — municipal | 17% | Yes |
| Paz Gas / Supergas | Gas — cooking/heating | 17% | Yes |
| Cellcom Energy | Green electricity supply | 17% | Yes |

### 3.3 Telecommunications

| Supplier | Typical description | Ma'am rate | Input credit |
|---|---|---|---|
| Cellcom (סלקום) | Mobile, broadband | 17% | Yes (business use) |
| Partner Communications (פרטנר) | Mobile, fiber, TV | 17% | Yes (business use) |
| Bezeq (בזק) | Fixed line, DSL internet | 17% | Yes (business use) |
| HOT (הוט) | Cable TV, internet, phone | 17% | Yes (business use) |
| 012 Mobile / 013 Netvision | MVNO, internet | 17% | Yes |
| Golan Telecom (גולן טלקום) | Discount mobile | 17% | Yes |

### 3.4 Transport and travel

| Supplier | Typical description | Ma'am rate | Input credit |
|---|---|---|---|
| El Al (אל על) | Domestic flights (Eilat) | 17% | Yes |
| El Al | International flights | 0% | No input credit applicable |
| Arkia | Domestic flights | 17% | Yes |
| Israir | Domestic flights | 17% | Yes |
| Israel Railways (רכבת ישראל) | Train tickets | 17% | Yes |
| Egged (אגד) | Bus — intercity | 17% | Yes |
| Dan (דן) | Bus — Tel Aviv metro | 17% | Yes |
| Gett (גט) | Taxi app | 17% | Yes (business use) |
| Yango | Ride-hailing | 17% | Yes (business use) |

### 3.5 Logistics and postal

| Supplier | Typical description | Ma'am rate | Input credit |
|---|---|---|---|
| Israel Post (דואר ישראל) | Domestic mail, parcels | 17% | Yes |
| DHL Israel | International courier | 0% (export) / 17% (domestic) | Yes |
| UPS Israel | International courier | 0% / 17% | Yes |
| FedEx Israel | International courier | 0% / 17% | Yes |
| Ashot Logistics | Domestic delivery | 17% | Yes |

### 3.6 Retail and office supplies

| Supplier | Typical description | Ma'am rate | Input credit |
|---|---|---|---|
| Shufersal (שופרסל) | Supermarket — food/non-food | 17% (food not zero-rated in IL) | Yes (business) |
| Rami Levy (רמי לוי) | Discount supermarket | 17% | Yes |
| Office Depot Israel | Office supplies | 17% | Yes |
| KSP (כ.ס.פ) | Electronics | 17% | Yes |
| SuperPharm | Pharmacy — medicines | 17% (medicines not zero-rated in IL) | Yes |
| Factory 54 / Castro | Clothing | 17% | Yes |

### 3.7 Software and digital services

| Supplier | Typical description | Ma'am rate | Input credit |
|---|---|---|---|
| Priority Software (פריוריטי) | Israeli ERP | 17% | Yes |
| Greeninvoice (חשבונית ירוקה) | Cloud invoicing platform | 17% | Yes |
| Hashavshevet (חשבשבת) | Accounting software | 17% | Yes |
| iCount | Cloud accounting | 17% | Yes |
| Microsoft Israel (Azure, M365) | Cloud services — B2B | 17% (buyer reverse-charge) | Yes |
| Google Workspace IL | Cloud — B2B | 17% (buyer reverse-charge) | Yes |
| Salesforce Israel | CRM — B2B | 17% (buyer reverse-charge) | Yes |
| AWS Israel | Cloud infrastructure — B2B | 17% (buyer reverse-charge) | Yes |

### 3.8 Professional services

| Supplier | Typical description | Ma'am rate | Input credit |
|---|---|---|---|
| Roeh Heshbon (רואה חשבון — CPA) | Accounting, audit | 17% | Yes |
| Orech Din (עורך דין — lawyer) | Legal services | 17% | Yes |
| Munahel Ishur (מנהל אישור — notary equivalent) | Document certification | 17% | Yes |
| Reklam / marketing agency | Advertising, PR | 17% | Yes |
| Building contractor (קבלן) | Construction services | 17% | Yes |

### 3.9 Insurance

| Supplier | Typical description | Ma'am rate | Input credit |
|---|---|---|---|
| Harel Insurance (הראל) | Business insurance | Exempt | No |
| Menora Mivtachim (מנורה מבטחים) | Property, liability | Exempt | No |
| Clal Insurance (כלל ביטוח) | Vehicle, business | Exempt | No |
| AIG Israel | Professional indemnity | Exempt | No |

### 3.10 Healthcare

| Supplier | Typical description | Ma'am rate | Input credit |
|---|---|---|---|
| Clalit (כללית) | Health fund / Kupat Holim | Exempt | No |
| Maccabi (מכבי) | Health fund | Exempt | No |
| Meuhedet (מאוחדת) | Health fund | Exempt | No |
| Private clinic / specialist | Private medical | Exempt | No |

---

## Section 4 — Worked examples

### Example 1 — Standard Ma'am on consulting fee

**Scenario:** Tel Aviv software consulting firm issues Heshbonit Mase to Israeli corporate client.

**Bank statement line (Bank Hapoalim format):**
```
תאריך    : 15/04/2025
סוג פעולה: זיכוי - העברה בנקאית
תיאור    : TECH SOLUTIONS LTD - חשבונית 041/2025 - שכ"ט ייעוץ
סכום     : +234,000 ₪
```

**Working:**
- Heshbonit Mase: net ILS 200,000 + Ma'am 17% ILS 34,000 = ILS 234,000
- Return entry: Output Iska — ILS 200,000 | Output Ma'am: ILS 34,000

---

### Example 2 — Import of goods (reverse-charge customs)

**Scenario:** Company imports electronics from Germany — customs clears at Ben Gurion.

**Bank statement line (Bank Leumi format):**
```
תאריך    : 10/04/2025
פעולה    : שוברי רכש - פרעון / מכס ומע"מ
תיאור    : תשלום מכס ומע"מ יבוא — ASYCUDA REF 2025-04-1234
סכום     : -87,040 ₪
```

**Working:**
- Import customs document: CIF value ILS 400,000 + customs duty ILS 112,000 = ILS 512,000 × 17% = ILS 87,040 Ma'am
- Pay at port of entry — then claim as input tax in Doch Ma'am filing
- Return entry: Input Totchaot — ILS 512,000; Input Ma'am: ILS 87,040

---

### Example 3 — Zero-rated tourism service

**Scenario:** Hotel provides accommodation to foreign tourist paying in USD.

**Bank statement line (Mizrahi Tefahot format):**
```
תאריך    : 18/04/2025
סוג      : זיכוי מטבע חוץ
תיאור    : HOTEL BOOKING - FOREIGN GUEST - BOOKING REF TL-2025-0418
סכום     : +7,650 ₪ (USD 2,100)
```

**Working:**
- Foreign tourist — payment in foreign currency — qualifies as zero-rated tourist service
- Requires: passport copy, foreign payment evidence, ITA Form 1345
- Return entry: Mechira LeZar — ILS 7,650 | Ma'am: ILS 0

---

### Example 4 — Reverse-charge on foreign digital service

**Scenario:** Company pays for Google Workspace (billed from Google Ireland).

**Bank statement line (Discount Bank format):**
```
תאריך    : 05/04/2025
פעולה    : חיוב — שירות בנקאי חו"ל
תיאור    : GOOGLE IRELAND LTD — WORKSPACE SUBSCRIPTION APR 2025
סכום     : -5,865 ₪ (USD 1,600)
```

**Working:**
- Foreign digital service to Israeli business — treated as supplied in Israel
- Buyer self-assesses: ILS 5,865 × 17/117 = ILS 852 Ma'am (or ILS 5,013 net + ILS 852 Ma'am)
- Declare as output AND claim as input — net zero for fully taxable business
- Return entry: Reverse-charge output ILS 5,013 | and Input Totchaot ILS 5,013

---

### Example 5 — Business vehicle purchase (blocked credit)

**Scenario:** Company purchases a passenger car (רכב פרטי) for a salesperson.

**Bank statement line (Hapoalim format):**
```
תאריך    : 03/04/2025
סוג פעולה: חיוב - העברה בנקאית
תיאור    : CHAMPION MOTORS LTD - רכישת רכב — חשב׳ 2025-V-041
סכום     : -175,500 ₪
```

**Working:**
- Passenger car (רכב פרטי): input Ma'am blocked under Section 41 of Ma'am Law
- Heshbonit Mase shows: net ILS 150,000 + Ma'am ILS 25,500 = ILS 175,500
- Input credit: ILS 0 — full block on private passenger vehicles
- Record as Tier 2 — confirm whether vehicle classified as commercial (רכב מסחרי) or private

---

### Example 6 — Bimonthly return summary

**Scenario:** Tech startup — March–April 2025 bimonthly period.

| Item | Net (ILS) | Ma'am (ILS) |
|---|---|---|
| Software sales (domestic) | 800,000 | 136,000 |
| Export (zero-rated) | 300,000 | 0 |
| Total Output | 1,100,000 | 136,000 |
| Purchases — hardware | 200,000 | 34,000 |
| Office rent | 50,000 | 8,500 |
| Cloud subscriptions (reverse-charge) | 30,000 | 5,100 |
| Total Input | 280,000 | 47,600 |
| **Net Ma'am payable** | | **88,400** |

---

## Section 5 — Tier 1 rules (compressed)

**Rate assignment:**
- 17% standard: almost all goods and services (food, clothing, electronics, professional services — all at standard rate unlike EU VAT)
- 0%: exports of goods with customs declaration, services exported to foreign residents used outside Israel, tourism services to non-residents with foreign currency payment
- Exempt: financial services, insurance, residential rent (non-commercial), medical services by licensed practitioners, educational services

**Input credit:**
- Credit allowed on all 17% purchases for taxable business activities
- Blocked: passenger vehicles (רכב פרטי) — Section 41 Ma'am Law
- Blocked: personal expenses — entertainment with non-business purpose
- Partially blocked: vehicles used partly for business — 2/3 credit allowed if mixed use claimed; needs documentation
- Reverse-charge (foreign services): output and input net to zero for fully taxable Osek Murshe

**Filing mechanics:**
- File bimonthly via Shaam Online by 15th of following month
- Monthly if turnover > ILS 1.5M (file by 15th of following month)
- All B2B invoices above ILS 305 must be Heshbonit Mase with supplier's Osek number
- Excess input credit carried forward — refund available for exporters after 3 months
- New businesses: first 6 months allowed monthly filing to facilitate refunds

---

## Section 6 — Tier 2 catalogue (genuinely data-unknowable items)

| Item | Why unknowable | What to ask |
|---|---|---|
| Vehicle purchase | Private (blocked credit) vs commercial (allowed) depends on registration | "Provide vehicle licence — is it רכב פרטי or רכב מסחרי?" |
| Home office | Business % of home use unknown | "What % of your home is used exclusively for business?" |
| Mobile phone | Business vs personal split | "Is this a dedicated business phone? Estimate business use %." |
| Entertainment | Must prove business purpose | "List attendees and business purpose of each entertainment expense." |
| Mixed residential/commercial property | Residential rent exempt, commercial 17% | "Is the lease for residential or commercial use? Provide lease agreement." |
| Export documentation incomplete | Zero-rate only with valid export evidence | "Provide customs export declaration or foreign payment evidence." |
| Osek Patur supplier | Unregistered supplier — no Heshbonit Mase available, no input credit | "Confirm supplier registration status — Osek Murshe or Osek Patur?" |

---

## Section 7 — Excel working paper

**Columns:** Date | Supplier / Customer | Osek No. | Invoice No. | Net (ILS) | Ma'am Rate % | Ma'am (ILS) | In/Out | Zero-rated? | Exempt? | Tier 2 flag | Notes

**Tab structure:**
1. `Output_Sales` — all sales (domestic 17%, zero-rated exports, exempt)
2. `Input_Purchases` — all purchases with Ma'am credit
3. `ReverseCharge_Foreign` — foreign services self-assessed
4. `MaamSummary` — bimonthly return totals
5. `Tier2_Items` — awaiting client response

**Key formula:**
```
Net_Maam_Payable = Total_Output_Maam - Total_Input_Maam - Excess_BF
```

---

## Section 8 — Bank statement reading guide

### Bank Hapoalim format
```
תאריך    : 15/04/2025
סוג פעולה: זיכוי - העברה בנקאית
תיאור    : TECH SOLUTIONS - חשבונית 041/2025
סכום     : +234,000 ₪
יתרה     : 1,234,000 ₪
```
Fields: תאריך (date) | סוג פעולה (transaction type) | תיאור (description) | סכום (amount, ILS)

### Bank Leumi format
```
15.04.2025  |  זיכוי  |  TECH SOLUTIONS  |  +234,000.00  |  יתרה: 1,234,000.00
```

### Key patterns:
- **ILS number format:** Comma = thousands separator; period = decimal (ILS 234,000.00)
- **זיכוי (credit):** Money in — match to issued Heshbonit Mase
- **חיוב (debit):** Money out — match to received Heshbonit Mase for input credit
- **מטבע חוץ (foreign currency):** Foreign payment — check for zero-rated export or reverse-charge
- **מכס ומע"מ:** Customs and Ma'am — import duty + import Ma'am payment

---

## Section 9 — Onboarding fallback

When client cannot provide Heshbonit Mase for all transactions:

1. Use bank statement amounts as Ma'am-inclusive totals and back-calculate:
   - Net = Total ÷ 1.17 | Ma'am = Total − Net
2. Apply conservative defaults: 17% output on all unverified sales; 0% input credit without valid Heshbonit Mase
3. Flag all items without Heshbonit Mase in Tier2_Items tab
4. Issue data request listing missing invoice references
5. Warn client: ITA can disallow input credit claims without valid Heshbonit Mase from Osek Murshe supplier — risk of penalty

---

## Section 10 — Reference material

| Resource | Reference |
|---|---|
| ITA filing portal (Shaam Online) | https://www.misim.gov.il |
| Ma'am Law (מס ערך מוסף, 1975) | ITA website — tax law library |
| ITA official guidance (חוזרים) | taxes.gov.il/maam |
| Registration threshold updates | ITA annual circular |
| Heshbonit Mase requirements | Section 9 Ma'am Law |
| Tourist refund scheme | ITA Form 1345 guidance |


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
