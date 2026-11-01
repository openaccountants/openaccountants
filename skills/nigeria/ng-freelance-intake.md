---
name: ng-freelance-intake
description: ALWAYS USE THIS SKILL when a user asks for help preparing a Nigerian tax return AND mentions freelancing, self-employment, software developer, contractor, sole proprietor, BN business, or private limited company in Nigeria. Trigger on phrases like "prepare my Nigerian tax return", "I'm a freelance developer Lagos", "I have an RC", "I'm self-employed Nigeria", "NTA 2025 small company", "FIRS Tax Pro-Max", "TIN Nigeria", "Lagos LIRS self-assessment", "PITA filing", "CIT 0% small company", "VAT Nigeria registration", or any similar phrasing where the user is a Nigeria-resident self-employed individual, sole proprietor (BN), or small/medium private limited company (RC) founder. This is the REQUIRED entry point for the Nigerian freelance/SME workflow; every downstream skill in the stack (ng-cit, ng-personal-income-tax, ng-paye, ng-statutory-deductions, ng-wht, ng-cgt, ng-vat, ng-payroll, ng-formation, ng-return-assembly) depends on this skill running first. Uses ask_user_input_v0-style structured questions. Nigerian residents only (full-year tax residents and foreigners with > 183 days presence). ALWAYS read this skill first when starting a Nigerian freelance/SME tax workflow.
version: 1.1
jurisdiction: NG
tax_year: 2026
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# NG Freelance Intake

Tax year 2026. Unofficial-source warning: see Status columns and "Not yet confirmed".

## Who this applies to

Nigerian-resident self-employed people, business names and small or larger private companies. This is the entry point for the Nigerian workflow. All NTA figures below are read from an unofficial copy and stay marked unverified until confirmed in an official document. "NTA" means the Nigeria Tax Act 2025, in force 1 January 2026 (commencement line of the Act).

Period rule: 2026 and later use the NTA; 2025 and earlier use the repealed Acts (s.195).

## Rates, bands and thresholds

| Item | Rate or amount | Tax year | Law | Status and link |
|---|---|---|---|---|
| Small company: gross turnover NGN 100,000,000 or less a year and total fixed assets not over NGN 250,000,000 | 0% company tax, no development levy | 2026 | NTA ss.56(a), 59(1), definition of small company | unverified: unofficial copy only, https://media.premiumtimesng.com/wp-content/files/2026/01/Final-Approved-Copy-for-Print-NIGERIA-TAX-ACT-2025.pdf |
| Any other company | 30%; falls to 25% only from a date set by presidential order | 2026 | NTA s.56(b) and proviso | unverified: unofficial copy only, https://media.premiumtimesng.com/wp-content/files/2026/01/Final-Approved-Copy-for-Print-NIGERIA-TAX-ACT-2025.pdf |
| Development levy, companies other than small and non-resident companies | 4% of assessable profits | 2026 | NTA s.59(1) | unverified: unofficial copy only, https://media.premiumtimesng.com/wp-content/files/2026/01/Final-Approved-Copy-for-Print-NIGERIA-TAX-ACT-2025.pdf |
| Minimum effective tax rate: MNE group turnover at least £750 million as printed in the copy read, or company turnover NGN 50,000,000,000 and above | 15% of net income | 2026 | NTA s.57 | unverified: unofficial copy only, https://media.premiumtimesng.com/wp-content/files/2026/01/Final-Approved-Copy-for-Print-NIGERIA-TAX-ACT-2025.pdf |
| Standard rate on taxable supplies | 7.5% | 2026 | NTA s.147 | unverified: unofficial copy only, https://media.premiumtimesng.com/wp-content/files/2026/01/Final-Approved-Copy-for-Print-NIGERIA-TAX-ACT-2025.pdf |
| Band 1, first NGN 800,000 | 0% | 2026 | NTA s.58, Fourth Schedule (a) | unverified: unofficial copy only, https://media.premiumtimesng.com/wp-content/files/2026/01/Final-Approved-Copy-for-Print-NIGERIA-TAX-ACT-2025.pdf |
| Band 2, next NGN 2,200,000 | 15% | 2026 | Fourth Schedule (b) | unverified: unofficial copy only, https://media.premiumtimesng.com/wp-content/files/2026/01/Final-Approved-Copy-for-Print-NIGERIA-TAX-ACT-2025.pdf |
| Band 3, next NGN 9,000,000 | 18% | 2026 | Fourth Schedule (c) | unverified: unofficial copy only, https://media.premiumtimesng.com/wp-content/files/2026/01/Final-Approved-Copy-for-Print-NIGERIA-TAX-ACT-2025.pdf |
| Band 4, next NGN 13,000,000 | 21% | 2026 | Fourth Schedule (d) | unverified: unofficial copy only, https://media.premiumtimesng.com/wp-content/files/2026/01/Final-Approved-Copy-for-Print-NIGERIA-TAX-ACT-2025.pdf |
| Band 5, next NGN 25,000,000 | 23% | 2026 | Fourth Schedule (e) | unverified: unofficial copy only, https://media.premiumtimesng.com/wp-content/files/2026/01/Final-Approved-Copy-for-Print-NIGERIA-TAX-ACT-2025.pdf |
| Band 6, above NGN 50,000,000 | 25% | 2026 | Fourth Schedule (f) | unverified: unofficial copy only, https://media.premiumtimesng.com/wp-content/files/2026/01/Final-Approved-Copy-for-Print-NIGERIA-TAX-ACT-2025.pdf |

Regime from 2026: sole trader or business name, personal bands; small company, 0%; every other company, 30% plus 4% levy. There is no medium band in s.56.

## The base

Individuals: [ng-income-tax](ng-income-tax.md). VAT: [nigeria-vat](nigeria-vat.md). Companies: total profits, with the small test applied on both turnover and fixed assets.

## Deadlines and filing

Filing dates sit in the Nigeria Tax Administration Act 2025, not read. The runbook below is the working order. References to FIRS mean the Nigeria Revenue Service from 2026; confirm the current portal with the client.

## Penalties and interest

Set by the Nigeria Tax Administration Act 2025, not read.

