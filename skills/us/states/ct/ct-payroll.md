---
name: ct-payroll
description: Use for Connecticut 2026 employer withholding, CT-W4/CT-941/CT-W3, SUI, CT Paid Leave, paid sick leave, cross-border workers, classification and final pay.
version: "0.3"
jurisdiction: US-CT
tax_year: 2026
last_updated: 2026-11-14
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
category: state-tax
type: computation
domain: payroll
---

# Connecticut payroll: withholding, unemployment and retained employment obligations

> **General reference only.** Written by Codex. Not reviewed by an accountant. Obtain qualified professional review before filing, paying or taking a tax position.

> **Circular 230 section 10.37:** Apply relevant law to the taxpayer's facts, evaluate reasonable assumptions and relevant circumstances, and obtain professional review of federal tax implications. Federal computations belong to linked federal owner skills.

**Answer first.** Compute state withholding with the actual 2026 Circular CT tables and the employee's CT-W4 code. Separately apply the employer's SUI notice to the first **$27,000** of each employee's covered 2026 wages. The 2026 new-employer SUI rate is **1.9% total**, not the old 2.5%. Paid Leave is a separate employee deduction. [2026 Circular CT](https://portal.ct.gov/-/media/drs/publications/pubsip/2026/ip-2026-1.pdf); [2026 CTDOL tax notice](https://portal.ct.gov/dol/divisions/unemployment-insurance-tax/information-on-unemployment-tax-rate-for-calendar-year-2026?language=en_US).

## Scope

Ordinary Connecticut wage withholding and state unemployment insurance, plus the existing skill's CTPL, sick leave, CTFMLA, worker-classification, cross-border and final-pay topics. Covers 2026; historic 2025 cases are identified explicitly. `us-form-941-940-payroll` owns federal withholding, FICA/FUTA, federal wage bases and federal returns; federal figures are not repeated here. `ct-income-tax` owns annual personal tax, `ct-sales-tax` sales/use, and `ct-corporate-tax` corporation tax. Connecticut unemployment uses CTDOL ReEmployCT; withholding uses DRS myconneCT; CTPL uses the Paid Leave Authority. These are separate filings/payments.

Excluded computations: Connecticut tribal employment, regular work in three or more states, nonresident athlete/entertainer withholding, federal payroll, other states' tax and UI, workers' compensation, pension withholding, garnishments, union-specific rules and litigation. Do not interpret a state classification decision as automatically settling every federal or labor-law test.

## Ask the client first

1. Entity, DRS/CTDOL/CTPL registrations, CT operations, employee count/location and acquisitions/successor history.
2. Each employee's residence, workdays/remote arrangement, current CT-W4/CT-W4NA and other-state withholding evidence.
3. Pay frequency, taxable wages, bonuses/commissions/benefits, year-to-date wages and prior payroll corrections.
4. DRS remitter notice/lookback, CTDOL rate notice, UI localization and CTPL/private-plan eligibility.
5. Hires/rehire dates, leave/PTO policies, employee leave records, contractor evidence and terminations.
6. Prior returns, deposits, W-2/1099 reconciliations, notices, extensions/waivers and payment confirmations.

## The method, step by step

### 1. Withholding obligation and the 2026 calculation

