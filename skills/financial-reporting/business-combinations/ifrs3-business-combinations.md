---
name: ifrs3-business-combinations
description: IFRS accounting for business combinations under IFRS 3 (Business Combinations) and the related goodwill impairment guidance in IAS 36 (Impairment of Assets). Covers the acquisition method — identify the acquirer, determine the acquisition date, recognise and measure the identifiable assets acquired, liabilities assumed and any non-controlling interest, and recognise goodwill or a bargain purchase gain — plus consideration transferred and contingent consideration, acquisition-related costs, the measurement period, step acquisitions, recognition exceptions, the definition of a business and the optional concentration test, in-process R&D, and subsequent goodwill impairment testing at the cash-generating-unit level under IAS 36. Produces recognition conclusions, journal entries, and a reviewer brief. Issued as the IFRS edition of the business-combinations topic; see us-gaap-asc805-business-combinations for the US GAAP edition. MUST load alongside financial-reporting-workflow-base.
version: 0.1
jurisdiction: GLOBAL
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on: - financial-reporting-workflow-base
category: financial-reporting
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Ifrs3 Business Combinations

## IFRS Business Combinations — IFRS 3 v0.1

IFRS Business Combinations — IFRS 3 v0.1

## What this file is

**This is a content skill that loads on top of `financial-reporting-workflow-base`.** It supplies the recognition, measurement, presentation, and disclosure rules for business combinations under IFRS, and the subsequent impairment testing of goodwill under IAS 36. The base supplies the two-layer output contract, the journal-entry format, and the self-checks.

- **Standard currency** — IFRS 3 (revised 2008) as currently effective, including *Definition of a Business* (Amendments to IFRS 3, effective for combinations on or after 1 January 2020) which added the optional concentration test, and the *Reference to the Conceptual Framework* amendments (effective 1 January 2022). Control is assessed under IFRS 10 (effective 1 January 2013). Confirm no entity-specific exemption applies.  _(IFRS 3 (revised 2008); IFRS 10 (2013))_
- **Scope** — IFRS 3 applies to a transaction or other event in which an acquirer obtains control of one or more businesses. It does not apply to: the formation of a joint arrangement in the financial statements of the joint arrangement itself; the acquisition of an asset or group of assets that is not a business (allocate cost, no goodwill); and combinations of entities or businesses under common control.  _(IFRS 3.1–.3, IFRS 3.2(a), IFRS 3.2(b), IFRS 3.2(c), B1–B4)_

## Section 1 — Scope statement

This skill covers:

- The acquisition method of IFRS 3 — the four steps (`IFRS 3.4`–`.5`).
- Consideration transferred at fair value, including contingent consideration and its subsequent measurement.
- Acquisition-related (transaction) costs.
- The recognition and measurement **exceptions** to the fair-value principle.
- The **per-transaction NCI measurement choice** (full vs. partial goodwill).
- The measurement period and retrospective measurement-period adjustments.
- Step (combination achieved in stages) acquisitions and the remeasurement of a previously held equity interest.
- Bargain purchases.
- The definition of a business and the optional **concentration test** (asset vs. business).
- In-process research and development (IPR&D).
- Subsequent impairment of goodwill at the **cash-generating-unit (CGU)** level under IAS 36.

This skill does NOT cover: asset acquisitions outside IFRS 3, common-control combinations (no IFRS standard; an accounting-policy choice), the consolidation procedures and the control assessment themselves (`IFRS 10`), or joint arrangements (`IFRS 11`). It defers the US GAAP treatment to `us-gaap-asc805-business-combinations`.

## Section 2 — Reference layer (Layer A): the acquisition method

- **Acquisition method** — Every business combination in scope is accounted for by applying the acquisition method. The method has four steps.  _(IFRS 3.4–.5, IFRS 3.5)_

### Step 1 — Identify the acquirer — `IFRS 3.6`–`.7`, `B13`–`B18`

- **Identify the acquirer** — The acquirer is the combining entity that obtains control of the acquiree. Control is assessed under IFRS 10: an investor controls an investee when it has power over the investee, exposure to variable returns, and the ability to use its power to affect those returns.  _(IFRS 3.6–.7, IFRS 10.6–.7)_
- **Acquirer indicators** — If IFRS 10 does not clearly identify the acquirer, apply the indicators: the entity transferring cash/assets or incurring liabilities is usually the acquirer; the entity issuing equity is usually the acquirer but watch for a reverse acquisition; relative voting rights, a large minority interest, governing-body composition, senior management, and relative size.  _(IFRS 3.B14–B18, IFRS 3.B19–B27)_

