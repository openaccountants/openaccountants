---
name: pillar-two-globe-minimum-tax
description: Use this skill whenever a multinational enterprise (MNE) group with consolidated revenue at or above EUR 750 million asks about the OECD Pillar Two / GloBE (Global Anti-Base Erosion) 15% global minimum tax. Trigger on phrases like "Pillar Two", "GloBE", "global minimum tax", "15% minimum tax", "IIR", "UTPR", "QDMTT", "domestic top-up tax", "GloBE Information Return", "GIR", "covered taxes", "transitional CbCR safe harbour", "substance-based income exclusion", or any request to assess Pillar Two exposure, compute a top-up tax, or determine which entities in a group are in scope. This skill covers the OECD GloBE Model Rules (December 2021), the Commentary (March 2022) and Administrative Guidance through 2024, plus the EU implementing Directive 2022/2523. It does NOT cover Pillar One (Amount A or Amount B), country-by-country reporting (CbCR) under BEPS Action 13, or US GILTI/CAMT as standalone regimes (but does map their interaction). Always read this skill before computing top-up tax, advising on jurisdictional ETRs, or designing group restructurings affected by GloBE.
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

# Pillar Two GLOBE Minimum Tax

## Pillar Two / GloBE 15% Global Minimum Tax v0.1

## What this file is

**This file is a content skill that loads on top of `cross-border-workflow-base`.** It implements the OECD Pillar Two Global Anti-Base Erosion (GloBE) rules and the EU Minimum Tax Directive 2022/2523, in force from fiscal years starting on or after 31 December 2023 (IIR) and 31 December 2024 (UTPR).

**Tax year coverage.** Current for **fiscal year 2025** as of currency date, reflecting OECD Administrative Guidance through July 2024 and the Agreed Administrative Guidance issued in February, July and December 2023.

**The reviewer is the customer of this output.** Pillar Two computations are jurisdiction-by-jurisdiction and ETR-sensitive; every output must be reviewed by a credentialed practitioner (typically a Big 4 or equivalent international tax specialist) before filing the GloBE Information Return.

## Section 1 — Scope statement

This skill covers:

- **Scope test** — consolidated group revenue ≥ EUR 750 million in at least 2 of the 4 preceding fiscal years  _(Article 1.1 OECD Model Rules / Article 2 EU Directive)_
- **Three charging mechanisms** — Income Inclusion Rule (IIR), Undertaxed Profits Rule (UTPR), Qualified Domestic Minimum Top-up Tax (QDMTT)
- **GloBE Income / Loss computation** — starting from financial accounting net income, with the standard adjustments  _(Article 3)_
- **Adjusted Covered Taxes** — including current and deferred tax with the substance limitations  _(Article 4)_
- **Effective Tax Rate (ETR) computation by jurisdiction** — Effective Tax Rate (ETR) computation by jurisdiction  _(Article 5.1)_
- **Top-up Tax computation** — including the Substance-Based Income Exclusion (SBIE) and the de minimis exclusion  _(Article 5.3 (SBIE); Article 5.5 (de minimis))_
- **Transitional CbCR Safe Harbour** — Through fiscal years beginning before 1 January 2027 and ending before 1 July 2028
- **Permanent Safe Harbours** — where adopted (QDMTT safe harbour, simplified calculations safe harbour for non-material constituent entities)
- **GloBE Information Return (GIR) filing mechanics** — including the central filing election under Article 8.1  _(Article 8.1)_
- **Interaction with other regimes** — Interaction with US GILTI (treated as a non-qualified blended CFC tax post-2025), US CAMT, UK MTT/DTT, Korean Hyper-Local Adopting Pillar Two, Japanese IIR, and EU Member State implementations

This skill does NOT cover:

- **Pillar One (Amount A or Amount B)** — see `pillar-one-amount-a-b.md` (forthcoming).
- **Country-by-Country Reporting (CbCR) under BEPS Action 13** as a standalone obligation — covered by `cbcr-beps-13.md` (forthcoming).
- **CFC regimes** that exist independently of Pillar Two (e.g., German Hinzurechnungsbesteuerung, UK CFC charge) — see country corporate tax skills.
- **Detailed deferred tax accounting** under IAS 12 or ASC 740 — see `ifrs-local-gaap-reconciliation.md`.
- **Transfer pricing methodology** — see country `*-transfer-pricing.md` skills and `transfer-pricing-workflow-base.md`.

