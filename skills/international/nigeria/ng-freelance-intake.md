---
name: ng-freelance-intake
description: ALWAYS USE THIS SKILL when a user asks for help preparing a Nigerian tax return AND mentions freelancing, self-employment, software developer, contractor, sole proprietor, BN business, or private limited company in Nigeria. Trigger on phrases like "prepare my Nigerian tax return", "I'm a freelance developer Lagos", "I have an RC", "I'm self-employed Nigeria", "NTA 2025 small company", "FIRS Tax Pro-Max", "TIN Nigeria", "Lagos LIRS self-assessment", "PITA filing", "CIT 0% small company", "VAT Nigeria registration", or any similar phrasing where the user is a Nigeria-resident self-employed individual, sole proprietor (BN), or small/medium private limited company (RC) founder. This is the REQUIRED entry point for the Nigerian freelance/SME workflow — every downstream skill in the stack (ng-cit, ng-personal-income-tax, ng-paye, ng-statutory-deductions, ng-wht, ng-cgt, ng-vat, ng-payroll, ng-formation, ng-return-assembly) depends on this skill running first. Uses ask_user_input_v0-style structured questions. Nigerian residents only (full-year tax residents and foreigners with > 183 days presence). ALWAYS read this skill first when starting a Nigerian freelance/SME tax workflow.
jurisdiction: NG
domain: international
tax_year: 2025
tier: 2
last_updated: 2026-07-06
---

# ng-freelance-intake

## What this file is

The intake orchestrator for Nigerian-resident self-employed individuals, sole proprietors (Business Name / BN registered with the Corporate Affairs Commission), and small / medium private limited company (RC) founders. Every downstream Nigerian content skill depends on this skill producing a structured intake package first.

Job: (1) confirm taxpayer is in scope, (2) classify the regime (PIT for sole/BN vs CIT 0% small-co vs CIT 20% medium vs CIT 30% large), (3) decide whether the period falls under pre-NTA-2025 rules (CITA / PITA / FA 2019–2023) or under the Nigeria Tax Act 2025 (NTA 2025) effective 1 January 2026, (4) identify downstream skills to run, (5) hand off to `ng-return-assembly`. Outputs addressed to a credentialed Nigerian reviewer (ICAN or ANAN Chartered Accountant, CITN-registered tax practitioner, or legal practitioner where applicable). The reviewer signs off — this skill is not the preparer of record.

## Section 1 — Quick reference: regime decision tree at a glance

```
Nigerian tax resident? -> NO = REFUSE (route to non-resident flow)
       |
Entity?
  +-- Sole trader / BN (no separate legal entity)
  |       -> Personal Income Tax Act (PITA) progressive rates 7-24%
  |          File with State Internal Revenue Service (LIRS / FCT-IRS / SIRS)
  |          Regime: ng-personal-income-tax (always); ng-statutory-deductions (NHF/NHIA/Pension if voluntary)
  |
  +-- Private limited company (RC, "Ltd")
          -> Companies Income Tax Act (CITA) until 31 Dec 2025
             Nigeria Tax Act 2025 (NTA 2025) from 1 Jan 2026
             |
             Turnover band (current FY):
               +-- ≤ N100m AND fixed assets ≤ N250m  (NTA 2025 "small company")
               |     -> CIT 0% (NTA 2025 s.56)  [pre-2026 threshold = N25m under FA 2019]
               |
               +-- N100m – N1bn  (NTA 2025 "medium company")
               |     -> CIT 20%
               |
               +-- > N1bn  (NTA 2025 "large company")
                     -> CIT 30% + 4% Development Levy (NTA 2025)
```

Parallel routing (independent of regime):

- Taxable turnover ≥ N25m trailing-12 → VAT registration mandatory (FA 2019 s.46; NTA 2025 carries this forward) → route `ng-vat`.
- Employees on payroll → route `ng-paye` + `ng-statutory-deductions` + `ng-payroll`.
- Pays Nigerian or foreign suppliers / contractors / rent / royalties → route `ng-wht`.
- Disposed of chargeable assets in the year → route `ng-cgt`.
- Entity unclear (sole / BN / RC / partnership / incorporated trustee) → route `ng-formation`.
- Books not on IFRS for SMEs or FRC-approved framework → flag for bookkeeping review.
- Always final → `ng-return-assembly`.

## Section 2 — Workflow runbook (order of operations)

Strict order. Do not narrate steps.

0. **Step 1** — Opening — one-line greeting + flow summary + reviewer reminder (ICAN/ANAN/CITN), then launch the refusal sweep.
0. **Step 2** — Refusal sweep — single `ask_user_input_v0` call with the 5 questions in Section 5.1.
0. **Step 3** — Document dump — ask user to upload everything at once (bank statements, invoices issued / received, WHT credit notes, prior FIRS / LIRS returns, CAC certificate, TIN slip, payroll schedules). Do not insist on bank statements alone.
0. **Step 4** — Inference pass — parse every document; extract turnover, expenses, WHT suffered, prior tax paid, employee headcount.
0. **Step 5** — Regime classification — apply Section 4 decision tree using inferred turnover + sweep answers + period start/end (pre-2026 vs from-2026).
0. **Step 6** — Confirmation — show inferred summary + proposed regime + downstream-skill list; invite corrections.
0. **Step 7** — Gap filling — `ask_user_input_v0` only for items documents cannot answer (state of residence for PIT, TIN status, Tax Pro-Max access, CAC details).
0. **Step 8** — Handoff — produce Section 6 summary and invoke `ng-return-assembly`.

