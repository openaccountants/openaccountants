---
name: indonesia-vat
description: Use this skill whenever asked to prepare, review, or advise on Indonesia VAT (Pajak Pertambahan Nilai / PPN) for any client. Trigger on phrases like "Indonesian VAT", "PPN", "SPT Masa PPN", "e-Faktur", "Faktur Pajak", "PPnBM", or any request involving Indonesia VAT filing, classification, or compliance. This skill contains the complete Indonesia PPN classification rules, SPT Masa PPN structure, e-Faktur requirements, deductibility rules, reverse charge treatment, registration thresholds, and filing deadlines required to produce a correct return. ALWAYS read this skill before touching any Indonesia VAT-related work.
---

# Indonesia VAT (PPN) Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Indonesia |
| Jurisdiction Code | ID |
| Primary Legislation | UU No. 42 Tahun 2009 tentang PPN dan PPnBM, as amended by UU No. 7 Tahun 2021 (Harmonisasi Peraturan Perpajakan / HPP Law) |
| Supporting Legislation | PP No. 44 Tahun 2022 (implementation); PMK No. 131/PMK.03/2024 (12% rate implementation); PMK No. 18/PMK.03/2021 (e-Faktur); PER-03/PJ/2022 (Faktur Pajak) |
| Tax Authority | Direktorat Jenderal Pajak (DJP) -- Directorate General of Taxes, Ministry of Finance |
| Filing Portal | https://web-efaktur.pajak.go.id (e-Faktur); https://djponline.pajak.go.id (DJP Online) |
| Currency | Indonesian Rupiah (IDR) |
| Contributor | [Pending -- must be validated by Indonesian licensed tax consultant] |
| Validated By | Deep research verification, April 2026 |
| Validation Date | April 2026 |
| Skill Version | 1.0 |
| Confidence Coverage | Tier 1: rate application, SPT Masa PPN structure, e-Faktur requirements, blocked input categories, registration threshold. Tier 2: partial crediting, mixed-use allocation, intercompany pricing, PPnBM classification. Tier 3: free trade zone treatment, BOI/tax holiday interactions, transfer pricing adjustments on customs value. |

---

## Confidence Tier Definitions

Every rule in this skill is tagged with a confidence tier:

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required. Claude executes, engine computes.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags the issue and presents options. A licensed Indonesian tax consultant (Konsultan Pajak) must confirm before filing.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Skill does not cover this. Do not guess. Escalate to licensed consultant and document the gap.

---

## Step 0: Client Onboarding Questions

Before classifying ANY transaction, you MUST know these facts about the client. Ask if not already known:

1. **Entity name and NPWP (Nomor Pokok Wajib Pajak)** [T1] -- 15-digit or 16-digit (NITKU) taxpayer identification number
2. **PKP status** [T1] -- Is the entity a Pengusaha Kena Pajak (Taxable Entrepreneur)? PKP confirmation letter required
3. **Tax period** [T1] -- monthly (standard for all PKP)
4. **Industry/sector** [T2] -- impacts whether activity is subject to PPN, exempt, or PPnBM-liable
5. **Does the business make exempt or non-PPN supplies?** [T2] -- If yes, partial input crediting rules apply under Article 9(6)
6. **Does the business import goods?** [T1] -- impacts customs PPN and PPnBM treatment
7. **Is the business in a Free Trade Zone (Kawasan Perdagangan Bebas)?** [T3] -- FTZ rules differ significantly; escalate
8. **Does the business use e-Faktur?** [T1] -- mandatory for all PKP since 2016
9. **Does the business make luxury goods subject to PPnBM?** [T2] -- Pajak Penjualan atas Barang Mewah
10. **Input tax credit carried forward from prior period** [T1] -- from prior SPT Masa PPN

**If any of items 1-3 are unknown, STOP. Do not classify any transactions until PKP status and period are confirmed.**

---

## Step 1: Transaction Classification Rules

### 1a. Determine Transaction Type [T1]

- Delivery/supply of taxable goods (Barang Kena Pajak / BKP) or taxable services (Jasa Kena Pajak / JKP) = output PPN
- Purchase/receipt of BKP or JKP = input PPN (Pajak Masukan)
- Salaries, wages, social security (BPJS), dividend distributions, loan repayments, income tax installments = OUT OF SCOPE
- **Legislation:** UU PPN, Article 1 (definitions); Article 4(1) (taxable events)

### 1b. Taxable Events (Objek PPN) [T1]

