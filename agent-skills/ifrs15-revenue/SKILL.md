---
name: ifrs15-revenue
description: "IFRS revenue recognition under IFRS 15 (Revenue from Contracts with Customers) and the related contract-cost guidance within IFRS 15. Covers the five-step model - identify the contract, identify performance obligations, determine the transaction price, allocate it, and recognise revenue as or when obligations are satisfied - plus variable consideration and the constraint, significant financing components, principal-versus-agent, licences, contract modifications, contract assets and liabilities, and the costs of obtaining and fulfilling a contract. Produces recognition conclusions, journal entries, and a reviewer brief. Issued as the IFRS edition of the revenue topic; see us-gaap-asc606-revenue for the US GAAP edition. MUST load alongside financial-reporting-workflow-base."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/ifrs15-revenue"
  jurisdiction: "GLOBAL"
  last_updated: "2026-11-16"
---

# IFRS 15 revenue v0.4

**Coverage is partial:** the individually identified supporting-standard and current US comparison gaps below remain outside usable instructions.

**General reference only.** Produces working papers and a reviewer brief, not an audit, assurance opinion or signed financial statements. Tier 2; not approved by an accountant.

## Scope

**Standard and effective-date basis:** IFRS 15 Revenue from Contracts with Customers; effective-date key **2018-01-01**. Paragraphs C1 and C1B require the Standard and April 2016 clarifications for annual periods beginning on or after 1 January 2018; early application is permitted with disclosure. Later consequential amendments require their own adoption analysis. [IFRS 15.C1/C1B](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs15.html).


**This is a content skill that loads on top of `financial-reporting-workflow-base`.** It supplies the recognition, measurement, presentation, and disclosure rules for revenue from contracts with customers under IFRS. The base supplies the two-layer output contract, the journal-entry format, and the self-checks.

- **Scope**  -  IFRS 15 applies to contracts with customers except: leases (IFRS 16), insurance contracts (IFRS 17), subject to the .5(b)/IFRS 17.8 option for issued fixed-fee-service contracts only where all 3 conditions hold: pricing does not reflect individual-customer risk assessment, compensation is services rather than cash, and the transferred insurance risk arises primarily from customer use rather than uncertainty over service cost. The contract-by-contract election is irrevocable; financial instruments and other contractual rights/obligations in IFRS 9 / IFRS 10 / IFRS 11 / IAS 27 / IAS 28, and certain non-monetary exchanges between entities in the same line of business to facilitate sales to customers.  _(IFRS 15.5)_


This skill covers:

- The five-step model of IFRS 15.
- Variable consideration and the constraint; significant financing components; non-cash consideration; consideration payable to a customer.
- Principal vs. agent, licences of IP, warranties, customer options (material rights), bill-and-hold, repurchase agreements, consignment.
- Contract modifications.
- Presentation of contract assets, contract liabilities, and refund liabilities.
- Incremental costs of obtaining a contract and costs to fulfil (`IFRS 15.91`–`104`).

This skill does NOT cover: lease income (`IFRS 16`), interest/dividend income (`IFRS 9`/`IAS 18`-legacy superseded), insurance (`IFRS 17`), except a .5(b) fixed-fee-service option supported by a separately sourced IFRS 17.8 conclusion. It defers the US GAAP treatment to `us-gaap-asc606-revenue`.


**Version basis for 2026 work.** The effective-date field identifies the directly read core amendment basis (initial application and clarifications, IFRS 15.C1/C1B). Apply IFRS 9/IFRS 17 consequential provisions only when those Standards apply; their separate transition dates were not recovered here. IFRS 18/IFRS 19 consequential presentation/disclosure changes are excluded until adopted. The 2026 issued HTML also contains future-effective text; do not assume its publication year is its effective date. The operative core was personally read in the official copy retrieved on 14 November 2026. Official source retrieval succeeded again on 16 November 2026; the core was reconciled with that body and the selected supporting clauses below were personally read. Source dates distinguish those reads from mere retrieval.