An employer maintaining an office or transacting business in Connecticut and paying covered resident/nonresident wages follows section 12-705 and Circular CT. Connecticut requires its own CT-W4, separately from federal W-4. Use the actual DRS 2026 tables or the sixteen-step annualized calculation; DRS states **there is no percentage method** for Connecticut wage withholding. A top-bracket percentage is not an ordinary payroll calculation. [Circular CT, withholding requirements and TPG-211 appendix](https://portal.ct.gov/-/media/drs/publications/pubsip/2026/ip-2026-1.pdf).

Annualize the period's wages by the number of annual pay periods. Table A uses annualized salary and the withholding code to find the personal exemption. Subtract it to obtain annualized taxable income; if nonpositive, initial withholding is zero and proceed to certificate adjustments. Otherwise use Table B initial tax, add Table C's **2% Tax Rate Phase-Out Add-Back** and Table D recapture (both based on annualized salary and code), and multiply the sum by **1 minus Table E personal-credit decimal**. Divide by annual pay periods; apply CT-W4 line 2 additional or line 3 reduced withholding, never below zero. Code D has zero exemption and zero personal credit. Codes A/D/F use the single-style Table B; B uses head-of-household; C uses joint. Do not use the annual-return table's filing status instead of the payroll code. [TPG-211, pages 1-6](https://portal.ct.gov/-/media/drs/publications/pubsip/2026/ip-2026-1.pdf).

The rate structure retained from the old skill is 2%, 4.5%, 5.5%, 6%, 6.5%, 6.9% and 6.99%. The single-style taxable-income boundaries are $10,000/$50,000/$100,000/$200,000/$250,000/$500,000; joint boundaries double these and head-of-household boundaries multiply them by 1.6. **These brackets alone are insufficient**: phased exemptions, phase-out addback, recapture and personal credits are compulsory. The old references to a “3% phase-out” and a universal $90 recapture step were incomplete: the current source names the 2% phase-out and supplies code-specific stepped Tables C/D. `ct-income-tax` retains the full annual-return bands; use the payroll-specific tables for wages. [2026 Tables A-E](https://portal.ct.gov/-/media/drs/publications/pubsip/2026/ip-2026-1.pdf).

### 2. CT-W4 codes, adjustments and nonresidents

| Code | Current CT-W4 use, subject to the certificate's precise conditions | Official source |
|---|---|---|
| A | MFS with expected gross income above $12,000, or both-working MFJ with combined gross income above $24,000 through $100,500 | [wh](https://portal.ct.gov/-/media/drs/publications/pubsip/2026/ip-2026-1.pdf) |
| B | Head of household above $19,000 gross income | [wh](https://portal.ct.gov/-/media/drs/publications/pubsip/2026/ip-2026-1.pdf) |
| C | MFJ spouse not employed and gross income above $24,000; qualifying surviving spouse above $24,000 | [wh](https://portal.ct.gov/-/media/drs/publications/pubsip/2026/ip-2026-1.pdf) |
| D | Both-working MFJ above $100,500; also the highest-withholding election for substantial other/nonwage income | [wh](https://portal.ct.gov/-/media/drs/publications/pubsip/2026/ip-2026-1.pdf) |
| E | Exempt/no withholding under the stated income conditions or qualifying MSRRA exemption | [wh](https://portal.ct.gov/-/media/drs/publications/pubsip/2026/ip-2026-1.pdf) |
| F | Single above $15,000 gross income | [wh](https://portal.ct.gov/-/media/drs/publications/pubsip/2026/ip-2026-1.pdf) |

For income-based Code E, certificate ceilings are MFS $12,000; single $15,000; head of household $19,000; joint/qualifying surviving spouse $24,000. Do not select E solely because the employee wants no withholding. Missing CT-W4 requires **6.99% with no exemption**, rather than the old asserted Code F default. Annual exempt certificates expire; if not renewed by February 15, apply the source's following-day withholding rule. Obtain a new certificate within ten days of relevant changes. Line 2 adds a per-period dollar amount and line 3 reduces it subject to the instructions; **CT-W4P is a pension certificate, not a wage reduction approval form**. DRS-invalidated certificates require the DRS-directed treatment. Retain the current certificate and follow any written DRS instruction. [CT-W4 instructions and employer certificate rules](https://portal.ct.gov/-/media/drs/publications/pubsip/2026/ip-2026-1.pdf).

A nonresident working partly inside and outside Connecticut uses **Form CT-W4NA**, a separate apportionment certificate, or adequate current employer records. Compute withholding on the full wage and multiply by the Connecticut service percentage. Absent the certificate or reliable records, withhold on the full wage. Count working days, not 365 calendar days; the form explains partial days and ancillary activities. Adjust when facts change; year-end actual source allocation can differ from estimates. The old CT-W4 “line 5” apportionment instruction actually belongs to CT-W4NA. [CT-W4NA and accompanying instructions](https://portal.ct.gov/-/media/drs/publications/pubsip/2026/ip-2026-1.pdf).

Nonresident compensation for services in Connecticut on **not more than fifteen days** generally falls under the source/withholding exception described in Circular CT. Once the employee exceeds fifteen days, withhold on **all** Connecticut-service compensation including the first fifteen days, subject to the rule's stated exclusions and other source-income facts. This is not an informal materiality rule or a fourteen-day rule. [Nonresident fifteen-day rule](https://portal.ct.gov/-/media/drs/publications/pubsip/2026/ip-2026-1.pdf).

### 3. Supplemental wages

For a bonus/commission/overtime/sales award paid with regular wages, compute withholding on the aggregate for the payroll period. For a separately identified payment, the Circular CT method combines it with the regular wages for the relevant/current or preceding payroll period, computes total withholding, and subtracts withholding on regular wages as directed. Where no tax was withheld on regular wages, follow the combined calculation. **There is no general 6.99% flat supplemental-wage election** in these instructions; that percentage appears in the missing-certificate rule. [Supplemental Compensation](https://portal.ct.gov/-/media/drs/publications/pubsip/2026/ip-2026-1.pdf).

### 4. Deposits, CT-941, CT-W3 and corrections

| Remitter category | Lookback withholding amount | Ordinary deadline | Official source |
|---|---|---|---|
| Quarterly | At most $2,000 | Last day of month after quarter | [wh](https://portal.ct.gov/-/media/drs/publications/pubsip/2026/ip-2026-1.pdf) |
| Monthly | More than $2,000 through $10,000 | Fifteenth of following month | [wh](https://portal.ct.gov/-/media/drs/publications/pubsip/2026/ip-2026-1.pdf) |
| Weekly | More than $10,000 | Wednesday following the Saturday-Friday weekly period | [wh](https://portal.ct.gov/-/media/drs/publications/pubsip/2026/ip-2026-1.pdf) |

The lookback is the twelve months ending June 30 of the prior calendar year; 2026 uses the period ending June 30, 2025. Follow the DRS category notice; new employers generally start quarterly. A weekly remitter paying Saturday-Tuesday reaches the **second Wednesday after payday**; Wednesday-Friday payroll reaches the next Wednesday. The old blanket “Wednesday following payday” could accelerate or misstate the actual period. Holidays/weekends follow Circular CT; do not use return extensions for deposits. Electronic filing/payment is required unless a granted DRS-EWVR waiver applies. [Remitter classifications, lookback and payment calendar](https://portal.ct.gov/-/media/drs/publications/pubsip/2026/ip-2026-1.pdf).

File CT-941 quarterly, including zero withholding unless the account has an approved seasonal, annual, household or agricultural exception. Quarter-end dates ordinarily produce April 30, July 31, October 31 and January 31 returns, subject to nonbusiness-day adjustment. If all tax was timely deposited and no balance remains, the source allows **ten additional days to file the return**, not to pay. Seasonal employers must meet the actual designation/instruction conditions; simply stopping payroll does not cancel the filing duty. [CT-941 filing rules](https://portal.ct.gov/-/media/drs/publications/pubsip/2026/ip-2026-1.pdf).

CT-W3 annually reconciles wages/Connecticut withholding with W-2s and CT-941 totals. Submit electronically by January 31 following the year, subject to calendar adjustment, and retain employee delivery/filing evidence. Reconcile each employee's wages and withholding to payroll records and deposits, investigate differences, and correct the applicable period. CT-1096 and reportable 1099s are a **separate** reporting stream, not automatically part of CT-W3. The old CT-941X amendment claim and detailed 1099 filing thresholds are not verified here; use myconneCT's current amended-return procedure and the current information-return specifications before submitting a correction. Final closure requires the final CT-941/CT-W3 and W-2s and closure of the DRS account; separately notify CTDOL if applicable. [Annual reconciliation, records and cancellation instructions](https://portal.ct.gov/-/media/drs/publications/pubsip/2026/ip-2026-1.pdf).

### 5. State unemployment insurance, registration and localization

Register/report/pay through **ReEmployCT**, separately from DRS. Determine whether services are covered, including statutory exclusions and the ordered multistate tests: localized service first, then base of operations, direction/control and residence under the handbook conditions. Employee residence alone does not allocate UI, and short incidental visits do not necessarily move a localized job. Report total gross wages each quarter while taxing only wages within the annual base for the same employer, subject to successor/prior-state-wage rules. Do not deduct employer UI from the employee. [CTDOL Employer Handbook, coverage/localization and taxable wages](https://portal.ct.gov/dol/-/media/dol/2022-new-design-system/about/divisions/unemployment-insurance-tax/updated-employer-guide-april-23-2026.pdf).

| 2026 component | Rate/amount | Official source |
|---|---|---|
| Annual taxable wage base | $27,000 per employee; prior 2025 base was $26,100 | [ui](https://portal.ct.gov/dol/divisions/unemployment-insurance-tax/information-on-unemployment-tax-rate-for-calendar-year-2026?language=en_US) |
| New-employer total rate | 1.9%; do not add the solvency percentage again | [ui](https://portal.ct.gov/dol/divisions/unemployment-insurance-tax/information-on-unemployment-tax-rate-for-calendar-year-2026?language=en_US) |
| Fund solvency rate | 1.0% | [ui](https://portal.ct.gov/dol/divisions/unemployment-insurance-tax/information-on-unemployment-tax-rate-for-calendar-year-2026?language=en_US) |
| Experience-rated total contribution range | 1.1%-9.9%; use the employer's actual notice | [ui](https://portal.ct.gov/dol/divisions/unemployment-insurance-tax/information-on-unemployment-tax-rate-for-calendar-year-2026?language=en_US) |
| Preliminary charged rate | Statutory minimum 0.1%, maximum 10%; 2026 divisor 1.125 yields effective maximum 8.9% before solvency tax | [ui](https://portal.ct.gov/dol/divisions/unemployment-insurance-tax/information-on-unemployment-tax-rate-for-calendar-year-2026?language=en_US) |

The actual 2026 notice takes the benefit ratio, converts it to a preliminary charged rate, divides by **1.125**, rounds **up** to the next tenth of one percent, then adds 1% solvency tax. The notice also supplies a qualifying industry-sector benefit-ratio reduction; use the issued rate rather than rebuilding a client's rate from incomplete data. The 2026 handbook still illustrates the 2024 $25,000 base; the dated **2026 tax notice controls** the current base and rate. The old 2.5%, 0.5%-6.2%, separate construction estimate and 1.4% solvency assertions are not 2026 instructions. [Actual 2026 notice and example](https://portal.ct.gov/dol/divisions/unemployment-insurance-tax/information-on-unemployment-tax-rate-for-calendar-year-2026?language=en_US).

The retained UC-2 contribution-return and UC-5A wage-report topics correspond to the employer tax/employee wage reporting jobs now performed in ReEmployCT. Quarter reports/contributions are ordinarily due the last day of the next month, with calendar adjustments. Report all wages even after the base is exhausted and respond promptly to separation/earnings verification requests. Acquisition/successor rules can transfer liability, experience and wage-base history; the handbook includes exceptions where no assets/common control transfer. Do not promise a new-business rate merely because a new legal entity is formed. The old claimed **March 31 voluntary-contribution rate-buydown deadline is Not yet confirmed**; no payment recommendation relies on it. [Quarterly reports, tax liability and successor employers](https://portal.ct.gov/dol/-/media/dol/2022-new-design-system/about/divisions/unemployment-insurance-tax/updated-employer-guide-april-23-2026.pdf).

### 6. Connecticut Paid Leave (CTPL)

CTPL contributions began January 1, 2021 and benefits January 1, 2022. The Authority's current page expressly maintains **0.5% for 2026**, employee-funded on subject wages up to the federal Social Security contribution/benefit base. `us-form-941-940-payroll` owns that federal year's cap; the old $168,600 asserted 2025 cap is not reused. Employers deduct/remit and register; there is no employer match. The same current page includes total-wage/in-kind/FICA-exclusion instructions. [Official Authority contribution instructions](https://www.ctpaidleave.org/remit-contributions); [Sections 31-49e and 31-49g](https://www.cga.ct.gov/current/pub/chap_557.htm).

Coverage generally includes private employers with one or more Connecticut employees, with statutory public-employer/school exceptions and negotiated covered-public-employee provisions. Connecticut-resident sole proprietors/self-employed people may opt in under the statutory enrollment rules. Do not call coverage universal or determine it solely by residence. Approved private plans have exemption conditions; obtain the approval rather than merely recording that the employer offers PTO. [Sections 31-49e, 31-49g and 31-49m](https://www.cga.ct.gov/current/pub/chap_557.htm); [Authority employer instructions](https://www.ctpaidleave.org/for-businesses-and-employers/i-am-an-employer).

Remit through the Authority's portal or approved batch process, separately from CT-941/UI. The current Authority says contributions are **due at quarter end** (March 31, June 30, September 30, December 31), with no penalties/interest if submitted by the last day of the following month. This distinguishes the statutory/administrative due date from the grace period; the old skill called the grace-period dates the due dates. The page describes 1% monthly noncompounding interest and a single late penalty up to 10% or $50, whichever greater. Keep the quarter confirmation and contribution reconciliation. [Contribution Due Dates and Calculating Interest and Penalties](https://www.ctpaidleave.org/remit-contributions).

CTPL provides wage replacement, not automatic job protection. Statutory benefits are up to twelve weeks in twelve months, plus two for pregnancy-related incapacitation. The formula is 95% of base weekly earnings up to forty times the current minimum fair wage, plus 60% above that breakpoint, capped at sixty times that wage and subject to statutory solvency provisions. The old approximately $941 weekly cap is stale; no unverified current dollar cap is supplied. Eligibility includes the statutory $2,325 highest-quarter subject earnings and current/recent employment or opted-in status. The Authority, rather than an employer's ordinary wage payroll, administers benefits. [Sections 31-49e and 31-49g](https://www.cga.ct.gov/current/pub/chap_557.htm).

### 7. Paid sick leave and CTFMLA

The historic 2012 sick-leave topic is retained as history: the old fifty-worker/service-worker regime is superseded for current coverage. Current phased employer thresholds are **25+ Connecticut employees from 2025, 11+ from 2026 and 1+ from 2027**, based on the January 1 payroll week under the current FAQ. Occupation is no longer the old service-worker gate. Seasonal employees working 120 days or fewer and specified construction multiemployer arrangements have exceptions; the “all employers in 2027” shorthand remains subject to statutory definitions. [CTDOL Paid Sick Leave FAQs, updated September 23, 2026](https://portal.ct.gov/dol/divisions/legal/connecticut-leave-programs/paid-sick-leave-faqs); [Sections 31-57r through 31-57w](https://www.cga.ct.gov/current/pub/chap_557.htm).

Accrue one hour per thirty hours actually worked up to forty hours/year; use begins after 120 calendar days of employment. Carry up to forty unused hours, or provide the lawful frontloaded alternative available at the year's start; the annual use entitlement is forty hours unless the employer offers more. Exempt employees are normally treated as working forty hours weekly or their shorter normal schedule, without extra accrual for overtime beyond forty. Keep records at least three years. Reasons include employee/family illness, preventive care and wellness, public-health closure/exposure, and family violence/sexual assault, under the broad family definition. Provide the required individual notice and poster; do not impose prohibited documentation/replacement-worker conditions. [Accrual, carryover, use, records and notice FAQs](https://portal.ct.gov/dol/divisions/legal/connecticut-leave-programs/paid-sick-leave-faqs).

CTFMLA generally covers employers with one or more employees, including the state, but excludes municipalities, school boards and nonpublic elementary/secondary schools except specified school paraprofessionals. An employee generally needs three consecutive months' employment (thirteen weeks); the old federal 1,250-hour/50-worker tests do not set Connecticut eligibility. It provides twelve workweeks in a twelve-month period plus two for pregnancy-related incapacitation and up to twenty-six in a single twelve-month military-caregiver period. Reasons include qualifying own/family serious health conditions, birth/adoption/foster placement, organ/bone-marrow donation and military exigency/caregiving. Apply certification, notice and restoration requirements. [CTDOL CTFMLA FAQs](https://portal.ct.gov/dolui/fmla-faqs).

CTFMLA is generally unpaid; accrued paid leave can be substituted at employee request or employer requirement, while the employee may preserve **up to two weeks** of accrued paid leave. The old categorical claim that employers cannot require PTO before CTPL is not a safe statement of this coordination rule. Determine CTFMLA job protection separately from CTPL benefit eligibility and federal FMLA. Do not infer that approval for wage replacement itself guarantees restoration. [Questions 8-10 and leave-coordination provisions](https://portal.ct.gov/dolui/fmla-faqs).

**Family-violence or sexual-assault leave is a separate entitlement under section 31-51ss.** It covers an employer engaged in business with three or more employees, including the state and political subdivisions. An employee who is a victim must be allowed reasonably necessary leave for medical care/counseling, victim services, relocation, or related civil/criminal proceedings. The employer may limit **unpaid** leave to twelve days per calendar year. The section does not itself require paid leave beyond the employee's existing entitlement, and unpaid leave remains available if paid leave is exhausted or unavailable. Other statutory leave and employment/collective-agreement rights are preserved. [Section 31-51ss(a), (b), (e) and (f)](https://www.cga.ct.gov/current/pub/chap_557.htm#sec_31-51ss).

For foreseeable leave, an employer may require advance notice of no more than seven days; otherwise notice is as soon as practicable. Follow subsection (d)'s signed certification and permitted supporting-record rules; keep the records confidential subject to subsection (g)'s limited disclosure exceptions and employee notice. Discharge, penalties, threats or coercion violating this section can support a civil action within 180 days, with reinstatement/damages and a prevailing employee's reasonable attorney fee. Refer disputed entitlement, documentation, confidentiality or retaliation promptly. These documentation provisions differ from the separate paid-sick-leave rule above. [Section 31-51ss(c), (d), (g) and (h), full section read 2026-11-14](https://www.cga.ct.gov/current/pub/chap_557.htm#sec_31-51ss).

### 8. Cross-border commuters and convenience rule

Connecticut has no simple New York reciprocity exemption. Nonresidents physically working in Connecticut ordinarily have Connecticut-source wages, subject to the fifteen-day rule. A Connecticut resident working in another taxing state can have Connecticut withholding **reduced by qualifying other-state withholding** where the employer transacts business/maintains an office in both states and the source conditions apply: calculate Connecticut withholding, allocate to the outside-state service and withhold the excess over that other state's withholding, plus Connecticut-service withholding. The result can be zero. Do not require full double withholding merely because the employee is a Connecticut resident. Final other-state tax credits are limited separately on the annual return. [Residents Employed Outside Connecticut](https://portal.ct.gov/-/media/drs/publications/pubsip/2026/ip-2026-1.pdf); `ct-income-tax`.

The convenience-of-employer test is reciprocal: residents of a state applying such a test may face similar Connecticut sourcing for work for a Connecticut employer. It is not a rule taxing every out-of-state remote worker merely because headquarters is in Connecticut. Keep the residence, home-state-rule, actual workday, employer-necessity and remote-agreement facts. Physical workday allocation and CT-W4NA remain necessary; an employer's “remote” label does not by itself settle source income. Foreign-state tax/return conclusions need that state's owner skill. [Convenience of the Employer Test and CT-W4NA](https://portal.ct.gov/-/media/drs/publications/pubsip/2026/ip-2026-1.pdf).

### 9. Worker classification, ABC evidence and audits

Connecticut UI presumes covered service employment unless the employer establishes all three statutory ABC elements: **A**, freedom from direction/control under contract and in fact; **B**, work outside the enterprise's usual course **or** outside all its places of business; **C**, an independently established trade/occupation/profession/business of the same nature. The disjunctive B alternatives both matter. An LLC, invoice, federal 1099 or home office does not decide the test. [Employer Handbook, Employment section](https://portal.ct.gov/dol/-/media/dol/2022-new-design-system/about/divisions/unemployment-insurance-tax/updated-employer-guide-april-23-2026.pdf); [Section 31-222(a)(1)(B)(ii)](https://www.cga.ct.gov/current/pub/chap_567.htm).

For A, collect actual schedule/method/tool/training/supervision evidence. For B, describe the usual business and every relevant place of business; do not automatically reject the outside-place alternative because work is within the usual course, or automatically accept a contractor's home as outside all places. For C, examine marketing, other clients, business continuity, licenses, capital/tools and profit/loss risk. A single client is a relevant fact, **not an automatic statutory failure**. The prior *Standard Oil of Connecticut, Inc. v. Administrator* (2016) citation is retained as an unresolved case-law reference: the full opinion was not read, so its precise holding is **Not yet confirmed** and no case-specific safe harbor is claimed.

Federal common-law classification and the state UI ABC test may differ; refer the resulting forms/withholding coordination rather than automatically issuing a federal 1099 alongside state employee treatment. The former $60,000 audit flag, routine five-year audit cycle, “most common”/multi-six-figure assessment claims and blanket three-year UI exposure window are **Not yet confirmed**, not compliance rules. Respond to an actual notice with employment records, contracts, invoices, client evidence and payroll/tax histories; obtain professional representation for an assessment.

### 10. Final pay and wage payment

Section 31-71c requires discharged employees' wages by the **next business day**; employees who quit receive wages by the next regular payday through usual channels or mail; layoffs use the next regular payday. Distinguish those events. Section 31-76k requires accrued fringe-benefit payout where the employer policy/collective agreement provides it. Analyze earned commissions and vested/nondiscretionary bonuses under the contract and wage definition; do not assume every discretionary bonus is wages. [Sections 31-71a, 31-71c and 31-76k](https://www.cga.ct.gov/current/pub/chap_558.htm).

The old “same payment method must always continue” and “postmark always establishes timely final pay” assertions are **Not yet confirmed**; section 31-71c's mailing language does not establish those blanket conclusions. Section 31-72 provides double recovery, fees/costs, with a good-faith-belief defense affecting the recovery measure. It is not confined to the old asserted willful-only standard. Refer disputed termination timing, commission/bonus entitlement, method of payment and wage claims. [Section 31-72 and adjacent wage provisions](https://www.cga.ct.gov/current/pub/chap_558.htm).

## Worked cases

**Case 1, ordinary 2026 withholding and SUI.** Single employee, Code F, $1,000 weekly pay, 52 periods, no other adjustments. Annualized wages $52,000; Table A exemption zero; Table B $2,000 + 5.5% of $2,000 = $2,110; Tables C/D zero; Table E .10; annual withholding $1,899. Period withholding is $36.51923077 before cent rounding. A $10 line 2 election makes it $46.51923077. Separately, a new employer with $26,000 prior covered wages pays SUI on only $1,000 of the current $3,000 wages: $19 at 1.9%. Report all $3,000 gross wages.

```oa-check
name: CT 2026 weekly withholding and SUI
inputs:
  weekly: 1000
  periods: 52
  extra: 10
  prior_wages: 26000
  current_wages: 3000
steps:
  - annual: weekly * periods
  - initial: 2000 + (annual - 50000) * .055
  - annual_tax: initial * .9
  - per_period: annual_tax / periods + extra
  - sui_wages: min(current_wages, max(27000 - prior_wages, 0))
  - sui: sui_wages * .019
expected:
  annual: 52000
  initial: 2110
  annual_tax: 1899
  per_period: 46.51923076923077
  sui_wages: 1000
  sui: 19
```

**Case 2, official experience-rate example and resident credit.** Three years' benefit charges total $1,500 on $30,000 taxable payroll. Ratio 5%; divide the charged rate by 1.125 and round upward to the next 0.1 percentage point, giving 4.5%; add 1% solvency for 5.5% total. This is an illustrative rate computation, not a substitute for the issued notice. Separately, in the source's qualifying resident/outside-state facts, computed CT withholding $160 less other-state withholding $100 leaves $60; computed CT $250 less other-state $300 leaves zero.

```oa-check
name: CT official charged rate and resident reduction
inputs:
  benefits: 1500
  payroll: 30000
  ct_wh: 160
  other_wh: 100
steps:
  - ratio: benefits / payroll
  - charged: ceil((ratio / 1.125) * 1000) / 1000
  - total_rate: charged + .01
  - ct_remaining: max(ct_wh - other_wh, 0)
  - zero_remaining: max(250 - 300, 0)
expected:
  ratio: 0.05
  charged: 0.045
  total_rate: 0.055
  ct_remaining: 60
  zero_remaining: 0
```

**Retained case 3, Cobalt Analytics LLC and commuters.** Cobalt's Hartford consultancy has 35 employees: twelve Westchester, NY residents work in Hartford five days weekly without home work; two Connecticut residents work at the midtown Manhattan satellite; the remaining twenty-one are Connecticut residents working in Connecticut. Wages range $80,000-$250,000. The twelve inbound commuters have ordinary Connecticut-source wages and give CT-W4, with CT-W4NA only where actual allocation is needed. The twenty-one Connecticut workers receive ordinary CT withholding. For the two Connecticut residents at the NY satellite, apply the qualifying other-state withholding reduction above; their CT withholding can be zero, so it is wrong to insist on positive CT withholding for all 35. The old NY tax-rate comparison, IT-201 credit conclusion and “NY-IT-2104 counterpart return” assertion are not supplied as verified New York instructions. Obtain the NY owner skill; a certificate is not automatically a quarterly return. Determine UI localization and CTPL covered service separately for each job, rather than using residence alone or treating every day across a border as a new UI state. Document the satellite, assignments and workday records.

**Retained case 4, Lighthouse Software Inc. and Priya Sharma.** Lighthouse is a Stamford C-corporation with 100 headquarters employees. The historic 2025 case hires Texas-resident Priya Sharma in Austin for a fully remote engineering position at $180,000, with two three-day Stamford offsites (six Connecticut days). If the actual facts meet the nonresident fifteen-day exception and there is no other CT-source trigger, the six days do not require the old “conservative” wage allocation. If allocation becomes necessary, use actual working days, not $180,000 x 6/365, and the separate CT-W4NA. Apply the reciprocal convenience test only after verifying the residence-state rule; no Texas-law conclusion is certified here. Determine localization/CTPL coverage from the actual employment facts and retain the remote agreement and travel records. Connecticut sick leave applies under its own employment-in-state conditions; the historic 2025 employer-size threshold was twenty-five and the 2026 threshold is eleven. Texas registration/UI, Austin ordinance preemption, a guaranteed business-necessity defense and the old $11,700/$35,000 hypothetical tax exposures remain **Not yet confirmed**. A flat marginal rate times the entire salary was not a valid CT tax computation.

**Retained case 5, Nutmeg Design Studio LLC and Jordan.** Nutmeg has four W-2 employees and hired Jordan for a nine-month, $90,000 book-illustration project in 2025. Jordan works at home in New Haven with his own laptop, Wacom tablet and licensed Adobe software, sets hours, has four other clients, his own EIN and Jordan Illustration LLC, invoices every two weeks, and receives chapter specifications without daily supervision. The old case also describes a website/portfolio, business risk and Schedule C filings; retain evidence rather than treating them as established merely because an example states them. In 2026 he claims unemployment. Those facts support investigation of A/C; B still requires the actual usual-course/place-of-business analysis. No automatic “likely win” is promised and the unreviewed *Standard Oil* opinion supplies no safe harbor. If Jordan instead had only Nutmeg as a client, C would need further factual analysis; single-client status alone does not conclusively fail it.

If reclassified, reconstruct the **actual 2025 payroll** with that year's notice and statutory facts; a 2026 audit does not turn 2025 wages into 2026 wages. For an explicitly separate **2026 wage illustration**, $90,000 covered wages at the issued new-employer rate yield SUI $27,000 x 1.9% = $513, not the old $625; CTPL would be $450 if all $90,000 is subject earnings below the actual federal cap. CTPL is the employee contribution and failure-to-withhold recovery requires the applicable law; it is not an extra employer matching tax. Compute state withholding from the actual period/code, not a flat annual estimate, and refer federal employment-tax exposure to its owner. With five counted employees, the firm is below the ordinary 2025 twenty-five and 2026 eleven sick-leave thresholds, subject to the actual counting/coverage rules; the 2027 threshold changes that result prospectively.

```oa-check
name: CT reclassification 2026 illustration only
inputs:
  wages: 90000
  sui_base: 27000
  sui_rate: 0.019
  ctpl_rate: 0.005
steps:
  - sui: min(wages, sui_base) * sui_rate
  - ctpl_below_federal_cap: wages * ctpl_rate
expected:
  sui: 513
  ctpl_below_federal_cap: 450
```

## Self-checks and delivery

Confirm certificates/code and source allocation; recompute a representative ordinary paycheck and bonus; confirm remitter notice and weekly period; reconcile CT-941/CT-W3/W-2/payroll/deposits; separate UI gross versus taxable wages and actual rate notice; reconcile CTPL contributions and cap to its separate portal; review headcount/accrual/leave notices; retain ABC evidence and final-pay dates. Obtain acceptance/payment confirmation for every filing stream, including zero reports and final account closure.

**New hire reporting.** The old simple twenty-day statement needs the statute's channel conditions: section 31-254(b) generally requires new hires within twenty days, but electronic/magnetic reporting is at least twice monthly, with transmissions twelve to sixteen days apart. The handbook's fourteen-day electronic / twenty-day fax/mail description should be implemented as the actual statutory/reporting schedule, not a universal twenty-day electronic delay. Check rehire rules and reportable independent-contractor service agreements of $5,000 or more under the current handbook/statute. [Section 31-254(b)](https://www.cga.ct.gov/current/pub/chap_567.htm) [2026 Employer Handbook, New Hire Reporting](https://portal.ct.gov/dol/-/media/dol/2022-new-design-system/about/divisions/unemployment-insurance-tax/updated-employer-guide-april-23-2026.pdf)

**Records.** DRS requires at least four years after tax becomes due or is paid, whichever later, and a current accurate CT-W4/CT-W4NA at all times. Keep wages/dates, identities, employment periods, withholding, certificates, returns and payments. UI records must be available for CTDOL inspection; sick-leave records have the separate three-year minimum. The old employment-plus-four-years shorthand is not the exact DRS retention test. Apply the longest relevant obligation and any open-notice preservation requirement.

## When to refuse or refer

Refer contested residence/convenience sourcing, disputed classifications, acquisition/experience transfers, federal/state classification conflicts, private-plan exemptions, wage/leave disputes, assessments and late-filing remediation. Do not invent another state's payroll position or estimate audit exposures from a top marginal rate.

## Sources

| Source | Read scope | Read date |
|---|---|---|
| [IP 2026(1), Circular CT](https://portal.ct.gov/-/media/drs/publications/pubsip/2026/ip-2026-1.pdf) | Read for all relevant employer withholding, certificates, nonresident/resident, supplemental, remitter, return, records and 2026 TPG-211 Tables A-E appendix sections. | 2026-11-13 |
| [CTDOL 2026 Unemployment Tax Notice](https://portal.ct.gov/dol/divisions/unemployment-insurance-tax/information-on-unemployment-tax-rate-for-calendar-year-2026?language=en_US) | Read for full dated 2026 tax/rate changes and charged-rate example. | 2026-11-13 |
| [CTDOL Employer Handbook, April 23 2026](https://portal.ct.gov/dol/-/media/dol/2022-new-design-system/about/divisions/unemployment-insurance-tax/updated-employer-guide-april-23-2026.pdf) | Read for coverage/localization, employment ABC, registration, successors, quarterly wages/contributions, new hires and records; stale 2024 base distinguished. | 2026-11-13 |
| [CGA Chapter 567](https://www.cga.ct.gov/current/pub/chap_567.htm) | Read for sections 31-222 ABC and 31-254 new hire reporting with adjacent clauses. | 2026-11-13 |
| [CGA Chapter 557](https://www.cga.ct.gov/current/pub/chap_557.htm) | Read for 31-49e/g/m paid leave definitions/contributions/benefits and paid-sick-leave sections 31-57r-w with adjacent clauses. | 2026-11-13 |
| [CGA section 31-51ss](https://www.cga.ct.gov/current/pub/chap_557.htm#sec_31-51ss) | Read the complete current subsections (a)-(h), amendment history and neighboring section 31-51tt definitions for separate family-violence/sexual-assault leave, coverage, unpaid cap, notice, certification, confidentiality and remedies. | 2026-11-14 |
| [Connecticut Paid Leave Authority, Remit Contributions](https://www.ctpaidleave.org/remit-contributions) | Read for full 2026 rate/cap instructions, due dates versus grace period, payment methods and late charges. | 2026-11-13 |
| [Connecticut Paid Leave Authority, Employers](https://www.ctpaidleave.org/for-businesses-and-employers/i-am-an-employer) | Read for registration, covered employee/employer and private-plan guidance. | 2026-11-13 |
| [CTDOL Paid Sick Leave FAQs](https://portal.ct.gov/dol/divisions/legal/connecticut-leave-programs/paid-sick-leave-faqs) | Read for 2026 coverage, exceptions, accrual/use/carryover/frontloading, records and notices. | 2026-11-13 |
| [CTDOL CTFMLA FAQs](https://portal.ct.gov/dolui/fmla-faqs) | Read for coverage/eligibility, reasons, duration, paid-leave substitution, notice and military caregiver provisions. | 2026-11-13 |
| [CGA Chapter 558](https://www.cga.ct.gov/current/pub/chap_558.htm) | Read for wage definition, final-pay timing, fringe benefits and civil recovery sections 31-71a/c, 31-72 and 31-76k. | 2026-11-13 |

## Not yet confirmed

- CT-941 amendment workflow/form identifier and detailed CT-1096/1099 thresholds need the current specific filing specifications. No unverified CT-941X route is instructed.
- Exact voluntary-contribution eligibility/deadline, special construction-new-employer rate and a blanket three-year UI assessment period were not established from the current notice/handbook.
- Full *Standard Oil* opinion, claimed automatic single-client failure, routine five-year audits, $60,000 audit triggers and generic six-figure assessment prevalence are not verified. The old categorical conclusions are withdrawn as unsafe assumptions.
- Current CTPL weekly dollar cap/minimum-wage amount and federal wage-base number are not repeated; use official benefit determination and the federal owner. Private-plan/public-employer and multistate cases need their actual coverage facts.
- Other-state tax forms/rates/credits, Texas registration and local ordinance conclusions, hypothetical flat-rate tax exposure, final-pay postmark and mandatory same-method claims remain unverified; they are not operational rules.
- Historic statutory/regulatory citations retained for orientation include sections 12-700, 12-705, 12-735, 31-222 through 31-274, 31-49e through 31-49t, 31-51kk through 31-51qq, 31-57r through 31-57w, 31-71c/31-72/31-76k and agency regulations 12-705(a)-1 et seq./12-705(b)-2. Full regulations and every historical public act were not separately reread; current official publications/law listed below support the usable rules.


Retained historical reference register: Public Act 11-52 (2011), Public Act 19-25 (2019), Public Act 21-200 (2021), Public Act 23-204 (2023), Public Act 24-8 (2024), DRS Informational Publication 2025(1), DRS Informational Publication 2025(7) (the old title/version attribution was not reverified), section 12-711(b)(2)(C), section 31-225 and its successor provisions, and *Standard Oil of Connecticut, Inc. v. Administrator, Unemployment Compensation Act*, 320 Conn. 611 (2016). These old citations are preserved, while operative 2026 instructions use the sources actually read above. Full historical act/opinion scope is Not yet confirmed.

Not yet confirmed: old CT-W3 HHE household-specific instructions, CT-1096 January 31 deadline and resident/withheld-payment test across every 1099 type, a three-year withholding-refund deadline, and the asserted automatic DRS reconciliation-notice process were not independently established in the specific current publications. Preserve those subjects for the appropriate account-specific instructions rather than treating the old assertions as filing rules.
