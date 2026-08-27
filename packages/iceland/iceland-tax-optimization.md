---
name: iceland-tax-optimization
description: Use this skill whenever asked about reducing tax in Iceland, tax planning, or legal strategies to minimise tax for a self-employed person or small company in Iceland. Trigger on phrases like "reduce tax Iceland", "ehf vs self-employed", "Iceland dividends 22%", "reiknað endurgjald", "reference salary", "Iceland company tax 20%", "save tax Iceland", "tax planning Iceland". This skill covers the ehf-company-plus-dividend structure vs self-employment, the mandatory owner reference-salary rule (reiknað endurgjald), capital-income vs labour-income treatment, pension and personal reliefs, and the anti-avoidance red lines. ALWAYS read this skill before advising on any Icelandic tax optimisation.
version: 0.1
jurisdiction: IS
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
category: tax-optimization
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Iceland Tax Optimization

## Iceland Tax Optimization Skill v0.1

**Tier 2 — research-verified. Sources: Skatturinn (Iceland Revenue), KPMG Iceland Tax Facts 2025, PwC Iceland. Figures must agree with `iceland-income-tax.md` / `iceland-social-contributions.md`. NOT yet signed off by an Icelandic tax adviser. Aggressive positions are never advised; every suggestion must be reviewed.**

## Section 1 -- Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Iceland |
| Currency | ISK |
| Headline lever | ehf company + dividends (20% CIT + 22% dividend) vs self-employment at high progressive labour rates — subject to the reference-salary rule |
| Corporate tax (ehf) | **20%** |
| Dividend / capital income | **22%** |
| Labour income | High progressive PIT + municipal tax (well above the capital rate) |
| Key rule | **reiknað endurgjald** — owner-managers must pay themselves a market reference salary before profit becomes low-taxed capital income |
| Anti-avoidance | Reference-salary rule; substance |

> **The Iceland lever is converting high-taxed labour income into lower-taxed capital income via an ehf** — but the **reiknað endurgjald** rule deliberately limits this: an active owner must first draw a reasonable salary (taxed as labour) before the remainder can be dividends at 22%.

## Section 2 -- ehf Company + Dividend vs Self-Employment

**ehf Company + Dividend vs Self-Employment**

| Route | Treatment |
| --- | --- |
| **Self-employed** | Business income taxed as **labour** on the high progressive scale + municipal tax + full social contributions |
| **ehf (private limited)** | 20% CIT on profit; profit extracted as **dividends at 22%** — but only **after** a market reference salary (labour-taxed) |

For higher earners the ehf can lower the overall rate by shifting the surplus (above a fair salary) into 22% capital income and deferring undistributed profit at the 20% corporate rate. **[RESEARCH GAP — reviewer to confirm the current labour-income brackets and whether retained ehf profit is genuinely deferred.]**

## Section 3 -- The Reference-Salary Rule (reiknað endurgjald) — the key constraint

- **Reference-salary requirement** — Skatturinn publishes minimum reference-salary tables by occupation. An owner-manager who actively works in their ehf (or as self-employed) must declare at least that reference salary as labour income; you cannot take everything as 22% dividends to dodge labour tax.  _(Skatturinn)_

> **AUDIT FLASH POINT.** Under-declaring the owner salary below the reference tables is a primary Skatturinn audit target. Set the salary at/above the published reference for the occupation and document it.

## Section 4 -- Deductions & Reliefs

**Deductions & Reliefs**

| Item | Detail |
| --- | --- |
| Personal tax credit (persónuafsláttur) | A fixed annual credit reduces tax for every resident — ensure fully used. |
| Pension contributions | Mandatory occupational pension + deductible additional (private) pension contributions up to a cap. **[RESEARCH GAP — reviewer to confirm the deductible private-pension percentage.]** |
| Business expenses | Genuine costs deductible (self-employed / ehf). |
| Inter-company dividends | Dividends between resident limited companies are not subject to the 22% WHT — relevant for holding structures. |

## Section 5 -- Red Lines (do not cross)

- **Reference salary red line** — Never set an active owner's salary below the published occupational reference to convert labour into capital income.
- **Substance requirement** — The ehf must carry on genuine business.
- **Mislabelling private spending** — Mislabelling private spending as company expense creates taxable benefits, not deductions.

## PROHIBITIONS

- **Prohibition 1** — NEVER advise an active owner to take a salary below the Skatturinn reference tables to maximise 22% dividends.
- **Prohibition 2** — NEVER present the ehf route as avoiding labour tax entirely — the reference salary is labour-taxed.
- **Prohibition 3** — NEVER contradict the rates in `iceland-income-tax.md` / `iceland-social-contributions.md`.
- **Prohibition 4** — NEVER present [RESEARCH GAP] figures as confirmed, nor optimisation as definitive advice — route to a licensed Icelandic tax adviser.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a licensed tax adviser in Iceland) before acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

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
