---
name: id-pph-final-umkm
description: "Use this skill whenever asked to compute, review, or advise on Indonesia PPh Final UMKM — the 0.5% final income tax on gross turnover available to micro, small, and medium enterprises (UMKM) under PP 23/2018 and PP 55/2022 (as revised). Trigger on phrases like \"PPh Final UMKM\", \"0.5 percent tax Indonesia\", \"PP 23/2018\", \"PP 55/2022\", \"MSME tax Indonesia\", \"pajak final UMKM\", \"tarif 0,5%\", \"peredaran bruto\", \"Pengusaha Kecil PPh\", or any question about whether a sole trader, PT Perorangan, CV, Firma, or Koperasi can use the 0.5% regime. Covers eligibility, the IDR 4.8 billion turnover threshold, time limits, the pekerjaan bebas (professional services) exclusion, opt-out mechanics, monthly self-deposit through Coretax DJP, annual SPT reporting, and the interaction with PPN/VAT and NIK-as-NPWP. Out of scope: corporate income tax under PPh Badan progressive rates (see PPh 25/29 workflows), partial-year regime changes, PPh 21 employment withholding (see id-payroll-pph21), PPN/VAT (see indonesia-vat), and any taxpayer above the IDR 4.8 billion threshold. ALWAYS read this skill before touching any PPh Final UMKM work."
jurisdiction: ID
tax_year: 2025
last_updated: 2026-07-13
reviewed_by: RILIA PUTRI
review_status: current
tier: 1
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# ID Pph Final Umkm

## Indonesia PPh Final UMKM — 0.5% MSME Final Tax Skill v1.0

> Load alongside `foundation.md` and `intake.md`. For employment withholding see `id-payroll-pph21.md`; for VAT/PPN see `indonesia-vat.md`. Covers ONLY the PPh Final UMKM facility under PP 23/2018 as superseded and revised by PP 55/2022.

## Verified rates & thresholds (accountant-reviewed)

> Reviewed against the cited tax authorities by **RILIA PUTRI** on 2026-06-03.
> Items flagged for further clarification are tracked separately and excluded here.
> This block is generated from verified `skill_facts` — edit the facts, not the prose.

### PPh Final UMKM 0.5%