**⚑ AUDIT FLASH POINT — reverse acquisitions.** When the legal subsidiary is the **accounting acquirer** (e.g. a private company merging into a listed shell), the consolidated statements are a continuation of the legal subsidiary's, and earnings per share is recalculated on the IFRS 3.B19–B27 basis. Misidentifying the acquirer inverts which net assets are fair-valued. Document the `IFRS 3.B14`–`B18` indicators.

### Step 2 — Determine the acquisition date — `IFRS 3.8`–`.9`

- **Acquisition date** — The acquisition date is the date the acquirer obtains control of the acquiree — generally the closing date on which consideration is transferred, assets are acquired, and liabilities assumed. Control may be obtained earlier or later than closing by written agreement; document the facts. The acquisition date fixes the measurement date for fair values, the remeasurement date for any previously held interest, and the start of the measurement period.  _(IFRS 3.8–.9, IFRS 3.9)_

### Step 3 — Recognise and measure identifiable assets, liabilities, and NCI — `IFRS 3.10`–`.31`

- **Recognition principle** — As of the acquisition date, the acquirer recognises, separately from goodwill, the identifiable assets acquired, the liabilities assumed, and any non-controlling interest (NCI) in the acquiree. To qualify, an item must meet the Conceptual Framework definition of an asset/liability at the acquisition date and be part of the business combination rather than a separate transaction.  _(IFRS 3.10, IFRS 3.11–.12, .51–.53)_
- **Identifiable intangibles** — Identifiable intangibles are recognised apart from goodwill if separable OR arising from contractual-legal rights: customer relationships, brands, technology, order backlog, non-compete agreements.  _(IFRS 3.B31–B34)_
- **Measurement principle** — Identifiable assets acquired and liabilities assumed are measured at their acquisition-date fair values (per IFRS 13).  _(IFRS 3.18)_
- **NCI measurement — the per-transaction choice** — For each business combination, the acquirer measures any NCI that is a present ownership interest entitling its holder to a proportionate share of net assets on liquidation at either: (a) fair value → full-goodwill method (goodwill includes the NCI's share); or (b) the NCI's proportionate share of the acquiree's identifiable net assets → partial-goodwill method (goodwill is only the acquirer's share). Other components of NCI (e.g. equity-settled share-based payment) are measured per the relevant standard, not by this choice.  _(IFRS 3.19)_

**⚑ AUDIT FLASH POINT — the NCI measurement election (full vs. partial goodwill).** This is the headline IFRS-vs-US-GAAP difference and an IFRS-internal policy choice made deal by deal. Full goodwill grosses up both goodwill and NCI; partial goodwill records neither the NCI's share of goodwill nor that goodwill on subsequent impairment (requiring a notional gross-up under `IAS 36.C4`–`C9` when testing). Document which method was chosen and why, and the numerical effect on goodwill, NCI, and future impairment.

#### Recognition and measurement exceptions (`IFRS 3.21`–`.31A`)

- **Income taxes** — Deferred taxes recognised and measured under IAS 12, not at fair value.  _(IFRS 3.24–.25)_
- **Employee benefits** — Measured under IAS 19.  _(IFRS 3.26)_
- **Indemnification assets** — Recognised on the same basis as the indemnified item.  _(IFRS 3.27–.28)_
- **Reacquired rights** — Measured on the basis of the remaining contractual term, ignoring renewals.  _(IFRS 3.29)_
- **Share-based payment transactions (replacement awards)** — Measured under IFRS 2; pre-combination service portion is consideration, the rest is post-combination expense.  _(IFRS 3.30)_
- **Assets held for sale** — Measured at fair value less costs to sell under IFRS 5.  _(IFRS 3.31)_
- **Contingent liabilities** — A present obligation arising from a past event whose fair value can be measured reliably is recognised even if an outflow is not probable — this overrides the IAS 37 probability recognition threshold at acquisition.  _(IFRS 3.22–.23)_
- **Contracts (revenue / leases)** — The acquirer classifies/designates contracts on the basis of conditions at the acquisition date. Note IFRS has no equivalent to US GAAP's ASU 2021-08 — acquired contract liabilities (deferred revenue) are measured at fair value, not under IFRS 15 as if originated. Leases (IFRS 16): the lease liability is the present value of remaining payments; the right-of-use asset is adjusted for off-market terms.  _(IFRS 3.15–.17, IFRS 3.28A–.28B)_

