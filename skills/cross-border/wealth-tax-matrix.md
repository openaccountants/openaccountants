---
name: wealth-tax-matrix
description: "Use this skill whenever an individual asks about annual net wealth tax exposure. Trigger on phrases like \"wealth tax\", \"net worth tax\", \"ISP (impôt sur la fortune immobilière)\", \"IFI\", \"patrimoine\", \"patrimonio\", \"Vermögensteuer\", \"Solidaritetsskatt\", \"formueskatt\", \"förmögenhetsskatt\", \"Swiss wealth tax\", \"Norway wealth tax\", \"Spain wealth tax\", \"Spain solidarity tax\", \"patrimonio extraordinaria\", \"Madrid wealth tax exemption\", \"Argentinian bienes personales\", \"Colombian impuesto al patrimonio\", \"Uruguay impuesto al patrimonio\", or any request to compute net wealth tax. Maps in-force annual net wealth tax regimes as of mid-2025 in Switzerland (cantonal), Norway, Spain (national IP + regional + Impuesto Temporal de Solidaridad), Argentina, Colombia, Uruguay, the Netherlands (Box 3 fictitious yield as wealth-tax-equivalent), and France (IFI on real estate only). Identifies regimes recently repealed (Italy IVAFE/IVIE remain narrow asset-specific; full wealth tax repealed long ago) and proposed wealth taxes (UK, US §2901 proposals, Brazil). Does NOT cover: inheritance / estate / gift tax (see inheritance-estate-gift-matrix), property transfer tax (see property-transfer-tax-matrix), wealth-related taxes on specific assets (Italy IVIE/IVAFE — see Italian skill). ALWAYS read this skill before computing net wealth tax in an in-force jurisdiction."
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

# Wealth Tax Matrix

## What this file is

**This file is a content skill that loads on top of `cross-border-workflow-base`.** It maps every in-force annual net wealth tax as of mid-2025.

**Tax year coverage.** Current for **calendar 2025**, reflecting:
- **Spain Impuesto Temporal de Solidaridad** extended into 2025 as a temporary national surcharge on net wealth ≥ EUR 3m, neutralising regional rebates (Madrid, Andalucía)
- **Norwegian wealth tax** rates updated; municipal portion 0.7% + state portion graduated 0.4%/0.6%/1.0%
- **Swiss cantonal wealth tax** rates by canton with substantial variation (Geneva ~1% top; Schwyz, Nidwalden ~0.2%)
- **Argentina Bienes Personales** with the new "Plan Aporte Especial" and PPP/Mileiomy-era reductions through Law 27.743
- **Colombia Impuesto al Patrimonio** as restructured under Law 2277 of 2022
- **Netherlands Box 3** in transition (constitutional challenge: HR 6 June 2024 effectively forces actual-return based system; transitional law in force 2025 with calculation methods)
- **France IFI** unchanged (real-estate-only since 2018 replacement of the ISF)

**The reviewer is the customer of this output.** Wealth tax valuation and exemptions are highly fact-specific. Every output must be reviewed by a credentialed local tax practitioner.

## Section 1 — Scope statement

This skill covers:

- **In-force regimes** in: Spain, Norway, Switzerland, Argentina, Colombia, Uruguay, France (real-estate-only IFI), Netherlands (Box 3 — yield basis acting as wealth-tax-equivalent)
- **Recently changed regimes** with material 2025 effects
- **Computation mechanics** — taxable base, exemptions, deduction debts, rate schedules
- **Cross-border considerations** — treaty wealth tax articles (rare), foreign asset reporting, double taxation relief

This skill does NOT cover:

- **Inheritance / estate / gift tax** — see `inheritance-estate-gift-matrix.md`
- **Property transfer tax** — see `property-transfer-tax-matrix.md`
- **Asset-specific taxes** (Italy IVIE on foreign property, IVAFE on foreign financial assets — see Italy tax skill)
- **Pension / retirement account taxation** beyond inclusion/exemption status
- **Capital gains tax** — see country income tax skills

