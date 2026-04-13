---
name: indonesia-vat
description: Use this skill whenever asked to prepare, review, or classify transactions for an Indonesia VAT (PPN — Pajak Pertambahan Nilai) return (SPT Masa PPN), handle e-Faktur compliance, or advise on PPN registration and filing in Indonesia. Trigger on phrases like "PPN Indonesia", "Pajak Pertambahan Nilai", "SPT Masa PPN", "e-Faktur", "Faktur Pajak", "PKP registration", "Pengusaha Kena Pajak", or any Indonesia PPN request. ALWAYS read this skill before touching any Indonesia PPN work.
version: 2.0
jurisdiction: ID
tax_year: 2025
category: international
depends_on:
  - vat-workflow-base
---

# Indonesia PPN (Pajak Pertambahan Nilai / VAT) Skill v2.0

---

## Section 1 — Quick reference

| Field | Value |
|---|---|
| Country | Indonesia (Republik Indonesia) |
| Tax | PPN — Pajak Pertambahan Nilai (Value Added Tax) |
| Currency | IDR (Indonesian Rupiah / Rupiah) |
| Tax year | Calendar year (1 Jan – 31 Dec) |
| Standard rate | 11% (effective April 2022; previously 10%) |
| Zero rate | 0% (exports of goods; exported services meeting criteria) |
| Exempt | Basic food staples (beras, jagung, etc.), medical services, education, financial services, insurance, employment services, certain mining activities, water (drinking water supply) |
| PPnBM | Pajak Penjualan atas Barang Mewah (Luxury Goods Sales Tax) — separate 10%–200% on luxury items; out of scope for this skill |
| Registration threshold | IDR 4,800,000,000 per year (IDR 4.8 billion) |
| Taxable Entrepreneur | PKP (Pengusaha Kena Pajak) — mandatory registration above threshold |
| Tax authority | DJP (Direktorat Jenderal Pajak — Directorate General of Taxes) |
| Filing | SPT Masa PPN — monthly VAT return via e-Faktur application |
| Filing deadline | End of month following the tax period (e.g., April period → 31 May) |
| Payment deadline | End of month following the tax period |
| e-Faktur | Mandatory electronic tax invoice system — all PKPs must use |
| Tax invoice | Faktur Pajak — required for input credit |
| NPWP | Nomor Pokok Wajib Pajak (15-digit taxpayer ID) |
| Contributor | Open Accountants Community |
| Validated by | Pending — requires sign-off by a licensed Indonesian tax consultant (Konsultan Pajak) |
| Skill version | 2.0 |

### Key SPT Masa PPN form lines

| Line | Meaning |
|---|---|
| I.A | Taxable sales at 11% (Penyerahan yang terutang PPN) |
| I.B | Zero-rated sales (Ekspor) |
| I.C | Exempt/non-taxable sales |
| II | Output PPN (Pajak Keluaran) |
| III.A | Input PPN from domestic purchases (Pajak Masukan) |
| III.B | Input PPN from imports |
| III.C | Input PPN not creditable (tidak dapat dikreditkan) |
| III.D | Net input PPN |
| IV | PPN payable (II − III.D) |
| V | Previous period excess credit (Lebih Bayar dikompensasi) |
| VI | Net payable or refund |

### Conservative defaults

| Ambiguity | Default |
|---|---|
| Unknown rate on a sale | 11% standard |
| Unknown counterparty registration (PKP or non-PKP) | Non-PKP — no input credit |
| Unknown counterparty country | Domestic Indonesia |
| Unknown export qualification | Domestic 11% until evidence confirmed |
| Unknown business-use % | 0% input credit |
| Unknown whether Faktur Pajak is available | No input credit |
| Unknown B2B vs B2C for digital services | B2C — 11% applicable |

### Red flag thresholds

| Threshold | Value |
|---|---|
| HIGH single transaction | IDR 100,000,000 |
| HIGH tax delta on single default | IDR 11,000,000 |
| MEDIUM counterparty concentration | >40% of output or input |
| MEDIUM conservative default count | >4 per period |
| LOW absolute net PPN position | IDR 50,000,000 |

---

## Section 2 — Required inputs and refusal catalogue

### Required inputs

**Minimum viable** — bank statement for the month in CSV, PDF, or pasted text. NPWP (15-digit tax ID) and confirmation of PKP status.

**Recommended** — Faktur Pajak for all input credits, e-Faktur reports from DJP system, prior month excess credit (Lebih Bayar), SPTPD (period tax return).

