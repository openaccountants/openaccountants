---
name: turkey-vat
description: Use this skill whenever asked to prepare, review, or advise on a Turkey VAT (KDV) return or any KDV-related classification. Trigger on phrases like "prepare KDV return", "Turkey VAT", "KDV beyannamesi", "Turkish VAT filing", "e-fatura", "tevkifat", or any request involving Turkish VAT obligations. This skill contains the complete Turkish KDV classification rules, rate tables, withholding (tevkifat) mechanics, e-invoice requirements, filing deadlines, and deductibility rules required to produce a correct return. ALWAYS read this skill before touching any Turkey VAT-related work.
---

# Turkey VAT (KDV) Return Preparation Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Turkey (Turkiye) |
| Jurisdiction Code | TR |
| Primary Legislation | KDV Kanunu (Katma Deger Vergisi Kanunu), Law No. 3065 of 25 October 1984 |
| Supporting Legislation | Income Tax Law No. 193; Corporate Tax Law No. 5520; Tax Procedure Law No. 213; Special Consumption Tax (OTV) Law No. 4760; Presidential Decrees on KDV rates |
| Tax Authority | Gelir Idaresi Baskanligi (GIB -- Revenue Administration, under the Ministry of Treasury and Finance) |
| Filing Portal | https://ebeyanname.gib.gov.tr (Interactive Tax Office) |
| Validated By | Deep research verification, April 2026 |
| Validation Date | April 2026 |
| Skill Version | 1.0 |
| Confidence Coverage | Tier 1: rate classification, return box assignment, reverse charge, e-invoice rules. Tier 2: tevkifat rates, partial exemption, sector-specific rules. Tier 3: group structures, free trade zones, investment incentive certificates. |

---

## Confidence Tier Definitions

Every rule in this skill is tagged with a confidence tier:

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Flag the issue and present options. A qualified tax adviser must confirm before filing.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Skill does not cover this. Do not guess. Escalate to qualified tax adviser and document the gap.

---

## Step 0: Client Onboarding Questions

Before classifying ANY transaction, you MUST know these facts about the client. Ask if not already known:

1. **Entity name and tax identification number (VKN or TCKN)** [T1] -- VKN is 10 digits for legal entities; TCKN is 11 digits for individuals
2. **Registration type** [T1] -- Standard taxpayer, simplified (basit usul), or exempt
3. **KDV period** [T1] -- Monthly (standard for all KDV taxpayers)
4. **Industry/sector** [T2] -- Impacts tevkifat (withholding) obligations and exemption eligibility
5. **Does the business make exempt supplies?** [T2] -- If yes, partial attribution required (Article 30/33 of KDV Kanunu)
6. **Is the client subject to e-fatura (e-invoice) requirements?** [T1] -- Mandatory above gross revenue threshold (currently TRY 3M for 2024 onwards)
7. **Is the client subject to e-arsiv fatura requirements?** [T1] -- Mandatory for all e-fatura users
8. **Does the client operate in a free trade zone (serbest bolge)?** [T3] -- Special rules apply; escalate
9. **Does the client hold an investment incentive certificate (yatirim tesvik belgesi)?** [T3] -- KDV exemptions may apply
10. **Credit carried forward from prior period** [T1] -- Sonraki Doneme Devreden KDV

**If any of items 1-3 are unknown, STOP. Do not classify any transactions until confirmed.**

---

## Step 1: Transaction Classification Rules

### 1a. Determine Transaction Type [T1]

- Sale (output KDV -- Hesaplanan KDV) or Purchase (input KDV -- Indirilecek KDV)
- Salaries (ucret), social security contributions (SGK), tax payments, loan repayments, dividends = OUT OF SCOPE (never on KDV return)
- **Legislation:** KDV Kanunu, Article 1 (scope of KDV)

### 1b. Determine Counterparty Location [T1]

- **Domestic (Turkey):** Supplier/customer is in Turkey
- **EU:** Turkey is NOT an EU member state. EU countries are treated as foreign (non-EU)
- **Foreign:** All countries outside Turkey
- **Note:** Turkey has a Customs Union with the EU for industrial goods, but this does NOT affect KDV treatment on the return
- **Legislation:** KDV Kanunu, Article 1(2) (imports), Article 6 (place of supply)

### 1c. Determine KDV Rate [T1]

| Rate | Category | Legal Basis |
|------|----------|-------------|
| 20% | Standard rate (genel oran) | Presidential Decree; KDV Kanunu Article 28 |
| 10% | Reduced rate (indirimli oran I) | List II of Council of Ministers Decree |
| 1% | Super-reduced rate (indirimli oran II) | List I of Council of Ministers Decree |
| 0% | Zero-rated (exports, international transport) | KDV Kanunu Article 11, 14, 15 |