## Section 2 — Spain

### 2.1 Three-layer wealth tax stack

- **Layer 1 — Impuesto sobre el Patrimonio (IP)** — National framework + autonomous community administration: Ley 19/1991 — national law; Each Comunidad Autónoma sets rates, brackets, and rebates; Effective rates: Catalonia ~0.21-2.75%; Madrid 100% rebate (effectively 0%); Andalucía 100% rebate (effectively 0%); Galicia ~0.2-2.5%; others vary; Tax-free minimum (national default): EUR 700,000 (autonomous communities may modify); Habitual residence exemption: EUR 300,000 per taxpayer  _(Ley 19/1991)_
- **Layer 2 — Impuesto Temporal de Solidaridad de las Grandes Fortunas** — Introduced 28 December 2022 (Ley 38/2022) as "temporary" with sunset at end of 2024; extended through 2025 by RDL 9/2024. National tax on net wealth ≥ EUR 3 million; effectively neutralises regional rebates. Rates: 0% to EUR 3m; 1.7% from EUR 3m-5.347m; 2.1% from EUR 5.347m-10.696m; 3.5% above EUR 10.696m. Credit for IP paid in the autonomous community  _(Ley 38/2022; RDL 9/2024)_
- **Layer 3 — Combined cap** — Total of personal income tax (IRPF) + IP + Solidaridad cannot exceed 60% of IRPF taxable base; cap excluded if assets are mostly non-productive

### 2.2 Computation example

A Madrid resident with EUR 8m net wealth:
- IP at Madrid 100% rebate → EUR 0
- Solidaridad: (5.347m − 3m) × 1.7% + (8m − 5.347m) × 2.1% = EUR 39,899 + EUR 55,713 = **EUR 95,612**
- IRPF + Solidaridad capped at 60% of IRPF base

A Catalonia resident with EUR 8m net wealth:
- IP at Catalonia top rate ~2.75% above EUR 10.7m (sub-cap brackets apply); estimate IP ≈ EUR 130,000
- Solidaridad: gross EUR 95,612 − IP paid EUR 130,000 = floor at 0; **net Solidaridad EUR 0**
- The Solidaridad cancels regional rebate effects

### 2.3 Exemptions

**Spain wealth tax exemptions**

| Exemption | Detail |
| --- | --- |
| Family business shares | Exempt if ≥5% direct ownership (or 20% group), held actively, directing functions |
| Habitual residence | First EUR 300k per taxpayer |
| Family heirlooms | Items of historical / artistic value classified |
| Author's IP rights | When inalienable |
| Pension rights | Defined-benefit, occupational pensions |

### 2.4 Filing

- **Spain filing requirements** — Form 714 (IP) and Form 718 (Solidaridad); Due May-June following calendar year; Tax base reference date: 31 December; Online filing mandatory above thresholds

## Section 3 — Norway

- **Norwegian Wealth Tax (Formuesskatt)** — Municipal portion: 0.7% above the threshold to municipalities. State portion (graduated): 0% to NOK 1.7m; 0.4% from NOK 1.7m to NOK 20m; 0.6% from NOK 20m to NOK 100m (per 2024 budget; verify 2025); 1.0% above NOK 20m for primary dwelling > NOK 10m / 2025 budget adjustments. Threshold: NOK 1.7m single / NOK 3.4m married couple (2025). Combined top rate: up to 1.7% on highest net wealth  _(Skattlova kap. 4)_
- **Valuation discounts** — Primary residence: 25% of market value below NOK 10m; 70% above. Secondary residence: 100% of market value. Commercial real estate: 80% of valuation. Operating assets (shares in non-listed companies): 80% of share value (since 2024). Listed shares: 80% of year-end price. Cash, deposits, bonds: 100%  _(Skattlova kap. 4)_
- **Foreign assets** — Worldwide taxation for Norwegian residents. Foreign tax credit for wealth tax paid abroad (e.g., Switzerland canton). Bilateral wealth tax treaty articles where in force (rare)  _(Skattlova kap. 4)_