## Cross-border points

Non-residents go to a separate flow. Resident test: see the definition in [ng-income-tax](ng-income-tax.md); it is wider than the old test and one limb is enough.

## Intake workflow

The questions and handoff follow, corrected to the NTA where they differed.



#### What this file is

The intake orchestrator for Nigerian-resident self-employed individuals, sole proprietors (Business Name / BN registered with the Corporate Affairs Commission), and private limited company (RC) founders. Every downstream Nigerian content skill depends on this skill producing a structured intake package first.

Job: (1) confirm taxpayer is in scope, (2) classify the regime (PIT for sole/BN vs CIT 0% small company vs CIT 30% any other company), (3) decide whether the period falls under pre-NTA-2025 rules (CITA / PITA / FA 2019-2023) or under the Nigeria Tax Act 2025 (NTA 2025) effective 1 January 2026, (4) identify downstream skills to run, (5) hand off to `ng-return-assembly`. Outputs addressed to a credentialed Nigerian reviewer (ICAN or ANAN Chartered Accountant, CITN-registered tax practitioner, or legal practitioner where applicable). The reviewer signs off: this skill is not the preparer of record.

#### Section 1: Quick reference: regime decision tree at a glance

```
Nigerian tax resident? -> NO = REFUSE (route to non-resident flow)
       |
Entity?
  +-- Sole trader / BN (no separate legal entity)
  |       -> Pre-2026: PITA 7-24%. From 2026: NTA Fourth Schedule 0-25%
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
               |
               +-- over N100m or fixed assets over N250m (NTA 2025 other company)
                     -> CIT 30% + 4% Development Levy (NTA 2025)
```

Parallel routing (independent of regime):

- Pre-2026 only: taxable turnover ≥ N25m trailing-12 → VAT registration mandatory (FA 2019 s.46). From 2026 no threshold figure appears in the NTA text read: ask whether the client makes taxable supplies → route `ng-vat`.
- Employees on payroll → route `ng-paye` + `ng-statutory-deductions` + `ng-payroll`.
- Pays Nigerian or foreign suppliers / contractors / rent / royalties → route `ng-wht`.
- Disposed of chargeable assets in the year → route `ng-cgt`.
- Entity unclear (sole / BN / RC / partnership / incorporated trustee) → route `ng-formation`.
- Books not on IFRS for SMEs or FRC-approved framework → flag for bookkeeping review.
- Always final → `ng-return-assembly`.

#### Section 2: Workflow runbook (order of operations)

Strict order. Do not narrate steps.

0. **Step 1**: Opening: one-line greeting + flow summary + reviewer reminder (ICAN/ANAN/CITN), then launch the refusal sweep.
0. **Step 2**: Refusal sweep: single `ask_user_input_v0` call with the 5 questions in Section 5.1.
0. **Step 3**: Document dump: ask user to upload everything at once (bank statements, invoices issued / received, WHT credit notes, prior FIRS / LIRS returns, CAC certificate, TIN slip, payroll schedules). Do not insist on bank statements alone.
0. **Step 4**: Inference pass: parse every document; extract turnover, expenses, WHT suffered, prior tax paid, employee headcount.
0. **Step 5**: Regime classification: apply Section 4 decision tree using inferred turnover + sweep answers + period start/end (pre-2026 vs from-2026).
0. **Step 6**: Confirmation: show inferred summary + proposed regime + downstream-skill list; invite corrections.
0. **Step 7**: Gap filling: `ask_user_input_v0` only for items documents cannot answer (state of residence for PIT, TIN status, Tax Pro-Max access, CAC details).
0. **Step 8**: Handoff: produce Section 6 summary and invoke `ng-return-assembly`.

Operating principles: use `ask_user_input_v0` for multi-choice; free text only for names / TIN / RC number / BVN-linked details. Batch up to 3 related independent questions. Never re-ask documents-visible facts. Spell out Nigerian acronyms on first mention (e.g., "Federal Inland Revenue Service (FIRS)", "Lagos State Internal Revenue Service (LIRS)"). All amounts in NGN.

#### Section 3: Required inputs

Some inferred from documents, the rest gap-filled. All mandatory before handoff.

- **Identity / registration:** legal name, Tax Identification Number (TIN: issued by JTB and now harmonised with FIRS / state IRS), Bank Verification Number (BVN) where relevant for PIT (FA 2019 / FA 2020), CAC registration (BN number for sole proprietors; RC number for limited companies), date of incorporation / registration.
- **State of residence** (PIT only: determines which State IRS administers; LIRS for Lagos, FCT-IRS for Abuja FCT, otherwise the relevant SIRS).
- **Entity:** Sole trader (no CAC registration) / BN (CAC business name) / RC (Ltd or PLC) / Partnership / Incorporated Trustee. RC: SCUML status if applicable.
- **Revenue:** current FY gross turnover, monthly turnover detail, domestic vs export mix (exports zero-rated for VAT under FA 2019 / NTA 2025), assessable profit / loss.
- **Tax history:** prior-year PIT (Form A) or CIT self-assessment, outstanding tax liabilities or refunds, audit history with FIRS / SIRS, any tax clearance certificate (TCC) issues.
- **Operational:** employee count (PAYE obligation), VAT-registered status, FIRS Tax Pro-Max active, pension scheme membership (PRA 2014), NHF / NHIA / ITF / NSITF contribution history.
- **Documents:** bank statements (NGN + USD where relevant), invoices issued and received, WHT credit notes (the most common WHT credit evidence; 5% / 10% standard rates pre-NTA 2025), prior returns (Form A, CIT self-assessment, VAT 002, PAYE Form H1), CAC certificate, TIN slip, payroll register, audited financial statements (RCs only).

#### Section 4: Regime decision tree with thresholds and citations

All thresholds reflect the rules current as at the period being prepared. Many returns being worked in 2026 still cover periods governed by **CITA / PITA / FA 2019-2023**. The **Nigeria Tax Act 2025 (NTA 2025)** commences 1 January 2026 and repeals those Acts from then (s.195); calendar 2025 and earlier stay on the prior framework. A financial year straddling that date goes to the reviewer. Section 6 always records which regime stack was applied.