**Legislation:** UU PPN, Article 4(1), as amended by HPP Law

| Event | Article | Description |
|-------|---------|-------------|
| Delivery of BKP in customs territory | 4(1)(a) | Standard domestic sale of goods |
| Import of BKP | 4(1)(b) | Goods entering Indonesian customs territory |
| Delivery of JKP in customs territory | 4(1)(c) | Standard domestic provision of services |
| Utilization of intangible BKP from abroad | 4(1)(d) | Imported intangible goods (software, licenses) |
| Utilization of JKP from abroad | 4(1)(e) | Services received from foreign providers |
| Export of tangible BKP | 4(1)(f) | Physical goods exported |
| Export of intangible BKP | 4(1)(g) | Intangible goods exported |
| Export of JKP | 4(1)(h) | Services exported |

### 1c. Determine PPN Rate [T1]

**Legislation:** UU PPN, Article 7, as amended by HPP Law; PMK No. 131/PMK.03/2024

| Rate | Application | Effective Date |
|------|-------------|----------------|
| 12% | Standard rate for all taxable supplies | 1 January 2025 onwards (per Article 7(1)(b) HPP Law) |
| 11% | Previous standard rate | 1 April 2022 -- 31 December 2024 |
| 0% | Exports of tangible BKP, intangible BKP, and certain JKP (Article 7(2)) | Ongoing |

**Important note on 12% implementation (PMK 131/2024):** The government introduced a mechanism where for most goods/services previously at 11%, the effective calculation uses a deemed taxable base (Dasar Pengenaan Pajak / DPP Nilai Lain) of 11/12 of the selling price, resulting in an **effective rate of 11%** despite the nominal 12% rate. Only certain luxury goods (subject to PPnBM) bear the full 12% effective rate. [T2] -- flag for consultant to confirm which goods/services bear the full 12% vs. the 11/12 DPP mechanism.

**Practical impact:** For most taxpayers, the transition from 11% to 12% is effectively neutral due to the DPP Nilai Lain mechanism. Faktur Pajak should show 12% applied to the DPP Nilai Lain (11/12 of selling price), resulting in the same tax amount as 11% on the full selling price. A transitional grace period applied from 1 January to 31 March 2025 allowing Faktur Pajak with either 12% on DPP Nilai Lain or 11% on full DPP.

### 1d. Determine Category [T1]

- Tangible goods (BKP): physical goods
- Intangible goods (BKP tidak berwujud): software, licenses, IP, franchises
- Services (JKP): all services not specifically excluded
- Capital goods (Barang Modal): assets with useful life > 1 year used in production (Article 9(2a))
- **Legislation:** UU PPN, Articles 1, 9(2a)

---

## Step 2: SPT Masa PPN Structure [T1]

**Legislation:** UU PPN, Article 3; PER-14/PJ/2020 (SPT form); DJP e-Faktur system

The SPT Masa PPN (Monthly PPN Return) is filed electronically via e-Faktur. Structure:

### Part I -- Output Tax (Pajak Keluaran)

| Section | Description | Classification |
|---------|-------------|----------------|
| I.A | Delivery of BKP/JKP subject to PPN (domestic taxable supplies) | Standard output |
| I.B.1 | Delivery of BKP/JKP to VAT Collector (Pemungut PPN) -- Government agencies | Output, collected by buyer |
| I.B.2 | Delivery of BKP/JKP to Pemungut PPN -- designated SOEs/entities | Output, collected by buyer |
| I.B.3 | Delivery of BKP/JKP to Pemungut PPN -- other designated collectors | Output, collected by buyer |
| I.C | Delivery of BKP/JKP not collected (not subject to PPN, exempt, or Faktur Pajak not yet created) | Non-collected output |
| I.D | Export of BKP (tangible) | Zero-rated export |
| I.E | Export of BKP (intangible) / JKP | Zero-rated export |

### Part II -- Input Tax (Pajak Masukan)

| Section | Description | Classification |
|---------|-------------|----------------|
| II.A | Input tax that CAN be credited | Creditable input |
| II.B | Input tax that CANNOT be credited | Blocked/non-creditable input |
| II.C | Input tax on import of BKP (SSP/PIB) | Import input tax |
| II.D | Input tax on utilization of intangible BKP/JKP from abroad (SSP) | Reverse charge input |

### Part III -- Tax Calculation

