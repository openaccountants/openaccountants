---
name: ifrs3-business-combinations
description: IFRS accounting for business combinations under IFRS 3 (Business Combinations) and scoped related IAS 36 goodwill impairment guidance. Covers the acquisition method  -  identify the acquirer, determine the acquisition date, recognise and measure the identifiable assets acquired, liabilities assumed and any non-controlling interest, and recognise goodwill or a bargain purchase gain  -  plus consideration transferred and contingent consideration, acquisition-related costs, the measurement period, step acquisitions, recognition exceptions, the definition of a business and the optional concentration test, in-process R&D, and scoped subsequent IAS 36 goodwill impairment testing. Produces recognition conclusions, journal entries, and a reviewer brief. Issued as the IFRS edition of the business-combinations topic; see us-gaap-asc805-business-combinations for the US GAAP edition. MUST load alongside financial-reporting-workflow-base.
version: 0.4
jurisdiction: GLOBAL
last_updated: 2026-11-16
depends_on:
  - financial-reporting-workflow-base
category: financial-statements
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: financial-reporting
type: computation
standard: "IFRS 3 Business Combinations"
effective_date: 2022-01-01
source_checked: 2026-11-16
---

# IFRS 3 business combinations v0.4

**Coverage is partial:** individually identified supporting-source and current US comparison gaps below remain outside usable instructions.

**General reference only.** Produces working papers and a reviewer brief, not an audit, assurance opinion or signed financial statements. Tier 2; not approved by an accountant.

## Scope

**Standard and effective-date basis:** IFRS 3 Business Combinations; effective-date key **2022-01-01** for the Reference to the Conceptual Framework amendments. Paragraph .64Q applies them to combinations acquired on or after the beginning of the first annual period beginning on or after 1 January 2022. Earlier application requires simultaneous or earlier application of all March 2018 Amendments to References to the Conceptual Framework. This date does not establish later supporting-standard adoption. [IFRS 3.64Q](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs3.html).


**This is a content skill that loads on top of `financial-reporting-workflow-base`.** It supplies the recognition, measurement, presentation, and disclosure rules for business combinations under IFRS, and the scoped subsequent IAS 36 goodwill impairment analysis below. The base supplies the two-layer output contract, the journal-entry format, and the self-checks.

- **Scope**  -  IFRS 3 applies to a transaction or other event in which an acquirer obtains control of one or more businesses. It does not apply to: the formation of a joint arrangement in the financial statements of the joint arrangement itself; the acquisition of an asset or group of assets that is not a business (allocate cost, no goodwill); and combinations of entities or businesses under common control.  _(IFRS 3.1–.3, IFRS 3.2(a), IFRS 3.2(b), IFRS 3.2(c), B1–B4)_


This skill covers:

- The acquisition method of IFRS 3  -  the 4 steps (`IFRS 3.4`–`.5`).
- Consideration transferred at fair value, including contingent consideration and its subsequent measurement.
- Acquisition-related (transaction) costs.
- The recognition and measurement **exceptions** to the fair-value principle.
- The **per-transaction NCI measurement choice** (full vs. partial goodwill).
- The measurement period and retrospective measurement-period adjustments.
- Step (combination achieved in stages) acquisitions and the remeasurement of a previously held equity interest.
- Bargain purchases.
- The definition of a business and the optional **concentration test** (asset vs. business).
- In-process research and development (IPR&D).
- Subsequent IAS 36 goodwill impairment at the CGU level, including allocation, testing and the partial-goodwill adjustment below.

This skill does NOT cover: asset acquisitions outside IFRS 3, common-control combinations (outside IFRS 3; separate applicable-policy analysis required), the consolidation procedures and the control assessment themselves (`IFRS 10`), or joint arrangements (`IFRS 11`). It defers the US GAAP treatment to `us-gaap-asc805-business-combinations`.


**Version basis for 2026 work.** The effective-date field identifies the Conceptual Framework amendment basis (IFRS 3.64Q). The revised-2008 Standard has the .64 acquisition/annual-period application gate beginning 1 July 2009; the definition/concentration amendments use the first annual period beginning on or after 1 January 2020 for combinations and asset acquisitions (.64P). IFRS 10 initially applies to annual periods beginning on or after 1 January 2013, with its early-adoption companion requirements (C1). Apply IFRS 9/IFRS 17 consequential provisions only when those Standards apply; their separate transition dates were not recovered here. IFRS 18/IFRS 19 consequential presentation/disclosure changes are excluded until adopted. The 2026 issued HTML also contains future-effective text; do not assume its publication year is its effective date. The operative core was personally read in the official copy retrieved on 14 November 2026. Official retrieval succeeded again on 16 November 2026 and the core was reconciled with that body; selected supporting clauses were personally read on 16 November. The source table distinguishes those reads from retrieval alone.

## Ask the client first