##### 4.1 Residency gate: NTA definitions from 2026; PITA s.2 and CITA s.13 for pre-2026

- **From 2026, individual**: any one limb of the NTA definition of resident individual: domiciled, permanent place available, habitual abode, substantial economic and immediate family ties, 183 days in a 12-month period, or Nigerian diplomat abroad.
- **From 2026, company**: a Nigerian company, meaning formed in Nigeria or with central or effective place of management or control in Nigeria (NTA definitions).

- **Pre-2026 individual resident test**: (i) domiciled in Nigeria during the year, OR (ii) present ≥ 183 days in any 12-month period, OR (iii) employed by the Nigerian government or a Nigerian-resident employer.  _(PITA s.2)_
- **Pre-2026 company resident test**: (i) incorporated in Nigeria (Nigerian company), OR (ii) management and control exercised in Nigeria.  _(CITA s.13)_
- **Non-resident refusal**: Non-residents (without a Nigerian fixed base / significant economic presence under FA 2019 / NTA 2025) → REFUSE and route to a separate non-resident flow.  _(FA 2019; NTA 2025)_

##### 4.2 Entity gate: sole trader / BN vs RC

- **Sole trader / BN treatment**: Not a separate legal entity. Owner pays PIT on business profits via self-assessment with the State Internal Revenue Service of residence (LIRS / FCT-IRS / SIRS). Route `ng-personal-income-tax`.
- **RC / PLC treatment**: Separate legal entity. Pays CIT to FIRS. Owner separately pays PIT on salary / dividends. Route `ng-cit`.
- **Partnership treatment**: Profits taxed at partner level under PITA. Route `ng-personal-income-tax` per partner.  _(PITA)_
- **Incorporated Trustee / NGO / cooperative**: Out of scope here: refuse and route to specialist.

##### 4.3 CIT rate gate: CITA s.40 (pre-NTA 2025) / NTA ss.56, 59 (from 1 Jan 2026)

The "small company" definition has shifted twice. Use the rule in force for the period being prepared.

**Small/medium/large company CIT bands by period**  _(CITA s.40; FA 2019 s.16; NTA 2025)_

| Period | Small company definition | Small co. CIT | Medium CIT | Large CIT | Source | Status |
| --- | --- | --- | --- | --- | --- | --- |
| Pre-FA 2019 | n/a | 30% flat | 30% | 30% | CITA s.40 | unverified, earlier text not re-read |
| FA 2019 → FY 2025 | Turnover ≤ N25m | 0% | 20% (turnover N25m-N100m) | 30% (> N100m) | FA 2019 s.16 | unverified, earlier text not re-read |
| NTA 2025 (from 1 Jan 2026) | Turnover ≤ N100m AND fixed assets ≤ N250m | 0% | none | 30% + 4% Development Levy on every company not small and not non-resident | NTA 2025 ss.56, 59 | unverified, earlier text not re-read |

- **Pre-FA 2019**: n/a  _(CITA s.40)_
- **FA 2019 → FY 2025**: Turnover ≤ N25m  _(FA 2019 s.16)_
- **NTA 2025 (from 1 Jan 2026)**: Turnover ≤ N100m AND fixed assets ≤ N250m  _(NTA 2025)_
- **Filing obligation for small companies**: Route `ng-cit` for all RCs. Small companies still file (CIT-nil return): they do not escape the filing obligation.
- **Minimum tax**: Historically applied at 0.5% of gross turnover where computed tax was lower  specific period.

##### 4.4 PIT computation gate: NTA Fourth Schedule from 2026; PITA Sixth Schedule for pre-2026

- **From 2026**: bands 0% to 25% and rent relief; no CRA and no 1% minimum tax. See [ng-income-tax](ng-income-tax.md). The three lines below are pre-2026 only.

- **Progressive PIT rates**: 7% / 11% / 15% / 19% / 21% / 24% on bands stacked from N300,000 to > N3,200,000.  _(PITA Sixth Schedule)_
- **Consolidated Relief Allowance (CRA)**: CRA = max(N200,000, 1% × gross income) + 20% × gross income  _(PITA Sixth Schedule)_
- **Minimum tax (PIT)**: 1% of gross income where computed PIT after CRA and reliefs would be lower  _(PITA Sixth Schedule)_
- **Routing**: Route `ng-personal-income-tax` for the computation; defer state-specific filing portal nuances to that skill.

##### 4.5 VAT gate: NTA Chapter Six from 2026; VATA as amended for pre-2026

- **From 2026**: 7.5% (s.147). Basic food, medical, educational and export items are zero rated (s.186), not exempt. No registration threshold figure appears in the NTA text read. The three lines below are pre-2026 only.

- **VAT registration threshold**: N25m taxable turnover in the trailing-12 months. Below threshold = exempt from VAT registration and from VAT charging obligations, but still no input VAT recovery.  _(FA 2019 s.46)_
- **VAT standard rate**: 7.5% standard. Exports zero-rated. Basic food, medical and educational items exempt.  _(FA 2019; VATA First Schedule)_
- **Routing above threshold**: Above threshold or voluntarily registered → route `ng-vat` and ensure FIRS Tax Pro-Max VAT module is active.

##### 4.6 PAYE / employer gate: PITA s.81; Operation of PAYE Regulations 2002

PITA is repealed from 2026 (NTA s.195). The 10th-of-month date below is pre-2026; the 2026 date sits in the Nigeria Tax Administration Act 2025, not read.

- **PAYE withholding and remittance**: Any employees → withhold PAYE monthly and remit to the employee's State Internal Revenue Service by the 10th of the following month. Route `ng-paye` + `ng-payroll`.  _(PITA s.81; Operation of PAYE Regulations 2002)_
- **Statutory deductions**: Pension PRA 2014 8% employee + 10% employer; NHF 2.5%; NHIA where applicable; ITF 1% of payroll for employers with ≥ 5 staff or ≥ N50m turnover; NSITF 1% → route `ng-statutory-deductions`.  _(PRA 2014; NHF Act 1992; NHIA Act 2022; ITF (Amendment) Act 2011; Employee Compensation Act 2010)_

