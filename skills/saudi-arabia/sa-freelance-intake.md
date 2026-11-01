---
name: sa-freelance-intake
description: ALWAYS USE THIS SKILL when a user asks for help with Saudi tax/Zakat compliance and mentions freelancing, self-employment, sole establishment (mu'assasah fardiyyah), LLC, JSC, branch of a foreign company, or any commercial activity in the Kingdom of Saudi Arabia (KSA). Trigger on phrases like "Saudi tax compliance", "ZATCA registration", "Saudi VAT", "Saudi Zakat return", "MISA registration", "freelance Saudi tax", "Riyadh business", "Jeddah company tax", "Saudi corporate income tax", "SAR turnover threshold", "Fatoorah Phase 2", "GOSI registration", "Saudization Nitaqat", "Saudi withholding tax", "RETT", "real estate transaction tax Saudi", "Saudi excise tax", "Hijri vs Gregorian tax year", "mixed ownership Saudi entity", "GCC owner Zakat", "non-resident Saudi tax", or any similar phrasing where the user is operating or planning to operate a business in KSA. This is the REQUIRED entry point for the Saudi freelance/SME workflow, and every downstream skill in the stack (sa-zakat, sa-corporate-tax, sa-withholding-tax, sa-rett, sa-gosi-saudization, sa-excise-tax, sa-formation, saudi-arabia-vat, saudi-einvoice, sa-return-assembly) depends on this skill running first. Uses ask_user_input_v0-style structured questions. Saudi tax/Zakat residents and foreign-owned KSA entities only. ALWAYS read this skill first when starting any Saudi freelance/SME tax or Zakat workflow.
jurisdiction: SA
version: 1.1
tax_year: 2026
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# SA Freelance Intake

## Scope


The intake orchestrator for Saudi-resident self-employed individuals, sole establishments (mu'assasah fardiyyah), single-shareholder LLCs, multi-member LLCs, joint-stock companies (JSC), and branches of foreign companies registered with ZATCA in the Kingdom of Saudi Arabia (KSA). Every downstream Saudi content skill depends on this skill producing a structured intake package first.

Job: (1) confirm taxpayer is in scope, (2) classify the regime split: Zakat vs Corporate Income Tax (CIT) vs mixed: based on ownership nationality, (3) check VAT, excise, RETT, WHT, GOSI/Saudization, e-invoicing (Fatoorah) gates, (4) confirm MISA registration exists for any foreign owner, (5) identify downstream skills to run, (6) hand off to `sa-return-assembly`. Outputs addressed to a credentialed Saudi reviewer (SOCPA-licensed Saudi CPA or a tax adviser registered with ZATCA). The reviewer signs off: this skill is not the preparer of record.


## Ask the client first

### Section 5: Questions to ask the user

Use `ask_user_input_v0`. Batch where independent.

#### 5.1 Refusal sweep (one batched `ask_user_input_v0` call, 5 single-select questions)

- **Q1 KSA tax residence / CR status:** CR issued and ZATCA-registered | CR issued, not yet ZATCA-registered | Pre-formation (no CR yet) | Foreign entity with PE | Non-resident, no PE.
- **Q2 Entity type:** Sole establishment (mu'assasah fardiyyah) | Single-shareholder LLC | Multi-member LLC | JSC (closed) | JSC (listed) | Branch of foreign company | Simple joint partnership | Not sure.
- **Q3 Ownership nationality mix (capital):** 100% Saudi nationals | 100% GCC nationals (incl. Saudi) | 100% foreign (non-GCC) | Mixed Saudi/GCC + foreign | Not sure.
- **Q4 2026 annual turnover (SAR):** < SAR 187,500 | SAR 187,500 to 375,000 | SAR 375,000 to 3 million | SAR 3 million - 40 million | > SAR 40 million | Not sure (infer from docs).
- **Q5 MISA investment registration (foreign owners only):** N/A (no foreign owner) | Yes, valid MISA registration | No MISA registration yet | Expired / under renewal.

**Refusal sweep routing table**

| Answer | Action |
| --- | --- |
| Q1 CR + ZATCA-registered | continue |
| Q1 CR but not yet ZATCA-registered | flag overdue registration; route `sa-formation` for ZATCA onboarding; continue |
| Q1 pre-formation | **REFUSE** core intake; route `sa-formation` only |
| Q1 foreign entity with PE | continue; force CIT route; flag PE attribution to reviewer |
| Q1 non-resident no PE | **REFUSE**: non-residents only have WHT; refer to ZATCA-registered tax adviser |
| Q2 sole establishment / LLC (single or multi) / JSC closed / branch | continue |
| Q2 JSC listed | flag float-share complexity; refer to SOCPA CPA |
| Q2 not sure | route `sa-formation` first |
| Q3 100% Saudi / 100% GCC | Zakat-only path; route `sa-zakat` |
| Q3 100% foreign | CIT-only path; route `sa-corporate-tax`; require MISA (Q5) |
| Q3 mixed | split path; route both `sa-zakat` + `sa-corporate-tax` |
| Q3 not sure | request shareholder register; defer to inference |
| Q4 < SAR 187,500 | no VAT registration (not even voluntary); continue |
| Q4 SAR 187,500 to 375,000 | voluntary VAT election available; ask reviewer to confirm |
| Q4 ≥ SAR 375,000 | mandatory VAT; route `saudi-arabia-vat` + `saudi-einvoice` |
| Q4 > SAR 40 million | monthly VAT returns; Fatoorah Phase 2 wave already passed; verify integration status |
| Q5 N/A | continue |
| Q5 valid MISA | continue |
| Q5 no MISA / expired | **REFUSE** workflow for foreign-owned entity; route `sa-formation`; reviewer engages corporate counsel |

#### 5.2 Secondary batched questions

- **Q6 VAT registration:** Yes (TIN ending 03) | No | Voluntary | Deregistered.
- **Q7 Employees 2026 (KSA payroll):** None | 1 to 5 | 6 to 20 | 21 to 50 | > 50.
- **Q8 Non-Saudi vs Saudi headcount split:** All Saudi | Majority Saudi | Majority non-Saudi | All non-Saudi | N/A.
- **Q9 Nitaqat current band:** Platinum | High Green | Medium Green | Low Green | Red | Not yet assigned | N/A.
- **Q10 Fiscal year basis:** Gregorian calendar (1 Jan - 31 Dec) | Gregorian non-calendar | Hijri (lunar) | Not sure.

**Secondary questions routing table**

| Answer | Action |
| --- | --- |
| Q6 yes | route `saudi-arabia-vat` + `saudi-einvoice` |
| Q6 no but Q4 ≥ SAR 375,000 | flag **VAT registration overdue**; route `saudi-arabia-vat`; reviewer to register |
| Q7 ≥ 1 | route `sa-gosi-saudization` |
| Q7 > 50 | flag (large-employer compliance load) |
| Q8 majority/all non-Saudi + Q9 Red/Low Green | flag Saudization risk; recommend Nitaqat remediation plan |
| Q9 Red | flag visa-block risk; reviewer escalation |
| Q10 Hijri + foreign ownership | conflict: Hijri only allowed for Zakat-only; flag to reviewer; default Gregorian |

#### 5.3 Withholding question

- **Q11 In 2026 did you pay any non-resident (foreign) suppliers, lenders, licensors, or service providers (e.g., software licences, head-office charges, foreign consultants, foreign loans)?** Yes (specify categories) | No.

Any "Yes" → route `sa-withholding-tax`. Reviewer applies treaty rates where available.

#### 5.4 RETT and Excise questions

- **Q12 In 2026 did you sell, transfer, or grant a long lease over any real estate in KSA?** Yes | No | Inheritance / family transfer only.
- **Q13 Do you import, manufacture, or hold inventory of tobacco, energy drinks, soft drinks, sweetened drinks, or e-cigarettes / e-liquids?** Yes | No.

Q12 "Yes" (non-inheritance) → route `sa-rett`. Q13 "Yes" → route `sa-excise-tax`.

#### 5.5 Fatoorah Phase 2 access

- **Q14 Fatoorah Phase 2 (Integration):** Already integrated (API live) | Notified by ZATCA, integration pending | Not yet in a wave | Not sure.

"Pending" or "not sure" → flag in `open_flags`; route `saudi-einvoice` for wave verification and integration readiness.

### Section 3: Required inputs

Some inferred from documents, the rest gap-filled. All mandatory before handoff.

- **Identity / registration:** legal name (Arabic + English), Commercial Registration (CR) number, ZATCA Tax Identification Number (TIN, 10-digit), VAT registration number (15-digit ending 03 if registered), MISA investment registration number (foreign-owned entities only), national address (Wasel).
- **Entity:** sole establishment (mu'assasah fardiyyah) / single-shareholder LLC / multi-member LLC / JSC / branch of foreign company / simple joint partnership. CR issuance date. Bylaws / Articles of Association.
- **Ownership:** complete shareholder register with nationality (Saudi national / GCC national / foreign) and ownership % each. Beneficial ownership disclosure (UBO file at ZATCA).
- **Fiscal year:** Gregorian calendar default. Hijri election only available to Zakat-only payers (no foreign ownership). Year-end date.
- **Revenue:** 2026 annual turnover (SAR), monthly breakdown, domestic vs export mix, exempt vs zero-rated vs standard-rated for VAT.
- **Tax history:** prior Zakat return, prior CIT return (if applicable), prior VAT returns (monthly or quarterly), prior WHT returns, outstanding ZATCA assessments or appeals.
- **Operational:** employee count (Saudi vs non-Saudi headcount for Nitaqat), GOSI registration status, Mudad WPS active, current Nitaqat band (Platinum / High Green / Medium Green / Low Green / Red), Fatoorah Phase 2 wave assignment.
- **Documents:** CR, MISA registration, ZATCA tax certificate, VAT certificate, bank statements 2026, sales tax invoices (Phase 2-compliant if integrated wave), purchase invoices, GOSI subscriber report, prior Zakat/CIT/VAT/WHT returns, payment receipts (SADAD).

## The method, step by step

### Rates, bands and thresholds

| Item | Amount | Tax year | Source |
|---|---|---|---|
| Zakat, Hijri year | 2.5% of the Zakat base | 2026 | Regulations art. 15, https://zatca.gov.sa/en/RulesRegulations/Documents/ZAKAT%20COLLECTION.pdf |
| Zakat, other fiscal year | 2.5% / Hijri days x fiscal days | 2026 | same |
| Income tax on the non-Saudi share | 20% | 2026 | ZATCA guideline, https://zatca.gov.sa/en/HelpCenter/guidelines/Documents/General-Guideline-for-Withholding-Tax-In-accordance-with-the-provisions-of-the-Income-Tax-Law-and-its-Implementing-Regulations.pdf |
| WHT management fees | 20% | 2026 | https://zatca.gov.sa/en/HelpCenter/guidelines/Documents/General-Guideline-for-Withholding-Tax-In-accordance-with-the-provisions-of-the-Income-Tax-Law-and-its-Implementing-Regulations.pdf |
| WHT royalties; land transport; other payments | 15% | 2026 | same |
| WHT dividends, rent, loan charges, insurance, technical and consulting services, air tickets and freight, international telecoms | 5% | 2026 | same |
| VAT monthly filing | annual supplies over SAR 40 million | 2026 | https://zatca.gov.sa/en/MediaCenter/News/Pages/Submit-VAT-Return-for-Oct-andQ3-2026.aspx |
| E-invoicing Wave 25 | VAT-liable revenue over SAR 187,500 in any of 2022 to 2025; integrate by 1 February 2027 | 2026 | https://zatca.gov.sa/en/MediaCenter/News/Pages/Wave25-E-invoicing.aspx |
| VAT mandatory registration | SAR 375,000 | 2026 | unverified |
| VAT voluntary registration | SAR 187,500 | 2026 | unverified |

### Section 1: Quick reference: regime decision tree at a glance

0. **Route to sa-zakat**: 100% Saudi/GCC natural persons → ZAKAT only

### Section 2: Workflow runbook (order of operations)

0. **Opening**: One-line greeting + flow summary + reviewer reminder, then launch the refusal sweep.
0. **Refusal sweep**: Single ask_user_input_v0 call with the 5 questions in Section 5.1.
0. **Document dump**: Ask user to upload everything at once (CR, MISA registration if foreign, ZATCA certificate, VAT certificate, bank statements, sales invoices, purchase invoices, GOSI subscriber list, prior Zakat/CIT returns, prior VAT returns).
0. **Inference pass**: Parse every document; extract turnover, ownership %, employee count, prior payments, fiscal year basis.
0. **Regime classification**: Apply Section 4 split logic using inferred ownership + sweep answers.
0. **Confirmation**: Show inferred summary + proposed regime split + downstream-skill list; invite corrections.
0. **Gap filling**: ask_user_input_v0 only for items documents cannot answer (Hijri vs Gregorian election, MISA registration number, Nitaqat color band).
0. **Handoff**: Produce Section 6 summary and invoke sa-return-assembly.

### Section 4: Regime decision tree with thresholds and citations

Thresholds for 2026. Figures not marked to a source are listed under Not yet confirmed.

#### 4.1 Residency gate: Income Tax Law (Royal Decree M/1, 1425H) art. 3; Implementing Regulations for Zakat Collection (Minister of Finance Decision 1007, 1445H, amended by Decision 1248, 1446H)

- **KSA tax/Zakat resident definition**: KSA tax/Zakat resident = entity established under Saudi law with a CR, or a foreign entity with a permanent establishment (PE) in KSA. Natural persons: a resident Saudi person practising a licensed activity pays Zakat (Zakat Regulations art. 3); a non-Saudi resident natural person practising an activity in the Kingdom pays income tax (ZATCA Income Tax Guideline). Non-resident with no PE → out of scope here → REFUSE.  _(Income Tax Law (Royal Decree M/1, 1425H) art. 3; Implementing Regulations for Zakat Collection (Minister of Finance Decision 1007, 1445H, amended by Decision 1248, 1446H))_

#### 4.2 Ownership-nationality gate: the Zakat/CIT split

- **Fundamental Zakat/CIT split rule**: Zakat applies to the share held by a Saudi person, and "Saudi" includes GCC nationals accorded similar treatment (Zakat Regulations arts. 1, 3). Income tax applies to shares of non-Saudi partners in resident capital companies ([ZATCA Income Tax Guideline](https://zatca.gov.sa/en/HelpCenter/guidelines/Documents/Simplified-Guideline-for-Income-Tax.pdf)).
- **Zakat rate for 100% Saudi/GCC natural-person owners**: 2.5% of the Zakat base for a Hijri year; for a fiscal year that differs, 2.5% divided by the days in the Hijri year, multiplied by the days in the fiscal year (Zakat Regulations art. 15)
- **CIT rate for 100% foreign (non-GCC) owners**: 20% percent (general rate on taxable income; oil & hydrocarbons up to 85%, natural gas 20%: both out of scope here; foreign ownership requires MISA registration issued before CR)
- **Mixed ownership split**: Proportional split. The Saudi/GCC share of equity attracts Zakat; the foreign share of taxable income attracts CIT. Both sa-zakat and sa-corporate-tax route. Single combined ZATCA filing covers both components.
- **GCC corporate owners treatment**: GCC corporate owners treated as foreign for CIT/Zakat split unless ZATCA accepts look-through (case-by-case; flag to reviewer).
- **Listed JSC treatment**: Listed JSC with free-float → proportional float treatment; out of scope here → flag to reviewer.

#### 4.3 VAT registration gate: VAT Law (Royal Decree M/113, 1438H) and VAT Implementing Regulations

- **Mandatory VAT registration threshold (unverified)**: 375,000 SAR (annual taxable supplies in trailing-12-month window (or expected in next 12 months))  _(VAT Law (Royal Decree M/113, 1438H) and VAT Implementing Regulations)_
- **Voluntary VAT registration range (unverified)**: 187,500 to 375,000 SAR (voluntary registration available)  _(VAT Law (Royal Decree M/113, 1438H) and VAT Implementing Regulations)_
- **Below voluntary threshold (unverified)**: Below SAR 187,500 → no VAT registration permitted.  _(VAT Law (Royal Decree M/113, 1438H) and VAT Implementing Regulations)_
- **Standard VAT rate**: 15% percent (since 1 July 2020. Zero-rated: exports, qualifying international transport, certain medicines/medical equipment. Exempt: financial services (margin-based), residential rental, residential real estate sales.)  _(Royal Order A/638)_
- **VAT routing**: → Route `saudi-arabia-vat` + `saudi-einvoice` if registered or over threshold.

#### 4.4 E-invoicing gate: Fatoorah (ZATCA E-Invoicing Regulation, December 2020)

Two phases:

- **Phase 1: Generation** (mandatory for all VAT-registered residents since 4 December 2021): structured electronic invoices with QR code for B2C; no integration required.
- **Phase 2: Integration**: wave-based mandate by annual taxable revenue threshold. ZATCA issues each wave at least six months in advance. Wave 1 started 1 January 2023 (≥ SAR 3 billion revenue); subsequent waves progressively cover smaller taxpayers. Wave 25 covers taxpayers whose VAT-liable revenue exceeded SAR 187,500 in 2022, 2023, 2024 or 2025, with integration no later than 1 February 2027 ([ZATCA](https://zatca.gov.sa/en/MediaCenter/News/Pages/Wave25-E-invoicing.aspx)). **Confirm the wave named in the taxpayer's ZATCA notice**: flag to reviewer if unclear.

→ All VAT-registered residents → route `saudi-einvoice`. Phase 2 wave triggers integration requirements (API connection, cryptographic stamp, real-time clearance for tax invoices, near-real-time reporting for simplified invoices).

#### 4.5 Excise tax gate: Excise Tax Law (Royal Decree M/86, 1438H)

- **Excise tax rates and registration**: Excise tax applies to tobacco products, energy drinks, soft drinks, sweetened drinks and electronic smoking devices and liquids (old rates of 100% and 50% are unverified here; see `sa-excise-tax`). From 1 January 2026 sweetened drinks are taxed by tiers based on total sugar per 100 ml of the ready-to-drink product, replacing the flat 50% of retail price ([ZATCA, Arabic](https://zatca.gov.sa/en/MediaCenter/News/Pages/excise-tax-regulation-2026.aspx)). Tier amounts are unverified. Excise registration with ZATCA required before importing, producing, or holding excise goods. → Route `sa-excise-tax`.  _(Excise Tax Law (Royal Decree M/86, 1438H))_

#### 4.6 RETT gate: Real Estate Transaction Tax Regulation (Royal Order A/84, 2 October 2020)

- **RETT flat rate**: 5% percent (applies to most real estate disposals (sale, transfer, long lease, contribution in kind to a company). RETT replaced VAT on real estate from 4 October 2020 (Council of Ministers Resolution). Limited exemptions (e.g., inheritance, gifts to first-degree relatives, first-home purchase up to SAR 1 million under certain conditions). → Route sa-rett if any real estate transaction in the year.)  _(Royal Order A/84, 2 October 2020)_

#### 4.7 Withholding tax gate: Income Tax Law art. 68; Implementing Regulations art. 63

- **WHT applicability**: WHT on payments from KSA-resident payers to non-residents without a PE. Any non-resident payments → route sa-withholding-tax.  _(Income Tax Law art. 68; Implementing Regulations art. 63)_
- **Dividends to non-resident**: 5% percent  _(Income Tax Law art. 68)_
- **Loan charges / interest**: 5% percent  _(Income Tax Law art. 68)_
- **Royalties**: 15% percent  _(Income Tax Law art. 68)_
- **Management fees**: 20% percent  _(Income Tax Law art. 68)_
- **Other categories**: rent 5%; technical and consulting services 5%; insurance and reinsurance 5%; air tickets, air or sea freight 5%; international telecommunications 5%; land transport within the Kingdom 15%; any other payments 15% ([ZATCA WHT Guideline, May 2026](https://zatca.gov.sa/en/HelpCenter/guidelines/Documents/General-Guideline-for-Withholding-Tax-In-accordance-with-the-provisions-of-the-Income-Tax-Law-and-its-Implementing-Regulations.pdf))  _(Income Tax Law art. 68)_
- **Tax treaty reduction**: Tax treaties (KSA has 50+ DTTs) may reduce rates; reviewer applies treaty.

#### 4.8 GOSI / Saudization gate: Social Insurance Law (Royal Decree M/33, 1421H); Nitaqat Program (Ministerial Decisions)

- **GOSI registration requirement**: Any employer with at least one employee must register with GOSI (General Organization for Social Insurance) and contribute monthly.  _(Social Insurance Law (Royal Decree M/33, 1421H))_
- **GOSI contribution rates for Saudi employees (unverified)**: annuities 9% employer + 9% employee; SANED 0.75% each; occupational hazards 2% employer, giving 11.75% employer and 9.75% employee, wage cap SAR 45,000. The old text said 21% employer, which does not add up. A newer law applies to entrants from 3 July 2024; see `sa-gosi-saudization`  _(Social Insurance Law (Royal Decree M/33, 1421H))_
- **GOSI employer contribution (non-Saudi employees)**: 2% % (occupational hazards only)
- **Nitaqat Saudization requirement**: Required Saudi-employee ratio based on sector + size. New entities: typically first-year exemption (grace period), then must meet sector + size quota. Bands: Platinum / High Green / Medium Green / Low Green / Red. Red band → visa block + work-permit restrictions. Mudad WPS (Wage Protection System) mandatory: payroll must run through approved banks via Mudad portal. → Any employees → route sa-gosi-saudization.  _(Nitaqat Program (Ministerial Decisions))_

#### 4.9 MISA registration gate: Investment Law (Royal Decree M/19, 1446H), which repeals the Foreign Investment Law

- **MISA registration requirement**: A foreign investor registers with the Ministry of Investment before making any investment, then issues the Commercial Registration; the updated law "replaced the licensing procedures with registration" ([MISA](https://misa.gov.sa/activities/laws-regulations-copy/)). Entities formed earlier hold a licence: accept a valid one. If a foreign-owned taxpayer presents at intake without a MISA registration → REFUSE the workflow and route to sa-formation for license + CR setup. Reviewer to engage Saudi corporate counsel.  _(Investment Law (Royal Decree M/19, 1446H), which repeals the Foreign Investment Law)_

#### 4.10 Fiscal year gate: Gregorian vs Hijri

- **Fiscal year basis rule**: Default Gregorian calendar. Unverified: Hijri tax year (lunar, ~354 days) is permitted only for Zakat-only payers (100% Saudi/GCC ownership). Mixed-ownership and CIT-only payers must use Gregorian. Flag inconsistencies to reviewer.

### Section 6: Intake output template

#### 6.1 Human-readable confirmation (shown to user)

```
INTAKE SUMMARY: 2026 Saudi Arabia (KSA)

Taxpayer: [Legal name AR / EN] | CR: [number] | TIN: [10-digit]
VAT No: [15-digit ending 03 | not registered]
MISA registration: [number | N/A | MISSING]
National address (Wasel): [captured | pending]

Entity: [sole est. | s/s LLC | multi-LLC | JSC closed | branch | …]
Ownership: [Saudi % | GCC % | Foreign %] → REGIME: [Zakat only | CIT only | Split]
Fiscal year: [Gregorian calendar | Gregorian non-cal | Hijri]

VAT: [registered | mandatory overdue | voluntary | not required]
Fatoorah Phase 2: [integrated | wave pending | not yet | unknown]
Employees: [count] | Saudi/Non-Saudi: [split] | Nitaqat: [band]
Excise products: [yes | no]
RETT transactions 2026: [yes | no]
Non-resident payments 2026: [yes | no]

DOWNSTREAM SKILLS:
  sa-zakat [if Saudi/GCC share],
  sa-corporate-tax [if foreign share or 100% foreign],
  saudi-arabia-vat [if VAT-registered or overdue],
  saudi-einvoice [if VAT-registered: wave check],
  sa-withholding-tax [if non-resident payments],
  sa-rett [if real estate disposal],
  sa-excise-tax [if excise products],
  sa-gosi-saudization [if employees],
  sa-formation [if MISA missing or entity unclear],
  sa-return-assembly [always last].

OPEN FLAGS, REFUSALS TRIGGERED, CONSERVATIVE DEFAULTS APPLIED: listed below.

Confirm or correct anything above.
```

#### 6.2 Structured intake package (internal JSON for sa-return-assembly)

```json
{
  "jurisdiction": "SA",
  "tax_year": 2026,
  "taxpayer": {
    "legal_name_en": "", "legal_name_ar": "",
    "cr_number": "", "zatca_tin": "", "vat_number": "",
    "misa_registration_number": "",
    "national_address_wasel": "",
    "entity_type": "sole_establishment|single_shareholder_llc|multi_member_llc|jsc_closed|jsc_listed|branch_foreign|simple_joint_partnership",
    "fiscal_year_basis": "gregorian_calendar|gregorian_non_calendar|hijri",
    "fiscal_year_end": ""
  },
  "ownership": {
    "saudi_pct": 0,
    "gcc_pct": 0,
    "foreign_pct": 0,
    "shareholder_register_received": false,
    "ubo_disclosed_zatca": false
  },
  "regime": {
    "zakat_applicable": false,
    "cit_applicable": false,
    "split_regime": false,
    "annual_turnover_sar": 0
  },
  "vat": {
    "registered": false,
    "vat_number_active": false,
    "mandatory_overdue_flag": false,
    "voluntary_eligible": false,
    "trailing12_taxable_supplies_sar": 0
  },
  "einvoice": {
    "phase1_generation_active": false,
    "phase2_integration_wave": "",
    "phase2_integration_live": false
  },
  "employment": {
    "has_employees": false,
    "employee_count": 0,
    "saudi_count": 0,
    "non_saudi_count": 0,
    "gosi_registered": false,
    "mudad_wps_active": false,
    "nitaqat_band": "platinum|high_green|medium_green|low_green|red|unassigned|na"
  },
  "withholding": {
    "paid_non_resident_dividends": false,
    "paid_non_resident_interest": false,
    "paid_non_resident_royalties": false,
    "paid_non_resident_services": false,
    "treaty_review_required": false
  },
  "rett": {
    "real_estate_transactions_2026": false,
    "transaction_count": 0
  },
  "excise": {
    "deals_in_excise_goods": false,
    "excise_registered": false
  },
  "formation": {
    "misa_required_and_missing": false,
    "entity_unclear": false
  },
  "documents_received": [],
  "downstream_skills_to_load": [],
  "open_flags": [],
  "refusals_triggered": [],
  "conservative_defaults_applied": []
}
```

### Section 7: Conservative defaults

When uncertain, prefer the safer (higher-tax / stricter-compliance) outcome and flag. All defaults visible to reviewer in `conservative_defaults_applied`.

**Conservative defaults table**

| Ambiguity | Conservative default |
| --- | --- |
| Ownership % unclear between Saudi/GCC and foreign | Treat as mixed and apply split (both Zakat + CIT); flag to reviewer to confirm with shareholder register |
| GCC corporate owner: look-through unclear | Treat as foreign (CIT); flag for ZATCA ruling |
| Turnover near SAR 375,000 (SAR 350k to 400k) | Assume above threshold → mandatory VAT registration |
| Trailing-12 VAT window unclear | Assume threshold breached in earliest plausible month → backdated registration risk; flag |
| MISA registration status unknown for foreign owner | Assume MISSING → REFUSE workflow; route `sa-formation` |
| Fatoorah Phase 2 wave unknown for VAT-registered | Assume Wave 25 applies if revenue exceeded SAR 187,500 → integration mandatory; flag for ZATCA wave confirmation |
| Fiscal year basis unclear with mixed ownership | Default Gregorian calendar (Hijri not permitted for mixed/foreign) |
| WHT category unclear for non-resident payment | Apply highest plausible rate (e.g., 20% management fees) and flag; treaty applied only with written documentation |
| Nitaqat band unknown | Assume Red until proven; flag visa-block risk |
| Excise inventory status unclear | Assume excise registration required if any excise goods present at year-end |
| RETT exemption claim unclear | Assume 5% RETT applies; flag exemption claim to reviewer |
| GOSI registration status unknown but employees present | Assume not registered → overdue; flag for backdated subscription |
| PE attribution borderline for foreign entity | Assume PE exists → CIT applies; flag for treaty analysis |
| Capital vs expense unclear | Capitalise + flag |

### Section 11: Cross-skill references

**Inputs:** user documents (CR, MISA registration, ZATCA certificate, VAT certificate, bank statements, invoices, GOSI subscriber list, prior returns) + user answers. **Output:** Section 6.2 package consumed by `sa-return-assembly`.

Downstream skills (via sa-return-assembly):

- `sa-zakat`: Zakat at 2.5% on the Zakat base for Saudi/GCC ownership share (Implementing Regulations, Minister of Finance Decision 1007, 1445H, amended by Decision 1248, 1446H).
- `sa-corporate-tax`: CIT 20% on taxable income for foreign ownership share (Income Tax Law, Royal Decree M/1, 1425H).
- `sa-withholding-tax`: WHT on payments to non-residents at 5%-20% per ITL art. 68; treaty rates applied with documentation.
- `sa-rett`: 5% Real Estate Transaction Tax on disposals (Royal Order A/84, 2 October 2020).
- `sa-gosi-saudization`: GOSI subscriptions + Nitaqat band management + Mudad WPS payroll.
- `sa-excise-tax`: Excise on tobacco, energy/soft/sweetened drinks, e-liquids (Royal Decree M/86, 1438H).
- `saudi-arabia-vat`: VAT 15% (Royal Decree M/113, 1438H; Royal Order A/638 of 2020 for rate increase).
- `saudi-einvoice`: Fatoorah Phase 1 generation and Phase 2 integration waves.
- `sa-formation`: MISA registration, CR, ZATCA registration, entity selection.
- `sa-return-assembly`: final orchestrator (Zakat + CIT return, VAT returns, WHT returns, working paper, reviewer brief, action list, payment via SADAD).

## Worked cases

**Case 1: mixed ownership, 60% Saudi and 40% foreign (decision: what is the 2026 liability on each side?).** Zakat base SAR 2,000,000, taxable income SAR 500,000, calendar 2026 fiscal year of 365 days and a 354-day Hijri year. The Zakat percentage is not a flat 2.5%: art. 15 scales it to 365 days. Zakat on the Saudi share is SAR 30,932.20; income tax on the foreign share at 20% is SAR 40,000.

```oa-check
name: Mixed entity, calendar fiscal year
inputs:
  zakat_base: 2000000
  taxable_income: 500000
  saudi_share: 0.6
steps:
  - zakat_rate: 0.025 / 354 * 365
  - zakat: zakat_base * saudi_share * zakat_rate
  - income_tax: taxable_income * (1 - saudi_share) * 0.20
expected:
  zakat: 30932.20
  income_tax: 40000.00
```

**Case 2: which withholding rate?** A resident pays a non-resident SAR 600,000 of royalties and SAR 200,000 of management fees, with no treaty relief. Royalties 15% is SAR 90,000; management fees 20% is SAR 40,000.

```oa-check
name: Non-resident payments
inputs:
  royalties: 600000
  management_fees: 200000
steps:
  - wht: royalties * 0.15 + management_fees * 0.20
expected:
  wht: 130000.00
```

### Section 10: Final handoff to sa-return-assembly

Once gap-filling and self-checks pass, output a short handoff message naming (a) taxpayer + entity + CR + TIN + ownership split, (b) regime selected (Zakat / CIT / split) with the headline computation citation, (c) downstream skills in run-order, (d) skills explicitly not running and why, (e) reviewer reminder (SOCPA CPA or ZATCA-registered tax adviser sign-off). Then invoke `sa-return-assembly` with the Section 6.2 package.

Example (single-shareholder LLC, 100% Saudi-owned, VAT-registered, 4 employees):

> Intake complete. Al-Salam Trading LLC, single-shareholder LLC, CR 1010XXXXXX, TIN 30012345XX, VAT 30012345XX0003, Riyadh national address active. 100% Saudi-owned natural person → Zakat-only. 2026 turnover SAR 2.4 million. VAT-registered (mandatory), Fatoorah Phase 1 active, not yet in Phase 2 wave (verify). 4 Saudi employees, GOSI active, Mudad WPS live, Nitaqat Medium Green. No real estate disposals, no excise products, no non-resident payments. Fiscal year Gregorian calendar. Running: sa-zakat (2.5% on Zakat base), saudi-arabia-vat, saudi-einvoice (wave check), sa-gosi-saudization, sa-return-assembly. Not running: sa-corporate-tax, sa-withholding-tax, sa-rett, sa-excise-tax, sa-formation. Needs SOCPA-licensed Saudi CPA sign-off before ZATCA submission. Handing off now.

Example (mixed-ownership multi-member LLC, 60% Saudi + 40% foreign, with MISA):

> Intake complete. Gulf Tech Solutions LLC, multi-member LLC, CR 1010YYYYYY, TIN 30099999XX, VAT 30099999XX0003, MISA registration 102030XX. Ownership: 60% Saudi national / 40% foreign → SPLIT regime: 60% share Zakat, 40% share CIT 20%. 2026 turnover SAR 18 million. VAT-registered (mandatory), Fatoorah Phase 2 Wave [X] live. 22 employees (12 Saudi / 10 non-Saudi), Nitaqat High Green. Paid foreign software licensor SAR 600k (royalty WHT 15%) and foreign management fees SAR 200k (WHT 20%): treaty review required. No real estate transactions, no excise. Fiscal year Gregorian calendar (Hijri not permitted with foreign ownership). Running: sa-zakat (Saudi share), sa-corporate-tax (foreign share), saudi-arabia-vat, saudi-einvoice, sa-withholding-tax, sa-gosi-saudization, sa-return-assembly. Not running: sa-rett, sa-excise-tax, sa-formation. Needs SOCPA CPA + treaty-qualified tax adviser sign-off before ZATCA submission. Handing off now.

## When to refuse or refer


Refusals fire from the refusal sweep or during inference. Protocol: stop the workflow, state the reason in one sentence, recommend a ZATCA-registered tax adviser or SOCPA-licensed CPA, do not work around.

In-scope refusals:

- Pre-formation taxpayer with no CR → `sa-formation` only.
- Foreign-owned entity with no valid MISA registration → `sa-formation` only; corporate counsel required.
- Non-resident with no PE in KSA → out of scope (WHT applies but is the payer's obligation).
- Listed JSC with public free float → SOCPA CPA + ZATCA large-taxpayer office.
- Oil, gas, or hydrocarbon producers → refuse (special CIT rates 20%-85%; specialist regime).
- Banks, insurers, financial institutions → refuse (sector-specific Zakat/CIT rules + SAMA supervision).
- Groups with transfer-pricing complexity (above SAR 6 million of arm's length value in 12 months for Master File and Local File; above SAR 3.2 billion group revenue for CbCR) → refuse; specialist transfer-pricing adviser required.
- Listed JSC with free-float Zakat/CIT proportional treatment → refuse.

Sample: "Stop: you have foreign ownership but no MISA investment registration on file. A MISA registration must be issued before the Commercial Registration for any foreign-owned KSA entity. Without it, the entity cannot legally operate or file with ZATCA. Engage Saudi corporate counsel and the Ministry of Investment first; I will route you to `sa-formation`."

## Completion checklist


Run all 16 before invoking `sa-return-assembly`. Any failure → fix, do not hand off.

1. Refusal sweep used `ask_user_input_v0`, not prose.
2. KSA residence / CR / ZATCA registration confirmed.
3. Entity type set.
4. Ownership %s captured (Saudi / GCC / foreign), summing to 100%.
5. Regime split decided (Zakat / CIT / both) with reason traced to ownership %.
6. MISA registration verified for any foreign-owned entity (number captured).
7. Turnover recorded in SAR with bucket band.
8. VAT status set; `mandatory_overdue_flag` set if turnover ≥ SAR 375,000 and not registered.
9. Fatoorah Phase 1 confirmed for all VAT-registered; Phase 2 wave noted.
10. Employee count + Saudi/non-Saudi split + Nitaqat band captured if employees present.
11. GOSI + Mudad WPS status set.
12. Excise registration set if dealing in excise goods.
13. RETT transactions in 2026 captured.
14. WHT obligations checked; `sa-withholding-tax` in list if applicable.
15. Fiscal year basis captured (Gregorian / Hijri); Hijri rejected for mixed/foreign.
16. All conservative defaults recorded with citation; reviewer disclaimer present in opening + handoff.

## Legal instruments named in this skill


Primary statutes, royal decrees, and ZATCA regulations cited (citation list, kept for reference; the table under Sources says what was opened):

- **Royal Decree M/1, 1425H**: Income Tax Law (ITL).
- **Implementing Regulations of the Income Tax Law**: Ministerial Resolution 1535, 1425H, as amended.
- **Minister of Finance Decision 1007, 1445H, amended by Decision 1248, 1446H**: Zakat Implementing Regulations.
- **Royal Decree M/113, 1438H**: Value Added Tax Law.
- **VAT Implementing Regulations**: ZATCA Board Resolution 3839, 1438H, as amended.
- **Royal Order A/638, 2020**: increase of VAT standard rate to 15% from 1 July 2020.
- **Royal Decree M/86, 1438H**: Excise Tax Law.
- **Royal Order A/84, 2 October 2020**: Real Estate Transaction Tax (RETT) 5% Regulation.
- **Royal Decree M/33, 1421H**: Social Insurance Law (GOSI).
- **Royal Decree M/19, 1446H, Investment Law, repealing the Foreign Investment Law**: Foreign Investment Law (MISA framework).
- **ZATCA E-Invoicing Regulation, December 2020**: Fatoorah Phase 1 (Generation) and Phase 2 (Integration).
- **ZATCA Transfer Pricing Bylaws, 15 February 2019** (and amendments): TP documentation thresholds, CbCR.
- **Companies Law, Royal Decree M/132, 1443H (effective January 2023)**: sole establishment, LLC, JSC, simple joint partnership, branch.
- **Council of Ministers Resolution, 4 October 2020**: RETT replacing VAT on real estate.
- **Ministerial Decisions on Nitaqat (various, MHRSD)**: Saudization bands and quotas.
- **Mudad WPS Regulations (MHRSD / SAMA)**: Wage Protection System.
- **Saudi GCC VAT Framework Agreement, 2017**: basis for VAT Law.
- **Bilateral Double Tax Treaties (DTTs)**: 50+ treaties; treaty rates verified case-by-case by reviewer.

## Change log

- **v1.0 (May 2026):** Initial intake skill for the Saudi Arabia freelance / SME workflow. Routes to sa-zakat, sa-corporate-tax, sa-withholding-tax, sa-rett, sa-gosi-saudization, sa-excise-tax, saudi-arabia-vat, saudi-einvoice, sa-formation, sa-return-assembly. Reflects Income Tax Law (M/1, 1425H), Zakat Implementing Regulations (Decision 1007, 1445H), VAT Law (M/113, 1438H) at 15%, RETT (A/84, 2020) at 5%, Fatoorah e-invoicing (Phase 1 mandatory, Phase 2 wave-based), MISA registration requirement for foreign owners, and Nitaqat Saudization framework for tax year 2026.

- **v1.1 (November 2026):** Moved to tax year 2026 and the method shape. Corrected the Zakat regulation, Zakat percentage, withholding rates, GOSI arithmetic, Investment Law registration and Wave 25. Dropped duplicated runbook lines and the old booking link block.

## Sources

| Source | URL | Read on |
|---|---|---|
| Read in full text: Implementing Regulations for Zakat Collection 1445 H, Minister of Finance Decision 1007, amended by Decision 1248: arts. 1, 3, 15, 27, 102, 106, 110 | https://zatca.gov.sa/en/RulesRegulations/Documents/ZAKAT%20COLLECTION.pdf | 2026-11-01 |
| Read in full text: ZATCA, Taxpayers' Obligations: Zakat and Returns Calendar 2026 | https://zatca.gov.sa/en/MediaCenter/Publications/Documents/Zakat%20Declaration%20and%20Tax%20Returns%20Calendar%20(EN).pdf | 2026-11-01 |
| Read in full text: ZATCA, General Guideline for Withholding Tax, second version, May 2026 | https://zatca.gov.sa/en/HelpCenter/guidelines/Documents/General-Guideline-for-Withholding-Tax-In-accordance-with-the-provisions-of-the-Income-Tax-Law-and-its-Implementing-Regulations.pdf | 2026-11-01 |
| Read in full text: ZATCA, Simplified Guideline for Income Tax, second version, May 2026 | https://zatca.gov.sa/en/HelpCenter/guidelines/Documents/Simplified-Guideline-for-Income-Tax.pdf | 2026-11-01 |
| Read in full text: ZATCA, Taxation Violation Fines (VAT) | https://zatca.gov.sa/en/RulesRegulations/VAT/Pages/Penalties.aspx | 2026-11-01 |
| Read in full text: ZATCA, VAT returns for September and Q3 2026 | https://zatca.gov.sa/en/MediaCenter/News/Pages/Submit-VAT-Return-for-Oct-andQ3-2026.aspx | 2026-11-01 |
| Read in full text: ZATCA, Wave 25 e-invoicing criteria | https://zatca.gov.sa/en/MediaCenter/News/Pages/Wave25-E-invoicing.aspx | 2026-11-01 |
| Read in full text: ZATCA, excise regulation amendments from 1 January 2026 (Arabic) | https://zatca.gov.sa/en/MediaCenter/News/Pages/excise-tax-regulation-2026.aspx | 2026-11-01 |
| Read in full text: ZATCA, Simplified Guide on cancellation of fines, as of 1 July 2026 | https://zatca.gov.sa/en/HelpCenter/guidelines/Documents/Cancellation-of-Fines-Exemption%20of-Financial-Penalties.pdf | 2026-11-01 |
| Read in full text: Ministry of Investment, updated Investment Law page | https://misa.gov.sa/activities/laws-regulations-copy/ | 2026-11-01 |

Not yet confirmed: the Income Tax Law and its Implementing Regulations were not opened directly (laws.boe.gov.sa did not connect), so articles are cited through the ZATCA guidelines above, and the English guidelines defer to the Arabic text. Also unconfirmed, and carried only where marked unverified: VAT thresholds of SAR 375,000 and SAR 187,500; Wave 24 criteria (seen in a search extract, page not opened); GOSI rates and the phase-in for new entrants; excise rates and sugar tier amounts; RETT rate, exemptions and the instrument number (the old text gave both Royal Order A/84 and Royal Decree M/84); interest limit, loss carry-forward and specialised oil and gas rates; audited accounts threshold; extension practice; refund timing; income tax record retention; Hijri year eligibility; treatment of GCC corporate owners and listed float; Nitaqat bands (the old skills disagree on Yellow); Investment Law in-force date; form names such as Form 800.

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
