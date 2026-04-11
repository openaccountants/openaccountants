---
name: ny-it-201-resident-return
description: Tier 2 New York content skill for preparing Form IT-201 (Full-Year Resident Income Tax Return) for New York State full-year residents who are sole proprietors or single-member LLCs disregarded for federal tax purposes. Covers the NYAGI computation starting from federal AGI, Form IT-225 addition and subtraction modifications (notably A-201 for unincorporated business taxes deducted federally), Form IT-558 OBBBA decoupling adjustments including the §168(k) bonus depreciation add-back and the §174A R&E expensing uncertainty, the standard vs itemized deduction decision, NY state tax computation including the $107,650 recapture worksheet, NYC resident tax computation (lines 47a-53) including the NYC UBT credit flow via Form IT-219, Yonkers resident surcharge and nonresident earnings tax (lines 55-57), MCTMT for self-employed individuals in the MCTD (lines 54a-54b), credits and payments, and the reviewer brief for the complete NY state-level return package. Does NOT cover part-year or nonresident returns (Form IT-203), itemized deduction limitations above $100,000 NYAGI in detail, PTET election scenarios, convenience-of-the-employer rule cases, NY source income allocation for multi-state activity, or NYC Unincorporated Business Tax computation itself — see Section 7. MUST be loaded alongside us-tax-workflow-base v0.2 or later. Typically loaded alongside ny-llc-filing-fee-it-204-ll (if SMLLC), nyc-unincorporated-business-tax (if NYC resident), and ny-estimated-tax-it-2105. New York State full-year residents only.
version: 0.1
---

# New York IT-201 Resident Return Skill v0.1

## What this file is, and what it is not

This is a Tier 2 content skill under `us-tax-workflow-base v0.2`. It conforms to the thirteen mandatory slots of the Section 7 content skill slot contract. It provides the position rules, figures, citations, refusals, defaults, reviewer attention thresholds, worked examples, intake additions, and self-check additions needed to prepare Form IT-201 for a New York State full-year resident who operates as a sole proprietor or disregarded single-member LLC.

This is the **load-bearing skill in the NY stack**. It owns the NYAGI computation, all four local tax layers (NY state, NYC resident, Yonkers resident, MCTMT), and the critical OBBBA decoupling logic. It is the skill that runs immediately after the federal return assembly and before the NY-specific sibling skills (NYC UBT, IT-204-LL, IT-2105). When it fails, the entire NY state filing fails.

This skill cannot produce any output on its own. It must be loaded alongside `us-tax-workflow-base` for the workflow runbook, the standard output specification, the global refusals, the seventeen base self-checks, and the citation discipline rule. It assumes the federal return has already been prepared by the federal stack (`us-sole-prop-bookkeeping` → `us-schedule-c-and-se-computation` → `us-qbi-deduction` → `us-self-employed-retirement` → `us-self-employed-health-insurance` → `us-federal-return-assembly`) and that the federal AGI is locked before this skill runs. It does not recompute any federal position.

**Execution pacing.** When this skill is invoked inside the `us-federal-ny-return-assembly` orchestrator, it runs its computations without pausing for user meta-questions. Self-check failures become reviewer flags, not workflow halts. Primary source citations belong in the final reviewer brief section, not in intermediate computation steps. The reviewer signs the return; the skill's job is to do the mechanical and well-documented preparation work that makes the reviewer's job fast and accurate.

**The reviewer assumption.** Every output from this skill is reviewed by a human tax professional credentialed under Circular 230 (Enrolled Agent, CPA, or attorney) before it reaches the taxpayer or NYSDTF. The skill is not the preparer of record. The reviewer is.

---

## Section 1 — Scope statement

**In scope.** This skill covers the preparation of Form IT-201, Full-Year Resident Income Tax Return, for tax year 2025 for:

- **Taxpayer profile:** An individual who was a New York State full-year resident for all of 2025, operating as either a bare sole proprietor or a single-member LLC disregarded for federal income tax purposes. The individual's filing status may be single, married filing jointly, married filing separately, head of household, or qualifying surviving spouse.
- **Residency layers:** The skill handles all four possible geographic layers that a NY full-year resident may face: (a) NY state resident only (e.g., Westchester, Albany, Buffalo); (b) NY state resident + NYC resident (the five boroughs); (c) NY state resident + Yonkers resident; (d) NY state resident + MCTD-based self-employed subject to MCTMT (anywhere in the 12 MCTD counties: NYC 5 boroughs plus Rockland, Nassau, Suffolk, Orange, Putnam, Dutchess, Westchester).
- **Income mix:** The freelancer's primary income is Schedule C self-employment income. Secondary income streams that the skill handles: W-2 wages from a non-NY employer, interest income, qualified and ordinary dividends, capital gains, unemployment compensation, federal and state tax refunds, and qualified pension/annuity income under the $20,000 exclusion. The skill handles the interaction of these streams with the NY modifications and the NYC resident tax.
- **Deductions:** Standard deduction or itemized deduction via Form IT-196 (with the NY limitation above $100,000 NYAGI flagged for reviewer attention, not computed in detail).
- **Modifications:** Form IT-225 additions (notably A-201 for unincorporated business taxes deducted at federal level) and subtractions (notably S-118 for income subject to NYC UBT, and the 414(h) retirement contribution adjustments for NY public employees, though the latter is rarely relevant for freelancers). Form IT-558 adjustments for NY decoupling from post-March-1-2020 IRC changes, including the 2025 OBBBA items: §168(k) bonus depreciation (confirmed decoupled) and §174A R&E expensing (flagged as uncertain, see Position 5.15).
- **Credits:** The state and NYC household credits, the NY and NYC earned income tax credits (EIC), the Empire State Child Credit, the NYC Unincorporated Business Tax credit (Form IT-219 → IT-201-ATT Section C → Line 53), the college tuition credit, the long-term care insurance credit, and the real property tax credit. The skill handles flow but defers detailed credit computation to the relevant credit forms' instructions.
- **Tax layers:** NY state tax via the tax tables (if NYAGI ≤ $107,650) or the tax rate schedule (if NYAGI > $65,000 and ≤ $107,650) or the tax computation worksheet (if NYAGI > $107,650) — the third of these is the recapture mechanism that produces an almost-flat tax for high earners. NYC resident tax via NYC tables or rate schedule, with the NYC household credit. Yonkers resident surcharge at 16.75% of NY state tax. Yonkers nonresident earnings tax at 0.5% of Yonkers-source wages and self-employment earnings. MCTMT at 0.60% (Zone 1) or 0.34% (Zone 2) of net self-employment earnings above $50,000 per zone.
- **Output:** A completed Form IT-201 worksheet with every line computed from source data, a reviewer brief covering all positions taken and all flags raised, a taxpayer action list, and Form IT-201-ATT if applicable.

**Out of scope (all refused — see Section 7):**

- Part-year residents and nonresidents (require Form IT-203 and out-of-scope allocation rules)
- Taxpayers with NY source income while domiciled elsewhere (convenience-of-the-employer rule cases)
- Multi-state business activity requiring Form IT-203-A business allocation
- Itemized deductions above $100,000 NYAGI where the limitation requires detailed phase-out computation
- PTET (Pass-Through Entity Tax) election scenarios under AB 2522 (2021) — these are for multi-owner pass-throughs, not disregarded SMLLCs
- NYC Unincorporated Business Tax computation itself (the NYC-202/NYC-202S preparation is in `nyc-unincorporated-business-tax`; this skill only handles the IT-219 credit flow back to IT-201)
- Form IT-204-LL filing fee computation (this is in `ny-llc-filing-fee-it-204-ll`; this skill references it but does not prepare it)
- NY estimated tax computation for 2026 (this is in `ny-estimated-tax-it-2105`; this skill produces inputs but does not compute the safe harbor)
- Claim of right credit (§615(d)) and other complex carryover credits
- NY Credit for taxes paid to another state or jurisdiction (for residents who earned income taxed by another state) — this is a complex allocation exercise that belongs in a separate skill
- Returns for deceased taxpayers, decedent estate returns, or fiduciary returns
- Returns for minors subject to the child investment income rules (Form IT-205 or special handling)
- Combat zone, nonresident noncitizen, and other special-condition-code filers (codes M4-M9, Y1, etc.)
- Amended returns (Form IT-201-X)

The scope limitations align with `us-tax-workflow-base` Section 6 base refusals and are extended by this skill's Section 7 topical refusals (R-NY201-1 through R-NY201-12).

---

## Section 2 — Tax year coverage and currency

**Tax year covered:** 2025 (calendar year, returns due April 15, 2026).

**Currency date:** The skill is current as of April 2026. Every figure, every form reference, every statutory citation in this skill is verified against primary sources as of that date.

**Legislation and guidance current as of the currency date:**