### Step 4 — Recognise and measure goodwill or a bargain-purchase gain — `IFRS 3.32`–`.36`

- **Goodwill residual formula** — Goodwill =  consideration transferred (at fair value) + amount of any NCI (at FV or proportionate share — the IFRS 3.19 choice) + acquisition-date fair value of the acquirer's previously held equity interest (step acquisition) - acquisition-date net of the identifiable assets acquired and liabilities assumed  _(IFRS 3.32)_
- **Bargain purchase** — If the residual is negative, the acquirer has a bargain purchase. Before recognising a gain, the acquirer must reassess whether it has correctly identified and measured all assets, liabilities, NCI, consideration, and any previously held interest. If a gain remains, recognise it in profit or loss on the acquisition date, attributed to the acquirer.  _(IFRS 3.34, IFRS 3.36)_

**⚑ AUDIT FLASH POINT — bargain purchase gain.** A day-one gain in profit or loss is a red flag for an error in the fair values rather than a genuine bargain. Genuine bargains exist (forced/distressed sellers) but require documented evidence of *why* the seller accepted less than fair value, plus the mandatory `IFRS 3.36` reassessment.

### Consideration transferred — `IFRS 3.37`

- **Consideration transferred** — Measured at acquisition-date fair value — the sum of the fair values of assets transferred, liabilities incurred to former owners, and equity interests issued by the acquirer. Equity issued is measured at acquisition-date fair value.  _(IFRS 3.37–.38)_

### Contingent consideration — `IFRS 3.39`–`.40`, `.58`

- **Initial recognition and classification** — Recognised at acquisition-date fair value as part of consideration transferred, and classified as a financial liability (or asset) or equity under IAS 32.  _(IFRS 3.39, IFRS 3.40)_
- **Subsequent measurement — equity-classified** — Not remeasured; settlement is accounted for within equity.  _(IFRS 3.58(a))_
- **Subsequent measurement — financial-liability/asset-classified** — Remeasured to fair value each period through profit or loss until settled, applying IFRS 9.  _(IFRS 3.58(b))_

**⚑ AUDIT FLASH POINT — contingent-consideration classification and remeasurement.** Liability vs. equity classification under `IAS 32` determines whether earn-out value changes hit P&L. Distinguish contingent consideration from **post-combination remuneration**: if an earn-out is forfeited when a selling shareholder ceases employment, it is post-combination **employee expense**, not consideration (`IFRS 3.B55`).

### Acquisition-related costs — `IFRS 3.53`

- **Acquisition-related costs** — Expensed as incurred in the periods the services are received — advisory, legal, accounting, valuation, finder's fees, and general administrative costs. They are not part of consideration and do not go to goodwill. Costs to issue debt or equity are accounted for under IFRS 9 / IAS 32 (debt costs against the debt; equity issuance costs in equity) — not expensed under this rule.  _(IFRS 3.53)_

### Measurement period — `IFRS 3.45`–`.50`

- **Measurement period** — If the initial accounting is incomplete at the reporting-period end, the acquirer records provisional amounts. During the measurement period — the time needed to obtain information about facts that existed at the acquisition date, not to exceed one year from the acquisition date — the acquirer retrospectively adjusts provisional amounts, with a corresponding adjustment to goodwill, for new information about acquisition-date facts. Unlike US GAAP (ASU 2015-16), IFRS requires the adjustment to be applied as if the accounting had been completed at the acquisition date — i.e. comparatives are retrospectively revised. Information about events after the acquisition date is not a measurement-period adjustment.  _(IFRS 3.45, .50, IFRS 3.45–.49, IFRS 3.49)_

### Business combination achieved in stages (step acquisition) — `IFRS 3.41`–`.42`

- **Step acquisition** — When the acquirer held an equity interest in the acquiree before obtaining control, it remeasures that previously held interest to its acquisition-date fair value and recognises any resulting gain or loss in profit or loss. Amounts previously recognised in OCI relating to that interest are reclassified (or transferred to retained earnings) on the same basis as if the interest had been disposed of. The remeasured fair value of the prior interest enters the goodwill computation (Step 4).  _(IFRS 3.41–.42, IFRS 3.42)_

