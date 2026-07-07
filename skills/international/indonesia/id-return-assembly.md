---
name: id-return-assembly
description: Use this skill whenever asked to assemble, finalize, or package an Indonesian annual tax return. Trigger on phrases like "assemble Indonesian return", "prepare SPT 1770", "prepare SPT 1771", "Indonesia annual tax return", "Indonesian working paper", "Indonesian tax filing package", "finalize SPT Tahunan", or "Coretax filing package". This is the capstone orchestrator that pulls together outputs from id-pph-final-umkm, id-income-tax, id-corporate-tax, id-payroll-pph21, indonesia-vat, id-withholding, and id-bookkeeping into a single SPT working paper plus payment and filing instructions. It does not recompute anything itself — it reconciles upstream outputs, builds the line-by-line SPT working paper, generates kode billing payment instructions for Coretax, and produces a reviewer brief and taxpayer action list. ALWAYS read this skill last when finalizing an Indonesian tax return.
jurisdiction: ID
domain: international
tax_year: 2025
tier: 2
last_updated: 2026-07-06
---

# id-return-assembly

## CRITICAL EXECUTION DIRECTIVE — READ FIRST

When this skill is invoked, the user has already passed through intake and the relevant content skills. They want their finished SPT working paper. Execute all steps without pausing for permission.

Specifically:

- Do NOT ask "do you want me to assemble the full package". The user asked for the return. Produce it.
- Do NOT re-interrogate the user about residency, NPWP, or business structure — intake already captured this; trust the upstream packages.
- Do NOT pause between reconciliation steps to check in. Run all cross-checks in sequence; flag failures in the reviewer brief and continue.
- Self-checks are targets, not blockers. If a check fails, note it under "Reviewer Attention Flags" and continue.
- Do NOT submit anything to Coretax. This skill produces a working paper plus filing instructions. A qualified Indonesian tax consultant (Konsultan Pajak bersertifikat) must review and the taxpayer (or authorised filer) submits via Coretax.

If you feel the urge to ask "how should I proceed", pick the most defensible path, proceed, and flag the decision for the reviewer.

## What this file is

The final capstone skill for Indonesian annual tax returns. It consumes the outputs of every other Indonesia skill and assembles a single unified working paper covering either:

- SPT 1770 / 1770S / 1770SS — annual return for resident individuals (Orang Pribadi), including sole proprietors operating under UMKM PPh Final (PP 55/2022) or the progressive regime
- SPT 1771 — annual return for resident corporates (Badan), including PT, CV, and Koperasi

The output is a reviewer-ready package: line-by-line SPT working paper, cross-skill reconciliation table, payment instructions (kode billing for Coretax), filing instructions, reviewer checklist, and taxpayer action list.

## Section 1 — Quick reference

**Quick reference table**

