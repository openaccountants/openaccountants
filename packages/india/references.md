---
name: india-references
jurisdiction: IN
last_updated: 2026-11-16
version: 1.1
description: Primary Indian tax sources and a preserved catalog of related open-source projects, with source, period, licence and calculation checks before any integration.
tier: 2
tax_year: 2026
type: router
---

# India: primary sources and related open-source projects

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

Route an Indian tax question to the enacted law and the appropriate India skill, and retain the existing software catalog as potential implementation references. Primary tax rules for Tax Year 2026-27 come from the Income-tax Act 2025, as amended, and notified Rules. The 2025-2026 filing cycle uses the earlier Act and its own forms. A project's README, popularity, licence label or tax-year filename does not establish legal accuracy.

The original catalog said Open Accountants is AGPL-3.0 and every listed project had a compatible licence. Preserve that history as a claim requiring a licence review of the actual material and proposed integration. It is not a blanket permission to copy code, data or UI assets. Two actual MIT files and India Compliance's GPL-3.0 file were opened; the calculator UI README claims MIT but its linked LICENSE returned 404. No code was installed, executed, copied into an engine or published by this skill.

## Ask the client first

- Which tax year, Act, jurisdiction, taxpayer type, regime and job does the proposed integration serve?
- Which exact repository commit and file, licence notice and dependencies will be used? Preserve attribution already present; this catalog does not grant a new permission.
- Is the intended reuse code, independently researched law, UI patterns, HSN descriptions, a return-preparation template, e-invoice validation or a rate table?
- What current official provision, eligibility conditions, exclusions, effective dates and calculator tests support each output?
- Do the current India skills already cover this job? Use `india-income-tax`, `in-tds-freelance`, `india-gst`, `india-einvoice` and the relevant return/advance-tax skills before proposing another rules source.

## The method, step by step

1. Fix the income period and applicable Act before selecting any project year. Read the official statute and amendments, not only a project table.
2. Read the existing India skill and its source/hold boundary. A catalog entry is a route to inspect software, not a replacement for the law or professional review.
3. Pin the exact project commit and file, inspect its actual licence and dependencies, and resolve reuse conditions before copying. A README's MIT label with a missing licence file remains unresolved.
4. Preserve the original catalog below, but distinguish project features from verified tax rules. Historical counts and claims are not current filing instructions.
5. Compare rates, whole-versus-excess bases, threshold equality, entity categories, dates, PAN and exemptions to the current official provision. Recompute the admission cases below; passing them is necessary evidence for these two cases only, not full engine approval.
6. Record source URLs, actual read scope/date, project commit/file, findings, unresolved rules and review result. Hold any unsupported output; do not silently replace official law with software defaults.

### taxcalcindia

