---
name: nigeria-vat
description: Use this skill whenever asked to prepare, review, or classify transactions for a Nigeria VAT return or advise on Nigerian VAT registration, filing, and compliance. Trigger on phrases like "prepare Nigeria VAT return", "Nigerian VAT", "FIRS VAT", "Form 002", or any Nigeria VAT request. ALWAYS read this skill before touching any Nigeria VAT work.
version: 2.0
jurisdiction: NG
tax_year: 2025
category: international
depends_on:
  - vat-workflow-base
---

# Nigeria VAT (Value Added Tax) Skill v2.0

---

## Section 1 — Quick reference

| Field | Value |
|---|---|
| Country | Nigeria (Federal Republic of Nigeria) |
| Tax | Value Added Tax (VAT) |
| Currency | NGN (Nigerian Naira — ₦) |
| Standard rate | 7.5% (effective February 2020; previously 5%) |
| Zero rate | 0% (exports of goods and services, goods purchased by diplomats, humanitarian donor organisations) |
| Exempt | Basic food items (unprocessed agricultural products), medical/pharmaceutical products, baby products, newspapers, educational materials, financial services, natural gas, exported services |
| Registration threshold | NGN 25,000,000 annual turnover (from 2020); below this — no obligation to register |
| Tax authority | Federal Inland Revenue Service (FIRS) |
| Filing portal | FIRS TaxPro Max — https://taxpromax.firs.gov.ng |
| Return form | VAT Form 002 (monthly return) |
| Filing frequency | Monthly |
| Deadline | 21st of the following month |
| e-Invoice | FIRS e-Invoice / e-Receipt pilot — expanding from 2024 |
| Contributor | Open Accountants Community |
| Validated by | Pending — requires sign-off by a Nigeria-licensed tax practitioner (CITN) |
| Skill version | 2.0 |

### Key VAT Form 002 lines

| Line | Meaning |
|---|---|
| Line 1 | Total taxable sales (net of VAT) |
| Line 2 | VAT on sales (Line 1 × 7.5%) |
| Line 3 | Zero-rated sales |
| Line 4 | Exempt sales |
| Line 5 | Total input VAT (on purchases for taxable activities) |
| Line 6 | Net VAT payable (Line 2 − Line 5) |
| Line 7 | Excess input VAT carried forward |

### Conservative defaults

| Ambiguity | Default |
|---|---|
| Unknown rate on a sale | 7.5% standard |
| Unknown whether food is processed/unprocessed | Treat as processed — 7.5% until confirmed |
| Unknown whether pharmaceutical is exempt | 7.5% until exemption confirmed with NAFDAC registration |
| Unknown whether export documentation complete | Treat as domestic 7.5% |
| Unknown business-use % | 0% input credit |
| Foreign digital service (B2B) | 7.5% reverse-charge — buyer self-assesses |
| Unknown whether NGN 25M threshold met | Assume must file |

### Red flag thresholds

| Threshold | Value |
|---|---|
| HIGH single transaction | NGN 10,000,000 |
| HIGH tax delta on single conservative default | NGN 750,000 |
| MEDIUM counterparty concentration | >40% of output or input |
| MEDIUM conservative default count | >4 per return |
| LOW absolute net VAT position | NGN 5,000,000 |

---

## Section 2 — Required inputs and refusal catalogue

### Required inputs

Before starting any Nigeria VAT work, obtain:

1. FIRS TIN (Tax Identification Number — 10 digits) and VAT registration certificate
2. Monthly bank statements in NGN (all business accounts)
3. Sales invoices with VAT registration number (VRN) printed
4. Purchase invoices from VAT-registered suppliers with their VRN
5. Prior month VAT return (for carried-forward excess input credit)
6. Export documentation (form NXP, shipping documents) for zero-rated exports
7. Details of exempt supplies (basic foodstuffs, medical goods) with product descriptions

### Refusal catalogue

Refuse and escalate to a CITN-licensed tax practitioner for:
- VAT on imported services — complex FIRS guidance and WHT interaction
- VAT grouping (rare in Nigeria)
- Petroleum Profit Tax (PPT) — separate legislation
- Real estate VAT (complex exemption rules on land vs. buildings)
- VAT refund claims — FIRS refund process is complex and slow; requires specialist
- State-level consumption taxes (Lagos, Rivers) — in addition to federal VAT
- Free trade zone (FTZ) VAT treatment

---

## Section 3 — Supplier pattern library

### 3.1 Banking and financial services

