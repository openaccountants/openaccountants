---
name: financial-reporting-router
description: Entry point for the OpenAccountants financial-reporting (US GAAP / IFRS) skill library. ALWAYS load this skill first when a user asks how to account for, recognise, measure, classify, or disclose a transaction under US GAAP or IFRS — e.g. "how do I book this contract", "is this a lease", "debt or equity", "how do I account for this acquisition", "revenue recognition for...", "what's the journal entry for...". The router does not compute anything. It (1) establishes the entity's reporting framework, (2) identifies which accounting standard(s) the transaction touches, (3) gates out transactions whose governing standard the library does not yet cover, (4) sequences the topic skills when more than one applies, and (5) hands off to the financial-reporting-workflow-base plus the correct topic content skill(s). Every topic skill (revenue, leases, debt vs. equity, business combinations) assumes this routing step has happened first.
version: 0.1
jurisdiction: GLOBAL
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
category: financial-reporting
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Financial Reporting Router

## What this file is

The **entry point** for the financial-reporting skill library. Before any topic skill can run, two things must be settled: *which framework* the entity reports under, and *which standard(s)* the transaction engages. This skill settles both, then loads the workflow base and the right topic skill(s).

**The user never sees this skill.** They describe a transaction in plain language; the router works silently and hands off.

The router **computes nothing** — no recognition, no measurement, no journal entries. Its only job is framework detection, standard identification, scope gating, sequencing, and handoff. If you find yourself booking an entry inside the router, stop: you have skipped the handoff.

## Step 0: Establish the reporting framework

**Reporting framework signals**  _(Step 0: Establish the reporting framework)_

| Signal | Example | Framework |
| --- | --- | --- |
| Explicit statement | "we report under IFRS", "US GAAP filer" | as stated |
| SEC registrant / US domestic filer | "10-K", "Form S-1", "SEC" | US GAAP |
| Local-GAAP-on-IFRS jurisdiction | EU-listed, UK, Australia, most of Asia/Africa | IFRS |
| US private company | "GAAP", "ASC", "FASB", US-based, no IFRS mention | US GAAP |
| Parent / subsidiary mismatch | "US sub of a German group", "we file local + group" | **Dual reporter — both** |

### Dual reporters

- **Dual reporter handling** — If the entity prepares one set of statements under US GAAP and another under IFRS (e.g. a US subsidiary consolidated into an IFRS group, or an IFRS company with a US-GAAP-reporting segment), load both editions of every applicable topic skill and run the computation under each, presenting the answers side by side with the topic skill's Divergence section called out. Flag this to the user explicitly — the divergence is usually the whole reason they asked.  _(Dual reporters)_

### If the framework is unclear

Ask ONE question and do not proceed until answered:

> "Which framework do these statements report under — US GAAP, IFRS, or both (e.g. a local statutory set plus a group-reporting set)? It changes the citations and sometimes the answer."

## Step 1: Identify the standard(s) the transaction touches

**Fact pattern to topic mapping**  _(Step 1: Identify the standard(s) the transaction touches)_

| Signal in the fact pattern | Topic | Skill (US GAAP / IFRS) |
| --- | --- | --- |
| Sale of goods/services, contract with a customer, performance obligations, variable consideration, licences, bundled deliverables, "when do we recognise revenue" | **Revenue** | `us-gaap-asc606-revenue` / `ifrs15-revenue` |
| Right to use an asset for a period, rent, hire, charter, embedded lease, lessor/lessee, sale-and-leaseback | **Leases** | `us-gaap-asc842-leases` / `ifrs16-leases` |
| Instrument that could be a liability or equity — preferred shares, redeemable instruments, warrants, convertible notes, "is this debt or equity", puttable instruments | **Debt vs. equity** | `us-gaap-debt-vs-equity` / `ias32-debt-vs-equity` |
| One entity obtains control of a business — acquisition, merger, purchase-price allocation, goodwill on acquisition, bargain purchase, contingent consideration | **Business combinations** | `us-gaap-asc805-business-combinations` / `ifrs3-business-combinations` |

- **Routing decision** — If the fact pattern matches a topic, route to it (Step 4). If it matches none, go to Step 2.  _(Step 1: Identify the standard(s) the transaction touches)_

## Step 2: Scope gate — what this library does NOT cover yet

**Uncovered standards table**  _(Step 2: Scope gate — what this library does NOT cover yet)_

