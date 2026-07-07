---
name: id-freelance-intake
description: ALWAYS USE THIS SKILL when a user asks for help preparing a 2025 Indonesian tax return AND mentions freelancing, self-employment, online seller, kontraktor, pekerjaan bebas, sole proprietor (Usaha Dagang), or a PT Perorangan in Indonesia. Trigger on phrases like "siapkan SPT Tahunan", "lapor pajak freelance Indonesia", "PPh Final UMKM 0,5%", "PP 55/2022", "PT Perorangan tax return", "online seller Indonesia tax", "kontraktor pajak", "pekerjaan bebas", "Usaha Dagang", "Coretax SPT", "NPWP 16 digit", or any similar phrasing where the user is an Indonesia-resident self-employed individual, sole proprietor, or micro-PT founder. This is the REQUIRED entry point for the Indonesian freelance/SME workflow — every downstream skill in the stack (id-pph-final-umkm, id-income-tax, id-corporate-tax, id-withholding, id-payroll-pph21, indonesia-vat, id-bookkeeping, id-einvoice-coretax, id-formation, id-tax-optimization, id-return-assembly) depends on this skill running first. Uses ask_user_input_v0-style structured questions. Indonesian residents only (full-year tax residents and foreigners with > 183 days permanent presence). ALWAYS read this skill first when starting an Indonesian freelance/SME tax workflow.
jurisdiction: ID
tax_year: 2025
tier: 2
last_updated: 2026-07-06
---

# id-freelance-intake

## What this file is

The intake orchestrator for Indonesian-resident self-employed individuals, sole proprietors (Usaha Dagang / UD), and micro-PT founders (PT Perorangan). Every downstream Indonesian content skill depends on this skill producing a structured intake package first.

Job: (1) confirm taxpayer is in scope, (2) classify the regime (UMKM Final 0.5% vs progressive PPh OP vs PPh Badan), (3) identify downstream skills to run, (4) hand off to `id-return-assembly`. Outputs addressed to a credentialed Indonesian reviewer (Konsultan Pajak with Brevet A/B/C, or an Akuntan Publik). The reviewer signs off — this skill is not the preparer of record.

## Section 1 — Quick reference: regime decision tree at a glance

```
Full-year Indonesian tax resident? -> NO = REFUSE
       |
Pekerjaan bebas? -> YES = Progressive PPh OP only (no UMKM Final)
       |
2025 peredaran bruto ≤ Rp4.8B?
       |
       +-- NO  -> Progressive PPh OP + mandatory pembukuan + likely PKP
       |
       +-- YES + UMKM clock not expired (OP 7y / PT 4y / CV 3y)
                -> UMKM Final 0.5% (PP 55/2022)
                   OP: first Rp500m exempt (UU 7/2021 art. 7(2a))
```

Parallel routing (independent of regime):

- Turnover > Rp4.8B trailing-12 → PKP mandatory → route `indonesia-vat` + `id-einvoice-coretax`.
- Employees → route `id-payroll-pph21`.
- Pays resident suppliers for services / rent / non-resident suppliers → route `id-withholding`.
- Entity unclear (OP / UD / PT Perorangan / CV / PT) → route `id-formation`.
- Books not on SAK ETAP / SAK EMKM → route `id-bookkeeping`.
- Optimisation requested or borderline → route `id-tax-optimization`.
- Always final → `id-return-assembly`.

## Section 2 — Workflow runbook (order of operations)

Strict order. Do not narrate steps.

0. **Opening** — one-line greeting + flow summary + reviewer reminder, then launch the refusal sweep.
0. **Refusal sweep** — single `ask_user_input_v0` call with the 4 questions in Section 5.1.
0. **Document dump** — ask user to upload everything at once (rekening koran, faktur, bukti potong, prior SPT). Do not insist on bank statements alone.
0. **Inference pass** — parse every document; extract turnover, expenses, withholding, prior payments.
0. **Regime classification** — apply Section 4 decision tree using inferred turnover + sweep answers.
0. **Confirmation** — show inferred summary + proposed regime + downstream-skill list; invite corrections.
0. **Gap filling** — `ask_user_input_v0` only for items documents cannot answer (PTKP, UMKM history, Coretax access).
0. **Handoff** — produce Section 6 summary and invoke `id-return-assembly`.

