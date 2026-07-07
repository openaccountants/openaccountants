---
name: us-state-bonus-depreciation-conformity-matrix
description: Tier 2 US federal-level reference skill providing the 50-state matrix of conformity to federal §168(k) bonus depreciation and §179 expensing. Covers tax year 2025 including state-by-state add-back requirements (CA never conforms with $25k §179 cap, NY decoupled since 2003, NJ partial, PA decoupled bonus with §179 conformity, etc.), recovery mechanisms for state add-backs (typically over 5 years or via decoupled MACRS lifetime), §163(j) interest limit conformity, NOL post-TCJA conformity, and the OBBBA-era bonus depreciation status with the TCJA phase-down (60% 2024 → 0% 2027 absent extension).
jurisdiction: US
domain: federal-tax
tax_year: 2025
tier: 2
last_updated: 2026-07-06
---

# us-state-bonus-depreciation-conformity-matrix

## US State Bonus Depreciation and §179 Conformity Matrix — Tax Year 2025

> **AUDIT FLASH POINT.** State depreciation add-back tracking is one of the most commonly mishandled items on multistate returns. Failures cluster in three patterns:
>
> 1. **Missing the add-back entirely in year of acquisition** — federal bonus depreciation flows through to state taxable income without adjustment, overstating the state deduction by up to 100% of cost in the first year.
> 2. **Failing to track the recovery (subtraction) over the recapture period** — once added back, most decoupled states allow recovery either over a fixed period (commonly 5 years) or via the decoupled MACRS schedule. Practitioners who add back but never recover overstate state taxable income in years 2-N.
> 3. **Confusing federal vs state §179 caps** — California's $25,000 cap and Indiana / New Jersey / others' partial caps frequently produce silent over-deductions that survive multiple cycles before audit.
>
> The matrix below is a reviewer reference. State add-backs are mechanical but unforgiving: a single missed year propagates through every subsequent year of the asset's recovery period.

## 1. Scope and Why This Matters

State income tax is computed on a base derived from federal taxable income, but every state defines its own conformity to the Internal Revenue Code. Three Code provisions create the most pervasive book-tax differences at the state level:

- **IRC §168(k) bonus depreciation** — first-year expensing of a percentage of cost.
- **IRC §179 expensing** — election to expense qualifying property within annual caps.
- **IRC §163(j) business interest limitation** — limit on deductibility of business interest expense.

When a state decouples from any of these, the practitioner must compute a **state-specific depreciation schedule** that runs parallel to the federal schedule for the life of the asset, often 5 to 20 years. This is the single largest source of multi-year tracking work on small-business state returns.

### Why decoupling matters for sole proprietors and SMLLCs

For pass-through owners, federal Schedule C net profit flows to state personal income tax (PIT) returns. If the state decouples, the state's modified Schedule C net profit differs from the federal — and that difference persists every year the asset is on the books. A laptop purchased in 2025 and §168(k)-expensed federally may still be generating state add-backs in 2030.

For multistate businesses with apportionment, the add-back interacts with the apportionment formula, meaning the same federal deduction can create different state-level adjustments in every state where the taxpayer files.

### The TCJA phase-down (pre-OBBBA baseline)

**TCJA phase-down schedule**

| Year placed in service | Bonus rate (TCJA pre-OBBBA) |
| --- | --- |
| 2017 (after Sep 27) – 2022 | 100% |
| 2023 | 80% |
| 2024 | 60% |
| 2025 | 40% |
| 2026 | 20% |
| 2027 and later | 0% |

### OBBBA modification — 2025 status

- **OBBBA restoration of 100% bonus depreciation** — The One Big Beautiful Bill Act (P.L. 119-21, enacted July 4, 2025) restored 100% bonus depreciation under §168(k) for qualified property acquired and placed in service after January 19, 2025. The pre-OBBBA phase-down (40% for 2025) applies to property acquired on or before January 19, 2025 under transition rules.  _(One Big Beautiful Bill Act (P.L. 119-21, enacted July 4, 2025))_

### OBBBA modification — 2025 status

**Practitioner note for 2025 returns:** taxpayers may have a split-year fact pattern — pre-January 19 acquisitions at 40% bonus and post-January 19 acquisitions at 100%. Track acquisition dates carefully.

> **Verification required.** Bonus depreciation rules are politically volatile. Re-verify the OBBBA §168(k) provisions against IRS Pub. 946 (2025) and §168(k) as amended by Title VII of P.L. 119-21 before relying on the 100% restoration.

### What is §168(k) "qualified property"

- **§168(k) qualified property** — Generally, tangible property with a MACRS recovery period of 20 years or less, computer software, qualified film/TV/live theatrical productions, and (since TCJA) used property meeting the §168(k)(2)(E)(ii) acquisition rules. Real property is excluded except for qualified improvement property (15-year recovery).  _(§168(k)(2)(E)(ii))_

### Federal §168(k) election out

- **Election out on class-by-class basis** — Taxpayers may elect out of bonus depreciation on a class-by-class basis under §168(k)(7). When a taxpayer elects out federally, no state add-back is needed because no federal bonus deduction was taken. This is the simplest planning strategy for taxpayers in decoupled states with minimal capital purchases.  _(§168(k)(7))_

