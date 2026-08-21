---
name: pk-freelance-intake
description: ALWAYS USE THIS SKILL when a user asks for help with their Pakistan taxes AND mentions freelancing, self-employment, sole proprietorship, IT exports, or being a business individual in Pakistan. Trigger on phrases like "help me with my Pakistan taxes", "I'm a freelancer in Pakistan", "I export IT services", "file my FBR return", "I'm self-employed in Pakistan". This is the REQUIRED entry point for the Pakistan self-employed workflow — downstream skills (pk-it-export-tax, pk-income-tax, pk-social-contributions, pakistan-sales-tax, pk-return-assembly) depend on it. Upload-first; Pakistan-resident individuals only.
version: 0.1
jurisdiction: PK
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
category: orchestrator
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# PK Freelance Intake

## Pakistan — Freelance / SME Intake — Skill v1.0

## What this file is

The intake orchestrator for Pakistan-resident self-employed individuals, sole proprietors, AOP (Association of Persons) partners, and small Pvt Ltd founders. Every downstream Pakistani content skill depends on this skill producing a structured intake package first.

Job: (1) confirm taxpayer is in scope, (2) classify the regime (Individual / AOP PIT business income vs Pvt Ltd CIT vs PSEB IT-export final-tax regime), (3) determine ATL filer status and provincial services-tax registration footprint, (4) identify downstream skills to run, (5) hand off to `pk-return-assembly`. Outputs addressed to a credentialed Pakistani reviewer (ICAP Chartered Accountant, ICMAP Cost & Management Accountant, or FBR Income Tax Practitioner / ITP). The reviewer signs off — this skill is not the preparer of record.

Pakistan's freelance economy is enormous (commonly cited as a top-3 global market by freelancer count). Software developers, digital content creators, designers, and remote contractors for foreign clients dominate. Filer status (inclusion on the FBR Active Taxpayers List) is the single biggest cost lever — non-filers pay 2-3x withholding on banking transactions, vehicle registration, property transfers, dividends, and prize bonds (Tenth Schedule, ITO 2001). PSEB (Pakistan Software Export Board) registration unlocks a reduced final-tax regime on IT and ITES exports (rate to be confirmed under Finance Act 2025 — historically 0.25%/1%). Pakistan tax year runs 1 July – 30 June.

## Section 1 — Quick reference: regime decision tree at a glance

```
Full-year Pakistan tax resident (ITO 2001 s.82)? -> NO = REFUSE
       |
Entity?
       |
       +-- Individual / AOP
       |        |
       |        +-- PSEB-registered IT/ITES exporter with foreign-currency receipts via banking channel?
       |        |        -> YES (Clause 133, Pt I, 2nd Sch / s.154A SBP procedure) -> 0.25% / 1% final
       |        |                tax on export proceeds — verify FA 2025 current rate (TBC)
       |        +-- Salary > 50% of taxable income? -> Salaried slab (s.12, 1st Sch Pt I Div I)
       |        +-- Otherwise -> Business / non-salaried slab (1st Sch Pt I Div I)
       |        +-- AOP -> Separate slab schedule (1st Sch Pt I Div I, AOP rates)
       |
       +-- Pvt Ltd (Companies Act 2017)
                -> CIT 29% (1st Sch Pt I Div II); + super tax s.4C if applicable;
                   + minimum tax on turnover s.113 if applicable
```

Parallel routing (independent of regime):