### Definition of a business and the optional concentration test — `IFRS 3.B7`–`B12D` (2020 amendments)

- **Definition of a business** — A business is an integrated set of activities and assets capable of being conducted and managed to provide goods or services — it must include, at a minimum, an input and a substantive process that together significantly contribute to the ability to create output.  _(IFRS 3.B7)_
- **Optional concentration test** — The 2020 amendments add an optional concentration test: if substantially all of the fair value of the gross assets acquired is concentrated in a single identifiable asset or group of similar assets, the set is not a business (allocate cost, no goodwill, transaction costs capitalised to the assets). If the concentration test is failed or not elected, assess inputs/processes/outputs under IFRS 3.B8–B12D.  _(IFRS 3.B7B, IFRS 3.B8–B12D)_

### In-process research and development (IPR&D)

- **IPR&D** — Acquired IPR&D meeting the identifiability criteria is recognised as a separate intangible asset at fair value, not expensed at acquisition. Until the project is complete it is treated as having an indefinite useful life and is tested for impairment annually (not amortised); once complete it is amortised over its useful life, or written off if abandoned.  _(IFRS 3.B31, IAS 38.34)_

## Section 4 — Reference layer: subsequent impairment of goodwill — IAS 36

- **Goodwill not amortised** — Goodwill is not amortised under IFRS — for all entities (there is no private-company amortisation option). After initial recognition it is measured at cost less accumulated impairment losses.  _(IFRS 3.B63(a), IAS 36.10)_
- **Allocation to CGUs** — Goodwill is allocated to each cash-generating unit (CGU) or group of CGUs expected to benefit from the synergies of the combination — at the lowest level monitored internally, and no larger than an operating segment.  _(IAS 36.80–.87, IAS 36.80)_
- **Annual test** — A CGU (or group) to which goodwill has been allocated is tested for impairment at least annually, and whenever there is an indicator of impairment.  _(IAS 36.10(b), .90)_
- **The test — recoverable amount formula** — Recoverable amount = the HIGHER of (a) fair value less costs of disposal (IAS 36.28),  and (b) value in use  (present value of future cash flows, IAS 36.30-.57)  _(IAS 36.18, .74, .90)_
- **Impairment allocation** — If carrying amount exceeds recoverable amount, the impairment loss is allocated first to goodwill of the CGU, then pro rata to the other assets of the CGU (subject to floors — an individual asset is not written below the higher of its own FVLCD, value in use, or zero).  _(IAS 36.104)_
- **Reversal** — An impairment of goodwill is NEVER reversed. However, impairment of other assets (and other CGU assets) may be reversed if the recoverable amount increases — a key contrast with US GAAP.  _(IAS 36.124, IAS 36.114–.123)_
- **Partial-goodwill gross-up for testing** — Where NCI was measured at its proportionate share (partial goodwill), the carrying amount of goodwill is notionally grossed up to include the goodwill attributable to the NCI before comparing to recoverable amount; any resulting impairment is then split between parent and NCI, but only the parent's share is recognised.  _(IAS 36.C4–C9)_

**⚑ AUDIT FLASH POINT — value-in-use assumptions and CGU identification.** Auditors challenge (a) how CGUs/groups were identified and whether goodwill was spread to avoid impairment, and (b) the value-in-use cash-flow projections, terminal growth rate, and pre-tax discount rate (`IAS 36.55`–`.57`). Disclose the key assumptions and the sensitivity (`IAS 36.134`). The partial-goodwill notional gross-up is frequently missed.

## Section 5 — Executable layer (Layer B): the procedure

Run these steps on the transaction's facts. Each cites the Layer A rule it executes.

