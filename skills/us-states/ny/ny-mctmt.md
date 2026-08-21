---
name: ny-mctmt
description: "The NY Metropolitan Commuter Transportation Mobility Tax (MCTMT, Tax Law Article 23) is a payroll-and-self-employment tax on employers and self-employed individuals doing business in the Metropolitan Commuter Transportation District (MCTD): the five NYC boroughs (Zone 1) and the suburban counties of Dutchess, Nassau, Orange, Putnam, Rockland, Suffolk, and Westchester (Zone 2). Quarterly payroll brackets run from 0.11% up to 0.60% in Zone 1 and 0.34% in Zone 2. Self-employed individuals owe MCTMT only when MCTD-allocated net earnings exceed $50,000 annually, paid via Form MTA-6 quarterly estimates and reconciled on the NY personal return. Employers file quarterly through NYS-45 (which absorbed Form MTA-305). Exemptions cover federal government, certain NY state employees, agricultural employers, public school districts, and household employers."
jurisdiction: US-NY
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# NY Mctmt

### 1.1 Statutory basis

- **MCTMT statutory basis** — The Metropolitan Commuter Transportation Mobility Tax (MCTMT) is imposed under New York Tax Law Article 23 (sections 800–810), enacted by Chapter 25 of the Laws of 2009 (effective March 1, 2009, for employers; January 1, 2009, for self-employed individuals). The tax is administered by NYSDTF and proceeds are dedicated to the MTA.  _(New York Tax Law Article 23 (sections 800–810); Chapter 25 of the Laws of 2009)_
- **2023 rate increase** — Part Q of Chapter 59 of the Laws of 2023 raised the top employer rate for Zone 1 from 0.34% to 0.60% effective for payroll paid on or after July 1, 2023, while leaving Zone 2 unchanged. Self-employed top-bracket rates were similarly increased for tax years beginning on or after January 1, 2023.  _(Part Q of Chapter 59 of the Laws of 2023)_
- **2024 rate confirmation** — Part R of Chapter 56 of the Laws of 2024 (the FY 2025 budget bill) confirmed and extended the bifurcated Zone 1 / Zone 2 rate schedule and finalized the post-increase brackets effective for payroll paid on or after January 1, 2024. The 0.60% top employer rate for Zone 1 and the unchanged 0.34% top employer rate for Zone 2 are the current law.  _(Part R of Chapter 56 of the Laws of 2024)_

### 1.2 Persons subject to the tax

- **Employer definition** — Any "employer" within the meaning of Tax Law §671 (i.e., a person required to deduct and withhold New York personal income tax from wages paid to employees) whose payroll expense for employees performing services within the MCTD exceeds the de minimis quarterly threshold described in Section 3. Payroll expense includes wages and compensation as defined in IRC §3121 (without regard to the FICA wage base cap), reported in Box 5 of federal Form W-2, for services performed within the MCTD during the calendar quarter.  _(Tax Law §671; IRC §3121)_
- **Self-employed individual definition** — Any individual (including a sole proprietor, single-member LLC disregarded for federal tax, or general partner in a partnership) whose net earnings from self-employment allocated to the MCTD for the taxable year exceed $50,000. The $50,000 threshold is computed annually, not quarterly; estimated payments are required only when the taxpayer reasonably expects to exceed that threshold for the year.

### 1.3 The Metropolitan Commuter Transportation District (MCTD)

- **MCTD composition** — The MCTD consists of twelve counties as defined in Public Authorities Law §1262. Zone 1 (New York City five boroughs): 1. New York County (Manhattan) 2. Kings County (Brooklyn) 3. Bronx County (The Bronx) 4. Queens County (Queens) 5. Richmond County (Staten Island). Zone 2 (Suburban counties): 6. Dutchess County 7. Nassau County 8. Orange County 9. Putnam County 10. Rockland County 11. Suffolk County 12. Westchester County. Counties outside this list — including Albany, Erie, Monroe, Onondaga, Saratoga, and all other New York counties — are not part of the MCTD. Cross-border activity in New Jersey, Connecticut, or Pennsylvania is also outside the MCTD regardless of proximity to the district.  _(Public Authorities Law §1262)_

### 1.4 What MCTMT is NOT

- **MCTMT is a separate tax** — MCTMT is a separate tax, distinct from: New York State personal income tax under Article 22; New York State corporate franchise tax under Article 9-A; New York City personal income tax (Administrative Code Title 11); New York City Unincorporated Business Tax (NYC UBT); New York City General Corporation Tax / Business Corporation Tax; New York State Pass-Through Entity Tax (PTET) under Article 24-A; New York State and local sales and use tax under Article 28/29; Federal Social Security or Medicare tax under FICA / SECA.
- **MCTMT deductibility interaction** — MCTMT is not deductible against the New York PTET base (see Section 8.2). It is, however, deductible as an ordinary and necessary business expense for federal income tax purposes when paid by an employer (against the federal payroll tax that flows to Schedule C / Form 1120 / Form 1065) and similarly when paid by a self-employed individual (against Schedule C net profit in the year paid, in the same manner as the deductible half of SE tax — but see Section 8.4 for the federal income tax treatment of MCTMT for self-employed taxpayers, which differs from FICA/SECA).

### 2.1 Why two zones exist

Prior to July 1, 2023, MCTMT used a single rate schedule across the entire MCTD, with a top employer rate of 0.34%. The 2023 legislation bifurcated the district into Zone 1 (the five NYC boroughs) and Zone 2 (the seven suburban counties) and raised the top Zone 1 employer bracket to 0.60%, while leaving Zone 2 at 0.34%. The legislative rationale was that NYC-located employees disproportionately use MTA services and that the Zone 1 increase would generate the bulk of additional MTA funding without raising rates in lower-revenue suburban counties.

### 2.2 Zone determination — employer perspective

- **Employer zone determination** — For an employer, the zone for each employee is determined by where the employee performs services, not by where the employer is headquartered. An employer with offices in both Manhattan and White Plains must: Apply Zone 1 rates to the payroll of employees performing services in Manhattan; Apply Zone 2 rates to the payroll of employees performing services in White Plains (Westchester); Apply MCTMT to the MCTD-allocated portion of payroll for any employee who splits time between MCTD and non-MCTD locations (see Section 7). The two zones are computed on separate thresholds: the $312,500 quarterly de minimis floor applies separately to Zone 1 payroll and to Zone 2 payroll. An employer with $300,000 of Zone 1 payroll and $300,000 of Zone 2 payroll in a quarter owes no MCTMT because neither zone exceeds the floor, even though combined MCTD payroll is $600,000.