| Line | Description |
|------|-------------|
| III.A | Total output tax (sum of Part I output) |
| III.B | Total creditable input tax (Part II.A + II.C + II.D) |
| III.C | Tax payable/overpaid (III.A - III.B) |
| III.D | PPN overpaid carried forward from prior period |
| III.E | Net tax payable or overpaid (III.C - III.D) |
| III.F | Compensation to next period / request for refund |

### Derived Calculations [T1]

```
III.A = sum of all output PPN from Parts I.A through I.E
III.B = Part II.A + Part II.C + Part II.D
III.C = III.A - III.B

IF III.C > 0 THEN
  Tax Payable = III.C - III.D (if positive)
  Overpaid C/F = III.D - III.C (if III.D > III.C)
ELSE
  Tax Payable = 0
  Overpaid = abs(III.C) + III.D
END
```

---

## Step 3: Supply Classification Matrix [T1]

### Non-Taxable Goods (Barang Tidak Kena Pajak) -- Article 4A(2)

**Legislation:** UU PPN, Article 4A(2), as amended by HPP Law; PP No. 49 Tahun 2022

| Category | Legislation | Notes |
|----------|-------------|-------|
| Mining/drilling products taken directly from source | Article 4A(2)(a) | Crude oil, natural gas, geothermal, minerals -- before processing |
| Basic necessities (barang kebutuhan pokok) | Article 4A(2)(b) | Rice, corn, sago, soybeans, salt, meat, eggs, milk, fruits, vegetables (as specified in PP 49/2022) |
| Food and beverages served at hotels/restaurants | Article 4A(2)(c) | Subject to local tax (PBJT) instead |
| Money, gold bars, securities | Article 4A(2)(d) | Financial instruments |

### Non-Taxable Services (Jasa Tidak Kena Pajak) -- Article 4A(3)

| Category | Legislation | Notes |
|----------|-------------|-------|
| Medical/healthcare services | Article 4A(3)(a) | Hospitals, clinics, doctors, dentists |
| Social services | Article 4A(3)(b) | Orphanages, nursing homes, funeral services |
| Financial services | Article 4A(3)(c) | Banking, insurance, leasing with option, factoring, pension funds (specific list in PP) |
| Insurance services | Article 4A(3)(c) | Life and general insurance |
| Religious services | Article 4A(3)(d) | Religious ceremonies and activities |
| Educational services | Article 4A(3)(e) | Schools, universities (accredited/licensed) |
| Arts and entertainment subject to local tax | Article 4A(3)(f) | Subject to PBJT instead |
| Public transport services | Article 4A(3)(g) | Land, water, air public transport |
| Labor services | Article 4A(3)(h) | Employment/staffing agency services in specific categories |
| Government services (non-competitive) | Article 4A(3)(i) | Government services not available commercially |
| Parking services subject to local tax | Article 4A(3)(j) | Subject to PBJT |
| Catering subject to local tax | Article 4A(3)(k) | Subject to PBJT |

### Zero-Rated (0%) -- Article 7(2)

| Category | Legislation | Notes |
|----------|-------------|-------|
| Export of tangible BKP | Article 7(2)(a); Article 4(1)(f) | Must have PEB (Pemberitahuan Ekspor Barang) customs document |
| Export of intangible BKP | Article 7(2)(b); Article 4(1)(g) | Software, licenses, IP exported |
| Export of JKP | Article 7(2)(c); Article 4(1)(h) | Qualifying exported services per PMK |

---

## Step 4: E-Faktur (Electronic Tax Invoice) Requirements [T1]

**Legislation:** UU PPN, Article 13; PER-03/PJ/2022; PMK No. 18/PMK.03/2021

### Mandatory E-Faktur [T1]

All PKP must issue Faktur Pajak (tax invoices) electronically through the DJP e-Faktur system since 1 July 2016. No paper Faktur Pajak is accepted.

### Faktur Pajak Content Requirements [T1]

A valid Faktur Pajak must contain (Article 13(5)):

1. Name, address, and NPWP of the seller (PKP)
2. Name, address, and NPWP of the buyer (or passport/NIK for non-NPWP holders)
3. Description of BKP or JKP delivered
4. Selling price or service fee replacement (Penggantian)
5. PPN amount collected
6. PPnBM amount collected (if applicable)
7. Transaction code and Faktur Pajak serial number (from NSFP allocation by DJP)
8. Date of Faktur Pajak issuance
9. Name, position, and signature of the issuer

### Faktur Pajak Transaction Codes [T1]