## Ask the client first

- Reporting framework, reporting-period start/end and any early adoption of IFRS 18/IFRS 19.
- Executed contract, side letters, cancellation and modification terms, customer identity and collectibility evidence.
- Every promised good/service, standalone selling prices, integration, acceptance, delivery and over-time payment rights.
- Fixed/variable/non-cash amounts, refunds, financing terms, royalties and principal/agent facts.
- Commission and fulfilment-cost records, expected recoveries, renewal periods and opening contract balances.

## The method, step by step

### Section 2  -  Reference layer (Layer A): the five-step model

### Step 1  -  Identify the contract  -  `IFRS 15.9`–`16`

- **Contract identification criteria**  -  A contract with a customer is in scope when **all 5** criteria are met: 1. The parties have **approved** the contract and are committed to perform. 2. Each party's **rights** are identifiable. 3. **Payment terms** are identifiable. 4. The contract has **commercial substance**. 5. It is **probable** the entity will collect the consideration it is entitled to. Assess the customer's ability and intention to pay the amount expected to be entitled, including genuine price concessions. The cross-framework definition/threshold comparison is reserved below.  _(IFRS 15.9)_
- **Criteria not met treatment**  -  If criteria are not met, consideration received is recognised as a **liability** until the criteria are met or the `15.15` release events occur.  _(IFRS 15.15)_
- **Combine contracts**  -  Combine contracts with the same customer (or related parties) entered into at/near the same time when negotiated as a package, consideration is interdependent, or the goods/services form a single performance obligation.  _(IFRS 15.17)_

> **⚑ AUDIT FLASH POINT  -  collectibility and the variable-consideration constraint are separate tests.** Document the .9(e) collectibility conclusion separately from .56 variable-consideration constraint; do not confuse those two tests.

### Step 2  -  Identify the performance obligations  -  `IFRS 15.22`–`30`

- **Performance obligation**  -  A performance obligation is a promise to transfer a **distinct** good/service or a **series** of distinct goods/services that are substantially the same and have the same pattern of transfer.  _(IFRS 15.22)_
- **Distinct criteria**  -  Distinct requires **both**: **Capable of being distinct**  -  the customer can benefit from it on its own or with readily available resources; and **Distinct within the context of the contract**  -  separately identifiable; the entity is not providing a significant integration service, the good does not significantly customise/modify another, and it is not highly interdependent/interrelated.  _(IFRS 15.27; IFRS 15.29)_

### Step 3  -  Determine the transaction price  -  `IFRS 15.47`–`72`

- **Transaction price**  -  Transaction price = consideration the entity expects to be **entitled to**, excluding amounts collected on behalf of third parties.  _(IFRS 15.47)_
- **Variable consideration**  -  Estimate using **expected value** or **most likely amount**.  _(IFRS 15.50–54)_
- **The constraint**  -  Include only to the extent **highly probable** that a significant reversal will not occur. Reassess the constraint at every reporting date (.59).  _(IFRS 15.56–58)_
- **Significant financing component**  -  Adjust for time value of money where significant. Practical expedient: ignore if ≤ 1 year between transfer and payment.  _(IFRS 15.60–65; IFRS 15.63)_
- **Non-cash consideration**  -  Measure at **fair value**; if fair value cannot be reasonably estimated, measure by reference to the standalone selling price.  _(IFRS 15.66–69)_
- **Consideration payable to a customer**  -  Reduction of transaction price unless for a distinct good/service.  _(IFRS 15.70–72)_

> **⚑ AUDIT FLASH POINT  -  non-cash consideration measurement date.** Use the fair-value/standalone-price requirements in .66-.69 and document the measurement-date policy. Current US comparison is reserved below.

### Step 4  -  Allocate the transaction price  -  `IFRS 15.73`–`90`