## Section 2 — Filing requirements and key deadlines

### Scope test (Article 1.1)

- **Scope test definition** — A group is in scope where consolidated revenue per the Ultimate Parent Entity (UPE) consolidated financial statements is **EUR 750 million or more** in **at least two of the four fiscal years immediately preceding the tested fiscal year**.  _(Article 1.1)_
- **[T1] Mechanical test** — 1. Identify the UPE and its consolidated financial statements prepared under an Acceptable Financial Accounting Standard. 2. For each of the four preceding fiscal years, read consolidated revenue. 3. If two or more of those years show revenue ≥ EUR 750m → the group is in scope for the tested year. 4. If the tested year is less than 12 months → annualise revenue by multiplying by 365 / number of days.  _(Article 1.1)_
- **Excluded entities** — governmental entities, international organisations, non-profit organisations, pension funds, investment funds that are UPEs, real estate investment vehicles that are UPEs, and entities at least 95% owned by such excluded entities (subject to conditions)  _(Article 1.5)_

### Filing deadlines

**Filing deadlines**  _(Article 8.1.6 OECD Model Rules; Article 44 EU Directive)_

| Filing | Deadline | Source |
| --- | --- | --- |
| GloBE Information Return (GIR) | 15 months after the end of the fiscal year; **18 months for the first GIR** of a group | Article 8.1.6 OECD Model Rules; Article 44 EU Directive |
| QDMTT return | Generally same as the GIR but determined by local law; many jurisdictions align with the 15/18-month rule | National implementation |
| Notification of filing entity | Generally 15/18 months; some jurisdictions require an earlier notification (e.g., UK: 6 months) | National implementation |
| Top-up tax payment | Determined by local law of the imposing jurisdiction; usually aligned with the GIR | National implementation |

- **[T1] First year deadlines for a calendar-year group** — First fiscal year subject to IIR: **2024** (year ending 31 December 2024). First GIR due: **30 June 2026** (18 months after 31 December 2024). First UTPR fiscal year: **2025** (year ending 31 December 2025), GIR due **30 June 2027**.

## Section 3 — Rates and thresholds

**Rates and thresholds table**  _(Article 5.2.1 OECD Model Rules)_

| Item | Amount | Source |
| --- | --- | --- |
| Minimum effective tax rate | **15%** | Article 5.2.1 OECD Model Rules |
| Group revenue scope threshold | EUR 750 million | Article 1.1 |
| De minimis revenue threshold | < EUR 10 million in jurisdiction | Article 5.5.1(a) |
| De minimis income threshold | < EUR 1 million in jurisdiction | Article 5.5.1(b) |
| SBIE payroll carve-out (2025) | 9.6% of eligible payroll | Article 9.2 transitional rates |
| SBIE payroll carve-out (steady state from 2033) | 5% | Article 5.3.3 |
| SBIE tangible asset carve-out (2025) | 7.8% of eligible tangible assets | Article 9.2 |
| SBIE tangible asset carve-out (steady state from 2033) | 5% | Article 5.3.4 |
| Transitional CbCR safe harbour — de minimis | Revenue < EUR 10m AND profit < EUR 1m | Agreed Admin Guidance Dec 2022 |
| Transitional CbCR safe harbour — simplified ETR | 15% (FY 2023/24), 16% (FY 2025), 17% (FY 2026) | Agreed Admin Guidance Dec 2022 |
| Transitional CbCR safe harbour — routine profits | Profit ≤ SBIE for that jurisdiction | Agreed Admin Guidance Dec 2022 |
| UTPR transition exemption (UPE jurisdiction) | Excludes UPE jurisdiction from UTPR allocation for FY beginning before 31 Dec 2026 and ending before 31 Dec 2027 if UPE jurisdiction has nominal corporate tax rate ≥ 20% | Article 9.3.5 |

**[T1] SBIE rates by year (Article 9.2 transitional table)**  _(Article 9.2)_