## 3. Federal §179 Expensing Limits — 2025

- **§179 deduction limit (cap)** — $1,220,000  _(Rev. Proc. 2024-40)_
- **§179 phase-out (investment) threshold** — $3,050,000 (dollar-for-dollar reduction begins at this level; deduction fully phased out at $4,270,000)  _(Rev. Proc. 2024-40)_
- **§179 SUV deduction limit** — $30,500 USD (qualifying sport utility vehicles over 6,000 lbs GVWR but under 14,000 lbs)  _(Rev. Proc. 2024-40)_
- **Taxable income limitation** — §179 deduction limited to taxable income from active trade or business  _(Rev. Proc. 2024-40)_
- **OBBBA modification for §179** — The 2025 OBBBA increased the §179 cap and phase-out for years after 2025. Verify 2026 figures separately.  _(OBBBA (P.L. 119-21))_

### §179 qualifying property

- **§179 qualifying property** — Tangible personal property used in a trade or business, off-the-shelf computer software, qualified real property improvements (roofs, HVAC, fire protection, alarm/security on nonresidential real property under §179(f)).  _(§179(f))_

### Difference between §179 and §168(k)

**§179 vs §168(k) bonus comparison**

| Feature | §179 | §168(k) bonus |
| --- | --- | --- |
| Election required | Yes (per asset class) | No (automatic; opt-out election available) |
| Annual cap | Yes ($1.22M for 2025) | No |
| Phase-out at investment level | Yes ($3.05M for 2025) | No |
| Income limitation | Yes (active trade/business income) | No |
| Used property eligible | Yes | Yes (post-TCJA, with restrictions) |
| Real property | Limited (qualified improvement property + §179(f)) | 15-year QIP only |
| State conformity | Mixed (more states conform) | Mostly decoupled |

## 4. The Conformity Continuum

States can be grouped into five categories:

### Category A: No personal income tax (7 states + 2 partial)

These states do not impose a personal income tax on wages or pass-through business income, so §168(k) and §179 conformity is moot for owners of disregarded SMLLCs and sole proprietors:

- Alaska (no PIT)
- Florida (no PIT)
- Nevada (no PIT)
- South Dakota (no PIT)
- Tennessee (no PIT as of 2021; previously taxed interest/dividends)
- Texas (no PIT)
- Washington (no PIT on wages; capital gains tax over $250k applies but does not affect Sch C)
- Wyoming (no PIT)
- New Hampshire (taxes interest/dividends only; effective 0% as of 2025 under prior phase-out; no Sch C tax)

**However**, where these states impose entity-level taxes (Texas franchise tax, Washington B&O, New Hampshire BPT/BET, Tennessee FAE), conformity to §168(k) and §179 must be tested separately under the state's entity tax statute. Texas Franchise Tax under Ch. 171 uses its own modified income computation and does not adopt §168(k) bonus depreciation for compensation method computations.

### Category B: Full conformity (rolling or static IRC conformity, both §168(k) and §179)

States that adopt the IRC and do not separately decouple from §168(k) or §179:

- Alabama
- Colorado (post-2022 conformity restored)
- Delaware
- Kansas
- Louisiana
- Missouri
- Montana
- Nebraska
- New Mexico
- North Dakota
- Oklahoma
- Oregon
- Rhode Island
- Utah
- West Virginia
- District of Columbia

### Category C: Conform to §179 but decouple from §168(k)

The most common pattern — the state allows §179 but requires bonus depreciation add-back:

- Arizona
- Arkansas
- Connecticut
- Georgia
- Hawaii
- Idaho
- Iowa (post-2021 conformity for bonus restored for some years — verify)
- Kentucky
- Maine
- Maryland
- Massachusetts
- Michigan
- Mississippi
- North Carolina
- Ohio (commercial activity tax instead of PIT for businesses)
- Pennsylvania
- South Carolina
- Vermont
- Virginia (with §179 cap difference, see Category D)
- Wisconsin

### Category D: Decouple from both §168(k) and §179 (or impose own §179 caps)

The most complex states:

- **California** — never conforms to bonus; §179 cap $25,000; investment phase-out $200,000
- **Indiana** — §179 cap $25,000 (decoupled)
- **Iowa** — historically decoupled, partial conformity 2021+, verify current year
- **Minnesota** — both decoupled; 80% add-back of bonus, recovered over 5 years; §179 historically capped (now conformed for tax years 2020+)
- **New Jersey** — bonus decoupled; §179 partial conformity with state cap rules and 50%-of-property limitation in some cases
- **New York** — bonus decoupled since 2003; §179 conforms but with NYC differences
- **Virginia** — §179 cap historically $25,000 (verify current year as Virginia has updated conformity)
- **Illinois** — decoupled in nuanced ways; treats bonus as add-back with recovery over MACRS life

### Category E: Quirks and special regimes

- **New Hampshire** (BPT) — decoupled, but no PIT for individuals
- **Texas** (franchise) — uses revenue or compensation-based computation, depreciation conformity less central
- **Washington** (B&O) — gross receipts, no depreciation conformity issue

## 5. 50-State + DC Conformity Matrix (2025)