**Rate history:** The standard rate was 18% until 9 July 2023, when it was increased to 20% by Presidential Decree No. 7346. The 8% reduced rate was simultaneously increased to 10%, and the 1% rate was maintained.

### 1d. Standard Rate (20%) Applies To [T1]

- All goods and services not listed in List I or List II
- Professional services (legal, accounting, consulting, engineering)
- Telecommunications, software, digital services
- Construction services (unless tevkifat applies)
- Motor vehicles (new)
- Electronics, furniture, clothing (non-basic)
- **Legislation:** KDV Kanunu Article 28; Presidential Decree No. 7346

### 1e. Reduced Rate (10%) Applies To [T1]

- Basic foodstuffs (processed foods, dairy, meat, fish)
- Tourism and accommodation services
- Textile and ready-made garments (basic)
- Books and similar publications (non-periodical)
- Passenger transport (domestic flights, buses)
- Medical devices
- **Legislation:** KDV Kanunu Article 28; List II items

### 1f. Super-Reduced Rate (1%) Applies To [T1]

- Agricultural products (unprocessed: raw cotton, dried hazelnuts, fresh fruits, cereals)
- Newspapers and periodicals
- Second-hand motor vehicles (sold by non-dealers or between individuals)
- Certain financial leasing transactions
- Residential property (net area <= 150 sqm, first delivery) [T2] -- rate depends on property type and location; confirm with adviser
- **Legislation:** KDV Kanunu Article 28; List I items

### 1g. Zero-Rated Supplies (Tam Istisna) [T1]

- Exports of goods (Article 11)
- Export of services (Article 11/1-a) -- service must be performed for a non-resident and benefit must accrue outside Turkey
- International transport (Article 14)
- Supplies to free trade zones (Article 12) [T3]
- Supplies to diplomats and international organizations (Article 15)
- Transit trade (Article 16/1-c)
- **Note:** Zero-rated suppliers can claim full input KDV refund
- **Legislation:** KDV Kanunu Articles 11-15

### 1h. Exempt Supplies (Kismi Istisna -- No Input Recovery) [T1]

- Financial and insurance services (Article 17/4-e)
- Residential property rental (Article 17/4-d)
- Health services by public institutions (Article 17/4-a)
- Education services by public/non-profit institutions (Article 17/1-a)
- Cultural and sporting services by associations (Article 17/1-a)
- Postal services by PTT (Article 17/2-b)
- Sale of real property held for 2+ years by corporate entities (Article 17/4-r) [T2]
- **Note:** Exempt suppliers CANNOT recover input KDV (Article 30/1)
- **Legislation:** KDV Kanunu Article 17

---

## Step 2: KDV Return Structure (KDV Beyannamesi - Form 1)

The monthly KDV-1 return is filed electronically via e-beyanname. The key sections are:

### Section A: Taxable Transactions (Matrah) [T1]

| Line | Description | Notes |
|------|-------------|-------|
| 101 | Deliveries subject to 20% | Standard rate sales |
| 102 | Deliveries subject to 10% | Reduced rate sales |
| 103 | Deliveries subject to 1% | Super-reduced rate sales |
| 104-199 | Other rate categories | Special rates if applicable |
| Hesaplanan KDV | Calculated output KDV | Sum of all rate x base amounts |

### Section B: Exemptions and Non-Taxable Transactions [T1]

| Line | Description | Notes |
|------|-------------|-------|
| 201 | Full exemptions (tam istisna) | Exports (Art 11), international transport (Art 14) |
| 202 | Partial exemptions (kismi istisna) | Art 17 exempt supplies |
| 203 | Non-taxable other transactions | Out-of-scope items reported for information |

### Section C: Reverse Charge / Withholding KDV Received [T1]

| Line | Description | Notes |
|------|-------------|-------|
| 301 | KDV withheld by buyers (tevkifat) | Reported by seller (partial KDV collected) |
| 302 | KDV on imports (declared at customs) | Gumruk KDV |

### Section D: Deductible Input KDV (Indirilecek KDV) [T1]

| Line | Description | Notes |
|------|-------------|-------|
| 401 | Domestic purchases -- input KDV | From invoices with KDV |
| 402 | Import KDV | From customs declarations (gumruk beyannamesi) |
| 403 | Tevkifat KDV (withholding paid as buyer) | Buyer's portion of withheld KDV |
| 404 | Other deductible KDV | Miscellaneous allowable credits |
| 405 | Prior period carry-forward (devreden KDV) | Credit from previous month |

