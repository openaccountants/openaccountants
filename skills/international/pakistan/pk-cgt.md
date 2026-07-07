---
name: pk-cgt
description: Use this skill whenever asked about Pakistan Capital Gains Tax. Trigger on phrases like "Pakistan CGT", "capital gains tax Pakistan", "PSX shares gain Pakistan", "property gain Pakistan", "Section 37A Pakistan", "Section 37 ITO 2001", "immovable property CGT Pakistan", "NCCPL capital gains", "filer vs non-filer CGT Pakistan", "crypto CGT Pakistan", "FBR capital gains", or any question about computing, filing, or reporting capital gains under the Income Tax Ordinance 2001. Scope covers CGT on securities (Section 37A) including PSX-listed shares, modaraba certificates and redeemable capital; CGT on immovable property (Section 37) including the holding-period scale and FBR valuation tables; CGT on other capital assets under Section 37; filer vs non-filer rate differentials; NCCPL collection at source for securities; bank/registrar collection for property; loss set-off and carry-forward; and the uncertain crypto position. ALWAYS read this skill before touching Pakistan CGT work.
jurisdiction: PK
domain: international
tax_year: 2025
reviewed_by: Ibrar Ali
review_status: accountant-reviewed
tier: 1
last_updated: 2026-07-06
---

# pk-cgt

## Pakistan — Capital Gains Tax — Skill v1.0

## Verified rates & thresholds (accountant-reviewed)

Reviewed against the cited tax authorities by **Ibrar Ali** on 2026-06-12.
Items flagged for further clarification are tracked separately and excluded here.
This block is generated from verified `skill_facts` — edit the facts, not the prose.

### pk-cgt

- **Securities §37A (TBC FA 2025)** — 
- **PSX-listed shares — filer** — 15% flat  _(ITO 2001 §37A)_
- **PSX-listed shares — non-filer** — Normal slab rates (up to 45%), with a minimum of 15%  _(ITO 2001 §37A)_
- **Modaraba certs / redeemable capital / listed debt** — Same 15% (filer) / normal slab rates up to 45% with a 15% minimum (non-filer)  _(ITO 2001 §37A)_
- **Collection** — At source by NCCPL on settled trades; investor reconciles in annual return  _(§37A / NCCPL)_
- **Immovable property §37 (illustrative taper — verify FA 2025)** — 
- **Holding ≤ 1 year — filer** — 15% (full statutory rate)  _(ITO 2001 §37)_
- **Holding > 1 ≤ 2 years** — 0.15  _(ITO 2001 §37)_
- **Holding > 2 ≤ 3 years** — 0.15  _(ITO 2001 §37)_
- **Holding > 3 ≤ 4 years** — 0.15  _(ITO 2001 §37)_
- **Holding > 4 years** — 0.15  _(ITO 2001 §37)_
- **Non-filers** — Normal slab rates (up to 45%) with a minimum of 15%  _(ITO 2001 §37)_
- **Deemed proceeds** — Higher of declared consideration and FBR-notified valuation table value  _(ITO 2001 §37)_
- **Collection** — §236C (seller) / §236K (buyer) advance tax at execution  _(§236C / §236K)_
- **Other capital assets (unlisted shares, art, etc.)** — Taxed at normal slab rates under §37 general  _(ITO 2001 §37)_
- **Crypto / virtual digital assets** — Treated as §37 capital asset (FBR position); framework unsettled — flag  _(ITO 2001 §37)_
- **Capital losses** — Ring-fenced — only set off against capital gains  _(ITO 2001 §37/§37A)_
- **Securities loss carry-forward** — 3 tax years  _(ITO 2001 §37A)_
- **Property/other loss carry-forward** — 6 tax years (verify); no carry-back  _(ITO 2001 §37)_
- **Inheritance** — Not a disposal — no CGT on inheritance; base cost carries over to the heir  _(ITO 2001)_

## Section 1 — Quick reference

**Section 1 — Quick reference**

| Field | Value |
| --- | --- |
| Country | Islamic Republic of Pakistan |
| Tax | Capital Gains Tax (CGT) |
| Currency | PKR (Pakistani Rupee, Rs.) |
| Tax year | 1 July to 30 June (TY 2025-26 = 1 July 2025 to 30 June 2026) |
| Primary legislation | Income Tax Ordinance 2001 (ITO 2001) — Sections 37 and 37A |
| Amending instrument | Finance Act 2025 (annual) — rates and brackets revised each FY |
| Tax authority | Federal Board of Revenue (FBR) |
| Securities collection agent | National Clearing Company of Pakistan Limited (NCCPL) |
| Property collection agent | Buyer's bank / property registrar at execution |
| Filing | Annual income tax return — IRIS portal |
| Validated by | Pending — requires sign-off by a Pakistani Chartered Accountant (ICAP) or Cost & Management Accountant (ICMAP) or registered FBR tax practitioner |
| Skill version | 1.0 |