**50-State + DC Conformity Matrix (2025)**

| # | State | §168(k) Bonus | §168(k) recovery method if decoupled | §179 Cap (if ≠ federal $1.22M) | §179 Phase-out (if ≠ federal $3.05M) | Add-back Method | Recovery Period for Add-back | NOL Post-TCJA (80% rule? Carryforward) | §163(j) Interest Conformity | Notable Quirks |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Alabama | F | — | Conforms | Conforms | None | N/A | 80% rule conforms; 15-yr CF (longer than federal) | Conforms | Rolling conformity |
| 2 | Alaska | N/A | — | — | — | — | — | — | — | No PIT |
| 3 | Arizona | D | Decoupled MACRS (state schedule) | Conforms | Conforms | 100% add-back yr 1, recover over MACRS life | MACRS life of asset | Conforms; 80% rule; 20-yr CF | Conforms | Subtraction over depreciable life |
| 4 | Arkansas | D | Decoupled MACRS | Conforms | Conforms | Add-back yr 1, recover over MACRS life | MACRS life | Conforms; 80% rule; 5-yr CF (shorter) | Conforms | Form AR1100REC for recovery |
| 5 | California | **D (never conforms)** | Decoupled MACRS / ACRS for pre-1987 | **$25,000** | **$200,000** | Add-back of full bonus; differs by year via Sch CA (540) | MACRS life of asset (state) | Does NOT conform to 80% rule; 20-yr CF (NOL); 50% AMT limit history | Does NOT conform to §163(j) | LARGE add-back tracking; oldest decoupling regime in US |
| 6 | Colorado | F (post-2022) | — | Conforms | Conforms | None (post-2022) | N/A | Conforms; 80% rule; 20-yr CF | Conforms | Pre-2022 had different rules |
| 7 | Connecticut | D | Recovery over 4 years (25%/yr) | Conforms | Conforms | 100% add-back yr 1; 25% subtraction yrs 2-5 | 4 years (25% per year) | Conforms; 80% rule; 20-yr CF | Conforms (with modifications) | 25%/yr recovery is unique |
| 8 | Delaware | F | — | Conforms | Conforms | None | N/A | Conforms | Conforms | Rolling conformity |
| 9 | DC | F | — | Conforms | Conforms | None | N/A | Conforms; 80% rule | Conforms | — |
| 10 | Florida | N/A (PIT); Corp tax decouples bonus | C-corp: 1/7th recovery | — | — | C-corp only: add-back & 1/7th annual subtraction | 7 years (corp tax) | C-corp: conforms post-TCJA | C-corp: conforms | No PIT for individuals / SMLLC owners |
| 11 | Georgia | D | Decoupled MACRS | Conforms | Conforms | Add-back full bonus; subtract via decoupled MACRS | MACRS life | Conforms; 80% rule | Conforms | Schedule 1 add/subtract on Form 500 |
| 12 | Hawaii | D | Decoupled MACRS | Conforms | Conforms | Add-back, recover via state MACRS | MACRS life | Conforms; 80% rule | Conforms | — |
| 13 | Idaho | D | Decoupled MACRS | Conforms | Conforms | Add-back, recover via decoupled MACRS | MACRS life | Conforms | Conforms | — |
| 14 | Illinois | **D** | Decoupled MACRS | **Conforms** (post-2018) | Conforms | Add-back federal bonus; subtraction over MACRS life via Schedule M | MACRS life | 80% rule conforms; 12-yr CF | Conforms | Complex; the Illinois Replacement Tax for PTEs also requires add-back |
| 15 | Indiana | D | Decoupled MACRS | **$25,000** | Conforms | Add-back bonus; §179 cap creates additional add-back | MACRS life | Conforms; 80% rule; 20-yr CF | Conforms | $25k §179 cap is significant |
| 16 | Iowa | F (post-2021) | — (post-2021) | Conforms (post-2020) | Conforms | None for 2021+; historical recapture continues for pre-2021 assets | N/A (post-2021) | Conforms; 80% rule; 20-yr CF | Conforms | Significant historical decoupling; track legacy assets |
| 17 | Kansas | F | — | Conforms | Conforms | None | N/A | Conforms | Conforms | Static IRC conformity, updated periodically |
| 18 | Kentucky | D | Decoupled MACRS (pre-2002 rules) | Conforms ($25k pre-2010; $1.22M post) | Conforms | Add-back federal bonus, recover via state MACRS | MACRS life | Conforms | Conforms | Kentucky uses pre-bonus federal law as state base |
| 19 | Louisiana | F | — | Conforms | Conforms | None | N/A | Conforms; 80% rule | Conforms | Rolling conformity |
| 20 | Maine | D | 5-yr straight-line recovery of add-back | Conforms | Conforms | Add-back yr 1; subtract 20%/yr yrs 2-6 | 5 years (20% per year) | Conforms; 80% rule | Conforms | Maine Capital Investment Credit (BETC) interacts |
| 21 | Maryland | D | Decoupled MACRS | Conforms | Conforms | Add-back federal bonus, recover via state schedule | MACRS life | Conforms; 80% rule | Conforms | Form 500DM tracks add-back / recovery |
| 22 | Massachusetts | D | Decoupled MACRS | Conforms | Conforms | Add-back federal bonus, recover via state MACRS | MACRS life | Conforms (corp); PIT no NOL CF for individuals (Sch C losses limited) | Conforms (corp); PIT no §163(j) | Form Schedule B / E adjustments |
| 23 | Michigan | D | Decoupled MACRS | Conforms | Conforms | Add-back federal bonus, recover via state MACRS | MACRS life | Conforms; 80% rule; 20-yr CF | Conforms | — |
| 24 | Minnesota | **D** | 80% added back yr 1; 20%/yr recovery yrs 2-6 | Conforms (post-2020) | Conforms (post-2020) | **80% of bonus added back yr 1; 20% subtracted in each of years 2-6** | 5 years (20%/yr) | Conforms; 80% rule | Conforms | Historic §179 decoupling; verify pre-2020 assets |
| 25 | Mississippi | D | Decoupled MACRS | Conforms | Conforms | Add-back, recover via state MACRS | MACRS life | Conforms | Conforms | — |
| 26 | Missouri | F | — | Conforms | Conforms | None | N/A | Conforms; 80% rule; 20-yr CF | Conforms | Rolling conformity |
| 27 | Montana | F | — | Conforms | Conforms | None | N/A | Conforms; 80% rule | Conforms | Rolling conformity |
| 28 | Nebraska | F | — | Conforms | Conforms | None | N/A | Conforms; 80% rule; 20-yr CF | Conforms | Rolling conformity |
| 29 | Nevada | N/A | — | — | — | — | — | — | — | No PIT |
| 30 | New Hampshire | D (BPT/BET only) | Decoupled MACRS | Conforms | Conforms | BPT/BET add-back; no individual PIT | MACRS life (BPT) | BPT NOL 10-yr CF | BPT conforms | Individuals not affected (no PIT on Sch C) |
| 31 | **New Jersey** | **D** | Decoupled MACRS | **Conforms** ($1.22M); but **50%-of-asset cap for certain real property** | Conforms | Add-back federal bonus; §179 partial cap interactions | MACRS life | Conforms (corp); GIT (PIT) — no NOL CF for individuals (only same-category offset) | CBT (corp) conforms with modifications; GIT (PIT) doesn't apply | NJ Gross Income Tax for PIT has very limited loss recognition |
| 32 | New Mexico | F | — | Conforms | Conforms | None | N/A | Conforms; 80% rule | Conforms | Rolling conformity |
| 33 | **New York** | **D (since 2003)** | Decoupled MACRS | Conforms | Conforms | Add-back federal bonus; recover via decoupled MACRS schedule | MACRS life | Conforms (corp); PIT itemized rules differ | Conforms (corp Article 9-A); PIT differs | NYS Form CT-399 / IT-399 tracks; NYC has additional decoupling for unincorporated business tax (UBT) |
| 34 | North Carolina | F (post-2020) | — | Conforms | Conforms | None (post-2020); legacy 85% add-back for pre-2020 with 5-yr recovery | N/A (current); 5 yr for legacy | Conforms; 80% rule | Conforms | Verify legacy add-back recoveries for pre-2020 assets |
| 35 | North Dakota | F | — | Conforms | Conforms | None | N/A | Conforms; 80% rule | Conforms | Rolling conformity |
| 36 | **Ohio** | **D** (CAT — Commercial Activity Tax; gross receipts) | N/A for CAT; PIT-level decouples bonus with 5/6 add-back and 1/6 subtraction over 5 yrs | Conforms (PIT) | Conforms (PIT) | PIT: 5/6 of bonus added back yr 1; 1/6 subtraction in each of yrs 1-6 | 6 years (1/6 per year) | Conforms (CAT/PIT) | Conforms | Ohio's 5/6 fraction is unique |
| 37 | Oklahoma | F | — | Conforms | Conforms | None | N/A | Conforms; 80% rule | Conforms | Rolling conformity |
| 38 | Oregon | F | — | Conforms | Conforms | None | N/A | Conforms; 80% rule; 15-yr CF | Conforms | — |
| 39 | **Pennsylvania** | **D** | Decoupled MACRS for corp; PIT no depreciation concept (Sch C uses fed) | Conforms (PIT); Corp: ratable over asset life | Conforms | CNI (corp): 100% add-back, recover ratably over MACRS life; PIT: federal depreciation flows (but no bonus add-back at PIT level if rev rul applies) | MACRS life (CNI) | CNI: 80% rule conforms; 20-yr CF; PIT: no NOL CF for losses | CNI conforms; PIT differs | PA PIT for Schedule C — verify current bonus treatment; PA historically decoupled at corp level |
| 40 | Rhode Island | F | — | Conforms | Conforms | None | N/A | Conforms; 80% rule | Conforms | Rolling conformity |
| 41 | South Carolina | D | Decoupled MACRS | Conforms | Conforms | Add-back federal bonus, recover over MACRS life | MACRS life | Conforms; 80% rule | Conforms | — |
| 42 | South Dakota | N/A | — | — | — | — | — | — | — | No PIT |
| 43 | Tennessee | N/A (Hall income tax repealed 2021); F&E corp tax conforms | F&E: conforms | — | — | F&E only | N/A | F&E conforms | F&E conforms | No PIT; individuals on Sch C unaffected |
| 44 | Texas | N/A (PIT); Franchise tax decouples bonus | Franchise tax: COGS / compensation method | — | — | Franchise: bonus excluded under COGS / compensation method | N/A (revenue-based) | Franchise: 5-yr CF | Franchise conforms with modifications | No PIT; LLCs file Form 05-102 PIR + No Tax Due or EZ |
| 45 | Utah | F | — | Conforms | Conforms | None | N/A | Conforms; 80% rule | Conforms | Rolling conformity |
| 46 | Vermont | D | Decoupled MACRS | Conforms | Conforms | Add-back, recover via MACRS | MACRS life | Conforms; 80% rule | Conforms | — |
| 47 | **Virginia** | **D** | 30%/70%/100% bonus disallowance varies by tax year; recovery over remaining MACRS life | Conforms (post-2017 — federal $1.22M) | Conforms | 100% add-back yr 1, recover via state MACRS | MACRS life | Conforms; 80% rule; 20-yr CF | Conforms | Virginia historically had $25k §179 cap; now conforms to federal cap (verify) |
| 48 | Washington | N/A | — | — | — | — | — | — | — | No PIT; B&O is gross receipts |
| 49 | West Virginia | F | — | Conforms | Conforms | None | N/A | Conforms; 80% rule | Conforms | Rolling conformity |
| 50 | **Wisconsin** | **D** | Decoupled MACRS using pre-1986 Code provisions for some asset classes; current uses federal MACRS without bonus | Conforms (post-2014) | Conforms | Add-back federal bonus; recover via state MACRS | MACRS life | Conforms; 80% rule; 20-yr CF | Conforms | WI historically used pre-1986 IRC; complex legacy tracking |
| 51 | Wyoming | N/A | — | — | — | — | — | — | — | No PIT |

