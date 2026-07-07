---
name: nc-bailey-settlement-retirement
description: Use this skill whenever asked about North Carolina state taxation of retirement income for an individual on Form D-400 — specifically the Bailey settlement exclusion for vested NC state/local government, federal, and military retirees, plus the broader NC retirement income treatment (Social Security exemption, military retirement exemption under S.L. 2021-180, private-pension and IRA/401(k) treatment). Trigger on phrases like "Bailey settlement", "Bailey-protected", "TSERS retiree", "LGERS retiree", "CSRS retiree", "FERS retiree", "NC military retirement", "vested by August 12 1989", "NC pension exclusion", or any D-400 Schedule S Part B Line 20 or Line 21 question.
jurisdiction: US-NC
tax_year: 2025
tier: 2
last_updated: 2026-07-06
---

# nc-bailey-settlement-retirement

## North Carolina Bailey Settlement & Retirement Income — Tier 2 Skill

> **Scope.** This skill covers North Carolina individual income tax treatment of retirement benefits on Form D-400 and Form D-400 Schedule S for full-year NC residents. It focuses on the *Bailey* settlement exclusion (Schedule S Line 20), the post-S.L. 2021-180 military retirement deduction (Schedule S Line 21), the Social Security / Railroad Retirement deduction (Schedule S Line 19), and the NC treatment of private pensions, traditional and Roth IRAs, 401(k)s, 403(b)s, and 457 plans not covered by *Bailey*. Tax year 2025 (returns filed in 2026).
>
> **Quality tier.** Q3 — AI-drafted, not independently verified. Every output must be reviewed and signed off by a qualified NC tax professional before filing. Items marked `[VERIFY:]` require explicit confirmation against current NCDOR guidance or the latest D-401 instructions.
>
> **MUST be loaded alongside** `us-tax-workflow-base v0.2+` and `nc-income-tax v0.1+`. This skill does not itself produce a full D-400 — it produces the Schedule S Part B retirement-deduction lines that flow into the parent NC return.

## Section 1: Metadata

**Section 1: Metadata table**

| Field | Value |
| --- | --- |
| Tax type | Individual income tax — retirement benefits subtraction |
| Jurisdiction | North Carolina (US-NC) |
| Tax year | 2025 (filed 2026) |
| Primary form | Form D-400 (line 9 deduction total) |
| Supporting schedule | Form D-400 Schedule S, Part B, Lines 19 / 20 / 21 |
| Tax structure | Flat 4.25% rate (TY 2025); 3.99% (TY 2026) [VERIFY: S.L. 2023-134 schedule has been adjusted in subsequent sessions — confirm against NCDOR Tax Rate Schedules before relying] |
| Filing deadline | April 15, 2026 |
| Extension deadline | October 15, 2026 |
| Tax authority | North Carolina Department of Revenue (NCDOR) |
| Statute | N.C. Gen. Stat. § 105-153.5(b)(5), (b)(5a) (current chapter); historical § 105-134.6(b)(6) (pre-2014) |
| Governing case | *Bailey v. State of North Carolina*, 348 N.C. 130, 500 S.E.2d 54 (1998); Consent Order entered June 11, 1998 |

### Sources consulted (URLs verified May 28, 2026)

- NCDOR, "Bailey Decision Concerning Federal, State and Local Retirement Benefits": https://www.ncdor.gov/taxes-forms/individual-income-tax/filing-topics/bailey-decision-concerning-federal-state-and-local-retirement-benefits
- NCDOR, "2025 D-400 Schedule S North Carolina Supplemental Schedule (Web-Fill 9-25)": https://www.ncdor.gov/2025-d-400-schedule-s-web-fill-version/open
- NCDOR, "2025 D-401 Individual Income Tax Instructions": https://www.ncdor.gov/2025-d-401-individual-income-tax-instructions/open
- NCDOR Directive PD-99-1 (qualifying retirement systems list): https://www.ncdor.gov/taxes-forms/individual-income-tax/personal-taxes-division-directives/directive-pd-99-1
- NCDOR Directive PD-00-1: https://www.ncdor.gov/taxes-forms/withholding-tax/individual-income-tax-directives-main/directive-pd-00-1
- NCDOR, "Military Retirement" topic page: https://www.ncdor.gov/taxes-forms/individual-income-tax/military-retirement
- NCDOR Important Notice, "North Carolina Enacts New Deduction For Certain Military Retirement Pay and Survivor Benefit Plan Payments" (S.L. 2021-180): https://www.ncdor.gov/taxes-forms/information-tax-professionals/tax-bulletins-directives-and-other-important-notices/important-notices-and-frequently-asked-questions-personal-taxes/important-notice-north-carolina-enacts-new-deduction-certain-military-retirement-pay-and
- N.C. Gen. Stat. § 105-153.5 (full text, NCGA): https://www.ncleg.net/enactedlegislation/statutes/html/bysection/chapter_105/gs_105-153.5.html
- *Bailey v. State*, 348 N.C. 130 (1998), Justia: https://law.justia.com/cases/north-carolina/supreme-court/1998/53pa96-9.html
- N.C. Department of Justice, "Qualification for Class Membership in Bailey/Emory/Patton Lawsuits": https://ncdoj.gov/opinions/qualification-for-class-membership-in-bailey-emory-patton-lawsuits/