Operating principles: use `ask_user_input_v0` for multi-choice; free text only for names / NPWP / KLU. Batch up to 3 related independent questions. Never re-ask documents-visible facts. Indonesian terms in parentheses on first mention (e.g., "annual turnover (peredaran bruto)"). All amounts in IDR.

## Section 3 — Required inputs

Some inferred from documents, the rest gap-filled. All mandatory before handoff.

- **Identity / registration:** legal name (KTP), NPWP (16 digits = NIK since 1 July 2024 per PMK 136/2023, PER-06/PJ/2024), KPP terdaftar, 5-digit KLU code (PER-17/PJ/2015), PTKP (TK/0…3, K/0…3, K/I/0…3).
- **Entity:** OP / UD / PT Perorangan (UU 11/2020 art. 109(2), PP 8/2021) / PT / CV / Firma. PT Perorangan: SK Menkumham date. PT / CV: Akta, NIB (OSS), domicile.
- **Revenue:** 2025 peredaran bruto, monthly turnover detail, domestic vs international mix (exported services may be excluded from PKP threshold under PMK 32/2019).
- **Tax history:** first year on UMKM Final 0.5% (PP 55/2022 art. 59 clock), prior-year SPT (1770 / 1770 S / 1770 SS / 1771), outstanding pajak terutang / lebih bayar.
- **Operational:** employee count (PPh 21 / BPJS), PKP status (PMK 197/2013), Coretax DJP account active (PER-24/PJ/2024; KMK 360/KMK.03/2024), e-Faktur usage if PKP.
- **Documents:** rekening koran 2025, faktur penjualan / kuitansi, faktur pembelian / faktur pajak masukan, bukti potong PPh 21 / 23 / 4(2) / 26, prior-year SPT, SSP / e-Billing receipts.

## Section 4 — Regime decision tree with thresholds and citations

All thresholds 2025-effective.

### 4.1 Residency gate — UU 36/2008 art. 2(3) as amended by UU 7/2021

- **Residency definition and refusal** — Indonesian tax resident = individual residing in Indonesia, or present > 183 days in any 12-month window, or present with intent to reside. Foreigners > 183 days are in scope here. The PMK 18/2021 qualified-expat 4-year regime is out of scope → refuse. Not full-year resident → REFUSE.  _(UU 36/2008 art. 2(3) as amended by UU 7/2021)_

### 4.2 Pekerjaan bebas gate — UU 36/2008 art. 4(1)(c)

- **Pekerjaan bebas definition and effect** — Pekerjaan bebas = individual professional service requiring special skill performed independently. Examples (PER-17/PJ/2015 + DJP guidance): doctors, dentists, notaries, PPAT, advokat, arsitek, akuntan, konsultan pajak, aktuaris, penilai, insinyur konsultan; artists, athletes, presenters, MCs, models, musicians; authors, researchers, translators. If pekerjaan bebas → UMKM Final 0.5% not available (PP 55/2022 art. 56(2)). Use progressive PPh OP (UU 36/2008 art. 17 as amended by UU 7/2021). Route `id-income-tax` only.  _(UU 36/2008 art. 4(1)(c); PP 55/2022 art. 56(2); UU 36/2008 art. 17 as amended by UU 7/2021)_

### 4.3 Turnover threshold gate — PP 55/2022 art. 56, 60; PMK 164/2023

