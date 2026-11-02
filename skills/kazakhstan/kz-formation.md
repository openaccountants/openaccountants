---
name: kz-formation
description: >
  Use this skill whenever asked how to register or start a business in Kazakhstan as a self-employed
  person. Trigger on phrases like "register ИП Kazakhstan", "how to start freelancing Kazakhstan",
  "open ТОО", "ИП регистрация", "Astana Hub registration", "business formation Kazakhstan". Covers
  registering an individual entrepreneur (ИП), choosing a tax regime at registration, the LLP (ТОО)
  alternative, and the Astana Hub IT regime. ALWAYS read this before any Kazakhstan formation work.
version: 1.0
jurisdiction: KZ
tax_year: 2026
tier: 2
last_updated: 2026-06-12
category: international
depends_on:
  - income-tax-workflow-base
---

# Kazakhstan Business Formation (ИП / ТОО) — Skill v1.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Section 1 — Quick Reference

| Field | Value |
|---|---|
| Self-employed vehicle | Individual entrepreneur — ИП (индивидуальный предприниматель) |
| Company alternative | Limited liability partnership — ТОО (товарищество с ограниченной ответственностью) |
| Registration channel | eGov.kz / e-Salyq Business app / КГД; near-instant for ИП |
| Cost | ИП registration is free (state duty waived); ТОО has minimal cost |
| Tax regime chosen at registration | Simplified declaration (4%) vs general regime — see kz-simplified-regime |
| IT incentive | Astana Hub (astanahub.com) — participants get major tax relief on IT income (verify current relief) |
| VAT registration threshold | Mandatory once turnover exceeds the threshold (verify the 2026 figure — lowered under the new Tax Code); voluntary below |
| Tax authority | State Revenue Committee (КГД) |
| Quality tier | Research-verified — pending sign-off by a Kazakhstan accountant |
| Skill version | 1.0 |

### Conservative defaults
| Ambiguity | Default |
|---|---|
| Vehicle unknown | ИП for a solo freelancer; ТОО if liability protection / investors needed |
| Regime unknown | Simplified declaration (4%) for small turnover |
| IT activity | Check Astana Hub eligibility — large savings |

## Section 2 — Registering as an ИП (Tier 1)
1. Have an IIN (ИИН individual identification number) and an EDS (digital signature) or Biometric login.
2. Register via **eGov / e-Salyq Business** — notification-based, effectively same-day.
3. Choose the **tax regime** (simplified declaration / general) and pick **OKED activity codes**.
4. Decide on **VAT registration** (mandatory above the threshold; voluntary below).
5. Open a business bank account; set up e-invoicing (ЭСФ) if required (see kz-einvoice).

## Section 3 — ТОО vs ИП
| Factor | ИП | ТОО |
|---|---|---|
| Liability | Personal | Limited to the company |
| Setup | Instant, free | Charter + registration |
| Tax | Simplified/general personal | CIT 20% (or simplified for small ТОО) |
| Best for | Solo freelancers | Teams, investors, higher risk |

## Section 4 — Astana Hub (IT)
IT companies/entrepreneurs accredited by **Astana Hub** receive substantial tax relief on qualifying IT income (historically exemption from CIT/IIT, VAT, and social tax on payroll for participants). Verify the current 2026 relief and eligibility — significant for software/IT freelancers.

## Section 10 — Prohibitions
- NEVER advise skipping VAT registration once over the threshold.
- NEVER assume Astana Hub relief without confirming accreditation + current rules.
- NEVER state the VAT threshold or Astana Hub benefits without verifying the 2026 figures.

## Disclaimer
Informational only; not advice. Verify registration steps, the VAT threshold, and Astana Hub relief with the КГД / Astana Hub. All outputs must be reviewed and signed off by a qualified Kazakhstan accountant before relying on them. Maintained at [openaccountants.com](https://www.openaccountants.com).