**Ideal** — complete e-Faktur data export, import customs declarations (PIB — Pemberitahuan Impor Barang), asset register, full purchase/sales ledger.

**Refusal if minimum missing — SOFT WARN.** No bank statement = hard stop. "Input PPN credits require Faktur Pajak verified in the DJP e-Faktur system. All credits are provisional pending Faktur verification."

### Refusal catalogue

**R-ID-1 — Non-PKP (below IDR 4.8B threshold).** "This business is not a Pengusaha Kena Pajak (PKP). Non-PKPs do not charge PPN and cannot recover input PPN. This skill covers PKP-registered businesses only."

**R-ID-2 — Luxury goods tax (PPnBM).** "PPnBM on luxury goods (vehicles, electronics above threshold, jewellery, etc.) is a separate tax mechanism. Out of scope — escalate to a Konsultan Pajak."

**R-ID-3 — Partial exemption (usaha campuran).** "Businesses making both taxable and exempt supplies must apportion input PPN. Apportionment requires the taxable/total ratio — out of scope without full-year data. Escalate."

**R-ID-4 — Export refund (restitusi PPN).** "PPN refund claims for exporters require separate documentation and DGT audit. Out of scope — escalate."

**R-ID-5 — Withholding PPN (Pemungut PPN).** "Government agencies and designated private companies act as PPN withholders. If your client has significant government contracts, the withheld PPN must be tracked and credited. Flag for specialist review."

---

## Section 3 — Supplier pattern library

Match by case-insensitive substring on counterparty name or reference. Most specific match wins. Fall through to Section 5 if no match.

### 3.1 Indonesian banks — fees and charges (exempt / exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| BANK CENTRAL ASIA, BCA | EXCLUDE (fee lines) | Financial service — PPN exempt |
| BANK RAKYAT INDONESIA, BRI | EXCLUDE (fee lines) | Same |
| BANK NEGARA INDONESIA, BNI | EXCLUDE (fee lines) | Same |
| BANK MANDIRI | EXCLUDE (fee lines) | Same |
| CIMB NIAGA | EXCLUDE (fee lines) | Same |
| BANK DANAMON | EXCLUDE (fee lines) | Same |
| BANK PERMATA | EXCLUDE (fee lines) | Same |
| OVO (fintech) | EXCLUDE (fee lines) | E-wallet fee — exempt financial service |
| GOPAY, GOJEK (payment fee) | EXCLUDE (fee lines) | Same |
| DANA E-WALLET | EXCLUDE (fee lines) | Same |
| BIAYA ADMIN, BUNGA, FEE | EXCLUDE | Bank admin fee/interest — exempt |

### 3.2 Indonesian government and statutory (exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| DIREKTORAT JENDERAL PAJAK, DJP | EXCLUDE | Tax payment |
| PAJAK PERTAMBAHAN NILAI, PPN | EXCLUDE | Tax remittance |
| PAJAK PENGHASILAN, PPH | EXCLUDE | Income tax — out of PPN scope |
| BPJS KESEHATAN | EXCLUDE | Health insurance — out of scope |
| BPJS KETENAGAKERJAAN | EXCLUDE | Employment insurance — out of scope |
| BEA CUKAI, CUSTOMS | EXCLUDE | Customs duty (import PPN tracked separately) |
| IURAN BPJS | EXCLUDE | BPJS contribution |

### 3.3 Indonesian utilities (taxable at 11%)

| Pattern | Treatment | Rate | Notes |
|---|---|---|---|
| PLN, PERUSAHAAN LISTRIK NEGARA | Input 11% | 11% | Electricity — taxable |
| PDAM, AIR MINUM | EXEMPT | 0% | Drinking water supply — exempt |
| PERTAMINA | Input 11% | 11% | Fuel/gas — taxable |
| PERTAGAS, PGN (gas network) | Input 11% | 11% | Gas — taxable |
| TELKOM INDONESIA | Input 11% | 11% | Telecom — taxable |
| TELKOMSEL | Input 11% | 11% | Mobile — taxable |
| INDOSAT OOREDOO HUTCHISON | Input 11% | 11% | Mobile — taxable |
| XL AXIATA | Input 11% | 11% | Mobile — taxable |
| SMARTFREN | Input 11% | 11% | Mobile — taxable |
| FIRST MEDIA, MNC PLAY | Input 11% | 11% | Internet/cable — taxable |