- **UMKM Final availability threshold** — Peredaran bruto ≤ Rp4.8B + not pekerjaan bebas → UMKM Final 0.5% available (optional; taxpayer may elect progressive instead). > Rp4.8B → UMKM Final not available; progressive PPh OP + mandatory pembukuan under UU 28/2007 art. 28. IDR  _(PP 55/2022 art. 56, 60; PMK 164/2023; UU 28/2007 art. 28)_
- **UMKM clock** — OP / UD = 7 years; PT = 4 years; CV / Firma / Koperasi / BUMDes = 3 years. Counted from first applied year (or PP 23/2018 effectivity if on regime in 2018).  _(PP 55/2022 art. 59)_
- **Rp500m OP band** — OP on UMKM Final 0.5% has first Rp500m of annual turnover exempt from 0.5% final tax. OP only — not badan. IDR  _(UU 7/2021 art. 7(2a))_
- **Routing** — → Route `id-pph-final-umkm` with monthly calc + Rp500m logic.  _(PP 55/2022)_

### 4.4 Entity gate — UU 40/2007, UU 11/2020, PP 8/2021

- **Entity type routing** — OP / UD → SPT 1770 / 1770 S / 1770 SS. Route `id-income-tax` and/or `id-pph-final-umkm`. PT Perorangan (UU 11/2020 art. 109(2), PP 8/2021) → separate entity → SPT 1771. Owner reports dividend/salary on SPT 1770. Limited to single Indonesian-citizen founder meeting micro/small criteria (PP 7/2021 art. 35). Route `id-corporate-tax`. PT / CV / Firma → SPT 1771 (CV/Firma treated as badan since UU 7/2021). Route `id-corporate-tax`. Entity unclear → route `id-formation`. PT Perorangan and small PT/CV in scope; full PT with > 50 employees, multiple subsidiaries, or audited financials → refuse.  _(UU 40/2007; UU 11/2020 art. 109(2); PP 8/2021; PP 7/2021 art. 35)_

### 4.5 PKP / VAT gate — UU 42/2009 as amended by UU 7/2021; PMK 197/2013

- **PKP mandatory threshold and VAT rates** — PKP mandatory if taxable turnover > Rp4.8B in any trailing-12 window. Voluntary below. VAT rate 11% from 1 April 2022. 12% luxury-goods rate from 1 January 2025 — verify (TBC — Perpres 201/2024, PMK 131/2024). PKP → route `indonesia-vat` + `id-einvoice-coretax`.  _(UU 42/2009 as amended by UU 7/2021; PMK 197/2013; Perpres 201/2024; PMK 131/2024)_

### 4.6 Employer gate — UU 36/2008 art. 21; PP 58/2023; PMK 168/2023

- **Employer withholding obligations** — Employees / wages → withhold PPh 21 monthly via Coretax + BPJS Kesehatan (UU 24/2011) + BPJS Ketenagakerjaan (UU 40/2004, UU 24/2011). TER schedule from 1 January 2024. Route `id-payroll-pph21`.  _(UU 36/2008 art. 21; PP 58/2023; PMK 168/2023; UU 24/2011; UU 40/2004)_

### 4.7 Withholding-agent gate — UU 36/2008 art. 23, 4(2), 26

- **Withholding agent obligations and rates** — Obligation arises if taxpayer is badan, or OP appointed as agent (PER-70/PJ/2007 list — e.g., notary, doctor with own practice), AND pays: resident suppliers for services (PPh 23, 2% on jasa); rent of immovable property (PPh 4(2) Final 10%, PP 34/2017); construction (PPh 4(2) Final, PP 9/2022); non-resident suppliers (PPh 26 20% subject to P3B treaty). Route `id-withholding`.  _(UU 36/2008 art. 23, 4(2), 26; PER-70/PJ/2007; PP 34/2017; PP 9/2022)_

### 4.8 Bookkeeping gate — UU 28/2007 art. 28

- **Bookkeeping requirement** — ≤ Rp4.8B + UMKM Final → pencatatan sufficient. Otherwise → pembukuan (full double-entry) mandatory. Route `id-bookkeeping` if pembukuan needed and not in place.  _(UU 28/2007 art. 28)_

### 4.9 Coretax DJP channel