## Section 4 — Switzerland (cantonal)

- **Federal Switzerland** — No federal wealth tax. Wealth tax is cantonal and municipal.

**Cantonal wealth tax matrix (illustrative, 2025)**

| Canton | Top combined rate | Threshold | Notable |
| --- | --- | --- | --- |
| **Geneva** | ~1.00% | CHF 73,300 single | High top rate; major changes considered annually |
| **Vaud** | ~0.79% | CHF 56,000 | n/a |
| **Bern** | ~0.59% | CHF 97,000 | n/a |
| **Zurich** | ~0.30% | CHF 77,000 | n/a |
| **Zug** | ~0.30% | CHF 200,000 | Low rate, high threshold |
| **Schwyz** | ~0.22% | CHF 100,000 | One of the lowest |
| **Nidwalden** | ~0.18% | CHF 95,000 | Lowest |
| **Ticino** | ~0.30% | CHF 207,000 | n/a |
| **Valais** | ~0.50% | CHF 30,000 | n/a |
| **Basel-Stadt** | ~0.66% | CHF 100,000 | n/a |

- **Tax base** — All worldwide assets at fair market value on 31 December (movable property at FMV; real estate at cantonal "Steuerwert" which is typically 60-80% of market). Less debts (deduction of all certified debts at face value). Movable assets located abroad excluded from cantonal taxation but enter the "rate-determining wealth" calculation (progressive rate effect)
- **Exemptions** — Household furniture for personal use. Personal effects. Pension assets (Säule 3a, 2nd pillar) until paid out. Annuity rights (limited)

## Section 5 — Argentina — Bienes Personales

- **Bienes Personales (BP)** — Rates 2025 (Law 27,743 reform): graduated 0.5%-1.25% on Argentine assets; 0.5%-1.5% on foreign assets if surcharge applies. Threshold: ARS 100m (2024 reform; indexed). Habitual home exemption: ARS 350m  _(Law 23,966 as amended)_
- **Plan Aporte Especial (REIBP)** — One-time advance payment regime introduced by Ley 27.743 (2024). Taxpayers electing prepay 5 years of BP at concessional rate (~0.45-1.5%). Provides stability against future rate increases through 2027  _(Ley 27.743 (2024))_
- **Foreign assets surcharge** — Higher rate (additional 50-100% multiplier) on assets outside Argentina unless repatriated. 5% of foreign assets brought back to Argentina secures the regular rate
- **Liquid assets ratio rule** — Certain bank deposits and government bonds receive reduced rates

## Section 6 — Colombia — Impuesto al Patrimonio

- **Law 2277 of 2022 (Tax Reform)** — Applies to natural persons (resident and non-resident) and certain national entities. Threshold: tax base ≥ 72,000 UVT (~COP 3,388m / ~USD 850k at 2025 UVT). Rate schedule (per 2024/2025 UVT): 0% up to 72,000 UVT; 0.5% from 72,000 to 122,000 UVT; 1.0% from 122,000 to 239,000 UVT; 1.5% above 239,000 UVT (subject to constitutional review). Filing form 420 annually  _(Law 2277 of 2022)_
- **Exemptions** — Habitual residence up to 12,000 UVT. Equity invested in active production companies (limited). Cultural and family heirlooms

## Section 7 — Uruguay — Impuesto al Patrimonio

- **Title 14 of Texto Ordenado / Decreto 318/995** — Applies to natural persons resident in Uruguay (and tax-resident companies; rules differ). Threshold: ~UYU 5.6m for 2025 (indexed UPM). Rate schedule (graduated): 0.2% to 0.7% for residents (rising); 1.5% for non-residents on Uruguayan assets. Filing annual, August following tax year. Deductible debts: capped (no foreign-bank debt allowed). Habitual home discount: 50% of value up to threshold  _(Title 14 of Texto Ordenado / Decreto 318/995)_

