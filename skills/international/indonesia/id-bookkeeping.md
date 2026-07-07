---
name: id-bookkeeping
description: "Use this skill whenever asked about Indonesian bookkeeping or transaction classification for income tax purposes. Trigger on phrases like \"Indonesia bookkeeping\", \"Pembukuan\", \"Pencatatan\", \"NPPN\", \"Norma Penghitungan\", \"Norma Penghitungan Penghasilan Neto\", \"classify transactions Indonesia\", \"bank statement Indonesia tax\", \"SPT 1770 classification\", \"SPT 1771 classification\", \"PPh OP bookkeeping\", \"PPh Badan bookkeeping\", \"KLU coefficient\", \"deemed profit Indonesia\", \"pembukuan vs pencatatan\". Covers the Pasal 28 UU KUP obligation, the pembukuan-vs-NPPN choice, KLU coefficient norms, transaction classification mapping to SPT 1770 Lampiran appendices and SPT 1771 Lampiran I, record retention, cash-vs-accrual election, and the Pasal 9 UU PPh non-deductible catalogue. Out of scope: the tax calculations themselves (those live in id-income-tax / id-corporate-tax), PPN/VAT classification (see indonesia-vat), PPh 21 payroll (see id-payroll-pph21), and final-tax PP 23 / PP 55 micro regimes are referenced but not computed here. ALWAYS read this skill before classifying transactions for an Indonesian SPT."
jurisdiction: ID
tax_year: 2025
reviewed_by: RILIA PUTRI
review_status: accountant-reviewed
tier: 1
last_updated: 2026-07-06
---

# id-bookkeeping

## Indonesia Bookkeeping (Pembukuan & NPPN) Skill v1.0

"Pembukuan" = full books. "Pencatatan" = simple records (NPPN electors). "Norma Penghitungan Penghasilan Neto" (NPPN) = deemed-deduction norm: Net Income = NPPN% × Gross Turnover, where NPPN% is set by KLU industry code.

This skill classifies money movements. It does NOT compute the tax. For PPh Orang Pribadi (individual) calculations see `id-income-tax`. For PPh Badan (corporate) calculations see `id-corporate-tax`. For PPN see `indonesia-vat`.

## Verified rates & thresholds (accountant-reviewed)

Reviewed against the cited tax authorities by **RILIA PUTRI** on 2026-06-03. Items flagged for further clarification are tracked separately and excluded here. This block is generated from verified `skill_facts` — edit the facts, not the prose.

### Bookkeeping