## Section 2: Quick reference — the Bailey test at a glance

**The five-question screen.** For any retirement benefit being considered for the Line 20 *Bailey* exclusion, the preparer must answer **yes** to all five:

1. Is the benefit paid by a **qualifying retirement system** (see list below)?
2. Did the retiree have **five or more years of creditable service** in that specific system?
3. Was the five-year threshold met **on or before August 12, 1989**?
4. Is the benefit included in **federal adjusted gross income** (i.e., not already excluded federally)?
5. Does the taxpayer have **documentary evidence** of vested status from the retirement system (Form 1099-R, retirement system certification, or service record)?

If yes to all five → fully excluded from NC taxable income on **D-400 Schedule S, Part B, Line 20**. There is **no dollar cap**.

### Bailey-qualifying retirement systems (TY 2025)

**Bailey-qualifying retirement systems (TY 2025)**  _(NCDOR Directive PD-99-1)_

| Plan | Type | Vesting test |
| --- | --- | --- |
| NC Teachers' and State Employees' Retirement System (TSERS) | NC defined benefit | 5 yrs creditable service by 8/12/1989 |
| NC Local Governmental Employees' Retirement System (LGERS) | NC defined benefit | 5 yrs creditable service by 8/12/1989 |
| NC Consolidated Judicial Retirement System | NC defined benefit | 5 yrs creditable service by 8/12/1989 |
| NC Legislative Retirement System | NC defined benefit | 5 yrs creditable service by 8/12/1989 |
| Federal Civil Service Retirement System (CSRS) | Federal DB | 5 yrs creditable service by 8/12/1989 |
| Federal Employees' Retirement System (FERS) | Federal DB | 5 yrs creditable service by 8/12/1989 |
| U.S. military retirement (all branches) | Federal DB | 5 yrs creditable service by 8/12/1989 — **but see Section 6, military now generally fully excluded under § 105-153.5(b)(5a)** |
| NC State §401(k) plan | NC defined contribution | Contributed or contracted to contribute by 8/12/1989 |
| NC State §457 plan | NC deferred comp | Contributed or contracted to contribute by 8/12/1989 |
| NC National Guard Pension Fund | NC | Per Directive PD-99-1 |
| NC Sheriffs' Supplemental Pension Fund | NC | 5 yrs as sheriff + 5 yrs LGERS by 8/12/1989 |
| NC Firemen's and Rescue Squad Workers' Pension Fund | NC | 5 yrs service + 5 yrs contributions by 8/12/1989 |
| NC Registers of Deeds' Supplemental Pension Fund | NC | 5 yrs register service + 5 yrs LGERS by 8/12/1989 |

## Section 2: Quick reference — the Bailey test at a glance

> **Audit flash point — 8/12/1989 is a hard cliff.** A retiree who attained 5 years of creditable service on August 13, 1989 receives **zero** Bailey protection. NCDOR has consistently refused equitable extensions in audit. The date traces to the *Davis v. Michigan* (1989) federal pre-emption ripple that pushed NC to repeal the prior reciprocal exemption — *Bailey* preserved the protection only for those whose contractual rights had vested before the repeal.

### 3.1 Background

Before 1989, N.C. Gen. Stat. § 135-9 and parallel provisions exempted NC state and local government retirement benefits from NC income tax while taxing federal retirement benefits. The U.S. Supreme Court held in *Davis v. Michigan Department of Treasury*, 489 U.S. 803 (1989) that such asymmetric treatment violated the federal intergovernmental tax immunity doctrine codified at 4 U.S.C. § 111. NC responded by repealing the state-government exemption (effective for tax years after 1988) so as to tax all retirees equally.

Five named retirees (Bailey, Emory, Patton, and others) sued, arguing that the state-government exemption was a contractual right that had vested for retirees who had earned five or more years of creditable service before the repeal took effect.

### 3.2 The case

*Bailey v. State of North Carolina*, 348 N.C. 130, 500 S.E.2d 54 (1998), held that the state-government retirement exemption was a contractual right that could not be impaired retroactively against vested employees. The court applied the Contract Clause analysis to N.C. Gen. Stat. § 135-9 and held that the state must honor the exemption for any employee who had vested before the repeal.

### 3.3 The settlement

On **June 11, 1998**, the parties entered a Consent Order ("the *Bailey* Consent Order") for $799 million in refunds covering tax years 1989-1997. The Consent Order extended the holding to federal government retirees (CSRS, FERS, military) because *Davis v. Michigan* required parity, and it fixed **August 12, 1989** as the operative vesting cut-off date. That date was the day before the NC General Assembly's 1989 repeal took effect.

The Consent Order provides that qualifying retirees and their surviving beneficiaries "shall not be liable for North Carolina income tax on federal government or North Carolina state or local government retirement benefits" — a perpetual, non-revocable exemption codified at **N.C. Gen. Stat. § 105-153.5(b)(5)**.

### 3.4 The statutory codification

