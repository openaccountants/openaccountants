---
name: ip-patent-box-matrix
description: "Use this skill whenever a company holding intellectual property asks about preferential tax regimes for income derived from that IP. Trigger on phrases like \"patent box\", \"IP box\", \"innovation box\", \"nexus approach\", \"qualifying IP income\", \"qualifying expenditure\", \"uplift expenditure\", \"modified nexus\", \"BEPS Action 5\", \"Cyprus IP box\", \"Dutch innovation box\", \"UK patent box\", \"Italian patent box\", \"Belgian innovation income deduction\", \"Luxembourg IP box\", \"Irish KDB\", \"knowledge development box\", \"Swiss patent box\", \"Hungary patent box\", \"Singapore IDI\", \"China HNTE\", \"qualifying IP\", \"embedded IP income\", or any request to assess whether a company's IP income qualifies for a preferential tax rate, and to compute the effective rate under the OECD modified nexus approach. Covers 18+ in-force IP regimes that satisfy the BEPS Action 5 modified nexus approach plus historical grandfathering. Does NOT cover: R&D tax credits (see rd-tax-credits-matrix), depreciation of IP assets, withholding tax on royalties (see withholding-tax-matrix), or transfer pricing of IP (see transfer-pricing-workflow-base). ALWAYS read this skill before advising on IP regime eligibility, computing the effective rate, or designing an IP holding structure."
version: 0.1
jurisdiction: GLOBAL
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on:
  - cross-border-workflow-base
category: cross-border
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# IP Patent Box Matrix

## IP / Patent Box Regimes Matrix v0.1

## What this file is

**This file is a content skill that loads on top of `cross-border-workflow-base`.** It implements the global landscape of preferential IP tax regimes that comply with the **OECD BEPS Action 5 Modified Nexus Approach** (published October 2015, refined through the FHTP peer review process).

**Tax year coverage.** Current for **fiscal year 2025**, reflecting:
- OECD FHTP 2024 peer review conclusions
- Hungary patent box regime conformity confirmed
- Cyprus IP box at 80% deduction (effective rate ~2.5%)
- Italian patent box converted in 2021 to an "iper-deduzione" (super-deduction of 110% on R&D costs related to IP — different mechanism from a classic patent box; analysed separately)
- Pillar Two interaction — many IP boxes produce ETRs below 15%, triggering top-up tax exposure (see `pillar-two-globe-minimum-tax.md`)

**The reviewer is the customer of this output.** IP box claims are heavily scrutinised in tax audits. Every output must be reviewed by a credentialed practitioner (typically a Big 4 international tax specialist or local tax counsel) before any claim is filed.

## Section 1 — Scope statement

This skill covers:

- **Modified nexus approach mechanics** — qualifying IP, qualifying expenditure, overall expenditure, uplift, embedded income.
- **Country regime matrix** — rate, scope, mechanism (deduction, exemption, separate rate, super-deduction), grandfathered legacy regimes if any.
- **Computation walk-through** for the principal regimes.
- **Pillar Two interaction** — when patent box income triggers GloBE top-up tax.

This skill does NOT cover:

- **R&D tax credits** — see `rd-tax-credits-matrix.md`.
- **IP amortisation / depreciation** — see country corporate tax skills.
- **Transfer pricing of IP** — see `transfer-pricing-workflow-base.md`.
- **Withholding tax on royalties** — see `withholding-tax-matrix.md`.
- **Italian super-deduction (iper-deduzione)** beyond a reference — fundamentally different mechanism.

## Section 2 — The OECD Modified Nexus Approach (MNA)

### 2.1 The formula

- **Eligible income for the preferential rate** — Eligible IP Income × Nexus Ratio = Income qualifying for the preferential rate Nexus Ratio = (Qualifying Expenditure × 1.3) ÷ Overall Expenditure (capped at 100%)  _([T1])_
- **Qualifying expenditure** — R&D expenditure incurred by the taxpayer directly, plus payments to unrelated third parties for R&D  _([T1])_
- **Overall expenditure** — qualifying expenditure + acquisition costs of the IP + related-party R&D outsourcing  _([T1])_
- **The 30% uplift (uplift expenditure)** — credit for IP improvement value beyond pure R&D spend  _([T1])_

### 2.2 Qualifying IP (under MNA)