- **Badan (all corporations)** — Full pembukuan mandatory  _(UU KUP Art. 28(1))_
- **OP turnover > IDR 4.8B** — Full pembukuan mandatory  _(UU KUP Art. 28(2))_
- **OP turnover ≤ IDR 4.8B** — Individual taxpayers with annual gross turnover not exceeding IDR 4.8 billion may maintain records (pencatatan) and elect NPPN treatment by submitting notification to DJP within the prescribed period. Taxpayers meeting UMKM Final eligibility requirements may alternatively apply the final income tax regime under prevailing regulations.  _(UU PPh Art. 14(2) as amended by UU HPP No. 7/2021; PER-17/PJ/2015; PP 55/2022 as amended by PP 20/2026.)_
- **Record retention** — 10 years from end of tax year  _(UU KUP Art. 28(11))_
- **Language & currency** — Bahasa Indonesia and IDR; bilingual/forex requires DJP approval  _(UU KUP Art. 28(4) as amended by UU HPP No. 7/2021.; PMK 81/2024)_
- **Cash vs accrual** — Elected at start; must be consistent; change requires DJP approval  _(UU KUP Art. 28(5))_
- **Inventory valuation** — FIFO or Weighted Average only; LIFO prohibited  _(UU PPh Art. 10(6) as amended by UU HPP No. 7/2021.)_
- **Retail trade** — Retail-trading NPPN coefficients generally range around 20%–35% depending on detailed KLU classification and region category  _(UU PPh Art. 14(2); PER-17/PJ/2015 Full NPPN coefficient table (3,477 KLU) provided in separate attachment: TER_NPPN_Attachment_Indonesia.xlsx — Sheet 'NPPN Coefficients'. Source: Lampiran PER-17/PJ/2015. Three rate columns apply: (1) Ibukota Provinsi, (2) Ibukota Daerah Provinsi Lainnya, (3) Daerah Lainnya)_
- **Restaurants / food service** — Restaurant and food-service NPPN coefficients generally range around 20%–30% depending on activity classification and region  _(UU PPh Art. 14(2); PER-17/PJ/2015 Full NPPN coefficient table (3,477 KLU) provided in separate attachment: TER_NPPN_Attachment_Indonesia.xlsx — Sheet 'NPPN Coefficients'. Source: Lampiran PER-17/PJ/2015. Three rate columns apply: (1) Ibukota Provinsi, (2) Ibukota Daerah Provinsi Lainnya, (3) Daerah Lainnya)_
- **Professional services** — Professional-service activities generally subject to NPPN coefficients around 45%–50% depending on profession type  _(UU PPh Art. 14(2); PER-17/PJ/2015 Full NPPN coefficient table (3,477 KLU) provided in separate attachment: TER_NPPN_Attachment_Indonesia.xlsx — Sheet 'NPPN Coefficients'. Source: Lampiran PER-17/PJ/2015. Three rate columns apply: (1) Ibukota Provinsi, (2) Ibukota Daerah Provinsi Lainnya, (3) Daerah Lainnya)_
- **Software / IT freelance** — Certain IT consulting and software freelance activities generally follow professional-service NPPN classifications around 50%  _(UU PPh Art. 14(2); PER-17/PJ/2015 Full NPPN coefficient table (3,477 KLU) provided in separate attachment: TER_NPPN_Attachment_Indonesia.xlsx — Sheet 'NPPN Coefficients'. Source: Lampiran PER-17/PJ/2015. Three rate columns apply: (1) Ibukota Provinsi, (2) Ibukota Daerah Provinsi Lainnya, (3) Daerah Lainnya)_
- **Doctor / medical practice** — Medical professional services generally subject to NPPN coefficients around 50%  _(UU PPh Art. 14(2); PER-17/PJ/2015 Full NPPN coefficient table (3,477 KLU) provided in separate attachment: TER_NPPN_Attachment_Indonesia.xlsx — Sheet 'NPPN Coefficients'. Source: Lampiran PER-17/PJ/2015. Three rate columns apply: (1) Ibukota Provinsi, (2) Ibukota Daerah Provinsi Lainnya, (3) Daerah Lainnya)_
- **Lawyer / notary** — Legal and notarial services generally subject to NPPN coefficients around 50%  _(UU PPh Art. 14(2); PER-17/PJ/2015 Full NPPN coefficient table (3,477 KLU) provided in separate attachment: TER_NPPN_Attachment_Indonesia.xlsx — Sheet 'NPPN Coefficients'. Source: Lampiran PER-17/PJ/2015. Three rate columns apply: (1) Ibukota Provinsi, (2) Ibukota Daerah Provinsi Lainnya, (3) Daerah Lainnya)_
- **Construction** — ~20-25%  _(KEP-536/PJ./2000 — TBC)_
- **Agriculture / fisheries** — Agriculture and fisheries activities generally subject to NPPN coefficients around 10%–20% depending on commodity and activity classification  _(UU PPh Art. 14(2); PER-17/PJ/2015 Full NPPN coefficient table (3,477 KLU) provided in separate attachment: TER_NPPN_Attachment_Indonesia.xlsx — Sheet 'NPPN Coefficients'. Source: Lampiran PER-17/PJ/2015. Three rate columns apply: (1) Ibukota Provinsi, (2) Ibukota Daerah Provinsi Lainnya, (3) Daerah Lainnya)_
- **Manufacturing — garments** — Garment manufacturing activities generally subject to NPPN coefficients around 12.5%–15% depending on manufacturing classification and region  _(UU PPh Art. 14(2); PER-17/PJ/2015 Full NPPN coefficient table (3,477 KLU) provided in separate attachment: TER_NPPN_Attachment_Indonesia.xlsx — Sheet 'NPPN Coefficients'. Source: Lampiran PER-17/PJ/2015. Three rate columns apply: (1) Ibukota Provinsi, (2) Ibukota Daerah Provinsi Lainnya, (3) Daerah Lainnya)_
- **Pembukuan → NPPN** — Changes between bookkeeping and deemed-profit recording methods must follow consistency requirements and generally require DJP approval under prevailing tax regulations.  _(UU KUP Art. 28(5) as amended by UU HPP; PMK 81/2024.)_
- **NPPN → Pembukuan** — Individual taxpayers previously using NPPN may transition to full bookkeeping starting from the following tax year in accordance with prevailing tax administration rules.  _(UU PPh Art. 14; PER-17/PJ/2015.)_
- **Either → PP 55 final tax** — Application of the UMKM Final income tax regime (0.5%) is subject to taxpayer eligibility requirements, turnover thresholds, and exclusion criteria under prevailing regulations. Eligibility provisions were significantly amended by PP 20/2026.  _(UU PPh Art. 4(2) as amended by UU HPP; PP 55/2022 Arts. 56–58 as amended by PP 20/2026; PMK 164/PMK.03/2023.)_

