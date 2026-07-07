---
name: tx-margin-tax
description: Deep content skill for the Texas Franchise (Margin) Tax imposed under Texas Tax Code Chapter 171.
jurisdiction: US-TX
domain: tax
tax_year: 2025
tier: 2
last_updated: 2026-07-06
---

# tx-margin-tax

## tx-margin-tax — Texas Franchise (Margin) Tax

Deep content skill for the Texas Franchise Tax ("margin tax") imposed under Texas Tax Code Chapter 171. Covers taxable entities doing business in Texas — corporations, LLCs, limited partnerships, LLPs, business trusts, and professional associations. Sole proprietors and general partnerships of natural persons are exempt. No-tax-due threshold is $2.47M total revenue (2024–2025 rate years). Retail/wholesale rate is 0.375%; standard rate is 0.75%. Margin equals the LOWEST of: total revenue × 70%; revenue minus COGS; revenue minus compensation; revenue minus $1M. Report due May 15; PIR/OIR mandatory. Tax year 2025 (report year 2026).

## 1. Scope

### 1.1 What this skill covers

This skill produces a complete Texas Franchise Tax computation and filing package for the **2026 report year**, which is based on the federal accounting period ending in **calendar year 2025**. Texas franchise tax is a *privilege* tax measured on a margin base — neither a pure income tax nor a sales tax — imposed for the privilege of doing business in the state.

The skill handles:

1. Determining whether an entity is a **taxable entity** under Tex. Tax Code §171.0002 or is exempt (sole prop, general partnership of natural persons, passive entity, exempt nonprofit).
2. Determining whether the entity is below the **no-tax-due threshold** of $2.47M of total revenue and whether it must still file the Public Information Report (PIR) or Ownership Information Report (OIR).
3. Computing **total revenue** from federal Form 1120, 1120-S, 1065, or Schedule C reconciliations, with the statutory exclusions of §171.1011.
4. Computing the **margin base** under §171.101 by selecting the lowest of the four statutory bases: 70% of total revenue; revenue minus COGS (§171.1012); revenue minus compensation (§171.1013); revenue minus $1,000,000.
5. Applying **single gross-receipts apportionment** under §171.106 (Texas gross receipts ÷ everywhere gross receipts), including the market-based sourcing rule for services adopted by 34 Tex. Admin. Code §3.591 effective for reports due on or after January 1, 2021.
6. Choosing between the **standard rate (0.75%)**, the **retail/wholesale reduced rate (0.375%)** under §171.002(b)–(c), and the **EZ Computation rate (0.331%)** under §171.1016 if the entity elects and qualifies.
7. Combined group reporting under §171.1014 when affiliates share more than 50% common ownership and conduct a unitary business.
8. Preparing the **Form 05-158-A/B Long Form** or **Form 05-169 EZ Computation Report**, plus the mandatory **Form 05-102 PIR** (corps and LLCs) or **Form 05-167 OIR** (LPs/partnerships).
9. Filing logistics — due date May 15, 2026; automatic extension via Form 05-164 to November 15, 2026; second extension only for mandatory electronic filers.
10. Penalty and interest computation under §171.362 and §111.060.

### 1.2 What this skill does NOT cover

- **Sales and use tax** — see `tx-sales-tax.md`. Franchise tax and sales tax are independent regimes.
- **Federal income tax** — the franchise tax computation references the federal accounting period but the federal return itself is built by `us-federal-return-assembly.md`.
- **Property tax** — handled at the county appraisal-district level; out of scope.
- **Unemployment insurance / payroll tax** — administered by the Texas Workforce Commission; out of scope.
- **Insurance company premium tax** and **banking** regimes — separate Chapter 221 and Chapter 222 frameworks.
- **Tiered-partnership election** beyond the basic mechanics — flagged for reviewer escalation.
- **Apportionment via the Comptroller's discretionary §171.106(f) method** — escalate.

### 1.3 Tax year and report year terminology

**Federal tax year vs Texas report year table**  _(Tex. Tax Code Chapter 171)_

| Federal tax year (accounting period ends) | Texas report year | Texas report due date |
| --- | --- | --- |
| 2024 (period ending 2024-12-31) | 2025 | 2025-05-15 |
| 2025 (period ending 2025-12-31) | 2026 | 2026-05-15 |

Texas uses **report year** terminology that is offset from the federal **tax year**: When the user says "my 2025 Texas franchise return," they almost always mean the **2026 report year** based on the federal 2025 accounting period. Confirm this terminology in the intake.

## 2. Who must file — taxable entities vs exempt

### 2.1 Taxable entities (Tex. Tax Code §171.0002(a))

- **Taxable entity categories** — An entity is a **taxable entity** if it falls within any of these categories AND is doing business in Texas: Corporations (C corps, S corps — Texas does not recognize S-corp passthrough for franchise tax purposes; both are taxable entities); Limited liability companies (LLCs), including single-member LLCs disregarded for federal tax; Banks (subject to Ch. 171 but with special rules); State limited banking associations; Savings and loan associations; Limited partnerships (LP); Limited liability partnerships (LLP); Professional associations (PA) and professional corporations (PC); Business trusts; Joint ventures; Joint stock companies; Holding companies; Any other legal entity not specifically excluded.  _(Tex. Tax Code §171.0002(a))_
- **Disregarded entities are still taxable for TX franchise tax** — A single-member LLC that is disregarded for federal income tax is still a **separate taxable entity** for Texas franchise tax. This is one of the most common compliance traps for freelancers who form an LLC for liability protection and assume the franchise tax follows the federal disregarded treatment. It does not.  _(Tex. Tax Code §171.0002(a))_

### 2.2 Non-taxable / exempt entities (§171.0002(b)–(d))

- **Sole proprietorships** — Not a separate legal entity; not taxable.  _(§171.0002(b)–(d))_
- **General partnerships (all-natural-person owners)** — General partnerships the *direct* owners of which are **all natural persons** — exempt. Note the natural-persons requirement: if even one partner is an LLC or corporation, the GP becomes a taxable entity.  _(§171.0002(b)–(d))_
- **Passive entities** — Passive entities under §171.0003 — at least 90% of federal gross income is from passive sources (dividends, interest, royalties, capital gains from sale of real property, net gains from sale of commodities/securities, distributive shares from passive partnerships) AND not more than 10% from active conduct of a trade or business. Passive entities are exempt from franchise tax, but the old No Tax Due Report was discontinued for report years 2024 and later; verify the entity-specific PIR/OIR or exemption filing path with the Comptroller.  _(§171.0003)_
- **REITs** — Real Estate Investment Trusts (REITs) meeting §856 of the IRC and the Texas qualification rules.  _(§171.0002(b)–(d))_
- **Nonprofits exempt under §171.063** — Nonprofits exempt under §171.063 (federal §501(c)(3), (4), (8), (10), (19) and similar) — must apply for the exemption with the Comptroller (Form AP-204).  _(§171.063)_
- **Insurance companies subject to premium tax** — Insurance companies subject to premium tax under Ch. 221.  _(Ch. 221)_
- **Open-end investment companies** — Open-end investment companies registered under the Investment Company Act of 1940.  _(§171.0002(b)–(d))_