| Code | Description |
|------|-------------|
| 01 | Delivery to non-Pemungut (standard domestic sale) |
| 02 | Delivery to Government Pemungut (Bendaharawan) |
| 03 | Delivery to designated SOE Pemungut |
| 04 | DPP Nilai Lain (deemed taxable base) -- specific transactions |
| 05 | Specific intangible BKP / inter-FTZ delivery |
| 06 | Delivery to diplomatic/international organization |
| 07 | Delivery exempt from PPN / not subject to PPN (for reporting) |
| 08 | Delivery subject to PPN with DPP Nilai Lain under specific regulation |
| 09 | Delivery of assets originally not intended for sale (Article 16D) |

### Faktur Pajak Timing [T1]

Faktur Pajak must be issued no later than (Article 13(1a)):
- The end of the month of delivery of BKP/JKP, OR
- The end of the month of receipt of payment (if payment is received before delivery), OR
- The end of the month of receipt of payment in the case of installment payments (for each installment)

Whichever occurs first.

### Credit Note (Nota Retur / Nota Pembatalan) [T1]

**Legislation:** PMK No. 65/PMK.03/2010

- **Nota Retur:** issued by the buyer when goods are returned
- **Nota Pembatalan:** issued when services are cancelled
- Must reference original Faktur Pajak
- Reduces output PPN of the seller and input PPN of the buyer in the month the Nota is issued

---

## Step 5: Registration Rules [T1]

**Legislation:** UU PPN, Article 3A; PMK No. 197/PMK.03/2013

| Rule | Detail |
|------|--------|
| Mandatory PKP registration threshold | Annual gross turnover exceeding IDR 4,800,000,000 from delivery of BKP/JKP |
| Timing | Must apply for PKP status before the start of the following tax year after exceeding the threshold |
| Voluntary registration | Allowed for any entrepreneur delivering BKP/JKP, even below threshold |
| Non-resident digital service providers (PMSE) | Must appoint a PPN collector or register if providing digital goods/services to consumers in Indonesia (PMK 60/2022) |
| Revocation | May be revoked by DJP if turnover falls below threshold or upon cessation |

### Registration Consequences [T1]

| Status | Input PPN Recovery | Output PPN Obligation |
|--------|--------------------|-----------------------|
| PKP (registered) | Full credit on business-related purchases (subject to crediting rules) | Must collect PPN on taxable supplies |
| Non-PKP (below threshold) | No credit | No obligation to collect PPN |
| PMSE (appointed collector) | N/A | Must collect and remit PPN on digital supplies to consumers |

---

## Step 6: Reverse Charge / Self-Assessment Mechanics [T1]

**Legislation:** UU PPN, Article 3A(3); Article 4(1)(d)-(e); PMK No. 40/PMK.03/2010

### Utilization of Intangible BKP / JKP from Abroad [T1]

When an Indonesian person/entity utilizes intangible goods or services from a foreign provider:

1. The Indonesian recipient must self-assess PPN at 12% on the service/goods value
2. Pay via SSP (Surat Setoran Pajak) by the 15th of the following month
3. The SSP serves as the equivalent of a Faktur Pajak for input credit purposes
4. Claim input PPN credit on SPT Masa PPN Part II.D (if the recipient is a PKP and the supply relates to taxable business activities)
5. **Net effect: zero for fully taxable PKP**

### Import of Tangible BKP [T1]

- PPN on imported goods is collected by Customs (Bea Cukai) at the border
- The PIB (Pemberitahuan Impor Barang) and SSP/billing code serve as evidence of PPN payment
- Claim input PPN on SPT Masa PPN Part II.C

### Pemungut PPN (VAT Collector) System [T1]

**Legislation:** UU PPN, Article 1(27); PMK No. 231/PMK.03/2019

Certain buyers are designated as PPN collectors (Pemungut PPN) and must withhold PPN from the seller:

| Pemungut | Rate Collected | Legislation |
|----------|---------------|-------------|
| Government treasurers (Bendaharawan) | 12% of DPP | KMK 563/2003 |
| Designated SOEs (BUMN) | 12% of DPP | PMK 8/2021 |
| E-commerce platforms (PMSE) | 12% of selling price | PMK 60/2022 |

The seller reports the full output PPN but notes the Pemungut-collected portion. The seller does not remit the portion already collected by the Pemungut.

---

## Step 7: Blocked / Non-Creditable Input Tax [T1]

**Legislation:** UU PPN, Article 9(8); PP No. 44 Tahun 2022

Input PPN that CANNOT be credited:

| Blocked Category | Legislation | Notes |
|------------------|-------------|-------|
| Purchases before PKP registration | Article 9(8)(a) | Input PPN incurred before PKP status is effective |
| Purchases not directly related to business | Article 9(8)(b) | Personal use, non-business expenditure |
| Production/purchase of BKP/JKP with no direct nexus to delivery | Article 9(8)(b) | No business connection |
| Sedan vehicles and station wagons | Article 9(8)(c) | Exception: inventory of car dealers, rental car operators, taxi operators |
| Entertainment, representation, and hospitality | Article 9(8)(c) | Client entertainment, gifts, recreation -- unless it is the core business (e.g., event organizers) |
| Purchases where Faktur Pajak does not meet Article 13(5) requirements | Article 9(8)(d) | Invalid, incomplete, or late Faktur Pajak |
| Purchases where Faktur Pajak is issued more than 3 months after the transaction | Article 9(8)(d) | Late Faktur Pajak -- input credit forfeited |
| Input PPN attributable to non-taxable supplies | Article 9(6) | Must be allocated if mixed supplies exist |

### Vehicle Blocking Rule Detail [T1]

- Applies to sedan cars and station wagons (not pickup trucks, buses, minibuses for > 10 passengers, or trucks)
- **Blocked:** purchase, lease, fuel, maintenance, insurance for sedans/wagons
- **Exceptions:** car dealers (inventory), car rental operators (rental fleet), taxi operators (taxi fleet)
- Motorcycles: NOT blocked (creditable if for business)
- [T2] if client claims vehicle is excepted -- flag for consultant confirmation

---

## Step 8: PPnBM (Luxury Goods Sales Tax) [T2]

**Legislation:** UU PPN, Articles 5, 8, 10; PP No. 61 Tahun 2020; PP No. 73 Tahun 2019

### Overview [T2]

PPnBM (Pajak Penjualan atas Barang Mewah) is a separate tax imposed on delivery or import of luxury goods (Barang Kena Pajak yang Tergolong Mewah):

- Imposed once only: at the manufacturer/importer level (not at each subsequent sale)
- Rates range from 10% to 200% depending on the goods category
- PPnBM is NOT creditable against PPN (it is a separate, final tax)

### Common PPnBM Categories [T2]

| Category | Rate | Legislation |
|----------|------|-------------|
| Motor vehicles (various categories by engine size, type) | 15% -- 95% | PP 73/2019 |
| Luxury residential property (> IDR 30B or specific area) | 20% | PP 61/2020 |
| Hot air balloons, firearms, luxury vessels | 40% -- 75% | PP 61/2020 |
| Luxury electronics, crystal, marble products | 20% -- 50% | PP 61/2020 |

**Flag for consultant: PPnBM classification is complex and rate determination requires matching the specific goods description against the tariff schedules. Always verify against current PP.**

---

## Step 9: Filing Deadlines and Penalties [T1]

**Legislation:** UU PPN, Article 15A; UU KUP (General Tax Provisions), Articles 7, 8, 9, 13, 14

### Filing Deadlines [T1]

| Obligation | Deadline | Notes |
|------------|----------|-------|
| PPN payment (SSP) | 15th of the following month | For output PPN, reverse charge SSP |
| SPT Masa PPN filing | End of the following month | E-filing via e-Faktur web-based |
| PPnBM payment | 15th of the following month | Same as PPN |
| Faktur Pajak issuance | End of the month of delivery/payment | Per Article 13(1a) |

### Penalties [T1]

| Offence | Penalty | Legislation |
|---------|---------|-------------|
| Late filing of SPT Masa PPN | Administrative fine: IDR 500,000 per late SPT | UU KUP, Article 7(1) |
| Late payment of PPN | Interest: 0.5% -- 2.2% per month on unpaid amount (rate set monthly by MOF based on reference rate) | UU KUP, Article 9(2a) as amended by HPP |
| Failure to issue Faktur Pajak | Penalty: 1% of DPP (taxable base) for each unreported Faktur | UU KUP, Article 14(4) |
| Issuing Faktur Pajak but not on time | Penalty: 1% of DPP | UU KUP, Article 14(4) |
| Understating output PPN (discovered by audit) | Additional tax + interest of 0.5%-2.2%/month + 75% penalty | UU KUP, Article 13(2)-(3) |
| Fraudulent Faktur Pajak (fictitious/fake) | Criminal: 2-6 years imprisonment + fine 2-6x tax amount | UU KUP, Article 39A |

### Interest Rate Mechanism (HPP Law) [T1]

