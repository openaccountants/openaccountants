---
name: pk-corporate-tax
description: "ALWAYS read this skill before touching any Pakistan corporate income tax (CIT) work. Use this skill whenever asked about Pakistan corporate tax for a resident Pakistani company. Trigger on phrases like \"Pakistan CIT\", \"Pakistan company tax\", \"Pvt Ltd Pakistan\", \"super tax Pakistan\", \"small company Pakistan tax\", \"PSEB IT export\", \"Finance Act 2025 corporate\", \"Section 4C super tax\", \"Section 113 minimum tax\", \"Section 113C ACT\", \"Section 147 advance tax\", \"IRIS return Pakistan\", \"group taxation Pakistan\", \"Section 59AA\", \"Section 59B\". Covers the 29% standard CIT rate under the Income Tax Ordinance 2001 (ITO 2001) as amended by Finance Act 2024 and Finance Act 2025, the 39% banking-company rate, the 20% small-company rate (turnover ≤ Rs 250M plus the other Section 2(59A) conditions), Section 4C super tax progressive bands (1%–10%) on income above Rs 150M, Section 113 minimum tax on turnover at 1.25%, Section 113C Alternative Corporate Tax (higher of normal tax or 17% of accounting income), the PSEB-registered IT/ITeS exports concessional regime (1% final tax — flag any FA 2025 changes as TBC), Section 59AA group relief and Section 59B group taxation, Section 147 quarterly advance tax computation and payment, and annual return filing via IRIS by 31 December. Out of scope: AOPs and individuals (separate regime), permanent establishments / branches of non-residents, oil and gas exploration and production, insurance company life/non-life special regimes, modarabas, NPOs and trusts, the special economic zone (SEZ) regimes, mutual funds, REITs, and any sales tax / FED matter (see pakistan-sales-tax)."
jurisdiction: PK
domain: international
tax_year: 2025
reviewed_by: Ibrar Ali
review_status: accountant-reviewed
tier: 1
last_updated: 2026-07-06
---

# pk-corporate-tax

## Pakistan — Corporate Income Tax — Skill v1.0

