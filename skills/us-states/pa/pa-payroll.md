---
name: pa-payroll
description: Tier 2 Pennsylvania content skill for employer payroll compliance covering tax year 2025. Includes the 3.07% flat PIT, Local Earned Income Tax under Act 32 with employer withholding by employee-residence PSD code (rates 0.5-3.9%), Local Services Tax (typically $52/year), reciprocal agreements with NJ/OH/IN/MD/VA/WV that exempt non-resident employees from state withholding, Philadelphia and Pittsburgh wage taxes (separate from state PIT under Sterling Act), SUC wage base $10,000 with rates 1.4-9.1%, REV-419 state withholding form, the Construction Workplace Misclassification Act, and quarterly PA-501/UC-2 combined filings.
jurisdiction: US-PA
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# PA Payroll

## Scope note (blockquote)

**Scope.** This skill provides the rules an employer (or its preparer) must apply when running a Pennsylvania payroll for tax year 2025. It covers PA Personal Income Tax (PIT) withholding under 72 P.S. §§ 7301–7361, Act 32 Local Earned Income Tax (LEIT) withholding under 53 P.S. § 6924.501 et seq., the Local Services Tax (LST) under 53 P.S. § 6924.301.1, State Unemployment Compensation (SUC) under 43 P.S. § 751 et seq., the Sterling Act wage taxes administered by Philadelphia and Pittsburgh, the six reciprocal-state agreements, the Construction Workplace Misclassification Act (43 P.S. § 933.1 et seq.), final-pay rules under the PA Wage Payment and Collection Law (43 P.S. § 260.1 et seq.), and the quarterly and annual employer filings (PA-501 / PA-W3 / UC-2 / UC-2A / CLGS-32-1 / CLGS-32-6).

**Not in scope.** Federal income tax withholding (Pub. 15 / Form 941), federal FUTA, federal IRC § 401(k) plan administration, PA inheritance tax, PA personal income tax filing on Form PA-40, multi-state apportionment of wages for employers with no PA nexus, household-employer (Schedule H) returns, agricultural-labour exceptions, statutory-employee rules, and tipped-employee minimum-wage credits (PA follows the federal $2.83 tip-credit floor; this skill does not address it). Entity-level corporate net income tax, capital stock/franchise tax, and the PA Inheritance Tax are out of scope. Pittsburgh Payroll Expense Tax (PPET) on the *employer* (0.55% of payroll) is out of scope — this skill addresses Pittsburgh's wage tax on the *employee*. School-district income tax for non-Pittsburgh school districts is folded into the Act 32 EIT rate, not separated.

**Reviewer.** All output must be reviewed and signed by a credentialed reviewer (Enrolled Agent, CPA, attorney admitted in PA, or a PA Department of Revenue–registered third-party administrator) before any return is filed or any payroll is run for a live employee. Tax law is a moving target. The figures in this skill were current as of **November 2025**; verify any rate that drives a material number on the PA DOR site (revenue.pa.gov), the PA DCED Municipal Statistics portal (munstats.pa.gov), the Department of Labor & Industry UC employer site (uctax.pa.gov), and the issuing Tax Collection Committee (TCC) for each PSD before relying on it.

## 1. The 30-second Pennsylvania payroll picture

**Five wage-tax layers table**  _(See individual rows for citations)_