- Taxable supplies of goods → FBR sales tax under Sales Tax Act 1990; threshold trigger → route `pk-sales-tax-federal`.
- Taxable services rendered → provincial sales tax (PRA Punjab, SRB Sindh, KPRA KP, BRA Balochistan, ICT-FBR for Islamabad Capital Territory) → route `pk-sales-tax-services` with the correct authority.
- Employees → EOBI (Employees' Old-Age Benefits Institution) + provincial social security (SESSI / PESSI / SI KP / BESSI) + monthly salary WHT → route `pk-payroll-eobi`.
- Pays Pakistani suppliers, rent, or non-resident services → WHT obligations under ITO 2001 s.149–s.165 → route `pk-withholding-tax`.
- Sold securities, immovable property, or crypto → route `pk-cgt`.
- Entity unclear / wants to incorporate → route `pk-formation`.
- Always final → `pk-return-assembly`.

## Section 2 — Workflow runbook (order of operations)

0. **Opening** — one-line greeting + flow summary + reviewer reminder, then launch the refusal sweep
0. **Refusal sweep** — single `ask_user_input_v0` call with the 5 questions in Section 5.1
0. **Document dump** — ask user to upload everything at once (bank statements, invoices, PSEB certificate, prior IRIS return, withholding certificates, CNIC / NTN). Do not insist on one document at a time.
0. **Inference pass** — parse every document; extract turnover, expenses, withholding suffered, prior payments, ATL status, export receipts in PKR equivalent and FX gross
0. **Regime classification** — apply Section 4 decision tree using inferred turnover + sweep answers
0. **Confirmation** — show inferred summary + proposed regime + downstream-skill list; invite corrections
0. **Gap filling** — `ask_user_input_v0` only for items documents cannot answer (CNIC, NTN, STRN, PSEB number, ATL status, provincial jurisdiction)
0. **Handoff** — produce Section 6 summary and invoke `pk-return-assembly`

## Section 2 — Workflow runbook (order of operations)

Strict order. Do not narrate steps.

Operating principles: use `ask_user_input_v0` for multi-choice; free text only for names / NTN / STRN / PSEB-ID. Batch up to 3 related independent questions. Never re-ask documents-visible facts. Urdu / regulatory terms in parentheses on first mention (e.g., "Active Taxpayers List (ATL)", "Income Tax Ordinance 2001 (ITO 2001)"). All amounts in PKR; foreign-currency receipts stated in both FX gross and PKR equivalent at the SBP-applicable rate on credit date.

## Section 3 — Required inputs

Some inferred from documents, the rest gap-filled. All mandatory before handoff.

- **Identity / registration:** legal name (CNIC), CNIC number, NTN (National Tax Number — 7-digit FBR identifier), STRN (Sales Tax Registration Number, if registered), PSEB Registration Number (if IT/ITES exporter), Iris/IRIS portal access status, business name (if sole prop trading under a name), Form-29 directors (if Pvt Ltd).
- **Entity:** Individual / Sole Proprietor / AOP (partnership) / Pvt Ltd (Companies Act 2017) / SMC-Pvt Ltd (Single Member Company). For AOP: partnership deed date and partner shares. For Pvt Ltd: SECP incorporation date, CUIN.
- **Residency:** days physically present in Pakistan during the 12-month tax year (1 July – 30 June), prior-year residency, dual-residency / treaty considerations.
- **Revenue:** 2025-26 turnover (PKR), monthly breakdown, domestic (PKR-invoiced) vs export (foreign-currency, via banking channel). For IT exporters: PSEB certificate validity, Encashment Certificates (PRCs) from banks, foreign inward remittance receipts.
- **Tax history:** prior-year IRIS return (Form 114 individual / 116 AOP / 32A company), ATL status at start of tax year, prior tax payable / refundable, advance tax paid under s.147.
- **Operational:** employee count, EOBI registration, provincial social-security registration (SESSI Sindh, PESSI Punjab, SI KP, BESSI Balochistan), PRA / SRB / KPRA / BRA / ICT services-tax registration, federal sales tax (FBR) registration if dealing in goods.
- **Provincial footprint:** province where services are rendered, province where client is located (origin-based vs destination-based rules differ across PRAs — reviewer to verify), permanent establishment in multiple provinces.
- **Documents:** bank statements (all accounts incl. foreign-currency), invoices issued, expense receipts, withholding tax certificates (CPRs — Computerised Payment Receipts) on bank profit / dividends / contracts, prior IRIS return, PSEB certificate, PRC/encashment certificates, partnership deed, SECP incorporation documents.

## Section 4 — Regime decision tree with thresholds and citations

All references to **ITO 2001** = Income Tax Ordinance 2001 (as amended through Finance Act 2025, TBC for any post-July 2025 amendments). All thresholds and rates 2025-26-effective subject to FA 2025 verification.

### 4.1 Residency gate — ITO 2001 s.82

- **Residency test** — Pakistan tax resident in a tax year (1 July – 30 June) if any of: (a) present in Pakistan for ≥183 days in the tax year; (b) present ≥120 days in the tax year AND ≥365 days across the four preceding tax years; (c) Pakistani citizen present in Pakistan during the tax year and not present in any other country for ≥183 days; (d) Government servant posted abroad. Otherwise non-resident. Not full-year resident → **REFUSE** (split-year and treaty cases require an ICAP/ITP).  _(ITO 2001 s.82)_

### 4.2 Entity gate

- **Individual / Sole Proprietor** — IRIS Form 114(I). Slab schedule per s.12 (salary > 50% of taxable income) or non-salaried (business income) (1st Sch Pt I Div I). Route `pk-income-tax`.  _(s.12, 1st Sch Pt I Div I)_
- **AOP** — IRIS Form 116. AOP slab schedule (1st Sch Pt I Div I — AOP rates differ from individuals). Partners' share is exempt at partner level (s.92). Route `pk-income-tax` (AOP branch).  _(s.92, 1st Sch Pt I Div I)_
- **Pvt Ltd / SMC-Pvt Ltd** — IRIS Form 32A (company return). CIT 29% (1st Sch Pt I Div II). Route `pk-corporate-tax`. Plus super tax s.4C if applicable; minimum tax on turnover s.113 if applicable; ACT (Alternate Corporate Tax) s.113C if applicable.  _(Companies Act 2017; 1st Sch Pt I Div II; s.4C; s.113; s.113C)_

Entity unclear → route `pk-formation`. Listed/public companies, banking companies, insurance, oil & gas, and groups with consolidated reporting → out of scope; refuse.

### 4.3 PSEB IT-export gate — Clause 133, Part I, Second Schedule, ITO 2001 (export-of-IT-services regime, TBC for FA 2025)

- **PSEB IT-export final tax** — If individual / AOP / Pvt Ltd is a PSEB-registered IT or ITES exporter AND export proceeds are received in convertible foreign exchange through the normal banking channel (SBP procedure / s.154A withholding regime): Historically 0.25% final tax on export proceeds for PSEB-registered exporters; 1% for non-PSEB but otherwise compliant; verify FA 2025 current rate (TBC). Final tax — not adjustable against other income. Local-Pakistan income outside the IT-export stream remains under normal regime.  _(Clause 133, Pt I, 2nd Sch, ITO 2001; s.154A)_
- **Strict requirements** — PSEB registration current, separate ledger of export proceeds, PRC / Encashment Certificate from bank, foreign-currency receipts via banking channel only (cash / crypto / hawala receipts are disqualified).  _(Clause 133, Pt I, 2nd Sch, ITO 2001; s.154A)_

Route `pk-income-tax` (for non-export income) + flag IT-export final-tax regime in the package. Software developers earning USD from Upwork / Fiverr / direct foreign clients almost always qualify — confirm PSEB registration and bank-channel compliance.

### 4.4 Filer / Non-Filer gate — Tenth Schedule, ITO 2001

- **ATL inclusion requirements** — ATL (Active Taxpayers List) is published weekly by FBR. Inclusion requires (a) prior-year return filed, (b) surcharge paid if filed after due date (Rs. 1,000 individual / Rs. 10,000 AOP / Rs. 20,000 company — verify FA 2025). Non-filer / non-ATL → 2x–3x WHT under Tenth Schedule on banking transactions, dividends, profit on debt, prize money, vehicle registration, property purchase, contracts.  _(Tenth Schedule, ITO 2001)_

Confirm ATL status at filing date and at year-start. If non-filer in 2024-25 but filing 2025-26 now → flag — ATL inclusion typically takes effect from the Monday after surcharge payment + return submission. Reviewer to advise on retrospective WHT recovery.

### 4.5 Federal sales tax (goods) gate — Sales Tax Act 1990

- **STRN registration threshold** — Mandatory STRN registration if dealing in taxable supplies of goods above the cottage-industry / manufacturer threshold (Rs. 10m turnover cottage-industry threshold, verify FA 2025). Standard rate 18% (verify FA 2025). Retailers under Tier-1 in special regime. Route `pk-sales-tax-federal` if dealing in goods at all.  _(Sales Tax Act 1990)_

Pure service providers and IT exporters generally do not register under STA 1990 — they fall under provincial services tax (Section 4.6).

### 4.6 Provincial services tax gate — Sindh STA 2011 / Punjab STA Services 2012 / KPRA Act 2013 / BRA Act 2015 / ICT Ordinance 2001

**Provincial services-tax authorities and rates**  _(Sindh Sales Tax on Services Act 2011; Punjab Sales Tax on Services Act 2012; KPRA Act 2013; BRA Act 2015; ICT (Tax on Services) Ordinance 2001)_

| Province/Territory | Authority | Act | Standard rate |
| --- | --- | --- | --- |
| Sindh | SRB (Sindh Revenue Board) | Sindh Sales Tax on Services Act 2011 | 13% (verify FA 2025) |
| Punjab | PRA (Punjab Revenue Authority) | Punjab Sales Tax on Services Act 2012 | 16% (verify FA 2025) |
| Khyber Pakhtunkhwa | KPRA (KP Revenue Authority) | KPRA Act 2013 | 15% (verify FA 2025) |
| Balochistan | BRA (Balochistan Revenue Authority) | BRA Act 2015 | 15% (verify FA 2025) |
| Islamabad Capital Territory | FBR ICT (Islamabad) | ICT (Tax on Services) Ordinance 2001 | 16% (verify FA 2025) |

This is the most jurisdictionally complex part of Pakistan VAT. The 18th Constitutional Amendment (2010) devolved sales tax on services to the provinces. Each province has its own authority, rate, and return.

**Jurisdiction rules (high-level — reviewer to verify per authority's current rules):**

- SRB (Sindh): origin-based for most services (where the service originates) plus destination-based for specified services.
- PRA (Punjab): broadly destination-based (where the service is received) for most categories.
- Multiple provincial registrations may be required if taxpayer has fixed places of business or renders services across provinces.
- **IT / software / digital services:** specific entries in each schedule — typically taxable. PSEB-exempt status varies per province (e.g., SRB has historically given IT-export exemptions; verify current rules under each province's FA 2025).

Route `pk-sales-tax-services` with the list of applicable authorities. If multi-jurisdictional → flag and require reviewer to confirm registration plan.

### 4.7 Withholding-tax-agent gate — ITO 2001 s.149–s.165

- **WHT agent thresholds** — WHT obligation arises if taxpayer is (a) company, (b) AOP with turnover > Rs. 50m prior year, (c) individual with turnover > Rs. 100m prior year (verify FA 2025 thresholds), AND pays any of: salary (s.149), dividends (s.150), profit on debt (s.151), contracts (s.153), services (s.153), commission (s.233), brokerage, rent (s.155), non-resident payments (s.152). Different rates apply for filers vs non-filers (Tenth Schedule). Route `pk-withholding-tax` if any qualifying payments made.  _(ITO 2001 s.149–s.165; Tenth Schedule)_

### 4.9 Minimum tax and super tax — s.113, s.4C

- **s.113 minimum tax on turnover** — 1.25% percent (verify FA 2025; applies on declared turnover of companies and certain AOPs / individuals where normal tax computed is less than minimum. Carryforward of excess for 3 years.)  _(ITO 2001 s.113)_
- **s.4C super tax** — Tiered, applies to high-income earners. Verify FA 2025 brackets and rates.  _(ITO 2001 s.4C)_
- **s.113C ACT (Alternate Corporate Tax)** — 17% percent (of accounting profit — applies to companies if higher than normal tax)  _(ITO 2001 s.113C)_

Flag for reviewer if turnover > Rs. 100m or if accounting profit substantially exceeds taxable profit.

### 4.10 Bookkeeping gate — ITO 2001 s.174 and ITR 2002

- **record-keeping requirements** — Taxpayers must maintain records sufficient to compute taxable income for 6 years. Companies → audited financial statements under Companies Act 2017 + ICAP accounting standards (IAS/IFRS as adopted in Pakistan or AFRS for SMEs). AOPs and large individuals → adequate accounting records. Small individuals on PSEB final-tax regime → bank channel reconciliation + invoice register sufficient. Flag if records insufficient.  _(ITO 2001 s.174; ITR 2002)_

### 4.11 IRIS filing channel

- **IRIS filing channel** — All FBR filings (income tax, federal sales tax, withholding statements) submitted through IRIS (Inland Revenue Information System). Provincial filings go through each authority's portal (e-SRB, e-PRA, KPRA portal, BRA portal). Confirm IRIS access (login + password + RSA token if applicable). If not active, flag for reviewer onboarding.

## Section 5 — Questions to ask the user

Use `ask_user_input_v0`. Batch where independent.

### 5.1 Refusal sweep (one batched `ask_user_input_v0` call, 5 single-select questions)

- **Q1 Residency 2025-26 (1 July 2025 – 30 June 2026):** Full-year resident (≥183 days in Pakistan) | Resident under 120-day rule (s.82(b)) | Pakistani citizen abroad | Non-resident | Not sure.
- **Q2 Entity:** Individual / Sole Proprietor | AOP (partnership) | Pvt Ltd | SMC-Pvt Ltd | Not sure / want to incorporate.
- **Q3 Primary income source:** Salary (employed) | Freelance / business (software dev, consulting, etc.) | Mix of salary + freelance | IT export only (USD from foreign clients) | Goods trading | Other.
- **Q4 2025-26 turnover (PKR equivalent):** ≤ Rs. 600,000 | Rs. 600k–Rs. 5m | Rs. 5m–Rs. 50m | Rs. 50m–Rs. 250m | > Rs. 250m | Not sure (infer from docs).
- **Q5 Province where you primarily render services / are based:** Sindh (Karachi / Hyderabad) | Punjab (Lahore / Faisalabad / Rawalpindi / Multan) | KP (Peshawar / Mardan) | Balochistan (Quetta) | ICT (Islamabad) | Mixed / multiple provinces | AJK / GB (special).

**Routing table**

| Answer | Action |
| --- | --- |
| Q1 full-year resident | continue |
| Q1 120-day rule | continue; flag treaty / dual-residence check |
| Q1 citizen abroad | continue; verify s.82(c) and treaty position; flag |
| Q1 non-resident / not sure | **REFUSE** — full-year residents only; refer to ICAP / ITP |
| Q2 individual / sole prop | continue; regime by Q3 + Q4 |
| Q2 AOP | continue; route `pk-income-tax` (AOP branch); partner-level exemption flag |
| Q2 Pvt Ltd / SMC | continue; route `pk-corporate-tax` |
| Q2 not sure | route `pk-formation` first |
| Q3 salary-only | route `pk-income-tax` (salaried slab) |
| Q3 freelance / business | route `pk-income-tax` (non-salaried) + PSEB check |
| Q3 mix | route both; segregate income |
| Q3 IT export only | PSEB final-tax candidate (s.154A / Clause 133); route `pk-income-tax` for any non-export receipts |
| Q3 goods trading | route `pk-sales-tax-federal` |
| Q4 ≤ Rs. 600k | likely below taxable threshold (basic exemption Rs. 600k for individuals — verify FA 2025); still file if registered |
| Q4 Rs. 600k–Rs. 50m | normal regime; PSEB exporter → final-tax |
| Q4 Rs. 50m–Rs. 250m | normal regime + minimum tax s.113 check + likely sales tax registration |
| Q4 > Rs. 250m | likely super tax s.4C + minimum tax + audit; flag — may need ICAP audit |
| Q4 not sure | defer to inference |
| Q5 Sindh | services → SRB |
| Q5 Punjab | services → PRA |
| Q5 KP | services → KPRA |
| Q5 Balochistan | services → BRA |
| Q5 ICT | services → FBR ICT |
| Q5 mixed | flag; multi-authority registration likely |
| Q5 AJK / GB | **REFUSE** — out of scope; refer to ICAP |

### 5.2 Secondary batched questions

- **Q6 NTN / FBR registration status:** Yes (NTN active, file via IRIS) | No (never registered) | Registered but not filed recently.
- **Q7 ATL (Active Taxpayers List) status:** On ATL (filer) | Not on ATL (non-filer) | Not sure (will check FBR site).
- **Q8 PSEB registration (only if Q3 includes IT export or freelance with foreign clients):** Yes (active PSEB ID) | No (not registered, foreign-client work) | Not applicable (no foreign client work).
- **Q9 Employees in 2025-26:** None | 1–5 | 6–20 | > 20.
- **Q10 STRN (Sales Tax Registration Number) status:** Yes — FBR (goods) | Yes — PRA / SRB / KPRA / BRA / ICT (services) | Yes — multiple authorities | No registration | Not sure.

**Routing table**

| Answer | Action |
| --- | --- |
| Q6 not registered | flag — must register NTN before IRIS filing; route `pk-formation` |
| Q6 registered not filed recently | flag prior-year compliance gap; reviewer to assess penalties |
| Q7 non-filer | flag — Tenth Schedule WHT applied at 2-3x; ATL inclusion takes effect after current-year filing + surcharge |
| Q7 not sure | flag for FBR ATL lookup at filing date |
| Q8 yes (active) | route IT-export final-tax regime in `pk-income-tax` |
| Q8 no but foreign-client work | flag — PSEB registration likely beneficial; reviewer to advise; default to 1% rate not 0.25% pending registration |
| Q9 ≥ 1 employee | route `pk-payroll-eobi` |
| Q9 > 20 | flag (audit-grade payroll volume) |
| Q10 STRN yes federal | route `pk-sales-tax-federal` |
| Q10 STRN yes provincial | route `pk-sales-tax-services` with named authority |
| Q10 no but turnover > threshold | flag **sales-tax registration overdue** |

### 5.3 Withholding question

- **Q11 In 2025-26 did you make any of: salary payments, rent on business premises, contractor/service payments above WHT threshold, payments to non-resident suppliers, dividends, profit-on-debt?** Yes (specify) | No.

Any "Yes" → route `pk-withholding-tax`. Reviewer confirms whether taxpayer crosses s.153 / s.155 / s.152 prescribed-person thresholds.

### 5.4 Capital gains question

- **Q12 In 2025-26 did you sell securities (listed shares, mutual funds), immovable property (plot / flat / house), or crypto / virtual assets?** Yes (specify) | No.

Any "Yes" → route `pk-cgt`. Note CGT regime under s.37A (securities) and s.37 (immovable property) — rates depend on holding period and filer status.

### 5.5 IRIS access

- **Q13 IRIS portal access:** Yes (active login) | No (never used) | Started but hit issues / locked out.

"No" or "issues" → flag in `open_flags`. IRIS is the only filing channel for FBR returns.

### 6.1 Human-readable confirmation (shown to user)

```
INTAKE SUMMARY — 2025-26 Pakistan (1 July 2025 – 30 June 2026)

Taxpayer: [Name] | CNIC: [13-digit] | NTN: [7-digit] | STRN: [if any]
Entity: [Individual | Sole Prop | AOP | Pvt Ltd | SMC-Pvt Ltd]
Residency: [full-year resident | 120-day rule | citizen abroad]
Province: [Sindh | Punjab | KP | Balochistan | ICT | multi]
IRIS: [active | onboarding needed]
ATL status: [on ATL (filer) | non-filer (flagged) | unknown]

REGIME: [Salaried PIT | Non-salaried PIT | AOP PIT | CIT 29% | PSEB IT-export final tax]
  - 2025-26 turnover: Rs. [X] (PKR [Y] from domestic + USD [Z] export = PKR equivalent)
  - PSEB registered: [yes — IT export 0.25%/1% final | no | n/a]
  - Sales tax footprint: [FBR goods | SRB Sindh | PRA Punjab | KPRA | BRA | ICT-FBR | multiple | none]
  - Employees: [count]
  - Min tax s.113 check: [applicable | not applicable]
  - Super tax s.4C check: [applicable | not applicable]

DOWNSTREAM SKILLS:
  pk-income-tax [if individual/AOP/salary],
  pk-corporate-tax [if Pvt Ltd / SMC],
  pk-withholding-tax [if WH-agent payments made],
  pk-sales-tax-federal [if goods + STRN],
  pk-sales-tax-services [if services + provincial registration],
  pk-payroll-eobi [if employees],
  pk-cgt [if disposed securities / property / crypto],
  pk-formation [if entity unclear / NTN not registered],
  pk-return-assembly [always last].

OPEN FLAGS, REFUSALS TRIGGERED, CONSERVATIVE DEFAULTS APPLIED — listed below.

Confirm or correct anything above.
```

### 6.2 Structured intake package (internal JSON for pk-return-assembly)

```json
{
  "jurisdiction": "PK",
  "tax_year": "2025-26",
  "tax_year_window": {"start": "2025-07-01", "end": "2026-06-30"},
  "taxpayer": {
    "name": "", "cnic": "", "ntn": "", "strn": "",
    "pseb_id": "", "iris_active": false,
    "entity_type": "Individual|SoleProp|AOP|PvtLtd|SMC_PvtLtd",
    "residency": "full_year_resident|120_day_rule|citizen_abroad",
    "primary_province": "Sindh|Punjab|KP|Balochistan|ICT|multi"
  },
  "atl": {
    "status": "on_atl|non_filer|unknown",
    "prior_year_filed": false,
    "surcharge_paid": false,
    "tenth_schedule_uplift_applied": true
  },
  "regime": {
    "selected": "salaried_pit|non_salaried_pit|aop_pit|cit_29|pseb_it_export_final",
    "annual_turnover_pkr": 0,
    "domestic_turnover_pkr": 0,
    "export_turnover_pkr_equivalent": 0,
    "export_turnover_fx_gross": 0,
    "export_currency": "USD|EUR|GBP|other",
    "pseb_registered": false,
    "pseb_final_tax_rate_pct": 0.25,
    "minimum_tax_s113_applicable": false,
    "super_tax_s4c_applicable": false,
    "act_s113c_applicable": false
  },
  "sales_tax": {
    "fbr_goods_registered": false,
    "srb_sindh_registered": false,
    "pra_punjab_registered": false,
    "kpra_registered": false,
    "bra_registered": false,
    "ict_fbr_registered": false,
    "multi_jurisdiction_flag": false,
    "registration_overdue_flag": false
  },
  "employment": {
    "has_employees": false,
    "employee_count": 0,
    "eobi_registered": false,
    "provincial_ss_registered": false,
    "provincial_professional_tax_due": false
  },
  "withholding": {
    "made_salary_payments": false,
    "made_rent_payments": false,
    "made_contractor_service_payments": false,
    "made_non_resident_payments": false,
    "made_dividend_payments": false,
    "is_prescribed_person_s153": false
  },
  "capital_gains": {
    "disposed_securities": false,
    "disposed_immovable_property": false,
    "disposed_crypto": false
  },
  "bookkeeping": {
    "method_required": "audited_ifrs|aop_records|individual_records|bank_channel_recon",
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

**Conservative defaults table**

| Ambiguity | Conservative default |
| --- | --- |
| Residency borderline (~180 days) | Assume non-resident → REFUSE; ICAP/ITP to determine (s.82) |
| ATL status unknown | Assume **non-filer** → apply Tenth Schedule uplift on WHT (2x–3x); reviewer to verify ATL at filing date |
| PSEB registration unclear | Assume **not PSEB-registered** → 1% rate not 0.25%; reviewer to verify PSEB certificate |
| Export receipts via non-banking channel | Disqualify from IT-export final-tax regime; treat as normal business income |
| Provincial services-tax jurisdiction unclear | Assume registration required in BOTH origin and destination province; reviewer to confirm |
| Sales-tax threshold near limit | Assume registration required; route `pk-sales-tax-federal` or `pk-sales-tax-services` |
| Entity type unclear (Individual vs AOP) | Assume Individual unless partnership deed sighted; flag |
| AOP partner share / partnership deed unclear | Refuse AOP allocation; reviewer to obtain deed (s.92) |
| WH-agent threshold unclear (s.153 prescribed person) | Assume taxpayer IS prescribed person if turnover > Rs. 100m prior year (individual) or Rs. 50m (AOP); apply WHT |
| Minimum tax s.113 applicability unclear | Assume applicable; compute and flag |
| Super tax s.4C applicability unclear (turnover/income borderline) | Assume applicable; compute and flag |
| Bookkeeping inadequate | Default to "records insufficient" → flag; reviewer to remediate before filing |
| IRIS access unknown | Assume not active; flag for onboarding |
| Capital vs revenue expense unclear | Capitalise + depreciate per ITR 2002; flag |
| FA 2025 rate / threshold ambiguity | Use FA 2024 rate + flag (TBC) for reviewer to confirm |

## Section 8 — Refusal handling

- **protocol** — Refusals fire from the refusal sweep or during inference. Protocol: stop the workflow, state the reason in one sentence, recommend an ICAP Chartered Accountant or FBR Income Tax Practitioner (ITP), or ICMAP CMA for cost-accounting-heavy cases. Do not work around.
- **In-scope refusals** — Part-year / non-resident. Foreign tax residents claiming Pakistan-source income only (treaty cases). Listed / public companies. Banking companies, insurance companies, oil & gas, mineral exploration (special regimes — 7th Schedule etc.). Companies with consolidated reporting, transfer-pricing returns, CbCR. Pvt Ltd with > 50 employees or audited revenue > Rs. 1 billion. AJK (Azad Jammu & Kashmir) and GB (Gilgit-Baltistan) residents — separate tax administrations. Smuggling / informal / cash-only operations with no documentation.

Sample: "Stop — you spent only 110 days in Pakistan in 2025-26, so you do not meet the s.82 resident tests. Non-residents are taxed only on Pakistan-source income and may have treaty relief — you need an ICAP Chartered Accountant or FBR-licensed Income Tax Practitioner. I cannot proceed."

## Section 9 — Self-checks before handoff

Run all 16 before invoking `pk-return-assembly`. Any failure → fix, do not hand off.

1. Refusal sweep used `ask_user_input_v0`, not prose.
2. Residency confirmed under s.82 with day-count or other test cited.
3. Entity type set; for AOP, partnership deed sighted or flagged; for Pvt Ltd, CUIN captured.
4. NTN captured (or flagged as not-yet-registered → `pk-formation`).
5. ATL status captured (on ATL / non-filer / unknown); Tenth Schedule uplift flag set if non-filer.
6. PSEB status captured if any foreign-client / IT-export income; export-receipts-via-banking-channel confirmed.
7. 2025-26 turnover recorded in PKR with domestic vs export split; FX gross also captured.
8. Regime selected with reason traced to (a) entity, (b) salary vs business split, (c) PSEB IT-export final-tax eligibility.
9. Sales-tax footprint identified (federal goods / provincial services authority / multi); registration overdue flag set if applicable.
10. Provincial services-tax jurisdiction(s) named explicitly (SRB / PRA / KPRA / BRA / ICT-FBR).
11. Employee count set; `pk-payroll-eobi` in downstream list if > 0; EOBI + provincial SS noted.
12. WH obligations checked against s.153 / s.155 / s.152 thresholds; `pk-withholding-tax` in list if applicable.
13. Minimum tax s.113, super tax s.4C, ACT s.113C applicability flagged where turnover / profit warrants.
14. CGT events identified (securities / property / crypto); `pk-cgt` routed if any.
15. IRIS access captured; onboarding flagged if not active.
16. All conservative defaults recorded with citation; FA 2025 ambiguities marked TBC; reviewer disclaimer present in opening + handoff.

## Section 10 — Final handoff to pk-return-assembly

Once gap-filling and self-checks pass, output a short handoff message naming (a) taxpayer + entity + province + ATL status + IRIS status, (b) regime selected with headline computation citation (e.g., PSEB final tax at 0.25% under Clause 133 / s.154A, TBC FA 2025), (c) downstream skills in run-order, (d) skills explicitly not running and why, (e) reviewer reminder (ICAP CA or FBR ITP sign-off before IRIS submission). Then invoke `pk-return-assembly` with the Section 6.2 package.

Example (Individual freelance software developer, PSEB-registered, no employees, services-only, Punjab):

> Intake complete. Ahmed Khan, Individual / Sole Proprietor, Lahore (Punjab), NTN 1234567, PSEB ID active. Full-year resident under s.82(a) (present 245 days). On ATL (filed 2024-25 on time). 2025-26 turnover: PKR equivalent Rs. 8.5m — domestic Rs. 0, export Rs. 8.5m (USD 30,000 via Meezan Bank Roshan Digital Account, PRCs sighted). Regime: PSEB IT-export final tax at 0.25% under Clause 133 Pt I 2nd Sch / s.154A (TBC FA 2025) → Rs. 21,250 final tax on export proceeds; no progressive tax on this stream. PRA registration check: software services to foreign clients — historically PRA-exempt under export-of-services entry; reviewer to verify FA 2025 schedule. Running: pk-income-tax (final-tax branch), pk-sales-tax-services (PRA exemption confirmation), pk-return-assembly. Not running: pk-corporate-tax, pk-sales-tax-federal, pk-payroll-eobi, pk-withholding-tax, pk-cgt, pk-formation. Needs ICAP CA or FBR ITP sign-off before IRIS submission. Handing off now.

## Section 11 — Cross-skill references

**Inputs:** user documents (bank statements, invoices, PRCs / encashment certificates, prior IRIS return, PSEB certificate, partnership deed, SECP docs, CPRs) + user answers. **Output:** Section 6.2 package consumed by `pk-return-assembly`.

Downstream skills (via pk-return-assembly):

- `pk-income-tax` — Individual / Sole Prop / AOP PIT under ITO 2001 s.9–s.12, slab schedule 1st Sch Pt I Div I; PSEB IT-export final tax branch (Clause 133 / s.154A).
- `pk-corporate-tax` — Pvt Ltd / SMC CIT 29% (1st Sch Pt I Div II); + s.4C super tax; + s.113 minimum tax; + s.113C ACT.
- `pk-withholding-tax` — s.149 salary, s.150 dividend, s.151 profit on debt, s.152 non-resident, s.153 contracts / services, s.155 rent; Tenth Schedule uplift for non-filers.
- `pk-sales-tax-federal` — Sales Tax Act 1990; STRN; FBR returns.
- `pk-sales-tax-services` — SRB / PRA / KPRA / BRA / ICT-FBR; provincial portals; origin vs destination rules.
- `pk-payroll-eobi` — EOBI Act 1976; provincial social security (SESSI / PESSI / SI KP / BESSI); s.149 monthly salary WHT; provincial professional tax.
- `pk-formation` — NTN registration on IRIS; SECP incorporation (Pvt Ltd / SMC); partnership / AOP deed; PSEB registration.
- `pk-cgt` — s.37 immovable property gains; s.37A securities gains; crypto / virtual-asset treatment (verify FA 2025 — TBC).
- `pk-return-assembly` — final orchestrator (IRIS forms 114(I) / 116 / 32A, working paper, reviewer brief, action list, ATL reinstatement plan if applicable).

## Section 12 — Sources

Primary statutes and regulations (all 2025-26-effective subject to Finance Act 2025 verification — TBC items flagged):

- **Income Tax Ordinance 2001 (ITO 2001)** as amended through Finance Act 2025 (TBC for any post-July 2025 amendments).
  - s.82 — residence of individuals.
  - s.9–s.12 — heads of income; salary vs business.
  - s.92 — taxation of AOPs and partners.
  - s.4C — super tax on high earners.
  - s.113 — minimum tax on turnover.
  - s.113C — Alternate Corporate Tax.
  - s.147 — advance tax instalments.
  - s.149–s.165 — withholding tax regime.
  - s.154A — withholding on export proceeds.
  - s.174 — record-keeping (6 years).
  - **Tenth Schedule** — non-filer / non-ATL WHT uplift.
  - **First Schedule, Part I, Division I** — individual / AOP slab rates.
  - **First Schedule, Part I, Division II** — company tax rate (29%).
  - **Second Schedule, Part I, Clause 133** — IT / ITES export final-tax regime (TBC FA 2025).
- **Income Tax Rules 2002 (ITR 2002)** — depreciation, business records, return-form prescriptions.
- **Sales Tax Act 1990 (STA 1990)** — federal sales tax on goods; STRN; FBR.
- **Sindh Sales Tax on Services Act 2011** — SRB.
- **Punjab Sales Tax on Services Act 2012** — PRA.
- **KPRA Finance Act 2013** — KPRA.
- **BRA Sales Tax on Services Act 2015** — BRA.
- **Islamabad Capital Territory (Tax on Services) Ordinance 2001** — ICT-FBR.
- **Companies Act 2017** — Pvt Ltd, SMC-Pvt Ltd, audited financials.
- **EOBI Act 1976** — Employees' Old-Age Benefits.
- **Provincial Employees' Social Security Ordinance 1965** — SESSI / PESSI / SI KP / BESSI.
- **Finance Act 2025** — annual amendments to ITO 2001, STA 1990, and Federal Excise Act 2005 (TBC — confirm gazetted text).
- **PSEB (Pakistan Software Export Board) registration framework** — operational rules for IT/ITES exporter status.
- **State Bank of Pakistan (SBP) Foreign Exchange Manual** — banking-channel requirements for export-proceeds receipts.
- **18th Constitutional Amendment 2010** — devolution of sales tax on services to provinces.

## Change log

**v1.0 (May 2026):** Initial intake skill for the Pakistan freelance / SME workflow. Routes to pk-income-tax, pk-corporate-tax, pk-withholding-tax, pk-sales-tax-federal, pk-sales-tax-services, pk-payroll-eobi, pk-formation, pk-cgt, pk-return-assembly. Reflects ITO 2001 (as amended through FA 2024 — FA 2025 amendments TBC), Companies Act 2017, the four provincial services-tax regimes (SRB / PRA / KPRA / BRA) plus ICT-FBR, PSEB IT-export final-tax regime, ATL filer / non-filer Tenth-Schedule mechanics, and IRIS as the federal filing channel for tax year 2025-26 (1 July 2025 – 30 June 2026).

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. OpenAccountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified Pakistani tax professional — an ICAP Chartered Accountant, an ICMAP Cost & Management Accountant, or an FBR-licensed Income Tax Practitioner (ITP) — before filing with FBR via IRIS or with any provincial revenue authority, and before acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com).

---

*OpenAccountants — open-source accounting skills for AI*
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
