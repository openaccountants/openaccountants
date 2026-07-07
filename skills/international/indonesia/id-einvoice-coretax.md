---
name: id-einvoice-coretax
description: Use this skill whenever asked about filing, invoicing, or submitting any Indonesian tax obligation through the Coretax DJP system that went live 1 January 2025. Trigger on phrases like "Coretax DJP", "Coretax pajak", "Coretax login", "e-Faktur Indonesia", "e-Bupot Unifikasi", "NSFP", "Nomor Seri Faktur Pajak", "SPT Masa Unifikasi", "Indonesia tax filing system", "DJP Online vs Coretax", "Coretax Form", "Coretax Mobile", "NIK as NPWP", "16-digit NPWP", "pajak.go.id new system", "Coretax onboarding", or any operational query about how to file, issue invoices, or pay tax to the Indonesian DJP from 2025 onward. This skill covers the Coretax platform mechanics, account activation, NIK/NPWP integration, e-Faktur issuance and NSFP management within Coretax, e-Bupot Unifikasi withholding slip workflow, SPT filing channels, and the DJP Online to Coretax cutover. It does NOT compute the underlying tax — VAT (PPN) sits in indonesia-vat, withholding PPh 21 sits in id-payroll-pph21, and corporate / individual income tax sits in their respective skills. ALWAYS read this skill when filing or invoicing through Coretax DJP.
jurisdiction: ID
tax_year: 2025
reviewed_by: RILIA PUTRI
review_status: accountant-reviewed
tier: 1
last_updated: 2026-07-06
---

# id-einvoice-coretax

## Indonesia — Coretax DJP, e-Faktur, e-Bupot Unifikasi Skill v1.0

This skill is the **platform manual** for the Indonesian tax administration system. It explains how the buttons work and where the filings live. The substantive tax content (rates, base, deductions) is in the per-tax skills (`indonesia-vat`, `id-payroll-pph21`, etc.).

## Verified rates & thresholds (accountant-reviewed)

> Reviewed against the cited tax authorities by **RILIA PUTRI** on 2026-06-03.
> Items flagged for further clarification are tracked separately and excluded here.
> This block is generated from verified `skill_facts` — edit the facts, not the prose.

### Coretax and e-Invoicing