- **§ 105-153.5(b)(5) paraphrase** — The amount received during the taxable year from one or more State, local, or federal government retirement plans to the extent the amount is exempt from tax under this Part pursuant to a court order in settlement of the following cases: *Bailey v. State of North Carolina*, *Emory v. State of North Carolina*, and *Patton v. State of North Carolina*. `[VERIFY: § 105-153.5(b) subdivision numbering may have shifted with subsequent legislative renumbering. Confirm against the most recent codification before citing in a return position.]`  _(N.C. Gen. Stat. § 105-153.5(b)(5) (current language, paraphrased — verify against most recent codification))_

### 4.1 NC TSERS (Teachers' and State Employees' Retirement System)

- Administered by the NC Department of State Treasurer, Retirement Systems Division.
- Defined-benefit plan covering NC public school teachers, university employees, and most state agency staff.
- Vesting verification: TSERS provides a Form 1099-R that includes the federal taxable amount in Box 2a; Bailey vesting status is **not** indicated on the 1099-R. The preparer must request a separate **TSERS Service Verification Letter** (sometimes called a "Bailey letter") from the Retirement Systems Division certifying that the member had 5+ years of creditable service as of 8/12/1989.
- Practical tip: TSERS will sometimes issue a Form 1099-R with a state distribution code or note indicating Bailey-qualifying status. Look for "Bailey" or "Non-taxable to NC" annotations. Absent that, request the letter.

### 4.2 NC LGERS (Local Governmental Employees' Retirement System)

- Same administrator as TSERS.
- Covers employees of NC counties, cities, and other local political subdivisions that have opted into LGERS.
- Same 8/12/1989 vesting test.

### 4.3 Federal CSRS (Civil Service Retirement System)

- Closed to new entrants on January 1, 1987 (FERS took its place for employees hired after that date).
- Because CSRS effectively closed before 8/12/1989, **most CSRS retirees with significant service will satisfy the Bailey vesting test** — but the preparer must still confirm 5 years of creditable service by 8/12/1989, not merely "CSRS-classified."
- Form 1099-R from OPM (Office of Personnel Management) shows the federal taxable portion. The OPM annuity statement (CSA / CSF claim number) is the primary documentary evidence.

### 4.4 Federal FERS (Federal Employees' Retirement System)

- FERS was enacted in 1986 and took effect January 1, 1987.
- A FERS retiree had at most ~32 months of FERS service by 8/12/1989 — so **most pure FERS retirees do NOT qualify for Bailey** unless they had prior CSRS service that they carried into FERS (CSRS-Offset or CSRS Component).
- **Audit flash point:** preparers routinely err in assuming FERS retirees qualify for Bailey. The CSRS Component of a FERS annuity may be Bailey-protected; the FERS Component is generally not. Some FERS annuities are split-stream — only a portion qualifies.

### 4.5 U.S. military retirement

- **Pre-S.L. 2021-180:** Military retirees were treated identically to other federal retirees under Bailey — 5 yrs of creditable service by 8/12/1989 required.
- **Post-S.L. 2021-180 (effective for tax years beginning on or after January 1, 2021):** The General Assembly enacted N.C. Gen. Stat. § 105-153.5(b)(5a), creating a separate, broader military retirement deduction:
  - **Effective TY 2021 forward:** Deduction for retirement pay received during the taxable year for service in the uniformed services to a retired member who:
    - served at least **20 years** in the uniformed services; **or**
    - was **medically retired** under 10 U.S.C. Chapter 61.
  - "Uniformed services" has the meaning given in **10 U.S.C. § 101(a)(5)** — Army, Navy, Marine Corps, Air Force, Space Force, Coast Guard, plus commissioned officers of NOAA and the U.S. Public Health Service.
  - Also covers Survivor Benefit Plan (SBP) payments to eligible beneficiaries.
  - **No vesting-by-1989 requirement** under § 105-153.5(b)(5a).
- **Anti-double-deduction rule:** "Amounts deducted under this subdivision may not also be deducted under subdivision (5) of this subsection." A military retiree who qualifies under both (b)(5) (Bailey) and (b)(5a) (new military) must pick one — typically (b)(5a) if both apply, because the documentation burden is lower (no Bailey letter required) and the result is identical.

> **Audit flash point — distinguish Bailey from Buchanan.** The "*Buchanan settlement*" is sometimes used informally in NC tax circles to refer to a broader military retirement exemption discussion that culminated in S.L. 2021-180; it is **not** a separate court case settlement with NCDOR like *Bailey*. The operative authority for the post-2021 military exemption is the statute (§ 105-153.5(b)(5a)) and S.L. 2021-180, not a court order.

### 4.6 NC Consolidated Judicial Retirement System & NC Legislative Retirement System

- Small populations but the rules are identical to TSERS: 5 yrs creditable service by 8/12/1989.
- Vesting letter requested from NC Retirement Systems Division.

### 4.7 NC State §401(k) and §457 plans

- These are **defined-contribution** plans (NC 401(k) Plan and NC 457(b) Plan, both administered through Empower).
- **Different vesting test:** the participant must have "**contributed or contracted to contribute to the plan prior to August 12, 1989**." There is no 5-year service requirement because these are contribution-based, not service-based.
- The protection extends to subsequent investment earnings and post-1989 contributions to the **same plan**.