- **Coretax filing channel requirement** — From tax year 2025 all SPT, e-Billing, e-Bupot, e-Faktur, and registration changes go through Coretax DJP (PER-24/PJ/2024; KMK 360/KMK.03/2024). Confirm access; if not active, flag for reviewer onboarding.  _(PER-24/PJ/2024; KMK 360/KMK.03/2024)_

## Section 5 — Questions to ask the user

Use `ask_user_input_v0`. Batch where independent.

### 5.1 Refusal sweep (one batched `ask_user_input_v0` call, 4 single-select questions)

- **Q1 Residency 2025:** Full-year resident (WNI / KITAS / KITAP) | Foreigner > 183 days | Part-year | Non-resident.
- **Q2 Entity:** OP (sole trader) | UD (with trade name) | PT Perorangan | PT / CV / Firma | Not sure.
- **Q3 Pekerjaan bebas?** Yes (doctor / notary / lawyer / architect / accountant / consultant / artist / …) | No (usaha / online seller / kontraktor) | Mixed.
- **Q4 2025 peredaran bruto (IDR):** ≤ Rp500m | Rp500m–Rp4.8B | Rp4.8B–Rp50B | > Rp50B | Not sure (infer from docs).

**Refusal sweep routing table**

| Answer | Action |
| --- | --- |
| Q1 full-year | continue |
| Q1 foreigner > 183d | continue; flag reviewer to rule out PMK 18/2021 expat regime |
| Q1 part-year / non-resident | **REFUSE** — full-year residents only; refer to Konsultan Pajak |
| Q2 OP / UD | continue; regime by Q3 + Q4 |
| Q2 PT Perorangan / PT / CV / Firma | continue; route `id-corporate-tax`; flag if > 50 employees |
| Q2 not sure | route `id-formation` first |
| Q3 pekerjaan bebas | force progressive PPh OP; drop UMKM Final; route `id-income-tax` |
| Q3 no | UMKM candidate (subject to Q4 + history) |
| Q3 mixed | flag; income must be segregated |
| Q4 ≤ Rp500m | UMKM Final 0.5%; OP band → effective Rp0; still file SPT; route `id-pph-final-umkm` |
| Q4 Rp500m–Rp4.8B | UMKM Final 0.5%; route `id-pph-final-umkm` |
| Q4 Rp4.8B–Rp50B | UMKM unavailable; route `id-income-tax` + `id-bookkeeping` + `indonesia-vat` |
| Q4 > Rp50B | **REFUSE** SPT prep; refer to Konsultan Pajak; still load bookkeeping / VAT |
| Q4 not sure | defer to inference |

### 5.2 Secondary batched questions

- **Q5 PKP status:** Yes (issuing e-Faktur) | No | Not sure.
- **Q6 Employees 2025:** None | 1–5 | 6–20 | > 20.
- **Q7 UMKM Final history (PP 23/2018 or PP 55/2022) — since which year?** Never | Since 2018 | 2019–2024 | Started 2025 | Not sure.
- **Q8 PTKP:** TK/0 | TK/1–3 | K/0 | K/1–3 | K/I/0–3.

**Secondary questions routing table**

| Answer | Action |
| --- | --- |
| Q5 yes / unsure with turnover > Rp4.8B | route `indonesia-vat` + `id-einvoice-coretax` |
| Q5 no but turnover > Rp4.8B | flag **PKP overdue**; route `indonesia-vat`; reviewer to register |
| Q6 ≥ 1 employee | route `id-payroll-pph21` |
| Q6 > 20 | flag (HR-grade load) |
| Q7 — apply PP 55/2022 art. 59 clock | if expired in 2025 → force progressive; drop `id-pph-final-umkm` |
| Q8 | captured for PTKP; consumed by `id-income-tax` (irrelevant under UMKM Final) |

### 5.3 Withholding question

- **Q9 In 2025 did you pay Indonesian suppliers for services, rent business premises, or pay non-resident suppliers?** Yes (services / rent / non-resident) | Multiple | No.

