---
name: egypt-vat
description: Use this skill whenever asked to prepare, review, or classify transactions for an Egypt VAT return or advise on Egyptian VAT registration, filing, and e-invoicing compliance. Trigger on phrases like "prepare Egypt VAT return", "Egyptian VAT", "ضريبة القيمة المضافة مصر", "ETA e-invoice", or any Egypt VAT request. ALWAYS read this skill before touching any Egypt VAT work.
version: 2.0
jurisdiction: EG
tax_year: 2025
category: international
depends_on:
  - vat-workflow-base
---

# Egypt VAT (ضريبة القيمة المضافة) Skill v2.0

---

## Section 1 — Quick reference

| Field | Value |
|---|---|
| Country | Egypt (جمهورية مصر العربية) |
| Tax | Value Added Tax (ضريبة القيمة المضافة — VAT) |
| Currency | EGP (Egyptian Pound — ج.م) |
| Standard rate | 14% |
| Reduced rate | 5% (selected equipment, machinery, some agricultural inputs) |
| Zero rate | 0% (exports of goods and services, international transport, diplomatic supplies) |
| Exempt | Financial services, insurance, medical services, educational services, residential rent, utilities (in certain cases) |
| Registration threshold | EGP 500,000 annual turnover |
| Tax authority | Egyptian Tax Authority (ETA — مصلحة الضرائب المصرية) |
| Filing portal | ETA e-Invoice portal — https://invoicing.eta.gov.eg |
| Return form | VAT Return (إقرار ضريبة القيمة المضافة) |
| Filing frequency | Monthly |
| Deadline | Last day of the following month |
| e-Invoice | Mandatory for all VAT-registered businesses (ETA e-Invoice system) |
| Contributor | Open Accountants Community |
| Validated by | Pending — requires sign-off by Egypt-licensed CPA (محاسب قانوني) |
| Skill version | 2.0 |

### Key return sections

| Section | Meaning |
|---|---|
| Section A | Taxable sales at 14% (net) |
| Section B | Taxable sales at 5% (net) |
| Section C | Zero-rated exports (net) |
| Section D | Exempt supplies (net) |
| Section E | Total output VAT |
| Section F | Input VAT on purchases at 14% |
| Section G | Input VAT on purchases at 5% |
| Section H | Import VAT paid at customs |
| Section I | Total input VAT |
| Section J | Net VAT payable (E − I; if positive) |
| Section K | Excess input VAT carried forward |

### Conservative defaults

| Ambiguity | Default |
|---|---|
| Unknown rate on a sale | 14% standard |
| Unknown whether 5% rate applies | 14% until confirmed |
| Unknown whether export documentation complete | Treat as domestic 14% |
| Unknown business-use % (vehicle, phone, home) | 0% input credit |
| Unknown whether e-Invoice issued via ETA | No input credit until confirmed |
| Financial service vs professional service | Treat as professional — 14% |
| Foreign digital service (B2B) | 14% reverse-charge — buyer self-assesses |

### Red flag thresholds

| Threshold | Value |
|---|---|
| HIGH single transaction | EGP 500,000 |
| HIGH tax delta on single conservative default | EGP 70,000 |
| MEDIUM counterparty concentration | >40% of output or input |
| MEDIUM conservative default count | >4 per return |
| LOW absolute net VAT position | EGP 1,000,000 |

---

## Section 2 — Required inputs and refusal catalogue

### Required inputs

Before starting any Egypt VAT work, obtain:

1. ETA Tax Registration Number (TRN — رقم التسجيل الضريبي — 9 digits)
2. ETA e-Invoice portal credentials and API key for accessing issued/received e-invoices
3. Monthly bank statements in EGP (all business accounts)
4. ETA e-Invoice XML downloads for all sales and purchases
5. Import customs declarations (بيان جمركي) from Egyptian Customs Authority
6. Prior month VAT return (for carried-forward excess input credit)
7. Details of export transactions with shipping documentation