- **Allocation by SSP**  -  Allocate to each PO by **standalone selling price**; estimate SSP where not observable (adjusted market assessment, expected cost plus margin, or residual approach with the `15.79` restrictions). Allocate discounts (`15.81`–`83`) and variable consideration (`15.84`–`86`) to specific POs where the criteria are met.  _(IFRS 15.76; IFRS 15.79; IFRS 15.81–83; IFRS 15.84–86)_

### Step 5  -  Recognise revenue when/as a PO is satisfied  -  `IFRS 15.31`–`45`

- **Recognition trigger**  -  Recognise revenue when the entity transfers **control** of the good/service.  _(IFRS 15.31)_
- **Over time criteria**  -  **Over time** if **any 1** of 3 criteria is met: 1. The customer **simultaneously receives and consumes** benefits as the entity performs; or 2. Performance **creates or enhances an asset the customer controls**; or 3. Performance does **not create an asset with alternative use** and the entity has an **enforceable right to payment** for performance to date.  _(IFRS 15.35)_
- **Measuring progress**  -  If over time, **measure progress** by output or input method; if progress cannot be reasonably measured but costs are recoverable, recognise revenue only to the extent of costs.  _(IFRS 15.39–45; IFRS 15.45)_
- **Point in time indicators**  -  **Point in time** otherwise  -  recognise when control transfers, using indicators in `15.38` (present right to payment, legal title, physical possession, risks and rewards, acceptance).  _(IFRS 15.38)_

### Section 3  -  Reference layer: high-frequency special topics

- **Principal vs. agent**  -  Principal **controls** the good/service before transfer → **gross**; agent → **net** (fee/commission). Evaluate the specified good/service and the .B37 control indicators.  _(IFRS 15.B34–B38)_
- **Licences of IP**  -  **Right to access** where all B58 criteria hold → **over time**; significant effects include changes to IP form/function or a benefit substantially derived from or dependent on the entity's activities (B59A), such as ongoing brand support; **right to use** (IP as it exists when granted) → **point in time**. Sales/usage-based **royalty exception**: recognise at the later of the subsequent sale/usage or satisfaction of the PO.  _(IFRS 15.B52–B63; IFRS 15.B63)_
- **Warranties**  -  Assurance-type → provision under `IAS 37`, not a PO; service-type → separate PO.  _(IFRS 15.B28–B33)_
- **Customer options / material rights**  -  A material right is a separate PO.  _(IFRS 15.B39–B43)_
- **Contract modifications**  -  Separate contract if distinct goods at SSP; otherwise prospective (if remaining goods distinct) or cumulative catch-up (if not).  _(IFRS 15.18–21)_

### Section 4  -  Reference layer: contract costs  -  `IFRS 15.91`–`104`

- **Incremental costs of obtaining a contract**  -  Recognised as an **asset** if expected to be recovered. Practical expedient: expense if amortisation period ≤ 1 year.  _(IFRS 15.91; IFRS 15.94)_
- **Costs to fulfil a contract**  -  Costs to fulfil a contract (not in another standard) are capitalised if they relate directly to a contract, generate/enhance resources used for future performance, and are expected to be recovered.  _(IFRS 15.95)_
- **Amortisation and impairment**  -  **Amortise** consistent with transfer of goods/services; test for impairment.  _(IFRS 15.99–104)_

### Section 5  -  Presentation  -  `IFRS 15.105`–`109`

- **Contract liability**  -  Consideration received/due before transfer of goods/services.  _(IFRS 15.105–109)_
- **Contract asset**  -  Right to consideration for goods/services transferred, conditional on something other than the passage of time. Once unconditional → **receivable** (in scope of `IFRS 9` for impairment).  _(IFRS 15.105–109)_
- **Refund liability**  -  Refund liability plus an **asset for the right to recover** returned goods.  _(IFRS 15.55, B20–B27)_

### Section 6  -  Executable layer (Layer B): the procedure

Apply the following IFRS 15 procedure under the base output contract:

0. **Confirm a contract exists**  -  Confirm a contract exists (`15.9`); if the .9 criteria fail, apply .15-.16: cash received remains a liability unless a specified .15 release event occurs; keep reassessing under .14.
0. **List promises → POs**  -  List promises → POs (`15.22`–`30`); document distinct analysis; flag series, material rights, warranties.
0. **Build the transaction price**  -  Build the transaction price (`15.47`–`72`): fixed + constrained variable; significant financing component; non-cash at fair value; net consideration payable.
0. **Determine SSP and allocate**  -  Determine SSP and allocate (`15.73`–`90`); show the table.
0. **Timing per PO**  -  Timing per PO (`15.31`–`45`): over time (criterion + progress measure) or point in time (control indicators).
0. **Principal/agent for third-party promises**  -  Principal/agent for third-party promises (`B34`–`B38`) → gross/net.
0. **Recognise revenue; book journal entries**  -  Recognise revenue; book **journal entries** (base §3) day 1 + subsequent.
0. **Capitalise/amortise contract costs**  -  Capitalise/amortise contract costs (`15.91`–`104`).
0. **Classify balances**  -  Classify balances (`15.105`–`109`).
0. **Disclosure checklist + reviewer brief**  -  Disclosure checklist (§8) + **reviewer brief** with every flash point.

### Section 8  -  Disclosure checklist  -  `IFRS 15.110`–`129`

- **Disclosure checklist**  -  - [ ] Disaggregation of revenue (`114`–`115`) - [ ] Contract balances and movements; revenue recognised from opening contract liabilities (`116`–`118`) - [ ] Performance obligations: nature, timing, significant payment terms (`119`) - [ ] Transaction price allocated to remaining POs (backlog) and timing (`120`–`122`) - [ ] Significant judgements: timing of satisfaction; determining/allocating transaction price (`123`–`126`) - [ ] Contract cost assets: closing balances and amortisation (`127`–`128`) - [ ] Practical expedients used (`129`)  _(IFRS 15.110–129)_

### Section 9  -  Topic self-checks (in addition to base §7)

- [ ] All 5 steps applied in order; each conclusion cites its IFRS 15 paragraph
- [ ] Collectibility assessed against customer ability and intention under .9(e) _(IFRS 15.9(e))_
- [ ] Distinct analysis documented per PO _(IFRS 15.22–.30)_
- [ ] Variable consideration estimated and constrained ("highly probable"); method stated _(IFRS 15.50–.59)_
- [ ] Significant financing component assessed (or expedient) for timing > 1 yr _(IFRS 15.60–.65)_
- [ ] SSP allocation table shown _(IFRS 15.73–.86)_
- [ ] Over-time vs. point-in-time tied to a `15.35` criterion or control indicator
- [ ] Principal/agent resolved → gross/net _(IFRS 15.B34–B38)_
- [ ] Contract costs capitalised/amortised per `15.91`–`104`; impairment (and any reversal) considered
- [ ] Balances classified: contract asset vs. receivable vs. contract liability vs. refund liability _(IFRS 15.55, .105–.109, B20–B27)_
- [ ] Prepare the dual-reporting handoff; current ASC 606 comparison remains reserved pending source recovery


### Conditions that complete the abbreviated special-topic rules

A series qualifies as a single performance obligation only where each distinct service/good meets the over-time criteria and the same progress method would be used (.23). Contract-cost capitalisation excludes general administration unless explicitly chargeable, waste not reflected in price, costs of past performance and costs that cannot be distinguished between satisfied/unsatisfied performance obligations (.98).