- **Three categories of qualifying IP under MNA** — 1. Patents — including pending applications, utility models, plant varieties 2. Copyrighted software 3. Other IP that is "functionally equivalent to a patent" — limited to: Other IP rights that are non-obvious, useful, novel, AND certified through a transparent process by a competent government agency. The OECD restricts category 3 to companies with annual gross revenue < EUR 50 million AND no more than 7.5% of qualifying IP income is from this category  _([T1])_
- **Marketing intangibles excluded** — Marketing intangibles (trademarks, brand value, customer lists) are NOT qualifying IP under MNA. Pre-MNA regimes that included them have been grandfathered or repealed.  _([T1])_

### 2.3 Tracking obligation

- **IP tracking obligation** — Taxpayers must track, on an IP-by-IP basis OR product/family-by-product/family basis: Qualifying expenditure, Overall expenditure, Income from each qualifying IP. Product-family tracking is allowed where IP-by-IP is "exceptionally difficult". The product family must be a coherent class of products with shared underlying IP.  _([T1])_

### 2.4 Grandfathering

- **Grandfathering of pre-MNA regimes** — Pre-MNA regimes for IP existing before 30 June 2016 benefit until 30 June 2021 (with limited national extensions). After this date, all regimes must apply MNA.  _([T1])_

## Section 3 — Country IP regime matrix

### 3.1 Europe

**Europe IP regime matrix**

| Country | Statutory rate | Effective IP rate | Mechanism | Scope |
| --- | --- | --- | --- | --- |
| **Cyprus** | 12.5% CIT | ~2.5% | 80% deduction of qualifying profits | Patents, copyrighted software, other-IP-equivalent-to-patent. Strict nexus tracking. |
| **Ireland — KDB** | 12.5% CIT | 6.25% | 50% deduction (income halved) | Patents, copyrighted software. The IDA's Knowledge Development Box certified for use in family-by-family tracking. |
| **United Kingdom — Patent Box** | 25% CIT | 10% | Reduced rate of 10% on qualifying patent profits | Patents granted by UKIPO, EPO, EEA states. Strict MNA tracking. Streaming or formulary apportionment for income identification. |
| **Netherlands — Innovation Box** | 25.8% CIT (2025) | 9% | Reduced rate of 9% (was 7% pre-2021) | Patents, plant breeder rights, copyrighted software, R&D-WBSO certificates. |
| **Luxembourg — IP Regime (Article 50ter)** | 17% CIT + municipal | ~5.2% (Luxembourg City) | 80% exemption of qualifying net income (i.e., 20% taxed) | Patents, utility models, supplementary protection certificates, copyrighted software. |
| **Belgium — Innovation Income Deduction** | 25% CIT | 3.75% | 85% deduction of qualifying innovation income | Patents, copyrighted software (subject to R&D plan), plant breeders rights, certain orphan drug designations. |
| **Italy — Patent Box (legacy)** | 24% IRES + ~3.9% IRAP | n/a (regime converted to super-deduction 2021) | Until FY2020: 50% exemption. From FY2021: 110% super-deduction of qualifying R&D expenditure related to IP — fundamentally different mechanism | Italy's new mechanism is closer to an R&D super-deduction than a patent box. See italian corporate tax skill. |
| **Spain — Patent Box (Régimen fiscal especial)** | 25% CIT | 10% | 60% reduction of qualifying net income; effective rate 10% | Patents, utility models, supplementary protection certificates, plant variety rights, copyrighted software. |
| **France — IP Reduced Rate** | 25% CIT | 10% | Reduced rate of 10% on qualifying IP income (CGI Art. 238) | Patents, utility certificates, software protected by copyright, plant variety certificates. |
| **Hungary — IP Regime** | 9% CIT | 4.5% | 50% deduction of qualifying royalty income; aggregate cap | Patents, copyrighted software, utility models, supplementary protection certificates. |
| **Poland — IP Box** | 19% CIT (large) / 9% (small) | 5% | Reduced rate of 5% on qualifying income | Patents, utility model rights, copyright on software, plant variety rights. |
| **Switzerland — Federal/Cantonal Patent Box** | Varies by canton (typically 12-21% combined) | ~10% (canton-dependent) | Up to 90% reduction at cantonal level (cap 70% combined relief with R&D super-deduction) | Patents, comparable rights. Cantonal implementation under Federal Act on Tax Reform and AHV Financing (TRAF). |
| **Portugal — Patent Box** | 21% CIT | 10.5% | 50% reduction on qualifying income | Patents, utility models, copyrighted software. |
| **Lithuania — R&D Reduced Rate** | 15% CIT | 5% | Reduced rate of 5% on profits from commercialisation of self-developed assets | Patents, utility models, copyrighted software. |
| **Slovakia — Patent Box** | 21% CIT (large) / 15% (small) | 10.5% / 7.5% | 50% exemption of qualifying income | Patents, utility models, copyrighted software (R&D-derived). |