Post-HPP Law, the monthly interest rate for late payment is:

```
Rate = (Reference Rate set by MOF + uplift%) / 12
Minimum = 0.5% per month
Maximum = 2.2% per month (approximately)
```

The MOF publishes the applicable rate monthly via KMK.

---

## Step 10: Partial Input Tax Crediting [T2]

**Legislation:** UU PPN, Article 9(6); PMK No. 135/PMK.011/2014

When a PKP makes both taxable and non-taxable deliveries, input PPN must be allocated:

### Allocation Method [T2]

1. **Direct allocation:** Input PPN directly traceable to taxable supplies = fully creditable. Input PPN directly traceable to non-taxable supplies = fully blocked.
2. **Proportional crediting:** For shared/common expenses:

```
Creditable Input PPN = Total Common Input PPN * (Taxable Deliveries / Total Deliveries)
```

3. Calculated on an **annual basis** with monthly estimates adjusted at year-end.
4. The year-end recalculation is done in the SPT Masa PPN for the third month after the fiscal year ends (typically March for calendar-year taxpayers).

**Flag for consultant: allocation method and annual recalculation must be verified. DJP may challenge the allocation basis.**

---

## Step 11: Key Thresholds [T1]

| Threshold | Value | Legislation |
|-----------|-------|-------------|
| PKP registration | IDR 4,800,000,000 annual gross turnover | Article 3A; PMK 197/2013 |
| Faktur Pajak late issuance cutoff | 3 months after transaction date | Article 9(8)(d) |
| Capital goods adjustment period | 5 years for buildings, otherwise as per useful life | Article 9(2a) |
| PMSE digital tax threshold | No specific IDR threshold -- based on transaction volume, value, and/or users in Indonesia | PMK 60/2022 |
| Luxury property PPnBM | IDR 30,000,000,000 selling price or specific area/criteria | PP 61/2020 |

---

## Step 12: Edge Case Registry

### EC1 -- Digital services from foreign platform (e.g., Netflix, Spotify) to consumers [T1]

**Situation:** Foreign digital platform provides streaming services to Indonesian consumers.
**Resolution:** The platform should be designated as PMSE PPN collector by DJP. If designated, the platform collects and remits 12% PPN directly. The consumer cannot claim input credit. If the platform is NOT yet designated and the consumer is a PKP, the PKP must self-assess via SSP.
**Legislation:** PMK 60/2022; PMK 48/2020.

### EC2 -- Intercompany management fees from foreign parent [T1]

**Situation:** Indonesian subsidiary receives management services from foreign parent company. Invoice in USD, no PPN.
**Resolution:** Self-assessment applies under Article 4(1)(e). Indonesian subsidiary pays PPN via SSP at 12% on the IDR-equivalent service value. Claims input credit on SPT Masa PPN Part II.D. Transfer pricing arm's-length requirement applies separately under income tax rules.
**Legislation:** UU PPN, Article 4(1)(e); Article 3A(3).

### EC3 -- Restaurant meals (client entertainment vs. internal meeting) [T1]

**Situation:** Company pays for meal at restaurant. PPN charged on the bill.
**Resolution:** Restaurant food/beverage service is subject to PBJT (local tax), NOT PPN, per Article 4A(2)(c). If the restaurant is also a PKP and charges PPN on non-food items (e.g., venue rental for an event), that portion may have creditable input PPN. Meals purely for client entertainment: even if PPN were charged, input credit is blocked under Article 9(8)(c). [T2] if mixed-use -- flag for consultant.
**Legislation:** UU PPN, Article 4A(2)(c); Article 9(8)(c).

### EC4 -- Sale of company car (Article 16D) [T1]

**Situation:** PKP sells a company vehicle that was originally purchased for business use (not inventory).
**Resolution:** Under Article 16D, the sale of assets originally not intended for sale by a PKP is subject to PPN. Even though the input PPN on the original purchase may have been blocked (sedan), the sale still triggers output PPN. Use Faktur Pajak code 09.
**Legislation:** UU PPN, Article 16D; PER-03/PJ/2022.

### EC5 -- Free goods / bonus goods [T1]

**Situation:** PKP gives free bonus goods to customers (buy-10-get-1-free).
**Resolution:** Free delivery of BKP by a PKP is a taxable event under Article 1A(1)(d). Output PPN must be assessed on the market value (Harga Jual). Issue Faktur Pajak with DPP = market value, transaction code 04.
**Legislation:** UU PPN, Article 1A(1)(d); Article 4(1)(a).