### 3.4 Transport and logistics

| Pattern | Treatment | Rate | Notes |
|---|---|---|---|
| GARUDA INDONESIA | Check route | 0%/11% | International 0%; domestic 11% |
| LION AIR, WINGS AIR | Check route | 0%/11% | International 0%; domestic 11% |
| CITILINK | Check route | 0%/11% | International 0%; domestic 11% |
| BATIK AIR | Check route | 0%/11% | Domestic 11%; international 0% |
| GOJEK (ride) | Input 11% | 11% | Ride-hailing — taxable |
| GRAB INDONESIA (ride) | Input 11% | 11% | Ride-hailing — taxable |
| BLUEBIRD TAXI | Input 11% | 11% | Taxi — taxable |
| DAMRI | Input 11% | 11% | Bus — taxable |
| KAI, KERETA API INDONESIA | Input 11% | 11% | Rail — taxable |
| JNE, JALUR NUGRAHA EKAKURIR | Input 11% | 11% | Courier — taxable |
| TIKI TITIPAN KILAT | Input 11% | 11% | Courier — taxable |
| J&T EXPRESS INDONESIA | Input 11% | 11% | Courier — taxable |
| SICEPAT EKSPRES | Input 11% | 11% | Courier — taxable |
| ANTERAJA | Input 11% | 11% | Courier — taxable |
| NINJA VAN INDONESIA | Input 11% | 11% | Courier — taxable |

### 3.5 Food and retail

| Pattern | Treatment | Rate | Notes |
|---|---|---|---|
| INDOMARET | Input 11% (non-food)/EXEMPT (basic staples) | Mixed | Food staples (beras, gula, etc.) exempt; packaged food 11% |
| ALFAMART | Input 11%/EXEMPT | Mixed | Same split |
| HYPERMART | Input 11%/EXEMPT | Mixed | Same |
| CARREFOUR INDONESIA, TRANS MART | Input 11%/EXEMPT | Mixed | Same |
| GIANT (HERO GROUP) | Input 11%/EXEMPT | Mixed | Same |
| TOKOPEDIA (marketplace) | Check invoice | — | Marketplace — check individual seller PKP status |
| SHOPEE INDONESIA (marketplace) | Check invoice | — | Same |
| LAZADA INDONESIA (marketplace) | Check invoice | — | Same |
| BUKALAPAK (marketplace) | Check invoice | — | Same |
| RESTORAN, RUMAH MAKAN (restaurant) | Input 11% | 11% | Restaurant meals — taxable (no block in Indonesia) |

### 3.6 SaaS — local Indonesian suppliers (11%)

| Pattern | Treatment | Rate | Notes |
|---|---|---|---|
| JURNAL.ID (Mekari) | Input 11% | 11% | Indonesian accounting SaaS — PKP registered |
| ACCURATE ONLINE | Input 11% | 11% | Indonesian accounting software |
| ZAHIR ACCOUNTING | Input 11% | 11% | Indonesian ERP |
| KLIKPAJAK (Mekari) | Input 11% | 11% | Indonesian tax software |
| TALENTA (Mekari) | Input 11% | 11% | Indonesian HR SaaS |

### 3.7 SaaS — international suppliers (PMSE — Perdagangan Melalui Sistem Elektronik)

DJP has a system for foreign digital service providers (PMSE) to register and collect 11% PPN directly from Indonesian B2C customers. For B2B: PKP buyers can claim input credit if the foreign provider is PMSE-registered and issues a valid commercial document (kuitansi).

| Pattern | Registration status | Treatment | Notes |
|---|---|---|---|
| GOOGLE (Workspace, Ads, Cloud) | PMSE registered | Input 11% if commercial invoice held | |
| MICROSOFT (365, Azure) | PMSE registered | Input 11% if invoice held | |
| META, FACEBOOK ADS | PMSE registered | Input 11% if invoice held | |
| NETFLIX | PMSE registered | 11% on subscription (B2C) | |
| SPOTIFY | PMSE registered | 11% on subscription | |
| ZOOM | PMSE registered | Input 11% if invoice held | |
| SLACK | PMSE registered | Input 11% if invoice held | |
| NOTION, OPENAI, ANTHROPIC | Check PMSE list | Flag if not registered | |
| AWS (Amazon) | PMSE registered | Input 11% if invoice held | |

### 3.8 Payment processors (exempt fees)