Operating principles: use `ask_user_input_v0` for multi-choice; free text only for names / TIN / RC number / BVN-linked details. Batch up to 3 related independent questions. Never re-ask documents-visible facts. Spell out Nigerian acronyms on first mention (e.g., "Federal Inland Revenue Service (FIRS)", "Lagos State Internal Revenue Service (LIRS)"). All amounts in NGN.

## Section 3 — Required inputs

Some inferred from documents, the rest gap-filled. All mandatory before handoff.

- **Identity / registration:** legal name, Tax Identification Number (TIN — issued by JTB and now harmonised with FIRS / state IRS), Bank Verification Number (BVN) where relevant for PIT (FA 2019 / FA 2020), CAC registration (BN number for sole proprietors; RC number for limited companies), date of incorporation / registration.
- **State of residence** (PIT only — determines which State IRS administers; LIRS for Lagos, FCT-IRS for Abuja FCT, otherwise the relevant SIRS).
- **Entity:** Sole trader (no CAC registration) / BN (CAC business name) / RC (Ltd or PLC) / Partnership / Incorporated Trustee. RC: SCUML status if applicable.
- **Revenue:** current FY gross turnover, monthly turnover detail, domestic vs export mix (exports zero-rated for VAT under FA 2019 / NTA 2025), assessable profit / loss.
- **Tax history:** prior-year PIT (Form A) or CIT self-assessment, outstanding tax liabilities or refunds, audit history with FIRS / SIRS, any tax clearance certificate (TCC) issues.
- **Operational:** employee count (PAYE obligation), VAT-registered status, FIRS Tax Pro-Max active, pension scheme membership (PRA 2014), NHF / NHIA / ITF / NSITF contribution history.
- **Documents:** bank statements (NGN + USD where relevant), invoices issued and received, WHT credit notes (the most common WHT credit evidence; 5% / 10% standard rates pre-NTA 2025), prior returns (Form A, CIT self-assessment, VAT 002, PAYE Form H1), CAC certificate, TIN slip, payroll register, audited financial statements (RCs only).

## Section 4 — Regime decision tree with thresholds and citations

All thresholds reflect the rules current as at the period being prepared. Many returns being worked in 2026 still cover periods governed by **CITA / PITA / FA 2019–2023**. The **Nigeria Tax Act 2025 (NTA 2025)** is effective 1 January 2026 and applies to financial years beginning on or after that date — earlier periods stay on the prior framework. Section 6 always records which regime stack was applied.

### 4.1 Residency gate — PITA s.2 (individuals); CITA s.13 (companies)

- **Individual resident test** — (i) domiciled in Nigeria during the year, OR (ii) present ≥ 183 days in any 12-month period, OR (iii) employed by the Nigerian government or a Nigerian-resident employer.  _(PITA s.2)_
- **Company resident test** — (i) incorporated in Nigeria (Nigerian company), OR (ii) management and control exercised in Nigeria.  _(CITA s.13)_
- **Non-resident refusal** — Non-residents (without a Nigerian fixed base / significant economic presence under FA 2019 / NTA 2025) → REFUSE and route to a separate non-resident flow.  _(FA 2019; NTA 2025)_

### 4.2 Entity gate — sole trader / BN vs RC

- **Sole trader / BN treatment** — Not a separate legal entity. Owner pays PIT on business profits via self-assessment with the State Internal Revenue Service of residence (LIRS / FCT-IRS / SIRS). Route `ng-personal-income-tax`.
- **RC / PLC treatment** — Separate legal entity. Pays CIT to FIRS. Owner separately pays PIT on salary / dividends. Route `ng-cit`.
- **Partnership treatment** — Profits taxed at partner level under PITA. Route `ng-personal-income-tax` per partner.  _(PITA)_
- **Incorporated Trustee / NGO / cooperative** — Out of scope here — refuse and route to specialist.

### 4.3 CIT band gate — CITA s.40 (pre-NTA 2025) / NTA 2025 (from 1 Jan 2026)

The "small company" definition has shifted twice. Use the rule in force for the period being prepared.

**Small/medium/large company CIT bands by period**  _(CITA s.40; FA 2019 s.16; NTA 2025)_