- Repository: [amrajacivil/taxcalcindia](https://github.com/amrajacivil/taxcalcindia).
- Licence: MIT, confirmed from the actual LICENSE file. Language: English.
- Preserved scope: Python package for Indian income tax calculation; old/new regimes, salary/business/capital gains income, common deductions including 80 C,80 D,HRA,professional tax, and slab breakdown. The README confirms the broad regime/income/deduction scope; individual deduction implementation and current-law correctness still require file-level testing.
- Preserved integration idea: tax-slab logic, regime comparison and deduction computation. These are candidates to inspect; the original phrase “directly usable” is held until licence conditions and current legal behavior are checked. [Project licence](https://github.com/amrajacivil/taxcalcindia/blob/main/LICENSE).

### Aikar (आयकर)

- Repository: [debjitl45/aikar](https://github.com/debjitl45/aikar).
- Licence: MIT, confirmed from the actual LICENSE file. Language: English / Hindi as described in the original catalog.
- Historical catalog stars: 5, retained as an undated historical count, not a current recommendation or quality signal.
- Preserved scope: Python income-tax and capital-gains library; old/new regimes, equity/debt/gold gains and ITR-form selection guidance. The current README confirms the regime and capital-gains feature claims; the exact ITR-selection behavior has not been executed.
- Preserved integration idea: STCG/LTCG computation and regime comparison. The current README mixes a FY 2024-25/AY 2025-26 heading with a “Post Budget 2025” table and omits the current intermediate 25% band. This is a README observation, not a claim that its installed engine was run or fails. Check 1 below demonstrates why its table cannot be used as the current law. [README](https://github.com/debjitl45/aikar/blob/main/README.md), [licence](https://github.com/debjitl45/aikar/blob/main/LICENSE).

### indian-financial-calculators

- Repository: [Ammar-32-dev/indian-financial-calculators](https://github.com/Ammar-32-dev/indian-financial-calculators).
- Original licence claim: MIT. The opened README repeats MIT and links LICENSE, but that file returned 404. Exact licence text/reuse permission is **Not yet confirmed**; do not state all material is freely reusable.
- Language: English / TypeScript. Preserved scope: FY 2025-26 dual-regime income-tax UI, age-based calculations, deduction suggestions and enhanced rebate up to INR 1,200,000 as a project feature claim, not a legal amount sourced from that repository.
- Preserved integration idea: UI patterns for regime comparison and rebate presentation. Current law and calculation tests remain separate, and reuse is held pending licence resolution. [README](https://github.com/Ammar-32-dev/indian-financial-calculators/blob/main/README.md).

### india-compliance

- Repository: [resilient-tech/india-compliance](https://github.com/resilient-tech/india-compliance).
- Licence: GPL-3.0 as identified by the actual licence file and README. Language: Python / JavaScript, ERPNext/Frappe framework. Historical catalog stars: 235, retained as an undated count, not a live metric.
- Preserved scope: Indian GST and TDS compliance module. The following original data and integration claims are retained as a map for inspection; project data is not an official tax source.
- **GST rate templates**: original path `gst_india/data/tax_defaults.json`, with current repository path `india_compliance/gst_india/data/tax_defaults.json`. The original catalog listed 0%,1%,3%,5%,6%,7.5%,12%,18%,28%, CGST/SGST/IGST/RCM account structures, and in-state/out-state/reverse-charge/composition templates. The current opened file contains a subset of those template rates; the historical list is **Not yet confirmed** as a complete current inventory and does not determine the tax on any supply. A real supply requires current official notification/HSN/exemption analysis in `india-gst`.
- **HSN code master**: original path `gst_india/data/hsn_codes.json`, described as approximately 1,200 four-digit HSN descriptions without rate mappings. Exact current path, count, completeness and no-rate-mapping claim remain **Not yet confirmed**; no HSN data file was claimed read here.
- **Current TDS data**: original path `income_tax_india/data/tds_details.json`, current path `india_compliance/income_tax_india/data/tds_details.json`, contains dated 2026-04-01 to 2027-03-31 entries and section 393-based categories. The original “35+ payment categories” and individual/company/no-PAN distinctions are retained as historical catalog claims; current opened data confirms those category styles, but neither its count nor rates substitute for full statutory conditions. Selected contractor/professional/technical entries were read; whole-file tax accuracy is not certified.
- **Legacy TDS data**: `income_tax_india/data/tds_details_old.json`, current path prefixed `india_compliance/`. Original FY 2023-24 through FY 2025-26 coverage is retained, including 194 C,194 D,194 DA,194 H,194 I(a/b),194 JA,194 JB,194,193,194 A,194 B,194 BB,194 EE,194 F,194 G,194 LA,192 A,194 LBB,194 IA,194 Q,206 C(1 H). The opened file also carries later dated rows, so “legacy” is not proof every row belongs to an older Act. Read each entry's actual effective dates and provision before use; no complete legal review of every row is claimed.
- **GSTR-1/GSTR-3 B utilities**: original Excel filenames `gstr1_excel_template_v2.1.xlsx`, `gstr3b_excel_utility_v5.7.xlsx` are preserved as catalog pointers. Availability, formulas, current portal compatibility and exact filenames remain **Not yet confirmed**; no workbook was opened or validated.
- **E-invoice and e-way bill constants**: preserved configuration/validation integration topic; exact current implementation and legal correctness remain **Not yet confirmed**.
- Preserved integration history: the original file said these data enriched `india-gst.md` and `in-tds-freelance.md` and were checked against the codebase in May 2026. That historical integration/verification claim has not been independently re-established here. Do not present it as current source approval. [Licence](https://github.com/resilient-tech/india-compliance/blob/develop/license.txt), [current TDS data](https://github.com/resilient-tech/india-compliance/blob/develop/india_compliance/income_tax_india/data/tds_details.json), [GST templates](https://github.com/resilient-tech/india-compliance/blob/develop/india_compliance/gst_india/data/tax_defaults.json).

### Official admission figures for the two checks

These are law-based calculation fixtures for evaluating an implementation; they do not certify a listed project. Figures stay separate from the preserved, unconfirmed software catalog rates.

| Fixture | Rule and conditions | Official source |
|---|---|---|
| Current ordinary new-regime slab | Taxable income 2,200,000: lower-band tax 200,000 plus 25% of excess over 2,000,000; derived base comes from 400,000-wide 5%,10%,15%,20% bands. No rebate at that income, no surcharge with no other income; cess 4% | Act 202(1)/156 and Finance Act 2026 s.3; https://egazette.gov.in/WriteReadData/2025/265620.pdf; https://egazette.gov.in/WriteReadData/2026/271439.pdf |
| Current professional versus technical TDS | Resident ordinary payee, company payer, valid PAN, properly classified service, no lower certificate, annual aggregate 50,100 (illustrative input for the computed TDS fixture) strictly above 50,000. Professional 6(iii)(b)10%; qualifying technical 6(iii)(a)2%. Whole sum, not threshold excess; director/other exceptions outside this fixture | Act 393(1)serial 6(iii), full service classification required; https://egazette.gov.in/WriteReadData/2025/265620.pdf |

## Worked cases

### Check 1: reject a missing current band before reuse

Hypothetical ordinarily resident individual with total taxable ordinary income 2,200,000, valid new regime, no special-rate income or surcharge. Official tax 250,000 and cess 10,000 give 260,000. Mechanically using the README's 30%above 2,000,000 table would produce 260,000 before cess and 270,400 after it, overstating by 10,400. This compares table arithmetic only; no repository code was executed.

```oa-check
name: India catalog admission, missing intermediate band
inputs:
  income: 2200000
  band_start: 2000000
  lower_band_tax: 200000
steps:
  excess: income-band_start
  official_tax: lower_band_tax+excess*0.25
  official_cess: official_tax*0.04
  official_total: official_tax+official_cess
  incomplete_table_tax: lower_band_tax+excess*0.30
  incomplete_table_total: incomplete_table_tax*1.04
  overstatement: incomplete_table_total-official_total
expected:
  excess: 200000
  official_tax: 250000
  official_cess: 10000
  official_total: 260000
  incomplete_table_tax: 260000
  incomplete_table_total: 270400
  overstatement: 10400
```

### Check 2: the same amount needs correct service classification

Hypothetical 50,100 fee. If it is professional service, TDS 5,010 and net 45,090; if it is a qualifying technical alternative, TDS 1,002 and net 49,098. Difference 4,008 shows why a payment-category table requires actual legal classification. Exact 50,000 annual equality gives no threshold-crossing deduction for this ordinary fee fixture. Missing PAN, director fees, different payer and certificates need their own rules.

```oa-check
name: India catalog admission, professional versus technical classification
inputs:
  fee: 50100
  equality: 50000
steps:
  professional_tds: fee*0.10
  technical_tds: fee*0.02
  professional_net: fee-professional_tds
  technical_net: fee-technical_tds
  difference: professional_tds-technical_tds
  equality_tds: equality*0
expected:
  professional_tds: 5010
  technical_tds: 1002
  professional_net: 45090
  technical_net: 49098
  difference: 4008
  equality_tds: 0
```

## When to refuse or refer

- Refuse to treat a GitHub rate table, star count, software name or licence as an official tax rule or proof a return is correct.
- Hold reuse where the actual licence/required notices or dependency rights are unresolved, including the calculator UI LICENSE 404. Project licence labels here are source observations, not a legal opinion on every proposed integration.
- Refer tax classifications, special-rate income, current form/extension/interest holds and client-specific filings to the named India skill and professional review.
- Do not install or execute a repository, upload client data, call paid APIs, change an engine or submit a return merely because it appears in this catalog.

## Filing and payment

This catalog does not select a return field, submit a form or make a payment. Route the actual task to `in-return-assembly`, `india-income-tax`, `in-tds-freelance`, `india-gst` or `india-einvoice` as applicable. Keep the applicable Act/year, current official form and underlying source conditions with the calculation, and retain an unresolved-source list for review.

## Completion checklist

- [ ] All original projects, scopes, integration ideas and historical counts retained with accurate current-evidence boundaries.
- [ ] Exact repository/file/commit, licence and proposed reuse recorded; missing permissions resolved before reuse.
- [ ] Current official law, taxpayer category, period, thresholds and exceptions checked independently of project code.
- [ ] Meaningful fixtures recomputed and their limits disclosed; no claim the engine itself ran.
- [ ] Every unconfirmed catalog claim stays out of current tax instructions or a blanket licence assertion.

## Sources

| Source | Read for | Actual read date |
|---|---|---|
| https://egazette.gov.in/WriteReadData/2025/265620.pdf | Read for 202 slabs,156 rebate,393(1)intro/serial 6(iii)and service/PAN conditions; official legal fixtures only, not complete code audit | 2026-11-15 |
| https://egazette.gov.in/WriteReadData/2026/271439.pdf | Read for individual surcharge/cess s.3 and First Schedule I-BPara A/F; 4%fixture cess and below-threshold no-surcharge facts | 2026-11-15 |
| https://github.com/amrajacivil/taxcalcindia | Read for README broad features; first-party project documentation only, not tax authority | 2026-11-15 |
| https://github.com/amrajacivil/taxcalcindia/blob/main/LICENSE | Read for actual MIT licence and notice/permission conditions; no blanket compatibility opinion | 2026-11-15 |
| https://github.com/debjitl45/aikar/blob/main/README.md | Read for current README feature list, year label and incomplete slab table; no execution or entire implementation review | 2026-11-15 |
| https://github.com/debjitl45/aikar/blob/main/LICENSE | Read for actual MIT licence and notice/permission conditions | 2026-11-15 |
| https://github.com/Ammar-32-dev/indian-financial-calculators/blob/main/README.md | Read for FY 2025-26 calculator features, TypeScript/UI scope and MIT claim; linked LICENSE returned 404, exact reuse rights unresolved | 2026-11-15 |
| https://github.com/resilient-tech/india-compliance | Read for README GST/ERPNext/Frappe scope and GPL label; not whole application audit | 2026-11-15 |
| https://github.com/resilient-tech/india-compliance/blob/develop/license.txt | Read for GPL-3.0 licence heading and project licence file existence; no full compatibility/legal opinion | 2026-11-15 |
| https://github.com/resilient-tech/india-compliance/blob/develop/india_compliance/gst_india/data/tax_defaults.json | Read for template structure and actual gst_rate fields only; historical complete rate list not verified as current law | 2026-11-15 |
| https://github.com/resilient-tech/india-compliance/blob/develop/india_compliance/income_tax_india/data/tds_details.json | Read for category names/effective date structure and selected professional/technical/contractor rows; not every rate's legal correctness | 2026-11-15 |
| https://github.com/resilient-tech/india-compliance/blob/develop/india_compliance/income_tax_india/data/tds_details_old.json | Read for date ranges and selected legacy/current rows; filename does not guarantee older-Act content, no full legal certification | 2026-11-15 |

**Not yet confirmed:** calculator UI actual licence file/reuse permission; historical 5/235 stars; original full GST template rate inventory 0/1/3/5/6/7.5/12/18/28%; HSNapproximately 1,200 four-digit no-rate-master claim/current path/completeness; 35+historical TDS category count as a historical measure; GSTRworkbook filenames/formulas/portal compatibility; e-invoice/e-waybill exact constants; prior May 2026 enrichment/verification history; exact project implementation, current-year correctness and reuse compatibility beyond opened licence/README observations. The 2025-2026 filingcycle project labels are preserved, not projected onto current Tax Year 2026-27. No tax filing conclusion comes from these unconfirmed catalog figures.