| Pattern | Treatment | Notes |
|---|---|---|
| MIDTRANS (biaya) | EXCLUDE | Payment processing fee — exempt |
| DOKU (biaya) | EXCLUDE | Payment gateway — exempt |
| XENDIT (biaya) | EXCLUDE | Payment gateway — exempt |
| STRIPE (biaya) | EXCLUDE | Payment gateway — exempt |

### 3.9 Internal transfers and exclusions

| Pattern | Treatment | Notes |
|---|---|---|
| TRANSFER ANTAR REKENING, INTERNAL | EXCLUDE | Internal movement |
| PINJAMAN, CICILAN PINJAMAN | EXCLUDE | Loan principal |
| GAJI, UPAH, SALARY | EXCLUDE | Payroll — outside PPN scope |
| DIVIDEN | EXCLUDE | Dividend — out of scope |
| UANG MUKA, DP (deposit advance) | Tier 2 — check | Advance payment for taxable supply triggers PPN |
| TARIK TUNAI, ATM | Tier 2 — ask | Default exclude |

---

## Section 4 — Worked examples

Six classifications from a hypothetical Jakarta-based IT consulting firm. Format: Bank BCA (Bank Central Asia) rekening koran (account statement).

### Example 1 — Domestic B2B revenue (11%)

**Input line:**
`15/04/2025  Transfer Masuk  PT TEKNOLOGI NUSANTARA  REF: FP-2025-041  Rp 111.000.000  Rp 500.000.000`

**Reasoning:**
Incoming Rp 111,000,000 from a Jakarta company for IT consulting. Standard 11% PPN. Gross Rp 111,000,000 includes PPN. Net = Rp 100,000,000 (DPP — Dasar Pengenaan Pajak) + Rp 11,000,000 Pajak Keluaran (output PPN). A Faktur Pajak must be issued via e-Faktur and reported in the SPT Masa PPN. Note Indonesian format: Rp 111.000.000 = IDR 111,000,000 (periods for thousands, comma for decimal).

**Classification:** Output PPN 11% — Rp 11,000,000. Net sales (DPP): Rp 100,000,000.

### Example 2 — Export service (zero-rated)

**Input line:**
`22/04/2025  Penerimaan Valas  ACME CORPORATION USA  Technical consulting Q1/2025  USD 5,000 (Rp 80.000.000)`

**Reasoning:**
USD payment from US company for services. Zero-rated if the service is consumed outside Indonesia. Evidence: contract, USD transfer record, services performed for foreign entity. Report Rp 80,000,000 on SPT line I.B (zero-rated exports). Output PPN: Rp 0. Conservative default: 11% if export qualification unconfirmed.

**Classification:** Zero-rated — Rp 80,000,000. Output PPN: Rp 0.

### Example 3 — Electricity bill (11%, input credit)

**Input line:**
`10/04/2025  Bayar Tagihan  PLN UNIT PELAYANAN  Listrik April 2025  Rp 5.500.000  Rp 44.500.000`

**Reasoning:**
Monthly electricity from PLN. Taxable at 11%. Gross Rp 5,500,000. Net DPP = Rp 4,954,955 + Rp 545,045 input PPN at 11%. PLN issues a Faktur Pajak — input credit claimable pending e-Faktur verification.

**Classification:** Input PPN 11% — Rp 545,045. DPP: Rp 4,954,955.

### Example 4 — Domestic courier (11%)

**Input line:**
`08/04/2025  Transfer Keluar  JNE JALUR NUGRAHA EKAKURIR  Ongkos Kirim Maret 2025  Rp 11.000.000  Rp 33.500.000`

**Reasoning:**
JNE courier services. Taxable at 11%. Gross Rp 11,000,000. DPP = Rp 9,909,910 + Rp 1,090,090 input PPN. JNE is a PKP-registered courier — Faktur Pajak available. Input credit claimable.

**Classification:** Input PPN 11% — Rp 1,090,090. DPP: Rp 9,909,910.

### Example 5 — International SaaS (PMSE)

**Input line:**
`05/04/2025  Debit Kartu  GOOGLE IRELAND LIMITED  Google Workspace April 2025  Rp 3.300.000  Rp 30.200.000`

**Reasoning:**
Google Workspace. Google is registered under the DJP PMSE system and collects 11% PPN from Indonesian customers. For a PKP business, input credit can be claimed using Google's commercial invoice as supporting document (kuitansi). This is different from a standard Faktur Pajak — check DJP guidance on PMSE input credit recovery. Flag: confirm whether the DJP currently allows PMSE commercial documents as input credit evidence for PKP buyers.

