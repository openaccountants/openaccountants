---
name: my-company-formation
description: "Use this skill whenever asked how to set up a company in Malaysia in 2026, choose between a sole proprietorship, partnership, LLP and Sdn Bhd, incorporate through SSM MyCoID, or keep a Malaysian private company compliant. Trigger on phrases like Sdn Bhd registration, incorporate company Malaysia, SSM, Companies Commission of Malaysia, MyCoID, company secretary Malaysia, annual return SSM, audit exemption Malaysia, Practice Directive 10/2024, resident director Malaysia. Covers the Companies Act 2016 minimums (one director ordinarily resident, a licensed secretary within 30 days), SSM fees (RM1,000 incorporation, RM150 annual return), financial statements timing, the phased audit exemption thresholds for 2025 to 2027, and the tax and payroll registrations after incorporation."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/my-company-formation"
  jurisdiction: "MY"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# Malaysia company formation and entity choice, 2026

> **General reference only.** This skill is general reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts. Do not rely on it to form a company or take a position without review by a qualified professional in Malaysia.

## Scope

How to form and keep compliant a Malaysian private company limited by shares (Sendirian Berhad, Sdn Bhd) under the Companies Act 2016, registered with the Companies Commission of Malaysia (SSM) through MyCoID. Other vehicles: public company (Berhad), limited liability partnership (PLT, LLP Act 2012), partnership and sole proprietorship (registered under the Registration of Businesses Act 1956). How each is taxed: `my-income-tax` (individuals and partners) and `my-corporate-income-tax` (companies).

## Ask the client first

1. **Who are the owners and directors**, and does at least one director have a principal place of residence in Malaysia?
2. **Activity**: does it need a licence or face foreign-ownership limits in its sector?
3. **Expected revenue, assets and staff** for the first years (audit exemption and SST, e-invoice and payroll registrations).
4. **Proposed name** and financial year end.
5. **Who will be company secretary** (must be licensed or a member of a listed body).

## The method, step by step

1. **Choose the vehicle.** A sole proprietor or partners are taxed on profits at personal rates; a Sdn Bhd is a separate taxpayer with limited liability; a PLT gives limited liability with partnership-style management.
2. **Reserve the name** with SSM (s. 27).
3. **Incorporate** on MyCoID under s. 14 with the constitution (optional), director and shareholder details and consents. A private company needs at least one director (s. 196(1)), a natural person aged 18 or over (s. 196(2)), and the minimum number of directors must ordinarily reside in Malaysia (s. 196(4)). One shareholder is enough, and may be the director.
4. **Appoint the first secretary within 30 days** of incorporation (s. 236(2)). The secretary must be a natural person, 18 or over, a citizen or permanent resident ordinarily residing in Malaysia (s. 235(1)), and licensed or a member of a body in the Fourth Schedule (s. 235(2)).
5. **Register for taxes and payroll**: income tax file with LHDN (Form C each year); employer registration with LHDN, EPF, SOCSO and EIS once there are staff (`my-pcb`, `my-epf-socso`); SST with RMCD if a threshold is reached (`malaysia-sst`); e-invoicing if in scope (`malaysia-einvoice`).
6. **Each year**: prepare financial statements (first within 18 months of incorporation, then within 6 months of the year end, s. 248); circulate them within 6 months of the year end (s. 258); lodge within 30 days of circulation (s. 259); lodge the annual return within 30 days of each incorporation anniversary, not in the year of incorporation (s. 68).
7. **Audit**: every private company appoints an auditor (s. 267(1)) unless exempt by the Registrar (s. 267(2)) under Practice Directive 10/2024 (see the table).

### Rates, bands and thresholds

| Item | Figure | Source |
| --- | --- | --- |
| Incorporation, company limited by shares (s. 14) | RM1,000 | https://www.ssm.com.my/Pages/Services/Registration-of-Company-(ROC)/Table-of-Fees.aspx |
| Incorporation, company limited by guarantee | RM3,000 | same |
| Name reservation (s. 27), per 30 days, up to 180 days | RM50 | same |
| Change of name (s. 28) | RM100 | same |
| Annual return, private company (s. 68) | RM150 | same |
| Annual return, public company | RM500 | same |
| Minimum directors, private company (s. 196(1)) | 1 | https://www.ssm.com.my/Pages/Legal_Framework/Document/Companies%20Act%202016_as%20at%2031%20January%202025.pdf |
| First secretary appointed within (s. 236(2)) | 30 days | same |
| Annual return due after the anniversary (s. 68(1)) | 30 days | same |
| Circulation of financial statements after year end (s. 258) | 6 months | same |
| Lodging after circulation (s. 259) | 30 days | same |
| Audit exemption, periods starting 1 Jan 2025 to 31 Dec 2025 (Phase 1): revenue / assets / employees | RM1,000,000 / RM1,000,000 / 10 | https://www.ssm.com.my/Pages/Legal_Framework/Document/NEW%20PD%2010-2024%20-%20Qualifying%20Criteria%20for%20Audit%20Exemption%20for%20Certain%20Categories%20of%20Private%20Companies%20(Portal).pdf |
| Audit exemption, periods starting in 2026 (Phase 2) | RM2,000,000 / RM2,000,000 / 20 | same |
| Audit exemption, periods starting from 1 Jan 2027 (Phase 3) | RM3,000,000 / RM3,000,000 / 30 | same |

