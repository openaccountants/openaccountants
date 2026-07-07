---
name: nd-corporate-tax
description: North Dakota Corporate Income Tax
jurisdiction: US-ND
domain: corporate-tax
tax_year: 2025
tier: 2
last_updated: 2026-07-06
---

# nd-corporate-tax

## North Dakota Corporate Income Tax

North Dakota imposes a graduated corporate income tax under N.D.C.C. Chapter 57-38 (the Income Tax Act of 1981) at three statutory brackets: **1.41% on the first $25,000**, **3.55% on the next $25,000 (to $50,000)**, and **4.31% on income above $50,000** [VERIFY: NDCC § 57-38-30 for TY 2025 thresholds]. ND does **not** impose a separate corporate franchise tax (contrast NC, TX, DE) and does **not** currently offer a pass-through entity tax (PTET) election — leaving ND S-corp and partnership owners without a federal SALT-cap workaround. The corporation return is **Form 40**, due the 15th day of the 4th month after year-end. ND apportions corporate income using a **three-factor formula** (property, payroll, sales) with the **sales factor double-weighted** by default and an optional **single-sales-factor election** for qualifying taxpayers [VERIFY: NDCC § 57-38.1-09 / Form 40 instructions]. The Oil Extraction Tax (NDCC § 57-51.1) and Oil & Gas Gross Production Tax (NDCC § 57-51) are **severance taxes computed at the well** and are **not** part of the entity-level CIT — they are mentioned here only because new ND practitioners frequently confuse them with corporate income tax. Tax year 2025.

## 1. Scope

This skill covers North Dakota state-level entity-level income tax:

- **Corporate income tax** (N.D.C.C. Chapter 57-38, Income Tax Act of 1981) — imposed on C-corporations doing business in or deriving income from ND sources, including LLCs that have elected federal C-corp treatment under Form 8832 or Form 2553-then-revoked.
- **Apportionment, sourcing, NOL, and estimated-payment rules** as they apply to ND corporate income tax.
- **S-corporation pass-through treatment** (informational only — Form 60 is the ND S-corp return).
- **Partnership / LLC pass-through treatment** (informational only — Form 58 is the ND partnership return).
- **Cross-link only:** Oil Extraction Tax (NDCC § 57-51.1) and Oil & Gas Gross Production Tax (NDCC § 57-51), and Bank of North Dakota's unique exemption (NDCC § 6-09). These are surfaced as **audit flash points** because new ND practitioners confuse them with corporate income tax; the operative computation belongs in dedicated severance / banking skills not yet authored.

**In scope:** Form 40 (Corporation Income Tax Return), Form 40-ES (corporate estimated tax voucher), Form 40-EXT (extension), Form 40-UT (underpayment of estimated tax), Schedule SA (apportionment), Form 60 (S-corp informational), Form 58 (partnership informational), Schedule K-1 (Form 58/60).

**Out of scope (refer elsewhere):**

- ND personal income tax (PIT) — covered by `nd-income-tax.md`. The 2025 PIT is a near-flat structure with a 0% / 1.95% / 2.50% schedule following the rate reductions enacted by HB 1158 (68th Legislative Assembly, 2023).
- ND sales and use tax — covered by `nd-sales-tax.md`.
- Federal corporate income tax (Form 1120) — covered by federal skills.
- **Oil Extraction Tax (5% of gross value at the well, NDCC § 57-51.1)** — severance tax on oil producers, computed at the well on producer's net interest. **NOT** a corporate income tax. Mentioned here only as a refusal / disambiguation.
- **Oil and Gas Gross Production Tax (NDCC § 57-51)** — separate 5% production tax on oil and gas. Also severance, not income tax.
- **Coal Conversion Tax (NDCC § 57-60)**, cigarette/tobacco tax, liquor tax — out of scope.
- **Bank of North Dakota** — the only state-owned bank in the United States, organized under NDCC Chapter 6-09. The bank itself is a state instrumentality and **pays no corporate income tax**. Private banks doing business in ND are subject to the **financial institution privilege tax** under NDCC Chapter 57-35.3, **not** the standard corporate income tax — refusal item, see § 13.
- **Insurance companies** — subject to the gross premiums tax under NDCC § 26.1-03-17, not corporate income tax.
- **Cities and counties** — ND has no local corporate income tax.