### Refusal catalogue

Refuse and escalate to a licensed Egyptian tax consultant for:
- Partial exemption calculations (businesses with mixed taxable/exempt supplies)
- VAT on real estate and construction (complex rules)
- Special tax regimes (simplified VAT for certain agricultural cooperatives)
- Reverse-charge on imported services — complex cases involving multiple service types
- VAT refund claims for exporters (long process requiring ETA audit)
- Turnover tax (ضريبة المبيعات) on certain categories — replaced by VAT but some transitional issues remain
- VAT on free zones and special economic zones

---

## Section 3 — Supplier pattern library

### 3.1 Banking and financial services

| Supplier | Typical description | VAT rate | Input credit |
|---|---|---|---|
| Commercial International Bank (CIB) | Bank fees, transfers | Exempt | No |
| National Bank of Egypt (NBE — البنك الأهلي المصري) | Loans, account fees | Exempt | No |
| Banque Misr (بنك مصر) | Commercial banking | Exempt | No |
| QNB Alahli (بنك قطر الوطني الأهلي) | Banking services | Exempt | No |
| Banque du Caire | Business banking | Exempt | No |
| Fawry (فوري) | Bill payment, digital collections | 14% | Yes |
| Instapay (إنستا باي) | P2P and B2B payments | Exempt (payment service) | No |
| Paymob | Payment gateway | 14% | Yes |
| Vodafone Cash | Mobile money transfer | Exempt | No |
| Orange Cash | Mobile wallet | Exempt | No |

### 3.2 Electricity and utilities

| Supplier | Typical description | VAT rate | Input credit |
|---|---|---|---|
| EEHC / Cairo Electricity (شركة القاهرة لتوزيع الكهرباء) | Electricity — commercial | 14% | Yes |
| Alexandria Electricity (شركة الإسكندرية لتوزيع الكهرباء) | Electricity — commercial | 14% | Yes |
| Cairo Water (شركة مياه القاهرة) | Water supply | 14% | Yes |
| Town Gas (طاون جاس) | Natural gas | 14% | Yes |
| Sawi Gas | Gas — household/commercial | 14% | Yes |

### 3.3 Telecommunications

| Supplier | Typical description | VAT rate | Input credit |
|---|---|---|---|
| Vodafone Egypt (فودافون مصر) | Mobile, data | 14% | Yes (business use) |
| Orange Egypt (أورنج مصر) | Mobile, fiber internet | 14% | Yes (business use) |
| Etisalat Egypt / e& Egypt | Mobile, business lines | 14% | Yes (business use) |
| WE (المصرية للاتصالات) | Fixed line, ADSL | 14% | Yes (business use) |
| Telecom Egypt | Wholesale, enterprise | 14% | Yes |

### 3.4 Transport and travel

| Supplier | Typical description | VAT rate | Input credit |
|---|---|---|---|
| EgyptAir (مصر للطيران) | Domestic flights | 14% | Yes |
| EgyptAir | International flights | 0% (export) | No input applicable |
| Air Arabia Egypt | Domestic/regional flights | 14% (domestic) | Yes |
| Egyptian National Railways (ENR — السكك الحديدية) | Train tickets | Exempt | No |
| Cairo Metro (مترو الأنفاق) | Metro tickets | Exempt | No |
| Uber Egypt | Ride-hailing | 14% | Yes (business use) |
| Careem Egypt | Ride-hailing | 14% | Yes (business use) |
| InDriver Egypt | Ride-hailing | 14% | Yes |

### 3.5 Logistics and courier

| Supplier | Typical description | VAT rate | Input credit |
|---|---|---|---|
| Aramex Egypt (أرامكس مصر) | International/domestic courier | 14% | Yes |
| DHL Egypt | International courier | 0% (export) / 14% (domestic) | Yes |
| FedEx Egypt | International courier | 0% / 14% | Yes |
| Egyptian Post (البريد المصري) | Postal services | 14% | Yes |
| Mylerz | E-commerce logistics | 14% | Yes |
| Bosta | Last-mile delivery | 14% | Yes |