1. **Confirm the transaction is a business combination** — definition of a business / optional concentration test (§3, `IFRS 3.B7`–`B12D`). If it is an asset acquisition, stop and allocate cost (no goodwill; costs capitalised).
2. **Identify the acquirer** (Step 1 / §2, `IFRS 3.6`–`.7`, IFRS 10 control). Check for a reverse acquisition.
3. **Determine the acquisition date** (Step 2 / §2, `IFRS 3.8`–`.9`).
4. **Build consideration transferred** at fair value (§3, `IFRS 3.37`): cash + assets + equity issued + acquisition-date fair value of contingent consideration (classified liability/equity). Strip out post-combination remuneration and settlement of pre-existing relationships.
5. **If a step acquisition**, remeasure the previously held interest to fair value; book the gain/loss to P&L (§3, `IFRS 3.42`).
6. **Recognise and fair-value the identifiable assets and liabilities** (Step 3 / §2, `IFRS 3.18`); apply each recognition/measurement **exception** (income tax, contingent liabilities, leases, etc.).
7. **Choose the NCI measurement** for this deal (§2, `IFRS 3.19`): fair value (full goodwill) **or** proportionate share of identifiable net assets (partial goodwill). State and justify the election.
8. **Compute goodwill** (Step 4 / §2, `IFRS 3.32`). If negative, **reassess** (`IFRS 3.36`), then recognise any remaining **bargain-purchase gain** in P&L.
9. **Expense acquisition-related costs** as incurred (§3, `IFRS 3.53`).
10. **Book the consolidation journal entry** (base §3 format); record provisional amounts if incomplete and open the **measurement period** (§3).
11. **Subsequently:** remeasure liability-classified contingent consideration through P&L (§3); test goodwill for impairment under **IAS 36** at the CGU level (§4), grossing up partial goodwill where applicable.
12. **Produce the disclosure checklist** (§7) and **reviewer brief** with every flash point.

### Worked example (illustrative)

**Acquirer** buys **80%** of **Target** for **$800,000 cash** on the acquisition date. The fair value of Target's **identifiable net assets** is **$700,000**. The acquisition-date **fair value of the 20% NCI** is **$190,000**. The acquirer held no prior interest. Acquisition-related costs were **$25,000** (cash). IFRS 3.19 gives a **per-transaction choice** — both methods are shown.

**(a) Full-goodwill method — NCI at fair value (`IFRS 3.19(a)`):**

```
Goodwill = consideration 800,000 + NCI at FV 190,000 - identifiable net assets 700,000 = 290,000
```

```
Acquisition date — consolidate Target, NCI at fair value — driving rule: IFRS 3.32 / .19(a)
  Dr  Identifiable net assets (at fair value)     700,000
  Dr  Goodwill                                     290,000
      Cr  Cash                                          800,000
      Cr  Non-controlling interest (equity)             190,000
  (memo: goodwill = 800,000 + 190,000 - 700,000 = 290,000.
   Debits 990,000 = Credits 990,000 ✓)
```

**(b) Partial-goodwill method — NCI at proportionate share (`IFRS 3.19(b)`):**

```
NCI = 20% × identifiable net assets 700,000 = 140,000
Goodwill = consideration 800,000 + NCI 140,000 - identifiable net assets 700,000 = 240,000
```

```
Acquisition date — consolidate Target, NCI at proportionate share — driving rule: IFRS 3.32 / .19(b)
  Dr  Identifiable net assets (at fair value)     700,000
  Dr  Goodwill                                     240,000
      Cr  Cash                                          800,000
      Cr  Non-controlling interest (equity)             140,000
  (memo: goodwill = 800,000 + 140,000 - 700,000 = 240,000.
   Debits 940,000 = Credits 940,000 ✓)
```

The two methods differ by **$50,000** (290,000 − 240,000) — the goodwill attributable to the NCI. Under partial goodwill it is **not** recognised; on a later impairment test it must be **notionally grossed up** (`IAS 36.C4`–`C9`). **US GAAP permits only method (a).**

```
Acquisition date — acquisition-related costs — driving rule: IFRS 3.53
  Dr  Acquisition expense (P&L)                     25,000
      Cr  Cash                                           25,000
  (memo: advisory + legal expensed as incurred, not capitalised to goodwill; debits = credits ✓)
```

**Step-acquisition note.** Suppose the acquirer previously held 10% of Target carried at $60,000 with an acquisition-date fair value of $95,000, then buys a further 70% giving control. Remeasure the prior interest to $95,000, booking a **$35,000 gain to P&L** (`IFRS 3.42`):

```
Acquisition date — remeasure previously held interest — driving rule: IFRS 3.42
  Dr  Investment in Target (equity interest)         35,000
      Cr  Gain on remeasurement of prior interest (P&L)  35,000
  (memo: 95,000 FV - 60,000 carrying amount = 35,000; debits = credits ✓)
```

The $95,000 remeasured fair value then enters the goodwill formula as the "previously held equity interest" term.

