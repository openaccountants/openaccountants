---
name: insurance-sector
description: "Use this skill whenever an insurer, reinsurer, captive, MGA, or insurance broker asks about accounting, regulatory, or tax issues specific to insurance entities. Trigger on phrases like \"IFRS 17\", \"ASC 944\", \"LDTI\", \"Solvency II\", \"Bermuda EBT\", \"captive insurance\", \"PFIC insurance exclusion\", \"PRA Pillar 1/2/3\", \"SCR\", \"MCR\", \"Lloyd's syndicate\", \"reinsurance recoverable\", \"deferred acquisition costs\", \"DAC\", \"premium deficiency reserve\", \"loss reserve discount\", \"insurance premium tax\", \"IPT\", \"consumption levy on insurance\", or any insurance-specific accounting/tax question. Covers IFRS 17 transition, US ASC 944 Long-Duration Targeted Improvements (LDTI), Solvency II prudential interaction with tax, captive insurance regimes (Bermuda, Cayman, Guernsey, Vermont), insurance premium tax matrix, and the PFIC active insurance exception. Does NOT cover: insurance product design / pricing, actuarial valuation methodology beyond reference, or insurance regulatory authorisation."
version: 0.1
jurisdiction: GLOBAL
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on: - corporate-income-tax-workflow-base
category: vertical
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Insurance Sector

## Insurance Sector Tax & Accounting v0.1

## What this file is

A sector overlay for life insurers, non-life insurers, reinsurers, captives, MGAs, and brokers.

## Section 1 — Scope

This skill covers:

- **IFRS 17 transition** — fully effective for annual periods beginning on or after 1 January 2023; comparative IFRS 17 to IFRS 4 differences
- **US ASC 944 LDTI** — fully effective for public business entities annual periods beginning after 15 December 2022 (calendar year 2023)
- **Solvency II interaction with tax** — risk margin, technical provisions, deferred tax on transitional measures
- **Captive insurance** regimes (Bermuda, Cayman, Guernsey, Isle of Man, Vermont, Hawaii, South Carolina, Singapore)
- **Insurance Premium Tax (IPT)** matrix
- **PFIC active insurance exception** for US-owned non-US insurers (IRC §1297(b)(2)(B), §1297(f))
- **BEAT and §250 GILTI/FDII** for US-based insurance groups
- **Pillar Two interaction** — IFRS 17 contractual service margin (CSM), risk adjustment volatility

This skill does NOT cover:

- **Insurance product design and pricing**
- **Actuarial valuation methodology** beyond reference
- **Insurance regulatory authorisation** procedures
- **Lloyd's of London-specific syndicate tax** (separate specialist skill)

## Section 2 — IFRS 17 ↔ ASC 944 LDTI differences

**[T1] See `ifrs-local-gaap-reconciliation.md` for foundation. Insurance-specific:**

**IFRS 17 vs ASC 944 LDTI differences**  _(Section 2 — IFRS 17 ↔ ASC 944 LDTI differences)_

| Topic | IFRS 17 | ASC 944 LDTI |
| --- | --- | --- |
| Liability measurement | Building Block Approach (BBA), Premium Allocation Approach (PAA) for short-duration, Variable Fee Approach (VFA) for direct participating | Net premium reserve; updated assumptions through P&L (LDTI improvements) |
| Discount rate | Top-down or bottom-up; reflects characteristics of cash flows | Single A-quality corporate yield curve (LDTI prescribed) |
| Contractual Service Margin (CSM) | Recognised in P&L over coverage period | No equivalent — gain at issue spread differently |
| Risk Adjustment | Reflects compensation for non-financial risk; entity-specific | Different — discretion in net premium reserve methodology |
| Onerous contract | Loss recognised immediately + Loss Component tracking | Premium Deficiency Reserve (PDR) at portfolio level |
| Reinsurance held | Asset/liability separately; expected to mirror underlying when treaty matches | Recognised as reduction of net premium |

- **Material tax interaction** — IFRS 17 CSM creates a deferred tax balance — the CSM is recognised in equity at transition but released to P&L over time. Deferred tax tracks this release.  _([T1] Material tax interaction)_

## Section 3 — Specific insurance tax items

### 3.1 US insurance taxation