| Fiscal year beginning in | Payroll % | Tangible assets % |
| --- | --- | --- |
| 2023 | 10.0% | 8.0% |
| 2024 | 9.8% | 7.8% |
| 2025 | 9.6% | 7.8% |
| 2026 | 9.4% | 7.6% |
| 2027 | 9.2% | 7.4% |
| 2028 | 9.0% | 7.2% |
| 2029 | 8.2% | 6.6% |
| 2030 | 7.4% | 6.0% |
| 2031 | 6.6% | 5.4% |
| 2032 | 5.8% | 5.2% |
| 2033 onwards | 5.0% | 5.0% |

## Section 4 — Computation rules

### Step 1 — Determine in-scope status

- **Determine in-scope status** — Apply the scope test in Section 2. If out of scope → STOP. Document the test for the GIR notification (some jurisdictions require even out-of-scope notification).

### Step 2 — Identify constituent entities (CEs)

- **Constituent entity** — A constituent entity is any entity included in the consolidation, or excluded only on size/materiality grounds, including permanent establishments. Map every CE by jurisdiction.  _(Article 1.3)_
- **[T1] For each CE, record** — Legal name and tax identifier; Jurisdiction of tax residence (or location of PE); Whether it is a stateless CE, investment entity, insurance investment entity, flow-through, or hybrid; Whether it qualifies as a minority-owned subgroup; Ownership chain back to the UPE

### Step 3 — Compute GloBE Income or Loss for each CE (Article 3)

- **Starting point** — Start from **Financial Accounting Net Income or Loss** before consolidation adjustments. Apply the standard adjustments.  _(Article 3)_

**GloBE Income adjustments table**  _(Article 3.2.1)_

| Adjustment | Direction | Rule |
| --- | --- | --- |
| Net taxes expense | Add back | Article 3.2.1(a) |
| Excluded dividends (≥10% ownership held ≥12 months OR portfolio) | Subtract | Article 3.2.1(b) |
| Excluded equity gains/losses | Subtract / Add back | Article 3.2.1(c) |
| Asymmetric foreign exchange gains/losses | Adjust | Article 3.2.1(g) |
| Policy disallowed expenses (illegal payments, fines > EUR 50,000) | Add back | Article 3.2.1(h) |
| Prior period errors and accounting principle changes | Adjust | Article 3.2.1(i) |
| Accrued pension expense difference | Adjust | Article 3.2.1(j) |
| Stock-based compensation election | Optional adjust | Article 3.2.2 |
| Arm's length adjustment for intra-group transactions | Adjust | Article 3.2.3 |
| Refundable tax credits (qualified vs non-qualified) | Treated as income / reduction of tax | Article 3.2.4; Admin Guidance Jul 2023 |
| Intra-group financing arrangement (Admin Guidance Feb 2023) | Disregard | Article 3.2.7 |

- **Aggregation to jurisdictional level** — Then aggregate to jurisdictional level: sum GloBE Income/Loss for all CEs in the same jurisdiction (with allocation rules for PEs, flow-throughs, and tax-transparent entities per Articles 3.4-3.5).  _(Articles 3.4-3.5)_

### Step 4 — Compute Adjusted Covered Taxes for each CE (Article 4)

- **Covered Taxes (included)** — Taxes on income or profits of the CE; Taxes imposed in lieu of corporate income tax; Taxes on retained earnings and corporate equity; Taxes on distributed profits and deemed distributions  _(Article 4.2)_
- **Covered Taxes (excluded)** — Top-up tax under the IIR; Qualified Domestic Minimum Top-up Tax (when separately tracked); Disqualified refundable imputation taxes; Taxes paid by an insurance company in respect of returns to policyholders  _(Article 4.2.2)_
- **Adjustments** — + current tax expense for the year on income subject to GloBE; + deferred tax adjustment (capped at 15% rate); + qualified refundable tax credits treated as income (already done in Step 3, ensure no double count); − any covered tax expense on income excluded from GloBE income; − refunds/credits not treated as adjustments to current tax expense; ± additional adjustments per Article 4.1.3  _(Article 4.1)_
- **Deferred tax adjustment** — Recompute deferred tax at the **lower of** the actual statutory rate **or 15%**. Exclude deferred tax on items not included in GloBE income. **Recapture rule:** deferred tax liabilities that do not reverse within 5 years are added back to covered taxes in the year originally taken. Exceptions for tangible asset, depreciation, lease, and similar long-tail DTLs.  _(Article 4.4; Article 4.4.4 (recapture); Article 4.4.5 (exceptions))_

