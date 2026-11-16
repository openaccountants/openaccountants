---
name: mc-company-formation
description: "Monaco company formation reference for 2026, using the independently reviewed October research and a November applicability check. Covers SARL and sole member SURL capital rules, the natural person exception, cash and in kind payment gates, and SAM subscription, minimum paid capital and approval requirements. Use for Monaco incorporation, entity choice and capital planning questions. Separates nationality and activity permissions from registry filings and records the 2025 and October 2026 reform transition limits. Includes two reproducible capital illustrations. Complete forms, beneficial ownership, fees, audit and accounts procedures await a named Monaco professional review."
version: 1.4
jurisdiction: MC
tax_year: 2026
last_updated: 2026-11-16
category: formation
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
type: situation-rules
---

# Monaco company formation and capital v1.4

> **General reference only.** This Guide is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

> **Source-cited draft; partial scope.** The substantive capital and permission rules were source-read on 24 October 2026 and independently reviewed on 25 October. Their current official text was checked for applicability on 16 November; unchanged research is reused. No named Monaco professional has reviewed this Guide. It produces a working paper, not a filing or a final tax position. Read the [country gap register](README.md) before use.

## Scope

This retained formation Guide covers the selected 2026 rules below. It is an Accounting packs topic, not an extra completed tax domain. It covers core SARL/SURL and SAM capital and permission gates. It does not provide a complete incorporation checklist, accounts/audit implementation or tested registry filing route.

## Ask the client first

- What activity, form, associates/managers, nationality and regulated status are intended?
- Is the sole member a natural person, and what cash/in-kind capital is proposed?
- What constitution/registration dates and existing permissions apply?
- What premises, beneficial ownership, audit and accounts requirements arise?

## The method, step by step

### Entity and capital rules