- **Go-live date** — Coretax / Sistem Inti Administrasi Perpajakan (SIAP) became effective starting 1 January 2025 under prevailing Indonesian tax administration regulations.  _(PMK 81/2024; PER-1/PJ/2025.)_
- **URL** — Coretax services are generally accessed through the official DJP/Coretax electronic portal.  _(DJP Portal / Coretax Portal.)_
- **Replaces** — Coretax integrates and migrates legacy DJP applications including DJP Online, e-Faktur, e-Bupot, e-Registration, tax payment, and tax reporting into a unified tax administration platform.  _(PMK 81/2024; PER-1/PJ/2025.)_
- **Mobile app** — Certain Coretax/SIAP services may also be accessed through DJP electronic platforms and digital channels under prevailing Indonesian tax administration procedures. Current official guidance emphasizes access through DJP/Coretax electronic systems, although no specific PMK/PER/SE currently appears to formally standardize a dedicated “Coretax DJP” mobile application name.  _(PMK 81/2024; PER-1/PJ/2025; DJP Coretax implementation guidance and taxpayer handbook..)_
- **Coretax Form (offline)** — PER-3/PJ/2026 regulates updated procedures for submission and processing of tax returns under Coretax implementation.  _(PER-3/PJ/2026.)_
- **Indonesian individual** — Resident Indonesian individuals generally use NIK as NPWP under prevailing Indonesian tax administration regulations.  _(PMK 112/2022; PMK 81/2024.)_
- **Foreign individual** — Foreign individuals/non-resident individuals generally use 16-digit NPWP format under prevailing Indonesian tax administration regulations.  _(PMK 112/2022; PMK 81/2024.)_
- **Indonesian entity** — Corporate taxpayers generally use 16-digit NPWP format under Coretax implementation and prevailing tax administration regulations.  _(PMK 112/2022; PMK 81/2024; PER-1/PJ/2025.)_
- **NSFP request** — NSFP requests are processed electronically through DJP/Coretax systems using taxpayer electronic certificates and prevailing VAT administration procedures.  _(PMK 81/2024; PER-1/PJ/2025.)_
- **NSFP return deadline** — Return of unused NSFPs remains subject to prevailing DJP VAT administration and technical procedures under electronic tax invoice regulations.  _(PMK 81/2024; PER-1/PJ/2025; prevailing VAT/e-Faktur regulations.)_
- **Faktur Pengganti** — Replacement tax invoices (Faktur Pengganti) must follow prevailing DJP VAT invoice correction and replacement procedures under Coretax/e-Faktur administration rules.  _(PMK 81/2024; PER-1/PJ/2025; PER-1/PJ/2026.)_
- **Faktur Dibatalkan** — Cancelled tax invoices remain administratively traceable and reported in the relevant VAT return period according to prevailing Coretax VAT administration procedures.  _(PMK 81/2024; PER-1/PJ/2025.)_
- **Covers** — e-Bupot Unifikasi generally covers withholding and/or collection obligations including PPh 23, PPh 26, Final PPh Art. 4(2), and other unified withholding-tax obligations under Coretax administration procedures.  _(PER-11/PJ/2025; PMK 81/2024.)_
- **Monthly SPT Masa Unifikasi** — Monthly SPT Masa Unifikasi is generally filed electronically through Coretax/SIAP by the 20th of the following month under prevailing Indonesian tax administration regulations. Unified withholding reporting, electronic filing procedures, and tax-object-code administration follow prevailing Coretax and SPT Unifikasi procedures.  _(UU KUP Art. 3 as amended by UU HPP; PMK 81/2024; PER-1/PJ/2025; PER-1/PJ/2026; PER-11/PJ/2025; KEP-143/PJ/2022.)_
- **Tax period Dec 2024 or earlier** — Tax periods prior to Coretax implementation generally continue to follow legacy DJP Online and transitional filing procedures under prevailing DJP transition/cutover guidance.  _(PMK 81/2024; DJP transition/cutover guidance; PER-1/PJ/2025.)_
- **Tax period Jan 2025 onward** — Tax periods starting January 2025 generally follow Coretax/SIAP administration and electronic filing procedures under prevailing Indonesian tax administration regulations.  _(PMK 81/2024; PER-1/PJ/2025; PER-1/PJ/2026.)_

## Section 1 — Quick reference

**Quick reference**

| Field | Value |
| --- | --- |
| Country | Indonesia (Republik Indonesia) |
| Platform | Coretax DJP (Sistem Inti Administrasi Perpajakan / SIAP) |
| Operator | Direktorat Jenderal Pajak (DJP), Kementerian Keuangan |
| Go-live | 1 January 2025 |
| Replaces | DJP Online e-Filing (2025+), desktop e-Faktur, separate e-Bupot apps, e-Registration, several legacy portals |
| Primary URL | coretaxdjp.pajak.go.id |
| Legacy URL still live | pajak.go.id / djponline.pajak.go.id (residual tax-year 2024 work) |
| Mobile app | "Coretax DJP" — Play Store and App Store (individual taxpayers) |
| Coretax Form | Offline preparation form for SPT 1770 — broadly available February 2026 |
| Currency | IDR (Indonesian Rupiah) |
| NPWP format | 16-digit (NIK-as-NPWP) for Indonesians since 1 July 2024; 15-digit padded to 16 for entities / foreigners |
| Tax invoice | Faktur Pajak via Coretax e-Faktur from 1 Jan 2025 |
| NSFP | Nomor Seri Faktur Pajak — invoice serial, requested in Coretax |
| Unified withholding | SPT Masa PPh Unifikasi (PPh 23/26/4(2)/15) |
| Filing channels | Coretax web, Coretax Mobile, Coretax Form upload, PJAP host-to-host |
| Contributor | Open Accountants Community |
| Validated by | Pending — Konsultan Pajak sign-off required |
| Skill version | 1.0 |

### Conservative defaults

**Conservative defaults**

