---
name: pk-freelance-intake
description: Use for pakistan freelance and sme intake. Read the stated period, eligibility conditions, evidence requirements, owner skills and unresolved boundaries before calculating or preparing a return.
version: 1.1
jurisdiction: PK
tax_year: 2026
last_updated: 2026-11-14
category: orchestrator
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: router
---

# Pakistan freelance and SME intake v1.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

Entry point for Pakistan resident self-employed individuals, sole proprietors, AOP partners and small private-company founders, preparing a reviewer package for tax year 2026, the normal year 1 July 2025 to 30 June 2026. Its job is evidence collection, classification and routing; it does not file a return or certify tax. Company status routes to the company skill, rather than being treated as an individual's business. Non-resident, uncertain-residence and special regimes require specialist handling.

Quick answer: read the available documents first, identify the person, period and income streams, then load the relevant skills. The salary-table gate is more than 75% of taxable income, not the old 50% threshold. The repealed 120-day-plus-prior 365-day residence test must not be used. [ITO s.82 and First Schedule Division I](https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf).

## Ask the client first

Use the records before asking. Obtain all available statements/invoices/certificates in one document collection; parse them and show an inferred summary, then ask only unresolved questions. Batch up to 3 related independent choices using the available structured-choice input tool, with free text for identifiers where needed; do not depend on a tool name that the execution environment does not provide.

Collect these fields with evidence and an explicit unknown state:

- Legal name, CNIC/NTN, trading name, STRN/provincial registrations, PSEB certificate/ID/validity, IRIS access status. Individuals' CNIC registration and AOP/company identifiers must not be conflated.
- Individual/sole proprietor, AOP/partnership, private company or SMC status; AOP deed/date/shares and member types; company incorporation/CUIN and actual director records.
- Days in Pakistan for the tax period, citizenship, foreign tax residence, government posting and any dual-residence/migration issue. Read every operative s.82 branch, not only day count.
- Gross turnover and monthly receipts, domestic/export split, gross foreign currency and evidenced PKR conversion, service category, PSEB period, bank/e-PRCs, platform fees/refunds and income from employment or other sources.
- Prior returns/acknowledgements, filing/ATL history and status at relevant payment dates, actual withholding certificates/CPRs, advance payments and refund history.
- Employees/headcount/locations, payroll/EOBI/provincial social-security status, professional-tax questions, supplier/rent/foreign/dividend/debt payments and payer status for each withholding section.
- Service provider/recipient locations, establishment(s), where supplied/used, goods/services split, federal/provincial registrations and any multi-authority exposure.
- Securities/property/crypto disposals, foreign assets, missing books, depreciation/asset records, and complete bank/wealth evidence.

Do not request passwords in the intake package. Access status is enough for routing; the taxpayer/authorised filer retains credentials.

## The method, step by step

1. **Open and sweep scope.** Explain the document-to-reviewer workflow and establish residence, entity, income mix, turnover and province. Non-resident/uncertain cases pause final classification. AJK/GB require their own administration analysis, not this ordinary Pakistan workflow. Income-tax residence under s.82 includes presence of at least 183 days, government posting, and the separate citizenship/foreign-residence alternatives (figures in words on the page). A resident AOP has a different s.84 test. [ss.82,84](https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf).
2. **Read and infer.** Import all accounts and source documents; separate gross receipts, costs, transfers, foreign conversion, withholding suffered and advances. Never re-ask a fact clearly evidenced by documents. Reconcile contradictory figures and present the discrepancy with sources instead of choosing an arbitrary higher-tax number.
3. **Classify entity and income.** Individual/AOP annual income returns are under s.114; s.116 is the resident individual's wealth statement, not an AOP return form. Salary-table eligibility is more than 75% salary of taxable income; the remaining individual/AOP table is shared, with a professional-AOP proviso. A company needs its applicable company regime. Do not certify an old form 32 A or guessed portal identifier. [ss.11,92,114,116; First Schedule](https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf).
4. **Test export candidate.** Genuine PSEB IT/ITeS export proceeds with authorised-dealer realisation go to `pk-it-export-tax`; finality also requires the statutory filing/other conditions and no foreign-tax credit. The s.154A(2)(c) proviso removes the sales-tax-return condition for the specified PSEB branch, not provincial liability itself. A foreign client/platform alone does not qualify and missing PSEB does not automatically mean ordinary slabs. [s.154A](https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf).
5. **Check ATL and withholding.** Capture actual event-date status and any late-filer history; route specific payment categories and payer definitions to `pk-withholding-tax`. Do not use a single turnover threshold for salary, services, rent and foreign payments or promise a weekly ATL update. Preserve the prior-return/surcharge evidence and missing-status flag.
6. **Run the parallel routing table.** Goods and services can require different returns. Employment creates a payroll assessment even where the person previously had no staff. Capital events and entity uncertainty need their own evidence/routing.
7. **Confirm and fill gaps.** Show the source-backed taxpayer/entity/period/province/ATL/access summary; receipts by stream, proposed regimes, registrations, staff, minimum/super/ACT flags and chosen skills. Invite corrections; ask only what documents could not establish. Missing registration is a flag to assess, not automatic proof of tax exemption.
8. **Handoff.** Deliver the structured package, evidence index, chosen skills/run order, reasons for skills not run, unresolved flags/refusals and professional-review requirement to `pk-return-assembly`. Unknown values remain null/unknown, not false or an assumed rate.

