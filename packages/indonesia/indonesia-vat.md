---
name: indonesia-vat
description: Use this skill whenever asked to prepare, review, or classify transactions for an Indonesia VAT (PPN — Pajak Pertambahan Nilai) return (SPT Masa PPN), handle e-Faktur compliance, or advise on PPN registration and filing in Indonesia. Trigger on phrases like "PPN Indonesia", "Pajak Pertambahan Nilai", "SPT Masa PPN", "e-Faktur", "Faktur Pajak", "PKP registration", "Pengusaha Kena Pajak", or any Indonesia PPN request. ALWAYS read this skill before touching any Indonesia PPN work.
version: 2.0
jurisdiction: ID
tax_year: 2025
last_updated: 2026-07-13
reviewed_by: RILIA PUTRI
review_status: current
depends_on: - vat-workflow-base
category: international
tier: 1
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Indonesia VAT

## Indonesia PPN (Pajak Pertambahan Nilai / VAT) Skill v2.1

## Verified rates & thresholds (accountant-reviewed)

> Reviewed against the cited tax authorities by **RILIA PUTRI** on 2026-06-03.
> Items flagged for further clarification are tracked separately and excluded here.
> This block is generated from verified `skill_facts` — edit the facts, not the prose.

### PPN - VAT

- **Standard effective rate (non-luxury)** — 11% — nominal 12% applied to DPP of 11/12 × selling price  _(UU HPP Art. 7; PMK 131/2024)_
- **Luxury goods (PPnBM-listed) rate** — 12% on full DPP from 1 Feb 2025. Transitional 11/12 DPP in Jan 2025.  _(PMK 131/2024)_
- **Export rate** — 0% on goods; qualifying exported services  _(UU PPN Art. 7(2))_
- **PKP mandatory threshold** — IDR 4,800,000,000 annual turnover  _(UU PPN Art. 3A; PMK 197/2013)_
- **SPT Masa PPN filing deadline** — SPT Masa PPN must be filed no later than the end of the following month after the tax period ends (akhir bulan berikutnya setelah berakhirnya Masa Pajak).  _([UU KUP as amended by UU HPP No. 7/2021.](https://www.pajak.go.id/en/node/34988))_
- **PPN payment deadline** — PPN and PPnBM generally must be paid by the end of the month following the tax period and before the relevant SPT Masa PPN is submitted, subject to applicable VAT regulations.  _(UU KUP, PMK 81/2024 Article 94(3) as amended by PMK 01/2026; UU KUP as amended by UU HPP No. 7/2021.)_
- **Faktur Pajak issuance** — Faktur Pajak generally must be issued at the time of taxable supply or in accordance with applicable VAT invoicing and electronic tax administration regulations.  _(PMK-151/PMK.03/2013, Indonesian VAT Law Article 13, PER-11/PJ/2025, and PMK 81/2024 as amended by PMK 01/2026.)_
- **Input credit window** — Within 3 months of the tax period  _(UU PPN)_
- **Late filing SPT Masa PPN** — IDR 500,000 per month  _(UU KUP Art. 7)_
- **Late PPN payment** — 2% per month of unpaid tax  _(UU KUP Article 9(2a), Article 13(2))_
- **Late Faktur Pajak** — 1% of DPP per Faktur  _([Indonesian VAT Law Article 14(4)](https://www.pajak.go.id/en/node/101543))_
- **Underpayment on audit** — 100% of underpaid tax  _(UU KUP Article 13(3), UU KUP as amended by UU HPP No. 7/2021.)_
- **Basic food staples** — Basic food staples such as rice, corn, sago, soybeans, salt, fresh meat, eggs, milk, fruits, and vegetables  _(Indonesian VAT Law Article 4A as amended by UU HPP No. 7/2021)_
- **Services exempt** — Medical, education, financial, insurance, employment, water supply  _(Indonesian VAT Law Article 4A as amended by UU HPP No. 7/2021, PMK 70/PMK.03/2022 Articles 3, 5–8)_
- **PMSE PPN rate** — 11% collected by registered foreign providers  _(Indonesian VAT Law Article 7, PMK 81/2024 Articles 332–339)_
- **PMSE registration threshold** — >IDR 600m annual turnover from Indonesia OR >12,000 users/year  _(PMK 81/2024 Articles 332–339)_
- **I.A — Taxable sales 11%** — Taxable supplies subject to VAT (Tax Base/DPP)  _(Indonesian VAT Law Articles 4 & 7; UU HPP No. 7/2021 Article 7)_
- **I.B — Zero-rated (exports)** — Exports  _(Indonesian VAT Law Articles 3A, 4(1)(f),(g),(h), & 7(2))_
- **I.C — Exempt/non-taxable** — VAT-exempt supplies  _(Indonesian VAT Law Article 4A as amended by UU HPP No. 7/2021; PMK 70/PMK.03/2022 Articles 3 & 5–8)_
- **II — Output PPN** — Output VAT  _(Indonesian VAT Law Articles 1A, 4, & 9)_
- **III.A — Domestic input PPN** — Domestic Input VAT  _(Indonesian VAT Law Article 9)_
- **IV — PPN payable** — Output VAT less allowable Input VAT  _(Indonesian VAT Law Article 9(2))_
- **Coretax mandatory from** — January 2025 implementation for VAT administration  _(PMK 81/2024 as amended by PMK 01/2026)_
- **e-Faktur system** — Mandatory for taxable entrepreneurs (PKPs); integrated with Coretax  _(Indonesian VAT Law Article 13; PER-11/PJ/2025; PMK 81/2024 as amended by PMK 01/2026)_
- **NPWP format on Faktur Pajak** — 16-digit NIK-based Taxpayer Identification Number  _(PMK-112/PMK.03/2022 Article 2(1)–(3) & PER-6/PJ/2024)_

## Section 1 — Quick reference

**Quick reference**

| Field | Value |
| --- | --- |
| Country | Indonesia (Republik Indonesia) |
| Tax | PPN — Pajak Pertambahan Nilai (Value Added Tax) |
| Currency | IDR (Indonesian Rupiah / Rupiah) |
| Tax year | Calendar year (1 Jan – 31 Dec) |
| Standard rate | Effective **11%** for non-luxury goods/services; **12%** for LGST-listed luxury goods from 1 Feb 2025. Under PMK 131/2024, the nominal rate is 12% but the tax base (DPP) for non-luxury supplies is 11/12 of the selling price, so the effective rate remains 11%. (See "Section — Recent changes (PMK 131/2024 + Coretax)" below.) |
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

**Key SPT Masa PPN form lines**

| Line | Meaning |
| --- | --- |
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

**Conservative defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown rate on a sale | 11% standard |
| Unknown counterparty registration (PKP or non-PKP) | Non-PKP — no input credit |
| Unknown counterparty country | Domestic Indonesia |
| Unknown export qualification | Domestic 11% until evidence confirmed |
| Unknown business-use % | 0% input credit |
| Unknown whether Faktur Pajak is available | No input credit |
| Unknown B2B vs B2C for digital services | B2C — 11% applicable |

### Red flag thresholds

**Red flag thresholds**

| Threshold | Value |
| --- | --- |
| HIGH single transaction | IDR 100,000,000 |
| HIGH tax delta on single default | IDR 11,000,000 |
| MEDIUM counterparty concentration | >40% of output or input |
| MEDIUM conservative default count | >4 per period |
| LOW absolute net PPN position | IDR 50,000,000 |

## Section 2 — Required inputs and refusal catalogue

### Required inputs

**Minimum viable** — bank statement for the month in CSV, PDF, or pasted text. NPWP (15-digit tax ID) and confirmation of PKP status.

**Recommended** — Faktur Pajak for all input credits, e-Faktur reports from DJP system, prior month excess credit (Lebih Bayar), SPTPD (period tax return).

**Ideal** — complete e-Faktur data export, import customs declarations (PIB — Pemberitahuan Impor Barang), asset register, full purchase/sales ledger.

**Refusal if minimum missing — SOFT WARN.** No bank statement = hard stop. "Input PPN credits require Faktur Pajak verified in the DJP e-Faktur system. All credits are provisional pending Faktur verification."

### Refusal catalogue

- **R-ID-1 — Non-PKP (below IDR 4.8B threshold)** — This business is not a Pengusaha Kena Pajak (PKP). Non-PKPs do not charge PPN and cannot recover input PPN. This skill covers PKP-registered businesses only.
- **R-ID-2 — Luxury goods tax (PPnBM)** — PPnBM on luxury goods (vehicles, electronics above threshold, jewellery, etc.) is a separate tax mechanism. Out of scope — escalate to a Konsultan Pajak.
- **R-ID-3 — Partial exemption (usaha campuran)** — Businesses making both taxable and exempt supplies must apportion input PPN. Apportionment requires the taxable/total ratio — out of scope without full-year data. Escalate.
- **R-ID-4 — Export refund (restitusi PPN)** — PPN refund claims for exporters require separate documentation and DGT audit. Out of scope — escalate.
- **R-ID-5 — Withholding PPN (Pemungut PPN)** — Government agencies and designated private companies act as PPN withholders. If your client has significant government contracts, the withheld PPN must be tracked and credited. Flag for specialist review.

## Section 3 — Supplier pattern library

Match by case-insensitive substring on counterparty name or reference. Most specific match wins. Fall through to Section 5 if no match.

### 3.1 Indonesian banks — fees and charges (exempt / exclude)

**3.1 Indonesian banks — fees and charges (exempt / exclude)**

| Pattern | Treatment | Notes |
| --- | --- | --- |
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

**3.2 Indonesian government and statutory (exclude)**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| DIREKTORAT JENDERAL PAJAK, DJP | EXCLUDE | Tax payment |
| PAJAK PERTAMBAHAN NILAI, PPN | EXCLUDE | Tax remittance |
| PAJAK PENGHASILAN, PPH | EXCLUDE | Income tax — out of PPN scope |
| BPJS KESEHATAN | EXCLUDE | Health insurance — out of scope |
| BPJS KETENAGAKERJAAN | EXCLUDE | Employment insurance — out of scope |
| BEA CUKAI, CUSTOMS | EXCLUDE | Customs duty (import PPN tracked separately) |
| IURAN BPJS | EXCLUDE | BPJS contribution |

### 3.3 Indonesian utilities (taxable at 11%)

**3.3 Indonesian utilities (taxable at 11%)**

| Pattern | Treatment | Rate | Notes |
| --- | --- | --- | --- |
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

**3.4 Transport and logistics**

| Pattern | Treatment | Rate | Notes |
| --- | --- | --- | --- |
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

**3.5 Food and retail**

| Pattern | Treatment | Rate | Notes |
| --- | --- | --- | --- |
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

**3.6 SaaS — local Indonesian suppliers (11%)**

| Pattern | Treatment | Rate | Notes |
| --- | --- | --- | --- |
| JURNAL.ID (Mekari) | Input 11% | 11% | Indonesian accounting SaaS — PKP registered |
| ACCURATE ONLINE | Input 11% | 11% | Indonesian accounting software |
| ZAHIR ACCOUNTING | Input 11% | 11% | Indonesian ERP |
| KLIKPAJAK (Mekari) | Input 11% | 11% | Indonesian tax software |
| TALENTA (Mekari) | Input 11% | 11% | Indonesian HR SaaS |

### 3.7 SaaS — international suppliers (PMSE — Perdagangan Melalui Sistem Elektronik)

DJP has a system for foreign digital service providers (PMSE) to register and collect 11% PPN directly from Indonesian B2C customers. For B2B: PKP buyers can claim input credit if the foreign provider is PMSE-registered and issues a valid commercial document (kuitansi).

**3.7 SaaS — international suppliers table**

| Pattern | Registration status | Treatment | Notes |
| --- | --- | --- | --- |
| GOOGLE (Workspace, Ads, Cloud) | PMSE registered | Input 11% if commercial invoice held |  |
| MICROSOFT (365, Azure) | PMSE registered | Input 11% if invoice held |  |
| META, FACEBOOK ADS | PMSE registered | Input 11% if invoice held |  |
| NETFLIX | PMSE registered | 11% on subscription (B2C) |  |
| SPOTIFY | PMSE registered | 11% on subscription |  |
| ZOOM | PMSE registered | Input 11% if invoice held |  |
| SLACK | PMSE registered | Input 11% if invoice held |  |
| NOTION, OPENAI, ANTHROPIC | Check PMSE list | Flag if not registered |  |
| AWS (Amazon) | PMSE registered | Input 11% if invoice held |  |

### 3.8 Payment processors (exempt fees)

**3.8 Payment processors (exempt fees)**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| MIDTRANS (biaya) | EXCLUDE | Payment processing fee — exempt |
| DOKU (biaya) | EXCLUDE | Payment gateway — exempt |
| XENDIT (biaya) | EXCLUDE | Payment gateway — exempt |
| STRIPE (biaya) | EXCLUDE | Payment gateway — exempt |

### 3.9 Internal transfers and exclusions

**3.9 Internal transfers and exclusions**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| TRANSFER ANTAR REKENING, INTERNAL | EXCLUDE | Internal movement |
| PINJAMAN, CICILAN PINJAMAN | EXCLUDE | Loan principal |
| GAJI, UPAH, SALARY | EXCLUDE | Payroll — outside PPN scope |
| DIVIDEN | EXCLUDE | Dividend — out of scope |
| UANG MUKA, DP (deposit advance) | Tier 2 — check | Advance payment for taxable supply triggers PPN |
| TARIK TUNAI, ATM | Tier 2 — ask | Default exclude |

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

## Section 5 — Tier 1 rules (compressed)

### 5.1 Standard rate 11%

- **Standard rate 11%** — Default rate for all taxable supplies. Rate increased from 10% to 11% effective 1 April 2022 (Law No. 7 of 2021 on Tax Regulation Harmonisation).  _(UU PPN No. 42/2009 as amended by UU HPP No. 7/2021)_

### 5.2 Zero rate — exports

- **Zero rate — exports** — Exports of goods and qualifying exported services. Zero-rated evidence for goods: Pemberitahuan Ekspor Barang (PEB — export declaration) and settlement documents. Services: contract + payment in foreign currency + consumed outside Indonesia.  _(UU PPN Article 7(2))_

### 5.3 Exempt supplies

- **Exempt supplies** — Basic food staples (beras, jagung, sagu, kedelai, garam, daging segar, telur, susu, buah-buahan, sayur-sayuran); medical/health services; education; financial services; insurance services; employment; water supply (drinking water).  _(UU PPN Article 4A)_

### 5.4 Faktur Pajak (tax invoice) requirements

- **Faktur Pajak requirements** — Issued via e-Faktur application (mandatory for all PKPs since 2016). Must be issued within: (a) end of month of delivery/payment for regular transactions. Required fields: seller NPWP, buyer NPWP, Faktur Pajak serial number (16-digit), date, description, DPP (tax base), PPN amount. Late issuance penalty: 2% of DPP per Faktur.

### 5.5 Input credit eligibility

- **Input credit eligibility** — Input PPN is creditable if: (1) valid Faktur Pajak is held; (2) the purchase relates to taxable business activities; (3) Faktur Pajak is verified in the DJP e-Faktur system; (4) claimed within 3 months of the tax period. Non-creditable: entertainment, golf, Faktur Pajak from non-PKP suppliers.

### 5.6 PMSE (digital economy)

- **PMSE (digital economy)** — Foreign digital service providers (PMSE) registered with DJP collect 11% PPN from Indonesian customers. For PKP buyers, check current DJP guidance on whether PMSE commercial documents (kuitansi) qualify as input credit evidence. Currently a grey area.

### 5.7 Withholding PPN (Pemungut)

- **Withholding PPN (Pemungut)** — Government agencies and certain designated private companies (BUMN and others) withhold the PPN portion of payments and remit directly to DJP. Suppliers receive only the net amount. The withheld PPN is NOT offset against the supplier's output PPN in the SPT — it is reported separately in section IV of the SPT.

### 5.8 Filing deadlines

**5.8 Filing deadlines**

| Obligation | Deadline |
| --- | --- |
| PPN payment | End of month following tax period |
| SPT Masa PPN filing | End of month following tax period |
| Faktur Pajak issuance | Within the month of supply (or end of month for periodic billing) |
| Input credit window | Within 3 months of the tax period |

### 5.9 Penalties

**5.9 Penalties**

| Offence | Penalty |
| --- | --- |
| Late filing SPT | IDR 500,000 per month |
| Late payment | 2% per month of unpaid tax |
| Late Faktur Pajak | 2% of DPP per Faktur |
| Underpayment detected by audit | 100% of underpaid tax |
| Fraudulent Faktur | Criminal liability |

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

## Section 8 — Bank statement reading guide

### Common Indonesian bank statement formats (rekening koran)

**Common Indonesian bank statement formats (rekening koran)**

| Bank | Key columns | Date format | Amount format |
| --- | --- | --- | --- |
| BCA | Tanggal, Keterangan, Debit, Kredit, Saldo | DD/MM/YYYY | Rp X.XXX.XXX (period=thousands, comma=decimal) |
| BRI | Tgl Transaksi, Uraian, Debit, Kredit, Saldo | DD/MM/YYYY | Rp format |
| BNI | Tanggal, Mutasi, Debet, Kredit, Saldo | DD/MM/YYYY | Rp format |
| Mandiri | Tgl, Ket/Keterangan, Debet, Kredit, Saldo | DD/MM/YYYY | Rp format |
| CIMB Niaga | Date, Description, Debit, Credit, Balance | DD/MM/YYYY | Rp format |

### Common Indonesian bank statement formats (rekening koran)

**Key note on Indonesian number format:** Rp 111.000.000 = IDR 111,000,000 (one hundred eleven million rupiah). Periods separate thousands; comma separates decimals (rarely used in IDR).

### Key Indonesian banking terms

**Key Indonesian banking terms**

| Indonesian | Meaning | Classification hint |
| --- | --- | --- |
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

## Section 10 — Reference material

### Key legislation

**Key legislation**

| Topic | Reference |
| --- | --- |
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

**Changelog**

| Version | Date | Change |
| --- | --- | --- |
| 1.0 | 2024 | Initial release |
| 2.0 | April 2026 | Full v2.0 rewrite: pattern library, worked examples, PMSE section, no inline tier tags |
| 2.1 | 2026-05 | Add PMK 131/2024 (nominal 12% with 11/12 DPP keeping non-luxury at 11% effective; 12% effective on LGST goods from 1 Feb 2025); add Coretax DJP filing channel; flag pending accountant verification |

## Section — Recent changes (PMK 131/2024 + Coretax)

### PMK 131/2024 — the 11% / 12% split (effective 1 January 2025)

- **PMK 131/2024 rate split** — PMK 131/2024 (issued 31 December 2024) changed the nominal PPN rate to 12%, but kept the effective rate at 11% for non-luxury supplies through a tax-base (DPP — Dasar Pengenaan Pajak) adjustment: - Non-luxury goods/services: 12% applied to a DPP of 11/12 × selling price → effective PPN = 11%. Output VAT and input VAT both follow this formula. Faktur Pajak shows the 12% rate but the underlying DPP is 11/12 of price. - Luxury goods (LGST-listed — PPnBM): from 1 February 2025, 12% applied to the full selling price → effective 12%. For 1–31 January 2025, the transitional 11/12 DPP also applied to luxury goods. Practical implication: most freelance/SME invoices remain effectively 11%. Only LGST-listed items (luxury vehicles, luxury non-vehicles per PMK 96/2021 + PMK 15/2023 and PMK 141/2021 + PMK 42/2022) carry a real 12%.  _(PMK 131/2024)_

### Coretax DJP — the new filing channel (effective 1 January 2025)

- **Coretax DJP filing channel** — From tax year 2025 onward, all PPN compliance flows through Coretax DJP: - e-Faktur is inside Coretax (replaces the standalone desktop app). NSFP (Nomor Seri Faktur Pajak) requested in-platform; QR code generated automatically. - SPT Masa PPN filed via Coretax (web upload / Coretax Form / Coretax Mobile). - For tax periods through December 2024, the legacy DJP Online / e-Faktur desktop is still used; from January 2025 (filed February 2025) onward, Coretax. - See `id-einvoice-coretax` skill for the full Coretax workflow.

### NPWP = NIK (effective 1 July 2024)

- **NPWP = NIK** — Indonesian-citizen taxpayers now use their 16-digit NIK (national ID) as their NPWP. Foreign-national taxpayers retain the 15-digit NPWP until further notice. Faktur Pajak issued to/from Indonesian counterparts should carry the 16-digit identifier.

## Prohibitions

- **Prohibitions** — - NEVER claim input credit from a non-PKP supplier's document — only valid Faktur Pajak qualifies - NEVER apply 10% rate — current nominal rate is 12% with an effective 11% on non-luxury via the PMK 131/2024 DPP 11/12 mechanism - NEVER exempt basic food staples if they are processed/packaged (only raw staples listed in Article 4A are exempt) - NEVER omit withholding PPN from government clients — track SSP separately - NEVER present calculations as definitive — direct to a licensed Indonesian tax consultant (Konsultan Pajak)

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for errors, omissions, or outcomes. All outputs must be reviewed by a qualified professional before filing.

The most up-to-date version is maintained at openaccountants.com.

## Talk to a verified accountant

This skill is a tool, not an engagement. Every taxpayer's situation is
different, and the rules in the skill may not match your specific facts.

To speak with one of the licensed accountants who verifies skills for your
jurisdiction — **no liability on either side until you and the accountant sign
a formal engagement letter** — book a free 30-minute call:

**→ [Book a call](https://calendly.com/openaccountants-info/30min)**

We'll route you to the named verifier covering your country or state. You can
also see the full list of verified accountants at
[openaccountants.com/network](https://openaccountants.com/network).

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