### CGT rate at a glance — TY 2025-26 (verify against current Finance Act)

**CGT rate at a glance — TY 2025-26 (verify against current Finance Act)**

| Asset class | Filer rate | Non-filer rate | Notes |
| --- | --- | --- | --- |
| Securities — PSX-listed shares (Section 37A) | **15% flat** (TBC — FA 2024 set 15%; FA 2025 figure to confirm) | **Normal slab rates (up to 45%), with a minimum of 15%** (TBC) | Collected at source by NCCPL; investor reconciles in annual return |
| Securities — modaraba certificates, redeemable capital, listed debt | 15% flat (TBC) | Normal slab rates up to 45% with a 15% minimum (TBC) | Same Section 37A regime |
| Immovable property — holding ≤ 1 year (Section 37) | **15%** (TBC) | higher slab (TBC) | Full rate band; FBR valuation tables apply |
| Immovable property — holding > 1 year, ≤ 2 years | scaled-down rate (TBC) | higher slab (TBC) | Holding-period scale |
| Immovable property — holding > 2 years | further scaled-down (TBC) | higher slab (TBC) | Continues to scale toward 0% over the statutory ladder |
| Immovable property — beyond statutory holding period | 0% | higher slab may still apply for non-filers (TBC) | Verify with current Finance Act |
| Other capital assets (Section 37 — non-property, non-security) | Normal income slab rates | Normal income slab rates | Treated as income under Section 18 / Section 37 general |
| Crypto / virtual assets | Treated as capital asset under Section 37 (FBR position since 2023) | Same | **Regulatory framework uncertain — flag for client and reviewer** |

**TBC = to be confirmed against the Finance Act 2025 text.** FA 2024 introduced a flat 15% on PSX securities for filers and 30% for non-filers. The FA 2025 figures must be verified against the published Act before use. Where the practitioner cannot confirm the current-year rate, apply the conservative default (see §7).

## Section 2 — Required inputs & refusal catalogue

### Required inputs

Before computing any Pakistan CGT position, obtain:

1. **Identity & residency** — taxpayer name, NTN/CNIC, residency status (resident, non-resident), **Active Taxpayer List (ATL) status** (filer vs non-filer) at the disposal date.
2. **Asset description** — class (PSX-listed security, unlisted share, modaraba certificate, immovable property, crypto, other).
3. **Acquisition data** — acquisition date, acquisition cost (with documentary support), incidental costs of acquisition.
4. **Disposal data** — disposal date, disposal proceeds (gross consideration), incidental costs of disposal (brokerage, CVT, legal, registration).
5. **Holding period** — exact days/months from acquisition to disposal (critical for both Section 37A securities and Section 37 immovable property).
6. **For securities** — NCCPL Capital Gains Tax certificate (the annual CGT statement issued to the investor); broker statements; any CDC records.
7. **For immovable property** — FBR-notified valuation for the locality (DC value / FBR value), buyer's bank withholding certificate, property registrar receipt, allotment / transfer letters.
8. **Filer / non-filer evidence** — ATL status snapshot at the date of disposal (FBR publishes ATL weekly).
9. **Prior-year capital losses** — losses brought forward and the asset class against which they may be set off (ring-fenced rules apply).
10. **Treaty position** — for non-residents, the relevant double-tax treaty article on capital gains.

### Refusal catalogue

- **Acquisition cost is unknown or undocumented** — Cannot compute gain; estimates require reviewer sign-off
- **Asset acquired by gift or inheritance with no FBR-acceptable valuation** — Need market-value documentation for base cost
- **Disposal of partnership / AOP interest** — Treatment uncertain; refer to FBR specialist guidance
- **Disposal of business assets attached to a trading concern (potentially income under normal heads)** — Possible income-tax characterisation rather than CGT — refer to specialist
- **Crypto / virtual asset disposal where the taxpayer needs a binding position** — Regulatory framework is unsettled — provide indicative computation only, do not finalise
- **Cross-border disposal where double-tax-treaty relief is in play** — Requires bilateral treaty analysis — out of scope of this skill
- **Disposal of mineral / oil & gas / petroleum rights** — Sector-specific overlay — out of scope
- **Trust / estate disposals or testamentary distributions** — Specialist regime — out of scope
- **Disposal of immovable property where FBR valuation table value materially diverges from declared consideration** — Valuation dispute risk — refer to a property tax specialist
- **Finance Act 2025 rate cannot be verified** — STOP and confirm current-year rate before computing

