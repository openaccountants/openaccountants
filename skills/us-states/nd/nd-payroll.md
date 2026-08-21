---
name: nd-payroll
description: Use this skill whenever asked about North Dakota employer payroll compliance — state income tax withholding, Form 306 quarterly returns, Form 307 annual W-2 reconciliation, NDW-R reciprocity for Minnesota and Montana residents, SUTA / unemployment insurance through Job Service ND, new-hire reporting, and Workforce Safety & Insurance (WSI) workers' compensation. Trigger on phrases like "ND payroll", "North Dakota withholding", "Form 306", "NDW-R", "Job Service ND", "WSI", "Fargo employer", "Minnesota commuter".
jurisdiction: US-ND
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# ND Payroll

## North Dakota Employer Payroll Compliance Skill

> **Scope.** This skill covers North Dakota employer payroll obligations for a business with employees performing services in North Dakota during tax year 2025 (returns and deposits filed 2025–2026). Covers: ND personal income tax (PIT) withholding under N.D.C.C. § 57-38-59; Form 306 quarterly withholding returns; Form 307 annual W-2/1099 transmittal; Form NDW-M (state W-4); Form NDW-R (MN/MT reciprocity exemption); ND State Unemployment Tax (SUTA) under Job Service North Dakota; new-hire reporting to the ND Child Support Division; and the WSI workers' compensation monopoly. Federal payroll (Form 941, Form 940, FICA, FUTA, federal W-4, federal new-hire reporting, federal Form W-2 filing with SSA) is out of scope — see the federal payroll skills.
>
> **Quality tier.** Tier 2 content skill. AI-drafted; awaiting verifier sign-off. All employer-side outputs must be reviewed by a qualified ND payroll professional before filing or remitting. `[VERIFY:]` markers flag figures that must be re-confirmed against current ND Tax Commissioner / Job Service ND / WSI publications for the applicable period.

## Section 1: Metadata

**Metadata table**