## Section 1 -- Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Republic of Indonesia |
| Currency | IDR (Rupiah). USD books are permitted only for specific industries (oil/gas, mining contracts, foreign-currency-functional taxpayers) with prior DJP approval per PMK 196/PMK.03/2007 as amended. |
| Tax year | Calendar year by default (1 January -- 31 December). A non-calendar fiscal year is allowed if used consistently and notified to DJP (Pasal 1 angka 8 UU KUP). |
| Tax authority | Direktorat Jenderal Pajak (DJP), Ministry of Finance |
| Filing portal | Coretax DJP (rolled out under PMK 81/PMK.03/2024). Replaces legacy e-Filing / e-SPT / DJP Online for SPT submission from 2025 onwards. |
| Forms (individuals) | SPT 1770 (with business / freelance income); SPT 1770 S (employees + simple other income); SPT 1770 SS (turnover < IDR 60m). |
| Forms (companies) | SPT 1771 (corporate income tax return, including Lampiran I -- profit calc). |
| Pembukuan obligation | All badan (corporations). Individuals with gross turnover from business / freelance > IDR 4.8 billion in the preceding tax year (Pasal 28 ayat 1-2 UU KUP). |
| Pencatatan + NPPN option | Individuals with turnover ≤ IDR 4.8b who notify DJP in writing within 3 months of the start of the tax year (Pasal 14 ayat 2 UU PPh). |
| Record retention | 10 years from the end of the relevant tax year (Pasal 28 ayat 11 UU KUP). |
| Cash vs accrual | Elected at the start; must be applied consistently year-over-year. Changing the method requires DJP approval (Pasal 28 ayat 5 UU KUP). |
| Bahasa & format | Books must be kept in Bahasa Indonesia and IDR; bilingual / foreign-currency books require prior DJP approval (Pasal 28 ayat 4 UU KUP, PMK 196/2007). |

### Primary legislation cited throughout

**Primary legislation cited throughout**

| Citation | Short title |
| --- | --- |
| UU No. 6/1983 jo. UU No. 7/2021 (HPP) | Ketentuan Umum dan Tata Cara Perpajakan (KUP) -- general tax procedure |
| UU No. 7/1983 jo. UU No. 36/2008 jo. UU No. 7/2021 | Pajak Penghasilan (PPh) -- income tax |
| KEP-536/PJ./2000 | NPPN coefficient schedule by KLU (still the operative reference; verify if superseded by a later KEP/PER before signing off) |
| PER-17/PJ/2015 | Procedures for notifying use of NPPN |
| PP 23/2018 | Final-tax 0.5% micro/UMKM regime (separate elective regime; NOT NPPN) |
| PP 55/2022 | Implementing rules for PPh including UMKM final tax and successor framework |
| PMK 81/PMK.03/2024 | Coretax administration rules from 2025 |
| PMK 196/PMK.03/2007 (as amended) | USD bookkeeping permission |

## Section 2 -- Who Must Do What

### Decision tree -- which regime applies

- **Decision tree** — Badan (PT, CV, koperasi, yayasan, BUT)? ├── YES → MANDATORY Pembukuan. SPT 1771. No NPPN option. │         PP 23 unavailable for PT after 3 yrs / CV after 4 yrs (PP 55/2022). └── NO (orang pribadi): prior-year gross turnover from usaha/pekerjaan bebas? ├── > IDR 4.8b  → MANDATORY Pembukuan. SPT 1770. No NPPN. No PP 23. └── ≤ IDR 4.8b  → THREE options: ├── (a) Pembukuan voluntarily (actual deductions) ├── (b) Pencatatan + NPPN: notify DJP in writing within 3 months │       of the start of the tax year (Pasal 14(2) UU PPh, │       PER-17/PJ/2015). Without timely notification, NPPN is │       invalid -- 50% uplift risk under Pasal 14(5). └── (c) PP 23/2018 0.5% final tax on gross (separate regime; classified in `id-income-tax`, not here).  _(Pasal 14(2) UU PPh; PER-17/PJ/2015; PP 55/2022)_

### Switching regimes

**Switching regimes**

| From | To | Allowed? |
| --- | --- | --- |
| Pembukuan | NPPN | NO without DJP approval; Pasal 28 ayat 5 + KEP-536/PJ./2000 art. 3. Once full books have been elected they must continue. |
| NPPN | Pembukuan | YES — taxpayer can always upgrade to full books at the start of the next tax year. Notify DJP. |
| Either | PP 23 final tax | Annual election by 31 March of the tax year (PMK 99/PMK.03/2018 as amended). |

**Conservative default:** if the prior-year turnover is unknown or border-line at IDR 4.8b, treat the client as having a pembukuan obligation and request the prior SPT and gross-turnover reconciliation before classifying.