| Period | Small company definition | Small co. CIT | Medium CIT | Large CIT | Source |
| --- | --- | --- | --- | --- | --- |
| Pre-FA 2019 | n/a | 30% flat | 30% | 30% | CITA s.40 |
| FA 2019 → FY 2025 | Turnover ≤ N25m | 0% | 20% (turnover N25m–N100m) | 30% (> N100m) | FA 2019 s.16 |
| NTA 2025 (FY starting on/after 1 Jan 2026) | Turnover ≤ N100m AND fixed assets ≤ N250m | 0% | 20% (N100m–N1bn) | 30% + 4% Development Levy (> N1bn) | NTA 2025 |

- **Pre-FA 2019** — n/a  _(CITA s.40)_
- **FA 2019 → FY 2025** — Turnover ≤ N25m  _(FA 2019 s.16)_
- **NTA 2025 (FY starting on/after 1 Jan 2026)** — Turnover ≤ N100m AND fixed assets ≤ N250m  _(NTA 2025)_
- **Filing obligation for small companies** — Route `ng-cit` for all RCs. Small companies still file (CIT-nil return) — they do not escape the filing obligation.
- **Minimum tax** — Historically applied at 0.5% of gross turnover where computed tax was lower; NTA 2025 retains a development-levy-style backstop for large companies. Reviewer to confirm for the specific period.

### 4.4 PIT computation gate — PITA Sixth Schedule

- **Progressive PIT rates** — 7% / 11% / 15% / 19% / 21% / 24% on bands stacked from N300,000 to > N3,200,000.  _(PITA Sixth Schedule)_
- **Consolidated Relief Allowance (CRA)** — CRA = max(N200,000, 1% × gross income) + 20% × gross income  _(PITA Sixth Schedule)_
- **Minimum tax (PIT)** — 1% of gross income where computed PIT after CRA and reliefs would be lower  _(PITA Sixth Schedule)_
- **Routing** — Route `ng-personal-income-tax` for the computation; defer state-specific filing portal nuances to that skill.

### 4.5 VAT gate — VATA as amended by FA 2019 / FA 2020 / FA 2023; NTA 2025 carry-forward

- **VAT registration threshold** — N25m taxable turnover in the trailing-12 months. Below threshold = exempt from VAT registration and from VAT charging obligations, but still no input VAT recovery.  _(FA 2019 s.46)_
- **VAT standard rate** — 7.5% standard. Exports zero-rated. Basic food, medical and educational items exempt.  _(FA 2019; VATA First Schedule)_
- **Routing above threshold** — Above threshold or voluntarily registered → route `ng-vat` and ensure FIRS Tax Pro-Max VAT module is active.

### 4.6 PAYE / employer gate — PITA s.81; Operation of PAYE Regulations 2002

- **PAYE withholding and remittance** — Any employees → withhold PAYE monthly and remit to the employee's State Internal Revenue Service by the 10th of the following month. Route `ng-paye` + `ng-payroll`.  _(PITA s.81; Operation of PAYE Regulations 2002)_
- **Statutory deductions** — Pension PRA 2014 8% employee + 10% employer; NHF 2.5%; NHIA where applicable; ITF 1% of payroll for employers with ≥ 5 staff or ≥ N50m turnover; NSITF 1% → route `ng-statutory-deductions`.  _(PRA 2014; NHF Act 1992; NHIA Act 2022; ITF (Amendment) Act 2011; Employee Compensation Act 2010)_

### 4.7 Withholding-tax gate — CITA s.78–82; PITA s.69–73; WHT Regulations 1997 (as amended)

- **WHT obligation trigger** — WHT obligation arises if the taxpayer (RC always; sole trader where appointed agent) pays the categories listed below.  _(CITA s.78–82; PITA s.69–73; WHT Regulations 1997)_
- **Contracts / supplies** — 5% (companies) / 5% (individuals)  _(WHT Regulations 1997)_
- **Professional services / consultancy / management** — 10% / 5%  _(WHT Regulations 1997)_
- **Rent** — 10% (companies and individuals)  _(WHT Regulations 1997)_
- **Royalties / interest / dividends** — 10% (5% under several DTTs)  _(WHT Regulations 1997)_
- **Non-resident payments** — 10% subject to DTT  _(WHT Regulations 1997)_
- **NTA 2025 streamlining and routing** — NTA 2025 streamlines WHT rates and broadens exemptions for small companies. Reviewer to confirm the matrix for the relevant period. Route `ng-wht` whenever the taxpayer has paid or received any of the above.  _(NTA 2025)_

### 4.8 CGT gate — CGTA s.2; FA 2021 (digital assets); NTA 2025

- **CGT rate** — Capital gains on disposal of chargeable assets (land, buildings, shares above the FA 2021 N100m / 100,000-share thresholds, digital assets) → 10% CGT. Route `ng-cgt` if any disposals in the year.  _(CGTA s.2; FA 2021; NTA 2025)_

### 4.9 Filing-channel gate — FIRS Tax Pro-Max; state IRS portals

- **FIRS returns channel** — All FIRS returns (CIT, VAT, WHT, CGT for companies) file through FIRS Tax Pro-Max (mandatory since 2022). Confirm access.  _(FIRS Tax Pro-Max)_
- **State IRS returns channel** — PAYE and PIT returns file through the State IRS portal (LIRS eTax for Lagos; FCT-IRS for Abuja; relevant SIRS otherwise). Confirm access and state of residence.
- **Access missing flag** — If access missing → flag in `open_flags`; reviewer onboards before filing.