| Ambiguity | Default |
| --- | --- |
| Coretax is unreachable at deadline | Document the attempt (screenshot, ticket number, timestamp), file as soon as access is restored, attach proof of attempted filing to the workpaper |
| Doubt over whether to file on Coretax vs DJP Online | Tax period **on or after January 2025 → Coretax**. Tax period **December 2024 or earlier → DJP Online** unless DJP has published a specific migration instruction for that form |
| NSFP request rejected or pending | Do not back-date a Faktur Pajak; issue once NSFP is granted; record the delay |
| 16-digit vs 15-digit NPWP unclear | Indonesian individual → use NIK as 16-digit NPWP; foreign national → use existing 15-digit NPWP padded with leading "0" to 16 digits inside Coretax |
| Withholding category unclear between PPh 23 / 4(2) | Hold the filing; do not guess across PPh categories — the e-Bupot Unifikasi form requires the correct article designation |
| Coretax UI behaviour appears to differ from this skill | Trust the live UI and DJP help text. Mark "TBC" in the workpaper and update this skill |

## Section 2 — Required inputs and refusal catalogue

### Required inputs

**Minimum viable** — Coretax account credentials (or DJP-issued activation letter with PIN); NPWP (16-digit for Indonesian individuals, 15-digit for foreigners / legacy); tax period and year; the underlying tax computation from a sister skill (`indonesia-vat`, `id-payroll-pph21`, etc.).

**Recommended** — Faktur Pajak or withholding ledger in CSV/Excel for bulk import; counterparty NPWPs pre-validated against DJP; confirmed NSFP balance.

**Ideal** — PJAP host-to-host connection for high-volume taxpayers; valid digital certificate (sertifikat elektronik) renewed within the last 24 months.

**Refusal if minimum missing — SOFT WARN.** Without an activated Coretax profile, no filing can be lodged. Without a sister-skill tax computation, this platform skill cannot produce a return on its own.

### Refusal catalogue

- **R-CT-1 — Tax content out of scope** — This skill is the Coretax platform manual. PPN classification, PPh 21 bands, corporate income tax computations, and planning are handled by `indonesia-vat`, `id-payroll-pph21`, or the relevant income-tax skill.  _(R-CT-1)_
- **R-CT-2 — Foreign-nationals' NPWP** — WNA onboarding differs from the NIK-as-NPWP route. Foreigners currently use a 15-digit NPWP padded to 16 in Coretax — confirm the current DJP flow before activation. TBC — a dedicated foreign-taxpayer ID has been signalled.  _(R-CT-2)_
- **R-CT-3 — Pre-2025 amendments via Coretax** — Pembetulan for a tax period **on or before December 2024** generally routes through DJP Online, not Coretax. Confirm the channel before submitting unless DJP has published a specific migration instruction.  _(R-CT-3)_
- **R-CT-4 — Host-to-host / PJAP integration** — Building or debugging a PJAP integration is engineering scope. Out of skill — escalate.  _(R-CT-4)_
- **R-CT-5 — System outage on the deadline** — Do NOT self-declare a Force Majeure waiver. DJP issues a `Pengumuman` when it grants relief. Reviewer must check pajak.go.id announcements before relying on any deemed extension.  _(R-CT-5)_
- **R-CT-6 — Confidential digital certificate operations** — Generating or renewing a taxpayer's `sertifikat digital` requires the taxpayer's own credentials — the skill walks through steps; it does not act on credentials.  _(R-CT-6)_

## Section 3 — Coretax DJP overview

Coretax DJP is the Indonesian tax administration's unified back-office and taxpayer-facing platform, built under the **Pembaruan Sistem Inti Administrasi Perpajakan (PSIAP)** project. It went live **1 January 2025** and consolidates services that previously lived across multiple legacy DJP portals.

### 3.1 What Coretax replaces

**What Coretax replaces**

