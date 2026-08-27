---
name: cross-border-tax-router
description: Entry point for the OpenAccountants cross-border / international personal-tax skill library. ALWAYS load this skill first when a person's facts touch more than one country — e.g. a US citizen living abroad, a dual resident, someone moving countries, a non-dom, an expatriating citizen, a foreign trust or foreign company owner, or "how is this taxed in country A and country B". The router computes nothing. It (1) builds the person's residency / citizenship / domicile map, (2) identifies which country skills and which international topic skills the facts engage, (3) gates out corridors the library does not yet cover, (4) SEQUENCES the steps — in cross-border, the order of events changes the tax (sever residency before vs. after a sale), and (5) hands off to cross-border-tax-workflow-base plus the topic skills. Every international topic skill (FEIE/FTC, FBAR/FATCA, CFC/GILTI, foreign trusts, exit tax) assumes this routing step has happened first.
version: 0.1
jurisdiction: GLOBAL
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Cross Border Tax Router

## Cross-Border Tax Router v0.1

## What this file is

The **entry point** for the cross-border / international personal-tax skill library. Before any topic skill can run, three things must be settled: *who the person is to each tax system* (citizenship, residence, domicile), *which countries' rules engage*, and *in what order the events happen*. This skill settles all three, then loads the workflow base and the right topic skill(s).

**The user never sees this skill.** They describe a situation in plain language ("I'm a US citizen living in Australia with a trust to sell"); the router works silently and hands off.

The router **computes nothing** — no tax, no characterization, no return lines. Its only job is residency mapping, corridor identification, scope gating, sequencing, and handoff. If you find yourself computing a liability inside the router, stop: you have skipped the handoff.

**Why a router exists for cross-border at all.** Within one country the rules compose cleanly. Across borders they do not: the same dollar can be taxed by two systems, a treaty can re-allocate it, and *the sequence of events* (when you cease to be resident, when an asset is sold, when a distribution is made) routinely changes the answer by more than the rate does. A single-country answer to a multi-country question is wrong by construction. The router's job is to refuse to give one.

## Step 0: Build the residency / citizenship / domicile map

**Basis a country may tax on**