| Field | Value |
| --- | --- |
| Tax type | Employer payroll (state withholding + SUTA + workers' comp) |
| Jurisdiction | North Dakota (US-ND) |
| Tax year | 2025 |
| Primary forms | Form 306 (quarterly), Form 307 (annual), NDW-M (state W-4), NDW-R (reciprocity), SFN 41263 (UI quarterly contribution & wage report) |
| Withholding statute | N.D.C.C. § 57-38-59 |
| Unemployment statute | N.D.C.C. Chapter 52-04 |
| Workers' compensation statute | N.D.C.C. Title 65 |
| Withholding authority | ND Office of State Tax Commissioner |
| Unemployment authority | Job Service North Dakota (JSND) |
| Workers' comp authority | Workforce Safety & Insurance (WSI) — monopolistic state fund |
| Withholding portal | ND Taxpayer Access Point (TAP): https://apps.nd.gov/tax/tap |
| UI portal | UI EASY: https://www.jobsnd.com |
| New-hire reporting | ND Child Support Division — within 20 days |
| Filing deadlines | Form 306: last day of month following quarter end; Form 307: January 31 |

### Sources consulted

- N.D.C.C. § 57-38-59 — Withholding from compensation. ndlegis.gov.
- ND Office of State Tax Commissioner, *Income Tax Withholding Rates & Instructions for Wages Paid in 2025* (the "2025 Withholding Booklet"): https://www.tax.nd.gov/sites/www/files/documents/misc-discuss-folder/Final_2025%20Income%20Tax%20Withholding%20Rates%20%20Instructions.pdf
- ND Office of State Tax Commissioner, Form 306 (Income Tax Withholding Return) and instructions: https://www.tax.nd.gov/sites/www/files/documents/forms/business/it-withholding/form-306-web.pdf
- ND Office of State Tax Commissioner, Form NDW-R (Reciprocity Exemption from Withholding for Qualifying MN and MT Residents Working in North Dakota): https://www.tax.nd.gov/sites/www/files/documents/forms/business/ndwrfillable.pdf
- ND Office of State Tax Commissioner, *Income Tax Withholding & Information Returns Guideline*: https://www.tax.nd.gov/sites/www/files/documents/guidelines/business/it-withhold/income-tax-withholding-information-returns-guideline.pdf
- ND Office of State Tax Commissioner, *Income Tax Withholding Deadlines*: https://www.tax.nd.gov/news/resources/tax-deadlines/income-tax-withholding-deadlines
- HB 1158 (68th Legislative Assembly, 2023) — text and fiscal note: https://ndlegis.gov/assembly/68-2023/regular/documents/23-0351-02000.pdf
- Job Service North Dakota, *2025 Unemployment Insurance Tax Rate Schedules*: https://www.jobsnd.com/sites/www/files/documents/jsnd-documents/uitaxrateschedules2025.pdf
- Job Service North Dakota, *Employer's Handbook on the Unemployment Insurance Program in North Dakota*: https://www.library.nd.gov/statedocs/JobService/jsnd4036.pdf
- 1976 Reciprocity Agreement between ND and MT Departments of Revenue, appendix to interim committee materials.
- Bloomberg Tax, *North Dakota Releases 2025 Withholding Methods*.
- PRWORA § 453A (42 U.S.C. § 653a) — new-hire reporting.
- N.D.C.C. § 34-14-03 — payment of wages upon separation.
- WSI employer information: https://www.workforcesafety.com

## Section 2: Quick reference

**Quick reference table**

| Item | Value |
| --- | --- |
| ND PIT bracket 1 (TY 2025, single) | 0% on first $47,150 [VERIFY: 2025 booklet thresholds] |
| ND PIT bracket 2 (TY 2025, single) | 1.95% on $47,150 – $238,200 [VERIFY: exact threshold] |
| ND PIT bracket 3 (TY 2025, single) | 2.50% above $238,200 [VERIFY: exact threshold] |
| Supplemental wage rate (TY 2025) | 1.5% |
| Form 306 due dates | April 30, July 31, October 31, January 31 |
| Form 306 mandatory e-filing threshold | Prior-year withholding ≥ $1,000 → must e-file via TAP |
| Form 307 annual reconciliation | January 31 |
| NDW-R (MN/MT reciprocity) renewal | Annual — by Feb 28 each year |
| NDW-R employer copy filing | Mail to Tax Commissioner by March 31 |
| SUTA wage base 2025 | $45,100 |
| SUTA wage base 2024 (reference) | $43,800 |
| SUTA experience-rated range | ~0.08% to ~9.97% [VERIFY: 2025 schedule] |
| SUTA new-employer rate | 1.02% non-construction; up to ~6.09% construction industry [VERIFY: 2025 schedule] |
| New-hire deadline | Within 20 days of hire |
| Workers' comp insurer | WSI — monopolistic. Private comp insurance is unlawful |
| Final paycheck (involuntary) | Next regular payday, per N.D.C.C. § 34-14-03 |
| Final paycheck (voluntary quit) | Next regular payday |
| State-mandated paid sick leave | None |
| State-mandated paid family leave | None |

## Section 3: North Dakota personal income tax withholding

### 3.1 Statutory basis

- **Withholding obligation** — N.D.C.C. § 57-38-59 requires every employer maintaining an office or transacting business within ND, and making payment of any wages subject to ND income tax, to deduct and withhold the tax. The withholding obligation parallels the federal obligation under IRC § 3402 and applies to wages of: ND residents, regardless of where services are performed; and Nonresidents, to the extent services are performed within ND (subject to the MN and MT reciprocity exemptions below).  _(N.D.C.C. § 57-38-59)_

### 3.2 HB 1158 of 2023 — phase-down context

In April 2023 the 68th Legislative Assembly enacted **HB 1158**, the largest individual income tax relief package in ND history. The Act: collapsed the prior five-bracket structure to **three** brackets; created a **0% bottom bracket** that exempts the first tranche of taxable income for every filer; and set the remaining two positive brackets at **1.95%** and **2.50%**.

The bracket thresholds are indexed annually. Practitioners must re-verify the bracket thresholds for each tax year against the Tax Commissioner's withholding booklet because (a) the indexing adjustments are non-trivial and (b) the legislature has shown a pattern (cf. NC SB 105 and GA HB 111) of making mid-cycle adjustments where revenue triggers are met.

### 3.3 TY 2025 brackets — single filer (withholding booklet)

**TY 2025 brackets — single filer**  _([VERIFY: 2025 ND Withholding Booklet, percentage method, Table 1A])_

| Taxable wages over | But not over | Withhold |
| --- | --- | --- |
| $0 | $47,150 | $0 |
| $47,150 | $238,200 | 1.95% of excess over $47,150 |
| $238,200 | — | $3,725.48 + 2.50% of excess over $238,200 |

### 3.4 TY 2025 brackets — married filing jointly (withholding booklet)

**TY 2025 brackets — married filing jointly**  _([VERIFY: 2025 ND Withholding Booklet, percentage method, Table 1B])_

| Taxable wages over | But not over | Withhold |
| --- | --- | --- |
| $0 | $78,775 | $0 |
| $78,775 | $289,975 | 1.95% of excess over $78,775 |
| $289,975 | — | $4,118.40 + 2.50% of excess over $289,975 |

### 3.5 Supplemental wage rate

- **Supplemental wage rate 2025** — 1.5% percent (flat rate for supplemental wages paid separately or separately identified; alternatively aggregate method may be used)

### 3.6 Pay-period frequency

- **Pay-period tables and method mandate** — The Tax Commissioner publishes percentage method tables and wage-bracket tables for the following frequencies: weekly, biweekly, semimonthly, monthly, quarterly, semiannual, annual, daily/miscellaneous. The percentage method is mandatory for software-driven payroll; wage-bracket tables remain authoritative for manual payroll under $1 million in wages.

## Section 4: Form NDW-M and choice of method

### 4.1 What NDW-M is

- **Form NDW-M** — Form NDW-M ("Withholding Allowance Certificate for Pension or Annuity Payments and Employee's State of Residence") is the ND state equivalent of federal Form W-4. Effective from 2020 onward, ND defaults to using the federal Form W-4 for state withholding purposes (no separate state W-4 required for the vast majority of employees). NDW-M is used only for: pension and annuity payees electing ND withholding; and employees who want different ND elections from their federal W-4 elections (rare).

### 4.2 Method election

- **Method election** — Employers may use either: Percentage method — required for computer payroll. Uses the bracket tables in §§ 3.3–3.4. Wage bracket method — published tables in the 2025 Withholding Booklet, acceptable for manual payroll only.

### 4.3 Employee with no W-4 on file

- **Default withholding when no W-4 on file** — Where an employee has not furnished a federal Form W-4 to the employer, the employer must withhold ND tax as if the employee had checked Single with no adjustments on the W-4 (consistent with the IRS § 3402 default).  _(IRC § 3402)_

## Section 5: Minnesota–North Dakota reciprocity — AUDIT FLASH POINT

### 5.1 Statutory and historical basis

- **MN-ND reciprocity basis and scope** — ND and MN have maintained an income tax reciprocity arrangement since 1957, suspended in tax years 2003 and 2004, and re-negotiated effective January 1, 2005. The agreement is supported on the ND side by N.D.C.C. § 57-38-59.1 and on the MN side by Minn. Stat. § 290.081. Both states issue parallel guidance each filing season confirming the agreement remains in force. Under the agreement, wage and salary income paid for personal services performed in ND by an MN resident is taxable only in MN; and vice versa for ND residents working in MN. The agreement does not cover: self-employment, partnership, S-corporation, or rental income; gambling winnings; income from a closely-held business that is not wage compensation; or lottery/contest winnings.  _(N.D.C.C. § 57-38-59.1; Minn. Stat. § 290.081)_

### 5.2 Mechanics — Form NDW-R

**Mechanics table — Form NDW-R**

| Step | Action | Deadline |
| --- | --- | --- |
| 1 | Employee completes NDW-R, swearing under penalty of perjury that they are a permanent MN (or MT) resident | By Feb 28 each year, or within 30 days of starting work / changing residence |
| 2 | Employer stops ND withholding from the next available payroll | Effective immediately on receipt |
| 3 | Employer mails the Tax Commissioner's copy of NDW-R to the ND Office of State Tax Commissioner | By March 31 each year |
| 4 | Employee renews NDW-R every year | Annually — prior-year form does not roll over |

### 5.2 Mechanics — Form NDW-R

- **Employer MN withholding requirement** — The employer must withhold Minnesota income tax instead (under MN Stat. § 290.92), which requires the employer to register for an MN withholding account if not already registered.  _(MN Stat. § 290.92)_

### 5.3 What happens if the NDW-R is missing — the audit flash point

- **Consequence of missing NDW-R** — If a qualifying MN resident's employer fails to obtain a current-year NDW-R, ND requires the employer to withhold ND tax from the employee's wages notwithstanding the underlying reciprocity. The employee's recourse is then to file Form ND-EZ at year-end claiming a full refund of the ND tax withheld — a 6-to-12-month cash-flow hit for the employee, and a common source of complaints against employers. Common employer errors: 1. Treating the NDW-R as evergreen. It is not. Each calendar year requires a fresh NDW-R. 2. Failing to mail the Tax Commissioner copy by March 31. This is a filing obligation on the employer, not the employee. Penalty exposure under N.D.C.C. § 57-38-45. 3. Forgetting to register for MN withholding. The employer must withhold MN tax. Failure to do so creates an MN delinquent-employer status. 4. Continuing the exemption after the employee moves to ND. If the employee's residence changes mid-year, the employer must restart ND withholding immediately. 5. Applying the exemption to self-employed contractors. NDW-R covers wages only.  _(N.D.C.C. § 57-38-45)_

### 5.4 Who can use NDW-R

- **Eligibility for NDW-R** — Eligibility requires the employee to be: a permanent resident of MN or MT for the entire tax year; maintain a permanent home in MN or MT throughout the year; and not maintain a permanent home in ND. A taxpayer who maintains an apartment in Fargo for convenience while keeping a permanent home in Moorhead, MN, generally qualifies. A taxpayer who has moved their permanent residence to Fargo does not, regardless of where their driver's license is issued.

## Section 6: Montana–North Dakota reciprocity

- **MT-ND reciprocity mechanics** — The ND-MT reciprocity agreement has been in force since 1976. The mechanics mirror the MN agreement: A qualifying MT resident files Form NDW-R with their ND employer. The employer stops ND withholding and starts MT withholding. The agreement covers wage and salary income only. The same Feb 28 / March 31 deadlines apply. The MT side of the agreement is administered by the MT Department of Revenue under § 15-30-2110, MCA. MT residents working in ND are not common in practice — the population centers are remote from the MT border — but oilfield and pipeline workers in Williston/Bakken can hit this regularly.  _(§ 15-30-2110, MCA)_

## Section 7: Quarterly Form 306 reporting

### 7.1 Form and due dates

**Form 306 quarterly due dates table**

| Quarter | Period | Due date |
| --- | --- | --- |
| Q1 | January 1 – March 31 | April 30 |
| Q2 | April 1 – June 30 | July 31 |
| Q3 | July 1 – September 30 | October 31 |
| Q4 | October 1 – December 31 | January 31 |

### 7.1 Form and due dates

- **Weekend/holiday due date rule** — When the due date falls on a Saturday, Sunday, or legal holiday, the next business day is the deadline.

### 7.2 Mandatory electronic filing

- **Mandatory e-filing threshold** — $1,000 USD (An employer whose ND withholding totaled $1,000 or more for the prior calendar year must file Form 306 electronically through the ND Taxpayer Access Point (TAP) at https://apps.nd.gov/tax/tap. Payment is via ACH Debit (initiated within TAP) or ACH Credit (initiated through the employer's bank). Paper Form 306 is available only for employers below the $1,000 threshold.)

### 7.3 No deposit-frequency election

- **No interim deposit requirement** — Unlike federal Form 941 (which is paired with semiweekly or monthly deposit schedules), ND does not require interim deposits. The full quarterly liability is paid with Form 306 on the quarter-end deadline. Practitioners migrating from CA, NY, or IL frequently over-engineer this — there is no ND analog to those interim deposit schedules.

### 7.4 Penalties

- **Late filing penalty** — 5% of tax due, minimum $5  _(N.D.C.C. § 57-38-45)_

### 7.4 Penalties

- **Late payment penalty** — 5% of tax due, plus interest at the rate set annually by the Tax Commissioner (12% per annum simple for 2025 [VERIFY: 2025 interest rate posting])

### 7.4 Penalties

- **Failure to file electronically penalty** — $500 per return  _(N.D.C.C. § 57-01-02.1)_

### 7.4 Penalties

- **Failure to deposit by EFT penalty** — Up to 5% of underpayment

### 7.5 Zero returns

- **Zero return filing requirement** — A registered employer who paid no ND wages for the quarter must still file a zero Form 306. Failure to file the zero return triggers the late-filing penalty floor.

## Section 8: Annual reconciliation — Form 307 + W-2/1099

### 8.1 Form 307

- **Form 307** — Form 307 ("Transmittal of Wage and Tax Statement") is the annual employer reconciliation, due January 31 of the year following the calendar year. Form 307 is the ND analog to federal Form W-3. It is filed electronically through TAP, together with copies of: all Forms W-2 issued to employees with ND wages or ND withholding; and all Forms 1099 (1099-NEC, 1099-MISC, 1099-R) that reported ND withholding.

### 8.2 W-2 filing

- **W-2 filing requirements** — For TY 2025, employers must file copies of all W-2s that report: wages paid to ND residents (regardless of withholding); or wages paid for services performed in ND; or ND tax withheld. Electronic filing is required for employers issuing 10 or more W-2s (aligning ND with the federal 10-form threshold under T.D. 9972). The TAP file specification follows the SSA EFW2 format with the ND state record extension.  _(T.D. 9972)_

### 8.3 1099-NEC filing

- **1099-NEC filing requirement** — Forms 1099-NEC reporting nonemployee compensation with ND withholding (rare because ND does not require 1099 backup withholding the way some states do) must be filed with the Tax Commissioner by January 31. 1099-NEC without ND withholding need not be filed separately with ND — the federal Combined Federal/State Filing (CF/SF) program covers this.

### 8.4 Reconciliation tie-out

- **Reconciliation tie-out requirement** — The sum of ND withholding reported on the four quarterly Forms 306 must equal the sum of ND tax withheld shown on the W-2/1099 forms transmitted with Form 307. Mismatches trigger a Tax Commissioner desk audit.

## Section 9: ND State Unemployment Tax (SUTA)

### 9.1 Administration

- **SUTA administration** — Job Service North Dakota (JSND) administers the state unemployment insurance program under N.D.C.C. Chapter 52-04. Employers register and file through the UI EASY portal at https://www.jobsnd.com.  _(N.D.C.C. Chapter 52-04)_

### 9.2 Wage base

**ND SUTA taxable wage base table**

| Year | ND SUTA taxable wage base |
| --- | --- |
| 2024 | $43,800 |
| **2025** | **$45,100** |
| 2026 | [VERIFY: not yet published as of 2026-05-28] |

### 9.2 Wage base

- **Wage base recalculation method** — The wage base is recalculated each year as 70% of the statewide average annual wage. ND's wage base is consistently among the five highest in the US.

### 9.3 Rate structure (2025)

- **Positive-balance experience rates** — 0.08% – 1.85% (Schedule 1)  _([VERIFY: 2025 Tax Rate Schedules from JSND])_

### 9.3 Rate structure (2025)

- **Negative-balance rates** — up to ~9.97%  _([VERIFY: 2025 Tax Rate Schedules from JSND])_

### 9.3 Rate structure (2025)

- **New employer (non-construction) rate** — 1.02% on rate Schedule [VERIFY]  _([VERIFY: 2025 Tax Rate Schedules from JSND])_

### 9.3 Rate structure (2025)

- **New employer (construction) rate** — 6.09% [VERIFY]  _([VERIFY: 2025 Tax Rate Schedules from JSND])_

### 9.3 Rate structure (2025)

- **Rate issuance and new employer duration** — Rates are issued annually in November/December for the following calendar year via SFN 41216. A new employer remains on the new-employer rate until they have been liable for ND UI for the period ending on the prior June 30 (i.e., typically 3 full fiscal years of experience).

### 9.4 Quarterly contribution and wage report

- **SFN 41263 requirements** — Form SFN 41263 is the quarterly Employer's Contribution and Wage Report, due the last day of the month following quarter end (same calendar as Form 306). Mandatory electronic filing via UI EASY for all employers as of 2018. Includes: gross wages by employee; excess wages (above the taxable wage base year-to-date); contribution computation; and SOC occupational code reporting (for ETA data) [VERIFY: still required 2025].

### 9.5 Penalties

- **Late report penalty** — $25 minimum, plus interest at 1.5% per month on unpaid contributions.

### 9.5 Penalties

- **Failure to file rate increase** — Rate increased by 1%  _(N.D.C.C. § 52-04-05)_

### 9.5 Penalties

- **Misclassification consequences** — Misclassification of workers (treating employees as 1099 contractors): exposes employer to back contributions, penalty, and interest, and JSND applies the multi-factor "right to control" test more aggressively than many states.

## Section 10: New-hire reporting

### 10.1 Federal basis

- **PRWORA new-hire reporting requirement** — PRWORA § 453A (codified at 42 U.S.C. § 653a) requires every employer to report each newly hired employee to the designated state agency within 20 days of the date of hire (or, for employers reporting magnetically/electronically, in two monthly transmissions not less than 12 and not more than 16 days apart).  _(42 U.S.C. § 653a)_

### 10.2 ND-specific mechanics

- **ND new-hire mechanics** — Reporting agency: North Dakota Child Support Division, Department of Health and Human Services. Method: Electronic upload via https://www.nd.gov/childsupport, fax, or paper W-4 with the employer's FEIN added. Trigger: Each newly hired or re-hired employee (re-hired = returning after a separation of 60+ days). Independent contractors paid $2,500 or more are also reportable in ND under § 14-09-09.5. Data required: Employee name, address, SSN, DOB, date of hire; employer name, address, FEIN.  _(N.D.C.C. § 14-09-09.5)_

### 10.3 Multistate-employer election

- **Multistate new-hire reporting election** — An employer with employees in two or more states may designate a single state for all its new-hire reporting under 42 U.S.C. § 653a(b)(1)(B). The designation is filed with the federal Office of Child Support Enforcement (form found at acf.hhs.gov). An employer headquartered in MN with workers in both MN and ND may elect to report all hires to MN — but the election must be filed; absent the election, the employer must report ND hires to ND.  _(42 U.S.C. § 653a(b)(1)(B))_

## Section 11: Workforce Safety & Insurance (WSI)

### 11.1 The monopoly — frequently missed by out-of-state employers

- **WSI monopoly status** — ND is one of only four US states (with OH, WA, and WY) operating a monopolistic state workers' compensation fund. WSI is the exclusive provider of workers' compensation coverage in ND. A private workers' compensation insurance policy purchased from a national carrier (Travelers, Liberty Mutual, The Hartford, etc.) does not satisfy the ND coverage requirement, and the employer is treated as uninsured.  _(N.D.C.C. Title 65)_

### 11.2 Mandatory coverage

- **Mandatory coverage scope** — Coverage is mandatory for every employer with one or more employees, including: full-time, part-time, seasonal, and temporary employees; corporate officers (unless they file Form C-3 elective exclusion); employees of out-of-state employers performing any work in ND (a Texas-based pipeline employer sending a crew to the Bakken triggers WSI coverage from day 1). Exemptions are narrow (limited to certain agricultural employers, real estate brokers paid solely on commission, and specific independent contractors meeting the 9-factor test).

### 11.3 Enforcement

- **Uninsured operation penalties** — WSI conducts compliance audits using NDDOR and JSND data feeds. Penalties for uninsured operation under N.D.C.C. § 65-04-33: Triple premium plus penalty (typically the prior 3 years' would-be premium × 3); Personal liability of corporate officers under N.D.C.C. § 65-09-02; Potential stop-work order shutting down the ND operation; and Treble damages in any employee injury suit.  _(N.D.C.C. § 65-04-33; N.D.C.C. § 65-09-02)_

### 11.4 Premium computation

- **Premium computation basis** — Premiums are based on classification code, payroll, and experience modifier. Reporting is annual via the WSI online portal. New employers receive an "industry average" rate for their NAICS code; experience modification kicks in after 3 years of claims history.

### 11.5 Practical reminder for the Fargo audit

If a Texas, Florida, or even South Dakota employer expands to a Fargo office and ports its existing national workers' comp policy, the ND coverage is invalid from day 1. The employer must apply to WSI before the first day of ND employment. This is the single most common compliance failure for employers expanding into ND.

## Section 12: Final pay, garnishment, child support

### 12.1 Final paycheck

- **Final pay rules** — Under N.D.C.C. § 34-14-03: Involuntary termination: final pay due on the next regular payday (the employee may demand earlier by certified mail, in which case the employer must pay within 15 days). Voluntary resignation: final pay due on the next regular payday. Accrued, unused PTO is payable only to the extent the employer's written policy or contract so provides — ND default rule is no PTO payout obligation absent agreement.  _(N.D.C.C. § 34-14-03)_

### 12.2 Wage garnishment

- **Garnishment limits** — ND follows federal Consumer Credit Protection Act (CCPA) limits: 25% of disposable earnings or 30 × federal minimum wage, whichever is less. Child support withholding orders take priority over creditor garnishments and may take up to 50–65% of disposable income under 15 U.S.C. § 1673(b)(2).  _(15 U.S.C. § 1673(b)(2))_

### 12.3 Child support withholding

- **IWO processing requirements** — Employers receive an Income Withholding for Support (IWO) from the ND CSD or another state's agency. Withholding must begin no later than the first pay period after 14 days from the date the IWO was mailed. Remittance to the ND State Disbursement Unit within 7 business days of withholding.

## Section 13: Tier 1 deterministic rules vs Tier 2 judgment rules

### 13.1 Tier 1 (deterministic — apply mechanically)

**Tier 1 rules table**

| Rule ID | Statement |
| --- | --- |
| T1-ND-PAY-01 | If employer's prior-year withholding ≥ $1,000, Form 306 must be filed electronically through TAP. |
| T1-ND-PAY-02 | Form 306 quarterly due dates are 4/30, 7/31, 10/31, 1/31. |
| T1-ND-PAY-03 | Form 307 annual reconciliation is due January 31. |
| T1-ND-PAY-04 | An MN or MT resident must file NDW-R **annually** to exempt wages from ND withholding. |
| T1-ND-PAY-05 | Employer must mail the Tax Commissioner copy of NDW-R by March 31. |
| T1-ND-PAY-06 | 2025 ND SUTA taxable wage base is $45,100. |
| T1-ND-PAY-07 | 2025 ND supplemental wage rate is 1.5%. |
| T1-ND-PAY-08 | New-hire reports are due to the ND CSD within 20 days of hire. |
| T1-ND-PAY-09 | ND workers' comp must be obtained from WSI — private coverage is invalid. |
| T1-ND-PAY-10 | Final pay is due on the next regular payday. |
| T1-ND-PAY-11 | An employer issuing 10+ W-2s must file them electronically with ND via TAP. |

### 13.2 Tier 2 (judgment — surface to verifier)

**Tier 2 rules table**

| Rule ID | Statement |
| --- | --- |
| T2-ND-PAY-01 | Whether a commuter qualifies as a "permanent MN resident" under NDW-R when they maintain a Fargo apartment for the work week is a domicile-law determination. |
| T2-ND-PAY-02 | Whether a corporate officer should file the WSI Form C-3 elective exclusion depends on closely-held-business risk tolerance. |
| T2-ND-PAY-03 | Whether the multistate-employer new-hire election should be made to ND, MN, or HQ-state is an administrative-burden tradeoff. |
| T2-ND-PAY-04 | Whether a worker is an employee or 1099 contractor for SUTA purposes — JSND applies a 9-factor right-to-control test that overlaps but differs from the IRS 20-factor test. |
| T2-ND-PAY-05 | Whether to use the percentage method or wage bracket method when both produce different cents of withholding for low-wage employees. |

## Section 14: Worked examples

### Example 1 — Standard ND-resident employee, biweekly $2,500, single, no NDW-R

**Facts.** Anna lives in Bismarck, ND. Biweekly gross wages = $2,500. Federal W-4 = single, no adjustments. No 401(k), no Section 125.

**Step 1 — Annualize.** $2,500 × 26 = $65,000 annual wages.

**Step 2 — Apply 2025 single bracket table** [VERIFY: 2025 booklet exact threshold]. Assume bottom-bracket cutoff = $47,150 single.

```
Taxable above cutoff: $65,000 - $47,150 = $17,850
Annual ND tax: $17,850 × 1.95% = $348.08
Per pay period: $348.08 / 26 = $13.39
```

**Step 3 — Round.** Round per the percentage method instruction (to the nearest whole dollar): **$13.00 withheld per biweekly pay**.

**Step 4 — Form 306, Q1.** Anna's six pays in Q1 → $13 × 6 = $78 ND tax remitted with Form 306 by April 30. (Aggregated with all other employees.)

### Example 2 — Minnesota commuter with NDW-R on file

**Facts.** Bjorn lives in Moorhead, MN, and commutes daily to a software job in Fargo, ND. Biweekly gross wages = $3,200. Filed NDW-R on his first day of work, dated February 1, 2025.

**Step 1 — Verify NDW-R.** Employer confirms: Permanent address in MN: yes (verified driver's license + lease). Form signed and dated within 30 days of start: yes. Calendar-year specific: yes (2025).

**Step 2 — ND withholding.** Zero ND tax withheld on Bjorn's wages for the entire 2025 calendar year.

**Step 3 — MN withholding.** Employer registers for an MN withholding account and withholds MN tax under MN Stat. § 290.92 using Form W-4MN.

**Step 4 — Employer's March 31 obligation.** Employer mails the Tax Commissioner copy of Bjorn's NDW-R to the ND Office of State Tax Commissioner by March 31, 2025.

**Step 5 — Renewal.** A fresh NDW-R is required on or before February 28, 2026 for the 2026 calendar year. The employer should diary this in December 2025.

**Failure mode.** If Bjorn forgets to renew in February 2026 and the employer does not collect a 2026 NDW-R, the employer must withhold ND tax from his 2026 wages starting January 1, 2026 (or, in practice, the first payroll after the Feb 28 default deadline). Bjorn then files Form ND-EZ in 2027 to claim the ND withholding back as a refund — a real cash flow hit, and the source of frequent payroll complaints.

### Example 3 — High-income ND-resident at the top bracket

**Facts.** Carla is a Bismarck-based oilfield engineer earning $325,000 annual salary, paid semimonthly ($13,541.67 gross per pay). Federal W-4 = single, no adjustments. She receives a $50,000 year-end bonus.

**Regular wage withholding per pay period**

Annualize: $13,541.67 × 24 = $325,000. Apply 2025 single percentage table [VERIFY exact thresholds]:

```
First $47,150 → 0%
$47,150 to $238,200 → 1.95% × $191,050 = $3,725.48
Above $238,200 → 2.50% × ($325,000 - $238,200) = 2.50% × $86,800 = $2,170.00
Annual ND tax = $5,895.48
Per pay (÷24) = $245.65
```

Round → **$246 ND withheld per semimonthly pay**.

**Year-end bonus — supplemental rate**

Paid on a separate check identified as a bonus:

```
$50,000 × 1.5% = $750 ND tax withheld
```

The 1.5% supplemental rate is below Carla's marginal rate of 2.50%, so she will under-withhold on the bonus by approximately ($50,000 × 1.00%) = $500. The employer is not at fault — the supplemental rate is a statutory safe harbor — but Carla should be advised to make an ND estimated payment on Form 540-ES [VERIFY: ND uses Form ND-1ES for estimates] to avoid a balance due in April 2026.

## Section 15: Refusal catalogue

**Refusal catalogue table**

| Refusal ID | Trigger | Response |
| --- | --- | --- |
| R-ND-PAY-01 | Federal payroll (941, 940, W-2 to SSA, FICA, FUTA, federal W-4) | "This skill covers ND state payroll only. Federal payroll is covered by the federal payroll skill." |
| R-ND-PAY-02 | Multistate payroll allocation beyond MN/MT reciprocity | "Multistate payroll allocation (e.g., employees splitting work between ND and a non-reciprocity state) requires a multistate payroll specialist." |
| R-ND-PAY-03 | S-corp reasonable compensation determination | "Reasonable compensation analysis for an S-corp shareholder-employee is outside this skill. Refer to the federal S-corp skill." |
| R-ND-PAY-04 | Pension and retirement plan distributions | "Pension/annuity withholding on distributions is outside this employer-payroll skill. Refer to the ND individual-tax skill and federal Form 1099-R guidance." |
| R-ND-PAY-05 | ND oil and gas worker housing per diem | "ND oilfield per diem taxability requires §62(a)(2)(A) accountable plan analysis — refer to the federal travel skill." |
| R-ND-PAY-06 | Independent contractor classification disputes | "Worker classification disputes between W-2 and 1099 require specialist review under JSND's right-to-control test." |
| R-ND-PAY-07 | Cafeteria plan / §125 plan design | "ND treats §125 elections per federal — plan design is out of scope." |
| R-ND-PAY-08 | Tribal-government employer issues (Standing Rock, Three Affiliated Tribes, etc.) | "Tribal sovereignty payroll issues require specialist counsel." |
| R-ND-PAY-09 | Workers' comp claims handling | "WSI claim handling and disputes are outside this skill — refer to a WSI claims specialist or ND attorney." |

## Section 16: Form mapping

**Form mapping table**

| Form | Purpose | Frequency | Filing channel | Federal cross-reference |
| --- | --- | --- | --- | --- |
| Form 306 | Quarterly ND withholding return | Quarterly | TAP (mandatory if PY WH ≥ $1,000) | Federal Form 941 |
| Form 307 | Annual W-2/1099 transmittal | Annual — Jan 31 | TAP | Federal Form W-3 |
| Form NDW-M | State allowance certificate (rare) | At hire / change | Retained by employer | Federal Form W-4 |
| Form NDW-R | MN/MT reciprocity exemption | Annual — Feb 28 | Employee → employer → Tax Commissioner by Mar 31 | — (no federal analog) |
| SFN 41263 | Quarterly UI contribution & wage report | Quarterly | UI EASY (mandatory e-file) | Federal Form 940 (annual FUTA) |
| WSI Annual Payroll Report | Workers' comp premium reconciliation | Annual | WSI portal | — (private states use carrier-direct billing) |
| ND New Hire Report | New-hire notification | Within 20 days of hire | ND CSD portal | Federal new-hire reporting (PRWORA) |
| Federal W-2 (Copy 1) | Employee wage statement to ND | Annual — Jan 31 | Bundled in Form 307 e-file | Federal W-2 Copies A/B/C/D |
| Federal 1099-NEC (Copy 1) | Contractor compensation to ND if ND WH | Annual — Jan 31 | TAP or CF/SF program | Federal 1099-NEC |

## Section 17: Provenance

**Provenance table**

| Field | Value |
| --- | --- |
| Author | OpenAccountants AI draft |
| Verifier | pending — ND CPA or EA with ND payroll specialty |
| Verification status | Tier 2, AI-drafted, pre-verification |
| Last updated | 2026-05-28 |
| Next review trigger | (a) Publication of TY 2026 ND Withholding Booklet; (b) any HB 1158 successor legislation; (c) annual JSND wage base release (typically November); (d) any WSI premium-rate restructure |
| `[VERIFY:]` count | All bracket thresholds, SUTA rate schedule percentages, the 2026 wage base, and the 2025 interest rate require re-verification against current ND Tax Commissioner / JSND publications |

### Key URLs (all visited 2026-05-28)

- ND Tax Commissioner — Withholding: https://www.tax.nd.gov/business/income-tax-withholding
- 2025 Withholding Booklet PDF: https://www.tax.nd.gov/sites/www/files/documents/misc-discuss-folder/Final_2025%20Income%20Tax%20Withholding%20Rates%20%20Instructions.pdf
- Form 306: https://www.tax.nd.gov/sites/www/files/documents/forms/business/it-withholding/form-306-web.pdf
- Form NDW-R: https://www.tax.nd.gov/sites/www/files/documents/forms/business/ndwrfillable.pdf
- Withholding Guideline: https://www.tax.nd.gov/sites/www/files/documents/guidelines/business/it-withhold/income-tax-withholding-information-returns-guideline.pdf
- JSND 2025 UI Rate Schedules: https://www.jobsnd.com/sites/www/files/documents/jsnd-documents/uitaxrateschedules2025.pdf
- JSND Employer Handbook: https://www.library.nd.gov/statedocs/JobService/jsnd4036.pdf
- HB 1158 (2023): https://ndlegis.gov/assembly/68-2023/regular/documents/23-0351-02000.pdf
- WSI: https://www.workforcesafety.com
- TAP: https://apps.nd.gov/tax/tap
- UI EASY: https://www.jobsnd.com
- ND CSD new-hire: https://www.nd.gov/childsupport

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, payroll, or workers' compensation advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional before filing, depositing, or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com).

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