| Supplier | Typical description | VAT rate | Input credit |
|---|---|---|---|
| Guaranty Trust Bank (GTBank) | Bank fees, transfer charges | Exempt | No |
| Zenith Bank | Account maintenance, corporate banking | Exempt | No |
| Access Bank | Business banking fees | Exempt | No |
| First Bank Nigeria | Commercial banking | Exempt | No |
| United Bank for Africa (UBA) | Pan-African banking fees | Exempt | No |
| Stanbic IBTC | Investment banking, advisory | Exempt | No |
| Flutterwave | Payment gateway — processing fee | 7.5% | Yes |
| Paystack | Payment gateway — commission | 7.5% | Yes |
| Interswitch | Card switching, POS services | 7.5% | Yes |
| PalmPay | Mobile payments | Exempt (payment) | No |
| Opay | Digital wallet | Exempt | No |

### 3.2 Electricity and utilities

| Supplier | Typical description | VAT rate | Input credit |
|---|---|---|---|
| Eko Electricity Distribution Company (EKEDC) | Electricity — Lagos Island/mainland south | 7.5% | Yes (business) |
| Ikeja Electric (IKEDC) | Electricity — Lagos Ikeja/mainland north | 7.5% | Yes (business) |
| Abuja Electricity Distribution Company (AEDC) | Electricity — FCT Abuja | 7.5% | Yes (business) |
| Lagos State Water Corporation | Water supply | 7.5% | Yes |
| LSWC / State water boards | Water — various states | 7.5% | Yes |
| Lagos Waste Management Authority (LAWMA) | Waste disposal | 7.5% | Yes |

### 3.3 Telecommunications

| Supplier | Typical description | VAT rate | Input credit |
|---|---|---|---|
| MTN Nigeria | Mobile, data | 7.5% | Yes (business use) |
| Airtel Nigeria | Mobile, broadband | 7.5% | Yes (business use) |
| Glo (Globacom) | Mobile, data | 7.5% | Yes (business use) |
| 9mobile (etisalat) | Mobile, business lines | 7.5% | Yes (business use) |
| IPNX | Fiber internet — enterprise | 7.5% | Yes |
| Spectranet | Fixed wireless broadband | 7.5% | Yes |
| Swift Networks | Enterprise connectivity | 7.5% | Yes |

### 3.4 Transport and travel

| Supplier | Typical description | VAT rate | Input credit |
|---|---|---|---|
| Air Peace | Domestic flights | 7.5% | Yes |
| Ibom Air | Domestic flights | 7.5% | Yes |
| United Nigeria Airlines | Domestic flights | 7.5% | Yes |
| Ethiopian Airlines Nigeria | International flights | 0% (export) | No input applicable |
| Bolt Nigeria | Ride-hailing | 7.5% | Yes (business use) |
| Uber Nigeria | Ride-hailing | 7.5% | Yes (business use) |
| Rensource / Tricycle services | Local transport | 7.5% | Yes |

### 3.5 Logistics and courier

| Supplier | Typical description | VAT rate | Input credit |
|---|---|---|---|
| DHL Nigeria | International courier | 0% (export) / 7.5% (domestic) | Yes |
| FedEx Nigeria | International courier | 0% / 7.5% | Yes |
| GIG Logistics | Domestic courier | 7.5% | Yes |
| ABC Cargo | Domestic freight | 7.5% | Yes |
| Kwik Delivery | Last-mile delivery | 7.5% | Yes |
| NIPOST | Nigerian postal service | 7.5% | Yes |

### 3.6 Retail and office supplies

| Supplier | Typical description | VAT rate | Input credit |
|---|---|---|---|
| Jumia Nigeria | E-commerce marketplace | 7.5% (taxable goods) | Yes (business) |
| Konga | E-commerce | 7.5% | Yes |
| Shoprite Nigeria | Supermarket — food/non-food | Mixed (basic food exempt; other 7.5%) | Partial |
| SPAR Nigeria | Supermarket | Mixed | Partial |
| Staples Nigeria / Office supplies store | Office stationery | 7.5% | Yes |
| Dangote Industries (cement) | Building materials | 7.5% | Yes |
| Copy Shop / printing | Document printing | 7.5% | Yes |

### 3.7 Software and digital services

| Supplier | Typical description | VAT rate | Input credit |
|---|---|---|---|
| Sage Nigeria | Accounting software | 7.5% | Yes |
| VFD Tech / Mono | Fintech API | 7.5% | Yes |
| Microsoft Nigeria (Azure, M365) | Cloud services — B2B | 7.5% (reverse-charge) | Yes |
| Google Nigeria (Workspace, Ads) | Digital services — B2B | 7.5% (reverse-charge) | Yes |
| Zoom Nigeria | Video conferencing — B2B | 7.5% (reverse-charge) | Yes |
| AWS Nigeria | Cloud infrastructure — B2B | 7.5% (reverse-charge) | Yes |
| Zoho Nigeria | Business software | 7.5% (reverse-charge if foreign) | Yes |

### 3.8 Professional services