- **Subchapter L** — Separate corporate income tax regime for insurance companies  _(IRC §§801-848)_
- **Life insurer** — §816(a) test: >50% reserves life or non-cancellable A&H: special reserves deduction, DAC capitalisation under §848  _(IRC §816(a), §848)_
- **Non-life insurer** — §832 "underwriting income" + investment income; loss reserves discounted per §846  _(IRC §832, §846)_
- **Captive PFIC exception** — "Qualifying insurance corporation" status if applicable insurance liabilities ≥ 25% of total assets (10% with safe harbour facts)  _(IRC §1297(f))_
- **§953(d) election** — Election for foreign insurance corporations to be treated as US for tax (election common for Bermuda captives owned by US)  _(IRC §953(d))_
- **§953(c)** — Related-party captive income — Subpart F  _(IRC §953(c))_

### 3.2 UK insurance taxation

- **General Insurer Tax Regulation (GITR)** — FA 2012 Part 2 / s.65  _(FA 2012 Part 2 / s.65)_
- **Life Insurer "I-E" basis** — Income less Expenses; complex calculations  _([T1] 3.2 UK insurance taxation)_
- **Lloyd's of London** — Special rules for syndicate members  _([T1] 3.2 UK insurance taxation)_
- **IPT (Insurance Premium Tax) — UK** — 12% standard; 20% higher rate (travel, mechanical/electrical insurance); 0% reinsurance  _([T1] 3.2 UK insurance taxation)_

### 3.3 EU IPT matrix

**EU IPT matrix**  _(3.3 EU IPT matrix)_

| Country | Standard rate | Notable |
| --- | --- | --- |
| **Germany** | 19% | Plus 22% on fire insurance |
| **France** | 9-30% by class | Auto 18%; health 7%; fire 30% |
| **Italy** | 21.25% standard; 12.5% life; 2.5% professional liability | Plus regional |
| **Spain** | 8% IPT | Plus Consorcio surcharge |
| **Netherlands** | 21% | Aligned with VAT standard |
| **Belgium** | 9.25% | Plus accident insurance surcharge |
| **Sweden** | 32% on auto, fire | Variable by class |
| **Ireland** | 3% | Low rate |

### 3.4 Bermuda corporate income tax (2025)

- **Bermuda 15% CIT** — Bermuda introduced 15% Corporate Income Tax effective 1 January 2025 for Bermuda Constituent Entity Groups (BCEG) within an MNE group with consolidated revenue ≥ EUR 750m. Insurance and reinsurance companies are within scope. Substantial transition relief and intra-group reorganisation rules.  _([T1] 3.4 Bermuda corporate income tax (2025))_

## Section 4 — Captive insurance

**[T1] Common captive jurisdictions:**

**Common captive jurisdictions**  _(Section 4 — Captive insurance)_

| Jurisdiction | Captive count | Notable |
| --- | --- | --- |
| Bermuda | ~700+ | 15% CIT from 2025; long-standing EBT regime; ART (alternative risk transfer) hub |
| Cayman | ~700+ | No CIT; Pillar Two QDMTT 2025 |
| Vermont (US) | ~600+ | US state captive; favorable regulatory; subject to US federal CIT |
| Hawaii (US) | ~250+ | Pacific Rim focus |
| South Carolina (US) | ~190+ | n/a |
| Tennessee (US) | n/a | Growing captive presence |
| Guernsey | ~200+ | n/a |
| Isle of Man | n/a | n/a |
| Singapore | n/a | Captive Insurance Act 2015 |
| Luxembourg | n/a | Reinsurance captive favoured by EU groups |

- **Captive tax planning watch-points** — - Sham insurance / lack of risk transfer challenges (US §831(b) "micro-captives" face IRS scrutiny under Notice 2016-66 and Listed Transaction status confirmed 2023) - BEAT on premium / reinsurance premium payments - Pillar Two now neutralises low-tax captive jurisdictions for in-scope MNE groups  _([T1] Captive tax planning watch-points)_

## Section 5 — Self-checks

- [ ] IFRS 17 transition adjustments to retained earnings documented
- [ ] CSM tracking schedule per group of insurance contracts
- [ ] Reinsurance held position separate from underlying
- [ ] Onerous contract Loss Component identified
- [ ] Discount rate methodology consistent year-over-year
- [ ] DAC capitalisation per IFRS 17 / §848 (US)
- [ ] §831(b) micro-captive Listed Transaction reporting if applicable
- [ ] §953(d) election validity confirmed for foreign captives
- [ ] Pillar Two ETR analysis including CSM-related deferred tax
- [ ] IPT collected and remitted per country
- [ ] Output flags every [T2]/[T3] item for reviewer judgement

## Section 6 — Disclaimer

Insurance accounting and tax are highly specialised. Outputs must be reviewed by credentialed insurance-sector practitioners. The most up-to-date version is at [openaccountants.com](https://openaccountants.com).

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