> ⚠️ **Authority confirmation rule.** Before relying on a rate, threshold, or form line in production, confirm against the current ND Office of State Tax Commissioner publications (Form 40 Corporate Income Tax Booklet, Schedule SA instructions, and any Commissioner's guidelines). The 1.41% / 3.55% / 4.31% bracket schedule has been stable since 2015 but the Legislative Assembly meets biennially and could amend rates in any odd-year session. Statutes change.

## 2. Metadata and Sources

**Metadata table**

| Field | Value |
| --- | --- |
| Jurisdiction | US-ND (North Dakota) |
| Tier | 2 (content) |
| Skill name | `nd-corporate-tax` |
| Version | 0.1 |
| Last updated | 2026-05-28 |
| Verified by | pending |
| Companion skills | `us-tax-workflow-base`, `us-federal-return-assembly`, `nd-income-tax`, `nd-sales-tax` |
| Primary statute | N.D.C.C. Chapter 57-38 (Income Tax Act of 1981) |
| Apportionment statute | N.D.C.C. Chapter 57-38.1 (Uniform Division of Income for Tax Purposes Act / UDITPA) |
| Primary form | Form 40 (Corporation Income Tax Return) |
| Filing agency | North Dakota Office of State Tax Commissioner |
| Tax year covered | 2025 (calendar) |

### Primary sources

1. **N.D.C.C. § 57-38-30** — Corporate income tax rate brackets [VERIFY: section may have been renumbered to § 57-38-30 or remain at original location; some practitioner guides reference § 57-38-30.3].
2. **N.D.C.C. § 57-38-01.4** — NOL rules; ND adopts federal § 172 by reference subject to ND modifications.
3. **N.D.C.C. Chapter 57-38.1** — Apportionment (UDITPA-derived; property + payroll + sales).
4. **N.D.C.C. § 57-38-08** — Sourcing rules and what constitutes ND-source income.
5. **N.D.C.C. § 57-38-62** — Estimated tax for corporations.
6. **Form 40 Corporation Income Tax Booklet (2025)** — ND Office of State Tax Commissioner.
7. **Form 40 Vendor Version (2025)** — referenced for line-level detail.

## 3. Quick Reference (TY 2025)

**Quick Reference table**  _(NDCC § 57-38-30 / Form 40 instructions)_

| Item | Value | Authority |
| --- | --- | --- |
| Corporate income tax — Bracket 1 | **1.41%** on first $25,000 of ND taxable income | NDCC § 57-38-30 [VERIFY] |
| Corporate income tax — Bracket 2 | **3.55%** on next $25,000 (to $50,000) | NDCC § 57-38-30 [VERIFY] |
| Corporate income tax — Bracket 3 | **4.31%** on income above $50,000 | NDCC § 57-38-30 [VERIFY] |
| Water's edge surtax | Additional **3.5%** of ND taxable income for water's-edge electors | NDCC § 57-38.1-15 / Form 40 instructions |
| Apportionment formula | Three-factor: property + payroll + sales (sales double-weighted) by default; **single-sales-factor election available** for qualifying taxpayers | NDCC § 57-38.1-09 [VERIFY weighting] |
| Sourcing | Cost-of-performance for services (default); ND has **not** broadly adopted market-based sourcing as of 2025 [VERIFY] | NDCC § 57-38.1-16 |
| NOL carryforward | **20 years** [VERIFY against current statute]; no carryback | NDCC § 57-38-01.4 |
| NOL 80% taxable-income limitation | ND conforms to federal § 172(a)(2)(B) **80% limit** for post-2017 NOLs [VERIFY conformity date] | NDCC § 57-38-01.4 + federal conformity |
| Filing form | Form 40 (Corporation Income Tax Return) | ND Tax Commissioner |
| Due date (calendar-year filer) | **April 15** (15th day of 4th month after year-end) | NDCC § 57-38-34 |
| Extension | Automatic 7-month extension if federal extension filed; Form 40-EXT for ND-only extension | Form 40 instructions |
| Estimated-tax threshold | Required if both **prior-year and current-year liability exceed $5,000** | NDCC § 57-38-62 [VERIFY threshold] |
| Estimated-tax form | Form 40-ES | ND Tax Commissioner |
| Underpayment form | Form 40-UT | ND Tax Commissioner |
| PTE election | **None — ND has NOT enacted a PTET** [VERIFY through 2025 legislative session] | n/a |
| Separate franchise tax? | **No.** ND has no general corporate franchise tax. | n/a |
| Minimum tax? | **None.** No statutory minimum CIT (unlike NC's $200 franchise floor). | n/a |
| S-corp at entity level? | No CIT; files informational Form 60 | NDCC § 57-38-01.4 (federal conformity) |
| Partnership / LLC default at entity level? | No CIT; files informational Form 58 | NDCC Chapter 57-38 |

## 4. Who's Subject

**Who's Subject table**

| Entity Type | Subject to ND CIT? | Form |
| --- | --- | --- |
| C-corporation (ND-domiciled or foreign doing business in ND) | YES — Form 40 | Form 40 |
| LLC electing C-corp treatment (federal Form 8832) | YES — Form 40 | Form 40 |
| LLC electing S-corp treatment (federal Form 2553) | NO at entity level; informational only | Form 60 |
| S-corporation (federal § 1362 election in effect) | NO at entity level; informational only | Form 60 |
| Multi-member LLC, default partnership | NO at entity level; informational only | Form 58 |
| Single-member LLC, disregarded | NO at entity level; owner reports on Form ND-1 or Form 40 if owner is a corp | none (flows to owner) |
| Limited partnership (LP) | NO at entity level; informational only | Form 58 |
| Nonprofit § 501(c)(3) corporation | NO if exempt under federal § 501; UBI subject to CIT | Form 40 if UBTI |
| Insurance company | NO (gross premiums tax instead) | NDCC § 26.1-03-17 |
| Bank of North Dakota | NO (state instrumentality) | NDCC Chapter 6-09 |
| Private bank / financial institution | NO standard CIT — subject to **financial institution privilege tax** | NDCC Chapter 57-35.3 |

### 4.1 Federal S-election automatically applies in ND

- **Federal S-election carries automatically to ND** — ND mirrors federal Subchapter S treatment under NDCC § 57-38-01.4. A federal S-corp election under IRC § 1362 automatically carries to North Dakota; there is no separate ND S-election and no separate S-revocation form. Shareholders of ND S-corps pay ND personal income tax on their pro-rata share of ND-source income at the standard PIT rates (covered in `nd-income-tax.md`).  _(NDCC § 57-38-01.4)_

### 4.2 LLCs electing C-corp — the same trap as elsewhere

- **LLC C-corp election binding for ND** — An LLC that affirmatively elects C-corp treatment by filing federal Form 8832 (or Form 2553 then revoked) becomes a Form 40 filer for ND purposes. The election is binding for ND. Practitioners should verify the federal election before assuming a multi-member LLC is on Form 58.  _(Form 40)_

### 4.3 Nexus

- **ND nexus criteria** — ND asserts income tax nexus on corporations that: (a) are incorporated or organized in ND; (b) are qualified to do business in ND; (c) have property, payroll, or sales in ND exceeding bright-line thresholds analogous to MTC factor presence; or (d) derive ND-source income under NDCC § 57-38-08. Wayfair-style economic nexus for corporate income tax has not been formally codified by ND beyond general "doing business" language [VERIFY for 2025 — Commissioner may have issued guidelines].  _(NDCC § 57-38-08)_

### 5.1 Graduated brackets — TY 2025

**Graduated brackets table**  _(N.D.C.C. § 57-38-30)_

| ND Taxable Income | Marginal Rate | Cumulative Tax at Top of Bracket |
| --- | --- | --- |
| $0 – $25,000 | **1.41%** | $352.50 |
| $25,001 – $50,000 | **3.55%** | $352.50 + 3.55% × (income − $25,000); $1,240 at $50,000 |
| Above $50,000 | **4.31%** | $1,240 + 4.31% × (income − $50,000) |

**Effective-rate examples table**  _(N.D.C.C. § 57-38-30)_

| ND Taxable Income | ND CIT | Effective Rate |
| --- | --- | --- |
| $10,000 | $141 | 1.41% |
| $25,000 | $352.50 | 1.41% |
| $50,000 | $1,240 | 2.48% |
| $100,000 | $3,395 | 3.40% |
| $500,000 | $20,635 | 4.13% |
| $1,000,000 | $42,185 | 4.22% |
| $5,000,000 | $214,685 | 4.29% |

The brackets are **not** indexed for inflation. The $25,000 and $50,000 thresholds have been stable since 2015 [VERIFY].

### 5.2 Water's-edge surtax (NDCC § 57-38.1-15)

- **Water's-edge surtax** — A corporation that elects the water's edge method of apportioning income (i.e., excludes certain foreign affiliates from the unitary group) is subject to an additional 3.5% surtax on its ND taxable income. The election trades broader inclusion of foreign affiliates (worldwide) for a flat 3.5% surcharge. Most US-only ND filers do not need to think about this; it matters only for multinationals filing a unitary return.  _(NDCC § 57-38.1-15)_

### 5.3 No minimum tax

- **No minimum tax** — Unlike NC ($200 franchise tax floor), CA ($800 LLC tax / franchise tax), or TX ($0 below the no-tax-due threshold), ND imposes no minimum corporate income tax. A C-corp with zero ND taxable income (e.g., a loss year or an entity with zero ND apportionment) owes $0 in ND CIT. The corporation must still file Form 40 to report the zero, but it owes nothing.  _(n/a)_

### 5.4 No separate franchise tax

- **No separate franchise tax** — ND has no general corporate franchise tax. The only entity-level taxes that apply to a typical ND C-corp are: 1. Corporate income tax under NDCC § 57-38-30 (this skill). 2. Sales/use tax on its purchases and (if a seller) on its sales (`nd-sales-tax.md`). 3. Payroll taxes on its employees (federal + ND state unemployment). 4. Real and personal property tax at the county/city level (not in scope). 5. Any industry-specific tax (e.g., oil extraction tax for producers). The absence of a franchise tax means an ND C-corp at the $0 income / loss-year extreme owes nothing at the entity level — a notable contrast with NC, TX, DE, and CA, where a loss-year C-corp still owes a franchise / privilege tax minimum.  _(n/a)_

### 6.1 Three-factor formula — default

- **Three-factor apportionment formula** — Apportionment = (Property Factor + Payroll Factor + 2 × Sales Factor) / 4  _(N.D.C.C. § 57-38.1-09 [VERIFY current weighting])_
- **Factor definitions** — The sales factor is double-weighted by default — i.e., the denominator is 4 (one each for property, payroll, and two for sales). This is the standard UDITPA "modified" formula widely adopted by states that have not moved to single sales factor. Each factor is: - Property factor = ND tangible property (owned at original cost + rented × 8) ÷ everywhere tangible property. - Payroll factor = ND wages and salaries ÷ everywhere wages and salaries. - Sales factor = ND-sourced sales (gross receipts) ÷ everywhere sales.  _(N.D.C.C. § 57-38.1-09)_

### 6.2 Single-sales-factor election (optional)

- **Single-sales-factor election** — ND permits qualifying taxpayers to elect a single-sales-factor apportionment under N.D.C.C. § 57-38.1-09(8) [VERIFY citation]. The election: - Is binding for a minimum of 5 years [VERIFY duration]. - Is made on Form 40 / Schedule SA in the year of election. - Cannot be revoked early without Commissioner consent. - Is generally beneficial for ND-headquartered manufacturers and oil/gas producers with substantial ND payroll and property but sales delivered nationally. The single-sales-factor option mirrors the broader national trend (NC, MI, IL, WI, CA all single-sales) but ND has preserved the three-factor default — a meaningful indicator that ND policymakers prioritize broad in-state-activity recognition over export-orientation incentives.  _(N.D.C.C. § 57-38.1-09(8) [VERIFY citation])_

### 6.3 Special industries

**Special industries apportionment table**  _(NDCC § 57-38.1)_

| Industry | Apportionment Method | Citation |
| --- | --- | --- |
| Railroads | Special factor formula | NDCC § 57-38.1 [VERIFY subsection] |
| Motor carriers | Mileage-weighted | NDCC § 57-38.1 [VERIFY] |
| Airlines | Departure / revenue-ton formula | NDCC § 57-38.1 [VERIFY] |
| Financial institutions | Subject to separate privilege tax under NDCC Ch. 57-35.3, not CIT | n/a |

### 6.4 NOL interaction with apportionment

- **NOL post-apportionment tracking** — Apportionment is applied after ND modifications to federal taxable income but before the ND NOL deduction. The ND NOL operates on a post-apportionment basis; it is tracked in ND-apportioned dollars, not pre-apportionment federal dollars.

### 6.5 Alternative apportionment

- **Alternative apportionment petition** — A taxpayer (or the Commissioner) may petition for an alternative apportionment method under NDCC § 57-38.1-18 if the statutory formula does not "fairly represent" the corporation's ND activity. As elsewhere, taxpayer-initiated alternative apportionment is rarely granted; the Commissioner more often imposes combined / unitary computation against an aggressive separate-entity filer.  _(NDCC § 57-38.1-18)_

### 7.1 Sales of tangible personal property — destination

- **Destination sourcing rule** — Sales of tangible personal property are sourced to ND if the property is delivered or shipped to a purchaser within ND, regardless of FOB terms (NDCC § 57-38.1-16). This is the standard UDITPA destination rule.  _(NDCC § 57-38.1-16)_

### 7.2 Sales of services — cost of performance (with caveats)

- **Cost-of-performance sourcing for services** — ND has not broadly adopted market-based sourcing for services as of 2025 [VERIFY]. Services receipts are generally sourced to ND if the income-producing activity is performed in ND, or if a greater proportion of the income-producing activity is performed in ND than in any other state (the "majority cost-of-performance" rule). This is the traditional UDITPA § 17 sourcing. This is a meaningful divergence from NC, CA, MA, IL, and 30+ other states that have moved to market-based sourcing. ND-headquartered service providers selling nationally currently benefit from cost-of-performance treatment because ND payroll / overhead generates ND-sourced receipts even when the customer is out-of-state. > ⚠️ **Audit flash point.** Whether ND has revised this rule for tax years 2024-2025 should be re-verified each filing season. Several Plains-region states (e.g., Iowa, Missouri) have moved to market-sourcing in recent biennia.  _(UDITPA § 17)_

### 7.3 Oil and gas — extraction at the well, not income tax

- **Oil and gas severance tax disambiguation** — This is the single most important sourcing disambiguation for new ND practitioners. The Oil Extraction Tax (NDCC Ch. 57-51.1) and the Oil & Gas Gross Production Tax (NDCC Ch. 57-51) are severance taxes imposed on the value of oil and gas at the wellhead. They are paid by the producer (or first purchaser) based on the volume × price × statutory rate (typically 5% each, so combined ~10% on oil and ~5% on gas at the well). The taxes are administered by the ND Tax Commissioner's Oil and Gas Tax Section. These taxes are not ND corporate income tax. They are NOT: - Computed on ND apportioned taxable income. - Reduced by ND NOL carryforwards. - Filed on Form 40. - Within the scope of this skill. For a C-corp producer doing business in ND, the oil extraction and gross production taxes are paid separately (different forms, different schedules) and are deductible in computing federal taxable income (and thus ND taxable income, as ND starts from federal taxable income). The producer also files Form 40 reporting ND apportioned income from its production activity (after deducting the severance taxes federally). A common practitioner error is to attempt to claim ND CIT credits for oil extraction tax paid, or to net the extraction tax against CIT liability. There is no such credit. They are separate tax regimes.  _(NDCC Ch. 57-51.1 / NDCC Ch. 57-51)_

### 7.4 Sourcing for SaaS and intangibles

- **SaaS and intangibles sourcing** — For receipts from intangible property and SaaS, ND follows a use-location rule for licensed software and a commercial domicile rule for intangibles generally (NDCC § 57-38.1-16 read with Commissioner's guidelines). SaaS receipts are often sourced by analogy to services (cost-of-performance) absent a clear ND market-sourcing directive. This is an under-developed area in ND administrative guidance and is a frequent grey zone in practice [VERIFY current ND Commissioner guidelines].  _(NDCC § 57-38.1-16)_

### 8.1 Regime

- **NOL regime parameters** — ND adopts federal § 172 by reference under NDCC § 57-38-01.4 with ND modifications. Key parameters [all VERIFY against current statute]: - Carryforward period: 20 years [VERIFY — could be revised to indefinite to mirror federal post-TCJA]. - Carryback: Not permitted for ND purposes (consistent with federal post-TCJA). - 80% of taxable income limitation: ND conforms to the federal § 172(a)(2)(B) 80% limit for NOLs generated in tax years beginning after Dec 31, 2017 [VERIFY conformity date and any decoupling]. - Tracked in ND-apportioned dollars — i.e., the NOL number on the schedule is the post-apportionment ND figure, not the pre-apportionment federal NOL. - No discrete schedule equivalent to NC Schedule NOL — the NOL is computed on Form 40 / Schedule SB attachments [VERIFY current schedule designation].  _(NDCC § 57-38-01.4)_

### 8.2 Ownership-change limitations (§ 382)

- **§382 ownership change limitations** — ND follows federal § 382 by reference for ownership-change limitations on NOL utilization. The ND § 382 base is computed independently using ND values and apportionment. As with most states, ND has issued limited published guidance distinct from federal § 382; practitioners apply federal mechanics and adjust for ND apportionment.

### 8.3 Interaction with rate stability

- **NOL value stability** — Unlike NC (whose CIT rate is phasing to 0% by 2030, eroding NOL value), ND CIT rates have been stable since 2015. An ND NOL carryforward holds its value across years — there is no rate-arbitrage planning lever analogous to the NC scenario. The only NOL planning is the standard "use it before it expires" check and the § 382 limitation if ownership changes.

## 9. PTE Election — **Absent in North Dakota**

### 9.1 Current status (TY 2025)

- **No PTET enacted** — North Dakota has NOT enacted a Pass-Through Entity Tax (PTET) election as of the 2025 tax year. This is confirmed by multiple practitioner surveys identifying ND (along with DE) as one of the few remaining states with a broad-based income tax that has not adopted a PTET workaround for the federal SALT cap [VERIFY through 68th and 69th Legislative Assembly sessions, 2023 and 2025].

### 9.2 Legislative history

- The 67th Legislative Assembly (2021) did not enact a PTET despite the federal SALT-cap workaround trend.
- The 68th Legislative Assembly (2023) considered tax reform broadly but did not enact a PTET.
- The 69th Legislative Assembly (2025) has not enacted a PTET as of the most recent confirmed legislative calendar [VERIFY against final 2025 session bills].

### 9.3 Practical consequences for ND pass-through owners

- **SALT cap exposure for ND pass-through owners** — ND S-corp shareholders and ND partnership/LLC members cannot elect entity-level taxation to escape the federal $10,000 SALT cap on their personal Schedule A. Their ND personal income tax remains a personal itemized deduction subject to the cap. For a high-income ND S-corp owner this is a meaningful federal tax disadvantage relative to peers in NC, CA, NY, MN, or any of the ~37 states that have enacted PTETs. A 2025 owner with $1,000,000 of ND S-corp income paying ~$25,000 of ND personal income tax has no SALT-cap workaround — the $25,000 is capped at $10,000 on Schedule A, costing roughly $5,550 in federal tax at the 37% marginal bracket compared with a PTET-eligible state.

### 9.4 OBBBA (2025) interaction

- **OBBBA SALT cap interaction** — The federal SALT cap was modified by the One Big Beautiful Bill Act (P.L. 119-21, July 4 2025) — relevant for years 2025 and onward [VERIFY OBBBA SALT-cap parameters in `us-tax-workflow-base`]. Even with whatever cap relief OBBBA provides, the absence of a ND PTET means ND owners cannot capture entity-level federal-deductible state-tax payments in the way that PTET-state owners can. This continues to be a competitive disadvantage for the ND professional-services and small-corporation sector.  _(P.L. 119-21)_

### 9.5 Planning workaround alternative

- **C-corp conversion workaround** — The principal practitioner workaround in a non-PTET state like ND is: - C-corp conversion analysis. For owners who can tolerate two layers of tax, converting an S-corp to a C-corp captures the corporate ND CIT (top bracket 4.31%) as a federal Form 1120 deductible item (no SALT cap applies to corporate state-tax deductions). The 21% federal corporate rate + 4.31% ND blended into an effective ~25% on the corp side may be worse or better than pass-through depending on owner's federal bracket and dividend distribution policy. The C-corp election is rarely beneficial purely for SALT-cap reasons — but in ND it is the only entity-level workaround. Practitioners should consult `us-s-corp-election-decision.md` and run the C-corp vs. S-corp model annually for high-income ND owners.

### 10.1 Forms

**Forms table**

| Form | Used By | Purpose |
| --- | --- | --- |
| Form 40 | C-corps and LLCs taxed as C-corps | ND Corporation Income Tax Return |
| Form 40-ES | All Form 40 filers above threshold | Quarterly estimated payment voucher |
| Form 40-EXT | All Form 40 filers needing extension | Application for extension (if not relying on federal extension) |
| Form 40-UT | All Form 40 filers underpaying | Underpayment of Estimated Income Tax |
| Schedule SA | All Form 40 filers with multistate activity | Apportionment schedule (property, payroll, sales factors) |
| Schedule FACT (or analog) | Form 40 filers with NOLs | NOL tracking schedule [VERIFY schedule designation] |
| Form 60 | S-corps (informational) | ND S-Corporation Income Tax Return |
| Schedule K-1 (Form 60) | S-corps | Shareholder's share of ND income |
| Form 58 | Partnerships and multi-member LLCs (informational) | ND Partnership Return |
| Schedule K-1 (Form 58) | Partnerships | Partner's share of ND income |

### 10.2 Due dates

- **Due dates and extension rules** — - Calendar-year filers: April 15 of the year following the tax year (15th day of the 4th month after year-end). - Fiscal-year filers: 15th day of the 4th month after the close of the fiscal year. - Extension: If a federal extension (Form 7004) is filed, ND automatically grants the same extension — no separate ND extension is required. If no federal extension is filed, a corporation may request a 7-month ND-only extension on Form 40-EXT. Extension extends time to file, not time to pay; interest and underpayment penalty run from the original due date.  _(NDCC § 57-38-34)_

### 10.3 Estimated payments — Form 40-ES

- **Estimated payment requirement** — A corporation must make quarterly estimated payments if: - Its prior-year ND CIT liability exceeded $5,000, AND - Its current-year ND CIT liability is expected to exceed $5,000. [VERIFY threshold — practitioner sources report $5,000 but the statute may use a different figure for 2025.] Quarterly installments are due on the 15th day of the 4th, 6th, 9th, and 12th months of the tax year.  _(NDCC § 57-38-62 [VERIFY threshold])_

**Quarterly installment schedule table**

| Installment | Due Date | Cumulative % |
| --- | --- | --- |
| 1st | April 15 | 25% |
| 2nd | June 15 | 50% |
| 3rd | September 15 | 75% |
| 4th | December 15 | 100% |

### 10.4 Safe harbor

- **Underpayment safe harbor** — The underpayment penalty (Form 40-UT) is avoided if the corporation has paid at least the lesser of: 1. 100% of the prior year's tax liability, OR 2. 90% of the current year's tax liability. The prior-year safe harbor is not available if the corporation had no liability or did not file a return in the prior year, or if the prior tax year was a short period.

### 10.5 Penalties and interest

- **Penalties and interest schedule** — - Late filing: 5% per month, max 25% [VERIFY against NDCC § 57-38-45 for 2025 amounts]. - Late payment: 5% of unpaid tax + 1% per month [VERIFY]. - Underpayment of estimated tax: Computed on Form 40-UT using the statutory interest rate (revised semi-annually by the Tax Commissioner). - Negligence: 25% of underpayment. - Fraud: 75% of underpayment.  _(NDCC § 57-38-45 [VERIFY])_

### 10.6 Combined and unitary reporting

- **Combined and unitary reporting requirement** — ND requires combined reporting for unitary businesses under NDCC § 57-38.1-19 [VERIFY]. A corporation that is part of a unitary business with other corporations must file a combined Form 40 reflecting the unitary group's combined income, with ND apportionment computed on the combined basis (Joyce / Finnigan election may apply — verify current ND rule). ND's combined-reporting requirement is meaningful: practitioners migrating from separate-return states (NC's default is separate-entity) must affirmatively analyze unitary status for any multistate ND filer. The water's-edge election (§ 5.2) is the principal mechanism to limit combined reporting to US-only affiliates.  _(NDCC § 57-38.1-19 [VERIFY])_

### 11.1 Example A — Small all-ND C-corp at the lowest bracket

**Facts.** Prairie Print Shop, Inc. is a Bismarck-domiciled C-corp providing commercial printing. Calendar-year filer. For 2025:

- Federal taxable income (Form 1120, line 30): $20,000
- ND additions: $0
- ND subtractions: $0
- 100% of activity (property, payroll, sales) in ND. Apportionment factor: 1.0000.
- No NOL carryforward.

**Step 1 — ND taxable income (2025):**

```
Federal taxable income            20,000
+ ND additions                         0
- ND subtractions                      0
= Pre-apportionment income        20,000
× ND apportionment factor         1.0000
= ND apportioned income           20,000
- NOL deduction                        0
= ND taxable income               20,000
```

**Step 2 — ND corporate income tax (bracket 1 only):**

```
$20,000 × 1.41% = $282.00
```

**Step 3 — Estimated-tax obligation:**

```
$282 prior-year < $5,000 threshold → no estimated payments required for 2026.
```

**Step 4 — Total 2025 ND tax:**

```
ND CIT       $282.00
(No franchise tax in ND)
Total        $282.00
```

**Takeaway.** A small ND C-corp at the lowest bracket owes a few hundred dollars. There is no minimum tax, no franchise tax, and no required estimated payments below the $5,000 threshold. This is dramatically simpler than NC, CA, TX, or DE, where even a tiny C-corp owes hundreds in franchise / minimum tax annually.

### 11.2 Example B — Mid-size C-corp with multistate apportionment (ND + MN + MT)

**Facts.** Red River Equipment, Inc. is a Fargo-domiciled C-corp selling agricultural equipment across the Plains. Calendar 2025:

- Federal taxable income: $2,000,000
- ND additions: $50,000 (state taxes deducted federally)
- ND subtractions: $10,000 (federal bonus depreciation timing)
- No NOL carryforward.

**Step 1 — Three-factor formula (sales double-weighted):**

```
Apportionment = (0.5000 + 0.6000 + 2 × 0.4000) / 4
              = (0.5000 + 0.6000 + 0.8000) / 4
              = 1.9000 / 4
              = 0.4750
```

**Step 2 — ND taxable income:**

```
Federal taxable income          2,000,000
+ ND additions                     50,000
- ND subtractions                 (10,000)
= Pre-apportionment income      2,040,000
× ND apportionment factor          0.4750
= ND apportioned income           969,000
- NOL deduction                         0
= ND taxable income               969,000
```

**Step 3 — ND CIT (graduated brackets):**

```
Bracket 1: $25,000  × 1.41% = $   352.50
Bracket 2: $25,000  × 3.55% = $   887.50
Bracket 3: $919,000 × 4.31% = $39,608.90
                              ----------
Total ND CIT                  $40,848.90
```

**Step 4 — Counterfactual: single-sales-factor election**

If Red River had previously elected single-sales-factor apportionment:

```
Apportionment = 0.4000 (sales only)
ND apportioned income = 2,040,000 × 0.4000 = 816,000
ND CIT:
  Bracket 1 / 2:                     $1,240.00
  Bracket 3: 766,000 × 4.31% =     $33,014.60
  Total                            $34,254.60

Saving from single-sales-factor:    $6,594.30
```

The single-sales election saves ~$6,600 annually because Red River has heavy ND payroll and property relative to ND sales — the classic ND-headquartered exporter profile. Over the 5-year minimum election period, that's ~$33,000 in cumulative ND tax savings, before factoring in growth.

**Step 5 — Estimated-tax obligation for 2026:**

```
$40,849 > $5,000 → quarterly Form 40-ES required.
Safe harbor: pay 100% of 2025 liability ($40,849) split into 4 installments
  of $10,212.25, due April / June / September / December 15, 2026.
```

**Takeaway.** A multistate ND C-corp needs to think carefully about whether to make the single-sales-factor election. The break-even is roughly where the ND sales factor is materially lower than the average of the property and payroll factors — typical of ND-headquartered producers selling nationally. The election is binding for 5 years, so model carefully.

**Apportionment factor inputs (Schedule SA)**

| Factor | ND | Everywhere | Factor Ratio |
| --- | --- | --- | --- |
| Property | $5,000,000 | $10,000,000 | 0.5000 |
| Payroll | $3,000,000 | $5,000,000 | 0.6000 |
| Sales | $8,000,000 | $20,000,000 | 0.4000 |

### 11.3 Example C — ND S-corp with zero entity-level CIT but pass-through

**Facts.** Bakken Software Solutions, Inc. is an ND S-corp (federal § 1362 election in effect) providing software consulting to oil & gas producers. Single shareholder, ND resident. Calendar 2025:

- Federal Form 1120-S ordinary business income: $400,000 (passes through to shareholder)
- 100% of activity in ND.
- No PTE election available (ND has none — see § 9).

**Step 1 — Entity-level ND CIT (Form 40):**

```
$0 — S-corps are exempt from ND corporate income tax. File Form 60 (informational).
```

**Step 2 — Shareholder-level ND PIT (Form ND-1, separate return):**

The $400,000 of S-corp income flows through to the shareholder's federal Schedule K-1 and onto ND Form ND-1. The shareholder pays ND personal income tax at the 2025 rates (top bracket ~2.50% per `nd-income-tax.md`) [VERIFY current PIT rate]:

```
Approx. ND PIT (top bracket 2.50% on amount above ND PIT threshold):
  400,000 × 2.50% ≈ $10,000 (simplified — actual ND-1 computation differs)
```

**Step 3 — Federal SALT-cap exposure (no PTET workaround):**

The shareholder pays approximately $10,000 of ND PIT plus state and local taxes (property tax on home, etc.). Total SALT likely well over $10,000. The federal Schedule A SALT deduction is capped at $10,000 (or as modified by OBBBA — verify).

Because ND has no PTET, the entity cannot pay the shareholder's ND PIT at the entity level and deduct it on Form 1120-S. The shareholder is fully exposed to the SALT cap.

**Comparison vs. a hypothetical PTET election:**

If ND had a PTET at a 2.50% rate, the entity would pay $10,000 of PTET, deduct it on Form 1120-S (reducing pass-through income to $390,000), and the shareholder would claim a refundable credit on Form ND-1. Federal tax saving at the 37% marginal bracket: $10,000 × 37% ≈ $3,700. This saving is unavailable in ND.

**Step 4 — Total ND tax burden:**

```
Entity-level (Form 60)         $0.00
Shareholder ND PIT (Form ND-1) ~$10,000.00
Federal SALT relief (lost)     ~($3,700) opportunity cost
Total ND tax                   ~$10,000
```

**Takeaway.** ND S-corp owners pay only personal income tax — there is no entity-level CIT. But because ND has no PTET, high-income S-corp owners lose ~$3,700 per $400,000 of pass-through income in federal tax compared with peers in PTET states. This is the principal competitive disadvantage of the ND tax code for the small-corporation owner segment.

### 11.4 Example D — Oil & gas C-corp: extraction tax vs. income tax (disambiguation)

**Facts.** Bakken Crude Operators, Inc. is an ND C-corp operating oil wells in McKenzie County. Calendar 2025:

- Federal taxable income: $5,000,000 (after deducting all severance taxes paid)
- 100% of activity in ND. Apportionment 1.0000.
- ND additions / subtractions: net $0.

**Question that confuses new practitioners:** "We paid $3,000,000 in ND oil extraction tax in 2025. Do we get a credit against our ND CIT?"

**Answer: No.** The oil extraction tax (NDCC Ch. 57-51.1) is a severance tax computed at the wellhead on the producer's net interest, at a base rate of approximately 5% of gross value (with various rate triggers tied to oil price). The oil and gas gross production tax (NDCC Ch. 57-51) is a separate 5% severance tax. These taxes are:

- Paid separately to the Oil and Gas Tax Section of the ND Tax Commissioner.
- Deductible in computing federal taxable income under § 164 (state taxes paid in carrying on a trade or business).
- Not credited against ND CIT.
- Not computed on Form 40.

**Step 1 — ND CIT computation on Form 40:**

```
Federal taxable income            5,000,000
  (already reduced by the $3M of severance tax deducted federally)
+ ND additions                            0
- ND subtractions                         0
= Pre-apportionment income        5,000,000
× ND apportionment                   1.0000
= ND taxable income               5,000,000
```

**Step 2 — ND CIT:**

```
Bracket 1: $25,000   × 1.41% = $    352.50
Bracket 2: $25,000   × 3.55% = $    887.50
Bracket 3: $4,950,000 × 4.31% = $213,345.00
                                 ----------
Total ND CIT                    $214,585.00
```

**Step 3 — Total ND tax burden (entity-level only):**

```
ND CIT (Form 40)                        $214,585
ND Oil Extraction Tax (paid separately)  $3,000,000
ND Oil & Gas Gross Production Tax        (varies — typically a similar magnitude)
                                        ----------
Total entity-level ND tax              ~$5M+
```

**Takeaway — audit flash point.** The severance taxes are vastly larger than the CIT for an ND oil producer and are governed by entirely separate statutes and forms. A new ND practitioner who attempts to net severance tax against CIT, or to claim a CIT credit, will produce a materially wrong return. The two regimes are independent. The only interaction is that the severance taxes are federally deductible (reducing federal taxable income, which is the starting point for ND CIT). For the actual severance computation, refer to a dedicated `nd-oil-extraction-tax` skill (not yet authored as of v0.1).

## 12. Quick Reference Summary Table

**Quick Reference Summary Table**

| Item | 2024 | 2025 | 2026 (planning) |
| --- | --- | --- | --- |
| ND CIT bracket 1 (up to $25,000) | 1.41% | 1.41% | 1.41% [VERIFY] |
| ND CIT bracket 2 ($25K–$50K) | 3.55% | 3.55% | 3.55% [VERIFY] |
| ND CIT bracket 3 (above $50K) | 4.31% | 4.31% | 4.31% [VERIFY] |
| Water's-edge surtax | 3.5% | 3.5% | 3.5% [VERIFY] |
| Minimum tax | $0 | $0 | $0 |
| Franchise tax | none | none | none |
| Apportionment (default) | 3-factor, sales 2× | 3-factor, sales 2× | 3-factor, sales 2× [VERIFY] |
| Single-sales-factor elect available? | Yes [VERIFY] | Yes [VERIFY] | Yes [VERIFY] |
| Sourcing (services) | Cost-of-performance | Cost-of-performance | Cost-of-performance [VERIFY] |
| NOL carryforward period | 20 years [VERIFY] | 20 years [VERIFY] | 20 years [VERIFY] |
| NOL 80% TI limit (post-2017) | Yes | Yes | Yes |
| PTE election | NONE | NONE | NONE [VERIFY 69th session] |
| Filing form (C-corp) | Form 40 | Form 40 | Form 40 |
| Filing form (S-corp) | Form 60 | Form 60 | Form 60 |
| Filing form (partnership) | Form 58 | Form 58 | Form 58 |
| Est. tax threshold | $5,000 [VERIFY] | $5,000 [VERIFY] | $5,000 [VERIFY] |
| Due date (calendar) | Apr 15 | Apr 15 | Apr 15 |
| ND PIT rate (top, for context) | ~2.50% | ~2.50% | ~2.50% |

## 13. Refusal Catalogue

- **Insurance companies** — Subject to the gross premiums tax under NDCC § 26.1-03-17, not Form 40 CIT. Refuse the engagement; refer to insurance-tax specialist.  _(NDCC § 26.1-03-17)_
- **Bank of North Dakota** — State-owned instrumentality under NDCC Ch. 6-09. Pays no corporate income tax. Has no Form 40 filing obligation. Audit flash point: practitioners encountering BND in apportionment denominators or intercompany analyses should refer to ND Treasury / specialized counsel.  _(NDCC Ch. 6-09)_
- **Private banks and financial institutions** — Subject to the financial institution privilege tax under NDCC Ch. 57-35.3, computed on net worth (not income). Form 35 series, not Form 40. Refuse standard CIT engagement; refer to financial-institution tax specialist.  _(NDCC Ch. 57-35.3)_
- **Oil and gas severance taxes** — NDCC Ch. 57-51 (gross production) and NDCC Ch. 57-51.1 (extraction). Computed at the wellhead on producer's net interest. NOT a CIT computation; NOT reduced by NOL; NOT credited against CIT. Refer to dedicated severance skill (not yet authored) or to a ND oil & gas tax specialist. Surface as audit flash point — see § 11.4.  _(NDCC Ch. 57-51 / NDCC Ch. 57-51.1)_
- **Coal Conversion Tax** — Coal Conversion Tax (NDCC Ch. 57-60). Separate severance regime on coal mined in ND. Out of scope.  _(NDCC Ch. 57-60)_
- **Cigarette / tobacco / liquor excise taxes** — Out of scope.
- **Multistate combined / unitary reporting beyond standard** — Complex Joyce / Finnigan questions, intercompany transfer pricing audits, and §482-style adjustments require a multistate tax specialist. Refer.
- **Transfer pricing and § 482 adjustments** — Refuse; refer to multistate / international tax specialist.
- **Captive REITs, captive RICs, and REIT subsidiary structures** — Special add-back rules; refer.
- **Federal tax controversy / IRS examination support** — Refer to tax controversy specialist.
- **Real and personal property tax assessments** — Real and personal property tax assessments (county/city level). Refer to local-tax specialist.
- **ND Indian Country tax issues** — ND Indian Country tax issues (tribal sovereignty, tax-immunity questions on reservation activity for the Three Affiliated Tribes / Standing Rock / Spirit Lake / Turtle Mountain / Trenton Indian Service Area). Highly fact-specific; refer to tribal-law specialist.
- **Renaissance Zone / Opportunity Zone tax credits** — Renaissance Zone / Opportunity Zone tax credits under NDCC Ch. 40-63 — not addressed in this v0.1; refer to a dedicated ND credits skill.  _(NDCC Ch. 40-63)_

## 14. Provenance and Authority

### 14.1 Primary statutory authority

- **N.D.C.C. Chapter 57-38** — Income Tax Act of 1981 (corporate provisions).  _(N.D.C.C. Chapter 57-38)_
- **N.D.C.C. § 57-38-30** — Corporate income tax rate brackets [VERIFY section number — practitioner guides also reference § 57-38-30.3].  _(N.D.C.C. § 57-38-30)_
- **N.D.C.C. § 57-38-01.4** — NOL conformity with federal § 172.  _(N.D.C.C. § 57-38-01.4)_
- **N.D.C.C. § 57-38-08** — Sourcing rules and ND-source income.  _(N.D.C.C. § 57-38-08)_
- **N.D.C.C. § 57-38-34** — Due dates for corporate returns.  _(N.D.C.C. § 57-38-34)_
- **N.D.C.C. § 57-38-45** — Penalties.  _(N.D.C.C. § 57-38-45)_
- **N.D.C.C. § 57-38-62** — Estimated-tax requirements for corporations.  _(N.D.C.C. § 57-38-62)_
- **N.D.C.C. Chapter 57-38.1** — Apportionment (UDITPA-derived).  _(N.D.C.C. Chapter 57-38.1)_
- **N.D.C.C. § 57-38.1-09** — Three-factor formula and single-sales-factor election [VERIFY subsection].  _(N.D.C.C. § 57-38.1-09)_
- **N.D.C.C. § 57-38.1-15** — Water's-edge surtax.  _(N.D.C.C. § 57-38.1-15)_
- **N.D.C.C. § 57-38.1-16** — Sales-factor sourcing.  _(N.D.C.C. § 57-38.1-16)_
- **N.D.C.C. § 57-38.1-18** — Alternative apportionment.  _(N.D.C.C. § 57-38.1-18)_
- **N.D.C.C. § 57-38.1-19** — Combined / unitary reporting.  _(N.D.C.C. § 57-38.1-19)_

### 14.2 Cross-referenced (out-of-scope) statutes

- **N.D.C.C. Chapter 6-09** — Bank of North Dakota organization and tax status.  _(N.D.C.C. Chapter 6-09)_
- **N.D.C.C. Chapter 57-35.3** — Financial institution privilege tax (private banks).  _(N.D.C.C. Chapter 57-35.3)_
- **N.D.C.C. § 26.1-03-17** — Insurance gross premiums tax.  _(N.D.C.C. § 26.1-03-17)_
- **N.D.C.C. Chapter 57-51** — Oil and Gas Gross Production Tax.  _(N.D.C.C. Chapter 57-51)_
- **N.D.C.C. Chapter 57-51.1** — Oil Extraction Tax.  _(N.D.C.C. Chapter 57-51.1)_
- **N.D.C.C. Chapter 57-60** — Coal Conversion Tax.  _(N.D.C.C. Chapter 57-60)_

### 14.3 Session laws (key reforms)

- **2015 — Rate bracket stabilization** — The current 1.41% / 3.55% / 4.31% brackets have been stable since 2015 [VERIFY session law citation].  _([VERIFY session law citation])_
- **2023 — 68th Legislative Assembly** — Considered tax reform; did not enact PTET.  _(68th Legislative Assembly)_
- **2025 — 69th Legislative Assembly** — Confirmed status of CIT brackets and continued absence of PTET as of session conclusion [VERIFY].  _(69th Legislative Assembly [VERIFY])_

### 14.4 Administrative guidance

- **Form 40 Corporation Income Tax Booklet (2025)** — ND Office of State Tax Commissioner. Source of bracket confirmation, due-date confirmation, water's-edge surtax mechanics, and Schedule SA apportionment instructions.  _(Form 40 Corporation Income Tax Booklet (2025))_
- **Form 40-ES instructions** — estimated-tax mechanics and $5,000 threshold [VERIFY].  _(Form 40-ES instructions)_
- **Form 40-UT instructions** — underpayment penalty computation.  _(Form 40-UT instructions)_
- **Form 60 instructions** — ND S-corporation filing.  _(Form 60 instructions)_
- **Form 58 instructions** — ND partnership filing.  _(Form 58 instructions)_
- **ND Office of State Tax Commissioner Corporate Income Tax web page** — current rates, forms, and Commissioner directives.  _([tax.nd.gov/business/corporate-income-tax](tax.nd.gov/business/corporate-income-tax))_

### 14.5 Cross-references in this skill bundle

ND personal income tax (Form ND-1), relevant for S-corp shareholders, LLC members, and the SALT-cap discussion (since no PTET workaround exists).

ND sales and use tax (separate regime).

Federal corporate return assembly (Form 1120) feeding ND starting taxable income.

Federal/state S-corp election framework — particularly relevant in ND given the absence of PTET makes the C-corp vs. S-corp analysis non-trivial.

federal SALT-cap parameters and OBBBA conformity.

### 14.6 Verification status

pending (skill is in draft; awaiting credentialed ND CPA/EA review per the verification model — lead + contributors per country).

entire skill (rate brackets, apportionment weighting, sourcing rules, NOL parameters, estimated-tax threshold, PTET absence confirmation through 69th Legislative Assembly).

1. Confirm 2025 bracket thresholds ($25,000 / $50,000) and rates (1.41% / 3.55% / 4.31%) in current NDCC § 57-38-30.
2. Confirm three-factor formula weighting (sales 2×) and that single-sales-factor election is still available under § 57-38.1-09.
3. Confirm ND has not adopted broad market-based sourcing as of TY 2025.
4. Confirm NOL carryforward period (20 years) and conformity with federal 80% TI limit.
5. Confirm $5,000 estimated-tax threshold under § 57-38-62.
6. Confirm absence of PTET through the 69th Legislative Assembly (2025).
7. Confirm water's-edge surtax remains at 3.5%.
8. Confirm sections of Form 40 booklet that reference current Schedule SA mechanics and any 2025 form-line renumbering.

### 14.7 Citation discipline

- **Re-verification requirement** — All statutory rate, threshold, and apportionment claims must be re-verified against the cited statute on each filing-season run.
- **Form line renumbering** — ND form line numbers may change year-to-year; cross-tie to the current-year Form 40 booklet before relying on line-level guidance in production.

Worked examples are illustrative; precise mechanics on the actual Form 40 / Schedule SA may differ in line ordering and rounding conventions.

This skill is **not** a substitute for credentialed reviewer signoff under the OpenAccountants verification model.

### 14.8 Audit flash points (re-summary)

For the reviewer's quick scan:

- **Bank of North Dakota** — state instrumentality, pays no CIT. Do not confuse with private banks (which pay the privilege tax under NDCC Ch. 57-35.3). See § 13 #2 and #3.  _(NDCC Ch. 57-35.3)_
- **Oil Extraction Tax** — severance, NOT income tax. Computed at well, not on Form 40. No CIT credit. See § 11.4 and § 13 #4.
- **No PTET in ND** — high-income S-corp owners cannot escape federal SALT cap via entity-level election. Materially different from NC, CA, NY, MN. See § 9.
- **Three-factor (not single-sales) by default** — practitioners migrating from single-sales states must use the modified UDITPA formula unless the taxpayer has elected single-sales. See § 6.
- **Cost-of-performance sourcing for services** — ND has not adopted market-based sourcing. See § 7.2.
- **Combined / unitary reporting required** — ND is not a separate-return state. See § 10.6.
- **No minimum tax, no franchise tax** — a zero-income ND C-corp owes $0 entity-level tax (still must file). See § 5.3 and § 5.4.

## End of nd-corporate-tax.md

*End of nd-corporate-tax.md (v0.1, 2026-05-28).*

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