### 2.3 Zone determination — self-employed perspective

- **Self-employed zone determination** — For a self-employed individual, the zone is determined by where the individual performs the services that produce the net earnings. A freelance developer based at a coworking space in Brooklyn (Zone 1) who occasionally works from a client site in Garden City (Nassau, Zone 2) allocates net earnings to each zone based on working days (see Section 7). If a self-employed individual works entirely within one zone, that zone's rate schedule applies to 100% of MCTD-allocated net earnings. If the individual splits between zones, each zone's brackets are applied to the portion of net earnings allocated to that zone. The $50,000 threshold is aggregate across both zones — a freelancer with $30,000 allocated to Zone 1 and $25,000 allocated to Zone 2 has $55,000 of MCTD-allocated net earnings and is over the threshold; MCTMT then applies to each zone's portion under its respective rate schedule (see Section 4.5).

### 2.4 Zone changes mid-year

- **Mid-year zone relocation** — When a business relocates from one zone to the other during the year — for example, an employer moves its office from Westchester to Manhattan effective May 1 — the zone determination changes prospectively. Payroll for services performed before the relocation is allocated to the prior zone; payroll for services performed after the relocation is allocated to the new zone. The de minimis thresholds are applied per quarter, per zone, so a mid-quarter relocation can result in a quarter with both Zone 1 and Zone 2 payroll, each tested separately against its own $312,500 floor.

### 3.1 Zone 1 (NYC five boroughs) — quarterly brackets

**Zone 1 quarterly employer brackets**

| Quarterly MCTD payroll (Zone 1) | Rate |
| --- | --- |
| $0 — $312,500 | 0.00% |
| $312,501 — $375,000 | 0.11% |
| $375,001 — $437,500 | 0.23% |
| $437,501 and above | 0.60% |

- **Zone 1 top bracket history** — The 0.60% top bracket is the rate raised by the 2023 legislation (from the prior 0.34%) and confirmed by the 2024 legislation. The lower-bracket rates (0.11% and 0.23%) were not increased.

### 3.2 Zone 2 (suburban counties) — quarterly brackets

**Zone 2 quarterly employer brackets**

| Quarterly MCTD payroll (Zone 2) | Rate |
| --- | --- |
| $0 — $312,500 | 0.00% |
| $312,501 — $375,000 | 0.11% |
| $375,001 — $437,500 | 0.23% |
| $437,501 and above | 0.34% |

- **Zone 2 top rate retention** — Zone 2 retains the pre-2023 top rate of 0.34%. The legislative intent was to leave the suburban tax burden unchanged while raising the NYC top rate.

### 3.3 Bracket mechanics — cliff, not graduated

- **Employer cliff schedule mechanics** — The MCTMT employer rate schedule is a cliff schedule, not a graduated schedule. Once quarterly MCTD payroll in a given zone exceeds a bracket threshold, the entire payroll amount is taxed at the applicable bracket rate. This is materially different from federal income tax marginal rates.

Example: A Zone 1 employer with $400,000 of Q3 2025 MCTD payroll pays MCTMT on the entire $400,000 at 0.23% (= $920), not $375,000 at 0.11% plus $25,000 at 0.23%. If that same employer had $438,000 of Q3 payroll, the entire $438,000 would be taxed at 0.60% (= $2,628), producing a steep cliff at the $437,500 boundary. Because of the cliff structure, employers operating near a bracket threshold face significant marginal tax incentives. A Zone 1 employer with $437,500 of quarterly payroll owes $1,006.25 (at 0.23%), while the same employer at $437,501 owes $2,625.01 (at 0.60%) — a $1,618.76 increase from a $1 payroll change. This is a known feature of the statute and is not a drafting error; it is consistent with the original 2009 design.

### 3.4 Quarterly, not annual, measurement

- **Quarterly measurement rule** — The brackets are tested per calendar quarter, not per year. A seasonal employer with one busy quarter at $500,000 of MCTD payroll and three quarters at $100,000 owes MCTMT only in the busy quarter (at 0.60% in Zone 1 or 0.34% in Zone 2). Annualizing the payroll across quarters is not permitted under the statute.

### 3.5 Successor employer rule

- **Successor employer treatment** — When an employer acquires substantially all the assets of another employer mid-quarter, the predecessor's MCTD payroll for that quarter does not transfer to the successor for purposes of the quarterly threshold test. Each employer separately tests its own quarterly payroll. This treatment differs from FUTA successor employer rules.

### 4.1 The $50,000 annual threshold

- **Self-employed annual MCTD net earnings threshold** — $50,000 USD (All-or-nothing threshold; below $50,000, no MCTMT owed and no return required; once crossed, MCTMT applies from the first dollar of MCTD-allocated net earnings under the applicable bracket schedule.)

Example: A freelance designer with $48,000 of MCTD-allocated net earnings owes $0 of MCTMT and need not file Form MTA-6. A freelance designer with $52,000 of MCTD-allocated net earnings is over the threshold and owes MCTMT on the entire $52,000 at the applicable rate.

- **Net earnings computation for MCTMT** — Net earnings from self-employment for MCTMT purposes are computed using the federal §1402 definition (the same base as SE tax) with the 92.35% net SE earnings adjustment, then allocated to the MCTD under Section 7. Note: this is the SAME base as Schedule SE Line 4a × 0.9235, not the full Schedule C net profit.  _(§1402)_

### 4.2 Zone 1 (NYC five boroughs) — annual brackets

**Zone 1 self-employed annual brackets**  _(NYSDTF Publication 420; TSB-M-23(1)MCTMT)_

| Annual MCTD net earnings (Zone 1) | Rate |
| --- | --- |
| $0 — $50,000 | 0.00% |
| $50,001 — $100,000 | 0.34%* |
| $100,001 — $150,000 | 0.40%* |
| $150,001 — $200,000 | 0.46%* |
| $200,001 — $300,000 | 0.55%* |
| $300,001 and above | 0.60% |

*Self-employed Zone 1 brackets reflect the 2023 increase that graduated the rate up to the new 0.60% top, replacing the prior flat 0.34%. Practitioners should consult NYSDTF Publication 420 and TSB-M-23(1)MCTMT for the most current confirmed schedule; the table above reflects the post-2023 legislative framework as interpreted by NYSDTF in published guidance through 2025. The 0.34% entry-level rate matches the historical employer top rate, and the 0.60% top matches the post-2023 employer top rate.

