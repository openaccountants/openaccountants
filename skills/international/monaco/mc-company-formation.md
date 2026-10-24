---
name: mc-company-formation
description: "Monaco company formation reference checked in October 2026. Covers SARL and sole member SURL capital rules, the natural person exception, cash and in kind payment gates, and SAM subscription, minimum paid capital and approval requirements. Use for Monaco incorporation, entity choice and capital planning questions. Separates nationality and activity permissions from registry filings and records the 2025 and October 2026 reform transition limits. Includes two reproducible capital illustrations. Complete forms, beneficial ownership, fees, audit and accounts procedures await a named Monaco professional review."
jurisdiction: MC
category: formation
tax_year: 2026
last_updated: 2026-10-24
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
version: 1.2
---

# Monaco company formation and capital

> **Source-cited draft; partial scope.** Checked 24 October 2026. No named Monaco professional has reviewed this Guide. It produces a working paper, not a filing or a final tax position. Read the [country gap register](README.md) before use.

## Scope and currency

This retained formation Guide is a source-cited reference checked 24 October 2026. It is an Accounting packs topic, not an extra completed tax domain. It covers core SARL/SURL and SAM capital and permission gates. It does not provide a complete incorporation checklist, accounts/audit implementation or tested registry filing route.

## Entity and capital rules

| Form | Rule | Current official source |
|---|---|---|
| SARL | Minimum EUR 15,000; capital fully subscribed | [Code de commerce, arts. 35-1–35-3](https://legimonaco.mc/code/code-commerce/) |
| SURL with one natural-person member | Minimum EUR 8,000; do not apply this exception to every sole-member company | [Art. 35-3](https://legimonaco.mc/code/code-commerce/) |
| SARL/SURL cash | At least the minimum capital paid at constitution; fully paid within eighteen months, subject to transition scope | [Art. 35-3 and consolidation note](https://legimonaco.mc/code/code-commerce/) |
| SARL/SURL in-kind | Fully paid at constitution; valuation and liability rules apply | [Art. 35-3](https://legimonaco.mc/code/code-commerce/) |
| SAM | Minimum EUR 150,000; all capital subscribed, each cash subscriber pays at least one quarter and total paid capital cannot be below the minimum | [Law 1.573, arts. 15–18](https://legimonaco.mc/tnc/loi/2025/04-08-1.573) |
| SAM cash balance | Within eighteen months after first constitutive assembly, subject to applicable special rules | [Art. 16](https://legimonaco.mc/tnc/loi/2025/04-08-1.573) |

Code article 35-1 recognises a sole-member SURL. Article 35-3 requires cash paid through a Monaco credit institution account evidenced for RCI registration. Its note limits the eighteen-month rule to companies registered after Law 1.573's entry into force. Assess actual incorporation and registration dates; do not rewrite older companies' obligations from the current rule alone. [Arts. 35-1–35-3](https://legimonaco.mc/code/code-commerce/).

SAM constitution needs administrative authorisation under article 11. Article 12 allows private deed or notarial deed. Do not repeat the old universal-notary or half-capital rule. In-kind contributions and special advantages need the separate article 18 procedure. Capital is not a formation fee and is not evidence of permission to trade. [Arts. 11–18](https://legimonaco.mc/tnc/loi/2025/04-08-1.573).

## Permissions and filing sequence

Determine activity, legal form, nationality of associates/managers and any regulated profession first. Law 1.144 distinguishes declarations for specified Monegasque persons/associates/managers from authorisation for foreign counterparts; specified regulated activities also require authorisation for Monegasque persons. Foreign branches/offices face their own authorisation rule. SAM approval is separate. Do not promise a universal approval time or start date. [Arts. 1–8](https://legimonaco.mc/tnc/loi/1991/07-26-1.144/); [Art. 11](https://legimonaco.mc/tnc/loi/2025/04-08-1.573).

Prepare the applicable permission dossier, constitutional documents, subscriptions, payment/valuation evidence and registry application. This is a working sequence, not a verified exhaustive filing list. Current application forms, beneficial-owner/registry filings, fees and practical acceptance have not been checked end to end.

## October 2026 reforms and unresolved accounts work

Read the consolidated Code together with Law 1.596 of 9 October 2026. Its article 93 generally applies from the day after publication; article 102 separately defers four specified provisions until implementing regulations set their date, no later than 31 December 2026. Articles 94–103 also address transitional cases. This Guide has not established the implementing instruments for those deferred provisions or a complete accounts/audit filing calendar. Do not state that every October amendment operates on the same date. [Arts. 93–103](https://legimonaco.mc/tnc/loi/2026/10-09-1.596/).

## Two capital illustrations

### Ordinary SARL cash capital

Assume a new post-reform SARL with EUR 30,000 all-cash subscribed capital and no special requirement. Minimum cash at constitution is EUR 15,000 and the remaining EUR 15,000 falls under the applicable eighteen-month rule, not a statement that 50% is a universal fraction. Code article 35-3.

```oa-check
name: SARL statutory minimum cash versus subscribed amount
inputs:
  subscribed: 30000
  minimum: 15000
steps:
  - initial_minimum: min(subscribed, minimum)
  - remaining: subscribed - initial_minimum
expected:
  initial_minimum: 15000
  remaining: 15000
```

### SAM aggregate floor overrides one quarter

Assume EUR 300,000 all-cash SAM capital, equal cash payment proportions for every shareholder and no special requirement. One quarter would be EUR 75,000, below the EUR 150,000 minimum. At least EUR 150,000 must therefore be paid overall, while each subscriber's quarter test is independently satisfied. EUR 150,000 remains due under article 16.

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

## Ask before choosing the route

- What activity, form, associates/managers, nationality and regulated status are intended?
- Is the sole member a natural person, and what cash/in-kind capital is proposed?
- What constitution/registration dates and existing permissions apply?
- What premises, beneficial ownership, audit and accounts requirements arise?

## Sources

| Official source and provisions read | URL | Read on |
|---|---|---|
| Code de commerce, arts. 35-1–35-3 and transition note | https://legimonaco.mc/code/code-commerce/ | 2026-10-24 |
| Law 1.573, arts. 11–18 and art. 101(7) | https://legimonaco.mc/tnc/loi/2025/04-08-1.573 | 2026-10-24 |
| Law 1.144, arts. 1–8 | https://legimonaco.mc/tnc/loi/1991/07-26-1.144/ | 2026-10-24 |
| Law 1.596, arts. 93–103 | https://legimonaco.mc/tnc/loi/2026/10-09-1.596/ | 2026-10-24 |

**Not yet confirmed:** complete registry/beneficial-owner procedures, fees, sanctions, account/audit thresholds and deferred October implementation. Obtain Monaco professional review before incorporation or filing.

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