## Section 3 -- Required Inputs (Intake Checklist)

**Required Inputs (Intake Checklist)**

| # | Input | Why |
| --- | --- | --- |
| 1 | NPWP (15-digit, or 16-digit NIK-as-NPWP from 2024) | OP vs badan; SPT header. |
| 2 | KLU / KBLI code (5-digit) | Drives NPPN% and SPT 1771 sector lines. |
| 3 | Prior-year peredaran bruto | Determines pembukuan threshold. |
| 4 | NPPN notification letter (if claimed) | NPPN invalid without timely notification. |
| 5 | Cash or accrual basis declaration | Must match prior years. |
| 6 | Bank statements (all business accounts, full year) | Classification source. |
| 7 | Cash book / petty cash log | Off-bank revenue. |
| 8 | E-faktur PPN data (if PKP) | Cross-check sales and input VAT. |
| 9 | Bukti potong (PPh 23, 22, 4(2), 26) | Prepaid-tax credits. |
| 10 | Asset register + depreciation method (Pasal 11 UU PPh) | Capital allowances. |
| 11 | Loan agreements, leases, related-party contracts | Pasal 18 TP and thin-cap DER 4:1 (PMK 169/2015). |
| 12 | Inventory count + valuation method (FIFO or WAvg; LIFO prohibited) | COGS. |

### Refusal catalogue -- DO NOT proceed; escalate to reviewer

**Refusal catalogue**

| Code | Trigger | Why refused |
| --- | --- | --- |
| R-ID-1 | Taxpayer is a PE of a foreign entity (BUT) | Specific Pasal 5 rules + PER on BUT — out of scope. |
| R-ID-2 | Mining, oil & gas, or shariah banking | Sector-specific PSAK and PMK regimes — out of scope. |
| R-ID-3 | USD or other foreign-currency books | Need to verify PMK 196/2007 permission letter first. |
| R-ID-4 | Taxpayer has cross-border related-party transactions and turnover > IDR 50b | Transfer pricing documentation per PMK 213/2016 required first. |
| R-ID-5 | Final-tax PP 23 (0.5%) regime is in force | Classification model is different; route to `id-income-tax`. |
| R-ID-6 | Yayasan / koperasi / educational entity with concessional treatment | Specific Pasal 4 ayat 3 exclusions need separate review. |
| R-ID-7 | KLU is missing or the client claims an NPPN coefficient that cannot be confirmed in KEP-536/PJ./2000 (or a later instrument) | Stop and verify KLU before applying any norm. |
| R-ID-8 | Crypto, derivative, or capital-markets income | Final-tax / Pasal 4(2) — see separate skill. |
| R-ID-9 | NPPN claimed without a timely written notification | NPPN is invalid; Pasal 14 ayat 5 uplift risk. Stop. |
| R-ID-10 | Mixed regime: pembukuan for part of the year, NPPN for part | Not allowed -- pick one regime per tax year. |

### What "pembukuan" means

- **Pembukuan definition** — Full double-entry bookkeeping producing, at minimum: general ledger + subsidiary ledgers (cash, A/R, A/P, inventory, fixed assets), trial balance, P&L (Laporan Laba Rugi), balance sheet (Neraca), and supporting documents (faktur, kuitansi, bukti potong, bank statements) linked to journal entries. Pasal 28(3) UU KUP requires good-faith books reflecting actual business condition. Pasal 28(7) requires Bahasa Indonesia, Latin alphabet, Arabic numerals, and IDR currency, with bilingual / USD permitted only on prior DJP approval (PMK 196/2007).  _(Pasal 28(3), 28(7) UU KUP; PMK 196/2007)_

### Who must keep pembukuan

- **Who must keep pembukuan** — 1. All badan (PT, CV, firma, koperasi, BUMN/BUMD, yayasan conducting business). No turnover threshold. 2. Orang pribadi conducting usaha or pekerjaan bebas with prior-year gross turnover > IDR 4.8b (Pasal 28(2) UU KUP).  _(Pasal 28(2) UU KUP)_

### Cash vs accrual

- **Cash vs accrual election** — Pasal 28(5) UU KUP allows either basis; whichever is elected must be applied consistently and a change requires DJP written approval. Inventory must be valued FIFO or weighted-average (Pasal 10(6)); LIFO is prohibited. **Conservative default:** if the basis is undocumented, ASSUME accrual and flag for confirmation.  _(Pasal 28(5) UU KUP; Pasal 10(6) UU PPh)_

### Record retention

- **Record retention** — 10 years from the end of the relevant tax year (Pasal 28(11) UU KUP) -- longer than the 5-year assessment SOL (Pasal 13) to cover criminal-procedure timelines.  _(Pasal 28(11) UU KUP; Pasal 13 UU KUP)_

