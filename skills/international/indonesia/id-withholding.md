---
name: id-withholding
description: "Use this skill whenever asked to compute, classify, or review Indonesian withholding tax obligations payable by a business on its outgoing payments to suppliers, landlords, contractors, lenders, shareholders, or non-resident recipients. Trigger on phrases like \"Indonesia withholding tax\", \"PPh 23\", \"PPh 26\", \"PPh 4(2) Final\", \"PPh Final\", \"Bukti Potong\", \"Bupot\", \"e-Bupot Unifikasi\", \"SPT Masa Unifikasi\", \"potong pajak supplier Indonesia\", \"withhold tax on supplier Indonesia\", \"rental withholding Indonesia\", \"construction services withholding\", \"royalty withholding Indonesia\", \"interest withholding Indonesia\", \"DGT Form\", \"P3B\", \"tax treaty Indonesia\", \"Coretax withholding\". This skill covers the three main withholding regimes that businesses operate when paying their counterparties — PPh 23 (services and passive income to Indonesian residents), PPh 26 (payments to non-residents), and PPh 4(2) Final (rental of land/building, construction services, bank interest, lottery prizes, IDX share sales, government bonds, etc.). Out of scope: PPh 21 employee/personnel withholding (covered separately in id-payroll-pph21), PPh 22 import/luxury goods withholding, PPh 15 special sectors (shipping/airlines), and the transfer of land/building (PPh 4(2) on disposal — mention only). ALWAYS read this skill before withholding tax on any Indonesian supplier payment."
jurisdiction: ID
tax_year: 2025
last_updated: 2026-07-13
reviewed_by: RILIA PUTRI
review_status: current
tier: 1
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# ID Withholding

## Indonesia Withholding Tax — PPh 23, PPh 26, PPh 4(2) Final — Skill v1.0

## Verified rates & thresholds (accountant-reviewed)

Reviewed against the cited tax authorities by **RILIA PUTRI** on 2026-06-03.
Items flagged for further clarification are tracked separately and excluded here.
This block is generated from verified `skill_facts` — edit the facts, not the prose.

### Withholding PPh 23-26-4(2)

- **Services (PMK 141/2015)** — 2% gross (4% if no NPWP)  _(UU PPh Art. 23 as amended by UU HPP No. 7/2021.; PMK 141/2015 as amended by PMK 81/2024 Art. 48)_
- **Rental — equipment/movable** — 2% gross (4% if no NPWP)  _(UU PPh Art. 23)_
- **Dividend (non-exempt resident)** — 15% (30% if no NPWP)  _(UU PPh Art. 23)_
- **Interest (non-bank)** — 15% (30% if no NPWP)  _(UU PPh Art. 23)_
- **Royalty** — 15% (30% if no NPWP)  _(UU PPh Art. 23)_
- **Prize (non-lottery)** — 15% (30% if no NPWP)  _(UU PPh Art. 23)_
- **Character (PPh 23)** — Creditable (not final)  _(UU PPh Art. 23)_
- **Standard rate (PPh 26)** — 20% of gross (or treaty rate if DGT Form held)  _(UU PPh Art. 26(1))_
- **DGT Form requirement** — Original DGT-1/DGT-2 signed by foreign tax authority, before payment  _(PER-25/PJ/2018)_
- **Character (PPh 26)** — Final  _(UU PPh Art. 26)_
- **Land/building rental** — 10% — Final  _(UU PPh Art. 4(2); PP 34/2017)_
- **Construction — small qualified** — 1.75% — Final  _(PP 9/2022)_
- **Construction — medium/large qualified** — 2.65% — Final  _(PP 9/2022)_
- **Construction — non-qualified** — 4% — Final  _(PP 9/2022)_
- **Construction consulting — qualified** — 3.5% — Final  _(PP 9/2022)_
- **Construction consulting — non-qualified** — 6% — Final  _(PP 9/2022)_
- **Construction — medium/large qualified** — 2.65% — Final  _(PP 9/2022)_
- **Integrated construction — non-qualified** — 4% — Final  _(PP 9/2022)_
- **Bank deposit interest** — 20% — Final  _(UU PPh Art. 4(2); PP 131/2000 jo. PP 123/2015; note: UU PPh as amended by UU HPP No. 7/2021.)_
- **Government bond (SUN/SBN) interest** — 10% — Final  _(PP 9/2021)_
- **Lottery prize** — 25% — Final  _(UU PPh Art. 4(2) as amended by UU HPP No. 7/2021.; PP 132/2000 as amended by UU HPP No. 7/2021.)_
- **Share sale on IDX — regular** — 0.1% gross — Final  _(UU PPh Art. 4(2)UU PPh as amended by UU HPP No. 7/2021.; PP 41/1994 as amended by PP 14/1997)_
- **Founders' shares at IPO** — +0.5% on founder shares — Final  _(UU PPh Art. 4(2) as amended by UU HPP No. 7/2021.; PP 41/1994 as amended by PP 14/1997)_
- **Transfer of land/building** — 2.5% gross — Final (mention only)  _(PP 34/2016)_
- **Monthly payment** — 10th of following month  _(UU KUP Art. 9(1) as amended by UU HPP No. 7/2021.; PMK 81/2024 as amended by PMK 1/2026)_
- **Monthly SPT Masa Unifikasi** — 20th of following month via Coretax  _(PMK 81/2024 as amended by PMK 1/2026)_
- **Bukti Potong (Bupot)** — Must be issued to payee for every withholding  _(UU PPh Art. 21 as amended by UU HPP No. 7/2021., Art. 23, Art. 26; PMK 168/2023)_