### 4.3 Zone 2 (suburban counties) — annual brackets

**Zone 2 self-employed annual brackets**

| Annual MCTD net earnings (Zone 2) | Rate |
| --- | --- |
| $0 — $50,000 | 0.00% |
| $50,001 and above | 0.34% |

- **Zone 2 flat rate** — Zone 2 retains a flat 0.34% rate above the $50,000 threshold, consistent with the pre-2023 schedule for the entire MCTD. No graduated upward stepping applies in Zone 2.

### 4.4 Graduated, not cliff, for self-employed

- **Self-employed graduated schedule** — Unlike the employer schedule, the self-employed Zone 1 brackets operate as a graduated schedule: each bracket's rate applies only to the portion of net earnings falling within that bracket. This avoids the cliff problem that exists for employers.

Example: A Zone 1 freelance developer with $250,000 of MCTD-allocated net earnings computes MCTMT as: $0 — $50,000 → $0; $50,001 — $100,000 → $50,000 × 0.34% = $170; $100,001 — $150,000 → $50,000 × 0.40% = $200; $150,001 — $200,000 → $50,000 × 0.46% = $230; $200,001 — $250,000 → $50,000 × 0.55% = $275; Total MCTMT = $875. The same $250,000 of payroll for an employer would be taxed at a flat 0.23% on the entire $250,000 (because the employer brackets are quarterly, $250,000 / 4 = $62,500 per quarter — actually below the employer threshold — but if compressed into a single quarter, the 0.23% rate would apply as a cliff). This asymmetry between employer cliff rates and self-employed graduated rates is deliberate.

### 4.5 Mixed-zone self-employed allocation

- **Mixed-zone allocation rule** — When a self-employed individual splits MCTD-allocated net earnings between Zone 1 and Zone 2, each zone's brackets apply separately to that zone's portion, but the $50,000 threshold is tested on the aggregate MCTD-allocated net earnings.

Example: A freelancer with $40,000 of Zone 1 earnings and $30,000 of Zone 2 earnings has aggregate MCTD-allocated net earnings of $70,000, exceeding the $50,000 threshold. MCTMT is then computed as: Zone 1: $40,000 × 0.34% (entry bracket) = $136; Zone 2: $30,000 × 0.34% = $102; Total MCTMT = $238. The $50,000 threshold is not allocated between zones — it is a single annual threshold tested on the aggregate amount.

### 4.6 Partners and S corporation shareholders

- **Partner and S corp treatment** — A general partner's distributive share of partnership self-employment earnings flows through to the partner's individual MCTMT computation under §1402, allocated to the MCTD based on where the partner performs services (not where the partnership is located). The partnership itself does not pay MCTMT on partner distributive shares. A limited partner whose distributive share is not subject to SE tax under §1402(a)(13) is similarly not subject to MCTMT on that distributive share. S corporation shareholders receive distributive shares as flow-through income that is not SE earnings (they receive W-2 wages instead); the W-2 wages are subject to MCTMT at the employer level (the S corp pays MCTMT on the shareholder's wages just as on any other employee's wages), and there is no separate self-employed MCTMT on the shareholder.  _(§1402(a)(13))_

### 5.1 Employer filing — Form NYS-45 (absorbing Form MTA-305)