- Reporting period, acquisition date, IFRS 17/18 adoption, reporting framework and any investment-entity exception.
- Purchase agreement, ownership/control history, legal/accounting acquirer and any common-control, joint-arrangement or SPAC facts.
- Business inputs, workforce/processes/outputs and whether the optional concentration test is elected.
- Cash/equity/prior-interest fair values, net-asset valuation, NCI rights and chosen eligible NCI measurement basis.
- Contingencies, leases, taxes, benefits, indemnities, replacement awards, earn-out employment terms and acquisition/issue costs.
- Provisional amounts, information outstanding and goodwill/CGU impairment evidence for the separate IAS 36 handoff.

## The method, step by step

### Section 2  -  Reference layer (Layer A): the acquisition method

- **Acquisition method**  -  Every business combination in scope is accounted for by applying the acquisition method. The method has 4 steps.  _(IFRS 3.4–.5, IFRS 3.5)_

### Step 1  -  Identify the acquirer  -  `IFRS 3.6`–`.7`, `B13`–`B18`

- **Identify the acquirer**  -  The acquirer is the combining entity that obtains control of the acquiree. IFRS 3.7 requires IFRS 10 guidance to identify it; obtain a separately evidenced IFRS 10 control conclusion before executing the acquisition method, using the recovered basic control clauses and any further applicable guidance. The basic IFRS 10.6-.7 test requires all 3 elements: power, exposure/rights to variable returns and ability to use that power to affect returns. Consider all facts and reassess changes (.8); protective rights alone do not supply power (.14). The underlying facts, principal/agent questions and any complex application still need the separate control working paper. _(IFRS 3.6–.7)_
- **Acquirer indicators**  -  If IFRS 10 does not clearly identify the acquirer, apply the indicators: the entity transferring cash/assets or incurring liabilities is usually the acquirer; the entity issuing equity is usually the acquirer but watch for a reverse acquisition; relative voting rights, a large minority interest, governing-body composition, senior management, and relative size.  _(IFRS 3.B14–B18, IFRS 3.B19–B27)_

**⚑ AUDIT FLASH POINT  -  reverse acquisitions.** When the legal subsidiary is the **accounting acquirer** (e.g. a private company merging into a listed shell), the consolidated statements are a continuation of the legal subsidiary's, and earnings per share is recalculated on the IFRS 3.B19–B27 basis. Misidentifying the acquirer inverts which net assets are fair-valued. Document the `IFRS 3.B14`–`B18` indicators.

### Step 2  -  Determine the acquisition date  -  `IFRS 3.8`–`.9`

- **Acquisition date**  -  The acquisition date is the date the acquirer obtains control of the acquiree  -  generally the closing date on which consideration is transferred, assets are acquired, and liabilities assumed. Control may be obtained earlier or later than closing by written agreement; document the facts. The acquisition date fixes the measurement date for fair values, the remeasurement date for any previously held interest, and the start of the measurement period.  _(IFRS 3.8–.9, IFRS 3.9)_

### Step 3  -  Recognise and measure identifiable assets, liabilities, and NCI  -  `IFRS 3.10`–`.31`

- **Recognition principle**  -  As of the acquisition date, the acquirer recognises, separately from goodwill, the identifiable assets acquired, the liabilities assumed, and any non-controlling interest (NCI) in the acquiree. To qualify, an item must meet the Conceptual Framework definition of an asset/liability at the acquisition date and be part of the business combination rather than a separate transaction.  _(IFRS 3.10, IFRS 3.11–.12, .51–.53)_
- **Identifiable intangibles**  -  Identifiable intangibles are recognised apart from goodwill if separable OR arising from contractual-legal rights: customer relationships, brands, technology, order backlog, non-compete agreements.  _(IFRS 3.B31–B34)_
- **Measurement principle**  -  Identifiable assets acquired and liabilities assumed are measured at their acquisition-date fair values (per IFRS 13).  _(IFRS 3.18)_
- **NCI measurement  -  the per-transaction choice**  -  For each business combination, the acquirer measures any NCI that is a present ownership interest entitling its holder to a proportionate share of net assets on liquidation at either: (a) fair value → full-goodwill method (goodwill includes the NCI's share); or (b) the NCI's proportionate share of the acquiree's identifiable net assets → partial-goodwill method (goodwill is only the acquirer's share). Other NCI components are measured at acquisition-date fair value unless another basis is required by an applicable IFRS; the eligible ownership-interest election does not extend to them.  _(IFRS 3.19)_

**⚑ AUDIT FLASH POINT  -  the NCI measurement election (full vs. partial goodwill).** This is an IFRS measurement choice for eligible NCI made deal by deal; the current US comparison is reserved. Full goodwill grosses up both goodwill and NCI; partial goodwill excludes the unrecognised NCI goodwill component; apply the scoped IAS 36 notional-gross-up and impairment-allocation rules below. Document which method was chosen and why, and the numerical effect on goodwill, NCI, and future impairment.

#### Recognition and measurement exceptions (`IFRS 3.21`–`.31A`)

