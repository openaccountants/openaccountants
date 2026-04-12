---
name: turkey-vat
description: Use this skill whenever asked to prepare, review, or classify transactions for a Turkey VAT (KDV — Katma Değer Vergisi) return or advise on Turkish VAT registration, filing, and reporting. Trigger on phrases like "prepare KDV return", "Turkish VAT", "KDV beyannamesi", "ÖKC fatura", or any Turkey VAT request. ALWAYS read this skill before touching any Turkey KDV-related work.
version: 2.0
jurisdiction: TR
tax_year: 2025
category: international
depends_on:
  - vat-workflow-base
---

# Turkey VAT (KDV — Katma Değer Vergisi) Skill v2.0

---

## Section 1 — Quick reference

| Field | Value |
|---|---|
| Country | Turkey (Türkiye Cumhuriyeti) |
| Tax | Katma Değer Vergisi (KDV) |
| Currency | TRY (Turkish Lira) |
| Standard rate | 20% (effective 10 July 2023; previously 18%) |
| Reduced rates | 10% (food, medicines, medical equipment, hotels, restaurants); 1% (basic foodstuffs, agricultural goods, residential property sales) |
| Zero rate | 0% (exports, diplomatic supplies, international transport) |
| Exempt | Financial services, insurance, education, healthcare, land sales, certain capital market transactions |
| Registration threshold | No threshold — any business making taxable supplies must register |
| Tax authority | Gelir İdaresi Başkanlığı (GİB) — Revenue Administration |
| Filing portal | İnteraktif Vergi Dairesi — https://ivd.gib.gov.tr |
| Return form | KDV Beyannamesi (1 No'lu KDV Beyannamesi for monthly; 2 No'lu for withholding) |
| Filing frequency | Monthly (all registered businesses) |
| Deadline | 28th of the following month (electronic filing via GİB) |
| E-invoice | e-Fatura mandatory for businesses exceeding TRY 3M annual turnover; e-Arşiv for others |
| Contributor | Open Accountants Community |
| Validated by | Pending — requires sign-off by a Turkey-licensed YMM (Yeminli Mali Müşavir) |
| Skill version | 2.0 |

### Key return form boxes

