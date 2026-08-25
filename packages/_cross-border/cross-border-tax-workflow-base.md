---
name: cross-border-tax-workflow-base
description: Foundation workflow base for cross-border / international personal-tax content skills. Contains the residency-map intake, the sequenced-plan output contract (a cross-border answer is an ORDERED set of steps, not N separate answers), the cross-border conservative-default principle, the AUDIT FLASH POINT marker convention, the double-tax-relief / treaty-bridge convention, and the mandatory human hand-off. This skill provides workflow architecture only — it contains no country-specific or topic-specific rules. It MUST be loaded alongside a topic content skill (e.g. us-feie-ftc, us-foreign-trust-reporting) and the relevant country skills. This base is the foundation every international content skill loads on top of.
version: 0.1
jurisdiction: GLOBAL
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Cross Border Tax Workflow Base

## Cross-Border Tax Workflow Base v0.1

## What this file is

**This file is the foundation workflow base that every cross-border / international
content skill loads on top of.** It is the shared contract. It carries no country
rules and no topic rules of its own — those live in the topic content skills
(FEIE/FTC, FBAR/FATCA, CFC/GILTI, foreign trusts, exit tax) and in each country's
own skills.

A content skill is useless without this base, and this base computes nothing
without content skills. Load both, plus the country skills the router identified.

**Currency.** Content skills state their own tax-year currency. This base is
year-agnostic and does not expire.

**This output is a working paper handed to a licensed accountant — never a filed
return.** Cross-border situations carry the highest penalty exposure in tax
(FBAR, 3520, 8938, exit tax), and the order of events is often irreversible once
executed. The skill produces a sequenced plan, a working paper, and a reviewer
brief — and it ends by handing that working paper to the named accountant for the
lead country **before** the person acts.

## Section 1 — The sequenced-plan output contract

A cross-border answer is **not** a stack of single-country answers. It is an
**ordered plan**. Every cross-border content skill produces both layers below.

### Layer A — Reference layer (the rules)

- **Layer A — Reference layer (the rules)** — For each country and topic engaged, a faithful, citation-anchored statement of the rule (statute / form / treaty article), expressed as decision trees an agent can reason over. Answers: "What does each system require, and where is it written?" Every rule cites its source (e.g. IRC §911, §877A, Form 3520, the relevant treaty article).  _(IRC §911; §877A; Form 3520)_

### Layer B — Executable layer (the sequenced plan)

- **Layer B — Executable layer (the sequenced plan)** — A step-by-step procedure that takes the person's facts and the order of events fixed by the router, and produces an ordered list of steps. Each step states: 1. What happens (the event, and when). 2. Which country taxes it, on what basis (citizenship / residence / domicile / source), citing the Layer A rule. 3. How double tax is relieved at that step — the treaty bridge (FTC, exemption, re-sourcing, tie-breaker), citing the article/section. 4. Which forms / filings the step triggers in each country (with deadlines). 5. Why this step is ordered where it is — what breaks if it moves. Layer B answers: "Given these facts and this order, who taxes what, in what sequence, and what gets filed?" **Rule:** every Layer B step must reference the Layer A rule it executes. No position without a cited source — and no treaty benefit asserted without the article and the filing that claims it.  _(Layer B rule statement)_

## Section 2 — The double-tax-relief / treaty-bridge convention

The single most valuable part of a cross-border answer is the bridge: how the two (or more) systems' taxing rights are reconciled so the same income is not taxed twice without relief. For every item that more than one country taxes, the skill MUST state, explicitly:

- Which country has the primary taxing right and which gives relief.
- The mechanism — foreign tax credit (§901/§904), exemption/exclusion (§911), treaty re-sourcing, residence tie-breaker, or a reduced treaty withholding rate.
- The filing that actually claims it (e.g. Form 1116, Form 2555, Form 8833) — a relief that is not claimed on the right form is not relief.
- The residual double tax, if any, that the mechanism does not eliminate (e.g. rate differentials, the US saving clause, state tax that ignores the treaty).

- **The saving clause caveat** — Most US treaties contain a saving clause that lets the US tax its citizens/residents as if the treaty did not exist, subject to listed exceptions. Never assert a treaty benefit for a US person without checking the saving clause and its exceptions first.  _(US treaty saving clause)_

## Section 3 — AUDIT FLASH POINT convention

Mark every position that tax authorities (IRS, HMRC, ATO, etc.) actively challenge with a bold marker:

> **⚑ AUDIT FLASH POINT —** [the judgement at issue, why it is contested, what evidence supports the position taken, and the filing/disclosure that defuses it.]

These are the positions a reviewer must personally own. Surface every flash point a situation triggers in the reviewer brief — never bury them.

