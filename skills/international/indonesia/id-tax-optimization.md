---
name: id-tax-optimization
description: "Use this skill whenever asked about Indonesian tax planning, regime selection, or year-end optimization for self-employed individuals (Orang Pribadi) and small businesses. Trigger on phrases like \"Indonesia tax planning\", \"PPh Final vs progressive Indonesia\", \"UMKM 0.5% break-even\", \"PP 55/2022\", \"optimize Indonesian tax\", \"PTKP planning\", \"Indonesian tax savings\", \"NPPN vs pembukuan\", \"PT Perorangan vs OP\", \"perencanaan pajak Indonesia\", \"hemat pajak\", \"tarif final UMKM\". Covers regime selection (UMKM Final 0.5%, NPPN deemed-profit, pembukuan), entity choice (OP vs PT Perorangan vs PT), Pasal 6/Pasal 9 deduction planning, PTKP optimization, PPh Final Pasal 4(2) for rental and construction, BPJS wage-cap planning, year-end timing. Out of scope: aggressive avoidance, treaty shopping, transfer pricing, paper-PT structures, CFC planning, and anything caught by UU KUP substance rules or Pasal 18 UU PPh. ALWAYS read this skill before advising on Indonesian tax planning."
jurisdiction: ID
tax_year: 2025
tier: 2
last_updated: 2026-07-06
---

# id-tax-optimization

## Indonesia Tax Optimization -- Self-Employed & Small Business Skill v1.0

## Verified rates & thresholds (accountant-reviewed)

Reviewed against the cited tax authorities by RILIA PUTRI on 2026-06-03. Items flagged for further clarification are tracked separately and excluded here. This block is generated from verified `skill_facts` — edit the facts, not the prose.

### Tax Optimization

- **Revenue < IDR 500M** — Eligible taxpayers under the UMKM final tax regime may utilize the 0.5% final income tax on gross turnover, with the first IDR 500 million of annual turnover generally excluded from taxable base calculation under prevailing regulations. Eligibility is limited to taxpayers covered under Article 57 as amended by PP 20/2026.  _(UU PPh Art. 7; PP 20/2026 Art. 57; PP 55/2022 Art. 60.)_
- **Revenue 500M–4.8B, low margin** — UMKM Final income tax regime at 0.5% of gross turnover may remain administratively simpler and beneficial for eligible taxpayers. Following PP 20/2026, eligibility is limited to individual taxpayers, Perseroan Perorangan, and cooperatives meeting Article 57 requirements.  _(PP 20/2026 Art. 57; UU PPh Art. 4(2).)_
- **Revenue 500M–4.8B, high-margin services** — Taxpayers should compare UMKM Final, ordinary bookkeeping, and NPPN approaches based on profitability and deductible expenses. Eligibility for UMKM Final is subject to revised Article 57 criteria under PP 20/2026 and exclusions under Article 56.  _(PP 20/2026 Art. 56–57; UU PPh Art. 14; PER-17/PJ/2015.)_
- **UMKM 7 years elapsed (OP)** — Mandatory exit; progressive only  _(PP 20/2026 Art. 6 (deletion of Art. 59); PP 20/2026 Art. 57.)_
- **Revenue > 4.8B sustained** — Taxpayers exceeding the IDR 4.8 billion turnover threshold are no longer eligible for UMKM Final taxation beginning the subsequent tax year and generally transition to ordinary income-tax rules with bookkeeping obligations.  _(PP 20/2026 Art. 57(1), 57(2)(e); UU KUP Art. 28.)_
- **Operating losses expected** — Tax loss carry-forward facilities generally apply under the ordinary income tax regime with bookkeeping. The UMKM Final regime does not provide ordinary tax-loss carry-forward treatment.  _(UU PPh Art. 6(2) as amanded by UU HPP; PP 78/2019.)_
- **Dividend extraction from PT** — Domestic dividends received by Indonesian individual taxpayers are generally excluded from income tax provided that the dividends are reinvested in Indonesia in accordance with prevailing regulations. If reinvestment requirements are not satisfied, the dividend may become taxable under ordinary income-tax provisions.  _(UU PPh as amended by UU HPP; PP 55/2022 Art. 9.)_
- **Owner salary from PT** — Salary or remuneration paid by a PT to its shareholder-owner/director may generally be deductible for corporate income-tax purposes provided that the remuneration relates to business activities and satisfies arm's-length/commercial reasonableness principles. Such remuneration is generally subject to PPh 21 withholding obligations. Excessive or non-commercial payments may be challenged as non-deductible expenses or deemed dividend distributions under prevailing tax regulations.  _(UU PPh Art. 6; Art. 21 U PPh as amended by UU HPP No. 7/2021.; PP 55/2022 (general anti-avoidance and arm's-length principles))_
- **KK (default joint)** — Married taxpayers generally follow combined family taxation approach unless separate tax-rights/obligations arrangements apply under prevailing Indonesian income-tax regulations. PTKP treatment depends on marital and dependent status under applicable rules.  _(UU PPh Art. 8; PP 58/2023; PMK 168/2023; PMK 101/PMK.010/2016.; note: UU PPh as amended by UU HPP No. 7/2021.)_

