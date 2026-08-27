---
name: us-pte-state-matrix
description: Tier 2 US federal-level reference skill providing the comprehensive state-by-state matrix of Pass-Through Entity Tax (PTET) elections under the SALT-cap workaround blessed by IRS Notice 2020-75 and codified state-by-state from 2021 onward. Covers election deadlines, rates, eligibility, owner-credit refundability, estimated-tax requirements, and resident-credit interactions for the 35+ states that have enacted PTET regimes. Includes a 5-step decision framework for electing PTET and common-trap callouts for CA, NY, GA, NC, IL, MN, VA. Tax year 2025 under OBBBA.
jurisdiction: US
tax_year: 2025
last_updated: 2026-07-13
reviewed_by: James Wallach
review_status: current
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# US PTE State Matrix

## 1. Scope

This is a **reference skill**, not a procedural skill. Practitioners consult it to answer questions of the form:

- "Does state X have a PTET regime?"
- "What is the PTET rate in state X, and is it flat or graduated?"
- "When is the election deadline?"
- "Is electing PTET worth it for my client?"
- "If my client's home state is A and the PTE files PTET in state B, will A grant a resident credit?"

It does **not** itself execute a PTET filing — actual return preparation is delegated to the appropriate state-specific skill (e.g., `us-ca-540-individual-return`, `us-ny-it-204-pte`, etc., where they exist) or handled by the credentialed reviewer.

**In scope:**
- The 35 US states (plus DC) that have enacted PTET regimes through tax year 2025.
- Federal SALT-cap interaction under IRC §164(b)(6) as modified by OBBBA (P.L. 119-21, July 4, 2025).
- Owner-level credit treatment, refundability, and resident-credit interaction.
- Decision framework for whether to elect.
- Common traps that void elections or destroy the federal benefit.

**Out of scope:**
- Detailed line-by-line PTET return preparation (see state-specific skills).
- Composite return vs. PTET trade-off analysis where PTET is unavailable (separate skill).
- C-corp state tax (PTET is by definition a pass-through regime).
- Trust and estate PTET treatment (most states limit PTET to S-corps and partnerships; trust treatment varies and is reviewer-driven).
- US territories (PR, GU, VI, MP, AS).

**Assumes:** a human reviewer credentialed under Circular 230 (EA, CPA, or attorney) reviews and signs off on any election recommendation before it reaches the taxpayer.

## 2. Background — The SALT Cap and Notice 2020-75

### 2.1 The §164(b)(6) cap

- **TCJA SALT cap under §164(b)(6)** — The Tax Cuts and Jobs Act of 2017 added IRC §164(b)(6), which limits an individual's federal itemized deduction for state and local taxes (income, property, sales) to $10,000 per return ($5,000 MFS) for tax years 2018 through 2025.  _(IRC §164(b)(6))_
- **SALT cap amount pre-OBBBA** — $10,000 USD (per return, 2018-2025; $5,000 MFS)  _(IRC §164(b)(6))_
- **OBBBA SALT cap increase** — The One Big Beautiful Bill Act (P.L. 119-21, enacted July 4, 2025) raised the cap to $40,000 for tax years 2025 through 2029, with a phase-down for high-income taxpayers (MAGI above $500,000, phasing back to $10,000 over a $100,000 range), and a 1% annual inflation adjustment. The cap returns to $10,000 in 2030 absent further legislation.  _(P.L. 119-21 (OBBBA), enacted July 4, 2025)_
- **PTET relevance under OBBBA** — For 2025, OBBBA's $40,000 cap means a typical owner with $250,000 of personal state income tax exposure still leaves $210,000+ of state tax outside the deduction. PTET remains highly relevant under OBBBA — it is not obsolete.  _(P.L. 119-21 (OBBBA))_

### 2.2 IRS Notice 2020-75

- **IRS Notice 2020-75 blessing of PTET workaround** — On November 9, 2020, the IRS released Notice 2020-75, in which Treasury announced its intent to issue proposed regulations confirming that: - A state-imposed income tax assessed on, and paid by, a partnership or S-corporation is deductible by the entity in computing non-separately-stated income. - The deduction is not subject to the §164(b)(6) SALT cap because the cap applies only to individuals. - This treatment applies whether the state tax is mandatory or elective, provided the entity is the legal taxpayer. This blessed what had been a contested workaround pioneered by Connecticut (effective 2018) and Wisconsin (effective 2018), and triggered a wave of state enactments. 35 states plus DC had enacted PTET regimes by 2025.  _(IRS Notice 2020-75)_
- **Structural mechanic of PTET workaround** — 1. The PTE elects PTET. The state taxes the PTE's apportioned income at the PTET rate. 2. The PTE deducts the PTET as a §162 business expense (state income tax of the entity, not §164 individual SALT). 3. Owners receive a credit on their state personal return for their share of PTET paid (most states), or an exclusion of PTET-taxed income from their state personal return (a few states, e.g., LA pre-2024). 4. Federal AGI is reduced by the PTET deduction at the entity level, flowing through K-1 Line 1. 5. Federal SALT cap is bypassed for the portion of state tax converted to PTET.  _(IRS Notice 2020-75)_

### 2.3 OBBBA technical changes

- **OBBBA changes relevant to PTET planning** — OBBBA made three changes relevant to PTET planning: 1. SALT cap raised to $40,000 (2025-2029) with phase-down above $500k MAGI. 2. §199A QBI made permanent at 20%, rising to 20% in 2026. PTET reduces QBI (because PTET reduces ordinary income flowing through K-1 Line 1), so the QBI deduction is reduced by 20% (or 20% in 2026) of the PTET deduction — netting the PTET federal benefit. 3. No direct PTET changes — Treasury has not retracted Notice 2020-75, and OBBBA did not codify or restrict the workaround. PTET remains an administrative blessing, not a statutory one.  _(P.L. 119-21 (OBBBA))_