### Step 5 — Compute the jurisdictional ETR (Article 5.1)

- **Jurisdictional ETR formula** — Jurisdictional ETR = Sum of Adjusted Covered Taxes (all CEs in jurisdiction) ÷ Net GloBE Income (all CEs in jurisdiction)  _(Article 5.1)_
- **Rounding and zero/loss treatment** — Round to 4 decimal places. If GloBE Income is zero or a net loss → no top-up tax in that jurisdiction this year (but carry forward applies).  _(Article 5.1)_

### Step 6 — Determine Top-up Tax Percentage and Excess Profit

- **Top-up Tax % formula** — Top-up Tax % = 15% − Jurisdictional ETR (if positive; otherwise 0)
- **SBIE formula** — SBIE = (Payroll carve-out % × eligible payroll) + (Tangible asset carve-out % × eligible tangible assets)  _(Article 5.3)_
- **Use transitional rates** — Use the transitional rates from Section 3.
- **Eligible payroll** — Salaries, wages, benefits, payroll taxes, employer social security; For employees and independent contractors who participate in the ordinary operating activities of the MNE Group in the jurisdiction; Excludes payroll capitalised into eligible tangible asset basis (to avoid double-counting)  _(Article 5.3.3)_
- **Eligible tangible assets** — Net book value (average of beginning and end of year) of: Property, plant and equipment located in the jurisdiction; Natural resources located in the jurisdiction; Lessee's right-of-use of tangible assets located in the jurisdiction; Licence or similar arrangement from government for use of immovable property or natural resources. Excludes property held for sale, lease, or investment; inventory  _(Article 5.3.4)_
- **Excess Profit and Top-up Tax formula** — Excess Profit = Net GloBE Income − SBIE Top-up Tax (before QDMTT credit) = Top-up Tax % × Excess Profit

### Step 7 — Apply de minimis exclusion (Article 5.5)

- **De minimis exclusion condition** — A jurisdiction is excluded from top-up tax for the year if both: Average GloBE Revenue over current and two preceding years < EUR 10 million; Average GloBE Income over current and two preceding years < EUR 1 million (or a loss)  _(Article 5.5)_
- **Election** — Made annually in the GIR for that jurisdiction.

### Step 8 — Apply QDMTT credit and allocate residual top-up tax

- **QDMTT credit rule** — If the source jurisdiction levies a Qualified Domestic Minimum Top-up Tax that the OECD Inclusive Framework has reviewed as qualifying, the QDMTT reduces the top-up tax computed at the IIR / UTPR level. Where the QDMTT also meets the QDMTT Safe Harbour conditions, the IIR/UTPR top-up tax is automatically set to zero for that jurisdiction.  _(Article 5.2.3; Admin Guidance July 2023)_
- **[T1] QDMTT credit decision tree** — 1. Is there a QDMTT in the source jurisdiction? → No: skip. 2. Does the QDMTT qualify (OECD peer review status)? → No: tax paid is added to Covered Taxes but does not eliminate residual top-up tax. 3. Does the QDMTT meet the QDMTT Safe Harbour? → Yes: residual top-up tax under IIR/UTPR = 0. Stop. 4. Otherwise: Top-up Tax (post-QDMTT) = Top-up Tax (pre-QDMTT) − QDMTT paid. If negative → 0.
- **Allocation order** — 1. IIR (Income Inclusion Rule) — top-up tax is charged at the Ultimate Parent Entity level (or first Intermediate Parent in an IIR jurisdiction). UPE jurisdiction has primary right. 2. UTPR (Undertaxed Profits Rule) — residual top-up tax is allocated to UTPR jurisdictions on the basis of the formula: 50% by employees + 50% by tangible assets in the UTPR jurisdiction.  _(Article 2.6)_