## Section 3 — Tier 1 — Section 37A securities vs Section 37 property vs Section 37 other

### 3.1 Section 37A — Capital gains on disposal of securities

- **Scope** — Section 37A applies to "securities" as defined, which includes: - Shares of a **public company** listed on the Pakistan Stock Exchange (PSX). - Vouchers of Pakistan Telecommunication Corporation, modaraba certificates, instruments of redeemable capital. - Debt securities (corporate debt instruments listed in Pakistan), Term Finance Certificates, Sukuks. - Units of an open-end mutual fund and units of an exchange-traded fund (where so prescribed).
- **Computation** — Chargeable gain = Disposal proceeds − Acquisition cost − Incidental costs of acquisition − Incidental costs of disposal CGT payable = Chargeable gain × applicable Section 37A rate (see §1 rate table — verify against current Finance Act).
- **Rate structure** — Historically Section 37A operated a holding-period sliding scale (e.g. 15% / 12.5% / 10% / 7.5% / 0%) decreasing as holding period lengthened. The **Finance Act 2024 moved to a flat 15% on PSX-listed securities for filers and 30% (or higher) for non-filers**, removing the holding-period taper for new acquisitions on or after a specified date. **The Finance Act 2025 figure must be confirmed in each engagement.**
- **Collection at source — NCCPL** — The National Clearing Company of Pakistan Limited operates the CGT collection mechanism for PSX trades: - NCCPL calculates the gain/loss on each settled trade based on the trade book and reference acquisition data. - CGT is deducted at source from the proceeds and remitted to FBR. - NCCPL issues an **annual CGT certificate** to the investor. - The investor reconciles the NCCPL-collected CGT against the position on the annual return; any over-collection is refundable, any under-collection (e.g. off-market trades) is payable on filing.
- **Filer vs non-filer** — ATL status at the date of each disposal determines the rate. A taxpayer who becomes a filer mid-year cannot retrospectively reduce the rate on earlier non-filer disposals.

### 3.2 Section 37 — Capital gains on immovable property

- **Scope** — Section 37 charges capital gains on the disposal of "capital assets" not otherwise charged under another head. The dominant category is **immovable property** (land and buildings) held by individuals and AOPs.
- **Holding-period scale** — Pakistan operates a **holding-period taper** on immovable property — the rate steps down as the holding period lengthens, reaching 0% beyond a statutory ceiling. The exact ladder is reset annually by the Finance Act. As an illustrative example only (pre-FA 2024 form):

**Holding period — Filer rate (illustrative) table**

| Holding period | Filer rate (illustrative) |
| --- | --- |
| ≤ 1 year | full statutory rate (e.g. 15%) |
| > 1 year, ≤ 2 years | reduced (e.g. 15%) |
| > 2 years, ≤ 3 years | further reduced (e.g. 15%) |
| > 3 years, ≤ 4 years | further reduced (e.g. 15%) |
| > 4 years | 15% |

- **Verify schedule** — **Verify the current schedule against FA 2025 before applying.** The Finance Act 2024 substantially revised the property CGT ladder and introduced **normal slab rates (up to 45%) with a minimum of 15% for non-filers** across all holding bands.
- **FBR valuation tables** — Disposal proceeds for Section 37 immovable property purposes are taken to be **the higher of** the declared consideration and the **FBR-notified valuation table value** for the locality (and, separately, the provincial DC value where higher). The same rule applies to acquisition cost where the original acquisition was at below-market value to a connected party.
- **Collection at source — buyer's bank / registrar** — Section 236C (advance tax on sale) and Section 236K (advance tax on purchase) are administered at the moment of registration / execution. The CGT under Section 37 is reconciled in the annual return; the advance taxes collected under 236C / 236K are credited.

### 3.3 Section 37 — other capital assets

