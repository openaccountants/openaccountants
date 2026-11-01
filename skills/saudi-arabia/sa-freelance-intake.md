---
name: sa-freelance-intake
description: Use this Guide to collect and reconcile the facts needed for a Saudi Arabia freelance or SME tax and Zakat workflow for tax year 2026. It covers resident sole establishments, privately held companies, foreign-owned companies and branches, records ownership and fiscal periods, checks registration evidence, and identifies VAT, withholding, real estate, excise, employment and e-invoicing workstreams. Trigger on Saudi business intake, ZATCA registration, mixed ownership, MISA registration, Fatoorah or Saudi compliance. It produces a documented intake package for sa-return-assembly and a qualified Saudi reviewer. Missing facts and unconfirmed legal rules remain explicit holds; this Guide does not submit returns.
jurisdiction: SA
version: 1.3
tax_year: 2026
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# SA Freelance Intake v1.3

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope


The intake orchestrator for Saudi-resident self-employed individuals, sole establishments (mu'assasah fardiyyah), single-shareholder LLCs, multi-member LLCs, joint-stock companies (JSC), and branches of foreign companies registered with ZATCA in the Kingdom of Saudi Arabia (KSA). Every downstream Saudi content skill depends on this skill producing a structured intake package first.

Job: establish the facts, document candidate Zakat/CIT allocation, identify the other workstreams, and hand off a package with explicit holds. Outputs go to a professional authorised for the work in Saudi Arabia. A membership name alone does not establish filing authority. Do not finalise a held tax position.


## Ask the client first

### Section 5: Six facts that change the route

Use structured questions where the host supports them. Read the documents first and ask only for missing facts. These six groups preserve the earlier Q1 to Q14 topics without treating a turnover estimate or missing certificate as a legal conclusion.

1. **Status and entity:** Where is the person resident, what business is carried on, what legal form and CR/ZATCA registrations exist, and is there a Saudi PE? Obtain residence and establishment evidence. Pre-formation goes to `sa-formation`; listed companies and special sectors go to a specialist.
2. **Owners and investment registration:** Obtain the shareholder register, direct and indirect nationalities, percentages and any change dates. Obtain MISA registration or existing licence and the activity. Unknown ownership or MISA status is a HOLD for classification, not a deemed foreign owner or an automatic bar to filing.
3. **Revenue and VAT:** Obtain actual monthly taxable supplies, exempt and outside-scope amounts, taxable expenses, forecasts and the VAT certificate. An estimated SAR 350,000 to 400,000 is insufficient to decide registration. HOLD that decision and route to `saudi-arabia-vat` for the current-law test.
4. **Fiscal period and prior filings:** Obtain the registered start/end dates, actual day counts, Hijri/Gregorian basis, prior returns, payments, assessments and approvals. Do not reject a Hijri period or substitute a Gregorian year because an owner is foreign.
5. **Payments and transactions:** Identify non-resident suppliers, lenders, licensors and service providers; obtain contracts, payment dates, Saudi-source/PE facts and treaty documents. Capture all real estate transfers, including gifts and inheritance, and all excise goods including imports, production and inventory. Route for review without assuming liability or exemption.
6. **Employees and e-invoicing:** Capture Saudi/non-Saudi headcounts, GOSI evidence, Mudad/WPS records, actual Nitaqat result, electronic-invoice status and the taxpayer's ZATCA Phase 2 notice. Unknown status stays unknown, never deemed Red or overdue.

**Routing decision record:** For each workstream record `candidate`, `supported`, `hold` or `out_of_scope`, the facts, source and reviewer needed. A candidate route requests legal verification and computation; it is not a finding that the upstream Guide is correct. The ten named-contributor Guides have not been reviewed by this revision.

### Section 3: Required inputs

Infer applicable facts from documents and ask for remaining facts. Record inapplicable items and unresolved evidence separately. An unresolved applicable fact blocks only its dependent conclusion; a partial handoff remains available.

- **Identity / registration:** legal name (Arabic + English), Commercial Registration (CR) number, ZATCA Tax Identification Number (TIN as shown on the certificate), VAT registration number (registration number copied from the certificate if registered), MISA investment registration evidence where applicable after the existing-investor, securities and other exceptions in Section 4.9 are checked, national address (Wasel).
- **Entity:** sole establishment (mu'assasah fardiyyah) / single-shareholder LLC / multi-member LLC / JSC / branch of foreign company / simple joint partnership. CR issuance date. Bylaws / Articles of Association.
- **Ownership:** complete shareholder register with nationality (Saudi national / GCC national / foreign) and ownership % each. Beneficial ownership disclosure (UBO file at ZATCA).
- **Fiscal year:** Capture the registered period, calendar basis, start/end dates, day counts and approvals. HOLD any change or eligibility conclusion until the applicable current rules and taxpayer evidence are verified.
- **Revenue:** 2026 annual turnover (SAR), monthly breakdown, domestic vs export mix, exempt vs zero-rated vs standard-rated for VAT.
- **Tax history:** prior Zakat return, prior CIT return (if applicable), prior VAT returns (monthly or quarterly), prior WHT returns, outstanding ZATCA assessments or appeals.
- **Operational:** employee count (Saudi vs non-Saudi headcount for Nitaqat), GOSI registration status, Mudad WPS active, current Nitaqat band (Platinum / High Green / Medium Green / Low Green / Red), Fatoorah Phase 2 wave assignment.
- **Documents:** CR, MISA registration, ZATCA tax certificate, VAT certificate, bank statements 2026, sales tax invoices (Phase 2-compliant if integrated wave), purchase invoices, GOSI subscriber report, prior Zakat/CIT/VAT/WHT returns, payment receipts (SADAD).

## The method, step by step

### Rates, bands and thresholds

| Item | Amount | Tax year | Source |
|---|---|---|---|
| Zakat, Hijri year | 2.5% of the applicable Zakat base for an ordinary full Hijri year | 2026 | Regulations art. 15, https://zatca.gov.sa/en/RulesRegulations/Documents/ZAKAT%20COLLECTION.pdf |
| Zakat, other fiscal year | 2.5% / actual Hijri-year days x actual fiscal-year days; commencement, cessation and mergers require arts. 14 to 15 review | 2026 | same |
| General income tax | 20% on taxable income allocated to the non-Saudi share of a resident capital company, or the covered non-Saudi resident business / Saudi PE; special sectors excluded | 2026 | ZATCA Income Tax Guideline sections 1, 2 and 4, PDF pp. 4 to 5: https://zatca.gov.sa/en/HelpCenter/guidelines/Documents/Simplified-Guideline-for-Income-Tax.pdf |
| WHT management fees, when the scope test below is met | 20% | 2026 | https://zatca.gov.sa/en/HelpCenter/guidelines/Documents/General-Guideline-for-Withholding-Tax-In-accordance-with-the-provisions-of-the-Income-Tax-Law-and-its-Implementing-Regulations.pdf |
| WHT royalties; land transport within the Kingdom; residual other payments, after category/scope review | 15% | 2026 | same |
| WHT dividends, rent, loan charges, insurance/reinsurance, technical and consulting services, air tickets or air/sea freight, international telecoms, subject to definitions and exclusions below | 5% | 2026 | same |
| VAT monthly filing | annual supplies over SAR 40 million | 2026 | https://zatca.gov.sa/en/MediaCenter/News/Pages/Submit-VAT-Return-for-Oct-andQ3-2026.aspx |
| E-invoicing Wave 25 | VAT-liable revenue over SAR 187,500 in any of 2022 to 2025; integrate by 1 February 2027 | 2026 | https://zatca.gov.sa/en/MediaCenter/News/Pages/Wave25-E-invoicing.aspx |
| VAT registration decision | HOLD pending current threshold and scope verification; no numeric default | 2026 | unverified |
| VAT voluntary eligibility | HOLD; taxable expenses and non-resident rules also require review | 2026 | unverified |

Apply a domestic rate only after confirming a resident payer or Saudi PE, a payment to a non-resident, a Saudi income source, the precise payment category and any PE connection, exclusion, exemption or documented treaty claim. [ZATCA WHT Guideline, sections 2 to 5](https://zatca.gov.sa/en/HelpCenter/guidelines/Documents/General-Guideline-for-Withholding-Tax-In-accordance-with-the-provisions-of-the-Income-Tax-Law-and-its-Implementing-Regulations.pdf). The table is not a rate-selection default. Unknown category means HOLD the calculation, never choose the highest rate. Natural-person payer rules cover activity-related payments, not personal consumption. Exclusions include relevant oil/gas investment dividends and specified telecom network/roaming payments. Interbank loan returns require the specific maximum-90-day and certified-statement conditions; freight definitions exclude inbound shipping to Saudi ports. Payments connected with a recipient's Saudi PE and capital gains need the separate income-tax treatment. Read the category definition and any treaty before the rate, not after.

### Section 1: Quick reference: regime decision tree at a glance

0. **Candidate annual Zakat/CIT route**: apply Sections 4.1 and 4.2 residence/activity and ownership conditions, including GCC similar-treatment eligibility. Do not infer Zakat-only treatment from nationality alone; indirect/GCC corporate and listed allocation stays HOLD. Other tax workstreams are separate.

### Section 2: Workflow runbook (order of operations)

0. **Opening**: One-line greeting + flow summary + reviewer reminder, then launch the refusal sweep.
0. **Scope and missing-fact sweep**: use the six question groups in Section 5, asking only what the documents have not answered; preserve a partial handoff and explicit holds.
0. **Document dump**: Ask user to upload everything at once (CR, MISA registration evidence if applicable under Section 4.9, ZATCA certificate, VAT certificate, bank statements, sales invoices, purchase invoices, GOSI subscriber list, prior Zakat/CIT returns, prior VAT returns).
0. **Inference pass**: Parse every document; extract turnover, ownership %, employee count, prior payments, fiscal year basis.
0. **Regime classification**: Apply Section 4 split logic using inferred ownership + sweep answers.
0. **Confirmation**: Show inferred summary + proposed regime split + downstream-skill list; invite corrections.
0. **Gap filling**: ask_user_input_v0 only for items documents cannot answer (Hijri vs Gregorian election, MISA registration number, Nitaqat color band).
0. **Handoff**: Produce Section 6 summary and invoke sa-return-assembly.

### Section 4: Regime decision tree with thresholds and citations

Thresholds for 2026. Figures not marked to a source are listed under Not yet confirmed.

#### 4.1 Residency and business gate

Establish residence rather than equating a CR or PE with residence. For Zakat, art. 4 distinguishes individuals (permanent residence plus at least 30 days, or at least 183 days) and legal persons (Saudi incorporation or principal headquarters). A foreign PE is an income-tax scope route, not proof of Saudi residence. [Zakat Regulations arts. 1, 3 to 4, PDF pp. 3 to 9](https://zatca.gov.sa/en/RulesRegulations/Documents/ZAKAT%20COLLECTION.pdf); [Income Tax Guideline sections 1 to 2, PDF p. 4](https://zatca.gov.sa/en/HelpCenter/guidelines/Documents/Simplified-Guideline-for-Income-Tax.pdf). A non-resident with no PE is outside this resident-business workflow; do not assert that WHT is their only possible liability. Capital gains and non-resident VAT need separate review, as the [WHT Guideline section 1.1.1, PDF p. 8](https://zatca.gov.sa/en/HelpCenter/guidelines/Documents/General-Guideline-for-Withholding-Tax-In-accordance-with-the-provisions-of-the-Income-Tax-Law-and-its-Implementing-Regulations.pdf) makes clear.

#### 4.2 Ownership-nationality gate: the Zakat/CIT split

For an ordinary resident privately held capital company, identify the Saudi share under Zakat Regulations arts. 1 and 3 and the non-Saudi share under Income Tax Guideline sections 1 to 2. "Saudi" includes GCC nationals accorded similar treatment. Route the applicable share to `sa-zakat` or `sa-corporate-tax`; mixed ownership requires separate supported bases and allocation, not one base used twice. [Zakat Regulations](https://zatca.gov.sa/en/RulesRegulations/Documents/ZAKAT%20COLLECTION.pdf); [Income Tax Guideline](https://zatca.gov.sa/en/HelpCenter/guidelines/Documents/Simplified-Guideline-for-Income-Tax.pdf). Natural-person business status requires its own residence/activity test.

Use art. 15's rate in the table after the upstream base has been legally checked. Do not treat the rate as proof that all assets, deductions or exemptions have been tested. Ownership at year-end and changes are reviewed under art. 13. **HOLD:** indirect/GCC corporate look-through, listed founder/free-float allocation, consolidated or special-sector treatment. Do not classify an unclear GCC corporate shareholder as foreign by default. Listed companies, oil/gas, banks, insurers and special regimes need specialist review; no specialised rate is selected here.

#### 4.3 VAT registration gate

**NON-OPERATIVE HOLD:** the earlier mandatory/voluntary thresholds and rate/exemption lists are not instructions in this Guide. Obtain actual taxable supplies and expenses and the registration certificate; route to `saudi-arabia-vat` for a current-law test of resident and non-resident scope, rolling/forward periods, voluntary expense eligibility, registration dates, standard/zero/exempt treatment and the threshold itself. Do not mark registration mandatory, voluntary, forbidden or overdue from an estimated turnover band, and do not backdate a registration from the earliest plausible month. An already registered taxpayer routes to VAT reconciliation and e-invoicing review.

For a registered taxpayer, the current ZATCA notice distinguishes monthly supplies exceeding SAR 40 million from quarterly supplies not exceeding that amount. This is a periodicity test, not a registration threshold. [ZATCA 2026 VAT filing notice](https://zatca.gov.sa/en/MediaCenter/News/Pages/Submit-VAT-Return-for-Oct-andQ3-2026.aspx).

#### 4.4 E-invoicing gate: Fatoorah

For taxpayers subject to the E-invoicing Regulation, Phase 1 began on 4 December 2021. Wave 25 includes taxpayers with VAT-liable revenue **exceeding** SAR 187,500 in any of 2022, 2023, 2024 or 2025, with integration by 1 February 2027. ZATCA says later waves are notified at least six months before their date. [ZATCA Wave 25 announcement, complete article](https://zatca.gov.sa/en/MediaCenter/News/Pages/Wave25-E-invoicing.aspx). Obtain the taxpayer's notice and route `saudi-einvoice`. If the notice or historical revenue is unknown, HOLD the wave conclusion. No deemed Wave 25 or earlier-wave conclusion is made from 2026 turnover. **HOLD:** the former Wave 1/Wave 24 numbers, invoice-type-specific QR/clearance/reporting rules, API and cryptographic specifications pending their own source review.

#### 4.5 Excise gate

Collect the goods list, product composition, imports, manufacturing and inventory records and route `sa-excise-tax`. The [official Arabic announcement](https://zatca.gov.sa/en/MediaCenter/News/Pages/excise-tax-regulation-2026.aspx) states the sweetened-drink method changes from a flat retail-price percentage to graduated total-sugar bands per 100 ml of ready-to-drink product from 1 January 2026. **HOLD:** individual rates, tier amounts, registration triggers and due dates outside the cited 2026 calendar. Inventory presence alone does not establish registration liability; no excise figure is computed here.

#### 4.6 Real estate transaction gate

Collect every sale, transfer, long lease, contribution, gift and inheritance with deed/date/value/parties and route `sa-rett`. **NON-OPERATIVE HOLD:** the earlier flat-rate assumption, exemptions, first-home limit, notarisation deadline and inconsistent royal-instrument numbers. Do not exclude an inheritance or family transfer from review or assume the tax because an exemption is unclear. No RETT liability or exemption is determined here.

#### 4.7 Withholding gate

Apply a domestic rate only after confirming a resident payer or Saudi PE, a payment to a non-resident, a Saudi income source, the precise payment category and any PE connection, exclusion, exemption or documented treaty claim. [ZATCA WHT Guideline, sections 2 to 5](https://zatca.gov.sa/en/HelpCenter/guidelines/Documents/General-Guideline-for-Withholding-Tax-In-accordance-with-the-provisions-of-the-Income-Tax-Law-and-its-Implementing-Regulations.pdf). The table is not a rate-selection default. Unknown category means HOLD the calculation, never choose the highest rate. Natural-person payer rules cover activity-related payments, not personal consumption. Exclusions include relevant oil/gas investment dividends and specified telecom network/roaming payments. Interbank loan returns require the specific maximum-90-day and certified-statement conditions; freight definitions exclude inbound shipping to Saudi ports. Payments connected with a recipient's Saudi PE and capital gains need the separate income-tax treatment. Read the category definition and any treaty before the rate, not after.

Document each contract and classify the payment before using the rates table. Important neighbouring rules: capital gains are not automatically WHT; payments connected with a recipient's Saudi PE belong in that PE's income-tax computation; oil/gas investment dividends and specified telecom network/roaming payments have exclusions. Loan-charge interbank exclusions and air/sea freight definitions require the category's exact source test. [WHT Guideline definitions, sections 1 to 5, PDF pp. 5 to 7, 8 to 29 and 31](https://zatca.gov.sa/en/HelpCenter/guidelines/Documents/General-Guideline-for-Withholding-Tax-In-accordance-with-the-provisions-of-the-Income-Tax-Law-and-its-Implementing-Regulations.pdf). Treaty reduction requires the actual treaty and procedure; no blanket certificate rule or treaty count is assumed. Unclear category or treaty claim remains a HOLD. Route `sa-withholding-tax` as a verification request, not automatic acceptance of its output.

#### 4.8 GOSI / Saudization / WPS gate

Collect employees, nationality, start dates, registration evidence, contribution statements, payroll bank records, Mudad/WPS submissions and actual Nitaqat result; route `sa-gosi-saudization`. **NON-OPERATIVE HOLD:** all earlier contribution percentages, caps, new-entrant phase-in, headcount thresholds, grace periods, band consequences and salary/reporting deadlines. Do not deem unknown registration overdue or an unknown band Red. A complete payroll pack is evidence collection, not a labour-law compliance certificate.

#### 4.9 MISA investment registration gate

Investment Law art. 7(2) requires a foreign investor to register before investment and expressly excludes securities governed by the Capital Market Law. MISA's FAQ 2.2 describes completed registration before CR/other licences; FAQ 2.4 says existing investors have no additional compliance requirements under the update. The law also preserves sectoral/zone regimes and acquired rights in art. 14. [Investment Law, arts. 1, 7 to 8, 14 to 16](https://misa.gov.sa/app/uploads/2024/08/Investment-Law.pdf); [MISA Q&A 2.2 to 2.4](https://misa.gov.sa/activities/laws-regulations-copy/); [Implementing Regulations arts. 11 to 13](https://misa.gov.sa/app/uploads/2025/06/THE-INVESTMENT-LAW-IMPLEMENTING-REGULATIONS.pdf).

Request registration or legacy licence and status evidence. Missing evidence is a **HOLD on the investment-compliance conclusion**, routed to `sa-formation` and Saudi counsel. Do not declare an existing business illegal, unable to file, or automatically refused solely because the intake lacks a new registration number. Do not change an existing tax filing deadline while this evidence is obtained. **HOLD:** universal pre-CR rule for every investor category, licence-transition details and the exact law commencement date.

#### 4.10 Fiscal year gate

Record the registered Hijri/Gregorian period and actual days. Zakat Regulations art. 1 defines a Zakat year irrespective of calendar, and art. 15 provides the day-count calculation; neither is a rule that foreign ownership prohibits Hijri periods. **NON-OPERATIVE HOLD:** that earlier eligibility/refusal rule and any default substitution of a Gregorian calendar. Obtain the current income-tax year rules and taxpayer approvals before changing a period or asserting eligibility. Keep ordinary elapsed-day deadline computation separate from calendar eligibility. [Zakat Regulations arts. 1 and 15](https://zatca.gov.sa/en/RulesRegulations/Documents/ZAKAT%20COLLECTION.pdf).

### Section 6: Intake output template

#### 6.1 Human-readable confirmation (shown to user)

```
INTAKE SUMMARY: 2026 Saudi Arabia (KSA)

Taxpayer: [Legal name AR / EN] | CR: [number] | TIN: [as certified]
VAT No: [registration number copied from the certificate | not registered]
MISA: [registration / existing licence evidence | supported exception | HOLD]
National address (Wasel): [captured | pending]

Entity: [sole est. | s/s LLC | multi-LLC | JSC closed | branch | …]
Ownership: [Saudi % | GCC % | Foreign %] → REGIME: [Zakat only | CIT only | Split]
Fiscal year: [Gregorian calendar | Gregorian non-cal | Hijri]

VAT: [certificate evidence | legally verified decision | HOLD]
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

OPEN FLAGS, LEGAL HOLDS, SCOPE REFERRALS: listed below. No default establishes liability.

Confirm or correct anything above.
```

#### 6.2 Structured intake package (internal JSON for sa-return-assembly)

The JSON is a field schema example, not findings. Replace absent amounts, percentages and statuses with `null`; replace false/zero example values only from evidence. Add `legal_holds` with affected field, missing proof, reviewer and source needed. Existing field names are retained for interoperability.

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

### Section 7: Missing facts and non-operative holds

Unknown is not a higher-tax fact. Use `open_flags` for missing evidence and keep any related computation unavailable. The legacy `conservative_defaults_applied` field remains for compatibility, but no assumed legal facts belong in it.

| Missing or unclear topic | Required treatment |
|---|---|
| Saudi/GCC/foreign ownership or GCC corporate look-through | HOLD the classification; obtain the register, chain and current treatment |
| VAT taxable supplies, expenses, window or threshold | HOLD registration/effective date; do not turn an estimated range into mandatory registration |
| MISA registration or legacy licence | HOLD investment compliance; obtain evidence and counsel review without asserting a tax-filing bar |
| E-invoicing wave | HOLD wave determination; obtain the actual notice and historical taxable revenue |
| Hijri/Gregorian basis or eligibility | Keep the recorded basis; HOLD any change; do not reject Hijri for foreign ownership |
| WHT category, PE link or treaty | HOLD the rate and claim; do not default to management fees |
| GOSI, WPS or Nitaqat status | HOLD compliance conclusion; do not deem Red, unregistered or overdue |
| Excise goods or RETT exemption | Capture facts and route; do not assume registration or a flat tax |
| PE attribution, capital/expense or other deduction | HOLD the tax treatment for current-law and document review |

### Section 11: Cross-skill references

**Inputs:** user documents (CR, MISA registration, ZATCA certificate, VAT certificate, bank statements, invoices, GOSI subscriber list, prior returns) + user answers. **Output:** Section 6.2 package consumed by `sa-return-assembly`.

Downstream Guides are workstream destinations, not incorporated legal authority. Request the calculation, supporting documents, exact legal citation and checked period from each: `sa-zakat` (base and ownership); `sa-corporate-tax` (income tax, deductions, losses and PE); `sa-withholding-tax` (source, category and treaty); `sa-rett` (property transactions); `sa-gosi-saudization` (employment); `sa-excise-tax` (goods and sugar tiers); `saudi-arabia-vat` (registration, rates, exemptions and returns); `saudi-einvoice` (notice and implementation); `sa-formation` (entity and investment evidence). `sa-return-assembly` receives the resulting package and all holds last. This revision does not attest to the contents of those ten Guides.

## Worked cases

**Case 1: mixed ownership, 60% Saudi and 40% foreign (decision: what is the 2026 liability on each side?).** Zakat base SAR 2,000,000, taxable income SAR 500,000, calendar 2026 fiscal year of 365 days and a 354-day Hijri year. Assume independently checked, unapportioned ordinary-company bases and established day counts, with no short-period, merger or specialised rule. Art. 15 scales the Zakat percentage to 365 days. Zakat on the Saudi share is SAR 30,932.20; income tax on the foreign share at 20% is SAR 40,000.

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

**Case 2: which withholding rate?** A resident company pays a non-resident SAR 600,000 of Saudi-source royalties and SAR 200,000 of Saudi-source management fees, with no recipient-PE connection, exclusion, exemption or treaty relief and with both categories supported by contracts. Royalties 15% is SAR 90,000; management fees 20% is SAR 40,000.

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

Output taxpayer, entity, CR/TIN from certificates, ownership with evidence, registered fiscal period, candidate workstreams and the basis for each. List workstreams not run with reasons and all holds; no amount is labelled final while its facts or law are held. Then invoke `sa-return-assembly` for a partial or complete reviewer package as appropriate. Do not label a taxpayer's VAT registration mandatory or investment compliance complete from turnover or a number alone.

**Handoff format:** "Intake package for [entity], [period]. Supported routes: [list with citations]. Evidence still required: [list]. Legal holds: [list]. Computations unavailable because of holds: [list]. Remaining upstream work: [list]. Professional authorisation and sign-off required before any filing."

## When to refuse or refer

Stop the affected conclusion, continue independent evidence collection, and name the missing fact or legal check. Pre-formation routes to `sa-formation`. Listed companies, oil/gas, banks, insurers, funds, zones, RHQ, complex PE/treaty or related-party cases go to a professional with the relevant Saudi authority and expertise. These are workflow scope limits, not assertions of a particular rate, threshold or filing exemption. Missing MISA evidence and a Hijri year are holds for review, never automatic findings of illegality or ineligibility. Do not submit anything through this Guide.

## Completion checklist


Complete these before a final handoff. If something is missing, hand over a partial package with the affected line held.

1. Residence, legal form, CR/TIN and registered period trace to documents.
2. Shareholder percentages reconcile to 100%; indirect/GCC/listed issues are supported or held.
3. Each candidate workstream has facts and a source; unknown facts remain unknown.
4. VAT registration, excise, RETT, GOSI, WPS and Nitaqat conclusions are supported separately or held.
5. MISA evidence and transition/scope exceptions are checked or held; no unsupported filing prohibition is asserted.
6. WHT categories, PE connections, exclusions and treaty claims are documented before rates.
7. E-invoicing notice and historical revenue are recorded; no wave is guessed.
8. Hijri/Gregorian basis and day counts are recorded; calendar eligibility is not inferred from ownership.
9. The Section 6 package retains identifiers, documents, downstream list and all flags. Unavailable figures are `null`, never zero estimates.
10. Every material legal or factual hold blocks finalising its computation and remains in the handoff for a professional authorised in Saudi Arabia.

## Legal instruments named in this skill

The Sources table identifies the texts actually read. **NON-OPERATIVE HISTORICAL TOPICS:** the earlier instrument list also named Income Tax Law M/1 (1425H), its Resolution 1535 regulations, Zakat Royal Decree M/40, VAT Law M/113 and Royal Order A/638, Excise Law M/86, conflicting RETT A/84/M/84 instruments, Social Insurance Laws M/33/M/22, Companies Law M/132, Nitaqat/WPS decisions, GCC VAT Agreement, bilateral treaties and a common "Tax Procedures Law". No unverified title, date, article attribution or universal procedural rule in that list is authority in this revision. Their relevant rules remain held where used. Obtain the operative current text before relying on any held topic; old instrument labels are retained here solely so the prior scope is not lost.

## Change log

- **v1.0 (May 2026):** Initial intake skill for the Saudi Arabia freelance / SME workflow. Routes to sa-zakat, sa-corporate-tax, sa-withholding-tax, sa-rett, sa-gosi-saudization, sa-excise-tax, saudi-arabia-vat, saudi-einvoice, sa-formation, sa-return-assembly. Reflects Income Tax Law (M/1, 1425H), Zakat Implementing Regulations (Decision 1007, 1445H), VAT Law (M/113, 1438H) at 15%, RETT (A/84, 2020) at 5%, Fatoorah e-invoicing (Phase 1 mandatory, Phase 2 wave-based), MISA registration requirement for foreign owners, and Nitaqat Saudization framework for tax year 2026.

- **v1.1 (November 2026):** Moved to tax year 2026 and the method shape. Corrected the Zakat regulation, Zakat percentage, withholding rates, GOSI arithmetic, Investment Law registration and Wave 25. Dropped duplicated runbook lines and the old booking link block.

- **v1.2 (1 November 2026):** Replaced operative assumptions with explicit local holds; corrected WHT nil-month and partnership exceptions, calendar scaling and the late-penalty example; recorded exact source scope and preserved earlier topics in the evidence ledger. Platform attribution and standard closing block preserved.
- **v1.3 (1 November 2026):** Bounded independent-review corrections align ownership and evidence routing, action templates, provisional planning and technical holds with the existing source ledger; earlier history and current-law limits remain.

## Sources

| Source and actual read scope | URL | Read on |
|---|---|---|
| Zakat Collection Regulations 1445H, Decision 1007 as amended by 1248; read in the original source: PDF pp. 2 to 9, 15 to 23, 58 to 63 (definitions, residence, period/rate, minimum/maximum and procedure/retention); no full-document claim | https://zatca.gov.sa/en/RulesRegulations/Documents/ZAKAT%20COLLECTION.pdf | 2026-11-01 |
| ZATCA Income Tax Guideline, May 2026; read in the original source: all 11 PDF pages, including rate diagram on p. 5 and obligations diagram on p. 6; Arabic prevails | https://zatca.gov.sa/en/HelpCenter/guidelines/Documents/Simplified-Guideline-for-Income-Tax.pdf | 2026-11-01 |
| Income-tax Implementing Regulations, Arabic compilation; read in the original source: cover/amendment list and arts. 9(2), 67 to 68, PDF pp. 1 to 2, 10 to 11, 55 to 57; compilation states amendments through Decision 2568 of 1440H, so no claim to complete 2026 amendment coverage | https://zatca.gov.sa/en/RulesRegulations/Taxes/Documents/Regulations_of_Income_Tax.pdf | 2026-11-01 |
| ZATCA WHT Guideline, May 2026; read in the original source: definitions and sections 1 to 5, PDF pp. 5 to 33: source/PE/category, exclusions, rates, nil months, annual partnership exception, retention and penalties | https://zatca.gov.sa/en/HelpCenter/guidelines/Documents/General-Guideline-for-Withholding-Tax-In-accordance-with-the-provisions-of-the-Income-Tax-Law-and-its-Implementing-Regulations.pdf | 2026-11-01 |
| ZATCA 2026 calendar; read in the original source: complete two-page PDF, annual deadline and all monthly VAT/WHT/excise entries; 2027 illustrative dates are calculated, not published in this calendar | https://zatca.gov.sa/en/MediaCenter/Publications/Documents/Zakat%20Declaration%20and%20Tax%20Returns%20Calendar%20(EN).pdf | 2026-11-01 |
| ZATCA VAT penalties; read in the original source: complete offence/fine table and neighbouring repeat-offence note | https://zatca.gov.sa/en/RulesRegulations/VAT/Pages/Penalties.aspx | 2026-11-01 |
| ZATCA September/Q3 2026 VAT notice; read in the original source: complete article and supplies split, not just title | https://zatca.gov.sa/en/MediaCenter/News/Pages/Submit-VAT-Return-for-Oct-andQ3-2026.aspx | 2026-11-01 |
| ZATCA Wave 25; read in the original source: complete article: qualifying years, strict threshold, notification, integration date and Phase 1 context | https://zatca.gov.sa/en/MediaCenter/News/Pages/Wave25-E-invoicing.aspx | 2026-11-01 |
| ZATCA sweetened-drink amendment announcement, Arabic; read in the original source: complete article: 2026 effective date, sugar method and 100 ml unit; not a tier-rate schedule | https://zatca.gov.sa/en/MediaCenter/News/Pages/excise-tax-regulation-2026.aspx | 2026-11-01 |
| ZATCA cancellation initiative; read in the original source: PDF pp. 1 to 9 including conditions and exclusions; no automatic eligibility conclusion | https://zatca.gov.sa/en/HelpCenter/guidelines/Documents/Cancellation-of-Fines-Exemption%20of-Financial-Penalties.pdf | 2026-11-01 |
| MISA Investment Law; read in the original source: bilingual PDF pp. 1 to 5, including arts. 1, 7 to 8 and 14 to 16 and securities exception | https://misa.gov.sa/app/uploads/2024/08/Investment-Law.pdf | 2026-11-01 |
| MISA updated law page; read in the original source: law text and Q&A 2.2 to 2.5, including existing-investor answer, not merely the registration headline | https://misa.gov.sa/activities/laws-regulations-copy/ | 2026-11-01 |
| MISA Implementing Regulations; read in the original source: arts. 1 to 2 and 9 to 13, PDF pp. 1 to 2 and 5 to 7, applicant information and annual-update context | https://misa.gov.sa/app/uploads/2025/06/THE-INVESTMENT-LAW-IMPLEMENTING-REGULATIONS.pdf | 2026-11-01 |

| Bureau of Experts Income Tax Law, **archived 15 February 2026** after direct TLS and ordinary-browser failure; read in original Arabic arts. 1 to 13 and amendment notes, 21 to 23, 60 to 61, 68 to 71, 76 to 77; later amendments not established | https://web.archive.org/web/20260215020442/https://laws.boe.gov.sa/boelaws/laws/lawdetails/23576008-1ce4-4685-ac3e-a9a700f2cb02/1 | 2026-11-01 |

Not yet confirmed: live Income Tax Law and amendments after the 15 February 2026 archive capture (direct BOE TLS fetch and ordinary browser failed); complete later amendments to the Arabic income-tax regulation compilation; VAT registration thresholds, rate and all transaction-specific zero/exempt conditions; Hijri eligibility or changes for income tax; interest limitation and loss-relief computation; specialised oil/gas rates; indirect/GCC corporate and listed-company allocation; actual mixed-return form and box identifiers; audit thresholds and attachment law; tax-specific portal/login/bill identifiers or status-update timing beyond the published income-tax steps; general extensions/refund periods; non-Zakat/non-WHT retention; GOSI rates, caps, new-entrant rules and payment dates; Nitaqat current bands/headcount thresholds/benefits/consequences; WPS mandate/deadline; RETT rate, exemptions, first-home limit, instrument and filing/payment date; excise product rates/tier amounts and registration test; Phase 1 invoice-type technical/QR/clearance/reporting rules and earlier waves; Investment Law commencement/transition and exceptions outside the read clauses; professional credential recognition and filing authority; transfer-pricing/Master File/Local File/CbCR thresholds; common Tax Procedures Law assertion. These are NON-OPERATIVE HOLDS: do not compute, classify, refuse, backdate, declare overdue, promise a date or finalise the affected line from a held rule. Named-contributor Guides remain outside this review and do not resolve a hold by themselves.

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