### Step 9 — Apply safe harbours

- **[T1] Transitional CbCR Safe Harbour** — Available for fiscal years beginning before 1 January 2027 and ending before 1 July 2028. The top-up tax for the jurisdiction is deemed zero if any one of the three tests is met using Qualified CbCR data.  _(Agreed Admin Guidance Dec 2022)_

**Transitional CbCR Safe Harbour tests**  _(Agreed Admin Guidance Dec 2022)_

| Test | Threshold |
| --- | --- |
| De minimis | CbCR revenue < EUR 10m AND CbCR profit before tax < EUR 1m |
| Simplified ETR | (Qualified Income Tax Expense ÷ Profit Before Tax) ≥ 15% (FY2023/24), 16% (FY2025), 17% (FY2026) |
| Routine profits | Profit Before Tax ≤ jurisdiction's SBIE |

- **[T2] Once-out-always-out** — If a jurisdiction did not apply the transitional CbCR safe harbour in a year in which it was eligible, it cannot apply it in any later year. Reviewer must confirm continuity.

### Step 10 — Compile GIR data points

- **GIR data requirements** — The GIR requires entity-level data for every CE: jurisdiction, ownership, GloBE Income, Adjusted Covered Taxes, ETR, top-up tax, SBIE inputs, safe harbour status. Use the OECD-prescribed schema (XML).

## Section 5 — Edge cases and special rules

### 5.1 Joint ventures (Article 6.4)

- **Joint ventures treatment** — Treat the JV and its subsidiaries as if they were a separate MNE Group whose UPE owns directly. Compute a separate jurisdictional ETR. Allocate JV top-up tax pro rata to JV parents (under IIR principles).  _(Article 6.4)_

### 5.2 Minority-owned subgroups (Article 6.4)

- **Minority-owned subgroups treatment** — A subgroup with 30% or less ownership by the UPE is treated as a separate group for ETR/top-up calculations within the same jurisdiction.  _(Article 6.4)_

### 5.3 Investment entities and insurance investment entities (Article 7.4–7.6)

- **Investment entities treatment** — Special elections allow taxable distribution treatment. Default: ETR computed separately for investment entities.  _(Article 7.4–7.6)_

### 5.4 Permanent establishments (Article 3.4)

- **PE income and tax allocation** — GloBE Income of a PE is allocated to the PE jurisdiction. Covered Taxes of the head office attributable to PE income are allocated to the PE jurisdiction. Where the PE jurisdiction does not tax (e.g., exempt PE), use the head office allocation rules with anti-avoidance constraints.  _(Article 3.4)_

### 5.5 Flow-through entities (Article 3.5, 7.1)

- **Flow-through entities treatment** — If the flow-through is the UPE → it computes GloBE Income at the entity level after allocating to non-group owners. If the flow-through is held by group entities → income allocated up the ownership chain by tax residence of the owner.  _(Article 3.5, 7.1)_

### 5.6 Distribution tax systems (Article 7.3)

- **Distribution tax systems election** — Estonia, Latvia, Georgia, and similar regimes that tax only distributions: an annual election allows a deemed distribution tax to be added to Covered Taxes, equal to the lower of (a) the actual top-up tax that would otherwise apply or (b) the distribution tax that would have applied if all GloBE Income had been distributed.  _(Article 7.3)_

### 5.7 GloBE Loss carryforward and DTA recognition

- **GloBE Loss election** — A jurisdictional election to create a GloBE Loss DTA equal to GloBE Loss × 15%. Once elected, becomes the sole carryforward mechanism for that jurisdiction.  _(Article 4.5)_
- **Standard DTL/DTA approach** — Track deferred tax at the 15% cap with the 5-year recapture rule.  _(Article 4.4)_
- **[T2] GloBE Loss election reviewer approval** — The GloBE Loss election should be reviewer-approved. It locks the jurisdiction into a simpler but less flexible mechanism. For most operating jurisdictions, the standard DTA/DTL approach is preferable.

### 5.8 Interaction with US GILTI

