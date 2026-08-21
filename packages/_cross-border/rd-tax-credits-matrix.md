---
name: rd-tax-credits-matrix
description: "Use this skill whenever a company asks about claiming a research and development tax credit, super-deduction, refundable cash incentive, or grant tied to R&D. Trigger on phrases like \"R&D credit\", \"R&D tax credit\", \"R&D super-deduction\", \"RDEC\", \"merged RDEC\", \"ERIS\", \"enhanced R&D intensive support\", \"SR&ED\", \"CIR\", \"Crédit d'Impôt Recherche\", \"Forschungszulage\", \"WBSO\", \"SLIM (Spain)\", \"credito ricerca\", \"patent box vs R&D\", \"R&D in OBBBA\", \"§174 capitalization\", \"§41 R&D credit\", \"JEI / JEU\", \"China R&D super-deduction\", \"India R&D §35\", \"Australia R&DTI\", \"USDA SBIR\", \"OECD frascati definition\", \"qualifying R&D\", or any request to compute eligibility, qualifying expenditure, and benefit value of an R&D incentive. Covers 25+ regimes including the post-2024 UK merged RDEC, US §174 capitalisation rules, France CIR, Germany Forschungszulage, Netherlands WBSO and Innovation Box interaction, China 175% super-deduction, India §35, Australia R&DTI, Canada SR&ED. Does NOT cover: patent box (see ip-patent-box-matrix), depreciation of capitalised R&D, grant accounting beyond reference, customs duty on R&D imports. ALWAYS read this skill before assessing R&D credit eligibility or computing a claim."
version: 0.1
jurisdiction: GLOBAL
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on: - cross-border-workflow-base
category: cross-border
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# RD Tax Credits Matrix

## R&D Tax Credits / Super-Deductions Matrix v0.1

## What this file is

**This file is a content skill that loads on top of `cross-border-workflow-base`.** It maps the world's principal R&D tax incentives — credits, super-deductions, refundable cash incentives — as of mid-2025.

**Tax year coverage.** Current for **fiscal year 2025**, reflecting:
- **UK merged RDEC scheme** (FA 2024) for accounting periods beginning on or after 1 April 2024, replacing the small/mid-size R&D scheme with a single 20% above-the-line credit (~15% post-tax)
- **UK ERIS (Enhanced R&D Intensive Support)** for R&D-intensive loss-making SMEs (40%+ qualifying expenditure ratio) — 86% uplift + 14.5% credit on surrendered loss
- **US §174 R&D capitalisation** still in force per TCJA 2017 amendments (5-year domestic / 15-year foreign amortisation), with continued legislative pressure to restore immediate expensing
- **Germany Forschungszulage** raised to **35%** of eligible costs for SMEs (otherwise 25%) under the Wachstumschancengesetz (March 2024); annual cap of EUR 10 million per claimant
- **France CIR** unchanged at 30% (up to EUR 100m of expenditure; 5% above)
- **Netherlands WBSO** rates and ceilings updated annually
- **OECD BEPS Action 5** Modified Nexus interaction with R&D
- **Pillar Two** — R&D super-deductions can lower ETR below 15% and trigger top-up tax

**The reviewer is the customer of this output.** R&D claims face significant tax-authority scrutiny. Every output must be reviewed by a credentialed practitioner (typically R&D specialist firms or Big 4 R&D advisory) before any claim is filed.

## Section 1 — Scope statement

This skill covers:

- **Qualifying R&D definition** — OECD Frascati Manual and country adaptations
- **Eligibility tests** — taxpayer type, sector, claim history
- **Qualifying expenditure** categories
- **Benefit mechanism** — credit, deduction, refundable cash, super-deduction
- **Filing mechanics and audit risk**
- **Pillar Two interaction**
- **Patent box interaction** (cross-reference)

This skill does NOT cover:

- **Patent box / IP regime** computation — see `ip-patent-box-matrix.md`
- **Grant accounting** beyond reference
- **Country-specific R&D wage subsidies** that are not tax credits
- **Depreciation / amortisation** of capitalised R&D assets — see country corporate tax skills

## Section 2 — The Frascati definition of R&D

- **OECD Frascati Manual (2015 edition) definition of R&D** — R&D comprises creative and systematic work undertaken to increase the stock of knowledge, and to devise new applications of available knowledge. Five criteria, ALL of which must be met: 1. Novel — aimed at new findings; 2. Creative — based on original, not obvious, concepts and hypotheses; 3. Uncertain — outcome uncertain; 4. Systematic — planned and budgeted; 5. Transferable / reproducible — leads to results that could be transferred to / reproduced by others. Three types: Basic research — experimental or theoretical work without specific application; Applied research — original investigation for specific practical aim; Experimental development — systematic work using existing knowledge to produce new materials, products, processes.  _([T1] OECD Frascati Manual (2015 edition))_
- **Local regime adoption of Frascati** — Local regimes adopt Frascati with minor variations. Country-specific exclusions are common (e.g., UK excludes market research; France excludes routine quality control).  _([T1])_

## Section 3 — Country regime matrix

### 3.1 Europe

**Europe R&D regime matrix**  _(Section 3.1 Europe country regime matrix)_