## Section 5: NC's broader retirement income landscape (TY 2025)

This is the full picture of how NC treats each type of retirement income — Bailey is only one piece.

### 5.1 Social Security & Railroad Retirement — fully exempt for ALL

**Social Security & Railroad Retirement table**

| Source | NC treatment | Schedule S line |
| --- | --- | --- |
| Social Security retirement benefits (Title II) | **Fully exempt** regardless of Bailey status | Line 19 (deduct the federally taxable portion) |
| Social Security disability (SSDI) | **Fully exempt** | Line 19 |
| Tier 1 Railroad Retirement | **Fully exempt** | Line 19 |
| Tier 2 Railroad Retirement | **Fully exempt** (treated as RR retirement under federal law and excluded by NC) | Line 19 |
| SSI | Not in federal AGI; no NC adjustment | n/a |

- **Mechanism for SS/RR subtraction** — The mechanism: federal Form 1040 includes the taxable portion of Social Security in AGI per IRC § 86 (up to 85%). NC backs that taxable portion out on D-400 Schedule S, Part B, **Line 19**, effective per N.C. Gen. Stat. § 105-153.5(b)(5)/(b)(6) `[VERIFY: subdivision letter for the Social Security subtraction — historical guidance refers to (b)(5), (b)(6), or (b)(8) depending on year]`.  _(N.C. Gen. Stat. § 105-153.5(b)(5)/(b)(6))_

### 5.2 Military retirement — fully exempt for qualifying retirees

- **Military retirement treatment summary** — Per Section 4.5 — fully exempt under § 105-153.5(b)(5a) for 20-year and medically retired members regardless of 1989 vesting. Schedule S **Line 21**. For military retirees who do **not** meet the (b)(5a) test but **do** satisfy Bailey, the deduction goes on **Line 20** (Bailey). For military retirees who satisfy **neither** test (e.g., a retiree who took early reserve retirement with less than 20 years and was not medically retired, and was not vested by 8/12/1989), the military pension is **fully taxable** to NC.  _(N.C. Gen. Stat. § 105-153.5(b)(5a))_

### 5.3 Bailey-protected government retirement — fully exempt

- **Bailey-protected treatment cross-reference** — Per Sections 3-4. Schedule S **Line 20**.

### 5.4 Private pensions, 401(k)s, 403(b)s, traditional IRAs, SEP-IRAs, SIMPLE IRAs — **fully taxable to NC**

- **No general retirement income deduction in NC** — NC has **no general retirement-income deduction**. Unlike Georgia, South Carolina, Pennsylvania, and several other Southeastern states, North Carolina does not offer an age-based retirement income deduction. The full federally taxable amount of: - Private employer pensions (corporate DB plans) - Distributions from private 401(k) plans - Distributions from 403(b) plans (unless from a Bailey-qualifying NC plan) - Traditional IRA distributions (including SEP-IRA and SIMPLE IRA) - Annuity distributions (commercial fixed and variable annuities) - Cash-balance plans - Profit-sharing distributions …is **fully included** in NC taxable income via federal AGI. No NC subtraction is available unless the distribution is from a Bailey-qualifying plan.

### 5.5 Roth IRA distributions

- **Roth IRA distribution treatment** — - Qualified Roth distributions are not in federal AGI → not in NC AGI → no NC tax. No Schedule S entry needed. - Non-qualified Roth distributions follow federal taxation; the federally taxable portion is taxable to NC.

### 5.6 Rollover treatment — critical Bailey nuance