### Section E: KDV Payable or Carry-Forward [T1]

```
Total Output KDV = Hesaplanan KDV (Section A total)
Total Input KDV  = Sum of Section D (401 + 402 + 403 + 404 + 405)

IF Total Output KDV > Total Input KDV THEN
    Odenecek KDV (Payable) = Total Output KDV - Total Input KDV
ELSE
    Sonraki Doneme Devreden KDV (Carry-forward) = Total Input KDV - Total Output KDV
END
```

**Legislation:** KDV Kanunu Article 29 (deduction right), Article 40 (filing obligation)

---

## Step 3: Reverse Charge on Imports and Foreign Services [T1]

### 3a. Import of Goods [T1]

- KDV on imported goods is assessed and collected by Customs (Gumruk Mudurlugu)
- The importer pays KDV at the border via customs declaration (gumruk beyannamesi)
- This import KDV is deductible as input KDV (Line 402)
- **Do NOT self-assess on the KDV return** -- Customs handles assessment
- **Legislation:** KDV Kanunu Article 1/2 (imports taxable), Article 21 (taxable base for imports), Article 29 (import KDV deductible)

### 3b. Import of Services (Reverse Charge) [T1]

- When a Turkey-resident business receives services from a non-resident with no fixed establishment in Turkey:
  1. The Turkish recipient must self-assess KDV via Form KDV-2 (Sorumlu Sifatiyla Beyan)
  2. File KDV-2 by the 24th of the following month
  3. Pay the KDV assessed on KDV-2
  4. Deduct the same amount as input KDV on KDV-1 (Line 404)
  5. Net effect: zero for fully taxable businesses
- **Legislation:** KDV Kanunu Article 9/1 (reverse charge mechanism)

### 3c. KDV-2 Return (Sorumlu Sifatiyla Beyan) [T1]

| Field | Description |
|-------|-------------|
| Purpose | Self-assessment of KDV on services received from non-residents |
| Filing frequency | Monthly (same as KDV-1) |
| Deadline | 24th of the month following the transaction |
| Payment | By 26th of the month following the transaction |
| Input recovery | Deduct on KDV-1 (Line 404) in the same or following period |

---

## Step 4: Withholding KDV (Tevkifat) Mechanism

### 4a. Overview [T1]

Under Article 9 of the KDV Kanunu, certain buyers are required to withhold a portion of the KDV charged by the seller and remit it directly to the tax office. The seller invoices the full KDV but only collects the non-withheld portion.

**Legislation:** KDV Kanunu Article 9; GIB General Communique on KDV Application (KDV Genel Uygulama Tebligi), Section I-C-2

### 4b. Full Withholding (Tam Tevkifat) [T1]

The buyer withholds 100% of the KDV. Applies to:

| Transaction | Buyer Obligation | Legal Basis |
|-------------|-----------------|-------------|
| Services from non-residents (no PE in Turkey) | Withhold 100%, file KDV-2 | Art 9/1 |
| Services from non-residents with a tax representative | Withhold 100% | Art 9/1 |

### 4c. Partial Withholding (Kismi Tevkifat) [T2]

The buyer withholds a fraction of the KDV. Rates vary by service type:

| Service Category | Withholding Rate | Communique Section |
|-----------------|-----------------|-------------------|
| Construction and repair services | 4/10 | I-C-2.1.3.2.1 |
| Landscaping and garden maintenance | 5/10 | I-C-2.1.3.2.2 |
| Cleaning services (temizlik) | 9/10 | I-C-2.1.3.2.4 |
| Security/guarding services (guvenlik) | 9/10 | I-C-2.1.3.2.5 |
| Catering services (yemek) | 5/10 | I-C-2.1.3.2.6 |
| Printing and publishing services | 5/10 | I-C-2.1.3.2.7 |
| Textile and garment manufacturing (fason) | 5/10 | I-C-2.1.3.2.3 |
| Personnel/staffing services | 9/10 | I-C-2.1.3.2.5 |
| Advertising services | 3/10 | I-C-2.1.3.2.15 |
| Waste and scrap metal deliveries | 7/10 | I-C-2.1.3.3.1 |
| Certain metal products | 5/10 | I-C-2.1.3.3.2 |
| Real estate sales by corporates | 5/10 | I-C-2.1.3.3.4 |
| Tour operator services | 5/10 | I-C-2.1.3.2.13 |

**Note:** Partial withholding only applies when the buyer is a designated entity (public bodies, banks, large corporates listed in GIB communique, etc.). If the buyer is not a designated entity, no withholding applies. [T2] -- Always confirm buyer designation status.