Audit exemption rule: a private company qualifies if it meets at least two of the three criteria for the current year and each of the two years before. Dormant companies (since incorporation, or in the current and previous year) stay exempt.

## Worked cases

Case, decision: does a Sdn Bhd need an audit for its 2026 year, and what does SSM charge in year one? A company incorporated in 2024 has revenue RM1.8 million, RM1.6 million and RM1.2 million (2026, 2025, 2024), assets RM2.4 million in each year and 12 employees each year. For a 2026 financial period the Phase 2 limits apply: revenue within RM2 million in all three years (met); assets over RM2 million (not met); employees within 20 (met). Two of three are met, so it is exempt from audit for 2026. A new company formed in 2026 with a name reservation of 30 days pays SSM RM1,000 + RM50 = RM1,050, then RM150 for each annual return from 2027.

```oa-check
name: Audit exemption test 2026 and first-year SSM fees
inputs:
  revenue_max: 1800000
  assets_max: 2400000
  staff_max: 12
steps:
  - revenue_ok: min(max(2000000 - revenue_max + 1, 0), 1)
  - assets_ok: min(max(2000000 - assets_max + 1, 0), 1)
  - staff_ok: min(max(20 - staff_max + 1, 0), 1)
  - criteria_met: revenue_ok + assets_ok + staff_ok
  - first_year_fees: 1000 + 50
expected:
  criteria_met: 2
  first_year_fees: 1050
```

## When to refuse or refer

| Code | Trigger | Message |
| --- | --- | --- |
| R-F-1 | Regulated or restricted sector (finance, telecoms, energy, distributive trade) | "This sector needs a licence or has ownership limits. Refer before incorporating." |
| R-F-2 | No director with a principal residence in Malaysia | "The Act requires the minimum number of directors to ordinarily reside in Malaysia. A resident director must be found first." |
| R-F-3 | Labuan entity or public company | "Out of scope; refer." |

## Filing and payment

| Filing | Where | When |
| --- | --- | --- |
| Name reservation and incorporation | SSM MyCoID | Before trading |
| First secretary | Board resolution, notified to SSM | Within 30 days of incorporation |
| Annual return | SSM (MBRS) | Within 30 days of each anniversary |
| Financial statements | SSM (MBRS) | Within 30 days of circulation, which is within 6 months of year end |
| Income tax return | LHDN, Form C | See `my-corporate-income-tax` |

## Completion checklist

- Vehicle chosen with tax effect noted.
- Resident director and qualified secretary identified.
- Fees budgeted from the SSM table.
- Year end, first financial statements date and annual return date diarised.
- Audit exemption tested for each year with two-of-three criteria.
- LHDN, payroll, SST and e-invoice registrations listed.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Read for the SSM table of fees: incorporation, name reservation and change, annual return | https://www.ssm.com.my/Pages/Services/Registration-of-Company-(ROC)/Table-of-Fees.aspx | 2026-11-14 |
| Read for the Companies Act 2016 as at 31 January 2025: ss. 14, 68, 196, 235, 236, 248, 258, 259 and 267 | https://www.ssm.com.my/Pages/Legal_Framework/Document/Companies%20Act%202016_as%20at%2031%20January%202025.pdf | 2026-11-14 |
| Read for Practice Directive 10/2024: two-of-three criteria and the phased thresholds | https://www.ssm.com.my/Pages/Legal_Framework/Document/NEW%20PD%2010-2024%20-%20Qualifying%20Criteria%20for%20Audit%20Exemption%20for%20Certain%20Categories%20of%20Private%20Companies%20(Portal).pdf | 2026-11-14 |

Not yet confirmed: the minimum paid-up capital of RM1 in the old file (the Act was not searched for a minimum); the incorporation timeline of 1 to 5 working days in the old file; foreign-ownership limits by sector; any amendment to the Companies Act after 31 January 2025.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `my-company-formation` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/my-company-formation. If neither is available, confirm every figure against the official source pages cited above before relying on it.