Typical cross-border flash-point families: residency-cessation date and day-count evidence; treaty-residence tie-breakers; grantor-vs-non-grantor trust characterization; FEIE-vs-FTC elections and the §911(d)(1) tax-home/bona-fide test; covered-expatriate status and exit-tax valuations; PFIC exposure inside foreign funds; reasonable-cause positions for late FBAR/3520/8938; and any position that depends on facts in another country the preparer cannot verify.

## Section 4 — Conservative-default principle (cross-border edition)

When facts are incomplete and a position could go either way across a border, the skill takes the position that is harder to challenge and creates the reporting trail, states it has done so, and lists the specific fact that would change the answer. Concretely, when unsure:

- Assume the broader taxing right applies (e.g. assume US residence/citizenship taxation reaches the item) rather than the narrower one.
- Assume the reporting obligation is triggered (file the FBAR / 8938 / 3520) rather than assuming an exemption — the cost of an unnecessary information return is near zero; the cost of a missed one is penalties measured in tens of thousands.
- Assume the higher-tax characterization of an entity or instrument until a fact establishes otherwise.

It does not silently pick the favourable treatment. Aggressive positions (e.g. a treaty position that overrides the saving clause, a non-filing position) require an affirmative, documented instruction and a named accountant's sign-off — they are never the default.

## Section 5 — Structured intake (the residency map)

If facts needed to run Layer B are missing, ask for them in a single structured block before computing — never piecemeal, never guessing. The router's Step 0 map is the intake; restate any gaps here grouped by the decision they unlock:

```
To sequence this I still need:
  1. [Fact] — used in [step / rule ref]
  2. [Fact] — used in [step / rule ref]
  ...
If you don't have [fact], I will assume [the broader taxing right / the reporting
obligation applies] (§4) and flag it for your accountant.
```

## Section 6 — Universal self-checks

Before delivering output, the agent verifies (each content skill adds topic-specific checks on top):

- [ ] Both layers produced (a cited rule for every step)
- [ ] The answer is an ordered plan, not N independent country answers
- [ ] Order of events stated and justified (what breaks if a step moves)
- [ ] For every item taxed by >1 country, the treaty bridge is stated with the relieving mechanism and the form that claims it
- [ ] Saving clause checked before asserting any treaty benefit for a US person
- [ ] Every US information-reporting form the facts trigger is listed (FBAR, 8938, 3520/3520-A, 5471/8865, 8621) — not just the income forms
- [ ] Every figure traces to a source input or a cited rule — no unsourced numbers
- [ ] Every triggered AUDIT FLASH POINT surfaced in the reviewer brief
- [ ] Conservative default applied and flagged wherever facts were incomplete
- [ ] Any uncovered country rule / named-treaty read / PFIC / estate item flagged as an open item, not improvised
- [ ] Output marked tier 2 (research-verified); the human hand-off (§8) is executed

## Section 7 — Output specification

Deliver, in this order:

1. Situation map — citizenship / residence(s) / domicile and the event, one block.
2. The sequenced plan — the ordered Layer B steps (event → who taxes → relief → filings → why ordered here).
3. Reference-layer trace — the rule / form / treaty article behind each step.
4. Double-tax bridge summary — per item: primary right, relief mechanism, claiming form, residual.
5. US reporting-forms checklist — every information return triggered, with deadlines and penalties.
6. Reviewer brief — the judgements taken, every AUDIT FLASH POINT, conservative defaults applied, and the open items the licensed accountant must personally clear.
7. Hand-off — per Section 8.

## Section 8 — Verification tier and the mandatory hand-off

Every cross-border output carries the tier 2 (research-verified) mark: drafted from authoritative statutes, forms, and treaties, and awaiting a named, licensed accountant's sign-off. No cross-border skill output is ever presented as accountant-verified on its own, because no human has yet signed the specific plan.

**The workflow MUST end by handing the working paper to a human.** Before the person executes any irreversible step (selling, distributing, ceasing residence, expatriating, filing), call `request_accountant_review` with:

- `jurisdiction` = the lead country (the one with the primary taxing right or the largest exposure — usually where the person is, or will be, resident, or the US where citizenship taxation dominates),
- `scenario` = the situation map, and
- `working_paper` = the full sequenced plan above.

The tool routes the plan to the lead verifier for that country so the accountant sees the numbers before the call. Tell the user, plainly: this is a working paper, not advice you can act on yet; a licensed accountant in [lead country] will review it and is the one who signs off and (if engaged) files.

0. **Mandatory hand-off to accountant review** — Call request_accountant_review with jurisdiction, scenario, and working_paper before the person executes any irreversible step.

## Section 9 — Disclaimer

These skills provide computational and interpretive guidance on cross-border personal taxation. They are not tax or legal advice, not an engagement, and not a filed return. Cross-border outcomes turn on entity-, residence-, and treaty-specific facts and significant judgement, and the order of events frequently changes the result. Always have outputs reviewed and signed by a qualified, licensed accountant in each relevant country before acting on them. Penalty exposure on cross-border information returns is severe; when in doubt, file and ask.

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