##### 4.7 Withholding-tax gate: CITA s.78-82; PITA s.69-73; WHT Regulations 1997 (as amended)

The rates below are pre-2026. For 2026 the NTA points to the Nigeria Tax Administration Act 2025 for deduction at source, and that Act was not read.

- **WHT obligation trigger**: WHT obligation arises if the taxpayer (RC always; sole trader where appointed agent) pays the categories listed below.  _(CITA s.78-82; PITA s.69-73; WHT Regulations 1997)_
- **Contracts / supplies**: 5% (companies) / 5% (individuals)  _(WHT Regulations 1997)_
- **Professional services / consultancy / management**: 10% / 5%  _(WHT Regulations 1997)_
- **Rent**: 10% (companies and individuals)  _(WHT Regulations 1997)_
- **Royalties / interest / dividends**: 10% (5% under several DTTs)  _(WHT Regulations 1997)_
- **Non-resident payments**: 10% subject to DTT  _(WHT Regulations 1997)_
- **Routing**: Reviewer to confirm the matrix for the relevant period. Route `ng-wht` whenever the taxpayer has paid or received any of the above.  

##### 4.8 CGT gate: CGTA s.2; FA 2021 (digital assets); NTA 2025

- **From 2026**: the Capital Gains Tax Act is repealed (NTA s.195). Chargeable gains enter an individual's total income (s.28(2)(a)(v)) and a company's total profits (s.27(1)), at the personal bands or the s.56 rate, not 10%. Nigerian share disposals are outside charge under the s.34(1)(a) conditions.
- **Pre-2026 CGT rate**: Capital gains on disposal of chargeable assets (land, buildings, shares above the FA 2021 N100m / 100,000-share thresholds, digital assets) → 10% CGT. Route `ng-cgt` if any disposals in the year, in either period.  _(CGTA s.2; FA 2021)_

##### 4.9 Filing-channel gate: FIRS Tax Pro-Max; state IRS portals

- **FIRS returns channel**: All FIRS returns (CIT, VAT, WHT, CGT for companies) file through FIRS Tax Pro-Max (mandatory since 2022). Confirm access.  _(FIRS Tax Pro-Max)_
- **State IRS returns channel**: PAYE and PIT returns file through the State IRS portal (LIRS eTax for Lagos; FCT-IRS for Abuja; relevant SIRS otherwise). Confirm access and state of residence.
- **Access missing flag**: If access missing → flag in `open_flags`; reviewer onboards before filing.

#### Section 5: Questions to ask the user

Use `ask_user_input_v0`. Batch where independent.

##### 5.1 Refusal sweep (one batched `ask_user_input_v0` call, 5 single-select questions)

- **Q1 Residency (period being prepared):** Full-year Nigerian resident | Foreigner present ≥ 183 days | Part-year | Non-resident with Nigerian-source income only.
- **Q2 Entity:** Sole trader (no CAC) | Business Name / BN (CAC Part B) | Private limited company / RC (Ltd) | Partnership | Incorporated Trustee / NGO | Not sure.
- **Q3 Period being prepared:** Calendar year 2025 (pre-NTA) | FY ending in 2025 (pre-NTA) | FY wholly from 1 Jan 2026 (NTA 2025) | Multiple periods or a straddle.
- **Q4 Current-FY turnover (NGN):** ≤ N25m | N25m-N100m | Above N100m | Not sure (infer from docs).
- **Q5 State of residence (PIT only) / state of operation (RC):** Lagos | FCT (Abuja) | Rivers | Other state: please name | Multiple states.

**Routing table**

| Answer | Action | Status |
| --- | --- | --- |
| Q1 full-year | continue | unverified, earlier text not re-read |
| Q1 foreigner ≥ 183d | continue; reviewer to verify DTT / significant economic presence rule | unverified, earlier text not re-read |
| Q1 part-year | continue with caution; flag split-year sourcing | unverified, earlier text not re-read |
| Q1 non-resident with NG-source only | **REFUSE**: separate non-resident workflow needed | unverified, earlier text not re-read |
| Q2 sole / BN | route `ng-personal-income-tax`; no `ng-cit` | unverified, earlier text not re-read |
| Q2 RC | route `ng-cit`; owner PIT only if salary / dividends drawn | unverified, earlier text not re-read |
| Q2 partnership | route `ng-personal-income-tax` per partner; flag for split | unverified, earlier text not re-read |
| Q2 Incorporated Trustee | **REFUSE**; route to specialist | unverified, earlier text not re-read |
| Q2 not sure | route `ng-formation` first | unverified, earlier text not re-read |
| Q3 calendar 2025 / FY ending 2025 | pre-NTA stack: CITA + PITA + FA 2019-2023 | unverified, earlier text not re-read |
| Q3 FY wholly from 1 Jan 2026 | NTA 2025 stack | unverified, earlier text not re-read |
| Q3 multiple periods or straddle | run each period through the appropriate stack | unverified, earlier text not re-read |
| Q4 ≤ N25m | pre-NTA: small company (FA 2019) OR below VAT threshold for sole/BN; NTA 2025: small if fixed assets ≤ N250m, no VAT threshold in text read | unverified, earlier text not re-read |
| Q4 N25m-N100m | pre-NTA: medium (CIT 20%); NTA 2025: small (CIT 0%) if fixed assets ≤ N250m, else 30% + 4% levy: period flag critical | unverified, earlier text not re-read |
| Q4 above N100m | pre-NTA: large (CIT 30%); NTA 2025: 30% + 4% levy | unverified, earlier text not re-read |
| Q4 not sure | defer to inference | unverified, earlier text not re-read |
| Q5 Lagos | PIT filings via LIRS eTax | unverified, earlier text not re-read |
| Q5 FCT | PIT filings via FCT-IRS | unverified, earlier text not re-read |
| Q5 other state | PIT filings via that SIRS; flag portal access | unverified, earlier text not re-read |
| Q5 multiple states | apportion by residence rule (PITA s.2(2)); flag for reviewer | unverified, earlier text not re-read |

##### 5.2 Secondary batched questions