## 5. 50-State + DC Conformity Matrix (2025)

> **Verification reminder.** This matrix is a working reference only. State conformity legislation changes annually — verify against the current year's state Form instructions and statutes before relying. Particular volatility in: IA, IL, MN, NC (recent moves toward conformity), OBBBA conforming legislation pending in many states.

## 6. Add-back Mechanics — How Each Decoupling State Computes the Adjustment

### Pattern 1: 100% add-back / decoupled MACRS recovery (most common)

- **Pattern 1 mechanics** — Used by AZ, AR, GA, HI, ID, IL, MD, MA, MI, MS, NJ, NY, PA (CNI), SC, VT, VA, WI. **Year 1 mechanics:** 1. Compute federal depreciation including §168(k) bonus. 2. Compute state depreciation using regular MACRS *without* bonus on the same asset. 3. Add to state taxable income: (Federal depreciation) − (State MACRS depreciation). **Years 2-N mechanics:** - Each subsequent year of the asset's MACRS recovery period, compute the difference: (State MACRS depreciation) − (Federal depreciation). - This difference will typically be **positive** (subtraction from state taxable income) because the federal depreciation in year 1 absorbed so much basis that years 2-N have little federal depreciation remaining. - The total state subtractions over the asset's life equal the year-1 add-back, restoring parity.