| If the user actually needs... | Governing standard (not yet covered) | What to say |
| --- | --- | --- |
| Goodwill / asset **impairment** testing | ASC 350 / ASC 360 ; IAS 36 | Business-combinations skill covers *initial* goodwill; impairment is a separate standard not yet in the library. |
| **Income tax** accounting, deferred tax | ASC 740 ; IAS 12 | Not covered. Deferred tax often *interacts* with every topic — flag it. |
| **Financial instruments** measurement / impairment (ECL), hedging | ASC 326 / ASC 815 ; IFRS 9 | Debt-vs-equity covers *classification* of the issuer's instrument only — not measurement, impairment, or hedge accounting. |
| **Share-based payment** | ASC 718 ; IFRS 2 | Not covered. |
| **Inventory**, PP&E, intangibles (standalone) | ASC 330/360/350 ; IAS 2/16/38 | Not covered except where acquired in a business combination. |
| **Provisions**, contingencies | ASC 450 ; IAS 37 | Not covered. |
| **Consolidation**, equity method, JVs | ASC 810/323 ; IFRS 10/11, IAS 28 | Business-combinations covers the acquisition accounting, not ongoing consolidation mechanics. |
| **Foreign currency** translation | ASC 830 ; IAS 21 | Not covered. |
| **Statement presentation**, cash-flow classification as a primary question | ASC 205/230 ; IAS 1/7 | Topic skills state where amounts land, but full statement presentation is not a standalone skill. |

### Out-of-scope message template

> "I can compute the part of this that falls under [covered topic], but the core of your question is governed by [standard], which isn't in the financial-reporting library yet. I'd flag that to your reviewer rather than guess. Want me to handle the [covered part] and mark the [uncovered part] as an open item for sign-off?"

Never fabricate a treatment for an uncovered standard. Conservative-default (workflow base §5) applies to *missing facts within a covered topic* — it is not licence to improvise an uncovered standard.

## Step 3: Sequence when multiple topics apply

**Combined fact pattern sequencing**  _(Step 3: Sequence when multiple topics apply)_

| Combined fact pattern | Order | Why |
| --- | --- | --- |
| **Business combination** that includes contracts/leases/instruments | **Business combination first**, then revenue / leases / debt-vs-equity on the acquired items | Acquired assets and liabilities are first measured at fair value at the acquisition date (ASC 805 / IFRS 3); the topic skills then apply *prospectively* from that fair-value baseline. |
| **Sale-and-leaseback** | **Revenue first** (is the transfer a sale under ASC 606 / IFRS 15?), then **leases** | Whether a sale occurred determines whether leaseback or financing accounting applies. |
| **Convertible / hybrid instrument** issued to fund or settle a contract | **Debt vs. equity first** (classify the instrument), then revenue/leases on the underlying deal | Classification of the instrument is independent of, and precedes, the customer/lease accounting. |
| Any combination with a **divergence-sensitive** dual reporter | Run the sequence under each framework separately | Ordering can differ in effect even when steps are the same. |

State the sequence to the user before computing:

> "This touches [topic A] and [topic B]. I'll do [A] first because [reason], then [B] using A's output as the starting point."

## Step 4: Handoff

0. **Load workflow base** — financial-reporting-workflow-base — the shared contract (output format, journal-entry format, flash points, self-checks).
0. **Load topic skill(s) identified in Step 1, in edition fixed by Step 0** — US GAAP filer → the us-gaap-* edition; IFRS filer → the ifrs*/ias* edition; Dual reporter → both editions.
0. **Load and run sequenced multi-topic skills** — Where Step 3 sequenced multiple topics, load them all and run in the stated order.

Then tell the user, in one line, what you loaded and what you'll produce:

> "Loaded the workflow base + [topic skill(s), edition]. I'll produce the conclusion, journal entries (day 1 + subsequent), statement impact, disclosure checklist, and a reviewer brief. I'll ask for any missing facts first."

Hand control to the workflow base's structured intake (§6) — do not start asking for facts inside the router.

## Router self-checks

Before handing off, confirm:

- [ ] Reporting framework established (or the one clarifying question asked)
- [ ] Every standard the fact pattern touches identified — including the *adjacent* ones in Step 2
- [ ] Anything uncovered named honestly, not improvised
- [ ] Multi-topic transactions sequenced, with the order stated to the user
- [ ] Correct edition(s) selected for the framework (both, for dual reporters)
- [ ] Workflow base loaded alongside the topic skill(s) — never a topic skill alone

## PROHIBITIONS

- **Prohibition list** — NEVER compute, classify, or book an entry inside the router — route and hand off. NEVER load a topic skill without also loading financial-reporting-workflow-base. NEVER guess the reporting framework — ask if unclear. NEVER fabricate a treatment for a standard the library does not cover — name it and flag it. NEVER pick a single edition for a dual reporter — load both and show the divergence. NEVER run multi-topic transactions out of order — business combination before the topics on acquired items; revenue (sale test) before leaseback.  _(PROHIBITIONS)_

## Disclaimer

This skill routes between computational guidance skills for US GAAP and IFRS. It does not constitute accounting, audit, or financial advice, is not an assurance engagement, and does not produce filed financial statements. Recognition, measurement, and disclosure frequently turn on entity-specific facts and significant judgement. All outputs of the skills this router loads must be reviewed and signed off by a qualified accountant (CPA, ACCA, Chartered Accountant, or equivalent) before they are reflected in financial statements relied upon by third parties.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com).

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
