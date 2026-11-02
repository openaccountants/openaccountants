---
name: pk-it-export-tax
description: >
  Use this skill whenever asked about how Pakistani freelancers and IT exporters are taxed on income
  earned from foreign clients. Trigger on phrases like "Pakistan freelancer tax", "IT export tax
  Pakistan", "PSEB tax", "Upwork Fiverr tax Pakistan", "0.25% IT export", "software export tax
  Pakistan", "remittance tax freelancer". Covers the concessional final-tax regime on exported IT and
  IT-enabled services, the PSEB registration benefit, the banking-channel/remittance requirement, and
  the difference vs ordinary business income. ALWAYS read this before any Pakistan IT-export work.
version: 1.0
jurisdiction: PK
tax_year: 2026
tier: 2
last_updated: 2026-06-12
category: international
depends_on:
  - income-tax-workflow-base
---

# Pakistan IT & Freelance Export Tax — Skill v1.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Section 1 — Quick Reference

| Field | Value |
|---|---|
| Country | Pakistan |
| Who this is for | Freelancers / firms exporting IT & IT-enabled services (software, design, BPO, remote work for foreign clients) |
| Concessional final tax — PSEB-registered exporter | ~0.25% of export proceeds (verify current Finance Act rate) |
| Concessional final tax — not PSEB-registered | ~1% of export proceeds (verify) |
| Condition | Proceeds **remitted through normal banking channels** into Pakistan (PRC / bank credit advice) |
| Currency | PKR |
| Tax year | 1 July – 30 June |
| Tax authority | Federal Board of Revenue (FBR) — IRIS portal (iris.fbr.gov.pk) |
| Registrations | NTN (FBR) + PSEB registration (pseb.org.pk) for the lower rate |
| Quality tier | Research-verified — pending sign-off by a Pakistani tax practitioner |
| Skill version | 1.0 |

### Conservative defaults
| Ambiguity | Default |
|---|---|
| PSEB registration unknown | Assume NOT registered → higher (~1%) rate; recommend registering |
| Remittance channel unknown | Assume informal → concession may be LOST; require banking-channel proof |
| Whether income is "export of services" | Foreign client + service delivered from Pakistan + foreign-currency remittance = export |

## Section 2 — How it works (Tier 1)
- Income from **export of IT/ITeS** is taxed under a **concessional final-tax regime** instead of the normal progressive business slabs — provided proceeds are **brought into Pakistan through banking channels** in foreign currency.
- **PSEB registration** (Pakistan Software Export Board) secures the **lowest** rate (~0.25%). Without it, a higher rate (~1%) applies. Verify the exact rates in the current Finance Act — these have changed and may be a final tax or a reduced/minimum tax.
- Keep the **bank credit advice / PRC (Proceeds Realization Certificate)** for every receipt — it is the evidence the concession depends on.
- Domestic (Pakistan-client) income does **not** get the export concession — it falls under ordinary business income (see pk-income-tax).

## Section 3 — Worked Example
Freelancer earns USD 30,000 from foreign clients via Upwork, remitted through a Pakistani bank (≈ PKR 8,400,000):
- **PSEB-registered:** ~0.25% final tax ≈ **PKR 21,000**.
- **Not PSEB-registered:** ~1% ≈ **PKR 84,000**.
- Compare with ordinary business slabs (up to 45%) — the export concession is dramatically lower. Verify rates.

## Section 10 — Prohibitions
- NEVER apply the export concession to proceeds NOT remitted through banking channels.
- NEVER apply it to domestic-client income.
- NEVER state the rate as final without verifying the current Finance Act (rates change yearly).
- NEVER omit the PSEB-registration recommendation for the lower rate.

## Disclaimer
Informational only; not advice. The IT-export tax rate, its final-vs-minimum character, and PSEB rules change with each Finance Act — verify with the FBR and PSEB. All outputs must be reviewed and signed off by a qualified Pakistani tax practitioner before filing. Maintained at [openaccountants.com](https://www.openaccountants.com).