- **GILTI blended CFC tax treatment** — Following the OECD Administrative Guidance of February 2023, US GILTI is treated as a blended CFC tax. The GILTI tax paid by the US parent is allocated to CFC jurisdictions in proportion to the CFC's "blended CFC allocation key" (GloBE Income × ETR shortfall). The Inflation Reduction Act 2022 Corporate Alternative Minimum Tax (CAMT) is generally treated as a covered tax of the US parent.  _(OECD Administrative Guidance February 2023)_
- **[T2] US-parented groups guidance** — For US-parented groups: the allocation methodology is mechanical but data-intensive. Confirm GILTI inclusion percentages, foreign tax credit positions, and BEAT exposure with US counsel before allocating.
- **[T3] Post-2025 GILTI changes (OBBBA P.L. 119-21)** — The OBBBA reduced the GILTI deduction from 50% to 40% (effective rate ~13.125% → ~15.75%) and the §250 FDII deduction commensurately. This affects whether GILTI exceeds the 15% threshold without further top-up at the CFC level. Escalate to US international tax specialist.  _(OBBBA P.L. 119-21)_

### 5.9 Interaction with EU Member State implementations

All 27 EU Member States transposed Directive 2022/2523. Key local variations:

**EU Member State implementations table**

| Jurisdiction | Notable features |
| --- | --- |
| **Germany** | MinStG (Mindeststeuergesetz) of 21 December 2023; QDMTT plus standard IIR/UTPR; tax group rules require domestic top-up to flow through Organschaft |
| **France** | CGI Article 223 VJ et seq.; QDMTT in place; consolidation regime (intégration fiscale) interactions documented in BOFiP |
| **Netherlands** | Wet minimumbelasting 2024; QDMTT plus IIR/UTPR; consultation on safe harbour confirmation procedures |
| **Ireland** | Pillar Two Implementing Provisions in Finance (No. 2) Act 2023; QDMTT (referred to as DTT); IIR/UTPR; specific rules for Section 110 vehicles and certain real estate funds |
| **Italy** | Decreto Legislativo n. 209/2023; QDMTT plus IIR/UTPR; coordination with CFC rules in TUIR |
| **Spain** | Ley 7/2024; QDMTT plus IIR/UTPR; interaction with Spanish CFC and territorial regime |
| **Luxembourg** | Loi du 22 décembre 2023; QDMTT plus IIR/UTPR; rulings practice for transitional CbCR safe harbour eligibility |
| **Belgium** | Law of 19 December 2023; QDMTT plus IIR/UTPR; coordination with new investment deduction regime |

### 5.10 Non-EU implementations as of FY 2025

**Non-EU implementations table**

| Jurisdiction | Status |
| --- | --- |
| **United Kingdom** | Multinational Top-up Tax (MTT — IIR equivalent) and Domestic Top-up Tax (DTT — QDMTT) from accounting periods beginning on or after 31 Dec 2023; UTPR from periods on or after 31 Dec 2024 |
| **Switzerland** | QDMTT (federal supplementary tax) from FY 2024; IIR from FY 2025 (referendum-confirmed); UTPR deferred to FY 2025+ at federal council discretion |
| **Japan** | IIR from fiscal years beginning on or after 1 April 2024; QDMTT and UTPR by FY 2026 per 2024 tax reform |
| **South Korea** | IIR and UTPR from FY 2024; QDMTT considered |
| **Canada** | Pillar Two Act and Income Tax Conventions Implementation Act; IIR and DMTT from FY 2024; UTPR from FY 2025 |
| **Australia** | Taxation (Multinational—Global and Domestic Minimum Tax) Imposition Act 2024; IIR and DMTT from fiscal years beginning on or after 1 January 2024; UTPR from 2025 |
| **Singapore** | Multinational Enterprise (Minimum Tax) Act 2024; DTT (QDMTT) and IIR from financial years beginning on or after 1 January 2025; UTPR not yet enacted |
| **Hong Kong** | DMTT and IIR from FY 2025 per 2024 budget; UTPR not yet enacted |
| **United States** | No Pillar Two adoption; GILTI and CAMT remain in force; CFC blended tax treatment under OECD Admin Guidance Feb 2023 |
| **China** | No formal Pillar Two legislation as of 2025; State Taxation Administration monitoring; CFC and indirect transfer rules may interact |
| **India** | No formal adoption; Budget 2025 announcements pending; CbCR continues under section 286 |

