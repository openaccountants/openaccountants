---
name: pa-local-eit
description: Pennsylvania Local Earned Income Tax (LEIT) — Act 32 of 2008
jurisdiction: US-PA
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# PA Local Eit

## Pennsylvania Local Earned Income Tax (LEIT) — Act 32 of 2008

Pennsylvania Local Earned Income Tax (LEIT) is a municipal and school district wage tax imposed under the Local Tax Enabling Act (Act 511 of 1965), as overhauled by Act 32 of 2008. Rates run roughly 0.5% to 3.9%; most combined (municipality + school district) rates fall between 1.0% and 1.5%. Act 32 created 70 county-based Tax Collection Districts (TCDs) with a single appointed collector each. Employers must withhold each payroll based on the employee's resident PSD code (Political Subdivision code) reported on Form CLGS-32-6, remit quarterly, and file an annual reconciliation. Self-employed individuals file an annual return by April 15 with quarterly estimates. Philadelphia is governed separately under the Sterling Act of 1932 and is outside the Act 32 regime. Tax year 2025.

## 1. Scope and legal basis

### 1.1 Statutory framework

- **Statutory framework** — Pennsylvania's local earned income tax (LEIT) is authorised by the Local Tax Enabling Act (Act 511 of 1965, 53 P.S. §6924.101 et seq.), as amended by Act 32 of 2008 (effective for tax years beginning on or after January 1, 2012). Act 32 consolidated approximately 560 separately administered local EIT regimes into 70 Tax Collection Districts (TCDs), one per county (Allegheny County split into four TCDs by statute, hence 69 county-based districts plus the special Allegheny structure totalling the canonical 70-figure). The statutory authority for the tax itself remains Act 511; Act 32 governs collection, withholding, reciprocity, and reporting mechanics. Act 511 sets rate ceilings and defines 'earned income' and 'net profits'; Act 32 imposes universal employer withholding and the resident-rate withholding rule.  _(53 P.S. §6924.101 et seq.; Act 32 of 2008)_

### 1.2 What is taxed

- **Earned income and Net profits** — Earned income: compensation for services rendered — wages, salaries, commissions, bonuses, tips, taxable fringe benefits, and similar items, generally aligned with PA PIT Class 1 (compensation). Net profits: net income from operation of a business, profession, or other activity (sole proprietorship, single-member LLC disregarded for federal tax, partnership distributive share allocated to a PA-resident partner) — generally aligned with PA PIT Class 4. LEIT does not apply to: interest, dividends, capital gains (other than business-asset gains caught by net profits), rental income (generally), pensions, Social Security, unemployment compensation, military pay (active duty exemption under Act 32 for service outside PA), or gambling winnings.

### 1.3 Geographic scope

- **Geographic scope** — Every PA municipality (city, borough, township, town) and every PA school district has the authority to impose an EIT under Act 511, except Philadelphia — which operates under the Sterling Act of 1932 (Act of August 5, 1932, P.L. 45, 53 P.S. §15971 et seq.). See Section 8. Approximately 2,500 of PA's 2,560 municipalities impose some form of EIT; the few that do not are typically low-population townships that have not enacted the levy. Every school district overlapping a taxing municipality may also impose its own EIT layer.  _(53 P.S. §15971 et seq.)_

### 1.4 Interaction with PA state Personal Income Tax (PIT)

- **LEIT vs PA PIT** — LEIT is in addition to PA state PIT, which is a flat 3.07% under 72 P.S. §7302. The two taxes do not interact — there is no credit on the PA state return for LEIT paid, and no credit on the LEIT return for state PIT paid. They are parallel obligations.  _(72 P.S. §7302)_

### 1.5 What this skill covers

This skill covers the Act 32 regime: PSD codes, employer withholding, Form CLGS-32-6 (Residency Certification), annual final return preparation, quarterly estimated tax for self-employed individuals, and reciprocal credit between PA municipalities. It also covers the Sterling Act (Philadelphia) regime at the level of triage — i.e., how to recognise a Philadelphia case, what rates apply, and where to route the work.

### 1.6 What this skill does NOT cover

- Philadelphia Business Income & Receipts Tax (BIRT) — separate skill required.
- Philadelphia Net Profits Tax (NPT) at preparation depth — overview only (Section 9).
- Local Services Tax (LST) — the flat $52/year occupational tax under Act 7 of 2007 — separate skill.
- Per Capita Tax — flat-rate residence tax authorised under Act 511 §301 — separate skill.
- Occupation Privilege Tax — pre-Act 7 forerunner of LST, retained in a few jurisdictions — separate skill.
- Mercantile / Business Privilege Tax — gross receipts tax in certain home-rule cities — separate skill.

## 2. Rates

### 2.1 General rate range (non-Philadelphia)

- **Combined LEIT rate range** — 0.5% to approximately 3.9% percent (Combined municipality + school district LEIT rates on taxable earned income and net profits)
- **Municipality rate (most common floor)** — 0.5% percent  _(Act 511 §311(1))_
- **School district rate (most common)** — 0.5% percent (may impose under Act 1 of 2006 referendum or historic Act 511 share)
- **Typical combined rate** — 1.0% (split 0.5% / 0.5%) percent

### 2.2 Statutory ceiling

- **Combined rate cap on residents** — 1.0% percent (unless municipality is Act 47 distressed (DCED approval), home rule charter with adopted higher rate, or has Act 1 of 2006 voter-approved EIT increase)  _(Act 511 §311(1))_

### 2.3 Higher-rate cities (illustrative; verify current rate with DCED)

**Higher-rate cities (illustrative; verify current rate with DCED)**