- **Computation and treatment** — For capital assets that are neither Section 37A securities nor immovable property (e.g. private company shares not listed on PSX, certain intangibles, art, collectibles, **crypto** on the FBR's current administrative position), gains are computed under Section 37 general: Chargeable gain = Disposal proceeds − Acquisition cost − Incidental costs The gain is then brought into the taxpayer's income and taxed at the **normal slab rates** under Section 18, subject to any reduction for long-term holding where the relevant Finance Act provides one.

### 3.4 Connected persons & market value

- **Connected persons & market value** — Where a disposal is between connected persons or at below-market consideration, FBR may substitute market value. For immovable property, the FBR valuation table is the default benchmark. For unlisted shares, a fair valuation (net asset value or DCF) may be required.

### 3.5 Capital losses — set-off and carry-forward

- **Capital losses are ring-fenced** — they may only be set off against capital gains, not against income from other heads.
- **Section 37A securities losses** — carry-forward up to 3 tax years against future Section 37A gains.
- **Section 37 non-securities losses (immovable property, other capital assets)** — carry-forward up to 6 tax years against future Section 37 gains (verify).
- **Connected-person disposal losses** — Losses on disposals between connected persons may be restricted to subsequent gains on disposals to the same connected person (anti-avoidance).
- **Carry-back** — Losses cannot be carried back.

## Section 4 — Tier 2 — non-resident CGT, treaty relief, exemptions

### 4.1 Non-resident CGT

- **Non-resident chargeable gains** — A non-resident is chargeable to Pakistan CGT on gains arising from the disposal of: - **Shares in a Pakistani company** (whether listed or unlisted) — Section 101(6) source rule. - **Immovable property situated in Pakistan**. - **Business assets connected with a Pakistan permanent establishment**. For PSX-listed securities, the non-resident gain is collected by NCCPL in the same way as for residents, subject to any treaty override. For immovable property, the buyer's bank withholds and remits under Sections 236C / 37 collection mechanisms. Non-resident filer/non-filer determination follows the same ATL rule, although non-residents are often non-filers by default for Pakistan purposes unless they have voluntarily filed.

### 4.2 Treaty relief

- **Treaty allocation (Article 13 style)** — Pakistan has a wide DTT network. Most treaties follow the OECD-style **Article 13** allocation: - Gains on **immovable property situated in Pakistan** — taxable in Pakistan. - Gains on **shares deriving > 50% of value from Pakistan immovable property** — generally taxable in Pakistan (land-rich company rule). - Gains on other shares — varies by treaty; some allocate exclusively to residence, some to source, some to both. - Gains on other personal property — generally taxable only in the state of residence of the alienator. A non-resident wishing to claim treaty relief must produce a **Certificate of Tax Residence** issued by the home tax authority and may need to apply to FBR for a treaty exemption certificate before NCCPL or the bank will release withholding.

### 4.3 Statutory exemptions and reduced rates

**Statutory exemptions and reduced rates**

| Exemption / reduction | Authority | Notes |
| --- | --- | --- |
| Gain on disposal of a self-occupied residence within prescribed limits | Specific Finance Act provisions (verify current year) | Subject to area and value limits |
| Inherited assets — no CGT on inheritance event | ITO 2001 — inheritance is not a "disposal" | Base cost carries over to the heir; CGT applies on the heir's subsequent disposal |
| Gifts to specified relatives | ITO 2001 — gift rules | Treated as non-arm's length; base cost may carry over |
| Government securities / federal bonds (in specified circumstances) | Schedule II exemptions | Verify against current schedule |
| Mutual fund unit redemptions (specific regimes) | Section 37A and Second Schedule | Verify whether mutual fund regime applies the Section 37A flat rate or a separate concessionary rate |
| First sale of immovable property by an original allottee (in specified housing schemes) | Specific Finance Act concessions | Verify current-year availability |

### 4.4 Crypto / virtual digital assets

- **FBR administrative position on crypto** — FBR's administrative position since approximately 2023 is that **crypto and virtual digital assets are capital assets** and gains on their disposal are chargeable under Section 37. However: - There is **no specific statutory regime** for crypto in the ITO 2001 as of TY 2025-26. - The **State Bank of Pakistan** has historically discouraged or prohibited crypto transactions through the banking system. - A formal **Virtual Digital Asset framework** is reportedly under development but not finalised as of skill publication. - **Conservative default:** treat any reported crypto gain as a Section 37 capital gain at normal slab rates, advise the client that the regulatory framework is unsettled, and flag for specialist review before any binding position is taken.

## Section 5 — Worked examples

**All rates below are illustrative.** Confirm current Finance Act 2025 rates before producing a final computation.

### Example A — PSX share sale (resident individual, filer)

Mr. Ahmed, a Karachi-resident filer, sold listed shares on the PSX through his broker during TY 2025-26.

**Disposal facts table**

| Disposal | Acquisition | Holding | Proceeds (Rs.) | Cost (Rs.) | Brokerage (Rs.) |
| --- | --- | --- | --- | --- | --- |
| Co. X — 10,000 shares | Aug 2024 | 11 months | 4,500,000 | 3,000,000 | 22,500 |
| Co. Y — 5,000 shares | Jan 2023 | ~30 months | 2,200,000 | 1,800,000 | 11,000 |

**Computation table**

| Line item | Amount (Rs.) |
| --- | --- |
| Co. X — gain (4,500,000 − 3,000,000 − 22,500) | 1,477,500 |
| Co. Y — gain (2,200,000 − 1,800,000 − 11,000) | 389,000 |
| **Aggregate Section 37A chargeable gain** | **1,866,500** |
| CGT at 15% filer rate (illustrative — confirm FA 2025) | **279,975** |

The CGT of Rs. 279,975 is collected at source by NCCPL on the settled trades and reported on the NCCPL annual CGT certificate. Mr. Ahmed reconciles the NCCPL-collected amount against this computation in his IRIS return and pays / claims refund of any difference.

### Example B — Immovable property sale (resident individual, filer)

Mrs. Khan, a Lahore-resident filer, sold a residential plot in DHA Lahore in March 2026. She acquired it in September 2022.

**Computation table**

| Line item | Amount (Rs.) |
| --- | --- |
| Declared disposal proceeds | 25,000,000 |
| FBR valuation table value | 28,000,000 |
| **Deemed proceeds (higher of declared and FBR value)** | **28,000,000** |
| Less: Acquisition cost (Sep 2022) | (12,000,000) |
| Less: Incidental acquisition costs (CVT, stamp duty, registration) | (450,000) |
| Less: Incidental disposal costs (legal, agent commission) | (550,000) |
| **Chargeable gain** | **15,000,000** |

- **Holding period band** — Holding period = ~42 months = > 3 years. Apply the **Section 37 immovable property holding-period rate** for the > 3 ≤ 4 year band per the current Finance Act 2025 schedule. Assuming the illustrative > 3 ≤ 4 year filer rate is 7.5%:

**CGT at illustrative rate table**

| Line item | Amount (Rs.) |
| --- | --- |
| CGT at illustrative 7.5% | **1,125,000** |

The buyer's bank will have withheld advance tax under Section 236C at the execution. Mrs. Khan claims credit for the 236C withholding in her annual return and pays / claims refund of the balance against the Section 37 CGT liability.

### Example C — Crypto disposal (resident individual)

Mr. Iqbal, a resident filer, acquired BTC in 2023 for Rs. 2,000,000 (equivalent at conversion) and sold it in TY 2025-26 for Rs. 5,500,000 via an offshore exchange. Funds were repatriated to a Pakistan bank account.

**Indicative treatment table**

| Line item | Amount (Rs.) |
| --- | --- |
| Disposal proceeds | 5,500,000 |
| Less: Acquisition cost | (2,000,000) |
| Less: Exchange / transaction fees | (50,000) |
| **Indicative chargeable gain (Section 37 — general capital asset)** | **3,450,000** |
| Tax at normal slab rate (illustrative — depends on Mr. Iqbal's total taxable income) | **TBC** |

> The regulatory framework for virtual digital assets in Pakistan is unsettled. The FBR's administrative position treats crypto disposals as Section 37 capital gains, but there is no specific statutory regime and the State Bank of Pakistan has historically restricted crypto transactions. This computation is indicative only. Specialist review is required before filing.

## Section 6 — Filing & payment

### 6.1 Annual return (resident individuals & AOPs)

- **Annual return requirements** — - CGT computation is part of the **annual income tax return** filed on the **IRIS portal** of FBR. - **Filing deadline**: **30 September** following the end of the tax year (TY 2025-26 → due 30 September 2026), unless extended by FBR notification. - The return must include: - **Wealth statement** (Section 116) reconciling opening and closing wealth — disposals must reconcile to wealth movements. - **Schedule of capital gains** segregated by Section 37A (securities) and Section 37 (immovable property / other). - **NCCPL CGT certificate** values for securities. - **236C / 236K** withholding tax credits for immovable property.

### 6.2 Companies

- **Company filing and taxation** — - Companies file their return under the same regime; **deadline 31 December** following the financial year end (Section 118). - CGT on company-held securities is collected by NCCPL in the same way and reconciled in the corporate return. - Companies are generally taxed on capital gains as part of their normal taxable income subject to Section 37A flat rates for securities; non-securities gains for a company may be taxed at the corporate rate depending on characterisation.

### 6.3 Collection at source

**Collection at source**

| Asset class | Collection mechanism | Recovery |
| --- | --- | --- |
| PSX-listed securities | NCCPL collects CGT at source on each settled trade; annual CGT certificate issued to investor | Reconcile in IRIS return; refund or top-up via the annual return |
| Immovable property — sale | Section 236C advance tax withheld by the registrar / society at execution | Credited against Section 37 CGT on the annual return |
| Immovable property — purchase | Section 236K advance tax withheld from buyer | Not creditable against seller's CGT — this is buyer's advance income tax |

### 6.4 Filer vs non-filer mechanics

- **Filer/non-filer mechanics** — - **Active Taxpayer List (ATL) status** at the date of each disposal determines the rate applied by NCCPL or the bank. - ATL is published **weekly** by FBR. A taxpayer's status can flip during the year if a return is filed late after the cut-off. - **Late filers** may move onto the ATL with a surcharge but the higher non-filer rate applied at the time of disposal is **not refunded** retrospectively in most cases — confirm with current FBR guidance. - Non-filer rates are typically **double or higher** than filer rates on both securities and property — the differential is a material planning point.

### 6.5 Records & retention

- **Records & retention** — - Retain acquisition documents, broker / NCCPL statements, FBR valuation evidence, transfer deeds, and bank withholding certificates for **6 years** from the end of the relevant tax year. - For property, retain documents covering the entire holding period plus 6 years post-disposal. - Crypto / virtual digital asset transactions — retain exchange statements, wallet addresses, and conversion-rate evidence; specialist advice recommended given the unsettled regime.

## Section 7 — Conservative defaults

**Conservative defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown acquisition cost | STOP — cannot compute gain |
| Acquisition by gift / inheritance with no valuation | Obtain valuation evidence; if unavailable, STOP |
| Current-year Finance Act rate cannot be confirmed | STOP — confirm rate before producing a final figure; do not estimate from prior years |
| Unknown ATL status at disposal date | Assume **non-filer** rate (conservative — higher liability) |
| Holding period of immovable property unclear at month level | Apply the **shorter** holding band (higher rate) until evidence resolves it |
| Declared property consideration below FBR valuation table | Use the higher of declared / FBR / DC value (conservative) |
| Routine repair vs capital enhancement ambiguous | Treat as routine repair → not deductible |
| Connected-party disposal at below market | Substitute FBR valuation / market value |
| Crypto disposal requires a binding position | Produce indicative figure only; advise specialist review; do not finalise |
| Cross-border disposal with possible treaty relief | STOP — refer to specialist treaty review |
| Non-resident seller, treaty certificate not in hand | Apply full non-resident rate without treaty relief until certificate produced |
| Capital loss carry-forward eligibility unclear | Treat as ring-fenced within its own class; do not net across Section 37 and Section 37A |
| Disposal of partnership / AOP interest | STOP — refer to specialist |

## Section 8 — Sources

1. **Income Tax Ordinance 2001 (ITO 2001)** — primary statute; Sections 37 and 37A.
2. **Income Tax Rules 2002** — procedural and computational rules.
3. **Finance Act 2024** — introduced the flat 15% (filer) / 30% (non-filer) regime on PSX securities under Section 37A; revised the immovable property holding-period schedule.
4. **Finance Act 2025** — annual amendments to Sections 37 and 37A rates and brackets (**confirm exact figures before applying**).
5. **NCCPL Capital Gains Tax mechanism** — National Clearing Company of Pakistan Limited rules for collection at source on PSX-settled trades.
6. **FBR Circulars and SROs** — including FBR-notified valuation tables for immovable property (locality-specific SROs) and FBR Circulars on Section 37A operation.
7. **FBR IRIS portal** — return filing infrastructure; current return forms incorporate the Section 37 / 37A schedules.
8. **Active Taxpayer List (ATL)** — FBR weekly publication used to determine filer / non-filer rates.
9. **State Bank of Pakistan circulars** — relevant to crypto / virtual digital asset position.
10. **Double Tax Treaties** — Pakistan's bilateral treaty network; Article 13 (capital gains) of each relevant treaty.
11. **ICAP and ICMAP technical guidance** — practitioner commentary on Finance Act changes and Section 37 / 37A operation.
12. **FBR Information Circulars on Capital Gains** — including the post-FA 2024 circulars clarifying the flat-rate regime on PSX securities.

## End of Skill — Pakistan CGT v1.0

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