## Section 6 — Output specification

The reviewer brief must include:

1. **Scope test result** — group revenue history and conclusion.
2. **Constituent entity register** — every CE with jurisdiction, ownership, type.
3. **Jurisdictional ETR table** — for every operating jurisdiction (see example table).
4. **Safe harbour analysis** — per jurisdiction, which (if any) safe harbour applies and the evidence supporting it.
5. **QDMTT credit table** — by jurisdiction.
6. **Allocation table** — IIR amounts at the UPE, UTPR allocation to UTPR jurisdictions.
7. **GIR filing schedule** — designated filing entity, jurisdictions where notification is required, deadline list.
8. **Year-over-year reconciliation** — comparison to prior year top-up tax and ETR.
9. **Reviewer questions** — open items flagged as [T2] or [T3].

**Jurisdictional ETR table example**

Jurisdiction | GloBE Income | Adj. Covered Tax | ETR  | SBIE   | Excess Profit | Top-up % | Top-up Tax |
DE           | 100,000,000  | 18,000,000       | 18.0%| 12,000,000 | 88,000,000 | 0%       | 0          |
IE           | 250,000,000  | 31,250,000       | 12.5%| 8,000,000  | 242,000,000| 2.5%     | 6,050,000  |
...

## Section 7 — Self-checks

Before delivering output, verify:

- [ ] Scope test applied with revenue from UPE consolidated financial statements, not segment data.
- [ ] All CEs mapped, including PEs, flow-throughs, and stateless entities.
- [ ] GloBE Income adjustments applied per Article 3 — net taxes added back, excluded dividends/equity items removed.
- [ ] Deferred tax recomputed at the lower of statutory rate or 15%, with the 5-year recapture tracker.
- [ ] Jurisdictional ETR computed at the **jurisdiction**, not the entity.
- [ ] SBIE rates match the transitional table for the fiscal year.
- [ ] De minimis tested with the **average over 3 years**, not the single-year figure.
- [ ] Transitional CbCR safe harbour uses **Qualified CbCR data**, not cherry-picked figures.
- [ ] "Once-out-always-out" rule tracked at the jurisdiction level.
- [ ] QDMTT qualifying status verified against the OECD peer review list.
- [ ] GIR data points populated against the OECD XML schema fields.
- [ ] Interaction with US GILTI / CAMT, UK MTT/DTT, EU country implementations documented.
- [ ] Output flags every assumption requiring reviewer judgement as [T2] or [T3].

## Section 8 — Prohibitions

- **Entity-level-only computation prohibition** — Do not compute Pillar Two at the entity level only. Pillar Two is jurisdictional.
- **Unverified CbCR safe harbour prohibition** — Do not apply the transitional CbCR safe harbour without verifying that the CbCR data is "Qualified" (CbCR prepared from Qualified Financial Statements per Admin Guidance Dec 2022).  _(Admin Guidance Dec 2022)_
- **GILTI blended CFC allocation prohibition** — Do not treat US GILTI as a CE-level covered tax without applying the blended CFC allocation under Admin Guidance Feb 2023.  _(Admin Guidance Feb 2023)_
- **Structuring advice escalation prohibition** — Do not advise on Pillar Two structuring to reduce top-up tax (e.g., asset relocation, substance acquisition) without explicit escalation to a credentialed international tax specialist — anti-abuse rules (Article 9) and the GAAR-like override in Admin Guidance July 2023 ¶3 apply.  _(Article 9; Admin Guidance July 2023 ¶3)_
- **Interaction with other regimes prohibition** — Do not ignore the interaction with CFC, BEAT, Hybrid Mismatch, IRC §163(j), IRC §951A, or Subpart F. These regimes may already produce 15%+ ETR or may need to be unwound for the Pillar Two computation.

## Section 9 — Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. Pillar Two is a complex, rapidly evolving area of international tax law with substantial financial exposure; every output must be reviewed and signed off by a credentialed international tax practitioner before the GloBE Information Return is filed or any structuring decision is taken.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version and track Administrative Guidance updates from the OECD Inclusive Framework.

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