## Section 8 — France — IFI (Impôt sur la Fortune Immobilière)

- **IFI scope and rate schedule** — IFI replaced ISF from 1 January 2018. Real-estate-only basis. Scope: net real estate wealth (primary residence with 30% discount; secondary residences at FMV; SCPI, OPCI, real estate company shares pro rata to real estate). Threshold: EUR 1.3 million. Rate schedule: 0% to EUR 800k; 0.5% from EUR 800k to 1.3m (kicks in only when total reaches 1.3m); 0.7% from EUR 1.3m to 2.57m; 1.0% from EUR 2.57m to 5m; 1.25% from EUR 5m to 10m; 1.5% above EUR 10m. Décote (reduction) between EUR 1.3m and 1.4m to smooth the threshold. Cap (plafond): IFI + IR + PFU + CSG cannot exceed 75% of prior year income; excess refunded. Form 2042-IFI filed with income tax return
- **Exemptions** — Real estate used in professional activity. Forestry holdings (75% discount). Bois et forêts under specific contracts. Real estate dedicated to rental at "loyer plafonné" (rent-capped) under certain schemes

## Section 9 — Netherlands — Box 3 (de facto wealth tax via fictitious yield)

- **Box 3 deemed yield formula** — Deemed yield = (allocated % × yield rate per asset class) − allocated debt × debt yield rate Box 3 tax = Deemed yield × 36% (2024/2025 rate, up from 32% in 2023)  _(Hoge Raad judgment of 6 June 2024)_
- **Background** — The Hoge Raad judgment of 6 June 2024 confirmed the existing fictitious-yield system unconstitutional where it exceeds actual return. The transitional Box 3 system in force from 2023 onwards (with retroactive cures) computes a deemed yield as per the formula.  _(Hoge Raad judgment of 6 June 2024)_
- **Asset class yields (2025 illustrative)** — Bank deposits: ~1.03%; Other assets (real estate, shares, crypto, foreign accounts): ~6.04%; Debt yield: ~2.47%
- **Tax-free allowance** — EUR 57,000 per taxpayer / EUR 114,000 fiscal partners
- **Effective wealth tax rate on "other assets"** — 6.04% × 36% = 2.17% (top range; on actual return-bearing assets that perform below the deemed yield, effective rate is higher)

Taxpayers can elect actual-yield computation (counter-proof) from 2025; complex documentation required. Permanent reform expected 2027-2028 to align with actual yield.

## Section 10 — Recently changed / proposed

**Recently changed / proposed wealth tax regimes**

| Jurisdiction | Status |
| --- | --- |
| **Italy** | No general wealth tax. IVIE (0.76% on foreign real estate) and IVAFE (0.2% on foreign financial assets) remain asset-specific. Long-term ISA proposals for super-rich resurface periodically. |
| **Germany** | Wealth tax (Vermögensteuer) suspended since 1997 (BVerfG ruling). Periodic SPD/Greens proposals; not in force as of 2025. |
| **United Kingdom** | No annual wealth tax. Wealth Tax Commission 2020 recommended a one-off 5% wealth tax above £500k; no enactment. 2024 Labour government rejected an annual wealth tax. |
| **United States** | No federal annual wealth tax. State-level proposals (California AB 259, New York AB 6010); proposed federal Warren/Sanders bills (§2901-2902 ITA) have not advanced. Senator Wyden's billionaire tax (proposed mark-to-market on unrealised gains) is conceptually distinct but related. |
| **Brazil** | No general wealth tax. CSLL on net profits applies to companies. Proposed Imposto sobre Grandes Fortunas (CF Art. 153 §VII) authorised by Constitution but never enacted. PEC 162/2022 proposal pending. |
| **Belgium** | No general wealth tax. **Securities Account Tax (Taxe sur les comptes-titres / TCT)** at 0.15% above EUR 1m per holder per account introduced 2021. |
| **Hungary** | No general wealth tax. Property tax (építményadó) and similar local taxes only. |
| **Iceland** | Wealth tax (auðlegðarskattur) abolished 2014. |
| **Sweden** | Wealth tax abolished 2007. |
| **Denmark** | Wealth tax abolished 1997. |
| **Finland** | Wealth tax abolished 2006. |