## Section 5 — Questions to ask the user

Use `ask_user_input_v0`. Batch where independent.

### 5.1 Refusal sweep (one batched `ask_user_input_v0` call, 5 single-select questions)

- **Q1 Residency (period being prepared):** Full-year Nigerian resident | Foreigner present ≥ 183 days | Part-year | Non-resident with Nigerian-source income only.
- **Q2 Entity:** Sole trader (no CAC) | Business Name / BN (CAC Part B) | Private limited company / RC (Ltd) | Partnership | Incorporated Trustee / NGO | Not sure.
- **Q3 Period being prepared:** Calendar year 2025 (pre-NTA) | FY ending in 2025 (pre-NTA) | FY starting on/after 1 Jan 2026 (NTA 2025) | Multiple periods.
- **Q4 Current-FY turnover (NGN):** ≤ N25m | N25m–N100m | N100m–N1bn | > N1bn | Not sure (infer from docs).
- **Q5 State of residence (PIT only) / state of operation (RC):** Lagos | FCT (Abuja) | Rivers | Other state — please name | Multiple states.

**Routing table**

| Answer | Action |
| --- | --- |
| Q1 full-year | continue |
| Q1 foreigner ≥ 183d | continue; reviewer to verify DTT / significant economic presence rule |
| Q1 part-year | continue with caution; flag split-year sourcing |
| Q1 non-resident with NG-source only | **REFUSE** — separate non-resident workflow needed |
| Q2 sole / BN | route `ng-personal-income-tax`; no `ng-cit` |
| Q2 RC | route `ng-cit`; owner PIT only if salary / dividends drawn |
| Q2 partnership | route `ng-personal-income-tax` per partner; flag for split |
| Q2 Incorporated Trustee | **REFUSE**; route to specialist |
| Q2 not sure | route `ng-formation` first |
| Q3 calendar 2025 / FY ending 2025 | pre-NTA stack: CITA + PITA + FA 2019–2023 |
| Q3 FY starting on/after 1 Jan 2026 | NTA 2025 stack |
| Q3 multiple periods | run each period through the appropriate stack |
| Q4 ≤ N25m | small company (FA 2019) OR below VAT threshold for sole/BN |
| Q4 N25m–N100m | pre-NTA: medium (CIT 20%); NTA 2025: still small (CIT 0%) — period flag critical |
| Q4 N100m–N1bn | pre-NTA: large (CIT 30%); NTA 2025: medium (CIT 20%) |
| Q4 > N1bn | large in both regimes (CIT 30%); NTA 2025 adds 4% Development Levy |
| Q4 not sure | defer to inference |
| Q5 Lagos | PIT filings via LIRS eTax |
| Q5 FCT | PIT filings via FCT-IRS |
| Q5 other state | PIT filings via that SIRS; flag portal access |
| Q5 multiple states | apportion by residence rule (PITA s.2(2)); flag for reviewer |

### 5.2 Secondary batched questions

- **Q6 VAT status:** Registered (issuing VAT invoices) | Not registered | Not sure.
- **Q7 Employees in the period:** None | 1–4 | 5–20 | > 20.
- **Q8 TIN status:** Have FIRS / JTB TIN (active) | Have CAC but no TIN | No registration yet.
- **Q9 Pension / statutory schemes:** All current (PenCom-compliant + NHF) | Some current | None.

**Routing table**

| Answer | Action |
| --- | --- |
| Q6 registered | route `ng-vat` |
| Q6 not registered but turnover > N25m | flag **VAT registration overdue**; route `ng-vat`; reviewer to register |
| Q6 not sure | defer to inference; default conservatively to "registration required" if turnover > N25m |
| Q7 ≥ 1 employee | route `ng-paye` + `ng-statutory-deductions` + `ng-payroll` |
| Q7 ≥ 5 employees | additionally flag ITF (1% of payroll) and NSITF (1%) obligations |
| Q8 no TIN | route to `ng-formation` onboarding fallback (Section 8); cannot file without TIN |
| Q9 some / none | route `ng-statutory-deductions` to remediate; flag for reviewer |

### 5.3 WHT and CGT questions

- **Q10 In the period did you pay Nigerian suppliers for contracts, professional services, rent, or non-resident suppliers?** Yes (contracts) | Yes (services) | Yes (rent) | Yes (non-resident) | Multiple | No.
- **Q11 Did you dispose of land, buildings, shares above the FA 2021 thresholds, or digital assets in the period?** Yes | No | Not sure.

Any "Yes" on Q10 → route `ng-wht`. Reviewer confirms whether sole trader is an appointed WHT agent (CITA s.78–82 applies automatically to companies). Q11 yes → route `ng-cgt`.

### 5.4 Tax Pro-Max / state portal access