### 4d. Tevkifat -- Seller Treatment [T1]

- Seller records full output KDV on invoice
- Seller reports the buyer-withheld portion in Section C (Line 301)
- Seller's net output KDV = Hesaplanan KDV - Tevkifat received
- Seller may claim input KDV refund if in a net credit position due to tevkifat

### 4e. Tevkifat -- Buyer Treatment [T1]

- Buyer withholds the specified fraction of KDV
- Buyer remits the withheld amount via KDV-2 return
- Buyer deducts the withheld amount as input KDV on KDV-1 (Line 403)
- Buyer pays the non-withheld portion to the seller

### 4f. Tevkifat Threshold [T1]

- Partial withholding does NOT apply if the total KDV on the invoice (including KDV) is below TRY 2,000
- **Legislation:** KDV Genel Uygulama Tebligi, Section I-C-2.1.3.4.1

---

## Step 5: E-Invoice and E-Document Requirements

### 5a. E-Fatura (Electronic Invoice) [T1]

| Requirement | Details |
|-------------|---------|
| Mandatory for | Taxpayers with gross revenue >= TRY 3,000,000 (2024 threshold) |
| Transition deadline | Must switch to e-fatura by 1 July of the year following threshold breach |
| Format | UBL-TR (Universal Business Language - Turkey) |
| Transmission | Via GIB e-Fatura portal or registered integrators (ozel entegrator) |
| Storage | 10 years (Tax Procedure Law Article 253) |
| B2B | Mandatory between two e-fatura registered taxpayers |

**Legislation:** Tax Procedure Law (VUK) Article 232; GIB Communique No. 509

### 5b. E-Arsiv Fatura (Electronic Archive Invoice) [T1]

| Requirement | Details |
|-------------|---------|
| Mandatory for | All e-fatura registered taxpayers |
| Use case | Invoices to non-e-fatura registered buyers (individuals, small businesses) |
| Delivery | Can be delivered electronically (email, portal) or printed |
| Threshold for e-arsiv | All taxpayers regardless of revenue (since 1 January 2020) |

### 5c. E-Irsaliye (Electronic Dispatch Note) [T1]

| Requirement | Details |
|-------------|---------|
| Mandatory for | Taxpayers with gross revenue >= TRY 10,000,000 (and specified sectors) |
| Purpose | Electronic waybill for goods in transit |
| Must be issued | Before goods leave the premises |

### 5d. E-Defter (Electronic Ledger) [T1]

| Requirement | Details |
|-------------|---------|
| Mandatory for | All e-fatura registered taxpayers |
| Format | XBRL-GL |
| Filing | Monthly ledger files uploaded to GIB by end of 3rd month following period |

**Legislation:** Tax Procedure Law; GIB Communique No. 509 (consolidated e-document rules)

---

## Step 6: Deductibility Rules

### 6a. General Deduction Right [T1]

- All input KDV on goods and services used for taxable business activities is deductible
- Input KDV must be documented by proper invoice (fatura) or customs declaration
- Deduction right must be exercised within the calendar year of the invoice (or by the January return of the following year)
- **Legislation:** KDV Kanunu Article 29

### 6b. Non-Deductible Input KDV (Article 30) [T1]

The following input KDV is BLOCKED and cannot be recovered:

| Category | Legal Basis | Notes |
|----------|-------------|-------|
| KDV on exempt supplies (kismi istisna) | Art 30/1 | Input KDV for Art 17 exempt activities |
| Motor vehicles (binek otomobil) | Art 30/b | Exception: taxi, rental car businesses, driving schools |
| Expenses not related to business | Art 30/d | Personal expenses |
| Losses not covered by insurance | Art 30/c | Fire, theft, natural disaster losses |
| Entertainment and hospitality | Art 30/d | Business meals, gifts (general rule) |

### 6c. Motor Vehicle Special Rules [T1]

- Input KDV on passenger cars (binek otomobil) is NOT deductible
- Exception: vehicles used directly in the business (taxis, rental cars, delivery vehicles, ambulances)
- Commercial vehicles (ticari arac: trucks, vans, minibuses for goods transport) -- input KDV IS deductible
- **Legislation:** KDV Kanunu Article 30/b

### 6d. Partial Deduction (Pro-Rata) [T2]

- If a business makes both taxable and exempt supplies, input KDV must be apportioned
- Pro-rata formula: `Deductible % = (Taxable Supplies / Total Supplies) x 100`
- Annual adjustment required in January return of the following year
- **Flag for reviewer:** Pro-rata calculation must be confirmed by qualified tax adviser
- **Legislation:** KDV Kanunu Article 33