### Pattern 2: Fixed-period straight-line recovery

**Fixed-period straight-line recovery states**

| State | Fraction added back yr 1 | Recovery schedule |
| --- | --- | --- |
| Connecticut | 100% | 25% per year, years 2-5 (4-year recovery) |
| Maine | 100% | 20% per year, years 2-6 (5-year recovery) |
| Minnesota | 80% | 20% per year, years 2-6 (5-year recovery), with 20% allowed in year 1 already |
| Ohio | 5/6 (83.33%) | 1/6 per year, years 1-6 (1/6 allowed yr 1; remaining 5/6 spread 1/6 per year over 5 more years) — total 6 yrs |

### Pattern 2: Fixed-period straight-line recovery

These fixed-period states do NOT use decoupled MACRS; the recovery is independent of the asset's actual recovery class.

### Pattern 3: California — full add-back, full state MACRS

- **California strictest pattern** — California is the strictest. Add back 100% of federal §168(k) bonus. State depreciation uses California MACRS (which itself differs from federal MACRS in some asset classifications, e.g., ADS lives for certain property). California §179 is capped at $25,000 with $200,000 investment phase-out.

### Pattern 4: §179-only differences

- **§179-only difference states and mechanics** — States with a §179 cap below federal but no bonus decoupling: - Indiana ($25,000 cap) - California ($25,000 cap) - New Jersey (partial caps and 50%-of-asset rules on certain property types) **Mechanics:** Add back the excess of federal §179 over state §179 cap. Recover via state MACRS over the asset's life.

### Decoupled MACRS recovery (Pattern 1)

- **Decoupled MACRS recovery mechanics** — The mechanical effect is that the asset's basis is recovered for state purposes over its full MACRS life (5, 7, 15, 20 years depending on class). The taxpayer maintains a **separate state depreciation schedule** showing: - Federal beginning basis - Federal §168(k) bonus + §179 + regular MACRS - State beginning basis (same) - State §168(k) (zero for decoupled states) - State §179 (state cap) - State regular MACRS (full schedule) - Cumulative state-federal difference (running balance) When the asset is sold or disposed, the state-federal basis difference must be **reconciled in the year of disposition** — typically by adjusting state gain/loss to reflect the remaining basis difference.