> **Produced by OpenAccountants (openaccountants.com)**
>
> This skill is for informational purposes only and does not constitute tax, legal, or financial advice. All outputs must be reviewed and signed off by a Pakistani tax professional (ICAP CA, ICMA Pakistan, or FBR-recognised tax adviser) before filing or acting upon. The latest verified version is maintained at [openaccountants.com](https://openaccountants.com).

## Verified rates & thresholds (accountant-reviewed)

> Reviewed against the cited tax authorities by **Ibrar Ali** on 2026-06-12.
> Items flagged for further clarification are tracked separately and excluded here.
> This block is generated from verified `skill_facts` — edit the facts, not the prose.

### pk-corporate-tax

- **Standard CIT rate** — 29% of taxable income  _(First Schedule, Pt I, Div II)_
- **Banking companies** — 0.44  _(First Schedule; Seventh Schedule)_
- **Small company rate** — 20%  _(§2(59A); First Schedule, Pt I, Div II)_
- **PSEB IT/ITeS export final tax** — 0.25% final tax if you are registered in PSEB  _(Second Schedule / §154A)_
- **Paid-up capital + undistributed reserves** — ≤ PKR 50,000,000  _(ITO 2001 §2(59A))_
- **Annual turnover** — ≤ PKR 250,000,000  _(ITO 2001 §2(59A))_
- **Employees** — ≤ 250  _(ITO 2001 §2(59A))_
- **Not formed by splitting an existing business** — Condition  _(ITO 2001 §2(59A)(d))_
- **Not a subsidiary/associate of a non-small company** — Not a small and medium enterprise (SME)  _(ITO 2001 §2(59A)(e))_

- **Up to 150,000,000** — 0%  _(§4C; First Schedule Div IIB)_
- **150,000,001 – 200,000,000** — 1%  _(§4C; First Schedule Div IIB)_
- **200,000,001 – 250,000,000** — 0.015  _(§4C; First Schedule Div IIB)_
- **250,000,001 – 300,000,000** — 0.025  _(§4C; First Schedule Div IIB)_
- **300,000,001 – 350,000,000** — 3.5  _(§4C; First Schedule Div IIB)_
- **350,000,001 – 400,000,000** — 5.5  _(§4C; First Schedule Div IIB)_
- **400,000,001 – 500,000,000** — 7.5  _(§4C; First Schedule Div IIB)_
- **Above 500,000,000** — 10%  _(§4C; First Schedule Div IIB)_
- **Minimum tax on turnover §113** — 1.25% of turnover where normal tax is lower (incl. loss years)  _(ITO 2001 §113)_
- **Minimum tax excess carry-forward** — 2 tax years  _(ITO 2001 §113(2)(c))_
- **Alternative Corporate Tax §113C** — 17% of accounting income (pay higher of normal tax or ACT)  _(ITO 2001 §113C)_
- **ACT excess carry-forward** — 10 tax years  _(ITO 2001 §113C)_
- **Tax loss carry-forward** — 6 years; no carry-back  _(ITO 2001 §57)_
- **Unabsorbed depreciation** — Carried forward indefinitely  _(ITO 2001 §57)_
- **Annual return (companies)** — Due 31 December for normal tax year; 30 September if special tax year ends between 1 July and 31 Dec.  _(ITO 2001 §118)_
- **Advance tax §147 instalments** — Quarterly: 25 Sep, 25 Dec, 25 Mar, 15 Jun (Q4 earlier)  _(ITO 2001 §147)_
- **Record retention** — 6 years from end of tax year  _(ITO 2001 §174)_
- **Late filing penalty §182** — 0.1% of tax/day; min PKR 40,000; max 200% of tax payable  _(ITO 2001 §182)_
- **Group relief (loss surrender)** — Requires 55% ownership (listed) or 75% (unlisted)  _(ITO 2001 §59AA)_
- **Group taxation (consolidated return)** — Requires 100% ownership and SECP designation  _(ITO 2001 §59B)_

## Section 1 — Quick Reference

**Section 1 — Quick Reference**

**Quick Reference Table**

| Field | Value |
| --- | --- |
| Country | Pakistan (Islamic Republic of Pakistan) |
| Tax | Corporate Income Tax (CIT) — under the Income Tax Ordinance 2001 |
| Currency | PKR (Rupees, Rs) |
| Tax year | Normal tax year = 1 July to 30 June (e.g., TY 2025-26 = 1 Jul 2025 to 30 Jun 2026). Special tax years require Commissioner approval under Section 74 ITO 2001. |
| Primary legislation | Income Tax Ordinance, 2001 (ITO 2001) as amended by Finance Act 2024 and **Finance Act 2025** |
| Supporting rules | Income Tax Rules, 2002 (ITR 2002); SROs and Circulars issued by FBR |
| **Standard CIT rate** | **29%** of taxable income (companies other than banking) — First Schedule, Part I, Division II |
| **Banking companies** | **0.44 (44%)** |
| **Small company rate** | **20%** for companies meeting all Section 2(59A) criteria (turnover ≤ Rs 250M, paid-up capital + reserves ≤ Rs 50M, employees ≤ 250, not formed by splitting an existing company, not a subsidiary of a non-small company) |
| **Super tax (Section 4C)** | **1%–10%** progressive bands on income above Rs 150M (see §4.1) |
| **Minimum tax (Section 113)** | **1.25%** of turnover where normal tax payable is below this floor or the company is in a tax-loss position |
| **Alternative Corporate Tax (Section 113C)** | Higher of normal tax or **17% of accounting income** |
| PSEB-registered IT/ITeS exports | **0.25% final tax** if registered in PSEB on export proceeds |
| Advance tax (Section 147) | Quarterly instalments — 25 Sep, 25 Dec, 25 Mar, 15 Jun |
| Annual return | Filed via **IRIS** by **31 December** for normal tax year; **30 September** if special tax year ends between 1 July and 31 December (i.e., 31 Dec 2026 for TY 2025-26) |
| Filing portal | IRIS (FBR's online tax administration system at iris.fbr.gov.pk) |
| Tax authority | Federal Board of Revenue (FBR), Government of Pakistan |
| Record retention | 6 years from end of tax year (Section 174 ITO 2001) |
| Validated by | Pending — sign-off by an ICAP CA / ICMA Pakistan member or FBR-recognised tax adviser |
| Skill version | 1.0 |

### 1.1 Conservative Defaults

**1.1 Conservative Defaults**

| Ambiguity | Default |
| --- | --- |
| Company size unknown | Treat as non-small (29% rate) |
| Banking vs non-banking unclear | Default to non-banking (29%) but flag |
| Super tax band unknown | Apply highest applicable band based on best-available income estimate |
| PSEB registration unverified | Apply standard 29%; flag pending verification |
| Minimum tax vs normal tax | Compute both; reviewer pays the higher |
| ACT applicability unclear | Compute both normal tax and 17% of accounting income; reviewer pays the higher |
| Group relief / group taxation election | Treat as standalone unless Section 59AA / 59B election is formally on record |
| Advance tax basis unknown | Use latest assessed taxable income (Section 147(4)) |
| FA 2025 change uncertain | Mark **TBC** and flag for reviewer to verify against current Finance Act text |

## Section 2 — Required Inputs and Refusal Catalogue

### 2.1 Required Inputs

**Minimum viable** — Full-year audited (or draft) financial statements (income statement, balance sheet), prior-year income tax return, computation of turnover and accounting income, confirmation of (i) company size status, (ii) sector (banking / non-banking), (iii) PSEB registration status if claiming IT exports concession, (iv) any group-relief / group-taxation election.

**Recommended** — General ledger, fixed-asset register and depreciation schedule per Third Schedule, related-party transactions schedule, withholding tax credit certificates (CPRs), prior-year tax-loss carry-forward schedule, prior-year minimum tax carry-forward (Section 113(2)(c)) and ACT carry-forward (Section 113C) schedules, advance tax payment receipts.

**Ideal** — Audited statements signed by an ICAP-registered audit firm, complete tax computation with reconciliation between accounting profit and taxable income, transfer-pricing disclosures (Schedule of related-party transactions and Section 108 statement), NTN and STRN certificates, board resolutions for material elections.

**HARD STOP if minimum is missing.** Without financial statements and the prior-year return, no corporate computation may be produced.

### 2.2 Refusal Catalogue

- **R-PK-CT-1** — Non-resident companies / branches / PE. Branches and PEs of non-resident companies are subject to attribution rules under Sections 105–107 and treaty interactions. Out of scope — escalate to a Pakistani tax adviser.  _(Sections 105–107 ITO 2001)_
- **R-PK-CT-2** — Sector-specific regimes. Banking and insurance carry separate computational rules (Seventh Schedule for banking, Fourth Schedule for insurance). Oil & gas exploration and production (Fifth Schedule), mineral extraction, modarabas, mutual funds, REITs — all out of scope.  _(Seventh Schedule; Fourth Schedule; Fifth Schedule)_
- **R-PK-CT-3** — Group consolidated returns / group taxation under Section 59B. Election under Section 59B (designated income group) requires 100% ownership and SECP designation; out of scope for this skill. Section 59AA (group relief — surrender of losses within a 100%-owned group) is discussed at Tier 2 but requires reviewer sign-off.  _(Section 59B ITO 2001)_
- **R-PK-CT-4** — AOPs, individuals, NPOs, trusts. Different rate schedules and computation rules. Out of scope — the company-specific First Schedule Part I Division II rules do not apply.  _(First Schedule Part I Division II)_
- **R-PK-CT-5** — Special Economic Zones (SEZ) / Export Processing Zones (EPZ). Sector and zone-specific exemptions under the SEZ Act 2012 and EPZ Ordinance. Out of scope.  _(SEZ Act 2012; EPZ Ordinance)_
- **R-PK-CT-6** — Active assessment / audit / appellate proceedings. If the company is in a Section 122 amendment, Section 177 audit, ATIR appeal, or High Court reference — escalate. Do not produce numbers that pre-empt the dispute.  _(Section 122; Section 177 ITO 2001)_
- **R-PK-CT-7** — Transfer pricing controversy. Active MAP or APA proceedings, or Section 108 / Rule 20–27D disputes. Out of scope.  _(Section 108 ITO 2001; Rules 20–27D)_
- **R-PK-CT-8** — Cross-skill scope. Sales tax and FED → pakistan-sales-tax. Withholding on payments (Section 149–158) is touched only insofar as it affects CIT credits — for compliance refer to a withholding-specific skill (TBD).  _(Sections 149–158 ITO 2001)_
- **R-PK-CT-9** — FA 2025 ambiguity. Where the Finance Act 2025 text is uncertain on a specific point (rates, thresholds, schedule amendments), flag as TBC and decline to commit to a number without reviewer verification of the gazetted Act.  _(Finance Act 2025)_

## Section 3 — Tier 1 — Rates by Company Size and Sector

### 3.1 Standard CIT Rate — 29%

- **Standard CIT rate** — 29% of taxable income for companies other than banking companies and small companies  _(First Schedule, Part I, Division II, ITO 2001 as amended by Finance Act 2024 and Finance Act 2025)_
- **CIT formula** — CIT = 29% × Taxable Income  _(First Schedule, Part I, Division II, ITO 2001)_

This is the default rate that applies unless the company qualifies for the small-company rate, falls within the banking rate, or is subject to a sector-specific schedule (insurance, oil & gas, etc.) — those are out of scope.

### 3.2 Banking Companies — 39%

- **Banking company rate** — 0.44 (44%) on taxable income computed under the Seventh Schedule. Reviewer should verify the gazetted FA 2025 text before applying.  _(First Schedule, Part I, Division II, ITO 2001; Seventh Schedule)_

The Seventh Schedule overrides much of the general computational framework — different rules for provisioning, bad debts, and certain receipts. The banking sector is largely out of scope for this skill (R-PK-CT-2); the 39% rate is referenced here only for completeness.

### 3.3 Small Companies — 20%

- **Small company** — A company that satisfies all of the small-company conditions per Section 2(59A) ITO 2001  _(Section 2(59A) ITO 2001 (definition); First Schedule, Part I, Division II (rate))_

**Small company conditions table**

| Condition | Threshold |
| --- | --- |
| Paid-up capital plus undistributed reserves | ≤ Rs 50,000,000 |
| Annual turnover | ≤ Rs 250,000,000 |
| Number of employees | ≤ 250 (any time during the year) |
| Not formed by splitting up or reconstitution of an existing business | Section 2(59A)(d) |
| Not a small and medium enterprise (SME) | Section 2(59A)(e) |
| Not engaged in certain excluded businesses | Per Section 2(59A) provisos (e.g., professional services with specific carve-outs) |

- **All-or-nothing test** — If all conditions are met, the rate is 20%. If any condition fails — even by one rupee of turnover — the standard 29% applies for the entire tax year.  _(Section 2(59A) ITO 2001)_
- **Small company CIT formula** — Small company CIT = 20% × Taxable Income  _(First Schedule, Part I, Division II)_
- **Fresh annual test** — The small-company test is applied each tax year on a fresh basis. A company exiting the band loses the rate for that entire year. The test is all-or-nothing — there is no sliding scale.  _(Section 2(59A) ITO 2001)_

### 3.4 PSEB-Registered IT / ITeS Exports — 0.25% Final Tax

- **PSEB IT/ITeS export final tax** — 0.25% final tax on export proceeds  _(Historically Clause (133) of Part I of the Second Schedule and SROs concerning IT/ITeS export receipts)_
- **Conditions for concession** — Active PSEB registration covering the tax year; Export proceeds remitted to Pakistan through normal banking channels and supported by Bank Credit Advices; Activities falling within the FBR/PSEB-defined IT/ITeS scope.  _(FA 2024)_

**TBC** — verify whether FA 2025 has amended the rate, scope, or the final-vs-minimum tax characterisation. Flag for reviewer.

- **Conservative default** — Apply 29% on the gross profit attributable to IT exports until PSEB registration and applicable SRO/Clause text for the relevant tax year are verified. The 0.25% concession should be applied only after reviewer confirms (a) current-year PSEB certificate, (b) banking-channel inward remittance, and (c) the relevant Clause/SRO is still in force for TY 2025-26.

### 3.5 Taxable Income

- **Taxable income formula** — Taxable Income = Total Income (Section 10) − Deductions (Sections 20–31) − Tax losses b/f (Sections 56–59)  _(Sections 10, 20–31, 56–59 ITO 2001)_
- **Heads of income** — Heads of income for companies — primarily Income from Business (Section 18). Other heads (capital gains, income from property, other sources) apply where relevant.  _(Section 18 ITO 2001)_
- **Tax losses and unabsorbed depreciation** — Tax losses may be carried forward for 6 tax years from the year the loss arose (Section 57); unabsorbed depreciation can be carried forward indefinitely. Carry-back is not available.  _(Section 57 ITO 2001)_
- **Depreciation** — Depreciation is governed by the Third Schedule — straight-line and reducing-balance rates per asset class; initial allowance under Section 23 applies in the first year for qualifying plant and machinery.  _(Third Schedule; Section 23 ITO 2001)_

## Section 4 — Tier 2 — Super Tax, Minimum Tax, ACT, Group Taxation

### 4.1 Super Tax — Section 4C ITO 2001

- **Super tax basis** — Super tax under Section 4C is an additional tax on "income" as defined for Section 4C purposes (broadly, income chargeable to tax under heads excluding certain exempt items — refer to the precise statutory definition). It is computed in progressive bands above Rs 150M.  _(Section 4C ITO 2001 as inserted/amended; rates set in Division IIB of Part I of the First Schedule; current schedule per FA 2024 (and FA 2025 — TBC))_

**Super Tax Bands (post-FA 2024)**  _(Section 4C ITO 2001; Division IIB, Part I, First Schedule)_

| Income Band | Super Tax Rate (post-FA 2024) |
| --- | --- |
| Up to Rs 150,000,000 | **0%** |
| Rs 150,000,001 — Rs 200,000,000 | 1% |
| Rs 200,000,001 — Rs 250,000,000 | 1.5% |
| Rs 250,000,001 — Rs 300,000,000 | 2.5% |
| Rs 300,000,001 — Rs 350,000,000 | 3.5% |
| Rs 350,000,001 — Rs 400,000,000 | 5.5% |
| Rs 400,000,001 — Rs 500,000,000 | 7.5% |
| Above Rs 500,000,000 | **10%** |

*(Reviewer: confirm the band schedule against the current Finance Act for TY 2025-26 — slight band recalibrations occur each year. Flag as **TBC** if FA 2025 has shifted any threshold.)*

- **Super tax interaction** — Super tax is in addition to the normal corporate tax and any minimum tax or ACT. It is not creditable against normal CIT and does not generate a carry-forward.  _(Section 4C ITO 2001)_
- **Super tax formula** — Super Tax = Σ (band rate × income within that band)  _(Section 4C ITO 2001)_
- **Conservative default** — Apply the highest applicable band based on best-available income estimate. Do not net super tax against tax credits or losses unless the statutory language expressly permits it (it generally does not).

### 4.2 Minimum Tax on Turnover — Section 113

- **Minimum tax rate** — 1.25% of turnover for companies (post-FA 2024); certain sectors carry reduced rates per Division IX of Part I of the First Schedule.  _(Section 113 ITO 2001)_
- **When minimum tax applies** — Where a company's normal tax liability for a tax year is less than 1.25% of turnover — including where the company is in a tax-loss position — the company must pay minimum tax at 1.25% of turnover.  _(Section 113(1) ITO 2001)_
- **Minimum tax formula** — Minimum Tax = 1.25% × Turnover (where normal CIT < this floor)  _(Section 113 ITO 2001)_
- **Turnover definition** — "Turnover" for Section 113 means gross receipts (Section 113(3) definition) — generally gross sales and gross receipts from services and other business activities, excluding sales tax, FED, and refunds/discounts. Verify the precise inclusions per the current Section 113(3) text.  _(Section 113(3) ITO 2001)_
- **Carry-forward** — Excess of minimum tax over normal tax is carried forward up to 2 tax years and adjustable against normal tax liability in those years.  _(Section 113(2)(c) ITO 2001)_
- **Sector variations** — Some sectors (e.g., distributors of certain goods, refineries, oil marketing companies) have reduced rates under Division IX — flag to reviewer if the company is in a Division IX listed sector.  _(Division IX, Part I, First Schedule)_
- **Conservative default** — Compute both normal tax and minimum tax; pay the higher. Track minimum tax excess as a 2-year carry-forward.

### 4.3 Alternative Corporate Tax (ACT) — Section 113C

- **ACT rate** — 17% of accounting income (post-FA 2024 — confirm FA 2025 as TBC)  _(Section 113C ITO 2001)_
- **Higher of test** — A company's tax liability for a tax year is the higher of: 1. Corporate Tax — normal CIT at the applicable rate (29% / 20% / 39%); or 2. Alternative Corporate Tax (ACT) — 17% of accounting income (accounting income as defined in Section 113C, broadly profit before tax as per the financial statements with prescribed adjustments).  _(Section 113C ITO 2001)_
- **ACT liability formula** — Liability = max ( Corporate Tax, 17% × Accounting Income )  _(Section 113C ITO 2001)_
- **Accounting income nuance** — "Accounting income" for Section 113C is defined with carve-outs (e.g., exempt income, income subject to final tax regimes, share of profit from AOPs already taxed). The precise adjustment list is in Section 113C — apply it carefully, do not equate "accounting income" with raw PBT.  _(Section 113C ITO 2001)_
- **ACT carry-forward** — Excess of ACT over normal corporate tax is carried forward up to 10 tax years and adjustable against normal CIT in those years.  _(Section 113C ITO 2001)_
- **Interaction with minimum tax and super tax** — ACT does not displace Section 113 minimum tax — both regimes can apply. The company pays the highest of (normal CIT, Section 113 minimum tax, Section 113C ACT). Super tax under Section 4C is then added on top.
- **Conservative default** — Compute all three (normal CIT, Section 113 minimum, Section 113C ACT) for every corporate engagement and pay the highest, then add Section 4C super tax.

### 4.4 Group Relief — Section 59AA

- **Group relief conditions** — Both companies are resident in Pakistan; The holding meets the ownership threshold: 55% (listed companies) or 75% (unlisted companies); The group is designated and the election is made within the statutory window; Continuity-of-business and continuity-of-ownership tests are met (per Section 59AA conditions and the related Rules); The surrendering company has no minimum-tax carry-forward issues that conflict with the surrender.  _(Section 59AA ITO 2001)_
- **Conservative default** — Treat companies as standalone (no group relief) unless the election and applicable ownership threshold (55% listed / 75% unlisted) are documented and reviewer confirms compliance with Section 59AA.

### 4.5 Group Taxation — Section 59B

- **Group taxation conditions** — 100% ownership (directly or through wholly-owned chain); SECP designation as a group; Audited accounts in compliance with prescribed standards.  _(Section 59B ITO 2001 and Group Taxation Rules)_
- **Out of scope (R-PK-CT-3)** — Section 59B election is complex and requires specialist advice; this skill does not produce group-taxation computations.  _(R-PK-CT-3)_

## Section 5 — Worked Examples

### 5.1 Pvt Ltd at Standard Rate

**Facts:** Brightline (Pvt) Ltd. Resident Pakistani company. Tax year 2025-26 (1 Jul 2025 – 30 Jun 2026).
- Turnover: Rs 1,200,000,000.
- Accounting profit before tax (per audited FS): Rs 220,000,000.
- Add-backs (depreciation accounting vs Third Schedule difference + non-deductible donations + accounting provisions reversed): + Rs 30,000,000.
- Deductions (initial allowance under Section 23): − Rs 20,000,000.
- Taxable income: Rs 230,000,000.
- Withholding tax credits (Bank profit, contract receipts WHT): Rs 12,000,000.
- Advance tax paid under Section 147 across four quarters: Rs 55,000,000.

**5.1.1 Normal CIT.** Brightline is not a small company (turnover Rs 1.2B exceeds Rs 250M). Standard 29% applies.
```
Normal CIT = 29% × 230,000,000 = Rs 66,700,000
```

**5.1.2 Section 113 Minimum Tax.**
```
Minimum Tax = 1.25% × 1,200,000,000 = Rs 15,000,000
```
Normal CIT (Rs 66.7M) > minimum tax (Rs 15M). Pay normal CIT. No minimum-tax excess to carry forward.

**5.1.3 Section 113C ACT.**
```
ACT = 17% × Accounting Income (Rs 220,000,000) = Rs 37,400,000
```
Normal CIT (Rs 66.7M) > ACT (Rs 37.4M). Pay normal CIT. No ACT excess to carry forward.

**5.1.4 Section 4C Super Tax.** Income for Section 4C is Rs 230M (within the Rs 200M–Rs 250M band).
```
Super tax on Rs 150,000,000             = 0%  × 150,000,000  = Rs 0
Super tax on Rs 50,000,000 (150M–200M)  = 1%  ×  50,000,000  = Rs 500,000
Super tax on Rs 30,000,000 (200M–230M)  = 1.5%  ×  30,000,000  = Rs 450,000
                                                                ─────────────
Total Section 4C Super Tax                                    = Rs 1,100,000
```

**5.1.5 Total liability.**
```
Normal CIT          Rs 66,700,000
Super Tax (4C)      Rs  1,100,000
                    ──────────────
Total              Rs 67,800,000

Less: WHT credits        Rs 12,000,000
Less: Advance tax paid   Rs 55,000,000
                    ──────────────
Payable at filing  Rs   800,000
```

Payable with the IRIS return by **31 December 2026**.

### 5.2 Small Company

**Facts:** TechSouk (SMC-Pvt) Ltd. All Section 2(59A) conditions met (paid-up + reserves Rs 30M; turnover Rs 180M; 80 employees; not a split-off; not a subsidiary).
- Turnover Rs 180,000,000.
- Taxable income Rs 22,000,000.

**5.2.1 Normal CIT at small-company rate.**
```
Normal CIT = 20% × 22,000,000 = Rs 4,400,000
```

**5.2.2 Section 113 Minimum.**
```
Minimum Tax = 1.25% × 180,000,000 = Rs 2,250,000
```
Normal CIT (Rs 4.4M) > minimum tax. Pay normal CIT.

**5.2.3 Section 113C ACT.** If accounting income = Rs 25M:
```
ACT = 17% × 25,000,000 = Rs 4,250,000
```
Normal CIT (Rs 4.4M) > ACT (Rs 4.25M). Pay normal CIT.

**5.2.4 Super Tax.** Income Rs 22M is below Rs 150M threshold — no Section 4C liability.

**Total liability: Rs 4,400,000** before WHT credits / advance tax.

### 5.3 PSEB-Registered IT Exporter (Conservative Default)

**Facts:** CodeKarachi (Pvt) Ltd. Claims PSEB-registered IT services exporter for TY 2025-26.
- IT export receipts (banking-channel remittance with BCAs): Rs 500,000,000.
- Domestic services receipts: Rs 50,000,000.
- Total turnover: Rs 550,000,000.

**Approach — Conservative.** Until reviewer verifies (i) current PSEB certificate for TY 2025-26 and (ii) the precise FA 2025 text on the 1% concession (**TBC**), apply the standard 29% to the full taxable income.

**If reviewer confirms the 1% concession applies** (final-tax basis on export remittances under the relevant Clause/SRO for TY 2025-26):

```
Tax on export receipts (final tax)  = 0.25% × 500,000,000 = Rs 1,250,000
Domestic income — taxed at normal CIT (29%) on attributable taxable income
```

Reviewer must confirm (a) the export receipts qualify as "IT/ITeS exports" per the PSEB/FBR list, (b) banking-channel remittance evidenced, (c) the Clause/SRO is in force for TY 2025-26, and (d) whether the 0.25% is final (no further tax on those proceeds) or minimum (top-up if normal tax is higher). The historical position is final tax — TBC under FA 2025.

### 5.4 Banking Company (Reference Only — Out of Scope)

**Facts:** AlphaBank Ltd. Taxable income (Seventh Schedule basis) Rs 8,000,000,000.

```
Banking CIT = 39% × 8,000,000,000 = Rs 3,120,000,000
```

Plus applicable super tax under Section 4C (banking-sector specific bands may apply — verify). Beyond this rate reference, banking is out of scope (R-PK-CT-2).

## Section 6 — Filing and Payment Mechanics

### 6.1 Annual Return — IRIS

**Form:** Income Tax Return for Companies — filed electronically via **IRIS** (iris.fbr.gov.pk).

**Required schedules** (typical, non-exhaustive):

**Required schedules table**

| Schedule | Content |
| --- | --- |
| Main return | Computation of taxable income; tax payable |
| Wealth statement | N/A for companies (applies to individuals) |
| Schedule of business income | Section 18 computation |
| Schedule of depreciation | Third Schedule rates per asset class |
| Schedule of tax credits | WHT credits, foreign tax credit, advance tax |
| Schedule of related-party transactions (Section 108) | Disclosures for transfer-pricing purposes |
| Schedule of minimum tax / ACT | Section 113 / 113C computations and carry-forwards |
| Schedule of super tax (Section 4C) | Band computation |
| Audited financial statements | Attached |

### 6.2 Filing Deadlines

**Filing deadlines table**

| Item | Deadline |
| --- | --- |
| Annual return (companies with normal tax year) | **31 December** following tax year-end (e.g., 31 Dec 2026 for TY 2025-26) |
| Special tax year return | 30 September following the special tax year-end, **unless** the Commissioner specifies otherwise — verify |
| Extension request | Application under Section 119 to the Commissioner; not automatic |
| Section 147 advance tax — Q1 | **25 September** |
| Section 147 advance tax — Q2 | **25 December** |
| Section 147 advance tax — Q3 | **25 March** |
| Section 147 advance tax — Q4 | **15 June** (note the earlier date in the fourth quarter) |
| Annual tax payable balance | Due with the annual return (i.e., by 31 December) |
| Section 108 statement (related-party) | Filed with the annual return |

### 6.3 Section 147 Advance Tax

- **Quarterly advance tax formula** — Quarterly advance tax = (Latest assessed taxable income × applicable CIT rate) / 4 − WHT credits attributable to that quarter  _(Section 147 ITO 2001)_
- **Section 147(6) estimate** — If the company estimates that current-year liability will be materially lower than the prior assessed basis, it may file an estimate under Section 147(6) and pay on that lower figure — but Section 147 contains default-surcharge mechanics if the year-end liability exceeds the estimate. Conservative default: pay on the latest-assessed basis.  _(Section 147(6) ITO 2001)_
- **Late or short advance payment** — Late or short advance payment triggers default surcharge under Section 205 (current rate per the Act / FBR — typically KIBOR-plus or a flat 12%/year-equivalent — verify against current Section 205 text).  _(Section 205 ITO 2001)_

### 6.4 Withholding Tax Credits

- **WHT creditable** — WHT collected against the company under Sections 149–158 (e.g., contract payments, services, bank profit, rent) is creditable against the annual CIT liability, subject to the CPR (Computerised Payment Receipt) evidence and matching in IRIS.  _(Sections 149–158 ITO 2001)_
- **Final tax WHT regimes** — Some WHT regimes are "final tax" (e.g., certain export receipts under Section 154, dividend tax under Section 150) — those receipts are excluded from the normal CIT computation entirely, and the WHT is not creditable against other income. Verify the head and the relevant clause / Division for each receipt before crediting.  _(Section 154; Section 150 ITO 2001)_

### 6.5 Audit, Assessment, and Statute of Limitations

- **Self-assessment** under Section 120 — return as filed becomes the assessment unless selected for audit.
- **Audit selection** under Section 177 / 214C — Commissioner may select; risk-based or parametric.
- **Amendment of assessment** under Section 122 — up to **5 years** from end of the financial year in which the original assessment was made (extendable in cases of concealment).
- **Appeals** — Commissioner (Appeals) → Appellate Tribunal Inland Revenue (ATIR) → High Court reference → Supreme Court appeal.

### 6.6 Common Penalty Headings (Section 182 and others)

**Penalty headings table**

| Infraction | Sanction |
| --- | --- |
| Failure to file return on time | 0.1% of tax payable per day, min Rs 40,000, max 200% of tax payable (Section 182, item 1) |
| Failure to maintain records | Rs 25,000 / 10% of tax — verify current schedule |
| Failure to file Section 108 statement | Per Section 182 schedule |
| Concealment of income | Up to 100% of tax sought to be evaded |
| Late payment of tax / advance tax | Default surcharge under Section 205 (verify current rate) |
| Wilful tax evasion | Prosecution under Sections 191–194 + financial penalties |

**Conservative default:** File and pay on time. Penalty figures above are illustrative — confirm against the current Section 182 table and any FA 2025 amendments before quoting to a client.

## Section 7 — Conservative Defaults Summary

**Conservative defaults summary table**

| Item | Default |
| --- | --- |
| Company size unknown | Treat as non-small (29%) |
| Sector unknown | Non-banking (29%, not 39%) |
| PSEB IT-exports concession | Apply 29% until PSEB certificate + FA 2025 text verified |
| Super tax band | Apply highest band consistent with best-available income estimate |
| Minimum tax vs normal tax | Pay the higher; track minimum-tax excess as 2-year carry-forward |
| ACT (Section 113C) | Compute alongside normal tax; pay the higher; track excess as 10-year carry-forward |
| Group relief / group taxation | Standalone unless Section 59AA / 59B election is formally documented |
| Advance tax (Section 147) | Use latest assessed basis; do not file Section 147(6) downward estimates without strong evidence |
| WHT crediting | Confirm normal vs final-tax characterisation before crediting against CIT |
| FA 2025 specifics where unconfirmed | Mark **TBC** and flag for reviewer to verify against gazetted text |
| Record retention | 6 years from end of tax year |
| Filing channel | IRIS only — e-filing is mandatory for companies |
| Tax loss carry-forward | 6 years (Section 57); unabsorbed depreciation indefinite |

## Section 8 — Sources

**Primary Legislation**

- **Income Tax Ordinance, 2001 (ITO 2001)** — primary corporate income tax statute.
  - Section 2(59A) — definition of "small company".
  - Section 4C — super tax on high earning persons (current bands per Division IIB, Part I, First Schedule).
  - Section 18 — income from business.
  - Section 20–31 — deductions.
  - Section 23 — initial allowance on plant and machinery.
  - Section 56–59 — set-off and carry-forward of losses.
  - Section 57 — 6-year loss carry-forward.
  - Section 59AA — group relief.
  - Section 59B — group taxation.
  - Section 74 — tax year and special tax year.
  - Section 105–107 — non-residents and permanent establishments (out of scope).
  - Section 108 — transfer-pricing disclosure statement.
  - Section 113 — minimum tax on turnover.
  - Section 113C — Alternative Corporate Tax (ACT).
  - Section 119 — extension of time for filing.
  - Section 120 — self-assessment.
  - Section 122 — amendment of assessment.
  - Section 147 — advance tax for companies (quarterly).
  - Section 149–158 — withholding tax regimes.
  - Section 154 — exports / certain receipts (final-tax regimes).
  - Section 174 — record-keeping (6 years).
  - Section 177 — audit selection.
  - Section 182 — penalty schedule.
  - Section 205 — default surcharge.
  - First Schedule, Part I, Division II — CIT rates.
  - Third Schedule — depreciation rates.
  - Fourth Schedule — insurance (out of scope).
  - Fifth Schedule — oil & gas (out of scope).
  - Seventh Schedule — banking (out of scope except 39% rate reference).
  - Second Schedule, Part I — exemptions (incl. IT exports clauses, historical Clause 133).
- **Finance Act 2024** — amended rates, super tax bands, minimum tax, ACT settings.
- **Finance Act 2025** — current-year amendments (verify gazetted text; **TBC** where uncertain).

**Subordinate Legislation**

- **Income Tax Rules, 2002 (ITR 2002)** — procedural detail, including transfer-pricing rules (Rules 20–27D) and Group Taxation Rules.
- **SROs and Circulars** issued by FBR — particularly on IT-exports regime, sectoral minimum-tax variations, and Section 147 estimate filings.

**FBR Resources and Platform**

- **IRIS** — FBR online filing portal at iris.fbr.gov.pk (mandatory for company returns).
- **FBR website** (fbr.gov.pk) — Acts, Rules, SROs, Circulars, and the consolidated ITO 2001 reading copy.
- **PSEB** (pseb.org.pk) — registration body for IT/ITeS exporters claiming the historical Clause 133 concession.

## PROHIBITIONS

- NEVER apply the small-company rate (20%) without confirming **all** Section 2(59A) conditions are met for the relevant tax year.
- NEVER apply the 0.25% PSEB IT-exports concession without (a) current PSEB registration for the tax year, (b) banking-channel remittance evidence, and (c) reviewer verification that the Clause/SRO is in force for TY 2025-26.
- NEVER skip the Section 113 minimum-tax computation — it applies even in tax-loss years.
- NEVER skip the Section 113C ACT computation — accounting income can exceed taxable income materially.
- NEVER omit Section 4C super tax where income exceeds Rs 150M.
- NEVER credit "final-tax" WHT against normal CIT — separate it out.
- NEVER use current-year forecast as Section 147 basis without filing a formal Section 147(6) estimate; default to the latest-assessed basis.
- NEVER advise late filing or late payment of tax / advance tax — Section 205 default surcharge and Section 182 penalties are severe.
- NEVER apply group relief (Section 59AA) without confirming 100% ownership, residency, and the statutory continuity tests.
- NEVER produce a group-consolidated computation under Section 59B (R-PK-CT-3).
- NEVER quote FA 2025 specifics without verifying the gazetted text — mark **TBC** where uncertain.
- NEVER ignore the four advance-tax due dates (25 Sep, 25 Dec, 25 Mar, **15 Jun**); note that Q4 falls earlier than the quarter-end pattern.
- NEVER treat WHT, super tax, minimum tax, and ACT as alternatives without computing each — the liability is normal CIT vs (max of minimum tax, ACT), **plus** Section 4C, **less** creditable WHT and advance tax.
- NEVER present figures as definitive — always label as estimates pending reviewer sign-off by an ICAP CA / ICMA Pakistan member.

## Disclaimer

This skill and its outputs are for informational and computational purposes only and do not constitute tax, legal, or financial advice. All outputs must be reviewed and signed off by a qualified Pakistani tax professional (ICAP CA, ICMA Pakistan member, or FBR-recognised tax adviser) before filing or acting upon. Finance Act 2025 specifics flagged as **TBC** must be verified against the gazetted Act text before reliance. The latest verified version is maintained at [openaccountants.com](https://openaccountants.com).

## OpenAccountants footer

*OpenAccountants — open-source accounting skills for AI*

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