- **Q6 VAT status:** Registered (issuing VAT invoices) | Not registered | Not sure.
- **Q7 Employees in the period:** None | 1-4 | 5-20 | > 20.
- **Q8 TIN status:** Have FIRS / JTB TIN (active) | Have CAC but no TIN | No registration yet.
- **Q9 Pension / statutory schemes:** All current (PenCom-compliant + NHF) | Some current | None.

**Routing table**

| Answer | Action | Status |
| --- | --- | --- |
| Q6 registered | route `ng-vat` | unverified, earlier text not re-read |
| Q6 not registered, pre-2026 period, turnover > N25m | flag **VAT registration overdue**; route `ng-vat`; reviewer to register | unverified, earlier text not re-read |
| Q6 not sure | defer to inference; default conservatively to "registration required" if the client makes taxable supplies from 2026, or turnover > N25m in a pre-2026 period | unverified, earlier text not re-read |
| Q7 ≥ 1 employee | route `ng-paye` + `ng-statutory-deductions` + `ng-payroll` | unverified, earlier text not re-read |
| Q7 ≥ 5 employees | additionally flag ITF (1% of payroll) and NSITF (1%) obligations | unverified, earlier text not re-read |
| Q8 no TIN | route to `ng-formation` onboarding fallback (Section 8); cannot file without TIN | unverified, earlier text not re-read |
| Q9 some / none | route `ng-statutory-deductions` to remediate; flag for reviewer | unverified, earlier text not re-read |

##### 5.3 WHT and CGT questions

- **Q10 In the period did you pay Nigerian suppliers for contracts, professional services, rent, or non-resident suppliers?** Yes (contracts) | Yes (services) | Yes (rent) | Yes (non-resident) | Multiple | No.
- **Q11 Did you dispose of land, buildings, shares above the FA 2021 thresholds, or digital assets in the period?** Yes | No | Not sure.

Any "Yes" on Q10 → route `ng-wht`. Reviewer confirms whether sole trader is an appointed WHT agent (CITA s.78-82 applies automatically to companies). Q11 yes → route `ng-cgt`.

##### 5.4 Tax Pro-Max / state portal access

- **Q12 FIRS Tax Pro-Max access?** Yes (active) | No (never logged in) | Started but hit issues.
- **Q13 State IRS portal access (LIRS eTax / FCT-IRS / SIRS)?** Yes | No | N/A (RC with no employees and no PIT due).

"No" or "issues" → flag in `open_flags`. Tax Pro-Max is the only FIRS filing channel; the relevant state portal is the only PAYE / PIT channel.

##### 6.1 Human-readable confirmation (shown to user)

```
INTAKE SUMMARY: Nigeria: Period: [CY2025 | FY ending YYYY-MM | FY starting 2026-01-01]

Taxpayer: [Name] | TIN: [12-digit] | CAC: [BN/RC number]
State of residence (PIT): [Lagos | FCT | …] | Entity: [Sole | BN | RC | Partnership]
Regime stack: [pre-NTA: CITA/PITA/FA 2019-2023 | NTA 2025]
FIRS Tax Pro-Max: [active | onboarding needed]
State IRS portal: [active | onboarding needed | N/A]

REGIME: [PIT progressive | CIT 0% small | CIT 30% + 4% Dev Levy | pre-NTA CIT 20% medium or 30% large]
  - Period turnover: N [X]
  - Entity size band: [small | medium | large]
  - VAT: [registered | below threshold | registration overdue]
  - Employees: [count]
  - WHT exposure: [paying | receiving | both | none]
  - CGT disposals: [yes | no]

DOWNSTREAM SKILLS:
  ng-personal-income-tax [if sole/BN/partnership],
  ng-cit [if RC], ng-vat [if registered or taxable supplies],
  ng-paye [if employees], ng-statutory-deductions [if employees],
  ng-payroll [if employees], ng-wht [if applicable],
  ng-cgt [if disposals], ng-formation [if entity unclear],
  ng-return-assembly [always last].

OPEN FLAGS, REFUSALS TRIGGERED, CONSERVATIVE DEFAULTS APPLIED: listed below.

Confirm or correct anything above.
```

##### 6.2 Structured intake package (internal JSON for ng-return-assembly)

