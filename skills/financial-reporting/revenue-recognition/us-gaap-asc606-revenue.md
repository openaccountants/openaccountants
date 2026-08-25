---
name: us-gaap-asc606-revenue
description: US GAAP revenue recognition under ASC 606 (Revenue from Contracts with Customers) and the related contract-cost guidance in ASC 340-40. Covers the five-step model — identify the contract, identify performance obligations, determine the transaction price, allocate it, and recognize revenue as or when obligations are satisfied — plus variable consideration and the constraint, significant financing components, principal-versus-agent, licenses, contract modifications, contract assets and liabilities, and the cost-to-obtain and cost-to-fulfill rules. Produces recognition conclusions, journal entries, and a reviewer brief. Issued as the US GAAP edition of the revenue topic; see ifrs15-revenue for the IFRS edition. MUST load alongside financial-reporting-workflow-base.
version: 0.1
jurisdiction: US
tax_year: 2025
last_updated: 2026-07-13
reviewed_by: James Wallach
review_status: current
depends_on:
  - financial-reporting-workflow-base
category: financial-reporting
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# US GAAP Asc606 Revenue

## US GAAP Revenue — ASC 606 v0.1

## What this file is

**This is a content skill that loads on top of `financial-reporting-workflow-base`.** It supplies the recognition, measurement, presentation, and disclosure rules for revenue from contracts with customers under US GAAP. The base supplies the two-layer output contract, the journal-entry format, and the self-checks.

- **Standard currency** — ASC 606 and ASC 340-40 as effective for all entities (public business entities since annual periods beginning after 15 Dec 2017; all others after 15 Dec 2018). No subsequent ASU has displaced the five-step core. Confirm no entity-specific industry guidance (e.g. ASC 924, 942, 944, 980) overrides.  _(ASC 606; ASC 340-40)_
- **Scope exclusions** — ASC 606 applies to contracts with customers except: leases (ASC 842), insurance (ASC 944), financial instruments (ASC 310, 320, 815, 825, 860), guarantees other than product/service warranties (ASC 460), and certain non-monetary exchanges between entities in the same line of business to facilitate sales to customers.  _(ASC 606-10-15-2)_

## Section 1 — Scope statement

This skill covers:

- The five-step model of `ASC 606-10-25` and `-32`.
- Variable consideration and the constraint; significant financing components; noncash consideration; consideration payable to a customer.
- Principal vs. agent (gross vs. net), licenses of IP, warranties, options for additional goods/services (material rights), bill-and-hold, repurchase agreements, consignment.
- Contract modifications.
- Presentation of contract assets, contract liabilities (deferred revenue), and refund liabilities.
- Incremental costs to obtain a contract and costs to fulfill under `ASC 340-40`.

This skill does NOT cover: lease revenue (`ASC 842`), interest/dividend income (`ASC 310`/`325`), insurance (`ASC 944`), or collaborative arrangements outside the customer relationship (`ASC 808`). It defers the IFRS treatment to `ifrs15-revenue`.

## Section 2 — Reference layer (Layer A): the five-step model

### Step 1 — Identify the contract — `ASC 606-10-25-1` to `25-8`

- **Five criteria for a contract to exist** — A contract exists when **all five** criteria are met: 1. Parties have **approved** the contract and are committed to perform. 2. Each party's **rights** to goods/services are identifiable. 3. **Payment terms** are identifiable. 4. The contract has **commercial substance**. 5. It is **probable** the entity will collect the consideration it is entitled to (a *collectibility* gate). "Probable" under US GAAP = **likely to occur** (a higher threshold than IFRS's "probable").  _(ASC 606-10-25-1 to 25-8)_
- **Criteria not met — deposit liability** — If the criteria are not met, no revenue; consideration received is a deposit liability until criteria are met or the release events occur (contract terminated and consideration non-refundable, or no remaining obligations and substantially all consideration received).  _(ASC 606-10-25-7)_
- **Combine contracts** — Combine contracts entered into at/near the same time with the same customer when they are negotiated as a package, consideration in one depends on the other, or the goods/services are a single performance obligation.  _(ASC 606-10-25-9)_

> **⚑ AUDIT FLASH POINT — collectibility gate.** Step 1 collectibility is assessed at the *customer* level on the consideration the entity expects to be entitled to (it may reflect an intention to offer a price concession, which is variable consideration, not a collectibility failure). Misusing Step 1 to defer revenue for a credit-risky customer when the real issue is a concession is a common error.

### Step 2 — Identify the performance obligations — `ASC 606-10-25-14` to `25-22`

