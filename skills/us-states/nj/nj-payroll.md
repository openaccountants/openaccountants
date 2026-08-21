---
name: nj-payroll
description: Tier 2 New Jersey content skill for employer payroll compliance covering tax year 2025. Includes the 10.75% Gross Income Tax top rate, supplemental wage rate 11.8%, NJ-927 single quarterly combined return for withholding/UI/TDI/FLI/WD, TDI rates split between employee (0.23%) and employer (0.93%), FLI 0.06% employee-only (post-2024 reduction), SUI wage base $43,300, ABC test contractor classification under NJ Wage and Hour Law, Earned Sick Leave Law 40-hour minimum, and the BAIT estimated payment schedule for PTE-electing pass-throughs.
jurisdiction: US-NJ
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# NJ Payroll

## New Jersey Payroll Compliance — Tax Year 2025

## 1. Scope

This skill covers New Jersey state-level payroll compliance for employers operating in NJ during the 2025 tax year. It is designed for use alongside `us-federal-payroll` (federal withholding, FICA, FUTA, Form 941, W-2/W-3) and any additional state skills for employees working across state lines (most commonly `us-ny-payroll` and `us-pa-payroll` given commuting patterns).

**In scope:**
- New Jersey Gross Income Tax (GIT) withholding under N.J.S.A. 54A:7-1 et seq.
- Form NJ-W4 (Employee's Withholding Allowance Certificate)
- Form NJ-927 / NJ-927-W (Quarterly Combined Withholding, UI, DI, FLI, WF Return)
- Temporary Disability Insurance (TDI / SDI) — employee + employer split
- Family Leave Insurance (FLI) — employee-only
- State Unemployment Insurance (SUI/UI) — employer-only (mostly)
- Workforce Development Partnership (WD/WF) — employee + employer
- Supplemental Workforce Fund (SWF) — employee + employer
- New hire reporting to NJ Department of Labor (NJDOL) and the federal NDNH
- Worker classification under the New Jersey ABC test (N.J.S.A. 43:21-19(i)(6))
- Earned Sick Leave Law (N.J.S.A. 34:11D)
- Wage Payment Law / pay frequency (N.J.S.A. 34:11-4.2)
- NJ–NY reverse credit and source-of-income interaction for cross-border commuters (high-level — full NY mechanics live in `us-ny-payroll`)
- BAIT (Pass-Through Business Alternative Income Tax) quarterly estimate schedule (deeper coverage in `nj-cbt-and-bait`)

**Out of scope:**
- Federal income tax withholding, FICA, FUTA, Form 941 — see `us-federal-payroll`.
- NJ Corporation Business Tax (CBT) and full BAIT mechanics — see `nj-cbt-and-bait`.
- Multi-state apportionment for income tax purposes — see `_cross-border/multistate-payroll`.
- Public sector / civil service payroll, agricultural labor, domestic service, and clergy compensation (NJ has special carve-outs not covered here).
- Workers' Compensation insurance (privately insured, not run through NJ-927).
- New Jersey Secure Choice mandatory retirement program implementation details (only flagged briefly).

> **AUDIT FLASH POINT — ABC test misclassification.** New Jersey is among the most aggressive jurisdictions in the United States for reclassifying 1099 contractors as W-2 employees. NJDOL audits routinely target staffing, construction, trucking, last-mile delivery, IT consulting, real estate brokerages, salons and barbershops, and gig platforms. The prong B "outside the usual course of business" test is the most commonly failed prong, and failing any one of A, B, or C triggers reclassification with retroactive liability for withholding, UI/TDI/FLI contributions, interest, and penalties — plus exposure under the NJ Insurance Fraud Prevention Act for any 1099 the employer issued knowingly to a misclassified worker. Construction has its own statute (Construction Industry Independent Contractor Act, N.J.S.A. 34:20-1) that layers on top of the ABC test and presumes employee status. Treat any 1099 issued in NJ as a presumptive misclassification risk and document the ABC analysis contemporaneously.

## 2. NJ Gross Income Tax (GIT) — Withholding Brackets 2025

### 2.1 Statutory framework

- **NJ GIT statutory basis** — NJ GIT is imposed under N.J.S.A. 54A:2-1. Employer withholding obligations sit at N.J.S.A. 54A:7-1 ("Requirement of withholding tax from wages"). The Division of Taxation publishes the rate tables in the NJ-WT booklet, which is reissued annually. For 2025 the rates below are drawn from the NJ-WT booklet effective January 1 2025 (Publication NJ-WT, January 2025 revision). NJ uses **separate** withholding tables by filing status (single, married/civil union joint, married/civil union separate, head of household, qualifying surviving spouse) and by payroll frequency (weekly, biweekly, semimonthly, monthly, daily/miscellaneous). Unlike federal withholding post-TCJA, NJ still operates on **allowances** rather than a dollar-based withholding mechanism, so the NJ-W4 is meaningfully different from the federal W-4 (see Section 6).  _(N.J.S.A. 54A:2-1; N.J.S.A. 54A:7-1; Publication NJ-WT, January 2025 revision)_

### 2.2 2025 GIT brackets — Single / married filing separately

**2025 GIT brackets — Single / married filing separately**

| Taxable income (annualized) | Marginal rate |
| --- | --- |
| $0 – $20,000 | 1.4% |
| $20,000 – $35,000 | 1.75% |
| $35,000 – $40,000 | 3.5% |
| $40,000 – $75,000 | 5.525% |
| $75,000 – $500,000 | 6.37% |
| $500,000 – $1,000,000 | 8.97% |
| Over $1,000,000 | **10.75%** (the millionaire surtax bracket) |

### 2.3 2025 GIT brackets — Married/CU filing jointly, head of household, qualifying surviving spouse

**2025 GIT brackets — Married/CU filing jointly, head of household, qualifying surviving spouse**

| Taxable income (annualized) | Marginal rate |
| --- | --- |
| $0 – $20,000 | 1.4% |
| $20,000 – $50,000 | 1.75% |
| $50,000 – $70,000 | 2.45% |
| $70,000 – $80,000 | 3.5% |
| $80,000 – $150,000 | 5.525% |
| $150,000 – $500,000 | 6.37% |
| $500,000 – $1,000,000 | 8.97% |
| Over $1,000,000 | **10.75%** |

### 2.3 2025 GIT brackets — Married/CU filing jointly, head of household, qualifying surviving spouse

> Verify: rates above mirror the 2024 brackets; the brackets are not indexed for inflation under current NJ law (P.L. 1976, c. 47, as amended through P.L. 2020, c. 95 which created the over-$1M bracket at 10.75%). The 10.75% top rate has been at $1M for joint filers since the 2020 expansion of the millionaire surtax (previously this rate kicked in at $5M from P.L. 2018, c. 45).

### 2.4 Supplemental wage rate

- **NJ supplemental wage withholding rate (YTD wages > $1,000,000)** — 11.8% percent (Supplemental payments to employees whose YTD wages exceed $1,000,000)  _(NJ-WT booklet)_

### 2.4 Supplemental wage rate

- **Supplemental wage rate mechanics** — Supplemental wages (bonuses, commissions, retroactive pay increases, severance, awards, accumulated sick/vacation payouts, taxable fringes paid in a lump) are withheld at the flat NJ supplemental rate when the employer chooses not to aggregate with the most recent regular pay. The 11.8% rate is set to capture the 10.75% rate plus the average uplift from non-uniform allowance treatment, and is the published rate in the NJ-WT booklet for high-earner supplemental wages. For supplemental payments below the $1,000,000 YTD threshold, the otherwise-applicable top bracket rate (typically the marginal rate from the regular tables) applies. For supplemental wages paid to employees whose YTD wages have not yet exceeded $1M, the employer may use either (a) aggregation with the most recent regular pay period (more accurate) or (b) the rate implied by the employee's marginal bracket on the regular tables.  _(NJ-WT booklet)_

### 2.4 Supplemental wage rate

> Verify against the NJ-WT 2025 booklet, "Supplemental Wage Payments" instructions, which historically print at the back of the booklet under "Method II" alternative.

### 2.5 Mechanics

- **Withholding computation steps** — Withholding is computed each pay period by: 1. Annualizing the gross taxable NJ wages for the pay period (multiply by 52 for weekly, 26 for biweekly, 24 for semimonthly, 12 for monthly). 2. Subtracting the value of the allowances claimed on the NJ-W4 (each allowance is worth $1,000 of withholding-exempt income — this has not changed since 1996 and is not indexed). 3. Applying the appropriate bracket table to compute annualized tax. 4. Dividing back by the number of pay periods in the year. Note that NJ does NOT use a standard deduction in the withholding mechanic — the bracket tables effectively bake in the $0 starting point. The personal exemption ($1,000 per exemption) shows up only as the per-allowance adjustment in step 2.

### 2.6 Common NJ-specific quirks

- **401(k), HSA, cafeteria plan, civil union conformity quirks** — **Pension and 401(k) interaction:** NJ does NOT conform to federal §401(k) elective-deferral exclusion. 401(k) contributions are NOT excluded from NJ taxable wages, so Box 16 (state wages) on the W-2 will typically exceed Box 1 (federal wages) by the amount of 401(k) deferrals. NJ DOES allow §125 cafeteria-plan exclusions (premiums for health, dental, vision, and HSA contributions through a §125 plan) and §403(b) employee deferrals are also excluded. §457(b) deferrals are excluded. - **Section 125 dependent care:** NJ does conform on dependent care FSA exclusions up to the same federal limit. - **HSA employer contributions:** NJ does NOT exclude HSA contributions from state taxable wages even when excluded federally. Box 16 includes HSA contributions; this is a common W-2 reconciliation issue. - **Domestic Partnership Act and Civil Union Act:** NJ withholding tables for "married/civil union" apply to civil union partners; NJ does not separately track domestic partnerships for withholding tables but the credit/exemption structure on the NJ-1040 differs.

## 3. Form NJ-927 — Quarterly Combined Return

### 3.1 What NJ-927 covers

- **NJ-927 combined return contents** — NJ-927 is one of the few truly combined state payroll returns in the United States. A single quarterly filing reports and remits: 1. NJ Gross Income Tax withheld (employee). 2. UI (Unemployment Insurance) contributions — employer share + employee share. 3. DI (Disability Insurance / TDI) — employer share + employee share. 4. FLI (Family Leave Insurance) — employee share only. 5. WF (Workforce Development Partnership) — employer share + employee share. 6. SWF (Supplemental Workforce Fund) — employer share + employee share. This contrasts with the federal model where Form 941 (federal income tax + FICA) is separate from Form 940 (FUTA). NJ merges the analogue of both — plus state-specific TDI and FLI — into NJ-927.

### 3.2 Filing variants

- **NJ-927 filing variants** — - **Form NJ-927** — standard quarterly version, used by employers that remit withholding quarterly or monthly. - **Form NJ-927-W** — weekly version, required for employers whose prior-year aggregate withholding exceeded $10,000 (these employers must remit withholding on a weekly basis via EFT but still file NJ-927-W quarterly with the weekly totals). - **Form NJ-927-H** — household employer annual version (one annual return rather than four quarterly). - **Form WR-30** — quarterly wage report (separate from NJ-927, lists each employee with quarterly wages and weeks worked). Required from every NJ-927 filer.

### 3.3 Filing schedule (2025 calendar)

All NJ-927 returns must be filed electronically through the NJ Employer Access portal at [myleavebenefits.nj.gov/labor/myleavebenefits/employer/ or business.nj.gov]. Paper returns are not accepted for any employer with more than zero employees.

### 3.3 Filing schedule (2025 calendar)

**Filing schedule (2025 calendar)**

| Quarter | Period | Filing due date | Notes |
| --- | --- | --- | --- |
| Q1 2025 | Jan 1 – Mar 31 | April 30 2025 |  |
| Q2 2025 | Apr 1 – Jun 30 | July 30 2025 | NJ uses the 30th of the month following quarter end, NOT the federal 31st. |
| Q3 2025 | Jul 1 – Sep 30 | October 30 2025 |  |
| Q4 2025 | Oct 1 – Dec 31 | February 2 2026 | Q4 is the only quarter where the due date moves to the federal-aligned end-of-January-equivalent (last day of the month following quarter close, adjusted for weekends). |

### 3.3 Filing schedule (2025 calendar)

> Verify the Q4 due date against the published NJ-927 instructions for 2025; historical practice has been the last business day of January. For 2025, January 31 is a Saturday, so the deadline moves to Monday February 2 2026.

### 3.4 Payment frequency for withholding remittance

**Payment frequency for withholding remittance**

| Prior-year withholding | Remittance frequency |
| --- | --- |
| Less than $500 | Quarterly (with NJ-927) |
| $500 – $10,000 | Monthly (Form NJ-500 or via EFT by the 15th of the following month) |
| More than $10,000 | Weekly (EFT only, by the Wednesday following the payroll Friday for Fri-Tue payrolls, or the Friday following the payroll Sat-Wed for Wed-Fri payrolls) |

### 3.4 Payment frequency for withholding remittance

- **Remittance vs filing schedule distinction** — This thresholding mirrors but is NOT identical to the federal Form 941 lookback / semiweekly mechanics. An employer can be a federal semiweekly depositor but a NJ monthly remitter, or vice versa.

### 3.5 Penalties

- **NJ-927 penalties** — - **Late filing of NJ-927:** 5% per month or fraction (capped at 25%) plus $100 per month per N.J.S.A. 54:49-4. - **Late payment:** 5% of underpayment + interest at prime + 3% (2025 rate approximately 11.5% per annum). - **Late WR-30:** $5 per employee not reported, up to $25,000 per quarter. - **Failure to file electronically:** the Division has authority to assess a flat $50 per return. - **Insufficient funds:** $50 per dishonored payment.  _(N.J.S.A. 54:49-4)_

## 4. TDI (Temporary Disability Insurance) and FLI (Family Leave Insurance)

### 4.1 Statutory framework

- **TDI and FLI statutory basis** — TDI is established under the Temporary Disability Benefits Law (TDBL), N.J.S.A. 43:21-25 et seq. (originally enacted 1948). FLI is established under N.J.S.A. 43:21-39.1 et seq. (enacted 2008). Both are administered by NJDOL's Division of Temporary Disability and Family Leave Insurance.  _(N.J.S.A. 43:21-25 et seq.; N.J.S.A. 43:21-39.1 et seq.)_

### 4.2 2025 contribution rates

**2025 contribution rates**

| Component | Employee rate | Employer rate | Taxable wage base |
| --- | --- | --- | --- |
| TDI (state plan) | **0.23%** | **0.93%** (experience-rated, this is the new-employer benchmark) | **$165,400** for employee; **$43,300** for employer (the SUI base) |
| FLI | **0.06%** | None | **$165,400** |

### 4.2 2025 contribution rates

> Verify against the NJDOL "2025 Rate Information" notice typically published in late November / early December 2024. The 0.23% employee TDI rate and 0.06% FLI rate represent significant reductions from peak 2020-2021 levels (TDI was 0.47% and FLI was 0.28% in 2021). FLI dropped from 0.14% in 2023 to 0.06% in 2024 and has held at 0.06% for 2025. These rates are recalculated annually based on the actuarial fund balance.

### 4.3 Wage base mechanics — the dual base trap

- **Dual TDI wage base mechanics** — NJ uses two different taxable wage bases for TDI: 1. **Employee TDI wage base:** $165,400 in 2025. The employee 0.23% withholding stops once an individual's YTD wages cross this number. 2. **Employer TDI wage base:** $43,300 in 2025 (this is the SAME as the SUI base). The employer 0.93% (or experience-rated) contribution stops at $43,300 per employee per year. This split is unusual and frequently mis-handled by out-of-state payroll software vendors. The result is that the employer TDI maxes out at $402.69 per employee per year (43,300 × 0.93%) while the employee maxes out at $380.42 (165,400 × 0.23%). FLI uses the $165,400 wage base for the employee side (no employer side).

### 4.4 Private plan alternative

- **Private plan opt-out for TDI/FLI** — Employers may opt out of the state TDI plan or state FLI plan and offer a "private plan" providing at least equivalent benefits, approved by NJDOL. If approved: - Employer pays for plan administration (no 0.93% state contribution). - Employees may still be subject to employee contribution (up to the state rate, if the plan permits). - Employer still files NJ-927 but reports the private plan number in the appropriate field. - Plan must be approved using Form DP-1 (TDI) or Form FL-1 (FLI). Private plans were historically common in NJ for unionized workforces and large employers; many smaller employers stay on the state plan because the administrative burden of a private plan exceeds the saving.

### 4.5 WD/WF and SWF — the forgotten components

**WD/WF and SWF rates**

| Component | Employee rate | Employer rate | Wage base |
| --- | --- | --- | --- |
| Workforce Development Partnership (WF/WD) | **0.0425%** | **0.1175%** | $43,300 (the SUI base) |
| Supplemental Workforce Fund for Basic Skills (SWF) | **0.0175%** | **0.0250%** | $43,300 |

### 4.5 WD/WF and SWF — the forgotten components

- **Combined WD/SWF totals and burden** — > Verify: the combined employee WD+SWF is 0.0600% (often shown as a single line on pay stubs as "WF/SWF" or just "WF"). Combined employer WD+SWF is 0.1425%. The total non-UI, non-TDI/FLI payroll tax burden is therefore: - **Employee:** 0.0600% on first $43,300 = max $25.98/year. - **Employer:** 0.1425% on first $43,300 = max $61.70/year. These small amounts get reported on NJ-927 in the same UI/WF section.

## 5. SUI (State Unemployment Insurance)

### 5.1 2025 SUI parameters

- **2025 SUI parameters** — - **Taxable wage base:** $43,300 (employer); $43,300 (employee). Yes — NJ is one of the few states where employees ALSO pay UI directly out of wages. The employee UI contribution is currently **0.3825%** on the first $43,300, for a max of $165.62/year. - **New-employer rate (employer share):** **2.8%** plus the 0.1175% WD plus 0.0250% SWF = effective 2.9425%. - **Experience-rated employers:** rates range from a statutory minimum of 0.4% to a statutory maximum of 5.4% (plus the WF/SWF add-ons), determined annually by NJDOL based on Schedule A through E. NJ has been on Schedule C for 2024 and 2025 based on the trust fund balance. - **Rate notices:** NJDOL issues Form UI-1 to each experience-rated employer in August for the rate year starting July 1 (NJ uses a July-to-June rate year for SUI, NOT the calendar year — another quirk).

### 5.1 2025 SUI parameters

> Verify against the 2024-2025 and 2025-2026 NJ Employer Contribution Rate Notice.

### 5.2 Employee SUI quirk

- **Employee-funded UI states and W-2 reporting** — Most US states fund UI exclusively through employer contributions. NJ, PA, and AK are exceptions where employees contribute too. In NJ: - Employee UI rate: 0.3825% on first $43,300 (= $165.62 max/year). - This is withheld from paychecks and remitted with NJ-927. - On the W-2, employee UI/WF/SWF contributions show in Box 14 with the label "UI/WF/SWF" — these are deductible on Schedule A as state and local taxes (subject to the federal $10,000 SALT cap), though for most W-2 employees the standard deduction will swallow this.

### 5.3 Voluntary contributions

- **Voluntary contribution to buy down experience rate** — Like several states, NJ permits employers to make a "voluntary contribution" to buy down their experience rate before the rate year begins. The window is typically 30 days from the date of the UI-1 rate notice. This is rarely cost-effective except for employers whose rate jumped a full schedule (e.g., from 1.2% to 3.5% due to claims).

## 6. Form NJ-W4 — State W-4

### 6.1 Why a separate state W-4

- **Reasons NJ has separate state W-4** — Unlike states that piggy-back on the federal W-4 (e.g., NM, CO pre-2022), NJ has its own Form NJ-W4 because: 1. NJ uses allowances ($1,000 per allowance), while the post-2020 federal W-4 abolished allowances. 2. NJ has separate filing statuses for civil union partners. 3. NJ permits the employee to elect a specific withholding "Rate Table" (A through E), letting two-earner couples avoid joint-rate under-withholding.

### 6.2 The five rate tables

- **NJ-W4 rate table selection feature** — The NJ-W4 has a unique feature: lines 3 and 4 let the employee select one of five rate tables (A, B, C, D, or E) without changing their actual filing status on the eventual NJ-1040. This is designed to fix the historical under-withholding for two-earner married couples where one spouse claims "married joint" but the other spouse's income pushes the joint return into a higher bracket.

### 6.2 The five rate tables

**The five rate tables**

| Table | Use case |
| --- | --- |
| A | Single, or married filing separately |
| B | Married/CU joint where employee is sole wage earner |
| C | Married/CU joint where employee is the higher wage earner and spouse also works |
| D | Married/CU joint where employee is the lower wage earner |
| E | Head of household |

### 6.2 The five rate tables

In practice, table C is the most commonly mis-selected — many employees pick B (joint, sole earner) when both spouses work, leading to a balance due at NJ-1040 time.

### 6.3 Mandatory completion

- **NJ-W4 default and retention rule** — Employers must obtain a completed NJ-W4 from every new hire. If an employee fails to submit one, NJ default treatment is single with zero allowances, table A. NJ-W4 must be retained for at least four years after the date of the last payment of wages to the employee (N.J.A.C. 18:35-7.1).  _(N.J.A.C. 18:35-7.1)_

### 6.4 NJ-W4 vs. federal W-4 interaction

- **Misconception about federal W-4 satisfying NJ requirements** — A common misconception is that the federal W-4 satisfies NJ requirements. It does not. Even if the employer's HRIS only collects a federal W-4, NJ default rules apply (single/zero/Table A) until a separate NJ-W4 is filed. Many payroll systems offer a NJ-W4 e-signature step; verify this is enabled.

## 7. New hire reporting

### 7.1 Statutory basis

- **New hire reporting statutory basis** — Federal PRWORA 1996 requires every employer to report new hires within 20 days. NJ implements this under N.J.S.A. 2A:17-56.61 with administration by the NJ Office of Child Support Services within the Department of Human Services.  _(N.J.S.A. 2A:17-56.61)_

### 7.2 Mechanics

- **New hire reporting mechanics** — - **Deadline:** 20 calendar days from the date of hire (= first day work is performed for pay). - **Where to file:** NJ New Hire Reporting Center at nj-newhire.com (operated under contract). Filing methods include online portal, secure FTP for large employers, mail (Form NJ-W4 + cover sheet), or fax. - **Required data points:** Employee name, address, SSN, date of hire (or rehire if 60+ day gap); employer name, address, FEIN. - **Rehires:** Must be re-reported if there has been a 60-day separation. - **Independent contractors:** NJ DOES require new hire reporting for contractors expected to be paid $2,500 or more in a calendar year (this is broader than federal, which is silent on contractors). The rule is at N.J.S.A. 2A:17-56.61(b).  _(N.J.S.A. 2A:17-56.61(b))_

### 7.3 Penalties

- **New hire reporting penalties** — $25 per unreported new hire; $500 if the failure is the result of a conspiracy between employer and employee to avoid the report (intended to catch arrangements to evade child support enforcement).

## 8. Worker classification — the NJ ABC test

### 8.1 Statutory basis

- **ABC test statutory basis and case law** — The ABC test for unemployment compensation purposes is at N.J.S.A. 43:21-19(i)(6). The same test has been applied by the NJ Supreme Court to Wage and Hour Law cases (Hargrove v. Sleepy's, LLC, 220 N.J. 289 (2015)) and to wage payment law cases. As a practical matter the ABC test governs essentially every employment-vs-contractor question in New Jersey other than federal tax (which uses the IRS common law test).  _(N.J.S.A. 43:21-19(i)(6); Hargrove v. Sleepy's, LLC, 220 N.J. 289 (2015))_

### 8.2 The three prongs

- **ABC test three prongs** — A worker is presumed to be an EMPLOYEE unless the putative employer can show ALL THREE of: - **A — Freedom from control or direction over the performance of the service**, both under the contract of service and in fact. - **B — The service is either outside the usual course of business for which it is performed, OR the service is performed outside of all the places of business of the enterprise for which it is performed.** - **C — The individual is customarily engaged in an independently established trade, occupation, profession, or business.** All three must be satisfied. Failing any one prong = employee.  _(N.J.S.A. 43:21-19(i)(6))_

### 8.3 Prong B is the killer

- **Prong B examples in NJ case law** — In practice the prong that catches NJ businesses is B. The "usual course of business" inquiry asks whether the work performed by the contractor IS the business — a courier company hiring couriers, a cleaning company hiring cleaners, a coding consultancy hiring coders. The "outside of all the places of business" alternative is rarely satisfied either, because "place of business" is read broadly to include sites where the company conducts work. Examples that have failed prong B in NJ case law: - Sleepy's mattress delivery drivers (Hargrove). - Uber drivers (multiple NJDOL audits resulting in seven-figure assessments). - Construction subcontractors building the GC's projects. - Coding contractors working on the consultancy's billable client projects. - Adjuncts at private colleges. Examples that have passed prong B: - Outside counsel law firm hired by a non-law-firm business. - HVAC contractor servicing the building of a non-HVAC business. - Bookkeeper providing accounting services to a non-accounting business.

### 8.4 Construction Industry Independent Contractor Act

- **Construction Industry Independent Contractor Act requirements** — For construction (broadly defined to include building, structural alteration, demolition, repair, painting, decorating, roofing, electrical, plumbing, HVAC, masonry, excavation, drilling, paving, and related work), N.J.S.A. 34:20-1 et seq. ADDS additional requirements on top of the ABC test: 1. The ABC test must be satisfied; AND 2. The contractor must have its own business name, federal EIN, business address separate from the GC, and registration with appropriate state agencies (Division of Revenue, NJDOL). Misclassification in construction carries enhanced penalties — fines up to $2,500 first offense, $5,000 subsequent offenses, plus stop-work orders.  _(N.J.S.A. 34:20-1 et seq.)_

### 8.5 NJ Insurance Fraud Prevention Act exposure

- **Insurance fraud exposure for misclassification** — Issuing a 1099-NEC to a worker who should be a W-2 employee can constitute insurance fraud under N.J.S.A. 17:33A (if it reduces the workers' comp premium) — exposing the employer to civil penalties of up to $5,000 per misclassification plus treble damages. > **AUDIT FLASH POINT — ABC test, prong B, prong C.** NJDOL Wage and Hour Compliance ramped up cross-agency audits with the Division of Taxation starting 2020 under Executive Order 125. Audits typically pull 3-4 years of records. Document the ABC analysis contemporaneously for EVERY contractor, including: (1) the written contract showing freedom from control, (2) evidence the work is not the company's core business, (3) the contractor's separate business registration, EIN, marketing, other clients, and business insurance. Without this documentation, the burden of proof is on the employer and is almost always lost.  _(N.J.S.A. 17:33A)_

### 8.6 What does NOT make someone a contractor

These are common myths in NJ:
- "We have a written contract calling them a contractor." — irrelevant if the ABC test fails.
- "They wanted to be 1099." — irrelevant; the ABC test is non-waivable.
- "They have their own LLC." — necessary but not sufficient.
- "They invoice us." — necessary but not sufficient.
- "They work part-time." — irrelevant.
- "They work from home." — only relevant to prong B's secondary leg.

## 9. Earned Sick Leave Law

### 9.1 Statutory framework

- **ESLL statutory basis and effective date** — The NJ Earned Sick Leave Law (ESLL), N.J.S.A. 34:11D-1 et seq., took effect October 29 2018. It is among the most expansive in the US — broader than NY's, broader than CT's, comparable to CA's.  _(N.J.S.A. 34:11D-1 et seq.)_

### 9.2 Core entitlement

- **ESLL core entitlement terms** — - **Accrual:** 1 hour of sick leave per 30 hours worked. - **Annual cap:** Employer may cap accrual and use at 40 hours per benefit year. - **Eligibility:** Effectively all NJ workers — full-time, part-time, temporary, seasonal. Limited exclusions: construction workers covered by a CBA, per-diem healthcare employees, public employees with other sick leave entitlements. - **Carryover:** Up to 40 hours of unused leave must carry over to the next year, OR the employer may pay out unused leave at year-end at the employee's regular rate. - **Front-loading alternative:** Employer may front-load 40 hours at the start of the year instead of accruing. - **Permissible uses:** Employee's own illness, family member's illness, school closure, domestic violence/sexual assault, public health emergency, school meeting attendance.  _(N.J.S.A. 34:11D-1 et seq.)_

### 9.3 Documentation and payment

- **ESLL documentation and payment rules** — - Pay rate during sick leave = the employee's normal hourly rate (not minimum wage). - Employer may require notice up to 7 days for foreseeable use, no advance notice for unforeseeable. - Employer may require documentation only if 3+ consecutive days are taken. - Sick leave is NOT a wage for purposes of the Wage Payment Law — unused balances need not be paid out on termination unless the employer's policy or CBA so provides.

### 9.4 Recordkeeping

- **ESLL recordkeeping requirement** — Five-year retention requirement for all accrual, use, and payment records. Failure to maintain records creates a presumption that the employee's allegation of accrued leave is correct (N.J.S.A. 34:11D-6).  _(N.J.S.A. 34:11D-6)_

### 9.5 Penalties

- **ESLL penalties** — Up to $250 first violation, $500 subsequent, plus treble damages on unpaid sick leave, plus attorney's fees. NJDOL Wage and Hour can also order reinstatement and back pay for retaliation.

## 10. Wage Payment Law — pay frequency and method

### 10.1 Frequency

- **Minimum pay frequency requirement** — N.J.S.A. 34:11-4.2: "Every employer shall pay the full amount of wages due to his employees at least twice during each calendar month, on regular paydays designated in advance by the employer." This is the bi-weekly minimum. Exceptions: - **Bona fide executive, supervisory, or other special classification** workers (FLSA exempt under federal regs) — may be paid monthly. - **Sales reps on commission** — commissions may be paid monthly even if base salary is bi-weekly. Weekly pay is permissible and common for hourly workers. Semimonthly (15th and last day) is also permissible.  _(N.J.S.A. 34:11-4.2)_

### 10.2 Pay day timing

- **Payday timing after pay period end** — Wages must be paid within 10 working days after the end of the pay period (N.J.S.A. 34:11-4.2). So a pay period ending Friday Jan 3 2025 must be paid by Friday Jan 17 2025 at the latest.  _(N.J.S.A. 34:11-4.2)_

### 10.3 Payment method

- **Permitted wage payment methods** — Permitted methods: - Cash. - Check (must be on a NJ bank or capable of clearing without a fee to the employee). - Direct deposit (only with employee written authorization, never as a condition of employment). - Payroll card (subject to consumer protections under the NJ Wage and Hour Law amendments at N.J.A.C. 12:55-2.4).  _(N.J.A.C. 12:55-2.4)_

### 10.4 Wage statements

- **Itemized wage statement requirements** — The Wage Theft Act amendments of 2019 (P.L. 2019, c. 212) require itemized wage statements showing gross wages, deductions itemized, net wages, rate of pay, hours worked (for hourly), and pay period dates. NJ does NOT require the printed paystub to identify the employer's FEIN, unlike CA.  _(P.L. 2019, c. 212)_

### 10.5 Final wages

- **Final wage payment timing on termination** — Final wages on termination must be paid by the next regular payday (N.J.S.A. 34:11-4.3). NJ does NOT require immediate final pay on termination — distinguishing it from CA, where same-day final pay is required for involuntary termination.  _(N.J.S.A. 34:11-4.3)_

### 10.6 Wage Theft Act (2019)

- **Wage Theft Act penalty expansion** — P.L. 2019, c. 212 substantially expanded penalties: - Treble damages and attorney's fees on unpaid wages. - 6-year statute of limitations (was 2 years). - Personal liability for owners, directors, officers, and managing agents. - Criminal liability for willful violations.  _(P.L. 2019, c. 212)_

## 11. NY–NJ cross-border issues

### 11.1 No reciprocity for residents

- **NJ-NY reciprocity absence and credit mechanics** — NJ does NOT have a reciprocal income tax agreement with New York. (NJ does have reciprocity with Pennsylvania under the 1977 Reciprocal Personal Income Tax Agreement, which is a different matter — see Section 11.4.) For an NJ resident commuting to a NY employer: - NY taxes the wage income at NY rates as NY-source income, withheld via NY IT-2104. - NJ taxes the same wage income as resident income of an NJ resident. - NJ grants a credit for taxes paid to NY under N.J.S.A. 54A:4-1 ("credit for income tax of another state"). - The credit is limited to the LESSER of NY tax actually paid on the wages OR the NJ tax that would have been imposed on those same wages. In practice the NJ credit fully offsets the NJ tax for most NJ-resident NYC commuters because NY's rates (4% to 10.9% state plus NYC's 3.876% top for residents but NOT for non-residents) typically exceed NJ's. For NJ residents working in NYC the relevant comparison is NY state only (NYC personal income tax does NOT apply to non-NYC-residents), so the credit math is essentially NY state vs. NJ.  _(N.J.S.A. 54A:4-1)_

### 11.2 New York's "convenience of the employer" rule

- **NY convenience of the employer rule and NJ interaction** — NY applies a convenience of the employer rule (NY Tax Law §601, 20 NYCRR 132.18) under which a day worked at the employee's home OUTSIDE NY for the convenience of the employee (rather than the necessity of the employer) is treated as a NY workday, sourced to NY. This rule has been highly contested and was largely upheld by NY courts (most recently in Zelinsky v. NY Tax Appeals Tribunal). For NJ residents who work some days at home in NJ and some days in NY, this means: - NY claims the NJ work-from-home days as NY-source. - NJ credits the NY tax on those days under the §54A:4-1 mechanic. NJ does not apply a reverse convenience rule. NJ taxes its residents on worldwide income but treats wages earned actually in NJ (whether for an NJ or NY employer) as NJ-source.  _(NY Tax Law §601; 20 NYCRR 132.18)_

### 11.3 NJ employer with NY-resident employee

- **NY resident working in NJ tax treatment** — This is the cleaner case. NY resident working in NJ: - NJ withholds GIT on NJ-source wages. - NY resident is taxed by NY on worldwide income. - NY grants a credit for the NJ tax paid (NY Tax Law §620). - No "convenience" issue because NY does not apply the rule to NJ-source income (the rule runs the other direction).  _(NY Tax Law §620)_

### 11.4 PA–NJ reciprocity

- **PA-NJ reciprocity agreement and forms** — NJ and PA have a full reciprocity agreement: a PA resident working in NJ pays only PA tax (NJ does not withhold) and an NJ resident working in PA pays only NJ tax (PA does not withhold). To use the reciprocity, the employee files: - **Form NJ-165** — Employee's Certificate of Non-Residence in NJ (used by a PA resident telling an NJ employer to withhold PA, not NJ). - **Form REV-419** — used in the reverse direction (PA employer with NJ resident). The reciprocity covers WAGES ONLY. It does not cover self-employment, partnership, S-corp K-1, rental, or investment income.  _(1977 Reciprocal Personal Income Tax Agreement)_

### 11.5 Worked example deferral

See worked example 12.1 (NJ resident commuting to NYC) and example 12.3 (multi-state with NY commuters).

> **AUDIT FLASH POINT — NY/NJ residency and source allocation.** The NY Department of Taxation and Finance aggressively audits NJ residents claiming reduced NY workday counts post-COVID. Maintain daily contemporaneous workday logs (location-stamped calendar entries, badge swipes, expense receipts) for at least 6 years. Conversely NJ Division of Taxation audits NJ residents who claim large credits for NY tax to verify the NY return was actually filed and the credit is computed correctly under N.J.A.C. 18:35-4.1. Mismatches between the W-2 Box 16 (NJ wages) and the NY Form IT-203 non-resident allocation are the single most common trigger.

## 12. BAIT — Pass-Through Business Alternative Income Tax

### 12.1 What BAIT is

- **BAIT overview and statutory basis** — BAIT is NJ's response to the federal SALT cap. P.L. 2019, c. 320 (enacted January 2020), as amended by P.L. 2021, c. 419 (effective 2022), permits a pass-through entity (partnership, S-corp, LLC taxed as either) to elect to pay an entity-level tax at NJ rates, with the partners/members claiming a refundable credit on their NJ-1040 for their share of the BAIT paid. The federal benefit is that the BAIT is a deductible business expense at the entity level, bypassing the $10,000 SALT cap at the individual level.  _(P.L. 2019, c. 320; P.L. 2021, c. 419)_

### 12.2 BAIT rates 2025

**BAIT rates 2025**

| Entity distributive share | Rate |
| --- | --- |
| First $250,000 | 5.675% |
| Next $750,000 (250K–1M) | 6.52% |
| Next $4M (1M–5M) | 9.12% |
| Over $5M | 10.9% |

### 12.2 BAIT rates 2025

> Verify against PTE-100 instructions for 2025.

The rates approximate but do not exactly track the GIT rates. The 10.9% top BAIT rate is slightly above the 10.75% top GIT rate.

### 12.3 BAIT estimated payments

**BAIT estimated payments schedule**

| Quarter | Period | Due date 2025 |
| --- | --- | --- |
| Q1 | Jan 1 – Mar 31 | April 15 2025 |
| Q2 | Apr 1 – May 31 | June 16 2025 (June 15 is Sunday) |
| Q3 | Jun 1 – Aug 31 | September 15 2025 |
| Q4 | Sep 1 – Dec 31 | January 15 2026 |

### 12.3 BAIT estimated payments

- **BAIT estimated payment mechanics and safe harbor** — This is the payroll-adjacent piece relevant to this skill. A BAIT-electing entity must make estimated payments as scheduled. Note the quirky NJ estimated tax quarters (3-2-3-4 split) match the federal individual estimate schedule but differ from the corporate schedule. Estimates are paid via Form PTE-150 (online through the Division of Taxation portal). Safe harbor is 80% of current-year liability or 100% of prior-year (110% if prior AGI > $150K).

### 12.4 BAIT election deadline

- **PTE-100 election deadline** — The PTE-100 election must be filed by March 15 of the year following the tax year (so the 2025 election is due by March 15 2026). The election is annual — must be re-filed each year. Once filed, it is irrevocable for that year. > **AUDIT FLASH POINT — BAIT estimated payment quarterly deadlines.** Missing a BAIT estimate triggers underpayment penalty under N.J.S.A. 54:9-1 (interest at prime + 3%, currently ~11.5%) AND raises the risk that the IRS challenges the federal deduction as not "paid" in the year claimed. Federal Notice 2020-75 specifies that the SALT cap workaround requires the state tax to be PAID by the entity in the tax year; aggressive IRS auditors have argued that late estimates push the deduction to the following year. Schedule estimates calendar-locked at entity formation and run a year-end true-up by December 15 to ensure the full liability is paid in-year.  _(N.J.S.A. 54:9-1; Federal Notice 2020-75)_

### 12.5 Coordination with NJ-1040 / NJ-927

- **BAIT reporting separation from payroll filings** — BAIT is NOT reported on NJ-927. NJ-927 is exclusively for payroll items (withholding, UI, TDI, FLI, WF). BAIT is reported on the PTE-100 (annual) and PTE-150 (estimates) — a separate filing track entirely. The owner-level mechanics: 1. Entity pays BAIT. 2. Entity issues NJ K-1 reporting each owner's share of BAIT paid. 3. Owner claims refundable credit on NJ-1040 line for "BAIT credit." 4. If owner is also a wage-earner of the entity, the W-2 wages flow through NJ-927 unchanged; the BAIT credit only offsets the K-1 share.

## 13. Worked examples

### 13.1 Example: NJ-resident commuting to NYC employer (5-day in-office)

**Facts:** Maria is an NJ resident living in Hoboken. She works for Acme Bank Inc., a NY corporation headquartered in Manhattan. She works in the NYC office 5 days a week, no work-from-home days. Annual salary: $180,000. Maria is single, claims 1 NJ allowance.

**NY withholding (computed by Acme's NY-side payroll):**
- NY treats Maria as a NY non-resident.
- NY IT-2104 controls NY withholding.
- NYC tax does NOT apply (Maria is not a NYC resident).
- NY state tax on $180K for a single non-resident ≈ approximately $10,500 per the 2025 NY non-resident tables (subject to verification with the `us-ny-payroll` skill).

**NJ withholding:**
- Maria is an NJ resident, so NJ requires NJ-resident withholding.
- BUT NJ allows the employer to NOT withhold NJ tax if (a) the employer is NOT registered to do business in NJ AND (b) the employee's NJ tax would be fully offset by the credit for NY tax under §54A:4-1.
- Acme is a NY corporation not registered in NJ. Acme could choose to NOT withhold NJ tax. Many large NY employers DO withhold NJ tax as a courtesy to their NJ-resident employees, but they are not legally required to.

**On NJ-1040 (Maria's annual return):**
- NJ tax on $180,000 wages (single, after the standard $1,000 personal exemption) ≈ approximately $9,500.
- Credit for NY tax paid (~$10,500), capped at the lesser of NY tax or NJ tax = $9,500.
- Net NJ liability = $0.
- Maria gets no NJ refund of NY tax — the credit only goes up to NJ liability.

**Practical recommendation:** Acme should NOT withhold NJ. Maria will get a small NY refund / owe nothing in NJ. If Acme withholds NJ, Maria has to file NJ-1040 and get the full withholding back as refund — administrative drag with no benefit.

**TDI/FLI/UI implications:**
- Maria's wages are NY-source for income tax but NJ generally would NOT impose TDI/FLI/UI on Maria because Acme has no NJ nexus. Maria has no NJ UI coverage either — this is a real coverage gap. If she's terminated she may have a UI claim against NY only.

### 13.2 Example: NJ employer with all NJ employees

**Facts:** Garden State Bagels LLC is an NJ LLC with 12 employees all working at a single retail location in Princeton NJ. Owner-employee Sara receives a $90K salary (single, claims 2 allowances). Counter staff are paid $18/hr, average 30 hrs/week. Quarterly wages Q1 2025 total $180,000 across the 12 employees.

**Q1 2025 NJ-927 computation:**

GIT withholding on Sara ($90K, single, 2 allowances, Table A):
- Annualized taxable wages: $90,000 − $2,000 allowances = $88,000.
- NJ tax on $88,000 single: approximately $3,600 (per Table A brackets).
- Per-pay-period withholding (biweekly, 26 periods): ~$138.46 per check.
- Q1 (6 pay periods): ~$831 withheld from Sara.

GIT withholding on counter staff: averaging ~$3-8 per check; estimated Q1 aggregate ~$1,200.

Total GIT withholding Q1 ≈ $2,031.

UI/TDI/FLI/WF for Q1 (assume Q1 wages well under wage bases for all employees):
- Employer UI (new-employer rate 2.8%): 2.8% × $180,000 = $5,040.
- Employer TDI (0.93%): 0.93% × min($180K, 12 × $43,300) = 0.93% × $180,000 = $1,674 (assumes no individual employee crossed $43,300 in Q1).
- Employer WF (0.1175%): $211.50.
- Employer SWF (0.0250%): $45.
- Employee UI (0.3825%): $688.50.
- Employee TDI (0.23%): $414.
- Employee FLI (0.06%): $108.
- Employee WF (0.0425%): $76.50.
- Employee SWF (0.0175%): $31.50.

**Q1 NJ-927 total remittance:** GIT $2,031 + employer payroll taxes $6,970.50 + employee payroll taxes $1,318.50 ≈ $10,320.

**Remittance schedule:** Because Garden State Bagels' prior-year withholding was likely below $10K, they remit GIT monthly with NJ-500. UI/TDI etc. remit quarterly with NJ-927 itself.

**WR-30 filing:** Lists each of the 12 employees with their Q1 wages and number of base weeks worked.

### 13.3 Example: Multi-state employer with NY commuters AND NJ residents

**Facts:** Acme SaaS Inc. is a Delaware corp with offices in Manhattan (HQ, 50 employees) and Jersey City NJ (regional, 20 employees). It has employees in five states (NY, NJ, CT, PA, FL remote). For this example we focus on three specific employees:
- **Pat** — NY resident, works in Jersey City office 5 days/week (NJ-source income, NY resident).
- **Quinn** — NJ resident, works in Manhattan office 3 days, Jersey City 2 days (mixed source, NJ resident).
- **Rory** — NJ resident, works in Manhattan office 5 days (NY-source, NJ resident — like example 13.1).

**Pat (NY resident, NJ work):**
- NJ withholds GIT on Pat's full wages (NJ-source under NJ rules).
- NJ TDI/FLI/UI/WF apply (employer NJ nexus, Pat is NJ worker).
- NY withholds NY tax (Pat is NY resident, NY taxes worldwide).
- On Pat's NY IT-201 (resident return), Pat claims NY's credit for NJ tax paid under NY Tax Law §620.

**Quinn (NJ resident, mixed work):**
- NJ withholds GIT (Quinn is NJ resident; NJ source on Jersey City days; on NY days, NJ either does NOT withhold OR withholds and Quinn claims credit on NJ-1040).
- NY withholds NY tax on the Manhattan days as NY-source.
- BUT — convenience rule. If Acme has classified Quinn's 2 Jersey City days as "for the employer's necessity" (e.g., Acme operates the JC office and Quinn's role requires JC presence), the days are NJ-source. If Quinn is just choosing to work from JC for convenience, NY claims the days as NY-source under the convenience rule.
- Best practice: Acme documents the necessity of the JC days (e.g., Quinn manages the JC team).
- NJ TDI/FLI/UI/WF: Apply to the NJ-source portion. Allocation by day-count is the common approach.

**Rory (NJ resident, NY work):**
- See example 13.1.
- Acme has an NJ nexus through the JC office, so unlike a pure NY employer Acme is registered in NJ and likely withholds NJ tax. Rory will get NJ refund and claim NY credit on NJ-1040.

**NJ-927 for Acme:**
- Acme files ONE NJ-927 for all NJ-source wages aggregated (Pat full, Quinn allocated, Rory allocated based on actual NJ days if any).
- WR-30 lists Pat, Quinn, Rory (and other employees with any NJ-source wages) with NJ-allocated wages.

**Audit risk:** Acme should expect a NJDOL audit if (a) WR-30 wages diverge substantially from W-2 Box 16 NJ wages, (b) employees with NJ addresses do not appear on WR-30, or (c) the day-count allocation for Quinn is not documented with calendar evidence.

> **AUDIT FLASH POINT — NY-resident commuter vs NJ-resident commuter source rules.** The day-count allocation is the highest-risk area in multi-state payroll. Maintain (a) a written work-location policy, (b) per-employee day-count logs (calendar, badge, VPN, or time-tracking app), (c) a year-end reconciliation between payroll records and W-2 boxes 1, 15, 16, 17, and 20. Mismatches between Box 16 NJ and Box 16 NY (which can both exist on the same W-2) often trigger dual audits. Build the workpaper before issuing W-2s, not after.

### 13.4 Example: Contractor misclassification reclassified — assessment math

**Facts:** Lakeshore Construction LLC is an NJ GC. In 2023 it paid 8 "subcontractors" $50,000 each ($400,000 aggregate) on 1099-NEC. NJDOL audits in 2025 and concludes all 8 fail prong B (they performed the same construction work Lakeshore performs) and prong C (no separate business entities, EINs, or other clients). Reclassification to W-2.

**Retroactive liabilities (2023 amounts):**
- Employer UI (assume 5.4% × $43,300 wage base × 8 = $18,706).
- Employer TDI (0.93% × $43,300 × 8 = $3,222).
- Employer WF/SWF (0.1425% × $43,300 × 8 = $494).
- Total employer payroll taxes: ~$22,422.
- Employer share of GIT withholding NOT remitted: theoretically the workers' own GIT, but NJDOL pursues the employer for the unwithheld amount as a separate liability. At 5.525% bracket × $400K = $22,100. (NJDOL may abate if it can show the workers paid their own GIT on their 1099-NEC; often pursued as a holding lever.)
- Employee UI/TDI/WF that should have been withheld: ~$5,400 (employer becomes liable as collector).
- Penalties: 15% to 25% of taxes assessed.
- Interest: prime + 3% from each missed quarter (~11.5%/year), running 2+ years.
- Construction Industry Independent Contractor Act civil penalty: $2,500 first offense per worker = $20,000.
- NJ Insurance Fraud Prevention Act exposure: up to $5,000/worker = $40,000 + treble damages on saved workers' comp premium.
- Workers' Compensation Bureau retroactive audit: workers comp premiums on $400K wages (construction code 5403 ≈ $20/$100 = $80,000 premium).

**Range of total exposure: $150K – $250K on $400K of payments** — a 40-60% effective penalty. The construction industry premium reflects the additional CIICA layer; non-construction misclassifications typically run at the 20-30% effective rate level.

This example illustrates why the ABC test analysis must be done CONTEMPORANEOUSLY and DOCUMENTED. Once a 1099 is issued, the burden falls on the employer to defend, and in NJ defense is very difficult.

## 14. Year-end and recordkeeping

### 14.1 W-2 issuance

- **W-2 issuance and NJ-W-3 reconciliation** — - **Federal W-2 Copy 1** is filed with the NJ Division of Taxation via the NJ-W-3 reconciliation by February 15 of the following year (note: this is earlier than the federal January 31 deadline for SSA filing, AND earlier than most states). - NJ uses MMRRF format for electronic W-2 reporting (an extension of the federal EFW2 format). - **NJ-W-3** (Annual Reconciliation) reconciles total NJ withholding for the year against the four NJ-927 returns + monthly NJ-500 remittances. Filed with the W-2 batch.

### 14.2 1099 issuance

- **1099 filing requirements with NJ** — - NJ requires 1099-NEC, 1099-MISC, 1099-K filings to be transmitted to NJ Division of Taxation via the IRS Combined Federal/State Filing program for NJ-source payments. - Issuers may also file directly via the NJ MMRRF process if not using CF/SF. - Deadline: same as federal (January 31 for NEC, February 28/March 31 for others depending on form).

### 14.3 Record retention

**Record retention**

| Record | Minimum retention |
| --- | --- |
| Payroll records (timesheets, wages, deductions) | 6 years (Wage Theft Act 2019) |
| NJ-W4 forms | 4 years after last payment of wages |
| NJ-927 and supporting workpapers | 4 years |
| Earned Sick Leave records | 5 years |
| ABC test documentation | 4 years (UI audit lookback) |
| BAIT workpapers | 4 years (income tax SOL) |

## 15. Provenance and citations

### 15.1 Statutory citations used

- **N.J.S.A. 54A:2-1 et seq.** — NJ Gross Income Tax Act.  _(N.J.S.A. 54A:2-1 et seq.)_
- **N.J.S.A. 54A:4-1** — Credit for tax paid to another jurisdiction.  _(N.J.S.A. 54A:4-1)_
- **N.J.S.A. 54A:7-1** — Requirement of withholding from wages.  _(N.J.S.A. 54A:7-1)_
- **N.J.S.A. 43:21-19(i)(6)** — ABC test for UI purposes.  _(N.J.S.A. 43:21-19(i)(6))_
- **N.J.S.A. 43:21-25 et seq.** — Temporary Disability Benefits Law.  _(N.J.S.A. 43:21-25 et seq.)_
- **N.J.S.A. 43:21-39.1 et seq.** — Family Leave Insurance.  _(N.J.S.A. 43:21-39.1 et seq.)_
- **N.J.S.A. 34:11-4.2** — Wage Payment Law (pay frequency).  _(N.J.S.A. 34:11-4.2)_
- **N.J.S.A. 34:11D-1 et seq.** — Earned Sick Leave Law.  _(N.J.S.A. 34:11D-1 et seq.)_
- **N.J.S.A. 34:20-1 et seq.** — Construction Industry Independent Contractor Act.  _(N.J.S.A. 34:20-1 et seq.)_
- **N.J.S.A. 2A:17-56.61** — New hire reporting.  _(N.J.S.A. 2A:17-56.61)_
- **N.J.S.A. 17:33A** — Insurance Fraud Prevention Act.  _(N.J.S.A. 17:33A)_
- **P.L. 2019, c. 212** — Wage Theft Act.  _(P.L. 2019, c. 212)_
- **P.L. 2019, c. 320 (as amended by P.L. 2021, c. 419)** — BAIT.  _(P.L. 2019, c. 320 (as amended by P.L. 2021, c. 419))_
- **P.L. 2020, c. 95** — 10.75% millionaire surtax expansion.  _(P.L. 2020, c. 95)_

### 15.2 Administrative guidance

- **Publication NJ-WT** — NJ Income Tax Withholding Instructions, January 2025 revision.  _(Publication NJ-WT, January 2025 revision)_
- **NJ-927 Instructions** — 2025 edition.  _(NJ-927 Instructions, 2025 edition)_
- **NJDOL "2025 Rate Information" notice** — TDI/FLI/UI rate schedule.  _(NJDOL "2025 Rate Information" notice)_
- **NJ Division of Taxation Technical Bulletin TB-86** — Cross-jurisdiction credit.  _(NJ Division of Taxation Technical Bulletin TB-86)_
- **N.J.A.C. 18:35-7.1** — Recordkeeping for NJ-W4.  _(N.J.A.C. 18:35-7.1)_
- **N.J.A.C. 12:55-2.4** — Payroll cards.  _(N.J.A.C. 12:55-2.4)_
- **N.J.A.C. 18:35-4.1** — Credit for tax paid to another state — computation rules.  _(N.J.A.C. 18:35-4.1)_

### 15.3 Key case law

- **Hargrove v. Sleepy's, LLC** — 220 N.J. 289 (2015) — adopted ABC test for Wage and Hour purposes.  _(Hargrove v. Sleepy's, LLC, 220 N.J. 289 (2015))_
- **Carpet Remnant Warehouse, Inc. v. NJDOL** — 125 N.J. 567 (1991) — foundational ABC test interpretation.  _(Carpet Remnant Warehouse, Inc. v. NJDOL, 125 N.J. 567 (1991))_
- **Zelinsky v. NY Tax Appeals Tribunal** — 1 N.Y.3d 85 (2003), reaffirmed 2024 — NY convenience-of-employer rule constitutional.  _(Zelinsky v. NY Tax Appeals Tribunal, 1 N.Y.3d 85 (2003), reaffirmed 2024)_

### 15.4 Verification flags

All 2025 rate and threshold figures in this skill must be re-verified against:
1. The NJ-WT booklet posted to nj.gov/treasury/taxation/ in late 2024 / early 2025.
2. The NJDOL Annual Rate Notice (typically issued in November 2024 for calendar year 2025).
3. The NJ-927 instructions for 2025.
4. The PTE-100 / PTE-150 instructions for 2025.

In particular, the following figures are flagged for primary-source verification at the time of use:

- **TDI employee rate 0.23%** — published estimate; confirm against NJDOL rate notice.  _(NJDOL "2025 Rate Information" notice)_
- **TDI employer rate 0.93%** — new-employer benchmark; experience-rated employers must use their UI-1 rate.  _(NJDOL "2025 Rate Information" notice)_
- **FLI employee rate 0.06%** — published estimate.  _(NJDOL "2025 Rate Information" notice)_
- **SDI/FLI wage base $165,400 (employee)** — confirm against 2025 NJDOL notice; the figure is indexed to NJ statewide average weekly wage.  _(NJDOL "2025 Rate Information" notice)_
- **SUI/employer TDI wage base $43,300** — confirm against 2025 UI-1 schedule.  _(2025 UI-1 schedule)_
- **Supplemental wage rate 11.8%** — confirm in 2025 NJ-WT booklet.  _(2025 NJ-WT booklet)_
- **BAIT brackets** — confirm against PTE-100 instructions; the brackets were updated by P.L. 2021, c. 419 effective for tax years beginning in 2022 and have been stable since.  _(PTE-100 instructions; P.L. 2021, c. 419)_

## 16. Cross-references

- `us-federal-payroll` — Form 941, FICA, FUTA, federal W-4, Form W-2/W-3 federal mechanics.
- `us-ny-payroll` — NY IT-2104, NY convenience rule mechanics, NYC personal income tax.
- `us-pa-payroll` — PA Local Services Tax, PA-NJ reciprocity from the PA side.
- `nj-cbt-and-bait` — Full BAIT mechanics, NJ Corporation Business Tax, PTE-100 detailed line-by-line.
- `_cross-border/multistate-payroll` — Multi-state apportionment frameworks, day-count methodologies.
- `us-federal-tx-return-assembly` (reference only) — for the federal interaction with state PTE elections.

## 17. Quick reference card

**NJ Payroll 2025 — Quick Reference**

```
NJ Payroll 2025 — Quick Reference

GIT brackets (single): 1.4% / 1.75% / 3.5% / 5.525% / 6.37% / 8.97% / 10.75%
GIT brackets (MFJ):    1.4% / 1.75% / 2.45% / 3.5% / 5.525% / 6.37% / 8.97% / 10.75%
Supplemental wage rate: 11.8% (high earners) / marginal rate (others)
NJ-W4 allowance value: $1,000 per allowance

TDI employee: 0.23% on first $165,400 (max $380.42)
TDI employer: 0.93% on first $43,300  (max $402.69)
FLI employee: 0.06% on first $165,400 (max $99.24)
FLI employer: none

UI employee: 0.3825% on first $43,300 (max $165.62)
UI employer: 2.8% new / 0.4-5.4% experience-rated
WF employee: 0.0425% on first $43,300 (max $18.40)
WF employer: 0.1175% on first $43,300 (max $50.88)
SWF employee: 0.0175% on first $43,300 (max $7.58)
SWF employer: 0.0250% on first $43,300 (max $10.83)

NJ-927: Q1 Apr 30 | Q2 Jul 30 | Q3 Oct 30 | Q4 Feb 2 (2026)
NJ-500: 15th of month following (monthly remitters)
Weekly remitters: EFT, by Wed (Fri-Tue) / Fri (Wed-Fri)

W-2 to NJ: Feb 15 (NJ-W-3 reconciliation)
1099 to NJ: Jan 31 (NEC) / Feb 28 (others) via CF/SF or MMRRF

BAIT estimates 2025: Apr 15 | Jun 16 | Sep 15 | Jan 15 2026
BAIT election: PTE-100 by March 15 (annual, irrevocable)

New hire reporting: 20 days (employees + contractors > $2,500)
Pay frequency: bi-weekly minimum, paid within 10 working days
Earned Sick Leave: 1 hr per 30 hrs worked, 40 hrs/year cap
```

## End of skill

*End of skill. Total approximate length: 45 KB.*

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