| Layer | Authority | 2025 rate | Wage base | Form |
| --- | --- | --- | --- | --- |
| Federal income tax (FIT) | IRC § 3402 | Graduated, Pub. 15-T | Unlimited | W-4, 941 |
| Federal FICA / Medicare | IRC § 3101 | 6.2% + 1.45% (+0.9% Add'l Medicare ≥ $200k) | $176,100 SS / unlimited Medicare | 941 |
| **PA Personal Income Tax** | 72 P.S. § 7302 | **3.07% flat** | Unlimited | REV-419, PA-W3, PA-501 |
| **PA SUC (employee)** | 43 P.S. § 781.4 | **0.07% (7¢ / $100)** | Unlimited (employee side) | (employer reports UC-2) |
| **PA SUC (employer)** | 43 P.S. § 781.3 | **1.419%–10.3734%** (2025 schedule, includes 9.2% solvency + 0.6% AETC + the basic rate 1.2125%–9.9333% — see §10) | **$10,000** | UC-2 / UC-2A |
| **Local EIT (Act 32)** | 53 P.S. § 6924.501 | **0.5%–3.9%** (employee-residence PSD) | Unlimited | CLGS-32-1 quarterly to TCC |
| **Local Services Tax (LST)** | 53 P.S. § 6924.301.1 | **Up to $52/yr per work location** | First $12,000 of wages (exemption threshold) | LST-1 / LST-3 |
| **Philadelphia wage tax** (Sterling Act) | 53 P.S. § 15971 et seq. | **3.75% resident / 3.44% non-resident** (eff. July 1 2025) | Unlimited | Quarterly Philadelphia Wage Tax return + W-2 Box 19/20 |
| **Pittsburgh wage tax** | Pittsburgh Code Ch. 245 | **3.0% total (1% city + 2% school)** for residents; **1.0%** for non-residents working in city | Unlimited | ET-1 quarterly |

- **Federal income tax (FIT)** — Graduated, Pub. 15-T  _(IRC § 3402)_
- **Federal FICA / Medicare** — 6.2% + 1.45% (+0.9% Add'l Medicare ≥ $200k)  _(IRC § 3101)_
- ****PA Personal Income Tax**** — **3.07% flat**  _(72 P.S. § 7302)_
- ****PA SUC (employee)**** — **0.07% (7¢ / $100)**  _(43 P.S. § 781.4)_
- ****PA SUC (employer)**** — **1.419%–10.3734%** (2025 schedule, includes 9.2% solvency + 0.6% AETC + the basic rate 1.2125%–9.9333% — see §10)  _(43 P.S. § 781.3)_
- ****Local EIT (Act 32)**** — **0.5%–3.9%** (employee-residence PSD)  _(53 P.S. § 6924.501)_
- ****Local Services Tax (LST)**** — **Up to $52/yr per work location**  _(53 P.S. § 6924.301.1)_
- ****Philadelphia wage tax** (Sterling Act)** — **3.75% resident / 3.44% non-resident** (eff. July 1 2025)  _(53 P.S. § 15971 et seq.)_
- ****Pittsburgh wage tax**** — **3.0% total (1% city + 2% school)** for residents; **1.0%** for non-residents working in city  _(Pittsburgh Code Ch. 245)_

Because four of these eight obligations are *local* (Act 32 EIT, LST, Philadelphia, Pittsburgh) and Act 32 keys to the **employee's residence** rather than the work site, PA payroll is widely regarded as the most complex state-local payroll regime in the United States. The single most common failure mode in practice is an employer who configures Act 32 by the **work location** PSD — that is correct only when the work-location rate exceeds the residence rate, and even then only as a "higher-of" override.

### 2.1 Rate, basis, and supplemental wages

- **PA PIT rate** — 3.07% (72 P.S. § 7302). Unchanged since 2004. Lowest flat-rate state income tax in the United States.  _(72 P.S. § 7302)_
- **Basis of compensation** — "Compensation" as defined in 72 P.S. § 7301(d), which is **broader** than federal "wages" in some respects (e.g., PA taxes the value of personal use of an employer-provided vehicle on a different valuation basis than IRC § 61) and **narrower** in others (PA does **not** tax most qualifying retirement-plan contributions, but **does** tax Roth 401(k) employer matches and *also* taxes traditional 401(k) deferrals at the time of deferral — PA is *not* a "401(k) follows federal" state; this is a frequent error).  _(72 P.S. § 7301(d))_
- **PA personal exemption / standard deduction** — **None.** PA PIT has no personal exemption, no standard deduction, and no itemized deductions other than the narrow IRC § 162 unreimbursed-employee-business-expense allowance on PA Schedule UE (for the employee's annual return, not the employer's withholding). Withholding is therefore a clean 3.07% of taxable compensation with no allowances to compute.  _(PA Schedule UE)_
- **Supplemental wages** — 3.07% (same as the regular rate). PA does not use the federal 22% supplemental rate. Bonuses, severance, commissions, and equity-compensation events are all withheld at 3.07%.  _(72 P.S. § 7302)_

### 2.2 Items NOT subject to PA PIT withholding

- **PA-PIT exempt items** — Section 125 cafeteria-plan elections for health, dental, vision, and dependent-care FSA (PA conforms to § 125 exclusion for these specific benefits). Qualified HSA payroll contributions (PA conforms to § 223). Workers' compensation, unemployment compensation, and most disability payments. Active-duty military pay earned by a PA resident outside PA. Most clergy housing allowances qualifying under IRC § 107.
- **PA-PIT taxable items despite federal deferral/exclusion** — Traditional 401(k), 403(b), and 457 elective deferrals (PA-PIT applies on contribution, not on distribution). Roth 401(k) deferrals (PA-PIT also applies on contribution). IRC § 132 qualified transportation fringe benefits in excess of statutory limits (PA conforms to the federal limit but only partially). Group-term life insurance > $50,000 (PA-PIT taxable on the same imputed amount as federal).

### 2.3 Form REV-419 — Pennsylvania's "Employee's Non-withholding Application"

- **REV-419** — REV-419 is **not** a normal W-4. It is filed by an employee who **claims an exemption** from PA withholding. There are only three grounds on which an employee can file REV-419: 1. The employee is a resident of a **reciprocal state** (NJ, OH, IN, MD, VA, WV — see §6) and the PA-source income is wages compensable in the reciprocal state. 2. The employee is a non-resident of PA whose only PA-source income is wages, and a treaty or statutory exemption applies. 3. The employee reasonably expects to have **no PA tax liability** for the year (rare for any employee earning above zero — PA has no zero bracket).  _(PA Reg. 61 Pa. Code § 113.6)_
- **REV-419 timing and forwarding** — REV-419 must be received **before** the employer ceases withholding. The employer retains the original and forwards a copy to the PA Department of Revenue within 30 days **only if** the employer has reason to believe the certificate is incorrect.  _(PA Reg. 61 Pa. Code § 113.6)_
- **No PA equivalent of federal Form W-4 default case** — There is **no PA equivalent of federal Form W-4 for the default withholding case** — every PA employee gets withheld at 3.07% unless an REV-419 is on file.

### 2.4 Deposit frequency and Form PA-501

**PA PIT deposit frequency table**  _(PA Reg. 61 Pa. Code § 113.4)_

| Annual PA PIT withheld | Deposit frequency | Form |
| --- | --- | --- |
| < $300 per quarter | Quarterly | PA-501 (paper) or e-TIDES filing |
| $300–$999 per quarter | Monthly (15th of following month) | PA-501 |
| $1,000–$4,999 per quarter | Semi-monthly | PA-501 |
| ≥ $5,000 per quarter | Semi-weekly (Wed./Fri. rule, mirrors federal) | PA-501 via myPATH only |

- **myPATH deposit portal** — Deposits are made through **myPATH** (PA DOR's portal, which replaced e-TIDES in November 2022). The PA-501 is technically a deposit coupon; the actual reconciliation occurs on the quarterly PA-W3 (see §2.5).  _(PA Reg. 61 Pa. Code § 113.4)_

### 2.5 Quarterly PA-W3 and annual reconciliation

- **PA-W3 filing frequency and due dates** — **PA-W3** is filed **quarterly** (not annually, despite its name — the "W3" is for the W-3 wage reconciliation that occurs in Q4). Due the last day of the month following the quarter end: April 30, July 31, October 31, January 31.
- **Annual reconciliation** — The **annual reconciliation** is the Q4 PA-W3 filed by January 31. It must agree to the sum of PA W-2 Box 16 wages and Box 17 PA tax withheld for all employees.
- **W-2 filing** — Federal Copy A is filed with the IRS; PA Copy (state copy) is filed with the PA DOR via myPATH by **January 31** following the calendar year. Paper filing is permitted only for employers with fewer than 10 W-2s; all others must file electronically.

**AUDIT FLASH POINT.** A PA-W3 that does not tie to the sum of W-2 Box 17s is the single most common trigger of a PA DOR desk audit. The reconciliation is mechanical — there is no allowance for rounding beyond $1 per W-2. If the employer also pays a third-party-sick-pay provider, the third-party W-2 must be aggregated into the reconciliation, which is a frequent miss.

### 3.1 What Act 32 changed (effective January 1, 2012)

- **Act 32 consolidation of local EIT collection** — Before Act 32 of 2008 (53 P.S. § 6924.501 et seq.), PA had over **560 separate local EIT collectors**, each with its own forms, deposit rules, and bank account. Act 32 consolidated collection by reorganising the Commonwealth into **69 Tax Collection Districts (TCDs)** — one per county, with the exception of Allegheny County (which has four) and Philadelphia (which is exempt from Act 32 because Sterling Act preempts; see §5). Each TCD elects a **Tax Collection Committee (TCC)** which appoints a **single Tax Collector** (such as Berkheimer, Keystone Collections Group, Capital Tax Collection Bureau, HAB-EIT, Centax, Jordan Tax Service, etc.). Employers now remit to *one* collector per TCD, not 560.  _(53 P.S. § 6924.501 et seq.)_

### 3.2 The PSD code system

- **Political Subdivision (PSD) code** — A **Political Subdivision (PSD) code** is a six-digit identifier issued by the PA Department of Community and Economic Development (DCED) that uniquely identifies a municipality + school district combination. The first two digits identify the TCD; the next two identify the municipality; the last two identify the school district. Every PA address resolves to exactly one PSD code, and every PSD code has exactly one resident EIT rate and one non-resident EIT rate published in the official **PSD Tax Register** at munstats.pa.gov.
- **Example PSD — Mt. Lebanon Township** — Example: Mt. Lebanon Township in Mt. Lebanon School District (Allegheny County) is **PSD 730203**, with a resident EIT rate of **1.30%** (1.0% municipal + 0.30% school) and a non-resident EIT rate of **1.00%** for tax year 2025.

### 3.3 The withholding rule — "higher of" residence vs. work site

- **Higher-of rule** — For each pay period, the employer must withhold the **greater of**: 1. The **resident EIT rate** of the employee's home PSD (the PSD where the employee lives), **or** 2. The **non-resident EIT rate** of the employer's work location PSD (the PSD where the employee performs services). The withholding is then remitted to the **work-location TCD's tax collector**. That collector forwards the resident portion to the employee's home TCD under the Act 32 interdistrict-settlement mechanism. The employer **never** remits to multiple TCCs for the same employee; the employer only ever deals with the TCC for its own work location.

**Worked illustration of the higher-of rule.**
Employee lives in **Upper St. Clair Township** (PSD 730304, resident rate 1.30%). Employee works at the employer's office in **Pittsburgh** (PSD 700102, non-resident rate 1.00% under the Sterling Act exception — see §7).
The higher-of comparison: resident 1.30% > non-resident 1.00%, so the employer withholds **1.30%** and remits to the Pittsburgh-area TCD collector (Jordan Tax Service for Allegheny South).
The Pittsburgh collector forwards the 1.00% non-resident portion to itself (it is also the work-location TCD) and the additional 0.30% to Mt. Lebanon-area collector for the school-district share via Act 32 settlement.

### 3.4 Form CLGS-32-6 — the Residency Certification Form

- **CLGS-32-6 requirement** — Before the **first** pay date for any new hire, the employer **must** obtain a completed **CLGS-32-6** ("Residency Certification Form / Local Earned Income Tax Withholding") from the employee. CLGS-32-6 requires the employee to certify: Home street address (residence); Home PSD code (employee looks up at munstats.pa.gov "PSD Code Finder"); Resident EIT rate; Work street address; Work PSD code; Non-resident EIT rate.
- **Employer reliance and liability** — The employer is **entitled to rely** on the PSD codes the employee certifies on CLGS-32-6 (53 P.S. § 6924.512(3)). If the employee enters a wrong PSD, the employee bears liability for under-withholding — **provided** the employer obtained and retained CLGS-32-6 on file. If the employer did not obtain CLGS-32-6, the employer is liable for the under-withheld amount plus penalties under 53 P.S. § 6924.509(g).  _(53 P.S. § 6924.512(3); 53 P.S. § 6924.509(g))_

**AUDIT FLASH POINT — Act 32 PSD code mismatch.** The PA DCED publishes an annual list of the top 25 PSDs with the highest employer error rate (typically townships whose names duplicate municipalities in other counties — e.g., **Hampton Township** exists in both Allegheny and Adams counties with different PSDs and different rates). When CLGS-32-6 shows a PSD that does not match the employee's W-2 Box 20 locality, the employer faces both a TCC under-withholding assessment and a potential PA DOR information-return penalty. Best practice: every CLGS-32-6 should be validated against the DCED PSD lookup at the time of intake, and re-validated annually for any employee with an address change.

### 3.5 Quarterly Act 32 filings

- **CLGS-32-1 filing** — Form **CLGS-32-1** is the quarterly EIT remittance return filed with the TCC's appointed tax collector (Berkheimer, Keystone, etc.). It is due the last day of the month following the quarter end (April 30, July 31, October 31, January 31). The return reports: Each employee's name, SSN, home PSD, gross compensation, EIT withheld; Total remitted with the return; Reconciliation to the prior quarter.
- **No statewide Act 32 portal** — Each tax collector publishes its own electronic filing portal — there is no statewide single portal for Act 32 (unlike PA-PIT, which is myPATH-only). Berkheimer uses "e-Filer"; Keystone uses "Pay Online with Keystone"; HAB-EIT uses "BSI." The format varies by collector.

### 3.6 Annual W-2 reporting for Act 32

- **W-2 Box 19/20 for Act 32 EIT** — **Box 19** — Local income tax withheld (Act 32 EIT, NOT including Philadelphia/Pittsburgh wage tax). **Box 20** — Locality name (use the resident PSD municipality name, formatted as "City/Twp Name PSD###### " — the PA DOR matching algorithm keys on PSD). A separate W-2 line is required for Philadelphia wage tax and for Pittsburgh wage tax — those are **not** Act 32 EIT and must be reported on their own Box 19/20 line with the city name (PHILADELPHIA / PITTSBURGH) instead of a PSD code.

### 4.1 What the LST is, and what it used to be

- **LST history and evolution** — The LST is the modern name for what was, before Act 7 of 2007, the **Emergency and Municipal Services Tax (EMST)** and, before 2004, the **Occupational Privilege Tax (OPT)** — a $10/year head tax on every person who worked in the municipality. Act 7 of 2007 (53 P.S. § 6924.301.1) raised the maximum cap from $10/year to **$52/year** (combined municipal + school-district share), restructured it to be deducted in **per-payroll** increments rather than once a year, and added an exemption for low-income workers earning **less than $12,000** at that work location.  _(53 P.S. § 6924.301.1)_

### 4.2 2025 mechanics

- **Maximum combined rate** — $52/year (municipal + school district combined). Cannot exceed $5/week per pay period.
- **Who imposes it** — Each municipality + its overlapping school district. Approximately **2,500** of PA's 2,560 municipalities impose some level of LST in 2025; the most common rates are $52 (urban/suburban), $47 ($10 muni + $37 school), $10 (rural), or zero (no ordinance).
- **Per-paycheck deduction** — $52 ÷ pay periods. For a biweekly payroll = $2.00/pay. For a weekly payroll = $1.00/pay. Cannot exceed $5/week regardless of pay frequency.
- **Withholding basis: work location, not residence** — Withhold by WORK LOCATION, not residence. This is the opposite of Act 32 EIT. If an employee lives in Erie but works in Pittsburgh, the employer deducts the Pittsburgh LST.
- **Low-income exemption** — An employee who reasonably expects total annual compensation from all sources at the LST work location to be less than $12,000 may file an **LST-3 Exemption Certificate** with the employer. Once the exemption is on file, no LST is withheld until the employee's YTD wages cross $12,000 at that work location, at which point retroactive catchup is required (the employer must deduct the full $52 over the remainder of the year).
- **Multiple work locations** — If an employee works in two or more municipalities, the LST is owed to the municipality where the employee works the **majority** of the time. A *primary employment* certificate (Form LST-2) is filed with the secondary employer to suspend LST withholding there.
- **Remittance** — Quarterly to the same Act 32 TCC tax collector that collects EIT. Form **LST-1** is the employer quarterly return; **LST-3** is the employee exemption certificate.

### 4.3 LST and self-employed earnings

- **LST for self-employed individuals** — The LST also applies to self-employed individuals who maintain a place of business in a municipality. Self-employed individuals file Form LST-3 / LST-S directly with the tax collector. This is out of scope for an employer payroll skill but is mentioned for completeness because LST disputes between an employer and a 1099 worker often turn on Construction Workplace Misclassification Act issues (see §9).

### 5.1 Why Philadelphia is different

- **Sterling Act background** — Philadelphia is the only Pennsylvania municipality whose wage tax pre-dates and supersedes Act 32. The **Sterling Act** of 1932 (53 P.S. § 15971 et seq.) grants Philadelphia a unique statutory authority to impose taxes "on any subject of taxation not preempted by the Commonwealth." The Philadelphia Wage Tax was first enacted in 1939 (Phila. Code § 19-1500) and is now the oldest local income tax in the United States. Because it pre-dates Act 32, the PA legislature explicitly carved Philadelphia out of the Act 32 system — Philadelphia has **no PSD code in the Act 32 sense**, and the Philadelphia Wage Tax is **separate from** and **in addition to** PA PIT.  _(53 P.S. § 15971 et seq.; Phila. Code § 19-1500)_

### 5.2 2025 rates

**Philadelphia 2025 wage tax rates**  _(phila.gov/revenue)_

| Category | Rate (Jan 1 – Jun 30 2025) | Rate (Jul 1 – Dec 31 2025) |
| --- | --- | --- |
| Resident (lives in Philadelphia) | 3.75% | 3.75% |
| Non-resident (works in Philadelphia, lives elsewhere) | 3.44% | 3.44% |

(Confirm both rates against the City of Philadelphia Department of Revenue site phila.gov/revenue before relying on these numbers — Philadelphia adjusts mid-year, and the FY26 budget that goes into effect July 1 2025 may revise the second-half rate.)

### 5.3 The residency rule

- **Philadelphia resident definition** — A **resident** is any individual domiciled in Philadelphia OR present in Philadelphia for more than 183 days in the year (Phila. Code § 19-1501).  _(Phila. Code § 19-1501)_
- **Non-resident employee working in Philadelphia** — A **non-resident employee** working in Philadelphia is subject to the non-resident rate (3.44%) on compensation for services performed within Philadelphia city limits.
- **Philadelphia resident working outside Philadelphia** — A Philadelphia resident who works **outside** Philadelphia is subject to the **resident** rate (3.75%) on all compensation from all sources — the employer in (say) King of Prussia must still withhold Philadelphia resident wage tax if the employee lives in Philadelphia.

### 5.4 The Sterling Act / Act 32 carve-out for PA residents

- **Sterling Act home-PSD credit mechanics** — A PA resident who lives outside Philadelphia and works in Philadelphia owes the Philadelphia non-resident wage tax (3.44%). That resident **also** owes Act 32 EIT to their home PSD. However, the Sterling Act provides a **credit** at the home-PSD level: the home municipality must give credit (up to the home-PSD rate) for Philadelphia wage tax paid. In practice, this means the home Act 32 EIT collector reduces the employee's annual local liability by the amount of Philadelphia wage tax withheld, with the result that the employee's combined local liability is the **higher of** Philadelphia non-resident rate or home PSD resident rate — never both stacked.
- **Payroll mechanics for the carve-out** — The employer withholds **Philadelphia non-resident wage tax at 3.44%** because the work location is in Philadelphia. The employer **does NOT also withhold Act 32 EIT** to the home PSD if the Philadelphia rate (3.44%) exceeds the home PSD rate (which it almost always will, since the highest non-Philadelphia PSD rate in PA is approximately 3.9%). The employee reconciles at year-end and may owe a small differential if the home PSD rate exceeds 3.44%. The employee files this differential on the home Act 32 annual return, not the employer.

**AUDIT FLASH POINT — Philadelphia under-withholding for commuting non-residents.** The Philadelphia Department of Revenue audits non-PA-resident commuters aggressively. A common employer error: employer is based in NJ but has a Philadelphia office; employer withholds NJ state income tax for NJ employees who commute to the Philadelphia office, but **fails** to withhold Philadelphia non-resident wage tax (3.44%). The Sterling Act applies to *every* non-resident who works in Philadelphia regardless of state of residence. NJ has a separate credit for Philadelphia wage tax on the NJ-1040, but the employer still must withhold the Philadelphia tax. Failure to withhold is a Philadelphia Code § 19-1503 violation carrying interest, penalty, and personal liability for the responsible party.

### 5.5 Philadelphia filings

- **Philadelphia filing requirements** — **Quarterly Wage Tax return** filed via the **Philadelphia Tax Center** (tax-services.phila.gov). Due April 30, July 31, October 31, January 31. **Annual reconciliation** filed by **January 31** following the year. **W-2 reporting.** Box 19 = Philadelphia wage tax withheld; Box 20 = "PHILADELPHIA". **Philadelphia BIRT (Business Income & Receipts Tax)** is a separate employer-level liability and is out of scope here.

### 6.1 The six reciprocal states

- **Reciprocity authority** — Pennsylvania has wage-tax reciprocity with six states (PA DOR Personal Income Tax Bulletin 2005-02 and subsequent updates).  _(PA DOR Personal Income Tax Bulletin 2005-02)_

**Reciprocal states table**  _(PA DOR Personal Income Tax Bulletin 2005-02)_

| State | Reciprocal form filed with PA employer | Notes |
| --- | --- | --- |
| New Jersey | NJ-165 ("Employee's Certificate of Non-Residence in New Jersey") + PA REV-419 | NJ employees of PA employers — PA does not withhold; NJ employer would otherwise withhold NJ tax |
| Ohio | IT-4NR ("Statement of Residency") + PA REV-419 | Ohio is *not* required to give credit — but Ohio has its own reciprocity statute that mirrors PA's |
| Indiana | WH-47 + PA REV-419 |  |
| Maryland | MW-507 line 8 (exempt) + PA REV-419 |  |
| Virginia | VA-4 line 4 (exempt) + PA REV-419 |  |
| West Virginia | WV/IT-104R + PA REV-419 |  |

### 6.2 How reciprocity works in payroll

- **Reciprocity payroll steps for NJ resident working in PA** — 1. Employee gives the PA employer a completed **PA REV-419** plus the NJ Form **NJ-165**. 2. PA employer **does not withhold PA PIT** (3.07%). 3. PA employer **withholds NJ state income tax** instead (graduated NJ rates, 1.4%–10.75%). 4. PA employer remits NJ withholding to the **NJ Division of Taxation** under the PA employer's NJ withholding account (the employer must register in NJ as a withholding agent — this is the practical pain point and the most common compliance failure). 5. Act 32 EIT — the rules here are subtle: The PA work-location PSD's **non-resident** EIT rate may still apply (because the employee earns income in PA, and Act 32 reaches non-residents). Reciprocity covers PA **state** PIT only; it does **not** waive Act 32 local EIT. In practice, NJ-resident employees pay the work-location PSD's non-resident EIT rate but get no credit against NJ tax (NJ does not credit PA local taxes — only the state-equivalent portion, and PA-PIT is the state-equivalent portion, which is now zero because of reciprocity). This is genuinely double taxation at the local level. NJ-resident commuters into PA pay NJ income tax plus PA non-resident Act 32 EIT. There is no cure. 6. **LST** still applies based on PA work location — reciprocity does not waive LST.

**AUDIT FLASH POINT — missed reciprocal-state filings.** A PA employer with NJ-resident employees must register as a NJ withholding agent and file NJ-927 quarterly. Failure to file is the most common compliance failure for small PA employers with one or two cross-border employees — the employer ends up withholding PA PIT improperly and the NJ employee gets a NJ underpayment notice. The fix is messy: NJ refund (or PA refund credit applied to NJ tax) plus penalties on both sides. Best practice: identify NJ/OH/IN/MD/VA/WV residents at onboarding via I-9 address review and immediately set up REV-419 + reciprocal certificate.

### 6.3 Maryland special case — Philadelphia-area Maryland commuters

- **Maryland-Philadelphia commuter puzzle** — PA-MD reciprocity exempts PA-state PIT withholding for the MD employee. But Philadelphia Wage Tax is **not** PA PIT — it is a separate municipal tax under the Sterling Act. Reciprocity does **not** apply to Philadelphia Wage Tax (Phila. Code does not honour PA reciprocity). The MD employee therefore owes Philadelphia non-resident wage tax (3.44%) **and** Maryland state tax (employer must withhold both — PA via reciprocity-waived REV-419, Philadelphia mandatory). Maryland gives a credit on Form 502CR for Philadelphia wage tax paid, but again the credit is at the MD employee level, not the employer payroll level.

### 7.1 The Pittsburgh structure

- **Pittsburgh wage tax authority** — The City of Pittsburgh and Pittsburgh School District jointly levy a wage tax under PA Act 511 of 1965 (the Local Tax Enabling Act, of which Act 32 is the modern EIT framework). Pittsburgh is **inside** the Act 32 system, but its rate structure is unusually high because of the school-district add-on.  _(PA Act 511 of 1965)_

**Pittsburgh wage tax rate table**  _(Pittsburgh Code Ch. 245)_

| Category | City share | School-district share | Total |
| --- | --- | --- | --- |
| Resident (PSD 700102 / 700101) | 1.0% | 2.0% | **3.0%** |
| Non-resident working in Pittsburgh | 1.0% | 0% (school cannot reach non-residents) | **1.0%** |

### 7.2 How Pittsburgh interacts with Act 32

- **Pittsburgh higher-of scenarios** — Because Pittsburgh is inside Act 32, the same higher-of rule applies: **Pittsburgh resident working in Pittsburgh** — 3.0% withholding (1.0% city + 2.0% school). **Pittsburgh resident working elsewhere in PA** — 3.0% (resident rate is higher than virtually any non-resident PSD rate the employer might find). **Non-Pittsburgh PA resident working in Pittsburgh** — higher of home PSD resident rate vs. 1.0% Pittsburgh non-resident. For most surrounding suburbs the home resident rate (~1.0%–1.3%) is higher, so the employer withholds the home rate and remits to the work-location TCD (Allegheny South), which forwards the residence portion to the home TCD. **NJ/OH/etc. resident working in Pittsburgh** — PA reciprocity covers PA PIT only; the 1.0% Pittsburgh non-resident wage tax still applies.

### 7.3 Pittsburgh Payroll Expense Tax (briefly)

- **Pittsburgh Payroll Expense Tax** — Pittsburgh also imposes a **Payroll Expense Tax** of **0.55%** on the **employer's** total compensation paid to employees who work within Pittsburgh. This is an employer-side tax (analogous to an Oregon transit tax), filed on Pittsburgh ET-1. It is mentioned here only to flag that "Pittsburgh tax" in PA can mean either of two things — the wage tax (employee-side, in scope here) or the payroll expense tax (employer-side, out of scope here).

### 7.4 Other major-city wage taxes

**Other major-city wage tax table**

| City | Resident rate | Non-resident rate | Notes |
| --- | --- | --- | --- |
| Allentown | 1.975% | 1.0% | Inside Act 32 (Lehigh County TCD) |
| Reading | 3.6% | 1.0% | Inside Act 32 (Berks County TCD); resident rate among highest in PA |
| Erie | 1.65% | 1.0% | Inside Act 32 (Erie County TCD) |
| Scranton | 3.4% | 1.0% | Inside Act 32 (Lackawanna County TCD); split as 1.0% city + 2.4% school |
| Harrisburg | 2.0% | 1.0% | Inside Act 32 (Dauphin County TCD) |
| Bethlehem | 1.0% | 1.0% | Spans Northampton and Lehigh; check which TCD |

All of these go through the Act 32 TCD system — Philadelphia is the only Sterling Act outlier.

### 8.1 Wage base, rates, and the employee contribution

- **Wage base** — **$10,000** per employee per year. PA's wage base has been $10,000 since 1984 and is among the lowest in the United States. Compare to states with wage bases above $40,000 (Oregon $54,300, Washington $72,800).  _(43 P.S. § 781.4)_
- **New-employer rate** — **3.689%** (basic 3.5000% + 9.2% solvency add-on factored in) for non-construction employers; **10.2238%** for construction employers. (The construction "new employer" rate reflects the higher-risk SIC code 23 classification.)
- **Experience-rated employer total** — **1.419%–10.3734%** for 2025, which combines: Basic rate: 1.2125% – 9.9333% (from PA UC Rate Schedule); Solvency add-on: 9.2% of basic (variable); Additional Contribution (AETC): 0.6% (suspended in some years, active in 2025); Interest factor: 0% (PA Trust Fund is solvent in 2025; no Title XII interest tax).
- **Employee contribution** — **0.07%** of total wages (unlimited, no wage cap on the employee side). PA is one of three states (with Alaska and NJ) that imposes a small employee UC contribution. Employer withholds and remits with the quarterly UC-2.

### 8.2 Quarterly Form UC-2 / UC-2A

- **UC-2 form** — **UC-2** — Employer's Report for Unemployment Compensation. Quarterly. Due the last day of the month following the quarter end.
- **UC-2A form** — **UC-2A** — Employer's Quarterly Report of Wages Paid to Each Employee. Filed with UC-2.
- **Electronic filing via UCMS** — Filed electronically through the **UCMS (Unemployment Compensation Management System)** at uctax.pa.gov. Paper filing is permitted only for employers with fewer than 100 employees. The UC-2 and UC-2A are filed separately from the PIT PA-W3 — there is no combined return in PA at the state level. (At the local level, CLGS-32-1 + LST-1 are usually filed together with the same TCC tax collector.)

### 8.3 Reporting newly hired employees

- **New hire reporting** — Within 20 days of hire, PA employers must report new hires to the **PA New Hire Reporting Program** (pacareerlink.pa.gov). This is in addition to (not instead of) federal new-hire reporting requirements.

## 9. Construction Workplace Misclassification Act

- **Three conditions for IC classification** — The Construction Workplace Misclassification Act (Act 72 of 2010, codified at 43 P.S. § 933.1 et seq.) sets a stringent test for treating a construction-industry worker as an independent contractor rather than an employee. All three of the following conditions must be met for IC classification to stand: 1. The individual has a **written contract** to perform the services. 2. The individual is **free from control or direction** over performance of the services, both under the contract and in fact. 3. The individual is **customarily engaged in an independently established trade, occupation, profession, or business** with respect to the services.  _(43 P.S. § 933.1 et seq.)_
- **Element 3 sub-tests** — Element 3 has six sub-tests, of which at least three must be met: Holds a federal employer identification number (EIN); Filed Schedule C / 1120 / 1065 for the trade in the prior year; Has a separate business location; Has a business name distinct from the worker's personal name; Maintains general liability insurance ≥ $50,000; Has the ability to realize a profit or loss.
- **Penalties** — $1,000 for the first intentional violation; $2,500 per subsequent. Stop-work orders are available against the employer. The Attorney General also has criminal-prosecution authority for repeated knowing violations.
- **Comparison to federal/common-law tests** — The Act 72 test is **stricter than the federal common-law test** and **stricter than the PA DOL economic-realities test** for non-construction industries. A construction worker who would qualify as a 1099 contractor under the IRS 20-factor test or the ABC test may nonetheless be a statutory employee under Act 72.
- **Non-construction classification tests** — For non-construction industries, PA uses the common-law "right to control" test for PIT withholding purposes and the broader "ABC test" for UC purposes.  _(43 P.S. § 753(l)(2)(B); Department of Labor & Industry v. Stuber, 822 A.2d 870 (Pa. Commw. 2003))_

## 10. Final Pay (PA Wage Payment and Collection Law)

- **Final wages timing** — **Voluntary termination or involuntary discharge** — final wages are due no later than the **next regular payday** on which the wages would have been paid had employment continued.  _(43 P.S. § 260.5)_
- **No same-day/72-hour rule** — **There is no PA equivalent of California's same-day or 72-hour final-pay rule** for involuntary discharge. Next regular payday is the bright-line rule for all separations.
- **Accrued vacation payout** — Whether accrued vacation must be paid out depends on the employer's written policy or contract (43 P.S. § 260.2a defines "wages" to include "fringe benefits or wage supplements" that are due under contract or policy). If the policy is silent, PA case law (*Geletta v. Allegheny Ludlum Steel*) suggests accrued vacation is generally payable.  _(43 P.S. § 260.2a; Geletta v. Allegheny Ludlum Steel)_
- **Penalties for late payment** — 25% of unpaid wages OR $500, whichever is greater, plus attorney's fees.  _(43 P.S. § 260.10)_

### 11.1 PA-resident commuting between two PA municipalities

**Facts.** Maria lives at 123 Main St, Mt. Lebanon Township, Allegheny County (PSD 730203, resident EIT rate 1.30%, school district Mt. Lebanon). She works at her employer's office in Greentree Borough, Allegheny County (PSD 730103, non-resident EIT rate 1.00%). The employer has approximately 50 employees and a quarterly PA PIT liability of ~$8,000, putting it on the semi-monthly deposit schedule. Maria's gross pay for the biweekly pay period is **$3,000** with no § 125 election. Mt. Lebanon and Greentree both impose a $52/year LST.

**Withholding for the pay period**

| Item | Calculation | Amount |
| --- | --- | --- |
| Federal income tax | Per W-4, Pub. 15-T | (FIT not computed here — federal scope) |
| Social Security | $3,000 × 6.2% | $186.00 |
| Medicare | $3,000 × 1.45% | $43.50 |
| **PA PIT** | $3,000 × 3.07% | **$92.10** |
| **PA UC (employee)** | $3,000 × 0.07% | **$2.10** |
| **Act 32 EIT** | Higher of (1.30% resident, 1.00% non-resident) = 1.30%; $3,000 × 1.30% | **$39.00** |
| **LST (work location)** | $52/year ÷ 26 pay periods | **$2.00** |
| **Total PA + local withholding** |  | **$135.20** |

PA PIT ($92.10) — remitted to PA DOR via myPATH on the employer's semi-monthly schedule; reported on PA-W3 Q1. PA UC employee contribution ($2.10) — bundled into the quarterly UC-2 and remitted to the PA Department of Labor & Industry. Employer also pays its own UC contribution on the first $10,000 of Maria's wages (separate calculation). Act 32 EIT ($39.00) — remitted to the **Allegheny South Tax Collection District** tax collector (Jordan Tax Service) on CLGS-32-1; the collector then forwards 0.30% (the school-district share for Mt. Lebanon) to Mt. Lebanon's TCC via Act 32 settlement. LST ($2.00) — remitted to the **Greentree work-location collector** on LST-1.

Federal W-4. PA REV-419 — **not required** (Maria is a PA resident, default 3.07% withholding applies). **CLGS-32-6** — required, listing Maria's home address, home PSD 730203 (resident rate 1.30%), work PSD 730103 (non-resident rate 1.00%). LST-3 — not filed (Maria's annual wages > $12,000).

### 11.2 NJ resident under PA-NJ reciprocity

**Facts.** Daniel lives at 45 Elm Ave, Cherry Hill, NJ. He works at his employer's office in Conshohocken, PA (PSD 460102, Montgomery County TCD, non-resident EIT rate 1.00%). Gross biweekly pay: **$4,000**.

Federal W-4. **PA REV-419** — filed by Daniel claiming exemption from PA PIT under PA-NJ reciprocity. **NJ-165** — filed by Daniel certifying NJ residence (employer keeps this with REV-419). **NJ-W4** — filed by Daniel for NJ withholding allowances. **CLGS-32-6** — Daniel certifies his home address is in NJ (no PSD code — NJ has no Act 32 system), and his work PSD is Conshohocken 460102. The form has a checkbox for "out-of-state resident."

**Withholding for the pay period**

| Item | Calculation | Amount |
| --- | --- | --- |
| Federal income tax | Per W-4 | (federal scope) |
| Social Security | $4,000 × 6.2% | $248.00 |
| Medicare | $4,000 × 1.45% | $58.00 |
| **PA PIT** | **$0** (REV-419 reciprocity exemption) | **$0.00** |
| **NJ state income tax** | NJ graduated tables, biweekly | (NJ rates; ~$140 for $4,000 biweekly assuming single + no allowances) |
| **PA UC (employee)** | $4,000 × 0.07% (still owed — UC is not income tax and is not within reciprocity) | **$2.80** |
| **Act 32 EIT** | Higher of (NJ has no resident PA rate = 0%, vs. 1.00% Conshohocken non-resident) = 1.00%; $4,000 × 1.00% | **$40.00** |
| **LST (work location)** | $52/year ÷ 26 pay periods (Conshohocken imposes LST) | **$2.00** |

The PA employer must register as a **NJ withholding agent** (NJ Form NJ-REG) and obtain a NJ withholding account number. NJ-927 is filed quarterly to remit NJ withholding. Failure to register is a common error and is one of the most-cited audit findings for small PA employers with cross-border commuters.

Daniel pays Conshohocken's non-resident EIT rate (1.00%) with no offsetting credit on his NJ return — this is genuine double taxation at the local level. NJ Form NJ-1040 line "credit for taxes paid to other jurisdictions" gives credit for the PA state-equivalent tax only, which is zero by virtue of reciprocity. Daniel cannot recover the $40 Conshohocken EIT through the NJ credit; it is a sunk cost of commuting.

### 11.3 PA resident commuting into Philadelphia (Sterling Act)

**Facts.** Sarah lives at 789 Oak St, Wayne, Radnor Township, Delaware County (PSD 230102, resident EIT rate 1.00%). She works at her employer's office at 1500 Market St, Philadelphia (Phila. is outside Act 32 — no PSD; Sterling Act applies). Gross biweekly pay: **$5,000**. The employer has a substantial Philadelphia workforce and is on the semi-monthly Philadelphia wage-tax deposit schedule.

Federal W-4. PA REV-419 — **not required** (Sarah is a PA resident; default 3.07% PA PIT applies). **CLGS-32-6** — Sarah certifies home PSD 230102 (Radnor Twp / Radnor SD, resident rate 1.00%). Work location is Philadelphia, which has no Act 32 PSD; the form indicates "Philadelphia — Sterling Act" in the work PSD field.

**Withholding for the pay period**

| Item | Calculation | Amount |
| --- | --- | --- |
| Federal income tax | Per W-4 | (federal scope) |
| Social Security | $5,000 × 6.2% | $310.00 |
| Medicare | $5,000 × 1.45% | $72.50 |
| **PA PIT** | $5,000 × 3.07% | **$153.50** |
| **PA UC (employee)** | $5,000 × 0.07% | **$3.50** |
| **Philadelphia non-resident wage tax** | $5,000 × 3.44% | **$172.00** |
| **Act 32 EIT** | **$0** — Philadelphia wage tax (3.44%) exceeds Radnor resident rate (1.00%); home-PSD credit absorbs the entire home obligation. Employer does not double-withhold. | **$0.00** |
| **LST (Philadelphia)** | Philadelphia imposes no LST equivalent at the work location (Philadelphia residents pay the School Income Tax instead, but commuters do not). | **$0.00** |

PA PIT — myPATH to PA DOR. PA UC — quarterly UC-2 to PA Department of Labor & Industry. Philadelphia wage tax — Philadelphia Tax Center (tax-services.phila.gov), filed quarterly on the Philadelphia Wage Tax return.

Box 15 — PA, employer's PA state ID. Box 16 — PA wages (= federal wages less PA-only exclusions, plus PA-only inclusions per §2.2). Box 17 — PA PIT withheld (sum of $153.50 × 26 ≈ $3,991). Box 18 — Local wages (Philadelphia wage subject to wage tax). Box 19 — Philadelphia wage tax withheld (sum of $172.00 × 26 ≈ $4,472). Box 20 — "PHILADELPHIA". Sarah files her annual Radnor Township local return showing $0 owed because Philadelphia wage tax exceeded the home rate (1.00% vs. 3.44%). The Radnor collector does not refund the difference; the Sterling Act credit operates as a non-refundable offset, not a refundable overpayment.

## 12. Summary checklist for a PA employer

Before running the first PA payroll for a new employee, the employer must confirm:
- [ ] Federal W-4 on file
- [ ] PA REV-419 on file **only if** claiming exemption (reciprocity or zero-liability ground)
- [ ] If reciprocal-state resident: home-state reciprocal form (NJ-165, IT-4NR, WH-47, MW-507, VA-4, WV/IT-104R) on file
- [ ] If reciprocal-state resident: PA employer registered as withholding agent in the home state
- [ ] CLGS-32-6 on file with employee-certified home PSD and work PSD
- [ ] PSD codes validated against munstats.pa.gov current-year register
- [ ] LST-3 exemption on file **only if** employee expects < $12,000 in annual wages at the work location
- [ ] Employee is correctly classified as employee, not contractor — for construction industry, all three Act 72 conditions met
- [ ] If new hire: report to PA New Hire Reporting Program within 20 days
- [ ] If employee works in Philadelphia: Philadelphia Department of Revenue business account registered; wage-tax filing schedule confirmed
- [ ] If employee works in Pittsburgh: Pittsburgh Tax Office account registered; ET-1 filing schedule confirmed
- [ ] PA UC account established with PA Department of Labor & Industry; experience rate or new-employer rate confirmed in writing

Each quarter, the employer files:
- [ ] PA-W3 (PA DOR via myPATH)
- [ ] CLGS-32-1 EIT return (to work-location TCC tax collector)
- [ ] LST-1 (to work-location TCC tax collector — often same form/portal as CLGS-32-1)
- [ ] UC-2 + UC-2A (PA L&I via UCMS)
- [ ] Philadelphia Wage Tax return (if applicable)
- [ ] Pittsburgh ET-1 (if applicable)
- [ ] Each reciprocal state: state withholding return (NJ-927, OH IT-501, IN WH-1, MD MW-506, VA VA-15, WV IT-101)

Each year, the employer files:
- [ ] PA W-2s with PA DOR (via myPATH, by January 31)
- [ ] Federal W-2s with SSA (federal scope)
- [ ] PA Annual Reconciliation (Q4 PA-W3 doubles as annual recon)
- [ ] Act 32 annual reconciliation with TCC tax collector
- [ ] LST annual reconciliation
- [ ] Philadelphia Wage Tax annual reconciliation (if applicable)

## 13. Provenance and citations

Primary authorities consulted in compiling this skill (verify before relying on any specific figure):
- 72 P.S. §§ 7301–7361 (PA Tax Reform Code of 1971, Article III — Personal Income Tax)
- 61 Pa. Code §§ 113.1–113.20 (PA Department of Revenue PIT withholding regulations)
- 53 P.S. § 6924.101 et seq. (Local Tax Enabling Act, including Act 32 of 2008 at § 6924.501)
- 53 P.S. § 6924.301.1 (Local Services Tax)
- 53 P.S. § 15971 et seq. (Sterling Act, 1932)
- Phila. Code §§ 19-1500 to 19-1510 (Philadelphia Wage Tax)
- Pittsburgh Code Ch. 245 (Pittsburgh Wage Tax)
- 43 P.S. §§ 751–918 (PA Unemployment Compensation Law)
- 43 P.S. §§ 933.1–933.17 (Construction Workplace Misclassification Act, Act 72 of 2010)
- 43 P.S. §§ 260.1–260.13 (PA Wage Payment and Collection Law)
- PA DOR Personal Income Tax Bulletin 2005-02 (reciprocity)
- PA DCED Municipal Statistics Portal — PSD Tax Register, current edition (munstats.pa.gov)
- PA DOR myPATH employer guide, 2025 edition
- PA L&I UCMS employer guide, 2025 edition
- Philadelphia Department of Revenue Wage Tax instructions, 2025 (phila.gov/revenue)
- Pittsburgh Tax Office ET-1 instructions, 2025

Cross-jurisdiction PA-NJ commuter authorities: *Edwards v. Director, Div. of Taxation*, 30 N.J. Tax 142 (2017) (NJ credit-for-taxes-paid mechanics for Philadelphia wage tax).

## 14. Circular 230 reviewer notice

This skill is a content reference and **does not constitute tax advice**. All output produced using this skill must be reviewed and signed by a credentialed practitioner subject to Circular 230 (Enrolled Agent, CPA, or attorney admitted in Pennsylvania) before any return, deposit, or W-2 is filed or any payroll is run for a live employee. The reviewer is responsible for:
1. Confirming each rate, threshold, and form reference against the issuing authority's current-year publication.
2. Confirming each PSD code against the PA DCED Municipal Statistics Portal.
3. Confirming each TCC tax collector's current filing format and portal.
4. Confirming reciprocal-state registration status for any cross-border employee.
5. Confirming Philadelphia / Pittsburgh registration status for any in-city work location.
6. Documenting the basis for every Act 72 contractor-vs.-employee determination.

The figures in this skill were current as of **November 15, 2025**. Material changes after that date — including the FY26 Philadelphia wage-tax rate revision effective July 1, 2025, any PA UC rate-schedule re-issuance, and any TCC-level tax-collector successor designation — must be confirmed before this skill is used to produce a live deliverable.

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