## 3. PTET State Matrix

**PTET State Matrix**  _(See per-state statute citations within table)_

| State | Statute | Eff Yr | Entities | Rate | Election Deadline | NR Benefit | Refundable | Est. Tax | RC Interaction | Notable Quirks |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **AL** | Code §40-18-24.4 | 2021 | B | 5.0% flat | By the original due date of the return (Mar 15 / Apr 15) | Y | C (5-yr) | Y — 4/15, 6/15, 9/15, 12/15 | Y (post-2022 AL DOR ruling) | Election is irrevocable for the year once made. Estimates required if PTET liability > $500. |
| **AR** | Act 362 of 2021, Ark. Code §26-65 | 2022 | B | 4.4% (2025, reduced from 4.7% in 2024) | Due date of return incl. extensions | Y | Y | Y — same as corp | Y | Rate ties to top individual rate, which is phasing down toward 3.9%. |
| **AZ** | A.R.S. §43-1014 | 2022 | B | 2.5% flat (post-2023 flat-tax conversion) | Due date of return | Y | Y | Y — 4/15, 6/15, 9/15, 1/15 | Y | Pre-2023 rate was 4.5%; 2023+ rate matches the AZ flat individual rate. |
| **CA** | R&TC §§17052.10, 19900-19906 | 2021 | B (S-corp + partnership; **NOT** SMLLC disregarded entities — must be multi-member) | 9.3% flat | **Two-prong: (1) prepayment by June 15 of the election year, equal to the GREATER of $1,000 or 50% of prior-year PTET; (2) final election by the original return due date (Mar 15).** Miss June 15 prepayment = election VOID. | N (NR partners get no CA credit) | C (5-yr carryforward, then refundable per AB 150 amendment) | N (the June 15 prepayment IS the estimate) | Y, but **CA does not grant a resident credit for PTET paid to other states** under R&TC §18001 unless the other state grants reciprocal credit (see Common Trap #1) | Owner must affirmatively consent on a per-owner basis (Form 3804 attaches owner list). Owner-by-owner election. Sunsets after 2025 — must be reauthorized; AB 150 was scheduled to sunset 12/31/2025 and 2024 extender legislation pushed it to 12/31/2026. |
| **CO** | C.R.S. §39-22-340 | 2022 (retroactive to 2018 — unique) | B | 4.40% (2024+ rate; was 4.55% in 2022-23) | Due date of return | Y | Y | Y — 4/15, 6/15, 9/15, 1/15 | Y | CO uniquely allows **retroactive election back to 2018** under the 2022 enactment — practitioners filed amended PTE returns for 2018-2021 to claim refunds. Retroactive window closed in 2023. |
| **CT** | Conn. Gen. Stat. §12-699 | **2018** (first in the nation) | B | 6.99% flat | **MANDATORY through 2023; ELECTIVE starting 2024** | Y | Y (resident); C (NR) | Y — 4/15, 6/15, 9/15, 1/15 | Y | CT was the only state with a **mandatory** PTET (2018-2023). Switched to elective for 2024+. Owner credit = 87.5% of PTET paid (reduced from 93.01% in pre-2024 mandatory regime). |
| **DC** | D.C. Code §47-1808.10 | Proposed — **NOT YET ENACTED as of 2025** | — | — | — | — | — | — | — | DC has discussed PTET but has not enacted. DC residents cannot use DC PTET; they remain subject to the SALT cap on DC income tax. |
| **GA** | O.C.G.A. §48-7-23 | 2022 | B | **5.39% (2024); 5.19% (2025); phasing to 4.99% by 2028** | Due date of return | Y | C | Y (above $500 threshold) | Y | Rate phase-down tracks GA individual rate reduction (HB 1437 of 2022). Election applies to all owners — no opt-out. |
| **HI** | HRS §235-51.5 | 2023 | B | 11.0% (top rate) graduated | Due date of return | Y | Y | Y | Y | HI uses the top individual rate. Graduated brackets from 1.4% to 11.0%, but most PTET payers hit 11%. |
| **ID** | Idaho Code §63-3026B | 2021 | B | 5.695% flat (2024+; was 5.8% 2022-23) | Due date of return incl. extensions | Y | Y | Y | Y | Rate ties to ID flat individual rate (post-2023). |
| **IL** | 35 ILCS 5/201(p) | 2021 | B | 4.95% flat | Due date of return incl. extensions | Y | Y | Y — 4/15, 6/15, 9/15, 12/15 | Y | **PTET does NOT exempt the PTE from the 1.5% Personal Property Replacement Tax (PPRT) for partnerships or the 2.5% PPRT for S-corps** — these are still owed and not creditable at owner level. PPRT is a separate, parallel tax. |
| **IN** | Ind. Code §6-3-2.1 | 2022 (retroactive to 2022 under SEA 2 of 2023) | B | 3.0% flat (2025; was 3.15% in 2023-24) | Due date of return | Y | Y | Y | Y | Rate ties to IN flat individual rate; phasing down to 2.9% by 2027. |
| **IA** | Iowa Code §422.16C | 2022 (retroactive — election available for 2022 by Apr 30, 2023 only) | B | **6.0% flat (2025); phasing to 3.9% flat by 2026** | Due date of return | Y | Y | Y | Y | Rate phase-down tracks IA individual rate consolidation. |
| **KS** | K.S.A. §79-32,287 | 2022 | B | 5.7% flat (top KS individual rate) | Due date of return | Y | C (10-yr) | Y | Y | Election binds all owners; no individual opt-out. |
| **KY** | KRS §141.209 | 2022 (retroactive to 2022 under HB 360 of 2023) | B | 4.0% flat (2025; was 4.5% in 2024, 5.0% in 2023) | Due date of return incl. extensions | Y | Y | Y | Y | Rate phase-down tracks KY individual rate (HB 8 of 2022). |
| **LA** | La. R.S. §47:287.732.2 | 2019 (one of the earliest) | B | **Graduated: 1.85% / 3.5% / 4.25%** — matches LA individual brackets | Due date of return | N (pre-2024); Y (post-2024 under Act 413 of 2023) | N — owner **excludes** PTET-taxed income rather than taking a credit | Y | N/A — exclusion model | LA uses an **exclusion model**, not a credit model — owners exclude the income from their LA personal return rather than claiming a credit. Federal benefit identical; state mechanics different. |
| **MD** | Md. Tax-Gen. §10-102.1 | 2020 | B | 8.0% flat (resident-allocable portion); 5.75% (NR-allocable portion + corporate-owner portion at 8.25%) | Due date of return | Y | Y | Y — 4/15, 6/15, 9/15, 12/15 | Y | MD splits the rate by owner type. Originally mandatory for some entities pre-2021; now fully elective. |
| **MA** | M.G.L. ch. 63D | 2021 | B | 5.0% flat | Due date of return incl. extensions | Y | Y | Y — 4/15, 6/15, 9/15, 1/15 | Y | Owner credit = 90% of PTET (10% haircut — a quirk of the MA design). |
| **MI** | MCL 206.815 | 2021 (retroactive to 2021 under PA 135 of 2021) | B | 4.25% flat | Due date of return; **irrevocable for 3 years once made** | Y | Y | Y — 4/15, 6/15, 9/15, 1/15 | Y | **3-year binding election** — once elected, cannot revoke for 3 tax years. Unusual lock-in. |
| **MN** | Minn. Stat. §289A.08 subd. 7a | 2021 | B | **9.85% flat (top MN individual rate)** | Due date of return | Y | Y | Y | Y | **Tax-haven inclusion** — MN's combined-reporting rules include tax-haven jurisdictions, which can complicate PTET base computation for multistate PTEs with foreign operations (see Common Trap #5). |
| **MS** | Miss. Code §27-7-26 | 2022 (retroactive) | B | 4.4% flat (2025; was 5.0% in 2022, 4.7% in 2023, 4.4% in 2024) | Due date of return | Y | Y | Y | Y | Rate phase-down tracks MS individual rate (HB 531 of 2022). |
| **MO** | RSMo §143.436 | 2022 | B | 4.7% flat (2025; was 4.95% in 2023, 4.8% in 2024) | Due date of return | Y | Y | Y | Y | Rate phase-down tracks MO individual rate. |
| **MT** | MCA §15-30-3312 | 2023 | B | 6.75% flat (2024+; was higher pre-2024 individual top rate consolidation) | Due date of return | Y | Y | Y | Y | Late-adopter — first effective year was 2023. |
| **NE** | Neb. Rev. Stat. §77-2734.03 | **2018 (retroactive — enacted 2023, election available for 2018-2022 by filing amended)** | B | 5.84% flat (2024+; phasing down) | Due date of return | Y | Y | Y | Y | NE allowed retroactive elections for 2018-2022 under LB 754 (2023) — practitioners filed amended PTE returns to claim refunds for those years. Window closed in 2024. |
| **NJ** | N.J.S.A. §54A:12-1 et seq. (BAIT — Business Alternative Income Tax) | 2020 | B | **Graduated: 5.675% / 6.52% / 9.12% / 10.9%** | Due date of return — **but election made via filing PTE-100, not a separate form** | Y | Y | Y — 4/15, 6/15, 9/15, 1/15 | Y | Known as **"BAIT"** rather than PTET in NJ-speak. Top rate is **10.9%** — highest in the nation among PTET states. Owner credit refundable but **not transferable** to other returns. |
| **NM** | NMSA §7-3A-9 | 2022 (retroactive to 2022) | B | 5.9% flat (top NM individual rate) | Due date of return | Y | Y | Y | Y | Late adopter; straightforward design. |
| **NY** | N.Y. Tax Law Art. 24-A (§§860-866) | 2021 | B | **Graduated: 6.85% / 9.65% / 10.30% / 10.90%** (NYS); plus **separate NYC PTET at 3.876%** for NYC residents | **March 15** for both NYS and NYC PTET (election due 6 weeks earlier than CA) — **separate forms, separate elections** | N (NR partners get no NY credit — see quirks) | Y | Y — 3/15, 6/15, 9/15, 12/15 | Y | **TWO separate PTETs**: NYS PTET and NYC PTET. Both elections due March 15 of the **tax year being elected** (not the return year — so election for 2025 was due March 15, 2025). **Quarterly estimates due 3/15, 6/15, 9/15, 12/15** (note the March, not April, first estimate). NR partners do NOT get a NY resident credit, so PTET for NR partners is wasted unless NR partner's home state grants RC for NY PTET. |
| **NC** | N.C.G.S. §105-154.1 | 2022 | B | **4.5% (2025); phasing to 3.99% by 2026, then to 2.49% by 2030** | Due date of return | Y | C | Y | Y | Rate phase-down tracks NC individual rate consolidation (the most aggressive in the country). |
| **OH** | ORC §5747.38 | 2022 (retroactive to 2022) | B | **3.0% (2025); phasing from 5.0% in 2022, 3.0% in 2023+** | Due date of return incl. extensions | Y | Y | Y — 4/15, 6/15, 9/15, 1/15 | Y | Rate dropped sharply post-2022. OH PTET is generally beneficial because OH individual top rate is also low (3.5% in 2025). |
| **OK** | 68 O.S. §2355.1P-4 | 2019 (one of the earliest) | B | 4.75% flat | Due date of return | Y | C | Y | Y | OK was an early adopter (2019, alongside RI and CT). Election binds owners. |
| **OR** | ORS §316.043 | 2022 | B | **9.0% (first $250k of distributive share) / 9.9% (above)** | **April 15** of the tax year — **election due before the year ends, not at return time** (this is the unusual prepay model) | Y | Y | Y — 4/15, 6/15, 9/15, 1/15 | Y | OR is the only state where the election is due **April 15 of the tax year itself** (so election for 2025 was due April 15, 2025) — earlier than NY's March 15 of the year. Combined with the prepay requirement, OR is administratively the most demanding. |
| **RI** | R.I. Gen. Laws §44-11-2.3 | 2019 | B | 5.99% flat | Due date of return incl. extensions | Y | Y | Y | Y | Early adopter; rate matches RI top individual rate. |
| **SC** | S.C. Code §12-6-545 | 2021 | B | **3.0% (2025); phasing from 7.0% in 2021, 6.4% in 2024, 6.2% in 2025 individual rate, but PTET rate matches the SC "active trade or business" income rate at 3.0% currently** | Due date of return | Y | Y | Y | Y | SC PTET uses the **3.0% "active trade or business" rate** rather than the regular individual top rate — quirky and beneficial. Phase-down tracks ATB income rate reductions. |
| **UT** | Utah Code §59-10-1402.5 | 2022 | B | 4.55% flat (2025; was 4.65% in 2024, 4.85% in 2022-23) | Due date of return | Y | Y | Y | Y | Rate phase-down tracks UT flat individual rate. |
| **VA** | Va. Code §58.1-390.1 et seq. | 2021 (retroactive to 2021 under HB 1121 of 2022) | B (**but only "qualifying PTEs" — see quirks**) | 5.75% flat | Due date of return incl. extensions | Y | Y | Y | Y | **VA PTET is only available to "qualifying PTEs"** — entities where **100% of owners are natural persons (or other PTEs whose ultimate owners are natural persons) eligible to claim the VA owner credit**. A single C-corp owner or ineligible owner disqualifies the entire PTE. See Common Trap #4. |
| **WI** | Wis. Stat. §71.21(6) | **2018** (S-corp only initially; partnerships added 2019 under Wis. Stat. §71.21(7)) | B (S-corp 2018+, partnership 2019+) | 7.9% flat (S-corp); 7.9% (partnership) | Due date of return incl. extensions; **all shareholders must consent in writing** | Y | Y | Y | Y | One of the first two PTET states (alongside CT). 100% shareholder consent required. |
| **WV** | W. Va. Code §11-21-3a | 2022 | B | 6.5% flat (matches WV top individual rate pre-2023; rate has changed with WV individual rate reductions) | Due date of return | Y | Y | Y | Y | Late adopter; rate tracks WV individual rate phase-down. |

### 3.1 Summary statistics

- **35 states + DC considered, 35 states with active PTET** as of tax year 2025 (DC has not enacted).
- **Earliest adopters (2018):** CT (mandatory), WI.
- **Latest adopters (2023):** HI, MT.
- **Highest top rate:** NJ at 10.9%.
- **Lowest rate:** IN, OH at 3.0%; AZ at 2.5%.
- **Most administratively demanding:** CA (June 15 prepayment trap) and OR (April 15 election deadline within the tax year itself).

## 4. States WITHOUT PTET

**States WITHOUT PTET**  _(See per-state reasons within table)_

| State | Reason | PTET planning impact |
| --- | --- | --- |
| **AK** | No state personal income tax (PIT) | PTET moot — no SALT cap exposure on AK income. |
| **DE** | Has PIT but no PTET enacted | DE residents/PTEs cannot bypass SALT cap on DE income; rely on the $40k SALT cap. |
| **FL** | No PIT | PTET moot. |
| **ME** | Has PIT but no PTET enacted | ME residents/PTEs cannot bypass SALT cap on ME income. |
| **NV** | No PIT | PTET moot. |
| **NH** | No PIT on wages/SE income (only interest/dividends, which are not PTET-eligible) | PTET moot for most owners. |
| **ND** | Has PIT (low rate) but no PTET enacted | ND PIT top rate is 2.5% (post-2023) — low enough that PTET workaround offers minimal benefit even if enacted. |
| **PA** | Has 3.07% flat PIT but no PTET enacted (despite repeated proposals — PA has historically resisted) | PA owners face full SALT cap on PA tax. PA-resident owners in other-state PTEs **do not get a PA resident credit for PTET paid to other states** under most readings (state-level dispute ongoing). See Common Trap #6. |
| **SD** | No PIT | PTET moot. |
| **TN** | No PIT (Hall income tax repealed 2021) | PTET moot. |
| **TX** | No PIT (but Texas Franchise Tax exists at entity level — separately, not a PTET) | PTET moot at state level; TX-resident owners in other-state PTEs may still benefit federally (see Worked Example 3). |
| **VT** | Has PIT but no PTET enacted as of 2025 (VT considered legislation in 2023-24 but did not pass) | VT residents/PTEs cannot bypass SALT cap on VT income. |
| **WA** | No PIT on wages (but capital gains tax at 7% post-2022 — narrow base) | PTET moot for most owners. |
| **WY** | No PIT | PTET moot. |

## 4. States WITHOUT PTET

**Note:** Eight states have no broad-based PIT (AK, FL, NV, NH, SD, TN, TX, WA, WY — nine including WA's narrow CG tax). For these, PTET planning is moot **at the state level** but may still be relevant for owners who are non-residents of these states earning income in PTET states (see Worked Example 3).

## 5. Decision Framework — Should the PTE Elect PTET?

A five-step go/no-go analysis. The reviewer answers each question; a "no" at any step may kill the election but does not always — proceed to the next step to confirm.

### Step 1 — Is the owner over the $10k/$40k SALT cap before considering state income tax on PTE income?

- **Step 1 SALT cap test** — **Test:** Compute the owner's other SALT (property tax + state PIT on W-2 wages + sales tax if elected) **before** layering on the state PIT attributable to the PTE share. If the owner's other SALT already exceeds $40,000 (for 2025-2029) or $10,000 (for 2030+), then **100% of the PTET-eligible state tax is cap-bypassed by election**. - **YES, over cap** → PTET adds incremental federal benefit. Proceed to Step 2. - **NO, under cap** → Marginal benefit only. Quantify the marginal benefit before recommending. PTET still saves the SALT cap difference but the cost-benefit may be marginal.

### Step 2 — Does the entity have predictable, taxable, state-tax-paying owners?

- **Step 2 owner mix test** — PTET works at the entity level but the federal benefit accrues to owners. If the owner mix includes: - C-corps (no individual SALT cap exposure — C-corp PTET share generally wasted) - Tax-exempt entities (no tax at owner level — PTET share wasted unless refundable) - Trusts with low distribution income (trust SALT cap is also $10k/$40k but trust marginal rates differ) - Foreign owners (state credit may be unusable) then the entity-level PTET benefit may be partially wasted. **Rule of thumb:** if >20% of distributive share goes to non-individual or non-cap-affected owners, model the wasted portion explicitly.

### Step 3 — Will the home state grant a resident credit for PTET paid to other state(s)?

- **Step 3 resident credit test** — If owner is a resident of state A and PTE files PTET in state B, owner needs state A to grant a resident credit (RC) for the share of PTET paid to state B. Without RC, the owner pays state A tax on the income twice (once via PTET to B, once via personal tax to A). - **Most states grant RC.** The matrix's "RC Interaction" column is the quick reference. - **CA is the major exception** — CA generally does NOT grant a resident credit to CA residents for PTET paid to other states under R&TC §18001, unless the other state grants reciprocal credit to non-resident CA owners. This makes CA residents who are partners in other-state PTEs **particularly vulnerable to double taxation** if the other state doesn't reciprocate. - **PA is also problematic** — PA's RC rules under 61 Pa. Code §111.5 have been read narrowly; PA-resident owners in NY PTET-paying PTEs have litigated this and lost. Get state-specific guidance.  _(R&TC §18001; 61 Pa. Code §111.5)_

### Step 4 — Does the entity have non-resident owners who'd otherwise face composite-return or NR withholding requirements?

- **Step 4 NR withholding test** — Some states (e.g., NY, NJ, MA, CA) require PTEs to either: - File a composite return on behalf of NR owners, or - Withhold tax from distributions to NR owners. PTET can **replace** the composite/withholding mechanism, simplifying state administration for NR owners. In some states (CO, MD), the PTET is administratively a successor to the older composite/withholding regime. - **Many NR owners** → PTET is administratively beneficial regardless of federal SALT consideration. - **Few NR owners** → No administrative benefit; focus on federal SALT cap math.

### Step 5 — Are the estimated-tax cash flows manageable?

- **Step 5 cash flow test** — Most PTET states require quarterly estimates. Cash flow at the entity level shifts: the entity now pays state tax that previously the owners paid individually. The entity needs cash on the quarterly estimate dates. **Owner-level cash flow:** owners receive a credit (or exclusion) but pay no individual state tax on PTET-taxed income. Net cash impact at owner level is small; net cash impact at entity level is large. If the entity lacks working capital to fund quarterly state estimates, PTET becomes a financing problem, not a tax problem.

### Output of decision framework

- **Elect / Decline / Marginal output rules** — **ELECT** if Steps 1, 3, 5 are favorable AND Step 2 shows >80% of share goes to cap-affected individuals. **DECLINE** if Step 1 is no AND no Step 4 administrative benefit; OR if Step 3 fails (home state denies RC) AND owner mix is heavily home-state residents. **MARGINAL — REVIEWER JUDGMENT** otherwise.

## 6. Common Traps by State

### 6.1 CA — The June 15 Prepayment Trap

- **CA June 15 prepayment requirement and void-on-miss rule** — **Trap:** California requires a prepayment by **June 15 of the election year** equal to the greater of: - $1,000, OR - 50% of the prior-year PTET liability. **If the prepayment is missed or short by even $1, the election is VOID for the entire year.** No cure provision. The FTB has been strict on this. **Practitioner action:** - Calendar June 15 every year for every CA PTET client. - For first-year PTE elections (no prior-year PTET), the $1,000 minimum prepayment applies. - Pay via Form FTB 3893 — separate voucher. - Document the wire/check date carefully; FTB has voided elections for payments dated June 16.

### 6.2 NY — Two Separate PTETs and the March 15 Deadline Within the Tax Year

- **NY dual PTET regimes and March 15 deadline** — **Trap:** NY has **two separate PTET regimes**: 1. **NYS PTET** (state-level) — election due March 15 of the tax year being elected (so election for 2026 is due March 15, 2026). 2. **NYC PTET** (city-level, for NYC residents) — election also due March 15 of the tax year, but on a different form. Both are made via the NY Tax Department's online portal. **Missing either deadline is fatal** — no cure provision. Owners of NYC-resident PTEs who only file NYS election miss the NYC benefit entirely. **Practitioner action:** - Calendar **two** March 15 deadlines for NY clients (the year of election, not the return year). - For NYC-resident owners in PTEs, file BOTH elections. - Quarterly estimates due **March 15, June 15, September 15, December 15** (note: March, not April, first estimate).

### 6.3 GA, NC, SC — Phase-Down Rates

- **GA/NC/SC phase-down rates shrinking PTET benefit** — **Trap:** GA, NC, and SC are aggressively phasing down individual income tax rates. The PTET rate generally tracks the top individual rate (except SC, which uses the special "active trade or business" rate). As individual rates fall, the PTET federal benefit shrinks. - GA: 5.39% (2024) → 4.99% (2028) - NC: 4.5% (2025) → 2.49% (2030) - SC: PTET at 3.0% (matches ATB income rate) **Practitioner action:** - Quantify break-even: at what PTET rate does the federal SALT benefit equal the administrative cost (form fees, return prep, quarterly estimates)? - For NC particularly, by 2028-2030 the federal benefit may be marginal — re-run the decision framework annually.

### 6.4 IL — PPRT Carve-Out

- **IL PPRT not bypassed by PTET** — **Trap:** Illinois has both: 1. **Personal Income Tax (PIT)** at 4.95%, which PTET bypasses, AND 2. **Personal Property Replacement Tax (PPRT)** at 1.5% for partnerships and 2.5% for S-corps, which is a **separate entity-level tax that is NOT bypassed by PTET** and is **not creditable at the owner level**. PPRT is owed regardless of PTET election. It is a federally deductible §164 entity tax (so deducts at entity level) but does not flow through as a credit. **Practitioner action:** - Model both: PTET (4.95%) + PPRT (1.5% or 2.5%) for total IL entity-level tax of 6.45% (partnership) or 7.45% (S-corp). - Owners get credit only for the 4.95% PTET portion.

### 6.5 MN — Tax-Haven Inclusion in Combined Return

- **MN tax-haven inclusion complicating PTET base** — **Trap:** Minnesota's worldwide combined-reporting framework includes tax-haven jurisdictions in the combined group. For multistate or multinational PTEs electing MN PTET, the PTET base may include income apportioned from tax-haven entities, increasing the PTET liability beyond what a separate-entity analysis would suggest. **Practitioner action:** - For PTEs with foreign or tax-haven operations, model MN PTET base including the tax-haven inclusion. - Consider whether the increased PTET base offsets the federal benefit.

### 6.6 VA — "Qualifying PTE" Requirement

- **VA qualifying PTE ownership requirement** — **Trap:** Virginia PTET is only available to **"qualifying PTEs"** — defined as entities where **100% of owners are natural persons or other qualifying PTEs whose ultimate owners are natural persons**. A single C-corp owner, single-member LLC disregarded entity owned by a C-corp, or any ineligible owner **disqualifies the entire PTE**. There is no partial-PTET regime for qualifying portion only. **Practitioner action:** - Audit the owner schedule before electing. - For PTEs with mixed individual + C-corp owners, VA PTET is unavailable — consider restructuring (e.g., C-corp owner sells to individuals).

### 6.7 PA — No Resident Credit for Other-State PTET (Disputed)

- **PA denial of resident credit for other-state PTET** — **Trap:** Pennsylvania does not grant a resident credit to PA-resident individuals for PTET paid by a PTE to another state. PA has historically taken the position that PTET is an entity tax, not an individual tax, and is therefore not creditable under PA's RC framework (61 Pa. Code §111.5). PA-resident owners of out-of-state PTEs that elect PTET may face **double taxation** at the state level (PTET to the other state + PA personal tax on the same income with no credit). **Practitioner action:** - For PA-resident owners in NY, NJ, MD, or other PTET states, **decline the PTET election** unless the federal benefit clearly outweighs the lost PA RC. - This issue has been litigated (no resolution as of 2025); track legislative developments.  _(61 Pa. Code §111.5)_

## 7. Worked Examples

### 7.1 Example 1 — CA-resident S-corp owner with $500,000 distributive share

**Facts:**
- Owner: CA resident, MFJ, $500,000 net S-corp income, $50,000 W-2 from another job, $20,000 property tax, $0 sales tax election.
- S-corp: 100% owned by individual, in CA only.
- CA PTET rate: 9.3% flat.
- CA individual top rate (post-MHST): 13.3% (above $1M); 9.3% in the $349k-$418k bracket; 10.3% above.

**Without PTET (2025, OBBBA $40k SALT cap):**
- CA state tax on $500k: approx. $42,000 (after standard deductions and using actual brackets).
- Other SALT: $20k property + $4,500 CA tax on $50k wages = $24,500 already counted in CA tax of $42k? No — wait, CA tax on TOTAL CA AGI of $550k = approximately $50,500 (top brackets engaged).
- Federal SALT deduction: capped at $40,000.
- Federal deduction lost: $50,500 + $20,000 = $70,500 actual SALT, capped at $40,000 → **$30,500 of SALT is non-deductible**.

**With PTET (S-corp elects):**
- S-corp pays CA PTET on $500k at 9.3% = $46,500.
- S-corp deducts $46,500 as §162 entity tax → owner's K-1 Line 1 is reduced by $46,500.
- Owner's federal AGI is $46,500 lower.
- Owner gets CA credit of $46,500 against CA personal tax, so CA personal tax on the $500k is wiped out.
- Owner still owes CA tax on $50k W-2 (approximately $3,000-$4,000) + property tax $20,000 = approx. $24,000 SALT.
- Federal SALT cap of $40,000 now covers all $24,000 of remaining SALT → no SALT loss.
- Plus federal AGI reduction of $46,500 saves federal tax at owner's marginal federal rate (approx. 35% in 2025 for $500k income MFJ) = **$16,275 federal tax savings**.
- Minus QBI deduction reduction: $46,500 × 20% = $9,300 less QBI deduction; federal cost = $9,300 × 35% = $3,255.
- **Net federal benefit: $16,275 − $3,255 = $13,020.**

Compare to without-PTET scenario: $30,500 of SALT non-deductible × 35% federal rate = $10,675 federal cost. By electing PTET, owner saves the $10,675 SALT-cap loss plus gains an additional $2,345 from AGI reduction beyond the cap — total economic benefit roughly $13,020.

**Decision:** ELECT, and calendar June 15 prepayment of greater of $1,000 or 50% of 2024 PTET liability.

### 7.2 Example 2 — NY-resident partners in a multi-state partnership (NY, NJ, CT)

**Facts:**
- Partnership: 60% activity in NY, 25% in NJ, 15% in CT. All four partners are NY residents.
- Partnership net income: $1,000,000.
- Each partner: 25% share = $250,000.

**Analysis:**
- NY PTET: rate up to 10.90% on the $600k NY-source income → $65,400 NYS PTET.
- NJ BAIT: rate up to 10.9% on the $250k NJ-source income → approx. $25,500 (at 10.9% top rate).
- CT PTET: 6.99% flat on the $150k CT-source income → $10,485.
- Total PTET paid: $101,385.
- Each partner's K-1 reduced by $25,346.
- Federal AGI reduction × 37% federal rate (top bracket for $250k+ MFJ on a millionaire household) = $9,378 federal tax savings per partner.
- Each partner gets:
  - NYS resident credit for NJ + CT PTET portion (since NY grants RC for other-state PTET — see matrix).
  - NYS PTET credit on NY personal return for the NYS PTET share.
- Net federal benefit per partner: approx. $9,000-$10,000 after QBI haircut.

**Election deadlines:**
- NYS PTET: March 15 of the tax year (e.g., March 15, 2026 for 2026 tax year).
- NJ BAIT: due date of PTE return.
- CT PTET: due date of return (CT is elective post-2024).

**Trap:** All three quarterly estimate schedules differ slightly. NY uses 3/15, 6/15, 9/15, 12/15. NJ uses 4/15, 6/15, 9/15, 1/15. CT uses 4/15, 6/15, 9/15, 1/15. The first NY estimate is **March 15**, easy to miss.

**Decision:** ELECT all three. Significant federal benefit. Calendar all three election deadlines and four × three = twelve estimate dates per year.

### 7.3 Example 3 — TX-resident partner in IL S-corp

**Facts:**
- TX-resident individual owns 50% of an IL S-corp.
- IL S-corp net income: $400,000. 100% IL-source.
- TX has no PIT. IL has 4.95% PIT.

**Without PTET:**
- IL S-corp's IL income tax: 0% at entity (S-corps pay only PPRT in IL, no IL income tax at entity level; income passes to shareholders).
- TX shareholder owes IL non-resident PIT on $200k share at 4.95% = $9,900.
- TX shareholder cannot deduct $9,900 of IL tax on TX return (no TX PIT).
- Federal SALT deduction: limited to $40k cap (2025) — counts the $9,900 of IL tax + property tax + sales tax (TX has high sales tax). Likely already over the $40k cap from sales tax + property tax + IL nonres tax.
- **$9,900 of IL nonres tax is fully SALT-capped at federal level — minimal deduction.**

**With PTET (IL S-corp elects):**
- IL S-corp pays IL PTET at 4.95% on $400k = $19,800.
- IL S-corp deducts $19,800 as §162 entity expense.
- Each shareholder's K-1 Line 1 reduced by $9,900.
- TX shareholder gets:
  - IL credit on IL non-resident return for $9,900 of PTET share → IL nonres tax owed = $0.
  - **TX has no PIT, so no TX resident credit needed.**
  - Federal AGI reduced by $9,900 → federal tax savings at 35% marginal rate = $3,465.
  - Minus QBI reduction at 20% × $9,900 × 35% = $693.
  - **Net federal benefit: $3,465 − $693 = $2,772.**

**Plus the IL PPRT** (2.5% for S-corp partnerships) of $400k × 2.5% = $10,000 is still owed and is a separate IL entity tax (not PTET, not bypassed).

**Decision:** ELECT. TX shareholder benefits federally from PTET even though no home-state RC is needed (because TX has no PIT). This is the classic "no-PIT home state" pattern — PTET in the source state always works federally regardless of home-state RC mechanics, because the SALT cap bypass operates at federal level.

**Key insight:** Practitioners sometimes assume PTET only benefits residents of high-tax states. The federal SALT bypass works for ANY US owner of a PTE in a PTET state, regardless of the owner's home-state tax regime. The home-state RC analysis is about avoiding double **state** tax, not about federal benefit.

## 8. Filing Deadline Calendar (Chronological)

This is a calendar of PTET-related dates throughout a typical year, for a PTE on calendar tax year. **Actual dates shift to next business day if on a weekend/holiday.**

### January

- **Jan 15** — Q4 prior-year estimates due: AZ, CO, MA, MI, NJ, OH, OR (all state PTET Q4).
- **Jan 15** — Form 1099-NEC/1096 due to recipients and IRS for prior-year contractor payments (not PTET-specific but federal calendar item).
- **Jan 31** — W-2/W-3 due. State withholding annual reconciliations begin to fall due.

### February

No major PTET deadlines.

### March

- **March 15** — Federal Form 1065 / 1120-S due (calendar-year PTEs).
- **March 15** — **NYS PTET election due** for the tax year now starting (e.g., March 15, 2026 = election for 2026 tax year).
- **March 15** — **NYC PTET election due** for the tax year.
- **March 15** — NYS PTET Q1 estimate due.
- **March 15** — CA Form 100S (S-corp) or Form 565/568 (partnership) due — also the deadline to make CA PTET election for the prior tax year (along with required June 15 prepayment that was already made).

### April

- **April 15** — Federal Form 1040 due.
- **April 15** — **OR PTET election due** for the tax year being elected (so April 15, 2026 = election for 2026 tax year).
- **April 15** — Q1 estimates due: AL, AZ, CO, IL, MA, MD, MI, NJ, OH, OR (Q1 PTET estimates for the current tax year).
- **April 15** — Many states' annual income tax returns due (individual and PTE alike).

### May

No major PTET deadlines.

### June

- **June 15** — **CA PTET prepayment deadline** (greater of $1,000 or 50% of prior-year PTET) — **missing this voids the CA election**.
- **June 15** — Q2 estimates due: AL, AZ, CO, IL, MA, MD, MI, NJ, NY (NYS and NYC), OH, OR.

### July

No major PTET deadlines.

### August

No major PTET deadlines.

### September

- **Sept 15** — Federal Form 1065 / 1120-S due (with extension) for calendar-year PTEs.
- **Sept 15** — Q3 estimates due: AL, AZ, CO, IL, MA, MD, MI, NJ, NY (NYS and NYC), OH, OR.
- **Sept 15** — Final NY PTET prior-year return (if extended).

### October

- **Oct 15** — Federal Form 1040 due (with extension).
- **Oct 15** — Final CA PTET return (Form 3804) for prior tax year if extended.

### November

No major PTET deadlines.

### December

- **Dec 15** — Q4 estimates due: AL, IL, MD, NY (NYS and NYC).

### Year-end alerts to set for clients

- Calendar reminder for CA: **June 15 prepayment** (high consequence if missed).
- Calendar reminder for NY: **March 15 PTET election** (high consequence if missed; election can't be made retroactively).
- Calendar reminder for OR: **April 15 election within the tax year** (highest-consequence in terms of how early it falls).
- Calendar reminder for all states with Q4 in January (AZ, CO, MA, MI, NJ, OH, OR): year-end cash needs to be ready.

## 9. Provenance

This skill is compiled from:

1. **Federal authority:**
   - IRC §164(b)(6) as amended by the Tax Cuts and Jobs Act (P.L. 115-97, 2017).
   - IRC §164(b)(6) as further amended by the One Big Beautiful Bill Act (P.L. 119-21, July 4, 2025).
   - IRS Notice 2020-75 (Nov. 9, 2020) — Treasury intent to issue proposed regs blessing PTET deductibility at the entity level.
   - IRC §199A (QBI deduction) as made permanent by OBBBA, relevant to net federal benefit calculation.

2. **State authority** — each row of the matrix in Section 3 includes the state statute citation. These were current as of November 2025 based on enacted state legislation and DOR guidance. Rates and phase-down schedules are checked against:
   - State revenue department PTET guidance pages.
   - State tax notice/bulletin publications.
   - State legislative session summaries (2024 and 2025 sessions).

3. **Practitioner sources** — the common-trap callouts (Section 6) reflect issues documented in:
   - AICPA Tax Section's "State PTE Tax" comparison chart (updated quarterly).
   - State CPA society publications (especially CalCPA on the June 15 trap, NYSSCPA on the dual NYS/NYC elections, VSCPA on the qualifying-PTE rule).
   - Published guidance from major accounting firms tracking state PTET enactments.

### Reviewer responsibilities

This skill is a **reference**, not a substitute for credentialed review. Before relying on any matrix entry:
- Confirm the state's current-year rate (rates are phasing down in many states — check the DOR website).
- Confirm the election deadline against the current-year calendar (deadlines shift for weekends/holidays).
- Confirm the owner-mix qualifies (VA "qualifying PTE" rule, owner consent requirements in WI, irrevocability lock-in in MI).
- Run the full decision framework (Section 5) for each client; do not rely on the matrix alone.
- For multi-state PTEs, coordinate the analysis across all source states AND each owner's home state.

### Update cadence

This skill should be reviewed:
- **Annually** after each state's spring legislative session (typically July-September of each year), to catch rate changes and new enactments.
- **In real time** when OBBBA-related federal guidance is issued (e.g., if Treasury issues final §164 regs that affect PTET treatment).
- **Before each March 15 / April 15 / June 15** to confirm no client-specific deadlines are missed.

### Confidence

- **High confidence:** existence of PTET in each state listed, base statutory rate, basic election mechanics.
- **Medium confidence:** exact 2025 rate after phase-downs (rates change frequently in GA, NC, SC, IA, KY, MO, OH, MS, NE, IN, UT).
- **Lower confidence:** edge-case mechanics like MN tax-haven inclusion, IL PPRT interaction with PTET base, PA non-recognition of other-state PTET for resident credit (litigated, unsettled).

Where confidence is low, the matrix flags it explicitly. For low-confidence determinations, the reviewer should consult the relevant state DOR directly and document the position taken in the client file.

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