Any "Yes" → route `id-withholding`. Reviewer confirms whether OP is an appointed withholding agent.

### 5.4 Coretax access

- **Q10 Coretax DJP access?** Yes (active, NPWP-as-NIK linked) | No (never logged in) | Started but hit issues.

"No" or "issues" → flag in `open_flags`. Coretax is the only filing channel for 2025 SPT.

## Section 6 — Intake output template

### 6.1 Human-readable confirmation (shown to user)

```
INTAKE SUMMARY — 2025 Indonesia

Taxpayer: [Name] | NPWP/NIK: [16-digit] | KPP: [office]
PTKP: [TK/0|K/2|…] | Entity: [OP|UD|PT Perorangan|PT|CV]
KLU: [5-digit — industry] | Residency: full-year resident
Coretax: [active | onboarding needed]

REGIME: [UMKM Final 0.5% | Progressive PPh OP | PPh Badan]
  - 2025 turnover: Rp [X]
  - Pekerjaan bebas: [yes|no|mixed]
  - UMKM history: started [year] — [years left] of [7|4|3]
  - PKP: [yes|no|mandatory registration overdue]
  - Employees: [count]

DOWNSTREAM SKILLS:
  id-bookkeeping [pembukuan|pencatatan], id-pph-final-umkm [if UMKM],
  id-income-tax [if progressive], id-corporate-tax [if PT/CV/PT Perorangan],
  indonesia-vat [if PKP], id-einvoice-coretax [if PKP],
  id-payroll-pph21 [if employees], id-withholding [if WH agent],
  id-tax-optimization [if requested], id-return-assembly [always last].

OPEN FLAGS, REFUSALS TRIGGERED, CONSERVATIVE DEFAULTS APPLIED — listed below.

Confirm or correct anything above.
```

### 6.2 Structured intake package (internal JSON for id-return-assembly)

```json
{
  "jurisdiction": "ID",
  "tax_year": 2025,
  "taxpayer": {
    "name": "", "npwp": "", "nik": "", "kpp": "",
    "klu_code": "", "ptkp": "TK/0|…|K/I/3",
    "residency": "full_year_resident|foreigner_183_plus",
    "entity_type": "OP|UD|PT_Perorangan|PT|CV|Firma",
    "coretax_active": false
  },
  "regime": {
    "selected": "umkm_final_0_5|progressive_pph_op|pph_badan",
    "pekerjaan_bebas": false,
    "annual_turnover_idr": 0,
    "umkm_first_year": 0,
    "umkm_years_remaining": 0,
    "rp500m_band_applicable": false
  },
  "vat": {
    "pkp": false, "pkp_overdue_registration_flag": false,
    "trailing12_turnover_at_threshold": 0, "e_faktur_active": false
  },
  "employment": {
    "has_employees": false, "employee_count": 0,
    "bpjs_kesehatan_active": false, "bpjs_ketenagakerjaan_active": false
  },
  "withholding": {
    "paid_resident_suppliers_services": false,
    "paid_rent_business_premises": false,
    "paid_non_resident_suppliers": false,
    "is_withholding_agent": false
  },
  "bookkeeping": {
    "method_required": "pembukuan|pencatatan",
    "currently_in_place": false
  },
  "documents_received": [],
  "downstream_skills_to_load": [],
  "open_flags": [],
  "refusals_triggered": [],
  "conservative_defaults_applied": []
}
```

## Section 7 — Conservative defaults

When uncertain, prefer the safer (higher-tax / stricter-compliance) outcome and flag. All defaults visible to reviewer in `conservative_defaults_applied`.

**Conservative defaults table**  _(multiple as listed in table)_