## Section 11 — Cross-border issues

### 11.1 Worldwide vs territorial scope

- **Worldwide vs territorial scope by regime** — Spain, France IFI: worldwide for residents; Spanish-/French-situs only for non-residents. Norway: worldwide for residents; Norwegian-situs only for non-residents (limited). Switzerland (cantonal): worldwide for residents (rate determination); cantonal-situs only for non-residents. Argentina Bienes Personales: worldwide for residents (with foreign-asset surcharge); Argentine-situs only for non-residents. Netherlands Box 3: worldwide for residents; Dutch-situs only for non-residents

### 11.2 Double taxation relief

- **Double taxation relief** — Few tax treaties contain wealth tax articles. Where present (e.g., OECD Model Article 22): Real estate taxed in the situs state; Business property of a PE taxed in the PE state; Ships and aircraft taxed in the residence state of the operator; All other property taxed in the residence state of the holder  _(OECD Model Article 22)_

In practice, double wealth taxation often results because neither state cedes primary right. Foreign tax credits available where bilateral treaty includes Article 22 (e.g., Norway-Switzerland).

### 11.3 Lex Beckham / impatriate regimes

- **Impatriate regimes and wealth tax** — Spain — Régimen Beckham: impatriates may opt for non-resident taxation for 6 years; IP and Solidaridad still apply on Spanish-situs assets only during election. Italy — Impatriate regime: income tax preferential; no wealth tax in Italy (n/a). Portugal — NHR (closed to new applicants 2024): no wealth tax

## Section 12 — Output specification

The reviewer brief must include:

1. **Tax base computation** at reference date with asset class valuation methodology
2. **Debt deduction schedule** with documentation status
3. **Exemption schedule** per regime
4. **Rate application** and tax due per regime
5. **Cap computations** (Spain 60%/income cap; France IFI 75%/income cap)
6. **Filing schedule** and form references per regime
7. **Cross-border tax credits** where applicable
8. **Reviewer questions** — open items flagged as [T2] or [T3]

## Section 13 — Self-checks

- [ ] Reference date applied (31 December typical)
- [ ] All assets valued per regime methodology (FMV vs official assessed value)
- [ ] Debts only deducted where regime allows
- [ ] Exemptions for family business / habitual home / pension applied
- [ ] Rate schedule applied to net taxable wealth (not gross)
- [ ] Caps applied (Spain 60%; France 75%)
- [ ] Foreign tax credits considered for double taxation
- [ ] Filing form and deadline per regime
- [ ] Output flags every [T2]/[T3] item for reviewer judgement

## Section 14 — Prohibitions

- **Do not** assume an asset is exempt because the country generally exempts family businesses — specific tests (≥5% ownership, active role) apply.
- **Do not** deduct foreign-bank debt against Uruguayan or Spanish wealth tax bases — restrictions apply.
- **Do not** treat the Madrid 100% IP rebate as eliminating all Spanish wealth tax — the Solidaridad surcharge applies.
- **Do not** ignore the December 31 reference date — wealth tax is a snapshot, not an average.
- **Do not** apply ISF rules to French clients — ISF was repealed in 2018; only IFI (real estate only) remains.

## Section 15 — Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Net wealth tax involves valuation judgment and frequent regime changes. Every output must be reviewed and signed off by a credentialed local tax practitioner before filing.

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