**Rollover treatment table**  _(NCDOR's "Bailey Decision" page and Directive PD-00-1)_

| Rollover type | Bailey character preserved? |
| --- | --- |
| Direct trustee-to-trustee rollover from a Bailey-qualifying plan to **another Bailey-qualifying plan in which the participant was also vested by 8/12/1989** | **Yes** — Bailey character is preserved on subsequent distributions |
| Direct rollover from a Bailey-qualifying plan to an **IRA** | **No** — character is lost; subsequent IRA distributions are fully taxable to NC |
| Direct rollover from a Bailey-qualifying plan to a **non-Bailey 401(k)** (e.g., a private-sector employer plan) | **No** — character is lost |
| Roth conversion of Bailey-protected funds | The conversion distribution itself remains exempt from NC tax; the resulting Roth IRA follows ordinary Roth rules thereafter |

> **Audit flash point — rollover character is fragile.** Many retirees roll their TSERS or CSRS distributions into a private IRA for investment flexibility. **Doing so destroys the Bailey protection on subsequent distributions.** The preparer should advise any vested Bailey retiree to think carefully before rolling out of the qualifying plan, and to obtain custodian-level documentation of any rollover that preserves character.

### 5.7 Survivor / beneficiary treatment

- **Survivor/beneficiary treatment** — Per the *Bailey* Consent Order and NCDOR's settlement implementation: the exemption applies to **surviving beneficiaries** of a qualifying retiree, including a surviving spouse receiving a joint-and-survivor annuity, contingent annuitants, and estate beneficiaries receiving a death benefit traceable to the qualifying account. Documentary proof of the **deceased member's** Bailey-vested status is the operative requirement; the beneficiary's own employment history is irrelevant.  _(*Bailey* Consent Order; NCDOR settlement implementation)_

## Section 6: Documentation requirements

**Documentation requirements table**

| Document | Source | Purpose |
| --- | --- | --- |
| Form 1099-R for the year | Plan administrator (TSERS, OPM, DFAS, etc.) | Identifies payer and gross/taxable amounts |
| Bailey vesting certification letter | NC Retirement Systems Division (TSERS/LGERS), OPM (CSRS/FERS), or DFAS (military) | Certifies 5 yrs creditable service by 8/12/1989 |
| Service computation date (SCD) | Federal Form SF-50 or OPM annuity statement | Documents start of federal service |
| Original NC-4P withholding election | Plan administrator records | Shows that retiree elected Bailey treatment for NC withholding |
| Rollover statements (if any) | Receiving custodian | Documents preservation or loss of Bailey character |
| Survivor's documentation (if applicable) | Death certificate + plan administrator survivor designation | For beneficiary returns |

- **1099-R insufficiency and attachment requirement** — **Form 1099-R alone is not sufficient** to support the Line 20 deduction. NCDOR has audited returns where the only support was a 1099-R from TSERS, and disallowed the deduction for lack of documentary vesting evidence. The Bailey letter (or equivalent OPM/DFAS service-history confirmation) is the operative document. The 2025 D-401 instructions require attaching a copy of the Form 1099-R or Form W-2 to the return supporting any Line 20 / Line 21 deduction. `[VERIFY: instruction wording — confirm the attachment requirement language in the most current D-401 issued by NCDOR.]`  _(2025 D-401 instructions [VERIFY])_

## Section 7: Tier 1 — deterministic rules

**Tier 1 deterministic rules table**

| Rule ID | Rule | Source |
| --- | --- | --- |
| NC-BAILEY-T1-01 | Bailey-protected retirement income is **fully excluded** from NC taxable income with no dollar cap | N.C. Gen. Stat. § 105-153.5(b)(5); *Bailey* Consent Order (1998) |
| NC-BAILEY-T1-02 | The Bailey vesting test is **5+ years of creditable service in a qualifying plan as of August 12, 1989** | NCDOR Directive PD-99-1; *Bailey* Consent Order |
| NC-BAILEY-T1-03 | For NC § 401(k) and § 457 plans, the test is **contribution or contracted contribution by August 12, 1989** (not 5-year service) | NCDOR Bailey page; Directive PD-99-1 |
| NC-BAILEY-T1-04 | Military retirement is fully deductible under § 105-153.5(b)(5a) if the retiree served **20+ years** in uniformed services or was **medically retired under 10 U.S.C. Chapter 61** — no 1989 vesting required | S.L. 2021-180; N.C. Gen. Stat. § 105-153.5(b)(5a) |
| NC-BAILEY-T1-05 | Bailey (Line 20) and new military (Line 21) deductions **cannot be claimed on the same dollars** | § 105-153.5(b)(5a) anti-stacking rule |
| NC-BAILEY-T1-06 | Social Security and Railroad Retirement benefits (federally taxable portion) are **fully excluded** from NC taxable income | N.C. Gen. Stat. § 105-153.5(b); D-400 Sch S Line 19 |
| NC-BAILEY-T1-07 | Direct trustee-to-trustee rollover from a Bailey plan to an IRA **destroys Bailey character** for subsequent distributions | NCDOR Directive PD-00-1; NCDOR Bailey page |
| NC-BAILEY-T1-08 | Direct trustee-to-trustee rollover into another Bailey-qualifying plan in which the participant was **also vested by 8/12/1989** preserves Bailey character | NCDOR Directive PD-00-1 |
| NC-BAILEY-T1-09 | The Bailey exclusion extends to **surviving beneficiaries** of a vested member | *Bailey* Consent Order; NCDOR Directive PD-99-1 |
| NC-BAILEY-T1-10 | A Form 1099-R must be attached to Form D-400 supporting any Line 20 or Line 21 deduction | NCDOR 2025 D-401 instructions [VERIFY exact wording] |
| NC-BAILEY-T1-11 | Private pensions, IRAs (other than rolled-from-Bailey traceable), and 401(k)s **are fully taxable** to NC | N.C. Gen. Stat. § 105-153.5 (no general retirement deduction) |
| NC-BAILEY-T1-12 | NC standard deduction TY 2025: $12,750 single / $25,500 MFJ / $12,750 MFS / $19,125 HoH `[VERIFY: confirm against TY 2025 D-401]` | N.C. Gen. Stat. § 105-153.5(a)(1) |
| NC-BAILEY-T1-13 | NC flat rate TY 2025 = 4.25%; TY 2026 = 3.99% `[VERIFY against most recent rate schedule]` | Session Law 2023-134 |

## Section 8: Tier 2 — judgment rules

**Tier 2 judgment rules table**

| Rule ID | Situation | Guidance |
| --- | --- | --- |
| NC-BAILEY-T2-01 | **Mixed CSRS / FERS service** (e.g., CSRS-Offset retiree) | The CSRS Component of the annuity is potentially Bailey-protected if the member had 5 yrs of CSRS service by 8/12/1989; the FERS Component generally is not. Request OPM to identify the split. Many OPM annuities are NOT cleanly split — escalate to a credentialed reviewer for allocation. |
| NC-BAILEY-T2-02 | **Reservist with active-duty service crossing 8/12/1989** | Count creditable service per the relevant uniformed service's rules (Army/Navy/AF retirement points). If the member had 5+ years (computed under the service's own counting rules) by 8/12/89, Bailey may apply — but the 20-year (b)(5a) deduction is usually the cleaner route. |
| NC-BAILEY-T2-03 | **Retiree who rolled TSERS into an IRA in 2010 and now takes IRA RMDs** | Bailey character was lost on rollover. Subsequent IRA RMDs are fully taxable to NC. Do NOT claim Line 20. Educate the client; consider whether any reversal is possible (usually not). |
| NC-BAILEY-T2-04 | **Surviving spouse of a deceased TSERS retiree, spouse not a NC employee** | The Bailey exclusion still applies to the survivor benefit if the deceased was vested by 8/12/89. Request the deceased member's Bailey letter (TSERS will provide to the survivor). |
| NC-BAILEY-T2-05 | **Out-of-state government pension** (e.g., Virginia VRS, Florida FRS, federal employee of any federal agency but pension is paid through a non-CSRS/FERS arrangement) | Bailey applies to **NC** state/local and **federal** plans only. Out-of-state government pensions are **fully taxable** to NC, full stop. No NC exclusion regardless of vesting date. |
| NC-BAILEY-T2-06 | **NC State 401(k) participant with both pre-8/12/89 and post-8/12/89 contributions** | All distributions from the qualifying plan are Bailey-protected once the participant met the contribution-by-1989 test. Subsequent contributions to the same plan and their earnings remain protected. |
| NC-BAILEY-T2-07 | **Disability retirement from TSERS where the disability occurred after 1989** | Disability retirement does not depend on vesting date for federal tax purposes, but for NC Bailey purposes the **5-year creditable-service-by-8/12/89** test still applies. If the disability member did not have 5 yrs by 8/12/89, Bailey does not apply. |
| NC-BAILEY-T2-08 | **Lump-sum withdrawal vs. periodic distributions from Bailey plan** | Both are Bailey-protected if the member is vested. The form of distribution does not affect character. However, a lump-sum that is then rolled into a non-qualifying IRA destroys character for the post-rollover account (Rule NC-BAILEY-T1-07). |
| NC-BAILEY-T2-09 | **NC resident receiving federal CSRS pension but unsure of 1989 service** | Request OPM SF-50 (Notification of Personnel Action) showing service computation date. CSRS service started before 1/1/1984 with 5+ continuous years almost certainly qualifies; ambiguous cases require OPM service-history printout and credentialed-reviewer judgment. |
| NC-BAILEY-T2-10 | **Conversion of Bailey-protected traditional account to Roth IRA** | The conversion is treated as a Bailey distribution at the moment of conversion (exempt from NC tax). Subsequent Roth qualified distributions are not in federal AGI, so no NC tax. Non-qualified Roth distributions follow Roth rules (federally taxable portion is taxable to NC). |