**Classification:** Tier 2 flag — Input PPN 11% Rp 330,000 potentially claimable; confirm PMSE input credit eligibility. DPP: Rp 3,000,000.

### Example 6 — Basic food staples (exempt)

**Input line:**
`12/04/2025  Pembelian  TOKO SEMBAKO MAKMUR  Beras dan Gula  Rp 5.000.000  Rp 25.200.000`

**Reasoning:**
Purchase of rice (beras) and sugar (gula) from a grocery. Basic food staples (bahan pokok) are exempt from PPN. No input PPN on this purchase. EXCLUDE from PPN computation. This is a business expense for income tax but generates no input credit.

**Classification:** EXEMPT — no input PPN. Out of PPN scope.

---

## Section 5 — Tier 1 rules (compressed)

### 5.1 Standard rate 11%

Default rate for all taxable supplies. Rate increased from 10% to 11% effective 1 April 2022 (Law No. 7 of 2021 on Tax Regulation Harmonisation). Legislation: UU PPN No. 42/2009 as amended by UU HPP No. 7/2021.

### 5.2 Zero rate — exports

Exports of goods and qualifying exported services. Zero-rated evidence for goods: Pemberitahuan Ekspor Barang (PEB — export declaration) and settlement documents. Services: contract + payment in foreign currency + consumed outside Indonesia. Legislation: UU PPN Article 7(2).

### 5.3 Exempt supplies

Basic food staples (beras, jagung, sagu, kedelai, garam, daging segar, telur, susu, buah-buahan, sayur-sayuran); medical/health services; education; financial services; insurance services; employment; water supply (drinking water). Legislation: UU PPN Article 4A.

### 5.4 Faktur Pajak (tax invoice) requirements

Issued via e-Faktur application (mandatory for all PKPs since 2016). Must be issued within: (a) end of month of delivery/payment for regular transactions. Required fields: seller NPWP, buyer NPWP, Faktur Pajak serial number (16-digit), date, description, DPP (tax base), PPN amount. Late issuance penalty: 2% of DPP per Faktur.

### 5.5 Input credit eligibility

Input PPN is creditable if: (1) valid Faktur Pajak is held; (2) the purchase relates to taxable business activities; (3) Faktur Pajak is verified in the DJP e-Faktur system; (4) claimed within 3 months of the tax period. Non-creditable: entertainment, golf, Faktur Pajak from non-PKP suppliers.

### 5.6 PMSE (digital economy)

Foreign digital service providers (PMSE) registered with DJP collect 11% PPN from Indonesian customers. For PKP buyers, check current DJP guidance on whether PMSE commercial documents (kuitansi) qualify as input credit evidence. Currently a grey area.

### 5.7 Withholding PPN (Pemungut)

Government agencies and certain designated private companies (BUMN and others) withhold the PPN portion of payments and remit directly to DJP. Suppliers receive only the net amount. The withheld PPN is NOT offset against the supplier's output PPN in the SPT — it is reported separately in section IV of the SPT.

### 5.8 Filing deadlines

| Obligation | Deadline |
|---|---|
| PPN payment | End of month following tax period |
| SPT Masa PPN filing | End of month following tax period |
| Faktur Pajak issuance | Within the month of supply (or end of month for periodic billing) |
| Input credit window | Within 3 months of the tax period |

### 5.9 Penalties

| Offence | Penalty |
|---|---|
| Late filing SPT | IDR 500,000 per month |
| Late payment | 2% per month of unpaid tax |
| Late Faktur Pajak | 2% of DPP per Faktur |
| Underpayment detected by audit | 100% of underpaid tax |
| Fraudulent Faktur | Criminal liability |

---

## Section 6 — Tier 2 catalogue

### 6.1 PMSE input credit eligibility

**What it shows:** Payment to a foreign digital service provider registered under PMSE.
**What's missing:** Whether DJP currently accepts the PMSE commercial invoice as an input credit document for PKP buyers.
**Conservative default:** No input credit pending DJP guidance confirmation.
**Question to ask:** "Do you have a commercial invoice from this foreign provider showing 11% PPN? Confirm with your tax consultant whether PMSE documents currently qualify for input credit."

### 6.2 Export service qualification

