---
name: income-tax-workflow-base
description: >
  Routing contract for country income-tax skills that declare this shared
  dependency. Load the universal workflow and the exact country, taxpayer and
  period content before starting a working paper. This method supplies no tax
  rates, thresholds, filing dates, forms or national rules. It keeps individual
  and corporate routes separate and stops when required content cannot be
  loaded or does not cover the requested person and period. Use when a country
  skill asks for income-tax-workflow-base, including income-tax work within an
  accounting pack. The country skill owns the calculation and the professional
  reviewer owns approval of the result.
version: 0.1
jurisdiction: GLOBAL
category: foundation
type: router
domain: income-tax
tax_year: 2026
last_updated: 2026-11-12
tier: 2
depends_on:
  - workflow-base
---

# Income tax workflow routing v0.1

> **General reference only.** This method routes work to other skills. It does not establish a tax position or replace professional review of the applicable country rules.

## The method, step by step

1. Load `workflow-base` and the country skill that requested this method. Read their scope, inputs, refusal rules, sources and period labels before computing.
2. Establish the country and any state or province, the taxpayer's residence, whether the taxpayer is an individual or a legal entity, and the exact period requested. Keep an unknown fact visible; do not invent it from a filename or currency.
3. Use the country skill only for the job and taxpayer it actually covers. For corporate work, also load `corporate-income-tax-workflow-base` and an applicable corporate content skill. A corporate workflow is not a replacement for an individual's income-tax rules.
4. If this dependency appears in a bookkeeping, formation or reporting skill, keep that skill's own workflow in control. Loading an income-tax method does not extend its scope to preparing an income-tax return.
5. Follow the universal working-paper and reviewer-brief contract. Take every rate, threshold, exception, filing step and deadline from the loaded country content and its official sources for the requested period. This router supplies none of those values. A general conservative default must never override the country rules or fill a required missing fact; stop and resolve the gap instead.
6. Before handoff, list the exact skills and versions used, the taxpayer and period, source documents, computations, unresolved questions and the matters needing the professional reviewer's decision.

For authoring or reviewing a companion skill, `docs/skill-template.md` is the controlling repository standard. Its declared-shape example requirements take precedence over the legacy universal base's five-example slot. Loading that older base is not evidence that its tax year or legal examples have been checked for the requested period.

## When to refuse or refer

- A required skill cannot be loaded, two skills have the same name but different guidance, or the country rules are missing: stop the affected work and name what is missing. Do not continue from model memory.
- The loaded content covers another country, taxpayer type or period: find a content skill that covers the request or refer the gap to a qualified professional. Do not relabel old figures as current.
- Country skills conflict or do not resolve a relevant exception: preserve the conflict in the working paper for review; do not choose an unsupported treatment.
- Without review by a qualified professional in the relevant jurisdiction, do not describe a working paper as a completed or approved filing.

## Sources

These are repository workflow contracts, not legal authority. Country content must supply the official legal sources. The old empty income-tax stub was removed in commit `6279b696c`; this router restores its loadable name while using the universal workflow introduced there.

| Repository contract | URL | Read on |
|---|---|---|
| Universal workflow and companion-content contract, version 0.1 | https://github.com/openaccountants/openaccountants/blob/a92b2c4365f48772530d14b7709f5184f538c3bb/skills/global/methods/workflow-base.md | 2026-11-12 |
| Controlling authoring standard, fixed core and declared-shape example requirements | https://github.com/openaccountants/openaccountants/blob/8cdabe2dd4bb575fb6817464ebd971a2b5903f5b/docs/skill-template.md | 2026-11-12 |
| Corporate taxpayer scope, version 0.1 | https://github.com/openaccountants/openaccountants/blob/a92b2c4365f48772530d14b7709f5184f538c3bb/skills/global/methods/corporate-income-tax-workflow-base.md | 2026-11-12 |

Not yet confirmed: no country-specific legal rules are asserted by this router.