### 2.3 The "doing business in Texas" nexus standard

- **Nexus standard** — Nexus is established under §171.001 if the entity: Is organized in Texas, OR Has a Texas physical presence (office, employee, property, inventory), OR Has **economic nexus**: $500,000 or more of Texas gross receipts in a federal accounting period, under 34 Tex. Admin. Code §3.586 effective for reports due on or after January 1, 2020.  _(§171.001; 34 Tex. Admin. Code §3.586)_
- **Economic nexus threshold** — $500,000 USD (Texas gross receipts in a federal accounting period; independent of the $2.47M no-tax-due threshold — an out-of-state entity with $600K of Texas sales has nexus and must file, but owes no tax because it is below the $2.47M threshold.)  _(34 Tex. Admin. Code §3.586)_

### 2.4 Foreign entities — qualification with the Secretary of State

- **Foreign entity registration and obligation** — A foreign entity transacting business in Texas must register with the Texas Secretary of State (Form 304 or 313 depending on entity type) and obtain a Certificate of Authority. The franchise tax obligation exists independent of registration: an unregistered foreign LLC with Texas nexus still owes franchise tax and the Comptroller can assess it.

## 3. The no-tax-due threshold and the post-2024 filing simplification

### 3.1 The $2.47M threshold

- **No-tax-due threshold, report years 2024 and 2025** — $2,470,000 USD (Total revenue; federal accounting periods ending in 2023 and 2024 respectively)  _(§171.006)_
- **No-tax-due threshold, report years 2026 and 2027** — $2,650,000 USD (Published by the Texas Comptroller; biennially indexed for inflation. If the Comptroller publishes a later biennial indexation effective January 1, 2026, use that. The 2024–2025 figure of $2.47M is the safe default until indexation is reconfirmed.)  _(§171.006)_
- **Effect of being at or below threshold** — If total revenue (apportioned and combined-group-aware) is **at or below** $2,470,000, the entity owes **$0** in franchise tax. The historical practice was to file **Form 05-163 No-Tax-Due Information Report** to claim the threshold. This has changed materially.  _(§171.006)_

### 3.2 HB 1361 (88th Legislature, 2023) — elimination of the No-Tax-Due Report

- **Elimination of No-Tax-Due Report requirement** — Effective for **reports originally due on or after January 1, 2024**, House Bill 1361 amended §171.204 to **eliminate the requirement** that taxable entities file a No-Tax-Due Report (Form 05-163) when total revenue is at or below the no-tax-due threshold. The Comptroller implemented this by retiring Form 05-163 for the 2024 and later report years.  _(§171.204 (HB 1361, 88th Legislature, 2023))_
- **Practical effect for the 2026 report year** — 1. If total revenue ≤ $2,470,000: **no franchise tax return** (Forms 05-158 / 05-169 / 05-163) is required. 2. BUT the entity **must still file** the appropriate information report: - **Form 05-102 Public Information Report (PIR)** — for corporations, LLCs, banks, professional associations, financial institutions. - **Form 05-167 Ownership Information Report (OIR)** — for partnerships (LP/LLP) and other entities not required to file a PIR. 3. The PIR/OIR is still due **May 15, 2026**. 4. Failure to file the PIR/OIR results in forfeiture of corporate privileges under §171.251 even though no tax is owed. This simplification removes paperwork for the ~95% of Texas entities that fall below the threshold but does **not** eliminate the PIR/OIR — that remains a hard requirement.  _(§171.251; HB 1361)_

### 3.3 Passive entity certification

- **Annual passive entity certification** — Passive entities under §171.0003 still must file an **annual certification** that the entity meets the 90% passive income test. For report years 2024+, this certification is incorporated into the PIR (an attestation block on Form 05-102). The standalone "Form 05-163 Passive" is retired.  _(§171.0003)_

### 3.4 Decision tree

```
Total revenue (apportioned) ≤ $2,470,000?
│
├── YES → No franchise tax return required.
│        File PIR (05-102) or OIR (05-167) by May 15.
│        Tax due = $0.
│
└── NO  → Franchise tax return required.
         File 05-158-A/B Long Form OR 05-169 EZ Computation.
         Plus PIR (05-102) or OIR (05-167).
         By May 15 (or November 15 with Form 05-164 extension).
```

## 4. Rate selection

### 4.1 Three statutory rates

**Three statutory rates table**  _(§171.002(b)-(c); §171.1016)_

| Rate | Applies to | Statute |
| --- | --- | --- |
| 0.375% | Entities primarily engaged in retail or wholesale trade | §171.002(c) |
| 0.75% | All other taxable entities (the "standard" rate) | §171.002(b) |
| 0.331% | EZ Computation: any entity with total revenue ≤ $20M that elects | §171.1016 |

- **0.375%** — Entities primarily engaged in retail or wholesale trade  _(§171.002(c))_
- **0.75%** — All other taxable entities (the "standard" rate)  _(§171.002(b))_
- **0.331%** — EZ Computation: any entity with total revenue ≤ $20M that elects  _(§171.1016)_

### 4.2 Retail/wholesale qualification (§171.002(c))

- **Requirements to use 0.375% rate** — To use the 0.375% rate, the entity must satisfy ALL of: 1. **Primary business activity** is retail (NAICS sectors 44–45) or wholesale (NAICS sector 42). "Primarily engaged" means **more than 50%** of total revenue from retail/wholesale activities. 2. **Less than 50% of revenue** from products the entity (or an affiliate) **manufactures, produces, or acquires for sale to a related party**. This excludes vertically integrated manufacturers from the reduced rate. 3. The entity is **not** primarily engaged in providing retail or wholesale **utilities** (electricity, gas, telecom — these stay at 0.75%). 4. Not primarily engaged in the **rental or leasing** of tangible personal property (but auto rental and heavy equipment rental have special treatment under §171.002(c-1)).  _(§171.002(c))_

**Common 0.375% qualifiers:** brick-and-mortar retailers, e-commerce retailers, restaurants (under 34 TAC §3.584(b)(4)(B)), wholesale distributors, auto dealers.

**Common 0.75% (standard) entities:** SaaS, consulting, professional services, construction, manufacturing, real estate.

### 4.3 EZ Computation election (§171.1016)

- **EZ Computation mechanics and eligibility** — The EZ method is a simplified alternative available to any taxable entity with **total revenue ≤ $20,000,000** (also indexed; verify). The mechanics: - Tax = (Total revenue × Apportionment factor) × **0.331%** - No COGS or compensation deduction is allowed. - No tiered partnership netting. - File **Form 05-169** instead of 05-158-A/B. - The election is annual — the entity can switch year to year.  _(§171.1016)_

**When EZ saves money:** When the long-form margin (after COGS or compensation) is close to 70% of revenue and the long-form rate is 0.75%. Compare:

- Long form (standard): 70% × revenue × 0.75% = **0.525% of revenue**
- Long form (retail): 70% × revenue × 0.375% = **0.2625% of revenue**
- EZ: 100% × revenue × 0.331% = **0.331% of revenue**

The EZ rate beats the standard long-form rate (0.525%) whenever the long-form margin selection cannot get below 70% of revenue — which is common for service businesses with thin COGS and modest compensation. For retailers eligible for 0.375%, the long form usually wins.

### 4.4 Rate decision algorithm

- **Rate decision algorithm** — ``` 1. Is total revenue > $20M? YES → Long form mandatory. Choose retail (0.375%) if §171.002(c) qualified, else 0.75%. NO  → Continue to step 2. 2. Compute long-form tax under best margin base + best rate (retail vs standard). 3. Compute EZ tax: revenue × apportionment × 0.331%. 4. Choose the lower. Document both computations in the workpaper. ```  _(§171.002; §171.1016)_

## 5. Margin calculation — the 4-way computation

### 5.1 Statutory framework (§171.101)

**4-way margin base table**  _(§171.101)_

| # | Base | Statute |
| --- | --- | --- |
| 1 | Total revenue × **70%** | §171.101(a)(1)(A) |
| 2 | Total revenue **minus COGS** | §171.101(a)(1)(B)(ii)(a) |
| 3 | Total revenue **minus compensation** (officer cap applies) | §171.101(a)(1)(B)(ii)(b) |
| 4 | Total revenue **minus $1,000,000** | §171.101(a)(1)(B)(ii)(c) |

- **1** — Total revenue × **70%**  _(§171.101(a)(1)(A))_
- **2** — Total revenue **minus COGS**  _(§171.101(a)(1)(B)(ii)(a))_
- **3** — Total revenue **minus compensation** (officer cap applies)  _(§171.101(a)(1)(B)(ii)(b))_
- **4** — Total revenue **minus $1,000,000**  _(§171.101(a)(1)(B)(ii)(c))_
- **Margin equals lowest of four bases; election rule** — Margin = the **LOWEST** of the four bases. The taxpayer **elects** which base to use each report year. The election is irrevocable for that year once the report is filed but can be changed in a subsequent year. In practice the taxpayer will always pick the lowest base because that produces the lowest margin and the lowest tax. The workpaper must show all four computations.  _(§171.101)_

### 5.2 Total revenue (§171.1011)