- **NYS-45 consolidation history** — From 2009 through 2021, employers filed MCTMT on a standalone quarterly return, Form MTA-305 (Employer's Quarterly Metropolitan Commuter Transportation Mobility Tax Return). Effective for quarters beginning March 1, 2022, NYSDTF consolidated the MCTMT return into the standard quarterly combined withholding, wage reporting, and unemployment insurance return, Form NYS-45 (Quarterly Combined Withholding, Wage Reporting, and Unemployment Insurance Return), with MCTMT reported on the new Part D of NYS-45. Form MTA-305 is no longer used for periods beginning March 1, 2022 or later.
- **NYS-45 Part D reporting lines** — Employers report MCTMT separately for Zone 1 and Zone 2 within NYS-45 Part D, with separate lines for: Zone 1 MCTD payroll subject to MCTMT; Zone 1 MCTMT rate (0.00% / 0.11% / 0.23% / 0.60%); Zone 1 MCTMT due; Zone 2 MCTD payroll subject to MCTMT; Zone 2 MCTMT rate (0.00% / 0.11% / 0.23% / 0.34%); Zone 2 MCTMT due; Total MCTMT due (Zone 1 + Zone 2).

### 5.2 Employer due dates

**NYS-45 employer quarterly due dates**

| Calendar quarter | Period covered | Due date |
| --- | --- | --- |
| Q1 | Jan 1 — Mar 31 | April 30 |
| Q2 | Apr 1 — Jun 30 | July 31 |
| Q3 | Jul 1 — Sep 30 | October 31 |
| Q4 | Oct 1 — Dec 31 | January 31 (next year) |

- **Due date weekend/holiday rule and filing method** — If a due date falls on a Saturday, Sunday, or legal holiday, the return is due the next business day. NYS-45 is filed electronically through the Department's online business services account; paper filing is generally restricted to employers granted a waiver.

### 5.3 Employer payment with return

- **Payment concurrency** — MCTMT is paid concurrently with the NYS-45 filing. There is no separate quarterly estimate; the tax computed on the quarter's payroll is the tax due on the quarter's NYS-45. Employers required to remit New York withholding tax on an accelerated schedule (PrompTax filers under §9 of the Tax Law) follow the same accelerated schedule for MCTMT payments, but the reconciliation occurs on the quarterly NYS-45.  _(Tax Law §9)_

### 5.4 Self-employed filing — Form MTA-6 quarterly estimates

**Form MTA-6 quarterly installment schedule**

| Installment | Period covered | Due date |
| --- | --- | --- |
| Q1 | Jan 1 — Mar 31 | April 15 |
| Q2 | Apr 1 — May 31 | June 15 |
| Q3 | Jun 1 — Aug 31 | September 15 |
| Q4 | Sep 1 — Dec 31 | January 15 (next year) |

- **MTA-6 vouchers and annual reconciliation** — Form MTA-6 functions as both the quarterly estimate and the annual reconciliation: Quarters 1, 2, and 3: Estimated payment vouchers (MTA-6 Voucher A, B, C); Annual reconciliation: Form MTA-6 filed by April 15 of the following year, accompanying the taxpayer's New York personal income tax return (IT-201 or IT-203). A self-employed individual whose MCTD-allocated net earnings remain below $50,000 for the year owes no MCTMT and is not required to file Form MTA-6. If the individual makes estimated payments anticipating exceeding $50,000 but ultimately falls below, the payments are refundable through the annual MTA-6 reconciliation.

### 5.5 Safe harbor — self-employed

- **Prior-year safe harbor** — Quarterly estimates equal to 25% of the prior year's MCTMT liability avoid underpayment penalty regardless of current-year liability. (No 110% surcharge applies — MCTMT uses 100% of prior year regardless of AGI.)  _(§6654)_
- **Current-year safe harbor** — Quarterly estimates equal to 25% of 90% of the current-year MCTMT liability avoid underpayment penalty.  _(§6654)_
- **Annualized income installment method** — Available for taxpayers with lumpy or seasonal SE earnings, computed analogously to Form 2210 Schedule AI. Underpayment penalty is computed on Form IT-2105.9 at the New York statutory underpayment rate (the same rate used for personal income tax underpayments).  _(Form IT-2105.9; Form 2210 Schedule AI)_

### 5.6 Annual reconciliation on IT-201 / IT-203

- **IT-201 reconciliation** — IT-201 (Full-year resident return): Form MTA-6 is filed as a supplementary schedule with IT-201. The MCTMT due flows to IT-201 Line 54a (or the equivalent line in the year's form layout) as an additional tax.
- **IT-203 reconciliation** — IT-203 (Nonresident / part-year resident return): Form MTA-6 is filed with IT-203, with MCTMT due flowing to IT-203 Line 52a (or equivalent). Nonresidents are subject to MCTMT on their MCTD-allocated SE earnings even if they are New York nonresidents for personal income tax purposes — MCTD activity is the trigger, not residency.

### 5.7 Late filing and late payment penalties

- **Late filing penalty** — 5% per month, up to 25%  _(NY Tax Law §685)_
- **Late payment penalty** — 0.5% per month, up to 25%  _(NY Tax Law §685)_
- **Combined cap** — 47.5% (when both apply)  _(NY Tax Law §685)_
- **Interest** — New York statutory underpayment interest rate, compounded daily  _(NY Tax Law §685)_

A self-employed individual who crosses the $50,000 threshold mid-year but did not make estimated payments may avoid the underpayment penalty by satisfying one of the safe harbors in Section 5.5 by withholding or by the annualized income installment method.

### 6.1 Federal government

- **Federal government exemption** — The United States government and its agencies and instrumentalities are exempt under the federal supremacy doctrine and explicitly under §801(3)(b). This includes military pay, civilian federal employee pay, Post Office, federal contractors (only to the extent the contractor is itself a federal instrumentality — private contractors are NOT exempt), and federal grant-funded positions.  _(Tax Law §801(3)(b))_

### 6.2 New York State government — limited

- **NY State government limited exemption** — New York State and its agencies are partially exempt. The State is generally not subject to MCTMT on state employee payroll, but several subdivisions are subject to MCTMT, including: Public benefit corporations (other than the MTA and its subsidiaries, which are obviously exempt as the recipient of the tax); State university system payroll above certain thresholds; Certain authorities and quasi-state entities. This is a frequent area of audit dispute; practitioners should consult NYSDTF Publication 420 and TSB-M-09(1)MCTMT for the most current list of exempt and non-exempt state subdivisions.  _(Tax Law §801; NYSDTF Publication 420; TSB-M-09(1)MCTMT)_

### 6.3 Local government — generally NOT exempt

- **Local government generally not exempt** — New York cities, counties, towns, villages, and special districts within the MCTD are subject to MCTMT as employers, unless specifically exempted (e.g., public school districts under Section 6.4). New York City is not exempt — NYC government payroll for civilian employees is subject to MCTMT at the Zone 1 rates.  _(Tax Law §801)_

### 6.4 Public school districts

- **Public school district exemption** — Public school districts located within the MCTD are statutorily exempt from MCTMT on payroll paid to their employees performing services within the MCTD. This exemption was added to mitigate the funding impact on local school districts that would otherwise have to raise property taxes to cover the MCTMT cost. Charter schools are not automatically exempt — they are exempt only if they qualify as a public school district under New York Education Law. Private and religious schools are not exempt and pay MCTMT on payroll like any other private employer.  _(Tax Law §801)_

### 6.5 Agricultural employers

- **Agricultural employer exemption** — An employer is exempt from MCTMT on payroll for agricultural labor as defined in Tax Law §671. This tracks the federal FUTA agricultural exemption (IRC §3306(k)) and the NY unemployment insurance agricultural carve-out. Greenhouses, dairies, orchards, and similar operations within the MCTD pay no MCTMT on their farm labor payroll. Non-farm labor of the same employer (e.g., an office worker at the farm's corporate headquarters) remains subject to MCTMT.  _(Tax Law §671; IRC §3306(k))_

### 6.6 Household employers

- **Household employer exemption** — An employer of domestic / household workers in a private home is exempt from MCTMT on the household payroll. This includes nannies, housekeepers, gardeners, and home health aides employed directly by the household. Agencies that employ workers and place them in client homes are NOT household employers — the agency pays MCTMT on its agency payroll.

### 6.7 Interstate rail and motor carriers

- **Interstate carrier exemption** — Certain interstate rail carriers and motor carriers operating across state lines have a federal-preemption exemption under 49 U.S.C. §11502 (rail) and §14503 (motor carriers) for SOME employees — typically those subject to the federal Railroad Retirement Act or whose work crosses state lines such that no single state may tax. This is a narrow exemption; consult an interstate transportation tax specialist.  _(49 U.S.C. §11502; 49 U.S.C. §14503)_

### 6.8 Self-employed exemptions

- **Self-employed exemption conditions** — A self-employed individual is exempt from MCTMT if any of: MCTD-allocated net earnings ≤ $50,000 for the year (Section 4.1); Earnings are not "net earnings from self-employment" under §1402 (e.g., passive rental income, dividend income, capital gains — these are not SE earnings and are not subject to MCTMT); Earnings derive from services performed entirely outside the MCTD (allocation = 0%); The individual qualifies as a §1402(a)(13) limited partner whose distributive share is not SE-taxable. There is no exemption for low-income self-employed individuals beyond the $50,000 threshold itself; once over the threshold, the full amount is subject to MCTMT regardless of the taxpayer's other income, marital status, or family circumstances. The threshold is not adjusted for inflation.  _(§1402; §1402(a)(13))_

### 7.1 The working-day allocation method

- **Default allocation method** — For employees or self-employed individuals who perform services both within and outside the MCTD, MCTMT applies only to the portion of payroll or net earnings allocated to the MCTD. The default allocation method is working days within MCTD ÷ total working days, applied to total wages or net SE earnings.
- **Working days definition** — Working days for this purpose are days on which the employee or self-employed individual performs substantial services (more than a de minimis amount — typically more than 4 hours of work or a half-day of activity). Days of leave, vacation, weekends, holidays, and travel days where no work is performed are excluded from both the numerator and denominator.

### 7.2 Employer-allocated wages

- **Employer wage allocation steps** — Step 1 — Working day inventory: Track each employee's working days by location for the calendar quarter. Step 2 — Allocation ratio: Compute MCTD working days ÷ total working days for the quarter. Step 3 — Allocated wages: Multiply the employee's gross wages for the quarter by the allocation ratio. Step 4 — Zone determination: If the MCTD working days fall across both zones (e.g., some Manhattan days and some White Plains days), further split the allocated wages between Zone 1 and Zone 2 using each zone's working days ÷ MCTD working days. Step 5 — Threshold and rate: Add each zone's allocated wages from all employees to the employer's quarterly Zone 1 and Zone 2 totals, and apply the bracket schedules.

### 7.3 Self-employed allocation

- **Self-employed allocation methods** — A self-employed individual computes net earnings from self-employment under §1402 (Schedule SE Line 4a × 0.9235) for the entire year, then allocates to the MCTD using: Working day method (default): MCTD working days ÷ total working days in the year, applied to total net SE earnings. Receipts method (alternative): MCTD-sourced gross receipts ÷ total gross receipts, applied to net SE earnings. This method is available only when working days cannot be reasonably determined (e.g., for project-based work with no clear daily attribution). Specific allocation: For separately identifiable engagements where revenue and direct expenses can be traced to a specific MCTD or non-MCTD project, the individual may directly allocate net profit from each engagement. The taxpayer must use a consistent method across years; switching methods requires reasonable cause.  _(§1402)_

### 7.4 Telecommuting and remote work

- **Convenience of the employer rule application** — The 2020–2024 expansion of remote work created significant MCTMT allocation complexity. NYSDTF's general position (consistent with the "convenience of the employer" rule applied to NY personal income tax for nonresidents) is: If the employee works remotely for the convenience of the employer (i.e., the employer requires the remote work), days worked from a non-MCTD location are excluded from MCTD working days. If the employee works remotely for the convenience of the employee (i.e., the employer has an MCTD office available but the employee chooses to work from home in NJ or upstate NY), those days may be treated as MCTD working days under the convenience rule, increasing the MCTMT allocation.

The convenience rule has been litigated extensively in personal income tax contexts (e.g., Zelinsky v. NY Commissioner) but is less developed in MCTMT case law. Conservative practice for ambiguous cases is to assume the convenience rule applies and allocate the remote days to MCTD, then reconcile if the employer provides written documentation of business-necessity remote work.

### 7.5 Multi-state and out-of-MCTD New York work

- **Multi-jurisdiction allocation example** — An employee with services split among Manhattan, Albany, and Boston: Manhattan days → Zone 1 MCTMT; Albany days → No MCTMT (Albany is outside MCTD); Boston days → No MCTMT (Boston is outside NY entirely). Albany days are NOT subject to MCTMT even though Albany is in New York. MCTD is a sub-state geographic concept and not the same as the New York Tax Law nexus for personal income tax purposes.

### 7.6 Single-day rule

- **Single working day allocation rule** — A working day is allocated to a single location, not split. An employee who works the morning in Manhattan and the afternoon in White Plains is allocated to the location where the majority of working hours were spent, with ties broken in favor of the first location. This avoids fractional working-day arithmetic. For self-employed individuals, the same single-day rule applies, with majority hours determining the day's allocation.

### 8.1 Federal income tax — MCTMT deductibility

- **Employer deductibility** — MCTMT paid by an employer is deductible as an ordinary and necessary business expense under IRC §162, treated as a state and local payroll tax. It is reported on the employer's Schedule C (sole proprietor employer), Form 1065 (partnership), Form 1120 (C corp), or Form 1120-S (S corp). It is NOT subject to the SALT cap because it is a business tax, not an individual SALT item.  _(IRC §162)_
- **Self-employed deductibility** — MCTMT paid on the individual's own SE earnings is deductible as a business expense on Schedule C under §164 and §162, in the same year paid. Unlike the deductible-half-of-SE-tax adjustment on Schedule 1 Line 15, which is an above-the-line adjustment to AGI, MCTMT for the self-employed is treated as a business tax on Schedule C because the underlying activity is the trade or business. This reduces both federal income tax and federal SE tax via the Schedule C bottom line.  _(IRC §164; IRC §162)_

Practitioners should confirm this position against current IRS guidance (Notice 2009-46 addressed the federal characterization of MCTMT at enactment). Conservative practice is to deduct on Schedule C in the year paid, regardless of the year of the underlying SE earnings.

### 8.2 New York PTET — exclusion of MCTMT

- **PTET base exclusion of MCTMT** — The New York Pass-Through Entity Tax (PTET) under Tax Law Article 24-A is computed on the entity's PTE taxable income, defined as the sum of the entity's New York source income of resident and nonresident members. MCTMT is not included in the PTET base — the PTET is a parallel state tax election with its own base, and MCTMT continues to be paid separately by: The employer (S corp or partnership) on its W-2 employee payroll, including any W-2 wages paid to S corp shareholder-employees; The individual partner on his or her distributive share allocated to MCTD (if SE-taxable). The PTET election does NOT shift MCTMT liability to the entity level. The PTET credit on the individual's IT-201/IT-203 does NOT offset MCTMT. These are two separate state taxes with distinct computations.  _(Tax Law Article 24-A)_

### 8.3 NYC Unincorporated Business Tax (NYC UBT)

- **NYC UBT and MCTMT are separate** — NYC UBT under Administrative Code Title 11 Chapter 5 applies to unincorporated businesses operating in NYC at 4% of UBT taxable income above $95,000. NYC UBT and MCTMT are separate, parallel taxes — a Manhattan-based freelance developer with $200,000 of net earnings owes: NYC UBT on the NYC-allocated UBT taxable income (with a UBT credit available on NYC personal income tax); MCTMT on the MCTD-allocated SE earnings under Zone 1 brackets; NY State personal income tax on the full NY-allocated income; NYC personal income tax on the NYC-allocated income; Federal SE tax on the §1402 SE earnings; Federal income tax on the federal AGI. There is no offset or credit between UBT and MCTMT. NYC UBT is paid to the NYC Department of Finance; MCTMT is paid to the NY State Department of Taxation and Finance.  _(Administrative Code Title 11 Chapter 5)_

### 8.4 New York unemployment insurance (UI)

- **UI and MCTMT combined filing but separate computation** — NY UI tax under Labor Law Article 18 is administered together with NYS-45 (UI is reported on NYS-45 Part A; MCTMT is reported on NYS-45 Part D). UI tax base, rate, and computation are separate from MCTMT and the two taxes do not cross-reference. NYS-45 is a single combined return that captures NY withholding, UI tax, wage reporting, and MCTMT, all on quarterly cadence.  _(Labor Law Article 18)_

### 8.5 New York Paid Family Leave (PFL)

- **PFL does not interact with MCTMT** — NY PFL premiums are deducted from employees' wages (employee-funded) and are administered separately by the NY State Workers' Compensation Board, not NYSDTF. PFL does NOT interact with MCTMT — MCTMT is an employer-paid tax based on gross wages (before any PFL or other deductions), so PFL deductions do not reduce the MCTMT base.

### 9.1 Example 1 — Employer in Zone 1

Facts. Lattice Studio LLC is a multi-member LLC (treated as a partnership for federal tax) headquartered in Manhattan with 24 W-2 employees, all of whom perform services from the Manhattan office. The company has no MCTMT-relevant Zone 2 activity. For Q3 2025 (July 1 — September 30), Lattice Studio paid: 18 designers at an average of $24,000/quarter ($1,800 quarterly bonuses included) → $432,000; 4 senior designers at $35,000/quarter → $140,000; 2 project managers at $30,000/quarter → $60,000. Total Q3 2025 MCTD payroll (Zone 1): $632,000. Analysis. Zone 1 quarterly payroll: $632,000. Bracket: $437,501 and above → 0.60% (top Zone 1 rate). Cliff schedule: the entire $632,000 is taxed at 0.60%. MCTMT due, Q3 2025: $632,000 × 0.60% = $3,792.00. Reporting. Lattice Studio files Form NYS-45 for Q3 2025 by October 31, 2025. On NYS-45 Part D: Line for Zone 1 MCTD payroll subject to MCTMT: $632,000; Line for Zone 1 MCTMT rate: 0.60%; Line for Zone 1 MCTMT due: $3,792.00; Line for Zone 2 MCTD payroll: $0; Line for Zone 2 MCTMT due: $0; Total MCTMT due: $3,792.00. Payment of $3,792.00 is remitted with the NYS-45 filing. The MCTMT is deducted as a business expense on Lattice Studio's Form 1065 in 2025, reducing the partners' distributive share of partnership ordinary income. Sensitivity. If Lattice Studio had only $430,000 of Q3 payroll (just below the $437,500 threshold), the bracket would drop to 0.23% and MCTMT would be $430,000 × 0.23% = $989.00 — a $2,803 cliff savings for $2,000 of payroll reduction. Lattice could plausibly time year-end bonuses across the Q3/Q4 boundary to manage the cliff, though anti-abuse rules apply if the timing is artificial.

### 9.2 Example 2 — Freelancer split between Manhattan and NJ

Facts. Yuki Tanaka is a freelance software developer based in Jersey City, NJ, who works on-site for clients in Manhattan two days per week and remotely from her Jersey City home office three days per week. The remote work is at her own discretion (the Manhattan clients have office space available for her). For tax year 2025, Yuki: Total working days: 240 (48 weeks × 5 days, excluding 12 weeks of vacation/holidays/sick); Manhattan working days: 96 (2 days × 48 weeks); Jersey City remote working days: 144 (3 days × 48 weeks); Schedule C net profit: $185,000; Schedule SE Line 4a (§1402 net SE earnings × 0.9235): $185,000 × 0.9235 = $170,847.50. Step 1 — Working day allocation. Manhattan days are Zone 1 MCTD working days. Jersey City days are non-MCTD (NJ is outside MCTD). Under the "convenience of the employee" rule (Yuki could work from Manhattan but chooses Jersey City), the conservative interpretation is to allocate the Jersey City remote days to NY as well. However, MCTMT is geographic to MCTD, not to NY state, so the convenience rule's interaction with MCTMT is uncertain. For this example, we apply the conservative MCTMT position: remote-by-choice days where the employer has MCTD office space available are treated as MCTD working days. Yuki's allocation is therefore 240/240 = 100% to MCTD Zone 1. Alternative position (more aggressive): only on-site Manhattan days count, yielding 96/240 = 40% to MCTD Zone 1. We compute both. Step 2a — Aggressive allocation (96/240 = 40%). MCTD-allocated net SE earnings: $170,847.50 × 40% = $68,339. Over $50,000 threshold? Yes ($68,339 > $50,000). Zone 1 graduated brackets applied: $0 — $50,000: $0; $50,001 — $68,339: $18,339 × 0.34% = $62.35. MCTMT due (aggressive): $62.35. Step 2b — Conservative allocation (240/240 = 100%, convenience rule). MCTD-allocated net SE earnings: $170,847.50 × 100% = $170,847.50. Zone 1 graduated brackets applied: $0 — $50,000: $0; $50,001 — $100,000: $50,000 × 0.34% = $170; $100,001 — $150,000: $50,000 × 0.40% = $200; $150,001 — $170,847.50: $20,847.50 × 0.46% = $95.90. MCTMT due (conservative): $465.90. Recommended position. Yuki should claim the aggressive 40% allocation if she can document that the Manhattan clients did NOT require her on-site presence beyond the 96 days, AND that she has a bona fide Jersey City home office (her own home, not a temporary workspace). Without that documentation, NYSDTF on audit may impose the conservative 100% allocation. The dollar difference is $403.55 — small enough that conservative compliance may be more cost-effective than litigation risk. Filing. Yuki files Form MTA-6 by April 15, 2026, accompanying her IT-203 (she is a NY nonresident — NJ resident — filing for NY-source income). She should have made quarterly estimates of approximately $116 per quarter (aggressive) or $465.90 / 4 = $116 per quarter (also). Coincidentally similar; the safe harbor of 25% of prior-year liability is the simpler test.

### 9.3 Example 3 — Medium employer in Westchester relocates to Zone 1

Facts. Riverstone Analytics Inc. is a NY S corporation with its offices in White Plains (Westchester County, Zone 2). The company has 12 W-2 employees. Effective May 1, 2025, Riverstone relocates its entire office to 250 Broadway, Manhattan (Zone 1). All 12 employees work from the office. For Q2 2025 (April 1 — June 30): April 2025 wages paid (White Plains, Zone 2): $138,000; May 2025 wages paid (Manhattan, Zone 1): $142,000; June 2025 wages paid (Manhattan, Zone 1): $145,000. Step 1 — Quarterly zone-split. Zone 2 payroll (April only): $138,000; Zone 1 payroll (May + June): $287,000. Step 2 — Threshold test per zone. Zone 2: $138,000 < $312,500 → NO MCTMT for Zone 2 in Q2; Zone 1: $287,000 < $312,500 → NO MCTMT for Zone 1 in Q2. Result, Q2 2025: Riverstone owes $0 of MCTMT for Q2 2025 because neither zone's quarterly payroll reaches the $312,500 floor. Step 3 — Q3 2025 projection. Now in Q3 2025, all wages are Zone 1: July: $145,000; August: $148,000; September: $150,000; Total Zone 1 Q3 2025: $443,000. Step 4 — Q3 bracket determination. Zone 1 payroll: $443,000; Bracket: $437,501 and above → 0.60% (cliff); Cliff at $437,500: Riverstone is $5,500 above the cliff; MCTMT Q3 2025: $443,000 × 0.60% = $2,658.00. Sensitivity. Had Riverstone held Q3 Zone 1 payroll to $437,500 or below, MCTMT would have been $437,500 × 0.23% = $1,006.25 — a $1,651.75 cliff savings. The $5,500 of incremental payroll cost Riverstone $1,651.75 of MCTMT, an effective marginal rate on those final dollars of approximately 30%. Compensation planning could include: Timing of Q3 bonuses to Q4 (if Q4 is below the cliff); Allocating a portion of senior employee comp to the S corp shareholder as distributions (NOT W-2 wages) — but this raises reasonable-compensation issues under §1366 and NYSDTF audit risk; Splitting bonus pools between Q3 and Q4 to stay below the cliff in both. For Q4 2025, with similar payroll, Riverstone would face the same 0.60% cliff if Q4 Zone 1 payroll exceeds $437,500. Annual MCTMT for 2025 in this scenario is approximately: Q1 (Zone 2, $138,000-ish): $0; Q2 (mixed, both below floor): $0; Q3 (Zone 1, $443,000): $2,658; Q4 (Zone 1, ~$447,000 est): ~$2,682; 2025 total MCTMT: ~$5,340. Filing. Riverstone files NYS-45 quarterly through 2025. The Q2 NYS-45 shows the zone-split (April Zone 2 / May-June Zone 1) with $0 MCTMT. The Q3 and Q4 NYS-45 show full Zone 1 reporting at the 0.60% rate. Riverstone has no reason to file a separate Zone 2 line on Q3 / Q4 NYS-45 because no Zone 2 payroll occurred.

## 10. Self-checks

Before submitting an MCTMT computation for reviewer signoff, run the following checks: 1. Zone identification: Confirm each location is correctly classified as Zone 1 (5 boroughs), Zone 2 (7 suburban counties), or outside MCTD. Common errors: Albany (outside MCTD), Jersey City (NJ, outside MCTD entirely), Yonkers (Westchester, Zone 2 — NOT NYC despite proximity). 2. Quarterly thresholds: Confirm the de minimis $312,500 floor is tested per quarter, per zone, not annualized or aggregated across zones. 3. Cliff vs graduated: Confirm employer MCTMT is computed as a cliff (entire payroll at one rate), and self-employed Zone 1 MCTMT is computed as graduated (bracket-by-bracket marginal rates). 4. $50,000 SE threshold: Confirm tested on aggregate MCTD-allocated net SE earnings (not per zone), and that no MCTMT is owed below the threshold. 5. Allocation method: Confirm working-day allocation is reasonable and documented; the convenience-of-the-employee rule may apply to remote-work days. 6. Exemption confirmation: Confirm no statutory exemption applies (federal government, agricultural, public school district, household employer). 7. Federal deduction: Confirm MCTMT is deducted on Schedule C / Form 1065 / Form 1120 in the year paid as an ordinary business expense. 8. PTET independence: Confirm MCTMT is NOT included in the PTET base and there is no PTET credit against MCTMT. 9. Filing route: Confirm employers file via NYS-45 Part D (not the discontinued MTA-305) and self-employed individuals file Form MTA-6 with their IT-201/IT-203. 10. Safe harbor compliance: Confirm self-employed estimates meet either prior-year (100%) or current-year (90%) safe harbor to avoid Form IT-2105.9 underpayment penalty.

## 11. Refusals

This skill does NOT cover the following items, which require either a specialized practitioner or a separate skill module:

- **MCTMT for interstate rail and motor carrier exemptions** — Narrow federal preemption analysis under 49 U.S.C. §11502 / §14503; defer to interstate transportation tax specialist.  _(49 U.S.C. §11502 / §14503)_
- **MCTMT audit defense and Tax Appeals Tribunal litigation** — Administrative practice not covered.
- **Pre-2022 MCTMT periods filed on the legacy Form MTA-305** — Historical periods only; current law applies to all periods from March 1, 2022 forward.  _(Form MTA-305)_
- **MCTMT in combined group / unitary contexts** — Combined return positions for affiliated corporations under Article 9-A do not extend to MCTMT, which is always computed on a separate-entity basis.  _(Article 9-A)_
- **NYC payroll tax interactions beyond MCTMT** — NYC has its own employer head-tax proposals from time to time; this skill addresses only the state-level MCTMT.
- **Tip income and statutory employees** — The §1402(c) analysis for statutory employees and the §3121(q) tip income wage allocations are not addressed here; assume standard W-2 Box 5 wage reporting unless flagged for further analysis.  _(IRC §1402(c); IRC §3121(q))_
- **MCTMT for clergy and members of religious orders** — Special §1402(e) exclusions for clergy SE earnings; defer to clergy tax specialist.  _(IRC §1402(e))_
- **MCTMT for nonresident aliens under tax treaty** — Treaty exemptions for income tax may or may not extend to MCTMT depending on the treaty's saving clause; defer to international tax specialist.

## 12. Provenance

### Statutory basis

- **NY Tax Law Article 23 (sections 800–810)** — Original enactment by Chapter 25 of the Laws of 2009; current text as amended through 2024 legislative session.  _(NY Tax Law Article 23 (sections 800–810))_
- **NY Public Authorities Law §1262** — Defines the Metropolitan Commuter Transportation District (12 counties).  _(NY Public Authorities Law §1262)_
- **NY Tax Law §671** — Defines "employer" for payroll tax purposes; cross-referenced for MCTMT employer scope.  _(NY Tax Law §671)_
- **NY Tax Law §685** — Penalty regime for late filing / late payment, applied to MCTMT.  _(NY Tax Law §685)_
- **NY Labor Law Article 18** — Unemployment insurance; NYS-45 cross-reference.  _(NY Labor Law Article 18)_

### Legislative amendments

- **Chapter 25 of the Laws of 2009** — Enactment.  _(Chapter 25 of the Laws of 2009)_
- **Part Q of Chapter 59 of the Laws of 2023** — Zone 1 top employer rate increased to 0.60%; self-employed Zone 1 graduated brackets introduced; effective July 1, 2023.  _(Part Q of Chapter 59 of the Laws of 2023)_
- **Part R of Chapter 56 of the Laws of 2024 (FY 2025 Budget Bill)** — Confirmation of Zone 1 / Zone 2 bifurcated schedule; effective January 1, 2024.  _(Part R of Chapter 56 of the Laws of 2024 (FY 2025 Budget Bill))_

### Administrative guidance

- **NYSDTF Publication 420** — Guide to the Metropolitan Commuter Transportation Mobility Tax (current edition).  _(NYSDTF Publication 420)_
- **TSB-M-09(1)MCTMT** — Initial MCTMT guidance memorandum (2009).  _(TSB-M-09(1)MCTMT)_
- **TSB-M-23(1)MCTMT** — Updated guidance memorandum on the 2023 rate increase and Zone 1 / Zone 2 bifurcation.  _(TSB-M-23(1)MCTMT)_
- **Form NYS-45 instructions** — Quarterly Combined Withholding, Wage Reporting, and Unemployment Insurance Return — Part D covers MCTMT effective March 1, 2022.  _(Form NYS-45 instructions)_
- **Form MTA-6 instructions** — Metropolitan Commuter Transportation Mobility Tax Return for Individuals.  _(Form MTA-6 instructions)_
- **Form MTA-305 instructions** — Discontinued for periods beginning March 1, 2022 — historical only.  _(Form MTA-305 instructions)_
- **NYSDTF online MCTMT resource center** — tax.ny.gov/bus/mctmt/  _([tax.ny.gov/bus/mctmt/](tax.ny.gov/bus/mctmt/))_

### Federal cross-references

- **IRC §1402** — Definition of net earnings from self-employment; used as the MCTMT base for self-employed individuals via the 92.35% adjustment.  _(IRC §1402)_
- **IRC §3121** — Definition of wages and FICA wages; used as the MCTMT employer payroll base, but without the FICA wage base cap.  _(IRC §3121)_
- **IRC §3306(k)** — FUTA agricultural labor definition; cross-referenced for the MCTMT agricultural exemption.  _(IRC §3306(k))_
- **IRC §162 / §164** — Deductibility of state and local taxes as ordinary and necessary business expenses; basis for federal deduction of MCTMT.  _(IRC §162 / §164)_
- **IRS Notice 2009-46** — IRS characterization of MCTMT as a federally deductible state tax at enactment.  _(IRS Notice 2009-46)_

### Verification status

This skill is at **version 0.1, verified_by: pending**. A NY-credentialed practitioner (CPA, EA, or NY attorney) with active payroll-tax practice should review and confirm:

- Current Zone 1 self-employed bracket schedule (Section 4.2) against the most recent NYSDTF Publication 420
- Confirmation that Form MTA-305 has been fully retired for all post-March 1, 2022 periods
- Confirmation of the federal deductibility position for self-employed MCTMT on Schedule C (Section 8.1) against current IRS guidance
- Any further legislative amendments in the 2025 NY budget cycle that may have adjusted brackets or thresholds

Last updated: 2025-11-15. Next scheduled review: prior to 2026 tax-filing season, after release of 2026 NY budget legislation and updated NYSDTF Publication 420.

## 13. Cross-references to other skills

- **us-tax-workflow-base** — Workflow scaffolding; MCTMT is a Tier 2 content skill loaded after the base.
- **us-sole-prop-bookkeeping** — Schedule C bookkeeping; provides the net profit input that feeds MCTMT for self-employed taxpayers.
- **us-schedule-c-and-se-computation** — Schedule SE Line 4a × 0.9235 computation; provides the §1402 net SE earnings base used for MCTMT.
- **ny-income-tax** — NY Article 22 personal income tax for full-year residents (IT-201) and nonresidents (IT-203); the MCTMT annual reconciliation rides with these returns.
- **ny-estimated-tax** — NY personal estimated tax (IT-2105); parallel quarterly cadence but separate from MCTMT estimates via MTA-6.
- **ny-llc-filing-fee** — NY LLC filing fee under Tax Law §658(c)(3); a separate parallel tax for multi-member LLCs and single-member LLCs that have elected partnership treatment.
- **nyc-ubt** — NYC Unincorporated Business Tax; parallel sub-state tax on freelance income inside NYC; coordinates with MCTMT only in that both apply to the same Manhattan-based freelancer.
- **us-ny-return-assembly** — Final assembly of the NY filing package; MCTMT output feeds this skill.
- **us-quarterly-estimated-tax** — Federal Form 1040-ES; parallel quarterly cadence; do NOT include MCTMT in the federal estimate base.
- **us-self-employed-retirement** — SEP-IRA / Solo 401(k) contributions reduce Schedule C net profit but do NOT reduce the §1402 net SE earnings base used for MCTMT (retirement contributions reduce AGI but not SE tax or MCTMT base).

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