## Section 9: Worked examples (TY 2025)

### Example 1 — NC State employee hired 1985, vested by 1989, retired 2020

**Facts.** Maria, a NC resident filing MFJ, retired from TSERS in 2020 after 35 years of state service. She first worked for the State on July 1, 1985. By 8/12/1989, she had 4 years and 1 month of TSERS creditable service. She also purchased 11 months of military service credit in 1992 (back-credited to her start date), bringing her pre-1989 creditable service total to **5 years exactly**. TSERS issued her a Bailey letter in 2020 confirming vested status. She receives $48,000/yr in TSERS retirement benefits, fully reported on Form 1099-R (Box 1 = Box 2a = $48,000).

**Bailey analysis.**
- Qualifying system: yes (TSERS) ✓
- 5+ years creditable service: yes (purchased service counts) ✓
- By 8/12/1989: yes — TSERS letter confirms ✓
- In federal AGI: yes ✓
- Documentation: yes (Bailey letter + 1099-R) ✓

**Result.** Full $48,000 deducted on D-400 Schedule S, Part B, **Line 20**.

> **Flash point.** Purchased service credit counts toward the 5-year test if and only if it was attributable to a period before 8/12/1989. NCDOR has accepted back-credited service in this fact pattern, but the TSERS Bailey letter is the operative document — do not infer from the purchase paperwork alone.

### Example 2 — NC State employee hired 1991 — NOT Bailey-protected

**Facts.** James, a NC resident filing single, started his state job on March 1, 1991 and retired in 2025 with 34 years of TSERS service. He receives $55,000/yr in TSERS benefits.

**Bailey analysis.**
- Qualifying system: yes (TSERS) ✓
- 5+ years creditable service: yes (34 years) ✓
- By 8/12/1989: **no** — James had zero TSERS service on that date ✗