| Municipality | Combined resident rate (illustrative) |
| --- | --- |
| Reading (Berks Co.) | ~3.6% |
| Scranton (Lackawanna Co.) | ~3.4% |
| Bethlehem (Northampton/Lehigh Co.) | ~1.0% |
| Allentown (Lehigh Co.) | ~1.975% |
| Harrisburg (Dauphin Co.) | ~2.0% (Act 47) |
| Pittsburgh (Allegheny Co.) | ~3.0% (1% municipal + 2% school district) |
| Wilkes-Barre (Luzerne Co.) | ~3.0% |
| Lancaster City (Lancaster Co.) | ~1.1% |
| York City (York Co.) | ~1.25% |
| Erie (Erie Co.) | ~1.65% |
| Chester (Delaware Co.) | ~3.75% (Act 47) |

CRITICAL: These rates change frequently. The DCED publishes the current rates at the Pennsylvania Municipal Statistics portal (https://munstats.pa.gov), which is the authoritative source. Always pull the current-year rate before preparing a return.

### 2.4 Non-resident rate

- **Non-resident rate rule** — A non-resident who works in a PA municipality pays the lower of: the work municipality's non-resident rate (often 1.0% in non-distressed municipalities; higher in Act 47 cities), or the resident municipality's resident rate. Under Act 32, the employer withholds the higher of (resident rate at employee's home, non-resident rate at work location). The resident TCD then administers the reciprocal credit (Section 7).

### 2.5 Philadelphia rates (preview — see Section 8)

- **Philadelphia resident wage tax (2025)** — 3.75% percent (effective July 1, 2025; was 3.75% effective July 1, 2024; verify against City of Philadelphia Department of Revenue announcement for rate effective during the wage period at issue)
- **Philadelphia non-resident wage tax (2025)** — 3.44% percent (the non-resident rate has historically been ~92% of the resident rate; verify current)
- **Philadelphia Net Profits Tax (NPT)** — resident 3.75% / non-resident 3.44% percent (same rates as wage tax, with adjustments — see Section 9)

Philadelphia rates change every July 1. Always pull the wage period-specific rate.

### 2.6 Rate base

- **LEIT rate base treatment** — LEIT applies to gross compensation (no deduction for federal income tax, FICA, or PA state PIT) and net profits (after PA Schedule C-style business deductions). Pre-tax §125 cafeteria plan deductions (health insurance, FSA) are not subject to LEIT — excluded from the wage base, mirroring PA PIT treatment. Pre-tax §401(k) deferrals, however, are subject to LEIT (PA does not conform to the federal exclusion for §401(k); the deferral is taxable when contributed for both PA PIT and LEIT purposes). This single point is the most common LEIT preparation error and warrants a self-check on every return.

## 3. Act 32 collection regime

### 3.1 Tax Collection Districts (TCDs)

- **TCD structure** — Act 32 §503 created 70 Tax Collection Districts. Boundaries follow county lines: 66 of PA's 67 counties = one TCD each (excluding Philadelphia, which is outside Act 32). Allegheny County is split into four TCDs: Allegheny Central, Allegheny North, Allegheny Southeast, and Allegheny Southwest. The City of Pittsburgh is its own subdivision within these. The remaining 70th slot is occupied historically by the 'Philadelphia TCD,' though Philadelphia operates under Sterling and not Act 32 — references to '70 TCDs' in practitioner literature include Philadelphia as a nominal placeholder.  _(Act 32 §503)_

### 3.2 Tax officers

- **Tax officer administration** — Each TCD elects a single tax officer to administer collection. Three private firms dominate the market: Berkheimer Tax Innovations (HAB) — covers many southeastern and northeastern PA TCDs; Keystone Collections Group — covers many south-central and southwestern PA TCDs (other than Allegheny core); Jordan Tax Service — covers Allegheny TCDs (particularly Allegheny Southwest). A handful of TCDs are administered by municipal authorities directly (e.g., Capital Tax Collection Bureau for Cumberland/Dauphin/Perry). The DCED publishes the current TCD/tax officer assignment at munstats.pa.gov.

### 3.3 What the tax officer does

- **Tax officer duties** — The TCD tax officer: receives employer withholding remittances quarterly; receives employer annual reconciliations; receives self-employed estimated payments quarterly; receives annual final returns from residents (Berkheimer Form CLGS-32-1; Keystone uses a similar form); distributes the collected revenue to the relevant municipality and school district based on PSD codes on each remittance; audits, issues notices, assesses penalty and interest.

### 3.4 Distribution mechanism

- **PSD-based routing** — The tax officer matches each dollar of remitted EIT to a PSD code and forwards the funds to the municipality and school district that share that PSD code. This is why PSD codes are non-optional — without them, the tax officer cannot route the revenue.

### 3.5 Quarterly remittance deadlines (employers)

**Quarterly remittance deadlines (employers)**

| Quarter | Period | Remittance due |
| --- | --- | --- |
| Q1 | Jan 1 – Mar 31 | Apr 30 |
| Q2 | Apr 1 – Jun 30 | Jul 31 |
| Q3 | Jul 1 – Sep 30 | Oct 31 |
| Q4 | Oct 1 – Dec 31 | Jan 31 (following year) |

### 3.6 Annual reconciliation (employers)

- **Employer annual reconciliation deadline** — The employer files an annual reconciliation of withholding with the tax officer by February 28 (sometimes by January 31, depending on the tax officer — Berkheimer requires Feb 28; Keystone requires Feb 28; confirm with the specific tax officer). The reconciliation must include each employee's PSD code, gross compensation, EIT withheld, and W-2 box totals.

### 3.7 Annual final return (individuals)

- **Individual annual final return deadline** — Residents file an annual final return with the tax officer by April 15 (aligned with federal and PA state). Extensions are typically honoured if a federal extension (Form 4868) is filed, but the local tax officer must be notified — practice varies. Berkheimer accepts a copy of the federal extension as evidence; Keystone requires an explicit local request.

## 4. PSD codes and Form CLGS-32-6

### 4.1 What a PSD code is

- **PSD code definition** — A Political Subdivision (PSD) code is a 6-digit numeric identifier for a specific PA municipality and school district pairing. The first two digits identify the TCD (county); the next two identify the municipality; the last two identify the school district. Example: PSD code 150602 identifies a specific borough in Cumberland County (TCD 15) within a specific school district. The DCED maintains the official PSD code register at munstats.pa.gov/Public/FindLocalTax.aspx, where any PA address can be looked up to retrieve the resident PSD code, the resident EIT rate, the non-resident EIT rate, and the tax officer.  _(munstats.pa.gov/Public/FindLocalTax.aspx)_

### 4.2 Why PSD codes matter

- **PSD code functions** — PSD codes drive three things: 1. Withholding rate: the employer pulls the resident rate for the employee's home PSD and the non-resident rate for the worksite PSD; withholds the higher of the two. 2. Revenue routing: the tax officer uses the PSD code on each remittance to distribute funds to the correct municipality and school district. 3. Reciprocal credit: the resident TCD uses the work-location PSD code on the annual return to compute the credit for tax paid to another PA jurisdiction (Section 7).

### 4.3 Form CLGS-32-6 — Residency Certification

- **Form CLGS-32-6 contents and use** — Every PA employee must complete a Residency Certification Form (Form CLGS-32-6) at hire and whenever they change residence or worksite. The form captures: Employee name, SSN, address; Resident PSD code (from munstats.pa.gov lookup of home address); Resident EIT rate; Worksite address; Work location PSD code (from munstats.pa.gov lookup of worksite address); Work location non-resident EIT rate; Employee signature certifying accuracy. Employers retain Form CLGS-32-6 in the payroll file (no filing with DCED or the tax officer). The form is the employer's defence in an audit: if the employee misrepresents their PSD code, the employer is generally held harmless if it relied on a properly completed CLGS-32-6.  _(Form CLGS-32-6)_

### 4.4 W-2 reporting

- **W-2 box mapping** — PA employers report local EIT on Form W-2: Box 18 — Local wages; Box 19 — Local income tax withheld; Box 20 — Locality name (commonly the PSD code itself, e.g., '150602', or the municipality + school district name truncated). If the employee worked in multiple PSDs during the year (e.g., transferred mid-year), the W-2 will show multiple lines in boxes 18-20, one per PSD.

### 4.5 Multi-state employees

- **Multi-state employee LEIT rule** — A PA resident working entirely in another state (e.g., New Jersey, Delaware, New York) still owes LEIT at the resident rate on those wages. The employer — even an out-of-state employer — must withhold and remit (see Section 5.4). The employee then claims a state income tax credit on the PA state PIT return (Schedule G-L) for the other state's tax paid, but no credit is available on the LEIT return against another state's tax. This is because Act 32's reciprocity is internal to PA only; tax paid to NJ or NY does not reduce PA LEIT. This is a frequently misunderstood point. See Worked Example 2 in Section 10.

## 5. Employer obligations

### 5.1 Registration

- **Employer registration requirement** — An employer with a PA worksite (or with PA-resident employees, even if the employer is out-of-state — see 5.4) must register with the TCD tax officer for the work-location TCD. Most tax officers offer online registration (Berkheimer: e-Tides portal; Keystone: e-file portal).

### 5.2 Per-payroll withholding

- **Per-payroll withholding steps** — On each payroll, the employer: 1. Determines the employee's resident PSD and rate (from Form CLGS-32-6). 2. Determines the worksite PSD and non-resident rate (from Form CLGS-32-6). 3. Compares the two rates. 4. Withholds the higher of the resident rate or the non-resident rate, on the LEIT base (gross compensation excluding §125 pre-tax, including §401(k) deferrals — see Section 2.6). 5. Codes the withholding to the resident PSD for remittance routing.

### 5.3 Pittsburgh-specific Local Services Tax (LST) overlay

- **LST overlay note** — Pittsburgh and several other distressed cities also impose a Local Services Tax (LST) — a flat $52/year ($1/week or $2/biweekly) on every employee working in the jurisdiction. This is separate from EIT and is governed by Act 7 of 2007. It is not covered in this skill — see the dedicated LST skill — but the practitioner should note it because Pittsburgh's $52 LST is often confused with EIT withholding on the pay stub.  _(Act 7 of 2007)_

### 5.4 Out-of-state employers with PA employees

- **Out-of-state employer withholding requirement** — Under Act 32 §512, an out-of-state employer that employs a PA resident is required to withhold PA LEIT on that employee's wages. This was a major reform in 2008 — pre-Act 32, out-of-state employers were not consistently required to withhold, and PA residents working remotely for out-of-state employers often had no withholding and faced large balances due at year-end. Enforcement: Act 32 §512 authorises the TCD to seek a court order compelling withholding. In practice, larger out-of-state employers (e.g., NYC investment banks with PA-resident commuters) comply. Smaller out-of-state employers often do not, and the PA-resident employee must instead make quarterly estimated payments directly to their resident TCD tax officer. See Worked Example 3 in Section 10.  _(Act 32 §512)_

### 5.5 Quarterly remittance

- **Employer quarterly remittance filing** — The employer files a quarterly remittance with the resident TCD tax officer of each employee, accompanied by Form CLGS-32-1A (employer quarterly return — used by Berkheimer and similar tax officers; Keystone uses a parallel form). Due dates per Section 3.5.  _(Form CLGS-32-1A)_

### 5.6 Annual reconciliation

- **Annual reconciliation content** — The employer files an annual reconciliation (per Section 3.6) plus Form W-2 copies for each employee. The reconciliation lines tie to: Total compensation paid (cross-checks to federal Form 941 totals, with PA-state adjustments for §125 / §401(k)); Total EIT withheld; Per-employee breakdown with PSD code, gross, withheld.

### 5.7 Penalties for non-compliance

- **Employer penalty schedule** — Failure to withhold: the employer is liable for the unwithheld tax, plus interest at the statutory rate (6% per annum or as adjusted) and a penalty of up to 30% under Act 32 §509. Failure to remit: similar interest and penalty, plus possible criminal liability for wilful failure under Act 511 §513. Failure to file annual reconciliation: $25 per W-2 not reported, capped under tax officer regulations.  _(Act 32 §509; Act 511 §513)_

## 6. Self-employed individuals

### 6.1 Who is "self-employed" for LEIT

- **Self-employed definition for LEIT** — Self-employed for LEIT purposes includes: Sole proprietors filing federal Schedule C; Single-member LLCs disregarded for federal tax (file Schedule C); Partners in a partnership (distributive share of trade or business income reported on PA Schedule RK-1); Independent contractors receiving Form 1099-NEC. Note: S-corporation shareholders are not self-employed for LEIT purposes on their K-1 distributive share — only their reasonable-compensation W-2 wages are LEIT-taxable.

### 6.2 Annual filing obligation

- **Self-employed annual return components** — A self-employed PA resident files the annual final return (Form CLGS-32-1 or tax-officer equivalent) with their resident TCD tax officer by April 15, reporting: Earned income (W-2 wages, if any); Net profits from Schedule C / partnership distributive share; Less: PA-conforming business expenses; Times: resident EIT rate; Less: EIT withheld by employer (if any); Less: quarterly estimated payments made; Less: reciprocal credit for tax paid to another PA jurisdiction (Section 7); = Balance due / refund.  _(Form CLGS-32-1)_

### 6.3 Quarterly estimated payments

**Quarterly estimated payments due dates**

| Quarter | Estimate due |
| --- | --- |
| Q1 | Apr 30 |
| Q2 | Jul 31 |
| Q3 | Oct 31 |
| Q4 | Jan 31 (following year) |

Note: these are calendar-quarter deadlines, NOT the federal 1040-ES deadlines. The federal Q2 estimate is due June 15 and Q3 is due September 15; the PA LEIT estimates are due July 31 and October 31. Practitioners often miss this mismatch. Most TCD tax officers accept ACH, check, or online card payment.

### 6.4 Underpayment penalty

- **Underpayment interest rule** — The tax officer charges interest on any underpayment of estimated tax, computed quarter-by-quarter at the statutory rate (typically 6% per annum), under Act 511 §509 as carried forward through Act 32. There is no safe-harbour mechanism analogous to the federal §6654 prior-year safe harbour — every quarter must be substantially paid. Practitioners should compute estimates from the current year's projection, not from the prior year's tax, and adjust each quarter.  _(Act 511 §509)_

### 6.5 Net profits scope

- **PA Schedule C adjustments affecting LEIT base** — LEIT 'net profits' generally tracks PA Schedule C (PA-40 Schedule C) — which itself tracks federal Schedule C with several PA-specific adjustments: No §179 expensing limit difference — PA conforms to federal §179 in principle but with a separate ceiling. No bonus depreciation — PA does not conform to federal §168(k) bonus depreciation; the federal bonus must be added back and depreciation recomputed on straight-line / MACRS without bonus. No federal QBI deduction — PA (and therefore LEIT) does not allow §199A. Home office — PA conforms to federal §280A in principle but applies its own substantiation standard. These adjustments cascade into the LEIT computation: a sole prop's federal Schedule C net profit will frequently differ from PA Schedule C net profit, which is the LEIT base.

## 7. Reciprocal credit between PA municipalities

### 7.1 The general rule

- **General reciprocal credit rule** — A PA resident who works in another PA municipality (and pays that municipality's non-resident EIT) is entitled to a credit against their resident EIT for the non-resident tax paid, limited to the amount of resident EIT that would otherwise apply to the same wages.

### 7.2 Mechanics

- **Reciprocal credit computation** — On the annual return (Form CLGS-32-1), the resident TCD tax officer computes: 1. Resident tax: Wages × resident rate. 2. Less credit: lesser of (non-resident tax paid to work municipality, resident tax on those wages). 3. = Resident tax due to home TCD.  _(Form CLGS-32-1)_

### 7.3 Why withholding handles most cases automatically

- **Automatic withholding reconciliation** — Under Act 32, the employer withholds the higher of (resident, non-resident) rates and codes the withholding to the resident PSD. This means: if the resident rate > non-resident rate (typical), the resident rate is withheld and routed to the home TCD — no credit needed, no inter-jurisdictional flow. If the non-resident rate > resident rate (e.g., resident lives in a low-rate township, works in a 3%+ Act 47 city), the non-resident rate is withheld — the work TCD takes its non-resident share; the home TCD takes nothing because the credit absorbs the full resident tax. The annual return effectively just reconciles this. The complexity arises when the employer fails to withhold correctly or when the employee has multiple jobs in different PSDs.

### 7.4 Limits

- **Credit limitation rule** — The credit is limited to the resident EIT rate on the work-municipality wages. If the non-resident rate exceeds the resident rate, the excess is not refundable — it stays with the work municipality. This is constitutional under PA case law (see Pittsburgh v. Alco Parking Corp., 417 U.S. 369 (1974), and related state-court decisions).  _(Pittsburgh v. Alco Parking Corp., 417 U.S. 369 (1974))_

### 7.5 No credit for non-PA tax

- **Non-PA state tax non-creditable against LEIT** — Tax paid to New Jersey, New York, Delaware, Ohio, West Virginia, Maryland (states bordering PA) is not creditable against LEIT. Only intra-PA tax credits. PA does provide a credit on the state PIT return (PA-40 Schedule G-L) for tax paid to other states, but that credit operates against the 3.07% state PIT, not LEIT. See Worked Example 2.  _(PA-40 Schedule G-L)_

### 7.6 Credit for Philadelphia tax paid

- **Philadelphia tax credit rule** — A PA resident living in (say) Bucks County who works in Philadelphia and pays Philadelphia's 3.44% non-resident wage tax is entitled to credit Philadelphia tax against their Bucks County LEIT. This is a specific Act 32 reciprocity rule even though Philadelphia is outside Act 32 — the resident TCD allows the credit by statute. Documentation: the W-2 with Philadelphia wage tax in Box 19 plus the locality 'Philadelphia' in Box 20, or a Philadelphia BIRT/wage tax statement. See Worked Example 4 in Section 10.

## 8. Philadelphia exception — the Sterling Act

### 8.1 Statutory basis

- **Sterling Act basis** — The Sterling Act of 1932 (Act of August 5, 1932, P.L. 45, 53 P.S. §15971 et seq.) grants the City of Philadelphia broad taxing authority that predates and is independent of Act 511 and Act 32. Philadelphia is the only PA municipality outside the Act 32 regime.  _(53 P.S. §15971 et seq.)_

### 8.2 Sterling Act primacy

- **Sterling Act primacy over Act 511** — Under longstanding PA Supreme Court jurisprudence (Murray v. Philadelphia, 364 Pa. 157 (1950); Philadelphia v. Cohen, 429 Pa. 109 (1968)), the Sterling Act takes priority over Act 511. The practical consequence: when a non-Philadelphia PA resident works in Philadelphia, Philadelphia takes the non-resident wage tax first, and the resident's home municipality must yield up to the amount of Philadelphia tax paid (Section 7.6).  _(Murray v. Philadelphia, 364 Pa. 157 (1950); Philadelphia v. Cohen, 429 Pa. 109 (1968))_

### 8.3 Philadelphia wage tax rates

**Philadelphia wage tax rates**

| Period | Resident rate | Non-resident rate |
| --- | --- | --- |
| Effective Jul 1, 2024 – Jun 30, 2025 | 3.75% | 3.44% |
| Effective Jul 1, 2025 – Jun 30, 2026 | 3.75% (verify) | 3.44% (verify) |

ALWAYS confirm the wage-period rate against the City of Philadelphia Department of Revenue current bulletin before preparing a return that spans a July 1 boundary.

### 8.4 Who collects

- **Philadelphia collector** — The City of Philadelphia Department of Revenue (not a TCD tax officer) collects Philadelphia wage tax. Filing is via the City's e-file portal (phila.gov/revenue).  _(phila.gov/revenue)_

### 8.5 Employer obligations in Philadelphia

- **Philadelphia employer obligations** — A Philadelphia employer must: Register with the City of Philadelphia Department of Revenue (separate from Act 32 registration); Withhold resident rate on Philadelphia-resident employees regardless of where they work (the Philadelphia resident rate applies to all worldwide compensation of a Philadelphia resident, including wages earned outside the City); Withhold non-resident rate on non-Philadelphia-resident employees who work in Philadelphia; File Philadelphia wage tax reconciliation annually by the last day of February (Form W-1 quarterly returns; Annual Reconciliation); Issue W-2 with Philadelphia wage tax in Box 19 and 'Philadelphia' or '51' (Philadelphia PSD code) in Box 20.  _(Form W-1)_

### 8.6 Philadelphia residents

- **Philadelphia resident worldwide taxation** — A Philadelphia resident owes Philadelphia wage tax on all earned income, worldwide, at the resident rate (3.75%). There is no general inbound reciprocity from other PA municipalities to Philadelphia: a Philadelphia resident who works in (say) Lower Merion (Montgomery County) at a 1.0% rate cannot use the Lower Merion tax to credit against Philadelphia's 3.75%. The reciprocity flows the other way — non-Philadelphia residents working in Philadelphia get credit at home.

### 8.7 Routing in this skill

- **Philadelphia routing scope** — This skill does not prepare Philadelphia wage tax returns. Philadelphia preparation should be routed to a dedicated Philadelphia wage tax / BIRT / NPT skill. This skill handles only: Recognition that the case has a Philadelphia leg; Application of the Section 7.6 credit on the non-Philadelphia resident's LEIT return for Philadelphia tax paid.

## 9. Net Profits Tax overview (Philadelphia, Pittsburgh, and others)

### 9.1 Philadelphia Net Profits Tax (NPT)

- **Philadelphia NPT rules** — Philadelphia imposes a separate Net Profits Tax (NPT) on the net profits of any sole proprietor, single-member LLC, or partnership that is either a Philadelphia resident (taxed on worldwide net profits at the resident rate); or a non-resident with Philadelphia-source net profits (taxed on Philadelphia-source net profits at the non-resident rate). Rates mirror the wage tax: 3.75% resident / 3.44% non-resident (verify current). NPT is filed annually on Form NPT by April 15. Quarterly estimates required. NPT is in addition to the Philadelphia Business Income & Receipts Tax (BIRT), which is a separate gross-receipts and net-income hybrid tax on any business with Philadelphia activity. NPT taxpayers can claim a 60% credit against NPT for BIRT net income tax paid (a partial integration mechanism to avoid full double taxation). This skill does not prepare NPT or BIRT. Route to the dedicated Philadelphia business tax skill.  _(Form NPT)_

### 9.2 Pittsburgh Net Profits / Payroll Expense Tax

- **Pittsburgh NPT and PET** — Pittsburgh, under its home rule charter, imposes: Net Profits Tax — incorporated into the 3% combined EIT rate (1% city + 2% Pittsburgh Public Schools), applied to net profits of sole proprietors and disregarded SMLLCs. Payroll Expense Tax (PET) — 0.55% of payroll, paid by employers (not employees) on Pittsburgh-sourced wages. Administered by the City of Pittsburgh Department of Finance. Pittsburgh is inside Act 32 (it is in Allegheny County's TCD structure), so the 3% combined EIT flows through the Jordan Tax Service / TCD machinery, not through a separate Sterling-like regime.

### 9.3 Scranton, Reading, Wilkes-Barre

- **Distressed cities net profits handling** — These Act 47 distressed cities apply their elevated combined rates uniformly to net profits as well as wages — no separate NPT form is required; the standard Act 32 annual final return handles both wages and net profits at the elevated rate.

### 9.4 Practical preparation note

For a PA-resident sole proprietor (non-Philadelphia, non-Pittsburgh), the LEIT preparation is straightforward: Schedule C net profit × resident rate, less withholding and estimates, on the annual final return. For a Philadelphia or Pittsburgh sole proprietor, route to the dedicated city-specific skill.

## 10. Worked examples

### Example 1 — PA resident commuting within PA (typical case)

Taxpayer: Sarah, full-year resident of Cumberland Township, Adams County (PSD code 010101, illustrative; combined resident EIT rate 1.7%: 0.5% municipality + 1.2% school district). Worksite: Carlisle Borough, Cumberland County (PSD code 210301, illustrative; non-resident EIT rate 1.0%). 2025 W-2 box 1 wages: $80,000. 2025 W-2 PA state wages: $82,500 (reflects §401(k) deferral of $2,500 included in PA wages — PA does not conform). §125 pre-tax health insurance: $3,000 (excluded from PA wages). LEIT base: $82,500 (same as PA state wages). §125: not in base; §401(k): in base.

**Analysis table**

| Step | Detail | Amount |
| --- | --- | --- |
| 1. Determine resident rate | Adams Co. PSD 010101 | 1.7% |
| 2. Determine non-resident rate | Cumberland Co. PSD 210301 | 1.0% |
| 3. Higher rate to withhold | max(1.7%, 1.0%) | 1.7% |
| 4. Withhold on LEIT base | $82,500 × 1.7% | $1,402.50 |
| 5. Remit to | Adams Co. TCD (resident TCD) | $1,402.50 |
| 6. Annual return resident tax | $82,500 × 1.7% | $1,402.50 |
| 7. Credit for non-resident tax paid | none (employer routed all to resident TCD) | $0 |
| 8. Balance due / refund | $1,402.50 − $1,402.50 | $0 |

No balance due, no refund. Withholding matches. PSD code routing handled automatically. Annual return still required to be filed with the Adams County TCD tax officer by April 15, 2026.

### Example 2 — PA resident commuting to New Jersey

Taxpayer: Marcus, full-year resident of Bensalem Township, Bucks County (resident EIT rate 1.0%: 0.5% municipality + 0.5% school district; PSD code 090101, illustrative). Worksite: Princeton, New Jersey (out of state). Employer: Princeton-based NJ corporation. 2025 W-2 box 1 wages: $120,000. 2025 W-2 PA state wages: $123,000 (reflects $3,000 §401(k) deferral). §125: $2,000 (not in base). LEIT base: $123,000. NJ state tax withheld: $5,800. PA state tax withheld: $0 (employer treated as NJ-only).

Under Act 32 §512, the NJ employer is required to withhold PA LEIT at Bensalem's 1.0% resident rate on Marcus's wages. Whether the employer actually did so is the threshold question.

**Sub-case 2A: NJ employer DID withhold PA LEIT**

| Step | Detail | Amount |
| --- | --- | --- |
| 1. Resident rate | Bensalem 1.0% | 1.0% |
| 2. LEIT base | $123,000 | — |
| 3. LEIT due | $123,000 × 1.0% | $1,230 |
| 4. Withheld by NJ employer | per W-2 Box 19 | $1,230 |
| 5. Balance due | $0 | $0 |
| 6. NJ tax credit on PA-40 Schedule G-L | NJ tax credited against PA state PIT (3.07%) | separate computation |
| 7. NJ tax credit against LEIT | **none** — Act 32 reciprocity is intra-PA only | $0 |

Annual return required to be filed with Bucks Co. TCD tax officer by April 15, 2026.

Marcus must instead: 1. Make quarterly estimated payments of $307.50 ($1,230/4) to Bucks Co. TCD tax officer by Apr 30, Jul 31, Oct 31 of 2025 and Jan 31 of 2026. 2. File annual final return by April 15, 2026, reporting $1,230 LEIT, $1,230 estimates paid, balance due / refund $0. 3. If estimates not made: $1,230 balance due plus underpayment interest (~6%/yr quarterly compounding) on each unpaid installment. Key point: No credit for NJ tax against LEIT, regardless of whether the NJ tax is much higher than the PA LEIT. The reciprocity argument is a frequent client complaint that must be firmly rebutted.

### Example 3 — Out-of-state employer hiring PA remote worker

Taxpayer: Priya, full-year resident of Lower Macungie Township, Lehigh County (resident EIT rate 1.0%: 0.5% municipality + 0.5% school district; PSD code 390501, illustrative). Employer: California-based tech company; Priya works fully remote from her PA home. Worksite (constructive): Priya's home in Lower Macungie. 2025 W-2 box 1 wages: $145,000. 2025 PA state wages: $148,000 (reflects $3,000 §401(k)). §125: $4,000 (not in base). LEIT base: $148,000. CA state tax withheld: $0 (no CA tax — Priya is non-resident of CA performing services in PA). PA state tax withheld: $4,544 (employer correctly remitted PA-40 withholding).

- **Analysis — CA employer PA LEIT withholding obligation** — Under Act 32 §512, yes, the CA employer is required to withhold and remit PA LEIT to the Lehigh Co. TCD tax officer. The fact that the employer has no physical PA presence is irrelevant — the obligation attaches because Priya is a PA resident and the wages are PA-source (services performed in PA).  _(Act 32 §512)_

**Sub-case 3A: CA employer DID register and withhold PA LEIT**

| Step | Detail | Amount |
| --- | --- | --- |
| 1. Resident rate (and non-resident rate, since worksite = home) | 1.0% | — |
| 2. LEIT base | $148,000 | — |
| 3. LEIT due | $148,000 × 1.0% | $1,480 |
| 4. Withheld | per W-2 | $1,480 |
| 5. Balance due | $0 | $0 |

Priya: 1. Makes quarterly estimated LEIT payments of $370 ($1,480/4) to Lehigh Co. TCD tax officer. 2. Files annual return by April 15, 2026. Practitioner workflow: If the CA employer has not been withholding, the practitioner should (a) calculate Priya's correct LEIT liability and arrange catch-up estimates, and (b) prepare a letter to the employer's payroll department citing Act 32 §512 and demanding prospective compliance. Berkheimer / Keystone publish standard 'Notice to Out-of-State Employer' templates for this purpose.

### Example 4 — PA suburban resident working in Philadelphia

Taxpayer: Daniel, full-year resident of Cheltenham Township, Montgomery County (resident EIT rate 1.0%; PSD code 460201, illustrative). Worksite: Center City Philadelphia. 2025 W-2 box 1 wages: $95,000. 2025 PA state wages: $97,500 ($2,500 §401(k)). §125: $3,500 (not in base). LEIT / Philadelphia wage tax base: $97,500. Philadelphia non-resident wage tax withheld (full year 2025 at 3.44%): $3,354.

Philadelphia is outside Act 32 but the credit under Section 7.6 applies.

**Analysis table**

| Step | Detail | Amount |
| --- | --- | --- |
| 1. Cheltenham resident tax | $97,500 × 1.0% | $975.00 |
| 2. Philadelphia non-resident tax paid | $97,500 × 3.44% | $3,354.00 |
| 3. Credit allowed against Cheltenham tax | lesser of $3,354 or $975 | $975.00 |
| 4. Cheltenham LEIT due | $975 − $975 | $0 |
| 5. Philadelphia tax retained (no refund) | $3,354 − $975 credit transfer | $3,354 stays with Philadelphia |

Cheltenham (Montgomery Co. TCD) collects nothing from Daniel; the credit fully absorbs the resident liability. Daniel receives no refund from Philadelphia of the 'excess' over Cheltenham's 1.0% — Philadelphia keeps its 3.44% under the Sterling Act. Annual return still required to be filed with Montgomery Co. TCD tax officer, reporting the Philadelphia tax and the credit. Attach W-2 with Philadelphia withholding visible in Box 19 / Box 20.

### Example 5 — Self-employed PA resident (sole prop)

Taxpayer: Yusra, full-year resident of Mt. Lebanon, Allegheny County (resident EIT rate 1.0%: 0.5% municipality + 0.5% school district; PSD code 730201, illustrative). 2025 Federal Schedule C net profit: $72,000. PA Schedule C adjustments: Add back federal §168(k) bonus depreciation of $4,000 (PA does not conform); Recompute depreciation on straight-line: $1,500 PA depreciation in lieu; Add back federal QBI deduction (already not in Schedule C, but noted). PA Schedule C net profit: $72,000 + $4,000 − $1,500 = $74,500. LEIT base: $74,500 (no §125 / §401(k) adjustment for self-employed — those apply only to employee wages). No W-2 wages, no employer withholding. No tax paid to other PA jurisdiction.

**Analysis table**

| Step | Detail | Amount |
| --- | --- | --- |
| 1. LEIT base (PA Schedule C net profit) | — | $74,500 |
| 2. Resident rate | Mt. Lebanon 1.0% | 1.0% |
| 3. LEIT due | $74,500 × 1.0% | $745.00 |
| 4. Estimates required quarterly | $745 / 4 | $186.25 per quarter |
| 5. Estimate deadlines | Apr 30, Jul 31, Oct 31, Jan 31 | — |

Yusra files annual final return with Jordan Tax Service (Allegheny SW TCD) by April 15, 2026. If she missed estimates, underpayment interest (~6%/yr) accrues on each unpaid installment.

## 11. Conservative defaults and self-checks

### 11.1 Rate pulls

- **Rate lookup requirement** — Always look up the current resident and non-resident EIT rate on munstats.pa.gov for the exact address provided. Do not rely on prior-year rates or memory of 'typical' rates. Always verify the Philadelphia wage tax rate against the City of Philadelphia Department of Revenue's bulletin for the specific wage period (rates change every July 1).

### 11.2 §401(k) treatment

- **§401(k) LEIT base confirmation** — Always confirm that PA Schedule W-2 wages (PA state wages, Box 16) — not federal Box 1 — is the LEIT base. The most common error is using Box 1 and under-reporting by the §401(k) deferral.

### 11.3 PSD code verification

- **PSD code verification requirement** — Always require Form CLGS-32-6 from the client. Do not infer PSD codes from address strings — small addressing variations (e.g., 'Philadelphia, PA' vs. 'Bala Cynwyd, PA 19004') materially change the PSD code.

### 11.4 Out-of-state employer review

- **Out-of-state employer withholding check** — Always ask whether the employer has been withholding PA LEIT. If not, arrange quarterly estimates and warn the client about underpayment interest.

### 11.5 Philadelphia leg

- **Philadelphia leg check** — Always check whether any wages were Philadelphia-source. If yes, route Philadelphia preparation to a dedicated skill but apply the Section 7.6 credit on the home-municipality return.

### 11.6 Annual return filing

- **Annual return filing requirement** — Always file the annual return with the resident TCD tax officer even when withholding fully covers the liability. Failure to file triggers tax officer notice cycles and possible $25–$300 non-filer penalties depending on the tax officer.

### 11.7 Pittsburgh / Scranton / Reading

- **Elevated rate city flag** — Always flag these as elevated-rate cases (3.0%–3.9% combined) and reconfirm with current munstats.pa.gov rates.

### 11.8 Multiple jobs

- **Multiple PSD job reconciliation** — If the client has multiple PA jobs in different PSDs, request all W-2s and Forms CLGS-32-6, and prepare a per-job reconciliation before the annual return.

## 12. Refusal catalogue (this skill will NOT do the following)

- **Refusal catalogue** — 1. Prepare Philadelphia wage tax, NPT, or BIRT returns — route to the Philadelphia city tax skill. 2. Prepare Pittsburgh Payroll Expense Tax — route to the Pittsburgh city tax skill. 3. Prepare Local Services Tax (LST) returns or per-capita / occupation taxes — route to dedicated LST skill. 4. Prepare PA Mercantile / Business Privilege Tax returns (where imposed by home rule cities) — route to dedicated municipal gross-receipts skill. 5. Compute multi-state apportionment for a part-year PA resident — route to a part-year residency skill. 6. Cover a taxpayer who was not a full-year PA resident — out of scope for v0.1. 7. Cover S-corporation reasonable compensation analysis for LEIT — defer to the S-corp election skill plus reasonable comp workflow.

## 13. Provenance

### 13.1 Primary statutes

Local Tax Enabling Act, Act 511 of 1965, 53 P.S. §6924.101 et seq. (as renumbered by Act 32 of 2008); Act 32 of 2008, P.L. 197, No. 32 — overhauled local EIT collection; effective for tax years beginning Jan 1, 2012; Sterling Act, Act of August 5, 1932, P.L. 45, 53 P.S. §15971 et seq.; Municipalities Financial Recovery Act, Act 47 of 1987, 53 P.S. §11701.101 et seq. — distressed municipality rate authority; Local Services Tax Act, Act 7 of 2007, 53 P.S. §6924.301 (renumbered the former Occupation Privilege Tax); Taxpayer Relief Act, Act 1 of 2006 — voter-approved EIT/property tax shift authority.

### 13.2 Primary authority on rates and PSD codes

Pennsylvania Department of Community and Economic Development (DCED), Municipal Statistics portal — munstats.pa.gov — official PSD code register, current EIT rate lookup, tax officer assignment; DCED Tax Register — annual publication of every municipal and school district EIT rate.

### 13.3 Philadelphia primary authority

City of Philadelphia, Department of Revenue, Wage Tax Regulations — phila.gov/revenue; Annual wage tax rate bulletin (effective each July 1); Philadelphia Code §19-1502 (Wage Tax), §19-1502.1 (Earnings Tax), §19-1503 (Net Profits Tax).

### 13.4 Major case law

Murray v. Philadelphia, 364 Pa. 157 (1950) — Sterling Act primacy; Philadelphia v. Cohen, 429 Pa. 109 (1968) — Sterling Act primacy reaffirmed; Pittsburgh v. Alco Parking Corp., 417 U.S. 369 (1974) — constitutional limits on municipal taxation; Williams v. City of Pittsburgh, 543 Pa. 121 (1995) — Act 511 cap interpretation.

### 13.5 Tax officer authority and forms

Berkheimer Tax Innovations / HAB — hab-inc.com — TCD tax officer for many southeastern and northeastern PA TCDs; publishes Form CLGS-32-1 (Annual Final Return), Form CLGS-32-1A (Employer Quarterly Return), Form CLGS-32-6 (Residency Certification). Keystone Collections Group — keystonecollects.com — TCD tax officer for many south-central and southwestern PA TCDs. Jordan Tax Service — jordantax.com — TCD tax officer for Allegheny County districts. Capital Tax Collection Bureau — captax.com — TCD tax officer for Cumberland / Dauphin / Perry.

### 13.6 Verification status

This skill has been drafted from primary statutory sources, DCED published materials, and tax officer published forms current as of the last_updated date. All rates require live verification before each return preparation — rates change mid-year (Philadelphia every July 1; non-Philadelphia municipalities effective January 1 of each year following a school district or municipal council enactment) and the figures in Section 2.3 are illustrative only. Verification status: pending — awaiting credentialed PA practitioner sign-off (CPA or PA-licensed attorney with municipal tax practice).

### 13.7 Cross-references to other skills

pa-income-tax.md — PA state PIT (3.07%) — parallel obligation; no integration with LEIT. pa-sales-tax.md — separate skill. us-sole-prop-bookkeeping.md — PA Schedule C derives from federal Schedule C with PA adjustments. us-schedule-c-and-se-computation.md — federal Schedule C / SE computation feeds LEIT net profits. us-quarterly-estimated-tax.md — federal estimates; not aligned with LEIT estimate deadlines. us-federal-return-assembly.md — federal package assembly; LEIT is a separate package.

### 13.8 Open items for v0.2

Add the current-year DCED rate table for all 67 counties at a point-in-time snapshot; Add the Pittsburgh Payroll Expense Tax cross-reference once that skill exists; Add Philadelphia BIRT/NPT cross-reference once that skill exists; Add Local Services Tax (LST) cross-reference once that skill exists; Expand the part-year residency case (move-in / move-out during tax year); Add treatment of stock-based compensation (RSU, NSO, ISO) under LEIT — PA conforms to federal treatment generally, but timing differences arise.

## End of pa-local-eit v0.1

End of pa-local-eit v0.1 — Pennsylvania Local Earned Income Tax (Act 32 of 2008). Tax year 2025.

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