| Supplier | Typical description | VAT rate | Input credit |
|---|---|---|---|
| Chartered Accountant (ICAN/ANAN) | Audit, tax advisory | 7.5% | Yes |
| Law firm | Legal services | 7.5% | Yes |
| Consulting firm | Management consulting | 7.5% | Yes |
| Advertising agency | Marketing services | 7.5% | Yes |
| CITN-registered tax practitioner | Tax compliance | 7.5% | Yes |

### 3.9 Insurance

| Supplier | Typical description | VAT rate | Input credit |
|---|---|---|---|
| AIICO Insurance | Business insurance | Exempt | No |
| Leadway Assurance | Property, liability | Exempt | No |
| AXA Mansard | Health, motor | Exempt | No |
| Cornerstone Insurance | All lines | Exempt | No |
| Stanbic IBTC Insurance | Life, annuity | Exempt | No |

### 3.10 Basic foodstuffs and exempt goods

| Supplier | Typical description | VAT rate | Input credit |
|---|---|---|---|
| Unprocessed agricultural produce (farm direct) | Rice, yam, vegetables — unprocessed | Exempt | No |
| Processed food manufacturers (e.g., Nestle, Cadbury) | Processed packaged food | 7.5% | Yes |
| Baby products (Pampers, etc.) | Diapers, formula | Exempt | No |
| Pharmaceutical manufacturers | Medicines — registered with NAFDAC | Exempt | No |
| Newspapers / educational textbooks | Print media, school books | Exempt | No |

---

## Section 4 — Worked examples

### Example 1 — Standard VAT on consulting service

**Scenario:** Lagos-based IT firm issues invoice to Nigerian corporate client.

**Bank statement line (GTBank format):**
```
Date        : 15/04/2025
Narration   : CREDIT TRANSFER — ACME CORP LTD — INV-2025-041 — IT CONSULTING
Amount      : +NGN 5,375,000.00
Balance     : NGN 25,375,000.00
```

**Working:**
- Invoice: net NGN 5,000,000 + VAT 7.5% NGN 375,000 = NGN 5,375,000
- Return entry: Line 1 — NGN 5,000,000 | Output VAT: NGN 375,000

---

### Example 2 — Exempt basic food sale

**Scenario:** Agricultural trader sells unprocessed yams to market.

**Bank statement line (Zenith Bank format):**
```
Date        : 10/04/2025
Description : PAYMENT — ALABA MARKET TRADERS — FARM PRODUCE SUPPLY
Reference   : INV-AGR-2025-010
Amount      : +NGN 2,000,000.00
```

**Working:**
- Unprocessed agricultural produce — exempt from VAT
- Return entry: Line 4 (Exempt) — NGN 2,000,000 | VAT: NGN 0
- No output VAT; no input credit on related purchases

---

### Example 3 — Electricity bill (business premises)

**Scenario:** Company pays EKEDC electricity bill for April 2025.

**Bank statement line (Access Bank format):**
```
Date        : 25/04/2025
Narration   : EKEDC BILL PAYMENT — APRIL 2025 — ACCT: 0123456789
Amount      : -NGN 2,150,000.00
```

**Working:**
- EKEDC invoice: net NGN 2,000,000 + VAT 7.5% NGN 150,000 = NGN 2,150,000
- 100% business use (office premises)
- Return entry: Line 5 (Input VAT) — NGN 150,000

---

### Example 4 — Reverse-charge on foreign digital service

**Scenario:** Company pays for Microsoft Azure (billed from Microsoft Ireland).

**Bank statement line (First Bank format):**
```
Date        : 05/04/2025
Narration   : INTL PAYMENT — MICROSOFT IRELAND — AZURE SERVICES APR 2025
Amount      : -NGN 11,200,000.00
```

**Working:**
- Foreign digital service to Nigerian business — self-assess VAT under FIRS guidance
- Self-assess: NGN 11,200,000 × 7.5/107.5 = NGN 781,395 VAT
- Declare as output AND claim as input — net zero for fully taxable business

---

### Example 5 — Export of software (zero-rated)

**Scenario:** Nigerian tech company exports software license to UK client.

**Bank statement line (UBA format):**
```
Date        : 20/04/2025
Narration   : SWIFT CREDIT — UK TECH LTD — SOFTWARE LICENSE Q1 2025
Amount      : +NGN 15,000,000.00 (USD 9,000)
```

**Working:**
- Export of service to non-resident — zero-rated
- Requires: contract, foreign bank transfer evidence, NXP form
- Return entry: Line 3 (Zero-rated) — NGN 15,000,000 | VAT: NGN 0

---

### Example 6 — Monthly return summary

**Scenario:** Manufacturing company — April 2025.

| Item | Net (NGN) | VAT (NGN) |
|---|---|---|
| Domestic taxable sales | 50,000,000 | 3,750,000 |
| Export sales (0%) | 20,000,000 | 0 |
| Exempt sales (basic food) | 10,000,000 | 0 |
| Total Output | 80,000,000 | 3,750,000 |
| Input on taxable purchases | 30,000,000 | 2,250,000 |
| **Net VAT payable** | | **1,500,000** |