- **Q12 FIRS Tax Pro-Max access?** Yes (active) | No (never logged in) | Started but hit issues.
- **Q13 State IRS portal access (LIRS eTax / FCT-IRS / SIRS)?** Yes | No | N/A (RC with no employees and no PIT due).

"No" or "issues" → flag in `open_flags`. Tax Pro-Max is the only FIRS filing channel; the relevant state portal is the only PAYE / PIT channel.

### 6.1 Human-readable confirmation (shown to user)

```
INTAKE SUMMARY — Nigeria — Period: [CY2025 | FY ending YYYY-MM | FY starting 2026-01-01]

Taxpayer: [Name] | TIN: [12-digit] | CAC: [BN/RC number]
State of residence (PIT): [Lagos | FCT | …] | Entity: [Sole | BN | RC | Partnership]
Regime stack: [pre-NTA — CITA/PITA/FA 2019-2023 | NTA 2025]
FIRS Tax Pro-Max: [active | onboarding needed]
State IRS portal: [active | onboarding needed | N/A]

REGIME: [PIT progressive | CIT 0% small | CIT 20% medium | CIT 30% large + 4% Dev Levy]
  - Period turnover: N [X]
  - Entity size band: [small | medium | large]
  - VAT: [registered | below threshold | registration overdue]
  - Employees: [count]
  - WHT exposure: [paying | receiving | both | none]
  - CGT disposals: [yes | no]

DOWNSTREAM SKILLS:
  ng-personal-income-tax [if sole/BN/partnership],
  ng-cit [if RC], ng-vat [if registered or > N25m],
  ng-paye [if employees], ng-statutory-deductions [if employees],
  ng-payroll [if employees], ng-wht [if applicable],
  ng-cgt [if disposals], ng-formation [if entity unclear],
  ng-return-assembly [always last].

OPEN FLAGS, REFUSALS TRIGGERED, CONSERVATIVE DEFAULTS APPLIED — listed below.

Confirm or correct anything above.
```

### 6.2 Structured intake package (internal JSON for ng-return-assembly)

```json
{
  "jurisdiction": "NG",
  "tax_year": 2025,
  "period": {
    "start": "YYYY-MM-DD",
    "end": "YYYY-MM-DD",
    "regime_stack": "pre_nta_2025|nta_2025"
  },
  "taxpayer": {
    "name": "", "tin": "", "cac_number": "",
    "state_of_residence": "lagos|fct|rivers|other",
    "entity_type": "sole|bn|rc|partnership|incorporated_trustee",
    "tax_pro_max_active": false,
    "state_irs_portal_active": false
  },
  "regime": {
    "selected": "pit_progressive|cit_0_small|cit_20_medium|cit_30_large",
    "period_turnover_ngn": 0,
    "fixed_assets_ngn": 0,
    "size_band": "small|medium|large",
    "development_levy_applicable": false
  },
  "vat": {
    "registered": false,
    "registration_overdue_flag": false,
    "trailing12_turnover_at_threshold": 0
  },
  "employment": {
    "has_employees": false,
    "employee_count": 0,
    "itf_applicable": false,
    "nsitf_applicable": false,
    "pension_compliant": false,
    "nhf_compliant": false
  },
  "withholding": {
    "paid_contracts": false,
    "paid_services": false,
    "paid_rent": false,
    "paid_non_resident": false,
    "is_wht_agent": false
  },
  "cgt": {
    "had_disposals": false
  },
  "documents_received": [],
  "downstream_skills_to_load": [],
  "open_flags": [],
  "refusals_triggered": [],
  "conservative_defaults_applied": []
}
```

## Section 7 — NTA 2025 transitional handling (pre-2026 vs from-2026)

The Nigeria Tax Act 2025 is effective for financial years beginning on or after 1 January 2026. Earlier periods stay on the prior framework. Always record which regime stack applies and apply rules consistently within a single period.

**Pre-NTA vs NTA 2025 comparison**  _(NTA 2025 (consolidated))_

| Item | Pre-NTA 2025 (FY ending ≤ Dec 2025) | NTA 2025 (FY starting ≥ Jan 2026) |
| --- | --- | --- |
| Statutes | CITA, PITA, VATA, CGTA, FA 2019 / 2020 / 2021 / 2023 | NTA 2025 (consolidated) |
| Small co. threshold | Turnover ≤ N25m (FA 2019) | Turnover ≤ N100m AND fixed assets ≤ N250m |
| Small co. CIT | 0% | 0% |
| Medium co. band | N25m–N100m | N100m–N1bn |
| Medium co. CIT | 20% | 20% |
| Large co. CIT | 30% | 30% |
| Development Levy | n/a (Tertiary Education Tax / NITDA / NASENI / police levy as separate items) | 4% consolidated levy on large companies |
| Minimum tax | 0.5% of turnover where applicable | NTA 2025 simplifies; reviewer to confirm |
| WHT rates | WHT Regulations 1997 + FA amendments | NTA 2025 simplifies and exempts small companies |
| VAT | VATA + FA 2019 (7.5%) | NTA 2025 carries 7.5% forward (subject to amendment) |
| Filing channel (federal) | FIRS Tax Pro-Max | FIRS Tax Pro-Max |
| Filing channel (state PIT/PAYE) | State IRS portal | State IRS portal |

