---
name: us-r-and-d-section-174-and-41
description: Tier 2 US federal content skill for the §174 mandatory R&E capitalization regime (TCJA, eff. 1/1/2022, 5-year domestic / 15-year foreign amortization, half-year convention) and the §41 R&D Credit (Regular Credit 20% / Alternative Simplified Credit 14%, four-part test, contract research at 65%, IUS software hurdle), including the §41(h) payroll tax credit election for Qualified Small Businesses (< $5M gross, no prior receipts beyond Immediate expensing unless §174A(c) amortization election is made) — increased to $500k by IRA 2022 — applied against Form 941 via Form 8974. Tax year 2025 (§174 capitalization remains law absent year-end extender). Federal only.
jurisdiction: US
domain: federal-tax
tax_year: 2025
tier: 2
last_updated: 2026-07-06
---

# us-r-and-d-section-174-and-41

## 0. Scope and Loading Contract

This skill is a **Tier 2 US federal content skill** that supplies the legal content, mechanics, computations, and reviewer-facing brief language for two **interrelated** federal regimes:

1. **IRC §174 — Specified Research or Experimental (SRE) Expenditures** (as amended by the Tax Cuts and Jobs Act of 2017, P.L. 115-97, with mandatory capitalization effective for amounts paid or incurred in taxable years beginning after December 31, 2021).
2. **IRC §41 — Credit for Increasing Research Activities** (the "R&D Credit"), including the **§41(h) payroll tax credit election** for Qualified Small Businesses.

**Loading contract.** This skill MUST be loaded alongside `us-tax-workflow-base` v0.2 or later. It is frequently loaded together with:

- `us-sole-prop-bookkeeping` (Schedule C source data — to identify QREs and §174 SRE costs out of expense classifications).
- `us-schedule-c-and-se-computation` (to integrate §174 amortization into Schedule C bottom line and the resulting §1402 net SE earnings).
- `us-federal-return-assembly` (the orchestrator pulls Form 6765, Form 8974, and the §174 amortization schedule into the final 1040 package).
- `us-s-corp-election-decision` (R&D credit and §174 capitalization materially change the S-corp vs. sole-prop break-even — both regimes survive the entity choice but the credit utilization differs).
- State skills where applicable (most states do not conform to TCJA §174 — see Section 10 on state non-conformity callouts; California is the largest carve-out via `ca-540-individual-return`).

**Out of scope for this skill.**

- §41(c)(4) special rules for **acquisitions and dispositions** of a trade or business (the "gross receipts apportionment" on a mid-year acquisition).
- §41(e) **basic research payments** for **corporations** other than at the modeling layer (we summarize the 75% mechanic; we refuse if the corporation has a base-period basic research floor that requires §41(e)(7) computation against the 1984-88 fixed-base).
- §1.41-4A historic election to deduct under former §174(b) for taxable years beginning before 1/1/2022 — pre-TCJA returns are out of scope. We do not amend pre-2022 returns through this skill.
- §168(k) bonus depreciation interaction with §174 amortization (different recovery system — §174 amortization is not §168 property; FLAG if the reviewer asks about combining them).
- §174(d) **disposition, retirement, or abandonment** rules in detail — we summarize the prohibition on accelerated deduction (must continue amortization even if the project is abandoned) but refuse complex disposition modeling.
- Foreign §174 stewardship cost allocation under §861 / Treas. Reg. §1.861-17 — relevant for multinational taxpayers, out of scope for sole-prop / SMLLC clients.
- Section 280C(c) state-conformity matrix beyond California (we cite the general rule; verify state-by-state at the state skill layer).

**Year-specific anchor.** All rates, thresholds, and form line references in this skill are as of **November 15, 2025**. If a year-end extender package amends §174 retroactively for 2025 (see Section 3.6 on the political status), the reviewer MUST re-check before filing season opens.

## 1. The Two-Regime Frame — Why §174 and §41 Are Discussed Together

**§174 vs §41 comparison table**

| Dimension | §174 (R&E Capitalization) | §41 (R&D Credit) |
| --- | --- | --- |
| **Nature** | Timing rule for **deduction** of R&E expenditures | **Tax credit** for qualified research expenditures |
| **Effect** | Defers deduction over 5 or 1Immediate expensing unless §174A(c) amortization election is made instead of immediate expense | Reduces tax liability dollar-for-dollar (subject to §280C and §38) |
| **Scope** | **Broader** — all R&E in connection with the trade or business | **Narrower** — must meet the four-part test of §41(d) |
| **Mandatory or elective** | **Mandatory** capitalization since 1/1/2022 (TCJA) | Elective (§41(h) for QSBs, §280C(c) reduced credit) |
| **Software development** | All software dev costs are §174 per §174(c)(3) | Software qualifies but **internal-use software** (IUS) has the high hurdle of innovation test |
| **Contractor R&D** | Capitalized at 100% of cost incurred | QRE counted at **65%** of contract amount (75% for qualified research consortia) |
| **Foreign R&D** | Capitalized over **1Immediate expensing unless §174A(c) amortization election is made** | **Excluded** entirely from QRE — no §41 credit for foreign research |
| **Form** | Schedule M-1/M-3 reconciliation + amortization schedule | Form 6765 (+ Form 8974 if §41(h) payroll election) |

- **§174 as prerequisite to QRE** — Per §174(a) and the IRS's reading of §41(d)(1)(A), a §174 expenditure is a prerequisite to being a QRE. The four-part test of §41(d) explicitly incorporates §174 as its first prong. Every QRE is also §174 SRE. Not every §174 SRE is a QRE (the §174 universe is much larger). The same dollar of qualifying research wages is both capitalized over Immediate expensing unless §174A(c) amortization election is made under §174 and counted (at 100% for wages) toward the §41 credit base in the year incurred. This dual treatment is not double-counting and is not a §280C(c) issue — it is the explicit design of the post-TCJA regime. The taxpayer suffers the §174 capitalization deferral and also receives the §41 credit; the credit does, however, trigger a §280C(c) wage-addback unless the reduced-credit election is made (see Section 6).  _(§174(a); §41(d)(1)(A))_

§174 and §41 are not the same thing, but the same dollar of payroll, contractor cost, supply cost, or overhead can be subject to both regimes simultaneously and the analyst MUST keep the two computations separate.

### 2.1 Pre-TCJA versus Post-TCJA

**Before 1/1/2022** (under former §174(a)–(b)):

- Taxpayers had three permissible methods: (1) immediate **expense** under §174(a); (2) **defer and amortize** over not less than 60 months under former §174(b); or (3) elective **10-year amortization** under §59(e).
- The default in practice was immediate expensing — every dollar of qualifying R&E reduced taxable income in the year paid or incurred.

**On and after 1/1/2022** (the TCJA amendment, codified at current §174):

- Immediate expensing is **eliminated**.
- All Specified Research or Experimental expenditures must be **capitalized** and **amortized** ratably:
  - **Immediate expensing unless §174A(c) amortization election is made** if the SRE is conducted **inside the United States** (domestic SRE).
  - **1Immediate expensing unless §174A(c) amortization election is made** if the SRE is conducted **outside the United States** (foreign SRE).
- The amortization period begins with the **midpoint of the taxable year** in which the expenditure is paid or incurred — i.e., a **half-year convention** applies in year 1. (Statutorily this is the "ratable" amortization beginning at the midpoint per §174(a)(2)(B).)

### 2.2 The Half-Year Convention — Mechanics

- **Domestic 5-year half-year convention example ($100,000)** — Year 1 (2025): half of 1/5 of the cost = $10,000 (i.e., 6 months of straight-line over a 60-month period). Years 2–5 (2026, 2027, 2028, 2029): full annual amortization = $20,000 each = $80,000 cumulative. Year 6 (2030): the remaining $10,000 (the back-half catch-up from the half-year start). Cumulative deduction by end of year 6: $100,000. Six tax years are required for a 5-year domestic SRE pool because the amortization straddles the midpoint convention.  _(§174(a)(2)(B))_
- **Foreign 15-year half-year convention example ($100,000)** — Year 1 (2025): $100,000 / 15 × 0.5 = $3,333. Years 2–15: $100,000 / 15 = $6,667 per year (×14 years = $93,333). Year 16 (2040): remaining $3,333 catch-up. Total recovery period: 16 tax years for foreign SRE.  _(§174(a)(2)(B))_

### 2.3 What Qualifies as §174 SRE — Broad by Design

