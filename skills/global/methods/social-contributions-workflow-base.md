---
name: social-contributions-workflow-base
description: >
  Routing contract for social-contribution skills that declare this shared
  dependency. Load the universal workflow and the applicable country content
  before preparing contribution working papers. This method supplies no rates,
  contribution ceilings, payment dates, forms or national coverage rules. It
  separates employee, employer and self-employed routes and keeps payroll
  preparation distinct from a self-employed contribution calculation. Use when
  a country skill asks for social-contributions-workflow-base, including
  pension, health-insurance or social-security computations. Missing country
  rules, unresolved coverage and period mismatches stop the affected work.
  A qualified professional reviews the result before filing or payment.
version: 0.1
jurisdiction: GLOBAL
category: foundation
type: router
domain: payroll
tax_year: 2026
last_updated: 2026-11-12
tier: 2
depends_on:
  - workflow-base
---

# Social contributions workflow routing v0.1

> **General reference only.** This method routes work to other skills. It supplies no national social-security rules and does not replace professional review of a contribution calculation.

## The method, step by step

1. Load `workflow-base` and the country contribution skill that requested this method. Read their scope, required inputs, refusal rules, sources and period labels first.
2. Establish the country and relevant subnational system, the contribution period, the person's work and residence locations, and their employee, employer or self-employed role. Do not infer statutory coverage solely from nationality, a bank account or the location of a customer.
3. For employer payroll, load `payroll-workflow-base` and the applicable country payroll content. For a self-employed calculation, use the country self-employed contribution rules; do not substitute payroll rates or caps. Keep employee deductions, employer cost and self-employed liabilities separate.
4. Take each scheme's coverage, contribution base, rate, floor, ceiling, relief, rounding and timing from the applicable country skill and its official sources for the requested period. This router sets no common values or order of deductions. A general conservative default must never override the country rules or fill a required missing fact; stop and resolve the gap instead.
5. Follow the country skill's computation and reconcile contributions already paid, deductions and any income-tax interaction. Use another country or cross-border content skill where the work requires it; a domestic method alone does not settle competing systems.
6. Hand off a working paper and reviewer brief under `workflow-base`, naming the exact skills and versions, scheme and role for each line, source inputs, calculations, amounts already paid and unresolved coverage or relief questions.

## When to refuse or refer

- A required country skill cannot be loaded, or its name is ambiguous: stop the affected work and identify the missing content. Do not compute from remembered national rates.
- The relevant scheme, worker status, period or contribution base is unknown: obtain the missing facts before presenting a liability.
- Cross-border coverage, a special employment status, an exemption or a conflict between sources is unresolved: record it for a qualified professional; do not select a system or exemption without authority.
- Without review by a qualified professional in the relevant jurisdiction, do not label a calculation as approved for filing or payment.

## Sources

These are repository workflow contracts, not legal authority. Country content supplies the official scheme rules. The old empty social-contributions stub was removed in commit `6279b696c`; this router restores its loadable name while using the universal workflow introduced there.

| Repository contract | URL | Read on |
|---|---|---|
| Universal workflow and companion-content contract, version 0.1 | https://github.com/openaccountants/openaccountants/blob/a92b2c4365f48772530d14b7709f5184f538c3bb/skills/global/methods/workflow-base.md | 2026-11-12 |
| Payroll workflow scope, version 1.0 | https://github.com/openaccountants/openaccountants/blob/a92b2c4365f48772530d14b7709f5184f538c3bb/skills/global/methods/payroll-workflow-base.md | 2026-11-12 |

Not yet confirmed: no country-specific legal rules are asserted by this router.