- ****Cyprus**** — 12.5% CIT  _(Patents, copyrighted software, other-IP-equivalent-to-patent. Strict nexus tracking.)_
- ****Ireland — KDB**** — 12.5% CIT  _(Patents, copyrighted software. The IDA's Knowledge Development Box certified for use in family-by-family tracking.)_
- ****United Kingdom — Patent Box**** — 25% CIT  _(Patents granted by UKIPO, EPO, EEA states. Strict MNA tracking. Streaming or formulary apportionment for income identification.)_
- ****Netherlands — Innovation Box**** — 25.8% CIT (2025)  _(Patents, plant breeder rights, copyrighted software, R&D-WBSO certificates.)_
- ****Luxembourg — IP Regime (Article 50ter)**** — 17% CIT + municipal  _(Patents, utility models, supplementary protection certificates, copyrighted software.)_
- ****Belgium — Innovation Income Deduction**** — 25% CIT  _(Patents, copyrighted software (subject to R&D plan), plant breeders rights, certain orphan drug designations.)_
- ****Italy — Patent Box (legacy)**** — 24% IRES + ~3.9% IRAP  _(Italy's new mechanism is closer to an R&D super-deduction than a patent box. See italian corporate tax skill.)_
- ****Spain — Patent Box (Régimen fiscal especial)**** — 25% CIT  _(Patents, utility models, supplementary protection certificates, plant variety rights, copyrighted software.)_
- ****France — IP Reduced Rate**** — 25% CIT  _(Patents, utility certificates, software protected by copyright, plant variety certificates.)_
- ****Hungary — IP Regime**** — 9% CIT  _(Patents, copyrighted software, utility models, supplementary protection certificates.)_
- ****Poland — IP Box**** — 19% CIT (large) / 9% (small)  _(Patents, utility model rights, copyright on software, plant variety rights.)_
- ****Switzerland — Federal/Cantonal Patent Box**** — Varies by canton (typically 12-21% combined)  _(Patents, comparable rights. Cantonal implementation under Federal Act on Tax Reform and AHV Financing (TRAF).)_
- ****Portugal — Patent Box**** — 21% CIT  _(Patents, utility models, copyrighted software.)_
- ****Lithuania — R&D Reduced Rate**** — 15% CIT  _(Patents, utility models, copyrighted software.)_
- ****Slovakia — Patent Box**** — 21% CIT (large) / 15% (small)  _(Patents, utility models, copyrighted software (R&D-derived).)_

### 3.2 Asia-Pacific

**Asia-Pacific IP regime matrix**

| Country | Statutory rate | Effective IP rate | Mechanism | Scope |
| --- | --- | --- | --- | --- |
| **Singapore — IDI** | 17% CIT | 5%, 10%, or 15% (case-by-case) | Concessionary rate negotiated with EDB | Patents, copyrighted software, broader IP for qualifying activities. Discretionary award. |
| **China — HNTE (High and New Tech Enterprise)** | 25% CIT | 15% | Reduced rate of 15% | Not a pure IP box — broader HNTE designation requires R&D intensity, IP ownership, qualified staff. |
| **South Korea — Tax incentive for IP** | 24.5% CIT | Varies | Effective deduction for income from self-developed IP — but the regime is largely an R&D super-deduction rather than a classic patent box | n/a |
| **India — Patent Box (§115BBF)** | 30% CIT + surcharge | 10% (effective) | Reduced rate of 10% on royalty income from patents developed and registered in India | Patents only, with the inventor a tax resident of India. |

- ****Singapore — IDI**** — 17% CIT  _(Patents, copyrighted software, broader IP for qualifying activities. Discretionary award.)_
- ****China — HNTE (High and New Tech Enterprise)**** — 25% CIT  _(Not a pure IP box — broader HNTE designation requires R&D intensity, IP ownership, qualified staff.)_
- ****South Korea — Tax incentive for IP**** — 24.5% CIT  _(n/a)_
- ****India — Patent Box (§115BBF)**** — 30% CIT + surcharge  _(Patents only, with the inventor a tax resident of India.)_

### 3.3 Notable absences

**Notable absences from patent box regimes**

| Country | Note |
| --- | --- |
| **United States** | No patent box. FDII (Foreign-Derived Intangible Income) deduction effectively reduces the rate on certain foreign-derived intangible income to ~13.125% (post-2018 deduction; under OBBBA P.L. 119-21 effective rate adjusted). FDII is NOT MNA-compliant per OECD review but remains in US law. |
| **Germany** | No patent box. Continues to oppose patent box regimes as harmful tax competition. |
| **Brazil** | No formal patent box; some sector-specific innovation incentives. |
| **Russia — Skolkovo and IT incentive** | Reduced rates for certain IT and R&D categories, broader than a classic patent box. |

- ****United States**** — No patent box. FDII (Foreign-Derived Intangible Income) deduction effectively reduces the rate on certain foreign-derived intangible income to ~13.125% (post-2018 deduction; under OBBBA P.L. 119-21 effective rate adjusted). FDII is NOT MNA-compliant per OECD review but remains in US law.
- ****Germany**** — No patent box. Continues to oppose patent box regimes as harmful tax competition.
- ****Brazil**** — No formal patent box; some sector-specific innovation incentives.
- ****Russia — Skolkovo and IT incentive**** — Reduced rates for certain IT and R&D categories, broader than a classic patent box.

## Section 4 — Computation walk-through

### Step 1 — Identify qualifying IP

- **Steps to identify qualifying IP** — For each potentially qualifying IP asset: - Confirm category (patent, software, equivalent-to-patent under MNA category 3) - Confirm legal protection in the jurisdiction(s) relevant under each regime's nationality rules - Confirm registration / grant date

### Step 2 — Identify IP income

- **IP income types** — Royalty income from licensing the IP; Embedded IP income — income from the sale of products that incorporate the IP, allocated to the IP via a transfer-pricing-style methodology; Gains on disposal of the IP; Damages and compensation in respect of the IP  _([T1])_
- **Allocation of embedded IP income — common methods** — Allocation of embedded IP income is the hardest practical question. Common methods: Comparable royalty rate ÷ sale price; Residual profit split where the IP is a key driver; Profit split between IP-related and non-IP-related profit drivers  _([T1])_

### Step 3 — Compute nexus ratio per IP / family

- **Nexus ratio computation** — Numerator   = Qualifying Expenditure × 1.3 Denominator = Qualifying Expenditure + Acquisition Cost + Related-Party R&D Outsourcing Nexus Ratio = MIN(1, Numerator ÷ Denominator)

### Step 4 — Compute qualifying income

- **Qualifying income formula** — Qualifying Income = (Eligible IP Income − Allocable Costs) × Nexus Ratio Allocable costs include: direct R&D costs (typically expensed during the period), allocated overheads, IP maintenance costs, depreciation of acquired IP.

### Step 5 — Apply the regime rate

- **Tax on qualifying and non-qualifying income** — Tax on Qualifying Income = Qualifying Income × Preferential Rate Tax on Non-Qualifying Income = Non-Qualifying Income × Standard Rate

### Step 6 — Pillar Two interaction (FY 2024+)

- **Pillar Two top-up tax on patent box income** — If the entity's jurisdictional ETR (per `pillar-two-globe-minimum-tax.md`) falls below 15% due to patent box income, the GloBE Top-up Tax applies at the IIR or UTPR level. The patent box benefit may be partially or fully clawed back.  _([T1])_
- **Mitigations under Pillar Two** — The QDMTT in the IP-box country captures the top-up tax locally rather than ceding it to a parent jurisdiction; The Transitional CbCR Safe Harbour may apply through FY 2026 if the simplified ETR test is met (15% for FY 2023/24, 16% for FY 2025, 17% for FY 2026); The substance-based income exclusion (SBIE) may reduce the top-up base where the IP-holding entity has payroll and tangible assets locally  _([T2])_

## Section 5 — Edge cases and special rules

### 5.1 Acquired IP and the nexus ratio

- **Acquired IP treatment in nexus ratio** — Acquired IP is in the denominator (overall expenditure) but NOT in the numerator. Heavy IP acquisition drives nexus ratio toward zero. The 30% uplift on qualifying expenditure partially offsets this but cannot exceed 100%.

### 5.2 Related-party R&D outsourcing

- **Related-party R&D outsourcing treatment** — R&D outsourced to related parties is in the denominator only (not the numerator). This is the central mechanism that pushes substance into the IP-holding jurisdiction.

### 5.3 Family-by-family tracking elections

- **Family tracking election thresholds** — Each regime sets thresholds for when product-family tracking is permitted (typically: IP-by-IP impossible or impracticable). Tax authorities require advance documentation justifying the family.

### 5.4 Tax loss interaction

- **Tax loss year interaction with regime benefit** — In a loss year for IP-related activities, the unused regime benefit is generally lost. Some regimes (e.g., Belgium Innovation Income Deduction, Netherlands Innovation Box) allow carryforward.

### 5.5 Transferred IP

- **Transferred IP rules** — When IP is contributed to or sold to the IP-box company: - The acquisition cost falls into overall expenditure (reducing nexus ratio) - Pre-MNA acquired IP may benefit from grandfathering only until the regime sunset - The OECD's "tracking and tracing" requirement applies — historic expenditure must be reconstructed

### 5.6 Combined IP-box + R&D super-deduction

- **Stacking IP-box and R&D super-deduction** — Some jurisdictions allow stacking (Italy 2021+, Switzerland). Most cap the combined benefit (Switzerland 70%). Verify the country rule.

### 5.7 Singapore IDI — discretionary status

- **Singapore IDI discretionary status** — Singapore's Intellectual Property Development Incentive (IDI) is awarded by the Economic Development Board. The concessionary rate (5/10/15%) is bespoke per company, conditioned on business spend, employment, and IP-creation activities in Singapore.

### 5.8 US FDII and OECD MNA non-compliance

- **US FDII and MNA non-compliance** — FDII applies a partial deduction yielding ~13.125% effective rate on Foreign-Derived Intangible Income. The OECD FHTP has rated FDII as not MNA-compliant. The US has not modified FDII. For Pillar Two purposes, FDII tax is included in Adjusted Covered Taxes — but ETR may still fall below 15%.

## Section 6 — Output specification

The reviewer brief must include:

1. **IP inventory** — every patent, software, plant variety, etc., with legal status and country of protection.
2. **Income allocation** — royalty income identified directly; embedded IP income allocated using a documented methodology.
3. **Nexus ratio computation** per IP or family, with the numerator/denominator tracking sheet.
4. **Qualifying income** per regime per year.
5. **Tax saving** vs the standard rate (sensitivity to nexus ratio and income allocation).
6. **Pillar Two impact** — ETR analysis post-IP-box benefit; top-up tax exposure if any.
7. **Grandfathering schedule** for pre-MNA assets.
8. **Reviewer questions** — open items flagged as [T2] or [T3].

## Section 7 — Self-checks

- [ ] IP category confirmed within the MNA scope (patent / software / equivalent-to-patent).
- [ ] Marketing intangibles excluded from claim.
- [ ] Nexus ratio numerator includes only own + unrelated-party R&D.
- [ ] Acquired IP and related-party outsourcing in denominator only.
- [ ] 30% uplift applied but capped so ratio ≤ 1.
- [ ] Embedded IP income allocated using a defensible TP method.
- [ ] Family tracking justified if used; IP-by-IP otherwise.
- [ ] Pillar Two ETR impact assessed and Top-up Tax modelled.
- [ ] Grandfathering of pre-30-June-2016 IP applied within sunset.
- [ ] Output flags every [T2]/[T3] item for reviewer judgement.

## Section 8 — Prohibitions

- **Prohibitions** — - **Do not** claim a patent box benefit for marketing intangibles (trademarks, brands, customer lists). - **Do not** include related-party R&D in qualifying expenditure — only in overall expenditure. - **Do not** apply Italian "iper-deduzione" alongside another country's classic patent box on the same expenditure — double benefit is prohibited and likely treaty-abused. - **Do not** ignore the Pillar Two top-up tax exposure on patent box benefits — for in-scope MNE groups (>EUR 750m global revenue), the effective benefit may be neutralised. - **Do not** advise on relocating IP to an IP-box jurisdiction without considering exit tax in the originating jurisdiction (often a deemed disposal at fair market value).

## Section 9 — Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Patent box claims face significant audit scrutiny, OECD peer review may move regimes off the approved list, and Pillar Two materially changes the benefit. Every output must be reviewed and signed off by a credentialed international tax practitioner before any claim is filed.

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