**Contingent-consideration note.** Suppose the deal also includes an **earn-out** with an acquisition-date fair value of **$120,000**, classified as a **financial liability** under `IAS 32`. It is part of consideration (increasing goodwill), remeasured each period through P&L:

```
Acquisition date — recognise contingent consideration — driving rule: IFRS 3.39
  Dr  Goodwill                                      120,000
      Cr  Contingent consideration liability            120,000
  (memo: earn-out at acquisition-date fair value; financial liability per IAS 32; debits = credits ✓)

Subsequent period — fair value rises to 150,000 — driving rule: IFRS 3.58(b)
  Dr  Fair value loss on contingent consideration (P&L)  30,000
      Cr  Contingent consideration liability                  30,000
  (memo: 150,000 - 120,000 = 30,000 through P&L, NOT goodwill; debits = credits ✓)
```

**⚑ AUDIT FLASH POINT — the NCI election cascades into impairment.** Because the partial-goodwill method omits the NCI's share of goodwill, a CGU impairment test requires the `IAS 36.C4`–`C9` notional gross-up, and only the parent's share of the resulting loss is recognised. A dual-reporter whose US parent must use full goodwill for the same deal will show different goodwill, NCI, and impairment. Reconcile both in the reviewer brief.

## Section 6 — Divergence from US GAAP (ASC 805 / ASC 350)

IFRS 3 and ASC 805 are substantially converged on the acquisition method, but several differences change the numbers. A dual-reporter must check each:

**IFRS vs US GAAP divergence table**  _(IFRS 3.19; ASC 805-20-30-1; ASC 350-20-15-4; IAS 36.80; IAS 36.18, .104; IAS 36.124, .114; IFRS 3.23; ASU 2021-08; IFRS 3.58; ASC 805-30-35-1; IFRS 3.53; 805-10-25-23; IFRS 3.49; ASU 2015-16)_

| Area | IFRS (IFRS 3 / IAS 36) | US GAAP (ASC 805 / ASC 350) |
| --- | --- | --- |
| **NCI measurement** | **Per-transaction choice**: fair value (full goodwill) **or** proportionate share of identifiable net assets (partial goodwill) (`IFRS 3.19`) | NCI **must** be at **fair value** → **full goodwill** only (`ASC 805-20-30-1`) |
| **Goodwill — subsequent** | Impairment-only for **all** entities; **no amortisation option** | Impairment-only for public entities; **private-company/NFP alternative** permits **amortisation ≤ 10 years** + triggering-event-only testing (`ASC 350-20-15-4`) |
| **Goodwill impairment unit** | **Cash-generating unit (CGU)** or group of CGUs (`IAS 36.80`) | **Reporting unit** (operating segment or one level below) |
| **Goodwill impairment measure** | Recoverable amount = **higher of** fair value less costs of disposal **and** value in use; loss to goodwill first, then pro rata (`IAS 36.18`, `.104`) | Single-step: carrying amount of reporting unit **over** its fair value, **capped at goodwill** (post-ASU 2017-04) |
| **Reversal of impairment** | Goodwill impairment **never reversed** (`IAS 36.124`); **other** asset impairments **may be reversed** (`IAS 36.114`) | Goodwill impairment **never reversed**; most other asset impairments **not** reversed |
| **Definition of a business** | **Optional concentration test** + framework (2020 amendments) | Screen test + framework (ASU 2017-01) — converged but cited separately |
| **Acquired contingent liabilities** | Recognise at fair value at acquisition **even if outflow not probable** (`IFRS 3.23`) — overrides IAS 37 threshold | Recognise at fair value if determinable; otherwise apply ASC 450 |
| **Acquired deferred revenue** | Measured at **fair value** (no ASU 2021-08 equivalent) | Measured under **ASC 606** as if originated (ASU 2021-08) — a divergence |
| **Contingent consideration — subsequent** | Liability → P&L; equity → not remeasured (`IFRS 3.58`) | Same — converged (`ASC 805-30-35-1`) |
| **Acquisition costs** | Expensed as incurred (`IFRS 3.53`) | Expensed as incurred (`805-10-25-23`) — converged |
| **Measurement period** | Up to 1 year; adjustments **retrospective** to acquisition date, comparatives revised (`IFRS 3.49`) | Up to 1 year; adjustments in **current period** with prior-period effect disclosed (ASU 2015-16) |

Run `us-gaap-asc805-business-combinations` in parallel for dual-reporters and present both answers (base §2).