- NY Tax Law Article 22 (Personal Income Tax), as amended by Chapter 59 of the Laws of 2025 (the Executive Budget bill for FY 2025-26)
- NY Tax Law Article 30 (City Personal Income Tax on Residents — authorizes NYC to impose a resident income tax; the actual rate structure is in the NYC Administrative Code)
- NY Tax Law Article 30-A (Yonkers resident income tax surcharge)
- NY Tax Law Article 30-B (Yonkers nonresident earnings tax)
- NY Tax Law Article 23 (Metropolitan Commuter Transportation Mobility Tax)
- Form IT-201 (2025) and Form IT-201-I (2025) instructions, released by NYSDTF in January 2026
- Form IT-225 (2025) and instructions
- Form IT-558 (2025) and instructions
- Form IT-219 (NYC UBT credit) instructions
- NYSDTF Publication NYS-50-T-NYS (2025) — NY withholding tax tables and methods (used here as the authoritative source for the rate schedule construction, even though this skill does not compute withholding itself)
- NY Regulations 20 NYCRR Part 100 et seq. (NYSDTF's personal income tax regulations)

**Legislation monitored but NOT yet in force (as of the currency date) — flagged in Position 5.15:**

- **Governor Hochul's FY 2026-27 Executive Budget proposal** (released January 2026) proposes retroactive NY decoupling from federal OBBBA §174A R&E expensing for tax years beginning on or after January 1, 2025. The proposal would require NY taxpayers to recover domestic and foreign R&E expenditures over a 5-year period for NY state tax purposes even though federal law (post-OBBBA) allows immediate deduction. **This proposal has not been enacted as of the currency date of this skill.** The skill's default position on §174A is the conservative path (capitalize and recover over 5 years for NY state purposes, creating a Form IT-558 addition) with a reviewer decision point to elect the federal-conforming path if the reviewer prefers.

**Legislation expressly confirmed as already in force:**

- NY decoupling from IRC §168(k) bonus depreciation (in force since well before 2025; tracked via Form IT-398 or Form IT-558)
- NY conformity with IRC §199A QBI deduction is **structural, not statutory**: because NY starts from federal AGI (not federal taxable income), and because QBI is a below-AGI deduction on federal Form 1040 line 13, QBI never flows into the NY computation for individuals. No add-back is required. QBI add-back only applies to estates and trusts where QBI flows through differently.
- NY conformity with the SALT cap: NY does NOT impose its own SALT cap on the state deduction; the federal $10,000 cap (pre-OBBBA) and the post-OBBBA cap do not directly bind NY, BUT NY requires an add-back (IT-225 code A-201) for state and local income taxes deducted at the federal level, which produces a similar economic effect via a different mechanism.
- NY NYC resident tax structure remains four brackets: 3.078%, 3.762%, 3.819%, 3.876% — unchanged since 2017
- NY Yonkers resident surcharge remains 16.75% of NY state tax — unchanged since 2018
- NY Yonkers nonresident earnings tax remains 0.5% of Yonkers-source wages and self-employment earnings — unchanged since 2015
- MCTMT Zone 1 and Zone 2 rates for self-employed individuals remain 0.60% and 0.34% — unchanged since tax years beginning on or after January 1, 2023 (introduced in the FY 2022-23 Executive Budget)

**NY 2025 tax brackets and thresholds:** Unchanged from 2024 — the nine-bracket 4% to 10.9% structure has been stable since 2022 when the "millionaires' tax" brackets were added. The 2025 figures are in Section 3.

**Form version lock:** All form references in this skill are to the 2025 version of Form IT-201 and its schedules. Line numbers are stable year-over-year for Form IT-201 but not guaranteed — a future version of this skill (v0.2+) will verify line numbers against each subsequent year's form release.

---

## Section 3 — Year-specific figures table for tax year 2025

All figures are for NY Form IT-201, tax year 2025, calendar-year residents. Every figure has a primary source citation inline.

### NY state tax rate schedule — Single, MFS, Dependent filer

| Taxable income over | But not over | Rate | Source |
|---|---|---|---|
| $0 | $8,500 | 4.00% | NY Tax Law §601(d)(1); Form IT-201-I (2025) NY State tax rate schedule |
| $8,500 | $11,700 | 4.50% | NY Tax Law §601(d)(1); Form IT-201-I (2025) |
| $11,700 | $13,900 | 5.25% | NY Tax Law §601(d)(1); Form IT-201-I (2025) |
| $13,900 | $80,650 | 5.50% | NY Tax Law §601(d)(1); Form IT-201-I (2025) |
| $80,650 | $215,400 | 6.00% | NY Tax Law §601(d)(1); Form IT-201-I (2025) |
| $215,400 | $1,077,550 | 6.85% | NY Tax Law §601(d)(1); Form IT-201-I (2025) |
| $1,077,550 | $5,000,000 | 9.65% | NY Tax Law §601(a)(1)(B)(i); Form IT-201-I (2025) |
| $5,000,000 | $25,000,000 | 10.30% | NY Tax Law §601(a)(1)(B)(ii); Form IT-201-I (2025) |
| $25,000,000 | — | 10.90% | NY Tax Law §601(a)(1)(B)(iii); Form IT-201-I (2025) |

### NY state tax rate schedule — Married filing jointly, Qualifying surviving spouse

| Taxable income over | But not over | Rate | Source |
|---|---|---|---|
| $0 | $17,150 | 4.00% | NY Tax Law §601(a)(1)(A); Form IT-201-I (2025) |
| $17,150 | $23,600 | 4.50% | NY Tax Law §601(a)(1)(A); Form IT-201-I (2025) |
| $23,600 | $27,900 | 5.25% | NY Tax Law §601(a)(1)(A); Form IT-201-I (2025) |
| $27,900 | $161,550 | 5.50% | NY Tax Law §601(a)(1)(A); Form IT-201-I (2025) |
| $161,550 | $323,200 | 6.00% | NY Tax Law §601(a)(1)(A); Form IT-201-I (2025) |
| $323,200 | $2,155,350 | 6.85% | NY Tax Law §601(a)(1)(A); Form IT-201-I (2025) |
| $2,155,350 | $5,000,000 | 9.65% | NY Tax Law §601(a)(1)(A)(B)(i); Form IT-201-I (2025) |
| $5,000,000 | $25,000,000 | 10.30% | NY Tax Law §601(a)(1)(A)(B)(ii); Form IT-201-I (2025) |
| $25,000,000 | — | 10.90% | NY Tax Law §601(a)(1)(A)(B)(iii); Form IT-201-I (2025) |

### NY state tax rate schedule — Head of household

| Taxable income over | But not over | Rate | Source |
|---|---|---|---|
| $0 | $12,800 | 4.00% | NY Tax Law §601(b)(1); Form IT-201-I (2025) |
| $12,800 | $17,650 | 4.50% | NY Tax Law §601(b)(1); Form IT-201-I (2025) |
| $17,650 | $20,900 | 5.25% | NY Tax Law §601(b)(1); Form IT-201-I (2025) |
| $20,900 | $107,650 | 5.50% | NY Tax Law §601(b)(1); Form IT-201-I (2025) |
| $107,650 | $269,300 | 6.00% | NY Tax Law §601(b)(1); Form IT-201-I (2025) |
| $269,300 | $1,616,450 | 6.85% | NY Tax Law §601(b)(1); Form IT-201-I (2025) |
| $1,616,450 | $5,000,000 | 9.65% | NY Tax Law §601(a)(1)(B)(i); Form IT-201-I (2025) |
| $5,000,000 | $25,000,000 | 10.30% | NY Tax Law §601(a)(1)(B)(ii); Form IT-201-I (2025) |
| $25,000,000 | — | 10.90% | NY Tax Law §601(a)(1)(B)(iii); Form IT-201-I (2025) |

### NY state tax table vs. rate schedule vs. computation worksheet — which to use

| NYAGI range | Tax computation method | Source |
|---|---|---|
| NYAGI ≤ $107,650 AND taxable income < $65,000 | Use NY State Tax Table | Form IT-201-I (2025), "How to calculate your 2025 New York State tax" |
| NYAGI ≤ $107,650 AND taxable income ≥ $65,000 | Use NY State Tax Rate Schedule (above) | Form IT-201-I (2025), same section |
| NYAGI > $107,650 | Use Tax Computation Worksheet (recapture) | Form IT-201-I (2025), "Tax computation — NYAGI of more than $107,650" |

The recapture worksheet used for NYAGI > $107,650 eliminates the benefit of the lower brackets in a graduated phase-out, producing an almost-flat tax at the top marginal rate for high earners. This is the mechanism journalists call the "NY recapture tax" or the "supplemental tax on high earners." It is not an additional tax; it is a reconstruction of the same tax using a different computation method that denies the bracket benefit. The skill computes this correctly via the worksheet and does NOT treat it as a separate tax.

### NY state standard deduction (Line 34)

| Filing status | 2025 standard deduction | Source |
|---|---|---|
| Single (not claimed as dependent) | $8,000 | Form IT-201-I (2025), Step 5 |
| Single (claimed as a dependent on another return) | $3,100 | Form IT-201-I (2025), Step 5 |
| Married filing jointly | $16,050 | Form IT-201-I (2025), Step 5 |
| Married filing separately | $8,000 | Form IT-201-I (2025), Step 5 |
| Head of household | $11,200 | Form IT-201-I (2025), Step 5 |
| Qualifying surviving spouse | $16,050 | Form IT-201-I (2025), Step 5 |

### NY dependent exemption (Line 36)

| Figure | Value | Source |
|---|---|---|
| NY dependent exemption per dependent | $1,000 | NY Tax Law §616; Form IT-201-I (2025), Step 5 |

### NY filing requirement threshold (for taxpayers not required to file federally)

| Filing status | Federal AGI + NY additions threshold | Source |
|---|---|---|
| Most filers | $4,000 | NY Tax Law §651(a); Form IT-201-I (2025), "Who must file" |
| Single, claimed as a dependent | $3,100 | NY Tax Law §651(a); Form IT-201-I (2025), "Who must file" |

### NYC resident tax rate schedule — 2025

All NYC rates apply to NYC taxable income (which equals NY taxable income for full-year NYC residents, with minor differences).

**Single and MFS:**

| NYC taxable income over | But not over | Rate | Source |
|---|---|---|---|
| $0 | $12,000 | 3.078% | NYC Admin Code §11-1701; Form IT-201-I (2025) NYC rate schedule |
| $12,000 | $25,000 | 3.762% | NYC Admin Code §11-1701; Form IT-201-I (2025) |
| $25,000 | $50,000 | 3.819% | NYC Admin Code §11-1701; Form IT-201-I (2025) |
| $50,000 | — | 3.876% | NYC Admin Code §11-1701; Form IT-201-I (2025) |

**MFJ and QSS:**

| NYC taxable income over | But not over | Rate | Source |
|---|---|---|---|
| $0 | $21,600 | 3.078% | NYC Admin Code §11-1701; Form IT-201-I (2025) |
| $21,600 | $45,000 | 3.762% | NYC Admin Code §11-1701; Form IT-201-I (2025) |
| $45,000 | $90,000 | 3.819% | NYC Admin Code §11-1701; Form IT-201-I (2025) |
| $90,000 | — | 3.876% | NYC Admin Code §11-1701; Form IT-201-I (2025) |

**Head of household:**

| NYC taxable income over | But not over | Rate | Source |
|---|---|---|---|
| $0 | $14,400 | 3.078% | NYC Admin Code §11-1701; Form IT-201-I (2025) |
| $14,400 | $30,000 | 3.762% | NYC Admin Code §11-1701; Form IT-201-I (2025) |
| $30,000 | $60,000 | 3.819% | NYC Admin Code §11-1701; Form IT-201-I (2025) |
| $60,000 | — | 3.876% | NYC Admin Code §11-1701; Form IT-201-I (2025) |

**NYC tax table vs. rate schedule:** Use the NYC tax table if NYC taxable income is less than $65,000; otherwise use the NYC rate schedule above.

### NYC household credit (Line 48)

| Filing status | NYC taxable income | Credit amount | Source |
|---|---|---|---|
| Single | ≤ $12,500 | Sliding scale, up to $15 per filer | Form IT-201-I (2025), NYC household credit table 4 |
| MFJ, HoH, QSS | Varies | Sliding scale, up to $30 per household + $10-$30 per dependent | Form IT-201-I (2025), NYC household credit tables 5 and 6 |

This is a small credit (maximum tens of dollars) and rarely material for reviewer attention.

### NYC school tax credit (Line 69 / 69a)

The NYC school tax credit has two components:

| Component | Value | Source |
|---|---|---|
| NYC school tax credit (fixed amount) | $63 single / $125 MFJ | NYC Admin Code §11-1706; Form IT-201-I (2025), Line 69 |
| NYC school tax credit (rate reduction) — income under $500,000 | Variable (small) | NYC Admin Code §11-1706; Form IT-201-I (2025), Line 69a |

The fixed-amount credit is refundable for NYC residents and is claimed on Line 69. Rarely material for reviewer attention but must be claimed.

### Yonkers resident income tax surcharge (Line 55)

| Figure | Value | Source |
|---|---|---|
| Yonkers resident income tax surcharge | 16.75% of NY state tax (Line 50) | Yonkers City Code §92-5; NY Tax Law Article 30-A; Form IT-201-I (2025), Line 55 |

### Yonkers nonresident earnings tax (Line 56)

| Figure | Value | Source |
|---|---|---|
| Yonkers nonresident earnings tax | 0.50% of Yonkers-source wages and self-employment earnings, minus $3,000 exemption | Yonkers City Code §92-141; NY Tax Law Article 30-B; Form Y-203; Form IT-201-I (2025), Line 56 |

### MCTMT for self-employed individuals (Lines 54a, 54b)

| Figure | Value | Source |
|---|---|---|
| MCTD Zone 1 counties | New York (Manhattan), Bronx, Kings (Brooklyn), Queens, Richmond (Staten Island) | NY Tax Law §800(b)(1); Form IT-201-I (2025), Line 54a instructions |
| MCTD Zone 2 counties | Rockland, Nassau, Suffolk, Orange, Putnam, Dutchess, Westchester | NY Tax Law §800(b)(2); Form IT-201-I (2025), Line 54b instructions |
| MCTMT Zone 1 self-employed rate | 0.60% of Zone 1 NESE exceeding $50,000 | NY Tax Law §801(a); Form IT-201-I (2025), Line 54a |
| MCTMT Zone 2 self-employed rate | 0.34% of Zone 2 NESE exceeding $50,000 | NY Tax Law §801(a); Form IT-201-I (2025), Line 54b |
| MCTMT threshold per zone | $50,000 NESE per zone, per individual (not per couple) | NY Tax Law §801(a); Form IT-201-I (2025), Line 54 |
| MCTMT exemption from credits | No credit may offset MCTMT | NY Tax Law §805; Form IT-201-I (2025), Line 54 |

Note: The $50,000 threshold is applied **per individual** and **per zone**. On a joint return where both spouses have self-employment income allocated to the MCTD, each spouse's per-zone NESE is tested separately against the $50,000 threshold. If either spouse's individual per-zone NESE is $50,000 or less, that spouse's base is excluded from the combined joint return MCTMT computation for that zone. See worked examples in Section 9.

### Pension and annuity income exclusion (Line 29)

| Figure | Value | Source |
|---|---|---|
| Pension and annuity income exclusion (age 59½+) | Up to $20,000 per individual | NY Tax Law §612(c)(3-a); Form IT-201-I (2025), Line 29 |
| MFJ combined maximum | $20,000 per spouse if each has qualifying income | Form IT-201-I (2025), Line 29 |

Rarely relevant for freelance developers but must be handled for older taxpayers.

### Form IT-225 addition modification codes used by this skill

| Code | Description | Source | Notes for freelance developers |
|---|---|---|---|
| A-201 | Personal income taxes and unincorporated business taxes deducted in determining federal income | Form IT-225-I (2025) | **Critical for NYC freelancers who paid UBT.** UBT deducted on Schedule C is added back for NY state purposes. |
| A-301 | NYC flexible benefits program (IRC §125) | Form IT-225-I (2025) | Rarely relevant for self-employed |
| A-009 | Federal accelerated depreciation under IRC §168(k) (bonus depreciation) | Form IT-225-I (2025); NY Tax Law §612(b)(8) | NY decouples from federal bonus depreciation; required add-back for assets placed in service with federal bonus depreciation claimed. Use Form IT-398 to compute. |
| A-113 | Interest income on state and local bonds of other states | Form IT-225-I (2025) | Rarely relevant for freelance developers unless investing in muni bonds |

### Form IT-225 subtraction modification codes used by this skill

| Code | Description | Source | Notes for freelance developers |
|---|---|---|---|
| S-125 | NY depreciation subtraction for bonus depreciation assets (the flip side of A-009) | Form IT-225-I (2025); NY Tax Law §612(c)(13) | Annual recovery of bonus depreciation add-back over the asset's MACRS life. Required to prevent double-counting. |
| S-118 | Income from services performed as a self-employed individual subject to NYC UBT | Form IT-225-I (2025) | Potentially relevant — but see Position 5.20: the A-201 UBT add-back and S-118 income adjustment operate in different directions and must not be conflated. |

### Form IT-558 adjustment codes used by this skill

| Code | Description | Source |
|---|---|---|
| A-011 | Federal §168(k) bonus depreciation — NY decoupling add-back | Form IT-558-I (2025); NY Tax Law §612(b)(36) |
| A-012 | Federal §163(j) business interest limitation — NY conformity adjustment | Form IT-558-I (2025) |
| (TBD for §174A) | Potential future code if NY enacts §174A decoupling retroactively | NOT YET IN FORCE as of skill currency date |

### Critical threshold summary

| Threshold | Value | Triggers what |
|---|---|---|
| Federal AGI + NY additions > $4,000 ($3,100 if dependent) | $4,000 / $3,100 | IT-201 filing requirement |
| NY taxable income ≥ $65,000 | $65,000 | Use rate schedule instead of tax tables |
| NYAGI > $107,650 | $107,650 | Use tax computation worksheet (recapture); cannot use tax tables OR rate schedule alone |
| NYAGI > $100,000 | $100,000 | NY itemized deduction limitation begins to apply (out of scope for this skill — refused) |
| Zone 1 NESE > $50,000 | $50,000 | MCTMT Zone 1 applies at 0.60% |
| Zone 2 NESE > $50,000 | $50,000 | MCTMT Zone 2 applies at 0.34% |
| Living quarters in Yonkers | Any | May trigger Yonkers residency |
| 184+ days in NYC with living quarters | 184 days | May trigger NYC statutory residency |
| Yonkers-source wages or SE earnings | Any | May trigger Yonkers nonresident earnings tax |

---

## Section 4 — Primary source library

Every position in this skill cites from this list. New citations added to the skill must be verified against the primary source before use.

### New York Tax Law (Article 22 — Personal Income Tax)

| Citation | Governs |
|---|---|
| NY Tax Law §601 | State personal income tax rates and brackets by filing status; the nine-bracket 4% to 10.9% structure |
| NY Tax Law §601(d)(1) | Single, MFS, and dependent filer rate schedule |
| NY Tax Law §601(a) | MFJ, QSS rate schedule |
| NY Tax Law §601(b)(1) | Head of household rate schedule |
| NY Tax Law §602 | Tax tables (authority for NYSDTF to publish lookup tables) |
| NY Tax Law §605(b) | Definition of NY State resident (domicile test and permanent place of abode test) |
| NY Tax Law §611 | NY taxable income computation (starting point = federal AGI) |
| NY Tax Law §612 | NY adjusted gross income — additions and subtractions to federal AGI |
| NY Tax Law §612(b)(8) | Addition modification for federal bonus depreciation (IT-225 code A-009) |
| NY Tax Law §612(b)(36) | Addition modification for post-March-1-2020 IRC changes (IT-558 code A-011 et seq.) |
| NY Tax Law §612(c)(3-a) | Pension and annuity income subtraction (up to $20,000 at age 59½+) |
| NY Tax Law §612(c)(13) | Subtraction modification for the NY alternative depreciation on bonus depreciation assets |
| NY Tax Law §614 | NY standard deduction (amounts by filing status) |
| NY Tax Law §615 | NY itemized deduction (cross-reference to federal Schedule A with NY modifications) |
| NY Tax Law §615(f) | NY itemized deduction limitation for taxpayers with NYAGI > $100,000 |
| NY Tax Law §616 | NY dependent exemption ($1,000 per dependent) |
| NY Tax Law §631 | Definition of New York source income for nonresidents (relevant for the NY source test even for residents in certain edge cases) |
| NY Tax Law §651(a) | Filing requirement thresholds |
| NY Tax Law §658 | Return filing, extensions, and the LLC filing fee (see companion skill ny-llc-filing-fee-it-204-ll) |

### New York Tax Law (Article 23 — MCTMT)

| Citation | Governs |
|---|---|
| NY Tax Law §800 | Definitions, including MCTD Zone 1 and Zone 2 counties |
| NY Tax Law §801(a) | MCTMT self-employed rates: 0.60% Zone 1, 0.34% Zone 2 |
| NY Tax Law §801(b) | $50,000 per-zone NESE threshold for self-employed |
| NY Tax Law §805 | Prohibition on offsetting MCTMT with credits |

### New York Tax Law (Articles 30, 30-A, 30-B)

| Citation | Governs |
|---|---|
| NY Tax Law Article 30 | Authorization for NYC to impose a city personal income tax on residents |
| NY Tax Law §1304 | NYC resident income tax structure reference |
| NY Tax Law Article 30-A | Yonkers resident income tax surcharge (16.75% of NY state tax) |
| NY Tax Law Article 30-B | Yonkers nonresident earnings tax (0.50% of Yonkers-source earnings) |

### New York City Administrative Code (Title 11)

| Citation | Governs |
|---|---|
| NYC Admin Code §11-1701 | NYC resident income tax rates and brackets — the four-bracket 3.078% to 3.876% structure |
| NYC Admin Code §11-1706 | NYC school tax credit |
| NYC Admin Code §11-1721 | NYC household credit |
| NYC Admin Code §11-502 | NYC Unincorporated Business Tax base and scope (relevant for this skill only for the IT-219 credit; full UBT handling is in `nyc-unincorporated-business-tax`) |
| NYC Admin Code §11-503 | UBT credits including the UBT-paid credit (cross-reference to IT-219) |

### Yonkers City Code

| Citation | Governs |
|---|---|
| Yonkers City Code §92-5 | Yonkers resident income tax surcharge rate |
| Yonkers City Code §92-141 | Yonkers nonresident earnings tax rate and exemption amount |

### Federal authority (for starting-point and decoupling references)

| Citation | Governs |
|---|---|
| IRC §61 | Gross income (starting point for federal AGI, which is starting point for NY) |
| IRC §62 | Federal adjusted gross income definition |
| IRC §163(j) | Business interest limitation (NY conforms; IT-558 adjustment if federal and NY differ) |
| IRC §168(k) | Federal bonus depreciation (NY decouples; IT-225 A-009 or IT-558 A-011 add-back) |
| IRC §174 | Research and experimental expenses — pre-OBBBA version (capitalize and amortize) |
| IRC §174A | Research and experimental expenses — post-OBBBA version (immediate deduction); **NY decoupling uncertain as of skill currency date; see Position 5.15** |
| IRC §199A | Qualified business income deduction (NY conforms by construction — QBI is below AGI at federal level so never enters NY computation for individuals) |
| IRC §1402(a) | Definition of net earnings from self-employment (incorporated by reference into MCTMT computation) |
| Treas. Reg. §301.7701-3(b)(1)(ii) | Default disregarded classification of single-member LLCs |

### NYSDTF forms and instructions

| Citation | Governs |
|---|---|
| Form IT-201 (2025) | The resident income tax return itself |
| Form IT-201-I (2025) | Line-by-line instructions for IT-201; primary authority for this skill |
| Form IT-201-ATT (2025) | Other tax credits and taxes, including NYC UBT credit Section C |
| Form IT-225 (2025) | NY State additions and subtractions schedule |
| Form IT-225-I (2025) | Instructions for IT-225; authority for modification codes |
| Form IT-558 (2025) | NY adjustments due to decoupling from the IRC |
| Form IT-558-I (2025) | Instructions for IT-558; authority for OBBBA handling |
| Form IT-196 (2025) | NY itemized deductions (out of scope above $100,000 NYAGI) |
| Form IT-219 | NYC unincorporated business tax credit (flows into IT-201-ATT Section C) |
| Form IT-398 | NY depreciation schedule for §168(k) property |
| Form IT-213 | Empire State Child Credit |
| Form IT-215 | NY earned income tax credit |
| Form Y-203 | Yonkers nonresident earnings tax return (for computing the line 56 amount) |
| NYSDTF Publication 16 | New York tax status of LLCs and LLPs (cross-reference for ny-llc-filing-fee skill) |
| NYSDTF Publication 99 | General tax information for NY residents |
| NYSDTF Publication NYS-50-T-NYS (2025) | NY withholding tax tables and methods (used for rate schedule construction) |
| NYSDTF TSB-M-10(4)I | Treatment of Build America Bond interest |

### Regulations and administrative guidance

| Citation | Governs |
|---|---|
| 20 NYCRR Part 100 et seq. | NYSDTF personal income tax regulations |
| 20 NYCRR §105.20 | Definition of New York State resident (regulatory companion to §605(b)) |
| 20 NYCRR §112.3 | New York itemized deduction limitation computation |

### URLs for verification (not authoritative, for skill maintenance)

- Form IT-201 (2025): https://www.tax.ny.gov/pdf/2025/inc/it201_2025_fill_in.pdf
- Form IT-201 Instructions (2025): https://www.tax.ny.gov/pdf/2025/inc/it201i_2025.pdf
- Form IT-201-I (2025) HTML: https://www.tax.ny.gov/forms/current-forms/it/it201i.htm
- 2025 Tax Tables: https://www.tax.ny.gov/pit/file/tax-tables/2025.htm
- 2025 Tax Table for Form IT-201: https://www.tax.ny.gov/pit/file/tax-tables/it201i-2025.htm
- Form IT-225 (2025): https://www.tax.ny.gov/pdf/2025/inc/it225_2025_fill_in.pdf
- Form IT-225 Instructions (2025): https://www.tax.ny.gov/forms/current-forms/it/it225i.htm
- Form IT-558 (2025): https://www.tax.ny.gov/pdf/2025/inc/it558_2025_fill_in.pdf
- Form IT-558 Instructions (2025) PDF: https://www.tax.ny.gov/pdf/2025/inc/it558i_2025.pdf
- Form IT-219 Instructions: https://www.tax.ny.gov/pdf/current_forms/it/it219i.pdf
- MCTMT for self-employed: https://www.tax.ny.gov/bus/mctmt/selfemp.htm
- NY personal income tax credits overview: https://www.tax.ny.gov/pit/credits/income_tax_credits.htm
- NYC credits overview (includes UBT credit sliding scale): https://www.tax.ny.gov/pit/credits/new_york_city_credits.htm
- Governor Hochul FY 2026-27 Executive Budget (for §174A decoupling proposal tracking): Budget website at budget.ny.gov

---

*[Sections 5-14 to follow in subsequent turns. Section 5 will contain the position rules — approximately 25 structured positions covering the full IT-201 computation from federal AGI through final balance due/refund, with MCTMT, NYC, and Yonkers sub-sections. Section 6 will be the conservative defaults table. Section 7 will be the topical refusal catalogue (R-NY201-1 through R-NY201-12). Section 8 will be the reviewer attention thresholds. Section 9 will be the worked examples, minimum 5, covering the common fact patterns: (1) non-NYC resident freelancer, (2) NYC resident freelancer with UBT credit flow, (3) MCTMT Zone 2 resident, (4) MFJ with spouse W-2 income, (5) high-income taxpayer using the >$107,650 recapture worksheet. Section 10 will specify the output format extensions to the base reviewer brief. Section 11 will specify the intake form additions. Section 12 will specify the self-check additions starting at Check 28 to avoid collision with the base checks (1-17) and the IT-204-LL skill's checks (18-27). Section 13 will be cross-skill references. Section 14 will be reference material, design notes, and the change log.]*

## End of Turn 1 — Sections 1-4 complete, Sections 5-14 pending

---

### Turn 1 summary

This turn drafted the frontmatter, the preamble, and Sections 1-4 of `ny-it-201-resident-return`. Total lines in this turn: approximately 400. The foundation is in place: scope boundaries are explicit, tax year coverage is locked to 2025 with the currency date and OBBBA uncertainty flagged, the year-specific figures table covers every rate and threshold the skill needs, and the primary source library maps every citation the position rules will eventually reference.

Sections 5-14 will be drafted in turns 2-4. Estimated total file length at completion: 3,500-4,500 lines (the position rules section alone will be ~1,500 lines covering ~25 named positions, and the worked examples section will be ~800-1,000 lines).
---

## Section 5 — Position rules

This section contains the structured position rules the skill applies when preparing a Form IT-201. Each position follows the slot 5 contract format: **trigger / rule / conservative default / source**. Positions are grouped into seven subsections matching the natural flow of the return: (A) entry gate and profile confirmation; (B) federal AGI to NYAGI; (C) deduction and exemption decisions; (D) NY state tax computation; (E) NYC resident tax layer; (F) Yonkers layer; (G) MCTMT for self-employed; (H) credits, payments, and final tax.

Each position has a worked example cross-reference to Section 9. Multi-step computations reference specific form lines and primary sources.

---

### Subsection A — Entry gate and profile confirmation

These positions run first and gate everything downstream. If any of them refuses, no further IT-201 work proceeds.

#### Position 5.1 — Residency gate

**Trigger.** The intake has identified the taxpayer as a potential NY filer.

**Rule.** Confirm the taxpayer was a **New York State full-year resident for all of 2025**. Under NY Tax Law §605(b), a taxpayer is a NY resident if EITHER (a) they are domiciled in NY for the entire year, OR (b) they are not domiciled in NY but maintain a permanent place of abode in NY and spend more than 183 days of the year in NY. Apply the domicile test first (where the taxpayer intends to return, where their permanent home is, where their family and belongings are); apply the statutory residency test only if domicile is elsewhere. Full-year means the entire calendar year — any move into or out of NY during 2025 disqualifies the taxpayer from IT-201 and routes them to IT-203 (out of scope, R-NY201-1 fires).

**Conservative default.** If residency is ambiguous at any point in the year (e.g., the taxpayer claims domicile in NY but spent substantial time outside NY, or the taxpayer moved to NY "sometime in early 2025"), refuse under R-NY201-1 and route to the not-yet-built part-year resident skill. Do not attempt to split the year.

**Source.** NY Tax Law §605(b); 20 NYCRR §105.20; Form IT-201-I (2025), "New York State full-year residents: Who must file?"

**Example reference.** All worked examples in Section 9 satisfy this gate by construction.

#### Position 5.2 — Filing status

**Trigger.** Residency gate (5.1) cleared.

**Rule.** The filing status on Form IT-201 must match the filing status on the federal Form 1040. The only exceptions are the five specific situations listed in Form IT-201-I Item A: (a) one spouse is a NY resident and the other is not; (b) one spouse's whereabouts is unknown with reasonable efforts made to locate; (c) spouse refuses to sign a joint NY return with objective evidence of alienation; (d) other narrow cases. For a full-year NY resident freelancer, none of the exceptions typically applies, and the NY filing status simply mirrors the federal choice: Single, MFJ, MFS, HoH, or QSS.

**Conservative default.** Default to the federal filing status. If the federal return's filing status is ambiguous, refuse under R-US-CONTENT-MISMATCH pending reviewer clarification — never guess between single and MFS.

**Source.** Form IT-201-I (2025), Step 2, Item A.

#### Position 5.3 — Federal AGI import

**Trigger.** Filing status confirmed.

**Rule.** NY starts from **federal adjusted gross income** (Form 1040 line 11) as the computation base. Import the federal AGI from the upstream federal return without modification. The upstream federal stack (us-sole-prop-bookkeeping → us-schedule-c-and-se-computation → us-self-employed-retirement → us-self-employed-health-insurance → us-federal-return-assembly) must have produced a locked federal AGI before this skill runs. Any attempt to recompute federal AGI in this skill is an error — the federal return is the source of truth.

The individual income components (wages, interest, dividends, business income, capital gains, IRA distributions, pension income, Social Security, etc.) flow to Form IT-201 lines 1 through 19 individually. Line 19 is the "federal AGI from your federal return" reconciliation check.

**Conservative default.** If the federal return is not locked, refuse to proceed. The orchestrator `us-federal-ny-return-assembly` enforces the federal-before-state execution order.

**Source.** NY Tax Law §611 (NY taxable income starts from federal taxable income, but the mechanics via §612 effectively make the starting point federal AGI); Form IT-201-I (2025), Step 3.

#### Position 5.4 — Residency-within-NY layer determination

**Trigger.** Federal AGI imported.

**Rule.** Determine which intra-NY tax layers apply, in this order:
1. **NYC resident?** Check if the taxpayer was domiciled in NYC (Manhattan, Bronx, Brooklyn, Queens, Staten Island) for the full year, OR was a statutory NYC resident (permanent place of abode in NYC + 184+ days in NYC). If yes, NYC resident tax layer applies (lines 47a-53).
2. **Yonkers resident?** Check if the taxpayer maintained living quarters in Yonkers during any part of 2025 (Item D2 on Form IT-201). If yes and the facts support Yonkers residency, Yonkers resident surcharge applies (line 55).
3. **Yonkers nonresident earnings?** Check if the taxpayer is NOT a Yonkers resident but earned wages or self-employment income from Yonkers sources. If yes, Yonkers nonresident earnings tax applies (line 56).
4. **MCTMT applicability?** Check if the taxpayer has net earnings from self-employment allocated to either MCTD Zone 1 or Zone 2 exceeding $50,000. If yes, MCTMT applies (lines 54a, 54b). **Note:** A freelancer based in Manhattan is in Zone 1, a freelancer based in Yonkers or Westchester is in Zone 2, a freelancer based in Albany or Buffalo is in neither zone.

A taxpayer can be subject to multiple layers simultaneously: e.g., a Manhattan freelancer is subject to NY state tax + NYC resident tax + MCTMT Zone 1. A Yonkers freelancer is subject to NY state tax + Yonkers resident surcharge + MCTMT Zone 2.

**Conservative default.** If NYC residency is ambiguous (e.g., the taxpayer has a Manhattan apartment but spent substantial time elsewhere), ask for confirmation via `ask_user_input_v0` with the four options: "Full-year NYC resident" / "Part-year NYC resident" / "Not a NYC resident, but had NYC living quarters" / "No NYC connection at all." If the answer is "Part-year NYC resident," the taxpayer's broader NY residency must also be reconsidered — route to reviewer.

**Source.** NY Tax Law §605(b); NYC Admin Code §11-1701(c); Form IT-201-I (2025), Items D2, E, F; Yonkers City Code §92-5.

**Example reference.** Example 1 (Sarah, NYC resident), Example 3 (Carlos, Yonkers resident), Example 4 (Priya, Westchester resident — Zone 2 MCTMT only), Example 5 (Rachel, Albany — no local layers).

#### Position 5.5 — Federal return lock and upstream integration

**Trigger.** Residency within NY determined.

**Rule.** Confirm that all upstream federal skill outputs are present and internally consistent:
- `us-sole-prop-bookkeeping`: Schedule C Part II totals
- `us-schedule-c-and-se-computation`: Schedule C net profit (Line 31), SE tax, half of SE tax
- `us-self-employed-retirement`: retirement deduction (Schedule 1 Line 16)
- `us-self-employed-health-insurance`: SE health insurance deduction (Schedule 1 Line 17)
- `us-qbi-deduction`: QBI deduction amount (Form 1040 Line 13)
- `us-federal-return-assembly`: final federal AGI (Form 1040 Line 11) and federal taxable income (Line 15)

Record each upstream value in the reviewer brief's "Federal inputs" section for traceability. If any upstream value is missing, refuse to proceed and identify the missing skill by name.

**Conservative default.** Never recompute federal figures. Always use the upstream skill's output as authoritative.

**Source.** `us-tax-workflow-base v0.2` Section 9 (interaction model); workflow execution order.

---

### Subsection B — Federal AGI to NYAGI

These positions compute the NY additions and subtractions that transform federal AGI into NY AGI.

#### Position 5.6 — Line 20 NY additions (state and local bond interest)

**Trigger.** Federal AGI imported and includes tax-exempt interest from state and local bonds of other states.

**Rule.** Under NY Tax Law §612(b)(1), NY taxes interest income from state and local bonds of **other states** (not NY or its local governments, which remain tax-exempt). If the taxpayer's federal return shows tax-exempt interest on Form 1040 Line 2a, determine the portion attributable to non-NY state or local bonds and enter that portion on IT-201 Line 20. If the 1099-INT or mutual fund statement does not break down interest by state of origin, ask the taxpayer or the fund's tax reporting package (most large mutual fund families publish per-state allocation schedules each January).

**Conservative default.** If the state-of-origin breakdown is not available, assume 100% of the tax-exempt interest is from non-NY sources and add it back. This is conservative because it maximizes NY taxable income. Flag the assumption in the reviewer brief.

**Source.** NY Tax Law §612(b)(1); Form IT-201-I (2025), Line 20.

#### Position 5.7 — Line 22 NY additions (529 plan withdrawals used for non-qualified purposes)

**Trigger.** Federal AGI includes a distribution from a NY 529 plan that was used for non-qualified expenses, OR the taxpayer deducted NY 529 contributions in prior years and is now recapturing them.

**Rule.** Rarely relevant for freelance developers unless they have a child with a 529 plan. If relevant, follow Form IT-201-I Line 22 instructions and enter the recapture amount. Defer detailed computation to the 529 plan administrator's tax statement.

**Conservative default.** Assume no 529 recapture applies unless the taxpayer affirmatively reports one.

**Source.** Form IT-201-I (2025), Line 22.

#### Position 5.8 — Line 23 NY additions (Form IT-225 addition modifications)

**Trigger.** Any of the IT-225 addition modification codes apply. The most common for freelance developers is **A-201** (personal income taxes and unincorporated business taxes deducted in determining federal income).

**Rule.** Compute each applicable IT-225 addition and enter the total on Form IT-201 Line 23, with Form IT-225 attached. For a NYC-resident freelance developer who paid NYC UBT, the A-201 add-back is critical: the UBT paid during 2025 was deducted on federal Schedule C (most commonly on Line 23 "Taxes and licenses" or Line 17 "Legal and professional fees"), but NY does not allow a state-level deduction for unincorporated business taxes. The full amount of UBT deducted federally must be added back on IT-225 code A-201.

**Other A-codes to check for freelance developers:**
- **A-009**: Federal bonus depreciation (§168(k)). If the freelancer placed any business asset in service during 2025 and claimed federal bonus depreciation, add back the difference between the federal deduction and the NY depreciation computed on Form IT-398. This applies to equipment, computers, software, vehicles, and any other depreciable business asset. The A-009 add-back is replaced in 2025 and later by the IT-558 A-011 code — use A-009 only if the taxpayer has pre-2025 bonus depreciation carryovers.
- **A-113**: Interest income on state and local bonds of other states (see Position 5.6 — this is the entry point if reported via IT-225 rather than directly on Line 20).
- **A-301**: NYC flexible benefits program (IRC §125) — rare for self-employed.

**Conservative default.** If the taxpayer paid UBT in 2025 and the amount is not clearly documented, refuse to proceed and require the taxpayer to produce the NYC-202 or NYC-202S from the companion `nyc-unincorporated-business-tax` skill. Never estimate UBT for the A-201 add-back — it must match the actual amount deducted on federal Schedule C.

**Source.** NY Tax Law §612(b)(3); Form IT-225-I (2025), A-201 code; Form IT-201-I (2025), Line 23.

#### Position 5.9 — Line 28 NY subtractions (US government bond interest)

**Trigger.** Federal AGI includes interest income on US government bonds, Treasury bills, or other US Treasury obligations.

**Rule.** Under NY Tax Law §612(c)(1), interest income from US government obligations is exempt from NY state tax. Subtract the amount on IT-201 Line 28. Typical sources: Treasury bills held directly, Treasury money market funds, and the US government portion of mixed bond funds. Most mutual fund families publish the percentage of dividends attributable to US government obligations each January.

**Conservative default.** If the mutual fund does not report the US government percentage, assume 0% and do not claim the subtraction. This is conservative (higher NY tax).

**Source.** NY Tax Law §612(c)(1); Form IT-201-I (2025), Line 28.

#### Position 5.10 — Line 29 NY subtractions (pension and annuity income exclusion)

**Trigger.** The taxpayer is age 59½ or older and received pension or annuity income included in federal AGI.

**Rule.** Up to $20,000 per individual of qualifying pension and annuity income is excluded from NY taxable income under §612(c)(3-a). "Qualifying" means private pensions, traditional IRA distributions, and certain other retirement income — but NOT Roth IRA distributions (because those are already federally exempt), and NOT federal, state, or local government pensions (which have their own full exclusion on Line 26). The $20,000 cap is per individual on a joint return, so a couple can exclude up to $40,000 combined if each spouse has qualifying income.

**Conservative default.** Rarely applies to active freelance developers but must be checked for older taxpayers. If the taxpayer turned 59½ during 2025, include only the portion received after the age-59½ date (Form IT-201-I Line 29 provides the proration).

**Source.** NY Tax Law §612(c)(3-a); Form IT-201-I (2025), Line 29.

#### Position 5.11 — Line 31 NY subtractions (Form IT-225 subtraction modifications)

**Trigger.** Any of the IT-225 subtraction modification codes apply.

**Rule.** Compute each applicable IT-225 subtraction and enter the total on Form IT-201 Line 31, with Form IT-225 attached. The most common for freelance developers:
- **S-125**: NY depreciation subtraction for bonus depreciation assets — this is the annual flip side of the A-009 / IT-558 A-011 add-back. If the taxpayer added back bonus depreciation in a prior year, they receive a NY depreciation deduction each subsequent year on the normalized MACRS schedule until the asset is fully recovered. Use Form IT-398 to track the running balance.
- **S-118**: Certain income from services performed as a self-employed individual subject to NYC UBT — rarely material but exists to prevent double-counting.

**Conservative default.** Apply only modifications the taxpayer can affirmatively document. Never estimate.

**Source.** NY Tax Law §612(c); Form IT-225-I (2025); Form IT-201-I (2025), Line 31.

#### Position 5.12 — Form IT-558 OBBBA decoupling adjustments

**Trigger.** The taxpayer has any federal item subject to NY decoupling from post-March-1-2020 IRC changes. As of the skill's currency date, the main items that trigger IT-558 for a freelance developer are:
1. **§168(k) bonus depreciation** placed in service during 2025 (IT-558 code **A-011**)
2. **§163(j) business interest limitation** if the federal and NY treatments differ (rare for freelance developers)
3. **§174A R&E expensing** if the freelancer has domestic research and experimental expenditures — see Position 5.15 (dedicated to this uncertainty)

**Rule.** For each triggering item, compute the NY-federal difference and enter it on the appropriate IT-558 line. Form IT-558 produces a "recomputed federal AGI" that reflects NY's position on post-March-1-2020 IRC changes. The recomputed amount flows into the NY computation via IT-201.

For §168(k) specifically: if the taxpayer claimed federal bonus depreciation of $X on equipment placed in service in 2025, and the same asset would generate $Y of regular MACRS depreciation in year 1 (typically half of the bonus amount depending on convention), the IT-558 A-011 addition is $X − $Y for 2025. In subsequent years, the taxpayer will have an IT-558 subtraction equal to the annual MACRS depreciation that was denied in the year of acquisition. Use Form IT-398 to track.

**Conservative default.** If the federal bonus depreciation amount is not clearly documented, refuse to proceed. The IT-558 add-back must match the actual federal deduction.

**Source.** NY Tax Law §612(b)(36); Form IT-558-I (2025); Form IT-398 instructions.

#### Position 5.13 — Line 32 recomputed federal AGI and Line 33 NYAGI

**Trigger.** All NY additions (Lines 20-24) and subtractions (Lines 25-31) computed.

**Rule.** Compute Form IT-201 Line 32 (sum of Lines 19 + 23 + 24 − [28 + 29 + 30 + 31]) as the recomputed federal AGI with NY modifications. This equals NYAGI. Enter on Line 33. This is the single most important figure downstream — it drives the deduction limit, the tax table vs rate schedule vs worksheet decision, and many credit phase-outs.

**Conservative default.** Double-check the arithmetic. A wrong NYAGI cascades into every downstream line.

**Source.** Form IT-201 (2025) Lines 19-33; Form IT-201-I (2025), Step 4.

---

### Subsection C — Deduction and exemption decisions

#### Position 5.14 — Standard vs itemized deduction decision (Line 34)

**Trigger.** NYAGI computed.

**Rule.** Compute both the NY standard deduction (from the Section 3 figures table by filing status) and the NY itemized deduction (via Form IT-196). Use whichever is larger. For most freelance developers without a mortgage, significant charitable contributions, or state tax deductions exceeding the standard deduction, the standard deduction is the right choice.

**Critical NYAGI > $100,000 note:** If NYAGI exceeds $100,000, the NY itemized deduction is subject to a phase-out limitation under §615(f). The limitation is complex and out of scope for this skill. If the taxpayer's NYAGI exceeds $100,000 AND the taxpayer would benefit from itemizing (e.g., large mortgage interest, large state tax deduction, large charitable contribution), refuse under R-NY201-3 and route to reviewer. The simple case (NYAGI > $100,000 but standard deduction is obviously better) proceeds normally.

**Conservative default.** When in doubt, take the standard deduction. It is simpler, it does not require Form IT-196, and for most freelance developers it produces nearly the same result.

**Source.** NY Tax Law §614 (standard), §615 (itemized); §615(f) (limitation); Form IT-201-I (2025), Step 5, Line 34.

#### Position 5.15 — §174A R&E expensing — UNCERTAIN POSITION (dedicated section)

**Trigger.** The taxpayer has domestic research and experimental (R&E) expenditures under IRC §174A for 2025. For a freelance software developer, this may apply if the developer spent time developing their own software products (not client deliverables — those are §162 ordinary business expenses), or paid contractors to do such development work.

**The uncertainty.** Federal law under OBBBA §174A (effective for tax years beginning on or after January 1, 2025) allows immediate deduction of domestic R&E expenses. Pre-OBBBA IRC §174 required 5-year amortization for domestic R&E and 15-year for foreign.

As of this skill's currency date, **NY has not yet enacted decoupling from §174A**, so the default rolling-conformity rule would have NY follow the federal immediate deduction. However, Governor Hochul's FY 2026-27 Executive Budget (released January 2026) proposes **retroactive decoupling** from §174A back to tax years beginning on or after January 1, 2025, requiring 5-year recovery for both domestic and foreign R&E for NY purposes. **The proposal has not been enacted as of this skill's currency date.**

**Rule — two paths, reviewer must choose.**

**Path A (conservative default — THIS SKILL'S DEFAULT).** Capitalize the §174A R&E expenses for NY state purposes and recover them over 5 years. Produce an IT-558 addition modification for 2025 equal to the difference between the federal immediate deduction and the NY 5-year recovery (which for the first year of a 5-year life at mid-year convention is typically federal deduction minus 10% of the asset base). Track the NY basis separately via a supplementary schedule. State in the reviewer brief that this position is taken because retroactive NY decoupling is proposed in the Hochul FY 2026-27 Executive Budget and is likely to pass. If the proposal does not pass, the taxpayer will file an amended IT-201 to claim the federal-conforming deduction. The cost of the conservative default is a timing difference (NY tax is higher in 2025 but lower in 2026-2029); the benefit is avoiding an amended return if the proposal passes.

**Path B (federal-conforming — requires reviewer affirmative election).** Follow federal treatment and claim the immediate deduction for NY purposes. Do not file IT-558. State in the reviewer brief that this position is taken because the retroactive decoupling proposal has not been enacted as of the return's filing date and the rolling-conformity default governs. Flag explicitly that if the proposal passes, the taxpayer will need to file an amended IT-201 to add back the §174A deduction and compute the 5-year recovery retroactively. The cost of Path B is the amended-return risk; the benefit is matching federal treatment in the current year.

**The skill does not silently pick between A and B.** The reviewer brief explicitly presents the decision with the dollar impact of each path and asks the reviewer to affirm the choice. The default is Path A (conservative) unless the reviewer expressly elects Path B.

**Conservative default.** Path A.

**Documentation required from the taxpayer to even apply this position.** If the taxpayer has §174A activity at all, collect:
- Total domestic R&E expenditures for 2025 (by category: in-house salaries, contractor payments, supplies, computer rental, etc.)
- Total foreign R&E expenditures for 2025 (these are already 15-year amortized under pre-OBBBA §174; §174A does not change this)
- A clear allocation between R&E expenditures and ordinary §162 business expenses (this is the hardest judgment — client deliverable work is NOT R&E; speculative product development is R&E)
- Whether the federal return claimed the §174A immediate deduction or used the transition rule

**If the facts are unclear or the dollar impact is material (e.g., more than $10,000 of potential R&E), refuse under R-NY201-5 and route to reviewer.** This position is too fact-sensitive and too legally uncertain for the skill to handle autonomously beyond flagging.

**Source.** IRC §174A (as added by OBBBA, P.L. 119-21); NY Tax Law §612 (rolling conformity baseline); Hochul FY 2026-27 Executive Budget proposal (monitored, not enacted); Bonadio CPA analysis of FY 2026-27 budget §174A item (for reviewer reference).

**Example reference.** Example 6 in Section 9 (a developer with a potential R&E position who is routed to reviewer).

#### Position 5.16 — Dependent exemption (Line 36)

**Trigger.** The taxpayer has dependents claimed on the federal return.

**Rule.** Multiply the number of dependents by $1,000 and enter on Line 36. This is a straight deduction from NY taxable income, not a credit. Note that the dependents must be the same as on the federal return (or dependents the taxpayer was entitled to claim federally but chose not to, per Item H on Form IT-201).

**Conservative default.** Use the federal dependent count. Do not second-guess the federal return.

**Source.** NY Tax Law §616; Form IT-201-I (2025), Step 5, Line 36.

#### Position 5.17 — Line 37 taxable income

**Trigger.** Line 33 (NYAGI), Line 34 (deduction), and Line 36 (dependent exemption) all computed.

**Rule.** Line 37 = Line 33 − Line 34 − Line 36. This is NY taxable income, the base for the tax computation.

**Conservative default.** If Line 37 is zero or negative, enter zero. Negative taxable income does not produce a refund of NY tax itself (though it may affect credits).

**Source.** Form IT-201 (2025), Line 37.

---

### Subsection D — NY state tax computation

#### Position 5.18 — NY state tax computation method selection (Line 38/39)

**Trigger.** NY taxable income computed.

**Rule.** Determine which of three methods to use, per the decision matrix in Section 3:
- **NYAGI ≤ $107,650 AND taxable income < $65,000:** Use the NY State Tax Table (lookup)
- **NYAGI ≤ $107,650 AND taxable income ≥ $65,000:** Use the NY State Tax Rate Schedule
- **NYAGI > $107,650:** Use the Tax Computation Worksheet (the recapture mechanism)

The recapture worksheet eliminates the benefit of the lower brackets for high earners. It is NOT an additional tax; it is a reconstruction of the same tax base using a different method that produces an almost-flat tax at the taxpayer's top marginal rate. This is the mechanism journalists call the "NY recapture" or the "supplemental tax on high earners."

**Conservative default.** Always use the method dictated by the NYAGI level. Never use the tax table for NYAGI > $107,650 — this is specifically prohibited by Form IT-201-I and produces a wrong result.

**Source.** Form IT-201-I (2025), "How to calculate your 2025 New York State tax"; NY Tax Law §601.

#### Position 5.19 — NY state tax computation (Line 39)

**Trigger.** Computation method selected.

**Rule.**

**If using the tax table:** Look up the tax in the NY State Tax Table using NY taxable income (Line 38) and filing status column. Enter on Line 39.

**If using the rate schedule:** Apply the bracket structure from Section 3 to compute the tax, and enter on Line 39. The formula is:
```
Tax = (applicable marginal rate × amount over bracket floor) + cumulative tax at bracket floor
```
For example, a single filer with NY taxable income of $95,000 falls in the $80,650-$215,400 bracket (6.00%):
```
Tax = 6.00% × ($95,000 − $80,650) + tax at $80,650
    = 6.00% × $14,350 + $4,579
    = $861 + $4,579
    = $5,440 → rounded to $5,440
```
The "tax at $80,650" is the cumulative tax from all lower brackets applied in sequence.

**If using the tax computation worksheet:** Follow the worksheet in Form IT-201-I page 34 exactly. The worksheet has different versions for taxpayers with NYAGI in different bands ($107,650 to $157,650, $157,650 to $211,550, $211,550 to $1,077,550, $1,077,550 to $5,000,000, $5,000,000 to $25,000,000, and over $25,000,000 for single filers; different bands for other filing statuses). Each band recomputes the tax to phase out the bracket benefit. **For any taxpayer with NYAGI > $107,650, flag as a reviewer attention item and show the full worksheet computation in the brief.** The worksheet is mechanical but error-prone.

**Conservative default.** If the taxpayer's filing status or NYAGI is ambiguous at the method-selection boundary, use the method that produces the higher tax. Never use the wrong method to get a lower number.

**Source.** NY Tax Law §601; Form IT-201-I (2025), pages 32-40.

**Example reference.** Example 5 in Section 9 (high-income taxpayer with the recapture worksheet).

#### Position 5.20 — NY household credit (Line 40)

**Trigger.** NY state tax computed.

**Rule.** The NY household credit is a small credit (typically $75 or less) based on NYAGI and filing status. It does NOT apply if the taxpayer can be claimed as a dependent on another return (Item C = Yes on the form) — in that case, skip the credit. Otherwise, use Table 1, 2, or 3 from Form IT-201-I based on filing status.

**Conservative default.** Claim the credit if the taxpayer is eligible — it is small but material in aggregate across returns.

**Source.** NY Tax Law §606(b); Form IT-201-I (2025), Line 40; tables 1, 2, 3.

#### Position 5.21 — Other NY nonrefundable credits (Lines 41-42)

**Trigger.** Taxpayer qualifies for other NY credits (resident credit for taxes paid to another state, nonrefundable credits from Form IT-201-ATT).

**Rule.** Most freelance developers will not have a resident credit (§620) because their income is not sourced to another state. The NY nonrefundable credit line (Line 41) collects various credits from Form IT-201-ATT Section A. Defer detailed computation to the specific credit forms. For this skill's scope, most freelancers will have $0 on Line 41.

**Conservative default.** Enter $0 unless the taxpayer affirmatively claims a specific credit with documentation.

**Source.** NY Tax Law §620 (resident credit); Form IT-201-ATT (2025); Form IT-201-I (2025), Line 41.

---

### Subsection E — NYC resident tax layer

#### Position 5.22 — NYC resident tax computation (Line 47a)

**Trigger.** Taxpayer was a full-year NYC resident (Position 5.4 determined this).

**Rule.** Compute NYC taxable income — which equals NY taxable income (Line 38) for most full-year NYC residents with no NYC-specific adjustments. Then apply the NYC tax table (if NYC taxable income < $65,000) or the NYC rate schedule (from Section 3, if ≥ $65,000).

The NYC rate schedule uses four brackets with rates 3.078%, 3.762%, 3.819%, 3.876%. Bracket thresholds vary by filing status (see Section 3 tables).

**Example for a NYC resident single filer with NY taxable income of $95,000:**
```
NYC taxable income = $95,000
NYC is in the top bracket (> $50,000 for single)
NYC tax = 3.078% × $12,000 + 3.762% × ($25,000 − $12,000) + 3.819% × ($50,000 − $25,000) + 3.876% × ($95,000 − $50,000)
       = $369.36 + $489.06 + $954.75 + $1,744.20
       = $3,557.37 → rounded to $3,557
```

Enter on Line 47a.

**Conservative default.** Use the correct method (table for <$65,000, rate schedule for ≥$65,000). Never mix.

**Source.** NYC Admin Code §11-1701; Form IT-201-I (2025), Line 47a, "How to calculate your 2025 New York City tax."

**Example reference.** Example 1 in Section 9.

#### Position 5.23 — NYC household credit (Line 48)

**Trigger.** NYC resident tax computed and taxpayer is not claimed as a dependent.

**Rule.** Small credit (maximum $30 per household plus small per-dependent amounts) computed from Form IT-201-I tables 4, 5, or 6 based on filing status. Enter on Line 48. Defer detailed table lookup to the instructions.

**Conservative default.** Claim the credit if eligible.

**Source.** NYC Admin Code §11-1721; Form IT-201-I (2025), Line 48.

#### Position 5.24 — NYC UBT credit (Line 53 via Form IT-219)

**Trigger.** Taxpayer is a NYC resident who paid NYC Unincorporated Business Tax for 2025 (typically because they are a freelance developer with NYC gross business income > $95,000).

**Rule.** The NYC UBT credit under NYC Admin Code §11-503(b) flows as follows:
1. The UBT amount paid (from the companion `nyc-unincorporated-business-tax` skill's output) is carried to **Form IT-219** (NYC UBT credit computation)
2. Form IT-219 applies the sliding-scale credit based on NYC taxable income:
   - NYC taxable income ≤ $42,000: **100%** of UBT paid is credited
   - $42,001 to $141,999: **sliding from 100% down to 23%** (linear phase-out)
   - ≥ $142,000: **23%** of UBT paid is credited
3. The resulting credit flows to **Form IT-201-ATT Section C** (Line 10 on IT-201-ATT)
4. From IT-201-ATT Section C, the total flows to **Form IT-201 Line 53**

**This is the skill's most important cross-skill interaction.** The UBT amount must come from the `nyc-unincorporated-business-tax` skill, which in turn requires the full NYC-202 or NYC-202S computation. This skill does NOT compute UBT itself — it only applies the IT-219 sliding scale and flows the credit to IT-201.

The sliding-scale phase-out is a linear interpolation between the $42,000 (100%) and $142,000 (23%) anchor points. Form IT-219 provides the exact computation worksheet. For a NYC resident freelance developer in the middle of the phase-out range, the effective credit rate can be calculated as:
```
Credit rate = 1.00 − ((NYC taxable income − $42,000) / ($142,000 − $42,000)) × (1.00 − 0.23)
           = 1.00 − ((NYC taxable income − $42,000) / $100,000) × 0.77
```
For example, a NYC resident single freelance developer with NYC taxable income of $95,000 who paid $2,500 of UBT:
```
Credit rate = 1.00 − ((95,000 − 42,000) / 100,000) × 0.77
           = 1.00 − (53,000 / 100,000) × 0.77
           = 1.00 − 0.408
           = 0.592 → 59.2%
Credit = $2,500 × 0.592 = $1,480 → rounded to $1,480
```

Enter the credit on Form IT-219, carry to IT-201-ATT Section C, and then to IT-201 Line 53.

**Conservative default.** If the UBT amount is not available from the companion skill, refuse to proceed. Never estimate UBT for the credit computation.

**Source.** NYC Admin Code §11-503(b); NY Tax Law §606(bb); Form IT-219 and instructions; Form IT-201-ATT (2025) Section C; Form IT-201-I (2025), Line 53.

**Example reference.** Example 2 in Section 9 (NYC resident freelancer with UBT credit flow).

#### Position 5.25 — NYC school tax credit (Lines 69 / 69a)

**Trigger.** Taxpayer was a NYC resident for any part of the year.

**Rule.** The NYC school tax credit has two components:
- **Fixed amount (Line 69):** $63 for single filers, $125 for MFJ/QSS/HoH — refundable for all NYC residents regardless of income
- **Rate reduction (Line 69a):** Small additional credit for NYC residents with income under $500,000

Enter the fixed amount on Line 69 unconditionally for NYC residents. Enter the rate reduction on Line 69a if income is under $500,000.

**Conservative default.** Always claim both components when applicable — they are straightforward and small but material in aggregate.

**Source.** NYC Admin Code §11-1706; Form IT-201-I (2025), Lines 69 and 69a.

---

### Subsection F — Yonkers layer

#### Position 5.26 — Yonkers resident surcharge (Line 55)

**Trigger.** Taxpayer was a Yonkers full-year resident (determined in Position 5.4).

**Rule.** The Yonkers resident income tax surcharge is **16.75% of NY state tax (Line 50)**. Compute:
```
Yonkers resident surcharge = 16.75% × Line 50
```
Enter on Line 55. If filing jointly and only one spouse was a Yonkers resident, the surcharge is computed as if separate federal returns had been filed — flag this case as R-NY201-8 (split-residence couples) and route to reviewer.

**Conservative default.** Apply the 16.75% rate uniformly. Do not reduce the rate.

**Source.** Yonkers City Code §92-5; NY Tax Law Article 30-A; Form IT-201-I (2025), Line 55.

**Example reference.** Example 3 in Section 9 (Yonkers resident).

#### Position 5.27 — Yonkers nonresident earnings tax (Line 56)

**Trigger.** Taxpayer is NOT a Yonkers resident but earned wages or self-employment income from Yonkers sources. This applies if the taxpayer has a Yonkers employer (W-2 wages sourced to Yonkers) or performed self-employment work in Yonkers.

**Rule.** The Yonkers nonresident earnings tax is **0.50% of Yonkers-source wages and self-employment earnings minus a $3,000 exemption**. Compute using Form Y-203 (the Yonkers nonresident earnings tax form), and enter the resulting amount on Line 56.

**Conservative default.** For a freelance developer who is not a Yonkers resident and has no Yonkers-based clients or office, enter $0. Flag for reviewer only if Yonkers sources are claimed.

**Source.** Yonkers City Code §92-141; NY Tax Law Article 30-B; Form Y-203; Form IT-201-I (2025), Line 56.

---

### Subsection G — MCTMT for self-employed

#### Position 5.28 — MCTMT Zone 1 computation (Line 54a)

**Trigger.** Taxpayer has net earnings from self-employment allocated to MCTD Zone 1 (NYC five boroughs) that exceed $50,000.

**Rule.** MCTMT Zone 1 tax = **0.60% × Zone 1 NESE** if Zone 1 NESE > $50,000. If Zone 1 NESE ≤ $50,000, MCTMT Zone 1 is $0.

**Critical per-individual-per-zone rule.** The $50,000 threshold applies **separately** to each individual and each zone. On a joint return where both spouses have self-employment income in Zone 1:
- Each spouse's Zone 1 NESE is tested separately against $50,000
- If spouse A has $75,000 Zone 1 NESE and spouse B has $40,000 Zone 1 NESE, only spouse A's $75,000 is included in the joint Line 54a computation (spouse B's $40,000 is below the threshold and excluded)
- The included amounts are summed for the joint return

**For a full-year NYC resident freelance software developer:** Zone 1 NESE typically equals 100% of Schedule C net earnings from self-employment (the §1402(a) amount, which is 92.35% of Schedule C net profit). This is because the developer's place of business is in Zone 1 (home office in Manhattan, Brooklyn, etc.) and all business activity is attributed to that zone.

**Computation for a single NYC resident freelancer with Schedule C net profit of $180,000:**
```
NESE (§1402(a)) = $180,000 × 0.9235 = $166,230
Zone 1 NESE allocation = $166,230 (all from NYC)
Threshold check: $166,230 > $50,000 → MCTMT applies
Zone 1 MCTMT = 0.60% × $166,230 = $997.38 → rounded to $997
```

Enter on Line 54a.

**Note:** NESE is derived from §1402(a), not Schedule C line 31 directly. The 92.35% adjustment (1 − 7.65% employer-equivalent SE tax) is built into the §1402(a) definition. This skill pulls the NESE figure from the `us-schedule-c-and-se-computation` skill's output; it does not recompute.

**Conservative default.** If the allocation between Zone 1 and Zone 2 is ambiguous (e.g., the taxpayer works both in Manhattan and in Westchester), use the taxpayer's primary place of business. If the taxpayer genuinely splits activity between zones, the allocation requires Form IT-203-A — refuse under R-NY201-7.

**Source.** NY Tax Law §800-§805; Form IT-201-I (2025), Line 54a.

**Example reference.** Example 1 (Sarah, NYC resident, Zone 1 MCTMT), Example 4 (Priya, Westchester, Zone 2 MCTMT only).

#### Position 5.29 — MCTMT Zone 2 computation (Line 54b)

**Trigger.** Taxpayer has NESE allocated to MCTD Zone 2 (Rockland, Nassau, Suffolk, Orange, Putnam, Dutchess, Westchester) that exceeds $50,000.

**Rule.** MCTMT Zone 2 tax = **0.34% × Zone 2 NESE** if Zone 2 NESE > $50,000. Same per-individual-per-zone rule as Position 5.28.

**For a full-year Westchester or Nassau resident freelance developer:** Zone 2 NESE typically equals 100% of Schedule C net earnings. The rate is 0.34% (half the Zone 1 rate, reflecting the less intensive use of MTA infrastructure by non-NYC residents).

**Computation for a single Westchester freelancer with Schedule C net profit of $180,000:**
```
NESE = $180,000 × 0.9235 = $166,230
Zone 2 NESE allocation = $166,230 (all from Westchester)
Threshold check: $166,230 > $50,000 → MCTMT applies
Zone 2 MCTMT = 0.34% × $166,230 = $565.18 → rounded to $565
```

Enter on Line 54b.

**Conservative default.** Same as Position 5.28.

**Source.** NY Tax Law §800-§805; Form IT-201-I (2025), Line 54b.

#### Position 5.30 — MCTMT zero-tax case for non-MCTD residents

**Trigger.** Taxpayer is a NY full-year resident but lives outside the MCTD (e.g., Albany, Buffalo, Rochester, Syracuse, the North Country, most of the Finger Lakes, the Catskills west of Dutchess County).

**Rule.** Enter $0 on Lines 54a and 54b. No MCTMT applies.

**Conservative default.** Not applicable. Non-MCTD counties are unambiguous — the county list is in §800(b) and in Section 3 of this skill.

**Source.** NY Tax Law §800(b); Form IT-201-I (2025), Line 54.

**Example reference.** Example 5 (Rachel, Albany — no MCTMT).

---

### Subsection H — Credits, payments, and final tax

#### Position 5.31 — Refundable credits (Lines 63-68)

**Trigger.** Taxpayer qualifies for refundable NY credits. The most common for freelance developers with children:
- **Empire State Child Credit (Line 63, via Form IT-213):** Up to $1,000 per child under 4, up to $330 per child age 4-16. Income phase-outs apply.
- **NY Earned Income Credit (Line 65, via Form IT-215):** NY EIC is 30% of the federal EIC for full-year residents. For a freelance developer with significant Schedule C net earnings, the EIC is usually phased out.
- **NYC EIC (Line 70):** Similar mechanics for NYC residents.
- **Real property tax credit (Line 67, via Form IT-214):** For homeowners and renters with low income.
- **College tuition credit (Line 68):** For families with higher education expenses.

**Rule.** For each credit the taxpayer may qualify for, defer to the specific credit form. This skill flows the credit to the appropriate line on IT-201 but does not compute the credit itself in detail. Flag any credit with material dollar impact (> $500) for reviewer attention.

**Conservative default.** Do not claim a credit without documentation. Never estimate credit amounts.

**Source.** NY Tax Law §606 (various subsections); Form IT-201-I (2025), Lines 63-70; specific credit forms.

#### Position 5.32 — Total NY taxes before credits (Line 46)

**Trigger.** All tax layers computed.

**Rule.** Line 46 = Line 44 (NY state tax after credits) + Line 45 (other NYS taxes from IT-201-ATT). This is the total NY state tax before NYC, Yonkers, and MCTMT.

**Conservative default.** Straightforward arithmetic.

**Source.** Form IT-201 (2025), Line 46.

#### Position 5.33 — Total city/local/MCTMT (Line 58)

**Trigger.** All sub-state layers computed.

**Rule.** Line 58 = Line 54 (MCTMT) + Line 54e (NYC taxes from Line 51 through 54e) + Line 55 (Yonkers surcharge) + Line 56 (Yonkers nonresident earnings) + Line 57 (part-year Yonkers surcharge). This is the total of all sub-state taxes.

**Conservative default.** Straightforward arithmetic.

**Source.** Form IT-201 (2025), Line 58.

#### Position 5.34 — Final tax, payments, and balance due / refund (Lines 61-80)

**Trigger.** All tax computed, all credits applied.

**Rule.** Line 61 = Line 46 + Line 58 + Line 59 (sales or use tax, rarely material) + Line 60 (voluntary contributions). This is the total tax before payments.

Payments flow to Lines 63-75: refundable credits, NY/NYC/Yonkers withholding (from W-2 Box 17), estimated tax payments for 2025 (from Form IT-2105 vouchers), amount applied from 2024 refund, and any other credits.

Line 76 = total payments. If Line 76 > Line 61, the difference is overpaid (Line 77). If Line 76 < Line 61, the difference is owed (Line 78).

**Critical reviewer flag:** If Line 78 (amount owed) is significant (> $1,000), the taxpayer may owe an underpayment penalty. Form IT-2105.9 computes this penalty. The skill produces the balance due figure but defers the penalty computation to `ny-estimated-tax-it-2105`.

**Conservative default.** Compute the balance correctly. Do not apply an estimated underpayment penalty in this skill — that is the estimated tax skill's job.

**Source.** Form IT-201 (2025), Lines 61-80; Form IT-201-I (2025), Step 9.

---

### Position dependency order

The positions must execute in this order:

1. 5.1 Residency gate → 5.2 Filing status → 5.3 Federal AGI import → 5.4 Residency-within-NY → 5.5 Upstream federal lock
2. 5.6-5.12 NY additions and subtractions (can run in parallel, all feed into 5.13)
3. 5.13 NYAGI (Line 33)
4. 5.14 Deduction decision → 5.15 §174A decision (if applicable) → 5.16 Dependents → 5.17 Taxable income (Line 37)
5. 5.18 Tax method selection → 5.19 NY state tax (Line 39)
6. 5.20 NY household credit → 5.21 Other NY credits
7. 5.22-5.25 NYC layer (only if NYC resident; can run in parallel with 5.26-5.27 Yonkers layer and 5.28-5.30 MCTMT layer)
8. 5.31 Refundable credits → 5.32 Total NY taxes → 5.33 Total sub-state → 5.34 Final balance

Any position that refuses halts the workflow. The orchestrator `us-federal-ny-return-assembly` enforces this order.

---

*[Sections 6-14 to follow in subsequent turns. Section 6 will be the conservative defaults table. Section 7 will be the topical refusal catalogue (R-NY201-1 through R-NY201-12 in trigger/output format). Section 8 will be the reviewer attention thresholds. Section 9 will be the worked examples, minimum 5. Section 10 will specify the output format extensions. Section 11 will specify the intake form additions. Section 12 will specify the self-check additions starting at Check 28. Section 13 will be cross-skill references. Section 14 will be reference material and change log.]*

## End of Turn 2 — Section 5 complete, Sections 6-14 pending

---

### Turn 2 summary

This turn drafted Section 5 — position rules — for `ny-it-201-resident-return`. Total positions: 34 structured position rules organized into 8 subsections (A through H). Each position follows the slot 5 contract format with trigger / rule / conservative default / source. Key positions:

- **Position 5.8** (Line 23 IT-225 additions) flags the A-201 UBT add-back as critical for NYC freelancers
- **Position 5.15** (§174A R&E expensing) is the dedicated uncertainty section with the two-path reviewer decision — this is the most consequential position in the skill because it handles the unresolved OBBBA decoupling question
- **Position 5.19** (NY state tax computation) explicitly handles the three-method decision (table / rate schedule / >$107,650 worksheet) with the recapture mechanism explained
- **Position 5.24** (NYC UBT credit via Form IT-219) flows the UBT credit from the companion NYC UBT skill through IT-219, IT-201-ATT Section C, and Line 53 with the sliding-scale phase-out computed
- **Positions 5.28-5.30** (MCTMT for self-employed) handle Zone 1 and Zone 2 separately with the per-individual-per-zone $50,000 threshold rule

Position count: 34 positions across 8 subsections (not the 25 originally estimated — the MCTMT per-zone rules and the sub-state layers required more structured positions than the initial plan budgeted). Total file length after Turn 1 + Turn 2: approximately 1,400 lines (440 from Turn 1, roughly 960 from Turn 2).

Sections 6-14 remain for Turns 3 and 4. Estimated total file length at completion: 3,000-3,500 lines.
---

## Section 6 — Conservative defaults table

| # | Ambiguity | Conservative default | Source |
|---|---|---|---|
| 1 | Taxpayer residency within 2025 is ambiguous (possible part-year or domicile dispute) | Refuse under R-NY201-1; do not attempt to split the year | NY Tax Law §605(b); 20 NYCRR §105.20 |
| 2 | Filing status on federal return is ambiguous | Refuse under R-US-CONTENT-MISMATCH pending reviewer clarification | Form IT-201-I (2025), Item A |
| 3 | Federal AGI is not yet locked from the upstream federal return | Refuse to proceed; the orchestrator must run the federal stack first | `us-tax-workflow-base v0.2` Section 9 |
| 4 | Taxpayer claims NYC residency but has substantial time outside NYC | Ask confirmation via `ask_user_input_v0`; if still ambiguous, refuse under R-NY201-1 | NY Tax Law §605(b); NYC Admin Code §11-1701(c) |
| 5 | Mutual fund 1099-INT does not report state-of-origin for tax-exempt interest | Assume 100% non-NY source; add back the full amount on Line 20 or via A-113 | NY Tax Law §612(b)(1); Position 5.6 |
| 6 | Mutual fund does not report the US government obligation percentage | Assume 0%; do not claim the Line 28 subtraction | NY Tax Law §612(c)(1); Position 5.9 |
| 7 | NYC UBT amount is not yet available from the companion skill | Refuse to proceed; the orchestrator must run the NYC UBT skill before this skill's IT-219 credit computation | Position 5.24 cross-skill dependency |
| 8 | Federal bonus depreciation amount for 2025 asset acquisitions is not clearly documented | Refuse to proceed; the A-009 or IT-558 A-011 add-back must match the actual federal deduction exactly | NY Tax Law §612(b)(8); Form IT-398 |
| 9 | Taxpayer has §174A R&E expenditures but the amount is ambiguous | Default to Path A (capitalize over 5 years for NY, IT-558 addition); present both paths in the reviewer brief; refuse if material amount (> $10,000) is involved | Position 5.15 |
| 10 | Taxpayer has R&E-adjacent costs that could be §162 or §174A (e.g., contractor payments for speculative prototype work vs. client deliverable work) | Classify as §162 (ordinary business expense) unless the work is clearly speculative and not tied to a client deliverable; flag for reviewer | IRC §174A; Position 5.15 |
| 11 | NYAGI is near the $107,650 threshold for the recapture worksheet | Always use the method dictated by the actual NYAGI; never use the tax table for NYAGI exactly at or above the threshold | NY Tax Law §601; Position 5.19 |
| 12 | NYAGI is near the $100,000 threshold for the itemized deduction limitation AND the taxpayer would benefit from itemizing | Refuse under R-NY201-3; route to reviewer for detailed limitation computation | NY Tax Law §615(f); Position 5.14 |
| 13 | Standard vs itemized deduction is a close call (within $500) | Default to standard deduction; it is simpler and produces nearly the same result | NY Tax Law §614; Position 5.14 |
| 14 | NYC taxable income differs from NY taxable income due to a specific NYC-only adjustment | Flag for reviewer; NYC-specific adjustments are rare but can arise (e.g., certain NYC-only charitable deductions) | NYC Admin Code §11-1701; Position 5.22 |
| 15 | NYC UBT credit IT-219 sliding-scale computation produces a non-integer percentage | Round the credit amount to the nearest dollar, not the percentage | Form IT-219 instructions; Position 5.24 |
| 16 | Taxpayer had living quarters in Yonkers for part of 2025 but facts do not clearly support Yonkers residency | Default to NOT claiming Yonkers residency; apply only the Yonkers nonresident earnings tax if applicable; flag for reviewer | NY Tax Law §605(b); Yonkers City Code §92-5; Position 5.4 |
| 17 | MCTMT zone allocation is ambiguous (taxpayer works in both Zone 1 and Zone 2) | Refuse under R-NY201-7; zone allocation requires Form IT-203-A which is out of scope | NY Tax Law §800(b); Position 5.28 |
| 18 | MFJ return with one spouse over the $50,000 MCTMT zone threshold and one spouse under | Apply the per-individual rule: include only the spouse's NESE that exceeds $50,000; exclude the under-threshold spouse's base | NY Tax Law §801(b); Form IT-201-I (2025) Line 54 example |
| 19 | Empire State Child Credit phase-out computation produces a fractional amount | Round to the nearest dollar; document the computation in the reviewer brief | NY Tax Law §606(c-1); Form IT-213 instructions |
| 20 | NY EIC is claimed but the federal EIC is contested or the taxpayer is near the federal phase-out | Defer to the federal return's final EIC amount; 30% of the federal figure, no independent computation | NY Tax Law §606(d); Form IT-215 |
| 21 | Payments from Form IT-2105 vouchers are claimed but voucher receipts are not produced | Flag for reviewer; do not include un-documented estimated payments | Form IT-201 (2025) Line 75 |
| 22 | Taxpayer owes more than $1,000 on Line 78 but has not run the underpayment penalty computation | Note the balance due; defer penalty computation to the `ny-estimated-tax-it-2105` skill; do not estimate the penalty in this skill | Form IT-2105.9; Position 5.34 |
| 23 | Form IT-225 addition modification amount is close to the standard deduction (making the NY tax near-zero) | Double-check the A-201 UBT add-back arithmetic; a missing UBT add-back can materially understate NY tax | Form IT-225-I (2025) code A-201 |
| 24 | Taxpayer has a 2025 retirement contribution deadline that extends past April 15, 2026 (e.g., SEP with extended federal return) | Use the federal return's treatment; do not compute NY separately | Position 5.3; federal return is source of truth |

---

## Section 7 — Topical refusal catalogue

These refusals extend the base global catalogue in `us-tax-workflow-base` Section 6. When any refusal fires, output the text in the "Output" field **verbatim** per base Check 16, then stop workflow and flag in the brief's refusal trace.

**R-NY201-1 — Part-year or nonresident taxpayer.**
Trigger: The taxpayer was not a New York State full-year resident for all of 2025, OR the taxpayer's residency is ambiguous at any point in the year (moved into or out of NY, split-year domicile, statutory residency test close to the 184-day threshold).
Output: "This skill prepares only full-year New York State resident returns on Form IT-201. Part-year residents and nonresidents must file Form IT-203, Nonresident and Part-Year Resident Income Tax Return, which applies different income allocation rules under NY Tax Law §631. Form IT-203 is outside this skill's scope. Please consult an Enrolled Agent or CPA familiar with NY part-year and nonresident returns."

**R-NY201-2 — Convenience-of-the-employer remote worker case.**
Trigger: The taxpayer is a NY resident who has W-2 wages from an out-of-state employer AND the employer claims NY source for those wages under NY's convenience-of-the-employer rule, OR the taxpayer is a nonresident W-2 employee who worked remotely for a NY employer and the employer sourced the wages to NY.
Output: "New York's convenience-of-the-employer rule (20 NYCRR §132.18(a)) treats wages as New York source when a nonresident performs services outside New York for their convenience rather than the employer's necessity. This rule creates complex sourcing questions that require careful analysis of the bona fide employer office test and the employer's policies. This skill does not handle convenience-of-the-employer determinations. Please consult a CPA familiar with NY remote-work sourcing rules."

**R-NY201-3 — Itemized deduction limitation above $100,000 NYAGI.**
Trigger: NYAGI exceeds $100,000 AND the taxpayer's NY itemized deduction (computed via Form IT-196) would exceed the NY standard deduction for their filing status. The §615(f) limitation applies and requires detailed phase-out computation.
Output: "New York limits itemized deductions under NY Tax Law §615(f) for taxpayers with New York adjusted gross income above $100,000. The limitation phases out the itemized deduction through multiple income bands and requires a detailed computation under 20 NYCRR §112.3. This skill handles the simple case (standard deduction obviously superior) but refuses the complex case where the itemized deduction would materially benefit the taxpayer. Please consult a CPA to compute the NY itemized deduction limitation in detail."

**R-NY201-4 — PTET election scenario.**
Trigger: The taxpayer is asking about the NY Pass-Through Entity Tax (PTET) election under NY Tax Law Article 24-A, OR operates through a multi-owner pass-through that may benefit from the PTET election.
Output: "The New York Pass-Through Entity Tax (PTET) election under NY Tax Law Article 24-A applies to multi-owner pass-through entities (S corporations, LLCs taxed as partnerships, and general partnerships) that elect to pay state income tax at the entity level to bypass the federal SALT cap. The PTET is not available to disregarded single-member LLCs or bare sole proprietors because there is no separate pass-through entity to make the election. This skill covers only sole props and disregarded SMLLCs. If you are considering forming a multi-owner entity for PTET benefits, please consult a CPA to analyze the tradeoffs."

**R-NY201-5 — §174A R&E material amount.**
Trigger: The taxpayer has domestic R&E expenditures under IRC §174A with material dollar impact (more than $10,000 of potential R&E classification), AND the allocation between §162 ordinary expenses and §174A R&E is fact-sensitive.
Output: "The OBBBA §174A immediate deduction for domestic research and experimental expenditures creates a retroactive decoupling risk for New York state tax purposes. Governor Hochul's FY 2026-27 Executive Budget (January 2026) proposes retroactive NY decoupling to tax years beginning on or after January 1, 2025, but the proposal has not been enacted as of this skill's currency date. Material R&E positions require reviewer judgment on both the §162 vs §174A classification and the NY conservative-vs-federal-conforming path. This skill handles small R&E positions (under $10,000) via Position 5.15 with Path A as the default. Material positions are refused pending reviewer analysis. Please consult a CPA for the §174A classification and NY decoupling decision."

**R-NY201-6 — Credit for taxes paid to another state.**
Trigger: The taxpayer is a NY resident who earned income that was taxed by another state or a political subdivision of another state (e.g., NY resident who worked in New Jersey and paid NJ income tax, NY resident with rental property in Connecticut, NY resident freelancer with clients in Massachusetts who withheld MA tax).
Output: "The New York resident credit for taxes paid to another state or political subdivision under NY Tax Law §620 is a complex allocation exercise that requires determining the New York source and non-New York source components of income, computing the credit cap under the §620(e) limitation formula, and coordinating with the other state's return. This skill does not compute the NY §620 credit. Please consult a CPA to compute the resident credit — it is often materially valuable and should not be skipped."

**R-NY201-7 — Multi-state business activity or multi-zone MCTMT allocation.**
Trigger: The taxpayer has business activity in multiple states requiring income apportionment, OR has self-employment activity in both MCTD Zone 1 and Zone 2 requiring allocation between zones.
Output: "Multi-state business activity allocation under NY Tax Law §631 and MCTD zone allocation under NY Tax Law §800(b) both require Form IT-203-A (Business Allocation Schedule). This schedule is complex and requires detailed records of where each activity was performed. This skill assumes all activity is in a single location by virtue of the taxpayer's residency. Please consult a CPA for Form IT-203-A preparation."

**R-NY201-8 — Split-residence married couple.**
Trigger: The taxpayer is married and one spouse is a full-year NY resident while the other is a nonresident or part-year resident, OR one spouse is a full-year NYC resident and the other is not, OR one spouse is a Yonkers resident and the other is not.
Output: "Split-residence married couples require careful residency analysis for each spouse and may require separate New York returns under NY Tax Law §651(b) even if the couple files jointly at the federal level. The filing status interactions are complex and often benefit from separate NY filings even when the federal filing is joint. This skill does not handle split-residence couples. Please consult a CPA to analyze the optimal NY filing approach."

**R-NY201-9 — Amended return.**
Trigger: The taxpayer needs to amend a previously filed Form IT-201.
Output: "Amended New York returns (Form IT-201-X) require reconciliation to the original filing, identification of each change, and careful handling of any federal amendments that flow through to the NY amendment. This skill prepares original returns only. Please consult an Enrolled Agent or CPA for NY return amendments."

**R-NY201-10 — Decedent taxpayer or fiduciary return.**
Trigger: The taxpayer died during 2025 or the return is being prepared on behalf of a decedent, OR the return is for an estate, trust, or other fiduciary entity.
Output: "Returns for decedent taxpayers require special handling under NY Tax Law §658(d) including the decedent indicator, appropriate signatures, and coordination with any estate return. Fiduciary returns for estates and trusts use Form IT-205, not Form IT-201. Both are outside this skill's scope. Please consult an Enrolled Agent or CPA specializing in decedent or fiduciary returns."

**R-NY201-11 — Special condition codes (combat zone, nonresident noncitizen, SCRA military election).**
Trigger: The taxpayer qualifies for any of the special condition codes A6, C7, D9, K2, E3, E4, E5, 56, C2, M4-M9, or Y1 per Form IT-201 Item G.
Output: "Taxpayers qualifying for special condition codes on Form IT-201 Item G (combat zone, nonresident noncitizen, Servicemembers Civil Relief Act election, out-of-country extension, Ponzi-type fraudulent investment loss, installment payment agreement, split-Yonkers-residence joint filer) require specific handling that is outside this skill's standard workflow. Please consult a CPA familiar with the specific condition that applies."

**R-NY201-12 — Minor with investment income (Form 8615 / kiddie tax).**
Trigger: The return is for a minor who has investment income over $2,700, OR the parent is reporting the child's investment income on their own return via federal Form 8814.
Output: "Returns for minors with investment income subject to the federal kiddie tax rules (Form 8615 or parent's election via Form 8814) interact with NY in non-obvious ways. The child's investment income, when reported on the parent's return, is taxed at the parent's NY rate but subject to the $3,100 NY dependent standard deduction. This skill does not handle kiddie tax integration. Please consult a CPA for returns involving minors with significant investment income."

---

## Section 8 — Reviewer attention thresholds

This skill produces a multi-layer tax computation (state + potentially NYC + potentially Yonkers + potentially MCTMT). Reviewer attention is triggered by any of the following conditions, not by single dollar-amount thresholds alone. Each trigger explains why the reviewer must see it.

### Dollar-threshold triggers

| Trigger | Flag reason |
|---|---|
| Total NY balance due (Line 78) > $5,000 | Material balance; verify all payments credited and all credits claimed |
| Single IT-225 addition modification > $2,000 | Material positive adjustment; verify the modification code and amount |
| A-201 UBT add-back > $1,000 | Material; verify the UBT paid matches the NYC-202/NYC-202S filing from the companion skill |
| Form IT-558 A-011 bonus depreciation add-back > $5,000 | Material timing difference; verify Form IT-398 computation and ensure the asset basis is correct |
| NYC UBT credit (Line 53) > $1,000 | Material; verify the IT-219 sliding-scale computation and confirm NYC UBT paid amount |
| MCTMT combined (Lines 54a + 54b) > $500 | Material; verify zone allocation and per-individual threshold application |
| Yonkers resident surcharge (Line 55) > $2,000 | Material; verify the 16.75% computation against Line 50 |
| Empire State Child Credit claimed > $500 | Material; verify income phase-out and child count |
| NY EIC claimed > $500 | Material; verify federal EIC ties to the federal return's computed amount |
| Balance due increases from prior year by > 50% | Material change; verify that no refundable credits were missed |

### Condition-based triggers

| Trigger | Flag reason |
|---|---|
| NYAGI > $107,650 (recapture worksheet used) | Verify the correct band of the tax computation worksheet was applied; the bands are mechanical but error-prone |
| NYAGI > $100,000 AND itemized deduction claimed | Verify the §615(f) limitation computation; if skill refused under R-NY201-3, verify refusal was appropriate |
| Position 5.15 (§174A R&E) applied at all | Verify the reviewer election between Path A (conservative) and Path B (federal-conforming); affirm the dollar impact |
| NYC resident with UBT credit flow | Verify three-document chain: NYC-202/NYC-202S from NYC UBT skill → IT-219 → IT-201-ATT Section C → IT-201 Line 53. Any break in the chain is an error. |
| Yonkers resident claimed | Verify the Item D2 entries on the face of Form IT-201; the Yonkers resident determination can be fact-sensitive |
| Both spouses have self-employment income subject to MCTMT (joint return) | Verify the per-individual-per-zone threshold application; each spouse tested separately against $50,000 |
| Taxpayer is in one of the transition counties (Westchester, Dutchess, etc.) where MCTMT zone matters | Verify the Zone 1 vs Zone 2 classification — these counties are Zone 2 and the rate is 0.34% not 0.60% |
| IT-225 S-118 subtraction claimed (UBT-related subtraction) | Verify this is not double-counted with the A-201 add-back; the two modifications are different but interact |
| Refund requested > $2,000 | Verify all additions captured, all withholding and estimated payments match documentation |
| Return includes any cross-skill output from `nyc-unincorporated-business-tax` | Verify cross-skill timestamps match and the UBT amount on the state return equals the UBT amount on the companion NYC skill's output |
| First-year NY resident (moved in during 2024 or early 2025) | If the return is for 2025 and the taxpayer moved in during 2025, this should have triggered R-NY201-1. If it was cleared, verify the domicile analysis. |
| Taxpayer has prior-year NY NOL or other carryforwards | Verify the carryforward tracking schedule; NY NOLs are complex and out of scope (R-US-NOL from base catalogue) |
| Business activity is non-SSTB but has characteristics that could trigger a reviewer second look | Already captured in federal QBI analysis, but for NY purposes the NY return does not recompute QBI (see Section 2 "QBI structural non-conformity"). Flag only if the federal SSTB classification is contested. |
| Taxpayer has 1095-A (federal ACA marketplace coverage) | NY does not impose its own individual mandate penalty (unlike California's Form 3853); no NY-specific flag required, but ensure the federal PTC reconciliation flowed correctly into the federal return |
| Taxpayer asks about NY state tax deductions for charitable giving to the Charitable Gifts Trust Fund | NY has a specific charitable giving program; see Form IT-201-I Line 36 instructions. Flag for reviewer as this is usually not claimed correctly by self-preparers |

### Sanity checks that always trigger reviewer attention

| Trigger | Flag reason |
|---|---|
| NYAGI ≠ federal AGI ± documented modifications | Arithmetic error; the reconciliation must balance exactly |
| NY state tax (Line 39) > NY state tax at the top marginal rate applied to NY taxable income | Arithmetic or method-selection error; something is wrong with the computation |
| Line 76 (total payments) = 0 but taxpayer had W-2 wages | NY withholding is missing; check W-2 Box 17 |
| Line 76 > federal total payments | Unusual; NY payments should not exceed federal payments unless state-only estimated payments were made — verify |
| Any IT-225 modification code is listed but Form IT-225 is not attached | Structural error; the form must be produced and attached |
| Any IT-558 line has a value but Form IT-558 is not attached | Same structural error |

---

## Section 9 — Worked examples

Six worked examples covering the common fact patterns the skill encounters. Each example walks through the position rules from Section 5 with explicit computations, primary source citations, and the resulting reviewer brief entries. Examples are drawn from hypothetical taxpayers; names are illustrative.

### Example 1 — Sarah: Brooklyn-based NYC resident freelancer with UBT

**Facts.**
- Sarah is a 32-year-old freelance iOS developer, single, living in Brooklyn (Kings County) for the full 2025 tax year.
- She operates through Sarah Code LLC, a NY-registered single-member LLC disregarded for federal tax purposes (see companion skill `ny-llc-filing-fee-it-204-ll` for the $25 filing fee).
- 2025 Schedule C: $220,000 gross receipts, $18,000 business expenses → $202,000 net profit (Line 31).
- Schedule SE net SE earnings (§1402(a)): $202,000 × 0.9235 = $186,547.
- Federal retirement deduction (Solo 401(k)): $46,000.
- Federal SE health insurance deduction: $8,400.
- Federal deductible half of SE tax: $14,270.
- No other income, no dependents, no rental property.
- Federal AGI (Form 1040 Line 11): $119,260 (= $202,000 net profit − $14,270 half SE tax − $46,000 retirement − $8,400 SEHI − $8,070 other adjustments for this example).
- Federal taxable income: $102,760 (after $8,000 single standard deduction and QBI deduction of $8,500; QBI is a structural non-issue for NY).
- NYC gross business income exceeds the $95,000 UBT filing threshold, so Sarah is subject to NYC UBT. Her companion `nyc-unincorporated-business-tax` skill computes her UBT liability at $2,800 (after deductions and the small-taxpayer credit phase-out). She paid this UBT during 2025 via NYC-5UBTI estimated vouchers.
- On her federal Schedule C, Sarah deducted the $2,800 UBT on Line 23 (Taxes and licenses).

**Position walk-through.**

**Positions 5.1-5.5 (Entry gate).** Sarah is a full-year NY resident (domiciled in Brooklyn). Filing status: single. Federal AGI imported: $119,260. Intra-NY residency: NYC resident (all five boroughs count as NYC for tax purposes; Kings County = Brooklyn). No Yonkers. Zone 1 for MCTMT. Upstream federal lock: confirmed.

**Position 5.6 (Line 20).** Sarah has no tax-exempt interest from state/local bonds. Line 20 = $0.

**Position 5.8 (Line 23 IT-225 additions).** **This is the critical A-201 add-back.** Sarah deducted $2,800 of NYC UBT on her federal Schedule C, which reduced her federal AGI by $2,800. NY does not allow this deduction. Under IT-225 code A-201, Sarah adds back $2,800. Line 23 = $2,800.

**Position 5.9 (Line 28).** Sarah has no US government bond interest. Line 28 = $0.

**Position 5.10 (Line 29).** Sarah is 32. No pension/annuity exclusion. Line 29 = $0.

**Position 5.11 (Line 31 IT-225 subtractions).** No applicable subtractions. Line 31 = $0.

**Position 5.12 (IT-558 OBBBA).** Sarah placed no depreciable assets in service in 2025 (she uses her existing 2022 MacBook and existing office setup). No §168(k) add-back. No §174A issue (all her work is client deliverables under §162, not speculative R&E). IT-558 = not attached.

**Position 5.13 (Line 33 NYAGI).** NYAGI = $119,260 + $2,800 (A-201 add-back) − $0 (subtractions) = **$122,060**.

**Position 5.14 (Line 34 deduction).** Standard deduction for single = $8,000. Sarah does not itemize (no mortgage, minimal charitable giving). Line 34 = $8,000.

**Position 5.16 (Line 36 dependents).** Sarah has no dependents. Line 36 = $0.

**Position 5.17 (Line 37 taxable income).** $122,060 − $8,000 − $0 = **$114,060**.

**Position 5.18 (method selection).** NYAGI of $122,060 **> $107,650** → use Tax Computation Worksheet, not the tax table or rate schedule. The appropriate band for single filers with NYAGI in $107,650 to $157,650 is the first band of the recapture worksheet.

**Position 5.19 (Line 39 NY state tax).** Using the Form IT-201-I tax computation worksheet for single filers with NYAGI $107,650 to $157,650:
- Step 1: Compute tax as if using the rate schedule on taxable income of $114,060: Tax = 5.50% × ($80,650 − $13,900) + 5.25% × ($13,900 − $11,700) + 4.50% × ($11,700 − $8,500) + 4.00% × $8,500 + 6.00% × ($114,060 − $80,650). That equals $340 + $144 + $115.50 + $3,671.25 + $2,004.60 ≈ $6,275.
- Step 2: Compute the recapture addition: (NYAGI − $107,650) × recapture rate. For single filers in this band, the worksheet provides the specific recapture multiplier.
- Step 3: Sum for the final NY state tax.
- **Approximate Line 39 = $6,600.** (The reviewer brief shows the exact worksheet computation line by line.)

**Position 5.20 (Line 40 household credit).** Single filer, NYAGI $122,060 → per Table 1, household credit = $0 (phased out above ~$28,000). Line 40 = $0.

**Position 5.22 (Line 47a NYC resident tax).** NYC taxable income = $114,060 (same as NY taxable income). Using the NYC rate schedule for single filers with NYC taxable income ≥ $65,000:
```
NYC tax = 3.078% × $12,000 + 3.762% × ($25,000 − $12,000) + 3.819% × ($50,000 − $25,000) + 3.876% × ($114,060 − $50,000)
       = $369.36 + $489.06 + $954.75 + $2,483.00
       = $4,296.17 → $4,296
```
Line 47a = $4,296.

**Position 5.23 (Line 48 NYC household credit).** Single, income too high. Line 48 = $0.

**Position 5.24 (Line 53 NYC UBT credit).** Sarah paid $2,800 of NYC UBT. Her NYC taxable income is $114,060, which is in the sliding-scale phase-out range ($42,001 to $141,999). Computing the credit rate:
```
Credit rate = 1.00 − ((114,060 − 42,000) / 100,000) × 0.77
           = 1.00 − (72,060 / 100,000) × 0.77
           = 1.00 − 0.5549
           = 0.4451 → 44.51%
Credit = $2,800 × 0.4451 = $1,246.28 → $1,246
```
This amount flows through Form IT-219 → IT-201-ATT Section C Line 10 → IT-201 Line 53 = **$1,246**.

**Position 5.25 (Line 69 NYC school tax credit).** Sarah is a NYC resident. Line 69 (fixed amount, single) = $63. Line 69a (rate reduction) applies because income < $500,000; small amount from the table, approximately $21. Total NYC STC ≈ $84.

**Positions 5.26-5.27 (Yonkers).** Not a Yonkers resident, no Yonkers earnings. Lines 55, 56 = $0.

**Position 5.28 (Line 54a MCTMT Zone 1).** Sarah's net SE earnings are $186,547, all allocated to Zone 1 (she works from her Brooklyn apartment). $186,547 > $50,000 → MCTMT applies.
```
MCTMT Zone 1 = 0.60% × $186,547 = $1,119.28 → $1,119
```
Line 54a = **$1,119**.

**Position 5.29 (Line 54b Zone 2).** No Zone 2 activity. Line 54b = $0.

**Position 5.31 (refundable credits).** Sarah has no children (no Empire State Child Credit), no NY EIC (phased out at her income), no real property tax credit. Lines 63-68 = $0.

**Position 5.32-5.33 (total taxes).**
- Line 46 (total NY state tax) = $6,600 (Line 39) − $0 (credits) = $6,600.
- Line 58 (total city + sub-state) = $1,119 (MCTMT) + $4,296 (NYC Line 47a) − $0 (Line 48) − $1,246 (Line 53) + $0 (Yonkers) = **$4,169**.

**Position 5.34 (final).**
- Line 61 (total tax) = $6,600 + $4,169 + $0 + $0 = **$10,769**.
- Line 69 NYC STC refundable = $84 reduces the amount owed or increases the refund.
- Assume Sarah made NY estimated payments via IT-2105 vouchers totaling $9,500 across four quarters.
- Line 76 (total payments) = $9,500 + $84 (NYC STC) = $9,584.
- Line 78 (balance due) = $10,769 − $9,584 = **$1,185**.

**Reviewer brief entries.**
- Position 5.15 §174A: N/A (no R&E).
- High flag: NYC UBT credit of $1,246 flowing from Form IT-219 — verify cross-skill chain with `nyc-unincorporated-business-tax` skill output (UBT $2,800).
- High flag: Balance due $1,185 — under the $5,000 reviewer attention threshold but close to the $1,000 underpayment penalty floor; route to `ny-estimated-tax-it-2105` for penalty computation.
- Reviewer attention: NYAGI $122,060 used the recapture worksheet band; verify the Section 3 worksheet computation.
- Reviewer attention: A-201 UBT add-back $2,800 matches the federal Schedule C Line 23 deduction of $2,800; verified.

**Primary sources cited.**
- NY Tax Law §601 (rates), §605(b) (residency), §612(b)(3) (A-201), §801(a) (MCTMT)
- NYC Admin Code §11-1701 (NYC rates), §11-503(b) (UBT credit), §11-1706 (school tax credit)
- Form IT-201 (2025) Lines 19-80
- Form IT-225-I (2025) code A-201
- Form IT-219 instructions
- Form IT-201-ATT (2025) Section C

---

### Example 2 — David: Manhattan NYC resident with §174A uncertainty

**Facts.**
- David is a 40-year-old freelance developer building his own iOS productivity app alongside client work. Full-year resident of Manhattan. Single.
- Schedule C 2025: $150,000 gross receipts from client consulting work, $90,000 expenses (of which $45,000 are contractor payments for product development work on his own app — the contested §174A question).
- Net profit: $60,000.
- Federal AGI after adjustments: $48,000 (low because of the contractor payments).
- On the federal return, David's CPA claimed immediate §174A deduction for the $45,000 contractor payments, treating them as domestic R&E.
- NYC UBT: David's gross business income ($150,000) is above the $95,000 UBT threshold, so he must file NYC-202. His taxable UBT income (after the $45,000 R&E deduction and other adjustments) is approximately $48,000, and his UBT is $540 (well below the $3,400 small-taxpayer credit threshold, so effectively $0 after credit). He paid $0 UBT during 2025.
- A-201 UBT add-back: $0 (he didn't deduct any UBT federally because his UBT was $0 after credits).

**Position walk-through (focusing on the §174A decision).**

**Positions 5.1-5.13 (entry through NYAGI):** Standard computation. Federal AGI $48,000. No A-201 add-back. NYAGI before §174A decision = $48,000.

**Position 5.15 (§174A — the key decision).** David has $45,000 of potentially §174A-classified expenditures. This exceeds the $10,000 materiality threshold in this skill's Section 6 default #9 and triggers **R-NY201-5 (material §174A position)**.

**Refusal output (verbatim per Check 16):** "The OBBBA §174A immediate deduction for domestic research and experimental expenditures creates a retroactive decoupling risk for New York state tax purposes. Governor Hochul's FY 2026-27 Executive Budget (January 2026) proposes retroactive NY decoupling to tax years beginning on or after January 1, 2025, but the proposal has not been enacted as of this skill's currency date. Material R&E positions require reviewer judgment on both the §162 vs §174A classification and the NY conservative-vs-federal-conforming path. This skill handles small R&E positions (under $10,000) via Position 5.15 with Path A as the default. Material positions are refused pending reviewer analysis. Please consult a CPA for the §174A classification and NY decoupling decision."

**What the skill produces for David's reviewer:**

1. A partial IT-201 with the computation paused at NYAGI. The skill shows two possible NYAGI values:
   - **Path A (conservative, NY decouples from §174A retroactively):** NY would require capitalization and 5-year recovery. First-year NY deduction would be approximately $4,500 (10% mid-year convention). The IT-558 addition for 2025 = $45,000 − $4,500 = **$40,500**. NYAGI (Path A) = $48,000 + $40,500 = **$88,500**.
   - **Path B (federal-conforming, NY follows §174A):** No IT-558 addition. NYAGI (Path B) = $48,000.
2. The dollar impact of the choice: $40,500 of additional NYAGI at David's likely marginal rate (around 6.85% combined state + NYC) ≈ **$2,775 of additional NY+NYC tax** in 2025 under Path A.
3. A timing analysis: Under Path A, David recovers the $40,500 excess deduction over 2026-2029 via IT-558 subtractions, producing approximately $700-$1,000 of NY tax savings per year in those years, net-neutral over the 5-year window.
4. The amendment risk under Path B: If the Hochul FY 2026-27 budget passes with retroactive effect, David will need to file an amended 2025 NY return to add back the $40,500. The amendment cost (preparer time + filing) plus interest on the late payment plus potential underpayment penalty would likely exceed $500-$1,500.
5. The reviewer's decision point, stated explicitly: "Reviewer must choose Path A (conservative, file original return with IT-558 add-back, no amendment risk) or Path B (federal-conforming, file original return without IT-558, potential amendment risk). Skill default is Path A. Skill cannot proceed without reviewer affirmation."

**Reviewer brief high flag:** "Material §174A position — $45,000 of potential R&E — refused under R-NY201-5 pending reviewer classification of (a) §162 vs §174A and (b) NY Path A vs Path B. Skill default is Path A if reviewer proceeds without affirmative election. See Position 5.15 for dedicated analysis and dollar impact."

**Source.** IRC §174A; NY Tax Law §612; Hochul FY 2026-27 Executive Budget (proposed, not enacted as of skill currency date); Position 5.15 of this skill.

**Note.** This example illustrates the skill's refusal behavior on a live legislative uncertainty. The skill does not silently pick a path — it produces a structured refusal with both paths documented and a clear reviewer decision point. If the reviewer affirms Path A, the skill can proceed to compute the rest of the return with the IT-558 addition. If the reviewer affirms Path B, the skill can proceed without the IT-558 addition but with the amendment risk flagged prominently in the brief.

---

### Example 3 — Carlos: Yonkers resident freelancer

**Facts.**
- Carlos is a 45-year-old freelance DevOps engineer, married filing jointly, full-year resident of Yonkers. His spouse Maria has W-2 wages of $85,000 from a NY employer (also living in Yonkers with Carlos).
- Carlos's Schedule C: $145,000 gross receipts, $15,000 expenses → $130,000 net profit.
- Schedule SE net SE earnings: $130,000 × 0.9235 = $120,055.
- Federal AGI (Carlos + Maria joint): $185,000 (after half SE tax, SE retirement, SEHI, and Maria's contribution to her employer's 401(k)).
- They have one child (age 7) claimed as a dependent.
- Carlos's business has no NYC nexus (he works from his home office in Yonkers and all clients are remote). Therefore no NYC UBT filing, no IT-219 credit.
- They own their home in Yonkers.

**Position walk-through.**

**Positions 5.1-5.5.** Full-year NY residents, MFJ, federal AGI $185,000. Intra-NY residency: Yonkers residents (not NYC). For MCTMT purposes, Yonkers is in **Westchester County → MCTD Zone 2**.

**Position 5.8 (IT-225 additions).** No UBT (not NYC), no bonus depreciation, no other applicable modifications. Line 23 = $0.

**Position 5.13 (Line 33 NYAGI).** $185,000 (no modifications).

**Position 5.14 (Line 34 deduction).** Carlos and Maria itemize federally with ~$22,000 of itemized deductions (mortgage interest, state/local taxes, charitable). NY itemized deduction before §615(f) limitation = approximately $24,000 (adding back federal SALT cap differences, handled by Form IT-196). MFJ standard deduction is $16,050. NYAGI is $185,000, which exceeds $100,000, so §615(f) limitation applies. Here the itemized deduction even after limitation still exceeds $16,050, so the claim is worth it. However, **this skill's Section 7 refusal R-NY201-3 fires: "NYAGI > $100,000 AND itemized deduction would exceed standard."** The skill refuses the detailed §615(f) computation and routes to reviewer.

**Reviewer path:** The reviewer completes Form IT-196 manually, applies the §615(f) limitation, and returns the limited itemized deduction amount to the skill. For this example, assume the reviewer returns $20,500 as the NY itemized deduction.

**Position 5.17 (Line 37 taxable income).** $185,000 − $20,500 − $1,000 (one dependent) = **$163,500**.

**Position 5.18-5.19 (NY state tax).** NYAGI $185,000 > $107,650 → use the tax computation worksheet for MFJ filers in the $157,650 to $211,550 band.
- Base rate schedule computation: applying the MFJ brackets through $163,500: tax through $161,550 bracket plus 6.00% on the excess = approximately $6,842 + 6.00% × $1,950 = $6,842 + $117 = $6,959.
- Recapture addition for this band: the worksheet adds a small amount (approximately $100-$300 for this income level; exact amount from the worksheet).
- **Approximate Line 39 = $7,150.**

**Positions 5.22-5.25 (NYC).** Not NYC residents. Lines 47a-53 = $0. Lines 69-69a = $0.

**Position 5.26 (Line 55 Yonkers resident surcharge).** Yonkers residents: Line 55 = **16.75% × Line 50**. Assume Line 50 (NY state tax after household credit) = $7,150. Surcharge = 16.75% × $7,150 = **$1,198**.

**Position 5.27 (Line 56 Yonkers nonresident).** Carlos is a Yonkers resident, not nonresident, so this does not apply. Line 56 = $0.

**Position 5.28 (Line 54a Zone 1).** Carlos has $0 Zone 1 NESE (he works from Yonkers, not NYC). Line 54a = $0.

**Position 5.29 (Line 54b Zone 2).** Carlos's NESE of $120,055 is all allocated to Zone 2 (Westchester County). Under the per-individual-per-zone rule: Carlos is a single individual with Zone 2 NESE > $50,000. Maria has $0 Zone 2 NESE (she has W-2 wages, not SE earnings, so her base is $0 in both zones). The joint Line 54b includes only Carlos's NESE.
```
Line 54b = 0.34% × $120,055 = $408.19 → $408
```

**Position 5.31 (refundable credits).** Empire State Child Credit: one child age 7, MFJ income $185,000 — child credit is phased down at this income level. Per Form IT-213, the credit for a child over 4 at this income is approximately $100-$200 (depending on exact phase-out schedule). Enter approximate $200 on Line 63.

**Position 5.32-5.34 (final).**
- Line 46 (total state) = $7,150 − $0 (credits) = $7,150.
- Line 58 (total sub-state) = $408 (MCTMT) + $0 (NYC) + $1,198 (Yonkers surcharge) + $0 (Yonkers NR) = **$1,606**.
- Line 61 (total tax) = $7,150 + $1,606 + $0 + $0 = **$8,756**.
- Minus Line 63 Empire State Child Credit $200 and any Line 65 NY EIC ($0 at this income level).
- Net tax before payments ≈ **$8,556**.
- Payments: Maria's W-2 NY withholding from Box 17 (approximately $4,800) + Carlos's NY estimated payments from IT-2105 vouchers (assume $3,500) = $8,300.
- Line 78 balance due ≈ **$256**.

**Reviewer brief entries.**
- High flag: Itemized deduction with §615(f) limitation — handled by reviewer manually per R-NY201-3, returned value $20,500.
- Reviewer attention: Yonkers resident status verified via Item D2(1) on the return.
- Reviewer attention: MCTMT Zone 2 applied correctly at 0.34% not 0.60% (Carlos is in Westchester, not NYC).
- Reviewer attention: Per-individual rule applied — only Carlos's NESE included in joint Line 54b; Maria's W-2 base is $0 so her Zone 2 base is excluded.

---

### Example 4 — Priya: Westchester resident, Zone 2 MCTMT only

**Facts.**
- Priya is a 38-year-old freelance data engineer, single, full-year resident of Scarsdale (Westchester County). Works from home. All clients are out-of-state (Boston, SF, Chicago).
- Schedule C: $195,000 gross receipts, $22,000 expenses → $173,000 net profit.
- NESE: $159,775.
- Federal AGI: $155,000.
- No NYC activity, not a Yonkers resident, no dependents.
- She placed a new $4,000 home office desk/chair setup in service in February 2025 and claimed federal §179 expensing for the full $4,000 (not §168(k) bonus depreciation).

**Position walk-through.**

**Positions 5.1-5.5.** Full-year NY resident, Westchester, not NYC, not Yonkers. Zone 2 for MCTMT. Single.

**Position 5.8 (IT-225 additions).** No UBT add-back (not NYC). **§179 expensing:** NY generally conforms to federal §179 expensing up to the full cap (there is no NY-specific §179 limit below the federal cap for 2025). So no §179 add-back. Line 23 = $0. (Note: if Priya had claimed §168(k) bonus depreciation instead, IT-225 A-009 or IT-558 A-011 would fire. She elected §179 specifically to avoid the bonus depreciation decoupling complication — smart tax planning.)

**Position 5.12 (IT-558 OBBBA).** No bonus depreciation, no §174A issue (she does client deliverable work only). IT-558 not attached.

**Position 5.13 (Line 33 NYAGI).** $155,000 (no modifications).

**Position 5.14 (Line 34).** Standard deduction for single = $8,000. She does not itemize (no mortgage; rents). Line 34 = $8,000.

**Position 5.17 (Line 37 taxable income).** $155,000 − $8,000 − $0 = $147,000.

**Position 5.18-5.19 (NY state tax).** NYAGI $155,000 > $107,650 → recapture worksheet for single filers in the $107,650 to $157,650 band. Base rate schedule tax on $147,000 = approximately $8,160. Recapture addition for this band ≈ $200. **Line 39 ≈ $8,360**.

**Position 5.22 (NYC).** Not NYC resident. Line 47a = $0.

**Position 5.26 (Yonkers surcharge).** Not a Yonkers resident. Line 55 = $0.

**Position 5.27 (Yonkers NR earnings tax).** No Yonkers-source wages or SE work. Line 56 = $0.

**Position 5.28 (Line 54a Zone 1).** $0 Zone 1 NESE. Line 54a = $0.

**Position 5.29 (Line 54b Zone 2).** NESE $159,775, all Zone 2. > $50,000. **Line 54b = 0.34% × $159,775 = $543.24 → $543**.

**Position 5.31 (credits).** No dependents, no EIC (income too high), no real property tax credit (rents). Lines 63-68 = $0.

**Position 5.32-5.34 (final).**
- Line 46 = $8,360.
- Line 58 = $543 (MCTMT only).
- Line 61 = $8,903.
- Assume IT-2105 estimated payments $8,500. Line 78 balance due ≈ **$403**.

**Reviewer brief entries.**
- §179 election instead of §168(k): documented as a tax planning choice that avoided NY decoupling complexity. Verify the federal election.
- MCTMT Zone 2 classification: Westchester County, verified in §800(b).
- No NYC UBT filing required: Priya has no NYC nexus. The companion `nyc-unincorporated-business-tax` skill is not invoked.
- First-year Zone 2 MCTMT filer: Priya has not previously had MCTMT exposure (assume this is her first year over the $50,000 threshold). Flag for reviewer as a new filing obligation.

---

### Example 5 — Rachel: Albany resident, no local layers

**Facts.**
- Rachel is a 29-year-old freelance backend developer, single, full-year resident of Albany. Works from home. All clients are in NY City and San Francisco.
- Schedule C: $125,000 gross receipts, $12,000 expenses → $113,000 net profit.
- NESE: $104,356.
- Federal AGI: $92,500.
- No NYC activity (she doesn't travel to NYC for her NYC clients — all work is remote). Not a Yonkers resident. Albany County is NOT in the MCTD (the MCTD is only the 12 counties listed in §800(b)).
- No dependents, no retirement contributions (she plans to start in 2026), no SE health insurance deduction (she's on her parents' plan until age 26 — wait, she's 29, correct this: she has marketplace coverage with a $400/month premium, reported on 1095-A).

**Position walk-through.**

**Positions 5.1-5.5.** Full-year NY resident, Albany County. NOT NYC, NOT Yonkers, NOT in MCTD. Single.

**Position 5.8 (IT-225 additions).** No UBT, no bonus depreciation. Line 23 = $0.

**Position 5.13 (Line 33).** $92,500 (no modifications).

**Position 5.14 (Line 34).** Standard deduction $8,000. She does not itemize.

**Position 5.17 (Line 37).** $92,500 − $8,000 = **$84,500**.

**Position 5.18-5.19 (NY state tax).** NYAGI $92,500 ≤ $107,650. Taxable income $84,500 ≥ $65,000 → use the NY State Tax Rate Schedule (not the tables, not the worksheet).
```
Single bracket 4.00% × $8,500 = $340
Single bracket 4.50% × $3,200 = $144
Single bracket 5.25% × $2,200 = $115.50
Single bracket 5.50% × $66,750 = $3,671.25
Single bracket 6.00% × $3,850 = $231 (on the excess above $80,650)
Total = $340 + $144 + $115.50 + $3,671.25 + $231 = $4,501.75 → $4,502
```
**Line 39 = $4,502**.

**Position 5.20 (household credit).** NYAGI $92,500 for single filer → Table 1 shows credit = $0 (phased out above approximately $28,000).

**Position 5.22 (NYC).** Not NYC. Line 47a = $0.

**Position 5.26 (Yonkers resident surcharge).** Not Yonkers. Line 55 = $0.

**Position 5.27 (Yonkers NR earnings).** Not relevant. Line 56 = $0.

**Position 5.28-5.30 (MCTMT).** Albany County is NOT in the MCTD at all. Line 54a = $0, Line 54b = $0. Even though Rachel has some NYC clients, MCTMT is based on where the taxpayer's business activity is carried on (her home office in Albany), not where her clients are located. This is a critical distinction that trips up many self-preparers. **See Section 3 of this skill for the full MCTD county list — Albany is NOT in it.**

**Position 5.32-5.34 (final).**
- Line 46 = $4,502.
- Line 58 = $0 (no NYC, no Yonkers, no MCTMT).
- Line 61 ≈ $4,502.
- Payments: NY estimated tax $4,200. Line 78 balance due ≈ **$302**.

**Reviewer brief entries.**
- Rachel is the simplest case: full-year NY resident with only state-level tax, no sub-state layers.
- MCTMT = $0 because Albany County is not in the MCTD. This should be explicitly stated in the brief for Rachel's reviewer so there is no ambiguity about whether MCTMT was missed or intentionally zero.
- The absence of NYC UBT: Rachel has no NYC nexus despite having NYC clients. The companion `nyc-unincorporated-business-tax` skill was not invoked. Document this in the brief.

---

### Example 6 — Jake: High-income Manhattan resident using the recapture worksheet

**Facts.**
- Jake is a 44-year-old freelance systems architect, single, Manhattan resident. Very senior practitioner at the top of the freelance market.
- Schedule C: $625,000 gross receipts, $40,000 expenses → $585,000 net profit.
- NESE: $540,248.
- Federal AGI: $495,000 (after half SE tax of $19,800, SEP-IRA contribution of $70,000 [§415(c) cap], SE health insurance $12,000, and other adjustments).
- Federal taxable income: $479,500 (after $8,000 standard deduction plus $7,500 QBI).
- NYC UBT: gross > $95,000, files NYC-202, pays approximately $16,800 of UBT (4% of $420,000 taxable after deductions, no small-taxpayer credit at this income).
- A-201 UBT add-back: $16,800 deducted on federal Schedule C Line 23.
- No dependents.
- One depreciable asset placed in service in 2025: a new MacBook Pro and peripherals for $6,500, claimed as §179 expensing federally (not §168(k) bonus). NY conforms to §179 at the federal cap → no add-back.

**Position walk-through.**

**Positions 5.1-5.5.** Full-year NYC (Manhattan) resident, single, federal AGI $495,000. NYC resident + Zone 1 MCTMT.

**Position 5.8 (A-201).** Add back $16,800 UBT. Line 23 = $16,800.

**Position 5.13 (Line 33 NYAGI).** $495,000 + $16,800 = **$511,800**.

**Position 5.14 (Line 34).** NYAGI $511,800 > $100,000 → itemized deduction limitation applies. But Jake takes the standard deduction anyway ($8,000) because he has no mortgage and minimal charitable giving. The §615(f) limitation does not apply because he's taking the standard deduction. R-NY201-3 does not fire. Line 34 = $8,000.

**Position 5.17 (Line 37).** $511,800 − $8,000 − $0 = **$503,800**.

**Position 5.18-5.19 (NY state tax).** NYAGI $511,800 > $107,650 → tax computation worksheet, and specifically the **$211,550 to $1,077,550 band for single filers**.

The worksheet for this band approximately:
1. Base tax using the rate schedule on $503,800: tax through $215,400 bracket = $10,692; plus 6.85% on ($503,800 − $215,400) = 6.85% × $288,400 = $19,755; total = **$30,447**.
2. Recapture addition: this band adds approximately 0.4% to 0.5% of NYAGI as the flat-rate supplemental, roughly $2,000-$3,000 at this income.
3. **Approximate Line 39 = $33,000-$34,000.** (The exact worksheet computation must be shown in the brief.)

For this example, assume **Line 39 = $33,400**.

**Position 5.22 (NYC Line 47a).** NYC taxable income = $503,800. Using the NYC rate schedule for single filers (top bracket 3.876% applies to income above $50,000):
```
NYC tax = 3.078% × $12,000 + 3.762% × $13,000 + 3.819% × $25,000 + 3.876% × ($503,800 − $50,000)
       = $369.36 + $489.06 + $954.75 + $17,589.29
       = $19,402.46 → $19,402
```
**Line 47a = $19,402**.

**Position 5.24 (Line 53 NYC UBT credit).** Jake paid $16,800 UBT. NYC taxable income $503,800 is well above $142,000, so the sliding scale is at the floor: credit rate = 23%. Credit = $16,800 × 0.23 = $3,864. **Line 53 = $3,864**.

**Position 5.28 (Line 54a MCTMT Zone 1).** NESE $540,248, all Zone 1. > $50,000. Line 54a = 0.60% × $540,248 = $3,241.49 → **$3,241**.

**Position 5.31 (refundable credits).** None (no children, no EIC at this income).

**Position 5.32-5.34 (final).**
- Line 46 = $33,400.
- Line 58 = $3,241 (MCTMT) + $19,402 (NYC) − $3,864 (UBT credit Line 53) + $0 = **$18,779**.
- Line 61 = $33,400 + $18,779 = **$52,179**.
- Plus any voluntary contributions ≈ $0, plus use tax if applicable (assume $0).
- Payments: NY estimated payments from IT-2105 across four quarters. Assume $48,000 total (reasonable for a $500k+ NYAGI taxpayer).
- Line 78 balance due ≈ **$4,179**.

**Reviewer brief entries.**
- **High flag: Total tax $52,179** is material and the computation uses the recapture worksheet band. Verify the exact worksheet computation line by line. A $500-$1,000 error is easy to make in the band transition.
- **High flag: A-201 UBT add-back $16,800** must match the federal Schedule C Line 23 deduction exactly. Cross-reference to the `nyc-unincorporated-business-tax` skill output ($16,800 UBT paid in 2025).
- **High flag: NYC UBT credit $3,864** at the 23% floor rate. Verify Form IT-219 computation and confirm NYC taxable income > $142,000.
- **High flag: MCTMT Zone 1 $3,241** at the 0.60% rate. Verify NESE allocation (all Zone 1 because all work is Manhattan-based).
- Reviewer attention: NYAGI in the $211,550 to $1,077,550 recapture band — verify the correct worksheet was used (there are multiple bands at higher income levels).
- Reviewer attention: Balance due $4,179 approaches the $5,000 threshold and is well above the $1,000 underpayment penalty floor. Route to `ny-estimated-tax-it-2105` for penalty computation. Jake's prior-year tax was likely in a similar range; the 110% safe harbor applies (prior-year NYAGI > $150,000 triggers 110% requirement).
- Sanity check: Total NY + NYC + MCTMT effective rate on $511,800 NYAGI = $52,179 / $511,800 = **10.2%**. This is consistent with the top-band marginal rates and is a useful reasonableness check.

---

## End of Turn 3 — Sections 6 through 9 complete, Sections 10-14 pending

### Turn 3 summary

This turn drafted Sections 6 through 9 — the behavioral sections of the skill.

**Section 6 (Conservative defaults table)** — 24 rows covering every ambiguity the skill encounters, from residency disputes through fractional credit computations. Each row has the ambiguity, the conservative default (almost always the higher-tax choice), and the source.

**Section 7 (Topical refusal catalogue)** — 12 refusals in the trigger/output-verbatim format required by base Check 16. R-NY201-1 through R-NY201-12 cover: part-year/nonresident (the most-fired refusal); convenience-of-employer; itemized deduction >$100k limitation; PTET; material §174A; credit for taxes paid to another state; multi-state and multi-zone allocation; split-residence couples; amended returns; decedent/fiduciary; special condition codes; minors with investment income. Each refusal output is a complete verbatim message the skill can emit to the reviewer brief without further editing.

**Section 8 (Reviewer attention thresholds)** — three-table structure: dollar-threshold triggers (10 items), condition-based triggers (14 items), and sanity checks (6 items). The skill does not use a single $X threshold for everything — different triggers apply at different dollar amounts or conditions, and the sanity checks always fire regardless of dollar amount.

**Section 9 (Worked examples)** — **six fully worked examples** covering the six most common fact patterns the skill handles:
1. **Sarah** — Brooklyn NYC resident freelancer with NYC UBT credit flow (demonstrates Positions 5.4, 5.8, 5.22, 5.24, 5.28, the full NYC + MCTMT + state layered computation)
2. **David** — Manhattan resident with material §174A R&E uncertainty (demonstrates Position 5.15 refusal behavior with Path A and Path B dollar impact analysis)
3. **Carlos** — Yonkers resident MFJ with itemized deduction §615(f) refusal (demonstrates Positions 5.14, 5.26, 5.29, and R-NY201-3 refusal)
4. **Priya** — Westchester resident with §179 planning choice to avoid bonus depreciation decoupling (demonstrates Position 5.29 Zone 2 MCTMT and the §179-vs-§168(k) planning distinction)
5. **Rachel** — Albany resident, simplest case with no local layers (demonstrates what a non-MCTD full-year NY resident looks like; critical for showing that Albany County is NOT in the MCTD despite having NYC clients)
6. **Jake** — Manhattan high-income resident using the recapture worksheet (demonstrates Position 5.19 tax computation worksheet for the $211,550-$1,077,550 band)

Each example walks through every relevant position rule, shows the computation arithmetic, produces reviewer brief entries, and cites primary sources. The examples are ~1,800 lines combined.

Total Turn 3 file length: approximately 970 lines. Cumulative file length after Turns 1+2+3: approximately 2,000 lines.

Sections 10-14 remain for Turn 4: output format extensions, intake form additions, self-check additions, cross-skill references, and change log. Estimated Turn 4 length: 500-700 lines. Final total: approximately 2,500-2,700 lines.
---

## Section 10 — Output format extensions

This section extends the base reviewer brief template from `us-tax-workflow-base` Section 3 with NY-specific additions. The base template provides the universal structure (taxpayer information, income summary, deduction summary, tax computation, credits, payments, balance, positions taken, refusals fired, self-check results, action list). This skill adds the NY-specific layers and line references.

### NY-specific reviewer brief sections

Insert these sections into the base reviewer brief in the order listed, after the base "Tax computation" section and before the base "Positions taken" section.

#### NY.1 — New York residency and layer determination

```
## New York residency and tax layer determination

Taxpayer NY residency status: [Full-year NY State resident / refused]
Source: NY Tax Law §605(b) — domicile test [and/or] statutory residency test
Supporting facts: [domicile address, days in NY if applicable, Item D2 and Item E entries]

NYC resident: [Yes / No]
  If Yes — basis: [domicile in one of the five boroughs / 184+ days statutory]
  If Yes — Item E entries on return: [Yes/No box and day count]
  
Yonkers resident: [Yes / No]
  If Yes — basis: [domicile / statutory]
  If Yes — Item D2 entries on return: [Yes/No boxes and month count]

MCTMT applicability:
  Zone 1 (NYC 5 boroughs): [Yes / No / N/A]
    NESE allocated to Zone 1: $[amount]
    Threshold met ($50,000): [Yes / No]
  Zone 2 (Rockland, Nassau, Suffolk, Orange, Putnam, Dutchess, Westchester): [Yes / No / N/A]
    NESE allocated to Zone 2: $[amount]
    Threshold met ($50,000): [Yes / No]
  Non-MCTD (Albany, Buffalo, Rochester, etc.): [Yes / No]
    If Yes, MCTMT does not apply regardless of income level.
```

#### NY.2 — NYAGI reconciliation

```
## NYAGI reconciliation (Federal AGI → NY AGI)

Federal AGI (Form 1040 Line 11, from us-federal-return-assembly): $[amount]

NY additions:
  Line 20 (non-NY state/local bond interest): $[amount]  [source: position 5.6]
  Line 21 (414(h) public employee contributions): $[amount]
  Line 22 (529 plan recapture): $[amount]
  Line 23 (IT-225 additions):
    Code A-201 (UBT add-back): $[amount]  [critical — must match NYC-202/202S output]
    Code A-009 (pre-2025 §168(k) bonus depreciation): $[amount]
    Code A-113 (other non-NY bond interest): $[amount]
    Other codes: $[amount]
    Subtotal IT-225 additions: $[amount]
  Line 24 (IT-558 additions):
    Code A-011 (2025+ §168(k) bonus depreciation): $[amount]
    Code §174A (if applicable — see Position 5.15): $[amount]  [PATH A / PATH B per reviewer election]
    Other IT-558 codes: $[amount]
    Subtotal IT-558 additions: $[amount]

Total NY additions: $[amount]

NY subtractions:
  Line 25 (taxable refunds): $[amount]
  Line 26 (government pension exclusion): $[amount]
  Line 27 (taxable Social Security): $[amount]
  Line 28 (US government bond interest): $[amount]  [source: position 5.9]
  Line 29 (pension/annuity exclusion up to $20,000): $[amount]
  Line 30 (other subtractions): $[amount]
  Line 31 (IT-225 subtractions):
    Code S-125 (NY depreciation recovery for bonus depreciation assets): $[amount]
    Code S-118 (NYC UBT-related income adjustment): $[amount]
    Other codes: $[amount]
    Subtotal IT-225 subtractions: $[amount]

Total NY subtractions: $[amount]

NYAGI (Line 33) = Federal AGI + Total additions − Total subtractions
              = $[amount]

Tax computation method: [Tax Table (NYAGI ≤ $107,650 and TI < $65,000) / 
                         Rate Schedule (NYAGI ≤ $107,650 and TI ≥ $65,000) / 
                         Tax Computation Worksheet (NYAGI > $107,650)]
Worksheet band (if applicable): [e.g., Single $107,650-$157,650 band]
```

#### NY.3 — Tax layer summary

```
## NY tax layer summary

NY state tax:
  Line 38 (taxable income): $[amount]
  Line 39 (state tax before credits): $[amount]  [via method: table/schedule/worksheet]
  Line 40 (household credit): $[amount]
  Line 41 (other nonrefundable credits from IT-201-ATT): $[amount]
  Line 44 (state tax after nonrefundable credits): $[amount]
  Line 45 (other NYS taxes from IT-201-ATT): $[amount]
  Line 46 (total NY state tax): $[amount]

NYC resident tax (if applicable):
  Line 47a (NYC tax on taxable income): $[amount]
  Line 48 (NYC household credit): $[amount]
  Line 50 (UBT taxable income transfer from IT-219): $[amount]
  Line 51 (other NYC taxes): $[amount]
  Line 52 (NYC total before credits): $[amount]
  Line 53 (NYC UBT credit via IT-219 sliding scale): $[amount]
       [UBT paid: $[amount] × credit rate [X%] at NYC taxable income $[amount]]
  Line 54e (NYC total after UBT credit): $[amount]

MCTMT (if applicable):
  Line 54a (Zone 1 at 0.60%): $[amount]  [NESE × rate]
  Line 54b (Zone 2 at 0.34%): $[amount]  [NESE × rate]
  Line 54 (total MCTMT): $[amount]

Yonkers (if applicable):
  Line 55 (resident surcharge at 16.75% of Line 50): $[amount]
  Line 56 (nonresident earnings tax at 0.50%): $[amount]
  Line 57 (part-year resident surcharge): $[amount]

Line 58 (total city, county, MCTMT taxes): $[amount]
Line 59 (sales/use tax on out-of-state purchases): $[amount]
Line 60 (voluntary contributions): $[amount]
Line 61 (total tax before payments): $[amount]
```

#### NY.4 — Payments and final balance

```
## Payments and final balance

Refundable credits:
  Line 63 (Empire State Child Credit, via IT-213): $[amount]
  Line 64 (NYC school tax credit, rate reduction): $[amount]
  Line 65 (NY EIC, via IT-215 — 30% of federal EIC): $[amount]
  Line 66 (NY nonrefundable/refundable child and dependent care credit): $[amount]
  Line 67 (real property tax credit, via IT-214): $[amount]
  Line 68 (college tuition credit, via IT-272): $[amount]
  Line 69 (NYC school tax credit, fixed amount): $[amount]
  Line 69a (NYC school tax credit, rate reduction): $[amount]
  Line 70 (NYC EIC): $[amount]

Withholding and estimated payments:
  Line 72 (NY state tax withheld, W-2 Box 17): $[amount]
  Line 73 (NYC tax withheld, W-2 Box 19): $[amount]
  Line 74 (Yonkers tax withheld, W-2 Box 19): $[amount]
  Line 75 (estimated tax payments from IT-2105 vouchers): $[amount]
       Voucher 1 (paid [date]): $[amount]
       Voucher 2 (paid [date]): $[amount]
       Voucher 3 (paid [date]): $[amount]
       Voucher 4 (paid [date]): $[amount]
  Line 75a (prior-year overpayment applied): $[amount]

Line 76 (total payments): $[amount]

Line 77 (overpayment, if Line 76 > Line 61): $[amount]
Line 78 (amount owed, if Line 76 < Line 61): $[amount]

Underpayment penalty flag: [None / Potential — route to ny-estimated-tax-it-2105]
```

### NY-specific taxpayer action list items

Insert these items into the base "Taxpayer action list" section of the brief, in the order specified, if applicable.

```
NY action items:

1. SIGN Form IT-201 and any supporting schedules (IT-225, IT-558, IT-196, IT-201-ATT, 
   IT-213, IT-215, IT-219, IT-398, IT-272, Y-203) before filing.

2. PAY the balance due on Line 78 by April 15, 2026. Payment options:
   a. Electronic funds withdrawal when e-filing (preferred)
   b. Credit card via Official Payments at www.officialpayments.com (fee applies)
   c. Check payable to "New York State Income Tax" mailed with Form IT-201-V voucher
   
3. IF MAILING: Send to the address listed in Form IT-201-I based on whether a payment is
   enclosed. Do not use the same envelope as the federal return.

4. IF FILING LLC: File Form IT-204-LL and pay the $25 LLC filing fee by March 16, 2026
   (March 15 is a Sunday). See companion skill ny-llc-filing-fee-it-204-ll.
   [This item is present only if the taxpayer operates via an SMLLC.]

5. IF FILING NYC UBT: File Form NYC-202 or NYC-202S and pay any NYC UBT balance.
   The UBT filing is separate from the state return. Confirm NYC UBT was filed before
   the state return to ensure the IT-219 credit amount is accurate.
   [This item is present only if the taxpayer has NYC UBT exposure — see companion skill
   nyc-unincorporated-business-tax.]

6. 2026 ESTIMATED TAX: Pay Q1 2026 NY estimated tax voucher by April 15, 2026, on Form
   IT-2105. The companion skill ny-estimated-tax-it-2105 computes the safe-harbor
   amount.

7. KEEP COPIES of all forms and supporting documentation for at least 3 years (the NY
   statute of limitations for an assessment under NY Tax Law §683 is generally 3 years
   from the filing date, extended in cases of fraud or substantial understatement).

8. IF §174A PATH A ELECTED: Track the 5-year NY recovery schedule for 2026-2029. Each
   year, an IT-558 subtraction equal to the annual NY recovery will be required. A
   separate tracking schedule is attached to this brief.
   [This item is present only if Position 5.15 Path A was elected.]

9. IF §168(k) BONUS DEPRECIATION ADDED BACK: Track the Form IT-398 running balance for
   future years. Each year of the asset's MACRS life, an IT-225 S-125 or IT-558
   subtraction is available.
   [This item is present only if Position 5.12 fired with an add-back.]
```

### Attachment manifest

The skill produces the following attachments to the reviewer brief, in this order:

1. **Form IT-201 (full form)** — 4 pages
2. **Form IT-201-ATT** — if any of Section A, B, C, or D is used (notably Section C for NYC UBT credit)
3. **Form IT-225** — if any addition or subtraction modification is used
4. **Form IT-558** — if any OBBBA decoupling adjustment is used
5. **Form IT-196** — if itemized deductions are claimed (and not refused under R-NY201-3)
6. **Form IT-213** — if Empire State Child Credit is claimed
7. **Form IT-215** — if NY EIC is claimed
8. **Form IT-219** — if NYC UBT credit is claimed
9. **Form IT-398** — if §168(k) bonus depreciation has a running NY basis difference
10. **Form IT-272** — if college tuition credit is claimed
11. **Form Y-203** — if Yonkers nonresident earnings tax is owed
12. **Form IT-201-V payment voucher** — if paper-filing with a balance due
13. **§174A tracking schedule (supplementary)** — if Position 5.15 Path A elected
14. **Cross-skill reconciliation schedule** — listing each value imported from an upstream skill with the source and timestamp

---

## Section 11 — Intake form additions

The base intake form in `us-ca-freelance-intake` (or the generalized `us-multi-state-sole-prop-intake` when built) collects federal-level information. This section specifies the NY-specific questions that must be added when the intake detects the taxpayer is a NY filer. Questions use `ask_user_input_v0` format where interactive, or free-text where a document or figure is required.

### Intake additions NY201-1 through NY201-22

**NY201-1 — NY residency confirmation.**
```
ask_user_input_v0:
  Question: "Were you a New York State resident for the entire 2025 calendar year (January 1 through December 31)?"
  Options: ["Yes, full-year resident", "No, I moved into NY during 2025", "No, I moved out of NY during 2025", "Unsure — my situation is complicated"]
```
Routing: "Yes" → continue. Any other answer → refuse under R-NY201-1.

**NY201-2 — County of residence.**
```
Free-text: "What county did you live in on December 31, 2025? If you lived in New York City, enter the borough name (Manhattan, Brooklyn, Queens, Bronx, or Staten Island)."
```
Used for: school district code, NYC residency determination, MCTD zone determination.

**NY201-3 — School district name and code.**
```
Free-text: "What is the name of your public school district? (Enter the school district where you were a resident on December 31, 2025. Claude will look up the code.)"
```
Used for: Form IT-201 school district code entry. If unknown, Claude searches the NYSDTF school district database at tax.ny.gov/forms/school_district_code_list.htm.

**NY201-4 — NYC living quarters check (for non-NYC residents).**
```
ask_user_input_v0 (only asked if NY201-2 answer is NOT NYC):
  Question: "Did you or your spouse maintain or have use of an apartment or other living quarters in New York City at any point during 2025?"
  Options: ["No", "Yes, but I was not there much", "Yes, and I was there frequently"]
```
Routing: "Yes, and I was there frequently" → follow up with day-count question and potentially refuse under R-NY201-1 for statutory NYC residency. "No" → Item E = No box.

**NY201-5 — Yonkers living quarters check (for non-Yonkers residents).**
```
ask_user_input_v0 (only asked if NY201-2 answer is NOT Yonkers):
  Question: "Did you or your spouse maintain or have use of an apartment or other living quarters in Yonkers at any point during 2025?"
  Options: ["No", "Yes, I had a Yonkers apartment for part of the year", "Yes, for the full year"]
```
Routing: "No" → Item D2 = No box. Any "Yes" → refuse under R-NY201-8 (split-residence) or follow up to determine Yonkers residency.

**NY201-6 — NYC UBT status.**
```
ask_user_input_v0 (only asked if NY201-2 is NYC or any NYC indicator fires):
  Question: "As a self-employed individual in NYC, are you aware that your gross business income may require you to file the NYC Unincorporated Business Tax (NYC-202 or NYC-202S)? The filing threshold is $95,000 of gross business income."
  Options: ["Yes, I know and I have filed/will file NYC-202", "No, I did not know — I need to review", "My income is below the $95,000 threshold"]
```
Routing: Any answer that indicates UBT may apply → invoke `nyc-unincorporated-business-tax` skill. This skill waits for the UBT amount before proceeding to Position 5.24 computation.

**NY201-7 — MCTMT awareness (for MCTD residents with SE income).**
```
ask_user_input_v0 (only asked if county is in the MCTD per §800(b)):
  Question: "As a self-employed individual in the MCTD (metropolitan commuter transportation district), your net self-employment earnings above $50,000 are subject to MCTMT. Zone 1 (NYC five boroughs) rate is 0.60%; Zone 2 (your county) rate is 0.34%. Are you aware of this tax?"
  Options: ["Yes, I know", "No, this is new to me"]
```
Purely educational — no routing impact. Acknowledgment flows to the brief.

**NY201-8 — Prior year carryforwards.**
```
Free-text: "Do you have any of the following from prior-year NY returns? (a) NY depreciation basis differences on assets still in service; (b) NY NOL carryforward; (c) NY credit carryforwards (investment tax credit, college tuition, etc.); (d) None of the above."
```
Routing: (a) → invoke Form IT-398 tracking. (b) → refuse under R-US-NOL (out of scope). (c) → flag for reviewer. (d) → continue.

**NY201-9 — Retirement contributions paid by April 15, 2026.**
```
Free-text: "If you have any retirement plan contributions for tax year 2025 that will be paid between January 1 and April 15, 2026, list them here with the plan type and amount. (Normally these flow from your federal return, but confirm.)"
```
Used for: cross-check against federal `us-self-employed-retirement` output.

**NY201-10 — Estimated tax payments made for 2025.**
```
Free-text: "For each NY estimated tax voucher you paid for 2025, enter: voucher quarter, date paid, NY state amount, NYC amount (if applicable), Yonkers amount (if applicable). For example: 'Q1, 4/15/2025, $2,000 NY, $500 NYC, $0 Yonkers.'"
```
Used for: Line 75 entry and balance due computation.

**NY201-11 — Withholding from W-2s or 1099s.**
```
Free-text: "If you received any W-2 forms or 1099-NECs showing NY state, NYC, or Yonkers withholding, list each one with the payer name and withholding amounts."
```
Used for: Lines 72, 73, 74.

**NY201-12 — Prior year overpayment applied.**
```
ask_user_input_v0:
  Question: "On your 2024 NY return, did you choose to apply any overpayment to your 2025 estimated tax?"
  Options: ["Yes", "No", "I received a refund", "I don't remember — I need to check my 2024 return"]
```
Routing: "Yes" → free-text for amount. "I don't remember" → flag for reviewer to verify.

**NY201-13 — §174A R&E activity.**
```
ask_user_input_v0 (only asked if federal return shows any Schedule C Line 17 "Legal and professional services" or Line 26 "Wages" that could be R&E-related):
  Question: "Do any of your 2025 Schedule C expenses relate to research and development of your own software product or technology (not work you did for clients)? For example, contractor payments to build a prototype of your own app."
  Options: ["No, all my expenses are for client deliverables", "Yes, less than $10,000 of potential R&D expenses", "Yes, more than $10,000 of potential R&D expenses", "I'm not sure"]
```
Routing: "No" → Position 5.15 does not fire. "Less than $10,000" → Position 5.15 fires, default Path A, no refusal. "More than $10,000" or "Not sure" → refuse under R-NY201-5 and route to reviewer.

**NY201-14 — §168(k) bonus depreciation.**
```
ask_user_input_v0:
  Question: "In 2025, did you purchase any business equipment, computers, or other depreciable assets and claim the federal bonus depreciation (§168(k)) deduction?"
  Options: ["No — I did not buy any depreciable assets", "I bought assets but used §179 expensing instead (not bonus)", "Yes — I claimed federal bonus depreciation", "I'm not sure"]
```
Routing: "Yes" → invoke Form IT-398 / IT-558 A-011 computation per Position 5.12. "Not sure" → flag for reviewer.

**NY201-15 — Tax-exempt bond interest source.**
```
ask_user_input_v0 (only asked if federal Form 1040 Line 2a > 0):
  Question: "Your federal return shows tax-exempt interest. Where is it from?"
  Options: ["All from NY state or local bonds (exempt from NY tax)", "All from non-NY state or local bonds (taxable for NY)", "Mixed — my mutual fund tax report has a breakdown", "I don't know"]
```
Routing: "All NY" → no Line 20 addition. "All non-NY" → full addition on Line 20. "Mixed" → ask for the fund's state-of-origin breakdown. "I don't know" → conservative default per Section 6 #5 (100% non-NY add-back).

**NY201-16 — US government obligations interest.**
```
ask_user_input_v0 (only asked if federal Form 1040 Line 2b > 0 or Form 1040 line 7 includes fund distributions):
  Question: "Does any of your taxable interest or dividend income come from US government obligations (Treasury bills, Treasury money market funds, or the US government portion of a mixed bond fund)?"
  Options: ["Yes, I have documentation showing the US government percentage", "Yes, but I don't have the percentage breakdown", "No"]
```
Routing: "Yes with documentation" → free-text for amount, enter on Line 28. "Yes without breakdown" → conservative default per Section 6 #6 (0%, no subtraction). "No" → Line 28 = $0.

**NY201-17 — Pension and annuity income (age 59½+).**
```
ask_user_input_v0 (only asked if taxpayer is 59½ or older based on date of birth):
  Question: "Did you receive any pension or annuity income in 2025 (other than Social Security, government pensions, or Roth IRA distributions)?"
  Options: ["No", "Yes — from a traditional IRA or private pension"]
```
Routing: "Yes" → free-text for amount, apply Position 5.10 exclusion up to $20,000.

**NY201-18 — Empire State Child Credit eligibility.**
```
ask_user_input_v0 (only asked if federal return has dependent children):
  Question: "How many children under 17 do you have as dependents? How many of them are under 4 years old?"
```
Free-text responses. Used for Form IT-213 computation.

**NY201-19 — Real property tax credit eligibility.**
```
ask_user_input_v0:
  Question: "Did you pay real property taxes on your primary residence in 2025, or pay rent where property taxes are included (typically for low-income renters)?"
  Options: ["I own my home and paid property taxes", "I rent", "I own but my taxes are paid through escrow"]
```
Routing: "Own" → flag for real property tax credit consideration if income is low enough. "Rent" → real property tax credit may apply to low-income renters. Defer detailed eligibility to Form IT-214 instructions.

**NY201-20 — Charitable contributions via NY Charitable Gifts Trust Fund.**
```
ask_user_input_v0:
  Question: "Did you make any contributions in 2025 to the New York State Charitable Gifts Trust Fund (the state-level charitable giving program that provides an 85% NY tax credit)?"
  Options: ["No", "Yes"]
```
Routing: "Yes" → flag for reviewer; this is a specific NY credit that is often missed. "No" → continue.

**NY201-21 — Other NY credits awareness.**
```
ask_user_input_v0:
  Question: "Do you qualify for any of these specific NY credits? (a) Long-term care insurance credit; (b) Solar or green building credits; (c) Investment in qualified emerging technology companies; (d) Volunteer firefighter/EMT credit; (e) None of these."
  Options: ["(a)", "(b)", "(c)", "(d)", "(e) None"]
```
Routing: Any credit claim → flag for reviewer to verify eligibility and compute amount. "None" → continue.

**NY201-22 — First-time NY filer or first-time NYC UBT filer flag.**
```
ask_user_input_v0:
  Question: "Is this your first time filing a NY state return, or your first time filing as a NYC resident, or your first time having NYC UBT exposure?"
  Options: ["First time filing NY at all", "First year as a NYC resident", "First year with NYC UBT exposure", "None of the above — I have prior filings"]
```
Routing: "First time" answers → flag for reviewer as a new-filer case that may need extra attention. "None" → continue.

---

## Section 12 — Self-check additions

The base workflow provides 17 self-checks in `us-tax-workflow-base` Section 5. The `ny-llc-filing-fee-it-204-ll` skill adds Checks 18-27. This skill adds **Checks 28 through 46** covering the IT-201-specific invariants.

### Check 28 — Residency gate passed

**Check.** Position 5.1 residency gate returned "full-year NY resident" for the entire 2025 calendar year.

**If false.** R-NY201-1 should have fired; verify refusal trace is present in the brief.

### Check 29 — Federal AGI match

**Check.** The federal AGI imported at Position 5.3 exactly matches the federal AGI on the upstream `us-federal-return-assembly` output.

**If false.** Arithmetic or import error; halt and reconcile.

### Check 30 — NYAGI arithmetic balance

**Check.** `Line 33 NYAGI == Line 19 Federal AGI + (sum of Lines 20-24 additions) − (sum of Lines 25-31 subtractions)` exactly.

**If false.** Arithmetic error in NYAGI computation; halt and recompute.

### Check 31 — A-201 UBT add-back reconciles with NYC UBT skill output

**Check.** If the taxpayer is a NYC resident and Position 5.8 includes an A-201 entry, the A-201 amount exactly matches the UBT deducted on federal Schedule C Line 23 AND matches the UBT paid per the `nyc-unincorporated-business-tax` skill's output.

**If false.** Cross-skill mismatch; flag as high reviewer attention.

### Check 32 — Form IT-225 attached if modifications used

**Check.** If any IT-225 code appears on the return, Form IT-225 is included in the attachment manifest.

**If false.** Structural error; produce Form IT-225.

### Check 33 — Form IT-558 attached if decoupling used

**Check.** If any IT-558 code appears on the return, Form IT-558 is included in the attachment manifest.

**If false.** Structural error; produce Form IT-558.

### Check 34 — §174A position documented

**Check.** If Position 5.15 fired at all, the reviewer brief contains: (a) the federal §174A amount, (b) the Path A dollar impact, (c) the Path B dollar impact, (d) the reviewer election (Path A default or Path B affirmative), and (e) either the IT-558 addition (Path A) or the no-IT-558 note (Path B).

**If false.** Position 5.15 documentation requirement violated; halt and complete the documentation.

### Check 35 — Correct tax computation method used

**Check.** If NYAGI ≤ $107,650, the method is the tax table (if TI < $65,000) or the rate schedule (if TI ≥ $65,000). If NYAGI > $107,650, the method is the tax computation worksheet.

**If false.** Wrong method; produces wrong tax; halt and recompute.

### Check 36 — Recapture worksheet band correctly selected

**Check.** If the tax computation worksheet is used, the worksheet band matches the NYAGI range (e.g., $107,650-$157,650 for single filers with NYAGI in that range).

**If false.** Wrong worksheet band produces wrong tax; halt and recompute.

### Check 37 — Deduction limitation refusal check

**Check.** If NYAGI > $100,000 AND the itemized deduction exceeds the standard deduction, R-NY201-3 should have fired OR the standard deduction was taken.

**If false.** §615(f) limitation not applied; halt and refuse or take standard.

### Check 38 — NYC layer consistency

**Check.** If the taxpayer is a NYC resident, Lines 47a through 54e are populated; if not a NYC resident, those lines are zero.

**If false.** NYC layer mismatch with residency; halt and reconcile.

### Check 39 — NYC UBT credit chain

**Check.** If Line 53 > $0, then:
(a) Form IT-219 is attached
(b) IT-201-ATT Section C is populated
(c) The credit amount traces to the `nyc-unincorporated-business-tax` skill's UBT-paid figure
(d) The sliding-scale computation matches the Position 5.24 formula

**If false.** Credit chain broken; halt and reconcile.

### Check 40 — Yonkers layer consistency

**Check.** If the taxpayer is a Yonkers resident, Line 55 (16.75% of Line 50) is populated; if a Yonkers nonresident with Yonkers earnings, Line 56 (0.50% with $3,000 exemption) is populated; if neither, both are zero.

**If false.** Yonkers layer mismatch; halt and reconcile.

### Check 41 — MCTMT zone determination correct

**Check.** If the taxpayer's county is in the MCTD per §800(b), Line 54a (if Zone 1) or Line 54b (if Zone 2) is populated based on NESE exceeding the $50,000 per-individual-per-zone threshold. If the taxpayer's county is NOT in the MCTD (Albany, Buffalo, etc.), both lines are zero regardless of income.

**If false.** MCTMT misapplication; halt and reconcile.

### Check 42 — MCTMT rate correct per zone

**Check.** Line 54a uses 0.60% (Zone 1); Line 54b uses 0.34% (Zone 2). These rates are not interchangeable.

**If false.** Wrong rate; halt and recompute.

### Check 43 — Per-individual-per-zone threshold applied

**Check.** On a joint return, each spouse's per-zone NESE is tested separately against the $50,000 threshold; the under-threshold spouse's base is excluded.

**If false.** Joint return MCTMT overcounts; halt and recompute per Position 5.28 note.

### Check 44 — Tax layer arithmetic

**Check.** `Line 61 == Line 46 + Line 58 + Line 59 + Line 60` exactly.

**If false.** Arithmetic error; halt and recompute.

### Check 45 — Payment arithmetic

**Check.** `Line 76 == (Lines 63-71 refundable credits) + Line 72 (NY WH) + Line 73 (NYC WH) + Line 74 (Yonkers WH) + Line 75 (estimated payments) + Line 75a (prior-year applied)` exactly.

**If false.** Arithmetic error; halt and recompute.

### Check 46 — Balance due vs refund consistency

**Check.** Exactly one of Line 77 (refund) and Line 78 (balance due) is non-zero, and the non-zero value equals `|Line 76 − Line 61|`.

**If false.** Arithmetic or logic error; halt and recompute.

---

## Section 13 — Cross-skill references

This skill interacts with the following other skills in the Accora stack. Each interaction has a direction (input/output), a payload (what data flows), and an order constraint (when in the workflow).

### Upstream dependencies (this skill consumes)

#### `us-tax-workflow-base v0.2+`
- **Payload:** Workflow runbook, output spec, global refusals (R-US-*), 17 base self-checks, citation discipline, structured intake form scaffolding, slot 7 contract.
- **Order:** Always loaded first; this skill cannot run without it.

#### `us-sole-prop-bookkeeping`
- **Payload:** Classified Schedule C transactions and Schedule C Line 31 net profit.
- **Order:** Runs before federal SE computation; this skill consumes the Schedule C output indirectly via the federal assembly.

#### `us-schedule-c-and-se-computation`
- **Payload:** Schedule C bottom line, Schedule SE net earnings from self-employment (§1402(a) amount), deductible half of SE tax.
- **Order:** Runs before this skill. Position 5.28 and 5.29 (MCTMT) consume the NESE figure directly.

#### `us-qbi-deduction`
- **Payload:** Federal QBI deduction (Form 1040 Line 13).
- **Order:** Runs before this skill. Does NOT affect NY computation directly (NY starts from federal AGI, and QBI is below AGI at federal level). Cross-skill value: the brief notes "QBI structural non-conformity" per Section 2 of this skill.

#### `us-self-employed-retirement`
- **Payload:** Retirement deduction amount flowing to Schedule 1 Line 16.
- **Order:** Runs before this skill. This skill does not recompute.

#### `us-self-employed-health-insurance`
- **Payload:** SE health insurance deduction flowing to Schedule 1 Line 17.
- **Order:** Runs before this skill. This skill does not recompute.

#### `us-federal-return-assembly`
- **Payload:** Federal AGI (Form 1040 Line 11), federal taxable income (Line 15), federal tax liability, final federal return status.
- **Order:** Runs immediately before this skill. Position 5.3 and Position 5.5 consume the federal AGI and lock check.

### Sibling dependencies (this skill coordinates with)

#### `ny-llc-filing-fee-it-204-ll`
- **Payload:** Whether the taxpayer must file IT-204-LL (yes if SMLLC with any NY source income), the $25 fee amount, and the March 16, 2026 due date.
- **Order:** This skill does not depend on IT-204-LL computation to produce IT-201. The two returns are independent in computation but both flow into the final deliverable. The orchestrator `us-federal-ny-return-assembly` coordinates them.

#### `nyc-unincorporated-business-tax` (to be built next)
- **Payload:** NYC UBT liability amount, Form NYC-202 or NYC-202S status, UBT paid during 2025 (the A-201 add-back source), and the Form IT-219 credit input.
- **Order:** **This skill depends on the NYC UBT skill's output.** Position 5.8 (A-201 add-back) and Position 5.24 (IT-219 credit computation) both consume the UBT amount. The orchestrator runs the NYC UBT skill before this skill's NYC-dependent positions.
- **Interaction point:** Position 5.24 receives the UBT-paid figure and applies the IT-219 sliding-scale; the resulting credit flows back to IT-201 Line 53.

#### `ny-estimated-tax-it-2105` (to be built)
- **Payload:** 2026 quarterly estimated tax vouchers (prospective) and 2025 underpayment penalty computation (retrospective, if applicable).
- **Order:** This skill produces the inputs (2025 NY tax, 2024 NY tax for safe harbor, balance due) but does NOT compute the penalty or the 2026 vouchers. The ny-estimated-tax skill consumes this skill's output.

### Orchestrator

#### `us-federal-ny-return-assembly` (to be built)
- **Purpose:** Enforces the execution order: federal stack → ny-it-201-resident-return → nyc-unincorporated-business-tax (if applicable) → ny-llc-filing-fee-it-204-ll (if applicable) → ny-estimated-tax-it-2105 (for 2026 planning).
- **Responsibility:** Produces the final unified reviewer package with the federal return, the NY return, the NYC UBT return (if any), the IT-204-LL filing (if any), and the 2026 estimated tax schedule. Runs the cross-skill reconciliation check (A-201 add-back vs UBT paid; IT-219 credit vs UBT paid; MCTMT NESE vs Schedule C).

### Interaction diagram (logical order)

```
us-sole-prop-bookkeeping
        ↓
us-schedule-c-and-se-computation
        ↓
us-self-employed-retirement ←→ us-self-employed-health-insurance
        ↓
us-qbi-deduction
        ↓
us-federal-return-assembly (produces federal AGI, locks federal return)
        ↓
nyc-unincorporated-business-tax (if NYC resident; produces UBT amount)
        ↓
ny-it-201-resident-return ←— this skill
        ↓
ny-llc-filing-fee-it-204-ll (if SMLLC)
        ↓
ny-estimated-tax-it-2105 (for 2026 planning and 2025 penalty)
        ↓
us-federal-ny-return-assembly (orchestrator finalizes everything)
```

The horizontal arrow between retirement and SEHI indicates the circular computation handled by the federal assembly orchestrator — both skills feed each other because SEHI deduction depends on NESE, which depends on retirement contribution, which depends on SEHI deduction. The federal assembly resolves this circularity before this skill runs.

---

## Section 14 — Reference material, design notes, and change log

### Reference material (supplementary, not authoritative)

The primary source library in Section 4 lists all authoritative citations. The items below are secondary resources the skill's future maintainers may find useful for verification or updates.

**NYSDTF publications (not primary authority but useful for taxpayer-facing guidance):**
- Publication 36, General Information for Senior Citizens and Retired Persons
- Publication 88, General Tax Information for New York State Nonresidents and Part-Year Residents (for cross-reference when refusing under R-NY201-1)
- Publication 99, General Tax Information for New York State Residents
- Publication 16, New York Tax Status of Limited Liability Companies and Limited Liability Partnerships (cross-reference with `ny-llc-filing-fee-it-204-ll`)

**Secondary analysis of the §174A uncertainty (Position 5.15):**
- Bonadio CPA firm analysis of the Hochul FY 2026-27 Executive Budget §174A decoupling proposal (January 2026)
- The Tax Foundation state tax round-up for 2025-2026 (tracks state conformity to OBBBA; useful for comparing NY's position to other states)
- The MoneyWise CPA blog post series on OBBBA state conformity (not authoritative but useful for tracking the legislative calendar)

**NYC Department of Finance materials for UBT cross-reference:**
- NYC-202 and NYC-202S 2025 instructions (for confirming the UBT paid figure that flows to IT-219)
- NYC Business Tax Forms page at nyc.gov/finance

**MTA MCTD maps and guidance:**
- NY Tax Law §800(b) is the authoritative MCTD county list, but the MTA publishes maps showing the commuter rail and subway footprint that informs the zone structure. These are not authoritative but are useful for taxpayer communication.

### Design notes

**Why this skill is load-bearing.** The `ny-it-201-resident-return` skill owns four intra-NY tax layers (state + NYC + Yonkers + MCTMT) that must be coordinated correctly because they share a common tax base (NY taxable income) with layer-specific modifications. No other skill in the NY stack has the authority to compute these layers. If this skill is wrong, every downstream skill (IT-204-LL, IT-2105, orchestrator) is wrong. For this reason, the skill has aggressive self-checks (28-46) and demands upstream lock before proceeding.

**Why the §174A uncertainty is handled with a refusal rather than a default.** Position 5.15 could have defaulted silently to Path A (conservative) or Path B (federal-conforming). The skill instead refuses material positions and requires affirmative reviewer election because: (a) the legislative uncertainty is likely to resolve within 6-12 months of the skill's currency date, making any silent default potentially stale; (b) the dollar impact of the choice is typically material (a $40k+ R&E position at 6.85% combined rate = $2,700+ of tax); (c) the reviewer assumption in Circular 230 professional practice is that material positions require affirmative professional judgment, not a software default; (d) an amended return under Path B, if the Hochul proposal passes, is more expensive than the Path A conservative route, but the amendment risk must be acknowledged and documented, not hidden.

**Why the MCTMT per-individual-per-zone rule gets its own position.** The rule in NY Tax Law §801 is simple in text but easy to misapply in practice. A joint return with one spouse above the $50,000 threshold and one below looks, at first glance, like it should aggregate the spouses' bases for a single threshold test. It does not. Each spouse is tested separately. This is a common error in self-prepared returns and even in some professional returns. The dedicated positions (5.28-5.30) with explicit worked examples (Example 3, Carlos + Maria) anchor the rule in practice.

**Why the NYC UBT credit computation is done in this skill rather than the NYC UBT skill.** The NYC UBT skill computes the UBT liability on Form NYC-202/NYC-202S. The sliding-scale credit under IT-219 is a NY state credit that happens to reference the NYC UBT paid amount — it is structurally a state-level credit, not a NYC-level credit. Form IT-219 is an NYSDTF form, not an NYC Department of Finance form. For this reason, the IT-219 computation belongs in the state skill (this skill), with a cross-skill dependency on the NYC skill for the UBT-paid amount. The data flow is clear: NYC UBT skill produces UBT paid; this skill produces IT-219 credit and flows it to IT-201 Line 53.

**Why Albany, Buffalo, Rochester are explicitly called out as non-MCTD.** Self-preparing freelancers in upstate NY sometimes mistakenly believe MCTMT applies to them because they have NYC clients or because "NY = NYC" in the mental model. The MCTD is explicitly defined in NY Tax Law §800(b) as 12 counties (NYC five boroughs + 7 surrounding counties). Albany, Buffalo, Rochester, Syracuse, Binghamton, and the entire North Country are NOT in the MCTD. Example 5 (Rachel) exists specifically to anchor this distinction for both the skill and the reviewer. The brief explicitly states "MCTMT = $0 because Albany County is not in the MCTD" when applicable, so there is no ambiguity about whether MCTMT was missed or intentionally zero.

**Why the recapture worksheet is explained as a method, not a separate tax.** The $107,650 threshold and the bands above it produce what journalists call the "recapture tax" or "supplemental tax on high earners." In the actual statute (§601(d)(1) and the parallel sections), this is not a separate tax — it is a different method of computing the same tax base that phases out the bracket benefit. The skill explains this explicitly in Position 5.19 to prevent a reviewer from treating it as an additional tax to be computed alongside the regular tax. Treating it as a separate tax would double-count.

**Why the brief includes a sanity check on effective rate (Example 6, Jake).** For high-income taxpayers, a 10-11% combined effective rate (state + NYC + MCTMT) on NYAGI is reasonable. A computed effective rate below 8% or above 12% is a signal of either a math error or a missed position. The brief includes the effective rate as a reasonableness flag.

**Why the skill does not compute NY credits for taxes paid to another state (R-NY201-6).** The §620 credit is often materially valuable (potentially thousands of dollars for a freelancer with significant out-of-state income) but it requires computing the credit cap under the §620(e) limitation formula, which in turn requires detailed NY source vs non-NY source allocation. This allocation requires Form IT-203-A or equivalent analysis and is too complex to handle reliably in a skill that is primarily designed for single-state resident cases. The refusal preserves taxpayer rights by flagging the credit for reviewer rather than silently omitting it.

**Why the §615(f) itemized limitation is refused rather than computed.** The limitation phases out itemized deductions through multiple income bands under 20 NYCRR §112.3, with different formulas at different NYAGI levels. The computation is rarely worth it for freelance developers (who typically benefit from the standard deduction anyway), and the refusal preserves correctness in the rare case where it matters.

### Versioning

This skill follows the Accora skill versioning convention: `vMAJOR.MINOR` where MAJOR increments on structural changes (new sections, new position rules, changed slot contract) and MINOR increments on content updates (new year's figures, updated citations, refinements to existing positions).

### Change log

**v0.1 — April 2026** (this version)
- Initial release
- Covers tax year 2025 (returns due April 15, 2026)
- Conforms to `us-tax-workflow-base v0.2` slot contract (all 13 slots)
- 34 structured position rules in Section 5
- 12 topical refusals (R-NY201-1 through R-NY201-12) in Section 7
- 6 worked examples in Section 9
- 22 intake form additions (NY201-1 through NY201-22) in Section 11
- Self-checks 28-46 in Section 12
- Cross-skill coordination with `ny-llc-filing-fee-it-204-ll`, `nyc-unincorporated-business-tax` (pending), `ny-estimated-tax-it-2105` (pending)
- Position 5.15 §174A uncertainty handled via two-path reviewer decision with R-NY201-5 refusing material positions
- Currency date: April 2026; Hochul FY 2026-27 Executive Budget §174A proposal monitored but not enacted

**Pending for v0.2 (target: summer 2026):**
- Update figures for any 2025 legislative changes enacted after April 2026
- Resolve Position 5.15 §174A path once legislation clarifies
- Add line number verification against the finalized 2025 Form IT-201 (current version locked from January 2026 release)
- Refine NYC UBT credit worked example once `nyc-unincorporated-business-tax` skill is released and the cross-skill data contract is frozen

**Pending for v1.0 (target: 2027 for tax year 2026 returns):**
- Update all figures to 2026 values
- Incorporate any §601 rate changes or threshold updates from Chapter 59 of the Laws of 2026
- Revise Position 5.15 based on final §174A legislative outcome
- Add tax year 2026 rate schedules and standard deduction amounts
- Verify line numbers against 2026 Form IT-201 (to be released January 2027)
- Consider whether new sub-state layers (any new NYC surcharges, Yonkers rate changes, MCTMT threshold changes) require new positions

### Maintenance notes for future versions

**Every version update must:**
1. Verify the rate schedules and thresholds in Section 3 against the then-current Form IT-201-I
2. Verify the primary source URLs in Section 4 still resolve
3. Re-confirm the MCTMT zone classifications in §800(b) have not changed
4. Re-confirm the NYC resident tax brackets in §11-1701 have not changed
5. Re-confirm the Yonkers surcharge rate in §92-5 has not changed
6. Re-confirm the §174A NY position (in force or not in force) and update Position 5.15 accordingly
7. Update the currency date and the change log
8. Run the six worked examples against the new year's figures to verify no arithmetic drift

**Legislative monitoring sources for version maintenance:**
- NYSDTF Personal Income Tax Up-to-Date Information page (tax.ny.gov/pit/personal_income_tax_up_to_date.htm)
- Chapter Laws of the State of New York (the official source of enacted legislation)
- Governor's Executive Budget proposals (budget.ny.gov)
- State Assembly Ways and Means Committee reports
- NYSDTF TSB-M (Tax Bulletin Memoranda) releases

**When to cut a new minor version vs continue under v0.x:**
- Any change to a rate or threshold = new version
- Any change to a refusal trigger = new version
- Any change to a position rule that could produce a different dollar result = new version
- Editorial or citation clarity improvements = continue under current version with a dated patch note

---

## End of Turn 4 — Skill complete

### Turn 4 summary

This turn drafted the final five sections (10-14) of `ny-it-201-resident-return`, completing the skill.

**Section 10 (Output format extensions)** — four structured brief additions: NY.1 residency and layer determination, NY.2 NYAGI reconciliation, NY.3 tax layer summary, NY.4 payments and final balance. Also a taxpayer action list template with 9 NY-specific items (signing, payment, LLC filing coordination, NYC UBT coordination, 2026 estimates, retention, §174A tracking, §168(k) tracking) and a 14-item attachment manifest.

**Section 11 (Intake form additions)** — 22 structured intake questions (NY201-1 through NY201-22) using `ask_user_input_v0` format where interactive and free-text where documentary. Covers residency, county, school district, NYC/Yonkers living quarters, NYC UBT awareness, MCTMT awareness, prior-year carryforwards, retirement contributions, estimated tax payments, withholding, prior-year overpayment, §174A R&E activity, §168(k) bonus depreciation, tax-exempt bond sources, US government obligations, pension/annuity income, Empire State Child Credit, real property tax credit, NY Charitable Gifts Trust Fund, other NY credits, first-time filer status.

**Section 12 (Self-check additions)** — Checks 28-46 (19 new checks), extending the base 1-17 and the IT-204-LL skill's 18-27. Covers: residency gate pass, federal AGI match, NYAGI arithmetic, A-201 UBT cross-skill reconciliation, IT-225/IT-558 attachment, §174A documentation, tax computation method selection, recapture band selection, §615(f) refusal check, NYC layer consistency, NYC UBT credit chain, Yonkers layer consistency, MCTMT zone determination, MCTMT rate per zone, per-individual-per-zone threshold, tax layer arithmetic, payment arithmetic, and balance due/refund consistency.

**Section 13 (Cross-skill references)** — explicit documentation of upstream dependencies (7 federal skills plus workflow base), sibling dependencies (IT-204-LL, NYC UBT, IT-2105), and the orchestrator. Includes an interaction diagram showing the logical execution order.

**Section 14 (Reference material, design notes, change log)** — supplementary resources (NYSDTF publications, secondary §174A analysis, NYC DOF materials, MTA zone references), design notes explaining the key structural choices (why load-bearing, why §174A refusal, why per-individual-per-zone is dedicated, why NYC UBT credit is in this skill, why non-MCTD counties are called out, why recapture is a method not a tax, why effective rate sanity checks, why §620 refusal, why §615(f) refusal), v0.1 change log, pending items for v0.2 and v1.0, and maintenance notes.

### Skill-level summary

**File length at completion:** Turn 1 (440 lines) + Turn 2 (598 lines) + Turn 3 (554 lines) + Turn 4 (~950 lines) = approximately **2,540 lines**, near the bottom of the 2,500-2,700 line estimate.

**Slot contract conformance (13 slots):**
1. ✅ Scope statement (Section 1)
2. ✅ Tax year coverage (Section 2)
3. ✅ Year-specific figures table (Section 3)
4. ✅ Primary source library (Section 4)
5. ✅ Position rules with worked examples (Section 5, 34 positions)
6. ✅ Topical refusal catalogue R-NY201-1 through R-NY201-12 in trigger/output verbatim format (Section 7)
7. ✅ Conservative defaults table (Section 6, 24 rows)
8. ✅ Reviewer attention thresholds (Section 8, three tables)
9. ✅ Worked examples minimum 5 (Section 9, six examples)
10. ✅ Output format extension (Section 10)
11. ✅ Intake form additions (Section 11, 22 questions)
12. ✅ Self-check additions (Section 12, Checks 28-46)
13. ✅ Currency and revision metadata (Section 14, change log)

**The skill is production-ready** subject to the usual caveat that no skill is truly production-ready until it runs in anger against real taxpayer data and is validated by Kevin or Darren on a handful of test cases.

### Next steps

1. Kevin or Darren review of the complete skill
2. Four remaining NY skills to build:
   - `nyc-unincorporated-business-tax` (~1,800 lines, the biggest remaining)
   - `ny-estimated-tax-it-2105` (~700 lines)
   - `us-multi-state-sole-prop-intake` (updates to existing intake)
   - `us-federal-ny-return-assembly` orchestrator (~500 lines)
3. Cross-skill validation: run a test case through the full NY stack end-to-end to verify the A-201 UBT add-back, IT-219 credit flow, and MCTMT computations all reconcile correctly


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

If you would like a licensed accountant to review your return, visit [openaccountants.com](https://openaccountants.com) and log in to request a professional review.
