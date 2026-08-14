---
name: ifrs15-revenue
description: IFRS revenue recognition under IFRS 15 (Revenue from Contracts with Customers) and the related contract-cost guidance within IFRS 15. Covers the five-step model — identify the contract, identify performance obligations, determine the transaction price, allocate it, and recognise revenue as or when obligations are satisfied — plus variable consideration and the constraint, significant financing components, principal-versus-agent, licences, contract modifications, contract assets and liabilities, and the costs of obtaining and fulfilling a contract. Produces recognition conclusions, journal entries, and a reviewer brief. Issued as the IFRS edition of the revenue topic; see us-gaap-asc606-revenue for the US GAAP edition. MUST load alongside financial-reporting-workflow-base.
version: 0.1
jurisdiction: GLOBAL
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on:
  - financial-reporting-workflow-base
category: financial-reporting
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Ifrs15 Revenue

## IFRS Revenue — IFRS 15 v0.1

## What this file is

**This is a content skill that loads on top of `financial-reporting-workflow-base`.** It supplies the recognition, measurement, presentation, and disclosure rules for revenue from contracts with customers under IFRS. The base supplies the two-layer output contract, the journal-entry format, and the self-checks.

- **Standard currency** — IFRS 15 as effective for annual periods beginning on or after 1 January 2018, including *Clarifications to IFRS 15* (April 2016). No subsequent amendment has displaced the five-step core.  _(IFRS 15)_
- **Scope** — IFRS 15 applies to contracts with customers except: leases (IFRS 16), insurance contracts (IFRS 17), financial instruments and other contractual rights/obligations in IFRS 9 / IFRS 10 / IFRS 11 / IAS 27 / IAS 28, and certain non-monetary exchanges between entities in the same line of business to facilitate sales to customers.  _(IFRS 15.5)_

## Section 1 — Scope statement

This skill covers:

- The five-step model of IFRS 15.
- Variable consideration and the constraint; significant financing components; non-cash consideration; consideration payable to a customer.
- Principal vs. agent, licences of IP, warranties, customer options (material rights), bill-and-hold, repurchase agreements, consignment.
- Contract modifications.
- Presentation of contract assets, contract liabilities, and refund liabilities.
- Incremental costs of obtaining a contract and costs to fulfil (`IFRS 15.91`–`104`).

This skill does NOT cover: lease income (`IFRS 16`), interest/dividend income (`IFRS 9`/`IAS 18`-legacy superseded), insurance (`IFRS 17`). It defers the US GAAP treatment to `us-gaap-asc606-revenue`.

## Section 2 — Reference layer (Layer A): the five-step model

### Step 1 — Identify the contract — `IFRS 15.9`–`16`

- **Contract identification criteria** — A contract with a customer is in scope when **all five** criteria are met: 1. The parties have **approved** the contract and are committed to perform. 2. Each party's **rights** are identifiable. 3. **Payment terms** are identifiable. 4. The contract has **commercial substance**. 5. It is **probable** the entity will collect the consideration it is entitled to. Under IFRS, **"probable" = more likely than not** — a **lower** threshold than US GAAP's "likely."  _(IFRS 15.9)_
- **Criteria not met treatment** — If criteria are not met, consideration received is recognised as a **liability** until the criteria are met or the `15.15` release events occur.  _(IFRS 15.15)_
- **Combine contracts** — Combine contracts with the same customer (or related parties) entered into at/near the same time when negotiated as a package, consideration is interdependent, or the goods/services form a single performance obligation.  _(IFRS 15.17)_

> **⚑ AUDIT FLASH POINT — collectibility threshold differs from US GAAP.** The IFRS bar to *have a contract* is lower. A US-GAAP-trained reviewer may wrongly defer revenue. Document the "more likely than not" assessment.

### Step 2 — Identify the performance obligations — `IFRS 15.22`–`30`

- **Performance obligation** — A performance obligation is a promise to transfer a **distinct** good/service or a **series** of distinct goods/services that are substantially the same and have the same pattern of transfer.  _(IFRS 15.22)_
- **Distinct criteria** — Distinct requires **both**: **Capable of being distinct** — the customer can benefit from it on its own or with readily available resources; and **Distinct within the context of the contract** — separately identifiable; the entity is not providing a significant integration service, the good does not significantly customise/modify another, and it is not highly interdependent/interrelated.  _(IFRS 15.27; IFRS 15.29)_

### Step 3 — Determine the transaction price — `IFRS 15.46`–`72`