| Ambiguity | Conservative default |
| --- | --- |
| Pekerjaan bebas vs usaha unclear | Treat as pekerjaan bebas → progressive PPh; no UMKM (PP 55/2022 art. 56(2)) |
| Turnover near Rp4.8B (Rp4.5B–Rp5.2B) | Assume above threshold → progressive + PKP registration (UU 42/2009 art. 14) |
| UMKM clock unclear | Assume started in earliest documented year incl. PP 23/2018 |
| Residency borderline (~180 days) | Assume non-resident → REFUSE |
| WH-agent status unclear (OP not clearly appointed) | Assume WH obligation exists if any qualifying payment; flag (UU 36/2008 art. 26(4); UU 28/2007 art. 13) |
| Pembukuan vs pencatatan near threshold | Assume pembukuan required (UU 28/2007 art. 28) |
| PTKP unclear | Default TK/0 |
| Coretax access unknown | Assume not active; flag for onboarding |
| Capital vs expense unclear | Capitalise + flag |

## Section 8 — Refusal handling

Refusals fire from the refusal sweep or during inference. Protocol: stop the workflow, state the reason in one sentence, recommend a Konsultan Pajak (Brevet C) or Akuntan Publik if audited financials needed, do not work around.

In-scope refusals: part-year / non-resident; turnover > Rp50B; PT with > 50 employees; PMK 18/2021 qualified-expat 4-year regime; corporate groups with consolidated reporting or transfer-pricing complexity.

Sample: "Stop — you are a part-year tax resident in 2025. I cover full-year Indonesian tax residents only. Part-year residents have split-year sourcing under UU 36/2008 art. 2A and may have treaty issues. You need a Konsultan Pajak."

## Section 9 — Self-checks before handoff

Run all 14 before invoking `id-return-assembly`. Any failure → fix, do not hand off.

1. Refusal sweep used `ask_user_input_v0`, not prose.
2. Residency confirmed (full-year or foreigner > 183d with flag).
3. Entity type set.
4. Pekerjaan bebas flag set (yes / no / mixed).
5. Peredaran bruto recorded in IDR with bucket band.
6. Regime selected with reason traced to (a) pekerjaan bebas, (b) turnover band, (c) UMKM clock (PP 55/2022 art. 59).
7. PKP status set; `pkp_overdue_registration_flag` set if turnover > Rp4.8B and not registered.
8. Employee count set; `id-payroll-pph21` in downstream list if > 0.
9. WH obligations checked; `id-withholding` in list if applicable.
10. Bookkeeping requirement set (pembukuan / pencatatan).
11. PTKP captured (default TK/0).
12. Coretax access captured.
13. All conservative defaults recorded with citation.
14. Reviewer disclaimer present in opening + handoff.

## Section 10 — Final handoff to id-return-assembly

Once gap-filling and self-checks pass, output a short handoff message naming (a) taxpayer + entity + KLU + PTKP + Coretax status, (b) regime selected with the headline computation citation, (c) downstream skills in run-order, (d) skills explicitly not running and why, (e) reviewer reminder (Konsultan Pajak Brevet A/B sign-off via Coretax). Then invoke `id-return-assembly` with the Section 6.2 package.

Example (OP, UMKM Final 0.5%, no employees, not PKP):

> Intake complete. Wira Pratama, OP, KLU 47749, KPP Jakarta Selatan, PTKP K/1, Coretax active. 2025 turnover Rp1.2B, not pekerjaan bebas, UMKM Year 3 of 7 (started 2023). Regime: UMKM Final 0.5% (PP 55/2022); first Rp500m exempt under UU 7/2021 art. 7(2a) → base Rp700m × 0.5% = Rp3.5m before prior monthly remittances. Running: id-bookkeeping (pencatatan), id-pph-final-umkm, id-return-assembly. Not running: id-corporate-tax, indonesia-vat, id-payroll-pph21, id-withholding, id-einvoice-coretax. Needs Konsultan Pajak (Brevet A/B) sign-off before Coretax submission. Handing off now.

## Section 11 — Cross-skill references

**Inputs:** user documents (rekening koran, faktur, bukti potong, prior SPT) + user answers. **Output:** Section 6.2 package consumed by `id-return-assembly`.

Downstream skills (via id-return-assembly):