- **Mixed periods handling** — Mixed periods (e.g., FY ending 31 March 2026 straddling 1 Jan 2026 cutover) are handled by `ng-return-assembly`, not by this intake — flag the straddle in `open_flags` and let the assembly skill do the apportionment under NTA 2025 transitional provisions.

## Section 8 — State-level considerations (LIRS vs other SIRS)

PIT and PAYE are state taxes under PITA. The state where the taxpayer is resident (PIT) or where the employee resides (PAYE) administers and collects.

**State administering authorities table**

| State | Administering authority | Portal | Notes |
| --- | --- | --- | --- |
| Lagos | Lagos State Internal Revenue Service (LIRS) | eTax (etax.lirs.net) | Most developed state portal; aggressive enforcement; tax audit cycle ~2 years; consent letters required for inter-state moves |
| Federal Capital Territory (Abuja) | FCT Internal Revenue Service (FCT-IRS) | FCT-IRS e-portal | FCT residents file here, not FIRS |
| Rivers | Rivers State IRS | RIRS portal |  |
| Kano / Kaduna / Oyo / others | State IRS of residence | Varies | Some states still accept paper filings; flag for reviewer |
| Cross-border residence | Apportionment rule (PITA s.2(2)) | n/a | Tax residence determined by principal place of residence on 1 January of the year |

- For sole traders / BN, PIT is filed where the individual is resident, not where the business is registered or operates.
- For RC employees, PAYE is remitted to each employee's state of residence — a Lagos-based RC with staff in Ogun must remit Ogun PAYE to Ogun SIRS.
- TCC (Tax Clearance Certificate) is issued by the relevant state IRS for PIT and by FIRS for CIT.

If the state is anything other than Lagos / FCT / Rivers, flag for reviewer — portal availability and procedural rules vary widely.

## Section 9 — Onboarding fallback (user has no TIN yet)

If Q8 returns "No registration yet" or no TIN is found in documents, stop the regime-classification flow and run this fallback before any further work:

1. Confirm entity intent: sole / BN / RC. If unsure, route `ng-formation` first.
2. CAC registration (if BN or RC): the user must register the business with the Corporate Affairs Commission at cac.gov.ng before a TIN can be issued. BN takes ~2–5 working days; RC takes ~5–10 working days.
3. TIN issuance:
   - RC: TIN is now auto-issued by FIRS upon CAC incorporation (Joint Tax Board harmonisation, 2021 onward). Confirm via Tax Pro-Max lookup.
   - Sole / BN / individual: Apply for TIN via JTB / FIRS / state IRS. Individuals can use BVN-linked auto-issuance where supported. Lagos residents: LIRS issues Tax ID on first eTax registration.
4. Tax Pro-Max / state portal onboarding: create account, link TIN, link bank account for direct debit.
5. VAT registration (if turnover > N25m or voluntary): separate Tax Pro-Max workflow once TIN is active.
6. PAYE registration (if employees): register with the relevant state IRS as an employer; obtain Employer Tax ID.

Until TIN is active, no return can be filed. Flag `onboarding_required` in `open_flags` and refer the user to a CITN-registered tax practitioner or ICAN/ANAN Chartered Accountant to walk through CAC + JTB / FIRS / state IRS registration.

## Section 10 — Conservative defaults

When uncertain, prefer the safer (higher-tax / stricter-compliance) outcome and flag. All defaults visible to reviewer in `conservative_defaults_applied`.

**Conservative defaults table**

| Ambiguity | Conservative default |
| --- | --- |
| Period straddles 1 Jan 2026 cutover | Apply pre-NTA stack to pre-cutover portion, NTA 2025 to post-cutover; flag for `ng-return-assembly` |
| Turnover near N25m (FA 2019) or N100m (NTA 2025) threshold | Assume above threshold → medium band + VAT registration required |
| Entity unclear (sole vs BN vs RC) | Treat as sole trader for PIT default; flag `ng-formation` |
| Residency borderline (~180 days) | Assume non-resident → REFUSE for individual returns |
| WHT-agent status unclear (sole trader not clearly appointed) | Assume WHT obligation exists for any qualifying payment; flag |
| Pension / NHF / NHIA compliance unclear | Assume non-compliant → flag remediation; defer to `ng-statutory-deductions` |
| Minimum tax (PIT 1% / CIT 0.5%) borderline | Apply minimum tax; reviewer can release if computed tax exceeds it |
| State of residence unclear | Default Lagos (LIRS) only if documents support; otherwise ask — never guess |
| Tax Pro-Max access unknown | Assume not active; flag for onboarding |
| Capital vs expense unclear | Capitalise + flag (capital allowance treatment) |
| Foreign-currency invoice without CBN rate | Use CBN official rate on invoice date; flag if no rate available |