## Section 7 — Disclosure checklist — `IFRS 3.59`–`.63`, `B64`–`B67`; IAS 36 disclosures

Trigger and produce as relevant:

- [ ] Name and description of the acquiree; acquisition date; percentage of voting equity interests acquired; primary reasons for the combination and how control was obtained (`IFRS 3.B64(a)`–`(d)`)
- [ ] Acquisition-date fair value of **total consideration** transferred, by major class (cash, equity, contingent consideration) (`IFRS 3.B64(f)`)
- [ ] **Contingent consideration**: amount recognised, description, range of outcomes; subsequent changes (`IFRS 3.B64(g)`, `B67(b)`)
- [ ] Amounts recognised for each major class of **assets acquired and liabilities assumed** (`IFRS 3.B64(i)`)
- [ ] **Contingent liabilities** recognised (or, if not, why) (`IFRS 3.B64(j)`)
- [ ] **Goodwill** recognised and a qualitative description of the factors that make it up; tax-deductible portion (`IFRS 3.B64(e)`, `(k)`)
- [ ] For a **bargain purchase**: the gain, the line item, and the reasons (`IFRS 3.B64(n)`)
- [ ] **NCI** recognised, the **measurement basis chosen** (fair value vs. proportionate share), and the valuation technique/key inputs if at fair value (`IFRS 3.B64(o)`)
- [ ] **Step acquisition:** acquisition-date fair value of the previously held interest and the **remeasurement gain/loss** and its line item (`IFRS 3.B64(p)`)
- [ ] Acquisition-related **costs**, the amount expensed, and the line item (`IFRS 3.B64(m)`)
- [ ] **Measurement-period** adjustments — nature and amount (`IFRS 3.B67(a)`)
- [ ] Acquiree **revenue and profit/loss** since acquisition and **supplemental pro forma** as if combined from the start of the period (`IFRS 3.B64(q)`)
- [ ] **Goodwill reconciliation**: gross carrying amount, accumulated impairment, movements (`IAS 36.134`–`.135`)
- [ ] Goodwill **impairment test** disclosures: CGU/group, recoverable-amount basis (FVLCD or value in use), key assumptions, discount rate, sensitivity (`IAS 36.130`, `.134`)

## Section 8 — Topic self-checks (in addition to base §7)

- [ ] Confirmed a **business** (concentration test considered) vs. an asset acquisition; if asset acquisition, no goodwill and costs capitalised
- [ ] **Acquirer** identified via IFRS 10 control; reverse-acquisition possibility checked
- [ ] **Acquisition date** = date control obtained, tied to `IFRS 3.8`–`.9`
- [ ] Identifiable assets/liabilities at **fair value**; each recognition/measurement **exception** applied (tax, contingent liabilities, leases, etc.)
- [ ] **NCI measurement choice** stated and justified (full vs. partial goodwill, `IFRS 3.19`); numerical effect shown
- [ ] **Consideration** at fair value; contingent consideration classified (liability/equity) and fair-valued; remuneration stripped out
- [ ] **Goodwill** = consideration + NCI + prior-interest FV − identifiable net assets; arithmetic shown and balanced for each method run
- [ ] Negative residual → **reassessed** (`IFRS 3.36`), then bargain-purchase **gain to P&L**
- [ ] Acquisition-related costs **expensed**, not capitalised to goodwill
- [ ] Step acquisition → prior interest **remeasured to FV**, gain/loss to P&L
- [ ] **Measurement period** opened for provisional amounts; ≤ 1 year; adjustments applied **retrospectively** (`IFRS 3.49`)
- [ ] Subsequent: liability contingent consideration remeasured to P&L; goodwill tested under **IAS 36** at CGU level; partial goodwill **grossed up** for testing
- [ ] Divergence from ASC 805 / ASC 350 checked for dual-reporters (NCI method, amortisation, impairment model, measurement-period treatment)

## Section 9 — Disclaimer

Provides computational and interpretive guidance on IFRS 3 / IAS 36 only. Not an audit and not assurance. Business-combination accounting turns heavily on entity-specific facts and significant judgement — fair-value measurement of intangibles and contingent consideration, identification of the acquirer, the business-vs-asset determination, the NCI measurement election, and goodwill impairment all require specialist input. Have outputs reviewed and signed by a qualified accountant before they are reflected in financial statements relied upon by third parties.

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
