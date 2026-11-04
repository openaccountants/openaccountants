---
name: dtt-template
description: "Reusable template for OpenAccountants bilateral Double Tax Treaty (DTT) summary skills. NOT a jurisdiction-specific guide — copy this template, replace placeholders, set a real last_updated and tax_year, and add this file's content to a new corridor path (e.g. skills/cross-border/treaty-corridors/ eg-sa/dtt-summary.md). Trigger on \"DTT template\", \"treaty corridor template\", \"create new DTT skill\", \"add new treaty corridor\". This template file is intentionally kept in the treaty-corridors directory (jurisdiction-optional) so that list_skills can find it for template-creation workflows."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/dtt-template"
  jurisdiction: "GLOBAL"
  tax_year: "2025"
  last_updated: "2026-07-12"
---

# [Country A] ↔ [Country B] Double Tax Treaty (DTT) Summary

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Quick Reference

| Field | Value |
|-------|-------|
| Treaty Name | Agreement between [Country A] and [Country B] for the Avoidance of Double Taxation and the Prevention of Fiscal Evasion with Respect to Taxes on Income |
| Signed | [date] |
| In Force | [date] |
| Current Version | [original / amended / new] |
| MLI Status | [ratified / signed / not party] |
| Jurisdictions Covered | [Country A (code), Country B (code)] |
| Last Verified | [month year] |
| Key Note | [one-line summary of most important feature] |

---

## Withholding Tax Rate Summary

| Income Type | Treaty Rate | Treaty Article | Domestic Rate (Source) | Notes |
|-------------|------------|----------------|------------------------|-------|
| Dividends — portfolio | [%] | Art [X] | [%] | [threshold notes] |
| Dividends — substantial (≥[%] holding) | [%] | Art [X] | [%] | [holding period / threshold] |
| Interest | [%] | Art [X] | [%] | [exceptions] |
| Royalties | [%] | Art [X] | [%] | [categories if split] |
| Technical services | [%] | Art [X] | [%] | [if separate article or under business profits] |
| Capital gains — immovable property | [%] | Art [X] | [%] | Source state may tax |
| Capital gains — shares | [%] | Art [X] | [%] | [exemption conditions] |
| Pensions | [%] | Art [X] | [%] | [residence-state only / source-state] |
| Directors' fees | [%] | Art [X] | [%] | Source state may tax |

---

## Article-by-Article Summary

### Article 4: Resident — Tie-Breaker Rules

[Summary of residency tie-breaker for dual residents: permanent home → centre of vital interests → habitual abode → nationality → mutual agreement]

### Article 5: Permanent Establishment

[Summary of PE definition: fixed place, 6-month construction, service PE, dependent agent, anti-fragmentation (MLI)]

### Article 6: Income from Immovable Property

[Summary: source state may tax income from immovable property situated therein]

### Article 7: Business Profits

[Summary: profits taxable only in residence state unless PE in source state; profit attribution rules]

### Article 8: Shipping and Air Transport

[Summary: taxable only in state of effective management]

### Article 9: Associated Enterprises

[Summary: arm's length principle, transfer pricing adjustments, corresponding adjustment]

### Article 10: Dividends

[Summary of rates, thresholds, beneficial ownership requirement, government exemption]

### Article 11: Interest

[Summary of rates, government exemption, definition of interest]

### Article 12: Royalties

[Summary of rates, government exemption, definition of royalties including technical assistance]

### Article 13: Capital Gains

[Summary: immovable property → source state; business assets of PE → source state; ships/aircraft → management state; shares → [source/residence state]; other property → residence state only]

### Article 14: Independent Personal Services

[Summary: residence state only, unless fixed base or 183-day threshold in source state]

### Article 15: Dependent Personal Services (Employment)

[Summary: residence state only, unless 183-day test fails in source state]

### Article 16: Directors' Fees

[Summary: source state may tax]

### Article 17: Artistes and Sportspersons

[Summary: source state may tax]

### Article 18: Pensions

[Summary: [residence state only / source state may tax]]

### Article 19: Government Service

[Summary: government salaries taxed only by paying government; pensions from government service]

### Article 20: Students and Trainees

[Summary: exemptions for maintenance/education payments]

### Article 21: Other Income

[Summary: residence state only, unless effectively connected to PE/fixed base]

### Article 23: Methods for Elimination of Double Taxation

[Summary: [credit method / exemption method]; [any limitations]]

---

## Tax Residency Certificate (TRC) Requirements

- **Format:** Original TRC from the resident's tax authority
- **Authentication:** [Apostille / legalisation] required for cross-border use
- **Validity:** Typically 1 year from date of issue (Egypt: [date-specific rules])
- **Egypt process:** Non-resident recipient must present TRC to claim treaty benefits; Egypt applies pay-and-refund mechanism under Ministerial Decree 771/2009 (controversial — see pitfalls)
- **[Country B] process:** [Country B-specific TRC requirements and process]

---

## Mutual Agreement Procedure (MAP)

| Field | Country A | Country B |
|-------|----------|----------|
| Competent Authority | [Ministry of Finance / ETA Conflict Resolution] | [Ministry of Finance / ZATCA / MoF] |
| Time Limit | [3 years from first notification] | [same / different] |
| Arbitration | [available / not included] | |

### MAP Contact Points

- **Egypt:** Egyptian Tax Authority (ETA) — Conflict Resolution Department, Ministry of Finance
- **[Country B]:** [Competent authority name, ministry]

---

## Anti-Treaty-Shopping / PPT (Principal Purpose Test)

[Summary of PPT or LOB provisions; MLI Article 7 status; when benefits may be denied]

---

## Cross-References to Upstream Skills

- **[countryA]-corporate-tax** — [how domestic CIT interacts with treaty]
- **[countryA]-withholding-tax** — [domestic WHT rates and DTT refund mechanism]
- **[countryB]-corporate-tax** — [how domestic tax system applies treaty benefits]

---

## Sources

- [Source 1: official treaty text URL]
- [Source 2: PwC / Deloitte / EY tax summaries]
- [Source 3: OECD Treaties Database]

**Last verified:** [month year]

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-07-12. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `dtt-template` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/dtt-template. If neither is available, confirm every figure against the official source pages cited above before relying on it.