### 3.6 Retail and office supplies

| Supplier | Typical description | VAT rate | Input credit |
|---|---|---|---|
| Carrefour Egypt (كارفور مصر) | Supermarket — mixed goods | 14% / exempt food mix | Partial |
| Spinneys Egypt | Premium supermarket | 14% | Yes |
| Seoudi Market | Upscale grocery | 14% | Yes |
| Metro Markets (ميترو) | Wholesale/cash-and-carry | 14% | Yes |
| Office 1 Egypt | Office supplies | 14% | Yes |
| B.Tech | Electronics retailer | 14% | Yes |
| Xcite | Electronics | 14% | Yes |

### 3.7 Software and digital services

| Supplier | Typical description | VAT rate | Input credit |
|---|---|---|---|
| Odoo Egypt | ERP — B2B | 14% | Yes |
| Fintech Galaxy / Khazna | Fintech platform | 14% | Yes |
| Microsoft Egypt (Azure, M365) | Cloud services — B2B | 14% (buyer reverse-charge) | Yes |
| Google Egypt (Workspace, Ads) | Digital services — B2B | 14% (buyer reverse-charge) | Yes |
| Amazon AWS Egypt | Cloud — B2B | 14% (buyer reverse-charge) | Yes |
| Zoom Egypt | Video conferencing — B2B | 14% (buyer reverse-charge) | Yes |
| ETA e-Invoice portal fees | System fees (if any) | 14% | Yes |

### 3.8 Professional services

| Supplier | Typical description | VAT rate | Input credit |
|---|---|---|---|
| Certified Public Accountant (محاسب قانوني) | Audit, tax advisory | 14% | Yes |
| Law firm (مكتب محاماة) | Legal services | 14% | Yes |
| Engineering / consulting firm | Technical consulting | 14% | Yes |
| Advertising agency | Marketing, PR | 14% | Yes |
| Recruitment firm | HR services | 14% | Yes |

### 3.9 Insurance

| Supplier | Typical description | VAT rate | Input credit |
|---|---|---|---|
| Misr Insurance (مصر للتأمين) | All lines | Exempt | No |
| Suez Canal Insurance | Marine, property | Exempt | No |
| AXA Egypt | Health, motor, property | Exempt | No |
| Allianz Egypt | Business insurance | Exempt | No |

### 3.10 Healthcare

| Supplier | Typical description | VAT rate | Input credit |
|---|---|---|---|
| Private hospital / clinic | Medical treatment | Exempt | No |
| Pharmacy (صيدلية) | Medicines | Exempt | No |
| Medical equipment supplier | Devices | 5% (reduced) | Yes |
| Seif Pharmacy / El-Ezaby | Pharmacy chain | Exempt (medicines) | No |

---

## Section 4 — Worked examples

### Example 1 — Standard VAT on service sale

**Scenario:** Cairo-based IT consulting firm issues e-Invoice to Egyptian corporate client.

**Bank statement line (CIB format):**
```
Date        : 15/04/2025
Transaction : Credit Transfer
Description : TECH SOLUTIONS CO — INV-2025-041 — IT CONSULTING SERVICES
Amount      : +EGP 570,000.00
Balance     : EGP 2,570,000.00
```

**Working:**
- ETA e-Invoice: net EGP 500,000 + VAT 14% EGP 70,000 = EGP 570,000
- Return entry: Section A — EGP 500,000 | Output VAT: EGP 70,000

---

### Example 2 — Export of services (zero-rated)

**Scenario:** Egyptian software firm exports SaaS to UK client. Payment in GBP.

**Bank statement line (NBE format):**
```
Date        : 20/04/2025
Transaction : Foreign Currency Credit
Description : BRITISH TECH LTD UK — SaaS SUBSCRIPTION APR 2025
Amount      : +EGP 1,250,000.00 (GBP 28,000)
```