### EC6 -- Reimbursement of expenses between related entities [T2]

**Situation:** Indonesian entity reimburses foreign affiliate for expenses incurred on its behalf (e.g., software licenses, travel booked by head office).
**Resolution:** If the reimbursement is for services utilized by the Indonesian entity, self-assessment PPN applies under Article 4(1)(e). If it is a pure pass-through with no mark-up and the foreign entity did not provide a service, the treatment is debatable. Flag for consultant: determine whether the reimbursement constitutes utilization of JKP from abroad or a mere cost allocation.
**Legislation:** UU PPN, Article 4(1)(e); DJP circular interpretations.

### EC7 -- Construction services (self-construction / bangun sendiri) [T1]

**Situation:** Company constructs its own building (not using a contractor PKP).
**Resolution:** Self-construction (kegiatan membangun sendiri) of a building with area >= 200 sqm is subject to PPN at an effective rate of 2.2% of total construction costs (excluding land), per PMK 61/2022 as adjusted for 12% rate. File and pay monthly via SSP code 409. This is NOT creditable as input PPN.
**Legislation:** UU PPN, Article 16C; PMK 61/2022.

### EC8 -- Subsidized goods (government price control) [T2]

**Situation:** Company sells subsidized fuel or fertilizer at government-controlled prices.
**Resolution:** PPN applies on the selling price (which may be below market). DPP is the actual selling price, not the market value, unless specific DPP Nilai Lain regulation applies. Flag for consultant: confirm whether specific DPP Nilai Lain rules apply to the subsidized product.
**Legislation:** UU PPN, Article 8A; specific PMK for subsidized goods.

### EC9 -- E-commerce marketplace seller below PKP threshold [T1]

**Situation:** Small seller on Tokopedia/Shopee with turnover below IDR 4.8B.
**Resolution:** Not required to be PKP. No obligation to collect or remit PPN. However, if the marketplace platform is designated as PMSE collector, the platform may collect PPN on the seller's behalf for digital aspects. Physical goods sold by non-PKP sellers: no PPN collected. Buyer cannot claim input credit.
**Legislation:** UU PPN, Article 3A; PMK 60/2022.

### EC10 -- Correction of SPT Masa PPN (Pembetulan) [T1]

**Situation:** PKP discovers an error in a previously filed SPT Masa PPN.
**Resolution:** May file a corrected SPT (SPT Pembetulan) provided no audit has commenced for that period. Interest applies on any additional tax due at the HPP-prescribed rate. The corrected SPT supersedes the original.
**Legislation:** UU KUP, Article 8(1); Article 8(2a).

---

## Step 13: Reviewer Escalation Protocol

When Claude identifies a [T2] situation, output the following structured flag before proceeding:

```
REVIEWER FLAG
Tier: T2
Transaction: [description]
Issue: [what is ambiguous]
Options: [list the possible treatments]
Recommended: [which treatment Claude considers most likely correct and why]
Action Required: Licensed Indonesian tax consultant (Konsultan Pajak) must confirm before filing.
```

When Claude identifies a [T3] situation, output:

```
ESCALATION REQUIRED
Tier: T3
Transaction: [description]
Issue: [what is outside skill scope]
Action Required: Do not classify. Refer to Konsultan Pajak. Document gap.
```

---

## Step 14: Test Suite

### Test 1 -- Standard domestic sale at 12%

**Input:** PKP sells goods domestically to another PKP. Selling price IDR 100,000,000.
**Expected output:** Faktur Pajak code 01. DPP = IDR 100,000,000. Output PPN = IDR 12,000,000 (or IDR 11,000,000 if 11/12 DPP mechanism applies -- [T2] confirm with consultant). SPT Part I.A.

### Test 2 -- Export of goods, zero-rated

**Input:** PKP exports goods FOB USD 50,000 (~IDR 790,000,000). PEB customs document obtained.
**Expected output:** Faktur Pajak code 04 (export). DPP = IDR 790,000,000. PPN = 0%. SPT Part I.D. Input PPN on production costs fully creditable.

### Test 3 -- Import of goods (Customs PPN)

**Input:** PKP imports machinery from Japan. CIF IDR 500,000,000. Import duty IDR 25,000,000. PPN paid at Customs = 12% of (IDR 500,000,000 + IDR 25,000,000) = IDR 63,000,000.
**Expected output:** SPT Part II.C = IDR 63,000,000 (input PPN). Creditable in full for taxable business.

### Test 4 -- Reverse charge on foreign management services

