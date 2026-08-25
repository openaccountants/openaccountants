---
name: armenia-tax-optimization
description: Use this skill whenever asked about reducing tax in Armenia, tax planning, or legal strategies to minimise tax for a sole proprietor or small company in Armenia. Trigger on phrases like "reduce tax Armenia", "turnover tax Armenia", "micro business Armenia 0%", "simplified tax", "sole proprietor vs LLC Armenia", "Armenia dividends 5%", "save tax Armenia", "tax planning Armenia". This skill covers the turnover-tax (simplified) regime, the micro-business 0% regime, the general system (CIT/PIT + VAT), dividend taxation, and the critical 2025 exclusion of professional/advisory services from the special regimes. ALWAYS read this skill before advising on any Armenian tax optimisation.
version: 0.1
jurisdiction: AM
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
category: tax-optimization
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Armenia Tax Optimization

## Armenia Tax Optimization Skill v0.1

**Tier 2 — research-verified. Sources: State Revenue Committee (SRC), PwC Armenia, Vardanyan & Partners, EasyTaxes. Figures must agree with `armenia-income-tax.md` / `armenia-social-contributions.md`. NOT yet signed off by an Armenian tax adviser. Aggressive positions are never advised; every suggestion must be reviewed.**

## Section 1 -- Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Republic of Armenia |
| Currency | AMD (dram) |
| Headline levers | Turnover tax (single tax replacing CIT + VAT); micro-business 0%; general system 18% CIT |
| Dividends | **5%** withholding |
| Anti-avoidance | **Professional/advisory services EXCLUDED from the special regimes (from 1 Jul 2025)** |

> **The Armenian headline is the TURNOVER-TAX regime** — a single tax on revenue that replaces both profit tax and VAT for businesses under the threshold. **But beware:** from **1 July 2025** professional/advisory services (legal, accounting, consulting, IT-advisory, engineering, etc.) are **excluded** and must use the general system.

## Section 2 -- Turnover-Tax (simplified) Regime

**Turnover-Tax (simplified) Regime**

| Feature | Detail |
| --- | --- |
| Threshold | Annual sales **< AMD 115,000,000** (~USD 291k) |
| Replaces | Profit tax **and** VAT — a single tax on revenue |
| Trade rate | **10%** (raised from 5% in 2025); since 2025 you can deduct **9.5% of documented purchase costs**, with a **1%-of-turnover minimum** effective floor |
| Other activities | Different turnover-tax rates apply by activity. **[RESEARCH GAP — reviewer to confirm the rate for the specific activity.]** |

## Section 3 -- Micro-Business (0%)

- **0% tax** for annual sales **< AMD 24,000,000** (~USD 61k), limited to specific activities (manufacturing, hospitality/accommodation, education, digital content creation, certain non-Yerevan retail, artisan work, etc.). (Vardanyan & Partners)

## Section 4 -- General System & Extraction

**General System & Extraction**

| Item | Rate |
| --- | --- |
| Sole proprietor (PE) profit tax | 23% |
| LLC corporate tax | 18% |
| Dividends | 5% withholding |
| PIT (employment) | 20% flat (per `armenia-income-tax.md`) |

For an LLC: 18% CIT, then 5% on dividends → relatively low all-in extraction; retained profit is taxed at the corporate level.

## Section 5 -- Red Lines (do not cross)

- **Professional/advisory services exclusion** — legal, accounting, audit, management consulting, market research, advertising, engineering, architectural, healthcare and similar advisory work cannot use the turnover-tax or micro-business regimes — they must operate under the general system (18% CIT + VAT). Misclassifying advisory work to claim the low regimes is a primary risk. AUDIT FLASH POINT.  _(from 1 Jul 2025)_
- **Genuine self-employment / substance requirement** — Genuine self-employment / substance required.
- **Mandatory health-insurance contribution from 2026** — Note the new mandatory health-insurance contribution from 2026 for higher earners (see `armenia-income-tax.md`) when modelling net position.  _(see `armenia-income-tax.md`)_

## PROHIBITIONS

- NEVER place professional/advisory-services income into the turnover-tax or micro-business regime (excluded from 1 Jul 2025).
- NEVER present the turnover tax as still 5% — the trade rate rose to 10% in 2025.
- NEVER ignore the AMD 115m / AMD 24m thresholds.
- NEVER contradict the rates in `armenia-income-tax.md` / `armenia-social-contributions.md`.
- NEVER present [RESEARCH GAP] figures as confirmed, nor optimisation as definitive advice — route to a licensed Armenian tax adviser.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a licensed tax adviser in Armenia) before acting upon.

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