- **Income taxes**  -  Deferred taxes recognised and measured under IAS 12, not at fair value.  _(IFRS 3.24–.25)_
- **Employee benefits**  -  Measured under IAS 19.  _(IFRS 3.26)_
- **Indemnification assets**  -  Recognise with the indemnified item on a consistent measurement basis, subject to collectibility and contractual limits. If fair value measures the indemnity, collectibility uncertainty is included in fair value rather than a separate allowance; for an exception item use consistent assumptions with the required collectibility assessment.  _(IFRS 3.27–.28)_
- **Reacquired rights**  -  Measured on the basis of the remaining contractual term, ignoring renewals.  _(IFRS 3.29)_
- **Share-based payment transactions (replacement awards)**  -  Measured under IFRS 2; pre-combination service portion is consideration, the rest is post-combination expense.  _(IFRS 3.30)_
- **Assets held for sale**  -  Measured at fair value less costs to sell under IFRS 5.  _(IFRS 3.31)_
- **Contingent liabilities**  -  A present obligation arising from a past event whose fair value can be measured reliably is recognised even if an outflow is not probable  -  this overrides the IAS 37 probability recognition threshold at acquisition.  _(IFRS 3.22–.23)_
- **Contracts (revenue / leases)**  -  The acquisition-date conditions generally determine classification/designation under .15. For an acquiree-lessor lease, .17 instead uses inception terms, or the relevant classification-changing modification date. Acquired contract liabilities follow the .18 fair-value principle subject to applicable exceptions; the current US comparison remains reserved. For acquiree-lessee leases identified under IFRS 16, .28A permits omission of ROU/liability where the lease term ends within 12 months of acquisition or the underlying asset is low value. Otherwise .28B measures the liability as a new lease at acquisition using remaining payments, and ROU at that liability adjusted for off-market terms.  _(IFRS 3.15–.17, IFRS 3.28A–.28B)_

### Step 4  -  Recognise and measure goodwill or a bargain-purchase gain  -  `IFRS 3.32`–`.36`

- **Goodwill residual formula**  -  Goodwill =  consideration transferred (at fair value) + amount of any NCI (at FV or proportionate share  -  the IFRS 3.19 choice) + acquisition-date fair value of the acquirer's previously held equity interest (step acquisition) - acquisition-date net of the identifiable assets acquired and liabilities assumed  _(IFRS 3.32)_
- **Bargain purchase**  -  If the residual is negative, the acquirer has a bargain purchase. Before recognising a gain, the acquirer must reassess whether it has correctly identified and measured all assets, liabilities, NCI, consideration, and any previously held interest. If a gain remains, recognise it in profit or loss on the acquisition date, attributed to the acquirer.  _(IFRS 3.34, IFRS 3.36)_

**⚑ AUDIT FLASH POINT  -  bargain purchase gain.** A day-one gain in profit or loss is a red flag for an error in the fair values rather than a genuine bargain. Genuine bargains exist (forced/distressed sellers) but require documented evidence of *why* the seller accepted less than fair value, plus the mandatory `IFRS 3.36` reassessment.

### Consideration transferred  -  `IFRS 3.37`

- **Consideration transferred**  -  Measured at acquisition-date fair value  -  the sum of the fair values of assets transferred, liabilities incurred to former owners, and equity interests issued by the acquirer. Equity issued is measured at acquisition-date fair value.  _(IFRS 3.37–.38)_

### Contingent consideration  -  `IFRS 3.39`–`.40`, `.58`

- **Initial recognition and classification**  -  Recognised at acquisition-date fair value as part of consideration transferred, and classified as a financial liability (or asset) or equity under IAS 32.  _(IFRS 3.39, IFRS 3.40)_
- **Subsequent measurement  -  equity-classified**  -  Not remeasured; settlement is accounted for within equity.  _(IFRS 3.58(a))_
- **Subsequent measurement  -  financial-liability/asset-classified**  -  Remeasured to fair value each period through profit or loss until settled, applying IFRS 9.  _(IFRS 3.58(b))_

**⚑ AUDIT FLASH POINT  -  contingent-consideration classification and remeasurement.** Liability vs. equity classification under `IAS 32` determines whether earn-out value changes hit P&L. Distinguish contingent consideration from **post-combination remuneration**: if an earn-out is forfeited when a selling shareholder ceases employment, it is post-combination **employee expense**, rather than consideration, unless the service condition is not substantive (`IFRS 3.B55(a)`; January 2013 agenda decision and the March 2024 decision published in April). Assess the actual service condition; a limited handover period, ordinary executive pay and specified death/disability/agreed-termination exceptions do not alone remove the agenda decision's fact pattern.

### Acquisition-related costs  -  `IFRS 3.53`

- **Acquisition-related costs**  -  Expensed as incurred in the periods the services are received  -  advisory, legal, accounting, valuation, finder's fees, and general administrative costs. They are not part of consideration and do not go to goodwill. Costs to issue debt or equity are accounted for under IFRS 9 / IAS 32 rather than the general acquisition-expense rule; the detailed IFRS 9/IAS 32 issue-cost treatment requires its separately sourced analysis.  _(IFRS 3.53)_

### Measurement period  -  `IFRS 3.45`–`.50`