| Country | Mechanism | Headline rate | Notable |
| --- | --- | --- | --- |
| **United Kingdom — Merged RDEC** | Above-the-line credit | **20% gross** (≈15% net) | Single scheme from periods beginning 1 Apr 2024. Subcontractor restriction (no overseas R&D from 1 Apr 2024 with limited exceptions). |
| **United Kingdom — ERIS (Enhanced R&D Intensive Support)** | SME loss surrender | **86% uplift + 14.5% credit** | Loss-making SMEs with ≥30% (reduced from 40% by FA(No.2) 2024) qualifying R&D expenditure ratio. |
| **France — CIR** | Refundable credit (4-year carryforward, refund if not used) | **30%** of qualifying expenditure to EUR 100m; **5%** above | Two-fold uplift for young innovative companies; doubling possible for grad-students hired. |
| **France — CII (Crédit d'Impôt Innovation)** | Credit | **30%** of qualifying innovation expenditure to EUR 400k | For SMEs; covers innovation prototyping (not pure R&D). Extended through 2027. |
| **France — JEI / JEU** | Combined tax + social contribution exemption | Up to 100% CIT exemption first year; 50% second year | Young Innovative Enterprises < 8 years old, R&D-intensive. |
| **Germany — Forschungszulage** | Cash subsidy via tax credit | **25%** (large) / **35%** (SMEs since March 2024) | Cap: EUR 10m eligible expenditure per claimant per year (was EUR 4m). Refundable if no tax liability. |
| **Italy — R&D Credit (Credito d'imposta R&S)** | Credit | **10%** basic research; **5%** development; uplift to 15% for South + women + youth | Reduced from prior 12-50% rates. Combined with Italian Patent Box super-deduction. |
| **Spain — R&D Credit (Deducción I+D+i)** | Non-refundable credit + cash conversion option | **25%** (excess over prior 2-year average) + **42%** on the excess; total cap 50% of CIT; cash-out at 80% of credit | Spanish CIT |
| **Netherlands — WBSO** | Payroll tax reduction | **32%** of first EUR 350k of qualifying R&D wages; **16%** above (rates as updated 2025) | Reduces wage tax/social contributions of R&D employees. Stackable with Innovation Box. |
| **Belgium — Partial Withholding Exemption** | Payroll tax exemption | **80%** exemption on R&D wages for qualifying researchers | Stackable with Innovation Income Deduction. |
| **Belgium — R&D Investment Deduction** | Increased depreciation | **15.5%** investment deduction one-shot OR **22.5%** spread | Choice; combined with patent income deduction. |
| **Ireland — R&D Tax Credit** | Refundable credit | **30%** (raised from 25% in FA 2023) | Cash refund possible over 3 years. |
| **Poland — R&D Tax Relief** | Super-deduction | **100% deduction** of qualifying costs; **200%** for wage costs (loss possible) | Combined with IP Box. |
| **Czech Republic — R&D Deduction** | Deduction | **100%** uplift (200% total) of qualifying expenditure | Multi-year carryforward. |
| **Romania — R&D Super-Deduction** | Super-deduction | **50% uplift** (150% deduction) | Plus 16% credit for certain expenses. |
| **Hungary — R&D Super-Deduction** | Super-deduction | **300%** deduction of qualifying expenditure | Limited to entities with own R&D operations. |
| **Slovakia — R&D Super-Deduction** | Super-deduction | **100% uplift** (200% deduction) | Plus 25% increase year-over-year. |
| **Portugal — SIFIDE II** | Credit | **32.5%** basic + uplift to 50% for incremental expenditure | Specific innovation funds. |
| **Norway — SkatteFUNN** | Credit | **19%** SMEs; **19%** large companies | Cap NOK 25m per project. |
| **Sweden — R&D Payroll Relief** | Payroll tax reduction | **20%** of R&D wages, cap SEK 1.5m/month | Plus general tax depreciation for R&D capex. |
| **Denmark — R&D Super-Deduction** | Deduction | **108%** of R&D expenses through 2025 (down from 130%); refundable for loss-makers up to DKK 25m | Negotiated annual extensions. |
| **Finland — R&D Combined Deduction** | Deduction | **150%** general R&D deduction + **50%** R&D wage uplift (combined max 200%) | Plus payroll tax relief |

### 3.2 Americas

**Americas R&D regime matrix**  _(Section 3.2 Americas country regime matrix)_

| Country | Mechanism | Headline rate | Notable |
| --- | --- | --- | --- |
| **United States — §41 R&D Credit (Federal)** | Non-refundable credit | **20%** regular method (over base period); **14%** ASC simplified | Plus 6% payroll tax offset for QSBs. §174 capitalisation 5/15 years amortisation continues in 2025. |
| **United States — State R&D Credits** | Various | 1.5% (NY)-15% (CA additional) | Stackable with federal |
| **Canada — SR&ED** | Refundable / non-refundable credit | **35% refundable** for CCPCs on first CAD 3m; **15% non-refundable** above and for non-CCPCs | Provincial top-ups in ON, QC, BC, MB, NS, SK |
| **Mexico — R&D Tax Credit** | Credit | **30%** of incremental R&D expenditure | Limited budget; advance allocation required |
| **Brazil — Lei do Bem** | Super-deduction + accelerated depreciation | **60-80%** of R&D expenditure deductible (additional to 100% expense); accelerated depreciation of equipment; reduced IPI on imports | Lucro Real taxpayers only |
| **Chile — R&D Credit (Ley 20.241)** | Credit | **35%** of qualifying R&D, refundable | Annual cap UF 15,000 |
| **Argentina** | Credit | Various sector schemes | Subject to currency and macro instability |
| **Colombia** | Deduction + credit | **100%** deduction + **25%** credit on R&D investment | Annual cap |

### 3.3 Asia-Pacific

**Asia-Pacific R&D regime matrix**  _(Section 3.3 Asia-Pacific country regime matrix)_

| Country | Mechanism | Headline rate | Notable |
| --- | --- | --- | --- |
| **Australia — R&DTI (R&D Tax Incentive)** | Refundable / non-refundable offset | **48.5%** refundable offset for aggregated turnover < AUD 20m; **38.5%** non-refundable for larger | Loss-making refunds available |
| **Japan — R&D Tax Credit** | Credit | **6-14%** of R&D expenditure (base); plus incremental + open innovation uplifts up to **30%** | SMEs higher base rate; multiple stackable categories |
| **China — R&D Super-Deduction** | Super-deduction | **100%** uplift (200% total deduction) for all industries (extended) | Permanent post-2021 expansion; manufacturing 200% historically maintained |
| **India — §35 Income Tax Act** | Super-deduction | **150%** in-house R&D (DSIR-approved); **100%** outside R&D | Reduced from 200% by Finance Act 2017. Plus weighted deduction for scientific research. |
| **Singapore — R&D Tax Deduction (§14C/§14D ITA)** | Super-deduction | **250%** of qualifying R&D expenditure in Singapore (raised from 150% in Budget 2023) | Cash payout option for SMEs |
| **South Korea — R&D Tax Credit** | Credit | **25-40%** SMEs; **15-40%** large (current vs base year) | Higher rates for "new growth engines" sectors |
| **Taiwan — R&D Investment Tax Credit** | Credit | **15%** of qualifying R&D, capped at 30% of CIT | Modified periodically |
| **Indonesia — R&D Super-Deduction** | Super-deduction | Up to **300%** for specified R&D categories | Pre-approval required |
| **Vietnam** | Deduction | 100% expensable; sector incentives separately | n/a |
| **Thailand — Smart Visa / BOI** | Various | Sector-specific | Combined with BOI incentives |
| **Malaysia — R&D Approved Status** | Deduction | **100%** in-house + special tax allowances | Pre-approval by MIDA |

### 3.4 Africa

**Africa R&D regime matrix**  _(Section 3.4 Africa country regime matrix)_

| Country | Mechanism | Headline rate |
| --- | --- | --- |
| **South Africa — §11D R&D Deduction** | Super-deduction | **150%** of qualifying R&D expenditure (pre-approval by DST required) |
| **Egypt** | Limited; sector schemes | n/a |
| **Kenya** | Limited; ICT and pharma sector incentives | n/a |
| **Nigeria** | 20% R&D credit (subject to approval) | n/a |

## Section 4 — Computation walk-through (UK merged RDEC example)

For a UK accounting period beginning on or after 1 April 2024:

### Step 1 — Qualifying activity test

- **BEIS Guidelines on R&D qualifying activity test** — Project seeks an advance in science or technology. Encounters scientific or technological uncertainty that a competent professional could not readily resolve. The advance must be a genuine advance in the relevant overall field, not just for the company.  _([T1] BEIS Guidelines on R&D (formerly DSIT Guidelines))_

### Step 2 — Qualifying expenditure

- **UK qualifying expenditure categories (CTA 2009 Part 13)** — Categories: Staff costs (gross salary, employer NICs, pension); Externally provided workers (EPWs) — restricted to UK workers post-2024; Subcontracted R&D — restricted to UK subcontractors post-2024 (limited overseas exception); Consumable items (utilities, materials transformed in R&D); Software, data, cloud costs (new from 2023); Payments to qualifying bodies (universities, charities, scientific research orgs); Externally licensed R&D resources. Capital expenditure NOT eligible for R&D credit but RDA / R&D Allowances available separately.  _([T1] CTA 2009 Part 13)_

### Step 3 — Compute the credit

- **Merged RDEC formula** — Credit = 20% × Qualifying R&D Expenditure. Credit is above-the-line (treated as taxable income). Net benefit (post-tax) = 20% × QRE × (1 - CT rate) ≈ 15% for main rate 25%. For ERIS (R&D-intensive loss-making SMEs): Uplifted loss = QRE × 186% (the 86% uplift); Surrendered loss credit = uplifted loss × 14.5% ≈ 27% net benefit.  _([T1])_

### Step 4 — Filing

- **UK filing mechanics and audit risk** — Notification of intent to claim required within 6 months of period end if no claim in past 3 years (CT600L). Additional Information Form (AIF) required for all claims from 8 August 2023. Claim period: 2 years from end of accounting period. Audit risk: HMRC has expanded R&D enquiry capacity since 2022; expect requests for technical narratives, project documentation, time records.  _(unsure)_

## Section 5 — Computation walk-through (France CIR example)

### Step 1 — Qualifying activity (CGI Art. 244 quater B)

- **France qualifying activity** — OECD Frascati criteria plus French specifics: Basic research, applied research, experimental development. Includes technological watch (max EUR 60k/yr) and patent expenses (deposit + maintenance + defence).  _([T1] CGI Art. 244 quater B; OECD Frascati criteria)_

### Step 2 — Qualifying expenditure

- **France qualifying expenditure categories** — Researcher and technician wages (with 50% uplift for operating costs — "frais de fonctionnement"); Depreciation of R&D assets; Subcontracted R&D — to approved bodies only; capped at 2× internal R&D spend OR EUR 12m; Patent costs; Standardisation expenses; Young doctors' wages — doubled for first two years post-graduation.  _([T1])_

### Step 3 — Compute the credit

- **CIR computation formula** — CIR = 30% × QRE up to EUR 100m + 5% × QRE above EUR 100m. For overseas territories: 50% on first slice. For young innovative companies: doubled.  _(unsure)_

### Step 4 — Use the credit

- **France CIR usage rules** — Offset against CIT due. Carry forward 3 years. Refund at end of year 4 if unused. Immediate refund for SMEs, JEI, young innovative companies, and loss-making companies in conciliation/safeguard. Pre-financing schemes (BPI France) advance the credit.  _(unsure)_

## Section 6 — US §174 capitalisation interaction

- **US §174 capitalisation rules** — TCJA 2017 amended IRC §174 effective for tax years beginning after 31 December 2021. Key effects: Domestic R&D expenditure must be capitalised and amortised over 5 years (mid-year convention). Foreign R&D expenditure must be capitalised and amortised over 15 years. Affects all R&D expenditure regardless of credit eligibility. §41 R&D credit base is independent of §174 capitalisation. Pending legislation has not restored immediate expensing as of mid-2025; bipartisan support exists but not enacted.  _([T1])_

[T2] Cash-flow timing of US R&D expenditure changed materially. R&D-intensive companies face significant Year 1 tax liabilities they did not have pre-TCJA. The §41 credit partially offsets but does not eliminate the cash impact.

## Section 7 — Pillar Two interaction

- **QRTC classification under Pillar Two** — Qualified Refundable Tax Credits (QRTCs) — i.e., refundable within 4 years — are treated as income in GloBE Income (not as reductions of Covered Taxes). This means refundable credits do not push ETR below 15%. Non-refundable / non-qualified credits reduce Adjusted Covered Taxes, lowering ETR. Heavy reliance on R&D super-deductions in low-tax jurisdictions can trigger top-up tax.  _([T1])_

[T2] By regime:
- US §41 — non-refundable beyond the QSB payroll offset → reduces Covered Taxes → ETR impact
- UK ERIS — credit refundable in 4 years → treated as income → no ETR push
- Germany Forschungszulage — refundable → treated as income
- France CIR — refundable post-4-yr → treated as income → no ETR push if claimed timely
- Australia R&DTI refundable offset — treated as income
- Canada SR&ED refundable (CCPC) — treated as income
- Italy super-deduction — non-refundable reduction → reduces Covered Taxes
- Hungary 300% super-deduction — non-refundable → reduces Covered Taxes
- Netherlands WBSO — refundable via payroll withholding → treated as income

## Section 8 — Edge cases and special rules

### 8.1 Subcontracted R&D and group transactions

- **Subcontracted R&D and group transaction rules** — Most regimes: Allow subcontracted R&D at restricted percentage of own R&D (commonly 65-80%). Restrict related-party subcontractor R&D to within OECD Modified Nexus Approach principles. The contracting party (the R&D commissioner) gets the credit; the contractor cannot also claim.  _(unsure)_

### 8.2 Grants and subsidised R&D

- **Grants and subsidised R&D offset rules** — Most regimes: Reduce the credit base by the amount of grant/state-aid funding received for the same expenditure. Some allow combining (Italy partially).  _(unsure)_

### 8.3 Foreign R&D performed abroad

- **Foreign R&D performed abroad rules by country** — UK (from 2024): generally exclude overseas R&D from claim. France: generally exclude unless within EEA + Norway / Iceland / Liechtenstein. US: include in §41 but §174 forces 15-year amortisation. Germany Forschungszulage: must be performed in Germany; EU sub-contracted possible under conditions.  _(unsure)_

### 8.4 Software development

- **Software development qualification by country** — UK: covered if seeking advance in computer science. US: §41 software covered if functional/process improvement is the goal. France: software R&D yes; routine custom development no.  _(unsure)_

### 8.5 Claim windows and amendments

**Claim windows and amendments by country**  _(unsure)_

| Country | Claim window |
| --- | --- |
| UK | 2 years post-period-end |
| US | 3 years from filing deadline; amended returns possible |
| France | 3 years post-period-end |
| Germany | 4 years generally |
| Canada SR&ED | 18 months from period-end |

### 8.6 Patent box stack

- **R&D credit and patent box stacking by country** — R&D credit and patent box are independent: France: CIR + IP Reduced Rate. UK: RDEC + Patent Box. Belgium: R&D investment deduction + Innovation Income Deduction. Italy: 110% iper-deduzione (now the "patent box replacement") combined with R&D credit. Netherlands: WBSO payroll relief + Innovation Box (the WBSO is partly a gateway condition for Innovation Box).  _(unsure)_

## Section 9 — Output specification

The reviewer brief must include:

1. **R&D project inventory** with technical narrative and Frascati test result per project
2. **Qualifying expenditure schedule** by category and project
3. **Credit/super-deduction computation** per regime claimed
4. **Refundable vs non-refundable analysis** and Pillar Two GloBE Income classification
5. **§174 amortisation schedule** (US claimants)
6. **Filing deadline calendar** per regime
7. **Grant / state-aid offset** schedule
8. **Patent box interaction** — confirm no double-counting; route IP income separately
9. **Audit risk assessment** — documentation status, prior enquiry history
10. **Reviewer questions** — open items flagged as [T2] or [T3]

## Section 10 — Self-checks

- [ ] Frascati criteria applied per project — novelty, creativity, uncertainty, systematic, transferable
- [ ] Qualifying expenditure categories per regime, not assumed by analogy
- [ ] Subcontractor restrictions applied (UK 2024+ overseas restriction)
- [ ] §174 capitalisation modelled separately from §41 credit (US claimants)
- [ ] Refundability tested for Pillar Two QRTC classification
- [ ] Grant / state-aid offset applied to credit base
- [ ] Patent box income excluded from R&D credit base where claimed under patent box
- [ ] Filing deadline plotted with safety margin
- [ ] Additional Information Form / equivalent technical documentation prepared
- [ ] Output flags every [T2]/[T3] item for reviewer judgement

## Section 11 — Prohibitions

- **Prohibitions list** — - Do not claim R&D credits for routine quality control, market research, social science research, or aesthetic/cosmetic activities — these fail the Frascati novelty test - Do not include grants in the qualifying expenditure base when the regime requires offset - Do not advise overseas subcontracting in the UK without confirming the limited 2024 exception applies - Do not stack R&D credit and patent box on the same IP income — Modified Nexus Approach requires separation - Do not treat the §41 US credit as solving the §174 capitalisation cash-flow timing problem — they are distinct - Do not ignore the OECD Pillar Two refundability classification — non-qualified credits push down the jurisdictional ETR  _(unsure)_

## Section 12 — Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. R&D claims face significant audit scrutiny across virtually every jurisdiction. Every output must be reviewed and signed off by a credentialed practitioner (R&D specialist firms, Big 4 R&D advisory, or local equivalent) before any claim is filed.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com).

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