- **Performance obligation (PO)** — A promise to transfer a **distinct** good/service, or a **series** of distinct goods/services that are substantially the same and have the same pattern of transfer.  _(ASC 606-10-25-14 to 25-22)_
- **Distinct — two conditions** — A good/service is **distinct** when both: **Capable of being distinct** — the customer can benefit from it on its own or with readily available resources (`25-19`); and **Distinct within the context of the contract** — the promise is separately identifiable, i.e. the entity is not providing a significant integration service, the item does not significantly modify/customize another, and it is not highly interdependent/interrelated with other promises (`25-21`).  _(ASC 606-10-25-19; 25-21)_
- **Not distinct — combine** — If not distinct, combine with other goods/services until a distinct bundle is identified.  _(ASC 606-10-25-14 to 25-22)_

> **⚑ AUDIT FLASH POINT — bundling/unbundling.** Whether implementation, setup, or customization is a separate PO or is bundled with a license/SaaS drives the timing of large amounts. Document the integration / interdependence analysis.

### Step 3 — Determine the transaction price — `ASC 606-10-32-2` to `32-27`

- **Transaction price** — Consideration the entity expects to be **entitled to** in exchange for transferring goods/services, excluding amounts collected for third parties (e.g. sales taxes).  _(ASC 606-10-32-2 to 32-27)_
- **Variable consideration** — Discounts, rebates, refunds, credits, price concessions, incentives, performance bonuses, penalties, returns. Estimate using **expected value** (probability-weighted) or **most likely amount**, whichever better predicts.  _(ASC 606-10-32-5 to 32-9)_
- **The constraint** — Include variable consideration only to the extent it is **probable** that a significant reversal will **not** occur when the uncertainty resolves. Factors that increase reversal risk: susceptibility to factors outside the entity's influence, long time to resolution, limited experience, broad range of outcomes.  _(ASC 606-10-32-11 to 32-13)_
- **Significant financing component** — Adjust for the time value of money when timing gives the customer/entity a significant financing benefit. Practical expedient: ignore if the period between transfer and payment is ≤ 1 year.  _(ASC 606-10-32-15 to 32-20)_
- **Noncash consideration** — Measure at fair value at contract inception.  _(ASC 606-10-32-21 to 32-24)_
- **Consideration payable to a customer** — A reduction of transaction price unless it is payment for a distinct good/service received (then account for as a purchase).  _(ASC 606-10-32-25 to 32-27)_

### Step 4 — Allocate the transaction price — `ASC 606-10-32-28` to `32-41`

- **Allocation basis** — Allocate to each PO in proportion to **standalone selling prices (SSP)** (`32-31`). If SSP is not observable, **estimate** it (adjusted market assessment, expected cost plus margin, or residual approach — residual only if the price is highly variable/uncertain, `32-34`).  _(ASC 606-10-32-31; 32-34)_
- **Discount allocation** — Allocate a **discount** to the PO(s) to which it relates if the criteria in `32-37` are met; otherwise pro-rata to all POs.  _(ASC 606-10-32-37)_
- **Variable consideration allocation** — Allocate **variable consideration** entirely to one PO (or distinct good in a series) if the `32-40` criteria are met.  _(ASC 606-10-32-40)_

### Step 5 — Recognize revenue when/as a PO is satisfied — `ASC 606-10-25-23` to `25-37`

- **Control** — Recognize revenue when the entity transfers **control** of the good/service to the customer. Control = ability to direct the use of, and obtain substantially all the remaining benefits from, the asset.  _(ASC 606-10-25-23 to 25-37)_
- **Over time criteria** — **Over time** if **any one** of three criteria is met: 1. The customer **simultaneously receives and consumes** the benefits as the entity performs (routine/recurring services); or 2. The entity's performance **creates or enhances an asset the customer controls** as it is created; or 3. Performance does **not create an asset with alternative use** to the entity **and** the entity has an **enforceable right to payment** for performance completed to date (incl. reasonable margin).  _(ASC 606-10-25-27)_
- **Measuring progress over time** — If over time, **measure progress** with an output method (units, milestones, value transferred) or input method (costs incurred, labor hours), applied consistently. If progress cannot be reasonably measured but costs are recoverable, recognize revenue only to the extent of costs.  _(ASC 606-10-25-31 to 25-37; 25-36)_
- **Point in time indicators** — **Point in time** otherwise — recognize when control transfers, using indicators: present right to payment, legal title, physical possession, risks and rewards of ownership, customer acceptance.  _(ASC 606-10-25-30)_

