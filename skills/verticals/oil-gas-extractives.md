---
name: oil-gas-extractives
description: "Use this skill whenever a producer, refiner, miner, oilfield services company, midstream operator, or LNG developer asks about sector-specific tax and accounting. Trigger on phrases like \"petroleum revenue tax\", \"PRT\", \"ring-fence corporation tax\", \"RFCT\", \"supplementary charge\", \"energy profits levy\", \"EPL\", \"OBPS\", \"carbon levy\", \"EU Solidarity Contribution\", \"windfall tax energy\", \"Norwegian special tax\", \"petroleum tax\", \"production sharing contract\", \"PSC\", \"concession\", \"royalty\", \"ad valorem royalty\", \"severance tax\", \"depletion allowance\", \"intangible drilling costs\", \"IDC\", \"successful efforts vs full cost\", \"decommissioning ARO\", \"EITI\", \"extractive industries transparency initiative\", \"country-by-country resource payments\", \"mining royalty\", or any question on extractives. Maps petroleum and mining fiscal regimes for 25+ jurisdictions plus the windfall taxes introduced 2022-2025. Does NOT cover: HSE / safety regulation, environmental remediation procedure beyond tax accounting, oil & gas reserves estimation methodology (PRMS)."
version: 0.1
jurisdiction: GLOBAL
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on:
  - corporate-income-tax-workflow-base
category: vertical
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Oil Gas Extractives

## What this file is

A sector overlay for oil & gas, mining, and other extractives companies.

## Section 1 — Fiscal regimes overview

**[T1] Three main regime models**  _(Section 1 — Fiscal regimes overview)_

| Regime | Mechanism | Examples |
| --- | --- | --- |
| **Concession / Royalty + Tax** | Operator pays royalty + standard CIT (often ring-fenced) | UK (Brent, North Sea), Norway, US (federal + state royalty + CIT), Canada, Australia |
| **Production Sharing Contract (PSC)** | Operator recovers costs from "cost oil/gas"; "profit oil/gas" split with government per scale | Indonesia, Nigeria, Angola, Egypt, Algeria, Brazil pre-salt, Kazakhstan |
| **Service / Risk Service** | Operator paid fee per unit produced; government retains ownership | Mexico (pre-2014 reform), Iran (buyback), Iraq (technical services contract) |

## Section 2 — UK North Sea fiscal regime

### 2.1 The ring-fence

- **UK ring-fence rule** — UK upstream petroleum activities are "ring-fenced" — losses and profits from non-ring-fence trades cannot offset ring-fence profits.  _([T1])_

### 2.2 Three taxes

- **Ring-Fence Corporation Tax (RFCT)** — 30%  _(Finance Act 2002)_
- **Supplementary Charge (SC)** — 10% additional tax (reduced from 32% in 2016, reinstated to 10% in 2024)  _([T1])_
- **Energy Profits Levy (EPL)** — 35% (rate increased to 38% from 1 November 2024 under Finance Act 2025 amendments; sunset extended to March 2030)  _(Energy Profits Levy Act 2022; Finance Act 2025)_
- **Total effective rate** — 30% + 10% + 38% = 78% (post-November 2024)  _([T1])_
- **Petroleum Revenue Tax (PRT)** — frozen at 0% from 2016 for new fields  _([T1])_

### 2.3 Allowances

- **Capital allowances** — 100% first-year on most plant and machinery in ring-fence  _([T1])_
- **Loss carryforward / carryback** — intricate  _([T1])_
- **EPL investment allowance** — 44% (reduced from 80%) for qualifying ring-fence investment expenditure  _([T1])_

## Section 3 — Norwegian Special Tax

- **Standard CIT** — 22%  _([T1])_
- **Special petroleum tax (SPT)** — 56% (effective rate)  _([T1])_
- **Combined marginal rate** — 78%  _([T1])_
- **Cash-flow basis tax reform** — Recently introduced cash-flow basis for tax reform: full first-year deduction of qualifying upstream investment (reformed 2022); SPT calculated on operating cash flow less qualified investment expense  _([T1])_

## Section 4 — EU Solidarity Contribution

- **Temporary solidarity contribution** — Temporary solidarity contribution on fossil fuel sector "surplus profits"  _(Council Regulation (EU) 2022/1854)_
- **Surcharge rate** — 33% surcharge on profits above 120% of 4-year average  _(Council Regulation (EU) 2022/1854 (October 2022))_
- **Member State implementation** — Member States implemented as temporary windfall taxes for 2022 and 2023  _([T1])_
- **Extension and UK treatment** — Most Member States extended through 2024-2025; UK has its own EPL outside EU framework  _([T1])_

## Section 5 — US oil and gas