- **Measurement period**  -  If the initial accounting is incomplete at the reporting-period end, the acquirer records provisional amounts. During the measurement period  -  the period ending as soon as the sought acquisition-date information is received or more information is learned to be unobtainable, with an absolute maximum of 1 year from acquisition  -  the acquirer retrospectively adjusts provisional amounts, with a corresponding adjustment to goodwill, for new information about acquisition-date facts. IFRS requires the adjustment to be applied as if the accounting had been completed at the acquisition date  -  i.e. comparatives are retrospectively revised. Information about events after the acquisition date is not a measurement-period adjustment.  _(IFRS 3.45, .50, IFRS 3.45–.49, IFRS 3.49)_

### Business combination achieved in stages (step acquisition)  -  `IFRS 3.41`–`.42`

- **Step acquisition**  -  When the acquirer held an equity interest in the acquiree before obtaining control, it remeasures that previously held interest to its acquisition-date fair value and recognises the resulting gain or loss in profit or loss or OCI as appropriate under .42. The remeasurement gain or loss goes to profit or loss or OCI as appropriate; amounts previously in OCI are treated on the same basis as a direct disposal. A profit-or-loss gain is therefore not universal (.42). The remeasured fair value of the prior interest enters the goodwill computation (Step 4).  _(IFRS 3.41–.42, IFRS 3.42)_

### Definition of a business and the optional concentration test  -  `IFRS 3.B7`–`B12D` (2020 amendments)

- **Definition of a business**  -  A business is an integrated set of activities and assets capable of being conducted and managed to provide goods or services, investment income (such as dividends or interest) or other income from ordinary activities  -  it must include, at a minimum, an input and a substantive process that together significantly contribute to the ability to create output.  _(IFRS 3.B7)_
- **Optional concentration test**  -  The 2020 amendments add an optional concentration test: if substantially all of the fair value of the gross assets acquired is concentrated in a single identifiable asset or group of similar assets, the set is not a business (allocate cost, no goodwill; transaction-cost treatment requires the applicable asset-standard analysis). If the concentration test is failed or not elected, assess inputs/processes/outputs under IFRS 3.B8–B12D.  _(IFRS 3.B7B, IFRS 3.B8–B12D)_

### In-process research and development (IPR&D)

- **IPR&D**  -  Acquired IPR&D meeting the identifiability criteria is recognised as a separate intangible asset at fair value, not expensed at acquisition. Before availability for use, do not amortise; test annually and on impairment indicators (IAS 36.9-.10; IAS 38.97). This does not automatically mean the useful life is indefinite. Determine finite/indefinite life under IAS 38.88-.96; finite-life amortisation starts when available for use (.97), and indefinite-life assets are not amortised but tested annually and on indicators (.107-.110). Later research expenditure is expensed; later development expenditure is capitalised only if every .57 criterion is demonstrated (.42-.43, .54-.67). Abandonment requires the impairment/derecognition analysis; derecognise when no future benefits are expected from use or disposal (.112), rather than assuming every discontinued project has zero recovery.  _(IFRS 3.10, .18, B31)_

### Goodwill after acquisition

IFRS 3.B63(a) carries goodwill at its recognised amount less accumulated impairment losses; it is not amortised. Apply these IAS 36 rules to the actual valuation facts:

- Allocate goodwill from acquisition to CGUs/groups expected to benefit from synergies, at the lowest level monitored internally and no larger than an operating segment **before aggregation** (.80-.87). If initial allocation cannot be completed in the acquisition year, complete it before the end of the first annual period beginning after acquisition and disclose the unallocated amount/reasons (.84-.85, .133).
- Test allocated goodwill annually and whenever indicators exist (.9-.10, .90). Annual testing is at a consistent time; goodwill acquired during the current annual period must be tested before that period ends (.96). Test relevant individual assets/lower-level CGUs before the goodwill-containing unit/group (.97-.98); the prior-year calculation relief requires every .99 criterion.
- Recoverable amount is the higher of fair value less costs of disposal and value in use (.18-.22, .74). Compare on a consistent carrying-amount basis, including attributable assets, applicable corporate assets and liabilities only as the .75-.79/.100-.102 conditions require.
- Value-in-use assumptions must be reasonable/supportable with greater weight on external evidence. Management-approved budgets/forecasts normally cover no more than **5 years**, unless a longer period is justified; use supported extrapolation and exclude uncommitted restructuring/enhancement, financing and income-tax cash flows (.30-.54). Use pre-tax discount rates without double-counting risks (.55-.57).
- Allocate a CGU impairment first to goodwill and then pro rata to other assets (.104). Do not reduce another asset below the highest of measurable fair value less disposal costs, determinable value in use and **0**; reallocate the excluded loss to other assets (.105).
- Never reverse goodwill impairment (.124-.125). For another asset, reversal requires a change in the recoverable-amount estimates, not the passage of time alone; cap the carrying amount by the no-impairment depreciated/amortised amount, and apply the revalued-asset, depreciation and CGU-allocation limits (.110-.123).
- For partial goodwill, gross up the goodwill carrying amount by the unrecognised NCI goodwill before the CGU comparison (C4). Allocate loss to goodwill before other assets (C5); the parent/NCI allocation depends on whether the subsidiary is the whole CGU or part of a larger CGU (C6-C7). Only an NCI loss relating to **unrecognised goodwill** is omitted from recognised goodwill impairment (C8); that exception does not eliminate recognised losses on other assets.

