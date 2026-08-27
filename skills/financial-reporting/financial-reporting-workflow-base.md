---
name: financial-reporting-workflow-base
description: Foundation workflow base for financial-reporting (US GAAP and IFRS) content skills. Contains the universal runbook, the two-layer output contract (reference layer + executable computation layer), the journal-entry format, the dual-standard convention, the AUDIT FLASH POINT marker convention, conservative-default principle, the structured question form, and the universal self-checks. This skill provides workflow architecture only — it contains no standard-specific recognition or measurement content. It MUST be loaded alongside a topic content skill (e.g. us-gaap-asc606-revenue, ifrs15-revenue) that provides the actual recognition, measurement, presentation, and disclosure rules. This base is the foundation every financial-reporting content skill loads on top of.
version: 0.1
jurisdiction: GLOBAL
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
category: financial-reporting
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Financial Reporting Workflow Base

## Financial Reporting Workflow Base v0.1

## What this file is

**This file is the foundation workflow base that every financial-reporting content skill loads on top of.** It is the shared contract. It carries no recognition or measurement rules of its own — those live in the topic content skills (revenue, leases, debt vs. equity, business combinations), each issued in a US GAAP (ASC) edition and an IFRS edition.

A content skill is useless without this base, and this base computes nothing without a content skill. Load both.

**Currency.** Content skills state their own standard-effective-date currency. This base is standard-agnostic and does not expire.

**The preparer and the reviewer are the customers of this output.** These skills assume a qualified preparer (controller, financial accountant, audit associate) is applying the skill to a real transaction, and that a credentialed reviewer (CPA, ACCA, Chartered Accountant, or equivalent) reviews and signs the resulting working papers. The skill produces working papers, journal entries, and a reviewer brief — **not** filed financial statements and not audit evidence.

## Section 1 — The two-layer output contract

Every financial-reporting content skill is built in **two layers**. An agent invoking a skill produces both unless the user asks for only one.

### Layer A — Reference layer (the rules)

- **Layer A — Reference layer (the rules)** — A faithful, citation-anchored statement of the standard's recognition, measurement, presentation, and disclosure requirements for the topic, expressed as decision trees and rules an agent can reason over. The reference layer answers: "What does the standard require, and where is it written?" Every rule cites the governing paragraph (e.g. ASC 606-10-25-1, IFRS 15.31, IAS 32.16, ASC 842-10-15-3).  _(ASC 606-10-25-1, IFRS 15.31, IAS 32.16, ASC 842-10-15-3)_

### Layer B — Executable layer (the computation)

- **Layer B — Executable layer (the computation)** — A step-by-step procedure that takes a specific transaction's facts and produces: 1. The recognition/measurement conclusion (with the reference-layer rule that drives it). 2. The journal entries (see Section 3 format), at initial recognition and over the relevant subsequent periods. 3. The amounts that flow to the primary statements (B/S, P&L / OCI, cash flow classification). 4. The disclosure checklist triggered by the transaction. Layer B answers: "Given these facts, what do I book, and what do I disclose?" Rule: Layer B steps must reference the Layer A rule number they execute. No computation without a cited rule.

## Section 2 — The dual-standard convention

Each topic ships as two files: a US GAAP (ASC) edition and an IFRS edition. They are separate skills, never merged, because the citations and — frequently — the answers differ.

Each content skill MUST include a "Divergence from [the other framework]" section that flags, for the topic, where US GAAP and IFRS reach different recognition, measurement, presentation, or disclosure outcomes. This is the single most valuable section for a dual-reporter (e.g. a US subsidiary of an IFRS parent) and the section reviewers scrutinise most.

When a user's facts touch both frameworks (group reporting under one, statutory under the other), an agent loads both editions for the topic and runs Layer B twice, presenting the two answers side by side with the divergence called out.

## Section 3 — Journal entry format

- **Journal entry format template** — [Date / period]  — [Event description] — driving rule: [ASC/IFRS ref] Dr  <Account caption>                         <amount> Dr  <Account caption>                         <amount> Cr  <Account caption>                          <amount> Cr  <Account caption>                          <amount> (memo: how each amount was derived) Rules: - Debits must equal credits on every entry. State the check. - Every account caption must map to a primary-statement line (asset, liability, equity, revenue, expense, OCI). - Where an amount is a present value, an allocation, or an estimate, the memo line shows the inputs (rate, term, standalone selling prices, fair values) and which Layer A rule produced it. - Show the subsequent-measurement entries, not only day 1 — unwinding of discount, amortisation, remeasurement, reclassification.  _(Section 3 — Journal entry format)_