| Legacy service | Coretax replacement |
| --- | --- |
| DJP Online e-Filing (web SPT submission) | Coretax web portal — SPT module |
| Desktop e-Faktur (Java client) | Coretax e-Faktur (browser-based) |
| e-Bupot 23/26 web app | Coretax e-Bupot Unifikasi |
| e-Bupot 4(2) and PPh 15 separate apps | Same — folded into e-Bupot Unifikasi |
| e-Bupot 21/26 (employment) | Coretax e-Bupot 21/26 (separate monthly form, on Coretax) |
| e-Registration | Coretax registration module |
| e-Objection / e-Appeal | Coretax dispute module |
| e-Billing (kode billing) | Coretax payment module — still issues 15-digit ID Billing |
| e-SKD (residence certificates) | Coretax DTP / e-SKD module |
| KSWP (taxpayer status) | Coretax taxpayer-status service |

### 3.2 What Coretax does NOT replace

Tax payment settlement still happens at a bank, BPD, Pos Indonesia, marketplace, or fintech accepting Kode Billing. Customs (Bea Cukai) PIB / PEB stays in INSW / CEISA. BPJS is a separate authority. Pre-2025 audit case files remain on legacy systems.

### 3.3 Coretax modules at a glance

**Coretax modules at a glance**

| Module | Purpose |
| --- | --- |
| Profil Wajib Pajak | Taxpayer profile, NPWP/NIK, KLU, address, PIC |
| Layanan | Service requests (PKP confirmation, NSFP, certificate, residence) |
| e-Faktur | Faktur Pajak issuance, NSFP balance, replacement & cancellation |
| e-Bupot Unifikasi | PPh 23/26/4(2)/15 slips + monthly SPT Masa Unifikasi |
| e-Bupot 21/26 | Employment withholding monthly form |
| SPT Tahunan | 1770 / 1770S / 1770SS (individuals); 1771 (corporates) |
| Pembayaran | Kode Billing, payment history |
| Restitusi | Refund applications |
| Sengketa | Objection (Keberatan) and appeal |

## Section 4 — Account activation and NIK-as-NPWP

### 4.1 NIK-as-NPWP — 16-digit format

- **NIK-as-NPWP unification** — Under **PMK-112/PMK.03/2022** (later operationalised through PER-04/PJ/2020 and amendments) the DJP unified the **NIK** (Nomor Induk Kependudukan — 16-digit national ID number) with the **NPWP** for Indonesian individual taxpayers. As of **1 July 2024** the 16-digit identifier is the only valid NPWP format for Indonesian citizens in all DJP services — Coretax enforces this.  _(PMK-112/PMK.03/2022; PER-04/PJ/2020 and amendments)_

**NPWP format inside Coretax**

| Taxpayer category | NPWP format inside Coretax |
| --- | --- |
| Indonesian individual (WNI) | 16-digit NIK = NPWP |
| Foreign individual (WNA) | 15-digit legacy NPWP, padded with leading "0" to 16 digits at display time (TBC — DJP has signalled a dedicated 16-digit foreign-taxpayer identifier; confirm current state) |
| Indonesian entity (Badan) | 15-digit NPWP padded to 16 digits with leading "0" inside Coretax |
| Government instrumentality | 15-digit padded to 16 |
| Branch (Cabang) | Parent 15-digit + 3-digit branch suffix → Coretax displays the consolidated identifier |

### 4.2 Activation flow — first login

Order matters: Coretax will not allow NSFP requests, Faktur Pajak issuance, or return signing without an activated profile and valid digital certificate.

1. Visit coretaxdjp.pajak.go.id (confirm URL against the current DJP announcement).
2. **Username** — NIK / 16-digit NPWP for individuals; 15-digit padded to 16 for entities.
3. **Reset password** via "Lupa Kata Sandi" using the email/phone on file at DJP.
4. Verify email and phone — required before any service request.
5. Set **Passphrase Sertifikat Digital** — required every time a return is signed.
6. Confirm **KLU** (business activity code) and address — mismatches block NSFP requests.
7. Add **PIC** (Person in Charge) — at least one required for entities; each PIC has own login and signing role.
8. **For PKPs:** request or migrate the digital certificate (`sertifikat elektronik`) via the Layanan menu.

### 4.3 Sub-user / impersonation