- **SRE definition and included items** — Per §174(b) and the legislative history of TCJA (Conference Report H.R. Rep. No. 115-466), SRE means research or experimental expenditures that are paid or incurred in connection with the taxpayer's trade or business. The §174 universe is intentionally broader than the §41 QRE universe. Included as §174 SRE (capitalize over 5/1Immediate expensing unless §174A(c) amortization election is made): W-2 wages and salaries of employees engaged in research or experimentation; self-employment compensation of the owner where the owner performs SRE (allocable share); independent contractor and consultant payments for R&E services; supplies and materials consumed in the research process (cloud compute, prototyping materials, lab consumables); rent and depreciation allocable to facilities used in R&E (but not the underlying building cost — see Section 2.5); overhead — utilities, IT support, software licenses used in R&E — allocable share; software development costs specifically — see §174(c)(3) below; patent costs incidental to research (attorneys' fees for filing, drafting, prosecution); failed projects and abandoned research — still capitalized over the full 5/1Immediate expensing unless §174A(c) amortization election is made even after abandonment (§174(d)).  _(§174(b); H.R. Rep. No. 115-466)_
- **§174(c)(3) software-development bombshell** — TCJA added §174(c)(3), which provides: "For purposes of this section, any amount paid or incurred in connection with the development of any software shall be treated as a research or experimental expenditure." This sweeps in all software development costs, including: internal-use software (custom CRM, internal tooling, back-office automation); dual-function software (some internal, some customer-facing); software developed for sale or licensing (a SaaS company's product code); minor improvements and bug fixes — the statute does not carve out "minor" from "major" enhancements; software written by full-time employees, contractors, or both. This is the provision that hit small SaaS companies hardest in the 2022 filing season — a company with $2M of engineering payroll and no other "R&D" was nonetheless required to capitalize that $2M and could only deduct $200,000 in 2022 (half of one-fifth). The cash-tax shock was severe and is the principal political driver of the repeal-bill activity (Section 3.6).  _(§174(c)(3))_

### 2.4 Domestic vs. Foreign — The Site-of-Performance Test

- **Site-of-performance test** — The 5-year vs. 15-year split turns on where the research is performed, not where the taxpayer is domiciled. Domestic SRE (Immediate expensing unless §174A(c) amortization election is made): research performed within the United States, including its possessions and territories per §7701(a)(9) and §7701(a)(30). Foreign SRE (1Immediate expensing unless §174A(c) amortization election is made): research performed anywhere else. For a US sole proprietor with a remote engineering team: engineer working from California: domestic SRE. Contractor working from Ukraine: foreign SRE. Engineer who travels to Berlin for two months mid-project: the portion of compensation reasonably allocable to the German-performed work is foreign SRE. Documentation: the taxpayer must maintain records (time logs, timesheets, location of contractor signing entity) to support the domestic/foreign split. Where the split is not separately tracked, the IRS will accept a reasonable proration based on payroll records and worksite information.  _(§7701(a)(9); §7701(a)(30))_

### 2.5 What Is NOT §174 SRE

- **Exclusions from §174 SRE** — Land, buildings, and other §168 depreciable property — capitalized under §263 and depreciated under §168, not §174. Cost of acquiring another person's patent, model, production, or process (§174(c)(2) — purchased IP is §197 intangible, not §174). Routine quality control testing (not "research" — already commercial production). Market research, advertising, and promotional expenses (excluded by Treas. Reg. §1.174-2(a)(6); deductible under §162). Efficiency surveys, management studies, consumer surveys (excluded under §41(d)(4) and analogously under §174). Research after commercial production has begun — but careful, the §174 line is drawn differently from the §41 line; see Section 5.3.  _(§263; §168; §174(c)(2); Treas. Reg. §1.174-2(a)(6); §162; §41(d)(4))_

### 2.6 §174(d) — No Acceleration on Abandonment

- **No acceleration on abandonment** — If the taxpayer abandons, disposes of, or retires the research project before the 5/15-year period elapses, the unamortized balance does NOT accelerate. It continues to amortize on the original schedule. This is a substantial departure from the pre-TCJA rule (where former §174(a) allowed an immediate write-off on abandonment) and is the source of much practitioner unhappiness. The capitalized balance is essentially a frozen tax asset. This rule has a practical consequence: when a SaaS company kills a product line, foreign R&E and legacy capitalized SRE balances may continue to amortize under §174. There is no automatic §165 loss just because the project was abandoned; analyze the current §174/§174A transition rules before accelerating any deduction.  _(§174(d))_

### 3.1 Identifying the R&E Pool

**Schedule C expense category treatment**

| Expense category (Schedule C line) | Treatment |
| --- | --- |
| Wages — engineering (Line 26) | Domestic R&E is currently deductible under §174A(a) for post-2024 tax years unless amortization is elected |
| Contract labor — engineers/contractors (Line 11) | Same treatment if the scope is software development or qualified research |
| Contract labor — non-R&E (sales, admin, ops) | Not R&E |
| Office expense / rent / utilities allocable to R&E | Allocable R&E support cost; document methodology |
| Depreciation on R&E-use equipment (Line 13) | Not R&E; recovered under §168 |
| Foreign R&E labor or contractors | Still capitalized and amortized over 15 years under §174 |

Step 1 is still identifying the dollars that constitute research or experimental expenditures for the year. For a freelance software developer or small SaaS company, the typical sources are shown in the table. A reasonable defensive position for a small SaaS company is to identify 100% of engineering payroll and direct contractor R&E costs, plus a defensible overhead allocation. The key 2025 question is no longer whether domestic R&E creates a new five-year pool; it is whether the cost is domestic §174A current-deduction R&E, elected §174A(c) amortization, foreign §174 amortization, or a legacy 2022–2024 transition balance.

### 3.2 The Schedule C / 1040 Mechanics

- **Schedule C / 1040 mechanics steps** — For a sole proprietor or single-member LLC disregarded for federal tax: 1. Domestic R&E paid or incurred in 2025 is generally deducted currently under §174A(a), unless the taxpayer elects §174A(c) amortization over at least 60 months. 2. Foreign R&E remains capitalized and amortized over 15 years using the half-year convention. 3. Legacy domestic SRE pools from 2022–2024 should be tracked separately under Rev. Proc. 2025-28 transition procedures. Remaining unamortized domestic balances may generally be recovered in 2025 or ratably over 2025–2026, depending on the taxpayer's election/method-change posture. 4. The workpaper should separate current §174A domestic deductions, legacy domestic transition deductions, elected §174A(c) amortization, and foreign §174 amortization.  _(§174A(a); §174A(c); Rev. Proc. 2025-28)_

Domestic R&E paid in 2025:                         $200,000
Current §174A(a) deduction:                       ($200,000)

Legacy 2024 domestic SRE pool originally capitalized: $150,000
Less 2024 year-1 amortization previously deducted:    ($15,000)
Remaining legacy domestic balance:                    $135,000
2025 transition deduction if 2-year recovery elected:  $67,500

Foreign R&E paid in 2025:                            $90,000
2025 foreign §174 amortization:                        $3,000
  = $90,000 / 15 × 1/2 half-year convention

### 3.3 Multi-Year Recovery Stack — Worked Example

**Multi-year recovery stack — Alpha LLC**

| Year | Legacy 2022–2024 domestic SRE | Post-2024 domestic R&E | Foreign R&E |
| --- | --- | --- | --- |
| 2025 | Recover remaining domestic balance in 2025 or ratably over 2025–2026 under transition procedures | Current §174A(a) deduction unless §174A(c) amortization elected | 15-year §174 amortization |
| 2026 | Remaining elected transition share, if any | Current §174A(a) deduction unless §174A(c) amortization elected | 15-year §174 amortization |

Suppose Alpha LLC (sole-member, calendar-year) has pre-OBBBA domestic SRE pools from 2022–2024 and pays new domestic R&E in 2025. Do not create a new five-year domestic amortization pool for 2025 domestic R&E unless the taxpayer affirmatively elects §174A(c) amortization. Foreign R&E remains a separate 15-year pool.

### 3.4 Domestic + Foreign Mixed Pool — Worked Example

- **Beta LLC mixed pool computation** — Beta LLC has $500,000 of 2025 R&E: $400,000 domestic + $100,000 foreign. Domestic 2025 R&E: $400,000 current deduction under §174A(a), unless §174A(c) amortization is elected. Foreign 2025 R&E: $100,000 / 15 × 1/2 = $3,333 deduction in 2025. Combined 2025 deduction: $403,333 against $500,000 paid, before considering any legacy domestic transition deductions. The foreign-pool deferral remains severe — a $100,000 contractor outside the United States in 2025 yields $3,333 of 2025 deduction and amortizes over 16 calendar years total. This is a strong tax reason to identify where R&E is performed, subject to non-tax business considerations.  _(§174A(a))_

### 3.5 The §174(d) "Abandonment Trap" — Worked Example

Gamma LLC capitalized $1,000,000 of SRE in 2024 for Product A. In mid-2025 Gamma kills Product A and pivots to Product B. The $1,000,000 pool continues to amortize: 2025 deduction: $200,000 (full year-2 amortization). 2026 deduction: $200,000. 2027 deduction: $200,000. 2028 deduction: $200,000. 2029 deduction: $100,000 (back-half catch-up). There is no acceleration, no §165 loss, no §197 abandonment. The $1M sits as a tax-amortization asset on Gamma's books regardless of whether the underlying code is ever used again.

### 3.6 The Repeal Debate — Where Things Stand as of November 15, 2025

§174 capitalization was sold to Congress in 2017 as a revenue offset for the broader TCJA package and was scheduled to take effect 1/1/2022 with the expectation that Congress would repeal or defer it before the effective date. That repeal did not happen in 2021, and §174 capitalization went live for tax year 2022. Since then:

- **Tax Relief for American Families and Workers Act of 2024** (H.R. 7024): bipartisan package including retroactive §174 repeal for domestic R&E from 2022 forward. Passed the House 357-70 on January 31, 2024. **Failed in the Senate** (cloture vote 48-44 on August 1, 2024).
- **Wyden-Crapo framework (2024)**: precursor bipartisan deal that became H.R. 7024. Same fate.
- **One Big Beautiful Bill Act (OBBBA), P.L. 119-21**, enacted July 4, 2025: the omnibus tax-and-spending bill of the 119th Congress. **Did NOT include §174 repeal in the final enacted text** despite multiple drafts circulating that did include it. Several provisions affecting depreciation, §199A, and the SALT cap were enacted; §174 was left intact.
- **Year-end extender prospects (Nov 2025)**: practitioner press has reported active negotiations on a small "tax technical corrections + extenders" package. §174 repeal is a candidate but is **NOT enacted as of November 15, 2025**.

**Posture for 2025 returns.** §174 capitalization remains the law for tax year 2025. Prepare returns on the capitalization assumption. If Congress passes retroactive repeal between mid-November 2025 and the April 2026 filing deadline, the analyst MUST:

1. Re-pull the §174 amortization stack and reverse the capitalization back to immediate expense.
2. Check whether the legislation provides automatic accounting-method-change consent (typically yes for catch-up adjustments).
3. Compute the §481(a) catch-up adjustment for prior-year pools.
4. Re-run §41 — the credit itself is generally unaffected by §174 repeal because §41 stands on its own and the §174 prerequisite remains met (immediate-expense §174 still satisfies the §41 first-prong test).
5. Re-run state returns since many states are decoupled from §174 already (California in particular has its own §17260 conformity tracking).

**Reviewer flag.** Every reviewer brief for a 2025 return with material §174 capitalization MUST contain a watch-item callout for the year-end extender package.

### 4.1 The Initial Method Change for 2022

- **Initial 2022 method change** — For taxpayers' first §174-capitalization year (tax year 2022 for calendar-year taxpayers), the IRS issued Rev. Proc. 2023-8 (later superseded by Rev. Proc. 2023-11) granting automatic consent under §446(e) to change accounting method to comply with the new §174 rules. The change was a §481(a) cut-off transition (no §481(a) catch-up for pre-2022 expensed amounts — those stay deducted) and required filing Form 3115 in duplicate (original with the return, copy to Ogden).  _(Rev. Proc. 2023-8; Rev. Proc. 2023-11; §446(e); §481(a))_

### 4.2 Rev. Proc. 2024-9 — The Current Procedural Framework

- **Rev. Proc. 2024-9 framework** — Rev. Proc. 2024-9 (issued in late 2023, applicable to tax years 2024 forward) continues the automatic-consent framework for ongoing §174 method matters: Change DCN (designated change number) 265 — adoption or change of method to comply with §174 as amended. DCN 357 — change in the treatment of software development costs to conform to §174(c)(3). Cut-off transition for the initial adoption year; §481(a) adjustment for subsequent changes in scope (e.g., a taxpayer who failed to capitalize software dev costs in 2022 and now amends or files a change to bring them in). Audit protection under the automatic-consent framework is generally provided as long as the change is implemented on a timely-filed return (including extensions) for the year of change.  _(Rev. Proc. 2024-9)_

### 4.3 Late or Missed Method Changes — The Practitioner Cleanup Problem

- **Cleanup for improperly expensed 2022-2024 §174 costs** — Many small businesses missed the 2022 method change because they (a) did not know about §174 capitalization, (b) lacked the workpaper sophistication to identify SRE expenditures, or (c) received bookkeeper-prepared returns that simply continued the pre-TCJA expense treatment. For a 2025-filing-season taxpayer who improperly expensed 2022, 2023, and 2024 §174 costs: File Form 3115 with the 2025 return using DCN 265. Compute a §481(a) adjustment equal to the cumulative excess deductions (improperly expensed amounts net of properly-allowed amortization) as a positive (taxable) adjustment spread over four years (or one year if elected). The catch-up income is reported on Schedule C as "§481(a) adjustment from method change" — Line 6 "Other income" or via Line 27a as a negative deduction with memo. No penalty typically applies if the original returns were prepared in good faith on reasonable practitioner advice, but interest accrues on the deferred tax. This cleanup is a meaningful practitioner offering for 2025 — many small SaaS clients are still mis-reporting.  _(DCN 265; §481(a))_

### 4.4 What This Skill Does NOT Do

This skill does not draft the Form 3115 itself for §174 method changes. It identifies the need for the change, computes the §481(a) adjustment, and flags the issue for the reviewer to prepare or supervise Form 3115. Form 3115 preparation is a separate workproduct.

### 5.1 Overview of the Two Credit Computations

- **Regular Credit and ASC definitions** — §41 offers two alternative computations for the credit: 1. Regular Credit (RC) — §41(a)(1): 20% × (current-year QREs − fixed-base percentage × average gross receipts of 4 preceding years). 2. Alternative Simplified Credit (ASC) — §41(c)(5): 14% × (current-year QREs − 50% × average QREs of 3 preceding years). If the taxpayer had no QREs in any of the 3 prior years, the ASC rate is 6% of current-year QREs (no base subtraction). Most taxpayers elect the ASC because the Regular Credit requires reconstructing the 1984-1988 fixed-base period (gross receipts and QREs from that period) — data that virtually no modern small business has retained. The ASC was introduced in 2007 precisely to spare taxpayers this archeology. The ASC election is annual and made on Form 6765, Section B. It cannot be revoked for that year once made on a timely-filed return (including extensions).  _(§41(a)(1); §41(c)(5))_
- **Regular Credit rate** — 20%  _(§41(a)(1))_
- **Alternative Simplified Credit (ASC) rate** — 14%  _(§41(c)(5))_
- **ASC no-base alternative rate (no QREs in any of 3 prior years)** — 6%  _(§41(c)(5))_

### 5.2 The Four-Part Test — §41(d)

- **Four-part test overview** — A research activity is "qualified research" (and its expenditures are QREs) only if it satisfies all four of the following tests: Test 1 — §174 Test. The expenditure must be one for which a deduction is allowable under §174. Per §41(d)(1)(A) and Treas. Reg. §1.41-4(a)(2)(i), the expenditure must qualify as §174 SRE. Post-TCJA this is a low bar for most software development — §174(c)(3) sweeps in essentially all software dev costs. Test 2 — Discovery / Technological in Nature. Per §41(d)(1)(B)(i), the research must be undertaken for the purpose of discovering information that is technological in nature. The research must fundamentally rely on principles of the physical or biological sciences, engineering, or computer science. Marketing research, social science, economic surveys, and accounting/finance research are excluded. Test 3 — Process of Experimentation. Per §41(d)(1)(C) and Treas. Reg. §1.41-4(a)(5), substantially all (≥80%) of the research activities must constitute elements of a process of experimentation — a systematic evaluation of alternatives to eliminate uncertainty about the capability, methodology, or design of a business component. The taxpayer must: Identify the uncertainty (capability, method, or appropriate design). Identify alternatives to resolve the uncertainty. Conduct experiments (modeling, simulation, prototyping, systematic trial-and-error). Evaluate the alternatives against the uncertainty. A pure "build to spec" engineering exercise where the answer is known at the outset does NOT qualify. A debugging exercise that systematically eliminates hypothesized bug sources DOES qualify (this is contested at audit). Test 4 — Business Component / Permitted Purpose. Per §41(d)(1)(B)(ii), the research must relate to a new or improved business component — a product, process, technique, formula, invention, or software — and must be intended to result in improved function, performance, reliability, or quality. Improvements to style, taste, cosmetic, or seasonal design factors do not qualify.  _(§41(d)(1)(A); §41(d)(1)(B)(i); §41(d)(1)(C); §41(d)(1)(B)(ii); Treas. Reg. §1.41-4(a)(2)(i); Treas. Reg. §1.41-4(a)(5))_
- **Process of experimentation substantially-all threshold** — 80%  _(Treas. Reg. §1.41-4(a)(5))_

### 5.3 §41(d)(4) Exclusions — The Long Disqualification List

**§41(d)(4) exclusion list**  _(§41(d)(4))_

| Exclusion | Description | Practitioner concern |
| --- | --- | --- |
| **§41(d)(4)(A) — Research after commercial production** | Activities after the business component is ready for commercial sale | Very contested — when does "ready" mean for a SaaS product? |
| **§41(d)(4)(B) — Adaptation** | Adapting an existing component to a particular customer's requirement | Custom integrations and one-off customizations excluded |
| **§41(d)(4)(C) — Duplication** | Reverse-engineering or duplicating an existing component | Cloning a competitor's feature excluded |
| **§41(d)(4)(D) — Surveys, studies, etc.** | Efficiency, management, market, consumer surveys; data collection without experimentation | Excludes "market R&D" |
| **§41(d)(4)(E) — Computer software, internal use** | Internal-use software unless the high-threshold-of-innovation (HTI) test of §1.41-4(c)(6) is met | See Section 5.4 below |
| **§41(d)(4)(F) — Foreign research** | Research conducted outside the US (or its possessions) | Hard exclusion — no QRE for foreign R&E even though §174 capitalizes it |
| **§41(d)(4)(G) — Social science research** | Research in social sciences, arts, or humanities | Excluded entirely |
| **§41(d)(4)(H) — Funded research** | Research funded by another person (e.g., a customer paying a fixed-price contract that absorbs the R&E risk) | Look to the contract: who bears the financial risk and who owns the IP — both must point to the taxpayer |

- **§41(d)(4)(H) funded research dual test** — The §41(d)(4)(H) "funded research" issue is the single largest area of §41 audit risk for contract software developers. Under Treas. Reg. §1.41-4A(d): If the taxpayer is paid a fixed fee for development AND owns no substantial rights in the result, the research is "funded" and excluded from QRE. If the taxpayer is paid on a time-and-materials or cost-plus basis OR retains substantial rights (the right to use the developed software in its own business, license it elsewhere, etc.), the research is NOT funded and qualifies. The dual test (financial risk + IP rights) is conjunctive — both must point to "not funded" for the taxpayer to claim. For a freelance software developer doing custom client work, this is a major hurdle: most client engagements have IP-assignment clauses ("Work for Hire" / "all deliverables assigned to client") that strip IP rights and may also be fixed-fee. Such engagements do not generate QRE for the developer (and may not even for the client, depending on whether the client meets the four-part test on the receiving side).  _(§41(d)(4)(H); Treas. Reg. §1.41-4A(d))_

### 5.4 Internal-Use Software (IUS) — The High Threshold of Innovation

- **High threshold of innovation (HTI) test** — §41(d)(4)(E) excludes internal-use software from QRE unless the software meets the high threshold of innovation (HTI) test of Treas. Reg. §1.41-4(c)(6). The HTI test has three prongs (all required): 1. Innovative: the software would result in a reduction in cost, improvement in speed, or other measurable improvement that is substantial and economically significant. 2. Significant economic risk: the taxpayer commits substantial resources and there is substantial uncertainty whether the resources committed can be recovered within a reasonable period. 3. Not commercially available: software meeting the taxpayer's requirements cannot be purchased, leased, or licensed and used for the intended purpose without modifications that would themselves satisfy the HTI test.  _(§41(d)(4)(E); Treas. Reg. §1.41-4(c)(6))_
- **What counts as internal-use software** — Per Treas. Reg. §1.41-4(c)(6)(iii): software developed primarily for use in general and administrative functions (financial management, HR management, support services). Software developed for use by customers, or for non-G&A functions interacting with third parties, is not internal-use and is exempt from the HTI test.  _(Treas. Reg. §1.41-4(c)(6)(iii))_
- **Dual-function software rules** — Dual-function software (some internal G&A, some external/customer-facing): per the 2016 final regulations (TD 9786), if the software has both internal and non-internal uses, the taxpayer can: Identify a subset of elements that enable interaction with third parties or allow third parties to initiate functions — that subset is presumed non-IUS and exempt from HTI. Or apply a 25% safe harbor: if the third-party-interaction portion is ≥25% of the total dev cost, the full project is treated as non-IUS for §41 purposes. This is highly favorable to SaaS companies — most modern web apps interact with third parties (customers, vendors, payment processors, API consumers) and qualify under the 25% safe harbor or the subset rule.  _(TD 9786)_
- **25% dual-function safe harbor** — 25% of total dev cost  _(TD 9786)_

### 5.5 What Counts as QRE — The Wage / Supplies / Contract Research Trio

- **In-house wages QRE category** — QREs are limited to three categories per §41(b). 1. In-house wages — §41(b)(2)(A)(i). Wages paid to employees for qualified services, defined as: Engaging in qualified research (direct performance — the engineer writing the code). Direct supervision of qualified research (the engineering manager directing the work — supervisor's time qualifies only to the extent supervising actual qualified research, not general management). Direct support of qualified research (the lab technician maintaining the engineer's environment, the data engineer building the test harness — must be directly tied to research, not general IT support). "Wages" follows the §3401(a) definition. For S-corp owners, reasonable W-2 compensation allocable to QR services qualifies. For sole props and SMLLCs, the owner's draw is NOT W-2 wages and does NOT qualify as in-house wages — this is a structural disadvantage for unincorporated solo developers seeking the credit.  _(§41(b)(2)(A)(i); §3401(a))_
- **80% rule for wage QRE** — Per Treas. Reg. §1.41-2(d)(2), if an employee spends at least 80% of total time on qualified services, 100% of the wages are QRE. Below 80%, only the proportional share is QRE. Time tracking by employee/role is the substantiation backbone.  _(Treas. Reg. §1.41-2(d)(2))_
- **80% wage QRE threshold value** — 80% of total time on qualified services  _(Treas. Reg. §1.41-2(d)(2))_
- **Supplies QRE category** — 2. Supplies — §41(b)(2)(A)(ii). Tangible property other than land or §168 depreciable property, consumed in research: Cloud compute consumed in training/testing (controversial — the IRS sometimes takes the position cloud compute is a service, not a supply; most practitioners and the Tax Court tilt toward treating it as a supply where it is consumed by the research activity). Prototyping materials. Lab consumables (for biotech / hardware businesses).  _(§41(b)(2)(A)(ii))_
- **Standard contract research QRE inclusion rate** — 65%  _(§41(b)(2)(A)(iii); §41(b)(3))_
- **Qualified research consortium QRE inclusion rate** — 75%  _(§41(b)(3)(C))_
- **Basic research payments to qualified universities inclusion rate** — 75%  _(§41(e))_
- **Contract research financial risk/IP dual test and foreign contractor caution** — For contract research to qualify, the taxpayer (NOT the contractor) must bear the financial risk and retain substantial rights in the results (the same dual test as §41(d)(4)(H) "funded research" — viewed from the other side). A contractor who does the development on a time-and-materials basis with IP flowing back to the principal is contract research to the principal (65%) and is NOT funded research to the contractor (because the contractor bears no financial risk and owns no IP — wait, that's backwards — the contractor in that case has funded research = excluded; the principal has contract research at 65%, which is included). Caution: foreign contractors. Contract research performed outside the United States is excluded entirely under §41(d)(4)(F). A $100,000 payment to a Ukrainian dev shop = $0 QRE (but still $100,000 of foreign §174 SRE capitalized over 1Immediate expensing unless §174A(c) amortization election is made).  _(§41(d)(4)(F); §41(d)(4)(H))_

### 5.6 Computing the ASC — Step by Step

- **ASC computation steps** — For a calendar-year 2025 taxpayer electing the ASC: 1. Compute current-year QREs (sum of in-house wages, 65%-of-contract-research, supplies for qualified domestic research only). 2. Compute average QREs for the 3 preceding years (2022, 2023, 2024). If any of those years had no QREs, use the 6% no-base alternative. 3. Compute base amount = 50% × 3-year average QREs. 4. Excess QREs = current-year QREs − base amount. 5. ASC = 14% × excess QREs. 6. Apply §280C(c) election: ASC × (1 − 21%) = ASC × 79% if reduced-credit election is made.  _(§41(c)(5); §280C(c))_

### 5.7 Computing the Regular Credit — Step by Step (Less Common)

- **Regular Credit computation steps** — 1. Compute the fixed-base percentage: aggregate QREs in 1984-1988 / aggregate gross receipts in 1984-1988. Cap at 16%. 2. Compute base amount = fixed-base percentage × average gross receipts of 4 preceding years. 3. Apply the §41(c)(2) minimum base: base amount cannot be less than 50% of current-year QREs. 4. Excess QREs = current-year QREs − base amount. 5. RC = 20% × excess QREs. 6. Apply §280C(c). For taxpayers without 1984-1988 data (effectively all modern small businesses), the RC is unusable in practice. ASC is the default.  _(§41(c)(2); §41(a)(1); §280C(c))_
- **Fixed-base percentage cap** — 16%  _(§41(c)(2))_

### 5.8 Worked Example — ASC Computation for a Mid-Size CA SaaS

Delta SaaS, Inc. (S-corp, calendar year, all US operations) reports:

- 2025 QREs: $5,000,000 (engineering wages $4M + 65% × $600K of contractors = $4.39M + supplies $610K = $5,000,000).
- 2022 QREs: $2,000,000.
- 2023 QREs: $3,000,000.
- 2024 QREs: $4,000,000.

3-year average: ($2M + $3M + $4M) / 3 = $3,000,000.

Base amount: 50% × $3M = $1,500,000.

Excess QREs: $5,000,000 − $1,500,000 = $3,500,000.

ASC (gross): 14% × $3,500,000 = **$490,000**.

§280C(c) reduced credit: $490,000 × (1 − 21%) = $490,000 × 0.79 = **$387,100** (this is what flows to the §38 general business credit).

**§174 interaction.** The same $5M of QRE is also §174 SRE. Of the $5M:

- $4M wages: domestic SRE (assume all US engineers) → 5-year amortization.
- $390K (65% × $600K contractors): the 65% is just the credit haircut; the full $600K of contractor cost is §174 SRE, assumed domestic → 5-year amortization. Note: $600K of contractor cost generates $390K of QRE but $600K of §174 capitalization. The two figures are independent.
- $610K supplies: NOT §174 (supplies consumed in research are §162 if not deductible elsewhere, or capitalized if into property — but the IRS view is that supplies consumed in §174 research are themselves §174 expenditures per Treas. Reg. §1.174-2(a)(1)). Treat as §174.

§174 amortization for 2025:

- New 2025 pool: $4M + $600K + $610K = $5.21M domestic. Year-1 amortization: $5.21M × 1/5 × 1/2 = $521,000.
- Plus prior-year pools' continuing amortization (compute analogously from each year's SRE — for brevity assume ~$1.2M of prior-year amortization in 2025).
- Total 2025 §174 deduction: ~$1.72M against $5.21M actually spent on R&E.

**Bottom line for Delta**: the company gets a $387,100 R&D credit (good news) but defers $3.49M of deduction from 2025 into 2026-2030 (bad news for cash tax). Net cash-tax effect depends on the marginal rate; at 21% federal corporate (Delta is an S-corp so this flows through to shareholders at their marginal individual rates), the deferred-deduction cost is ~$0.7M-$1M of accelerated federal income tax in 2025.

### 6.1 The Default Rule

- **§280C(c)(1) default addback rule** — Per §280C(c)(1), if the taxpayer claims the §41 credit, the taxpayer must add back to taxable income an amount equal to the credit (because Congress did not want a double-benefit of credit + deduction on the same wages). The addback flows through Schedule C or the corporate return as a positive adjustment. For Delta SaaS in the example above, the default would mean adding back $490,000 to taxable income, then taking the $490,000 credit against tax.  _(§280C(c)(1))_

### 6.2 The §280C(c)(2) Reduced Credit Election

- **§280C(c)(2) reduced credit formula** — Alternatively, the taxpayer may elect under §280C(c)(2) to take a reduced credit equal to: Credit × (1 − maximum corporate rate) = Credit × (1 − 21%) = Credit × 0.79. In exchange for the reduced credit, no addback is required. This is virtually always the better election for taxpayers in the 21% bracket or higher because the addback at 21% net costs the same as the 21% reduction, and the reduced election is simpler administratively. The election is annual and is made on Form 6765, Section A or B, by checking the appropriate box. It applies to the entire year's credit — cannot be partial.  _(§280C(c)(2))_
- **Edge case for unincorporated taxpayers** — For an unincorporated taxpayer (sole prop / SMLLC) whose marginal rate exceeds 21% (e.g., 32%, 35%, 37% brackets), the §280C(c) reduced election is still typically preferred because the addback at the individual's marginal rate is more costly than the 21% reduction. But for taxpayers in the 10% or 12% bracket, the math reverses — taking the full credit and the addback may be better. In practice few §41-credit claimants are in the lowest brackets so this is rare.  _(§280C(c))_

### 7.1 The QSB Definition

- **Qualified Small Business definition** — §41(h)(3) defines a "Qualified Small Business" for purposes of the payroll-tax credit election as a corporation (including an S-corp), partnership, or sole proprietorship that meets both: 1. Gross receipts <$5 million in the current taxable year, AND 2. No gross receipts in any taxable year preceding the 5-taxable-year period ending with the current year. In plain English: the taxpayer's first year with any revenue must be within the last Immediate expensing unless §174A(c) amortization election is made (including the current year). A taxpayer in its first revenue year qualifies; a taxpayer in its 6th revenue year does not (regardless of revenue level).  _(§41(h)(3))_
- **QSB gross receipts threshold** — Less than $5,000,000 in the current taxable year  _(§41(h)(3))_
- **Gross receipts definition** — Gross receipts is defined under §448(c)(3) — basically gross income from all sources, including investment income, rental income, etc., aggregated under §52(a)/(b) controlled-group rules.  _(§448(c)(3); §52(a); §52(b))_

### 7.2 The Election — Up to $500K Against Payroll Tax

- **§41(h)(1) payroll tax credit election mechanics** — Per §41(h)(1), a QSB may elect to apply up to $500,000 of the year's §41 credit (after §280C(c) reduction) as a credit against the employer's share of OASDI (Social Security, 6.2%) payroll tax under §3111(a), and (after IRA 2022 amendments) the Medicare hospital insurance tax under §3111(b).  _(§41(h)(1); §3111(a); §3111(b))_
- **§41(h) payroll credit cap increased by IRA 2022** — $500,000 cap, increased from $250,000, effective for tax years beginning after December 31, 2022  _(Inflation Reduction Act of 2022 (P.L. 117-169, §13902))_

A pre-revenue or thinly-profitable startup may have $0 of federal income tax liability and therefore no use for an income-tax credit (carries forward 20 years under §39, but cash-tax value is zero today). But the startup IS paying ~7.65% in employer payroll tax on every dollar of engineering wages. Converting the income-tax credit into a payroll-tax offset turns a 20-year-deferred benefit into a same-quarter cash benefit.

### 7.3 The Mechanics

- **§41(h) election and Form 8974 mechanics steps** — 1. Annual election on Form 6765, Section D. The election is irrevocable for the year. 2. The elected credit amount (up to $500K) is transferred to Form 8974 ("Qualified Small Business Payroll Tax Credit for Increasing Research Activities"). 3. Form 8974 is attached to Form 941 (Employer's Quarterly Federal Tax Return) starting in the quarter following the income tax return filing — for a calendar-year corporation filing the 2025 1120-S in March 2026, Form 8974 first attaches to the Q2 2026 Form 941. 4. The credit applies against the employer share of OASDI first, then HI (Medicare), each quarter, until exhausted. 5. Any unused credit at year-end carries forward to the next quarter, indefinitely until used.  _(Form 6765; Form 8974; Form 941)_

### 7.4 The $500K Cap — Five-Year Lifetime Limit

- **No aggregate lifetime statutory cap but practical 5-year sunset** — A QSB can elect up to $500K per year, but there is no aggregate lifetime cap in the statute — a QSB that remains a QSB and generates large credits each year can elect $500K each year. Practically, however, the QSB status itself sunsets after Immediate expensing unless §174A(c) amortization election is made of gross receipts, so the maximum lifetime payroll-credit election is roughly $500K × 5 = $2.5 million for the most aggressive case.  _(§41(h))_

### 7.5 Worked Example — Pre-Revenue SaaS Startup

Echo Robotics, Inc. (Delaware C-corp, calendar year):

- Founded: January 2024 (first taxable year).
- 2024 gross receipts: $50,000 (pilot revenue).
- 2025 gross receipts: $400,000.
- 2025 QREs: $1,500,000 (3 founder-engineers + 2 contractor engineers, all US).
- Prior QREs: 2024 = $800,000. 2022 and 2023: zero (entity did not exist).

**ASC computation.**

Echo has QREs in only 1 of the 3 preceding years (2024), so technically the 3-year-average rule applies with zeros for 2022 and 2023: (0 + 0 + $800K) / 3 = $266,667. Base = 50% × $266,667 = $133,333.

But wait — per §41(c)(5)(B), if the taxpayer had no QREs in any one or more of the 3 preceding years, the taxpayer may still use the regular 14% ASC formula (with zeros included in the average). The 6% no-base alternative applies only if there were no QREs in any of the 3 preceding years. Echo had QREs in 2024, so 14% applies with the average including zeros.

Excess QREs = $1,500,000 − $133,333 = $1,366,667.

ASC (gross) = 14% × $1,366,667 = **$191,333**.

§280C(c)(2) reduced election: $191,333 × 0.79 = **$151,153**.

**QSB eligibility.** Echo's 2025 gross receipts = $400K < $5M ✓. Echo's first year with gross receipts was 2024, well within the 5-year window ✓. **QSB qualified.**

**§41(h) payroll-credit election.** Echo elects to apply the entire $151,153 against payroll tax (below the $500K cap). Filed on:

- Form 6765 attached to 2025 Form 1120 (filed March/April 2026, Section D election).
- Form 8974 attached to Form 941 starting **Q2 2026** (the quarter after the 1120 is filed).
- Echo's Q2 2026 employer OASDI liability (on ~$100K of payroll for the quarter, assume) = $100K × 6.2% = $6,200. Credit offsets this fully.
- Remaining credit carries to Q3, Q4, and into 2027 as needed.

**Cash benefit timing**: $151,153 of cash-tax savings spread over the four quarters of payroll tax filings starting Q2 2026. Without §41(h), the same $151,153 would carry forward as an income tax credit and likely produce $0 of cash benefit for years until Echo achieves profitability.

## 8. Stacking §174 + §41 — The "Same Dollar" Issue

- **Double-dipping question** — A frequent client question: "If I capitalize the wage under §174 AND claim the §41 credit on the same wage, isn't that double-dipping?" Answer: no. The two regimes operate on different axes: §174 is a timing rule for the deduction. The wage is fully deductible over 5/1 Immediate expensing unless §174A(c) amortization election is made — eventually the full amount is recovered. §41 is a credit against tax. The credit is a separate benefit on top of the (deferred) deduction.  _(§174; §41)_
- **§280C(c) interaction** — The interaction is handled by §280C(c): the credit reduces taxable income (via addback) by the credit amount unless the reduced election is made. There is no separate §280C-style rule that requires reducing §174 amortization by the §41 credit.  _(§280C(c))_

**Resulting cash-flow profile for a stacked claim (per $1 of QRE wage)**  _($0.10 × 0.21 + $0.0876 = $0.109)_

| Year | §174 deduction | §41 credit (ASC, reduced) | Total cash benefit at 21% rate |
| --- | --- | --- | --- |
| 1 | $0.10 | $0.111 × 0.79 = $0.0876 (one-time, assume the wage is 100% above base) | $0.10 × 0.21 + $0.0876 = $0.109 |
| 2 | $0.20 | $0 | $0.042 |
| 3 | $0.20 | $0 | $0.042 |
| 4 | $0.20 | $0 | $0.042 |
| 5 | $0.20 | $0 | $0.042 |
| 6 | $0.10 | $0 | $0.021 |
| **Total** | **$1.00** | **$0.0876** | **$0.298 (=29.8 cents per $1)** |

- **Pre-TCJA comparison** — Compared to pre-TCJA (immediate expense + credit) at 21% rate: $0.21 (immediate deduction benefit) + $0.0876 (credit) = $0.297 — virtually identical undiscounted. But discounted at any positive rate the post-TCJA stack is substantially worse because the deduction benefit is deferred. The §41 credit partially compensates for the §174 capitalization pain, but does NOT undo it.  _(unsure)_

## 9. Documentation and Substantiation

### 9.1 Project-Level Documentation

- **Documentation to maintain** — For both §174 and §41, the taxpayer should maintain at the project level: Project descriptions identifying the business component, the technological uncertainty being resolved, and the planned process of experimentation. Time tracking by employee/contractor, by project, by activity category (direct research vs. direct support vs. supervision vs. non-qualifying). Wage allocation worksheets applying the 80% rule and computing QRE per employee. Contracts with contractors and consultants (IP terms, payment terms, scope of work). Cost records for supplies consumed. Site-of-performance records for domestic/foreign split.  _(unsure)_

### 9.2 Recent IRS Enforcement Push — The Amended Return Disclosure

- **CCM 20214101F and 2022 IRS Memorandum disclosure requirement** — In CCM 20214101F (September 2021) and subsequent guidance including the 2022 IRS Memorandum on §41 claim substantiation (effective January 10, 2022; transition period extended through January 10, 2026), the IRS imposed a heightened disclosure requirement specifically for §41 credit claims filed on amended returns or refund claims (Form 1120X, 1040X, etc.). The amended-return §41 claim MUST include, at the time of filing: 1. Identify all business components to which the §41 credit relates. 2. Identify all research activities performed for each business component. 3. Identify all individuals who performed each research activity. 4. Identify all information each individual sought to discover. 5. Provide total qualified employee wage expenses, supply expenses, and contract research expenses for each business component. If the amended claim does not include these five items, the IRS will treat the claim as invalid and refuse to process the refund. The taxpayer may have one opportunity to perfect the claim within a 45-day cure period. This requirement applies only to amended-return claims, not to original returns. But practitioners have generalized the discipline — increasingly, even original-return §41 claims are being papered up with the five disclosures to pre-empt audit questions.  _(CCM 20214101F (September 2021); 2022 IRS Memorandum on §41 claim substantiation (effective January 10, 2022; transition period extended through January 10, 2026))_

### 9.3 §6663 and §6694 — Penalty Exposure

- **§6663 civil fraud** — §6663 civil fraud (75% penalty) is rarely applied to §41 claims, but the IRS has used it for egregious "credit-mill" claims with no underlying research.  _(§6663)_
- **§6662 accuracy-related** — §6662 accuracy-related (20% penalty) is the more common exposure for unreasonable §41 positions.  _(§6662)_
- **§6694 preparer penalty** — §6694 preparer penalty ($1,000 per return, or 50% of fee if greater) applies to the preparer who claims a §41 credit without a reasonable basis. Practitioners signing a §41 claim should retain the substantiation file.  _(§6694)_

### 9.4 §174 Substantiation

- **§174 audit risk profile** — §174 documentation is generally less contested than §41 — the IRS rarely audits §174 capitalization for amount (because the IRS gets revenue from the deferral!). The audit pressure is at the §41 credit, with §174 essentially the floor. The principal §174 risk is wholesale failure to capitalize (e.g., a SaaS company that expensed all engineering payroll in 2022-2024). Cleanup via Rev. Proc. 2024-9 method change is the practitioner solution; see Section 4.3.  _(Rev. Proc. 2024-9)_

## 10. State Conformity — A Critical Reviewer Item

- **General principle** — §174 capitalization is a federal rule. State conformity varies dramatically.  _(unsure)_
- **California** — California does NOT conform to TCJA §174. Per R&TC §17260, California permits immediate §174 expensing (continues pre-TCJA treatment). Result: the §174 capitalization adjustment is a Schedule CA decoupling item — the taxpayer adds back the federal §174 amortization and subtracts the full California-allowed expense in Year 1, then reverses in Years 2-6 as the federal amortization comes through. California also has its own R&D credit (R&TC §17052.12 for individuals, §23609 for corporations) at 15% RC / 7.5% partial ASC with its own base-period rules.  _(R&TC §17260; R&TC §17052.12; R&TC §23609)_
- **Texas** — Texas: no state income tax. §174 irrelevant for Texas franchise tax purposes (which is a margin tax with its own COGS / compensation deduction system).  _(unsure)_
- **New York, Illinois, other rolling-conformity states** — New York, Illinois, most other rolling-conformity states: generally follow federal §174. No decoupling.  _(unsure)_
- **Tennessee** — Tennessee (Excise Tax): has its own R&D regime; verify.  _(unsure)_
- **Wisconsin, Indiana, Mississippi** — Wisconsin, Indiana, Mississippi: have decoupled from TCJA §174 by state legislation (variable years).  _(unsure)_
- **Scope note** — This skill flags the decoupling but defers to the state skill for the actual state computation.  _(unsure)_

## 11. Worked Examples — Integrated

### Example 1 — Pre-Revenue Solo Founder Claiming §41(h) Payroll Credit

Foxtrot AI, LLC (Delaware C-corp, single-shareholder, calendar year, US-only ops): Founded January 2024. 2024 gross receipts: $0 (pre-revenue). 2025 gross receipts: $150,000 (early pilot revenue). 2025 W-2 wages: $300,000 (founder/sole employee, 100% engineering time on the company's ML platform). 2025 contractor R&D: $200,000 (US-based ML consultant on time-and-materials, IP assigned to Foxtrot). 2025 cloud compute (AWS): $80,000. 2025 office, admin, other: $40,000. Prior QREs: 2024 had $100,000 (3 months of founder salary at startup launch). 2022 and 2023: $0 (entity did not exist).

Founder wages: $300,000 (assume 100% qualified-services-related → all §174 SRE; the founder also wears a CEO hat but the 80% rule presumes 100% if substantially-all engineering). Contractor R&D: $200,000 ($174 SRE in full; the 65% haircut is a §41 mechanic, not a §174 mechanic). Cloud compute: $80,000 (supplies consumed in research, capitalize as §174). Office/admin: $40,000 (general §162 expense, not §174). Total 2025 domestic §174 pool: $580,000.

2025 pool: $580,000 × 1/5 × 1/2 = $58,000 Year-1 deduction. 2024 pool: $100,000 × 1/5 = $20,000 Year-2 deduction. 2025 total §174 deduction: $78,000. Deferred to future years: $580,000 + $80,000 (remaining 2024 pool) − $78,000 = $582,000 of future §174 amortization to recover.

In-house wages: $300,000. Contract research at 65%: $200,000 × 0.65 = $130,000. Supplies (cloud compute, consumed in research): $80,000. Total 2025 QREs: $510,000.

3-year average QREs: (0 + 0 + $100,000) / 3 = $33,333. Base amount: 50% × $33,333 = $16,667. Excess QREs: $510,000 − $16,667 = $493,333. ASC (gross): 14% × $493,333 = $69,067. §280C(c) reduced: $69,067 × 0.79 = $54,563.

2025 gross receipts: $150,000 < $5M ✓. Foxtrot's first taxable year was 2024 — within the 5-year window ✓. QSB qualified. Elect §41(h) on Form 6765 Section D: apply $54,563 against employer payroll tax via Form 8974.

Income tax: Foxtrot has $150,000 gross receipts − $78,000 §174 amortization − $40,000 office/admin − ($300,000 wages already booked but captured in §174 pool, so back out the $300K from current Schedule C wages deduction and recover via §174 amortization) = approximately ($168,000) loss for 2025. $0 federal income tax. Without the §41(h) election, the $54,563 credit carries forward 20 years. With the §41(h) election, $54,563 offsets 2026 employer OASDI/HI starting Q2 2026 — typically uses up over 2-3 quarters at Foxtrot's payroll level. Cash benefit accelerated by ~19 years.

1. §174 capitalization pain is severe — $300K of wages produces only $30K (half of $60K) of current-year deduction. Founder should understand cash-tax shock if revenue scales. 2. §41(h) election locks in the credit at the lower ASC amount — if Foxtrot's revenue explodes in 2026 and they exit QSB status, the 2025 election still applies but future credits will be income-tax-only. 3. Watch year-end extender legislation — if §174 is repealed retroactively, recompute.

### Example 2 — Mid-Size CA SaaS Computing ASC + §174

Delta SaaS, Inc. — see Section 5.8 above for full numbers. Briefly: S-corp, calendar year, California. 2025 QREs: $5M ($4M wages + $390K contract research at 65% + $610K supplies = $5.0M). §174 pool 2025: $5.21M ($4M + $600K contractors + $610K supplies; supplies are §174 per Reg §1.174-2(a)(1)). Prior 3-year average QREs: $3M. 2025 gross receipts: $30M (NOT QSB — far exceeds $5M). All US operations.

ASC gross: $490,000. §280C(c) reduced: $387,100.

New 2025 pool Y1: $521,000. Prior years' ongoing amortization (assume): ~$1.2M. Total 2025 §174 deduction: ~$1.72M against $5.21M actually spent. Deferred: ~$3.49M from 2025 into 2026-2030.

For California Schedule CA (540) — assuming the S-corp's K-1 income flows to a CA-resident shareholder — the shareholder claims the full $5.21M California §174 deduction in 2025 (because R&TC §17260 has not conformed to TCJA §174). The shareholder backs out the $1.72M federal §174 amortization and substitutes the full $5.21M California expense. California decoupling benefit: ($5.21M − $1.72M) × CA marginal rate (top bracket ~13.3% + 1% MHST = 14.3%) = $3.49M × 14.3% = ~$499,000 of CA tax deferral captured in 2025 (subject to reversal in 2026-2030 as the federal amortization catches up but California has already taken the full deduction). California R&D Credit (R&TC §17052.12). California's own §41 analog. ASC version available at 7.5% (not 14%). On Delta's $3.5M excess: 7.5% × $3.5M = $262,500 California R&D credit before any §280C(c) state addback (California has its own §17052.12(g) reduced election).

Federal §174 amortization schedule — 6-year roll-forward through 2030. Form 6765 Section B (ASC) with §280C(c) reduced election checked. Schedule CA (540) decoupling — full California §174 expense + California §174 amortization addback worksheet. California Form FTB 3523 (R&D credit) computation. Watch-item: year-end extender.

### Example 3 — Contractor R&D Allocation and the Funded-Research Trap

Gamma Consulting LLC (single-member, sole prop, CA resident, calendar year): 2025 gross receipts: $800,000. Client A: $400,000 revenue. Fixed-price contract for custom integration software. Client A owns all IP. (Standard "Work for Hire" clause.) Client B: $300,000 revenue. Time-and-materials contract for ML model development. Gamma retains the right to license the developed model to other clients. Client C: $100,000 revenue. Hourly consulting on Client C's internal tooling. No IP assignment; Client C owns its own output. Gamma's costs: $200,000 sole-prop draw (NOT W-2 wages — disqualified for §41 in-house wage QRE), $100,000 subcontractor (US-based, time-and-materials, IP flows to Gamma), $30,000 cloud compute, $50,000 other office.

Self-employed draw: §174 SRE if Gamma performed R&E. But draw is not §162 deductible to begin with for a sole prop (it's not a wage; it's the owner's distribution). No §174 capture for draw. (Source of disadvantage versus an S-corp: an S-corp owner-employee with W-2 comp captures §174 on the W-2 portion.) Subcontractor $100,000: §174 SRE (domestic) → $10,000 Y1 amortization. Cloud compute $30,000: §174 if consumed in research, capitalize → $3,000 Y1 amortization. Other office $50,000: not §174, deduct as §162.

Client A revenue: Gamma is funded under §41(d)(4)(H) (fixed-price, IP transfers to Client A, Gamma bears no economic risk if the project succeeds — Gamma gets paid the fixed fee regardless). No QRE from Client A work. Client B revenue: Gamma is NOT funded (time-and-materials = no financial risk concentration in Gamma; Gamma retains substantial IP rights). QRE potentially available for Client B work. Client C revenue: Gamma is funded (no IP rights to Gamma). No QRE from Client C work.

Of Gamma's $100,000 subcontractor cost, allocate the portion working on Client B project. Assume 50% → $50,000 of subcontractor on Client B = $50,000 × 65% = $32,500 QRE. Of cloud compute $30,000, allocate similarly: $15,000 on Client B = $15,000 supplies QRE. Self-employed draw: NOT QRE (no W-2 wages). Gamma's total 2025 QRE: $47,500.

6% no-base alternative: $47,500 × 6% = $2,850 ASC. §280C(c) reduced: $2,850 × 0.79 = $2,252.

$800K gross receipts < $5M ✓. But Gamma has been operating for 8 years (assume) — so the "no gross receipts before the 5-year window" test FAILS. NOT a QSB. No §41(h) election available. The $2,252 credit goes to income tax with 20-year carryforward.

1. Sole-prop disadvantage — the $200K owner draw produces zero §41 in-house wage QRE. If Gamma generated meaningful R&D credit potential, an S-corp election with reasonable owner W-2 comp would unlock the wage QRE. See `us-s-corp-election-decision`. 2. Funded research trap — 50% of Gamma's revenue is funded research that produces NO §41 credit despite being §174 SRE for Gamma. Recommend Gamma restructure contracts with Clients A and C to retain at least non-exclusive IP rights or shift to T&M billing. 3. Tiny credit ($2,252) — likely not worth the substantiation cost for Gamma. Recommend skipping §41 claim unless credit grows materially. 4. §174 still applies to all of Gamma's R&E even where §41 doesn't. The $113K of §174 SRE ($100K subcontractor + $13K cloud after 50% allocation? — recompute) is fully capitalized regardless of the funded-research issue.

## 12. Self-Checks Before Sign-Off

Before the reviewer signs off on a §174/§41 workpaper, run the following self-checks: 1. §174 vs. §41 separation. Are the two computations maintained as separate workpapers? The §174 pool includes 100% of contractor cost; the §41 base includes 65% of contractor cost. These figures MUST NOT be combined. 2. Domestic/foreign split. Has the analyst documented site-of-performance for every R&E contractor and traveling employee? 3. §41 four-part test. For each business component claimed, is there contemporaneous documentation of: business component, uncertainty, alternatives evaluated, experimentation process? 4. Internal-use software gate. If any component is IUS, does it pass HTI or qualify under the dual-function 25% safe harbor? 5. Funded research test. For every contract-derived QRE, has the analyst verified the dual test (taxpayer bears financial risk + taxpayer retains substantial rights)? 6. §280C(c) election. Is the reduced-credit box checked on Form 6765? (Default for almost all taxpayers.) 7. §41(h) eligibility. Is the QSB definitively below $5M and within the 5-year window? Cap on election is $500K. 8. Sole-prop draw. Has the analyst confirmed that owner-draw is NOT in the §41 wage base (only applies to W-2 wages)? 9. State conformity. Has the analyst flagged any state-decoupling (California especially)? 10. Year-end extender watch. Is there an open watch-item for §174 retroactive repeal? Re-check before transmittal. 11. Method change. If the taxpayer has been improperly expensing §174 in any prior year, has Form 3115 been queued (DCN 265)? 12. Amended-return disclosure. If this is an amended-return §41 claim, are all five required disclosures (business component, activities, individuals, information sought, expenses) included? 13. Substantiation file. Time tracking, contracts, project descriptions, cost ledgers — all assembled and retained? 14. §174(d) abandonment. If any project has been abandoned, is the amortization still continuing on the original schedule?

## 13. Refusal Catalogue (Skill-Specific)

- **R-174-1** — Multinational allocations of §174 SRE under §861 / §1.861-17 stewardship rules.  _(§861 / §1.861-17)_
- **R-174-2** — Pre-2022 §174 elections (former §174(b), §59(e)).  _(former §174(b); §59(e))_
- **R-174-3** — §174 interaction with §168(k) bonus depreciation for property used in research.  _(§168(k))_
- **R-174-4** — §174 for partnerships with §704(b) special allocations of R&E.  _(§704(b))_
- **R-41-1** — §41(c)(4) gross-receipts apportionment on mid-year acquisitions.  _(§41(c)(4))_
- **R-41-2** — §41(e) basic research payments by corporations with a fixed-base period floor.  _(§41(e))_
- **R-41-3** — Controlled-group aggregation under §41(f) / §52(a)(b) where the aggregated group exceeds $5M and QSB sub-entity status is contested.  _(§41(f); §52(a)(b))_
- **R-41-4** — Form 6765 Section G (controlled group apportionment).  _(Form 6765 Section G)_
- **R-41-5** — Amended-return §41 claims older than 3 prior tax years (statute of limitations and the 2022 IRS Memorandum disclosure regime require specialist handling).  _(2022 IRS Memorandum)_
- **R-41-6** — §41(h) election cleanup where Form 8974 has been filed inconsistently in prior quarters.  _(Form 8974)_
- **R-STATE-1** — State R&D credit computation other than California (defer to state skill).  _(unsure)_
- **R-CLAIM-MILL** — Any "credit study" produced by a third-party credit-mill firm that the analyst is asked to merely sign off on. Independent validation required.  _(unsure)_

## 14. Provenance and Sources

- **IRC §41** — Credit for increasing research activities — current through P.L. 119-21 (OBBBA, July 4, 2025).  _(IRC §41; P.L. 119-21)_
- **IRC §174** — Amortization of research and experimental expenditures — as amended by TCJA §13206, P.L. 115-97 (December 22, 2017).  _(IRC §174; TCJA §13206, P.L. 115-97)_
- **IRC §280C(c)** — Wage addback / reduced credit election.  _(IRC §280C(c))_
- **IRC §3111(a),(b)** — Employer payroll tax — credit target for §41(h).  _(IRC §3111(a), (b))_
- **IRC §41(h)(3)** — QSB definition.  _(IRC §41(h)(3))_
- **Inflation Reduction Act of 2022** — P.L. 117-169, §13902 (cap increase from $250K to $500K).  _(Inflation Reduction Act of 2022, P.L. 117-169, §13902)_
- **One Big Beautiful Bill Act** — P.L. 119-21 (July 4, 2025) — did NOT amend §174.  _(P.L. 119-21)_
- **Treas. Reg. §1.41-2** — Computation of in-house wage QRE; 80% rule.  _(Treas. Reg. §1.41-2)_
- **Treas. Reg. §1.41-4** — Four-part test mechanics.  _(Treas. Reg. §1.41-4)_
- **Treas. Reg. §1.41-4(c)(6)** — Internal-use software, HTI test, dual-function rules.  _(Treas. Reg. §1.41-4(c)(6))_
- **Treas. Reg. §1.41-4A(d)** — Funded research dual test.  _(Treas. Reg. §1.41-4A(d))_
- **Treas. Reg. §1.174-2** — Definition of §174 expenditures.  _(Treas. Reg. §1.174-2)_
- **TD 9786** — October 2016 — IUS final regulations including 25% dual-function safe harbor.  _(TD 9786)_
- **Rev. Proc. 2023-8 / 2023-11** — Initial §174 method change for 2022.  _(Rev. Proc. 2023-8 / Rev. Proc. 2023-11)_
- **Rev. Proc. 2024-9** — Current automatic-consent framework, DCN 265 and 357.  _(Rev. Proc. 2024-9)_
- **IRS Chief Counsel Advice CCA 20214101F** — Sep 17, 2021 — amended-return §41 claim substantiation.  _(CCA 20214101F)_
- **2022 IRS Memorandum** — On §41 amended claim five-fact disclosure (effective January 10, 2022; transition period extended through January 10, 2026 by subsequent IRS announcements).  _(2022 IRS Memorandum)_
- **H.R. Rep. No. 115-466** — TCJA Conference Report, December 2017 — §174 changes.  _(H.R. Rep. No. 115-466)_
- **H.R. 7024** — Tax Relief for American Families and Workers Act of 2024 — House-passed; failed cloture in Senate, August 1, 2024.  _(H.R. 7024)_
- **Suder v. Commissioner** — T.C. Memo. 2014-201 (foundational on contemporaneous documentation requirements for §41).  _(Suder v. Commissioner, T.C. Memo. 2014-201)_
- **Populous Holdings, Inc. v. Commissioner** — T.C. Docket No. 405-17 (2019, settled) — funded research dual test for architectural firms; persuasive for software analog.  _(Populous Holdings, Inc. v. Commissioner, T.C. Docket No. 405-17)_
- **Little Sandy Coal Co. v. Commissioner** — 62 F.4th 287 (7th Cir. 2023) — process of experimentation rigor; sets a high bar that practitioners must respect.  _(Little Sandy Coal Co. v. Commissioner, 62 F.4th 287 (7th Cir. 2023))_
- **Forms** — Form 6765 (Credit for Increasing Research Activities) — 2025 revision. Form 8974 (Qualified Small Business Payroll Tax Credit for Increasing Research Activities) — current revision. Form 941 (Employer's Quarterly Federal Tax Return) — for §41(h) application. Form 3115 (Application for Change in Accounting Method) — for §174 method changes. Form 1040 Schedule C (sole proprietors) and Form 1120/1120-S (corporations) — host returns.  _(Form 6765; Form 8974; Form 941; Form 3115; Form 1040 Schedule C; Form 1120/1120-S)_

verified_by: pending — this skill has not yet been signed off by a credentialed §41/§174 specialist. The lead US Federal verifier should review Sections 5 (four-part test), 7 (§41(h) mechanics), and 11 (worked examples) for accuracy before promotion to verified_by: <name>.

2025-11-15. Next mandatory re-review: April 1, 2026 (after the 2025 filing season closes and any year-end extender legislation is enacted).

## Talk to a verified accountant

This skill is a tool, not an engagement. Every taxpayer's situation is different, and the rules in the skill may not match your specific facts. To speak with one of the licensed accountants who verifies skills for your jurisdiction — no liability on either side until you and the accountant sign a formal engagement letter — book a free 30-minute call: → [Book a call](https://calendly.com/openaccountants-info/30min) We'll route you to the named verifier covering your country or state. You can also see the full list of verified accountants at [openaccountants.com/network](https://openaccountants.com/network).