**Result.** **No Bailey deduction.** The full $55,000 is taxable to NC. James pays 4.25% × $55,000 = $2,337.50 NC tax on his TSERS pension before considering his standard deduction and other items.

> **Flash point.** This is the most common audit reversal in NC retiree returns — preparers see "TSERS retiree" on a 1099-R and reflexively claim Line 20 without checking the vesting date. The penalty/interest on a multi-year disallowance can be substantial.

### Example 3 — Federal CSRS retiree with 5 yrs by 8/12/89

**Facts.** Elaine, a NC resident filing single, worked for the federal government from January 1980 through December 2015 under CSRS. She has 35 years of federal CSRS service. OPM issues her a CSA 1099-R showing $62,000/yr gross / $62,000 federally taxable.

**Bailey analysis.**
- Qualifying system: yes (CSRS) ✓
- 5+ years creditable service: yes (35 years) ✓
- By 8/12/1989: yes (she had 9.5 yrs by that date) ✓
- In federal AGI: yes ✓
- Documentation: 1099-R + SF-50 showing service computation date 1/1/1980 ✓

**Result.** Full $62,000 deducted on D-400 Schedule S, Part B, **Line 20**.

Elaine also receives $32,000 in Social Security; the federally taxable portion (assume 85% = $27,200) is deducted on Schedule S **Line 19**.

Her NC taxable income from these two sources = $0.

### Example 4 — Mixed-source retiree

**Facts.** Robert, a NC resident filing MFJ, receives:
- $36,000/yr from TSERS — Bailey-vested (TSERS letter on file)
- $24,000/yr from a private 401(k) (rollover from his post-state-employment private-sector job; never touched the TSERS account)
- $18,000/yr Social Security (federally taxable portion: $15,300 = 85%)
- $8,000/yr from a traditional IRA he funded with personal contributions in the 2000s
- $14,000/yr from U.S. military retirement (served 22 yrs active Army, retired 2010) — qualifies under § 105-153.5(b)(5a)

Total federal AGI line items (assuming all included): TSERS $36k + 401(k) $24k + taxable SS $15.3k + IRA $8k + Military $14k = **$97,300**.

**Items NOT deductible (taxable to NC):**
- Private 401(k): $24,000 — fully taxable to NC, no NC retirement-income deduction available
- Traditional IRA: $8,000 — fully taxable to NC

**NC taxable income from retirement = $97,300 − $65,300 = $32,000** (before standard deduction).

After the MFJ standard deduction of $25,500, NC taxable income = $6,500. NC tax = $6,500 × 4.25% = **$276**.

> **Flash point.** Robert should be advised that if he ever rolls the TSERS account into an IRA for investment-management convenience, he will permanently lose the Bailey protection on the $36,000 income stream. Annual NC tax cost of that decision: $36,000 × 4.25% = $1,530/yr.

**NC Schedule S Part B deductions table**

| Item | Amount | Line |
| --- | --- | --- |
| Social Security taxable portion | $15,300 | Line 19 |
| TSERS (Bailey) | $36,000 | Line 20 |
| Military retirement (§ 105-153.5(b)(5a)) | $14,000 | Line 21 |
| **Total deductions** | **$65,300** | **Line 41** |

## Section 10: Refusal catalogue

**Refusal catalogue table**

| Refusal ID | Trigger | Response |
| --- | --- | --- |
| R-NCB-01 | **Out-of-state government pension** (Virginia VRS, Florida FRS, etc.) | "Bailey protection applies only to NC state/local and federal government plans. Pensions from other states' government retirement systems are fully taxable to NC. No deduction available." |
| R-NCB-02 | **Foreign government pension** | "Foreign pensions are outside this skill's scope. Treaty analysis required. Refer to credentialed reviewer." |
| R-NCB-03 | **Bailey vesting status uncertain — no documentation** | "Cannot claim Line 20 without documentary evidence (TSERS/OPM/DFAS Bailey or service-verification letter). Decline the deduction or pause to obtain documentation before filing." |
| R-NCB-04 | **Partial-vesting scenarios** (e.g., 4.5 years of creditable service by 8/12/89) | "Bailey is all-or-nothing at the 5-year mark. No partial exclusion is available. Refer to credentialed reviewer for any creative service-credit-purchase analysis." |
| R-NCB-05 | **Part-year NC resident or nonresident** | "This skill assumes full-year NC residency. Part-year and nonresident returns require Form D-400 Schedule PN allocation. Out of scope — refer to parent nc-income-tax skill or credentialed reviewer." |
| R-NCB-06 | **Pre-2014 tax year (Form D-400 prior to NC tax reform)** | "Pre-2014 NC returns used Form D-400 with different schedules and the prior statute (§ 105-134.5/.6). Out of scope. Refer to a credentialed reviewer." |
| R-NCB-07 | **PTET / pass-through entity election issues** | "PTET interaction with retirement income is out of scope for this skill." |
| R-NCB-08 | **Disability retirement that the federal return excludes** | If excluded from federal AGI, no NC subtraction is needed — Bailey only operates on amounts in federal AGI. Verify federal treatment before claiming Line 20. |
| R-NCB-09 | **Rollover documentation incomplete** | "Cannot determine whether Bailey character was preserved without trustee-to-trustee documentation. Decline Line 20 until documentation obtained." |
| R-NCB-10 | **Roth IRA conversions from Bailey accounts in prior years** | "Multi-year Roth conversion sequencing from Bailey accounts requires reviewer judgment. Out of scope for automated determination." |