## Section 3 — Reference layer: high-frequency special topics

- **Principal vs. agent** — The entity is **principal** if it controls the good/service before transfer (indicators: primary responsibility for fulfillment, inventory risk, discretion in pricing). Principal recognizes **gross**; agent recognizes **net** (the fee/commission). This is the single most common gross-vs-net dispute.  _(ASC 606-10-55-36 to 55-40)_
- **Licenses of IP** — **Right to access** IP as it exists throughout the license period → **over time**; **right to use** IP as it exists at the point in time the license is granted → **point in time**. Sales/usage-based royalties on licenses of IP: recognize at the **later** of the subsequent sale/usage or satisfaction of the PO (the royalty exception).  _(ASC 606-10-55-54 to 55-65; 55-65)_
- **Warranties** — Assurance-type warranty → `ASC 460` cost accrual, not a PO; service-type warranty → a separate PO.  _(ASC 606-10-55-30 to 55-35)_
- **Customer options / material rights** — An option that gives a material right (discount the customer would not otherwise get) is a separate PO; allocate consideration to it.  _(ASC 606-10-55-41 to 55-45)_
- **Contract modifications** — Separate contract if it adds distinct goods/services at SSP; otherwise, if remaining goods are distinct → **prospective** (treat as termination + new contract); if not distinct → **cumulative catch-up**.  _(ASC 606-10-25-10 to 25-13)_

## Section 4 — Reference layer: contract costs — `ASC 340-40`

- **Incremental costs to obtain** — Incremental costs to obtain a contract (e.g. sales commissions) are **capitalized** if expected to be recovered. Practical expedient: expense if the amortization period would be ≤ 1 year.  _(ASC 340-40-25-1; 340-40-25-4)_
- **Costs to fulfill** — Costs to fulfill a contract are capitalized if they relate directly to a contract, generate/enhance resources used to satisfy POs, and are expected to be recovered, and are not in another standard's scope.  _(ASC 340-40-25-5)_
- **Amortization** — Amortize on a systematic basis consistent with the transfer of the related goods/services; review for impairment.  _(ASC 340-40-35)_

## Section 5 — Presentation — `ASC 606-10-45`

- **Contract liability (deferred revenue)** — Consideration received/due before the entity transfers goods/services.  _(ASC 606-10-45)_
- **Contract asset** — The entity's right to consideration in exchange for goods/services already transferred, when that right is conditional on something other than the passage of time. Once unconditional → **receivable**.  _(ASC 606-10-45)_
- **Refund liability** — Consideration the entity expects to refund (e.g. expected returns); paired with an **asset for the right to recover returned goods** at former carrying amount less recovery costs.  _(ASC 606-10-45)_

## Section 6 — Executable layer (Layer B): the procedure

Run these steps on the transaction's facts. Each cites the Layer A rule it executes.

1. **Confirm a contract exists** (Step 1 / §2). If the collectibility gate fails, book consideration received as a deposit liability and stop.
2. **List the promises and group into POs** (Step 2 / §2). Document the distinct analysis for each. Identify any series, material rights, warranties.
3. **Build the transaction price** (Step 3 / §2): fixed + constrained variable consideration; adjust for any significant financing component; measure noncash at fair value; net consideration payable to the customer.
4. **Determine SSP for each PO and allocate** (Step 4 / §2). Show the allocation table.
5. **For each PO, determine timing** (Step 5 / §2): over time (which criterion + progress measure) or point in time (control indicators).
6. **Resolve principal/agent for any third-party-involved promise** (§3) → gross or net.
7. **Recognize revenue** per timing; book **journal entries** (base §3 format) at day 1 and each subsequent period.
8. **Capitalize and amortize contract costs** (§4).
9. **Classify balances** (§5): contract asset / receivable / contract liability / refund liability.
10. **Produce the disclosure checklist** (§8) and **reviewer brief** with every flash point.

### Worked example (illustrative)

SaaS provider sells a 24-month subscription for $24,000 paid upfront, plus a one-time setup/implementation service priced at $6,000. Setup is not capable of being used without the subscription and involves significant integration → **not distinct** → combine into a single PO delivered over the 24-month period (Step 2, `25-21`). Transaction price = $30,000, no variable consideration, no significant financing component (paid upfront for a service delivered evenly; expedient not needed but TVM benefit assessed and deemed not significant). Over time under criterion 1 (customer simultaneously receives/consumes), straight-line progress.