## Section 1 -- Quick Reference: When Each Regime / Entity Wins

**Quick reference field table**

| Field | Value |
| --- | --- |
| Country | Republic of Indonesia (Republik Indonesia) |
| Tax authority | Direktorat Jenderal Pajak (DJP) -- Ministry of Finance (Kementerian Keuangan) |
| Key optimization legislation | UU 36/2008 (Pajak Penghasilan -- "UU PPh"); UU 7/2021 (Harmonisasi Peraturan Perpajakan -- "UU HPP"); PP 55/2022 (PPh Final UMKM 0.5%); PP 58/2023 (PPh 21 withholding rules); PMK 168/2023 (PPh 21 implementation); PER-17/PJ/2015 (Norma Penghitungan Penghasilan Neto -- NPPN); UU 28/2007 (Ketentuan Umum Perpajakan -- "KUP"); UU 40/2007 (Perseroan Terbatas); UU 11/2020 (Cipta Kerja) -- PT Perorangan |
| Currency | Indonesian Rupiah (IDR) |
| Tax year | Calendar year (1 Jan -- 31 Dec) |
| Annual return (SPT Tahunan PPh OP) deadline | 31 March of the following year for individuals (Orang Pribadi -- OP); 30 April for corporates (Badan) |
| GAAR posture | Indonesia does not have a fully codified statutory GAAR but applies a substance-over-form doctrine via Pasal 18 UU PPh (special relationships and arm's-length adjustments) and KUP Article 28 (bookkeeping integrity). Pasal 28A of UU KUP empowers DJP to disregard transactions lacking economic substance. Treaty anti-abuse rules apply under PER-25/PJ/2018 (beneficial owner certification). |

### When each option wins -- one-line rules of thumb

**Situation / Best option table**

| Situation | Best option |
| --- | --- |
| Revenue < IDR 500M/year | UMKM 0.5% (zero-rate band, but check margin) |
| Revenue 500M -- 4.8B, low margin | UMKM Final 0.5% on gross |
| Revenue 500M -- 4.8B, high-margin services | UMKM Final (usually) -- compare to NPPN below |
| Used UMKM 7 years already (OP) | Mandatory exit; progressive only |
| Revenue > 4.8B sustained | Pembukuan; consider PT Perorangan / PT |
| Operating losses expected | Pembukuan -- only regime with 5-yr loss carry-forward |
| Land/building rental income | PPh Final Pasal 4(2) 10% applies automatically |
| Construction services | PPh Final Pasal 4(2) per PP 9/2022 -- rate by SBU class |

## Section 2 -- Required Inputs & Refusal Catalogue

### Required inputs before any planning recommendation

1. Gross annual turnover (peredaran bruto) -- last 3 years + current-year projection.
2. Net margin -- approximate net / gross. Critical for break-even.
3. Entity form -- OP, CV/firma, PT Perorangan, PT, koperasi.
4. Years inside UMKM regime -- 7-year cap for OP, 3-4 years for badan (PP 55/2022).
5. NPWP status -- single or married with PH/MT/HB code.
6. Marital status -- TK / K / K/I.
7. Dependents (max 3 per Pasal 7(3)).
8. Income sources -- usaha / pekerjaan bebas / employment / rental / capital / foreign.
9. BPJS enrolment -- Kesehatan and Ketenagakerjaan (JHT/JKK/JKM/JP).
10. KLU code -- determines NPPN % and PPh Final classification.

### Refusal catalogue (out of scope -- escalate to a registered Konsultan Pajak)

- **R-1** — Treaty shopping / conduit entities (Singapore, HK, NL) for P3B benefits -- needs BEPS / PER-25/PJ/2018 analysis
- **R-2** — Controlled Foreign Corporation rules (PMK 93/PMK.03/2019)
- **R-3** — Transfer pricing structures, intra-group services, royalty restructuring (PMK 213/PMK.03/2016)
- **R-4** — Tax amnesty (PPS) / voluntary disclosure participation
- **R-5** — "Paper PT" with no real operations -- disregarded under Pasal 28A KUP and Pasal 18 UU PPh
- **R-6** — Aggressive split-invoicing between OP and PT controlled by same person (Pasal 18(3) re-attribution)
- **R-7** — Sector-specific regimes: mining, O&G, plantation, financial services
- **R-8** — Property developer regime under PP 34/2016
- **R-9** — E-commerce marketplace seller PPN/PPh 22 issues (PER-37/PJ/2022)
- **R-10** — Cryptocurrency mining / staking optimization (PMK 68/PMK.03/2022)

## Section 3 -- Regime Selection: Break-Even Between the Three OP Regimes

Indonesian self-employed individuals (Orang Pribadi) generally choose between three regimes for taxing business / professional income. Each has dramatically different mechanics.

### 3.1 The three regimes summarized

**Three regimes table**

| Regime | Legislation | Mechanics |
| --- | --- | --- |
| **UMKM Final 0.5%** | PP 55/2022 | 0.5% × gross monthly turnover, paid monthly; no expense deduction; final tax. OP ≤ IDR 4.8B turnover; max 7 years OP / 3 years badan (Art. 5). |
| **Progressive with NPPN** (deemed net income) | Pasal 14(2) UU PPh; PER-17/PJ/2015 | DJP-published deemed-profit % × gross revenue, then PTKP, then progressive brackets. Requires notification to DJP within first 3 months of tax year. |
| **Progressive with Pembukuan** | Pasal 14(1); Pasal 28 KUP | Full accrual bookkeeping; Pasal 6 deductions / Pasal 9 add-backs; PTKP; progressive. Mandatory above IDR 4.8B. Only regime allowing 5-year loss carry-forward (Pasal 6(2)). |

### 3.2 The 2025 PTKP and progressive brackets

**PTKP 2025 table**  _(PMK 101/PMK.010/2016)_

| Code | Annual PTKP (IDR) |
| --- | --- |
| TK/0 (single, no dependents) | 54,000,000 |
| TK/1 | 58,500,000 |
| TK/2 | 63,000,000 |
| TK/3 | 67,500,000 |
| K/0 (married, no dependents) | 58,500,000 |
| K/1 | 63,000,000 |
| K/2 | 67,500,000 |
| K/3 | 72,000,000 |
| K/I/0 (married, spouse's income combined, no dependents) | 112,500,000 |
| K/I/3 | 126,000,000 |

**Progressive brackets table**  _(Pasal 17(1)(a) UU PPh, as amended by UU HPP 7/2021)_

| Annual taxable income (IDR) | Rate |
| --- | --- |
| 0 -- 60,000,000 | 5% |
| 60,000,001 -- 250,000,000 | 15% |
| 250,000,001 -- 500,000,000 | 25% |
| 500,000,001 -- 5,000,000,000 | 30% |
| > 5,000,000,000 | 35% |

### 3.3 The UMKM Final 0.5% zero-rate band

- **UMKM zero-rate band** — For OP, the first IDR 500 million of gross annual turnover is taxed at 0%. The 0.5% applies only above that. Example: R = 800M → PPh Final = 0.5% × 300M = IDR 1,500,000.  _(PP 55/2022 Art. 60)_

### 3.4 Break-even formula -- UMKM vs Progressive with NPPN

- **Break-even formula UMKM vs NPPN** — Let R = gross revenue, n = NPPN deemed-profit %, P = PTKP, T(·) = progressive function. PPh UMKM = 0.5% × max(R − 500,000,000, 0). PPh NPPN = T(max(n·R − P, 0)). UMKM wins when 0.005 × max(R − 500M, 0) < T(max(n·R − P, 0)).

### 3.5 NPPN deemed-profit rates -- common categories (PER-17/PJ/2015)

The actual table covers ~1,500 KLU codes across 3 city tiers (Jakarta + 9 major cities; other provincial capitals; other locations). Always look up the exact KLU.

**NPPN deemed-profit rates table**  _(PER-17/PJ/2015)_

| Activity (KLU) | Tier 1 | Tier 2 | Tier 3 |
| --- | --- | --- | --- |
| Software / IT services | 50% | 50% | 50% |
| Lawyer / consultant (pekerjaan bebas) | 51% | 50% | 50% |
| Retail trade (general) | 30% | 25% | 20% |
| Restaurants / food services | 25% | 22.5% | 20% |
| Construction (subject to PPh Final 4(2) override) | 23.5% | 21.5% | 20% |

### 3.6 Pembukuan -- when it beats both UMKM and NPPN

- Actual margin < NPPN deemed margin (NPPN taxes phantom income).
- Operating losses expected -- only pembukuan allows 5-year loss carry-forward (Pasal 6(2)).
- Heavy capex -- only pembukuan allows depreciation (Pasal 11).
- Mixed usaha + pekerjaan bebas income; or PPh 24 foreign tax credit claims.

## Section 4 -- Entity Choice: OP vs PT Perorangan vs PT

### 4.1 The three entity types in the small-business space

**Entity types table**

| Entity | Legislation | Liability | Tax treatment |
| --- | --- | --- | --- |
| Orang Pribadi (OP) -- sole trader | UU PPh (no separate entity law -- registered via NPWP only) | Unlimited personal liability | Personal PPh (regimes in Section 3) |
| PT Perorangan (single-shareholder micro/small PT) | UU 11/2020 (Cipta Kerja), PP 8/2021 | Limited liability | Corporate PPh per Pasal 17(2a) UU PPh -- 22% standard, or UMKM Final 0.5% if eligible (max 3 years for badan per PP 55/2022 Art. 5(2)) |
| PT (Perseroan Terbatas) -- standard limited company | UU 40/2007 | Limited liability | Corporate PPh 22%; UMKM Final 0.5% for max 3 years if turnover ≤ 4.8B |

### 4.2 Tax + administrative cost trade-off

**Cost trade-off table**

| Factor | OP | PT Perorangan | PT |
| --- | --- | --- | --- |
| Setup cost | ~ IDR 0 | ~ IDR 50,000 (AHU online) | IDR 5M -- 15M (notary, OSS, NIB) |
| Minimum capital | None | Self-declared | Self-declared since Cipta Kerja |
| Audit requirement | No | Only if turnover ≥ IDR 50B / regulated sector | Same |
| Monthly PPh 25 | Only if pembukuan | Yes | Yes |
| Annual filing | Form 1770 by 31 March | Form 1771 by 30 April | Form 1771 by 30 April |
| Dividend tax on extraction | N/A | 10% PPh Final, or exempt if reinvested (Pasal 4(3)(f) UU PPh / HPP) | Same |
| Salary to owner | N/A | Deductible at PT if reasonable; PPh 21 to owner | Same |
| Substance risk | Low | Medium -- DJP scrutinises paper PT | Lower |

### 4.3 Decision heuristic

- Revenue < IDR 500M, low expenses → OP + UMKM Final (effectively zero tax via zero-rate band).
- Revenue IDR 500M -- 2.5B, profitable → OP + UMKM Final for 7 years, then revisit.
- Revenue IDR 2.5B -- 4.8B, liability protection wanted → PT Perorangan + UMKM Final (max 3 years), then progressive corporate.
- Revenue > IDR 4.8B sustained → PT (or PT Perorangan if eligible), pembukuan, 22% corporate, plan reinvestment per HPP 4(3)(f).

### 4.4 The 22% corporate-rate reinvestment opportunity

- **Dividend reinvestment exemption** — Dividends received by Indonesian resident individuals or entities are exempt from PPh if reinvested in Indonesia within 3 years in qualifying instruments (PMK 18/2021). This converts 22% + 10% dividend = 29.8% combined into a clean 22% -- a ~7.8 pp saving versus extraction.  _(Pasal 4(3)(f) UU PPh (as amended by UU HPP))_

## Section 5 -- PTKP Optimization

PTKP (Penghasilan Tidak Kena Pajak) is the personal allowance deducted before applying progressive brackets. It only matters under the progressive regimes (NPPN or pembukuan). It is irrelevant under UMKM Final.

### 5.1 Joint vs separate assessment for married couples

**Marital assessment status table**  _(Pasal 8(1)-(3) UU PPh)_

| Status | NPWP arrangement | When to use |
| --- | --- | --- |
| **KK -- default joint (Kepala Keluarga)** | Spouse on husband's NPWP; combined PTKP K/I/n | Default. PTKP from IDR 112.5M for K/I/0. |
| **PH (Pisah Harta)** | Own NPWP each, with notarised property-separation agreement | Both spouses have substantial business income. |
| **MT (Memilih Terpisah)** | Own NPWP each; tax computed jointly then allocated by gross income | Simpler compromise. |
| **HB (Hidup Berpisah)** | Legally separated by court order | Each files independently TK/n. |

### 5.2 Joint filing benefit when one spouse's income is final

- **Joint filing exclusion of final income** — If one spouse earns income already taxed as PPh Final (e.g., UMKM under PP 55/2022 or PPh Final 4(2) rental), that income is excluded from the joint progressive calculation per Pasal 4(2). Joint filing then only adds non-Final income while Final income is settled. This is legislative design, not avoidance.  _(Pasal 4(2))_

### 5.3 Dependents -- 3 maximum (Pasal 7(3) UU PPh)

- **Dependents limit and PTKP addition** — Maximum 3 dependents count for PTKP. Each adds IDR 4,500,000. Eligible: blood relatives in direct line (parents, parents-in-law) wholly maintained; adopted/step-children fully maintained. Lateral line (siblings) generally not counted unless sole-maintenance proven. Planning: dependent status fixed at 1 January (Pasal 7(2)). Time qualifying events (marriage, parental dependency declaration) before year-end.  _(Pasal 7(3) UU PPh; Pasal 7(2))_

### 5.4 PTKP cash impact -- worked example

OP, married, two children, all on his NPWP (K/2 = IDR 67.5M PTKP). NPPN deemed net IDR 200M.

- K/2: taxable 132.5M → PPh 13,875,000.
- If forgot to register (TK/0, PTKP 54M): taxable 146M → PPh 15,900,000.

Saving from registering dependents: IDR 2,025,000/year. Register on NPWP via KSWP / DJP Online before filing.

## Section 6 -- Deductible Expense Planning (Pasal 6) and Pasal 9 Non-Deductibles

Only relevant under pembukuan (full bookkeeping). Under NPPN, the deemed-profit % includes implicit expense allowance; under UMKM Final, expenses are irrelevant.

### 6.1 Pasal 6 UU PPh -- deductible business expenses

**Pasal 6 deductible expense categories table**

| Category | Reference | Planning note |
| --- | --- | --- |
| Costs of obtaining, collecting, maintaining income | Pasal 6(1)(a) | The general rule -- direct nexus required. |
| Depreciation / amortization | Pasal 6(1)(b); Pasal 11, 11A | See Section 6.3. |
| Pension fund contributions to DJP-approved fund | Pasal 6(1)(c) | Employer DPLK + employee voluntary up to allowed limits. |
| Realized losses on disposal of fixed assets | Pasal 6(1)(d) | Time disposals strategically. |
| Realized FX losses | Pasal 6(1)(e) | Unrealized FX subject to specific rules. |
| R&D in Indonesia | Pasal 6(1)(f); PMK 153/2020 | **Super deduction up to 300%** -- major opportunity. |
| Vocational training | Pasal 6(1)(g); PMK 128/2019 | **Super deduction up to 200%** in priority sectors. |
| Bad debts written off | Pasal 6(1)(h) | DJP notification per PMK 207/2015. |
| Approved donations | Pasal 6(1)(i)-(m); PP 93/2010 | Up to 5% of prior year net income, DJP-approved channels. |

### 6.2 Pasal 9 -- non-deductible items (always disallowed)

**Pasal 9 non-deductible items table**

| Item | Reference | Note |
| --- | --- | --- |
| Dividend distributions | Pasal 9(1)(a) | Use reinvestment exemption (§4.4). |
| Reserves / provisions (except sector-approved) | Pasal 9(1)(c) | No general bad-debt provision. |
| Insurance premiums on OP himself (life/health/accident) | Pasal 9(1)(d) | Employee health insurance is deductible. |
| Excess related-party remuneration | Pasal 9(1)(f) | Arm's-length scrutiny. |
| Personal donations / personal expenses of owner | Pasal 9(1)(g)-(h) | Segregate clearly. |
| Salary OP pays to himself | Pasal 9(1)(j) | Genuine spouse/family salary may be deductible. |
| PPh paid; penalties | Pasal 9(1)(h),(k) | PBB / PB1 are deductible; PPh never. |
| Entertainment without Daftar Nominatif | SE-27/PJ.22/1986 | Must list date, place, purpose, attendees -- else disallowed. |

### 6.3 Depreciation (Pasal 11 UU PPh; PMK 96/PMK.03/2009)

**Depreciation groups table**  _(Pasal 11 UU PPh; PMK 96/PMK.03/2009)_

| Group | Life | Straight-line | Declining-balance |
| --- | --- | --- | --- |
| I (computers, office equipment) | 4 yr | 25% | 50% |
| II | 8 yr | 12.5% | 25% |
| III | 16 yr | 6.25% | 12.5% |
| IV | 20 yr | 5% | 10% |
| Building -- permanent | 20 yr | 5% | n/a |
| Building -- non-permanent | 10 yr | 10% | n/a |

- **Depreciation election and timing** — Election straight-line vs declining-balance is per asset group, applied consistently. Declining-balance front-loads deductions. Depreciation starts month of first business use, pro-rated monthly.  _(Pasal 11 UU PPh; PMK 96/PMK.03/2009)_

## Section 7 -- PPh Final Pasal 4(2) Planning

Pasal 4(2) UU PPh covers categories where income is taxed at a flat final rate at the gross level, separate from the OP's progressive computation. These cannot be opted out of -- they apply automatically by the nature of the income.

### 7.1 Rental of land and/or buildings

- **Rental of land/buildings final tax rate** — 10% percent of gross rent  _(PP 34/2017)_

**Rental planning strategy table**

| Strategy | Detail |
| --- | --- |
| Gross-up clause in lease | Make the lease state who bears the 10% PPh Final to avoid disputes. |
| Service charges vs rent | Maintenance / security / cleaning charges are not rent -- subject to PPh 23 or progressive instead. Separate the contract. |
| Furnished rental | Land/building portion is 4(2); furniture rental can sometimes be split off. |
| Sub-leasing | Sub-rent is 10% on gross; rent paid out is not deductible (final-tax category). |

### 7.2 Construction services

**Construction services final tax rate table**  _(PP 9/2022 (amends PP 51/2008))_

| Service type | SBU status | Rate |
| --- | --- | --- |
| Execution (pelaksanaan) -- small | Certified | 1.75% |
| Execution -- medium/large | Certified | 2.65% |
| Execution | Uncertified | 4% |
| Planning / supervision | Certified | 3.5% |
| Planning / supervision | Uncertified | 6% |
| Integrated construction | Certified / Uncertified | 2.65% / 4% |

A valid SBU from LPJK saves 1.35-2.5 pp on every invoice -- certification cost is usually trivial against single-project savings.

### 7.3 Other Pasal 4(2) categories worth noting

- Bank interest 20% (PP 131/2000); bond interest 10% (PP 91/2021); lottery 25%.
- IDX share sales 0.1% of gross; land/building sales 2.5% (PP 34/2016).
- Listed-share dividends to individuals: 10% PPh Final, or exempt if reinvested per HPP / PMK 18/2021.

## Section 8 -- BPJS Optimization

Indonesian social security comes in two branches:

### 8.1 BPJS Kesehatan (health) -- Perpres 64/2020

- **BPJS Kesehatan contributions and wage cap** — PBPU (self-employed): flat IDR 35,000 (class III) / 100,000 (class II) / 150,000 (class I) per family member per month. PPU (employee): 5% of salary, 4% employer + 1% employee. Wage cap: IDR 12,000,000/month. Salary above the cap incurs no additional BPJS Kesehatan -- structure bonuses / top-up above 12M to capture this.  _(Perpres 64/2020)_

### 8.2 BPJS Ketenagakerjaan (employment) -- UU 24/2011 + PP 44/45/46 2015

**BPJS Ketenagakerjaan programme table**  _(UU 24/2011 + PP 44/45/46 2015)_

| Programme | Employer | Employee | Wage cap |
| --- | --- | --- | --- |
| JKK (work accident) | 0.24% -- 1.74% (risk class) | 0 | None |
| JKM (death) | 0.30% | 0 | None |
| JHT (old age) | 3.7% | 2% | None |
| JP (pension) | 2% | 1% | **IDR ~10,547,400/month** (2025; adjusted annually -- TBC against latest Permenaker) |

- **Planning note on JP cap and deductibility** — Structuring founder compensation so fixed monthly wage sits just above the JP cap maximises pension coverage with no further JP cost. Employer BPJS deductible under Pasal 6(1)(c); employee parts reduce PPh 21 base. A self-employed OP without employees usually only pays BPJS Kesehatan PBPU.  _(Pasal 6(1)(c))_

### 8.3 BPJS deductibility recap

**BPJS deductibility recap table**

| Payer | Deductible? |
| --- | --- |
| Employer PT -- all BPJS employer parts | Yes -- Pasal 6(1)(c). |
| Employee parts in payroll | Reduce employee PPh 21 base (PMK 168/2023). |
| OP self -- BPJS PBPU | Generally not deductible for OP himself (analogue to Pasal 9(1)(d)); employed family members: yes. |

## Section 9 -- Year-End Timing of Expenses & Income Recognition

Indonesia uses accrual basis for pembukuan (per SAK / PSAK). Cash basis is generally not permitted except where DJP has explicitly allowed it for specific professions / small OPs. NPPN effectively operates on a "received" basis (gross revenue earned), and UMKM Final is monthly on gross received.

### 9.1 Income deferral techniques (accrual basis)

**Income deferral techniques table**

| Technique | Notes |
| --- | --- |
| Invoice in January for December delivery | Only valid if performance actually completes in January -- substance over form. |
| Stage-based recognition (PSAK 72) | Plan project milestones around year-end if contract terms genuinely allow. |
| Advance receipts | Deposits for future work are liabilities, not revenue, until performance. |
| Year-end rebate / discount accruals | Must be contractual; conditional discounts only when conditions met. |

### 9.2 Expense acceleration techniques

**Expense acceleration techniques table**

| Technique | Notes |
| --- | --- |
| Prepay annual contracts in December | Under accrual, only the portion accruing to current year is deductible (unless service fully delivered in year). |
| Year-end bonus accrual | Declared and committed before year-end -- expense current year, PPh 21 when paid. |
| Asset purchase before year-end | Depreciation starts month of first business use -- December gives 1 month. |
| Bad debt write-off | Clear evidence of failure + PMK 207/2015 notification. |
| R&D / vocational training spend | Super deductions up to 300% / 200% (PMK 153/2020; PMK 128/2019). |

### 9.3 Regime choice is a January decision

- UMKM Final 0.5% must be elected at start of year or first NPWP registration.
- NPPN requires DJP notification within first 3 months (PER-17/PJ/2015).
- Pembukuan always available; mandatory above IDR 4.8B.

Run the break-even on projected revenue and margin, not actuals -- the choice is locked once payments begin.

## Section 10 -- Worked Example: Software Developer Break-Even

### Setup

Single OP software developer, Jakarta:
- Gross revenue R = IDR 1,200,000,000 (~USD 75,000)
- Genuine operating expenses = IDR 200,000,000 (actual margin ~83%)
- NPPN % for software Tier 1 (Jakarta) = 50%
- TK/0 → PTKP IDR 54,000,000
- 2 years already used inside UMKM (5 years remain)

### Option A -- UMKM Final 0.5%

- **Option A calculation** — PPh = 0.5% × (1,200,000,000 − 500,000,000) = IDR 3,500,000.

### Option B -- Progressive PPh with NPPN

- **Option B calculation** — Deemed net = 50% × 1,200,000,000 = 600,000,000. Taxable = 600,000,000 − 54,000,000 = 546,000,000. PPh (brackets 5/15/25/30): 3,000,000 + 28,500,000 + 62,500,000 + 13,800,000 = IDR 107,800,000.

### Option C -- Progressive PPh with Pembukuan

- **Option C calculation** — Actual net = 1,200,000,000 − 200,000,000 = 1,000,000,000. Taxable = 1,000,000,000 − 54,000,000 = 946,000,000. PPh: 3,000,000 + 28,500,000 + 62,500,000 + 133,800,000 = IDR 227,800,000.

### Verdict

**Verdict comparison table**

| Regime | PPh (IDR) | Effective rate on revenue |
| --- | --- | --- |
| **UMKM Final 0.5%** | **3,500,000** | 0.29% |
| Progressive + NPPN | 107,800,000 | 8.98% |
| Progressive + Pembukuan | 227,800,000 | 18.98% |

UMKM Final dominates because (1) high actual margin (~83%), (2) revenue under IDR 4.8B ceiling, (3) first IDR 500M at 0%.

**Forward-looking planning:** UMKM is available for only 7 years. From year 8 onwards this developer pays NPPN (IDR 107.8M) or pembukuan (IDR 227.8M) on the same income -- prepare for the cliff.

### Break-even rules of thumb (Jakarta NPPN 50%, TK/0)

- UMKM dominates NPPN at virtually all revenues up to the 4.8B ceiling.
- UMKM dominates pembukuan whenever actual margin > ~12%.
- NPPN beats pembukuan whenever actual margin > 50%; pembukuan beats NPPN whenever margin < 50%.

## Section 11 -- Conservative Defaults

**Conservative defaults table**

| Scenario | Default |
| --- | --- |
| UMKM 7-year clock uncertain | Treat as expired -- recommend pembukuan plan (illegal continuation = recalc + 2%/month surcharge per Pasal 19 KUP). |
| NPPN deemed-profit % uncertain | Use higher of candidate KLU codes. |
| Mixed business + employment income | Progressive PPh on combined; UMKM Final only on qualifying business slice. |
| Dependents not registered on NPWP | Apply TK/n until registration proof shown. |
| Spouse business income, no PH agreement | Assume joint (default KK). |
| Asset purchase | Capitalize and depreciate; expense only if useful life < 1 year (Pasal 11(8)). |
| Entertainment without Daftar Nominatif | Disallow entirely. |
| R&D super deduction without PMK 153/2020 ruling | Standard 100%; advise to apply for ruling. |
| Dividend reinvestment exemption | Apply only with PMK 18/2021 commitment letter on file. |
| OP self BPJS contributions | Non-deductible personal unless business nexus documented. |
| Mixed rental contract | 10% PPh Final 4(2) on full rent unless services clearly carved out. |

## Section 12 -- Sources

### Primary statutes

- **UU 36/2008** -- UU Pajak Penghasilan ("UU PPh"), as amended by UU 7/2021 (HPP).
- **UU 7/2021** -- UU Harmonisasi Peraturan Perpajakan ("UU HPP"). Amends PTKP, brackets, top rate, dividend reinvestment.
- **UU 28/2007** -- UU KUP (general administration). Pasal 28 bookkeeping; Pasal 28A substance.
- **UU 40/2007** -- UU Perseroan Terbatas.
- **UU 11/2020** -- UU Cipta Kerja -- introduces PT Perorangan.
- **UU 24/2011** -- BPJS Law.

### Government regulations (PP)

- **PP 55/2022** -- UMKM Final 0.5%; 7-year OP / 3-year badan limit; IDR 500M zero-rate band for OP.
- **PP 58/2023** -- PPh 21 TER withholding.
- **PP 9/2022** -- Construction services final tax (amends PP 51/2008).
- **PP 34/2017** -- Land/building rental 10% PPh Final.
- **PP 34/2016** -- Land/building sale 2.5% PPh Final.
- **PP 45/2019** -- R&D / vocational super deductions.
- **PP 91/2021**, **PP 131/2000**, **PP 93/2010** -- bond, bank interest, donations.

### Ministerial regulations (PMK)

PMK 168/2023 (PPh 21 implementation); PMK 101/PMK.010/2016 (PTKP); PMK 96/PMK.03/2009 (depreciation); PMK 207/2015 (bad debt); PMK 153/2020 (R&D 300%); PMK 128/2019 (training 200%); PMK 18/2021 (dividend reinvestment); PMK 213/2016 (TP docs); PMK 93/2019 (CFC); PMK 68/2022 (crypto).

### DJP regulations (PER)

PER-17/PJ/2015 (NPPN rates); PER-25/PJ/2018 (beneficial owner); PER-37/PJ/2022 (marketplace); SE-27/PJ.22/1986 (Daftar Nominatif).

### Forms

- Form 1770 / 1770S / 1770SS -- SPT Tahunan PPh OP (individuals).
- Form 1771 -- SPT Tahunan PPh Badan (entities).
- Form 1721 / 1721-A1 -- PPh 21 employee withholding.
- SPT Masa PPh 25 -- monthly installment.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (Konsultan Pajak bersertifikat A/B/C, Akuntan Publik, or other Indonesian-licensed practitioner) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com).

## Talk to a verified accountant

This skill is a tool, not an engagement. Every taxpayer's situation is different, and the rules in the skill may not match your specific facts.

To speak with one of the licensed accountants who verifies skills for your jurisdiction — no liability on either side until you and the accountant sign a formal engagement letter — book a free 30-minute call:

**→ [Book a call](https://calendly.com/openaccountants-info/30min)**

We'll route you to the named verifier covering your country or state. You can also see the full list of verified accountants at [openaccountants.com/network](https://openaccountants.com/network).
