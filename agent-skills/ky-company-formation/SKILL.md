---
name: ky-company-formation
description: "Forming a company in the Cayman Islands in 2026, step by step. Covers the entity types (exempted company, ordinary company, limited duration company, LLC, exempted limited partnership), registration with the General Registry and its 2026 exempted company registration fees by share capital (CI$700 to CI$42,000 of capital, then CI$1,000, CI$1,984 and CI$2,568), the tax undertaking, economic substance notification, and what follows. No tax registration is needed because there is no income tax or VAT. Trigger on Cayman company formation, exempted company Cayman, register a company in Cayman, General Registry fees. Built from the General Registry fee table and Cayman legislation; not reviewed by an accountant."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/ky-company-formation"
  jurisdiction: "KY"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# Cayman Islands: forming a company

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope and who this is for

People setting up a Cayman entity in 2026: exempted companies (the usual vehicle for business outside the Islands), ordinary companies, limited duration companies, limited liability companies, and exempted limited partnerships. It covers the registration steps and the tax-related filings. There is no income tax or VAT, so no tax registration exists. Amounts are CI$; the General Registry converts at US$1 = CI$0.82.

## Ask the client first

1. Will the entity do business in the Islands, or only outside (exempted company)?
2. Planned authorised share capital (it sets the registration fee band).
3. Will it carry on a relevant activity for economic substance (banking, distribution and service centre, financing and leasing, fund management, headquarters, holding company, insurance, intellectual property, shipping)?
4. Will it employ staff in Cayman (pensions, health insurance, work permits)?
5. Does it want a tax undertaking?

## The method, step by step

### Rates, bands and thresholds

| Item | 2026 figure | Conditions | Source |
|---|---|---|---|
| Exempted company registration fee, share capital up to CI$42,000 | CI$700 (US$853.66) | Companies Act s. 26(4)(b)(i) | Cayman Islands General Registry, fees: https://www.ciregistry.ky/fees/ |
| Share capital CI$42,001 to 820,000 | CI$1,000 (US$1,219.51) | s. 26(4)(b)(ii) | same |
| Share capital CI$820,001 to 1,640,000 | CI$1,984 (US$2,419.51) | s. 26(4)(b)(iii) | same |
| Share capital over CI$1,640,001 | CI$2,568 (US$3,131.71) | s. 26(4)(b)(iv) | same |
| Tax undertaking | Up to 30 years | Application to the Financial Secretary | Tax Concessions Act (2018 Revision), s. 6: https://legislation.gov.ky/cms/images/LEGISLATION/PRINCIPAL/1964/1964-0164/1964-0164_2018%20Revision.pdf |
| Economic substance notification | Annually | Every entity, s. 7(1) | International Tax Co-operation (Economic Substance) Act (2026 Revision): https://legislation.gov.ky/cms/images/LEGISLATION/PRINCIPAL/2018/2018-0045/2018-0045_2026%20Revision.pdf |
| Companies Act | 2026 Revision in force | | Cayman legislation, current by title: https://legislation.gov.ky/cms/legislation/current/by-title.html |

### Steps in order

1. **Choose the vehicle.** An exempted company is for business carried on mainly outside the Islands; an ordinary company for local business. The General Registry fee table also lists exempted companies limited by guarantee, by continuation, and limited duration companies, each with its own fee lines.
2. **Instruct a registered office provider** in the Islands to prepare and file the memorandum and articles with the General Registry (registered office rules: see Not yet confirmed).
3. **Pay the registration fee** for the capital band (table above).
4. **Apply for a tax undertaking** if wanted (Tax Concessions Act s. 6).
5. **Economic substance.** Make the first annual notification; if a relevant activity is carried on, plan the substance and the report due 12 months after the first year end (`ky-corporate-income-tax`).
6. **Staff in Cayman.** Enrol employees in a pension plan and health insurance and obtain work permits (`ky-payroll-social`).
7. **Each year.** Annual return and fee to the Registry (timing and amounts: see Not yet confirmed); economic substance notification and report.

### What happens after

The Registry issues a certificate of incorporation. No tax authority registration follows, because there is no income tax or VAT. Import duty applies to goods the company brings in (`ky-vat-gst`).

## Worked cases

### Exempted company with US$50,000 of share capital

US$50,000 at US$1 = CI$0.82 is CI$41,000, inside the first band, so the registration fee is CI$700. Raising capital to US$60,000 (CI$49,200) moves it into the CI$1,000 band.

```oa-check
name: KY exempted company fee band, US 50000 vs 60000 capital
inputs:
  capital_usd_a: 50000
  capital_usd_b: 60000
  rate: 0.82
steps:
  - capital_kyd_a: capital_usd_a * rate
  - capital_kyd_b: capital_usd_b * rate
  - fee_a: 700
  - fee_b: 1000
  - extra_fee: fee_b - fee_a
expected:
  capital_kyd_a: 41000
  capital_kyd_b: 49200
  extra_fee: 300
```

## When to refuse or refer

- Drafting constitutional documents, registered office services, segregated portfolio companies, foundation companies and funds: refer to a Cayman attorney or licensed corporate services provider.
- CRS/FATCA classification: refer.
- Beneficial ownership filings: refer (rules not read for this version).

## Filing and payment

| Item | Where | When |
|---|---|---|
| Registration | General Registry, through the registered office provider | At formation |
| Registration fee | General Registry | With the application |
| Tax undertaking | Financial Secretary | After incorporation, if wanted |
| Economic substance notification and report | The Authority named in the Act, in its approved form | Annually; report 12 months after year end |

## Sources

| Source | URL | Read on |
|---|---|---|
| Cayman Islands General Registry, fees: read for the exempted company registration fees by capital band and the US$ conversion at 0.82 | https://www.ciregistry.ky/fees/ | 2026-11-14 |
| Tax Concessions Act (2018 Revision): read for s. 6 undertakings | https://legislation.gov.ky/cms/images/LEGISLATION/PRINCIPAL/1964/1964-0164/1964-0164_2018%20Revision.pdf | 2026-11-14 |
| International Tax Co-operation (Economic Substance) Act (2026 Revision): read for s. 7 notification and report | https://legislation.gov.ky/cms/images/LEGISLATION/PRINCIPAL/2018/2018-0045/2018-0045_2026%20Revision.pdf | 2026-11-14 |
| Cayman legislation, current by title: read for the Companies Act 2026 Revision and the absence of income tax and VAT Acts | https://legislation.gov.ky/cms/legislation/current/by-title.html | 2026-11-14 |

Not yet confirmed: annual government fees (the old CI$925 and CI$1,225 for 2025 came from the Registry page but the page read today showed only the registration fee table; the January filing date is not confirmed); name reservation fees (old: US$49 to US$195); incorporation timeline (old: 1 to 5 business days); minimum directors and shareholders and the registered office rule in the Companies Act (old file relied on firm and vendor pages); ordinary company, LLC and exempted limited partnership fees; beneficial ownership register duties.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `ky-company-formation` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/ky-company-formation. If neither is available, confirm every figure against the official source pages cited above before relying on it.