| Field | Value |
| --- | --- |
| Country | Indonesia (Republik Indonesia) |
| Tax authority | Direktorat Jenderal Pajak (DJP) — Directorate General of Taxes |
| Filing portal | Coretax DJP (https://coretaxdjp.pajak.go.id) — successor to DJP Online/e-Filing as of 1 January 2025 |
| Currency | IDR (Indonesian Rupiah / Rp) |
| Tax year | Calendar year (1 January – 31 December) |
| Current tax year | 2025 (filing window opens 1 January 2026) |
| Individual return | SPT Tahunan PPh Orang Pribadi — Form 1770 / 1770S / 1770SS |
| Corporate return | SPT Tahunan PPh Badan — Form 1771 |
| Individual deadline | 31 March 2026 (3 months after year-end) |
| Corporate deadline | 30 April 2026 (4 months after year-end) |
| Confirmation receipt | BPE — Bukti Penerimaan Elektronik (electronic filing receipt) |
| Governing law | UU KUP No. 6/1983 (as amended); UU PPh No. 36/2008; UU HPP No. 7/2021; PMK 81/2024 (Coretax implementation) |
| Skill version | 1.0 |
| Validated by | Pending — requires sign-off by Konsultan Pajak bersertifikat (certified Indonesian tax consultant) |

## Section 2 — Required inputs from upstream skills

The assembly skill does not recompute anything. It expects structured outputs from the following upstream skills. If an upstream skill did not run, the assembly notes the gap and continues with available data.

### 2.1 Individual return (SPT 1770) — inputs

**Individual return inputs table**

| Upstream skill | Output consumed | Where it lands on the SPT |
| --- | --- | --- |
| `id-bookkeeping` | General ledger trial balance; income/expense detail | Source for Lampiran I (business income) |
| `id-income-tax` | Progressive PPh OP computation: PKP, PPh terutang, PTKP applied | Form 1770 Induk Part B & C |
| `id-pph-final-umkm` | UMKM Final 0.5% computation; monthly SSP records; cumulative gross turnover; verification turnover is ≤ IDR 4.8 billion | Lampiran III-A (PPh Final & Bersifat Final) |
| `id-payroll-pph21` | Employment income from Bukti Potong 1721-A1; PPh 21 already withheld | Form 1770 Induk Part A; Lampiran I Bagian B |
| `indonesia-vat` | If individual is PKP: VAT input/output position; nothing flows to PPh return but reviewer checks consistency of revenue figures | Cross-check only, not a line on 1770 |
| `id-withholding` | Bukti Potong PPh 22 / 23 / 4(2) received as a recipient; PPh 22 / 23 / 4(2) paid as a withholder | Lampiran I & III (credits); separate SPT Masa for amounts withheld |

### 2.2 Corporate return (SPT 1771) — inputs

**Corporate return inputs table**

| Upstream skill | Output consumed | Where it lands on the SPT |
| --- | --- | --- |
| `id-bookkeeping` | Full audited or management financial statements: Neraca (balance sheet), Laporan Laba Rugi (P&L) | Lampiran V (financial statements); Lampiran I (fiscal reconciliation) |
| `id-corporate-tax` | Fiscal profit (laba fiskal); PPh Badan computation at 22% (or facility-eligible rates per UU HPP); deferred tax | Form 1771 Induk Part B & C |
| `id-pph-final-umkm` | If entity qualifies for PP 55/2022 0.5% Final regime and is within the 3-year UMKM Badan window (PT) or 4-year window (CV/Firma/Koperasi) | Lampiran IV (PPh Final & Bersifat Final) |
| `id-payroll-pph21` | Employee payroll cost classification; PPh 21 employer obligations reconciled | Lampiran II (cost of employment) |
| `indonesia-vat` | If PKP: VAT input/output reconciled; PPN paid is not deductible for PPh; cross-check revenue figures match | Cross-check; PPN Masukan that becomes a cost flows to fiscal P&L |
| `id-withholding` | PPh 22/23/4(2)/15/26 withheld by counterparties (credits on 1771); withholding made by entity on suppliers (SPT Masa obligations) | Lampiran III (kredit pajak); separate SPT Masa monthly |

### 2.3 Intake-required identifiers

**Intake-required identifiers table**

| Identifier | Required for |
| --- | --- |
| NPWP (Nomor Pokok Wajib Pajak) — 16-digit (post-Coretax merge with NIK for individuals) | All returns |
| NITKU (Nomor Identitas Tempat Kegiatan Usaha) — branch/location identifier introduced under Coretax | All returns post-PMK 81/2024 |
| KLU (Klasifikasi Lapangan Usaha) — business classification code | Determines JKK class, applicability of UMKM regime |
| KPP code (Kantor Pelayanan Pajak / tax office) | Filing location, kode billing routing |
| Marital status & dependents (for individuals) | PTKP determination |

### 2.3 Intake-required identifiers

If any identifier is missing, the assembly skill flags it as "Needs Input" and produces the working paper with placeholders rather than halting.

## Section 3 — Tax computation reconciliation

The assembly skill verifies that numbers from the upstream skills are mutually consistent. If a cross-check fails by more than IDR 1,000, the discrepancy is raised in the reviewer brief — never silently rounded.

### Cross-check 1 — Revenue reconciliation (turnover ties across skills)

**Revenue reconciliation table**

| Source | Figure | Rule |
| --- | --- | --- |
| `id-bookkeeping` P&L gross revenue | Total operating revenue | Anchor figure |
| `indonesia-vat` annual DPP (Dasar Pengenaan Pajak) on output VAT | Sum of monthly SPT Masa PPN Faktur Pajak Keluaran | Must reconcile to bookkeeping revenue ± permitted timing differences |
| `id-pph-final-umkm` cumulative gross turnover | Sum of monthly UMKM gross | Must equal bookkeeping revenue for the UMKM-eligible portion |
| `id-income-tax` or `id-corporate-tax` gross income | Top line of fiscal P&L | Must equal bookkeeping ± fiscal-vs-commercial adjustments (Lampiran I) |

### Cross-check 1 — Revenue reconciliation (turnover ties across skills)

If mismatch: Likely causes are (i) VAT-exempt revenue (PPN dibebaskan) not in VAT output, (ii) accrual vs cash timing differences, (iii) intra-group eliminations, (iv) revenue that is itself PPh Final at source (rental, construction).

### Cross-check 2 — PPh credits add up correctly

For individuals (SPT 1770):

### Cross-check 2 — PPh credits add up correctly

**PPh credits table (individuals)**

| Line | Source skill | Description |
| --- | --- | --- |
| PPh 21 withheld by employer(s) | id-payroll-pph21 (Bukti Potong 1721-A1) | Credit |
| PPh 22 withheld at import / state purchase | id-withholding | Credit |
| PPh 23 withheld on services / royalties / dividends | id-withholding | Credit |
| PPh 24 — foreign tax credit | id-income-tax (if applicable) | Credit, capped |
| PPh 25 — monthly installments paid during the year | id-income-tax | Credit |
| PPh Final paid (UMKM 0.5%, rental, etc.) | id-pph-final-umkm | NOT a credit against progressive PPh — separate column |

### Cross-check 2 — PPh credits add up correctly

- **Corporate credit list and credit cap rule** — For corporates (SPT 1771): same list except no PPh 21 employment credit (employer does not personally claim PPh 21 against PPh Badan). Total credits cannot exceed PPh terutang (tax liable) for refund purposes unless the excess is properly recognised in Lampiran III with supporting Bukti Potong.

### Cross-check 3 — PPh Final UMKM matches monthly SSPs (Surat Setoran Pajak)

**UMKM SSP reconciliation table**

| Item | Source | Rule |
| --- | --- | --- |
| Sum of monthly UMKM 0.5% paid via SSP | id-pph-final-umkm monthly log | Must equal 0.5% × cumulative gross turnover for UMKM-eligible months |
| Coretax billing receipts (NTPN — Nomor Transaksi Penerimaan Negara) | Bank statements / Coretax history | Each monthly payment must have an NTPN |
| Threshold guard: cumulative turnover ≤ IDR 4.8 billion for the year | id-pph-final-umkm | If exceeded mid-year, switch to progressive PPh from the month following the breach |

### Cross-check 3 — PPh Final UMKM matches monthly SSPs (Surat Setoran Pajak)

If mismatch: Investigate missing months (UMKM is monthly, due 15th of the following month under PMK 164/2023), incorrect NTPN, or threshold breach not actioned.

### Cross-check 4 — PPh 21 reconciliation between annual and monthly returns

**PPh 21 reconciliation table**

| Item | Source | Rule |
| --- | --- | --- |
| Sum of monthly SPT Masa PPh 21 filed (Jan–Nov via TER) | id-payroll-pph21 | Should match total TER withholding for the year |
| December true-up (annual recalculation under PP 58/2023) | id-payroll-pph21 | Reconciled to annual PPh 21 terutang |
| Total PPh 21 borne by entity | id-payroll-pph21 employer cost | Cross-checked to Form 1721 A1 (employer's annual PPh 21 return), due 31 March 2026 |

### Cross-check 4 — PPh 21 reconciliation between annual and monthly returns

If mismatch: Likely cause is mid-year joiners/leavers, bonus or THR not included in the correct month's TER, or December true-up not booked.

### Cross-check 5 — Withholding compliance as a withholding agent

If the taxpayer (especially a Badan) is required to withhold PPh on its suppliers:

### Cross-check 5 — Withholding compliance as a withholding agent

**Withholding agent compliance table**

| Item | Source | Rule |
| --- | --- | --- |
| PPh 23 withheld on services and royalties paid | id-withholding | Sum of monthly SPT Masa PPh 23/26 |
| PPh 4(2) withheld on rent, construction, prizes | id-withholding | Sum of monthly SPT Masa PPh 4(2) |
| PPh 21/26 withheld on consultants and non-employees | id-payroll-pph21 + id-withholding | Sum of monthly SPT Masa PPh 21/26 |
| Bukti Potong issued to counterparties | id-withholding e-Bupot Unifikasi | Should match the SPT Masa filings |

### Cross-check 5 — Withholding compliance as a withholding agent

- **Withholding obligation rule** — Withholding is the entity's obligation, not its own tax credit. Failure to withhold is corrected with Surat Setoran Pajak plus 2% per month interest (UU HPP). Flag any apparent failure for the reviewer.  _(UU HPP)_

### Cross-check 6 — VAT-to-PPh consistency (for PKP)

**VAT-to-PPh consistency table**

| Item | Source | Rule |
| --- | --- | --- |
| PPN Masukan that was creditable | indonesia-vat | NOT a cost in fiscal P&L |
| PPN Masukan that was non-creditable (per Pasal 9(8) UU PPN) | indonesia-vat | IS a cost in fiscal P&L |
| PPN on capital goods | indonesia-vat | Either credited (PKP) or capitalised into asset cost (non-PKP) |

### Cross-check 6 — VAT-to-PPh consistency (for PKP)

If inconsistency: An expense net of PPN in the P&L while the PPN was also not claimed on the VAT return means the PPN is lost. Flag for reviewer.

### Cross-check 7 — Tolerance discipline

- **Reconciliation tolerance thresholds** — For every cross-check above, the threshold is IDR 1,000. If a difference is between IDR 1,000 and IDR 100,000, document the variance and proceed with a reviewer flag. If above IDR 100,000, raise as "Needs Input" — the reviewer should resolve before sign-off.

## Section 4 — Working paper template: individual SPT 1770

The working paper is built around the structure of Form 1770 (the full form for individuals with business or multiple income sources). Form 1770S applies to individuals with single-employer income above IDR 60 million but no business income; Form 1770SS applies to single-employer income ≤ IDR 60 million. The assembly skill picks the correct form based on intake.

### 4.1 Induk Form 1770 — line-by-line

**Induk Form 1770 line-by-line table**

| Bagian (Part) | Line | Description | Source |
| --- | --- | --- | --- |
| **Identitas** | NPWP, NIK, NITKU, name, KLU, address, marital status | All | Intake |
| **A. Penghasilan Neto** | 1 | Net income from business (usaha) — progressive regime | id-income-tax |
|  | 2 | Net income from independent profession (pekerjaan bebas) | id-income-tax |
|  | 3 | Net income from employment | id-payroll-pph21 (sum of Bukti Potong 1721-A1) |
|  | 4 | Net income from other sources (dalam negeri lainnya) | id-bookkeeping (interest, royalties, sewa non-final) |
|  | 5 | Net foreign income (luar negeri) | id-income-tax (if applicable) |
|  | 6 | **Total penghasilan neto** | Sum 1–5 |
| **B. Penghasilan Tidak Kena Pajak (PTKP)** | 7 | PTKP based on K/0, K/1, …, TK/0, etc. | id-payroll-pph21 PTKP table |
| **C. Penghasilan Kena Pajak (PKP)** | 8 | Line 6 − Line 7 | Computed |
| **D. PPh Terutang** | 9 | Apply progressive brackets to Line 8 | id-income-tax |
| **E. Kredit Pajak** | 10 | PPh 21 withheld | id-payroll-pph21 |
|  | 11 | PPh 22 / 23 / 24 / 25 | id-withholding + id-income-tax (PPh 25) |
|  | 12 | Total credits | Sum |
| **F. PPh Kurang/Lebih Bayar** | 13 | Line 9 − Line 12 (positive = balance due; negative = refund / kompensasi) | Computed |
| **G. Angsuran PPh 25 tahun berikutnya** | 14 | Monthly installment for 2026 = PPh terutang ÷ 12 (subject to adjustments per PMK 215/2018) | id-income-tax |

### 4.2 Lampiran (Schedules) checklist

**Lampiran checklist table (1770)**

| Lampiran | Title | When used |
| --- | --- | --- |
| Lampiran I | Penghasilan Neto Dalam Negeri Lainnya & Penghasilan Neto Luar Negeri | If non-employment, non-business income exists |
| Lampiran II | Daftar Pemotongan / Pemungutan PPh oleh Pihak Lain dan PPh Yang Ditanggung Pemerintah | List every Bukti Potong received |
| Lampiran III | Penghasilan yang Dikenakan PPh Final dan/atau Bersifat Final | UMKM 0.5%, deposito interest 20%, dividend 10%, rental 10%, etc. |
| Lampiran IV | Harta pada Akhir Tahun & Kewajiban / Utang pada Akhir Tahun | Net worth disclosure (mandatory) |
| Lampiran V | Daftar Susunan Anggota Keluarga | Family members for PTKP support |

### 4.3 UMKM PPh Final treatment on 1770

- **UMKM treatment on 1770** — If the taxpayer used PP 55/2022 UMKM 0.5% during 2025: Business gross turnover that was UMKM-final goes to Lampiran III, NOT Part A line 1. PPh Final UMKM paid via monthly SSP is reported on Lampiran III; it is not a credit against progressive PPh — it is a separate final settlement. If the IDR 4.8 billion cumulative threshold was breached mid-year, the months after the breach revert to progressive regime; the working paper must split the year cleanly.  _(PP 55/2022)_

## Section 5 — Working paper template: corporate SPT 1771

### 5.1 Induk Form 1771 — line-by-line

**Induk Form 1771 line-by-line table**

| Bagian | Line | Description | Source |
| --- | --- | --- | --- |
| **Identitas** | NPWP, NITKU, name, KLU, address, accounting period | All | Intake |
| **A. Penghasilan Kena Pajak** | 1a | Peredaran usaha (gross revenue) | id-bookkeeping |
|  | 1b | HPP / cost of goods sold | id-bookkeeping |
|  | 1c | Laba bruto | Computed |
|  | 1d | Operating expenses (biaya usaha lainnya) | id-bookkeeping |
|  | 1e | Laba neto komersial | Computed |
|  | 2 | Fiscal adjustments (koreksi fiskal positif / negatif) | id-corporate-tax (Lampiran I) |
|  | 3 | Penghasilan neto fiskal | Computed |
|  | 4 | Kompensasi kerugian (loss carryforward, up to 5 years per UU PPh Pasal 6) | id-corporate-tax |
|  | 5 | **Penghasilan Kena Pajak** | Line 3 − Line 4 |
| **B. PPh Terutang** | 6 | Tax rate applied: 22% standard (UU HPP Pasal 17); or 11% facility on PKP up to IDR 4.8B for entities with revenue ≤ IDR 50B (UU HPP Pasal 31E) | id-corporate-tax |
|  | 7 | PPh terutang | Line 5 × rate |
| **C. Kredit Pajak** | 8a | PPh 22 withheld | id-withholding |
|  | 8b | PPh 23 withheld | id-withholding |
|  | 8c | PPh 24 foreign tax credit (capped) | id-corporate-tax |
|  | 8d | PPh 25 monthly installments paid | id-corporate-tax |
|  | 8e | PPh 26 (if applicable) | id-withholding |
|  | 8f | Total | Sum |
| **D. PPh Kurang/Lebih Bayar** | 9 | Line 7 − Line 8f | Computed |
| **E. Angsuran PPh 25 tahun berikutnya** | 10 | Monthly installment for 2026 | id-corporate-tax |

### 5.2 Lampiran (Schedules) checklist

**Lampiran checklist table (1771)**

| Lampiran | Title | When used |
| --- | --- | --- |
| Lampiran I — 1771-I | Penghitungan Penghasilan Neto Fiskal (fiscal reconciliation) | Always |
| Lampiran II — 1771-II | Perincian Harga Pokok Penjualan, Biaya Usaha Lainnya, dan Biaya dari Luar Usaha | Always |
| Lampiran III — 1771-III | Kredit Pajak Dalam Negeri | If domestic withholding credits exist |
| Lampiran IV — 1771-IV | PPh Final dan Penghasilan Yang Tidak Termasuk Objek Pajak | If UMKM Final or non-objek income |
| Lampiran V — 1771-V | Daftar Pemegang Saham/Pemilik Modal dan Daftar Susunan Pengurus/Komisaris | Always |
| Lampiran VI — 1771-VI | Daftar Penyertaan Modal Pada Perusahaan Afiliasi, Daftar Pinjaman Antar Pihak Berelasi | If related-party transactions exist (transfer pricing trigger) |
| Lampiran khusus | Transfer pricing documentation summary (Lampiran 3A / 3B) | If related-party transactions exceed thresholds in PMK 213/2016 |

### 5.3 UMKM PPh Final treatment on 1771

- **UMKM treatment on 1771 and window durations** — If the entity used PP 55/2022 UMKM 0.5% during 2025: The UMKM window is time-limited: 3 years for PT, 4 years for CV/Firma/Koperasi, 7 years for individuals (Orang Pribadi) measured from the start year of UMKM utilisation (PP 55/2022 Pasal 59). Revenue under UMKM goes to Lampiran IV (PPh Final), not the main PKP computation. The reviewer must confirm the entity is within its UMKM window. If 2025 is the final eligible year, this must be flagged so 2026 planning reflects the switch to standard 22% regime.  _(PP 55/2022 Pasal 59)_

## Section 6 — Payment instructions: kode billing & SSP via Coretax

Under PMK 81/2024 (Coretax implementation), all PPh payments are settled by generating a kode billing (15-digit billing code) in Coretax DJP, then paying via bank channel (teller, ATM, internet banking, m-banking) or authorised payment processor. The successful payment generates an NTPN (Nomor Transaksi Penerimaan Negara) which is the proof of payment.

### 6.1 Kode Akun Pajak (MAP) — common codes

**MAP codes table**  _(PMK 81/2024)_

| MAP code | Description | Used for |
| --- | --- | --- |
| 411125 | PPh Pasal 25/29 Orang Pribadi | Individual annual settlement (Line 13 on 1770) + monthly PPh 25 |
| 411126 | PPh Pasal 25/29 Badan | Corporate annual settlement (Line 9 on 1771) + monthly PPh 25 |
| 411128 | PPh Final | UMKM 0.5% (PP 55/2022); rental 10%; deposit interest 20%; etc. — Kode Jenis Setoran (KJS) sub-code disambiguates |
| 411121 | PPh Pasal 21 | Monthly employment withholding |
| 411124 | PPh Pasal 23 | Monthly withholding on services, royalties, etc. |
| 411127 | PPh Pasal 26 | Withholding on non-residents |
| 411122 | PPh Pasal 22 | Import / state purchases / pertamina |
| 411211 | PPN Dalam Negeri | Monthly PPN settlement |
| 411221 | PPN Impor | Import VAT |

### 6.1 Kode Akun Pajak (MAP) — common codes

TBC — verify current MAP code in Coretax before generating the billing. The list below is the conventional set; Coretax may have introduced new MAP codes since 1 January 2025 transition. Always confirm against the Coretax dropdown at billing time.

### 6.2 KJS (Kode Jenis Setoran) — sub-code

- **KJS sub-code rule** — For each MAP code, a KJS specifies the nature of the payment (e.g., MAP 411125 with KJS 200 = "Tahunan" / annual; KJS 100 = "Masa" / monthly). The reviewer must confirm the correct KJS pairing. Coretax surfaces only the valid combinations once the MAP is selected.

### 6.3 Billing-to-payment flow

1. Log into Coretax DJP with NPWP + password (or DJP-issued certificate for businesses)
2. Navigate to "Pembuatan Kode Billing" (Generate Billing Code)
3. Select Jenis Pajak (MAP), KJS, Masa Pajak (tax period), and amount
4. Generate billing — receives 15-digit ID-Billing valid for 30 days
5. Pay via authorised channel (bank transfer / Virtual Account / Tokopedia / Bukalapak / Pos Indonesia / etc.)
6. Receive NTPN (printable / downloadable in Coretax) — this is the legal proof of payment
7. NTPN auto-feeds into Coretax taxpayer ledger; appears as a credit on the relevant SPT

### 6.4 Payment timing relative to filing

**Payment timing table**

| Payment | Due date | Filing reference |
| --- | --- | --- |
| PPh kurang bayar — Individuals (1770) | **Before** filing the SPT 1770 and **no later than 31 March 2026** | Line 13 on 1770 |
| PPh kurang bayar — Corporates (1771) | **Before** filing the SPT 1771 and **no later than 30 April 2026** | Line 9 on 1771 |
| Monthly PPh 21 (December 2025) | 10 January 2026 (PMK 81/2024 Article 60) | SPT Masa PPh 21 December |
| Monthly PPh 25 (December 2025) | 15 January 2026 | Monthly installment |
| Monthly UMKM Final (December 2025) | 15 January 2026 | SSP via Coretax |
| Monthly PPN (December 2025) | End of January 2026 | SPT Masa PPN December |

### 6.4 Payment timing relative to filing

- **NTPN existence rule** — The NTPN must exist before SPT submission, otherwise the credit cannot be claimed on the return.

## Section 7 — Filing instructions: Coretax DJP

### 7.1 Filing channels

**Filing channels table**

| Channel | Description | Best for |
| --- | --- | --- |
| **Coretax Web — Form Upload** | Generate XML from Coretax Form (preview / fill in browser), download, re-upload | Standard returns |
| **Coretax Web — Direct Entry** | Fill the SPT directly in the browser | Simple returns (1770SS, 1770S without business income) |
| **Coretax Web — Bulk XML Upload** | For taxpayers using third-party software that exports the DJP-compliant XML | Corporates with ERP integration |
| **Coretax Mobile App** | Limited subset (1770SS / simple individual) | Salaried individuals with single employer |

### 7.2 Submission steps

1. Pay first — all kurang bayar amounts must be settled (NTPN issued) before submission
2. Log into Coretax (NPWP + password; or sertifikat elektronik for badan)
3. Navigate to "SPT Tahunan" → select form type (1770 / 1770S / 1770SS / 1771)
4. Upload supporting documents:
   - Form 1721-A1 (employer's PPh 21 statement) for individuals with employment income
   - Bukti Potong PPh 22 / 23 / 4(2) for any withholding credits claimed
   - Laporan Keuangan (financial statements) for individuals using progressive regime with business income AND for all corporates
   - Audit report (Laporan Auditor Independen) for corporates required to audit (revenue / assets thresholds per UU PT)
5. Validate — Coretax runs schema and arithmetic checks; resolve any errors
6. Submit — receive BPE (Bukti Penerimaan Elektronik) with a 19-digit BPE number and timestamp
7. Save BPE — this is the legal proof of filing and must be retained

### 7.3 Deadlines (tax year 2025)

**Deadlines table**

| Filer type | SPT form | Deadline |
| --- | --- | --- |
| Individual (Orang Pribadi) | 1770 / 1770S / 1770SS | **31 March 2026** (UU KUP Pasal 3 ayat 3 huruf b) |
| Corporate (Badan) | 1771 | **30 April 2026** (UU KUP Pasal 3 ayat 3 huruf c) |
| Extension request | Form 1770-Y or 1771-Y | Filed before the original deadline; extension is max 2 months; interest accrues on any underpayment |

### 7.4 Late filing penalties

**Late filing penalties table**

| Filer | Penalty | Basis |
| --- | --- | --- |
| Individual | IDR 100,000 (administrative fine) | UU KUP Pasal 7 |
| Corporate | IDR 1,000,000 (administrative fine) | UU KUP Pasal 7 |
| Late payment | 2% interest per month (capped at 24 months), now linked to MoF benchmark interest rate under UU HPP | UU KUP Pasal 9 ayat 2a |

## Section 8 — Reviewer brief contents

The reviewer brief is a single markdown file the warranted reviewer (Konsultan Pajak bersertifikat) reads before sign-off.

```markdown
# Complete Return Package — [Taxpayer Name] — Tax Year 2025

## Executive Summary
- Filing entity: [Orang Pribadi / Badan (PT / CV / Koperasi)]
- NPWP: [16-digit]
- NITKU: [if applicable]
- KLU: [code + description]
- Tax regime: [Progressive PPh OP / PPh Badan 22% / UMKM PP 55/2022 0.5% Final]
- VAT status: [PKP / non-PKP]
- SPT form: [1770 / 1770S / 1770SS / 1771]
- PPh terutang: IDR X
- Total kredit pajak: IDR X
- PPh kurang/lebih bayar: IDR X
- Filing deadline: [31 March 2026 / 30 April 2026]

## Income Tax Computation
[From id-income-tax or id-corporate-tax]
- Line-by-line working paper of the Induk form
- Fiscal reconciliation (Lampiran I-1771) for corporates
- Loss carryforward schedule for corporates
- Foreign tax credit computation (PPh 24) if applicable

## UMKM Final Tax (if applicable)
[From id-pph-final-umkm]
- Monthly SSP register with NTPN
- Cumulative turnover tracker
- UMKM window remaining (years left under PP 55/2022)
- IDR 4.8B threshold guard

## Payroll & PPh 21
[From id-payroll-pph21]
- Form 1721 A1 summary (annual employer return)
- Monthly TER reconciliation
- December true-up
- BPJS reconciliation

## VAT (if PKP)
[From indonesia-vat]
- Annual SPT Masa PPN summary
- Output / input VAT reconciliation
- Cross-check to PPh revenue

## Withholding (PPh 22 / 23 / 4(2) / 26)
[From id-withholding]
- As recipient: list of Bukti Potong claimed as credits
- As withholding agent: monthly SPT Masa compliance

## Cross-Skill Reconciliation
- Revenue reconciliation: [pass/fail]
- PPh credits add up: [pass/fail]
- UMKM monthly SSPs reconcile: [pass/fail]
- PPh 21 annual vs monthly: [pass/fail]
- Withholding agent compliance: [pass/fail]
- VAT-to-PPh consistency: [pass/fail]

## Reviewer Attention Flags
- Items requiring Konsultan Pajak confirmation
- Mixed-use expenses; entertainment with no nominatif list (UU PPh Pasal 6 - non-deductible if no list)
- Related-party transactions (transfer pricing trigger per PMK 213/2016)
- UMKM window expiring
- Approaching IDR 4.8B threshold
- Bukti Potong without matching NTPN

## Positions Taken
[List with legislation citations]
- e.g., "UMKM 0.5% applied on IDR X turnover — PP 55/2022 Pasal 56"
- e.g., "Article 31E facility applied: 11% on PKP up to IDR 4.8B — UU HPP Pasal 17(2b)"
- e.g., "Entertainment expenses included in nominatif list — UU PPh Pasal 6 ayat 1(a)"

## Planning Notes for 2026
- Monthly PPh 25 installments for 2026
- UMKM window monitoring
- VAT threshold (IDR 4.8B PKP threshold)
- Anticipated transfer pricing documentation requirements
- Legislative changes effective 1 January 2026 (if any)
```

## Section 9 — Final taxpayer action list

```markdown
# Action List — [Taxpayer Name] — Tax Year 2025

## Immediate (before SPT filing deadline)

### For individuals — deadline 31 March 2026:
1. Generate kode billing for PPh kurang bayar of IDR X (MAP 411125, KJS 200) in Coretax
2. Pay via bank channel; obtain NTPN
3. Confirm all monthly PPh 21 (Dec 2025) settled (MAP 411121)
4. Confirm December PPh 25 installment (MAP 411125, KJS 100) settled
5. Confirm December UMKM Final (MAP 411128) settled, if applicable
6. Upload documents in Coretax → submit SPT 1770 → save BPE

### For corporates — deadline 30 April 2026:
1. Generate kode billing for PPh Badan kurang bayar of IDR X (MAP 411126, KJS 200)
2. Pay via bank channel; obtain NTPN
3. Confirm all monthly PPh 21 (Dec 2025) settled (MAP 411121)
4. Confirm December PPh 25 installment (MAP 411126, KJS 100) settled
5. Confirm December UMKM Final (MAP 411128) settled, if applicable
6. Attach audited financial statements (if revenue / asset thresholds breached)
7. Upload documents in Coretax → submit SPT 1771 → save BPE
8. File Form 1721 A1 (annual PPh 21 employer return) — deadline 31 March 2026

## Monthly compliance through 2026

| Item | MAP | Due |
|---|---|---|
| PPh 21 (monthly) | 411121 | 10th of following month |
| PPh 25 (monthly installment) | 411125/126 KJS 100 | 15th of following month |
| UMKM Final 0.5% (if applicable) | 411128 | 15th of following month |
| PPh 23 / 4(2) withheld | 411124 / 411128 | 10th of following month |
| SPT Masa PPN (if PKP) | 411211 | End of following month |

## Record retention

Per UU KUP Pasal 28 ayat 11, accounting records must be retained for 10 years in Indonesia. This includes:
- General ledger and supporting documents
- Bukti Potong issued and received
- Faktur Pajak (PPN invoices)
- SSP / NTPN receipts
- BPE filing receipts

Records must be kept in Indonesia (Pasal 28 ayat 11) — offshore storage requires DJP approval.
```

## Section 9 — Final taxpayer action list

**Monthly compliance through 2026**

| Item | MAP | Due |
| --- | --- | --- |
| PPh 21 (monthly) | 411121 | 10th of following month |
| PPh 25 (monthly installment) | 411125/126 KJS 100 | 15th of following month |
| UMKM Final 0.5% (if applicable) | 411128 | 15th of following month |
| PPh 23 / 4(2) withheld | 411124 / 411128 | 10th of following month |
| SPT Masa PPN (if PKP) | 411211 | End of following month |

## Section 9 — Final taxpayer action list

- **Record retention period** — Per UU KUP Pasal 28 ayat 11, accounting records must be retained for 10 years in Indonesia, including general ledger and supporting documents, Bukti Potong issued and received, Faktur Pajak (PPN invoices), SSP/NTPN receipts, and BPE filing receipts. Records must be kept in Indonesia (Pasal 28 ayat 11) — offshore storage requires DJP approval.  _(UU KUP Pasal 28 ayat 11)_

## Section 10 — 2026 planning notes

The capstone produces a forward-looking section so the taxpayer arrives at next year's filing with no surprises.

### 10.1 Monthly PPh 25 for 2026

- **PPh 25 monthly installment formula** — Individuals (PMK 215/PMK.03/2018): PPh 25 monthly = (PPh terutang 2025 − all kredit pajak 2025) ÷ 12, paid by the 15th of each month from January 2026 via MAP 411125 KJS 100. Corporates: Same formula; MAP 411126 KJS 100. New businesses / first year of progressive regime: PPh 25 = 0 for the months before the first full assessment year; first installment is the month after registration / breach of UMKM threshold.  _(PMK 215/PMK.03/2018)_

### 10.2 UMKM regime planning

- **UMKM regime planning rules** — If the taxpayer is using UMKM 0.5% in 2025: Check the UMKM window remaining (3y for PT / 4y for CV / 7y for Orang Pribadi from start year under PP 55/2022). If 2025 is the final year, 2026 reverts to: Individual — Progressive PPh OP with bookkeeping (pembukuan), switch from norma penghitungan if applicable; Corporate — Standard PPh Badan 22% (or Article 31E facility for SME). Even if window is not closing, monitor cumulative gross turnover. If 2026 turnover is expected to exceed IDR 4.8B, plan the regime switch and PKP-VAT registration.  _(PP 55/2022)_

### 10.3 VAT planning

- **VAT PKP registration planning** — PKP registration threshold: cumulative gross turnover IDR 4.8 billion in a year (PMK 197/PMK.03/2013). If approaching threshold during 2026, register as PKP before crossing — issue Faktur Pajak from registration date.  _(PMK 197/PMK.03/2013)_

### 10.4 Coretax compliance updates

PMK 81/2024 introduced Coretax DJP as the single integrated tax system. Reviewers should monitor DJP circulars (Surat Edaran Direktur Jenderal Pajak) through 2026 for transitional easements, form revisions, and new MAP / KJS combinations. TBC — confirm the active list at filing time.

### 10.5 Transfer pricing planning

- **Transfer pricing planning rules** — For corporates with related-party transactions (under PMK 213/PMK.03/2016 thresholds): Local file & master file due by SPT 1771 filing deadline (30 April 2026). CbCR (Country-by-Country Reporting) for groups with consolidated revenue ≥ IDR 11 trillion — 12 months after fiscal year-end. Flag if 2025 related-party gross transactions exceeded IDR 50 billion or any single counterparty exceeded IDR 5 billion.  _(PMK 213/PMK.03/2016)_

## Section 11 — Conservative defaults

**Conservative defaults table**

| Situation | Conservative default |
| --- | --- |
| Cross-skill reconciliation differs by > IDR 1,000 | Flag as "Needs Input"; do not silently round |
| MAP / KJS code uncertain for a payment | Use "TBC — verify current MAP code in Coretax" and DO NOT generate billing |
| UMKM window status unclear | Treat as final year; default 2026 to progressive regime |
| KLU code missing | Flag; use 70209 (General consulting) as placeholder for individuals; 64200 (Holding) for badan — note it must be corrected before filing |
| NITKU missing post-Coretax | Flag; cannot submit without it |
| Bukti Potong missing for a claimed credit | Exclude the credit; flag for taxpayer to obtain the Bukti Potong |
| Audit requirement unclear (Badan revenue near threshold) | Recommend audit (UU PT thresholds: revenue ≥ IDR 50B or assets ≥ IDR 50B) |
| December PPh 21 true-up not yet booked | Treat year as incomplete; cannot finalise SPT until December payroll closed |
| Foreign income with no certificate of residency | Disallow PPh 24 credit; flag for documentation |
| Related-party transactions undocumented | Flag transfer pricing risk; do not silently assume arm's-length |
| Payment due but no NTPN | Mark SPT credit as "pending payment"; advise taxpayer to settle before filing |

## Section 11 — Conservative defaults

- **Tolerance rule (repeated for emphasis)** — IDR 1,000 reconciliation tolerance. Any larger discrepancy is escalated, not absorbed.

## Section 12 — Refusals

- **R-ID-ASM-1** — Upstream skill did not run. Name the missing skill. Continue with available data; flag the gap; do not fabricate the missing computation.  _(R-ID-ASM-1)_
- **R-ID-ASM-2** — Upstream self-check failed. Note the specific check; continue but flag.  _(R-ID-ASM-2)_
- **R-ID-ASM-3** — Cross-skill reconciliation > IDR 1,000. Raise as "Needs Input"; do not silently round.  _(R-ID-ASM-3)_
- **R-ID-ASM-4** — Out of scope: VAT margin scheme, oil & gas / mining special regimes, branch profit tax (BPT) under PPh 26(4) for permanent establishments, controlled foreign company (CFC) rules under PMK 93/2019, tax holidays under PP 78/2019, special economic zone (KEK) facilities. Flag for human specialist; do not attempt.  _(R-ID-ASM-4)_
- **R-ID-ASM-5** — Out of scope: non-resident individuals, mixed-residency years, expatriate package taxation under PMK 18/2021. Refer to a specialist; this skill assumes full-year Indonesian tax residency.  _(R-ID-ASM-5)_
- **R-ID-ASM-6** — Intake incomplete. Name the missing intake field (NPWP, NITKU, KLU, marital status, dependents). Cannot finalise the SPT until provided.  _(R-ID-ASM-6)_
- **R-ID-ASM-7** — Asked to submit to Coretax. This skill produces a working paper. Submission is the taxpayer's (or their authorised filer's) action, after Konsultan Pajak review and sign-off. Decline politely; provide the filing instructions instead.  _(R-ID-ASM-7)_

## Section 13 — Self-checks

- **Check ID-ASM-1** — All upstream skills required for the chosen form have produced output, or the gap is flagged.  _(Check ID-ASM-1)_
- **Check ID-ASM-2** — Revenue reconciles between id-bookkeeping, indonesia-vat, and the chosen PPh skill within IDR 1,000.  _(Check ID-ASM-2)_
- **Check ID-ASM-3** — PPh credits sum correctly across PPh 21/22/23/24/25/26, with each credit backed by a Bukti Potong + NTPN.  _(Check ID-ASM-3)_
- **Check ID-ASM-4** — UMKM monthly SSPs (if applicable) sum to 0.5% of cumulative UMKM-eligible turnover; each month has an NTPN.  _(Check ID-ASM-4)_
- **Check ID-ASM-5** — PPh 21 annual employer return (1721 A1) ties to sum of monthly TER plus December true-up.  _(Check ID-ASM-5)_
- **Check ID-ASM-6** — For corporates: fiscal reconciliation (Lampiran I-1771) ties commercial profit to fiscal profit; loss carryforward used does not exceed 5-year limit (UU PPh Pasal 6).  _(Check ID-ASM-6)_
- **Check ID-ASM-7** — UMKM window status is verified and 2026 regime is named.  _(Check ID-ASM-7)_
- **Check ID-ASM-8** — All MAP / KJS codes used in the kode billing instructions are flagged "TBC — verify in Coretax" if not directly confirmed against current PMK 81/2024 annexes.  _(Check ID-ASM-8)_
- **Check ID-ASM-9** — Filing deadline (31 March or 30 April 2026) is explicitly stated in the action list with the correct date.  _(Check ID-ASM-9)_
- **Check ID-ASM-10** — Record retention period (10 years per UU KUP Pasal 28) is stated.  _(Check ID-ASM-10)_
- **Check ID-ASM-11** — Reviewer brief contains legislation citations for every position taken (UU KUP, UU PPh, UU HPP, UU PPN, relevant PP / PMK).  _(Check ID-ASM-11)_
- **Check ID-ASM-12** — BPE (Bukti Penerimaan Elektronik) retention is included in the action list.  _(Check ID-ASM-12)_
- **Check ID-ASM-13** — Konsultan Pajak sign-off requirement is stated in the executive summary and action list.  _(Check ID-ASM-13)_

## Section 14 — Output files

The final output is three files:

1. `[taxpayer_slug]_2025_id_master.xlsx` — Master workbook. Sheets: Cover, Identitas, 1770 Induk (or 1771 Induk), Lampiran I-V (or I-VI for corporate), UMKM Final Tracker, Bukti Potong Register, NTPN Register, Cross-Check Summary, Kode Billing Schedule. Use live formulas where possible; verify no `#REF!` errors.

2. `reviewer_brief.md` — Markdown file with all Section 8 contents.

3. `taxpayer_action_list.md` — Markdown file with all Section 9 contents.

All three files are placed in `/mnt/user-data/outputs/` and presented to the user at the end.

If execution runs out of context mid-build, complete the computation work first and produce whichever formatted outputs are finished, then state clearly which deliverables are partial.

## Section 15 — Known gaps

1. PDF form filling is not automated; the reviewer or taxpayer enters values into Coretax using the working paper.
2. Coretax XML generation is not produced by this skill; integrations with ERP / third-party software handle that.
3. Audit report attachment is the taxpayer's responsibility; this skill only flags when audit is required.
4. Transfer pricing local file / master file content is referenced but not assembled here (separate skill needed).
5. PPh 26 (non-resident withholding) computations are not part of UMKM and are referenced via id-withholding only.
6. Tax holidays, KEK, and special facility regimes (PP 78/2019, PMK 130/2020, etc.) are out of scope.
7. CbCR XML is not assembled here.
8. Coretax MAP / KJS combinations are subject to change in 2025–2026 transition; every code in this skill should be verified against the live Coretax dropdown.

### Change log

v1.0 (May 2026): Initial release. Modelled on mt-return-assembly and us-ca-return-assembly, adapted for Indonesian SPT 1770 / 1771, Coretax DJP filing, and PMK 81/2024 transition. Coordinates seven upstream Indonesia skills.

## Section 16 — Sources

**Sources table**

| Source | Reference |
| --- | --- |
| UU KUP No. 6/1983 (as amended through UU HPP) | General tax administration: deadlines, penalties, retention |
| UU PPh No. 36/2008 (as amended) | Income tax framework |
| UU HPP No. 7/2021 | Harmonisasi Peraturan Perpajakan — updated brackets, Pasal 17, Article 31E facility |
| UU PPN No. 42/2009 (as amended through UU HPP) | VAT framework, PKP threshold |
| PP 55/2022 | UMKM PPh Final 0.5%; window durations by entity type |
| PP 58/2023 | TER PPh 21 (employment withholding scheme effective 1 Jan 2024) |
| PMK 81/2024 | Coretax DJP implementation (effective 1 January 2025) |
| PMK 168/2023 | TER implementation rules |
| PMK 215/PMK.03/2018 | PPh 25 monthly installment computation |
| PMK 213/PMK.03/2016 | Transfer pricing documentation thresholds |
| PMK 197/PMK.03/2013 | VAT PKP threshold IDR 4.8 billion |
| PMK 164/2023 | UMKM Final monthly payment due dates |
| DJP — Direktorat Jenderal Pajak | https://www.pajak.go.id |
| Coretax DJP | https://coretaxdjp.pajak.go.id |
| Skill version | 1.0 |

## Footer disclaimer

OpenAccountants — open-source accounting skills for AI. This is not tax advice. All outputs must be reviewed and signed off by a qualified Indonesian tax consultant (Konsultan Pajak bersertifikat) before filing via Coretax DJP.

## Talk to a verified accountant

This skill is a tool, not an engagement. Every taxpayer's situation is different, and the rules in the skill may not match your specific facts.

To speak with one of the licensed accountants who verifies skills for your jurisdiction — no liability on either side until you and the accountant sign a formal engagement letter — book a free 30-minute call:

→ [Book a call](https://calendly.com/openaccountants-info/30min)

We'll route you to the named verifier covering your country or state. You can also see the full list of verified accountants at [openaccountants.com/network](https://openaccountants.com/network).

### 2.1 Individual return (SPT 1770) — inputs

0. **Consume id-bookkeeping output** — General ledger trial balance; income/expense detail feeding Lampiran I
0. **Consume id-income-tax output** — Progressive PPh OP computation feeds Form 1770 Induk Part B & C
0. **Consume id-pph-final-umkm output** — UMKM Final 0.5% computation feeds Lampiran III-A
0. **Consume id-payroll-pph21 output** — Employment income and withheld PPh21 feed Form 1770 Induk Part A; Lampiran I Bagian B
0. **Consume indonesia-vat output** — VAT position cross-checked against revenue figures
0. **Consume id-withholding output** — Bukti Potong PPh 22/23/4(2) as recipient and as withholder feed Lampiran I & III

### 2.2 Corporate return (SPT 1771) — inputs

0. **Consume id-bookkeeping output** — Full financial statements feed Lampiran V and Lampiran I
0. **Consume id-corporate-tax output** — Fiscal profit and PPh Badan computation feed Form 1771 Induk Part B & C
0. **Consume id-pph-final-umkm output** — UMKM Final regime data feeds Lampiran IV
0. **Consume id-payroll-pph21 output** — Employee payroll cost classification feeds Lampiran II
0. **Consume indonesia-vat output** — VAT input/output reconciled; PPN Masukan cost treatment cross-checked
0. **Consume id-withholding output** — Withholding credits and SPT Masa obligations feed Lampiran III

## Section 3 — Tax computation reconciliation

0. **Run all cross-checks in sequence** — Execute Cross-checks 1 through 7 across upstream outputs, flagging failures in the reviewer brief without pausing

## Section 14 — Output files

0. **Produce final output files** — Generate master workbook, reviewer_brief.md, and taxpayer_action_list.md and place them in /mnt/user-data/outputs/