Entities grant role-based access — typical roles are *Penanggung Jawab* (signing officer), *Karyawan* (operator), *Konsultan Pajak* (external agent). External tax agents act under their own NPWP via the **Wakil Wajib Pajak** flow.

## Section 5 — e-Faktur inside Coretax

The desktop e-Faktur Java client has been retired. All Faktur Pajak issuance from **1 January 2025** is browser-based inside Coretax. The legal substance of the Faktur Pajak (deadlines, 11% rate, exempt categories) is unchanged and lives in `indonesia-vat`. This section covers platform mechanics only.

### 5.1 NSFP — Nomor Seri Faktur Pajak

Every Faktur Pajak must carry a serial number issued by DJP. Coretax centralises NSFP request and consumption.

**Coretax action steps**

| Step | Coretax action |
| --- | --- |
| 1 | Navigate to **e-Faktur → Permintaan NSFP** |
| 2 | Enter requested quantity. Coretax benchmarks against historical issuance and may auto-approve or queue |
| 3 | Sign the request with the digital certificate passphrase |
| 4 | DJP responds with a serial range (e.g., `0100002500000001`–`0100002500001000`); positions 3-4 carry the year |
| 5 | Allocated NSFPs sit in the taxpayer's balance; each issued Faktur consumes one |
| 6 | Unused NSFPs must be returned via **Pengembalian NSFP** by 31 March of the following year |

**Practical timing.** Peak windows queue NSFP requests for hours or days — do not wait until the Faktur is due.

### 5.2 Issuing a Faktur Pajak

1. **e-Faktur → Buat Faktur Keluaran**.
2. Pick the **Kode Transaksi** — `01` standard B2B, `04` special DPP, `07` zero-rated export of services, `08` exempt, etc.
3. Enter the **counterparty NPWP** — Coretax validates against the DJP master file in real time.
4. Enter **DPP** and **PPN**. Coretax computes PPN; override requires a flagged reason code.
5. Save — Coretax assigns the next NSFP from the pool.
6. **Sign** with the digital certificate passphrase. Coretax issues the QR-coded PDF.

### 5.3 QR code, replacement, cancellation

Each finalised Faktur Pajak carries a QR code linking to pajak.go.id verification. Faktur that fail QR verification are not creditable.

**Scenario / Coretax action**

| Scenario | Coretax action |
| --- | --- |
| Faktur Pengganti (replacement) | New Faktur with same period referencing original; code's first digit changes to `1` (`011` instead of `010`) |
| Faktur Dibatalkan (cancellation) | Use **Pembatalan Faktur**; cancelled Faktur still reported in the SPT Masa PPN of the issue period |
| Nota Retur (sales return) | Issued by buyer; recorded by seller as a credit |

### 5.4 Bulk upload

Coretax accepts CSV/XML bulk upload (template in the e-Faktur module). Server-side validation produces a status report within minutes — the standard path for high-volume PKPs.

## Section 6 — e-Bupot Unifikasi

### 6.1 What "Unifikasi" means

- **Unifikasi definition** — Before Coretax, a withholder filed multiple separate monthly returns: - SPT Masa PPh Pasal 23/26 via e-Bupot 23/26 - SPT Masa PPh Pasal 4(2) via e-Bupot 4(2) - SPT Masa PPh Pasal 15 via e-Bupot 15 **PER-24/PJ/2021** (introduced the original e-Bupot Unifikasi) and the broader DJP regulation set referenced under **PER-2/PJ/2024** consolidated these into **one** monthly form: **SPT Masa PPh Unifikasi**. Coretax is the single venue for the unified slip workflow. > **Note.** SPT Masa PPh Pasal 21/26 (employment withholding on wages) is **not** included in the Unifikasi. PPh 21 keeps its own monthly form, but that form is also filed inside Coretax. See `id-payroll-pph21`.  _(PER-24/PJ/2021; PER-2/PJ/2024)_

### 6.2 Articles covered by the Unifikasi

**Articles covered by the Unifikasi**