### Fixed-period recovery (Pattern 2)

- **Fixed-period recovery mechanics** — Simpler: the year-1 add-back is recovered in equal installments over the recovery period. If the asset is sold before full recovery, the **remaining unrecovered add-back is allowed as a subtraction in the year of sale** in most states. Verify state-specific rules.

### Special disposition rules

- **California:** Form 3885A reconciles state and federal depreciation; basis differences flow to Schedule D-1 / D for gain or loss.
- **New York:** Form IT-399 / CT-399 carries the running difference until disposition.
- **Maryland:** Form 500DM reconciles annually.

## 8. NOL Conformity Post-TCJA

- **Federal NOL rules post-TCJA** — TCJA changed federal NOL rules: - Losses arising in tax years beginning after 12/31/2017: **80% of taxable income limit**, **indefinite carryforward**, **no carryback** (except for farming and certain insurance). - Losses arising in tax years beginning before 1/1/2018: 2-year carryback, 20-year carryforward, 100% offset. CARES Act temporarily restored 5-year carryback for 2018-2020 NOLs (federal).

### State NOL conformity (summary)

**State NOL conformity summary table**

| State pattern | States |
| --- | --- |
| Fully conform to TCJA NOL rules | Most rolling-conformity states |
| Decouple — keep pre-TCJA 100% offset | California (decoupled; allows 100% NOL deduction historically), Massachusetts (corp), several others |
| Decouple — different carryforward years | Arkansas (5-yr CF), Pennsylvania (40-yr CF for some), Mississippi, Vermont |
| PIT-level: no NOL carryforward for individuals | New Jersey GIT, Pennsylvania PIT, Massachusetts PIT (Sch C losses limited) |

### State NOL conformity (summary)

> **Audit flash point — NJ and PA personal income tax.** New Jersey Gross Income Tax and Pennsylvania Personal Income Tax do NOT allow NOL carryforwards for individuals; losses are limited to offset same-category income in the same year. Federal Schedule C loss carryforwards do not flow to NJ-1040 or PA-40 the way they do federally.

## 9. §163(j) Business Interest Limitation Conformity

- **Federal §163(j) limitation** — Federal §163(j) limits business interest deductibility to: - 30% of adjusted taxable income (ATI) (TCJA), - Plus business interest income, - Plus floor plan financing interest. **Small business exception:** taxpayers with average annual gross receipts under $30M (2024 threshold, indexed) are exempt.

### State conformity summary

**§163(j) state conformity summary**