For the original 80% acquisition example, the **USD 50,000** difference between recorded full and partial goodwill reflects the supplied NCI fair value versus proportionate net assets. It is not automatically the C4 notional gross-up. Establish the CGU, synergies and parent/NCI allocation before any impairment calculation; no impairment amount is inferred from that difference.

⚑ AUDIT FLASH POINT - document CGU identification and value-in-use cash flows, terminal growth and pre-tax discount rates. IAS 36.130 applies to losses/reversals in the period, with the prescribed event, amount, asset/CGU and valuation information. For significant goodwill/indefinite-life allocations, .134 requires carrying amounts, recoverable-amount basis, key assumptions/management approach and applicable forecast/growth/discount information; a reasonably possible assumption change that would remove headroom triggers .134(f)'s quantified sensitivity. For individually insignificant allocations with a significant aggregate sharing assumptions, apply .135's separate aggregate disclosures. These are specific triggers, not an identical sensitivity note for every CGU.

### Section 5  -  Executable layer (Layer B): the procedure

Run these steps on the transaction's facts. Each cites the Layer A rule it executes.

1. **Confirm the transaction is a business combination**  -  definition of a business / optional concentration test (§3, `IFRS 3.B7`–`B12D`). If it is an asset acquisition, stop this business-combination method; allocate cost without goodwill under .2(b), and obtain the applicable asset-standard cost analysis.
2. **Identify the acquirer** (Step 1 / §2, `IFRS 3.6`–`.7`) only after a separately sourced IFRS 10 control conclusion is available; otherwise stop that conclusion and obtain the missing analysis. Check for a reverse acquisition.
3. **Determine the acquisition date** (Step 2 / §2, `IFRS 3.8`–`.9`).
4. **Build consideration transferred** at fair value (§3, `IFRS 3.37`): cash + assets + equity issued + acquisition-date fair value of contingent consideration (classified liability/equity). Strip out post-combination remuneration and settlement of pre-existing relationships.
5. **If a step acquisition**, remeasure the previously held interest to fair value; recognise the gain/loss in profit or loss or OCI as appropriate, and treat prior OCI on the basis required for a direct disposal (§3, `IFRS 3.42`).
6. **Recognise and fair-value the identifiable assets and liabilities** (Step 3 / §2, `IFRS 3.18`); apply each recognition/measurement **exception** (income tax, contingent liabilities, leases, etc.).
7. **Measure NCI** (§2, `IFRS 3.19`): apply the fair-value/proportionate-net-assets election only to eligible present ownership interests; measure other components at acquisition-date fair value unless another IFRS requires a different basis. State eligibility and the elected basis.
8. **Compute goodwill** (Step 4 / §2, `IFRS 3.32`). If negative, **reassess** (`IFRS 3.36`), then recognise any remaining **bargain-purchase gain** in P&L.
9. **Expense acquisition-related costs** as incurred (§3, `IFRS 3.53`).
10. **Book the consolidation journal entry** (base §3 format); record provisional amounts if incomplete and open the **measurement period** (§3). _(IFRS 3.45–.50)_
11. **Subsequently:** remeasure liability-classified contingent consideration through P&L unless a measurement-period adjustment applies (§3). Apply the scoped IAS 36 impairment/CGU/partial-goodwill method above with a supported valuation working paper.
12. **Produce the disclosure checklist** (§7) and **reviewer brief** with every flash point.

### Section 7  -  Disclosure checklist  -  `IFRS 3.59`–`.63`, `B64`–`B67`; separate IAS 36 handoff

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
- [ ] **Measurement-period** adjustments  -  nature and amount (`IFRS 3.B67(a)`)
- [ ] Acquiree **revenue and profit/loss** since acquisition and **supplemental pro forma** as if combined from the start of the period (`IFRS 3.B64(q)`)
- [ ] **Goodwill reconciliation** required by IFRS 3.B67(d): opening/closing gross amount and accumulated impairment, additions, disposal-group adjustments, deferred-tax adjustments, disposals, impairment losses, exchange movements and other changes, as applicable. The separate IAS 36 event/significance-triggered disclosures are described above.
- [ ] Apply the actual IAS 36 triggers before finalising: Goodwill **impairment test** disclosures: CGU/group, recoverable-amount basis (FVLCD or value in use), key assumptions, discount rate, sensitivity (`IAS 36.130`, `.134`)

### Section 8  -  Topic self-checks (in addition to base §7)