```json
{
  "jurisdiction": "NG",
  "tax_year": 2026,
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
    "selected": "pit_progressive|cit_0_small|cit_30_other|cit_20_medium_pre2026|cit_30_large_pre2026",
    "period_turnover_ngn": 0,
    "fixed_assets_ngn": 0,
    "size_band": "small|other|medium_pre2026|large_pre2026",
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

#### Section 7: NTA 2025 transitional handling (pre-2026 vs from-2026)

The Nigeria Tax Act 2025 commences 1 January 2026 (s.195 repeals the old Acts from then). Earlier periods stay on the prior framework. Always record which regime stack applies and apply rules consistently within a single period.

**Pre-NTA vs NTA 2025 comparison**  _(NTA 2025 (consolidated))_

| Item | Pre-NTA 2025 (to 31 Dec 2025) | NTA 2025 (from 1 Jan 2026) | Status |
| --- | --- | --- | --- |
| Statutes | CITA, PITA, VATA, CGTA, FA 2019 / 2020 / 2021 / 2023 | NTA 2025 (consolidated) | unverified, earlier text not re-read |
| Small co. threshold | Turnover ≤ N25m (FA 2019) | Turnover ≤ N100m AND fixed assets ≤ N250m | unverified, earlier text not re-read |
| Small co. CIT | 0% | 0% | unverified, earlier text not re-read |
| Medium co. band | N25m-N100m | none | unverified, earlier text not re-read |
| Medium co. CIT | 20% | none, s.56 has no medium band | unverified, earlier text not re-read |
| Large co. CIT | 30% | 30% | unverified, earlier text not re-read |
| Development Levy | n/a (Tertiary Education Tax / NITDA / NASENI / police levy as separate items) | 4% levy on every company other than small and non-resident companies (s.59(1)) | unverified, earlier text not re-read |
| Minimum tax | 0.5% of turnover where applicable | 15% minimum effective rate only for s.57 companies | unverified, earlier text not re-read |
| WHT rates | WHT Regulations 1997 + FA amendments | Not in the NTA text read; sits in the Nigeria Tax Administration Act 2025, not read | unverified, earlier text not re-read |
| VAT | VATA + FA 2019 (7.5%) | 7.5% (NTA s.147); food, medical and education items zero rated (s.186) | unverified, earlier text not re-read |
| Filing channel (federal) | FIRS Tax Pro-Max | not confirmed; ask the client | unverified, earlier text not re-read |
| Filing channel (state PIT/PAYE) | State IRS portal | not confirmed; ask the client | unverified, earlier text not re-read |

- **Mixed periods handling**: Mixed periods (e.g., FY ending 31 March 2026 straddling 1 Jan 2026 cutover) are handled by `ng-return-assembly`, not by this intake: flag the straddle in `open_flags` and let the assembly skill do the apportionment under NTA 2025 transitional provisions.

#### Section 8: State-level considerations (LIRS vs other SIRS)

PIT and PAYE are state taxes; PITA governs pre-2026 periods. For 2026 use the NTA term "relevant tax authority"; its definition points to a Thirteenth Schedule that in the copy read covers agriculture, so the state split below is not confirmed for 2026. The state where the taxpayer is resident (PIT) or where the employee resides (PAYE) administers and collects.

**State administering authorities table**

| State | Administering authority | Portal | Notes | Status |
| --- | --- | --- | --- | --- |
| Lagos | Lagos State Internal Revenue Service (LIRS) | eTax (etax.lirs.net) | Most developed state portal; aggressive enforcement; tax audit cycle ~2 years; consent letters required for inter-state moves | unverified, earlier text not re-read |
| Federal Capital Territory (Abuja) | FCT Internal Revenue Service (FCT-IRS) | FCT-IRS e-portal | FCT residents file here, not FIRS | unverified, earlier text not re-read |
| Rivers | Rivers State IRS | RIRS portal |  | unverified, earlier text not re-read |
| Kano / Kaduna / Oyo / others | State IRS of residence | Varies | Some states still accept paper filings; flag for reviewer | unverified, earlier text not re-read |
| Cross-border residence | Pre-2026 apportionment rule (PITA s.2(2)) | n/a | Tax residence determined by principal place of residence on 1 January of the year | unverified, earlier text not re-read |

- For sole traders / BN, PIT is filed where the individual is resident, not where the business is registered or operates.
- For RC employees, PAYE is remitted to each employee's state of residence: a Lagos-based RC with staff in Ogun must remit Ogun PAYE to Ogun SIRS.
- TCC (Tax Clearance Certificate) is issued by the relevant state IRS for PIT and by FIRS for CIT.

If the state is anything other than Lagos / FCT / Rivers, flag for reviewer: portal availability and procedural rules vary widely.

#### Section 9: Onboarding fallback (user has no TIN yet)

If Q8 returns "No registration yet" or no TIN is found in documents, stop the regime-classification flow and run this fallback before any further work:

1. Confirm entity intent: sole / BN / RC. If unsure, route `ng-formation` first.
2. CAC registration (if BN or RC): the user must register the business with the Corporate Affairs Commission at cac.gov.ng before a TIN can be issued. BN takes ~2-5 working days; RC takes ~5-10 working days.
3. TIN issuance:
   - RC: TIN is now auto-issued by FIRS upon CAC incorporation (Joint Tax Board harmonisation, 2021 onward). Confirm via Tax Pro-Max lookup.
   - Sole / BN / individual: Apply for TIN via JTB / FIRS / state IRS. Individuals can use BVN-linked auto-issuance where supported. Lagos residents: LIRS issues Tax ID on first eTax registration.
4. Tax Pro-Max / state portal onboarding: create account, link TIN, link bank account for direct debit.
5. VAT registration (pre-2026 turnover > N25m or voluntary; from 2026 see Section 4.5): separate Tax Pro-Max workflow once TIN is active.
6. PAYE registration (if employees): register with the relevant state IRS as an employer; obtain Employer Tax ID.

Until TIN is active, no return can be filed. Flag `onboarding_required` in `open_flags` and refer the user to a CITN-registered tax practitioner or ICAN/ANAN Chartered Accountant to walk through CAC + JTB / FIRS / state IRS registration.

#### Section 10: Conservative defaults

When uncertain, prefer the safer (higher-tax / stricter-compliance) outcome and flag. All defaults visible to reviewer in `conservative_defaults_applied`.

**Conservative defaults table**

| Ambiguity | Conservative default | Status |
| --- | --- | --- |
| Period straddles 1 Jan 2026 cutover | Apply pre-NTA stack to pre-cutover portion, NTA 2025 to post-cutover; flag for `ng-return-assembly` | unverified, earlier text not re-read |
| Turnover near N25m (FA 2019) or N100m (NTA 2025) threshold | Assume above threshold: from 2026 not small, 30% plus levy; pre-2026 medium band + VAT registration required | unverified, earlier text not re-read |
| Entity unclear (sole vs BN vs RC) | Treat as sole trader for PIT default; flag `ng-formation` | unverified, earlier text not re-read |
| Residency borderline (~180 days) | Pre-2026: assume non-resident → REFUSE for individual returns. From 2026: test every NTA limb first; any one limb makes the person resident | unverified, earlier text not re-read |
| WHT-agent status unclear (sole trader not clearly appointed) | Assume WHT obligation exists for any qualifying payment; flag | unverified, earlier text not re-read |
| Pension / NHF / NHIA compliance unclear | Assume non-compliant → flag remediation; defer to `ng-statutory-deductions` | unverified, earlier text not re-read |
| Pre-2026 only: minimum tax (PIT 1% / CIT 0.5%) borderline | Apply minimum tax; reviewer can release if computed tax exceeds it | unverified, earlier text not re-read |
| State of residence unclear | Default Lagos (LIRS) only if documents support; otherwise ask: never guess | unverified, earlier text not re-read |
| Tax Pro-Max access unknown | Assume not active; flag for onboarding | unverified, earlier text not re-read |
| Capital vs expense unclear | Capitalise + flag (capital allowance treatment) | unverified, earlier text not re-read |
| Foreign-currency invoice without CBN rate | Use CBN official rate on invoice date; flag if no rate available | unverified, earlier text not re-read |

#### Section 11: Refusal handling

Refusals fire from the refusal sweep or during inference. Protocol: stop the workflow, state the reason in one sentence, recommend a CITN-registered tax practitioner or ICAN / ANAN Chartered Accountant (or an audit firm where audited financials are needed), do not work around.

- **In-scope refusals**: - Non-resident with Nigerian-source income only (separate flow needed). - Part-year residence with split sourcing complexity beyond a single relocation. - Incorporated Trustees / NGOs / cooperatives / Public Benefit Organisations. - Large companies with consolidated reporting, transfer-pricing audit exposure (TP Regulations 2018), or country-by-country reporting obligations. - RCs requiring audited financial statements (CAMA 2020 s.402) where audit is not yet complete: refuse until audit signed. - Oil and gas companies (PPTA / NUPRC regime): out of scope. - Free Zone Enterprises under NEPZA / OGFZA: out of scope. - Pioneer-status companies during pioneer period (Industrial Development (Income Tax Relief) Act): refuse; specialist territory.  _(CAMA 2020 s.402; TP Regulations 2018; PPTA; NEPZA; OGFZA; Industrial Development (Income Tax Relief) Act)_

Sample: "Stop: your RC's financial statements have not yet been audited. CAMA 2020 s.402 requires audited accounts for the CIT filing, and FIRS will reject a Tax Pro-Max submission without them. You need an ICAN-registered auditor to sign off before I can prepare the return."

#### Section 12: Self-checks before handoff

Run all 15 before invoking `ng-return-assembly`. Any failure → fix, do not hand off.

1. Refusal sweep used `ask_user_input_v0`, not prose.
2. Residency confirmed (full-year, ≥ 183d foreigner with flag, or refused).
3. Entity type set (sole / BN / RC / partnership).
4. Regime stack chosen (pre-NTA vs NTA 2025) and recorded.
5. Period turnover recorded in NGN with bucket band.
6. Regime selected with reason traced to (a) entity, (b) turnover, (c) period.
7. VAT status set; `registration_overdue_flag` set if a pre-2026 period has turnover > N25m and no registration.
8. Employee count set; `ng-paye` + `ng-statutory-deductions` + `ng-payroll` in downstream list if > 0.
9. ITF / NSITF flags set if ≥ 5 employees or ≥ N50m payroll.
10. WHT exposure checked; `ng-wht` in list if applicable.
11. CGT disposals checked; `ng-cgt` in list if applicable.
12. State of residence captured (PIT path) or state of operation (RC path).
13. TIN status captured; onboarding fallback triggered if absent.
14. Tax Pro-Max + state IRS portal access captured.
15. Reviewer disclaimer present in opening + handoff (CITN / ICAN / ANAN sign-off).

#### Section 13: Final handoff to ng-return-assembly

Once gap-filling and self-checks pass, output a short handoff message naming (a) taxpayer + entity + state + TIN + Tax Pro-Max status, (b) regime stack + regime selected with the headline computation citation, (c) downstream skills in run-order, (d) skills explicitly not running and why, (e) reviewer reminder. Then invoke `ng-return-assembly` with the Section 6.2 package.

Example (sole trader, Lagos, FY 2025 pre-NTA, no employees, below VAT threshold):

> Intake complete. Adebayo Okonkwo, sole trader, Lagos resident, TIN active, LIRS eTax onboarded, no CAC (sole, not BN). Period: CY 2025, pre-NTA stack. Turnover N18m. Regime: PIT progressive (PITA Sixth Schedule); CRA = max(N200k, 1% × gross) + 20% × gross; minimum tax 1% if computed PIT lower. Running: ng-personal-income-tax, ng-wht (Q10 yes on services received), ng-return-assembly. Not running: ng-cit (sole trader), ng-vat (below N25m), ng-paye / ng-statutory-deductions / ng-payroll (no employees), ng-cgt (no disposals). Needs CITN-registered tax practitioner sign-off before LIRS eTax submission. Handing off now.

Example (RC, FY ending 31 Dec 2026, NTA 2025 stack, 8 employees, above VAT threshold):

> Intake complete. Pomelo Tech Ltd, RC 1234567, registered office Lagos, TIN active, Tax Pro-Max active. Period: FY ending 31 Dec 2026, NTA 2025 stack. Turnover N420m, fixed assets N80m  → not small, 30% plus levy; earlier label medium company. Regime: CIT 20% (NTA 2025). Running: ng-cit, ng-vat (registered), ng-paye + ng-statutory-deductions + ng-payroll (8 employees; ITF applicable as headcount ≥ 5), ng-wht (paying both contractors and rent), ng-return-assembly. Not running: ng-personal-income-tax (separate workflow for owner salary), ng-cgt (no disposals). Needs ICAN-registered Chartered Accountant sign-off and audited financials (CAMA 2020 s.402) before Tax Pro-Max submission. Handing off now.

#### Section 14: Cross-skill references

Inputs: user documents (bank statements, invoices, WHT credit notes, prior returns, CAC certificate, TIN slip, payroll register) + user answers. Output: Section 6.2 package consumed by `ng-return-assembly`.

Downstream skills (via ng-return-assembly):

- `ng-personal-income-tax`: PIT progressive 7-24%, CRA, 1% minimum tax (PITA Sixth Schedule).
- `ng-cit`: Companies Income Tax: 0% / 30% + 4% Development Levy from 2026 (NTA ss.56, 59); 0% / 20% / 30% pre-2026 (CITA).
- `ng-paye`: Operation of PAYE Regulations 2002; monthly remittance to state IRS by the 10th.
- `ng-statutory-deductions`: Pension (PRA 2014), NHF, NHIA, ITF, NSITF.
- `ng-payroll`: payslip generation; gross-to-net; employer cost summary.
- `ng-wht`: Withholding tax matrix (CITA s.78-82; PITA s.69-73; WHT Regulations 1997; NTA 2025 simplifications).
- `ng-cgt`: Capital Gains Tax 10% (CGTA; FA 2021 digital assets and N100m share threshold).
- `ng-vat`: VAT 7.5% standard, zero-rate exports, exemptions (VATA + FA 2019 amendments).
- `ng-formation`: Entity choice + CAC / TIN onboarding.
- `ng-return-assembly`: final orchestrator (returns + working paper + reviewer brief + action list).

#### Section 15: Sources

Primary statutes and regulations cited (reviewer to verify the exact version in force for the period being prepared):

- Personal Income Tax Act (PITA), Cap. P8 LFN 2004, as amended by Finance Acts 2019-2023.
- Companies Income Tax Act (CITA), Cap. C21 LFN 2004, as amended.
- Value Added Tax Act (VATA), Cap. V1 LFN 2004, as amended by Finance Acts 2019, 2020, 2021, 2023.
- Capital Gains Tax Act (CGTA), Cap. C1 LFN 2004, as amended; FA 2021 (digital assets; share-disposal threshold).
- Finance Act 2019: small company definition (turnover ≤ N25m); VAT rate to 7.5%; VAT registration threshold N25m.
- Finance Act 2020 / 2021 / 2023: incremental amendments.
- Nigeria Tax Act 2025 (NTA 2025): consolidated framework commencing 1 January 2026; small company 0% (N100m turnover, N250m fixed assets), any other company 30% (s.56); 4% Development Levy (s.59). Repeals CITA, PITA, VATA and CGTA (s.195).
- Companies and Allied Matters Act (CAMA) 2020: entity types; audit requirements (s.402); CAC procedures.
- Pension Reform Act (PRA) 2014: employer 10% + employee 8% pension contributions.
- National Housing Fund Act 1992: NHF 2.5% employee deduction.
- National Health Insurance Authority Act 2022: NHIA, replacing NHIS Act 1999.
- Industrial Training Fund (Amendment) Act 2011: ITF 1% of payroll where headcount ≥ 5 or turnover ≥ N50m.
- Employee Compensation Act 2010: NSITF 1% of payroll.
- Operation of PAYE Regulations 2002.
- Withholding Tax Regulations 1997 (as amended), pre-2026.
- Transfer Pricing Regulations 2018 (out of scope here).
- Joint Tax Board (JTB) TIN harmonisation circulars (2021 onward).
- FIRS Tax Pro-Max: mandatory federal filing channel since 2022.
- State IRS portals: LIRS eTax, FCT-IRS, RIRS, etc.

#### Change log

v1.0 (May 2026): Initial intake skill for the Nigerian freelance / SME workflow. Routes to ng-personal-income-tax, ng-cit, ng-paye, ng-statutory-deductions, ng-payroll, ng-wht, ng-cgt, ng-vat, ng-formation, ng-return-assembly. Covers both the pre-NTA stack (CITA / PITA / FA 2019-2023) for periods ending on or before 31 December 2025 and the Nigeria Tax Act 2025 stack from 1 January 2026, with the shift from N25m / N100m bands to the single small company test (N100m turnover, N250m fixed assets).



## Two worked examples that recompute

Simple: RC with turnover NGN 420,000,000, fixed assets NGN 80,000,000, assessable profit NGN 60,000,000: not small.

```oa-check
name: Regime check, other company
inputs:
  profit: 60000000