## Section 4 — AUDIT FLASH POINT convention

- **AUDIT FLASH POINT marker convention** — Mark every position that auditors, regulators (SEC, FRC, ESMA), or peer reviewers actively challenge with a bold marker: > **⚑ AUDIT FLASH POINT —** [the judgement at issue, why it is contested, what evidence supports the position taken, and the disclosure that defuses it.] These are not edge cases for completeness; they are the judgements a reviewer must personally own. An agent must surface every flash point a transaction triggers in the reviewer brief, never bury them. Typical flash-point families across topics: estimates and significant judgements, related-party and non-arm's-length terms, cut-off and period-end timing, principal-vs-agent and gross-vs-net, classification that changes a key metric (EBITDA, leverage, current ratio), and anything that moves an amount between P&L and OCI or between periods.  _(Section 4 — AUDIT FLASH POINT convention)_

## Section 5 — Conservative-default principle

- **Conservative-default principle** — When the facts are incomplete and a judgement could go either way, the skill takes the position that is harder to challenge and easier to unwind, states that it has done so, and lists the specific fact that would change the answer. It does not silently pick the favourable treatment. Aggressive positions require an affirmative, documented instruction and a named reviewer.  _(Section 5 — Conservative-default principle)_

## Section 6 — Structured intake (the question form)

- **Structured intake question form** — If the transaction facts needed to run Layer B are missing, the agent asks for them in a single structured block before computing — never piecemeal, never guessing. Group questions by the Layer A decision they unlock. Example shape: To apply [topic] under [standard] I need: 1. [Fact] — used in [step / rule ref] 2. [Fact] — used in [step / rule ref] ... If you don't have [fact], I will assume [conservative default] and flag it.  _(Section 6 — Structured intake (the question form))_

## Section 7 — Universal self-checks

- **Universal self-checks checklist** — Before delivering output, the agent verifies (the content skill adds topic-specific checks on top): - [ ] Both layers produced (reference rule cited for every Layer B step) - [ ] Every journal entry balances; debits = credits stated - [ ] Every account caption maps to a primary-statement line - [ ] Subsequent-measurement entries shown, not just day 1 - [ ] Every figure traces to a source input or a cited rule — no unsourced numbers - [ ] Standard edition matches the entity's reporting framework (ASC vs IFRS) - [ ] Divergence section checked where the entity is a dual-reporter - [ ] Every triggered AUDIT FLASH POINT surfaced in the reviewer brief - [ ] Conservative default applied and flagged wherever facts were incomplete - [ ] Disclosure checklist produced for the transaction - [ ] Effective-date / transition correct for the reporting period - [ ] Output marked with its verification tier; reviewer sign-off requested  _(Section 7 — Universal self-checks)_

## Section 8 — Output specification

- **Output specification order** — Deliver, in this order: 1. Conclusion — one paragraph: recognition/measurement outcome and the rule that drives it. 2. Reference-layer trace — the decision path through Layer A, with citations. 3. Journal entries — Section 3 format, day 1 + subsequent periods. 4. Statement impact — what hits B/S, P&L, OCI, cash flow; effect on key metrics. 5. Disclosure checklist — every disclosure the transaction triggers, with reference. 6. Reviewer brief — the judgements taken, every AUDIT FLASH POINT, conservative defaults applied, and the open questions the credentialed reviewer must personally clear before sign-off. 7. Divergence note — where the other framework would differ (if relevant).  _(Section 8 — Output specification)_

## Section 9 — Verification status and disclaimer

- **Verification status tiers and disclaimer** — Each content skill carries a quality tier. Research-verified means drafted from the authoritative standards and awaiting credentialed sign-off; Accountant-verified means a named, licensed practitioner has reviewed and signed off the section. These skills provide computational and interpretive guidance on accounting standards. They are not an audit, not an assurance engagement, and not a substitute for professional judgement. Recognition, measurement, and disclosure under US GAAP and IFRS frequently turn on entity-specific facts and significant judgement. Always have outputs reviewed and signed by a qualified accountant before they are reflected in financial statements relied upon by third parties.  _(Section 9 — Verification status and disclaimer)_

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