### Mechanic

- **NPPN mechanic** — Net Income (Penghasilan Neto) = NPPN% × Gross Turnover (Peredaran Bruto) The NPPN% varies by KLU industry code and by region tier (the historical KEP-536/PJ./2000 schedule distinguishes "10 ibukota provinsi", "ibukota provinsi lain", and "daerah lainnya" -- often abbreviated tier 1 / tier 2 / tier 3). The taxpayer does NOT separately claim any business expenses; the NPPN% IS the deemed expense deduction.  _(KEP-536/PJ./2000)_

### Eligibility

- **NPPN eligibility** — - Orang pribadi only (no badan). - Prior-year gross turnover ≤ IDR 4.8 billion (Pasal 14 ayat 2 UU PPh, threshold set by PMK 17/PMK.03/2013 and successor instruments aligned with the pembukuan threshold). - Written notification to DJP within 3 months of the start of the tax year (Pasal 14 ayat 2; procedurally PER-17/PJ/2015). - Pencatatan (simple records of gross turnover) must still be kept.  _(Pasal 14 ayat 2 UU PPh; PMK 17/PMK.03/2013; PER-17/PJ/2015)_

### What "pencatatan" requires

- **Pencatatan requirement** — A daily log of gross receipts by month, supported by invoices / receipts. No expense ledger is required because no expenses are deducted. Income from outside the business (employment, dividend, rental) is added separately to total taxable income.

### Non-creditable input VAT under NPPN

- **Non-creditable input VAT under NPPN** — Because the NPPN taxpayer is not deducting actual expenses, input VAT on purchases is also not creditable for PPh purposes -- the NPPN% is gross-of-input-VAT. (Input VAT crediting under PPN itself depends on PKP status, which is a separate question handled by `indonesia-vat`.)

### Failure-to-keep-books uplift

- **Failure-to-keep-books uplift** — Pasal 14 ayat 5 UU PPh -- if a taxpayer is required to keep books but does not, or refuses to produce them on inspection, DJP may apply the NPPN% to gross turnover AND add a 50% uplift to the resulting taxable income (or 20% for individuals subject to other Pasal 14 conditions; the 50% applies to badan under jabatan assessment). Conservative reading: any non-NPPN-electing taxpayer without books faces the uplift.  _(Pasal 14 ayat 5 UU PPh)_

## Section 6 -- Sample KLU NPPN Coefficients

> **CAUTION.** The coefficients below are illustrative samples drawn from
> KEP-536/PJ./2000. Two warnings:
>
> 1. KEP-536/PJ./2000 was issued under the pre-2008 PPh law and uses the old
>    9-digit KLU. The DJP has migrated to the 5-digit KBLI 2020. You MUST
>    confirm the exact NPPN% applicable to the client's current 5-digit KBLI
>    code in the latest KEP / PER published on www.pajak.go.id before signing
>    off any return.
> 2. The KEP-536 schedule distinguishes three regional tiers (10 ibukota
>    provinsi -- typically the highest %; other ibukota -- middle; daerah
>    lainnya -- lowest). The samples below show the 10-ibukota tier. Adjust
>    for the client's actual domicile tier.
>
> Where a coefficient cannot be confirmed in the current schedule, write
> "TBC -- see current KLU table" in the working paper and trigger R-ID-7.

**Sample KLU NPPN Coefficients**  _(KEP-536/PJ./2000)_

| Activity | KBLI | Indicative NPPN% (tier 1) |
| --- | --- | --- |
| Retail trade -- food & beverages (perdagangan eceran) | 47111 | ~30% (TBC) |
| Retail trade -- clothing | 47711 | ~30% (TBC) |
| Online retail seller (e-commerce) | 47911 | ~30% (TBC -- post-KEP-536 KBLI; use retail proxy) |
| Restaurants & cafés (restoran) | 56101 | ~25% (TBC) |
| Construction -- residential building | 41011 | ~20-25% (TBC) |
| Land transport -- taxi / ride-hail | 49429 | ~20% (TBC) |
| Vehicle rental without driver | 77100 | ~25% (TBC) |
| Hairdressing & beauty (salon) | 96021 | ~40% (TBC) |
| Doctor (specialist, private practice) | 86202 | ~50% (TBC) |
| Lawyer / advocate (pengacara) | 69100 | ~50% (TBC) |
| Notary / PPAT | 69200 | ~50% (TBC) |
| Accountant / tax consultant | 69201/69202 | ~50% (TBC) |
| Architect | 71101 | ~50% (TBC) |
| Software developer / freelance IT | 62010 | ~50% (TBC -- pekerjaan bebas) |
| Independent author / journalist | 90001 | ~50% (TBC) |
| Manufacture -- garments | 14111 | ~12.5-15% (TBC) |
| Repair of motor vehicles | 45201 | ~20% (TBC) |
| Educational tutoring (private) | 85490 | ~35% (TBC) |
| Photography services | 74201 | ~50% (TBC) |