For a right-to-access licence, all B58 criteria must hold: expected activities significantly affect the IP, expose the customer to their positive/negative effects and do not transfer a separate good/service as they occur. B59A includes both expected significant form/function changes and a customer benefit substantially derived from or dependent on the activities; IP need not itself change in the latter case. Significant stand-alone functionality limits that latter inference as B59A explains. Otherwise use right-to-use timing, never before the customer can use and benefit (B58-B61). Apply the sales/usage royalty exception only to IP-only or IP-predominant royalties (B63-B63B). For repurchase agreements evaluate forwards/calls and customer puts, prices, time value and incentive; outcomes include a lease, financing or sale with return rights (B64-B76). Consignment does not produce revenue on delivery while control is retained (B77-B78). Bill-and-hold additionally requires a substantive reason, separately identified customer goods, readiness for delivery and no ability to redirect/use; separately assess custodial services (B79-B82).

A customer payment for a distinct good/service reduces revenue to the extent it exceeds fair value; inability to estimate fair value means the whole payment reduces revenue (.70-.72). The 1-year financing expedient measures the expected transfer-to-payment period at inception (.63); .62 separately excludes specified non-financing payment differences. Contract-cost impairment reversals are capped at the carrying amount that would exist without impairment (.104). For refunds, recognise the refund liability and the recoverable-return asset separately, with recovery costs and impairment considered (B20-B27).

## Worked cases

All monetary amounts, rates and transaction dates below are illustrative supplied facts, not legal thresholds or prescribed yields. Keep the original whole-dollar journal displays separate from the cent-precision check.

### Worked example (illustrative)

Illustrative SaaS contract ($24,000 subscription + $6,000 non-distinct setup, paid upfront, 24-month delivery). Single combined PO, over time under `15.35(a)`, straight-line. Assume a documented .60-.65 assessment establishes no significant financing component; the recoverable $3,000 commission relates only to this 24-month service period, with no renewal or longer expected benefit period.

```
Day 1  -  driving rule: IFRS 15.106 (contract liability)
  Dr  Cash                                   30,000
      Cr  Contract liability                       30,000
  (memo: single combined PO; no revenue at inception)

Each month (×24)  -  driving rule: IFRS 15.35(a)
  Dr  Contract liability                       1,250
      Cr  Revenue                                    1,250
  (memo: 30,000 / 24; debits = credits ✓)

Day 1  -  incremental cost to obtain  -  driving rule: IFRS 15.91
  Dr  Contract cost asset                      3,000
      Cr  Cash                                       3,000

Each month (×24)  -  amortise  -  driving rule: IFRS 15.99
  Dr  Amortisation expense                       125
      Cr  Contract cost asset                          125
```

> **⚑ AUDIT FLASH POINT  -  combine/separate judgement.** The distinct conclusion drives IFRS timing; evidence the integration analysis. The foreign-framework comparison remains reserved.

```oa-check
name: Existing SaaS case, non-distinct setup and recoverable commission
inputs:
  subscription: 24000
  setup: 6000
  months: 24
  commission: 3000
  elapsed: 12
steps:
  - transaction_price: subscription + setup
  - monthly_revenue: transaction_price / months
  - monthly_amortisation: commission / months
  - closing_contract_liability: transaction_price - monthly_revenue * elapsed
  - closing_cost_asset: commission - monthly_amortisation * elapsed
expected:
  monthly_revenue: 1250
  monthly_amortisation: 125
  closing_contract_liability: 15000
  closing_cost_asset: 1500
```

An additional allocation case has distinct delivered equipment with an evidenced standalone selling price of $8,000 and a 12-month service with an evidenced standalone price of $4,000. Fixed consideration is $9,000; there is no allocation exception, variable amount or significant financing component. Allocate $6,000 to equipment on control transfer and $3,000 to service, recognised $250 monthly as the service is supplied. These are illustrative transaction inputs, not statutory rates (IFRS 15.74-80, .31-40).

```oa-check
name: Relative standalone selling prices, delivered equipment and future service
inputs:
  equipment_ssp: 8000
  service_ssp: 4000
  price: 9000
  months: 12
steps:
  - total_ssp: equipment_ssp + service_ssp
  - equipment_revenue: price * equipment_ssp / total_ssp
  - service_allocation: price * service_ssp / total_ssp
  - monthly_service: service_allocation / months
expected:
  equipment_revenue: 6000
  service_allocation: 3000
  monthly_service: 250
```