| Article | Typical withholding base |
| --- | --- |
| PPh 23 | Domestic withholding on services, rent (other than land/building), royalty, interest (non-bank), dividend to non-corporate residents |
| PPh 26 | Withholding on payments to non-residents (subject to tax treaty rates) |
| PPh 4(2) — Final | Land/building rent, construction services, deposit interest, lottery prizes, certain UMKM final tax |
| PPh 15 | Specific industries — shipping, aviation, oil & gas drilling services, etc. |

### 6.3 Issuance flow inside Coretax

1. **e-Bupot Unifikasi → Buat Bukti Potong**.
2. Pick the **article** — PPh 23, 26, 4(2), or 15. Form fields change accordingly.
3. Enter **payee NPWP** (or passport / TIN for non-residents under PPh 26).
4. Enter gross amount and tax rate. Coretax computes the withheld amount.
5. For PPh 26 — attach the **DGT Form (SKD — Surat Keterangan Domisili)** for a treaty rate; otherwise default 20%.
6. Sign with the digital certificate passphrase.
7. The Bukti Potong Unifikasi is issued — payee downloads it from their own Coretax profile.

### 6.4 Monthly SPT Masa PPh Unifikasi

- **Monthly SPT Masa PPh Unifikasi process and deadlines** — At month-end Coretax aggregates all Bukti Potong issued per article. The user reviews, adjusts for voids/amendments, generates a **Kode Billing**, pays, then returns to attach the **NTPN** (Nomor Transaksi Penerimaan Negara) and lodges the SPT. Statutory deadlines (unchanged by Coretax): SPT Masa Unifikasi due by the **20th** of the following month; payment by the **10th** of the following month (UU KUP). PPh 21 deadlines live in `id-payroll-pph21`.  _(UU KUP)_

## Section 7 — SPT filing channels

Coretax exposes four channels for SPT submission. Pick the channel that matches the form and the taxpayer's volume.

**SPT filing channels**

| Channel | Used for | Notes |
| --- | --- | --- |
| **Coretax web portal** | All forms — SPT Masa (PPN, Unifikasi, PPh 21/26), SPT Tahunan (1770, 1770S, 1770SS, 1771) | Default channel; supports inline editing and validation |
| **Coretax Form** | SPT 1770 (individual self-employed) initially; later expansion | Downloadable offline form; user fills it, then uploads the signed file back to Coretax. Phased rollout — broad availability **February 2026** for SPT 1770 |
| **Coretax Mobile** | SPT Tahunan 1770 SS and 1770 S for simple individual returns; profile updates; payment | iOS and Android. Convenient for employees with one source of income |
| **Host-to-host (PJAP)** | Bulk Faktur Pajak issuance, bulk Bukti Potong, automated SPT lodgement | Requires PJAP onboarding — engineering project; out of scope for this skill |

### 7.1 Deadlines and reminders

**Deadlines and reminders**

| Obligation | Deadline | Coretax reminder |
| --- | --- | --- |
| SPT Masa PPN payment | End of month following the tax period | Coretax dashboard banner; email |
| SPT Masa PPN filing | End of month following the tax period | Same |
| SPT Masa PPh Unifikasi payment | 10th of the following month | Coretax dashboard + e-mail nudge |
| SPT Masa PPh Unifikasi filing | 20th of the following month | Same |
| SPT Masa PPh 21/26 payment | 10th of the following month | Same |
| SPT Masa PPh 21/26 filing | 20th of the following month | Same |
| SPT Tahunan 1770 individual | 31 March of the following year | Coretax sends e-mail reminders from January |
| SPT Tahunan 1771 corporate | 30 April (4 months after fiscal year-end) | Same |
| NSFP year-end return | 31 March of the following year for unused serials | Coretax e-Faktur reminder |

### 7.2 Bukti Penerimaan Elektronik (BPE)

Every successful filing generates a **Bukti Penerimaan Elektronik** — the electronic receipt. Save the BPE PDF to the workpaper. It carries a unique receipt number; this is the primary evidence of filing if DJP later challenges timeliness.

## Section 8 — Common implementation issues (Jan–Mar 2025)

The Coretax cutover was bumpy. Reviewers preparing a workpaper for an early-2025 period should expect to document at least one of these.