steps:
  - cit: profit * 0.30
  - levy: profit * 0.04
  - total: cit + levy
expected:
  total: 20400000.00
```

Decision, which period stack? A company with turnover NGN 90,000,000: 2025 pre-2026 text puts it at 20%; 2026 at 0% if fixed assets are within the limit. On NGN 10,000,000 profit that is the difference shown.

```oa-check
name: Period flag, turnover NGN 90,000,000
inputs:
  profit: 10000000
steps:
  - old: profit * 0.20
  - new: profit * 0
  - difference: old - new
expected:
  difference: 2000000.00
```

## Ask the client first

1. Period being prepared?
2. Entity type?
3. Gross turnover and total fixed assets?
4. State of residence?
5. Employees?
6. Non-resident customers or suppliers?


## Sources

| Source | URL | Read on |
|---|---|---|
| Nigeria Tax Act 2025, Act No. 7, Official Gazette No. 117, 26 June 2025. UNOFFICIAL COPY hosted by Premium Times, not an official host. Sections read: ss.27, 28, 34, 56 to 59, 147, 186, 195, Fourth Schedule, definitions | https://media.premiumtimesng.com/wp-content/files/2026/01/Final-Approved-Copy-for-Print-NIGERIA-TAX-ACT-2025.pdf | 2026-11-01 |
| NRS notice of 20 July 2026 on e-invoicing (read by an earlier pass; official) | https://www.nrs.gov.ng/ | 2026-11-01 |

NRS guides at https://www.nrs.gov.ng/taxpayer-services/tax-guides-and-manuals could not be read: a page shell loaded, then other NRS pages showed a CAPTCHA, so no cross-check was done.

Not yet confirmed: every NTA figure in this skill, including the s.57 group test, printed as £750 million in the copy read. Each comes from an unofficial press-hosted copy and was not confirmed in an official document, because nrs.gov.ng showed a CAPTCHA on 2026-11-01 and it was not touched. Also unconfirmed: all filing dates, forms, portals and penalties under the Nigeria Tax Administration Act 2025, whose text we did not open; the VAT registration threshold (no figure appears in the NTA text read); capital allowance rates for ordinary trades; and all earlier text. Also unconfirmed: how a financial year straddling 1 January 2026 is assessed, since the sections read give the commencement date only. Lost content restored: 0, nothing removed.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. OpenAccountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified Nigerian professional: a CITN-registered tax practitioner, an ICAN or ANAN Chartered Accountant, or a legal practitioner where applicable, and an external auditor where CAMA 2020 s.402 requires audited financial statements: before filing with FIRS via Tax Pro-Max or with the relevant State Internal Revenue Service, or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com).

---

*OpenAccountants: open-source accounting skills for AI*
*This output must be reviewed by a qualified professional before filing or acting upon.*
*Latest verified skills: openaccountants.com | Report errors: github.com/openaccountants/openaccountants*

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