| Form | Amount or rule | Current official source |
|---|---|---|
| SARL | Minimum EUR 15,000; capital fully subscribed | [Code de commerce, arts. 35-1–35-3](https://legimonaco.mc/code/code-commerce/) |
| SURL with one natural-person member | Minimum EUR 8,000; do not apply this exception to every sole-member company | [Art. 35-3](https://legimonaco.mc/code/code-commerce/) |
| SARL/SURL cash | At least the minimum capital paid at constitution; fully paid within eighteen months, subject to transition scope | [Art. 35-3 and consolidation note](https://legimonaco.mc/code/code-commerce/) |
| SARL/SURL in-kind | Fully paid at constitution; valuation and liability rules apply | [Art. 35-3](https://legimonaco.mc/code/code-commerce/) |
| SAM | Minimum EUR 150,000; all capital subscribed, each cash subscriber pays at least one quarter and total paid capital cannot be below the minimum | [Law 1.573, arts. 15–18](https://legimonaco.mc/tnc/loi/2025/04-08-1.573) |
| SAM cash balance | Within eighteen months after first constitutive assembly, subject to applicable special rules | [Art. 16](https://legimonaco.mc/tnc/loi/2025/04-08-1.573) |

Code article 35-1 recognises a sole-member SURL. Article 35-3 requires cash paid through a Monaco credit institution account evidenced for RCI registration. Its note limits the eighteen-month rule to companies registered after Law 1.573's entry into force. Assess actual incorporation and registration dates; do not rewrite older companies' obligations from the current rule alone. [Arts. 35-1–35-3](https://legimonaco.mc/code/code-commerce/).

SAM constitution needs administrative authorisation under article 11. Article 12 allows private deed or notarial deed. Do not repeat the old universal-notary or half-capital rule. In-kind contributions and special advantages need the separate article 18 procedure. Capital is not a formation fee and is not evidence of permission to trade. [Arts. 11–18](https://legimonaco.mc/tnc/loi/2025/04-08-1.573).

### Permissions and filing sequence

Determine activity, legal form, nationality of associates/managers and any regulated profession first. Law 1.144 distinguishes declarations for specified Monegasque persons/associates/managers from authorisation for foreign counterparts; specified regulated activities also require authorisation for Monegasque persons. Foreign branches/offices face their own authorisation rule. SAM approval is separate. Do not promise a universal approval time or start date. [Arts. 1–8](https://legimonaco.mc/tnc/loi/1991/07-26-1.144/); [Art. 11](https://legimonaco.mc/tnc/loi/2025/04-08-1.573).

Prepare the applicable permission dossier, constitutional documents, subscriptions, payment/valuation evidence and registry application. This is a working sequence, not a verified exhaustive filing list. Current application forms, beneficial-owner/registry filings, fees and practical acceptance have not been checked end to end.

### October 2026 reforms and unresolved accounts work

Read the consolidated Code together with Law 1.596 of 9 October 2026. Its article 93 generally applies from the day after publication; article 102 separately defers four specified provisions until implementing regulations set their date, no later than 31 December 2026. Articles 94–103 also address transitional cases. This Guide has not established the implementing instruments for those deferred provisions or a complete accounts/audit filing calendar. Do not state that every October amendment operates on the same date. [Arts. 93–103](https://legimonaco.mc/tnc/loi/2026/10-09-1.596/).

## Worked cases

### Ordinary SARL cash capital and the SAM funding decision

Assume a new post-reform SARL with EUR 30,000 all-cash subscribed capital and no special requirement. Minimum cash at constitution is EUR 15,000 and the remaining EUR 15,000 falls under the applicable eighteen-month rule, not a statement that 50% is a universal fraction. [Code article 35-3](https://legimonaco.mc/code/code-commerce/). If the same EUR 30,000 is the founders' entire cash budget, it funds this SARL's stated minimum but falls EUR 120,000 below the SAM's EUR 150,000 minimum. That is a funding screen, not a conclusion that the SARL is licensed or suitable for the activity ([Law 1.573 arts. 15-16](https://legimonaco.mc/tnc/loi/2025/04-08-1.573)).

```oa-check
name: SARL statutory minimum cash versus subscribed amount
inputs:
  subscribed: 30000
  minimum: 15000
  sam_minimum: 150000
steps:
  - initial_minimum: min(subscribed, minimum)
  - remaining: subscribed - initial_minimum
  - sam_funding_shortfall: max(0, sam_minimum - subscribed)
expected:
  initial_minimum: 15000
  remaining: 15000
  sam_funding_shortfall: 120000
```

### SAM aggregate floor overrides one quarter

Assume EUR 300,000 all-cash SAM capital, equal cash payment proportions for every shareholder and no special requirement. One quarter would be EUR 75,000, below the EUR 150,000 minimum. At least EUR 150,000 must therefore be paid overall, while each subscriber's quarter test is independently satisfied. EUR 150,000 remains due under [Law 1.573 article 16](https://legimonaco.mc/tnc/loi/2025/04-08-1.573).

```oa-check
name: SAM quarter subscription with aggregate minimum floor
inputs:
  subscribed: 300000
  minimum: 150000
steps:
  - quarter: subscribed / 4
  - initial_minimum: max(quarter, minimum)
  - remaining: subscribed - initial_minimum
expected:
  quarter: 75000
  initial_minimum: 150000
  remaining: 150000
```

## When to refuse or refer

Stop at a working paper where the activity permission, existing-company transition, contribution valuation, registry/beneficial-owner process or accounts/audit obligations have not been established for the facts. Do not treat deposited capital as a fee, a licence or permission to start trading. The unconfirmed items below are outside usable filing guidance; obtain a Monaco professional's advice for the incorporation itself.

## Completion checklist

Record nationality/activity gates, incorporation and registration dates, subscriptions, cash and in-kind amounts, payment evidence and the applicable transition. Keep every original capital input in the working paper. Refer implementation gaps rather than presenting this selected reference as a complete incorporation checklist.

## Sources

| Official source and provisions read | URL | Read on |
|---|---|---|
| Code de commerce, arts. 35-1–35-3 and transition note; original read reused with unchanged official visible text checked on 2026-11-16 | https://legimonaco.mc/code/code-commerce/ | 2026-10-24 |
| Law 1.573, arts. 11–18 and art. 101(7); original read reused with unchanged official visible text checked on 2026-11-16 | https://legimonaco.mc/tnc/loi/2025/04-08-1.573 | 2026-10-24 |
| Law 1.144, arts. 1–8; original read reused with unchanged official visible text checked on 2026-11-16 | https://legimonaco.mc/tnc/loi/1991/07-26-1.144/ | 2026-10-24 |
| Law 1.596, arts. 93–103; original read reused with unchanged official visible text checked on 2026-11-16 | https://legimonaco.mc/tnc/loi/2026/10-09-1.596/ | 2026-10-24 |

**Not yet confirmed:** SNC and SCS partnership rules, SAM board size and statutory-auditor duty (carried in the earlier version without a cited provision), complete registry/beneficial-owner procedures, fees, sanctions, account/audit thresholds and deferred October implementation. Obtain Monaco professional review before incorporation or filing.

> Contributed by OpenAccountants.
