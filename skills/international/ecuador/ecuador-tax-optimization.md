---
name: ecuador-tax-optimization
description: Use this skill whenever asked about reducing tax in Ecuador, tax planning, or legal strategies to minimise tax for a microenterprise, entrepreneur, or self-employed person in Ecuador. Trigger on phrases like "reduce tax Ecuador", "RIMPE", "negocio popular", "régimen emprendedores", "Ecuador 2% tax", "gastos personales", "self-employed Ecuador", "save tax Ecuador", "tax planning Ecuador". This skill covers the RIMPE regime (Negocio Popular and Emprendedor), the 2025 transition of Emprendedor to the general regime, the personal-expense rebate, and the eligibility/anti-avoidance red lines. ALWAYS read this skill before advising on any Ecuadorian tax optimisation.
version: 0.1
jurisdiction: EC
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
category: tax-optimization
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Ecuador Tax Optimization

## Ecuador Tax Optimization Skill v0.1

**Tier 2 — research-verified. Sources: SRI (Servicio de Rentas Internas), PwC Ecuador, JEZL/Contifico. Figures must agree with `ecuador-income-tax.md` / `ecuador-social-contributions.md`. NOT yet signed off by an Ecuadorian tax adviser. Aggressive positions are never advised; every suggestion must be reviewed.**

## Section 1 -- Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Republic of Ecuador |
| Currency | USD |
| Headline levers | RIMPE (Negocio Popular / Emprendedor); personal-expense rebate; IESS structuring |
| RIMPE rate | **1%–2% on gross income** (regardless of expenses); does not exceed 2% |
| 2025 change | **RIMPE Emprendedor is being moved to the General Regime** (taxed on results, not turnover) |
| Anti-avoidance | RIMPE eligibility; substance |

> **Ecuador's small-business lever is RIMPE**, but 2025 narrowed it: **Negocio Popular** (≤ USD 20,000) keeps a tiny fixed tax and **0% VAT** on its sales; **Emprendedor** ($20k–$300k) is **transitioning out to the General Regime**.

## Section 2 -- RIMPE (Negocio Popular / Emprendedor)

**RIMPE (Negocio Popular / Emprendedor)**

| Category | Who | Treatment |
| --- | --- | --- |
| **Negocio Popular** | Natural persons, gross income ≤ **USD 20,000** prior year | Tiny fixed annual income tax; **sales treated as 0% VAT** (no VAT declarations) |
| **Emprendedor** | Income **> $20,000 ≤ $300,000** (and companies $0–$300k) | 1%–2% income tax on **gross** income (regardless of expenses) — but see the 2025 change |

- **AUDIT FLASH POINT (2025)** — RIMPE **Emprendedor** taxpayers are being required to **leave RIMPE and move to the General Regime**, paying income tax on **actual results** (income − expenses) rather than on turnover. Confirm the client's current regime before relying on the 1–2% turnover rate.  _(SRI; Primicias)_

## Section 3 -- General Regime & Personal-Expense Rebate

- **General Regime taxation** — Under the General Regime: progressive income tax (per `ecuador-income-tax.md`), with **real expenses** deductible.  _(ecuador-income-tax.md)_
- **Rebaja por gastos personales** — A personal-expense **tax credit** based on family burdens (cargas familiares) reduces the tax; ensure it is claimed (Form SRI-GP). **[RESEARCH GAP — reviewer to confirm the current rebate cap by number of dependants.]**
- **RIMPE Emprendedor vs General Regime modelling** — For RIMPE Emprendedor moving to General: when real expenses are high, the General Regime can beat the 1–2% turnover tax — model both.

## Section 4 -- Red Lines (do not cross)

- **RIMPE Emprendedor transition (2025)** — Don't plan around the 1–2% turnover rate if the client must move to the General Regime.
- **Negocio Popular cap** — USD 20,000 USD (exceed it and the regime changes)
- **Substance requirement** — Substance / genuine self-employment.

## PROHIBITIONS

- **Prohibition 1** — NEVER assume RIMPE Emprendedor's 1–2% turnover tax still applies without confirming the 2025 transition.
- **Prohibition 2** — NEVER present Negocio Popular above the USD 20,000 cap.
- **Prohibition 3** — NEVER ignore the gastos-personales rebate when modelling the General Regime.
- **Prohibition 4** — NEVER contradict the rates in `ecuador-income-tax.md` / `ecuador-social-contributions.md`.
- **Prohibition 5** — NEVER present [RESEARCH GAP] figures as confirmed, nor optimisation as definitive advice — route to a licensed Ecuadorian tax adviser.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a licensed tax adviser in Ecuador) before acting upon.

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