## Section 1 — Quick reference

**Quick reference**

| Field | Value |
| --- | --- |
| Country | Indonesia (Republik Indonesia) |
| Taxes covered | PPh 23 (services/passive income — residents); PPh 26 (non-residents); PPh 4(2) Final (specified items) |
| Currency | IDR (Indonesian Rupiah / Rp) only. Payments in foreign currency are converted at the Menteri Keuangan (KMK) reference rate on the date the tax becomes payable. |
| Tax year | Calendar year (1 Jan – 31 Dec) |
| Current tax year | 2025 |
| Tax authority | Direktorat Jenderal Pajak (DJP) — Directorate General of Taxes |
| Filing portal | Coretax DJP (https://coretaxdjp.pajak.go.id) — replaced the legacy DJP Online / e-Bupot 23/26 desktop from 1 January 2025 |
| Withholding slip | Bukti Pemotongan PPh (Bupot) — must be issued to the payee for every withholding |
| Monthly payment deadline | 10th of the month following the tax point (kode billing via SSP) |
| Monthly return deadline | 20th of the month following the tax point (SPT Masa PPh Unifikasi via Coretax) |
| Governing law | UU PPh No. 36/2008 as last amended by UU HPP No. 7/2021; PP 9/2021 (bond interest); PP 51/2008 jo. PP 9/2022 (construction services); PMK 141/PMK.03/2015 (services subject to PPh 23); PMK 34/PMK.010/2017 (land/building rental); PER-2/PJ/2024 (e-Bupot Unifikasi); P3B treaty network with ~70 countries |
| Validated by | Pending — requires sign-off by a qualified Indonesian tax consultant (Konsultan Pajak bersertifikat) |
| Skill version | 1.0 |

### Quick-look: payment type → article → rate

**Quick-look: payment type → article → rate**

| Payment type | Article | Rate (resident, with NPWP) | Rate (no NPWP) | Final? |
| --- | --- | --- | --- | --- |
| Services (jasa) listed in PMK 141/2015 | PPh 23 | 2% gross | 4% gross | No (creditable) |
| Sewa — rental of equipment / movable property | PPh 23 | 2% gross | 4% gross | No |
| Dividend to resident corporate (non-exempt) | PPh 23 | 15% | 30% | No |
| Interest (non-bank) to resident | PPh 23 | 15% | 30% | No |
| Royalty to resident | PPh 23 | 15% | 30% | No |
| Hadiah / prize (non-lottery) to resident | PPh 23 | 15% | 30% | No |
| Rental of land and/or building | PPh 4(2) | 10% | 10% | Yes — Final |
| Construction services — small qualified contractor | PPh 4(2) | 1.75% | 1.75% | Yes — Final |
| Construction services — medium / large qualified | PPh 4(2) | 2.65% | 2.65% | Yes — Final |
| Construction services — non-qualified contractor | PPh 4(2) | 4% | 4% | Yes — Final |
| Construction consulting — qualified | PPh 4(2) | 3.5% | 3.5% | Yes — Final |
| Construction consulting — non-qualified | PPh 4(2) | 6% | 6% | Yes — Final |
| Bank deposit interest, SBI, savings | PPh 4(2) | 20% | 20% | Yes — Final |
| Government bond (SUN/SBN) interest — resident | PPh 4(2) | 10% | 10% | Yes — Final |
| Lottery prize (hadiah undian) | PPh 4(2) | 25% | 25% | Yes — Final |
| Share sale on IDX — regular | PPh 4(2) | 0.1% gross | 0.1% gross | Yes — Final |
| Founders' shares additional levy at IPO | PPh 4(2) | +0.5% on founder shares | +0.5% | Yes — Final |
| Transfer of land/building (sale by seller) | PPh 4(2) | 2.5% gross | 2.5% | Yes — Final — DEFERRED (mention only) |
| Any payment to a non-resident (subject to treaty) | PPh 26 | 20% gross (treaty rate if DGT Form valid) | 20% | Yes — Final |

- **Critical rule — no NPWP doubling** — When the recipient does not provide a valid NPWP (Nomor Pokok Wajib Pajak), the PPh 23 rate is doubled — i.e. 2% becomes 4%, 15% becomes 30%. This does not apply to PPh 4(2) Final or PPh 26.  _(Pasal 23 ayat (1a) UU PPh)_

## Section 2 — Required inputs and refusal catalogue

### 2.1 Mandatory inputs before any withholding computation

**Mandatory inputs before any withholding computation**

| Input | Why it matters |
| --- | --- |
| Payer identity and NPWP | The withholding agent must be a registered Indonesian taxpayer; obligation depends on payer category (corporate, government, individuals appointed per KEP-50/PJ/1994) |
| Recipient legal name and tax residence | Determines PPh 23 (resident) vs PPh 26 (non-resident); also whether DGT Form is required |
| Recipient NPWP (if resident) | Determines whether PPh 23 doubles to 4% / 30% |
| Nature of payment (jasa, sewa, royalti, bunga, dividen, etc.) | Determines article and whether final or creditable |
| Gross contract value, VAT-exclusive | Base excludes PPN; if invoice is gross-of-VAT, strip the 12% PPN first |
| Date of payment OR accrual, whichever is earlier | Tax point under Pasal 23 ayat (4) |
| For PPh 26 treaty: original Form DGT-1/DGT-2 signed by foreign tax authority, dated before payment | Treaty relief denied if DGT Form not held at tax point |
| For construction services: SBU qualification class | Determines 1.75% / 2.65% / 4% rate under PP 9/2022 |
| For rental: land/building vs movable | Land/building → PPh 4(2) 10%. Movable (vehicle, machinery, equipment) → PPh 23 2%/4%. |

Refuse to compute withholding tax without ALL of the following:

### 2.2 Refusal catalogue

**Refusal catalogue**

| # | Situation | Reason |
| --- | --- | --- |
| R-ID-WHT-1 | Payment to an employee/director under employment | PPh 21 — out of scope. Route to id-payroll-pph21. |
| R-ID-WHT-2 | Import or luxury goods subject to PPh 22 | Import-stage regime collected by DGCE; out of scope. |
| R-ID-WHT-3 | Shipping, airline, or oil & gas contractor (PPh 15) | Special sectoral final regime; out of scope. |
| R-ID-WHT-4 | Sale of land/building (PPh 4(2) transfer at 2.5%) | Mention only; refer to PPAT/notaris. |
| R-ID-WHT-5 | Withholding by individual payer not appointed under KEP-50/PJ/1994 | Most individuals are NOT withholding agents; do not impose obligation unless appointed. |
| R-ID-WHT-6 | Treaty rate without valid DGT-1/DGT-2 before tax point | Per PER-25/PJ/2018 — no DGT, no treaty; default 20%. |
| R-ID-WHT-7 | Crypto / e-commerce platform commission (PMK 68/2022, PMK 71/2022) | Bespoke final regimes — out of scope. |
| R-ID-WHT-8 | UMKM final tax 0.5% under PP 55/2022 | Self-imposed seller turnover tax, NOT buyer withholding. Do not confuse with PPh 23. |
| R-ID-WHT-9 | Partial-year withholding-agent appointments / branch nuances / split contracts | Refer to a Konsultan Pajak. |
| R-ID-WHT-10 | Payments to a BUT (Indonesian PE of foreign company) | BUT is taxed as domestic (PPh 23 not PPh 26), but Pasal 26 ayat (4) Branch Profits Tax on after-tax profits is delicate — refer to a Konsultan Pajak. |

- **R-ID-WHT-1** — Payment to an employee/director under employment  _(PPh 21 — out of scope. Route to id-payroll-pph21.)_
- **R-ID-WHT-2** — Import or luxury goods subject to PPh 22  _(Import-stage regime collected by DGCE; out of scope.)_
- **R-ID-WHT-3** — Shipping, airline, or oil & gas contractor (PPh 15)  _(Special sectoral final regime; out of scope.)_
- **R-ID-WHT-4** — Sale of land/building (PPh 4(2) transfer at 2.5%)  _(Mention only; refer to PPAT/notaris.)_
- **R-ID-WHT-5** — Withholding by individual payer not appointed under KEP-50/PJ/1994  _(Most individuals are NOT withholding agents; do not impose obligation unless appointed.)_
- **R-ID-WHT-6** — Treaty rate without valid DGT-1/DGT-2 before tax point  _(Per PER-25/PJ/2018 — no DGT, no treaty; default 20%.)_
- **R-ID-WHT-7** — Crypto / e-commerce platform commission (PMK 68/2022, PMK 71/2022)  _(Bespoke final regimes — out of scope.)_
- **R-ID-WHT-8** — UMKM final tax 0.5% under PP 55/2022  _(Self-imposed seller turnover tax, NOT buyer withholding. Do not confuse with PPh 23.)_
- **R-ID-WHT-9** — Partial-year withholding-agent appointments / branch nuances / split contracts  _(Refer to a Konsultan Pajak.)_
- **R-ID-WHT-10** — Payments to a BUT (Indonesian PE of foreign company)  _(BUT is taxed as domestic (PPh 23 not PPh 26), but Pasal 26 ayat (4) Branch Profits Tax on after-tax profits is delicate — refer to a Konsultan Pajak.)_

## Section 3 — PPh 23 (Pajak Penghasilan Pasal 23)

### 3.1 Statutory basis

- **Statutory basis** — Pasal 23 UU PPh No. 36/2008 as last amended by UU HPP No. 7/2021. Implementing rules in PMK 141/PMK.03/2015 (list of 62 services subject to 2% withholding). The withholding agent is any Indonesian-resident body (badan), government entity, permanent establishment, or appointed individual making a payment of the listed type to another Indonesian resident.  _(Pasal 23 UU PPh No. 36/2008; PMK 141/PMK.03/2015)_

### 3.2 The 2% / 4% rate (services and rental of movable property)

- **Rate for rental and services (2% of gross)** — 2% of the gross amount for: Sewa dan penghasilan lain sehubungan dengan penggunaan harta — rental and other income from the use of property, except rental of land and building (which falls under PPh 4(2)); and Imbalan sehubungan dengan jasa — fees for services performed, covering the 62 categories listed in PMK 141/PMK.03/2015 including: jasa teknik, jasa manajemen, jasa konsultan (kecuali konsultan konstruksi), jasa akuntansi/pembukuan/atestasi, jasa hukum, jasa perancang/desain, jasa kebersihan, katering, maintenance and repair of non-vehicles, and jasa pengurusan transportasi (freight forwarding other than air freight).  _(Pasal 23 ayat (1) huruf c UU PPh)_
- **No-NPWP doubling** — If the recipient has no NPWP, the rate is 100% higher — i.e. 4%.  _(Pasal 23 ayat (1a))_

### 3.3 The 15% / 30% rate (passive income)

- **Rate for passive income (15% of gross)** — 15% of the gross amount for: Dividen — dividends paid to resident corporate shareholders, except dividends covered by the participation exemption under Pasal 4 ayat (3) huruf f (i.e. dividends from Indonesian companies to corporate shareholders holding ≥25% are exempt) and dividends reinvested under Pasal 4 ayat (3) huruf f UU HPP for individuals. Bunga — interest, premium, discount, and similar, except bank deposit interest (which falls under PPh 4(2) Final at 20%). Royalti — royalties for the right to use intellectual property, patents, trademarks, copyrights, know-how, and franchise/licence fees. Hadiah, penghargaan, bonus, dan sejenisnya — prizes and awards other than lottery prizes (which fall under PPh 4(2) Final at 25%) and other than those already taxed under PPh 21 (which would be employment-related awards).  _(Pasal 23 ayat (1) huruf a UU PPh)_
- **No-NPWP surcharge** — No-NPWP surcharge doubles these to 30%.

### 3.4 Tax base

- **Withholding base calculation** — The withholding base is the gross amount excluding PPN. If the invoice shows IDR 110,000,000 inclusive of 12% PPN, the PPh 23 base is IDR 110,000,000 / 1.12 = IDR 98,214,286, not IDR 110,000,000.
- **Reimbursements treatment** — For reimbursements (reimbursable expenses), if the reimbursement is supported by third-party invoices in the name of the payer, it is excluded from the withholding base per SE-53/PJ/2009. If it is in the name of the service provider, it is included.  _(SE-53/PJ/2009)_

### 3.5 Exemptions

- **PPh 23 exemptions** — PPh 23 does NOT apply to: income paid to a bank; finance lease payments (sewa guna usaha dengan hak opsi); dividends qualifying for participation exemption under Pasal 4 ayat (3) huruf f; distributions of profit to firm/CV/persekutuan partners; SHU (sisa hasil usaha) of a koperasi paid to members; income already subject to PPh Final under Pasal 4 ayat (2).  _(Pasal 23 ayat (4) UU PPh)_

### 3.6 Worked mini-example — PPh 23 on technical services

PT ABC engages PT XYZ (resident, NPWP valid) for technical engineering. Invoice IDR 220,000,000 incl. 12% PPN. PPN component IDR 23,571,429 (220M × 12/112); tax base IDR 196,428,571; PPh 23 at 2% = IDR 3,928,571; net to PT XYZ IDR 216,071,429. PT ABC deposits IDR 3,928,571 by the 10th of the next month and issues Bupot PPh 23. Without NPWP: 4% = IDR 7,857,143.

## Section 4 — PPh 26 (Pajak Penghasilan Pasal 26)

### 4.1 Statutory basis

- **Statutory basis** — Pasal 26 UU PPh No. 36/2008 as last amended by UU HPP No. 7/2021. PPh 26 is the withholding regime for payments from Indonesia to non-residents (Subjek Pajak Luar Negeri / SPLN). It is a final tax in the hands of the non-resident, unless the non-resident has a permanent establishment (BUT) in Indonesia, in which case the income flows to the BUT and is taxed as resident income (with PPh 23 applying instead, and Branch Profits Tax under Pasal 26 ayat (4) on after-tax profits).  _(Pasal 26 UU PPh No. 36/2008)_

### 4.2 Standard rate — 20% gross

- **Standard PPh 26 rate** — 20% of the gross amount for: dividen; bunga (incl. premium, discount, guarantee fees); royalti, sewa, dan penghasilan lain sehubungan dengan penggunaan harta; imbalan sehubungan dengan jasa, pekerjaan, dan kegiatan (incl. services performed abroad for an Indonesian payer per SE-04/PJ/2017); hadiah dan penghargaan; pensiun dan pembayaran berkala lainnya; premi swap dan transaksi lindung nilai; keuntungan karena pembebasan utang (gain from debt forgiveness).  _(Pasal 26 ayat (1))_

### 4.3 Branch Profits Tax — Pasal 26 ayat (4)

- **Branch Profits Tax** — After-tax profits of an Indonesian permanent establishment (BUT) repatriated abroad are subject to an additional 20% Branch Profits Tax on the after-tax profit, unless reduced by an applicable P3B (most treaties cap BPT at 10%–15%, some at 5%). BPT is waived if profits are reinvested in Indonesia subject to PMK 14/PMK.03/2011 conditions.  _(Pasal 26 ayat (4); PMK 14/PMK.03/2011)_

### 4.4 Treaty relief (P3B)

- **Treaty relief requirements** — Indonesia has tax treaties (Persetujuan Penghindaran Pajak Berganda / P3B) with approximately 70 countries. To claim the treaty-reduced rate, the non-resident recipient MUST provide the payer, before the tax point: Form DGT-1 (general) or Form DGT-2 (banks, pension funds, and other listed entities), per PER-25/PJ/2018 as amended by PER-08/PJ/2019. The form must be signed by the competent authority of the residence country (Part II) — not merely by the recipient. The form is valid for up to 12 months from the date of the foreign competent authority's signature. The form must be submitted electronically by the payer via Coretax (previously DJP Online) before filing the SPT Masa.  _(PER-25/PJ/2018 as amended by PER-08/PJ/2019)_
- **No DGT form default** — Without a valid, attested DGT Form held by the payer at the tax point, the default 20% rate applies — even if a treaty exists. The non-resident can in theory claim a refund, but this is rarely practical.

Common treaty rates (illustrative — verify against the specific P3B before applying). Singapore: dividends 10/15%, interest 10%, royalty 8/10%. Netherlands: dividends 5/10%, interest 0/5/10%, royalty 5/10%. United States: dividends 10/15%, interest 10%, royalty 10%. United Kingdom: dividends 10/15%, interest 10%, royalty 10/15%. Japan: dividends 10/15%, interest 10%, royalty 10%. Hong Kong: dividends 5/10%, interest 10%, royalty 5%. Australia: dividends 15%, interest 10%, royalty 10/15%.

> Always verify the exact P3B text. Treaty rates differ between portfolio and substantial dividends, between specified and unspecified interest, and between cultural vs industrial royalties.

### 4.5 Worked mini-example — PPh 26 to non-resident software vendor

Indonesian PT ABC pays USD 50,000 to a Singapore-resident software company for a license fee. KMK exchange rate on payment date: IDR 16,000 / USD.

**Scenario A — no DGT Form on file.**

- Gross IDR equivalent: USD 50,000 × IDR 16,000 = IDR 800,000,000
- PPh 26 at 20%: IDR 160,000,000
- Net remitted abroad: IDR 640,000,000 (USD 40,000)
- PT ABC issues Bupot PPh 26 to the Singapore vendor and remits IDR 160,000,000 to DJP.

**Scenario B — valid DGT-1 from IRAS Singapore on file.**

- Indonesia–Singapore treaty royalty rate (Article 12): 8% for use of equipment, 10% for general royalties. Software licence fees are commonly treated as royalties → 10%.
- PPh 26 at 10%: IDR 80,000,000
- Net remitted abroad: IDR 720,000,000

> **Software classification caveat.** Whether a payment for software is a "royalty" (per Article 12 of the treaty) or "business profits" (Article 7) is a persistent area of dispute. Default to royalty treatment for shrink-wrap, SaaS subscription, and licensed-use software; treat as business profits only with a robust legal opinion. Indonesia's interpretation under SE-03/PJ.03/2024 generally treats software payments as royalty.

## Section 5 — PPh 4(2) Final — major categories

- **Overview of PPh 4(2)** — PPh Pasal 4 ayat (2) UU PPh is the "final" withholding regime. Income subject to PPh 4(2) is taxed at a fixed rate and is not aggregated with other income in the annual return — the withholding is the final tax burden on that income.

### 5.1 Rental of land and/or building — PMK 34/PMK.010/2017

- **Rate for rental of land/building** — 10% of gross rental, applied to all forms of rental of tanah dan/atau bangunan (land, building, apartment, office, retail, warehouse, factory). Withholding agent: the tenant if a corporate/government body or appointed individual; otherwise the landlord self-deposits. Base: gross rental including service charges (biaya servis) but excluding PPN. Final — the landlord does not aggregate this in the SPT Tahunan.  _(PMK 34/PMK.010/2017)_

> If the building owner provides significant operational services (hotel, serviced office), the entire stream may be re-characterised as business income (not rental) and fall outside PPh 4(2). Check substance.

### 5.2 Construction services — PP 51/2008 jo. PP 9/2022, PMK 141/2015

**Construction services rates**  _(PP 51/2008 jo. PP 9/2022, PMK 141/2015)_

| Service | Contractor qualification | Rate |
| --- | --- | --- |
| Pelaksanaan konstruksi | Small (Kecil) qualified | 1.75% |
| Pelaksanaan konstruksi | Medium (Menengah) or Large (Besar) qualified | 2.65% |
| Pelaksanaan konstruksi | Without SBU qualification | 4% |
| Pelaksanaan konstruksi | Individual (orang pribadi) qualified | 2.65% |
| Perencanaan / pengawasan | Qualified (any class) | 3.5% |
| Perencanaan / pengawasan | Without SBU qualification | 6% |
| Integrated construction work (pekerjaan terintegrasi) | Qualified | 2.65% |
| Integrated construction work | Without SBU | 4% |

- **Construction rate basis and finality** — Construction services are split between construction execution (pelaksanaan konstruksi) and construction consultancy (perencanaan / pengawasan konstruksi). Rates depend on the contractor's qualification certificate (Sertifikat Badan Usaha / SBU) issued by LPJK. All rates are applied to gross contract value excluding PPN. Final — the contractor does not aggregate this with other income. The PPh 4(2) withheld is the contractor's final liability on that contract.

### 5.3 Interest on bank deposits, savings, and SBI — PP 131/2000 jo. PP 123/2015

- **Bank deposit/savings/SBI interest rate** — 20% of gross interest, final, withheld by the bank. Same 20% applies to non-resident depositors (treaty may reduce). Includes time deposits (deposito), savings (tabungan), and SBI; Bank Indonesia syariah instruments (SBIS) are treated equivalently.  _(PP 131/2000 jo. PP 123/2015)_

### 5.4 Interest on government bonds (SBN) — PP 9/2021

- **Government bond interest rate** — 10% final to both resident and non-resident holders (down from pre-2021 15%/20%). Withholding agent: the paying agent/custodian.  _(PP 9/2021)_

### 5.5 Lottery prizes (hadiah undian) — PP 132/2000

- **Lottery prize rate** — 25% of gross prize value, final, withheld by the lottery organiser. Includes cash and in-kind prizes (in-kind at market value). Distinct from PPh 23's 15% on non-lottery prizes (competition awards, loyalty prizes).  _(PP 132/2000)_

### 5.6 Share sales on the Indonesia Stock Exchange (IDX) — PP 14/1997 jo. PP 41/1994

- **IDX share sale rate** — Regular sales: 0.1% of gross transaction value, final, withheld by the broker. Founders' shares: additional +0.5% on saham pendiri at IPO, in addition to the 0.1% on the actual sale. Applies only to IDX-listed transactions. Off-exchange share transfers are NOT subject to PPh 4(2) (general progressive rates, or PMK 256/PMK.03/2008 narrow scope — defer to consultant).  _(PP 14/1997 jo. PP 41/1994)_

### 5.7 Transfer of land/building by the seller — PP 34/2016 (mention only)

- **Transfer of land/building rate** — 2.5% of gross transfer value, paid by the seller before the deed is signed by the PPAT/notaris. Reduced to 1% for transfers to Government for public-interest purposes and simple housing programs. DEFERRED — this is a real-estate transfer regime separate from supplier-payment withholding. Refer to a Konsultan Pajak / PPAT.  _(PP 34/2016)_

### 5.8 Other PPh 4(2) Final categories (brief mention, not computed)

Hadiah penjualan to consumers (25%, PP 132/2000); pengalihan saham mitra modal ventura (0.1%); dividends to resident individuals post UU HPP (Pasal 4 ayat (3) huruf f — exempt if reinvested in Indonesia, otherwise progressive — not 10% final as pre-HPP); turnkey/EPC contracts (use construction execution rate, not separate PPh 23).

## Section 6 — Bukti Pemotongan (Bupot) and e-Bupot Unifikasi via Coretax

### 6.1 What is e-Bupot Unifikasi?

- **e-Bupot Unifikasi** — Per PER-2/PJ/2024, DJP unified the previously separate e-Bupot PPh 23/26 and e-Bupot PPh 21/26 systems into a single e-Bupot Unifikasi application, accessed since 1 January 2025 through Coretax DJP (https://coretaxdjp.pajak.go.id). The unified slip and unified SPT Masa cover PPh 21, 22, 23, 26, 4(2), and 15 in a single monthly filing. The earlier desktop e-SPT Masa PPh 23/26 and the web e-Bupot 23/26 were retired with the Coretax rollout.  _(PER-2/PJ/2024)_

### 6.2 Issuance flow

0. **Identify the transaction** — Identify the transaction — enter supplier NPWP/NIK (or passport for non-resident), gross amount, article (23/26/4(2)/15), and object code (kode objek pajak — e.g. 24-104-01 technical services, 27-100-99 foreign royalty).
0. **System computes the tax** — System computes the tax — Coretax pre-populates the rate based on object code and NPWP status.
0. **Generate the Bupot** — Generate the Bupot — system assigns a unique Nomor Bupot. The PDF is shareable with the recipient and serves as tax credit (non-final PPh 23) or tax receipt (PPh 26 / 4(2) Final).
0. **Pay the tax** — Pay the tax — generate kode billing (ID Billing) and pay via bank/ATM/e-wallet by the 10th of the following month using SSP.
0. **File SPT Masa Unifikasi** — File SPT Masa Unifikasi — submit by the 20th of the following month, reconciling Bupot issued with SSP paid.

### 6.3 Bupot content

- **Bupot content elements** — Identity of payer (NPWP, name, address); identity of recipient (NPWP/NIK for residents; passport/TIN for non-residents); article; object code; tax base (DPP); rate; tax amount; underlying invoice reference; DGT Form number and date (PPh 26 treaty); tax point date.

### 6.4 Corrections

- **Corrections process** — Pembetulan via Coretax triggers a revised SPT Masa Unifikasi. Under-deposited tax attracts ~1% per month interest under UU KUP Pasal 9 ayat (2a) (capped per UU HPP). Late-deposit interest is set by PMK 81/PMK.03/2024 at the benchmark-rate-linked monthly tariff.  _(UU KUP Pasal 9 ayat (2a); PMK 81/PMK.03/2024)_

## Section 7 — Monthly mechanics

### 7.1 Tax point

- **Tax point determination** — The withholding obligation arises at the earlier of: Date of cash payment, or Date the cost/expense is accrued (booked as biaya) in the payer's accounting records, or Date of the invoice from the supplier. In practice for accrual-basis companies, the tax point is often the invoice date.  _(Pasal 8 PMK 242/PMK.03/2014)_

### 7.2 Payment deadline — 10th of the following month

- **Payment deadline** — The tax must be paid via SSP (Surat Setoran Pajak) using a kode billing generated in Coretax, by the 10th of the month following the tax point. Late payment triggers interest under UU KUP Pasal 9 ayat (2a) at the monthly tariff set by PMK (typically ~1% per month, capped at 24 months).  _(UU KUP Pasal 9 ayat (2a))_

### 7.3 Filing deadline — 20th of the following month

- **Filing deadline** — The unified return SPT Masa PPh Unifikasi is filed via Coretax by the 20th of the following month. The return must be filed even if zero (SPT nihil), unless the agent has been formally deregistered as a withholding agent. Late filing triggers a fixed administrative penalty of IDR 100,000 per month per type under UU KUP Pasal 7 (unchanged through 2025).  _(UU KUP Pasal 7)_

### 7.4 Year-end reconciliation

- **Year-end reconciliation** — There is no separate annual PPh 23/26/4(2) return. The annual SPT Tahunan PPh Badan (corporate income tax return) of the withholding agent will list the total PPh 23/26/4(2) withheld and remitted in the year, cross-checked with the 12 monthly Unifikasi returns. The recipient of PPh 23 withholding (non-final) credits the amount against its own annual PPh Badan / PPh OP — the Bupot is the credit evidence (kredit pajak). The recipient of PPh 26 / PPh 4(2) Final does NOT credit it — the tax is final.

## Section 8 — Worked examples

### 8.1 Consultant invoice (PPh 23, with NPWP)

PT Klien Indonesia receives an invoice from CV Konsultan Hukum dated 15 March 2025 for legal advisory services — fee IDR 50,000,000 plus PPN 12% IDR 6,000,000, invoice total IDR 56,000,000. CV Konsultan Hukum is a registered resident PKP with a valid NPWP.

- Article: PPh 23, object code 24-104-08 (jasa konsultan hukum)
- Tax base: IDR 50,000,000 (excluding PPN); Rate: 2%
- PPh 23 to withhold: IDR 1,000,000
- Net payment to CV Konsultan Hukum: IDR 55,000,000; PPN of IDR 6,000,000 paid to CV Konsultan Hukum (who remits via its own PPN return — the buyer claims input VAT).
- Timeline: tax point 15 March; deposit PPh 23 by 10 April via kode billing in Coretax; issue Bupot PPh 23; file SPT Masa Unifikasi for March 2025 by 20 April.

### 8.2 Rental of office space (PPh 4(2) Final)

PT Klien Indonesia rents an office floor from PT Properti Sentosa at IDR 90,000,000 per quarter, plus PPN 12% IDR 10,800,000 — invoice total IDR 100,800,000.

- Article: PPh 4(2), object code 28-403-01 (sewa tanah dan/atau bangunan)
- Tax base: IDR 90,000,000 (excluding PPN); Rate: 10% final per PMK 34/PMK.010/2017
- PPh 4(2) to withhold: IDR 9,000,000; Net payment: IDR 91,800,000
- Final — PT Properti does not aggregate this rental income in its annual SPT Tahunan (subject to the substance test in 5.1).
- If the tenant were an individual not appointed under KEP-50/PJ/1994, the landlord self-deposits the 10% (see R-ID-WHT-5).

### 8.3 Payment to non-resident software vendor (PPh 26 with and without treaty)

PT Klien Indonesia subscribes to a SaaS platform from Acme Inc., a US-resident company with no Indonesian PE — annual licence USD 24,000, invoiced 1 February 2025, KMK rate IDR 16,200/USD (use the actual KMK rate). Gross: IDR 388,800,000.

**Scenario A — no DGT Form on file.** Article PPh 26 (object 27-100-09 royalti luar negeri — software), rate 20% per Pasal 26 ayat (1) huruf c → PPh 26 IDR 77,760,000; net remitted IDR 311,040,000 (USD 19,200). PPN PMSE (12% on IDR 388,800,000 = IDR 46,656,000) collected separately under PMK 60/PMK.03/2022.

**Scenario B — valid Form DGT-1 from IRS on file dated before 1 February 2025.** US–Indonesia P3B (1988) Article 13 royalty rate is 10% (incl. software) → PPh 26 IDR 38,880,000; net remitted IDR 349,920,000 (USD 21,600). DGT-1 number and date recorded on the Bupot PPh 26.

> Verify the actual P3B Article and the SaaS-as-royalty position with the underlying treaty text and Indonesian practice. Indonesia's general position post SE-03/PJ.03/2024 is that SaaS / software access is royalty.

## Section 9 — Conservative defaults

When any input is ambiguous, missing, or contested, default to the conservative position that minimises the risk of under-withholding (since under-withholding makes the payer secondarily liable for the unpaid tax plus interest plus penalties under UU KUP Pasal 13 — and the recipient has no incentive to remediate):

**Conservative defaults table**

| Ambiguity | Conservative default |
| --- | --- |
| Recipient NPWP status unknown | Treat as no-NPWP → PPh 23 doubled to 4% / 30% |
| Resident vs non-resident unclear | Treat as non-resident → PPh 26 at 20% (UNLESS recipient is clearly Indonesian) |
| Service vs goods classification ambiguous | Treat as service → PPh 23 applies |
| Construction contractor SBU unverified | Treat as non-qualified → 4% / 6% |
| Software licence vs business profits | Treat as royalty → withhold per Pasal 26 / Pasal 23 |
| Reimbursement of expenses unclear | Include in withholding base unless third-party invoices are in the payer's name |
| Treaty rate claim without original DGT Form | Apply default 20% PPh 26 — no treaty relief |
| Rental — land/building vs equipment unclear | If immovable property attached, PPh 4(2) 10% (final, broader) |
| KMK exchange rate not yet published | Defer payment to next day; do NOT use Bank Indonesia mid-rate |
| Mixed contract (goods + services) | Split if separately invoiced; if bundled, withhold on the full amount as services |
| Multiple object codes possible | Pick the higher-rate code |

The general principle: withhold the higher rate when in doubt and let the recipient claim a refund or credit. A refund claim from DJP is administratively heavy but available; making good an under-withholding from the payer's own pocket months after the supplier has been paid is much worse.

## Section 10 — Sources

**Primary legislation.** UU No. 36/2008 (Income Tax Law), as last amended by UU No. 7/2021 (UU HPP); UU No. 6/1983 (UU KUP), as last amended by UU HPP and PERPPU 2/2022.

**Government Regulations (Peraturan Pemerintah).** PP 131/2000 jo. PP 123/2015 (bank deposit interest 20% Final); PP 132/2000 (lottery 25% Final); PP 14/1997 jo. PP 41/1994 (IDX shares 0.1% + 0.5% founder); PP 51/2008 jo. PP 9/2022 (construction services); PP 34/2016 (land/building transfer 2.5%, mention only); PP 9/2021 (bond interest 10% Final); PP 55/2022 (UMKM final 0.5%, out of scope — R-ID-WHT-8).

**Ministerial Regulations (PMK).** PMK 141/PMK.03/2015 (62 services for PPh 23); PMK 34/PMK.010/2017 (rental of land/building 10%); PMK 242/PMK.03/2014 (PPh payment and tax point); PMK 14/PMK.03/2011 (BUT reinvestment to avoid BPT); PMK 60/PMK.03/2022 (PPN PMSE); PMK 81/PMK.03/2024 (late-payment interest tariff 2024–2025).

**DJP Regulations (PER) and circulars.** PER-25/PJ/2018 as amended by PER-08/PJ/2019 (DGT-1/DGT-2); PER-2/PJ/2024 (e-Bupot Unifikasi via Coretax); PER-04/PJ/2017 and successors (kode objek pajak); SE-04/PJ/2017 (services performed abroad for an Indonesian payer); SE-53/PJ/2009 (reimbursements in PPh 23 base); SE-03/PJ.03/2024 (software / SaaS as royalty).

**Decree.** KEP-50/PJ/1994 — appointment of certain individuals as withholding agents for rental of land/building.

**Treaty network.** P3B (Persetujuan Penghindaran Pajak Berganda) — Indonesia's ~70 bilateral treaties. Always verify the specific treaty article text.

**Portal.** Coretax DJP — https://coretaxdjp.pajak.go.id — operational from 1 January 2025; replaced DJP Online for withholding filings.

## Section 11 — Cross-references

- For PPh 21 (employee/personnel withholding) → see `id-payroll-pph21.md`.
- For PPN (VAT, including how withholding base excludes PPN) → see `indonesia-vat.md`.
- For Indonesian client intake and identity verification → see `intake.md`.
- For Indonesia foundation (currency, calendar, authority, general principles) → see `foundation.md`.

## Footer notice

*Skill version 1.0. Tax year 2025. Pending sign-off by a qualified Indonesian Konsultan Pajak. Do not file a withholding tax return based solely on this skill without credentialed local review.*

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