1. **Login / password reset failures** — "Lupa Kata Sandi" failed where the e-mail or phone on the DJP master file was stale. Fix: in-person visit to the local KPP to update contact data.
2. **NSFP request delays** — peak windows queued requests for days; PKPs were unable to issue Faktur Pajak in real time. Rely on a formal `Pengumuman` only.
3. **Digital certificate migration glitches** — legacy desktop e-Faktur certificates did not always migrate cleanly. Remedy: request a new certificate via Coretax Layanan.
4. **PJAP integration latency** — host-to-host had teething problems; documented workaround was bulk upload via the Coretax UI.
5. **NPWP validation false-negatives** — Coretax intermittently rejected valid counterparty NPWPs (especially 15-digit padded). Workaround: re-enter as 16-digit with leading "0".
6. **SPT Masa PPN slow render** — long render time for taxpayers with high invoice counts; use bulk upload.

For each, the Section 10 default applies: document the attempt, screenshot the error, retain the ticket number, file as soon as access is restored.

## Section 9 — Cutover between DJP Online and Coretax

**Cutover routing table**

| Filing | Tax period | Channel |
| --- | --- | --- |
| SPT Masa PPN (original) | December 2024 or earlier | **DJP Online + desktop e-Faktur** |
| SPT Masa PPN (original) | January 2025 onward | **Coretax** |
| SPT Masa PPN (pembetulan / amendment) | December 2024 or earlier | **DJP Online** (unless DJP announces a Coretax migration of legacy amendments — TBC) |
| SPT Masa PPN (pembetulan) | January 2025 onward | **Coretax** |
| SPT Masa PPh 23/26 (original) | December 2024 or earlier | **e-Bupot 23/26 (legacy)** |
| SPT Masa PPh Unifikasi (original) | January 2025 onward | **Coretax e-Bupot Unifikasi** |
| SPT Masa PPh 21/26 (original) | December 2024 or earlier | **e-Bupot 21/26 (legacy)** |
| SPT Masa PPh 21/26 (original) | January 2025 onward | **Coretax e-Bupot 21/26** |
| SPT Tahunan 1770 / 1771 | Tax year 2024 (filed Q1 2025) | **DJP Online** — the 2024 annual returns filed in early 2025 mostly remained on the legacy portal (TBC — confirm against current DJP announcement) |
| SPT Tahunan 1770 / 1771 | Tax year 2025 (filed 2026) | **Coretax** |
| Kode Billing for any tax payment | From 1 Jan 2025 | **Coretax** (legacy DJP Online billing module sunsetted) |
| Faktur Pajak | From 1 Jan 2025 | **Coretax e-Faktur only** — desktop e-Faktur Java client retired |

If the routing is unclear, default to Coretax for any tax period of January 2025 onward and to the legacy environment for December 2024 and earlier. Confirm against the most recent DJP `Pengumuman` before lodgement.

## Section 10 — Conservative defaults

When Coretax behaves unexpectedly, prefer **document-and-retry** over **guess-and-file**.

1. **System down** — screenshot the error (URL + timestamp), capture the helpdesk ticket, file as soon as access is restored. Save the BPE.
2. **Late filing due to outage** — do NOT self-declare relief. Wait for an official DJP `Pengumuman`; file as soon as possible and prepare a written explanation for the KPP.
3. **NSFP rejected** — never back-date a Faktur Pajak. Issue once NSFP is granted.
4. **Withholding article unclear** — hold the filing. Mis-categorisation between PPh 23 / 4(2) / 15 / 26 requires a pembetulan, not an in-form note.
5. **QR fails verification** — re-issue. A Faktur Pajak with a failing QR code is not creditable.
6. **Sertifikat Digital expiring** — renew at least 30 days before expiry; Coretax blocks signing on lapse.
7. **PIC departure** — revoke access immediately; rotate the certificate passphrase if it was known to that user.
8. **Always retain PDFs** — Faktur Pajak, Bukti Potong, BPE. Workpapers hold offline copies for at least 10 years (UU KUP record retention).

## Section 11 — Reference material

### Key legislation and regulations

**Key legislation and regulations**