### 6e. Depreciation of Non-Deductible KDV [T1]

- Non-deductible input KDV must be capitalized as part of the asset cost (for capital goods) or expensed (for operating expenses)
- It is NOT lost -- it becomes a deductible expense for income/corporate tax purposes
- **Legislation:** KDV Kanunu Article 58

---

## Step 7: KDV Refund Mechanism

### 7a. Refund Eligibility [T1]

KDV refunds arise in these situations:

| Situation | Refund Type | Legal Basis |
|-----------|-------------|-------------|
| Exports (tam istisna) | Full refund of input KDV attributable to exports | Art 32 |
| Tevkifat (withholding) excess | Refund of excess input KDV from withheld amounts | Art 9 |
| Reduced rate differential | Input KDV at 20% exceeds output KDV at 1% or 10% | Art 29/2 |
| Investment incentive certificate | KDV on qualifying capital expenditure | Art 13/d |

### 7b. Refund Methods [T1]

| Method | Threshold | Timeline |
|--------|-----------|----------|
| Offset (mahsup) | No minimum | Applied against other tax liabilities immediately |
| Cash refund without audit (YMM report) | Up to TRY 10,000 per period | After tax adviser (YMM) certification |
| Cash refund with audit | Above TRY 10,000 | After full tax audit (may take 3-12 months) |
| Cash refund with bank guarantee | Above TRY 10,000 | Immediate upon bank guarantee, audit follows |

**Legislation:** KDV Kanunu Article 32; KDV Genel Uygulama Tebligi, Section IV

### 7c. Reduced Rate Refund (Indirimli Oran Iade) [T2]

- When sales are predominantly at 1% or 10%, accumulated input KDV credit may grow indefinitely
- Article 29/2 allows a refund of the excess, subject to annual limits set by Presidential Decree
- Minimum threshold: refund only available for amounts exceeding TRY 57,300 (2024; adjusted annually)
- **Flag for reviewer:** Calculation of indirimli oran iade is complex; confirm with tax adviser
- **Legislation:** KDV Kanunu Article 29/2

---

## Step 8: Key Thresholds

| Threshold | Value | Notes |
|-----------|-------|-------|
| Standard KDV rate | 20% | Since 10 July 2023 |
| Reduced KDV rate | 10% | Since 10 July 2023 |
| Super-reduced KDV rate | 1% | Unchanged |
| E-fatura mandatory revenue | TRY 3,000,000 gross revenue | Annual; checked each year-end |
| E-irsaliye mandatory revenue | TRY 10,000,000 | Sector-specific thresholds may be lower |
| Tevkifat minimum invoice amount | TRY 2,000 (including KDV) | Below this, no partial withholding |
| Indirimli oran iade minimum | TRY 57,300 (2024) | Adjusted annually |
| KDV-free small enterprise (basit usul) | Income thresholds per Art 46-48 of Income Tax Law | [T2] Confirm annually |

---

## Step 9: Filing Deadlines

| Return | Period | Filing Deadline | Payment Deadline |
|--------|--------|-----------------|-----------------|
| KDV-1 (Standard return) | Monthly | 28th of the following month | 28th of the following month |
| KDV-2 (Reverse charge / tevkifat) | Monthly | 24th of the following month | 26th of the following month |
| KDV-4 (Occasional / one-off) | Per transaction | 15 days after transaction | 15 days after transaction |
| Annual reconciliation | Calendar year | No separate annual return (monthly filings suffice) | N/A |

**Legislation:** KDV Kanunu Article 40, 41, 46; Tax Procedure Law

**Late filing penalties:**

| Violation | Penalty |
|-----------|---------|
| Late filing | Uselessness penalty (VUK Art 352): TRY 10,000+ (2024 scale) |
| Late payment | Monthly interest at 3.5% (gecikme zammi) |
| Failure to file | Tax assessment by office (resen tarhiyat) + penalty |
| Missing e-fatura | Special uselessness penalty per invoice (VUK Art 353) |

---

## Step 10: Special Consumption Tax (OTV) -- Reference Only [T3]

- OTV (Ozel Tuketim Vergisi) is a separate excise tax under Law No. 4760
- Applies to: motor vehicles, petroleum products, tobacco, alcohol, luxury goods
- OTV is charged ONCE (at production or import), not at each stage like KDV
- OTV is included in the KDV base (i.e., KDV is calculated on price + OTV)
- **Do NOT confuse OTV with KDV.** They are separate taxes with separate returns
- **Legislation:** OTV Kanunu (Law No. 4760)

---

## Step 11: Edge Case Registry