## Section 11 — Refusal handling

Refusals fire from the refusal sweep or during inference. Protocol: stop the workflow, state the reason in one sentence, recommend a CITN-registered tax practitioner or ICAN / ANAN Chartered Accountant (or an audit firm where audited financials are needed), do not work around.

- **In-scope refusals** — - Non-resident with Nigerian-source income only (separate flow needed). - Part-year residence with split sourcing complexity beyond a single relocation. - Incorporated Trustees / NGOs / cooperatives / Public Benefit Organisations. - Large companies with consolidated reporting, transfer-pricing audit exposure (TP Regulations 2018), or country-by-country reporting obligations. - RCs requiring audited financial statements (CAMA 2020 s.402) where audit is not yet complete — refuse until audit signed. - Oil and gas companies (PPTA / NUPRC regime) — out of scope. - Free Zone Enterprises under NEPZA / OGFZA — out of scope. - Pioneer-status companies during pioneer period (Industrial Development (Income Tax Relief) Act) — refuse; specialist territory.  _(CAMA 2020 s.402; TP Regulations 2018; PPTA; NEPZA; OGFZA; Industrial Development (Income Tax Relief) Act)_

Sample: "Stop — your RC's financial statements have not yet been audited. CAMA 2020 s.402 requires audited accounts for the CIT filing, and FIRS will reject a Tax Pro-Max submission without them. You need an ICAN-registered auditor to sign off before I can prepare the return."

## Section 12 — Self-checks before handoff

Run all 15 before invoking `ng-return-assembly`. Any failure → fix, do not hand off.

1. Refusal sweep used `ask_user_input_v0`, not prose.
2. Residency confirmed (full-year, ≥ 183d foreigner with flag, or refused).
3. Entity type set (sole / BN / RC / partnership).
4. Regime stack chosen (pre-NTA vs NTA 2025) and recorded.
5. Period turnover recorded in NGN with bucket band.
6. Regime selected with reason traced to (a) entity, (b) turnover, (c) period.
7. VAT status set; `registration_overdue_flag` set if turnover > N25m and not registered.
8. Employee count set; `ng-paye` + `ng-statutory-deductions` + `ng-payroll` in downstream list if > 0.
9. ITF / NSITF flags set if ≥ 5 employees or ≥ N50m payroll.
10. WHT exposure checked; `ng-wht` in list if applicable.
11. CGT disposals checked; `ng-cgt` in list if applicable.
12. State of residence captured (PIT path) or state of operation (RC path).
13. TIN status captured; onboarding fallback triggered if absent.
14. Tax Pro-Max + state IRS portal access captured.
15. Reviewer disclaimer present in opening + handoff (CITN / ICAN / ANAN sign-off).

## Section 13 — Final handoff to ng-return-assembly

Once gap-filling and self-checks pass, output a short handoff message naming (a) taxpayer + entity + state + TIN + Tax Pro-Max status, (b) regime stack + regime selected with the headline computation citation, (c) downstream skills in run-order, (d) skills explicitly not running and why, (e) reviewer reminder. Then invoke `ng-return-assembly` with the Section 6.2 package.

Example (sole trader, Lagos, FY 2025 pre-NTA, no employees, below VAT threshold):

> Intake complete. Adebayo Okonkwo, sole trader, Lagos resident, TIN active, LIRS eTax onboarded, no CAC (sole, not BN). Period: CY 2025, pre-NTA stack. Turnover N18m. Regime: PIT progressive (PITA Sixth Schedule); CRA = max(N200k, 1% × gross) + 20% × gross; minimum tax 1% if computed PIT lower. Running: ng-personal-income-tax, ng-wht (Q10 yes on services received), ng-return-assembly. Not running: ng-cit (sole trader), ng-vat (below N25m), ng-paye / ng-statutory-deductions / ng-payroll (no employees), ng-cgt (no disposals). Needs CITN-registered tax practitioner sign-off before LIRS eTax submission. Handing off now.

Example (RC, FY ending 31 Dec 2026, NTA 2025 stack, 8 employees, above VAT threshold):

> Intake complete. Pomelo Tech Ltd, RC 1234567, registered office Lagos, TIN active, Tax Pro-Max active. Period: FY ending 31 Dec 2026, NTA 2025 stack. Turnover N420m, fixed assets N80m → medium company. Regime: CIT 20% (NTA 2025). Running: ng-cit, ng-vat (registered), ng-paye + ng-statutory-deductions + ng-payroll (8 employees; ITF applicable as headcount ≥ 5), ng-wht (paying both contractors and rent), ng-return-assembly. Not running: ng-personal-income-tax (separate workflow for owner salary), ng-cgt (no disposals). Needs ICAN-registered Chartered Accountant sign-off and audited financials (CAMA 2020 s.402) before Tax Pro-Max submission. Handing off now.

## Section 14 — Cross-skill references

Inputs: user documents (bank statements, invoices, WHT credit notes, prior returns, CAC certificate, TIN slip, payroll register) + user answers. Output: Section 6.2 package consumed by `ng-return-assembly`.