- **Transaction price** — Transaction price = consideration the entity expects to be **entitled to**, excluding amounts collected on behalf of third parties.  _(IFRS 15.46)_
- **Variable consideration** — Estimate using **expected value** or **most likely amount**.  _(IFRS 15.50–54)_
- **The constraint** — Include only to the extent **highly probable** that a significant reversal will not occur. *(IFRS uses "highly probable"; US GAAP uses "probable" — wording differs, intended threshold is the same.)*  _(IFRS 15.56–58)_
- **Significant financing component** — Adjust for time value of money where significant. Practical expedient: ignore if ≤ 1 year between transfer and payment.  _(IFRS 15.60–65; IFRS 15.63)_
- **Non-cash consideration** — Measure at **fair value**; if fair value cannot be reasonably estimated, measure by reference to the standalone selling price.  _(IFRS 15.66–69)_
- **Consideration payable to a customer** — Reduction of transaction price unless for a distinct good/service.  _(IFRS 15.70–72)_

> **⚑ AUDIT FLASH POINT — non-cash consideration measurement date.** IFRS measures non-cash consideration at fair value (with a fallback to SSP) and the measurement-date approach can differ from ASC 606's "contract inception" rule. Flag for dual-reporters.

### Step 4 — Allocate the transaction price — `IFRS 15.73`–`90`

- **Allocation by SSP** — Allocate to each PO by **standalone selling price**; estimate SSP where not observable (adjusted market assessment, expected cost plus margin, or residual approach with the `15.79` restrictions). Allocate discounts (`15.81`–`83`) and variable consideration (`15.84`–`86`) to specific POs where the criteria are met.  _(IFRS 15.76; IFRS 15.79; IFRS 15.81–83; IFRS 15.84–86)_

### Step 5 — Recognise revenue when/as a PO is satisfied — `IFRS 15.31`–`45`

- **Recognition trigger** — Recognise revenue when the entity transfers **control** of the good/service.  _(IFRS 15.31)_
- **Over time criteria** — **Over time** if **any one** of three criteria is met: 1. The customer **simultaneously receives and consumes** benefits as the entity performs; or 2. Performance **creates or enhances an asset the customer controls**; or 3. Performance does **not create an asset with alternative use** and the entity has an **enforceable right to payment** for performance to date.  _(IFRS 15.35)_
- **Measuring progress** — If over time, **measure progress** by output or input method; if progress cannot be reasonably measured but costs are recoverable, recognise revenue only to the extent of costs.  _(IFRS 15.39–45; IFRS 15.45)_
- **Point in time indicators** — **Point in time** otherwise — recognise when control transfers, using indicators in `15.38` (present right to payment, legal title, physical possession, risks and rewards, acceptance).  _(IFRS 15.38)_

## Section 3 — Reference layer: high-frequency special topics

- **Principal vs. agent** — Principal **controls** the good/service before transfer → **gross**; agent → **net** (fee/commission). Same indicators as US GAAP.  _(IFRS 15.B34–B38)_
- **Licences of IP** — **Right to access** (IP changes over the period) → **over time**; **right to use** (IP as it exists when granted) → **point in time**. Sales/usage-based **royalty exception**: recognise at the later of the subsequent sale/usage or satisfaction of the PO.  _(IFRS 15.B52–B63; IFRS 15.B63)_
- **Warranties** — Assurance-type → provision under `IAS 37`, not a PO; service-type → separate PO.  _(IFRS 15.B28–B33)_
- **Customer options / material rights** — A material right is a separate PO.  _(IFRS 15.B39–B43)_
- **Contract modifications** — Separate contract if distinct goods at SSP; otherwise prospective (if remaining goods distinct) or cumulative catch-up (if not).  _(IFRS 15.18–21)_

## Section 4 — Reference layer: contract costs — `IFRS 15.91`–`104`

- **Incremental costs of obtaining a contract** — Recognised as an **asset** if expected to be recovered. Practical expedient: expense if amortisation period ≤ 1 year.  _(IFRS 15.91; IFRS 15.94)_
- **Costs to fulfil a contract** — Costs to fulfil a contract (not in another standard) are capitalised if they relate directly to a contract, generate/enhance resources, and are expected to be recovered.  _(IFRS 15.95)_
- **Amortisation and impairment** — **Amortise** consistent with transfer of goods/services; test for impairment.  _(IFRS 15.99–104)_

## Section 5 — Presentation — `IFRS 15.105`–`109`

- **Contract liability** — Consideration received/due before transfer of goods/services.  _(IFRS 15.105–109)_
- **Contract asset** — Right to consideration for goods/services transferred, conditional on something other than the passage of time. Once unconditional → **receivable** (in scope of `IFRS 9` for impairment).  _(IFRS 15.105–109)_
- **Refund liability** — Refund liability plus an **asset for the right to recover** returned goods.  _(IFRS 15.105–109)_

## Section 6 — Executable layer (Layer B): the procedure

Identical procedure to the US GAAP edition (base §1, two layers), citing IFRS 15 paragraphs:

0. **Confirm a contract exists** — Confirm a contract exists (`15.9`); if collectibility (more-likely-than-not) fails, book a liability and stop.
0. **List promises → POs** — List promises → POs (`15.22`–`30`); document distinct analysis; flag series, material rights, warranties.
0. **Build the transaction price** — Build the transaction price (`15.46`–`72`): fixed + constrained variable; significant financing component; non-cash at fair value; net consideration payable.
0. **Determine SSP and allocate** — Determine SSP and allocate (`15.73`–`90`); show the table.
0. **Timing per PO** — Timing per PO (`15.31`–`45`): over time (criterion + progress measure) or point in time (control indicators).
0. **Principal/agent for third-party promises** — Principal/agent for third-party promises (`B34`–`B38`) → gross/net.
0. **Recognise revenue; book journal entries** — Recognise revenue; book **journal entries** (base §3) day 1 + subsequent.
0. **Capitalise/amortise contract costs** — Capitalise/amortise contract costs (`15.91`–`104`).
0. **Classify balances** — Classify balances (`15.105`–`109`).
0. **Disclosure checklist + reviewer brief** — Disclosure checklist (§8) + **reviewer brief** with every flash point.

### Worked example (illustrative)

Same SaaS facts as the US GAAP edition ($24,000 subscription + $6,000 non-distinct setup, paid upfront, 24-month delivery). Single combined PO, over time under `15.35(a)`, straight-line.

```
Day 1 — driving rule: IFRS 15.106 (contract liability)
  Dr  Cash                                   30,000
      Cr  Contract liability                       30,000
  (memo: single combined PO; no revenue at inception)

Each month (×24) — driving rule: IFRS 15.35(a)
  Dr  Contract liability                       1,250
      Cr  Revenue                                    1,250
  (memo: 30,000 / 24; debits = credits ✓)

Day 1 — incremental cost to obtain — driving rule: IFRS 15.91
  Dr  Contract cost asset                      3,000
      Cr  Cash                                       3,000

Each month (×24) — amortise — driving rule: IFRS 15.99
  Dr  Amortisation expense                       125
      Cr  Contract cost asset                          125
```

> **⚑ AUDIT FLASH POINT — same combine/separate judgement as US GAAP.** The distinct conclusion drives timing identically; evidence the integration analysis.

## Section 7 — Divergence from US GAAP (ASC 606)

**IFRS 15 vs US GAAP (ASC 606) divergence table**  _(IFRS 15 / ASC 606 comparison)_

| Area | IFRS 15 | US GAAP (ASC 606) |
| --- | --- | --- |
| Collectibility threshold (Step 1) | "Probable" = **more likely than not** (lower bar) | "Probable" = **likely** (higher bar) |
| Constraint wording | "Highly probable" | "Probable" (same intended threshold) |
| Shipping & handling | **No** policy election — assess as promised service | Policy election to treat as fulfillment activity |
| Immaterial promised goods/services | No explicit relief; general materiality | Explicit relief to disregard (`606-10-25-16A`) |
| Non-cash consideration | Fair value, fallback to SSP; measurement-date guidance differs | Fair value at contract inception |
| Licensing renewals & sales-based royalties | Minor application differences | Minor application differences |
| Interim disclosures | IAS 34 | US public-entity interim regime |
| Reversal of impairment of contract cost assets | **Permitted** (consistent with IFRS) | **Prohibited** (US GAAP generally bars reversal) |

Run `us-gaap-asc606-revenue` in parallel for dual-reporters and present both answers (base §2).

## Section 8 — Disclosure checklist — `IFRS 15.110`–`129`

- **Disclosure checklist** — - [ ] Disaggregation of revenue (`114`–`115`) - [ ] Contract balances and movements; revenue recognised from opening contract liabilities (`116`–`118`) - [ ] Performance obligations: nature, timing, significant payment terms (`119`) - [ ] Transaction price allocated to remaining POs (backlog) and timing (`120`–`122`) - [ ] Significant judgements: timing of satisfaction; determining/allocating transaction price (`123`–`126`) - [ ] Contract cost assets: closing balances and amortisation (`127`–`128`) - [ ] Practical expedients used (`129`)  _(IFRS 15.110–129)_

## Section 9 — Topic self-checks (in addition to base §7)

- [ ] All five steps applied in order; each conclusion cites its IFRS 15 paragraph
- [ ] Collectibility assessed on the **more-likely-than-not** basis (not US GAAP "likely")
- [ ] Distinct analysis documented per PO
- [ ] Variable consideration estimated and constrained ("highly probable"); method stated
- [ ] Significant financing component assessed (or expedient) for timing > 1 yr
- [ ] SSP allocation table shown
- [ ] Over-time vs. point-in-time tied to a `15.35` criterion or control indicator
- [ ] Principal/agent resolved → gross/net
- [ ] Contract costs capitalised/amortised per `15.91`–`104`; impairment (and any reversal) considered
- [ ] Balances classified: contract asset vs. receivable vs. contract liability vs. refund liability
- [ ] Divergence from ASC 606 checked for dual-reporters

## Section 10 — Disclaimer

Provides computational and interpretive guidance on IFRS 15 only. Not an audit and not assurance. Revenue recognition turns heavily on entity-specific facts and significant judgement. Have outputs reviewed and signed by a qualified accountant before they are reflected in financial statements relied upon by third parties.

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