- **Federal CIT** — 21%  _([T1])_
- **State CIT** — variable  _([T1])_
- **Severance taxes** — state-level on extracted product (Texas oil severance 4.6%; Oklahoma 7%; ND 6.5%; WV 5%; etc.)  _([T1])_
- **Royalty** — federal lease 18.75% offshore / 12.5% onshore (raised from 12.5% to 16.67% in 2022 reform); state and private lease rates negotiated  _([T1])_
- **IDC (Intangible Drilling Costs)** — election to expense currently (§263(c))  _(§263(c))_
- **Depletion allowance** — percentage depletion for small producers (§613A) or cost depletion (§612)  _(§613A; §612)_
- **Successful Efforts vs Full Cost** — financial accounting method choice (ASC 932)  _(ASC 932)_

### 6.1 Major mining jurisdictions

**Major mining jurisdictions**  _(Section 6 — Mining sector)_

| Country | Royalty | CIT | Notable |
| --- | --- | --- | --- |
| **Australia** | Mineral Resources Rent Tax (MRRT) repealed 2014; state royalties (NSW, QLD, WA variable 2-10%) | 30% CIT; full expensing of capital | Major iron ore, coal, gold |
| **Canada** | Provincial royalty + CIT 26.5% combined | Federal 15% + provincial | Major potash, oil sands |
| **Chile** | Mining royalty (2024 reform: ad-valorem + margin-based 1-2% + 10-32% on profits above thresholds) | 25% CIT | World's largest copper |
| **Peru** | Mining royalty 1-12% by margin; Special Mining Tax 2-8.4% on operating margin; CIT 29.5% | 29.5% | Major copper, gold, zinc |
| **South Africa** | Mining royalty 0.5-7% by refined vs unrefined | 27% CIT (post-2024) | Major platinum, gold |
| **Indonesia** | Royalty 3-6% by mineral; PSC for oil/gas | 22% CIT | Major coal, nickel |

### 6.2 EITI (Extractive Industries Transparency Initiative)

- **EITI reporting** — 50+ implementing countries publish reconciled extractive payments and receipts. EU Accounting and Transparency Directives require listed extractive companies to publish payments to governments (Country-by-Country Reporting equivalent).  _([T1])_

### 7.1 Successful Efforts vs Full Cost

- **Successful Efforts** — only successful exploration costs capitalised; dry holes expensed.  _([T1])_
- **Full Cost** — all exploration and development costs capitalised in "cost pool" by country.  _([T1])_
- **GAAP/IFRS treatment** — US GAAP ASC 932 permits both. IFRS 6 (Exploration and Evaluation Assets) allows choice for E&E phase but development phase aligned to IAS 16 / IAS 38.  _(ASC 932; IFRS 6; IAS 16; IAS 38)_

### 7.2 Asset Retirement Obligation (ARO) / Decommissioning

- **ARO recognition** — IAS 37 / ASC 410: provision for future decommissioning recognised at discounted PV of cost when constructive obligation arises (typically at first production).  _(IAS 37; ASC 410)_
- **Provision accounting treatment** — Provision debited as asset addition; depleted with the reserve  _([T1])_
- **Tax deduction timing** — Tax deduction generally only when actually incurred (jurisdiction-specific)  _([T1])_
- **Deferred tax impact** — Material deferred tax timing difference  _([T1])_

### 7.3 Reserves estimation (PRMS)

- **Petroleum Resources Management System** — 1P (proved), 2P (proved + probable), 3P (proved + probable + possible). Recoverable reserves drive depletion accounting.  _([T1])_

## Section 8 — Pillar Two interaction

- **Pillar Two complexity for extractives** — Extractives jurisdictions with low CIT but high royalty/severance face Pillar Two complexity: - Royalty is typically treated as "Covered Tax" if levied on income (some jurisdictions classify as production tax, ambiguous) - Severance taxes mostly NOT Covered Taxes - Carve-out for "International Shipping Income" exists; no equivalent for extractives - Substance-Based Income Exclusion (SBIE) particularly material for capital-intensive extractives  _([T1])_

## Section 9 — Self-checks

- [ ] Fiscal regime classified (concession / PSC / service)
- [ ] Ring-fence applied where required (UK)
- [ ] EPL / SC rate current
- [ ] Royalty treatment (revenue vs Covered Tax) confirmed
- [ ] Successful Efforts vs Full Cost election documented
- [ ] ARO / decommissioning provision recognised
- [ ] Depletion / depreciation per tax basis
- [ ] EITI / CbC reporting submitted where applicable
- [ ] Pillar Two analysis for in-scope groups
- [ ] Output flags every [T2]/[T3] item for reviewer judgement

## Section 10 — Disclaimer

Extractives taxation is highly specialised. Outputs must be reviewed by credentialed extractives sector practitioners. The most up-to-date version is at [openaccountants.com](https://openaccountants.com).

## Talk to a verified accountant

This skill is a tool, not an engagement. Every taxpayer's situation is
different, and the rules in the skill may not match your specific facts.

To speak with one of the licensed accountants who verifies skills for your
jurisdiction — **no liability on either side until you and the accountant sign
a formal engagement letter** — book a free 30-minute call:

**→ [Book a call](https://calendly.com/openaccountants-info/30min)**

We'll route you to the named verifier covering your country or state. You can
also see the full list of verified accountants at
[openaccountants.com/network](https://openaccountants.com/network).

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