- **Total revenue build by entity type** — Total revenue is **derived from the federal return** with statutory inclusions and exclusions. Start from: - **C corp** (Form 1120): Line 1c gross receipts + Line 4 dividends + Line 5 interest + Line 6 gross rents + Line 7 gross royalties + Line 8 capital gain + Line 9 net gain Form 4797 + Line 10 other income — modify per §171.1011. - **S corp** (Form 1120-S): Line 1c + Line 4 + Line 5 (similar build). - **Partnership** (Form 1065): Line 1c + Line 4 + Line 5 + Line 6 + Line 7. - **Single-member LLC disregarded** (Schedule C): Line 1 gross receipts + other income items.  _(§171.1011)_
- **Mandatory exclusions from total revenue** — **Mandatory exclusions** from total revenue (§171.1011(g)–(v)) — non-exhaustive: - Bad debt expense allowed as a federal §166 deduction (g) - Foreign royalties and dividends to the extent included in federal income (j) - Net distributive income from a pass-through that is itself a taxable entity (k) — prevents double-counting in tiered structures - Flow-through funds mandated by law or fiduciary duty (sales tax collected, excise tax collected, escrow funds) (f) - Subcontractor payments for certain industries (lawyers' client trust disbursements (m), pharmacy networks (n), staff leasing services (s), certain healthcare providers (p)–(q)) - Federal income tax refunds  _(§171.1011(g)–(v))_

### 5.3 Base 1: Total revenue × 70%

The simplest base. No documentation burden. Always available as a **floor / safety net** — the taxpayer can always elect 70% even if COGS or compensation calculations would be messy. Common choice for service businesses with no COGS and modest compensation.

### 5.4 Base 2: Total revenue minus COGS (§171.1012)

- **Texas COGS is a distinct statutory construct** — **Texas COGS is its own statutory construct** — it is **not** federal COGS. Read §171.1012 carefully because the Texas definition is broader than federal §263A in some respects and narrower in others.  _(§171.1012)_
- **Includable COGS items** — **Includable COGS items (§171.1012(c)–(d)):** - Direct materials and supplies consumed in production - Direct labor (production workers, not officers or owners) - Production-related rent, utilities, depreciation, repairs of production facilities - Quality control, R&D in some cases (§171.1012(d)(8)) - Geophysical/geological costs (for oil & gas) - Production-related insurance, taxes, licenses  _(§171.1012(c)–(d))_
- **Excludable COGS items** — **Excludable COGS items (§171.1012(e)):** - Selling costs (commissions, advertising, distribution after production) - Officer compensation (always — even if officers do production work) - Idle facility costs - Distribution costs not mandated by law (transportation to customer) - Federal income tax - Strike costs  _(§171.1012(e))_
- **Service providers generally cannot use COGS** — **Service providers** generally cannot use COGS — §171.1012(a)(3)(A) defines "goods" as real or tangible personal property. Pure service businesses (consulting, SaaS, legal, accounting) get **no COGS deduction** and default to compensation or 70%.  _(§171.1012(a)(3)(A))_
- **Construction contractor subcontractor COGS election** — **Construction contractors** under §171.1012(i) have a special election to include subcontractor costs in COGS even though those are services — a major industry-specific carve-out.  _(§171.1012(i))_
- **Mixed transactions allocation** — **Mixed transactions** — if the entity sells both goods and services, only the goods-portion COGS qualifies. Allocate by revenue ratio.

### 5.5 Base 3: Total revenue minus compensation (§171.1013)

- **Compensation includes** — **Compensation includes:** - W-2 wages and salaries (Form W-2 Box 5 Medicare wages, *not* Box 1 federal wages — Texas uses Medicare base) - §401(k), §403(b), and similar deferrals are **already included** in Box 5; do not add again - Employer-paid health insurance, group-term life under $50K, dependent care assistance — **add back** to the extent not in Box 5 - Employer §401(k) match contributions — **add** (deductible under §171.1013(b)(1)(B)) - Employer health insurance premiums — **add** (deductible under §171.1013(b)(2)) - Employer workers' comp premiums — **add**  _(§171.1013)_
- **Compensation cap per person, report years 2024–2025** — $450,000 USD per person (For report year 2024–2025 the cap is $450,000 per individual employee or officer.)  _(§171.1013)_
- **Compensation cap per person, report years 2026–2027** — $480,000 USD per person (Published by the Texas Comptroller for report years 2026 and 2027. The 2024–2025 figure remains $450,000.)  _(§171.1013)_
- **Officer compensation and 1099 contractor treatment** — **Officer compensation** is fully deductible up to the cap, in contrast to COGS where officer pay is excluded entirely. This means a closely-held service business that pays the owner $400K W-2 can shelter $400K under compensation but $0 under COGS. **1099 contractors are NOT compensation** under §171.1013 — they are not W-2 employees of the taxable entity. (Construction subcontractors may qualify under the §171.1012(i) COGS election; that is a separate path.)  _(§171.1013)_
- **Compensation excluded items** — **Compensation excluded items:** - Stock-based compensation under §171.1013(b)(1)(A) is included only to the extent of W-2 Box 5 reporting (ISO/ESPP gains not in Medicare wages are excluded) - Severance pay — included - Sign-on bonuses — included if in Box 5 - Independent contractor payments — excluded - Payments to partners that are not on a W-2 — excluded (partner guaranteed payments do **not** qualify as compensation)  _(§171.1013(b)(1)(A))_

### 5.6 Base 4: Total revenue minus $1,000,000

- **Base 4 description and applicability** — A flat $1M deduction. No qualification required. Available to every taxable entity. Best for entities with revenue between $2.47M and ~$3.5M where neither COGS nor compensation produces a lower margin than 70% × revenue but $1M reduces it further.

Example: Revenue $3M, no COGS, $200K compensation.

- Base 1: $3M × 70% = $2.1M
- Base 2: N/A (no goods)
- Base 3: $3M − $200K = $2.8M
- Base 4: $3M − $1M = **$2.0M** ← LOWEST

### 5.7 Worked example of the 4-way

**Facts.** Texas LLC, software development services for U.S. customers. Federal tax year 2025. Total revenue $3,500,000. No tangible goods. W-2 compensation paid to 5 employees: $250K each = $1,250,000. Owner draws are not W-2 (LLC disregarded — owner takes distributions). Employer health $40K. Employer 401(k) match $30K. All revenue sourced to Texas (apportionment = 100%).

**Compensation computation:** $1,250,000 W-2 + $40K health + $30K 401(k) match = $1,320,000. Each employee is at $250K, well under the $450K cap. Owner draws excluded (not W-2).

**Margin bases table**

| Base | Computation | Result |
| --- | --- | --- |
| 1: 70% revenue | $3.5M × 0.70 | $2,450,000 |
| 2: − COGS | N/A (services) | — |
| 3: − Compensation | $3.5M − $1.32M | $2,180,000 |
| 4: − $1M | $3.5M − $1M | $2,500,000 |

- **1: 70% revenue** — $3.5M × 0.70  _($2,450,000)_
- **2: − COGS** — N/A (services)  _(—)_
- **3: − Compensation** — $3.5M − $1.32M  _($2,180,000)_
- **4: − $1M** — $3.5M − $1M  _($2,500,000)_

**LOWEST = Base 3** ($2,180,000).

**Tax (long form, standard rate):** $2,180,000 × 100% apportionment × 0.75% = **$16,350**.

**Compare EZ:** $3,500,000 × 100% × 0.331% = $11,585. **EZ wins by $4,765.** Elect EZ via Form 05-169.

This example illustrates why the workpaper must run both long form and EZ for any entity under $20M revenue.

## 6. The EZ Computation in detail

### 6.1 Mechanics

- **EZ Computation formula** — ``` EZ tax = Total revenue × Apportionment factor × 0.331% ``` No deductions for COGS, compensation, or the $1M.  _(§171.1016)_

### 6.2 Eligibility

- **EZ eligibility criteria** — - Total revenue (after §171.1011 adjustments) ≤ **$20,000,000** for the report year. Indexed. - Available to combined groups using combined total revenue. - No additional industry restrictions.  _(§171.1016)_

### 6.3 When EZ beats long form

- **EZ vs long-form breakeven analysis** — The breakeven analysis. Define R = total revenue, M = optimal long-form margin selected from the 4-way, r_LF = long-form rate (0.75% or 0.375%), f = apportionment factor. - Long form tax = M × f × r_LF - EZ tax = R × f × 0.331% EZ is cheaper when M × r_LF > R × 0.331%, i.e. M/R > 0.331%/r_LF. - For standard 0.75%: M/R > 0.4413 → EZ wins if margin ratio exceeds 44.1% of revenue. - For retail 0.375%: M/R > 0.8827 → EZ wins only if margin > 88.3% of revenue (very rare — retailers normally beat EZ).

**Heuristic:**

- Service business (standard rate, thin COGS): EZ almost always wins.
- Retailer/wholesaler (0.375% rate): EZ rarely wins.
- Consultant with high owner compensation: Long form (compensation base) often wins because compensation pushes margin below 44% of revenue.

### 6.4 Form 05-169 fields

- **Form 05-169 field list** — - Line 1: Total revenue from Forms (compute per §171.1011) - Line 2: Gross receipts in Texas - Line 3: Gross receipts everywhere - Line 4: Apportionment factor = Line 2 / Line 3 - Line 5: Apportioned revenue = Line 1 × Line 4 - Line 6: Tax = Line 5 × 0.331% Plus the discount-based tax credits under §171.0021 — discontinued for report years 2008 onward, ignore for 2026.  _(§171.1011; §171.0021)_

## 7. Apportionment — single gross-receipts factor

### 7.1 The formula (§171.106)

- **Apportionment factor formula** — Margin (or revenue, for EZ) is apportioned by a **single factor**: ``` Apportionment factor = Texas gross receipts / Total gross receipts everywhere ``` Texas is one of the few states that uses **single-factor** apportionment — no payroll or property factor.  _(§171.106)_

### 7.2 Texas gross receipts (§171.103)

- **Sourcing rules by transaction type** — - **Sale of tangible personal property**: sourced to Texas if delivered to a Texas purchaser (destination-based). - **Sale of real property**: located in Texas. - **Rental of real property**: located in Texas. - **Rental of tangible personal property**: located in Texas at the time of rental. - **Services**: **market-based** — sourced to Texas if the **service is performed in Texas** OR the benefit is received in Texas. Effective for reports due on or after January 1, 2021, the Comptroller adopted market-based sourcing for services in 34 Tex. Admin. Code §3.591(e)(26), reversing the previous "cost of performance" test. For services to a business customer, source to Texas if the customer's principal place of business or office that uses the service is in Texas. For services to an individual, source to Texas if the individual is a Texas resident. - **Intangibles** (royalties, licenses, software-as-a-service treated as intangibles): sourced to the legal domicile of the payor. - **Loans**: sourced to the location of the borrower's business or residence. - **Securities sold by a securities broker**: sourced to the location of the broker's customer.  _(§171.103; 34 Tex. Admin. Code §3.591(e)(26))_

### 7.3 SaaS sourcing — a frequent ambiguity

- **SaaS sourcing rule** — SaaS is treated as a service for Texas franchise tax sourcing in most cases — 34 TAC §3.591 was amended in 2021 to confirm that "the use of computer software accessed remotely" is sourced to the customer's location. A SaaS company headquartered in Austin selling to a California customer sources that revenue to California, not Texas. Pre-2021 audits often applied the old "location of the server" test for SaaS. For report years 2021+, the market-based test controls.  _(34 Tex. Admin. Code §3.591)_

### 7.4 Throwback / throwout rules

- **No throwback rule in Texas** — Texas does **not** have a throwback rule. Receipts from sales into states where the seller is not taxable simply fall out of the Texas numerator without being thrown back to Texas. This is favorable to Texas-based exporters and to drop-shippers.

### 7.5 Worked apportionment example

Texas LLC, SaaS for business customers. Total revenue $5M. Customer principal-office locations:

- Texas customers: $1.2M (24%)
- California customers: $2.0M (40%)
- Other U.S. states: $1.5M (30%)
- EU customers: $0.3M (6%)

**Apportionment numerator** (TX receipts): $1,200,000.
**Apportionment denominator** (everywhere receipts): $5,000,000.
**Apportionment factor:** 0.2400 (24.00%).

If the entity uses EZ at 0.331%: $5,000,000 × 0.24 × 0.00331 = **$3,972**.

If the entity uses long form at standard rate with compensation deduction reducing margin to $3M: $3,000,000 × 0.24 × 0.0075 = **$5,400**.

EZ wins by $1,428.

## 8. Combined groups (§171.1014)

### 8.1 When combined reporting is required

- **Mandatory combined reporting conditions** — Mandatory combined reporting when: 1. Two or more taxable entities have **more than 50% common ownership** (direct or indirect, by vote or by value), AND 2. The entities are engaged in a **unitary business** under the federal Mobil Oil three-factor test (functional integration, centralization of management, economies of scale). Common ownership is tested by §171.0001(4) and §171.0001(2): it includes ownership by a common parent corporation, partnership, individual, or trust. Constructive ownership rules of §267(c) apply.  _(§171.1014; §171.0001(4); §171.0001(2); §267(c))_

### 8.2 Mechanics

- **Combined reporting mechanics** — - A **single combined report** is filed by the **reporting entity** (typically the largest member or the parent). - **One $2.47M no-tax-due threshold** applies to the entire group, not per member. This is a significant anti-fragmentation rule — splitting a $10M business into four $2.5M LLCs does **not** avoid franchise tax if they are unitary. - **Combined total revenue** = sum of each member's total revenue, then **eliminate** intercompany transactions per §171.1014(c)(1). - **Combined margin** = computed at the group level by the 4-way test (the group elects one base — apply the test to combined revenue, combined COGS, combined compensation). - **Apportionment factor** = combined Texas receipts ÷ combined everywhere receipts. Joyce vs Finnigan: Texas follows **Finnigan** for combined groups — receipts of any member into Texas count even if that specific member lacks nexus. - **PIR** must be filed by each member that is a corporation or LLC; the group does not file a single PIR.  _(§171.1014(c)(1))_

### 8.3 The "passive entity" trap in combined groups

- **Passive entity exclusion from combined group** — A passive entity affiliated with an active business is **excluded** from the combined group under §171.1014(a)(2). This permits planning by isolating passive holdings (real estate, intangibles) in a separate passive LLC. However, the passive entity must independently meet the §171.0003 90% test — partial passive doesn't qualify.  _(§171.1014(a)(2); §171.0003)_

### 8.4 Disregarded entities in combined groups

- **Disregarded entities as separate group members** — A federally disregarded entity is **its own taxable entity** for Texas franchise tax (see §2.1). In a combined group, the disregarded entity is a separate member of the group; it does not collapse into its parent.

## 9. Public Information Report (PIR) and Ownership Information Report (OIR)

### 9.1 Form 05-102 PIR — corporations and LLCs

- **Who files and what's reported** — **Who files:** Every corporation (C, S, professional), LLC (single-member or multi-member), bank, savings & loan, professional association. **What's reported:** - Entity name, Texas taxpayer number, FEIN - Mailing address, principal office address - Officers and directors (corporations) — name, title, mailing address, term expiration. Owner-only LLCs list the manager(s) or member-manager(s). - Members or managers of an LLC - Registered agent name and address (must match Secretary of State records) - Owner information: name and percentage ownership of any person owning ≥ 10% - For passive entities, the §171.0003 attestation - Officer/director signature under penalty of perjury **Filing:** Submitted with the franchise tax return (05-158 / 05-169) or filed standalone if below threshold. Due **May 15**.  _(§171.0003)_

**Privacy:** PIR data is publicly available through the Comptroller's online lookup at https://comptroller.texas.gov/taxes/franchise/. Officer names and addresses are visible. Some closely-held businesses use a registered agent address for officers to mitigate this.

### 9.2 Form 05-167 OIR — partnerships and other non-PIR entities

- **Who files and what's reported** — **Who files:** Limited partnerships (LP), LLPs, professional partnerships, and other taxable entities that are NOT corporations or LLCs. **What's reported:** Owner/partner names, addresses, and percentage interests. No officer/director list (partnerships don't have these). General partners are identified. Registered agent and principal office. **Filing:** Same as PIR — May 15 due date.

### 9.3 Consequence of non-filing

- **Forfeiture consequences under §171.251** — Under §171.251, failure to file the PIR or OIR results in **forfeiture of the entity's right to transact business in Texas**. The Comptroller publishes the entity as "Forfeited" on the public franchise tax status. Forfeiture means: - Loss of right to sue or defend in Texas courts under §171.252 - Personal liability of officers and directors for the entity's debts incurred during the forfeiture period under §171.255 - Eventual involuntary termination by the Secretary of State Cure: file the missing PIR/OIR and pay a $50 late filing penalty plus any franchise tax due. The entity is reinstated. This penalty is asymmetric — a missing $0-tax PIR can still trigger personal liability under §171.255. Reviewers must treat PIR filing as a hard deadline.  _(§171.251; §171.252; §171.255)_

## 10. Filing logistics and extensions

### 10.1 Due dates

- **Due dates for annual, final, and first-year reports** — - **Annual report:** May 15 each year, based on the federal accounting period ending in the prior calendar year. For the 2026 report year, the original due date is **May 15, 2026** (a Friday — no weekend adjustment needed). - **Final report:** Due 60 days after the entity ceases doing business in Texas. - **First-year report ("initial report"):** Due May 15 of the year **after** the entity's first calendar year of nexus. New entities are not first-year liable until the second May 15 after formation under §171.151. Example: LLC formed June 1, 2025 — first franchise report due May 15, 2026 (the 2026 report year, covering the federal period ending December 31, 2025).  _(§171.151)_

### 10.2 Extension — Form 05-164

- **Automatic extension to November 15** — A single automatic extension to **November 15** is available by filing Form 05-164 by May 15 and paying: - For mandatory EFT taxpayers (prior-year tax > $10K): 90% of current-year liability OR 100% of prior-year tax. - For non-EFT taxpayers: 100% of prior-year tax OR 90% of current year. A failure to pay the required extension amount voids the extension and re-imposes May 15 penalties.

### 10.3 Second extension

- **Second extension for mandatory EFT filers** — Only for mandatory EFT filers — extends from November 15 to **August 15 of the following year**. Rare.

### 10.4 Mandatory electronic filing

- **Electronic filing threshold and methods** — Required if prior-year franchise tax owed was > $10,000. Use the Comptroller's **WebFile** system or an approved third-party software (most major tax software supports it). Paper filing is permitted for sub-$10K entities but not recommended.

### 10.5 Payment

- **Payment methods** — Tax is paid by: - ACH debit through WebFile (free) - Credit card (2.25% convenience fee, third-party processor) - Paper check with Form 05-170 voucher (sub-$10K only) - TEXNET wire (mandatory EFT filers)

### 10.6 Federal deductibility

- **Federal deductibility of margin tax** — The Texas franchise (margin) tax **is deductible on the federal return** as a state income tax under IRC §164(a)(3). The IRS has accepted (Rev. Rul. 2008-32 and subsequent CCA memoranda) that the Texas margin tax is "based on net income" notwithstanding the margin construct, and therefore qualifies as a state income tax rather than a non-deductible privilege tax. For C corps it is fully deductible on Form 1120 Line 17 (taxes and licenses). For pass-throughs, it flows through to the owner subject to the **$10,000 SALT cap** under §164(b)(6) for individual owners — but Texas's adoption of the **Pass-Through Entity Tax** (PTET) is **not** available because Texas has no pass-through entity income tax election (Texas SB 113 etc. do not exist; Texas's only PTET-style workaround is to pay the franchise tax at the entity level, which already happens because the margin tax is an entity-level tax — so the SALT cap does not apply to the margin tax itself for owners). In short: an LLC pays its franchise tax with entity funds; the LLC deducts it on the federal return (Schedule C, 1065, or 1120); the deduction reduces federal taxable income before flow-through. The owner does not separately deduct it. The $10K SALT cap is not implicated.  _(IRC §164(a)(3); Rev. Rul. 2008-32; §164(b)(6))_

## 11. Penalties and interest

### 11.1 Late filing penalty (§171.362)

- **Late filing penalty structure** — - **$50 flat penalty** for late filing if the report is filed at any point after the due date, regardless of tax owed. Applies even to $0-tax PIRs. - Plus, if tax is owed: - **5% of tax due** if filed/paid 1–30 days late. - **10% of tax due** if filed/paid more than 30 days late.  _(§171.362)_

### 11.2 Interest (§111.060)

- **Interest accrual rate** — Interest accrues on unpaid tax from the due date at the **prime rate plus 1%**, set by the Comptroller annually. For 2024 the rate was 9.5%; for 2025 it is 9.0% (verify on the Comptroller's site — rate posted each January 1). Interest compounds daily.  _(§111.060)_

### 11.3 Forfeiture (§171.251)

- **Forfeiture trigger** — If the entity fails to file or pay for 120 days past the due date (and is not in extension), the Comptroller initiates forfeiture proceedings. See §9.3 for the cascade of consequences.  _(§171.251)_

### 11.4 Fraud penalty (§111.061)

- **Fraud penalty rate and escalation** — 50% of underpayment attributable to fraud. Reviewer escalation required if fraud is suspected — do not handle through this skill.  _(§111.061)_

### 12.1 Example A — SaaS LLC under the no-tax-due threshold

**Facts.**
- Texas single-member LLC formed January 2023, federally disregarded.
- Federal tax year 2025 ends December 31, 2025.
- Texas report year: 2026, due May 15, 2026.
- Total revenue (Schedule C Line 1 gross receipts adjusted for §171.1011): $480,000.
- Customers: 60% Texas, 40% other U.S. states. Apportionment factor 0.60.
- Owner takes draws (no W-2 to himself); one W-2 employee at $80,000.

**Analysis.**

1. **Taxable entity?** Yes — the LLC is a separate taxable entity for Texas franchise tax even though federally disregarded.
2. **Apportioned total revenue:** $480,000 × 0.60 = $288,000.
3. **No-tax-due threshold:** $288,000 < $2,470,000. **Below threshold. Tax due = $0.**
4. **Filing requirement:** Under HB 1361 post-2024 simplification, **no franchise tax return** (Forms 05-158 / 05-169) is required. PIR (Form 05-102) is still required.
5. **PIR deadline:** May 15, 2026.

**Deliverable.** File only Form 05-102 PIR listing the owner-manager, the registered agent, and the entity addresses. Tax due $0. No long form. No EZ form. Done.

**Owner action items.**
- File Form 05-102 PIR by May 15, 2026 via WebFile.
- Maintain franchise tax workpaper showing the threshold computation in case of audit.
- Confirm registered agent address still matches Secretary of State records (else update via Form 401).

### 12.2 Example B — Texas retailer at 0.375%

- Texas LLC operating a retail furniture store and an e-commerce site.
- Federal tax year 2025, 2026 report year.
- Total revenue: $4,200,000.
- COGS (Texas §171.1012 definition): direct furniture purchase costs $2,000,000 + direct sales-floor labor $300,000 + showroom rent and utilities $180,000 = $2,480,000.
- W-2 compensation including officers (capped per person at $450K): $720,000.
- Customers: 75% Texas (in-store + online to TX addresses), 25% other states. Apportionment 0.75.
- NAICS code 442110 — Furniture Stores — clearly retail. Less than 50% of products manufactured by the entity (zero, in fact). Not utilities, not rental. **Qualifies for 0.375% retail rate.**

**Margin 4-way**  _(12.2 Example B — Texas retailer at 0.375%)_

| Base | Calc | Result |
| --- | --- | --- |
| 1: 70% | $4.2M × 0.70 | $2,940,000 |
| 2: − COGS | $4.2M − $2.48M | **$1,720,000** ← LOWEST |
| 3: − Compensation | $4.2M − $720K | $3,480,000 |
| 4: − $1M | $4.2M − $1M | $3,200,000 |

**Long-form tax (retail 0.375%):** $1,720,000 × 0.75 × 0.00375 = **$4,838**.

**EZ Computation comparison:** $4,200,000 × 0.75 × 0.00331 = **$10,427**. EZ is much worse — retail rate + COGS deduction wins decisively.

**Final.**
- Margin base: **Total revenue minus COGS** (Base 2).
- Rate: **0.375%** retail.
- Tax: **$4,838**.
- File **Form 05-158-A** (long form revenue & deductions), **05-158-B** (margin & apportionment), and **Form 05-102 PIR**.
- Owner pays via WebFile by May 15, 2026.

**Workpaper notes for reviewer.**
- Document the retail-rate qualification: NAICS 442110, products not manufactured by entity (purchases from third-party vendors only, attach vendor breakdown), no utility/rental component. Cite §171.002(c) and 34 TAC §3.584.
- Document COGS computation: tie to GL accounts; segregate Texas §171.1012 includable costs from excluded selling/administrative costs. Reviewer should confirm that delivery-to-customer costs are excluded (they are NOT in COGS per §171.1012(e)).
- Federal deductibility: $4,838 is deductible on Schedule C (if disregarded SMLLC) or 1120-S Line 12 / 1065 Line 14 (if multi-member). Track in 2025 federal workpapers.

### 12.3 Example C — Consultant LLC at 0.75% with compensation deduction winning

- Texas multi-member LLC, two member-managers, providing strategy consulting.
- 2026 report year.
- Total revenue: $3,800,000.
- No COGS — pure services.
- W-2 compensation: each member-manager paid $300,000 W-2 (LLC elected to put members on payroll via a §761 election or because it elected S-corp federally — assume W-2 payments are valid). Plus 4 staff consultants at $150,000 each = $600,000. Plus employer health $80,000 and 401(k) match $60,000.
- Total compensation = $300K + $300K + $600K + $80K + $60K = $1,340,000. All members and staff under the $450K cap, so no cap haircut.
- Customers: 50% Texas, 30% other U.S. states (market-based sourcing to client's principal office), 20% international.
- Apportionment factor: $1,900,000 / $3,800,000 = 0.50.

**Margin 4-way**  _(12.3 Example C — Consultant LLC at 0.75% with compensation deduction winning)_

| Base | Calc | Result |
| --- | --- | --- |
| 1: 70% | $3.8M × 0.70 | $2,660,000 |
| 2: − COGS | N/A | — |
| 3: − Compensation | $3.8M − $1.34M | **$2,460,000** ← LOWEST |
| 4: − $1M | $3.8M − $1M | $2,800,000 |

**Long-form tax (standard 0.75%):** $2,460,000 × 0.50 × 0.0075 = **$9,225**.

**EZ comparison:** $3,800,000 × 0.50 × 0.00331 = **$6,289**.

**EZ wins by $2,936.** Elect EZ.

**Final.**
- Method: **EZ Computation**.
- Rate: **0.331%**.
- Tax: **$6,289**.
- File **Form 05-169** (EZ) and **Form 05-102 PIR**.
- Due May 15, 2026.

**Owner action items.**
- Pay $6,289 via WebFile by May 15, 2026.
- File Form 05-169 EZ + Form 05-102 PIR.
- For 2027 planning: if revenue grows past $20M, EZ will be unavailable — model long form with compensation base for next year's projection.
- Deduct $6,289 on the federal 1065 Line 14 (taxes and licenses); flows through to members' K-1s as part of ordinary income.

**Workpaper notes for reviewer.**
- The EZ-vs-long-form analysis must show both computations.
- Confirm market-based sourcing for services: each non-Texas client's principal office must be identified in the workpaper. Cite 34 TAC §3.591(e)(26).
- Texas does not have throwback; the 20% international receipts simply reduce the apportionment numerator (they're not in the numerator and stay in the denominator), which is favorable here.
- If a member draws are recharacterized in audit (e.g. Comptroller argues guaranteed payments are not "compensation" under §171.1013), compensation base disappears and Base 1 (70%) becomes the floor — model the worst case. Long-form tax under 70% base = $2.66M × 0.50 × 0.0075 = $9,975. EZ still wins; the election is defensible.

## 13. Self-checks

Before finalizing any Texas franchise tax output, the skill must run:

1. **Entity classification check:** Confirm the entity is on the §171.0002(a) taxable-entity list. If sole prop / general partnership of natural persons → refuse with "exempt entity" and do not file.
2. **Disregarded entity trap:** If the user's federal classification is "disregarded SMLLC," explicitly confirm the LLC is still a Texas taxable entity. Flag if the user assumed otherwise.
3. **Threshold check:** Compare apportioned total revenue to $2,470,000. If below, route to PIR-only path under HB 1361. If above, route to long form / EZ analysis.
4. **Both methods computed:** For any entity with revenue ≤ $20M and above threshold, the workpaper must show both long-form margin (with 4-way) and EZ computations. Choose lower.
5. **Retail/wholesale qualification:** If user claims 0.375%, verify all four §171.002(c) criteria are documented.
6. **Compensation cap:** Confirm no person's compensation exceeds the per-person cap ($450K for 2024–2025; verify 2026 figure). If any person is above the cap, haircut the deduction.
7. **Apportionment sourcing:** For service revenue, confirm market-based (customer principal office) sourcing, not cost-of-performance. Cite 34 TAC §3.591(e)(26).
8. **Combined group check:** If any affiliated entity has > 50% common ownership and unitary operations, combined return is mandatory. The threshold applies once per group.
9. **PIR/OIR filed:** Confirm PIR (corp/LLC) or OIR (LP/partnership) is included regardless of tax owed.
10. **Due date and extension:** May 15. Extension via Form 05-164 only with proper payment of the safe-harbor amount.
11. **Federal deduction recorded:** Franchise tax paid is deductible on the federal return — flag for federal workpapers.
12. **Indexation refresh:** The $2.47M threshold, $20M EZ ceiling, and $450K compensation cap are biennially indexed. Refuse to proceed without confirming current-year figures.

## 14. Refusals — escalate to reviewer

This skill refuses to produce a final return without reviewer signoff in the following scenarios:

- **R-TX-1** — Entity has any insurance, banking, or regulated utility operations.  _(R-TX-1)_
- **R-TX-2** — Tiered-partnership election under §171.1015 is in play. The election can shift revenue to upper-tier entities but requires careful analysis; escalate.  _(R-TX-2, §171.1015)_
- **R-TX-3** — Combined group with intercompany transactions exceeding 25% of group revenue — the elimination workpaper must be reviewer-validated.  _(R-TX-3)_
- **R-TX-4** — §171.106(f) alternative apportionment — Comptroller discretionary; not self-elected.  _(R-TX-4, §171.106(f))_
- **R-TX-5** — Industry-specific revenue exclusions beyond the routine — e.g. staff leasing services (§171.1011(s)), pharmacy cooperatives (§171.1011(n)), waste hauling (§171.1011(p-1)).  _(R-TX-5, §171.1011(s), §171.1011(n), §171.1011(p-1))_
- **R-TX-6** — Cost-of-goods-sold for construction contractors under §171.1012(i) where subcontractor-cost election is used — requires reviewer to confirm the election and the subcontractor list.  _(R-TX-6, §171.1012(i))_
- **R-TX-7** — Final report / merger / acquisition in the report year — final period computation is mechanically different and audit-sensitive.  _(R-TX-7)_
- **R-TX-8** — Foreign entity (organized outside Texas) without confirmed registration with the Secretary of State — flag a parallel SOS qualification step before franchise tax is filed.  _(R-TX-8)_
- **R-TX-9** — Suspected fraud or material misstatement in prior-year filings — refer to credentialed practitioner immediately.  _(R-TX-9)_
- **R-TX-10** — Audit assessment or Comptroller notice in hand — handle via 90-day petition under §111.009, not a normal return cycle.  _(R-TX-10, §111.009)_
- **R-TX-11** — REIT, RIC, or §1031 exchange specialty entity classification.  _(R-TX-11)_
- **R-TX-12** — Passive entity certification with marginal facts (passive income between 85% and 95% of gross income) — escalate; thin-margin §171.0003 claims invite audit.  _(R-TX-12, §171.0003)_

## 15. Provenance and citations

### 15.1 Statutory authority

- **Tex. Tax Code Ch. 171 (Franchise Tax) — primary authority** — §171.0002 taxable entities; §171.0003 passive entities; §171.001 imposition/nexus; §171.002 rates (0.75%, 0.375%); §171.006 biennial indexation of thresholds; §171.101 margin election (4-way); §171.1011 total revenue and exclusions; §171.1012 COGS computation; §171.1013 compensation deduction; §171.1014 combined reporting; §171.1015 tiered partnerships; §171.1016 EZ Computation election; §171.103 Texas gross receipts; §171.106 apportionment; §171.151 first-year and report year mechanics; §171.204 reports required (as amended by HB 1361); §171.251–§171.255 forfeiture and personal liability; §171.362 penalties.  _(Tex. Tax Code Ch. 171)_
- **Tex. Tax Code Ch. 111 (Procedures)** — §111.060 interest on delinquent tax; §111.061 fraud penalty.  _(Tex. Tax Code Ch. 111)_
- **House Bill 1361** — House Bill 1361, 88th Legislature, Regular Session (2023) — eliminated the No-Tax-Due Report requirement for reports due on or after January 1, 2024.  _(House Bill 1361, 88th Legislature, Regular Session (2023))_

### 15.2 Administrative authority

- **34 TAC §3.584** — Margin: Reports and Payments.  _(34 Texas Administrative Code §3.584)_
- **34 TAC §3.586** — Margin: Nexus (including the $500K economic nexus rule, eff. 2020-01-01).  _(34 Texas Administrative Code §3.586)_
- **34 TAC §3.587** — Margin: Total Revenue.  _(34 Texas Administrative Code §3.587)_
- **34 TAC §3.588** — Margin: Cost of Goods Sold.  _(34 Texas Administrative Code §3.588)_
- **34 TAC §3.589** — Margin: Compensation.  _(34 Texas Administrative Code §3.589)_
- **34 TAC §3.590** — Margin: Combined Reporting.  _(34 Texas Administrative Code §3.590)_
- **34 TAC §3.591** — Margin: Apportionment (market-based sourcing for services, eff. reports due 2021-01-01).  _(34 Texas Administrative Code §3.591)_
- **34 TAC §3.592** — Margin: Additional Tax and Final Reports.  _(34 Texas Administrative Code §3.592)_

### 15.3 Forms

- **Form 05-158-A / 05-158-B** — Franchise Tax Long Form Report.  _(Form 05-158-A / 05-158-B)_
- **Form 05-169** — Franchise Tax EZ Computation Report.  _(Form 05-169)_
- **Form 05-163** — Franchise Tax No Tax Due Report (RETIRED for report years 2024+).  _(Form 05-163)_
- **Form 05-102** — Public Information Report (PIR).  _(Form 05-102)_
- **Form 05-167** — Ownership Information Report (OIR).  _(Form 05-167)_
- **Form 05-164** — Extension Request.  _(Form 05-164)_
- **Form 05-170** — Payment Form (paper voucher).  _(Form 05-170)_
- **Form AP-204** — Application for Exemption (nonprofits).  _(Form AP-204)_

### 15.4 Comptroller resources

- Franchise Tax landing page: https://comptroller.texas.gov/taxes/franchise/
- WebFile system: https://comptroller.texas.gov/taxes/file-pay/
- Entity status / forfeiture lookup: https://mycpa.cpa.state.tx.us/coa/
- Franchise Tax FAQs (updated annually): https://comptroller.texas.gov/taxes/franchise/faq/
- Biennial threshold indexation announcement: published January of even-numbered years.

### 15.5 Federal deductibility authority

- **IRC §164(a)(3)** — Deduction for state income taxes.  _(IRC §164(a)(3))_
- **IRC §164(b)(6)** — $10K SALT cap (applies to individuals, not entities).  _(IRC §164(b)(6))_
- **Rev. Rul. 2008-32** — Texas margin tax treated as an income tax for federal §164 purposes.  _(Rev. Rul. 2008-32)_
- **CCA 200947036 and subsequent** — Texas margin tax fully deductible at entity level.  _(CCA 200947036)_

### 15.6 Version notes

**Version notes table**  _(15.6 Version notes)_

| Version | Date | Notes |
| --- | --- | --- |
| 0.1 | 2025-11-15 | Initial drafting. Pending reviewer verification. 2026 indexation figures TBD — using 2024–2025 defaults ($2.47M threshold, $20M EZ ceiling, $450K compensation cap). Re-verify in January 2026 when biennial publication is released. |

### 15.7 Ambiguity catalogue

Whether SaaS provided to a Texas-based reseller who in turn serves out-of-state end users is sourced to Texas or to the end-user state. The plain reading of 34 TAC §3.591(e)(26) sources it to the Texas reseller; aggressive sourcing to end users is unsettled.

Whether transportation services with origin and destination both outside Texas, but billed from a Texas office, source to Texas. Comptroller's position is the service is performed and benefits accrue outside Texas — not in numerator.

Whether digital downloads sold to Texas customers are tangible personal property (destination sourcing) or intangibles (legal-domicile-of-payor sourcing). 34 TAC §3.591(e)(7) treats them as services for sourcing post-2021.

Whether owner-distributions paid as W-2 by an LLC that has elected S-corp federally count toward §171.1013 compensation. Comptroller has not formally ruled; practitioners treat W-2 Box 5 wages as qualifying compensation regardless of federal flow-through status.

Whether the compensation cap is tested per employer or per employee across a combined group. The statute is per-individual; combined-group reports aggregate compensation but still apply the per-individual cap separately at each member level. This favors groups with multiple W-2 employers paying the same person — rare but exists.

Treatment of crypto-asset gains under §171.1011 — Comptroller has not issued guidance; conservative position is to include net gains in total revenue and source to the legal domicile of the entity (intangible treatment).

### 15.8 Cross-references to other skills

- `us-sole-prop-bookkeeping.md` — builds the federal Schedule C / 1120 / 1065 from which Texas total revenue derives.
- `us-federal-return-assembly.md` — federal return that books the franchise tax deduction.
- `us-federal-tx-return-assembly.md` — orchestrator that pairs this skill with the federal package for Texas residents.
- `tx-sales-tax.md` — companion sales/use tax skill (separate tax base; both can apply).
- `us-tx-freelance-intake.md` — intake that triggers this skill when a Texas LLC/corp is identified.
- `us-s-corp-election-decision.md` — when an S-corp election is on the table, the Texas franchise tax compensation deduction interaction must be modeled.

## End of tx-margin-tax.md v0.1 (2025-11-15).

*End of tx-margin-tax.md v0.1 (2025-11-15).*

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
