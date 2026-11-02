---
name: kz-tax-optimization
description: >
  Use this skill whenever asked about legally reducing tax for a self-employed person or small
  business in Kazakhstan. Trigger on phrases like "reduce tax Kazakhstan", "simplified vs general
  Kazakhstan", "tax planning Kazakhstan ИП", "VAT threshold Kazakhstan", "Astana Hub tax". Covers
  choosing the optimal special tax regime, the VAT-threshold lever, the Astana Hub IT relief, and
  the disguised-employment risk — legal planning only. ALWAYS read this before Kazakhstan planning.
version: 1.0
jurisdiction: KZ
tax_year: 2026
tier: 2
last_updated: 2026-06-12
category: international
depends_on:
  - income-tax-workflow-base
---

# Kazakhstan Tax Optimization (Self-Employed) — Skill v1.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Section 1 — Quick Reference

| Field | Value |
|---|---|
| Scope | LEGAL tax planning only |
| Currency | KZT; MRP (МРП) ₸4,325, min wage ₸85,000 for 2026 (verify) |
| Main levers | Regime choice · VAT threshold · Astana Hub (IT) · contribution minimums |
| Tax authority | State Revenue Committee (КГД) |
| Quality tier | Research-verified — pending sign-off by a Kazakhstan accountant |
| Skill version | 1.0 |

> **2026 Tax Code context:** the patent and retail-tax special regimes were abolished and the special-regime menu cut to three; the simplified declaration is now a single **4%** rate (maslikhat-adjustable 2–6%). VAT rate and registration threshold changed — verify the current figures.

## Section 2 — Choosing the regime (Tier 1)

| Regime | Tax | Best when |
|---|---|---|
| Simplified declaration (Форма 910) | 4% of turnover (no expense deduction) | Service/low-cost businesses under the turnover ceiling |
| General regime | ИПН 10% on **net profit** | High documented expenses (low margin), or over the simplified ceiling |
| Astana Hub (IT) | Major relief on qualifying IT income | Software/IT activity that qualifies for accreditation |

**Break-even logic:** simplified (4% of turnover) beats general (10% of profit) whenever your net margin is **above 40%** (4% of turnover = 10% of profit at a 40% margin). Below ~40% margin with documented costs, the general regime is usually cheaper.

## Section 3 — The VAT threshold lever
Staying below the VAT registration threshold avoids charging VAT and the compliance burden. The 2026 Tax Code **lowered** the threshold (verify), so more small businesses now cross it — plan turnover timing and watch the rolling test. Once over, registration is mandatory.

## Section 4 — Astana Hub (IT)
For software/IT freelancers, **Astana Hub** accreditation can deliver the single biggest legal saving (historically CIT/IIT, VAT and payroll social-tax relief on qualifying IT income). Verify current eligibility and relief.

## Section 5 — Worked personas
- **Designer, ₸15m turnover, 80% margin:** simplified 4% = ₸600,000. General 10% on ₸12m profit = ₸1.2m. **Simplified wins.**
- **Reseller, ₸40m turnover, 15% margin:** simplified 4% = ₸1.6m. General 10% on ₸6m profit = ₸600,000. **General wins** (and watch the VAT threshold).
- **IT contractor:** check **Astana Hub** first — can beat both.

## Section 6 — Risks & red flags
- **Disguised employment:** a company replacing employees with ИП contractors to cut social/payroll tax is an anti-avoidance target — flag, don't advise.
- **Artificial splitting** of turnover across multiple ИП to stay under thresholds is an evasion scheme — prohibited.

## Section 10 — Prohibitions
- NEVER advise disguised employment or turnover-splitting to dodge thresholds.
- NEVER claim Astana Hub relief without confirming accreditation + current rules.
- NEVER state VAT threshold / rates without verifying the 2026 Tax Code.

## Disclaimer
Informational only; legal planning needs a qualified Kazakhstan accountant. Verify all 2026 figures with the КГД. Maintained at [openaccountants.com](https://www.openaccountants.com).