| Topic | Reference |
| --- | --- |
| Tax administration framework | UU KUP (UU No. 28/2007 sebagaimana terakhir diubah dengan UU HPP No. 7/2021) |
| Coretax — overall implementing regulation | **PMK 81/2024** (Peraturan Menteri Keuangan tentang Ketentuan Perpajakan dalam rangka Pelaksanaan Sistem Inti Administrasi Perpajakan) |
| NIK-as-NPWP | PMK-112/PMK.03/2022; PER-04/PJ/2020 and amendments |
| Faktur Pajak (substance) | PMK-151/PMK.03/2013 and successors; DJP Circular SE-17/PJ/2014 |
| e-Faktur | PER-16/PJ/2014 as updated; superseded operational rules folded into PMK 81/2024 |
| e-Bupot Unifikasi | **PER-24/PJ/2021** (original Unifikasi), refreshed by **PER-2/PJ/2024** (operational rules for e-Bupot Unifikasi inside Coretax — confirm latest amending number) |
| e-Bupot 21/26 | PER-2/PJ/2024 (companion provisions for employment withholding inside Coretax) |
| PMSE (foreign digital service providers) | PMK-48/PMK.03/2020 — independent of Coretax but reportable inside it |
| Penalties | UU KUP Chapter VIII (Sanksi) |

### Useful DJP resources

- pajak.go.id — official DJP portal (announcements, FAQs, Coretax onboarding).
- coretaxdjp.pajak.go.id — Coretax production tenant.
- DJP Kring Pajak 1500200 — taxpayer hotline.

### Known gaps

- **Foreign-taxpayer onboarding** — DJP has signalled a dedicated 16-digit foreign ID; foreigners currently retain 15-digit NPWP padded to 16. **TBC.**
- **Coretax Form** — full SPT 1770 availability **February 2026**; later expansion TBC.
- **Pembetulan of pre-2025 periods through Coretax** — no single conclusive DJP instruction; default to legacy channel.
- **PJAP integration patterns** — out of scope for this skill.

### Self-check before lodging through Coretax

- [ ] Tax period in the correct cutover bucket (see Section 9)
- [ ] NPWP entered in the right format (16-digit NIK or 15-digit padded)
- [ ] Digital certificate valid; passphrase known
- [ ] NSFP balance adequate for expected Faktur Pajak volume
- [ ] All Bukti Potong correctly classified by article (PPh 23 vs 4(2) vs 15 vs 26)
- [ ] DGT Form attached for any treaty-rate PPh 26
- [ ] Kode Billing paid; NTPN attached before lodging the SPT
- [ ] BPE saved to the workpaper
- [ ] Outage / delay events documented with screenshots and timestamps

### Changelog

**Changelog**

| Version | Date | Change |
| --- | --- | --- |
| 1.0 | May 2026 | Initial release covering Coretax DJP from 1 Jan 2025 go-live: account activation, NIK-as-NPWP, e-Faktur inside Coretax, e-Bupot Unifikasi, SPT channels, Q1-2025 implementation issues, and DJP Online cutover routing. |

## Prohibitions

- NEVER advise filing a 2025-period Faktur Pajak through the retired desktop e-Faktur client — Coretax is the only valid issuance channel from 1 Jan 2025.
- NEVER back-date a Faktur Pajak to avoid an NSFP delay.
- NEVER guess between PPh 23 / 4(2) / 15 / 26 to expedite an e-Bupot Unifikasi filing.
- NEVER self-declare an outage-based deadline waiver in the absence of a DJP `Pengumuman`.
- NEVER reuse or share a taxpayer's digital-certificate passphrase across reviewer or PIC accounts.
- NEVER present this skill's content as a substitute for the substantive tax skills (`indonesia-vat`, `id-payroll-pph21`, the income-tax skills) — Coretax is the platform; the tax content lives elsewhere.

## Disclaimer

Provided for informational purposes only; not tax, legal, or financial advice. Open Accountants and its contributors accept no liability. Coretax behaviour, URLs, and procedures may change without notice — cross-check against the latest DJP `Pengumuman` on pajak.go.id. All outputs must be reviewed by a qualified Konsultan Pajak before lodgement.

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
