---
name: dominican-republic-social-contributions
description: Use this skill whenever asked about Dominican Republic social-security contributions (Sistema Dominicano de Seguridad Social / SDSS) for employees, employers, or self-employed persons. Trigger on phrases like "TSS contributions", "Tesorería de la Seguridad Social", "AFP Dominican Republic", "SFS health insurance", "Seguro Familiar de Salud", "SRL riesgos laborales", "INFOTEP", "aporte seguridad social RD", "cotización TSS", "salario cotizable", "tope cotizable", "self-employed social security Dominican Republic", or any question about SDSS contribution rates, ceilings, or TSS filing. Also trigger when classifying bank transactions for TSS / AFP / SFS / INFOTEP remittances, or reconciling SDSS for an ISR computation. This skill covers AFP (pension), SFS (health), SRL (occupational risk), INFOTEP (training), the contributory-wage floor and ceilings, payment schedule, and the interaction with income tax (ISR). ALWAYS read this skill before touching any Dominican Republic social-contribution work.
version: 0.1
jurisdiction: DO
tax_year: 2025
last_updated: 2026-07-13
reviewed_by: Miguel Lantigua
review_status: current
depends_on: - social-contributions-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Dominican Republic Social Security Contributions (SDSS / TSS)

## Dominican Republic Social Security Contributions (SDSS / TSS) Skill v0.1

**Tier 2 — research-verified. Figures sourced from the Tesorería de la Seguridad Social (TSS), PwC Worldwide Tax Summaries (updated 5 Dec 2025), and Dominican payroll references. NOT yet signed off by a licensed Dominican contador. Treat every computation as an estimate pending professional review.**

## Section 1 -- Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Dominican Republic |
| Currency | DOP (Dominican peso, RD$) only |
| System | Sistema Dominicano de Seguridad Social (SDSS) |
| Collection agency | Tesorería de la Seguridad Social (TSS) |
| Pension | AFP (Administradoras de Fondos de Pensiones) |
| Health | SFS (Seguro Familiar de Salud), administered via ARS |
| Occupational risk | SRL (Seguro de Riesgos Laborales) |
| Training levy | INFOTEP |
| Legislation | Ley 87-01 (SDSS); Ley 116-80 + Reglamento (INFOTEP) |
| Payment | Monthly, via the TSS platform, within the first working days of the following month |
| Validated by | Pending -- requires sign-off by a licensed Dominican contador |
| Skill version | 0.1 |

### Contribution rates (employment)

**Contribution rates (employment)**  _(Sources: TSS; PwC Worldwide Tax Summaries — Dominican Republic, Other taxes.)_

| Contribution | Employee | Employer | Total | Base ceiling |
| --- | --- | --- | --- | --- |
| AFP — pension | 2.87% | 7.10% | 9.97% | 20× the minimum cotizable wage |
| SFS — health (family) | 3.04% | 7.09% | 10.13% | 10× the minimum cotizable wage |
| SRL — occupational risk | 0.00% | ~1.20% (1.0% fixed + variable by risk class) | ~1.20% | 4× the minimum cotizable wage; employer-only |
| INFOTEP — training | 0.50% of bonuses only | 1.00% of monthly payroll | — | no SDSS ceiling |
| **Employee payroll total** | **5.91%** (AFP 2.87 + SFS 3.04) | — |  |  |
| **Employer payroll total** | — | **~16.39%** (7.10 + 7.09 + ~1.20 + 1.00) |  |  |

> **SRL is approximate.** ~1.0% fixed for all employers plus a variable surcharge by risk classification (Type I–IV). Confirm the company's assigned SRL rate from its TSS classification rather than assuming 1.20%. [TSS; Contadom]
>
> **INFOTEP employee 0.5% applies only to bonuses/gratification (regalía), not to ordinary salary.**

### Contributory-wage floor and ceilings

- **Salario cotizable base** — The base is the salario cotizable, between 1× the minimum cotizable wage (floor) and the per-fund ceiling. The minimum cotizable wage is set by TSS resolution.  _(TSS Res. 01-2025)_

**Contributory-wage floor and ceilings table**  _(TSS Res. 01-2025)_

| Period | Min cotizable wage | AFP ceiling (20×) | SFS ceiling (10×) | SRL ceiling (4×) |
| --- | --- | --- | --- | --- |
| 1 Apr 2025 – 31 Jan 2026 | RD$21,674.80/mo | RD$433,496/mo | RD$216,748/mo | RD$86,699.20/mo |
| from 1 Feb 2026 | RD$23,223/mo | RD$464,460/mo | RD$232,230/mo | RD$92,892/mo |

- **Ceiling application rule** — Use the ceiling matching the contribution month. Salary above a fund's ceiling does not increase that fund's contribution.  _(TSS Res. 01-2025)_

### Conservative defaults

**Conservative defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown SRL risk class | Use 1.20% and flag for reviewer to confirm the TSS-assigned rate |
| Unknown contribution month (which ceiling) | Use the ceiling for the period the salary was paid |
| Self-employed vs employee unclear | STOP — the regimes differ; confirm before computing |
| Salary below 1× min cotizable | Apply the 1× floor as the base |

## Section 2 -- Required Inputs & Refusal Catalogue