### Parallel routing, preserving the original jobs

| Evidence/question | Load and handoff |
|---|---|
| Individual/sole proprietor/salary/AOP income | `pk-income-tax`; final export stream additionally `pk-it-export-tax`; AOP company-member and audited-account exceptions preserved |
| Pvt Ltd or SMC | `pk-corporate-tax`, with current period/eligibility checked; approved sibling is not rewritten or treated as automatically current |
| Taxable goods or federal registration issue | `pk-sales-tax-federal`; `pakistan-sales-tax` for bank-transaction classification; do not invent a general turnover exemption |
| Services in Sindh/Punjab/KP/Balochistan/ICT | `pk-sales-tax-services`, naming SRB/PRA/KPRA/BRA/FBR-ICT; determine each applicable place-of-provision rule, not a blanket origin/destination default |
| Any employee | `pk-payroll-eobi`, `pk-payroll` and `pk-social-contributions` as relevant; employer and worker locations/coverage must be established |
| Salary, goods/services/contracts, rent, commission, dividend, debt or foreign-supplier payments | `pk-withholding-tax`; section-specific prescribed-person and treatment tests |
| Securities or property disposal | `pk-cgt`, acquisition/disposal/ATL/holding evidence and actual certificates |
| Crypto/virtual assets | `pk-crypto-tax` for regulatory/tax-classification boundary; `pk-cgt` only after asset classification is established |
| Entity choice/incorporation or NTN onboarding | `pk-formation`; sector/foreign-ownership and beneficial-owner checks |
| Missing books/financial statements | `pk-bookkeeping` and `pk-financial-statements`; no assumption that a bank reconciliation is every legal record required |
| Turnover/income/asset position indicates special charges | Flag s.113 minimum tax,s.4C super tax,s.113C company ACT and industrial/sector issues for their owner; turnover is not automatically super-tax income |
| Final supported package | `pk-return-assembly` last, with every missing computation named |

### Structured package

Keep the original handoff fields, but record evidence and unknowns explicitly. `tax_year` is 2026 and the normal window is 2025-07-01 through 2026-06-30 (derived under s.74). Each registration/eligibility field is true/false only when established.

```json
{
  "jurisdiction": "PK", "tax_year": 2026,
  "tax_year_window": {"start": "2025-07-01", "end": "2026-06-30", "special_year": null},
  "taxpayer": {"name": "", "cnic": "", "ntn": "", "strn": "", "pseb_id": "", "iris_active": null,
    "entity_type": null, "residency": null, "residency_evidence": [], "primary_province": null, "cuin": ""},
  "atl": {"status": "unknown", "event_dates": [], "prior_year_filed": null, "surcharge_paid": null,
    "tenth_schedule_uplift_applied": null},
  "regime": {"selected": null, "annual_turnover_pkr": null, "domestic_turnover_pkr": null,
    "export_turnover_pkr_equivalent": null, "export_turnover_fx_gross": null, "export_currency": null,
    "pseb_registered": null, "pseb_final_tax_rate_pct": null, "finality_conditions": [],
    "minimum_tax_s113_applicable": null, "super_tax_s4c_applicable": null, "act_s113c_applicable": null},
  "sales_tax": {"fbr_goods_registered": null, "srb_sindh_registered": null, "pra_punjab_registered": null,
    "kpra_registered": null, "bra_registered": null, "ict_fbr_registered": null,
    "multi_jurisdiction_flag": null, "registration_overdue_flag": null},
  "employment": {"has_employees": null, "employee_count": null, "eobi_registered": null,
    "provincial_ss_registered": null, "provincial_professional_tax_due": null},
  "withholding": {"made_salary_payments": null, "made_rent_payments": null,
    "made_contractor_service_payments": null, "made_non_resident_payments": null,
    "made_dividend_payments": null, "made_debt_payments": null, "is_prescribed_person_s153": null},
  "capital_gains": {"disposed_securities": null, "disposed_immovable_property": null, "disposed_crypto": null},
  "bookkeeping": {"method_required": null, "currently_in_place": null},
  "documents_received": [], "evidence_index": [], "downstream_skills_to_load": [],
  "open_flags": [], "refusals_triggered": [], "conservative_defaults_applied": []
}
```

## Worked cases

### Ahmed Khan historical intake, retained with conditions