**Conservative default:** when two KBLI codes plausibly fit a client's activity and one has a higher NPPN% than the other, apply the higher percentage (= higher deemed income = higher tax). Document the choice in the working paper and let the reviewer relax it if they disagree.

### Mixed activities

- **Mixed activities** — If a taxpayer has multiple distinct revenue streams (e.g. a freelance accountant who also runs an Etsy shop), apply the NPPN% separately to each stream's gross turnover. Pasal 14 ayat 3 UU PPh and PER-17/PJ/2015 art. 4 require segregated pencatatan by activity.  _(Pasal 14 ayat 3 UU PPh; PER-17/PJ/2015 art. 4)_

## Section 7 -- Transaction Classification

### How to map a bank statement line to an SPT line

- **Mapping procedure** — For each inflow/outflow: 1. Identify the counterparty and the underlying transaction (look at description, reference, invoice). 2. Decide which classification bucket it belongs to (table below). 3. Map to the SPT 1770 (individual) or SPT 1771 (corporate) line. 4. Tag any PPN component (recoverable / non-recoverable / out of scope). 5. Tag any PPh withholding that should have been or was applied. 6. Flag conservative defaults and "Needs Input" lines per the foundation contract.

### Buckets and SPT mapping -- INDIVIDUAL (SPT 1770)

**Buckets and SPT mapping -- INDIVIDUAL (SPT 1770)**

| Bucket (Bahasa) | Examples | SPT 1770 line |
| --- | --- | --- |
| Peredaran bruto dari usaha | Invoices paid, Shopee/Tokopedia payouts, POS settlement | Lampiran I Bag. A (pembukuan); Bag. B (NPPN) |
| Penghasilan dari pekerjaan bebas | Doctor/lawyer/consultant fees | As above; distinguished by KLU |
| Harga Pokok Penjualan (HPP) | Stock purchases, freight-in, direct labour, factory overhead | Pembukuan only -- Lampiran I Bag. A. NPPN: not claimed. |
| Beban usaha | Gaji, sewa, listrik, internet, ATK, penyusutan, asuransi | Pembukuan only. NPPN: not claimed. |
| Penghasilan lain-lain | Bank interest (final tax), forex gain, asset disposal gain | Induk Bag. A line 2; final-tax items → Lampiran III |
| Pasal 9 non-deductibles | Prive, private use, non-qualifying donations, certain provisions, in-kind (subject to PMK 66/2023), admin penalties | Pembukuan: koreksi fiskal positif. NPPN: n/a. |
| Pembelian aktiva tetap | Equipment, vehicles, computers | Capitalised; depreciated Pasal 11 golongan I-IV. NPPN: n/a. |
| Setoran modal pemilik | Owner injects cash | Equity -- not income. |
| Prive | Owner takes cash | Equity -- non-deductible (Pasal 9(1)(b)). |
| Pokok pinjaman | Loan drawdown / repayment principal | Balance sheet only. Interest deductible subject to DER 4:1. |
| Pembayaran pajak | PPh 25 instalments, withholdings, PPN setoran | PPh 25 = prepaid credit; own PPh = non-deductible (Pasal 9(1)(h)). |

### Buckets and SPT mapping -- BADAN (SPT 1771)

**Buckets and SPT mapping -- BADAN (SPT 1771)**

| Bucket | Bahasa | SPT 1771 line |
| --- | --- | --- |
| Gross revenue | Peredaran usaha | Lampiran I line 1.a |
| Cost of goods sold | Harga pokok penjualan | Lampiran I line 1.b |
| Gross profit | Laba bruto | Lampiran I line 1.c |
| Operating expenses | Biaya usaha lainnya | Lampiran I line 1.d |
| Operating profit | Penghasilan neto dari usaha | Lampiran I line 1.e |
| Non-operating income/expense | Penghasilan dari luar usaha / biaya dari luar usaha | Lampiran I line 2, 3 |
| Fiscal adjustments positive (add-backs) | Penyesuaian fiskal positif | Lampiran I line 5 |
| Fiscal adjustments negative | Penyesuaian fiskal negatif | Lampiran I line 6 |
| Final-tax income (carved out) | Penghasilan yang dikenakan PPh Final | Lampiran IV |
| Non-taxable income | Penghasilan yang tidak termasuk objek pajak | Lampiran IV |