**Working:**
- Export of services consumed outside Egypt by foreign entity — 0% VAT
- Requires: contract, bank transfer evidence, service agreement showing UK consumption
- Return entry: Section C — EGP 1,250,000 | VAT: EGP 0

---

### Example 3 — Reverse-charge on foreign digital service

**Scenario:** Company pays for Microsoft Azure (billed from Microsoft Ireland).

**Bank statement line (Banque Misr format):**
```
Date        : 05/04/2025
Transaction : Foreign Payment / SWIFT
Description : MICROSOFT IRELAND — AZURE CLOUD SERVICES APR 2025
Amount      : -EGP 112,000.00
```

**Working:**
- Foreign digital service to Egyptian business — taxable in Egypt
- Self-assess: EGP 112,000 × 14/114 = EGP 13,754 VAT (or EGP 98,246 net + EGP 13,754 VAT)
- Declare as output VAT AND claim as input — net zero for fully taxable business
- Include in VAT return both output (Section E) and input (Section I)

---

### Example 4 — Fawry payment collection (14% service fee)

**Scenario:** Company uses Fawry to collect customer payments; Fawry charges a collection fee.

**Bank statement line (QNB Alahli format):**
```
Date        : 30/04/2025
Transaction : Debit — Service Fee
Description : FAWRY FOR BANKING TECHNOLOGY — APR 2025 COLLECTION FEE
Amount      : -EGP 57,000.00
```

**Working:**
- Fawry e-Invoice: net EGP 50,000 + VAT 14% EGP 7,000 = EGP 57,000
- Input credit: EGP 7,000 — deductible (business service)
- Return entry: Section F — EGP 50,000; Input VAT: EGP 7,000

---

### Example 5 — Import of goods (customs VAT)

**Scenario:** Importing machinery from Germany. EGP equivalent at import.

**Bank statement line (CIB format):**
```
Date        : 08/04/2025
Transaction : Customs Payment
Description : CUSTOMS DUTY + VAT — BAYAN 2025-EG-04-7890 — INDUSTRIAL MACHINERY
Amount      : -EGP 700,000.00
```

**Working:**
- Customs declaration: CIF value EGP 4,000,000 + customs duty EGP 1,000,000 = EGP 5,000,000 × 14% = EGP 700,000 VAT
- Pay at customs; claim as input VAT in monthly return (Section H)
- Input credit: EGP 700,000 — full credit if machinery for taxable production

---

### Example 6 — Monthly return summary

**Scenario:** Trading company — April 2025.

| Item | Net (EGP) | VAT (EGP) |
|---|---|---|
| Domestic sales at 14% | 3,000,000 | 420,000 |
| Export sales (0%) | 1,000,000 | 0 |
| Total Output | 4,000,000 | 420,000 |
| Local purchases | 1,500,000 | 210,000 |
| Import VAT (customs) | 2,000,000 | 280,000 |
| Foreign services (reverse-charge) | 200,000 | 28,000 |
| Total Input | 3,700,000 | 518,000 |
| **Excess input c/f** | | **98,000** |

---

## Section 5 — Tier 1 rules (compressed)

**Rate assignment:**
- 14% standard: most goods and services
- 5%: selected equipment and machinery (check ETA reduced-rate schedule)
- 0%: exports of goods with customs declaration, services exported to non-residents consumed outside Egypt, international transport
- Exempt: financial services, insurance, medical services by licensed practitioners, educational services, residential rent, public transport (ENR, metro)

**Input credit:**
- Credit allowed on all taxable purchases for taxable business activities
- No credit on exempt purchases (financial services, insurance)
- Reverse-charge on imported services: output and input net to zero for fully taxable businesses
- Import VAT paid at customs: claim as input in same month's return with customs declaration
- e-Invoice requirement: from October 2020 ETA made e-invoice mandatory — invoices without valid ETA UUID have contested input credit eligibility