- [ ] Confirmed a **business** (concentration test considered) vs. an asset acquisition; if asset acquisition, no goodwill and applicable asset-cost analysis referred _(IFRS 3.2(b), B7–B12D)_
- [ ] **Acquirer** identified via IFRS 10 control; reverse-acquisition possibility checked
- [ ] **Acquisition date** = date control obtained, tied to `IFRS 3.8`–`.9`
- [ ] Identifiable assets/liabilities at **fair value**; each recognition/measurement **exception** applied (tax, contingent liabilities, leases, etc.) _(IFRS 3.10–.31A)_
- [ ] **NCI measurement choice** stated and justified (full vs. partial goodwill, `IFRS 3.19`); numerical effect shown
- [ ] **Consideration** at fair value; contingent consideration classified (liability/equity) and fair-valued; remuneration stripped out _(IFRS 3.37–.40, .51–.53, B50–B56)_
- [ ] **Goodwill** = consideration + NCI + prior-interest FV − identifiable net assets; arithmetic shown and balanced for each method run _(IFRS 3.32)_
- [ ] Negative residual → **reassessed** (`IFRS 3.36`), then bargain-purchase **gain to P&L**
- [ ] Acquisition-related costs **expensed**, not capitalised to goodwill _(IFRS 3.53)_
- [ ] Step acquisition → prior interest **remeasured to FV**, gain/loss to profit or loss or OCI as appropriate; prior OCI treated as on direct disposal (.42)
- [ ] **Measurement period** opened for provisional amounts; ends on receipt of sought information or learning more is unobtainable, never later than 1 year; adjustments applied **retrospectively** (`IFRS 3.49`)
- [ ] Subsequent: contingent-consideration movement distinguishes measurement-period facts from later events; IAS 36 impairment/CGU/partial-goodwill analysis documented under the recovered rules above
- [ ] Divergence from ASC 805 / ASC 350 checked for dual-reporters (NCI method, amortisation, impairment model, measurement-period treatment)


### Exceptions and scope recovered from neighbouring paragraphs

IFRS 3.2A excludes an investment entity acquisition of a subsidiary investment required to be measured at fair value through profit or loss. For IAS 37/IFRIC 21 liabilities, use the present-obligation/obligating-event tests specified in .21A-.21C; do not recognise contingent assets (.23A). The acquisition-date lessee exception permits omission of ROU/liability for leases ending within 12 months of acquisition or low-value underlying assets (.28A-.28B). Acquiree-lessor classification uses inception terms, or the relevant modification date, rather than automatically reclassifying at acquisition (.17). Insurance-contract groups and insurance-acquisition cash-flow assets follow IFRS 17 measurement (.31A), effective with IFRS 17 (.64N). Indemnity assets are subject to collectibility and contractual limits (.27-.28, .57).

Replacement awards require the B56 obligation test: if acquiree awards would expire because of the combination and the acquirer voluntarily replaces them without an obligation, the entire replacement-award measure is post-combination remuneration. Apply the B57–B62 allocation conditions separately when replacement is obligatory (B56).

For the concentration test, document B7B gross-asset definitions and exclusions (including cash/cash equivalents, deferred-tax assets and goodwill from deferred-tax liabilities), the aggregation rules for a single identifiable asset, and the similar-asset nature/risk conditions. Do not infer concentration from a headline purchase price; stop for a separately documented B7B analysis if those inputs are missing. _(IFRS 3.B7A–B7B)_

For a set without outputs the substantive-process test requires a critical process and an acquired organised workforce plus developable inputs; with outputs, apply the workforce/critical-process route or the significant-contribution plus unique/scarce/not-readily-replaceable route (B12B-B12D). An accounting acquiree must itself be a business for reverse-acquisition accounting; an acquired listed shell may instead be outside IFRS 3 (B19).

## Worked cases

All monetary amounts, rates and transaction dates below are illustrative supplied facts, not legal thresholds or prescribed yields. Keep the original whole-dollar journal displays separate from the cent-precision check.

### Worked example (illustrative)

**Acquirer** buys **80%** of **Target** for **$800,000 cash** on the acquisition date. The fair value of Target's **identifiable net assets** is **$700,000**. The acquisition-date **fair value of the 20% NCI** is **$190,000**. Assume the 20% NCI consists of present ownership interests entitling holders to a proportionate share of net assets on liquidation, so it is eligible for the .19 measurement election. The acquirer held no prior interest. Acquisition-related costs were **$25,000** (cash). IFRS 3.19 gives a **per-transaction choice**  -  both methods are shown.

**(a) Full-goodwill method  -  NCI at fair value (`IFRS 3.19(a)`):**

```
Goodwill = consideration 800,000 + NCI at FV 190,000 - identifiable net assets 700,000 = 290,000
```

```
Acquisition date  -  consolidate Target, NCI at fair value  -  driving rule: IFRS 3.32 / .19(a)
  Dr  Identifiable net assets (at fair value)     700,000
  Dr  Goodwill                                     290,000
      Cr  Cash                                          800,000
      Cr  Non-controlling interest (equity)             190,000
  (memo: goodwill = 800,000 + 190,000 - 700,000 = 290,000.
   Debits 990,000 = Credits 990,000 ✓)
```

