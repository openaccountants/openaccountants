---
name: japan-references
jurisdiction: JP
last_updated: 2026-11-14
version: 1.1
description: Japan source and workflow reference router, preserving the Shinkoku open-source project reference and distinguishing software workflow inspiration from official Japanese tax authority.
tier: 2
tax_year: 2026
type: router
---

# Japan: related open-source projects and official source routing

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

Locate the Japanese primary source and the existing country workflow for the question. This file carries no tax rates, deadlines, thresholds or computation. Software documentation is evidence of the software's stated scope, not evidence of Japanese law. OpenAccountants software and skill content have different licensing tracks: read the repository's `LICENSING.md` before copying material.

### Shinkoku

- Repository: [kazukinagata/shinkoku](https://github.com/kazukinagata/shinkoku).
- License stated in its own README: MIT. Check the actual licence and attribution before incorporation; no code or dependency is installed by this reference.
- Language: Japanese.
- Stated scope: AI-agent plugin for Japanese individual tax workflows, including bookkeeping, income/consumption tax, settlement, e-Tax preparation and browser-assisted input into the NTA's 確定申告書等作成コーナー.
- Use: Japan-specific terminology, workflow design, bookkeeping patterns and validation ideas. Consider data-model or command compatibility only after examining the actual implementation and its current supported/unsupported cases.

### Current OpenAccountants Usage

The prior Japan workflow cites Shinkoku as an influence. Preserve that reference when maintaining those workflows. Check the project before inventing replacement process patterns, then confirm each legal rule against an official source and the current NTA system. A compatibility idea is not an implemented integration or an accountant approval.

## The method, step by step

1. Identify the tax job, person/entity and year. Load the existing Japan skill before choosing a portal or computing anything.
2. For residence and foreign income use `jp-nonpermanent-resident`; for ordinary resident income computation use `jp-income-tax`; for advance payments use `jp-estimated-tax`.
3. Use `jp-consumption-tax` for sole-proprietor consumption-tax eligibility/method/computation, `japan-consumption-tax` for transaction and return working papers, `jp-return-assembly` for document reconciliation and `jp-etax-filing` for reviewed input/submission preparation. Read each scope; names alone do not establish eligibility.
4. For insurance distinguish self-employed `jp-social-insurance` from employer `japan-payroll`. Use the actual municipality/insurer's official schedule, not a generic national estimate.
5. For books, accounts, formation, incorporation decisions, crypto or related-party pricing use the matching Japan skill and its source table. A software example or library sibling never replaces that job's operative law.
6. Open the official legal text, tax-authority page or filing manual that supports the particular claim. Check period, exceptions and the skill's Not yet confirmed line. Use Shinkoku only for software design/terminology, and keep outputs review-first and accountant-facing.
7. Handoff the source URLs, period, relevant documents, unconfirmed items and the working paper. Do not claim a live filing, payment or software compatibility test occurred when it did not.

## When to refuse or refer

If the source cannot be opened, the year is unsupported, the job is excluded or a workflow refusal fires, stop dependent guidance and refer with the missing evidence. Do not treat a project's feature claim, search snippet or an old example as current tax law. Never enter a taxpayer's authentication secret or submit a return through a software-integration idea.

## Sources

| Source | URL | Read on | What was read |
| --- | --- | --- | --- |
| NTA residence categories | https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/2010.htm | 2026-11-14 | Read for statutory resident/non-resident scope and conditions, as an official entry point rather than a software source |
| NTA final-return procedure | https://www.nta.go.jp/taxes/shiraberu/taxanswer/shotoku/2020.htm | 2026-11-14 | Read for official return-preparation link, filing routes and distinction between return and payment |
| Japan Pension Service premium procedure | https://www.nenkin.go.jp/service/kokunen/hokenryo/hokenryo.html | 2026-11-14 | Read for official premium/payment source and routing to relief, distinct from software calculations |
| Shinkoku's own README, software reference only | https://github.com/kazukinagata/shinkoku/blob/main/README.md | 2026-11-14 | Read for stated scope, unsupported jobs, Japanese workflows, licence statement and architecture; not cited for any legal figure |

Not yet confirmed: OpenAccountants-to-Shinkoku data/command compatibility, live browser workflow and any proposed code incorporation; current accuracy of Shinkoku tax calculations or claims of stronger coverage than other projects. Its README feature list establishes no legal verification. This routing-only file supplies no worked tax arithmetic.