| Pattern | States |
| --- | --- |
| Conform to §163(j) (with own ATI definition) | Most |
| **Decouple — do NOT impose §163(j)** | California (Conformity Act doesn't pick up §163(j) for individuals); some others |
| Modified — own §163(j) computation | Tennessee (F&E); Wisconsin |

### State conformity summary

Sole proprietors and small SMLLCs are typically under the gross receipts threshold and unaffected. Re-verify for larger pass-throughs.

## 10. Practitioner Workflow — Maintaining Dual Depreciation Schedules

### Sample bookkeeping entry: depreciation add-back tracking schedule

For a $50,000 equipment purchase placed in service 2025 in California (decoupled state):

```
Asset: Equipment placed in service 2025-03-15
Cost: $50,000
MACRS class: 5-year property

FEDERAL DEPRECIATION (post-OBBBA, assuming 100% bonus, placed in service after 1/19/2025):
  2025: $50,000 (100% bonus depreciation)
  2026-2030: $0

CALIFORNIA DEPRECIATION (no bonus; §179 capped at $25,000):
  Assume taxpayer takes CA §179 of $25,000 on this asset.
  Remaining basis $25,000 depreciated using CA MACRS 5-year (200% DB, half-year convention):
    2025: $25,000 × 20.00% = $5,000
    2026: $25,000 × 32.00% = $8,000
    2027: $25,000 × 19.20% = $4,800
    2028: $25,000 × 11.52% = $2,880
    2029: $25,000 × 11.52% = $2,880
    2030: $25,000 × 5.76%  = $1,440
  CA Total: $25,000 §179 + $25,000 MACRS = $50,000 over 6 years

ADD-BACK / SUBTRACTION on Schedule CA (540):
  2025: Federal $50,000 − CA ($25,000 + $5,000) = ADD-BACK $20,000
  2026: Federal $0 − CA $8,000 = SUBTRACTION $8,000
  2027: Federal $0 − CA $4,800 = SUBTRACTION $4,800
  2028: Federal $0 − CA $2,880 = SUBTRACTION $2,880
  2029: Federal $0 − CA $2,880 = SUBTRACTION $2,880
  2030: Federal $0 − CA $1,440 = SUBTRACTION $1,440
  Total: $20,000 add-back − $20,000 subtractions = $0 net (parity over asset life)
```

### Tax software handling

**Tax software conformity handling table**

| Software | State depreciation tracking | Notes |
| --- | --- | --- |
| Intuit Lacerte | Strong — automatic state depreciation modules for all decoupling states | Asset module flows to state via "State If Different" override |
| Thomson Reuters UltraTax | Strong — state depreciation modules; auto-conformity update each year | State book on asset entry screen |
| Drake | Adequate — requires manual state book entry for decoupled states | Less automation than Lacerte/UltraTax |
| CCH Axcess Tax / ProSystem fx | Strong — Wolters Kluwer maintains state conformity database | "Override federal for state" toggle per asset |
| Intuit ProConnect | Adequate — state book derived from federal with override | Smaller-practice tool |
| Drake Documents | N/A — document management only | — |

### Tax software handling

**Best-practice workflow:**
1. **At asset entry:** flag the state of taxation. If decoupling state, populate both federal and state depreciation columns.
2. **Year-end review:** print the Federal-to-State Depreciation Reconciliation report. Verify the year-1 add-back equals the federal §168(k) bonus claimed.
3. **Disposition:** before booking a sale, run the "asset basis comparison" report to flag any remaining state-federal basis difference. Include this difference in the state gain/loss computation.
4. **Annual carryforward:** for fixed-period recovery states (CT, ME, MN, OH), maintain a separate annual schedule outside of MACRS depreciation reports (typically a spreadsheet) tracking the original add-back and remaining recovery installments.

## 11. Worked Examples

### Example 1 — California sole proprietor buying $50,000 of equipment

Facts:
- Maria, sole proprietor in California, places $50,000 of equipment in service on 2025-06-01.
- Property is 5-year MACRS.
- Federal: takes 100% §168(k) bonus depreciation (post-OBBBA, placed after 1/19/2025).
- California: takes §179 election for $25,000 (state cap) on this asset; remaining $25,000 depreciated under CA MACRS.

**Federal Schedule C:**
- Line 13 depreciation: $50,000

**California Form 540 / Schedule CA (540):**
- Federal AGI includes the $50,000 deduction
- Schedule CA (540) Section B — Subtractions/Additions column:
  - Add back $50,000 federal depreciation
  - Subtract $25,000 CA §179 + $5,000 CA MACRS year 1 = $30,000
  - **Net addition to CA taxable income: $20,000**

**Years 2026-2030:** No federal depreciation remains. CA depreciation continues per the schedule in Section 10 above. Each year a subtraction adjustment is made on Schedule CA (540). Total subtractions over the asset's life equal the year-1 add-back, achieving parity.

**Practitioner audit flash:**
- If Maria's 2026 preparer misses the $8,000 CA depreciation subtraction, her CA taxable income is overstated by $8,000 → CA tax overpayment of approximately $740 at her marginal 9.3% rate.
- Over the 6-year recovery cycle, missing each subtraction could result in $1,800+ in total CA tax overpayment.
- Statute of limitations on amended CA returns is generally 4 years; older overpayments may be lost.

### Example 2 — New Jersey multistate manufacturer

Facts:
- ABC LLC (single-member, owned by John, NJ resident) operates manufacturing equipment in NJ and PA.
- Apportionment: 60% NJ, 40% PA.
- Places $200,000 of 7-year MACRS equipment in service 2025-09-15.
- Federal: 100% §168(k) bonus depreciation = $200,000.
- §179 not elected.

**Federal Schedule C (John's Form 1040):** $200,000 depreciation.

**NJ-1040 Gross Income Tax (Schedule NJ-BUS-1):**
- NJ decouples from §168(k). Apply NJ MACRS 7-year schedule:
  - 2025: $200,000 × 14.29% = $28,580 (NJ depreciation, half-year convention)
- NJ add-back via apportionment: ($200,000 − $28,580) × 60% NJ apportionment = $102,852 add-back to NJ-source income for John's NJ GIT.
- Subsequent years: NJ MACRS deductions subtracted against same NJ-apportioned share.

**PA-40 Personal Income Tax:**
- PA PIT for Sch C uses federal depreciation by default (verify current PA Bulletin guidance for bonus depreciation).
- If PA decouples at PIT level: $200,000 − $28,580 = $171,420 × 40% PA apportionment = $68,568 add-back.
- If PA conforms at PIT level (federal flow-through): no add-back.

**Practitioner audit flash:**
- Misallocating the add-back to the wrong state's apportionment share is a common error.
- The add-back follows the **source** of the deduction (the federal depreciation) and is allocated under each state's apportionment formula.
- If John ceases NJ residency mid-year, the recovery subtractions in later years must be tracked against his then-residency status, potentially making part of the recovery unusable.

### Example 3 — Texas full-conformity (no PIT) sole prop

Facts:
- Pete, sole proprietor in Texas, places $50,000 of equipment in service 2025-04-01.
- Federal: 100% §168(k) bonus depreciation = $50,000.

**Federal Schedule C:** $50,000 depreciation.

**Texas state return:** None for personal income (no PIT).

**Texas Franchise Tax:** Pete is a sole prop (no LLC) — not subject to franchise tax. If he were an SMLLC:
- Form 05-102 (Public Information Report) required regardless.
- Total revenue under $2,470,000 → No Tax Due threshold met → no franchise tax owed.
- Bonus depreciation conformity at TX franchise level is irrelevant for a No Tax Due filer; relevant only for EZ Computation or Long Form filers above the threshold.

**Practitioner audit flash:**
- TX residents with **out-of-state** rental or business activity may file in decoupling states (e.g., CA, NY). The full federal bonus deduction flows freely on the Texas side, but the out-of-state filing requires a separate add-back schedule for that state.
- Common mistake: assuming "I'm in Texas so I don't have add-backs" — wrong if the taxpayer has out-of-state nexus.

## 12. Audit Flash Points Summary

> **AUDIT FLASH POINT 1 — Missing multi-year add-back tracking.** Once a state add-back is made in year 1, the recovery (subtraction) in years 2-N must be tracked for the asset's full life. Failure to claim the subtraction overstates state taxable income every year. Most common at firm transitions, prior-year file imports, and software migrations where asset records lose the state book.

> **AUDIT FLASH POINT 2 — §179 cap confusion.** States with §179 caps below federal (CA $25k, IN $25k, NJ partial) require a separate add-back computation. Practitioners frequently use the federal §179 election as the state amount, silently over-deducting in the state.

> **AUDIT FLASH POINT 3 — Multistate apportionment misallocation.** When a taxpayer has nexus in multiple decoupling states, each state's add-back must follow that state's apportionment formula. Don't assume the federal apportionment percentage applies to the add-back.

> **AUDIT FLASH POINT 4 — Disposition reconciliation missed.** When an asset is sold before its full state recovery period, the state-federal basis difference must be reconciled at disposition. Missing this overstates or understates state gain/loss.

> **AUDIT FLASH POINT 5 — Residency change mid-life.** A taxpayer who moves from a decoupling state to a non-PIT state mid-recovery may lose access to remaining state subtractions. Plan acquisitions and dispositions around residency changes.

> **AUDIT FLASH POINT 6 — Pass-through entity (PTE) tax interactions.** Where a state PTET election is in effect (e.g., NJ BAIT, NY PTET, CA PTE), bonus depreciation add-backs occur at the entity level. The owner's K-1 reflects state-modified income that already includes the entity-level add-back — don't add back again on the owner's personal return.

> **AUDIT FLASH POINT 7 — OBBBA state conformity lag.** State legislatures typically take 6-18 months to enact conformity bills after federal changes. The OBBBA §168(k) restoration may not yet be reflected in state conformity dates as of TY2025 filing. Verify each state's IRC conformity date against OBBBA enactment (7/4/2025).

### Primary sources

- **Federal:**
  - IRC §168(k) as amended by P.L. 119-21 (OBBBA, 7/4/2025) — verify Title VII provisions
  - IRC §179, Rev. Proc. 2024-40 (2025 inflation adjustments)
  - IRC §163(j) and Treas. Reg. §1.163(j)-1 through §1.163(j)-11
  - IRC §172 (NOL rules post-TCJA)
  - IRS Pub. 946 "How to Depreciate Property" (2025 edition)

- **State conformity:** each state's IRC conformity statute and current-year Form instructions:
  - California: R&TC §17024.5; FTB Pub. 1001
  - New York: NY Tax Law §612(b)(8); IT-225 instructions
  - New Jersey: N.J.S.A. 54A:5-1; Schedule NJ-BUS-1 instructions
  - Pennsylvania: 72 P.S. §7401; PA Schedule C-F Reconciliation
  - Illinois: 35 ILCS 5/203(b)(2)(E-10); Schedule M
  - Minnesota: Minn. Stat. §290.01 subd. 19; M1 instructions
  - Ohio: Ohio Rev. Code §5747.01(A); Schedule of Adjustments
  - Massachusetts: M.G.L. c. 62 §6F; Schedule B/E
  - Connecticut: Conn. Gen. Stat. §12-217; CT-1120 ATT
  - Virginia: Va. Code §58.1-301; Schedule ADJ

- **Tertiary references (verify before citing):**
  - CCH State Tax Smart Charts — Depreciation
  - RIA Checkpoint State & Local Tax Reporter
  - BNA Bloomberg Tax — State Tax Library

### Update frequency

This matrix should be re-verified annually after:
1. State legislative sessions end (typically June-September)
2. State annual conformity bills are enacted (typically by October)
3. State tax department guidance / FAQ updates (continuous)

### Verification status

- **last_updated:** 2025-11-15
- **verified_by:** pending — requires sign-off by a US tax practitioner credentialed under Circular 230 with multistate practice experience
- **next review:** 2026-Q1 after state legislative wrap-up

## 14. Reviewer Sign-off

This document is a reference reviewer-aid only. It does NOT replace state-specific verification for any particular client engagement. Every multistate return must be prepared against the current state form instructions and statute as of the return year, not against this matrix.

For any client engagement where state depreciation add-backs are material (typically >$10,000 in any single state), the reviewer must:
1. Confirm the current-year IRC conformity date for each state.
2. Re-verify the §179 cap and phase-out for each state.
3. Confirm the add-back methodology against the current-year form instructions.
4. Document the multi-year tracking schedule for each asset in the workpapers.

— End of US State Bonus Depreciation and §179 Conformity Matrix —

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
