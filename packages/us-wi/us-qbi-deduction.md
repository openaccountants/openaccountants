---
name: us-qbi-deduction
description: Tier 2 content skill for computing the §199A Qualified Business Income deduction for US sole proprietors and single-member LLCs disregarded for federal tax purposes. Covers tax year 2025 under the One Big Beautiful Bill Act (P.L. 119-21, July 4 2025) which made §199A permanent at 20%. Handles the QBI calculation from Schedule C net profit, the deductible SE tax and SE health insurance adjustments, the taxable income thresholds ($197,300 single / $394,600 MFJ), phase-in ranges for SSTB and W-2/UBIA limitations, the specified service trade or business (SSTB) classification, W-2 wage and UBIA of qualified property limitations, the interaction with retirement contributions, and Forms 8995 (simplified) and 8995-A (detailed). Consumes net profit from us-schedule-c-and-se-computation and SE health insurance / retirement from companion skills. MUST be loaded alongside us-tax-workflow-base v0.1 or later. Federal only. No state tax.
version: 0.2
jurisdiction: US
tax_year: 2025
last_updated: 2026-07-13
reviewed_by: A licensed accountant (name withheld at their request)
review_status: current
tier: 1
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# US QBI Deduction

## US QBI Deduction Skill v0.3

## Verified rates & thresholds (accountant-reviewed)

- **§199A QBI deduction rate for tax year 2025** — 20% percent (tax years beginning after Dec 31, 2024)  _(§199A, OBBBA P.L. 119-21 §70105)_

Reviewed against the cited tax authorities by a licensed accountant on 2026-06-03. Items flagged for further clarification are tracked separately and excluded here. This block is generated from verified `skill_facts` — edit the facts, not the prose.

### QBI Deduction

- **Rate 2025** — 20%  _(IRC 199A; OBBBA (made 199A permanent at 20%).)_
- **Rate 2026+** — The QBI rate remains 20% in 2026 and beyond. OBBBA made 199A permanent at 20%; the proposed increase to 23% (House bill) did not become law.  _(IRC 199A; OBBBA (PL 119-21).)_
- **Single threshold 2025** — $197,300 (Single/other)  _(Rev. Proc. 2024-40.)_
- **MFJ threshold 2025** — $394,600 (MFJ)  _(Rev. Proc. 2024-40.)_

## What this file is, and what it is not

This file is a content skill that loads on top of `us-tax-workflow-base` v0.1. It computes the §199A Qualified Business Income (QBI) deduction for sole proprietors and single-member LLCs (disregarded entities) for tax year 2025. It does not classify transactions (that is `us-sole-prop-bookkeeping`), compute Schedule C net profit or SE tax (that is `us-schedule-c-and-se-computation`), or compute retirement contributions or SE health insurance (those are companion skills whose outputs feed into this one).

**Where this skill fits in the pipeline:**

```
Bank statement / source data
        ↓
us-sole-prop-bookkeeping (classifies every transaction into a Schedule C line)
        ↓
us-schedule-c-and-se-computation (aggregates, runs Form 8829, computes net profit, computes SE tax)
        ↓
us-self-employed-retirement + us-self-employed-health-insurance (retirement deduction, SE health insurance deduction)
        ↓
us-qbi-deduction (THIS SKILL — computes QBI and the §199A deduction)
        ↓
us-quarterly-estimated-tax (safe harbor for following year)
```

This skill is downstream of Schedule C computation AND of the retirement and SE health insurance skills. That ordering matters because QBI is reduced by retirement contributions and SE health insurance premiums, creating a circular dependency that must be resolved iteratively or algebraically.

**Tax year coverage.** This skill is current for **tax year 2025** as of its currency date (April 2026). It reflects the One Big Beautiful Bill Act (Public Law 119-21, signed July 4, 2025), which made §199A permanent at the 20% rate. The 23% rate that appeared in the House-passed version of H.R. 1 was NOT enacted — the deduction rate is 20% for 2025 and remains 20% for 2026 and later years. For tax years beginning after December 31, 2025, OBBBA §70105 widens the phase-in ranges to $75,000 (non-joint) / $150,000 (joint) and adds a new §199A(i) minimum deduction (greater of the computed deduction or $400, for taxpayers with at least $1,000 of aggregate QBI from active qualified trades or businesses). Those 2026+ changes do NOT apply to tax year 2025 returns.

**The reviewer is the customer of this output.** The skill produces a QBI computation worksheet and a brief that the reviewing EA or CPA can audit and sign off on.

## Section 1 — Scope statement

This skill covers, for tax year 2025:

- **QBI computation** from Schedule C net profit, adjusted for the deductible half of SE tax, SE health insurance premiums, and retirement contributions
- **§199A deduction calculation** at the 20% rate
- **Taxable income threshold testing** — determining whether the simplified or detailed computation applies
- **Specified service trade or business (SSTB) classification** — determining whether the taxpayer's trade or business is an SSTB under §199A(d)(2) and Treas. Reg. §1.199A-5
- **W-2 wage limitation** — the greater-of test under §199A(b)(2): (a) 50% of W-2 wages, or (b) 25% of W-2 wages plus 2.5% of UBIA of qualified property
- **UBIA of qualified property limitation** — unadjusted basis immediately after acquisition of qualified property
- **Phase-in computation** for taxpayers with taxable income within the phase-in range above the threshold
- **Form 8995 (simplified)** — for taxpayers with taxable income at or below the threshold
- **Form 8995-A (detailed)** — for taxpayers with taxable income above the threshold, SSTBs, or multiple trades or businesses
- **The circular dependency** between QBI, retirement contributions, and SE health insurance
- **Taxable income limitation** — QBI deduction cannot exceed 20% of taxable income (excluding net capital gain)

This skill does NOT cover:

- QBI from sources other than Schedule C (partnerships on K-1, S corporations on K-1, REITs, PTPs) — out of scope
- Aggregation of multiple trades or businesses under Treas. Reg. §1.199A-4 — flagged for reviewer if multiple Schedule Cs exist
- Net operating loss interactions with QBI — flagged for reviewer
- QBI carryover of losses from prior years — flagged for reviewer
- Any state-level QBI deduction or addback — out of scope
- Computation of the deduction for cooperatives under §199A(g) — out of scope
- The §199A(i) minimum deduction ($400) — first applies to tax years beginning after December 31, 2025; out of scope for TY2025 returns

## Section 2 — Year coverage and currency

**Tax year covered:** 2025 (returns due April 15, 2026, or October 15, 2026 with extension).

**Currency date:** April 2026.

**Legislation reflected:**
- Internal Revenue Code §199A as in force for tax year 2025
- One Big Beautiful Bill Act (OBBBA), Public Law 119-21, signed July 4, 2025 — §70105 made §199A permanent at the 20% rate (it was set to expire after 2025 under TCJA). The 23% rate in the House-passed bill was NOT enacted. Effective for tax years beginning after December 31, 2025, §70105 also widens the phase-in ranges to $75,000 (non-joint) / $150,000 (joint) and adds the §199A(i) minimum deduction ($400 / $1,000-of-QBI test, indexed after 2026)
- OBBBA §70102 — retroactively increased the 2025 standard deduction to $15,750 single/MFS, $23,625 HoH, $31,500 MFJ (used in this skill's taxable-income computations)
- Tax Cuts and Jobs Act of 2017 — original enactment of §199A
- Treasury Regulations §1.199A-1 through §1.199A-6 — final regulations (January 2019) and subsequent amendments
- Rev. Proc. 2024-40 — 2025 inflation adjustments for taxable income thresholds (§199A item at §3.27)
- Rev. Proc. 2025-32 — modified Rev. Proc. 2024-40 for OBBBA (2025 standard deduction) and published the 2026 §199A thresholds
- Form 8995 and Form 8995-A Instructions for tax year 2025
- IRS Publication 334 (Tax Guide for Small Business) — Pub 535 was discontinued after its 2022 revision

**Currency limitations:**
- OBBBA made §199A permanent at 20%. No OBBBA provision changed the 2025 QBI mechanics (rate, thresholds, $50,000/$100,000 phase-in widths, SSTB rules, W-2 wage test, UBIA test). The wider $75,000/$150,000 phase-in ranges and the $400 minimum deduction apply only to tax years beginning after December 31, 2025.
- For tax year 2025 the phase-in range widths ($50,000 non-joint / $100,000 joint) are statutory under §199A(b)(3)(B) and §199A(d)(3)(A) and are NOT indexed for inflation. (For 2026+ the statutory widths become $75,000 / $150,000.)

## Section 3 — Year-specific figures table for tax year 2025

**Year-specific figures table for tax year 2025**  _(Section 3 table, various IRC/Rev. Proc. citations as shown)_

| Figure | Value for TY2025 | Primary source |
| --- | --- | --- |
| §199A QBI deduction rate | 20% | IRC §199A(a); OBBBA P.L. 119-21 §70105 (permanent) |
| §199A QBI deduction rate (2026 onward) | 20% — unchanged; the 23% House-bill rate was not enacted | IRC §199A(a) as amended by OBBBA P.L. 119-21 |
| Taxable income threshold (single / HoH / QSS) | $197,300 | Rev. Proc. 2024-40 §3.27; IRC §199A(e)(2) |
| Taxable income threshold (MFJ) | $394,600 | Rev. Proc. 2024-40 §3.27 |
| Taxable income threshold (MFS) | $197,300 | Rev. Proc. 2024-40 §3.27 |
| Phase-in range width (single / HoH / QSS / MFS) | $50,000 above threshold | IRC §199A(b)(3)(B), §199A(d)(3)(A); statutory, not indexed |
| Phase-in range width (MFJ) | $100,000 above threshold | IRC §199A(b)(3)(B), §199A(d)(3)(A); statutory, not indexed |
| Phase-in range top (single / MFS) | $247,300 | $197,300 + $50,000; Rev. Proc. 2024-40 §3.27 |
| Phase-in range top (MFJ) | $494,600 | $394,600 + $100,000; Rev. Proc. 2024-40 §3.27 |
| W-2 wage limitation — alternative 1 | 50% of W-2 wages | IRC §199A(b)(2)(B)(i) |
| W-2 wage limitation — alternative 2 | 25% of W-2 wages + 2.5% of UBIA | IRC §199A(b)(2)(B)(ii) |
| Taxable income cap on QBI deduction | 20% of taxable income (excl. net capital gain) | IRC §199A(a)(1)(B) |
| Standard deduction (single / MFS) | $15,750 (OBBBA retroactive increase) | OBBBA §70102; Rev. Proc. 2025-32 §3.01 |
| Standard deduction (HoH) | $23,625 | OBBBA §70102; Rev. Proc. 2025-32 §3.01 |
| Standard deduction (MFJ / QSS) | $31,500 | OBBBA §70102; Rev. Proc. 2025-32 §3.01 |
| SE tax rate (for deductible-half computation) | 15.3% (12.4% OASDI + 2.9% Medicare) | IRC §1401 |
| Net SE earnings adjustment factor | 92.35% | IRC §1402(a)(12) |
| Social Security (OASDI) wage base | $176,100 | SSA; Schedule SE instructions (2025) |

**Forward look — figures for tax year 2026 (do NOT apply to 2025 returns):** thresholds $201,750 single/HoH/QSS, $201,775 MFS, $403,500 MFJ; phase-in completion amounts $276,750 / $276,775 / $553,500 (widths $75,000 / $75,000 / $150,000); minimum deduction $400 where aggregate QBI from active qualified trades or businesses ≥ $1,000. Source: Rev. Proc. 2025-32 §4.26 and §2.12; IRC §199A(i).

## Section 4 — Primary source library

### Statute (Internal Revenue Code, Title 26 USC)

- **IRC §199A** — Qualified business income deduction (full section)
- **IRC §199A(a)** — Allowance of deduction: lesser of (A) combined QBI amount or (B) 20% of taxable income minus net capital gain
- **IRC §199A(b)** — Combined QBI amount: sum of deductible amounts for each qualified trade or business
- **IRC §199A(b)(2)** — W-2 wage / UBIA limitation (applies above the threshold)
- **IRC §199A(b)(3)(B)** — Phase-in of the W-2/UBIA limitation ($50,000 / $100,000 range widths for 2025; $75,000 / $150,000 for 2026+)
- **IRC §199A(b)(6)(B)** — Depreciable period for UBIA purposes (later of 10 years or the §168 recovery period determined without regard to §168(g))
- **IRC §199A(c)** — Definition of qualified business income
- **IRC §199A(c)(3)(B)** — Items excluded from QBI: capital gains/losses, dividends, interest not allocable to trade or business, commodities transactions, foreign currency gains/losses, certain annuity income
- **IRC §199A(c)(4)** — QBI does not include reasonable compensation paid to taxpayer by S corp or guaranteed payments from partnership
- **IRC §199A(d)** — Qualified trade or business definition, SSTB exclusion
- **IRC §199A(d)(2)** — Specified service trade or business defined
- **IRC §199A(d)(3)** — Exception for taxpayers below threshold; SSTB phase-in range
- **IRC §199A(e)(2)** — Taxable income threshold amount
- **IRC §199A(f)** — Special rules (netting of QBI from multiple businesses, carryover of losses)
- **IRC §199A(i)** — Minimum deduction (added by OBBBA §70105; tax years beginning after December 31, 2025 only)
- **IRC §164(f)** — Deductible half of SE tax
- **IRC §162(l)** — Self-employed health insurance deduction
- **IRC §1402(a)(12)** — 92.35% net SE earnings adjustment

### Treasury Regulations (26 CFR)

- **Treas. Reg. §1.199A-1** — Operational rules
- **Treas. Reg. §1.199A-2** — W-2 wages and UBIA of qualified property
- **Treas. Reg. §1.199A-3** — Qualified business income, qualified REIT dividends, qualified PTP income
- **Treas. Reg. §1.199A-4** — Aggregation of trades or businesses
- **Treas. Reg. §1.199A-5** — Specified service trades or businesses and the trade or business of performing services as an employee
- **Treas. Reg. §1.199A-6** — RPE-level reporting

### IRS Guidance and Forms

- **Rev. Proc. 2024-40** — 2025 inflation adjustments (§199A thresholds at §3.27)
- **Rev. Proc. 2025-32** — OBBBA modifications to 2025 amounts; 2026 inflation adjustments (§199A at §4.26)
- **Form 8995** — Qualified Business Income Deduction Simplified Computation (and instructions)
- **Form 8995-A** — Qualified Business Income Deduction (detailed, with Schedules A through D) (and instructions)
- **IRS Publication 334** — Tax Guide for Small Business (Publication 535 was discontinued after the 2022 revision)

## Section 5 — The QBI computation for sole proprietors

### Step 1 — Determine qualified business income (QBI)

- **QBI formula** — QBI = Schedule C net profit (Line 31) − Deductible half of SE tax (Schedule 1, Line 15) − SE health insurance deduction (Schedule 1, Line 17) − Deductible retirement contributions (Schedule 1, Line 16 — SEP, SIMPLE, Solo 401(k))  _(IRC §199A(c)(1); §62(a)(1))_
- **Items NOT subtracted from QBI** — The standard deduction or itemized deductions (these are not attributable to the trade or business); Traditional IRA contributions (personal deduction under §219, not attributable to the trade or business — see Edge case 9); The QBI deduction itself (that would be circular — the statute explicitly excludes it); Estimated tax payments (these are not deductions); State income taxes (not deductible on Schedule C and not attributable under §199A)  _(IRC §219; IRC §199A(c)(1))_

### Step 2 — Determine taxable income BEFORE the QBI deduction

- **Taxable income for QBI purposes** — Taxable income for QBI threshold purposes = AGI minus the greater of the standard deduction or itemized deductions, computed WITHOUT the QBI deduction itself. This figure determines: 1. Whether the taxpayer is below, within, or above the phase-in range; 2. The overall cap on the QBI deduction (20% of taxable income excluding net capital gain)  _(IRC §199A(e)(2))_

### Step 3 — Apply the threshold test

- **Below the threshold** — Below the threshold (taxable income ≤ $197,300 single / $394,600 MFJ): The QBI deduction is simply 20% of QBI, subject to the taxable income cap; SSTB classification does NOT matter (the SSTB exclusion is phased in above the threshold); W-2 wage and UBIA limitations do NOT apply; Use Form 8995 (simplified computation)  _(IRC §199A(d)(3); §199A(b)(3))_
- **Above threshold but within phase-in range** — Above the threshold but within the phase-in range ($197,300 < TI ≤ $247,300 single / $394,600 < TI ≤ $494,600 MFJ): W-2 wage / UBIA limitations are phased in; SSTB exclusion is phased in (QBI, W-2 wages, and UBIA are reduced by the applicable percentage); Use Form 8995-A (detailed computation); The phase-in percentage = (taxable income − threshold) / phase-in range width  _(IRC §199A(b)(3)(B); §199A(d)(3))_
- **Above the phase-in range** — Above the phase-in range (taxable income > $247,300 single / $494,600 MFJ): W-2 wage / UBIA limitations apply in full; SSTB businesses get ZERO QBI deduction; Use Form 8995-A (detailed computation)  _(IRC §199A(b)(2); §199A(d)(3))_

### Step 4 — W-2 wage and UBIA limitation (when applicable)

- **W-2/UBIA limitation greater-of test** — For taxpayers above the threshold, the QBI deduction for each qualified trade or business cannot exceed the GREATER of: (a) 50% of W-2 wages paid by that trade or business, OR (b) 25% of W-2 wages paid by that trade or business PLUS 2.5% of the unadjusted basis immediately after acquisition (UBIA) of qualified property held by the business. For most sole props without employees: W-2 wages = $0 (the sole proprietor's own draw is NOT W-2 wages). This means: Alternative (a) = $0; Alternative (b) = 2.5% of UBIA of qualified property. If the sole prop has no depreciable property still within its depreciable period (see Step 5), UBIA = $0, and BOTH alternatives = $0. This means the QBI deduction is limited to $0 for taxpayers fully above the phase-in range. This is the critical cliff for high-income sole props without employees. If taxable income exceeds the phase-in range top and the business has no W-2 wages and no qualifying property, the QBI deduction is $0. This is a major reason high-income sole props consider S corporation election (to create W-2 wages via reasonable compensation).  _(IRC §199A(b)(2)(B)(i)-(ii))_

### Step 5 — UBIA of qualified property

- **UBIA definition** — UBIA = the unadjusted basis of tangible depreciable property held at the close of the tax year, that is: Used in the production of QBI, AND Still within its depreciable period — which ends on the LATER of (a) 10 years after the placed-in-service date, or (b) the last day of the last full year in the applicable recovery period under §168 determined without regard to §168(g) (i.e., the regular MACRS/GDS recovery period, not ADS). "Unadjusted" means the original cost basis without reduction for depreciation. The property must still be in use at year-end.  _(IRC §199A(b)(6)(B); Treas. Reg. §1.199A-2(c)(2)(i))_

**Example:** A MacBook Pro purchased for $3,499 in 2025, placed in service immediately, with a 5-year MACRS recovery period. UBIA = $3,499 for tax years 2025 through 2034 (the 10-year period is longer than the 5-year recovery period, so 10 years controls). Even if 100% bonus depreciation was taken in year 1, the UBIA remains $3,499 for QBI purposes.

### Step 6 — Specified service trade or business (SSTB) rules

- **SSTB definition** — Under IRC §199A(d)(2) and Treas. Reg. §1.199A-5, an SSTB is a trade or business involving the performance of services in the fields of: Health; Law; Accounting; Actuarial science; Performing arts; Consulting (defined narrowly — see below); Athletics; Financial services; Brokerage services; Any trade or business where the principal asset is the reputation or skill of one or more of its employees or owners (narrowed by regulation to mean income from endorsements, licensing of name/likeness/image, and appearance fees); Engineering and architecture were EXCLUDED from the SSTB list by statute (§199A(d)(2) flush language)  _(IRC §199A(d)(2); Treas. Reg. §1.199A-5)_

**Key SSTB determinations for sole props in the target demographic**  _(Treas. Reg. §1.199A-5)_

| Activity | SSTB? | Authority |
| --- | --- | --- |
| Software development | NO | Treas. Reg. §1.199A-5(b)(2)(vii) — not consulting |
| Web development | NO | Same reasoning as software development |
| UX/UI design | NO | Design is not a listed field |
| Graphic design | NO | Design is not a listed field |
| Data science / analytics | NO | Not a listed field; not consulting under the narrow reg definition |
| IT consulting (advisory only, no deliverable) | MAYBE | Treas. Reg. §1.199A-5(b)(2)(vii) — "consulting" means providing advice and counsel, not delivering a work product. If the engagement produces a deliverable (code, report, system), it is NOT consulting for SSTB purposes |
| Marketing consulting | MAYBE | Same analysis — depends on whether the taxpayer provides advice vs. deliverables |
| Financial planning / advisory | YES | Financial services under §199A(d)(2) |
| Legal services | YES | Law under §199A(d)(2) |
| Medical / dental practice | YES | Health under §199A(d)(2) |
| Accounting / bookkeeping services | YES | Accounting under §199A(d)(2) |
| Real estate agent | NO | Not a listed field |

- **The consulting trap** — The regulations define consulting narrowly as "the provision of advice and counsel to clients to assist the client in achieving goals and solving problems." Treas. Reg. §1.199A-5(b)(2)(vii). Importantly, performing services in the field of consulting does NOT include "the performance of services other than advice and counsel, such as sales or the provision of training courses." If a "consultant" actually delivers code, designs, systems, analyses, or other work product, the business is NOT consulting for SSTB purposes.  _(Treas. Reg. §1.199A-5(b)(2)(vii))_

### Step 7 — Compute the deduction

- **Below threshold formula (Form 8995)** — QBI deduction = lesser of: (A) 20% × QBI (B) 20% × (taxable income − net capital gain)  _(IRC §199A(a))_
- **Within phase-in range formula (Form 8995-A)** — The computation requires: 1. Calculate the "reduction amount" for the W-2/UBIA limitation 2. Calculate the "applicable percentage" for SSTB reduction (if SSTB) 3. Apply phase-in percentage to transition from unlimited to limited Phase-in percentage = (taxable income − threshold) / ($50,000 single or $100,000 MFJ, for TY2025) For non-SSTB businesses: - Tentative QBI deduction = 20% × QBI - W-2/UBIA limited amount = greater of 50% × W-2 wages or 25% × W-2 wages + 2.5% × UBIA - Reduction amount = (tentative QBI deduction − W-2/UBIA limited amount) × phase-in percentage - QBI deduction = tentative QBI deduction − reduction amount For SSTB businesses: - Applicable percentage = 1 − phase-in percentage - Adjusted QBI = QBI × applicable percentage - Adjusted W-2 wages = W-2 wages × applicable percentage - Adjusted UBIA = UBIA × applicable percentage - Then apply the non-SSTB formula above using the adjusted figures  _(IRC §199A(b)(3)(B); §199A(d)(3))_
- **Above phase-in range formula (Form 8995-A)** — For non-SSTB: - QBI deduction = lesser of 20% × QBI or W-2/UBIA limited amount For SSTB: - QBI deduction = $0  _(IRC §199A(b)(2); §199A(d)(3))_

### Step 8 — Apply the taxable income cap

- **Taxable income cap** — The final QBI deduction cannot exceed 20% of taxable income (excluding net capital gain). This cap always applies regardless of threshold position.  _(IRC §199A(a)(1)(B))_

### Step 9 — The circular dependency with retirement contributions

- **Circular dependency resolution** — The computation of QBI depends on retirement contributions (which reduce QBI), but some retirement contribution limits depend on net SE earnings which are independent of QBI. However, the QBI deduction affects taxable income, which affects the threshold test, which can change the QBI deduction. For most sole props below the threshold, this circularity is irrelevant — the 20% rate applies regardless. For those near the threshold, the skill must iterate: 1. Compute retirement contributions and SE health insurance first (these depend on net SE earnings, not QBI) 2. Compute QBI = Schedule C net profit − deductible half of SE tax − SE health insurance − retirement contributions 3. Compute the QBI deduction 4. Compute taxable income including the QBI deduction 5. Verify the threshold position — if it changed from step 3's assumption, recompute In practice, for most sole props, a single pass is sufficient because retirement and SE health insurance are fixed once net SE earnings are known.

## Section 6 — Form 8995 (simplified computation)

- **When Form 8995 is used** — Form 8995 is used when: Taxable income is at or below $197,300 (single) / $394,600 (MFJ); The taxpayer has only one trade or business (or does not need aggregation); No SSTB considerations apply (below threshold, SSTB status is irrelevant)  _(Form 8995 Instructions)_

**Form 8995 line-by-line:**

- **Line 1:** Trade, business, or aggregation name and TIN (sole prop = SSN)
- **Line 2:** Qualified business income (QBI) — from the computation in Section 5
- **Line 3:** Total QBI — sum of all lines 2 (typically just one for single-Schedule-C filers)
- **Line 4:** QBI component — if line 3 is positive, multiply by 20%. If negative, enter $0 (loss is carried forward)
- **Line 5:** Qualified REIT dividends and PTP income — $0 for most sole props
- **Line 6:** REIT/PTP component — 20% of line 5
- **Line 7:** Total QBI deduction before income limitation — line 4 + line 6
- **Line 8:** Taxable income before QBI deduction
- **Line 9:** Net capital gain — enter as positive number
- **Line 10:** Line 8 minus line 9
- **Line 11:** Income limitation — 20% of line 10
- **Line 12:** QBI deduction — smaller of line 7 or line 11
- **Line 13:** Total QBI loss carryforward — if line 3 is negative, carry to next year
- **Line 14:** Total REIT/PTP loss carryforward

## Section 7 — Form 8995-A (detailed computation)

- **When Form 8995-A is used** — Form 8995-A is used when: Taxable income exceeds the threshold ($197,300 single / $394,600 MFJ); The taxpayer has an SSTB (regardless of income — though below threshold, Form 8995 may still be used); Multiple trades or businesses require separate computation; Aggregation election under Treas. Reg. §1.199A-4  _(Treas. Reg. §1.199A-4)_

Form 8995-A is substantially more complex. The skill produces the computation worksheet but defers the actual form preparation to the reviewer. Key additional schedules:

- **Schedule A** — SSTB determination for each trade or business
- **Schedule B** — Aggregation of business operations
- **Schedule C** — Loss netting and carryforward
- **Schedule D** — Special rules for patrons of agricultural and horticultural cooperatives

For a single-Schedule-C sole prop above the threshold with a non-SSTB business, the key computation on Form 8995-A is:

1. Report QBI, W-2 wages, and UBIA for the business
2. Compute the W-2/UBIA limitation
3. Apply the phase-in if within the range
4. Apply the taxable income cap

## Section 8 — QBI loss carryover rules

- **QBI loss carryover rules** — Under IRC §199A(c)(2), if QBI from a qualified trade or business is negative (a loss), the loss: 1. Is NOT deductible as part of the QBI deduction in the loss year 2. Is carried forward to the next tax year 3. Reduces QBI from the SAME trade or business in the next year (and subsequent years until absorbed) 4. Is treated as a loss from a separate trade or business in the carryforward year For sole props with a single business: a Schedule C loss year produces zero QBI deduction, and the loss carries forward to reduce QBI in the next profitable year. The carryforward is tracked on Form 8995 line 13 or Form 8995-A Schedule C.  _(IRC §199A(c)(2))_

## Section 9 — Conservative defaults table

**Conservative defaults table**

| Ambiguity | Conservative default |
| --- | --- |
| SSTB status unclear | Assume SSTB (reduces or eliminates deduction above threshold); flag for reviewer |
| Taxable income near the threshold (within $5,000) | Compute both ways (below-threshold simplified and above-threshold detailed); present both to reviewer |
| W-2 wages unclear (did the business have common-law employees?) | Assume $0 W-2 wages (conservative above threshold); ask for clarification |
| UBIA of qualified property not documented | Assume $0 UBIA (conservative above threshold); ask for Form 4562 or asset list |
| Prior-year QBI loss carryover amount not provided | Assume $0 carryover; flag for reviewer to check prior-year Form 8995/8995-A |
| Retirement contributions not yet computed | Compute retirement first, then QBI; do not skip the QBI adjustment |
| SE health insurance deduction not yet computed | Compute SE health insurance first, then QBI; do not skip the QBI adjustment |
| Multiple Schedule Cs | Compute QBI separately for each; do NOT net positive and negative QBI across businesses without applying §199A(c)(2) loss rules |
| Taxpayer has both SE income and W-2 wages from another employer | W-2 wages from another employer are NOT the taxpayer's qualified trade or business's W-2 wages for the §199A(b)(2) limitation |

## Section 10 — Topical refusal catalogue

Refusals on top of the global catalogue in `us-tax-workflow-base` Section 6 and the upstream skills' catalogues.

- **R-QBI-MULTI** — Trigger: The taxpayer has multiple Schedule Cs or K-1s with QBI, and the question of aggregation under Treas. Reg. §1.199A-4 arises. Output: "Aggregation of multiple trades or businesses for QBI purposes under Treas. Reg. §1.199A-4 requires analysis of common ownership, shared facilities, shared employees, and interdependence. This skill computes QBI for a single Schedule C. For multi-business aggregation, please consult a CPA or Enrolled Agent."  _(Treas. Reg. §1.199A-4)_
- **R-QBI-K1** — Trigger: The taxpayer has QBI flowing from a Form K-1 (partnership or S corporation). Output: "QBI from partnerships and S corporations flows through Form K-1 and requires coordination with the entity-level W-2 wage and UBIA reporting. This skill handles sole proprietor QBI only. For K-1 QBI, please consult a CPA or Enrolled Agent."
- **R-QBI-REIT** — Trigger: The taxpayer has qualified REIT dividends or qualified PTP income eligible for the §199A deduction. Output: "Qualified REIT dividends and publicly traded partnership (PTP) income have a separate 20% deduction under §199A(a)(1)(B) with different rules than trade-or-business QBI. This skill does not compute the REIT/PTP component. Please consult a CPA or Enrolled Agent."  _(IRC §199A(a)(1)(B))_
- **R-QBI-NOL** — Trigger: The taxpayer has an NOL carryforward that affects taxable income, which in turn affects the QBI threshold test. Output: "NOL carryforwards reduce taxable income, which can change the QBI threshold position and the taxable income cap on the QBI deduction. NOL-QBI interaction requires careful ordering. Please consult a CPA or Enrolled Agent."
- **R-QBI-SSTB-MIXED** — Trigger: The taxpayer's business has both SSTB and non-SSTB components (e.g., a CPA who also sells software products). Output: "When a business has both SSTB and non-SSTB activities, the de minimis rule under Treas. Reg. §1.199A-5(c)(1) may apply: if gross receipts from the SSTB activity are less than 10% of total gross receipts (or 5% if total gross receipts exceed $25 million), the entire business may be treated as non-SSTB. This requires detailed revenue analysis. Please consult a CPA or Enrolled Agent."  _(Treas. Reg. §1.199A-5(c)(1))_

## Section 11 — Reviewer attention thresholds

**Reviewer attention thresholds**

| Threshold | Trigger | Rationale |
| --- | --- | --- |
| Taxable income within $10,000 of threshold | Always flag | Small changes in income could shift QBI computation dramatically |
| Taxable income above phase-in range top + sole prop has no W-2 wages | Always flag | QBI deduction is likely $0; S-corp election discussion warranted |
| QBI deduction > $15,000 | Always flag | Material deduction; verify all adjustments |
| SSTB classification is ambiguous | Always flag | Wrong classification can eliminate deduction above threshold |
| Business has both consulting and deliverable-based work | Always flag | "Consulting" SSTB classification depends on facts and circumstances |
| Prior-year QBI loss carryover applied | Always flag | Verify against prior-year Form 8995/8995-A |
| QBI is negative (loss year) | Always flag | Carryforward must be tracked |
| Retirement contribution was not subtracted from QBI | Always flag | Overstates QBI and the deduction |
| Taxpayer has multiple businesses | Always flag | Aggregation and loss netting rules apply |

## Section 12 — Worked examples

### Example 1 — Below threshold, non-SSTB sole prop (simplified — Form 8995)

**Taxpayer:** Maria Hernandez, single, freelance UX designer (NOT SSTB), Austin TX.

**Inputs from upstream skills:**
- Schedule C net profit (Line 31): $62,644
- Deductible half of SE tax: $4,427
- SE health insurance deduction: $8,400
- Solo 401(k) employee deferral: $23,500
- Employer contribution: $7,264

**QBI computation:**
```
Schedule C net profit:                $62,644
Less: deductible half of SE tax:     ($4,427)
Less: SE health insurance:           ($8,400)
Less: retirement contributions:      ($30,764)  [$23,500 + $7,264]
                                     --------
QBI:                                  $19,053
```

**Tentative QBI deduction:** 20% × $19,053 = **$3,811**

**Taxable income check:** AGI = $62,644 − $4,427 − $8,400 − $30,764 = $19,053. Taxable income = $19,053 − $15,750 standard deduction (2025, post-OBBBA) = $3,303. Well below the $197,300 threshold. QBI deduction limited to lesser of $3,811 or 20% × $3,303 = $661.

**Result: QBI deduction = $661** (limited by taxable income cap).

**Form:** 8995 (simplified).

### Example 2 — Below threshold, higher income, non-SSTB

**Taxpayer:** James Chen, single, freelance software developer (NOT SSTB), San Francisco.

**Inputs:**
- Schedule C net profit: $150,000
- Deductible half of SE tax: $10,597
- SE health insurance: $9,600
- SEP-IRA contribution: $26,081
- Standard deduction: $15,750 (2025, post-OBBBA)

**QBI computation:**
```
Schedule C net profit:                $150,000
Less: deductible half of SE tax:     ($10,597)
Less: SE health insurance:            ($9,600)
Less: SEP-IRA contribution:          ($26,081)
                                     --------
QBI:                                  $103,722
```

**QBI deduction (tentative):** 20% × $103,722 = $20,744

**Taxable income:** $150,000 − $10,597 − $9,600 − $26,081 − $15,750 = $87,972. Below $197,300.

**Taxable income cap:** 20% × $87,972 = $17,594

**Result: QBI deduction = $17,594** (limited by taxable income cap).

### Example 3 — Above threshold, SSTB, within phase-in

**Taxpayer:** Sarah Kim, MFJ, freelance financial advisor (SSTB — financial services).

**Inputs:**
- Schedule C net profit: $380,000
- Deductible half of SE tax: $16,007
  - Net SE earnings = $380,000 × 92.35% = $350,930
  - OASDI = 12.4% × $176,100 (2025 wage base cap) = $21,836.40
  - Medicare = 2.9% × $350,930 = $10,176.97
  - SE tax = $32,013.37; deductible half = $16,007
- SE health insurance: $14,400
- Solo 401(k) total contributions: $58,000
- Spouse W-2 income: $165,000 (no other income; MFJ standard deduction $31,500)

**Derived taxable income (before QBI):**
```
Total income:        $380,000 + $165,000          = $545,000
Adjustments:         $16,007 + $14,400 + $58,000  = ($88,407)
AGI:                                                $456,593
Standard deduction (MFJ, 2025):                    ($31,500)
Taxable income before QBI:                          $425,093
```

**Analysis:** $425,093 is above the $394,600 MFJ threshold but within the $494,600 phase-in top.

```
Phase-in percentage   = ($425,093 − $394,600) / $100,000 = 30.49%
Applicable percentage = 1 − 30.49%                       = 69.51%

QBI          = $380,000 − $16,007 − $14,400 − $58,000    = $291,593
Adjusted QBI = $291,593 × 69.51%                         = $202,686
Tentative QBI deduction = 20% × $202,686                 = $40,537

Adjusted W-2 wages = $0 × 69.51% = $0 (no employees)
Adjusted UBIA      = $0 (no qualifying property)
W-2/UBIA limited amount                                  = $0

Reduction amount = ($40,537 − $0) × 30.49%               = $12,360
QBI deduction    = $40,537 − $12,360                     = $28,177

Taxable income cap = 20% × $425,093 = $85,019 (not binding)
```

**Result: QBI deduction ≈ $28,177** (Form 8995-A). Note the deduction does NOT vanish in the middle of the phase-in range — it reaches $0 only when taxable income reaches the $494,600 phase-in top (SSTB with no W-2 wages/UBIA). Flag for reviewer — at this income level an S-corp election discussion is warranted.

## Section 13 — Edge cases

1. **QBI is negative.** Schedule C loss or large retirement contributions create negative QBI. Deduction = $0; loss carries forward. Track on Form 8995 line 13 or Form 8995-A Schedule C.

2. **Taxable income is negative.** QBI deduction = $0 (cannot create or increase a loss). The QBI itself still carries forward if negative.

3. **Sole prop has employees (has W-2 wages).** W-2 wages paid to employees count for the §199A(b)(2) limitation, but the sole prop's own draw does NOT. This is unusual for freelancers but possible. Verify with Form 941/944 filings.

4. **Software developer who also provides "consulting."** If the same Schedule C includes both development (deliverable-based, NOT SSTB) and advisory consulting (advice-only, potentially SSTB), the de minimis rule under Treas. Reg. §1.199A-5(c)(1) applies: if SSTB revenue < 10% of total, the entire business is non-SSTB. If ≥ 10%, the skill cannot resolve — flag for reviewer.

5. **Taxpayer exactly at the threshold.** At $197,300 (single) exactly, the simplified computation applies. The phase-in begins at $197,301. Use Form 8995.

6. **Mid-year change in business activity.** If the business changed character mid-year (e.g., from consulting to software product sales), QBI is not split — it is all from the same Schedule C trade or business for the full year. SSTB status is determined based on the overall character for the full year.

7. **Property fully depreciated but within 10-year UBIA window.** The depreciable period for UBIA ends on the LONGER of 10 years from placed-in-service or the regular MACRS (§168(c), GDS) recovery period — determined without regard to ADS (§168(g)). A laptop with a 5-year MACRS recovery period therefore keeps its UBIA for 10 years even though it is fully depreciated. IRC §199A(b)(6)(B); Treas. Reg. §1.199A-2(c)(2)(i).

8. **Married filing separately.** For 2025 the MFS threshold is $197,300 (same as single) and the phase-in range width is $50,000 (also same as single — phase-in completion $247,300 per Rev. Proc. 2024-40). MFS does NOT get a halved phase-in range. The MFS trap is the threshold itself: a high-earning couple filing separately hits the $197,300 threshold at half the joint income level.

9. **Roth IRA and traditional IRA contributions do NOT reduce QBI.** Only retirement deductions attributable to the trade or business (SEP, SIMPLE, Solo 401(k) pre-tax contributions) reduce QBI. Traditional IRA contributions are personal deductions under §219 — deductible from AGI but NOT attributable to the business, so they do not reduce QBI (Form 8995 instructions; Treas. Reg. §1.199A-3(b)(1)(vi)). Roth contributions are after-tax and affect neither.

10. **Community property states.** In community property states (CA, TX, etc.), a sole prop's Schedule C income may be split between spouses for tax purposes. Each spouse reports their share, and QBI follows the income allocation. The skill flags this if the filing status is MFJ and the state is a community property state, but does not perform the split — that is a personal return issue.

## Section 14 — Test suite

### Test 1 — Basic below-threshold computation

**Input:** Schedule C net profit $80,000; deductible half of SE tax $5,652; SE health insurance $6,000; SEP-IRA $13,470; single; standard deduction $15,750 (2025, post-OBBBA); no capital gains.
**Expected:** QBI = $80,000 − $5,652 − $6,000 − $13,470 = $54,878. Tentative QBI deduction = 20% × $54,878 = $10,976. Taxable income = $80,000 − $5,652 − $6,000 − $13,470 − $15,750 = $39,128. TI cap = 20% × $39,128 = $7,826. **QBI deduction = $7,826** (TI-limited). Form 8995.

### Test 2 — Loss year

**Input:** Schedule C net loss ($15,000); deductible half of SE tax $0 (no profit); single.
**Expected:** QBI = ($15,000). QBI deduction = $0. QBI loss carryforward = ($15,000) to next year. Form 8995 line 13.

### Test 3 — Above threshold, non-SSTB, no W-2 wages, no UBIA

**Input:** Schedule C net profit $300,000; deductible half of SE tax $14,935 (= 50% × [12.4% × $176,100 + 2.9% × ($300,000 × 92.35%)] = 50% × [$21,836.40 + $8,034.45]); SE health insurance $12,000; Solo 401(k) $55,000; taxable interest income $7,685; single; standard deduction $15,750.
**Expected:** QBI = $300,000 − $14,935 − $12,000 − $55,000 = $218,065. AGI = $218,065 + $7,685 = $225,750. Taxable income (before QBI) = $225,750 − $15,750 = $210,000 > $197,300. Phase-in % = ($210,000 − $197,300) / $50,000 = 25.4%. Tentative = 20% × $218,065 = $43,613. W-2/UBIA limit = $0. Reduction = ($43,613 − $0) × 25.4% = $11,078. QBI deduction = $43,613 − $11,078 = $32,535. TI cap = 20% × $210,000 = $42,000 (not binding). **QBI deduction = $32,535**. Form 8995-A.

### Test 4 — SSTB fully above phase-in range

**Input:** Schedule C net profit $350,000 (accounting firm); single; taxable income (before QBI) $260,000.
**Expected:** $260,000 > $247,300 (phase-in top). SSTB = accounting (yes). **QBI deduction = $0**. Form 8995-A.

### Test 5 — Below threshold, SSTB irrelevant

**Input:** Schedule C net profit $100,000 (legal consulting — SSTB); deductible half SE tax $7,065; SE health insurance $7,200; Solo 401(k) $30,000; single; standard deduction $15,750; no other income.
**Expected:** QBI = $100,000 − $7,065 − $7,200 − $30,000 = $55,735. Taxable income = $55,735 − $15,750 = $39,985 < $197,300. SSTB status irrelevant below threshold. Tentative = 20% × $55,735 = $11,147. TI cap = 20% × $39,985 = $7,997. **QBI deduction = $7,997** (TI-limited). Form 8995.

### Test 6 — Taxable income cap binds

**Input:** Schedule C net profit $50,000; no retirement; no SE health insurance; deductible half SE tax $3,532; single; itemizes with $30,000 deductions (mortgage interest + SALT + charitable; exceeds the $15,750 standard deduction).
**Expected:** QBI = $50,000 − $3,532 = $46,468. Tentative = 20% × $46,468 = $9,294. Taxable income = $50,000 − $3,532 − $30,000 = $16,468. TI cap = 20% × $16,468 = $3,294. **QBI deduction = $3,294** (TI-limited). Form 8995.

## Section 15 — PROHIBITIONS

- **Prohibition 1** — NEVER compute the QBI deduction without first subtracting deductible half of SE tax, SE health insurance, and retirement contributions from Schedule C net profit. Skipping any of these adjustments overstates QBI and the deduction.
- **Prohibition 2** — NEVER apply a 23% §199A rate for ANY tax year. The 23% rate appeared only in the House-passed version of H.R. 1 (May 2025). The enacted One Big Beautiful Bill Act (P.L. 119-21) kept the rate at 20% and made it permanent. The rate is 20% for 2025, 2026, and all later years unless Congress acts again.  _(P.L. 119-21)_
- **Prohibition 3** — NEVER tell a taxpayer their SSTB status does not matter without checking their taxable income. SSTB status is irrelevant below the threshold but critical above it.
- **Prohibition 4** — NEVER treat the sole proprietor's own draw or self-employment income as W-2 wages for the §199A(b)(2) limitation. Only wages paid to common-law employees count.  _(§199A(b)(2))_
- **Prohibition 5** — NEVER assume UBIA is zero without asking. A sole prop who purchased equipment, vehicles, or other depreciable property may have significant UBIA even if the property is fully depreciated (the 10-year lookback applies).
- **Prohibition 6** — NEVER net QBI losses across multiple businesses without applying the §199A(c)(2) ordering rules. Losses from one business reduce QBI from other businesses proportionally — they do not simply offset dollar-for-dollar.  _(§199A(c)(2))_
- **Prohibition 7** — NEVER apply the QBI deduction to reduce self-employment tax. The QBI deduction reduces income tax only (it is below the AGI line). It does not affect Schedule SE.
- **Prohibition 8** — NEVER ignore the taxable income cap. Even when 20% of QBI is large, the deduction cannot exceed 20% of taxable income excluding net capital gain.
- **Prohibition 9** — NEVER file Form 8995 when Form 8995-A is required. If taxable income exceeds the threshold, Form 8995-A must be used.
- **Prohibition 10** — NEVER classify software development as an SSTB. Software development is not consulting, not engineering (excluded from SSTB by statute), and not any other listed field. This is confirmed by Treas. Reg. §1.199A-5(b)(2)(vii).  _(Treas. Reg. §1.199A-5(b)(2)(vii))_
- **Prohibition 11** — NEVER apply the 2026+ OBBBA changes (wider $75,000/$150,000 phase-in ranges, $400 minimum deduction) to a tax year 2025 return. They are effective only for tax years beginning after December 31, 2025.

## Section 16 — Cross-skill references

**Upstream skills**

| Upstream skill | Data consumed |
| --- | --- |
| `us-sole-prop-bookkeeping` | Classified transactions for Schedule C |
| `us-schedule-c-and-se-computation` | Schedule C Line 31 (net profit), deductible half of SE tax |
| `us-self-employed-health-insurance` | SE health insurance deduction amount |
| `us-self-employed-retirement` | Retirement contribution deduction amount |

**Downstream skills**

| Downstream skill | Data provided |
| --- | --- |
| `us-quarterly-estimated-tax` | QBI deduction amount (reduces estimated tax liability) |
| `us-federal-return-assembly` | QBI deduction for Form 1040 Line 13 |
| `us-federal-tx-return-assembly` | QBI deduction for Texas-resident federal return |
| `us-ca-return-assembly` | QBI deduction for CA-resident federal return |

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

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