## Section 8 -- Pasal 9 UU PPh: Non-Deductible Expenses

These items are NEVER deductible for either OP (pembukuan) or badan. If they appear in the books, classify them as koreksi fiskal positif (positive fiscal adjustment / add-back) when computing taxable income.

**Pasal 9(1) Non-Deductible Expenses**  _(Pasal 9(1) UU PPh)_

| Pasal 9(1) | Item | Notes |
| --- | --- | --- |
| a | Profit distributions (dividen, prive, SHU) | Already taxed at entity level. |
| b | Personal-benefit expenses of shareholders/partners | Private vehicle, family travel, personal insurance. |
| c | Reserves & provisions | Exceptions for bank bad-debt, mining reclamation, forestry replanting, insurance technical reserve (PMK 81/2009). |
| d | Self-paid health/life/accident/endowment premiums (individual) | Employer-paid for employees may be deductible as compensation. |
| e | Benefits in kind (natura/kenikmatan) | Largely deductible post-UU HPP subject to PMK 66/2023 carve-outs; add back if no carve-out confirmed. |
| f | Excessive related-party compensation | Only arm's-length portion deductible. |
| g | Gifts, aid, donations | Exception: approved zakat / disaster relief. |
| h | PPh on taxpayer's own income | Never deductible. Third-party withholdings are credits, not expenses. |
| i | Personal living expenses | Private rent, groceries, school fees. |
| j | "Salary" to members of firma/CV (capital not in shares) | Treated as profit distribution. |
| k | Administrative tax penalties (UU KUP sanksi) | Always added back. |

**Conservative default:** if a payment plausibly mixes personal and business use (vehicles, mobile phone, internet, partial home office), apportion using a reasonable business-use percentage and document the basis. If no basis can be documented, treat the entire amount as non-deductible.

## Section 9 -- Worked Example

### Scenario

Andi, an Indonesian individual resident, runs a freelance graphic-design practice. KLU/KBLI 74100 (specialised design activities) -- treated under pekerjaan bebas. Tax year 2025. He notified DJP on 28 February 2025 that he would use NPPN for 2025. His prior-year (2024) turnover was IDR 380 million, so he is eligible. Assume tier-1 NPPN% for design services is ~50% (TBC against current schedule).

### Bank statement extract (BCA business account, Jan-Dec 2025)

**Bank statement extract (BCA business account, Jan-Dec 2025)**

| Date | Description | Amount IDR | Classification | Notes |
| --- | --- | --- | --- | --- |
| 12 Jan | From PT XYZ -- invoice 001 | +18,500,000 | Peredaran bruto | PT XYZ should have withheld PPh 23 at 2%; declare gross (assume IDR 18.87m gross, 377k withheld) and claim credit. |
| 25 Jan | Sewa kantor co-working | -2,500,000 | Beban usaha (rent) | NPPN: NOT separately deductible. |
| 03 Feb | Cash -- penjualan tunai project A | +6,000,000 | Peredaran bruto | Add to gross. |
| 18 Feb | Adobe Creative Cloud | -812,000 | Beban usaha (software) | NPPN: ignored. Flag for PPN-PMSE. |
| 06 Mar | Penarikan biaya rumah tangga | -5,000,000 | Prive | Pasal 9(1)(b) -- never deductible. |
| 15 May | From CV ABC (gross 25m, PPh 23 500k) | +24,500,000 | Peredaran bruto | Declare 25m gross; claim 500k credit. |
| 30 Jun | PPh 25 angsuran Q2 | -1,200,000 | Prepaid PPh 25 | Credit; not an expense. |
| 08 Aug | Refund to client (project cancelled) | -3,000,000 | Reduction of peredaran bruto | Retur penjualan. |
| 12 Sep | Bank interest (giro) | +84,000 | Final-tax under PP 131/2000 (PPh 4(2)) | Exclude from NPPN base; Lampiran III. |
| 30 Nov | Stripe payout (USD 1,200) | +19,200,000 | Peredaran bruto -- export of services | No PPh 23 (non-resident payer). |

### NPPN computation (assuming 50% coefficient, TBC)

**NPPN computation (assuming 50% coefficient, TBC)**