Downstream skills (via ng-return-assembly):

- `ng-personal-income-tax` — PIT progressive 7–24%, CRA, 1% minimum tax (PITA Sixth Schedule).
- `ng-cit` — Companies Income Tax: 0% / 20% / 30% bands + 4% Development Levy for large companies (CITA pre-2026; NTA 2025 from 2026).
- `ng-paye` — Operation of PAYE Regulations 2002; monthly remittance to state IRS by the 10th.
- `ng-statutory-deductions` — Pension (PRA 2014), NHF, NHIA, ITF, NSITF.
- `ng-payroll` — payslip generation; gross-to-net; employer cost summary.
- `ng-wht` — Withholding tax matrix (CITA s.78–82; PITA s.69–73; WHT Regulations 1997; NTA 2025 simplifications).
- `ng-cgt` — Capital Gains Tax 10% (CGTA; FA 2021 digital assets and N100m share threshold).
- `ng-vat` — VAT 7.5% standard, zero-rate exports, exemptions (VATA + FA 2019 amendments).
- `ng-formation` — Entity choice + CAC / TIN onboarding.
- `ng-return-assembly` — final orchestrator (returns + working paper + reviewer brief + action list).

## Section 15 — Sources

Primary statutes and regulations cited (reviewer to verify the exact version in force for the period being prepared):

- Personal Income Tax Act (PITA), Cap. P8 LFN 2004, as amended by Finance Acts 2019–2023.
- Companies Income Tax Act (CITA), Cap. C21 LFN 2004, as amended.
- Value Added Tax Act (VATA), Cap. V1 LFN 2004, as amended by Finance Acts 2019, 2020, 2021, 2023.
- Capital Gains Tax Act (CGTA), Cap. C1 LFN 2004, as amended; FA 2021 (digital assets; share-disposal threshold).
- Finance Act 2019 — small company definition (turnover ≤ N25m); VAT rate to 7.5%; VAT registration threshold N25m.
- Finance Act 2020 / 2021 / 2023 — incremental amendments.
- Nigeria Tax Act 2025 (NTA 2025) — consolidated framework effective for financial years beginning on or after 1 January 2026; new small / medium / large bands (N100m / N1bn); 4% Development Levy for large companies; WHT simplification.
- Companies and Allied Matters Act (CAMA) 2020 — entity types; audit requirements (s.402); CAC procedures.
- Pension Reform Act (PRA) 2014 — employer 10% + employee 8% pension contributions.
- National Housing Fund Act 1992 — NHF 2.5% employee deduction.
- National Health Insurance Authority Act 2022 — NHIA, replacing NHIS Act 1999.
- Industrial Training Fund (Amendment) Act 2011 — ITF 1% of payroll where headcount ≥ 5 or turnover ≥ N50m.
- Employee Compensation Act 2010 — NSITF 1% of payroll.
- Operation of PAYE Regulations 2002.
- Withholding Tax Regulations 1997 (as amended); NTA 2025 transitional rules.
- Transfer Pricing Regulations 2018 (out of scope here).
- Joint Tax Board (JTB) TIN harmonisation circulars (2021 onward).
- FIRS Tax Pro-Max — mandatory federal filing channel since 2022.
- State IRS portals — LIRS eTax, FCT-IRS, RIRS, etc.

## Change log

v1.0 (May 2026): Initial intake skill for the Nigerian freelance / SME workflow. Routes to ng-personal-income-tax, ng-cit, ng-paye, ng-statutory-deductions, ng-payroll, ng-wht, ng-cgt, ng-vat, ng-formation, ng-return-assembly. Covers both the pre-NTA stack (CITA / PITA / FA 2019–2023) for periods ending on or before 31 December 2025 and the Nigeria Tax Act 2025 stack for financial years beginning on or after 1 January 2026, with explicit handling of the small / medium / large CIT band shift (N25m / N100m thresholds → N100m / N1bn thresholds).

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. OpenAccountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified Nigerian professional — a CITN-registered tax practitioner, an ICAN or ANAN Chartered Accountant, or a legal practitioner where applicable, and an external auditor where CAMA 2020 s.402 requires audited financial statements — before filing with FIRS via Tax Pro-Max or with the relevant State Internal Revenue Service, or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com).

---

*OpenAccountants — open-source accounting skills for AI*
*This output must be reviewed by a qualified professional before filing or acting upon.*
*Latest verified skills: openaccountants.com | Report errors: github.com/openaccountants/openaccountants*

## Talk to a verified accountant

This skill is a tool, not an engagement. Every taxpayer's situation is
different, and the rules in the skill may not match your specific facts.

To speak with one of the licensed accountants who verifies skills for your
jurisdiction — no liability on either side until you and the accountant sign
a formal engagement letter — book a free 30-minute call:

→ [Book a call](https://calendly.com/openaccountants-info/30min)

We'll route you to the named verifier covering your country or state. You can
also see the full list of verified accountants at
[openaccountants.com/network](https://openaccountants.com/network).