## When to refuse or refer

Refuse a final recognition, classification, valuation or disclosure conclusion when required contracts, applicable reporting period, adoption facts or supporting standards are missing. Refer significant valuations, enforceability, control, impairment and complex settlement terms to a qualified reporting specialist. Return the facts, paragraph-by-paragraph reasoning, balanced journals, reconciliation and open items to the reviewer. Do not issue audit or assurance language. Any topic reserved below remains outside usable instructions until its operative primary source is recovered.


### Original professional disclaimer

Provides computational and interpretive guidance on IFRS 15 only. Not an audit and not assurance. Revenue recognition turns heavily on entity-specific facts and significant judgement. Have outputs reviewed and signed by a qualified accountant before they are reflected in financial statements relied upon by third parties.

## Sources

| Source | Official URL | Actual read scope and date |
|---|---|---|
| IFRS 15 Revenue from Contracts with Customers | [IFRS 15 Revenue from Contracts with Customers](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs15.html) | Read for .5-.45, .46-.104, .105-.129, B20-B43, B52-B82, C1-C1D in the official 2026-issued copy retrieved 2026-11-14, personally read 2026-11-15; official body retrieved again and reconciled 2026-11-16; existing read scope retained |
| IFRS 17 fixed-fee services | [IFRS 17](https://www.ifrs.org/content/dam/ifrs/publications/html-standards/english/2026/issued/ifrs17.html) | Read 2026-11-16: .3-.9, especially all .8 conditions and irrevocable contract-by-contract option; no wider insurance measurement covered. |
| Current US comparison | [Authoritative ASC](https://asc.fasb.org/) | Attempted again 2026-11-16; official ASC web pages returned 0 readable lines. Current operative Codification not read; historical recovery limits are preserved in external evidence. |

Not yet confirmed: jurisdiction-specific endorsement and entity-specific early adoption; all individually retained source-limited items below. These boundaries are not accountant approval.

#### Not yet confirmed: individual current ASC 606 comparisons

Official ASC web recovery on 16 November 2026 returned no readable operative paragraphs. Do not treat the old comparison values as current US instructions. Each topic remains separately identified for source recovery and the dual-reporting handoff:

| Original comparison | Specific unresolved US-dependent conclusion |
| --- | --- |
| Collectibility | Current ASC definition/application of probable, the old more-likely-than-not versus likely comparison and any claimed lower/higher bar; no numerical probability is supplied here. |
| Variable-consideration constraint | The original claim that IFRS highly probable and ASC probable were intended to produce the same threshold; assess the actual rule in each edition. |
| Shipping/handling | Current ASC policy election versus the IFRS promised-service assessment. |
| Immaterial promises | Current scope and conditions of ASC 606-10-25-16A relief versus IFRS materiality. |
| Non-cash consideration | Current ASC contract-inception measurement-date rule and any difference from the documented IFRS policy. |
| Licensing renewals and royalties | Identify the actual difference and its conditions; the old phrase minor differences does not determine treatment. |
| Interim disclosures | Current US public-entity interim regime versus a separately sourced IAS 34 analysis. |
| Contract-cost impairment | Current ASC prohibition/conditions for reversals versus the IFRS 15.104 capped reversal. |
| Principal/agent and SaaS integration | Do not assume identical indicators or timing merely because the IFRS example or method also appears in another edition. |

The IFRS 15.9(e) collectibility wording is supported. Its old more-likely-than-not gloss and a cross-framework probability comparison are not instructions in this file. Recover the relevant definitions/current ASC and apply facts before drawing a dual-reporting outcome. The base workflow still requires separate supported runs and reconciliation.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-16. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `ifrs15-revenue` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/ifrs15-revenue. If neither is available, confirm every figure against the official source pages cited above before relying on it.