| Box | Meaning |
|---|---|
| 101 | Taxable sales at 20% (net) |
| 102 | Taxable sales at 10% (net) |
| 103 | Taxable sales at 1% (net) |
| 104 | Zero-rated exports (net) |
| 105 | Exempt supplies (net) |
| 106 | Total output KDV (calculated) |
| 107 | Input KDV deductible (purchases at 20%) |
| 108 | Input KDV deductible (purchases at 10%) |
| 109 | Input KDV deductible (purchases at 1%) |
| 110 | Reverse-charge KDV (services from abroad — 2 No'lu beyanname) |
| 111 | Total input KDV (calculated) |
| 112 | KDV payable (106 − 111; if positive) |
| 113 | Excess input KDV carried forward (if 111 > 106) |

### Conservative defaults

| Ambiguity | Default |
|---|---|
| Unknown rate on a sale | 20% standard |
| Unknown whether food qualifies for 10% | 20% until confirmed |
| Unknown whether basic foodstuff qualifies for 1% | 10% until confirmed |
| Unknown whether export documentation complete | Treat as domestic 20% |
| Unknown business-use % (vehicle, phone, home) | 0% input credit |
| Unknown whether e-Fatura issued | Assume not issued — flag for compliance |
| Foreign digital service (B2B vs B2C) | B2B — buyer self-assesses via 2 No'lu beyanname |

### Red flag thresholds

| Threshold | Value |
|---|---|
| HIGH single transaction | TRY 500,000 |
| HIGH tax delta on single conservative default | TRY 50,000 |
| MEDIUM counterparty concentration | >40% of output or input |
| MEDIUM conservative default count | >4 per return |
| LOW absolute net KDV position | TRY 1,000,000 |

---

## Section 2 — Required inputs and refusal catalogue

### Required inputs

Before starting any Turkey KDV work, obtain:

1. GİB taxpayer number (Vergi Kimlik Numarası — VKN, 10 digits) or TC ID for sole traders
2. KDV registration certificate confirming registration status and type
3. Monthly bank statements in TRY (all accounts used for business)
4. e-Fatura / e-Arşiv Fatura downloads from GİB portal (gib.gov.tr/efatura) — XML or PDF
5. Supplier invoices with VKN, KDV rate, and ÖKC (POS) receipts for retail purchases
6. Import documents (Gümrük beyannamesi — customs declarations) for imported goods
7. Prior month KDV return (for carried-forward excess input credit)
8. 2 No'lu KDV beyannamesi data for any foreign digital/service purchases

### Refusal catalogue

Refuse and escalate to a YMM for:
- Partial exemption calculations (businesses with mixed taxable/exempt supplies)
- KDV withholding (tevkifat) — special rules for construction, cleaning, security, scrap metal
- Intra-group transactions and transfer pricing KDV implications
- Tourism VAT refund scheme (Türkiye'ye gelen yabancılara KDV iadesi)
- Capital goods KDV adjustment scheme (Düzeltme)
- KDV exemption certificates (İstisna belgesi) for exporters
- Özel Matrah (special taxable base) — used for auctions, used vehicles, gold
- Investment incentive certificates (Yatırım Teşvik Belgesi) KDV exemptions

---

## Section 3 — Supplier pattern library

### 3.1 Banking and payment processors

| Supplier | Typical description | KDV rate | Input credit |
|---|---|---|---|
| İş Bankası (Türkiye İş Bankası A.Ş.) | BSMV — Banka Sigorta Muameleleri Vergisi | Exempt (BSMV not KDV) | No |
| Garanti BBVA | Bank fees, wire transfer charges | Exempt | No |
| Akbank | Account maintenance, EFT fees | Exempt | No |
| Ziraat Bankası | State bank — loan interest, fees | Exempt | No |
| Halkbank | SME banking fees | Exempt | No |
| VakıfBank | Mortgage, commercial banking | Exempt | No |
| Yapı Kredi Bankası (YKB) | Credit card processing fees | Exempt | No |
| Papara | Digital wallet — transfer fees | Exempt (payment service) | No |
| İyzico | Payment gateway — commission | 20% | Yes |
| PayTR | E-commerce payment processing | 20% | Yes |

### 3.2 Electricity and utilities

| Supplier | Typical description | KDV rate | Input credit |
|---|---|---|---|
| TEDAŞ (Türkiye Elektrik Dağıtım A.Ş.) | Electricity distribution | 20% | Yes (business use) |
| BAŞKENT EDAŞ / ENERJİSA | Electricity — Ankara/Central | 20% | Yes (business use) |
| IGDAŞ / BAŞKENTGAZ | Natural gas — Istanbul/Ankara | 20% | Yes (business use) |
| İSKİ (İstanbul Su ve Kanalizasyon İdaresi) | Water — Istanbul | 1% | Yes (business use) |
| ASKİ (Ankara Su ve Kanalizasyon İdaresi) | Water — Ankara | 1% | Yes (business use) |

### 3.3 Telecommunications

| Supplier | Typical description | KDV rate | Input credit |
|---|---|---|---|
| Turkcell | Mobile, data, roaming | 20% | Yes (business use) |
| Vodafone Turkey | Mobile, business lines | 20% | Yes (business use) |
| Türk Telekom | Fixed line, fiber internet, mobile | 20% | Yes (business use) |
| Türksat | Satellite TV (if business subscription) | 20% | Yes |

### 3.4 Transport and travel

| Supplier | Typical description | KDV rate | Input credit |
|---|---|---|---|
| Türk Hava Yolları (THY — Turkish Airlines) | Domestic flights | 10% | Yes |
| Türk Hava Yolları (THY) | International flights | 0% (export) | No input credit applicable |
| Pegasus Airlines | Domestic flights | 10% | Yes |
| AnadoluJet | Domestic budget flights | 10% | Yes |
| TCDD (Türkiye Cumhuriyeti Devlet Demiryolları) | Train tickets | 10% | Yes |
| İstanbul Metro / Metrobüs (İETT) | Public transit — İstanbul | 1% | Yes (business use) |
| Uber Turkey | Ride-hailing | 10% | Yes (business use only) |
| BiTaksi | Turkish taxi app | 10% | Yes (business use only) |

### 3.5 Logistics and courier

| Supplier | Typical description | KDV rate | Input credit |
|---|---|---|---|
| Yurtiçi Kargo | Domestic courier | 20% | Yes |
| MNG Kargo | Domestic courier | 20% | Yes |
| Aras Kargo | Domestic courier | 20% | Yes |
| PTT Kargo (Posta ve Telgraf Teşkilatı) | State postal service | 20% | Yes |
| DHL Turkey | International courier | 0% (export) / 20% (domestic) | Yes |
| UPS Turkey | International courier | 0% (export) / 20% (domestic) | Yes |

### 3.6 Retail and office supplies

| Supplier | Typical description | KDV rate | Input credit |
|---|---|---|---|
| BİM (Birleşik Mağazacılık) | Grocery — basic foodstuffs | 1%/10% mixed | Partial |
| A101 | Discount grocery retail | 1%/10%/20% mixed | Partial |
| Migros | Supermarket — mixed goods | 1%/10%/20% mixed | Partial |
| Teknosa | Electronics retailer | 20% | Yes |
| Media Markt Turkey | Electronics | 20% | Yes |
| Kırtasiyeci / Ofis Depot | Office supplies | 20% | Yes |

### 3.7 Software and digital services

| Supplier | Typical description | KDV rate | Input credit |
|---|---|---|---|
| Foriba | e-Fatura integration platform | 20% | Yes |
| Logo Yazılım | ERP/accounting software (Turkish) | 20% | Yes |
| Mikro Yazılım | SME accounting software | 20% | Yes |
| Nebim Winner | Retail ERP | 20% | Yes |
| Microsoft Turkey (Azure, M365) | Cloud services — B2B | 20% (buyer self-assesses) | Yes (via 2 No'lu) |
| Google Turkey (Workspace, Ads) | Digital services — B2B | 20% (buyer self-assesses) | Yes (via 2 No'lu) |
| Zoom Turkey | Video conferencing — B2B | 20% (buyer self-assesses) | Yes (via 2 No'lu) |
| Amazon Web Services (AWS) Turkey | Cloud — B2B | 20% (buyer self-assesses) | Yes (via 2 No'lu) |

### 3.8 Professional services

| Supplier | Typical description | KDV rate | Input credit |
|---|---|---|---|
| Serbest Muhasebeci Mali Müşavir (SMMM) | Accounting and tax advisory | 20% | Yes |
| Avukatlık bürosu | Legal services | 20% | Yes |
| Mühendislik / Mimarlık bürosu | Engineering/architecture consulting | 20% | Yes |
| Reklam ajansı | Advertising agency | 20% | Yes |
| Yeminli Mali Müşavir (YMM) | Certified public accountant | 20% | Yes |

### 3.9 Insurance

| Supplier | Typical description | KDV rate | Input credit |
|---|---|---|---|
| Allianz Turkey | Property, vehicle, liability insurance | Exempt (BSMV applies) | No |
| Axa Sigorta | Insurance premiums | Exempt | No |
| Güneş Sigorta | Insurance premiums | Exempt | No |
| Mapfre Turkey | Insurance premiums | Exempt | No |

### 3.10 Healthcare

| Supplier | Typical description | KDV rate | Input credit |
|---|---|---|---|
| Özel hastane (private hospital) | Medical treatment | Exempt | No |
| Eczane (pharmacy) | Medicines (prescription) | 1% | Yes |
| Medikal malzeme (medical devices) | Medical equipment | 10% | Yes |

---

## Section 4 — Worked examples

### Example 1 — Standard KDV on domestic sale

**Scenario:** IT consulting firm (İstanbul) issues invoice to Turkish corporate client.

**Bank statement line (Garanti BBVA format):**
```
Tarih       : 15/04/2025
İşlem       : Havale/EFT Alındı
Açıklama    : YAZILIM DANIŞMANLIK HİZMETİ - FATURA NO: YD-2025-041
Tutar       : +240.000,00 TRY
```

**Working:**
- Invoice net: TRY 200,000.00
- KDV 20%: TRY 40,000.00
- Invoice total: TRY 240,000.00
- Return entry: Box 101 — TRY 200,000 | Output KDV: TRY 40,000

---

### Example 2 — Reverse-charge on foreign digital service (2 No'lu)

**Scenario:** Company subscribes to Microsoft Azure (monthly billing from Ireland entity).

**Bank statement line (İş Bankası format):**
```
Tarih       : 01/04/2025
İşlem Türü  : Yurt Dışı Ödeme
Alıcı       : MICROSOFT IRELAND OPERATIONS LTD
Açıklama    : AZURE CLOUD SERVICES - INV#MS-2025-04
Tutar       : -18.000,00 TRY
```

**Working:**
- Service: cloud hosting from foreign provider — taxable in Turkey where customer is established
- File 2 No'lu KDV Beyannamesi: Box 110 — TRY 18,000 base; KDV 20% = TRY 3,600
- Simultaneously claim TRY 3,600 as input in 1 No'lu return (net zero effect for fully taxable business)

---

### Example 3 — Reduced rate (10%) restaurant purchase

**Scenario:** Client pays restaurant bill for business lunch.

**Bank statement line (Yapı Kredi format):**
```
Tarih       : 12/04/2025
Kanal       : POS
Açıklama    : ASITANE RESTAURANT ISTANBUL
Tutar       : -2.200,00 TRY
```

**Working:**
- Receipt shows: net TRY 2,000 + KDV 10% TRY 200 = TRY 2,200
- Input KDV: TRY 200 — deductible if business meal documented with attendees
- Return entry: Box 108 — TRY 2,000 purchase; Input KDV TRY 200

---

### Example 4 — Domestic export (0%)

**Scenario:** Software company exports SaaS to a US client. Payment received from abroad.

**Bank statement line (Akbank format):**
```
Tarih       : 20/04/2025
İşlem       : Swift / Döviz Alındı
Açıklama    : ABC TECHNOLOGIES INC USA - SAAS SUBSCRIPTION APR2025
Tutar       : +750.000,00 TRY (USD 25.000)
```

**Working:**
- Export of service to non-Turkey entity used and enjoyed outside Turkey — 0% KDV
- Requires export declaration or service export exemption certificate (İhracat istisnası belgesi)
- Return entry: Box 104 — TRY 750,000 | KDV: TRY 0

---

### Example 5 — Mixed invoice (1% basic food + 20% non-food)

**Scenario:** Client purchases groceries and cleaning products from BİM.

**Bank statement line (Ziraat format):**
```
Tarih       : 08/04/2025
Kanal       : POS Hareketi
Açıklama    : BIM MAGAZALAR A.S. ISTANBUL
Tutar       : -3.500,00 TRY
```

**Working:**
- Fiscal receipt (ÖKC) shows: bread/rice/vegetables TRY 2,000 × 1% KDV = TRY 20; cleaning supplies TRY 1,480 × 20% KDV = TRY 296; Total TRY 3,500
- Input credit if business: TRY 316 (split between Box 109 and Box 107)
- If ÖKC receipt not available: 0% input credit — conservative default

---

### Example 6 — Electricity bill (business premises)

**Scenario:** Office electricity from ENERJİSA for April 2025.

**Bank statement line (Halkbank format):**
```
Tarih       : 25/04/2025
İşlem       : Otomatik Ödeme
Açıklama    : ENERJİSA ELEKTRIK PERAKENDE SATIS — NISAN 2025 FATURU
Tutar       : -36.000,00 TRY
```

**Working:**
- e-Fatura from GİB portal: net TRY 30,000 + KDV 20% TRY 6,000 = TRY 36,000
- 100% business use (office premises) — full input credit
- Return entry: Box 107 — TRY 30,000 | Input KDV: TRY 6,000

---

## Section 5 — Tier 1 rules (compressed)

**Rate assignment:**
- 20% standard: most goods and services not listed below
- 10%: food/non-alcoholic beverages (restaurant/café service), hotels, medicines, medical equipment, domestic airline tickets, train tickets, tourism services
- 1%: basic foodstuffs (bread, rice, pasta, flour, sugar, salt, fresh fruit/veg), residential property first sale, agricultural goods
- 0%: exports of goods with customs declaration, services exported to non-residents used outside Turkey, international transport
- Exempt: financial services (BSMV applies instead), insurance (BSMV), medical treatment, education, leasing of residential property, land sales, social services

**Input credit:**
- Credit allowed on all taxable purchases used for taxable business activities
- No credit on exempt purchases (e.g., financial services)
- No credit on personal/non-business expenditure
- Vehicle purchase: input credit blocked for private passenger cars (binek otomobil); allowed for commercial vehicles (ticari araç)
- Entertainment: fully deductible if documented; 50% blocked if personal element present
- 2 No'lu reverse-charge: output and input net to zero for fully taxable businesses

**Filing mechanics:**
- File 1 No'lu KDV Beyannamesi monthly via GİB İnteraktif Vergi Dairesi by 28th
- File 2 No'lu KDV Beyannamesi in same month as the foreign service payment
- e-Fatura mandatory above TRY 3M annual turnover — use Foriba, Logo, or GİB's free portal
- Excess input KDV carries forward indefinitely (refund rarely granted for domestic supplies)
- Export KDV refund (iade): available for exporters with sustained credit position — requires YMM certification

---

## Section 6 — Tier 2 catalogue (genuinely data-unknowable items)

These items require specific facts from the client before classification. Do not guess.

| Item | Why unknowable | What to ask |
|---|---|---|
| Vehicle purchase/lease | Binek otomobil (private car) has blocked input KDV; ticari araç (commercial) does not — requires registration document (ruhsat) | "What is the vehicle's registration type — binek or ticari? Provide ruhsat." |
| Home office expenses | KDV input credit only for business portion — ratio unknown | "What % of your home is used exclusively for business?" |
| Mobile phone contract | Personal vs business use split | "Is this a dedicated business line? What % business use?" |
| Restaurant/entertainment | Documentation requirements — must prove business purpose and attendees | "Who attended? What was the business purpose?" |
| Mixed-use property purchase | Residential (exempt) vs commercial (taxable) classification | "Is the property classified as residential or commercial in the tapu (title deed)?" |
| Export qualification | Whether service actually used and enjoyed outside Turkey | "Where is the client located? Do you have evidence they used the service outside Turkey?" |
| Software subscription (foreign) | B2B (buyer self-assesses) vs B2C — depends on whether buyer is a KDV-registered business | "Does the supplier have your VKN on file? Are you receiving a B2B invoice?" |
| Agricultural goods | 1% rate applies only to specific listed products — item detail needed | "What specific agricultural products were purchased? Provide itemised receipt." |

---

## Section 7 — Excel working paper

**Columns:** Date | Supplier Name | VKN | Invoice No | e-Fatura? (Y/N) | Net Amount (TRY) | KDV Rate % | KDV Amount (TRY) | Return Box | Input/Output | Tier 2 flag | Notes

**Tab structure:**
1. `Output_Sales` — all sales by KDV rate
2. `Input_Purchases_Local` — domestic purchases
3. `Input_ReverseCharge` — foreign services (2 No'lu)
4. `KDV_Summary` — box totals feeding into beyanname
5. `Tier2_Items` — flagged items awaiting client response

**Key formula (Box 112 — KDV payable):**
```
=IF(Total_Output_KDV - Total_Input_KDV > 0, Total_Output_KDV - Total_Input_KDV, 0)
```

**Key formula (Box 113 — excess credit c/f):**
```
=IF(Total_Input_KDV - Total_Output_KDV > 0, Total_Input_KDV - Total_Output_KDV, 0)
```

---

## Section 8 — Bank statement reading guide

### Garanti BBVA format
```
Tarih       : 15/04/2025
İşlem       : Havale/EFT Alındı
Açıklama    : YAZILIM DANIŞMANLIK HİZMETİ - FATURA NO: YD-2025-041
Tutar       : +240.000,00 TRY
```
Fields: Tarih (date) | İşlem (transaction type) | Açıklama (description) | Tutar (amount, TRY, comma = decimal)

### İş Bankası format
```
Tarih       : 15/04/2025
İşlem Türü  : Havale Alındı
Açıklama    : DANISMANLIK HIZMET BEDELI FATURA 041/2025
Tutar       : +240.000,00 TRY
Bakiye      : 1.240.000,00 TRY
```

### Ziraat Bankası format
```
Tarih       : 15/04/2025
Kanal       : EFT/Havale
Açıklama    : TICARI DANISMANLIK HIZMETI
Tutar       : +240.000,00 TRY
```

### Key patterns:
- **Turkish number format:** Period = thousands separator; comma = decimal (TRY 240.000,00 = TRY 240,000.00)
- **POS transactions:** Usually show merchant name + city — match to receipt for KDV rate
- **Yurt Dışı Ödeme:** Foreign payment — check if reverse-charge applies (2 No'lu)
- **Otomatik Ödeme:** Direct debit — utility bills, subscriptions; match to e-Fatura
- **EFT/Havale Alındı:** Domestic wire received — match to issued invoice

---

## Section 9 — Onboarding fallback

When client cannot provide e-Fatura / ÖKC receipts:

1. Use bank statement amounts as total (KDV-inclusive) and back-calculate:
   - Net = Total ÷ 1.20 (for 20% rate)
   - Net = Total ÷ 1.10 (for 10% rate)
   - Net = Total ÷ 1.01 (for 1% rate)
2. Apply conservative default for all unverified items: 20% output; 0% input credit
3. Flag every conservative default in the Tier2_Items tab
4. Issue a one-page data request to client listing missing e-Fatura references
5. For clients above TRY 3M turnover missing e-Fatura: escalate — non-compliance risk (GİB can impose penalties of TRY 10,000+ per missing e-Fatura)

---

## Section 10 — Reference material

| Resource | URL / Reference |
|---|---|
| GİB İnteraktif Vergi Dairesi (filing portal) | https://ivd.gib.gov.tr |
| KDV Kanunu (KDV Law No. 3065) | gib.gov.tr — Mevzuat section |
| e-Fatura portal | https://www.efatura.gov.tr |
| KDV rates table (GİB) | gib.gov.tr/kdv-oranlari |
| KDV Genel Uygulama Tebliği | Official Gazette — KDV implementation circular |
| 2 No'lu KDV Beyannamesi guide | GİB official guidance on reverse-charge |