**What it shows:** Revenue from a foreign client.
**What's missing:** Whether the service was consumed outside Indonesia and payment was in foreign currency.
**Conservative default:** 11% domestic rate.
**Question to ask:** "Was this service entirely consumed outside Indonesia? Was payment received in foreign currency (USD/EUR/etc.)? Is there a signed contract with the foreign client?"

### 6.3 Mixed basic staples vs. packaged goods

**What it shows:** Purchase from a supermarket or grocery store.
**What's missing:** Split between exempt basic staples and taxable packaged goods.
**Conservative default:** 11% on full amount.
**Question to ask:** "Do you have an itemised receipt? Which items were basic staples (beras, gula, telur, etc. — exempt) vs. packaged/processed food (11%)?"

### 6.4 Government contract withholding PPN

**What it shows:** Receipt from a government agency that appears lower than invoiced amount.
**What's missing:** Whether PPN was withheld (Pemungut PPN).
**Conservative default:** Record full output PPN on invoice; check for SSP (payment slip) from government withholding.
**Question to ask:** "Did this government client withhold PPN? Do you have the withholding confirmation (SSP PPN) to include in your SPT?"

### 6.5 Advance payments (uang muka)

**What it shows:** Incoming advance payment before delivery of goods/services.
**What's missing:** Whether a Faktur Pajak has been issued for the advance.
**Conservative default:** Treat as taxable — output PPN due on receipt of advance.
**Question to ask:** "Was a Faktur Pajak issued for this advance payment? PPN is due when advance is received, not at delivery."

---

## Section 7 — Excel working paper template

```
INDONESIA PPN WORKING PAPER — KERTAS KERJA SPT MASA PPN
Masa Pajak (Period): ____________  NPWP: ____________

A. PAJAK KELUARAN (OUTPUT PPN)
  A1. Penyerahan kena pajak 11% (DPP)         ___________
  A2. Pajak Keluaran 11% (A1 × 11%)           ___________
  A3. Ekspor 0% (DPP)                          ___________
  A4. Penyerahan bebas PPN (DPP)               ___________
  A5. Total Pajak Keluaran (A2)                ___________

B. PAJAK MASUKAN (INPUT PPN)
  B1. Perolehan dalam negeri 11% (DPP)         ___________
  B2. Pajak Masukan 11% (B1 × 11%)             ___________
  B3. Impor barang / jasa luar negeri (DPP)    ___________
  B4. PPN impor (B3 × 11%)                     ___________
  B5. Total Pajak Masukan (B2+B4)              ___________
  B6. Pajak Masukan tidak dapat dikreditkan    ___________
  B7. Pajak Masukan dapat dikreditkan (B5−B6) ___________

C. PENGHITUNGAN PPN
  C1. Kurang / Lebih bayar (A5 − B7)           ___________
  C2. Kompensasi Lebih Bayar periode lalu      ___________
  C3. PPN kurang dibayar (C1 − C2)             ___________
  C4. Atau: Lebih Bayar (jika C1 < C2)         ___________

REVIEWER FLAGS:
  [ ] All Faktur Pajak verified in e-Faktur system?
  [ ] Export evidence (PEB) held for zero-rated sales?
  [ ] Government withholding PPN (SSP) collected?
  [ ] PMSE input credit eligibility confirmed?
  [ ] Basic staples correctly excluded (exempt)?
  [ ] Advance payments: Faktur Pajak issued?
```

---

## Section 8 — Bank statement reading guide

### Common Indonesian bank statement formats (rekening koran)

| Bank | Key columns | Date format | Amount format |
|---|---|---|---|
| BCA | Tanggal, Keterangan, Debit, Kredit, Saldo | DD/MM/YYYY | Rp X.XXX.XXX (period=thousands, comma=decimal) |
| BRI | Tgl Transaksi, Uraian, Debit, Kredit, Saldo | DD/MM/YYYY | Rp format |
| BNI | Tanggal, Mutasi, Debet, Kredit, Saldo | DD/MM/YYYY | Rp format |
| Mandiri | Tgl, Ket/Keterangan, Debet, Kredit, Saldo | DD/MM/YYYY | Rp format |
| CIMB Niaga | Date, Description, Debit, Credit, Balance | DD/MM/YYYY | Rp format |

**Key note on Indonesian number format:** Rp 111.000.000 = IDR 111,000,000 (one hundred eleven million rupiah). Periods separate thousands; comma separates decimals (rarely used in IDR).