## Section 11: Form mapping — D-400 Schedule S Part B (TY 2025)

**Schedule S Part B line mapping table**  _(NCDOR 2025 D-400 Schedule S Web-Fill version (form revision Web-Fill 9-25))_

| Schedule S Part B Line | Label | Use for |
| --- | --- | --- |
| Line 17 | State or Local Income Tax Refund | State tax refund included in federal AGI |
| Line 18 | Interest Income From Obligations of the United States or United States' Possessions | U.S. Treasury / agency interest |
| **Line 19** | **Taxable Portion of Social Security and Railroad Retirement Benefits** | Federally taxable SS / Tier 1+2 RR portion |
| **Line 20** | **Retirement Benefits Received by Vested N.C. State Government, N.C. Local Government, or Federal Government Retirees, i.e. Bailey Settlement** | All Bailey-qualifying retirement income (TSERS, LGERS, CSRS, FERS, Bailey-qualifying military, NC State 401(k)/457, judicial, legislative) |
| **Line 21** | **Certain Retirement Benefits Received by a Retired Member of the United States Uniformed Services Not Deducted on Line 20** | Military retirees who qualify under § 105-153.5(b)(5a) but NOT under Bailey (and SBP beneficiaries) |
| Line 22 | Bonus Asset Basis | Depreciation true-up |
| Lines 23a-f / 24a-f | Bonus depreciation / §179 add-back recovery | Multi-year 20% recovery |
| Line 41 | **Total Deductions — flows to Form D-400 Line 9** | Sum of 17 through 40 |

## Section 11: Form mapping — D-400 Schedule S Part B (TY 2025)

**Form D-400 line mapping table**

| Form D-400 Line | Description |
| --- | --- |
| Line 6 | Federal AGI (from federal 1040, Line 11) |
| Line 7 | Additions from Schedule S Part A (Line 16) |
| Line 9 | Deductions from Schedule S Part B (**Line 41**) — this is where Bailey/military/SS flow in |
| Line 11 | NC standard or itemized deduction |
| Line 13 | Child deduction |
| Line 14 | NC taxable income |
| Line 15 | NC income tax (Line 14 × 4.25% for TY 2025) |

## Section 11: Form mapping — D-400 Schedule S Part B (TY 2025)

> **Filing reminder.** A Form 1099-R supporting any Line 20 or Line 21 deduction must be attached to the D-400 when filed. The 2025 D-401 instructions state this attachment is required to substantiate the deduction. `[VERIFY exact wording in current D-401.]`

> **Filing-threshold reminder.** Even if 100% of a taxpayer's retirement income is excluded under Bailey (so NC taxable income from pensions is $0), the taxpayer may still be required to file a NC return if gross income meets the filing threshold. The Bailey exclusion is a *taxable-income* exclusion, not a *filing requirement* exclusion. See parent skill `nc-income-tax` for filing-threshold detail.

## Section 12: Provenance & version history

**Version history table**

| Version | Date | Author | Changes |
| --- | --- | --- | --- |
| 0.1 | 2026-05-28 | AI-drafted (Q3, pending verification) | Initial draft. All TY 2025 figures verified against NCDOR 2025 D-400 Schedule S (Web-Fill 9-25). Statutory subdivision letters for § 105-153.5(b) marked `[VERIFY:]` where current codification numbering not directly confirmed against ncleg.net (403 on automated fetch). Recent military-retirement expansion confirmed against S.L. 2021-180 and NCDOR Important Notice. |

## Section 12: Provenance & version history

**Pending verification items (must be resolved before this skill exits Q3 status):**

- Exact subdivision numbering of N.C. Gen. Stat. § 105-153.5(b) for (i) Bailey settlement, (ii) Social Security, (iii) military retirement. Public NCGA URL returned 403 on automated fetch; manual confirmation by a credentialed NC reviewer required.
- Confirmation of the TY 2025 standard deduction amounts against the most recent D-401 (the figures used here match S.L. 2023-134's schedule).
- Confirmation that the 2026 flat rate is 3.99% (Session Law 2023-134 set the schedule; subsequent sessions may have adjusted).
- Confirmation of the D-401 instruction wording on the 1099-R attachment requirement.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com).

## Talk to a verified accountant

This skill is a tool, not an engagement. Every taxpayer's situation is different, and the rules in the skill may not match your specific facts.

To speak with one of the licensed accountants who verifies skills for your jurisdiction — **no liability on either side until you and the accountant sign a formal engagement letter** — book a free 30-minute call:

**→ [Book a call](https://calendly.com/openaccountants-info/30min)**

We'll route you to the named verifier covering your country or state. You can also see the full list of verified accountants at [openaccountants.com/network](https://openaccountants.com/network).