- **Minimum viable inputs** — Minimum viable — gross monthly salary (or self-employed contributory income) and the contribution month (to pick the ceiling). Without a salary figure, STOP.
- **Recommended inputs** — Recommended — the employer's SRL risk classification, and whether the worker is salaried (employee) or self-employed/independent.
- **R-DO-SSC-1** — Self-employed/voluntary affiliation. Self-employed affiliation rules and rates differ from the salaried split above; do not apply the 2.87% / 7.10% employee/employer split to a self-employed person. Escalate to a reviewer.  _(R-DO-SSC-1)_
- **R-DO-SSC-2** — SRL arrears or reclassification. Do not quantify SRL arrears or risk-class disputes without the TSS classification letter.  _(R-DO-SSC-2)_

## Section 3 -- Payment Pattern Library (bank statement / accounting)

**Payment Pattern Library**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| TSS, TESORERIA SEGURIDAD SOCIAL | EXCLUDE — SDSS remittance | Combined AFP+SFS+SRL+INFOTEP payment |
| AFP, FONDO PENSIONES, SIPEN | EXCLUDE — pension | Part of the TSS remittance |
| SFS, ARS, SEGURO FAMILIAR SALUD | EXCLUDE — health | Part of the TSS remittance |
| INFOTEP | EXCLUDE — training levy | Employer 1% of payroll |
| DGII, ISR, RETENCIÓN | EXCLUDE — income tax, not SDSS | Different obligation |

### Example 1 — Mid salary (gross RD$50,000/month, Apr-2025 ceilings)

- AFP employee 2.87% × 50,000 = **RD$1,435.00**; SFS employee 3.04% × 50,000 = **RD$1,520.00** → employee TSS = **RD$2,955.00**
- Employer: AFP 7.10% = 3,550.00; SFS 7.09% = 3,545.00; SRL 1.20% = 600.00; INFOTEP 1% = 500.00 → **RD$8,195.00**
- All below the per-fund ceilings (50,000 < 216,748 SFS ceiling).

### Example 2 — High salary above the SFS ceiling (gross RD$300,000/month)

- SFS base capped at RD$216,748 → SFS employee 3.04% × 216,748 = **RD$6,589.14** (NOT 3.04% × 300,000)
- AFP base 300,000 < 433,496 ceiling → AFP employee 2.87% × 300,000 = **RD$8,610.00**
- Apply each fund's own ceiling independently.

## Section 5 -- Tier 1 Rules

- **[T1] Employee TSS total** — Employee TSS = AFP 2.87% + SFS 3.04% = 5.91% of salario cotizable, each capped at its own ceiling (AFP 20×, SFS 10×).  _([TSS; PwC])_
- **[T1] Employer TSS total** — Employer TSS = AFP 7.10% + SFS 7.09% + SRL ~1.20% + INFOTEP 1% ≈ 16.39%.  _([TSS; PwC])_
- **[T1] Independent ceilings per fund** — Each fund uses its OWN ceiling — cap AFP at 20×, SFS at 10×, SRL at 4× the minimum cotizable wage; do not apply one ceiling to all funds.
- **[T1] INFOTEP base restriction** — INFOTEP employee 0.5% applies only to bonuses/gratification, never to ordinary salary.
- **[T1] Remittance schedule** — Contributions are remitted monthly via the TSS platform; the same remittance covers all four funds.

## Section 6 -- Tier 2 Catalogue (reviewer judgement)

- **T2-1 SRL risk class.** The variable SRL surcharge depends on the company's Type I–IV classification; confirm the assigned rate.
- **T2-2 Self-employed affiliation.** Different rate structure — confirm before computing.
- **T2-3 Multiple employers.** Contribution-base aggregation across employers needs reviewer handling.

## Section 7 -- Interaction with Income Tax

- **AFP+SFS deducted before ISR** — Employee AFP + SFS contributions (5.91%) are deducted from salary before the ISR retención is computed — see `dominican-republic-payroll.md` and `dominican-republic-income-tax.md`. The ISR annual exempt threshold is RD$416,220 (FY2025).  _(dominican-republic-payroll.md; dominican-republic-income-tax.md)_

## Section 8 -- Test Suite

**Test 1:** Gross RD$50,000 (Apr-2025). → employee TSS 2,955.00; employer TSS 8,195.00.
**Test 2:** Gross RD$300,000. → SFS employee capped at 216,748 → 6,589.14; AFP employee 8,610.00 (uncapped at this level).
**Test 3:** Gross RD$21,674.80 (= 1× floor, Apr-2025). → employee TSS 5.91% × 21,674.80 = RD$1,281.00.

## PROHIBITIONS

- NEVER apply one ceiling to all funds — AFP (20×), SFS (10×), and SRL (4×) each have their own.
- NEVER charge employees SRL — it is employer-only.
- NEVER apply INFOTEP 0.5% to ordinary salary — it is on bonuses only.
- NEVER use the wrong period's minimum cotizable wage — the ceilings changed on 1 Feb 2026.
- NEVER present SDSS figures as definitive — label as estimated and direct to a licensed Dominican contador.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a licensed contador in the Dominican Republic) before filing or acting upon.

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