**(b) Partial-goodwill method  -  NCI at proportionate share (`IFRS 3.19(b)`):**

```
NCI = 20% × identifiable net assets 700,000 = 140,000
Goodwill = consideration 800,000 + NCI 140,000 - identifiable net assets 700,000 = 240,000
```

```
Acquisition date  -  consolidate Target, NCI at proportionate share  -  driving rule: IFRS 3.32 / .19(b)
  Dr  Identifiable net assets (at fair value)     700,000
  Dr  Goodwill                                     240,000
      Cr  Cash                                          800,000
      Cr  Non-controlling interest (equity)             140,000
  (memo: goodwill = 800,000 + 140,000 - 700,000 = 240,000.
   Debits 940,000 = Credits 940,000 ✓)
```

The two recorded amounts differ by **$50,000** (290,000 − 240,000), arising from the supplied NCI fair value versus the proportionate net-asset share. This difference is not itself an IAS 36 notional gross-up calculation; apply the separate CGU/parent/NCI analysis above. The current US comparison remains reserved below.

```
Acquisition date  -  acquisition-related costs  -  driving rule: IFRS 3.53
  Dr  Acquisition expense (P&L)                     25,000
      Cr  Cash                                           25,000
  (memo: advisory + legal expensed as incurred, not capitalised to goodwill; debits = credits ✓)
```

**Step-acquisition note.** Suppose the acquirer previously held 10% of Target carried at $60,000 with an acquisition-date fair value of $95,000, then buys a further 70% giving control. Assume the prior interest is an equity-method investment whose remeasurement is recognised in profit or loss. Remeasure the prior interest to $95,000, booking a **$35,000 gain to P&L** (`IFRS 3.42`):

```
Acquisition date  -  remeasure previously held interest  -  driving rule: IFRS 3.42
  Dr  Investment in Target (equity interest)         35,000
      Cr  Gain on remeasurement of prior interest (P&L)  35,000
  (memo: 95,000 FV - 60,000 carrying amount = 35,000; debits = credits ✓)
```

The $95,000 remeasured fair value then enters the goodwill formula as the "previously held equity interest" term.

**Contingent-consideration note.** Suppose the deal also includes an **earn-out** with an acquisition-date fair value of **$120,000**, classified as a **financial liability** under `IAS 32`. It is part of consideration (increasing goodwill), remeasured each period through P&L:

```
Acquisition date  -  recognise contingent consideration  -  driving rule: IFRS 3.39
  Dr  Goodwill                                      120,000
      Cr  Contingent consideration liability            120,000
  (memo: earn-out at acquisition-date fair value; financial liability per IAS 32; debits = credits ✓)

Subsequent period  -  fair value rises to 150,000  -  driving rule: IFRS 3.58(b)
  Dr  Fair value loss on contingent consideration (P&L)  30,000
      Cr  Contingent consideration liability                  30,000
  (memo: 150,000 - 120,000 = 30,000 through P&L, NOT goodwill; debits = credits ✓)
```

**⚑ AUDIT FLASH POINT  -  the NCI election requires an impairment handoff.** Document the recovered IAS 36 partial-goodwill/CGU analysis above and recover the current US rule before quantifying any dual-reporting adjustment.

```oa-check
name: Existing acquisition, compare eligible full and partial goodwill
inputs:
  consideration: 800000
  nci_fair_value: 190000
  identifiable_net_assets: 700000
  nci_fraction: 0.2
  costs: 25000
steps:
  - full_goodwill: consideration + nci_fair_value - identifiable_net_assets
  - partial_nci: nci_fraction * identifiable_net_assets
  - partial_goodwill: consideration + partial_nci - identifiable_net_assets
  - difference: full_goodwill - partial_goodwill
  - cash_outflow: consideration + costs
expected:
  full_goodwill: 290000
  partial_nci: 140000
  partial_goodwill: 240000
  difference: 50000
  cash_outflow: 825000
```

The preserved step-acquisition variant assumes the $800,000 is consideration for the further 70% purchased, in addition to the previously held 10%. With prior-interest fair value $95,000, carrying amount $60,000, NCI $190,000 and the same $700,000 recognised net assets, goodwill is $385,000 and, assuming the prior interest is an equity-method investment, the remeasurement gain in profit or loss is $35,000. Adding a separate acquisition-date liability earn-out of $120,000 increases goodwill to $505,000; its later increase to $150,000 produces a $30,000 loss if caused by post-acquisition performance, not new acquisition-date information. The variants are not additions to the original 80%-purchase case (IFRS 3.32, .39-.42, .58).

```oa-check
name: Step acquisition with an earn-out and later fair-value loss
inputs:
  new_cash: 800000
  prior_fv: 95000
  prior_book: 60000
  nci_fv: 190000
  net_assets: 700000
  initial_earnout: 120000
  later_earnout: 150000
steps:
  - prior_gain: prior_fv - prior_book
  - goodwill_before_earnout: new_cash + prior_fv + nci_fv - net_assets
  - goodwill_with_earnout: goodwill_before_earnout + initial_earnout
  - later_loss: later_earnout - initial_earnout
expected:
  prior_gain: 35000
  goodwill_before_earnout: 385000
  goodwill_with_earnout: 505000
  later_loss: 30000
```