| Item | IDR |
| --- | --- |
| Peredaran bruto (domestic clients) | 18,870,000 + 6,000,000 + 25,000,000 - 3,000,000 = 46,870,000 |
| Peredaran bruto (foreign clients) | 19,200,000 |
| Total peredaran bruto | 66,070,000 |
| NPPN% (50%) × peredaran bruto | 33,035,000 |
| Penghasilan neto dari pekerjaan bebas | 33,035,000 |
| Plus: bank interest -- FINAL TAX, not added to ordinary base | (excluded) |
| Less: PTKP (TK/0 hypothetically -- IDR 54,000,000) | (54,000,000) |
| Penghasilan Kena Pajak | NIL (loss carried forward NOT allowed under NPPN -- pencatatan does not produce a fiscal loss; Pasal 6 ayat 2 UU PPh only allows loss carryforward where pembukuan is kept) |
| PPh credits to claim | PPh 23 IDR 877,000 (370k + 500k+ 7k rounding) + PPh 25 IDR 1,200,000 -- may produce a refund (lebih bayar) |

This worked example is for illustration only. The actual rate, PTKP, and percentages must be computed in `id-income-tax`.

## Section 10 -- Conservative Defaults (Recap)

**Conservative Defaults (Recap)**

| Situation | Default |
| --- | --- |
| Turnover threshold ambiguous | Treat as pembukuan-required |
| Cash vs accrual ambiguous | Accrual |
| KLU has two plausible matches with different NPPN% | Use the higher % |
| Expense plausibly mixed personal/business with no documentation | Treat fully non-deductible |
| NPPN notification cannot be located in the file | Assume NOT validly elected -- treat as pembukuan and flag uplift risk under Pasal 14(5) |
| Income type unclear (final-tax vs ordinary) | Treat as ordinary (higher likely tax) and flag for reviewer |
| Foreign-currency receipt | Translate at the BI tengah-rate on receipt date; flag if BI rate not available |
| Inventory valuation method undocumented | Assume weighted-average |
| Bukti potong PPh 23/22/4(2) cannot be located | Do NOT claim the credit until obtained; revenue is still declared gross |
| Capex vs revex unclear (item between IDR 0 and IDR 1m useful life > 1 yr) | Capitalise. (Pasal 11 has no de-minimis; reviewer can expense.) |

## Section 11 -- Sources

**Sources**

| Citation | Where it bites |
| --- | --- |
| UU 6/1983 jo. UU 16/2009 jo. UU 7/2021 (HPP) -- KUP | Pembukuan obligation (Pasal 28), retention 10 yrs (Pasal 28(11)), Bahasa/IDR (Pasal 28(4)&(7)), method consistency (Pasal 28(5)), statute of limitations (Pasal 13) |
| UU 7/1983 jo. UU 36/2008 jo. UU 7/2021 -- PPh | NPPN & uplift (Pasal 14), non-deductibles (Pasal 9), depreciation (Pasal 11), loss carryforward (Pasal 6), inventory FIFO/avg (Pasal 10), arm's length (Pasal 18) |
| KEP-536/PJ./2000 | NPPN KLU coefficient schedule. Confirm with later PER/KEP before signing. |
| PER-17/PJ/2015 | NPPN notification procedure; segregated pencatatan by activity |
| PMK 196/PMK.03/2007 (as amended) | USD bookkeeping permission |
| PMK 213/PMK.03/2016 | Transfer pricing documentation refusal trigger |
| PP 23/2018 + PP 55/2022 | UMKM 0.5% final-tax regime + time limits |
| PMK 66/PMK.03/2023 | In-kind benefit (natura) carve-outs |
| PMK 81/PMK.03/2024 | Coretax filing channel from 2025 |
| PMK 169/PMK.010/2015 | Thin-cap DER 4:1 |

**Verification status:** All citations above are statutory or PMK-level references that were operative at the time of drafting (tax year 2025). The NPPN coefficient table in Section 6 is illustrative; before signing off any return that relies on a specific NPPN%, the reviewer must confirm the current coefficient in the latest DJP-published instrument for the client's exact 5-digit KBLI and regional tier.

## Section 12 -- Output Contract

When this skill is invoked to classify a transaction set, produce:

1. **Working paper (CSV or table)** -- one row per transaction with columns: date, counterparty, amount IDR, classification bucket, SPT 1770/1771 line, PPh withholding flag, PPN flag, conservative-default flag, evidence reference, reviewer note.
2. **Regime summary** -- pembukuan or NPPN; if NPPN, the KLU code used, the NPPN% applied, and the citation.
3. **Reviewer brief** -- list of "Needs Input" items and "Assumed" items with cash impact ranking per the foundation contract.
4. **Sources block** -- every cited Pasal / PMK / KEP that materially drove a classification.
5. **Sign-off checklist** -- pre-populated for the credentialed reviewer (Konsultan Pajak Bersertifikat / Akuntan Publik / Kuasa Hukum Pajak per UU Konsultan Pajak draft & PMK 111/PMK.03/2014).

No SPT figure leaves this skill without a numbered citation. No NPPN coefficient leaves this skill without a "TBC verified against current KEP/PER on [date]" note.

## End of skill.

*End of skill.*

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
