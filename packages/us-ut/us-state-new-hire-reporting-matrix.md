---
name: us-state-new-hire-reporting-matrix
description: Tier 2 US federal-level reference skill providing the 50-state matrix of new-hire reporting requirements under PRWORA §453A. Covers tax year 2025 including each state's reporting agency and online portal URL, the 20-day federal deadline plus state variations, multistate employer single-state designation election under §453A(b)(2), independent contractor reporting requirements (CA DE 542, NY, NJ, MA, KY, FL state-specific), penalty ranges from $25 to $500 per missed report, conditional and rehire reporting rules, and integration with major payroll systems (Gusto, ADP, Paychex, QuickBooks Payroll).
jurisdiction: US
tax_year: 2025
last_updated: 2026-07-13
reviewed_by: James Wallach
review_status: current
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# US State New Hire Reporting Matrix

## US 50-State New-Hire Reporting Matrix

## 1. Scope

- **Governing statute** — Employer new-hire reporting obligations under the Personal Responsibility and Work Opportunity Reconciliation Act of 1996 (PRWORA), Pub. L. 104-193, codified principally at 42 U.S.C. §653a (commonly referenced as "§453A" of the Social Security Act). PRWORA requires every employer to report each newly hired or rehired employee to a designated State Directory of New Hires (SDNH) within 20 days of hire. The SDNH transmits the data to the federal National Directory of New Hires (NDNH) operated by the Office of Child Support Enforcement (OCSE), which uses it to enforce child support orders, detect unemployment-insurance fraud, locate workers for income-withholding orders, and identify ineligible recipients of public assistance, SNAP, and Medicaid.  _(PRWORA, Pub. L. 104-193; 42 U.S.C. §653a)_

The scope includes:

- The federal PRWORA baseline (20-day deadline, required data elements, multistate employer election under §453A(b)(2)).
- State-specific implementations for all 50 states and the District of Columbia, including agency name, online portal, deadline, format, contractor reporting rules, penalty range, rehire rule, and notable quirks.
- Independent contractor reporting under state law (notably California EDD DE 542 for contractors paid $600 or more, New York for $2,500+, New Jersey, Massachusetts, Kentucky, and Florida variations).
- Penalty calculation methodology, ranging from $25 per missed report (most states' baseline) to $500 per missed report where conspiracy with the employee to avoid reporting is proved.
- Payroll software integration patterns for Gusto, ADP, Paychex, and QuickBooks Online Payroll, all of which automate new-hire reporting once the new-hire wizard is completed.
- Worked examples illustrating common compliance traps.

Out of scope: federal contractor reporting on Form W-2 / Form W-4 (covered separately), Form I-9 employment eligibility verification (a separate DHS regime under 8 U.S.C. §1324a), unemployment insurance quarterly wage reporting, and state-level E-Verify mandates. Multistate employer state income tax nexus questions are out of scope and are handled by `us-multi-state-residency-and-allocation` and `us-pl-86-272-income-tax-nexus`.

> **AUDIT FLASH POINT:** New-hire reporting is one of the most consistently missed compliance items for small employers. The agency that enforces it (a child-support division, not the IRS or DOL) is unfamiliar to most taxpayers, and the data does not appear on any return the reviewer normally signs. Always verify in the engagement checklist that new-hire reporting is configured before the first payroll runs.

### 2.1 Statutory basis

- **Statutory basis** — The governing federal statute is section 453A of the Social Security Act (42 U.S.C. §653a), enacted by §313 of PRWORA (Pub. L. 104-193, August 22 1996). It is implemented by federal regulations at 45 C.F.R. §303.108 and operational guidance from the federal Office of Child Support Enforcement (OCSE), now rebranded as the Office of Child Support Services (OCSS) within the U.S. Department of Health and Human Services Administration for Children and Families.  _(42 U.S.C. §653a; Pub. L. 104-193 §313; 45 C.F.R. §303.108)_

### 2.2 Who must report

- **Who must report** — Every "employer" as defined in §3401(d) of the Internal Revenue Code must report. This includes: - Sole proprietors who hire at least one W-2 employee. - Single-member LLCs disregarded for federal tax that hire W-2 employees (reported under the owner's SSN or the LLC's EIN, depending on payroll setup). - Partnerships, S corps, C corps, nonprofits, governmental entities. - Household employers who hire nannies, housekeepers, gardeners (Schedule H filers). - Agricultural employers, religious organizations, and tribal employers. The reporting obligation is triggered by the W-2 employer-employee relationship, regardless of whether the employee is full-time, part-time, temporary, seasonal, or probationary. There is no minimum-hours threshold and no minimum-wage threshold.  _(IRC §3401(d))_

### 2.3 Federal data elements

- **Federal data elements (required)** — 1. Employee's full legal name (first, middle initial, last). 2. Employee's home address. 3. Employee's Social Security Number (SSN). 4. Employee's date of hire (first day of paid service). 5. Employer's name. 6. Employer's address. 7. Employer's Federal Employer Identification Number (FEIN/EIN).  _(Federal statute (PRWORA §453A))_
- **OCSS recommended optional elements (mandatory in most states)** — - Employee's date of birth (mandatory in most states). - Employee's state of hire. - Whether dependent health insurance is available. - Date health insurance becomes available.  _(OCSS guidance)_

### 2.4 Federal deadline

- **Federal new-hire reporting deadline** — 20 days from the date of hire, or in the case of an employer that transmits reports magnetically or electronically, by two monthly transmissions not less than 12 days nor more than 16 days apart. States may set a shorter deadline (and many have), but cannot set a longer one. days  _(42 U.S.C. §653a(b)(2)(A))_

### 2.5 Federal penalties

- **Federal penalty, no conspiracy** — $25 per unreported new hire (civil monetary penalty), where there is no conspiracy. USD per unreported new hire  _(§453A(d))_
- **Federal penalty, conspiracy** — $500 per unreported new hire where there is a conspiracy between the employer and the employee to fail to file or to file a false report. USD per unreported new hire  _(§453A(d))_
- **Penalty caps as floors** — These penalty caps are floors — states may impose higher penalties under state law but most have adopted the federal $25 / $500 schedule.  _(§453A(d))_

### 3.1 The election

- **Multistate single-state election** — Section 453A(b)(2) of the Social Security Act allows an employer that has employees in two or more states to designate one of those states as the single state to which it will transmit all new-hire reports, regardless of where each new hire actually works. This election is made by filing the "Multistate Employer Notification Form for New Hire Reporting" with the federal OCSS (not with any single state).  _(§453A(b)(2))_

### 3.2 Mechanics

- **Election mechanics** — The employer: 1. Selects one state in which it has employees. 2. Files the federal multistate notification (online at the OCSS Employer Services portal: <https://www.acf.hhs.gov/css/employers/employer-responsibilities/new-hire-reporting>) listing all states in which it has employees. 3. Transmits all new-hire reports to the designated state, formatted to that state's data spec, by that state's deadline (which must be no later than the federal 20-day maximum). 4. The designated state's SDNH transmits the data to the federal NDNH, which redistributes it to the relevant child-support agencies in each work state.  _(§453A(b)(2))_

### 3.3 When to elect

The election is most useful for:

- Multi-location employers with payroll consolidated in one state.
- Employers using a single PEO or HRIS that natively reports to one state.
- Employers in states with the most permissive contractor rules (selecting a state that does NOT require independent contractor reporting can simplify compliance — but does NOT eliminate the contractor reporting obligation under the law of the state where the contractor works, since the election is for employee reporting only).

> **AUDIT FLASH POINT:** Multi-state employers that miss the single-state designation default to the rule that they must file in **every** state where they hire. Reviewers should always confirm, for any client with employees in more than one state, whether the federal multistate notification has been filed and which state was designated. The risk of duplicate filings is annoying; the risk of missed filings is a $25-per-employee penalty per state.

### 3.4 What the election does NOT do

- **Limits of the election** — - Does not relieve the employer of state income tax withholding registration in each work state. - Does not change the state to which unemployment insurance contributions are paid. - Does not affect Form W-2 state reporting. - Does not cover independent contractor reporting (which is a state-law construct not governed by PRWORA — see §4).

## 4. Independent Contractor Reporting

- **PRWORA does not cover contractors** — PRWORA itself does not require reporting of independent contractors. However, several states have enacted laws extending new-hire reporting (or a parallel regime) to independent contractors paid above a state-specific threshold. This is one of the most commonly overlooked compliance items because the federal baseline does not flag it.

### 4.1 California — Form DE 542

- **California contractor reporting requirement** — California requires service-recipients (the payor) to report any independent contractor paid $600 or more within a calendar year to the California Employment Development Department (EDD) on Form DE 542 within 20 days of the earlier of (a) the date the contract is executed or (b) the date $600 in cumulative payments is reached during the calendar year. USD  _(California Unemployment Insurance Code §1088.8)_
- **California DE 542 penalty** — $24 per missed report; $490 if conspiracy with the contractor. USD per missed report  _(California Unemployment Insurance Code §1088.8)_

- Portal: <https://edd.ca.gov/en/payroll_taxes/new_hire_reporting/>
- Form: DE 542 (paper) or e-Services for Business (online).

### 4.2 New York

- **New York contractor reporting requirement** — New York requires reporting of contractors expected to earn $2,500 or more in any calendar year, within 20 days of the earlier of contract execution or first payment. USD  _(NY Tax Law §171-h)_
- **New York contractor penalty** — $20 per failure; $450 if conspiracy. USD per failure  _(NY Tax Law §171-h)_

Portal: <https://www.nynewhire.com>

### 4.3 New Jersey

- **New Jersey contractor reporting requirement** — New Jersey requires reporting of independent contractors (defined under state law) within 20 days, with no minimum-dollar threshold for the contractor category once the relationship exists for compensation.  _(N.J.S.A. 2A:17-56.61)_
- **New Jersey contractor penalty** — $25 per failure. USD per failure  _(N.J.S.A. 2A:17-56.61)_

Portal: <https://www.nj-newhire.com>

### 4.4 Massachusetts

- **Massachusetts contractor reporting requirement** — Massachusetts requires reporting of independent contractors paid more than $600 in a calendar year within 14 days. USD  _(M.G.L. c. 62E §2 (post-2008 amendments))_

Portal: <https://www.ma-newhire.com>

### 4.5 Kentucky

- **Kentucky contractor reporting requirement** — Kentucky requires reporting of independent contractors expected to be paid $600 or more for services, within 20 days. USD  _(KRS 405.435)_

Portal: <https://newhire-reporting.com/KY-Newhire/>

### 4.6 Florida (limited)

- **Florida limited contractor reporting** — Florida does not require general contractor reporting, but service-recipients that pay independent contractors $600 or more must report contractors who are subject to existing child-support obligations on request from the Department of Revenue. Practically, Florida is not a §4 contractor-reporting state, but agency confirmation orders may attach.

> **AUDIT FLASH POINT:** California EDD DE 542 contractor reporting is missed in roughly one out of every two new freelance-developer clients we review. The penalty per missed contractor report is small, but the cumulative penalty for a software company with 30 contractors over three years can exceed $2,000 — and the EDD uses the DE 542 database to issue 1099 cross-matching audits. Always verify DE 542 filings for any California client paying contractors.

### 4.7 Other states with contractor reporting features

- **Ohio contractor reporting** — Ohio: contractors paid $2,500+ in a year — reporting required, but enforcement is limited. USD
- **Connecticut contractor reporting** — Connecticut: voluntary contractor reporting accepted; not mandatory.
- **Iowa contractor reporting** — Iowa: contractors who are subject to a wage-withholding order — limited scope.
- **All other states** — All other states do not require contractor reporting under PRWORA-parallel state law.

## 5. 50-State + DC Matrix

The matrix below summarizes for each of the 50 states and the District of Columbia: (1) reporting agency and portal; (2) filing deadline; (3) multistate election compatibility; (4) contractor reporting requirement; (5) reporting format (online portal / form / both); (6) penalty range; (7) rehire and conditional reporting rule; (8) notable quirks.

A "rehire" is generally defined under federal regulations as an employee returning to work for a former employer after a separation of at least 60 consecutive days. Many states have adopted this rule by reference; some (notably Illinois pre-2020) used different separation thresholds.

### 5.1 Matrix table

**50-State + DC New-Hire Reporting Matrix**  _(5.1 Matrix table)_

| # | State | Agency | Portal | Deadline | Contractor reporting? | Format | Penalty (no conspiracy / conspiracy) | Rehire rule | Notable quirks |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Alabama | AL Dept. of Labor New Hire Unit | newhire-reporting.com/AL-Newhire/ | 7 days | No | Online + form | $25 / $500 | 60-day separation | One of the shortest deadlines (7 days) |
| 2 | Alaska | AK Child Support Services Division | newhire-reporting.com/AK-Newhire/ | 20 days | No | Online + form | $25 / $500 | 60 days | Federal default |
| 3 | Arizona | AZ New Hire Reporting Center | az-newhire.com | 20 days | No | Online + form | $25 / $500 | 60 days | State imposes additional $500 for failure to update |
| 4 | Arkansas | AR New Hire Reporting Center | ar-newhire.com | 14 days | No | Online + form | $25 / $500 | 60 days | 14-day deadline (shorter than federal) |
| 5 | California | CA Employment Development Dept. (EDD) | edd.ca.gov/en/payroll_taxes/new_hire_reporting/ | 20 days | **Yes — DE 542, $600+** | Online (e-Services) + form (DE 34, DE 542) | $24 / $490 | 60 days | Two-form regime: DE 34 employees + DE 542 contractors |
| 6 | Colorado | CO State Directory of New Hires | newhire.state.co.us | 20 days | No | Online + form | $25 / $500 | 60 days | Penalty doubled for second offense |
| 7 | Connecticut | CT Dept. of Labor | ctnewhires.com | 20 days | Voluntary | Online + form | $25 / $500 | 60 days | Accepts (but does not require) contractor reports |
| 8 | Delaware | DE Division of Child Support Services | newhire-reporting.com/DE-Newhire/ | 20 days | No | Online + form | $25 / $500 | 60 days | Federal default |
| 9 | DC | DC Child Support Services Division | newhire-reporting.com/DC-Newhire/ | 20 days | No | Online + form | $25 / $500 | 60 days | Federal default |
| 10 | Florida | FL Dept. of Revenue Child Support Program | servicesforemployers.floridarevenue.com | 20 days | Limited (on order) | Online + form | $25 / $500 | 60 days | Online-only filing required for employers with 250+ employees |
| 11 | Georgia | GA New Hire Reporting Program | ga-newhire.com | 10 days | No | Online + form | $25 / $500 | 60 days | 10-day deadline (significantly shorter) |
| 12 | Hawaii | HI Child Support Enforcement Agency | newhire-reporting.com/HI-Newhire/ | 20 days | No | Online + form | $25 / $500 | 60 days | Federal default |
| 13 | Idaho | ID Dept. of Labor | labor.idaho.gov/dnn/Businesses/New-Hire-Reporting | 20 days | No | Online + form | $25 / $500 | 60 days | Federal default |
| 14 | Illinois | IL Dept. of Employment Security (IDES) | ides.illinois.gov/employer-resources/taxes-reporting/new-hire-reporting.html | 20 days | No | Online + form | $15 per offense after 3rd | 60 days | Penalty schedule deviates: 3 strikes then $15 each |
| 15 | Indiana | IN New Hire Reporting Center | in-newhire.com | 20 days | No | Online + form | $25 / $500 | 60 days | Federal default |
| 16 | Iowa | IA Centralized Employee Registry | iowachildsupport.gov/employers/CER | 15 days | Limited (wage-withholding) | Online + form | $25 / $500 | 60 days | 15-day deadline |
| 17 | Kansas | KS New Hire Reporting Center | ks-newhire.com | 20 days | No | Online + form | $25 / $500 | 60 days | Federal default |
| 18 | Kentucky | KY New Hire Reporting Center | newhire-reporting.com/KY-Newhire/ | 20 days | **Yes — $600+** | Online + form | $25 / $500 | 60 days | Contractor reporting required (often missed) |
| 19 | Louisiana | LA Directory of New Hires | newhire-reporting.com/LA-Newhire/ | 20 days | No | Online + form | $25 / $500 | 60 days | Federal default |
| 20 | Maine | ME Division of Support Enforcement | newhire-reporting.com/ME-Newhire/ | 7 days | No | Online + form | $200 max per quarter | 60 days | 7-day deadline; capped quarterly penalty |
| 21 | Maryland | MD New Hire Registry | newhire-reporting.com/MD-Newhire/ | 20 days | No | Online + form | $25 / $500 | 60 days | Federal default |
| 22 | Massachusetts | MA Dept. of Revenue Child Support | ma-newhire.com | 14 days | **Yes — $600+** | Online + form | $25 / $500 | 60 days | Contractor reporting required; 14-day deadline |
| 23 | Michigan | MI New Hires Operations Center | mi-newhire.com | 20 days | No | Online + form | $25 / $500 | 60 days | Federal default |
| 24 | Minnesota | MN New Hire Reporting Center | mn-newhire.com | 20 days | No | Online + form | $25 / $500 | 60 days | Federal default |
| 25 | Mississippi | MS Dept. of Human Services | ms-newhire.com | 15 days | No | Online + form | $25 / $500 | 60 days | 15-day deadline |
| 26 | Missouri | MO Family Support Division | mo-newhire.com | 20 days | No | Online + form | $25 / $350 | 60 days | Lower conspiracy penalty ($350) |
| 27 | Montana | MT New Hire Reporting Program | newhire-reporting.com/MT-Newhire/ | 20 days | No | Online + form | $25 / $500 | 60 days | Federal default |
| 28 | Nebraska | NE State Directory of New Hires | newhire-reporting.com/NE-Newhire/ | 20 days | No | Online + form | $25 / $500 | 60 days | Federal default |
| 29 | Nevada | NV Dept. of Employment, Training and Rehabilitation | newhire-reporting.com/NV-Newhire/ | 20 days | No | Online + form | $25 / $500 | 60 days | Federal default |
| 30 | New Hampshire | NH New Hires Program | nh-newhire.com | 20 days | No | Online + form | $25 / $500 | 60 days | Federal default |
| 31 | New Jersey | NJ New Hire Reporting Center | nj-newhire.com | 20 days | **Yes — all contractors** | Online + form | $25 / $500 | 60 days | Broad contractor reporting (no $ threshold) |
| 32 | New Mexico | NM New Hires Directory | nm-newhire.com | 20 days | No | Online + form | $25 / $500 | 60 days | Federal default |
| 33 | New York | NY New Hire Online Reporting Center | nynewhire.com | 20 days | **Yes — $2,500+** | Online + form | $20 / $450 | 60 days | Contractor reporting at $2,500 threshold; lower penalty |
| 34 | North Carolina | NC Directory of New Hires | ncnewhires.com | 20 days | No | Online + form | $25 / $500 | 60 days | Federal default |
| 35 | North Dakota | ND State Directory of New Hires | nd-newhire.com | 20 days | No | Online + form | $25 / $500 | 60 days | Federal default |
| 36 | Ohio | OH New Hire Reporting Center | oh-newhire.com | 20 days | Limited ($2,500+) | Online + form | $25 / $500 | 60 days | Soft contractor reporting (not strictly enforced) |
| 37 | Oklahoma | OK New Hire Reporting Center | ok-newhire.com | 20 days | No | Online + form | $25 / $500 | 60 days | Federal default |
| 38 | Oregon | OR Dept. of Justice Division of Child Support | oregonchildsupport.gov/employers | 20 days | No | Online + form | $25 / $500 | 60 days | Federal default |
| 39 | Pennsylvania | PA Child Support New Hire Reporting | cwds.pa.gov/ | 20 days | No | Online + form | $25 / $500 | 60 days | Federal default |
| 40 | Rhode Island | RI Office of Child Support Services | ri-newhire.com | 14 days | No | Online + form | $20 / $500 | 60 days | 14-day deadline |
| 41 | South Carolina | SC Dept. of Social Services | newhire.sc.gov | 20 days | No | Online + form | $25 / $500 | 60 days | Federal default |
| 42 | South Dakota | SD Dept. of Labor and Regulation | sdnewhire.com | 20 days | No | Online + form | $25 / $500 | 60 days | Federal default |
| 43 | Tennessee | TN New Hire Reporting Program | tn-newhire.com | 20 days | No | Online + form | $20 / $400 | 60 days | Lower penalty schedule |
| 44 | Texas | TX Office of the Attorney General | employer.oag.state.tx.us | 20 days | No | Online + form | $25 / $500 | 60 days | Multistate-employer-friendly (popular designation choice) |
| 45 | Utah | UT Dept. of Workforce Services | jobs.utah.gov/employer/business/newhire.html | 20 days | No | Online + form | $25 / $500 | 60 days | Federal default |
| 46 | Vermont | VT Dept. for Children and Families | vtnewhire.com | 10 days | No | Online + form | $25 / $500 | 60 days | 10-day deadline |
| 47 | Virginia | VA New Hire Reporting Center | va-newhire.com | 20 days | No | Online + form | $25 / $500 | 60 days | Federal default |
| 48 | Washington | WA Dept. of Social and Health Services | secure.dshs.wa.gov/ESA/NHRPWeb/ | 20 days | No | Online + form | $25 / $500 | 60 days | Federal default |
| 49 | West Virginia | WV Bureau for Child Support Enforcement | wv-newhire.com | 14 days | No | Online + form | $25 / $500 | 60 days | 14-day deadline |
| 50 | Wisconsin | WI New Hire Reporting Center | wi-newhire.com | 20 days | No | Online + form | $25 / $500 | 60 days | Federal default |
| 51 | Wyoming | WY New Hire Reporting Center | newhire-reporting.com/WY-Newhire/ | 20 days | No | Online + form | $25 / $500 | 60 days | Federal default |

### 5.2 Deadlines shorter than the federal 20-day maximum

- **Shorter-than-federal deadline jurisdictions** — The following 11 jurisdictions impose deadlines shorter than the federal 20-day default. Reviewers should flag these for clients with operations in any of them: - **7 days:** Alabama, Maine. - **10 days:** Georgia, Vermont. - **14 days:** Arkansas, Massachusetts, Rhode Island, West Virginia. - **15 days:** Iowa, Mississippi. - All other 40 states and DC: 20 days.

### 5.3 Contractor-reporting states summary

**Contractor-reporting states summary**  _(5.3 Contractor-reporting states summary)_

| State | Threshold | Authority | Form/portal |
| --- | --- | --- | --- |
| California | $600+ in calendar year | CA UIC §1088.8 | DE 542 / e-Services |
| Massachusetts | $600+ in calendar year | M.G.L. c. 62E §2 | ma-newhire.com |
| Kentucky | $600+ for services | KRS 405.435 | newhire-reporting.com/KY-Newhire/ |
| New York | $2,500+ in calendar year | NY Tax Law §171-h | nynewhire.com |
| New Jersey | All contractors | N.J.S.A. 2A:17-56.61 | nj-newhire.com |
| Ohio | $2,500+ in year (soft) | ORC §3121.892 | oh-newhire.com |

### 6.1 Standard schedule

- **Standard penalty schedule** — Most states adopt the federal $25 / $500 schedule. The penalty is per missed report, not per pay period. That is, a single employee who is never reported is a single $25 penalty.

### 6.2 Variations

- **State penalty variations** — - **Illinois:** does not charge per-report; instead allows three free "warnings" per calendar year and then charges $15 per subsequent violation. Cumulative cap of approximately $7,500 per year. - **Maine:** capped at $200 per calendar quarter regardless of the number of unreported hires. - **Missouri:** lower conspiracy penalty ($350 instead of $500). - **Tennessee:** lower schedule ($20 / $400). - **New York:** lower schedule ($20 / $450). - **California:** $24 / $490 (statutory cap slightly under federal). - **Rhode Island:** $20 base / $500 conspiracy.

### 6.3 Statute of limitations

- **Statute of limitations** — The federal statute (§453A) does not contain its own SOL, so most states apply their general civil-action SOL (typically 3 to 6 years) to enforcement actions for missed new-hire reports. In practice, enforcement is rare and usually occurs only after a child-support audit or unemployment-insurance fraud investigation reveals undisclosed employees.  _(§453A)_

### 6.4 Cumulative penalty exposure example

A multistate employer with 30 W-2 hires in 2024 across 5 states, none reported, faces:

- 30 × $25 = **$750** in baseline civil penalties.
- If any conspiracy was alleged (e.g., paying under-the-table to evade child-support garnishment), the per-report penalty rises to $500: 30 × $500 = **$15,000**.
- If the employer is in California with 10 of those 30 also being independent contractors not reported on DE 542: an additional 10 × $24 = **$240**.

The dollar exposure is small relative to other payroll-tax exposures, but a finding of conspiracy can also trigger child-support garnishment recovery actions, FUTA credit denial review, and state unemployment insurance audit.

## 7. Payroll Software Integration

The big four payroll-services platforms — Gusto, ADP RUN, Paychex Flex, and QuickBooks Online Payroll — all automate state new-hire reporting as a standard feature. Reviewers should verify, during onboarding, that the feature is enabled and that the designated reporting state matches the employer's intended PRWORA election (or default work-state).

### 7.1 Gusto

- **Gusto integration** — Gusto automatically files new-hire reports in all 50 states and DC for any W-2 employee added through the New Hire wizard. The integration includes: - Auto-filing within state deadlines. - Independent contractor reporting in CA, NY, NJ, MA, KY (Gusto's contractor onboarding flow triggers DE 542 / state contractor reports where applicable). - A new-hire reporting log accessible at Gusto → Payroll → Compliance → New Hire Reports. Gusto charges no additional fee for this filing. Multistate clients should verify the "primary state" setting under company profile.

### 7.2 ADP (RUN, Workforce Now)

- **ADP integration** — ADP files new-hire reports for all employees onboarded through its system. ADP supports the federal multistate employer election and will, on request, designate one state for all clients. For independent contractor reporting in CA, ADP's Workforce Now system files DE 542 automatically; ADP RUN (the small-business product) does NOT, and requires manual filing by the client. This is a common gotcha for ADP RUN users.

### 7.3 Paychex (Flex, Paychex Go)

- **Paychex integration** — Paychex Flex files new-hire reports in all states for W-2 employees. Contractor reporting is not automatic in Paychex Flex; the user must manually file DE 542 / NY / MA / KY equivalents through the state portal.

### 7.4 QuickBooks Online Payroll

- **QBO Payroll integration** — QBO Payroll automatically files new-hire reports for W-2 employees in all 50 states. Independent contractor reporting is not automated in QBO; users must file CA DE 542 / NY / NJ / MA / KY contractor reports through the state portals manually.

### 7.5 Reviewer checklist

- **Onboarding reviewer checklist** — During onboarding of any new client with employees, the reviewer should: 1. Confirm the payroll platform in use. 2. Confirm the new-hire reporting state is correctly set (single state for multistate-election employers, otherwise each work state). 3. Confirm whether the platform handles contractor reporting (Gusto: yes; ADP Workforce Now: yes; ADP RUN: no; Paychex: no; QBO: no). 4. For non-automating platforms in CA/NY/NJ/MA/KY, confirm manual contractor-reporting workflow. 5. Pull the new-hire reporting log for the prior 12 months and reconcile to the W-2 list.

### Example 8.1 — Small business, 5 employees in one state

**Facts.** Acme Bakery LLC is a single-member LLC organized in Texas and operating exclusively in Austin, Texas. In March 2025, Acme hires 5 W-2 employees: 2 bakers, 2 cashiers, 1 driver. Payroll runs through Gusto.

**Analysis.**

- Texas is the work state for all 5 employees. No multistate election is needed.
- Federal deadline is 20 days. Texas adopts the federal default (20 days).
- Required data elements: name, address, SSN, hire date, employer EIN, employer name, employer address.
- Gusto auto-files all 5 reports to the Texas Office of the Attorney General's Employer New Hire Reporting Operations Center within 20 days.
- No independent contractor reports are required in Texas.

**Compliance status:** Fully compliant, no manual action required. Reviewer should confirm in Gusto → Compliance → New Hire Reports that all 5 reports show "Filed."

**Reviewer note:** The TX OAG portal is also the popular designation choice for multistate employers because of Texas's friendly employer interface and no contractor reporting requirement.

### Example 8.2 — Multistate employer with 50 hires across 8 states using single-state election

**Facts.** TechCo Inc. is a Delaware C corp with employees in 8 states: CA (15), NY (8), TX (10), FL (5), WA (4), MA (3), CO (3), IL (2), for 50 total hires in 2025. Payroll runs through ADP Workforce Now.

**Analysis (with election).**

- TechCo files the OCSS Multistate Employer Notification designating **Texas** as its single reporting state.
- All 50 new-hire reports are transmitted to the Texas SDNH within 20 days of each hire.
- Texas SDNH forwards each report to the federal NDNH, which redistributes to the work-state child-support agencies.
- ADP Workforce Now is configured to file to TX for all 50 employees.

**However — contractor reporting is NOT covered by the election.** Independently, TechCo must file:

- **CA DE 542** for any contractor paid $600+ during 2025 by the California payor entity. (Note: only the CA-based service-recipient is subject; if TechCo's CA office contracts are signed by the TX entity and paid centrally from TX, a fact-intensive nexus analysis is required.)
- **NY** contractor report for any contractor expected to earn $2,500+.
- **MA** contractor report for any contractor paid $600+ (14-day deadline).

**Analysis (without election — counterfactual).** If TechCo had failed to file the multistate notification, it would default to filing in each of 8 states. With 50 hires unreported across 8 jurisdictions, exposure is 50 × $25 = $1,250 in base civil penalties, plus potential conspiracy uplift if challenged. The election eliminates this exposure entirely for the employee reports.

**Reviewer action:** Confirm the OCSS multistate notification was filed (a printed confirmation should be in the client's compliance binder). Confirm ADP designated state matches. Separately confirm CA DE 542, NY, and MA contractor reporting for any 1099 payments.

> **AUDIT FLASH POINT:** This is the most common multistate audit finding — the election covers W-2 employees but NOT independent contractors. A multistate employer with the election in place is still on the hook for state-by-state contractor reporting.

### Example 8.3 — 1099 contractor reporting trap for CA payor

**Facts.** Jane Doe operates a sole-proprietor freelance design agency in San Francisco, CA. In 2025, she contracts with 8 subcontractor designers, paying each more than $600 over the year. She does not have any W-2 employees. She files 1099-NEC for each contractor at year-end. She does NOT file any DE 542 forms.

**Analysis.**

- California Unemployment Insurance Code §1088.8 requires service-recipients (which includes sole proprietors) to file Form DE 542 for any independent contractor paid $600 or more in a calendar year, within 20 days of the earlier of contract execution or reaching the $600 cumulative threshold.
- Jane is a "service-recipient" under §1088.8 because she pays for personal services.
- Filing 1099-NEC at year-end does NOT satisfy the DE 542 requirement, which is a real-time reporting obligation transmitted to the California Child Support Services Division (via EDD).
- Penalty exposure: 8 × $24 = **$192** in baseline civil penalty. If EDD finds Jane intentionally avoided filing to help a contractor evade a child-support obligation, the per-report penalty rises to $490, total **$3,920**.
- More important than the dollar penalty: the EDD uses DE 542 data to cross-match against 1099-NEC filings. A discrepancy (1099-NEC filed but no DE 542) is a common trigger for an EDD worker-classification audit, where the agency may attempt to reclassify the contractors as employees and assess back UI and ETT tax under AB 5 / Dynamex (PUC §2750.3).

**Compliance remediation.** Jane should file DE 542 for all 8 contractors immediately (late but mitigates further exposure), and going forward should file within 20 days of the earlier of contract execution or hitting $600. QBO Payroll does not automate this, so a manual workflow is required.

> **AUDIT FLASH POINT:** CA DE 542 contractor reporting is missed by roughly half of new freelance/agency clients. The 1099-NEC at year-end is NOT a substitute. Always add DE 542 to the engagement checklist for California-resident service businesses.

## 9. Reviewer Output Checklist

- **Reviewer output checklist** — Before signing off on any engagement with employees or independent contractors, the reviewer should confirm: - [ ] Employer is registered with at least one state's SDNH (or has filed federal multistate notification with designated state). - [ ] If multistate employer with operations in 2+ states: federal multistate notification on file; designated state matches payroll configuration. - [ ] Payroll platform (Gusto / ADP / Paychex / QBO) is configured to auto-file new-hire reports. - [ ] New-hire reporting log shows all W-2 hires for the engagement period as Filed. - [ ] If client is in CA, NY, NJ, MA, KY: contractor reporting workflow is in place and DE 542 / state equivalents are filed for $600+ (or state-specific threshold) contractors. - [ ] Rehire reporting: any employee returning after 60+ days has been re-reported. - [ ] Conditional reporting: any conditional or contingent hires (e.g., hire pending background check) are reported only after first day of paid service, per §453A(b)(1). - [ ] No deadline state (AL, ME = 7 days; GA, VT = 10 days; AR, MA, RI, WV = 14 days; IA, MS = 15 days) is missed by a payroll platform's default 20-day cadence.  _(§453A(b)(1))_

## 10. References and Authorities

- **References and authorities list** — - 42 U.S.C. §653a (Social Security Act §453A) — federal new-hire reporting statute. - Pub. L. 104-193 (PRWORA), §313 (1996) — enacting legislation. - 45 C.F.R. §303.108 — federal implementing regulation. - OCSS Employer Services portal: <https://www.acf.hhs.gov/css/employers/employer-responsibilities/new-hire-reporting>. - California Unemployment Insurance Code §1088.8 — CA contractor reporting. - N.Y. Tax Law §171-h — NY contractor reporting. - N.J.S.A. 2A:17-56.61 — NJ contractor reporting. - M.G.L. c. 62E §2 — MA contractor reporting. - KRS 405.435 — KY contractor reporting. - Ohio Revised Code §3121.892 — OH contractor reporting (soft). - IRS Pub. 15 (Circular E) — referenced for employer definition (§3401(d)).

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