**Input:** PKP receives management consulting from Singapore affiliate. Fee USD 20,000 (~IDR 316,000,000). No PPN on invoice.
**Expected output:** Self-assess PPN via SSP = IDR 316,000,000 * 12% = IDR 37,920,000. Pay by 15th of following month. Claim IDR 37,920,000 input credit on SPT Part II.D. Net effect = zero.

### Test 5 -- Client entertainment, blocked input

**Input:** PKP hosts dinner for prospective clients at a hotel ballroom. Hotel invoices IDR 50,000,000 + PPN IDR 6,000,000. Valid Faktur Pajak.
**Expected output:** SPT Part II.B = IDR 6,000,000 (non-creditable). Input PPN blocked under Article 9(8)(c). Expense = IDR 56,000,000 gross.

### Test 6 -- Sedan purchase, blocked vehicle

**Input:** PKP purchases a sedan for director use. Price IDR 800,000,000 + PPN IDR 96,000,000 + PPnBM IDR 120,000,000 (15%).
**Expected output:** PPN IDR 96,000,000 blocked (Article 9(8)(c)). PPnBM IDR 120,000,000 is never creditable. Total cost of vehicle = IDR 1,016,000,000. SPT Part II.B = IDR 96,000,000.

### Test 7 -- Sale of company asset (Article 16D)

**Input:** PKP sells old office furniture for IDR 10,000,000. Originally purchased for business use.
**Expected output:** Taxable under Article 16D. Faktur Pajak code 09. DPP = IDR 10,000,000. Output PPN = IDR 1,200,000. SPT Part I.A.

### Test 8 -- Non-PKP small operator

**Input:** Small trader with annual turnover IDR 3,000,000,000. Not PKP-registered.
**Expected output:** No SPT Masa PPN filing. No PPN collected. No input PPN credit. Subject to PP 55/2022 final income tax (0.5% of gross turnover) if eligible.

### Test 9 -- Government procurement (Pemungut)

**Input:** PKP supplies office equipment to government ministry. DPP IDR 200,000,000. PPN IDR 24,000,000.
**Expected output:** Faktur Pajak code 02. Government treasurer (Bendaharawan) withholds IDR 24,000,000 PPN. PKP reports full output in SPT Part I.B.1. PKP does NOT remit PPN -- Pemungut remits it.

### Test 10 -- Free bonus goods

**Input:** PKP gives 100 units free as promotion. Market value IDR 500,000 per unit. Total IDR 50,000,000.
**Expected output:** Deemed delivery under Article 1A(1)(d). Faktur Pajak code 04. DPP = IDR 50,000,000. Output PPN = IDR 6,000,000. SPT Part I.A. Input PPN on the goods is creditable.

---

## PROHIBITIONS [T1]

- NEVER let AI guess SPT Masa PPN classifications -- they are deterministic from facts
- NEVER credit input PPN without a valid Faktur Pajak per Article 13(5) or valid SSP/PIB for imports/reverse charge
- NEVER credit input PPN on blocked categories (entertainment, sedans, personal use)
- NEVER credit PPnBM as input PPN -- PPnBM is a separate non-creditable tax
- NEVER confuse PBJT (local tax on restaurants/entertainment/parking) with PPN -- they are separate tax systems
- NEVER apply the 11% rate to transactions on or after 1 January 2025 -- the statutory rate is 12% (subject to DPP 11/12 mechanism for certain goods)
- NEVER omit the SSP payment for reverse charge on foreign services -- it is a separate obligation from the SPT
- NEVER credit input PPN from Faktur Pajak issued more than 3 months after the transaction date
- NEVER file SPT Masa PPN without reconciling to the e-Faktur system output (Pajak Keluaran and Pajak Masukan registers)
- NEVER confuse withholding tax (PPh) with PPN -- they are separate obligations, separate forms
- NEVER compute any number -- all arithmetic is handled by the deterministic engine, not Claude

---

## Contribution Notes

This skill requires validation by a licensed Indonesian tax consultant (Konsultan Pajak Bersertifikat) before production use. All T1 rules are based on UU PPN as amended by UU HPP No. 7/2021, PP 44/2022, PMK 131/2024 (12% rate with DPP Nilai Lain), and DJP regulations current as of early 2026.

**A skill may not be published without sign-off from a licensed practitioner in the relevant jurisdiction.**


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

If you would like a licensed accountant to review your return, visit [openaccountants.com](https://openaccountants.com) and log in to request a professional review.
