---
name: luxembourg-tax-optimization
description: Use this skill whenever asked about reducing tax in Luxembourg, tax planning, or legal strategies to minimise tax for a self-employed person or small company in Luxembourg. Trigger on phrases like "reduce tax Luxembourg", "self-employed vs SARL", "SARL-S", "Luxembourg deductions", "third-pillar pension deduction", "interest deduction Luxembourg", "save tax Luxembourg", "tax planning Luxembourg". This skill covers the self-employed-vs-company choice, the SARL EUR 17,500 allowance, business and interest deductions, private-pension (third pillar) relief, the CNAP contribution, personal abatements, and the substance/reasonable-salary red lines. ALWAYS read this skill before advising on any Luxembourg tax optimisation.
version: 0.1
jurisdiction: LU
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
category: tax-optimization
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Luxembourg Tax Optimization

## Luxembourg Tax Optimization Skill v0.1

Tier 2 — research-verified. Sources: Administration des contributions directes (ACD), PwC Luxembourg, Guichet.lu. Figures must agree with `luxembourg-income-tax.md` / `luxembourg-social-contributions.md`. NOT yet signed off by a Luxembourg tax adviser. Aggressive positions are never advised; every suggestion must be reviewed.

## Section 1 -- Quick Reference

**Quick Reference table**

| Field | Value |
| --- | --- |
| Country | Grand Duchy of Luxembourg |
| Currency | EUR |
| Headline levers | Self-employed vs SARL/SARL-S; third-pillar pension deduction; interest & insurance deductions |
| Personal income tax | Progressive, 23 brackets, **0%–42%** |
| Corporate tax (2025) | CIT **14%** (base < €175,000) / **16%** (base > €200,000), plus municipal business tax + solidarity surtax |
| SARL allowance | Automatic **€17,500** business allowance |
| Self-employed pension (CNAP) | **24%** of net income, payable in full by the self-employed person |
| Anti-avoidance | Substance; reasonable remuneration; ATAD GAAR |

**Lever:** beyond a certain income, a **SARL/SARL-S** separates company income (CIT ~14–16%) from personal income (PIT up to 42%), letting you retain/reinvest at the lower corporate rate and control extraction. Below that, the self-employed route with full use of personal deductions is simpler.

## Section 2 -- Self-Employed vs SARL / SARL-S

**Self-Employed vs SARL / SARL-S table**

| Route | Treatment | Best when |
| --- | --- | --- |
| **Self-employed (indépendant)** | Net profit taxed on the progressive 0–42% scale; CNAP 24%; full personal deductions | Lower income, low complexity |
| **SARL-S / SARL** | CIT 14–16% on profit; **automatic €17,500 allowance**; owner takes salary (deductible) + dividends; profit can be retained at the corporate rate | Higher income, reinvesting, liability/credibility |

- **AUDIT FLASH POINT** — An owner-manager must take a reasonable salary for work performed; converting all profit into low-taxed distributions without substance is challengeable.

## Section 3 -- Deductions Most People Miss

**Deductions Most People Miss table**

| Deduction | Detail |
| --- | --- |
| Business expenses | Genuine costs of running the activity (self-employed) / company (SARL). |
| Mortgage interest (own home) | Deductible — **uncapped** for the year the rental value is fixed + the following year; then ceilings €4,000 / €3,000 / €2,000. |
| Personal-loan & insurance interest/premiums | Life/health/accident/liability premiums + personal-loan interest deductible up to **€672** (+ same per spouse and per dependent child). |
| SARL €17,500 allowance | Automatic, no formalities. |

## Section 4 -- Pension & Retirement Reliefs

**Pension & Retirement Reliefs table**

| Relief | Detail |
| --- | --- |
| Third-pillar private pension | Premiums deductible up to **€3,200** (**€4,500 from tax year 2026**). |
| Employer pension scheme (employee) | Deductible up to **€1,200/yr**. |
| CNAP (self-employed) | 24% of net income — mandatory, but full deductibility/relief mechanics should be confirmed. **[RESEARCH GAP — reviewer to confirm CNAP deductibility for the self-employed.]** |

## Section 5 -- Personal Abatements

**Personal Abatements table**

| Item | Detail |
| --- | --- |
| Joint professional abatement | €4,500 where both jointly-taxed spouses/partners have professional income. |
| Tax classes | Class 1 / 1a / 2 affect the rate — confirm the correct class (married/partnered/with children). |
| Extra-professional / commuter / other abatements | Several standard abatements apply — confirm eligibility. **[RESEARCH GAP — reviewer to confirm current abatement amounts.]** |

## Section 6 -- Red Lines (do not cross)

- **Reasonable salary** — Owner-managers must be paid a market salary; all-dividend extraction without substance is challengeable.
- **Substance** — A SARL must carry on genuine business and be managed in Luxembourg.
- **ATAD GAAR** — ATAD GAAR applies to arrangements whose main purpose is a tax advantage.

## PROHIBITIONS

- **No-salary-only-distributions advice** — NEVER advise an active SARL owner to take no salary and only distributions.
- **Incorporation as pure tax play** — NEVER present incorporation purely as a tax play without the substance/reasonable-salary warning.
- **Rate contradiction** — NEVER contradict the rates in `luxembourg-income-tax.md` / `luxembourg-social-contributions.md` (note: 2026 pension contribution is 8.5% each side).
- **Research gap presentation** — NEVER present [RESEARCH GAP] figures as confirmed, nor optimisation as definitive advice — route to a licensed Luxembourg tax adviser.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a licensed tax adviser in Luxembourg) before acting upon.

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