---

## Section 5 — Tier 1 rules (compressed)

**Rate assignment:**
- 7.5% standard: all goods and services not specifically exempt or zero-rated
- 0%: exports of goods and services with proper documentation, diplomatic purchases, goods for humanitarian organisations
- Exempt: basic unprocessed food items, medical/pharmaceutical products (NAFDAC-registered), baby products, financial services, insurance, educational materials (not stationery), newspapers, natural gas (domestic), exported services

**Input credit:**
- Credit allowed on VAT paid on purchases used for taxable activities
- Must have valid VAT invoice from VAT-registered supplier (with their VRN)
- No credit on exempt purchases or purchases unrelated to taxable activities
- No credit if supplier is below the NGN 25M registration threshold (they should not be charging VAT)
- Reverse-charge on foreign digital services: output and input net to zero for fully taxable businesses

**Filing mechanics:**
- File VAT Form 002 monthly via FIRS TaxPro Max by 21st of following month
- Also file WHT returns if subject to withholding — separate form
- Excess input VAT carries forward; FIRS refunds are slow — expect 90+ days
- Remit VAT collected from customers to FIRS monthly (not annual)

---

## Section 6 — Tier 2 catalogue (genuinely data-unknowable items)

| Item | Why unknowable | What to ask |
|---|---|---|
| Food product classification | Processed (7.5%) vs unprocessed/basic (exempt) depends on product detail | "Is this raw agricultural produce or processed/packaged food? NAFDAC registration?" |
| Pharmaceutical exemption | Only NAFDAC-registered medicines exempt | "What is the product? Provide NAFDAC registration number." |
| Export documentation | Zero-rate requires NXP form, shipping docs | "Provide export documentation — NXP form and freight evidence." |
| Foreign digital service | B2B (reverse-charge) vs B2C | "Is the Nigerian entity VAT-registered? Does supplier have your TIN?" |
| Real estate transaction | Land (exempt) vs building services (7.5%) | "Is this land only, or construction/building services?" |
| Sub-NGN 25M supplier | Should not be charging VAT — no input credit | "Confirm supplier's annual turnover and VAT registration status." |

---

## Section 7 — Excel working paper

**Columns:** Date | Supplier/Customer | VRN | Invoice No. | Net (NGN) | VAT Rate % | VAT (NGN) | In/Out | Zero-rated? | Exempt? | Tier 2 flag | Notes

**Tab structure:**
1. `Output_Sales` — all sales by type (taxable/zero-rated/exempt)
2. `Input_Purchases` — all purchases with VAT credit
3. `ReverseCharge_Foreign` — foreign services
4. `VAT_Summary` — monthly Form 002 totals
5. `Tier2_Items` — awaiting client response

---

## Section 8 — Bank statement reading guide

### GTBank format
```
Date        : 15/04/2025
Narration   : CREDIT TRANSFER — COMPANY NAME — INV-2025-041 — DESCRIPTION
Amount      : +NGN 5,375,000.00
Balance     : NGN 25,375,000.00
```

### Zenith Bank format
```
15/04/2025  |  TRF FROM ACME CORP  |  +5,375,000.00  |  BAL: 25,375,000.00
```

### Key patterns:
- **NGN number format:** Comma = thousands; period = decimal (NGN 5,375,000.00)
- **INTL PAYMENT / SWIFT:** Foreign payment — check for export zero-rate or reverse-charge
- **BILL PAYMENT:** Utility payments — usually include VAT; request invoice
- **CREDIT TRANSFER:** Domestic wire — match to issued invoice for output VAT

---

## Section 9 — Onboarding fallback

When client cannot provide VAT invoices for all transactions:

1. Use bank statement amounts as VAT-inclusive totals and back-calculate:
   - Net = Total ÷ 1.075 | VAT = Total − Net
2. Apply conservative defaults: 7.5% output on all unverified taxable sales; 0% input credit without valid VRN invoice
3. Flag all items without VRN invoices in Tier2_Items tab
4. Issue data request listing missing invoice references
5. Warn client: FIRS can disallow input credit claims without valid VAT invoices from registered suppliers

---

## Section 10 — Reference material

| Resource | Reference |
|---|---|
| FIRS TaxPro Max (filing portal) | https://taxpromax.firs.gov.ng |
| FIRS main portal | https://www.firs.gov.ng |
| VAT Act (as amended by Finance Act 2019/2020) | FIRS website — legislation |
| Finance Act 2020 — VAT rate increase to 7.5% | Official Gazette |
| VAT registration threshold guidance | FIRS circular 2020 |
| FIRS e-Invoice pilot | FIRS announcements — 2024 |