## When to refuse or refer

Refuse a final recognition, classification, valuation or disclosure conclusion when required contracts, applicable reporting period, adoption facts or supporting standards are missing. Refer significant valuations, enforceability, control, impairment and complex settlement terms to a qualified reporting specialist. Return the facts, paragraph-by-paragraph reasoning, balanced journals, reconciliation and open items to the reviewer. Do not issue audit or assurance language. Any topic reserved below remains outside usable instructions until its operative primary source is recovered.


### Original professional disclaimer

Provides computational and interpretive guidance on IFRS 3 / IAS 36 only. Not an audit and not assurance. Business-combination accounting turns heavily on entity-specific facts and significant judgement  -  fair-value measurement of intangibles and contingent consideration, identification of the acquirer, the business-vs-asset determination, the NCI measurement election, and goodwill impairment all require specialist input. Have outputs reviewed and signed by a qualified accountant before they are reflected in financial statements relied upon by third parties.

## Sources

| Source | Official URL | Actual read scope and date |
|---|---|---|
| IFRS 3 Business Combinations | [IFRS 3 Business Combinations](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs3.html) | Read for .2-.64R, B7-B41, B50-B56, B62A-B67 in the official 2026-issued copy retrieved 2026-11-14, personally read 2026-11-15; official body retrieved again and reconciled 2026-11-16; existing read scope retained  Adjacent E17/E18 agenda-decision text personally read in full on 2026-11-16 for continuing-employment and non-substantive-service qualification; decisions are explanatory material, not a new amendment. |
| Supporting IAS36 | [IAS36](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ias36.html) | Retrieved and personally read 2026-11-16: .9-.10, .18-.22, .30-.57, .74-.105, .110-.125, .130/.133-.135 and C1-C9 with neighboring qualifications; scoped coverage, not all supporting execution. |
| Supporting IAS38 | [IAS38](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ias38.html) | Retrieved and personally read 2026-11-16: .33-.35, .42-.44, .54-.67, .88-.97, .107-.110 and .112-.117 with neighboring qualifications; scoped coverage, not all supporting execution. |
| Supporting IFRS10 | [IFRS10](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs10.html) | Retrieved and personally read 2026-11-16: .4-.18, .31-.33 and C1-C1A with neighboring qualifications; scoped coverage, not all supporting execution. |
| Current US comparison | [Authoritative ASC](https://asc.fasb.org/) | Attempted again 2026-11-16; official ASC web pages returned 0 readable lines. Current operative Codification not read; historical recovery limits remain in external evidence. |

Not yet confirmed: jurisdiction-specific endorsement and entity-specific early adoption; all individually retained source-limited items below. These boundaries are not accountant approval.

#### Not yet confirmed: individual current US comparisons and supporting execution

Current ASC web recovery returned 0 readable operative lines on 16 November. Each former comparison needs its actual current ASC rule and conditions before use:

| Original topic | Specific unresolved US-dependent conclusion |
| --- | --- |
| NCI measurement | ASC 805 fair-value requirement and any applicable exceptions versus the eligible IFRS election. |
| Goodwill amortisation | Current private-company/NFP alternative, the old **10-year** maximum and triggering-event testing; not an IFRS option. |
| Impairment unit | Current US reporting-unit definition, including the old operating-segment-or-1-level-below comparison. |
| Impairment measure | Current US single-step carrying-value/fair-value test, goodwill cap and ASU 2017-04 application. |
| Reversals | Current US goodwill and other-asset prohibitions/qualifications versus the separately supported IAS 36 rules. |
| Definition of a business | Current ASC screen/framework and ASU 2017-01 compared with IFRS's optional concentration test; do not presume complete convergence. |
| Contingent liabilities | Current ASC fair-value/ASC 450 fallbacks versus IFRS's specified acquisition-date present-obligation rule. |
| Contract assets/liabilities | Current ASC 606 exception communicated by ASU 2021-08 and its scope/transition versus IFRS .18 and applicable exceptions. |
| Contingent consideration | Current ASC classification/remeasurement; do not assume all outcomes match. |
| Acquisition costs | Current ASC expense/issuance-cost rules and exceptions versus IFRS .53. |
| Measurement period | Current ASC treatment under ASU 2015-16, including current-period adjustment/prior-period effects; do not infer current applicability solely from the amendment PDF. |

The IFRS 10 basic control clauses and the stated IAS 36/IAS 38 rules are recovered. Complex control/principal-agent/consolidation execution, IFRS 13 valuation, IAS 12 tax recognition, IAS 19 benefits, IFRS 2 award measurement and IFRS 5 held-for-sale execution still require their transaction-specific supporting analysis. The IFRS 3 exceptions above are supported as referrals; they do not themselves execute those other Standards.