| Basis a country may tax on | Typical triggers | Example countries |
| --- | --- | --- |
| **Citizenship** (worldwide, regardless of residence) | holding the passport | **United States** (and Eritrea) |
| **Tax residence** (worldwide while resident) | days present, permanent home, centre of vital interests | most of the world |
| **Domicile / remittance** | domicile of origin/choice; income/gains remitted vs. kept offshore | UK (to 2025), Malta, Ireland, Cyprus |
| **Source** (that country's income only) | income arising there, real estate there, a PE there | every country, for non-residents |

- ****Citizenship** (worldwide, regardless of residence)** — holding the passport  _(**United States** (and Eritrea))_
- ****Tax residence** (worldwide while resident)** — days present, permanent home, centre of vital interests  _(most of the world)_
- ****Domicile / remittance**** — domicile of origin/choice; income/gains remitted vs. kept offshore  _(UK (to 2025), Malta, Ireland, Cyprus)_
- ****Source** (that country's income only)** — income arising there, real estate there, a PE there  _(every country, for non-residents)_

Capture, in one structured block:

```
Cross-border map — I need, for each country in play:
  1. Citizenship(s) held — used for citizenship-based taxation (US) and exit-tax tests
  2. Tax residence(s) now, and any change of residence in play (dates) — used for the residence test
  3. Domicile (if a remittance-basis country is involved) — used for the remittance basis
  4. The asset(s) / income / event in question, and WHEN each happens — used for sequencing
  5. Any foreign entities owned (companies, trusts, partnerships, pensions) — used for the anti-deferral and reporting skills
If you don't have one of these, I will assume the position that creates the BROADER
taxing right and the reporting obligation (workflow base §5) and flag it.
```

Do not proceed past Step 0 until citizenship, current residence(s), and the event in question are known. These three settle which country skills load.

## Step 1: Identify the corridors and topics the facts engage

**Signal in the facts / International topic skill**

| Signal in the facts | International topic skill |
| --- | --- |
| US citizen / green-card holder living or working abroad; foreign salary; foreign taxes paid | `us-feie-ftc` |
| US person with foreign bank / brokerage / pension accounts | `us-fbar-fatca-reporting` |
| US person owning ≥10% of a foreign company; foreign corp with US owners | `us-cfc-gilti` |
| US person who is a grantor, owner, or beneficiary of a **foreign trust**; gifts/inheritances from non-US persons | `us-foreign-trust-reporting` |
| US citizen / long-term green-card holder **giving up** US status | `us-expatriation-exit-tax` |
| A position that relies on a tax treaty (residence tie-breaker, reduced withholding, re-sourcing) | `us-treaty-positions-basics` |

- **US citizen / green-card holder living or working abroad; foreign salary; foreign taxes paid** — `us-feie-ftc`
- **US person with foreign bank / brokerage / pension accounts** — `us-fbar-fatca-reporting`
- **US person owning ≥10% of a foreign company; foreign corp with US owners** — `us-cfc-gilti`
- **US person who is a grantor, owner, or beneficiary of a **foreign trust**; gifts/inheritances from non-US persons** — `us-foreign-trust-reporting`
- **US citizen / long-term green-card holder **giving up** US status** — `us-expatriation-exit-tax`
- **A position that relies on a tax treaty (residence tie-breaker, reduced withholding, re-sourcing)** — `us-treaty-positions-basics`

Then identify the **country skills** for each jurisdiction in the map (e.g. the US, Malta, Australia personal-income / CGT skills), loaded via the normal single-country flow. The router's value-add is binding the topic skills *to* the country skills in the right order.

If the facts match a topic, route to it (Step 4). If a needed corridor is missing, go to Step 2.

## Step 2: Scope gate — what this library does NOT cover yet

The international library currently covers the **US-outbound / US-person spine**. Many cross-border situations sit just outside it. Be honest: route to the closest skill for the part that is covered, and explicitly name the country rule or treaty the user still needs a human for.

**If the person actually needs... / Not yet covered — what to say**

| If the person actually needs... | Not yet covered — what to say |
| --- | --- |
| The **other country's** domestic treatment of the same event (e.g. Australian CGT on the trust, Maltese remittance treatment) | Load that country's own skill if it exists; if not, name it as an open item for a local accountant. The international topic skills cover the **US** side only. |
| A **specific treaty article** read in full (US–AU, US–MT, etc.) | `us-treaty-positions-basics` covers the *mechanics* of taking a treaty position (Form 8833, tie-breaker, saving clause) — not a clause-by-clause read of a named treaty. Flag the specific article for human review. |
| **State** tax residency / sourcing (e.g. California "safe-harbour", domicile) | Covered by the relevant US-state skill, not here. Flag if a high-tax state is in play. |
| **PFIC** (passive foreign investment companies — foreign funds/ETFs) | Not yet covered. Name it: foreign mutual funds/ETFs are almost always PFICs (Form 8621) and need a specialist. |
| **Social-security / totalization**, foreign pension characterization | Not yet covered. Flag. |
| **Estate / gift / inheritance** across borders | Not covered. Flag — situs and treaty rules differ sharply from income tax. |
| **Non-US** anti-deferral regimes (UK, EU CFC; ATAD) | Not covered. The CFC/GILTI skill is US-side only. |

- **The **other country's** domestic treatment of the same event (e.g. Australian CGT on the trust, Maltese remittance treatment)** — Load that country's own skill if it exists; if not, name it as an open item for a local accountant. The international topic skills cover the **US** side only.
- **A **specific treaty article** read in full (US–AU, US–MT, etc.)** — `us-treaty-positions-basics` covers the *mechanics* of taking a treaty position (Form 8833, tie-breaker, saving clause) — not a clause-by-clause read of a named treaty. Flag the specific article for human review.
- ****State** tax residency / sourcing (e.g. California "safe-harbour", domicile)** — Covered by the relevant US-state skill, not here. Flag if a high-tax state is in play.
- ****PFIC** (passive foreign investment companies — foreign funds/ETFs)** — Not yet covered. Name it: foreign mutual funds/ETFs are almost always PFICs (Form 8621) and need a specialist.
- ****Social-security / totalization**, foreign pension characterization** — Not yet covered. Flag.
- ****Estate / gift / inheritance** across borders** — Not covered. Flag — situs and treaty rules differ sharply from income tax.
- ****Non-US** anti-deferral regimes (UK, EU CFC; ATAD)** — Not covered. The CFC/GILTI skill is US-side only.

### Out-of-scope message template

> "I can work the US side of this under [topic skill], but [the other country's treatment / the specific treaty article / PFIC / estate] isn't in the library yet and turns on facts I shouldn't guess across a border. I'd flag that to a local accountant rather than improvise. Want me to handle the US side and mark the rest as open items for sign-off?"

Never fabricate another country's treatment or a treaty outcome. Conservative-default (workflow base §5) governs *missing facts within a covered topic* — it is not licence to invent an uncovered country's rule.

## Step 3: Sequence — order of events changes the tax

This is the heart of cross-border and the thing single-country tools cannot do. When two or more steps apply, run them in the order the **events** occur and the **taxing rights** attach — later steps depend on earlier ones.

**Combined fact pattern / Order / Why**

| Combined fact pattern | Order | Why |
| --- | --- | --- |
| **Changing tax residence** *and* **selling an asset** | Settle the residency-cessation date **first**, then test the sale against each country's rule as of that date | Whether a country can tax the gain usually turns on residence **at the moment of disposal** (and some countries impose a deemed-disposal exit charge on departure). Selling before vs. after cessation can change which systems tax the gain. |
| **US citizen** *and* anything | The US taxing right is **always on** (citizenship basis) — apply the US topic skill to every item, then use FTC/treaty to relieve double tax | A non-US "I'm not resident there" analysis never removes the US right; it only changes relief. |
| **Foreign trust** distribution / sale | Characterize the trust (grantor vs. non-grantor) **first**, then the distribution / disposition | Who is taxed on the trust's income, and how throwback applies, depends on the grantor analysis done first. |
| **Expatriation** in play | Run the covered-expatriate / exit-tax test **before** planning any post-exit disposal | The mark-to-market exit charge and the date of expatriation reset basis and timing for everything after. |
| **CFC / GILTI** plus a later distribution | Inclusion **first** (Subpart F / GILTI at the shareholder), then the distribution (previously-taxed income) | Avoids double-counting income already included. |

- ****Changing tax residence** *and* **selling an asset**** — Settle the residency-cessation date **first**, then test the sale against each country's rule as of that date  _(Whether a country can tax the gain usually turns on residence **at the moment of disposal** (and some countries impose a deemed-disposal exit charge on departure). Selling before vs. after cessation can change which systems tax the gain.)_
- ****US citizen** *and* anything** — The US taxing right is **always on** (citizenship basis) — apply the US topic skill to every item, then use FTC/treaty to relieve double tax  _(A non-US "I'm not resident there" analysis never removes the US right; it only changes relief.)_
- ****Foreign trust** distribution / sale** — Characterize the trust (grantor vs. non-grantor) **first**, then the distribution / disposition  _(Who is taxed on the trust's income, and how throwback applies, depends on the grantor analysis done first.)_
- ****Expatriation** in play** — Run the covered-expatriate / exit-tax test **before** planning any post-exit disposal  _(The mark-to-market exit charge and the date of expatriation reset basis and timing for everything after.)_
- ****CFC / GILTI** plus a later distribution** — Inclusion **first** (Subpart F / GILTI at the shareholder), then the distribution (previously-taxed income)  _(Avoids double-counting income already included.)_

State the sequence to the user before computing:

> "The order matters here. I'll fix [the residency-cessation date] first because [the gain's taxability turns on residence at disposal], then apply [country A] and [country B] to the sale as of that date, then [relief]."

## Step 4: Handoff

0. **Load workflow base** — Always load, in this order: 1. cross-border-tax-workflow-base
0. **Load workflow base — the shared contract** — `cross-border-tax-workflow-base` — the shared contract (residency intake, the conservative cross-border default, flash points, the mandatory human hand-off, self-checks).
0. **Load international topic skill(s) identified in Step 1** — The international topic skill(s) identified in Step 1.
0. **Load country skill(s) for each jurisdiction in map** — The country skill(s) for each jurisdiction in the map, via the normal single-country flow, applied in the order fixed in Step 3.

Then tell the user, in one line, what you loaded and what you'll produce:

> "Loaded the cross-border workflow base + [topic skills] + the [country] skills. I'll produce a sequenced plan: the order of steps, each country's treatment at each step, the treaty bridge for double-tax relief, the US reporting forms triggered, and a hand-off to the named accountant for the lead country. I'll ask for any missing facts first."

Hand control to the workflow base's structured intake — do not start computing inside the router.

## Router self-checks

Before handing off, confirm:

- [ ] Residency / citizenship / domicile captured for **every** country in play
- [ ] Every taxing basis identified (citizenship for US; residence; domicile/remittance; source)
- [ ] Every international topic the facts touch identified — including reporting (FBAR/FATCA) the user didn't ask about
- [ ] Anything uncovered (other country's rule, named treaty article, PFIC, estate) named honestly, not improvised
- [ ] The sequence of events fixed, and stated to the user, **before** any computation
- [ ] Workflow base loaded alongside the topic skill(s) — never a topic skill alone

## PROHIBITIONS

- **Never compute or characterize tax inside the router** — NEVER compute or characterize tax inside the router — route and hand off.
- **Never load a topic skill without workflow base** — NEVER load an international topic skill without also loading `cross-border-tax-workflow-base`.
- **Never answer multi-country as if silo'd** — NEVER answer a multi-country question one country at a time as if the others didn't exist — that is the silo the router exists to prevent.
- **Never assume non-US analysis removes US taxing right** — NEVER assume a non-US analysis removes the US citizenship-based taxing right — it only changes relief.
- **Never fabricate another country's rule or treaty outcome** — NEVER fabricate another country's domestic rule or a treaty outcome — name it and flag it for a local accountant.
- **Never plan disposal before fixing residency-cessation/expatriation dates** — NEVER plan a disposal before fixing the residency-cessation date and (where relevant) the expatriation test.

## Disclaimer

This skill routes between cross-border tax-guidance skills. It does not constitute tax, legal, or financial advice, is not an engagement, and does not produce a filed return. Cross-border outcomes turn on entity- and treaty-specific facts and significant judgement, and the order of events frequently changes the result. All outputs of the skills this router loads are **research-grade until a licensed accountant in the relevant country reviews and signs them off**, and the workflow must end by handing the working paper to that accountant.

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