- `id-bookkeeping` — pembukuan / pencatatan per UU 28/2007 art. 28.
- `id-pph-final-umkm` — PP 55/2022 0.5% final, Rp500m OP band, clock.
- `id-income-tax` — progressive PPh OP (UU 36/2008 art. 17 + UU 7/2021); PTKP; NPPN if elected.
- `id-corporate-tax` — PPh Badan for PT / PT Perorangan / CV / Firma at 22% (UU 36/2008 art. 17(2a) + UU 7/2021).
- `indonesia-vat` — PPN 11% (12% luxury 2025 — TBC) per UU 42/2009 + UU 7/2021.
- `id-einvoice-coretax` — e-Faktur via Coretax DJP.
- `id-payroll-pph21` — monthly PPh 21 + BPJS using TER (PP 58/2023, PMK 168/2023).
- `id-withholding` — PPh 23 / 4(2) / 26.
- `id-formation` — entity choice + PT Perorangan registration.
- `id-tax-optimization` — regime comparison.
- `id-return-assembly` — final orchestrator (SPT, working paper, reviewer brief, action list).

## Section 12 — Sources

Primary statutes and regulations cited (all 2025-effective; reviewer to verify 2025 amendments — notably PPN luxury-goods rate change, TBC):

- **UU 36/2008** Pajak Penghasilan, as amended.
- **UU 28/2007** KUP (General Tax Procedures), as amended.
- **UU 42/2009** PPN dan PPnBM, as amended.
- **UU 7/2021** Harmonisasi Peraturan Perpajakan (HPP) — PTKP, Rp500m UMKM band, PPh rates, PPN 11%.
- **UU 11/2020** Cipta Kerja — art. 109(2) introduces PT Perorangan.
- **PP 55/2022** UMKM Final 0.5%; art. 56–60 (scope, exclusions, 7/4/3-y clock).
- **PP 23/2018** predecessor UMKM regime (still relevant for clock).
- **PP 8/2021** PT Perorangan implementing rules.
- **PP 7/2021** PT Perorangan micro / small criteria.
- **PP 58/2023** TER schedule for PPh 21.
- **PP 34/2017** PPh 4(2) rent of immovable property.
- **PP 9/2022** PPh 4(2) construction services.
- **PMK 168/2023** PPh 21 TER from 1 January 2024.
- **PMK 197/2013** as amended — PKP threshold Rp4.8B.
- **PMK 164/2023** PP 55/2022 implementing rules.
- **PMK 18/2021** qualified expat 4-year regime (out of scope).
- **PMK 136/2023** NPWP-as-NIK from 1 July 2024.
- **PER-24/PJ/2024** Coretax DJP go-live.
- **PER-06/PJ/2024** NPWP-as-NIK procedures.
- **PER-17/PJ/2015** KLU classifications.
- **KMK 360/KMK.03/2024** Coretax effective date.
- **UU 40/2007** Perseroan Terbatas; **UU 24/2011** BPJS; **UU 40/2004** SJSN.

## Change log

**v1.0 (May 2026):** Initial intake skill for the Indonesian freelance / SME workflow. Routes to id-pph-final-umkm, id-income-tax, id-corporate-tax, id-withholding, id-payroll-pph21, indonesia-vat, id-bookkeeping, id-einvoice-coretax, id-formation, id-tax-optimization, id-return-assembly. Reflects UU 7/2021 (HPP), PP 55/2022 (UMKM), UU 11/2020 (PT Perorangan), and Coretax DJP go-live for tax year 2025.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. OpenAccountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified Indonesian tax professional (Konsultan Pajak with Brevet A/B/C, or an Akuntan Publik where audited financials are required) before filing with the DJP via Coretax or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com).

---

*OpenAccountants — open-source accounting skills for AI*
*This output must be reviewed by a qualified professional before filing or acting upon.*
*Latest verified skills: openaccountants.com | Report errors: github.com/openaccountants/openaccountants*

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