- **Tax rate** — Rate of 0.5% remains applicable for qualifying taxpayers with certain gross turnover. PP 20/2026 does not change the tax rate but revises taxpayer eligibility criteria and exclusions.  _(UU PPh Art. 4(2); PP 55/2022 Art. 56 as amended by PP 20/2026.)_
- **Character** — Final — not creditable; no expenses deductible  _(UU PPh Art. 4(2); PP 55/2022 Art. 56 as amended by PP 20/2026.)_
- **Tax rate** — Rate of 0.5% remains applicable for qualifying taxpayers with certain gross turnover. PP 20/2026 does not change the tax rate but revises taxpayer eligibility criteria and exclusions.  _(UU PPh Art. 4(2); PP 55/2022 Art. 56 as amended by PP 20/2026.)_
- **Monthly deposit deadline** — Final income tax under the UMKM regime is generally payable no later than the 15th day of the following month after the tax period. Administrative procedures follow prevailing tax administration regulations.  _(UU KUP as amended by UU HPP; PP 55/2022 Art. 62; PMK 81/2024.)_
- **OP SPT deadline** — 31 March 2026 for FY2025  _(UU KUP Art. 3(3)(b) as amended by UU HPP)_
- **Entity SPT deadline** — 30 April 2026 for FY2025  _(UU KUP Art. 3(3)(c) as amended by UU HPP)_
- **OP tax-free band** — Individual taxpayers remain entitled to the IDR 500 million annual gross-turnover exemption before the 0.5% final tax applies.  _(UU PPh Art. 7; PP 55/2022 Art. 60; PP 20/2026.)_
- **Orang Pribadi (sole trader)** — No time limit (revised — originally 7 years)  _(PP 20/2026 Article I items 4 and 6.)_
- **PT Perorangan** — No time limit (revised)  _(PP 20/2026 Article I items 4 and 6.)_
- **Koperasi, CV, Firma, BUMDes** — 4 tahun (Koperasi only); CV, Firma, BUMDes no longer eligible under PP 20/2026 (transitional period only for remaining PP 55/2022 term)  _([PP 20/2026 Article I item 4.](https://www.pajak.go.id/en/node/119954))_
- **PT (ordinary)** — 3 years  _(PP 20/2026 Article I item 4.)_
- **Pekerjaan bebas** — Excluded — doctors, lawyers, notaries, accountants, architects, consultants, actuaries must use progressive  _(PP 20/2026 Article I item 3.)_
- **BUT / non-residents** — Permanent establishments (BUT) remain excluded from the UMKM final tax regime.  _(PP 55/2022 Art. 57(2)(d) as amended by PP 20/2026.)_
- **Late monthly payment** — Late tax payment generally subject to monthly interest sanctions calculated using the prevailing Minister of Finance interest rate determined under Indonesian tax administration regulations  _(UU KUP Art. 9(2a) as amended by UU HPP; PMK 81/2024 as amended by PMK 1/2026)_
- **Late SPT Tahunan OP** — IDR 100,000 fine  _(UU KUP Art. 7)_
- **Late SPT Tahunan Badan** — IDR 1,000,000 fine  _(UU KUP Art. 7)_
- **Bribery/gratuity — deductibility** — NEW provision per PP 20/2026 Article 20A: Expenditures in the form of bribes, gratuities, and other payments related to corruption or bribery offences — including payments to foreign public officials — are NOT deductible as business expenses for corporate taxpayers. Effective 22 April 2026. Introduced pursuant to OECD anti-bribery recommendations as part of Indonesia's OECD accession process.  _(PP 20/2026 Article I items 1 and 2.)_

## Section 1 — Quick reference

**Quick reference table**

| Field | Value |
| --- | --- |
| Country | Indonesia (Republik Indonesia) |
| Tax | PPh Final UMKM — 0.5% Final Income Tax on Gross Turnover (Peredaran Bruto) |
| Currency | IDR (Indonesian Rupiah / Rp) |
| Tax year | Calendar year (1 Jan – 31 Dec); current = 2025 |
| Statutory basis | UU 7/2021 (HPP); UU 36/2008 (PPh) as amended; PP 23/2018; PP 55/2022 Bagian Kedua, as revised |
| Tax rate | 0.5% of monthly gross turnover (peredaran bruto) |
| Eligibility threshold | Annual peredaran bruto ≤ IDR 4,800,000,000 (IDR 4.8B) |
| Character | **Final** — not creditable; no expenses deductible against it |
| Tax authority | Direktorat Jenderal Pajak (DJP) |
| Filing portal | Coretax DJP (phased 2024–2025 replacement of DJP Online / e-Billing) |
| Monthly deposit deadline | By the 15th of the following month |
| Annual SPT (individual) | SPT Tahunan 1770, "Lampiran PPh Final" — due **31 March 2026** for FY2025 |
| Annual SPT (entity) | SPT Tahunan PPh Badan 1771, "Lampiran PPh Final" — due **30 April 2026** for FY2025 |
| MAP/KJS payment code | **411128 / 420** — TBC, verify with Indonesian accountant |
| Individual NPWP | NIK-as-NPWP since 1 July 2024 (PMK 136/2023) |
| Validated by | Pending — Konsultan Pajak sign-off required |
| Skill version | 1.0 |

### Who qualifies — at a glance

**Who qualifies — at a glance table**

| Taxpayer type | Eligible? | Time limit (PP 55/2022 as revised) |
| --- | --- | --- |
| Orang Pribadi (sole trader) | Yes, if turnover ≤ IDR 4.8B and not pekerjaan bebas | **No time limit** (revised); OP facility extended through end of 2025 (commentary: through 2029). See Section 4. |
| PT Perorangan (single-member micro PT) | Yes | **No time limit** (revised). See Section 4. |
| Koperasi, CV, Firma, BUMDes | Yes | **4 years** from registration or 2018 (later) |
| PT (ordinary) | Yes (originally) | **3 years** from registration or 2018 (later) |
| Pekerjaan bebas (doctors, lawyers, notaries, accountants, architects, consultants, actuaries, etc.) | **No** | Must use Article 17 progressive rates |
| BUT (permanent establishment) and non-residents | **No** | Out of scope |

Conservative defaults are consolidated in Section 7.

## Section 2 — Required inputs and refusal catalogue

### Required inputs

- **Minimum viable** — (1) Full-year resident confirmation (per `intake.md`); (2) annual gross turnover for FY2025; (3) taxpayer type; (4) confirmation activity is not pekerjaan bebas; (5) year first registered for 0.5% (time-limit test).
- **Recommended** — Monthly turnover schedule, NPWP/NIK, prior-year SPT, kode billing / BPN receipts, PKP status (see `indonesia-vat.md`).
- **Ideal** — Full sales ledger / bank statements / invoices, prior SPT Tahunan, PP 23/2018 election notification, written activity description.
- **Refusal if minimum missing** — Hard stop if turnover cannot be quantified. Soft warn if only an annual aggregate exists — produce annualised computation but flag that monthly deposits cannot be reconciled.

### Refusal catalogue (PPh Final UMKM specific)

- **R-ID-UMKM-1** — Turnover exceeds IDR 4.8B. Facility unavailable. Taxpayer must compute under Article 17 progressive (OP) or PPh Badan (currently 22% headline). Escalate to Konsultan Pajak.  _(R-ID-UMKM-1)_
- **R-ID-UMKM-2** — Pekerjaan bebas. Activity listed in the PP 55/2022 penjelasan as tenaga ahli (pengacara, akuntan, arsitek, dokter, konsultan, notaris, penilai, aktuaris) or other independent profession. 0.5% regime never available regardless of turnover. Must use Article 17 with deductible expenses or NPPN if eligible. Escalate.  _(R-ID-UMKM-2)_
- **R-ID-UMKM-3** — Time limit elapsed. Cap exceeded (3 yrs PT non-perorangan; 4 yrs CV/Firma/Koperasi/BUMDes). For OP and PT Perorangan the revised PP 55/2022 removed the cap — re-verify taxpayer type. Escalate.  _(R-ID-UMKM-3)_
- **R-ID-UMKM-4** — Permanent establishment / non-resident. BUT and non-residents cannot use PPh Final UMKM. Escalate.  _(R-ID-UMKM-4)_
- **R-ID-UMKM-5** — Mid-year regime change. Mid-year crossing of IDR 4.8B, mid-year opt-out, or mid-year first registration. Requires Konsultan Pajak judgement on apportionment. Escalate.  _(R-ID-UMKM-5)_
- **R-ID-UMKM-6** — Multiple entities / branches. Threshold and time limit must be tested per legal entity. Group structures require manual review. Escalate.  _(R-ID-UMKM-6)_
- **R-ID-UMKM-7** — Foreign-source business income. Facility applies only to Indonesian-source business income. Foreign-source income follows ordinary tax with FTC (Article 24). Escalate.  _(R-ID-UMKM-7)_
- **R-ID-UMKM-8** — Passive income disputes. Rental, interest, dividends, royalties, capital gains are governed by other final-tax articles (PPh 4(2), 23, 26) and are not peredaran bruto for PP 23/2018. If allocation unclear, escalate.  _(R-ID-UMKM-8)_

## Section 3 — Tier 1 rules: qualification and calculation

### 3.1 The four eligibility tests (all must pass)

- **Threshold** — Prior-year (FY2024) peredaran bruto ≤ IDR 4,800,000,000. New taxpayers tested on annualised projection.
- **Taxpayer type** — OP, PT Perorangan, PT (ordinary), CV, Firma, Koperasi, or BUMDes. Yayasan and BUT excluded.
- **Activity** — Not pekerjaan bebas (Section 4.2).
- **Time limit** — Cumulative years using the facility within the cap for the taxpayer's category (Section 4.1).
- **Failure outcome** — If any test fails, compute under ordinary rules (Article 17 for OP; PPh Badan for entities). This skill stops there.

### 3.2 The 0.5% calculation

- **Tax base** — Peredaran bruto = gross business receipts in the calendar month, before any deduction for COGS, operating expenses, or input PPN. Excludes: Passive income under other final-tax articles (PPh 4(2), 23, 26); Salary/employment income (handled by PPh 21 — see id-payroll-pph21.md); Capital gains and one-off non-recurring income; PPN collected by PKPs on behalf of the state (see indonesia-vat.md).
- **Formula** — PPh Final per month = 0.5% × peredaran bruto. No deduction, no PTKP, no biaya jabatan, no capital allowance, no loss carry-forward. Months with zero turnover have zero tax.

### 3.3 PTKP-equivalent relief for Orang Pribadi (≤ IDR 500M)

- **PP 55/2022 relief** — PP 55/2022 introduced a relief: an OP pays 0.5% only on peredaran bruto above IDR 500,000,000 per year. The first IDR 500M of annual turnover is exempt.
- **Individuals only** — Individuals only — not available to PT, PT Perorangan, CV, Firma, Koperasi, or BUMDes.
- **Operation** — The exemption operates cumulatively. 0.5% kicks in from the month cumulative turnover crosses IDR 500M, and applies only to the excess in that month; from the following month, 0.5% applies to the full monthly turnover. See Example 1.

### 3.4 Interaction with PPN/VAT

- **Independence of regimes** — PPh Final UMKM and PPN are independent regimes. The IDR 4.8B threshold coincides with the PPN PKP registration threshold but is not linked.
- **Below 4.8B** — A UMKM taxpayer below IDR 4.8B is generally below the PKP threshold and does not charge PPN.
- **Voluntary PKP registration** — A UMKM taxpayer may voluntarily register as PKP (e.g., to issue Faktur Pajak to B2B customers). In that case they collect 11% PPN on sales and still pay 0.5% PPh Final on turnover. Regimes run in parallel.
- **PPN treatment** — Peredaran bruto is net of PPN collected — PPN is a state collection, not income.

### 3.5 Interaction with PPh 21 (employment income)

- **Parallel employment income** — If the same individual is both an employee and a UMKM sole trader, the employer withholds PPh 21 on salary (see id-payroll-pph21.md) and the individual separately pays 0.5% PPh Final on UMKM turnover. SPT 1770 reports both streams. The PPh Final is not creditable against PPh 21.

### 3.6 NIK-as-NPWP

- **NIK-as-NPWP** — Since 1 July 2024 (PMK 136/2023), the 16-digit NIK functions as the NPWP for individuals. OP UMKM taxpayers use NIK on kode billing, SPT Tahunan, and Faktur Pajak (if PKP). Entities use the 15-digit NPWP Badan (a 16-digit entity NPWP is also being issued under Coretax). If uncertain, write "TBC — verify with Indonesian accountant".  _(PMK 136/2023)_

## Section 4 — Tier 2 catalogue: revisions, exclusions, and edge cases

### 4.1 PP 55/2022 — revised time limits

- **Original caps intro** — PP 55/2022 (which superseded and consolidated PP 23/2018) originally set the following caps from the year of registration or from FY2018, whichever is later:

**Original cap table**

| Taxpayer type | Original cap (PP 55/2022 as enacted Dec 2022) |
| --- | --- |
| Orang Pribadi | 7 years |
| Koperasi, CV, Firma, BUMDes | 4 years |
| PT (Perseroan Terbatas) | 3 years |

- **REVISION 1 — No time limit for OP and PT Perorangan** — Per analysis by DDTC and MUC, the original 7-year cap for OP (and the 3-year cap insofar as it would apply to PT Perorangan — a single-member micro-PT under UU Cipta Kerja) has effectively been removed. OP and PT Perorangan may continue using the 0.5% facility indefinitely so long as they remain below IDR 4.8B and satisfy the other tests. TBC — verify the exact PP/PMK reference with an Indonesian accountant before quoting to a client.
- **REVISION 2 — Extension of OP facility through end of 2025** — The OP 7-year window for taxpayers who first elected in 2018 would have expired at end of 2024. The Government issued an extension keeping OPs in the regime through at least end of 2025, and some practitioner commentary references a further extension running through 2029. Both should be noted in the reviewer brief; the safe operating position for FY2025 is that OPs who would otherwise have aged out remain in. TBC — verify the exact extension instrument with an Indonesian accountant.
- **Operational note for entities** — The 3-year and 4-year caps remain. A PT first registered in 2022 used 0.5% in 2022–2024 and from FY2025 must compute under ordinary PPh Badan. A CV first registered in 2021 used the facility 2021–2024 and exits in FY2025. Always confirm "first year used" from the client's PP 23/2018 election notification (Surat Pemberitahuan).

### 4.2 Pekerjaan bebas (independent professions) — excluded

- **Excluded activities list** — PP 55/2022 (penjelasan) excludes OPs providing services as pekerjaan bebas. Drawing from Article 1 UU PPh and the penjelasan, the list includes: Tenaga ahli: pengacara, akuntan, arsitek, dokter, konsultan, notaris, penilai, aktuaris. Performers (pemain musik, penyanyi, bintang film/iklan, sutradara, kru film, foto model, pemain drama, penari); olahragawan. Penasihat, pengajar, pelatih, penceramah, moderator; pengarang, peneliti, penerjemah; agen iklan; pengawas/pengelola proyek. Perantara (brokers); petugas penjaja barang dagangan; agen asuransi; distributor MLM / direct selling. These taxpayers compute on net income at Article 17 rates (or NPPN if eligible). They never qualify for 0.5% regardless of turnover.
- **Edge case — borderline activities** — A software developer selling SaaS to multiple unrelated customers is a business (eligible). A freelance developer billing one client for personal effort with no separate establishment may be challenged as pekerjaan bebas. A YouTuber/content creator generally qualifies. A trainer running an institutionalised training company qualifies; the same person consulting solo is pekerjaan bebas. When in doubt, treat as pekerjaan bebas and flag for reviewer.

### 4.3 Opt-out election (one-way per year)

- **Opt-out mechanics** — A taxpayer who qualifies may elect to compute under ordinary rules by submitting a Surat Pemberitahuan to the local KPP. Election must be made before the start of the tax year in which it takes effect, or at first registration. One-way for that tax year — no reversion mid-year. A taxpayer who opted out may return to 0.5% in a subsequent year by simply not renewing the opt-out, provided eligibility and time-limit tests still pass.
- **When opt-out makes sense** — Low net-margin businesses (high COGS) can find 0.5% of gross exceeds Article 17 progressive tax on net. Break-even is roughly where (PKP × Art. 17 effective rate) < (gross × 0.5%); for an OP with PTKP TK/0 of IDR 54M, opt-out tends to be cheaper once gross margin drops below ~5% (TBC — compute case-by-case).

### 4.4 Transition edge cases

- **First-year taxpayer** — Tested on annualised projection. Apply 0.5% from month of registration.
- **Mid-year crossing of IDR 4.8B** — Continue 0.5% for FY2025; threshold breach takes effect from FY2026 (PP 55/2022 Art. 8 — prospective). Reviewer flags the FY2026 regime change.  _(PP 55/2022 Art. 8)_
- **Returning from opt-out** — Resume 0.5% from January of the new year, subject to time-limit and threshold tests.
- **Cessation of business mid-year** — Pay 0.5% on actual months of operation; final SPT Tahunan reconciles.
- **Acquisition / merger** — Out of scope — escalate.

### 4.5 Historical note — OP 7-year window

For OPs who first used the regime in FY2018, the original 7-year window expired at end of FY2024. Per the extension and the indefinite-period clarification (Section 4.1), these OPs remain in the regime for FY2025. Reviewer brief should record both (a) the original cap that would have expired and (b) the citation supporting continued eligibility, so the position is defensible.

## Section 5 — Worked examples

### Example 1 — Freelancer Orang Pribadi

Pak Andi, sole-trader e-commerce reseller (jualan online via Tokopedia/Shopee). Full-year resident, single, no salary. Registered for PP 23/2018 in 2021. Activity = trading goods (not pekerjaan bebas). FY2025 monthly turnover (IDR): Jan 40M, Feb 45M, Mar 50M, Apr 55M, May 60M, Jun 55M, Jul 65M, Aug 70M, Sep 70M, Oct 75M, Nov 80M, Dec 85M — annual total IDR 750,000,000.

Threshold: IDR 750M ≤ IDR 4.8B — pass. Type: OP — pass. Activity: trading — pass. Time limit: no cap for OP under revised PP 55/2022 — pass. PTKP-equivalent: first IDR 500M exempt (Section 3.3).

Cumulative crosses IDR 500M in September. Tax only on the excess in Sep, then on full monthly turnover from Oct.

**Monthly PPh Final table**

| Month | Taxable portion (IDR) | 0.5% (IDR) | Due |
| --- | --- | --- | --- |
| Jan–Aug | 0 | 0 | n/a |
| Sep | 10,000,000 | **50,000** | 15 Oct 2025 |
| Oct | 75,000,000 | **375,000** | 15 Nov 2025 |
| Nov | 80,000,000 | **400,000** | 15 Dec 2025 |
| Dec | 85,000,000 | **425,000** | 15 Jan 2026 |
| **Total** | **250,000,000** | **1,250,000** |  |

SPT Tahunan 1770 by 31 March 2026 reports IDR 750M turnover in Lampiran PPh Final with IDR 1,250,000 already paid. Not creditable against any other tax.

Confirm NIK-as-NPWP registration (PMK 136/2023); confirm monthly kode billing generated via Coretax DJP with MAP/KJS 411128/420 (TBC).

### Example 2 — PT Perorangan

PT Mawar Digital Perorangan, single-member micro-PT (UU Cipta Kerja), incorporated March 2024. Sells digital templates and stock photos to international customers via Etsy. FY2025 annual gross turnover: IDR 2,200,000,000.

Threshold IDR 2.2B — pass. Type PT Perorangan — pass. Activity (digital goods to many unrelated customers) — business, not pekerjaan bebas. (A solo designer billing one client for personal creative service would be pekerjaan bebas; the PT Perorangan structure with multiple customers establishes a business.) Time limit: no cap under revised PP 55/2022 — pass. PTKP-equivalent: not available to entities — full IDR 2.2B is the base.

0.5% × monthly turnover, paid by 15th of following month via Coretax DJP under entity NPWP.

**Quarterly turnover table**

| Quarter | Quarterly turnover | 0.5% |
| --- | --- | --- |
| Q1 | 480,000,000 | 2,400,000 |
| Q2 | 520,000,000 | 2,600,000 |
| Q3 | 560,000,000 | 2,800,000 |
| Q4 | 640,000,000 | 3,200,000 |
| **FY2025** | **2,200,000,000** | **11,000,000** |

(Quarterly aggregation shown for compactness — actual deposits are monthly.)

SPT Tahunan PPh Badan 1771 by 30 April 2026 reports IDR 2.2B in Lampiran PPh Final with IDR 11M paid. No PPh Badan 22% is computed on this turnover — PPh Final discharges the business income-tax liability in full.

(a) Confirm PP 23/2018 election notification on file at KPP. (b) Confirm no voluntary PKP registration; advise on PPN implications well before any approach to IDR 4.8B (see indonesia-vat.md). (c) Salary/dividends from PT to the shareholder-director handled separately — salary under PPh 21 (see id-payroll-pph21.md); dividends potentially exempt under PMK 18/2021 if reinvested.

## Section 6 — Filing and payment mechanics

### 6.1 Monthly self-deposit (setor sendiri)

- **Overview** — PPh Final UMKM is a self-assessed, self-deposited tax. No DJP-issued invoice triggers it.

0. **Step 1** — End of month — sum gross business turnover (peredaran bruto).
0. **Step 2** — For OP only — track cumulative annual turnover. If still ≤ IDR 500M, no tax due. If cumulative crosses IDR 500M during the month, apply 0.5% only to the excess. From the next month, apply 0.5% to the full monthly turnover.
0. **Step 3** — Compute: PPh Final = 0.5% × taxable portion.
0. **Step 4** — Generate kode billing through Coretax DJP (coretaxdjp.pajak.go.id). Use MAP/KJS 411128 / 420 (PPh Final atas Penghasilan dari Usaha Wajib Pajak yang Memiliki Peredaran Bruto Tertentu). TBC — verify the exact KJS with an Indonesian accountant; KJS codes have been updated during the Coretax rollout.
0. **Step 5** — Pay by the 15th of the following month. Late payment triggers sanksi administrasi bunga (interest) per Article 9 KUP — monthly rate set by MoF.
0. **Step 6** — Retain Bukti Penerimaan Negara (BPN) — the state receipt issued automatically.

### 6.2 Coretax DJP transition

Coretax DJP is the integrated DJP administration platform rolled out in late 2024 / early 2025, replacing legacy DJP Online, e-Billing, parts of e-Faktur, and e-Bupot. As of mid-2025 most PPh Final UMKM billing flows through Coretax. The MAP/KJS structure is preserved across the legacy and Coretax channels. Verify the live URL with the client before each filing — the DJP entry point has shifted several times during the rollout.

### 6.3 Annual SPT

- **Reporting requirement** — PPh Final paid monthly must still be reported annually in the SPT Tahunan, even though no additional tax is due on the same income.

**Annual SPT table**

| Taxpayer | Form | Lampiran | Filing deadline FY2025 |
| --- | --- | --- | --- |
| Orang Pribadi | SPT Tahunan PPh OP 1770 | Lampiran III (Penghasilan yang Dikenakan PPh Final dan/atau Bersifat Final) | **31 March 2026** |
| PT, PT Perorangan, CV, Firma, Koperasi, BUMDes | SPT Tahunan PPh Badan 1771 | Lampiran IV / PPh Final attachment | **30 April 2026** |

The Lampiran captures: gross turnover (peredaran bruto), tax base, PPh Final paid, and the supporting BPN references. The reviewer should reconcile the monthly BPN total to the annual SPT figure.

### 6.4 Sanctions and records

**Sanctions table**

| Event | Sanction |
| --- | --- |
| Late monthly payment | Sanksi bunga per Article 9(2a) KUP — monthly rate published by MoF (typically ~1–2.5%/month, max 24 months) |
| Late/non-filing SPT Tahunan OP | Denda IDR 100,000 per SPT |
| Late/non-filing SPT Tahunan Badan | Denda IDR 1,000,000 per SPT |
| Audit understatement | Sanksi bunga + sanksi kenaikan up to 50% (UU KUP) |

- **Record retention** — Article 28 UU KUP requires retention of books and supporting documents for 10 years from end of tax year — monthly turnover calc, BPN receipts, kode billing prints, BPE acknowledgements.  _(Article 28 UU KUP)_

## Section 7 — Conservative defaults (consolidated)

**Conservative defaults table**

| Question | Default |
| --- | --- |
| Activity is pekerjaan bebas? | **Yes (excluded)** until taxpayer proves otherwise; require written activity description |
| Below IDR 4.8B? | Test on prior-year actual; otherwise on current-year annualised projection |
| Time limit elapsed? | Elapsed for non-OP/non-PT-Perorangan if unclear; not elapsed for OP/PT Perorangan per revised PP 55/2022 — always flag citation uncertainty |
| MAP/KJS code? | "TBC — verify with Indonesian accountant"; do not auto-generate kode billing |
| Mixed business + pekerjaan bebas? | Split income streams; 0.5% only on business; flag |
| Cash or accrual? | **Cash receipts** (peredaran bruto received) for PPh Final, even if accrual books exist |
| PKP voluntary registration? | Out of scope — refer to `indonesia-vat.md` |
| Multiple businesses under one NPWP? | Sum gross turnover for the IDR 4.8B test |
| Foreign-currency receipts? | Convert at BI middle rate on receipt date; flag if FX is material |

## Section 8 — Sources

All citations are to primary Indonesian statutes, government regulations (PP), Minister of Finance regulations (PMK), and DJP guidance. Practitioner commentary (DDTC, MUC, Ortax) is cited where it supports interpretation of revised provisions — practitioner commentary is not law, and the reviewer must verify against the underlying instrument.

### Primary legislation

- **placeholder** — 
- **UU 7/2021 (HPP)** — amends UU PPh, UU PPN, UU KUP; introduced NIK-as-NPWP.  _([UU 7/2021](https://peraturan.bpk.go.id/Details/187081/uu-no-7-tahun-2021))_
- **UU 36/2008 (PPh), as amended** — Art. 4(2) authorises final taxes; Art. 17 is the ordinary progressive schedule.  _([UU 36/2008](https://peraturan.bpk.go.id/Details/39305/uu-no-36-tahun-2008))_
- **UU 6/1983 (KUP), as amended** — Arts. 9, 28, 36, 38.  _([UU 6/1983](https://peraturan.bpk.go.id/Details/47169/uu-no-6-tahun-1983))_

### Government regulations (PP)

- **PP 23/2018** — original 0.5% UMKM regulation.  _([PP 23/2018](https://peraturan.bpk.go.id/Details/82146/pp-no-23-tahun-2018))_
- **PP 55/2022** — Bagian Kedua (Arts. 56–63) consolidates and replaces PP 23/2018 from 2022; introduces IDR 500M OP relief; originally set 3/4/7-year caps. Subsequent revision removed the OP/PT-Perorangan cap and extended the OP facility through FY2025 (commentary: through 2029).  _([PP 55/2022](https://peraturan.bpk.go.id/Details/238760/pp-no-55-tahun-2022))_

### Minister of Finance regulations (PMK)

- **PMK 136/2023** — NIK-as-NPWP implementation (effective 1 July 2024).  _([PMK 136/2023](https://peraturan.bpk.go.id/Details/271732/pmk-no-136-pmk032023))_
- **PMK 168/2023** — PPh 21 TER (context for parallel employment income).  _(PMK 168/2023)_

### DJP guidance and practitioner commentary

DJP PPh Final UMKM: <https://www.pajak.go.id/index-tarif-pph-umkm>, <https://www.pajak.go.id/id/pp-23-tahun-2018>
Coretax DJP portal: <https://coretaxdjp.pajak.go.id> (verify URL at filing time)
DDTC News — analysis of OP time-limit revision and 0.5% extension: <https://news.ddtc.co.id>
MUC Consulting — PP 55/2022 revision and indefinite period for OP / PT Perorangan: <https://mucglobal.com/news>
Ortax — KJS codes and kode billing structure: <https://ortax.org>

### Cross-references in this package

`foundation.md` — workflow architecture.
`intake.md` — Step 1 scope check.
`id-payroll-pph21.md` — PPh 21 and BPJS for parallel employment income.
`indonesia-vat.md` — PPN / PKP registration alongside UMKM.
`references.md` — bibliography.

## PROHIBITIONS

NEVER treat pekerjaan bebas income as eligible for 0.5%, regardless of turnover.
NEVER offset COGS, expenses, or losses against the 0.5% base — the base is gross turnover.
NEVER treat PPh Final as creditable against PPh 21/22/23/25/29 — it is final.
NEVER apply the IDR 500M PTKP-equivalent relief to entities — OP only.
NEVER quote an MAP/KJS code without verification — write "TBC".
NEVER ignore the time-limit test for entities (PT non-perorangan: 3 yrs; CV/Firma/Koperasi/BUMDes: 4 yrs).
NEVER combine passive income (rent, royalties, interest, dividends, capital gains) into the 0.5% base.
NEVER present the calculation as definitive — always label as estimated, pending Konsultan Pajak review.
NEVER advise on a mid-year regime change without reviewer sign-off (R-ID-UMKM-5).
NEVER assume the Coretax DJP entry URL is unchanged — verify before filing.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for errors, omissions, or outcomes arising from use of this skill. All outputs must be reviewed and signed off by a licensed Indonesian tax consultant (Konsultan Pajak) before filing or acting. Indonesian tax law — and in particular the PP 55/2022 framework, the Coretax DJP rollout, and the kode billing MAP/KJS structure — has been changing rapidly in 2023–2025; always verify with primary sources.

The up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review, and track updates as Indonesian tax law changes.

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