### EC1 -- Software subscription from US provider (e.g., AWS, Google Cloud) [T1]

**Situation:** Turkish business pays for cloud services from a US company, no KDV on invoice.
**Resolution:** Reverse charge via KDV-2. Self-assess at 20%. Deduct as input on KDV-1.
**Legislation:** KDV Kanunu Article 9/1

### EC2 -- Construction services received by a public institution [T2]

**Situation:** Contractor invoices a government ministry for construction work.
**Resolution:** Partial withholding (tevkifat) at 4/10. Ministry withholds 40% of KDV, remits via KDV-2. Contractor reports 60% collected KDV as output.
**Legislation:** KDV Genel Uygulama Tebligi I-C-2.1.3.2.1

### EC3 -- Export of goods via customs [T1]

**Situation:** Turkish manufacturer sells goods to a US buyer, goods cleared through customs.
**Resolution:** Zero-rated (tam istisna). Report net amount in Line 201. No output KDV. Claim input KDV refund. Must have customs export declaration (gumruk cikis beyannamesi) as proof.
**Legislation:** KDV Kanunu Article 11/1-a

### EC4 -- Purchase of passenger car [T1]

**Situation:** Business purchases a sedan for management use.
**Resolution:** Input KDV is BLOCKED under Article 30/b. KDV becomes part of the cost of the asset (capitalized). Deductible for income/corporate tax via depreciation.
**Legislation:** KDV Kanunu Article 30/b, Article 58

### EC5 -- Rental of commercial property [T1]

**Situation:** Business rents an office space from a landlord.
**Resolution:** Commercial property rental is subject to KDV at 20%. Input KDV is deductible. If landlord is a real person (gercek kisi), tenant must withhold 100% of KDV via KDV-2.
**Legislation:** KDV Kanunu Article 1/3-f; Article 9

### EC6 -- Sale of real property held for 2+ years [T2]

**Situation:** Corporate entity sells a building held for more than 2 years.
**Resolution:** Exempt under Article 17/4-r. No output KDV. But previously deducted input KDV on the property must be reversed (correction). Flag for reviewer.
**Legislation:** KDV Kanunu Article 17/4-r, Article 30/1

### EC7 -- Cleaning services received by a bank [T1]

**Situation:** Bank receives cleaning services from a contractor.
**Resolution:** Bank is a designated withholding entity. Withhold 9/10 of the KDV. Bank remits withheld KDV via KDV-2. Contractor collects only 1/10 of KDV.
**Legislation:** KDV Genel Uygulama Tebligi I-C-2.1.3.2.4

### EC8 -- Goods purchased from a free trade zone [T3]

**Situation:** Turkish business buys goods from a company in a Turkish free trade zone.
**Resolution:** Complex rules apply. Goods entering Turkey from FTZ are treated as imports. KDV is assessed at customs. Escalate to qualified tax adviser.
**Legislation:** KDV Kanunu Article 16; Free Trade Zones Law No. 3218

### EC9 -- Invoice from EU supplier for goods (Customs Union) [T1]

**Situation:** Turkish business imports industrial goods from Germany.
**Resolution:** Despite the Customs Union, KDV on imports is still assessed at customs. Import KDV (gumruk KDV) is deductible on KDV-1 Line 402. Customs duties may be zero under Customs Union, but KDV still applies.
**Legislation:** KDV Kanunu Article 1/2, Article 21

### EC10 -- Digital services provided by Turkish company to foreign consumer (B2C) [T1]

**Situation:** Turkish software company sells app subscriptions to customers in the EU.
**Resolution:** Export of electronic services. Zero-rated under Article 11/1-a if the customer is abroad AND the benefit accrues outside Turkey. Proof of foreign benefit required.
**Legislation:** KDV Kanunu Article 11/1-a; KDV Genel Uygulama Tebligi II-A

### EC11 -- Donations and free supplies [T2]

**Situation:** Business donates goods to a charity.
**Resolution:** Free delivery of goods is generally treated as a taxable supply (emsal bedel -- deemed supply at market value) under Article 27. However, donations to specific approved institutions may be exempt under Article 17/2-b. Flag for reviewer.
**Legislation:** KDV Kanunu Article 27, Article 17/2-b

### EC12 -- Advance payments received [T1]

**Situation:** Business receives an advance payment before delivering goods.
**Resolution:** KDV is triggered when the advance is received (Article 10/b -- receipt of payment triggers tax point). Must issue invoice and report output KDV in the month of receipt.
**Legislation:** KDV Kanunu Article 10/b

---

## Step 12: Reviewer Escalation Protocol

When a [T2] situation is identified, output:

```
REVIEWER FLAG
Tier: T2
Transaction: [description]
Issue: [what is ambiguous]
Options: [list the possible treatments]
Recommended: [which treatment is most likely correct and why]
Action Required: Qualified tax adviser must confirm before filing.
```

When a [T3] situation is identified, output:

```
ESCALATION REQUIRED
Tier: T3
Transaction: [description]
Issue: [what is outside skill scope]
Action Required: Do not classify. Refer to qualified tax adviser. Document gap.
```

---

## Step 13: Test Suite

### Test 1 -- Standard domestic sale at 20%

**Input:** Turkish company sells consulting services to a Turkish client, net TRY 100,000, KDV TRY 20,000.
**Expected output:** Line 101 matrah = TRY 100,000. Hesaplanan KDV = TRY 20,000. Output KDV reported.

### Test 2 -- Reduced rate sale at 10%

**Input:** Hotel invoices a Turkish guest for accommodation, net TRY 5,000, KDV TRY 500.
**Expected output:** Line 102 matrah = TRY 5,000. Hesaplanan KDV = TRY 500.

### Test 3 -- Export of goods, zero-rated

**Input:** Turkish manufacturer exports textiles to a US buyer, net TRY 200,000, customs declaration obtained.
**Expected output:** Line 201 (tam istisna) = TRY 200,000. No output KDV. Input KDV on related purchases refundable.

### Test 4 -- Import of services, reverse charge

**Input:** Turkish company receives legal services from a UK law firm, GBP 5,000 (approx. TRY 210,000). No KDV on invoice.
**Expected output:** KDV-2 filed: matrah TRY 210,000, KDV TRY 42,000 (20%). KDV-1 Line 404 input KDV TRY 42,000. Net effect = zero.

### Test 5 -- Cleaning services with tevkifat (9/10)

**Input:** Bank (designated entity) receives cleaning services, net TRY 50,000, KDV TRY 10,000.
**Expected output:** Bank withholds 9/10 of KDV = TRY 9,000 (remit via KDV-2). Bank pays contractor TRY 50,000 + TRY 1,000 = TRY 51,000. Bank deducts TRY 10,000 as input KDV on KDV-1.

### Test 6 -- Passenger car purchase, blocked input

**Input:** Company purchases sedan, net TRY 1,500,000, KDV TRY 300,000.
**Expected output:** Input KDV of TRY 300,000 is BLOCKED (Article 30/b). Asset capitalized at TRY 1,800,000. No input KDV recovery.

### Test 7 -- Agricultural product sale at 1%

**Input:** Farmer sells raw cotton, net TRY 80,000, KDV TRY 800.
**Expected output:** Line 103 matrah = TRY 80,000. Hesaplanan KDV = TRY 800.

### Test 8 -- Commercial property rental from individual landlord

**Input:** Company rents office from individual, monthly rent TRY 30,000 + KDV TRY 6,000.
**Expected output:** Tenant withholds 100% of KDV (TRY 6,000) via KDV-2. Tenant deducts TRY 6,000 as input KDV on KDV-1.

---

## PROHIBITIONS [T1]

- NEVER confuse KDV with OTV (special consumption tax) -- they are separate taxes
- NEVER allow input KDV deduction on passenger vehicles (unless taxi/rental business)
- NEVER skip KDV-2 filing for reverse charge on foreign services
- NEVER apply tevkifat when invoice total (including KDV) is below TRY 2,000
- NEVER apply tevkifat when buyer is not a designated withholding entity
- NEVER treat Customs Union trade as KDV-free -- KDV still applies at import
- NEVER allow input KDV deduction beyond the calendar year of the invoice
- NEVER confuse tam istisna (full exemption with refund right) with kismi istisna (partial exemption without refund right)
- NEVER compute any number -- all arithmetic is handled by the deterministic engine, not the AI
- NEVER guess free trade zone rules -- always escalate [T3]

---

## Step 14: Invoice Requirements and Documentation

### 14a. Fatura (Invoice) Requirements [T1]

| Requirement | Details |
|-------------|---------|
| Who must issue | All taxpayers for transactions above TRY 10,900 (2024 threshold; adjusted annually) |
| Below threshold | Perakende satis fisi (retail receipt) or gider pusulasi (expense slip) |
| Mandatory fields | Seller name/title, VKN/TCKN, buyer name/title, VKN/TCKN, date, sequential number, item description, quantity, unit price, KDV rate, KDV amount, total |
| Issuance deadline | Within 7 days of delivery or service completion |
| Storage | 5 years from end of the calendar year (Tax Procedure Law Art 253) |
| Language | Turkish (foreign language may be added alongside) |