### Key Indonesian banking terms

| Indonesian | Meaning | Classification hint |
|---|---|---|
| Transfer Masuk | Incoming transfer | Potential revenue |
| Transfer Keluar | Outgoing transfer | Potential expense |
| Bayar Tagihan | Bill payment | Expense |
| Penerimaan Valas | Foreign currency receipt | Potential export |
| Bunga | Interest | Exempt |
| Biaya Admin | Admin fee | Bank fee — exempt |
| Saldo | Balance | Running balance — ignore |
| Keterangan / Uraian | Description / narrative | Key classification field |
| Tarik Tunai / ATM | ATM withdrawal | Tier 2 — ask |
| Gaji | Salary | Out of PPN scope |

---

## Section 9 — Onboarding fallback

If the client provides a bank statement but cannot answer all questions immediately:

1. Classify all transactions using the pattern library (Section 3)
2. Apply conservative defaults (Section 1)
3. Mark Tier 2 items as "PENDING — reviewer must confirm"
4. Generate working paper with flags

```
INDONESIA PPN ONBOARDING — PERTANYAAN MINIMUM
1. NPWP (15-digit Nomor Pokok Wajib Pajak)?
2. Apakah sudah PKP (Pengusaha Kena Pajak)?
   Jika ya: Nomor Pengukuhan PKP?
3. Masa pajak (bulan) yang dicakup laporan bank ini?
4. Ada penjualan ekspor (tarif 0%)?
   Jika ya: apakah ada PEB (Pemberitahuan Ekspor Barang) atau kontrak dengan pihak asing?
5. Ada pemungutan PPN oleh instansi pemerintah (pemungut PPN)?
   Jika ya: sudah ada SSP PPN dari pemungut?
6. Ada langganan software/SaaS asing (Google, Microsoft, dll.)?
   Apakah penyedia asing sudah terdaftar PMSE DJP?
7. Lebih bayar PPN dari masa sebelumnya yang dikompensasi?
8. Ada uang muka (advance payment) yang diterima — sudah ada Faktur Pajak?
```

---

## Section 10 — Reference material

### Key legislation

| Topic | Reference |
|---|---|
| PPN Law | UU PPN No. 42/2009 as amended by UU HPP No. 7/2021 |
| 11% rate | UU HPP No. 7/2021 Article 7 |
| Exempt supplies | UU PPN Article 4A |
| Faktur Pajak | PMK-151/PMK.03/2013; DJP Circular SE-17/PJ/2014 |
| e-Faktur | PER-16/PJ/2014 and updates |
| PMSE digital | PMK-48/PMK.03/2020 |
| Export zero-rating | UU PPN Article 7(2); PMK on export |
| Withholding PPN | PMK on Pemungut PPN |
| Penalties | UU KUP (Tax Administration Law) No. 28/2007 |

### Known gaps

- PPnBM (luxury goods tax) — separate mechanism; out of scope
- Partial exemption (usaha campuran) apportionment — requires full-year data; escalate
- PPN refund (restitusi) claims for exporters — out of scope; requires DGT process
- Real estate and construction special rules — escalate
- PMSE input credit current DJP stance — verify latest guidance before claiming

### Self-check before filing

- [ ] All Faktur Pajak issued within month of supply
- [ ] All input Faktur Pajak verified in e-Faktur system
- [ ] Export PEB held for zero-rated sales
- [ ] Government SSP PPN collected and applied
- [ ] PMSE commercial invoices assessed for input credit eligibility
- [ ] Basic food staples correctly excluded
- [ ] Prior month Lebih Bayar correctly applied

### Changelog

| Version | Date | Change |
|---|---|---|
| 1.0 | 2024 | Initial release |
| 2.0 | April 2026 | Full v2.0 rewrite: pattern library, worked examples, PMSE section, no inline tier tags |

---

## Prohibitions

- NEVER claim input credit from a non-PKP supplier's document — only valid Faktur Pajak qualifies
- NEVER apply 10% rate — current rate is 11% (since April 2022)
- NEVER exempt basic food staples if they are processed/packaged (only raw staples listed in Article 4A are exempt)
- NEVER omit withholding PPN from government clients — track SSP separately
- NEVER present calculations as definitive — direct to a licensed Indonesian tax consultant (Konsultan Pajak)

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for errors, omissions, or outcomes. All outputs must be reviewed by a qualified professional before filing.

The most up-to-date version is maintained at openaccountants.com.