```
Day 1 — cash received, nothing yet transferred — driving rule: ASC 606-10-45 (contract liability)
  Dr  Cash                                   30,000
      Cr  Contract liability (deferred rev)        30,000
  (memo: single combined PO, $30,000; no revenue recognized at inception)

Each month (×24) — performance over time — driving rule: ASC 606-10-25-27(a), straight-line progress
  Dr  Contract liability (deferred rev)        1,250
      Cr  Revenue                                    1,250
  (memo: 30,000 / 24 = 1,250 per month; debits = credits ✓)

Day 1 — sales commission of $3,000, recovery expected — driving rule: ASC 340-40-25-1
  Dr  Capitalized contract cost (asset)        3,000
      Cr  Cash                                       3,000
  (memo: incremental cost to obtain; amortization period 24 mo > 1 yr, so capitalize)

Each month (×24) — amortize cost — driving rule: ASC 340-40-35-1
  Dr  Amortization of contract cost (expense)    125
      Cr  Capitalized contract cost (asset)            125
  (memo: 3,000 / 24 = 125; consistent with revenue pattern)
```

> **⚑ AUDIT FLASH POINT — combine vs. separate the setup PO.** If setup were instead judged *distinct*, $6,000 would (after SSP allocation) be recognized at a point in time on go-live, accelerating revenue. The integration/interdependence conclusion must be evidenced.

## Section 7 — Divergence from IFRS 15

ASC 606 and IFRS 15 share the five-step model and converge on most outcomes. Known divergences a dual-reporter must check:

**Divergence from IFRS 15 table**  _(ASC 606; IFRS 15)_

| Area | US GAAP (ASC 606) | IFRS (IFRS 15) |
| --- | --- | --- |
| Collectibility threshold (Step 1) | "Probable" = **likely** (higher bar) | "Probable" = **more likely than not** (lower bar) — `IFRS 15.9(e)` |
| Licenses — sales/usage royalty exception | Applies to licenses of IP only | Same, but interaction with other guidance differs in edge cases |
| Shipping & handling | Policy election to treat as a fulfillment activity (`606-10-25-18A`) | No equivalent election |
| Immaterial promised goods/services | May disregard (`606-10-25-16A`) | No explicit equivalent; assess materiality generally |
| Noncash consideration measurement date | Fair value at **contract inception** | At contract inception, but measurement-date guidance was not amended identically |
| Disclosure / interim | Different interim disclosure requirements (US public entities) | IAS 34 interim regime |

Always run `ifrs15-revenue` in parallel for dual-reporters and present both answers (base §2).

## Section 8 — Disclosure checklist — `ASC 606-10-50`

Trigger and produce as relevant:

- [ ] Disaggregation of revenue into categories (`50-5`)
- [ ] Contract balances: opening/closing contract assets, liabilities, and receivables; revenue recognized from prior-period contract liabilities (`50-8` to `50-10`)
- [ ] Performance obligations: nature, timing of satisfaction, significant payment terms (`50-12`)
- [ ] Transaction price allocated to **remaining** performance obligations (backlog) and when expected to be recognized (`50-13` to `50-15`)
- [ ] Significant judgments: timing of satisfaction, determining/allocating transaction price (`50-17` to `50-20`)
- [ ] Contract cost assets: closing balances by category and amortization (`340-40-50-2`)
- [ ] Practical expedients elected (`50-22`, `50-23`)

## Section 9 — Topic self-checks (in addition to base §7)

- [ ] All five steps applied **in order**; each conclusion cites its `ASC 606-10` paragraph
- [ ] Collectibility gate assessed correctly (concession ≠ collectibility failure)
- [ ] Each PO's distinct analysis documented (capable + separately identifiable)
- [ ] Variable consideration estimated **and constrained**; method (expected value / most likely) stated
- [ ] Significant financing component assessed (or expedient applied) for payment timing > 1 yr
- [ ] SSP allocation table shown; discount/variable allocation rules applied
- [ ] Over-time vs. point-in-time conclusion tied to a specific `25-27` criterion or control indicator
- [ ] Principal/agent resolved for every third-party promise → gross/net stated
- [ ] Contract costs capitalized/expensed per ASC 340-40; amortization shown
- [ ] Balances classified: contract asset vs. receivable vs. contract liability vs. refund liability
- [ ] Divergence from IFRS 15 checked for dual-reporters

## Section 10 — Disclaimer

Provides computational and interpretive guidance on ASC 606 / ASC 340-40 only. Not an audit and not assurance. Revenue recognition turns heavily on entity-specific facts and significant judgment. Have outputs reviewed and signed by a qualified accountant before they are reflected in financial statements relied upon by third parties.

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