Ahmed Khan remains the Lahore individual/sole proprietor from the earlier handoff, present 245 days, with an assumed active PSEB ID and timely tax-year-2025 return/ATL history. The old illustrative NTN 1234567 remains an unvalidated historical label, not a certified individual identifier format. He has assumed PKR 8,500,000 export proceeds and no domestic income/staff. The earlier USD 30,000/PKR 8,500,000 pairing is an assumed conversion, not a live quote. The bank-account label, including the older Meezan Bank Roshan Digital Account description, does not independently prove permissible business-export realisation. With genuine PSEB eligibility, authorised-dealer proof and all finality conditions, withholding is 21,250 (derived). PRA export treatment must be established separately; do not promise exemption from PSEB alone.

```oa-check
name: Ahmed Khan qualifying export candidate
inputs:
  documented_export_proceeds: 8500000
  documented_domestic_proceeds: 0
steps:
  - export_withholding: documented_export_proceeds * 0.0025
  - total_proceeds: documented_export_proceeds + documented_domestic_proceeds
expected:
  export_withholding: 21250
  total_proceeds: 8500000
```

Route income/export and provincial services-tax checks, then assembly; do not load company/goods/payroll/CGT/formation computations absent the corresponding facts. Preserve an evidence gap rather than asserting a nonexistent return or registration obligation.

```oa-check
name: Salary-routing boundary corrects old50percent gate
inputs:
  taxable_income: 3000000
  salary_income: 2100000
steps:
  - salary_percent: salary_income / taxable_income * 100
  - distance_below_salary_gate: 75 - salary_percent
expected:
  salary_percent: 70
  distance_below_salary_gate: 5
```

Salary is 70% (derived), so this is below the statutory more-than 75% gate; the old 50% routing would wrongly choose the salary table. This is a classification case, not a full tax computation.

## When to refuse or refer

Preserve the original scope refusals: non-resident/part-year/dual-resident treaty cases; foreign-resident Pakistan-source-only claims; listed/public companies and consolidated groups; banking, insurance, petroleum/oil/gas/mineral regimes; transfer-pricing/CbCR; AJK/GB administration; undocumented smuggling/informal/cash-only operations; and missing AOP deed/allocation evidence. Private companies with more than 50 staff or audited revenue over PKR 1,000,000,000 remain an **internal specialist-review trigger**, not a statutory tax threshold. More than 20 staff remains an internal payroll-volume flag, not a legal audit requirement.

Do not repeat the old sample asserting that 110 days proves non-residence: all s.82 alternatives must be tested. Unknown ATL, PSEB, province, entity, threshold, minimum tax, super tax or book status stays unresolved; do not invent non-filer tax, dual-province registration, an individual entity, a foreign exchange rate or an old-year rate. Pause the affected final conclusion while completing supported reconstruction. Never claim the professional reviewer has approved the package merely because intake is complete.

## Completion checklist

Preserve every original handoff check: scope/residence evidence; legal entity/deed/CUIN; NTN/registration gaps; event-date ATL; PSEB period and bank evidence; gross PKR/FX and domestic/export split; regime reason; goods/services footprint and named authorities; employee/headcount/location and coverage; section-specific payer obligations; minimum/super/ACT flags; capital events; books/framework needs; IRIS access; all defaults/open items/refusals; chosen and omitted skills with reasons; and reviewer disclaimer.

## Sindh self-employed coverage screen

Ask about work category and existing SESSI coverage even without staff. Sindh 2021 amendment ss.2-3 adds self-employed workers and s.20A fixed PKR 1,500 monthly contribution subject to prescribed conditions. Obtain those conditions before determining that a particular freelancer is covered; no-staff status alone is insufficient. Route to `pk-social-contributions`. [Official amendment](https://www.sessi.gov.pk/assets/files/content/2026/01/Sindh-Act-No.XIX-of-2021.pdf), read for ss.2-3 on 2026-11-14.

## Sources

| Source and actual portions read | Official URL | Read on |
|---|---|---|
| Read for ITO ss.11,71,74,82/84,92,114/116,147,154 A,174 and First Schedule salary classification; repealed residence footnote distinguished from operative text | https://download1.fbr.gov.pk/Docs/2025881983148210Income-Tax-Ordinance,-2001-Amended-upto-31.07.2025.pdf | 2026-11-14 |

Not yet confirmed: event-specific ATL rates/refresh and eligibility for the current re-entry routes, all provincial registration/place/exemption decisions, EOBI/provincial coverage and bases, actual current IRIS identifiers/screens, taxpayer evidence, identifier-format lengths and special-year/treaty regimes. The s.113 excess-minimum-tax carry-forward and s.113C company calculation belong to their computation owners; no turnover-bin estimate decides them. The old turnover intake bins 600,000/5,000,000/50,000,000/250,000,000 were workflow bins, not universal liability thresholds; no tax conclusion follows from them. Repeated tax tables belong to their named computation owners, with source checks required before use; unsupported historic 50% salary/120+365-day residence routes are withdrawn as contradicted by the cited law.