**Legislation:** Tax Procedure Law (VUK) Articles 229-232

### 14b. Gider Pusulasi (Expense Voucher) [T1]

| Requirement | Details |
|-------------|---------|
| Who issues | Buyer (when purchasing from non-taxpayer individuals) |
| Purpose | Documents payment to individuals not required to issue invoices |
| Withholding | Income tax and stamp duty withholding may apply |
| KDV | Generally no KDV on gider pusulasi transactions |

### 14c. Serbest Meslek Makbuzu (Self-Employment Receipt) [T1]

| Requirement | Details |
|-------------|---------|
| Who issues | Self-employed professionals (lawyers, doctors, architects, CPAs) |
| KDV | KDV is shown separately; subject to 20% withholding by the payer if payer is a corporation |
| Income tax | 20% income tax withholding by the payer |

**Legislation:** VUK Article 236; Income Tax Law Article 94

---

## Step 15: Place of Supply Rules

### 15a. Supply of Goods [T1]

| Scenario | Place of Supply | Legal Basis |
|----------|----------------|-------------|
| Goods located in Turkey at time of supply | Turkey | KDV Art 6/1 |
| Goods imported into Turkey | Turkey (at customs) | KDV Art 1/2 |
| Goods exported from Turkey | Turkey (zero-rated) | KDV Art 11 |
| Installation/assembly goods | Where installation takes place | KDV Art 6/2 |

### 15b. Supply of Services [T1]

| Scenario | Place of Supply | Legal Basis |
|----------|----------------|-------------|
| General rule | Where the service is performed | KDV Art 6/2 |
| Services related to real property | Where the property is located | KDV Art 6/2 |
| Transport services | Where transport takes place (proportionally) | KDV Art 6/2 |
| Digital/electronic services to Turkey | Turkey (if received/used in Turkey) | KDV Art 1, Art 9 |
| B2B services from abroad | Turkey (reverse charge) | KDV Art 9/1 |

**Note:** Turkey's place of supply rules differ from EU rules. The general rule focuses on where the service is "performed" or "benefited from" rather than the customer's establishment.

**Legislation:** KDV Kanunu Article 6

---

## Step 16: Penalties and Interest Reference Table

| Violation | Amount / Rate | Legal Basis |
|-----------|--------------|-------------|
| Late filing of KDV return | Uselessness penalty 1st degree (VUK Art 352) | VUK Art 352 |
| Failure to file KDV return | Resen tarhiyat + tax loss penalty (VUK Art 344) | VUK Art 344 |
| Late payment of KDV | Gecikme zammi: monthly rate set by Presidential Decree (currently 3.5%/month) | Law 6183, Art 51 |
| Failure to issue e-fatura | Special uselessness penalty per invoice (VUK Art 353/1) | VUK Art 353 |
| Issuing incorrect e-fatura | Special uselessness penalty (VUK Art 353/2) | VUK Art 353 |
| Failure to maintain e-defter | Special uselessness penalty (VUK Art 353) | VUK Art 353 |
| Tax fraud (vergi kacakciligi) | Criminal prosecution; 18 months to 5 years imprisonment | VUK Art 359 |
| Use of forged invoices (sahte fatura) | Criminal prosecution; 3 to 8 years imprisonment | VUK Art 359/b |
| Failure to withhold tevkifat | Tax loss penalty + late payment interest | VUK Art 344; Law 6183 |

---

## Step 17: Record-Keeping Requirements [T1]

| Record Type | Retention Period | Legal Basis |
|-------------|-----------------|-------------|
| Invoices (e-fatura, e-arsiv) | 10 years | VUK Art 253 |
| Ledgers (e-defter) | 10 years | VUK Art 253 |
| Bank statements | 10 years | VUK Art 253 |
| Contracts and agreements | 10 years | VUK Art 253 |
| Customs declarations (gumruk beyannamesi) | 10 years | VUK Art 253 |
| KDV returns (filed electronically) | Indefinite (maintained by GIB) | Electronic filing |
| Gider pusulasi and serbest meslek makbuzu | 10 years | VUK Art 253 |

---

## Contribution Notes

This skill covers Turkey KDV as of April 2026. Turkish tax law changes frequently via Presidential Decree. All rates and thresholds should be verified against the most recent GIB communiques before filing. A qualified Turkish tax adviser (YMM or SMMM) must validate all T1 rules before this skill is used in production.

**A skill may not be published without sign-off from a qualified practitioner in the relevant jurisdiction.**


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

If you would like a licensed accountant to review your return, visit [openaccountants.com](https://openaccountants.com) and log in to request a professional review.