**Filing mechanics:**
- File monthly via ETA online portal by last day of following month
- All B2B sales require ETA e-Invoice (UUID-stamped) transmitted to ETA in real time
- Excess input VAT carries forward; refunds available for exporters after ETA audit

---

## Section 6 — Tier 2 catalogue (genuinely data-unknowable items)

| Item | Why unknowable | What to ask |
|---|---|---|
| Reduced-rate machinery (5%) | Whether specific item is on the ministerial reduced-rate schedule | "Provide item description and HS code — need to check ETA 5% schedule." |
| Mixed-use property rent | Commercial (14%) vs residential (exempt) | "Is the lease for commercial or residential use? Provide contract." |
| Export qualification | Whether service consumed outside Egypt | "Where is the customer? Evidence of offshore service consumption?" |
| Foreign digital service | B2B (reverse-charge) vs B2C — determines who accounts | "Is buyer an Egyptian TRN-registered entity?" |
| Vehicle purchase | Business vs personal — determines input credit eligibility | "Is this vehicle registered in the company's name for business use?" |
| Entertainment | Must prove business purpose for input credit | "List attendees and business purpose." |
| e-Invoice validity | Old paper invoices may not qualify for input credit post-mandate | "Confirm supplier is ETA e-Invoice registered — provide UUID reference." |

---

## Section 7 — Excel working paper

**Columns:** Date | Supplier/Customer | TRN | ETA Invoice UUID | Net (EGP) | VAT Rate % | VAT (EGP) | In/Out | Zero-rated? | Exempt? | Tier 2 flag | Notes

**Tab structure:**
1. `Output_Sales` — all sales by rate
2. `Input_Purchases` — all purchases with VAT credit
3. `Import_Customs` — import VAT paid at customs
4. `ReverseCharge_Foreign` — foreign services
5. `VATSummary` — monthly return totals
6. `Tier2_Items` — awaiting client response

**Key formula:**
```
Net_VAT = Total_Output_VAT - Total_Input_VAT - Prior_Excess_Credit
```

---

## Section 8 — Bank statement reading guide

### CIB format
```
Date        : 15/04/2025
Transaction : Credit Transfer
Description : COMPANY NAME — INV-2025-041 — SERVICE DESCRIPTION
Amount      : +EGP 570,000.00
Balance     : EGP 2,570,000.00
```

### NBE (National Bank of Egypt) format
```
15/04/2025  |  Incoming Transfer  |  COMPANY NAME  |  REF: INV-041  |  +570,000.00 EGP
```

### Key patterns:
- **EGP number format:** Comma = thousands; period = decimal (EGP 570,000.00)
- **Foreign Currency Credit:** Foreign payment — check for export zero-rate or reverse-charge
- **Customs Payment:** Import duty + VAT — claim VAT as input with customs declaration
- **SWIFT/Foreign Payment:** May trigger reverse-charge on imported services

---

## Section 9 — Onboarding fallback

When client cannot provide ETA e-Invoices for all transactions:

1. Use bank statement amounts as VAT-inclusive totals and back-calculate:
   - Net = Total ÷ 1.14 | VAT = Total − Net
2. Apply conservative defaults: 14% output; 0% input credit without ETA e-Invoice UUID
3. Flag all items without e-Invoice UUID in Tier2_Items tab
4. Issue data request listing missing invoice references
5. Warn client: ETA can disallow input credit for invoices without valid UUID — systemic risk if supplier not e-Invoice registered

---

## Section 10 — Reference material

| Resource | Reference |
|---|---|
| ETA e-Invoice portal | https://invoicing.eta.gov.eg |
| ETA main portal | https://www.eta.gov.eg |
| VAT Law No. 67 of 2016 | ETA website — legislation section |
| VAT Executive Regulations | Ministerial Decree 2017 |
| ETA e-Invoice mandatory rules | ETA Decree 2020/2021 — phased rollout |
| Reduced rate schedule | Annex to VAT Law — ministerial updates |


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
