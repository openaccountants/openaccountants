---
name: ct-payroll
description: Tier 2 Connecticut content skill for employer payroll compliance covering tax year 2025. Includes the CT PIT brackets up to 6.99%, CT-W4 state W-4, CT-941 quarterly withholding, CT-W3 annual reconciliation, CT UI wage base $25,000 with rates 0.50-6.20%, CT Paid Leave 0.5% employee-paid contribution effective January 2022, the post-2024 expansion of Paid Sick Leave to all 50+ employer industries, no reciprocal agreement with NY, and the convenience-of-employer rule for CT employers with remote out-of-state workers.
jurisdiction: US-CT
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# CT Payroll

## Connecticut Payroll — Employer Compliance for Tax Year 2025

## 1. Scope

This is a **Tier 2 Connecticut content skill** for employer payroll compliance in the State of Connecticut for tax year 2025. It is loaded by the workflow base whenever a payroll workflow involves a Connecticut employer, a Connecticut resident employee, or wages sourced to Connecticut under the convenience-of-employer rule.

### In scope

- Connecticut Personal Income Tax (CT PIT) withholding, including the 2025 bracket structure topping out at **6.99%** and the supplemental wage rate of **6.99%**.
- Form **CT-W4**, the Connecticut Employee's Withholding Certificate, including withholding codes A through F and the additional withholding amount on Line 2.
- Form **CT-941**, the Connecticut Quarterly Reconciliation of Withholding, including the four quarterly filing deadlines and the weekly/monthly/quarterly remitter categories.
- Form **CT-W3**, the Connecticut Annual Reconciliation of Withholding, due January 31 of the following year.
- Connecticut **Unemployment Insurance (UI)** administered by the Connecticut Department of Labor (CTDOL), including the **$25,000 taxable wage base** for 2025, the experience-rated tax rate range of **0.50% to 6.20%**, and the **2.5% new employer rate**.
- Connecticut **Paid Leave (CTPL)** contributions of **0.5% of wages, employee-paid only**, effective since January 1, 2022, administered by the CT Paid Leave Authority.
- Connecticut **Paid Sick Leave** under Conn. Gen. Stat. §31-57r through §31-57w, including the post-2024 expansion under Public Act 24-8 that broadens coverage from "service workers" only to all industries with **50 or more employees** (phasing in through January 1, 2027 with smaller employers).
- The **Connecticut Family and Medical Leave Act (CT FMLA)**, which runs in parallel to the federal FMLA but is broader in scope, lower in headcount threshold, and the unpaid leave entitlement paired with the CTPL paid benefit.
- The **lack of any reciprocal income tax agreement between Connecticut and New York**, with the practical consequence that CT residents commuting to NY pay both states and claim a credit on CT Form CT-1040.
- The **convenience-of-employer rule** as Connecticut has codified it (Conn. Gen. Stat. §12-711(b)(2)(C)), which mirrors the well-known New York rule and which can pull remote out-of-state workers of CT employers back into the CT tax net.
- Worker classification under the **ABC test** as applied by CTDOL for unemployment purposes (Conn. Gen. Stat. §31-222(a)(1)(B)(ii)).
- The **final pay** rules: discharged employees by next business day, voluntary quits by next regular payday (Conn. Gen. Stat. §31-71c).

### Out of scope

- Connecticut **personal income tax return preparation** (Form CT-1040) for the employee — that is the role of `ct-income-tax`.
- **Federal payroll tax** (Form 941, FUTA, federal income tax withholding) — defer to the federal payroll skill set.
- **Tribal employers** within Connecticut.
- **Connecticut nonresident composite returns** for partnerships and S corporations.
- **Wage garnishments, child support orders, and judgment liens** — these have specific Connecticut procedural rules but are outside this skill's scope.
- **Connecticut SUTA dumping detection** — handled administratively by CTDOL.
- **Pension and 401(k) plan administration** — deferred to the retirement skills.

### Coordination

- For an employee who is a Connecticut resident filing Form CT-1040, hand off to `ct-income-tax` for the personal return.
- For Connecticut sales and use tax on goods or services sold by the employer, hand off to `ct-sales-tax`.
- For the federal payroll forms (W-2, W-3, 941, 940), defer to the federal skill set.
- When a CT employer pays a worker who turns out to be properly classified as an independent contractor under the ABC test, the worker becomes a self-employed taxpayer — hand off to `us-sole-prop-bookkeeping` and the federal Schedule C/SE skills for that worker's return.

## 2. Connecticut Personal Income Tax (CT PIT) Withholding

### 2.1 Statutory basis

- **CT PIT statutory basis and withholding requirement** — Connecticut's personal income tax is imposed under Conn. Gen. Stat. §12-700. Employer withholding is required under §12-705 and implemented by Department of Revenue Services (DRS) regulation Conn. Agencies Regs. §12-705(a)-1 et seq. Every employer that maintains an office or transacts business in Connecticut and pays wages to any resident or nonresident employee for services performed within Connecticut must withhold Connecticut income tax. The starting point is the federal Form W-4 only for federal purposes; Connecticut uses its own Form CT-W4.  _(Conn. Gen. Stat. §12-700, §12-705; Conn. Agencies Regs. §12-705(a)-1 et seq.)_

### 2.2 2025 Connecticut PIT brackets — the structure

Connecticut has a **graduated** income tax with brackets that depend on filing status. For tax year 2025, the rate schedule applies as follows (these are statutory bracket boundaries for the calculation of the tax on Connecticut taxable income, and they are reflected in the withholding tables that DRS publishes in Informational Publication 2025(1)).

**Single / Married Filing Separately**  _(DRS Informational Publication 2025(1))_

| Connecticut Taxable Income | Marginal Rate |
| --- | --- |
| $0 – $10,000 | 2.0% (phased to 3.0% — see note) |
| $10,000 – $50,000 | 4.5% |
| $50,000 – $100,000 | 5.5% |
| $100,000 – $200,000 | 6.0% |
| $200,000 – $250,000 | 6.5% |
| $250,000 – $500,000 | 6.9% |
| Over $500,000 | 6.99% |

**Heads of Household**  _(DRS Informational Publication 2025(1))_

| Connecticut Taxable Income | Marginal Rate |
| --- | --- |
| $0 – $16,000 | 2.0% (phased to 3.0%) |
| $16,000 – $80,000 | 4.5% |
| $80,000 – $160,000 | 5.5% |
| $160,000 – $320,000 | 6.0% |
| $320,000 – $400,000 | 6.5% |
| $400,000 – $800,000 | 6.9% |
| Over $800,000 | 6.99% |

**Married Filing Jointly / Qualifying Surviving Spouse**  _(DRS Informational Publication 2025(1))_

| Connecticut Taxable Income | Marginal Rate |
| --- | --- |
| $0 – $20,000 | 2.0% (phased to 3.0%) |
| $20,000 – $100,000 | 4.5% |
| $100,000 – $200,000 | 5.5% |
| $200,000 – $400,000 | 6.0% |
| $400,000 – $500,000 | 6.5% |
| $500,000 – $1,000,000 | 6.9% |
| Over $1,000,000 | 6.99% |

- **2025 rate cut note** — Public Act 23-204 reduced the bottom two rates: the 3.0% rate dropped to **2.0%** and the 5.0% rate dropped to **4.5%** effective January 1, 2024. These reductions remain in effect for tax year 2025. The description in the user prompt of "brackets 3.0%–6.99%" reflects the pre-2024 schedule. The current 2025 schedule begins at **2.0%**, not 3.0%. The skill follows the actual 2025 schedule for accuracy and flags the discrepancy in case a reviewer is working from older documentation.  _(Public Act 23-204)_
- **3% phase-out** — The **3% phase-out** under Conn. Gen. Stat. §12-700(a)(8) gradually claws back the benefit of the 2.0% bracket once Connecticut AGI crosses the recapture thresholds (CT AGI over $56,500 for single, $100,500 for MFJ, etc.), turning the bottom-bracket rate into an effective 4.5% on the first slice for higher earners. The withholding tables embed this.  _(Conn. Gen. Stat. §12-700(a)(8))_
- **tax recapture** — The **tax recapture** under Conn. Gen. Stat. §12-700(c)(1) further claws back the lower brackets for high earners on a sliding scale, adding $90 increments for each $5,000 of CT AGI above the threshold ($200,000 single / $400,000 MFJ).  _(Conn. Gen. Stat. §12-700(c)(1))_

### 2.3 Supplemental wage rate

- **CT supplemental wage withholding rate** — 6.99% percent (Applies to supplemental wages (bonuses, commissions, severance, retroactive pay) when paid separately from regular wages or not aggregated with regular wages on the employee's most recent regular paycheck; aligns with CT's top marginal bracket.)  _(CT statutory withholding rules)_
- **Aggregated supplemental wages** — If supplemental wages are aggregated with regular wages and there is no identifiable separate payment, the employer uses the regular withholding tables based on the CT-W4 code.  _(CT statutory withholding rules)_

### 2.4 Remitter categories — how often to deposit

**Remitter categories**  _(Conn. Agencies Regs. §12-705(b)-2)_

| Category | Annual Withholding Threshold | Deposit Frequency |
| --- | --- | --- |
| Weekly remitter | More than $10,000 in look-back year | By Wednesday following payday (electronic) |
| Monthly remitter | $2,000 to $10,000 | By 15th of following month |
| Quarterly remitter | Less than $2,000 | With Form CT-941 by last day of month following quarter |

- **Look-back year and electronic payment** — The look-back year is the 12-month period ending June 30 of the prior calendar year. DRS sends a notice each November confirming the remitter category for the following year. All payments must be made **electronically** through the myconneCT portal — DRS no longer accepts paper coupons.  _(Conn. Agencies Regs. §12-705(b)-2)_

## 3. Form CT-W4 — Connecticut Employee's Withholding Certificate

### 3.1 What it is and when it's required

- **CT-W4 requirement** — Form CT-W4 is **distinct from federal Form W-4** and is required from every employee at the start of employment and whenever the employee's withholding situation changes. Connecticut does not piggyback on the federal W-4. An employee who only completes a federal W-4 will default to withholding code **F** ("Single") regardless of their actual filing status.

### 3.2 Withholding codes

The CT-W4 uses a single-letter code that the employer enters into payroll to select the correct table. The codes for 2025 are:

**Withholding codes table**

| Code | Description | Typical Use |
| --- | --- | --- |
| A | Married Filing Jointly, only one spouse works, combined wages under threshold | Single-earner MFJ households |
| B | Married Filing Jointly, both spouses work, combined wages over threshold | Most dual-earner MFJ households |
| C | Married Filing Jointly, both spouses work, combined wages and the higher-earner uses Code C while lower uses Code D | Asymmetric dual-earner |
| D | Married Filing Jointly, both work, lower earner | Spousal companion to Code C |
| E | Head of Household | HoH filers |
| F | Single or Married Filing Separately | Default for unmarried filers and MFS |

### 3.3 Additional withholding and reduced withholding

- **Line 2 and Line 3 adjustments** — **Line 2 — Additional withholding.** The employee may request an extra dollar amount be withheld per pay period. **Line 3 — Reduced withholding.** Less commonly, an employee may request reduced withholding by certifying expected credits, deductions, or losses that will reduce their CT-1040 liability. This requires DRS approval via Form CT-W4P or a similar attestation if the reduction is significant.

### 3.4 Nonresident employees

- **Nonresident CT-W4 handling** — A nonresident employee working in Connecticut completes the CT-W4 in the same way but checks the nonresident box on the form. CT-W4 line 5 (proportion of wages allocable to CT services) is then completed when the nonresident performs services partly in CT and partly outside. The employer withholds only on the CT-source portion. This is the flip side of the convenience-of-employer rule discussed in Section 9.

### 3.5 Recordkeeping

- **CT-W4 recordkeeping period** — The employer retains the CT-W4 for the duration of employment plus **four years** after the last withholding under that certificate. DRS may inspect on audit. If DRS issues a written determination that a particular CT-W4 is invalid (typically because the employee claimed too many adjustments), the employer must withhold at the default rate (Code F, no adjustments) until a replacement certificate is filed.

## 4. Form CT-941 — Quarterly Reconciliation of Withholding

### 4.1 What it is

- **CT-941 purpose** — Form CT-941 is the quarterly reconciliation that every Connecticut withholding employer files, regardless of whether they remit weekly, monthly, or quarterly. It reconciles the amount **withheld** during the quarter, the amount **remitted** during the quarter, and the resulting underpayment or overpayment.

### 4.2 Due dates

**CT-941 due dates**

| Quarter | Period Covered | CT-941 Due Date |
| --- | --- | --- |
| Q1 | January 1 – March 31 | April 30 |
| Q2 | April 1 – June 30 | July 31 |
| Q3 | July 1 – September 30 | October 31 |
| Q4 | October 1 – December 31 | January 31 (following year) |

- **Q4 deadline alignment** — The Q4 deadline aligns with the Form CT-W3 annual reconciliation and the W-2 furnishing deadline.

### 4.3 Filing channel

- **CT-941 filing channel** — CT-941 must be filed electronically through **myconneCT**. Paper filing is allowed only with a hardship waiver granted by DRS in advance — this is rare.

### 4.4 Seasonal employers

- **Zero CT-941 requirement** — A seasonal employer who has no wages in a quarter must still file a CT-941 marked "no wages." Failing to file a zero CT-941 generates a non-filer notice and a penalty under Conn. Gen. Stat. §12-735.  _(Conn. Gen. Stat. §12-735)_

### 4.5 Amended CT-941

- **CT-941X amendment** — To correct a prior CT-941, the employer files Form **CT-941X**. Refund claims must be made within three years from the due date of the return.

## 5. Form CT-W3 — Annual Reconciliation

### 5.1 What it is

- **CT-W3 purpose** — Form CT-W3 (and the related Form CT-W3 HHE for household employers) is the annual reconciliation that ties together the four quarterly CT-941 filings to the total of W-2 Box 17 (Connecticut state tax withheld) reported to the employee. It is the Connecticut counterpart to federal Form W-3.

### 5.2 Due date and filing channel

- **CT-W3 due date and channel** — **Due:** January 31 of the year following the wage year (so 2025 wages reported January 31, 2026). **Channel:** myconneCT, electronic only. **Attachments:** All W-2 Copy 1 forms for Connecticut employees must accompany the CT-W3 electronically.

### 5.3 Reconciliation

- **DRS reconciliation checks** — DRS automatically reconciles: Sum of CT income tax withheld per the four CT-941 forms, Sum of CT income tax withheld per the W-2 Copy 1 attachments, Total remitted through myconneCT during the year. If the three figures do not match, the employer receives an automated notice. Common causes of mismatch: a year-end bonus paid in December but the withholding deposited in January; a Code F default used because a CT-W4 was lost; a refund of overwithheld CT tax to a terminating employee not properly reflected.

### 5.4 1099 reporting

- **CT-1096 requirement** — Connecticut also requires **Form CT-1096** as the annual reconciliation of 1099-NEC, 1099-MISC, and 1099-R reporting where CT tax was withheld or where the payee is a CT resident. This is mainly relevant when the employer pays an independent contractor classified outside the ABC test (see Section 11) and is conducting backup withholding.

## 6. Connecticut Unemployment Insurance (UI)

### 6.1 Statutory basis

- **CT UI statutory basis** — Connecticut UI is governed by the Connecticut Unemployment Compensation Act, Conn. Gen. Stat. §31-222 through §31-274, and administered by the Connecticut Department of Labor (CTDOL).  _(Conn. Gen. Stat. §31-222 through §31-274)_

### 6.2 2025 wage base

- **CT UI taxable wage base 2025** — $25,000 USD per employee per year (One of the higher state wage bases in New England, the result of the 2024 statutory increase that took CT from a long-stagnant $15,000 to a phased-in $25,000 by 2025 under Public Act 21-200 (the "Trust Fund Solvency" legislation). The wage base is indexed to track average annual wages and will continue rising.)  _(Public Act 21-200)_

### 6.3 Rate range and new employer rate

**UI rate components 2025**

| Rate Component | 2025 Value |
| --- | --- |
| Minimum experience-rated rate | **0.50%** |
| Maximum experience-rated rate | **6.20%** |
| New employer rate (non-construction) | **2.5%** (also called the standard rate) |
| New employer rate (construction) | Higher, typically the industry average around 4.5% |
| Fund Solvency Tax | Added on top — 1.4% for 2025 |
| Charged Tax (experience portion) | Variable based on benefit ratio |

- **Effective rate composition and new employer period** — The effective rate an employer sees on the CTDOL "Form UC-1 Tax Rate Notice" combines the **charged tax** (experience-rated portion) and the **fund solvency tax** (flat, currently 1.4%). New employers pay 2.5% until they have enough employment history (typically 3 years) to be experience-rated.

### 6.4 Quarterly reporting — Form UC-2 and UC-5A

**UC-2 and UC-5A forms**

| Form | Purpose | Due |
| --- | --- | --- |
| UC-2 | Employer Contribution Return (computes tax) | Last day of month following quarter end |
| UC-5A | Employee Quarterly Earnings Report (lists each employee and their gross wages) | Same |

- **Filing channel** — Both are filed jointly through the CTDOL **ReEmployCT** portal. Paper filing is no longer accepted.

### 6.5 Successor employer rules

- **Successor employer experience rate inheritance** — When a business acquires substantially all the assets of another CT employer, the successor inherits the predecessor's experience rate under Conn. Gen. Stat. §31-225(g). This prevents "SUTA dumping" — the practice of spinning off a new entity to escape a high experience rate.  _(Conn. Gen. Stat. §31-225(g))_

### 6.6 Voluntary contributions

- **Voluntary contribution deadline** — An employer may make a voluntary contribution to its CTDOL account by March 31 of any year to reduce its experience rate for that year. This is a cash-against-tax tradeoff and only makes sense in narrow circumstances where the contribution buys a rate reduction worth more than the contribution itself.

## 7. Connecticut Paid Leave (CTPL)

### 7.1 Statutory basis and timeline

- **CTPL creation and timeline** — CTPL was created by Public Act 19-25, the Paid Family and Medical Leave Insurance Act, codified at Conn. Gen. Stat. §31-49e through §31-49t. The contribution requirement became effective **January 1, 2021**, and benefits became payable **January 1, 2022**.  _(Public Act 19-25; Conn. Gen. Stat. §31-49e through §31-49t)_

### 7.2 Contribution — 0.5%, employee-paid only

- **CTPL contribution rate** — 0.5% percent of employee wages (Capped each year at the Social Security wage base (for 2025, capped at $168,600 — wages above that are not subject to CTPL contribution). The contribution is entirely employee-paid; the employer does not contribute. The employer's role is solely to withhold the 0.5% from each paycheck and remit to the CT Paid Leave Authority.)

### 7.3 Coverage

- **CTPL coverage scope** — CTPL covers virtually every employer with **one or more employees** in Connecticut. Unlike CT FMLA's job-protection rules, CTPL's contribution and benefit reach is essentially universal. Sole proprietors and the self-employed may opt in voluntarily.

### 7.4 Remittance

- **CTPL remittance schedule** — Contributions are remitted **quarterly** to the CT Paid Leave Authority through the ctpaidleave.org portal. Due dates align with the CT-941 quarterly deadlines (April 30, July 31, October 31, January 31).

### 7.5 Benefits (informational)

- **CTPL benefit structure** — Eligible employees may receive up to **12 weeks** of paid benefits in a 12-month period (plus 2 additional weeks for pregnancy-related incapacitation), paid at a percentage of the employee's average weekly wage capped at 60 times the CT minimum wage. As of 2025, the benefit cap is approximately **$941/week** (60 × $15.69 minimum wage). The Authority pays the benefit directly to the employee — not through the employer's payroll.

### 7.6 Interaction with CT FMLA

- **CTPL and CT FMLA relationship** — CTPL is the **paid benefit**; CT FMLA is the **unpaid job-protected leave**. An employee may take CT FMLA leave and simultaneously collect CTPL benefits. Employers may not require employees to use accrued PTO before CTPL benefits begin (one of the key CTPL distinctions from federal FMLA).

## 8. Connecticut Paid Sick Leave — and the Post-2024 Expansion

### 8.1 Original (2012) law — service workers only

- **Original CT paid sick leave law** — Connecticut became the first U.S. state to require paid sick leave when Public Act 11-52 took effect January 1, 2012, codified at Conn. Gen. Stat. §31-57r through §31-57w. The original law applied only to employers with **50 or more employees** and only required paid sick leave for **"service workers"** — a defined list of approximately 70 occupations heavily weighted toward food service, healthcare, and personal care.  _(Public Act 11-52; Conn. Gen. Stat. §31-57r through §31-57w)_

### 8.2 The Public Act 24-8 expansion

Public Act 24-8 (effective January 1, 2025 for the largest employers, phasing in through January 1, 2027) dramatically expanded the law in two directions:

- **Removed the "service worker" limitation.** All employees of covered employers are now entitled to paid sick leave, regardless of occupation.
- **Phased-in headcount reduction.**

**Phased headcount thresholds**  _(Public Act 24-8)_

| Effective Date | Covered Employer Size |
| --- | --- |
| January 1, 2025 | 25 or more employees |
| January 1, 2026 | 11 or more employees |
| January 1, 2027 | 1 or more employees |

- **2025 threshold note** — For 2025, the threshold is **25 employees** — which is below the original "50 or more" service-worker threshold the user prompt mentioned. By 2027, paid sick leave is universal in Connecticut.  _(Public Act 24-8)_

### 8.3 Accrual

- **Paid sick leave accrual rate** — Employees accrue **1 hour of paid sick leave for every 30 hours worked**, up to a maximum of **40 hours per year**. Carryover of up to 40 hours into the following year is permitted, but the cap of 40 used per year still applies.

### 8.4 Permitted uses

- **Permitted uses of paid sick leave** — - Employee's own illness, injury, or medical appointment. - Care for a family member (defined broadly under PA 24-8 — includes spouse, sibling, parent, grandparent, grandchild, child, and "individuals related by blood or whose close association is the equivalent of a family relationship"). - Absence related to domestic violence or sexual assault. - Closure of the employer's business or the child's school by a public official for a public health emergency.  _(Public Act 24-8)_

### 8.5 Notification

- **Notification requirement** — The employer must provide written notice to each employee at hire of their paid sick leave rights and must display the CTDOL paid sick leave poster.

## 9. The Convenience-of-Employer Rule and Cross-Border Issues

### 9.1 No reciprocal agreement with NY — and the consequences

- **AUDIT FLASH POINT — no reciprocal agreement** — > **AUDIT FLASH POINT.** Connecticut has **NO reciprocal income tax agreement** with **any** neighboring state, including New York, Massachusetts, Rhode Island, or New Jersey. A CT resident commuting to NY pays both states' income tax on the same wages, and recovers the duplication only through the **resident credit** on Form CT-1040 Schedule 2 for taxes paid to NY. The credit is limited to the lesser of (a) the tax actually paid to NY on the NY-source wages or (b) the CT tax attributable to those same wages. Because NY's top rate plus NYC tax often exceeds CT's, the practical result is that the CT resident pays NY's higher rate with no CT refund — CT simply forgives its tax on those wages. This is **not** an exemption — the wages still appear on the CT return; the credit just zeros out the CT liability on them.  _(Form CT-1040 Schedule 2)_

### 9.2 The convenience-of-employer rule — CT's version

- **CT convenience-of-employer rule text** — Conn. Gen. Stat. §12-711(b)(2)(C), enacted by Public Act 18-49 and amended several times, contains Connecticut's own **convenience-of-employer** rule. The rule states: "Compensation for personal services rendered by a nonresident individual whose service is rendered for an employer located in this state shall be deemed to be derived from or connected with sources within this state if such compensation is for services rendered for the convenience of the employee rather than for the necessity of the employer." In plain English: if a CT employer has a remote employee who lives in (say) Texas and works from Texas because the employee prefers it (convenience) rather than because the employer requires them to be in Texas (necessity), Connecticut will deem the wages **CT-source** and require CT withholding. The remote employee is then a CT-source nonresident taxpayer.  _(Conn. Gen. Stat. §12-711(b)(2)(C); Public Act 18-49)_
- **Reciprocal trigger design and AUDIT FLASH POINT** — The Connecticut version is **reciprocal** in design — it applies only to nonresidents of CT working remotely for a CT employer when the **employee's home state also imposes a convenience-of-employer rule** on its own employers. The reciprocal trigger means CT's rule "catches" employees in states like New York and Delaware (which do have convenience rules) but generally not employees in pure physical-presence states like Texas, Florida, or California — unless the relevant case law has evolved. > **AUDIT FLASH POINT.** The reciprocal-trigger language is the key. DRS has audited CT employers with remote workers in CofE-rule states (NY, NE, DE, PA, AR) and pulled the wages back into CT. Where the remote worker is in a non-CofE state (TX, FL, CA, WA), DRS has generally **not** asserted CT sourcing, but employers should not assume — there are open audit positions. Always document the necessity-of-employer rationale for any remote arrangement.  _(Conn. Gen. Stat. §12-711(b)(2)(C))_

### 9.3 Practical employer outcomes by scenario

**Practical employer outcomes by scenario table**

| Employee Resident | Works in | CT Tax Treatment |
| --- | --- | --- |
| CT resident | CT | Standard CT withholding on full wages |
| CT resident | NY (commuter) | CT withholds on full wages; employee gets CT credit for NY tax paid on CT-1040 |
| CT resident | Remote from home in CT | Standard CT withholding |
| NY resident | CT (commuter into CT) | CT withholds on CT-source portion (Line 5 CT-W4); NY taxes full wages with NY credit for CT |
| NY resident | Remote from NY for CT employer | **Convenience-of-employer rule may apply** — if remote is for employee convenience, CT may treat as CT-source |
| TX resident | Remote from TX for CT employer | Generally not CT-source (TX has no income tax and no CofE rule); CT does not withhold |

## 10. CT Family and Medical Leave Act (CT FMLA)

### 10.1 Coverage broader than federal FMLA

**CT FMLA vs federal FMLA comparison**  _(Conn. Gen. Stat. §31-51kk through §31-51qq)_

| Dimension | Federal FMLA | CT FMLA (post-2022) |
| --- | --- | --- |
| Employer threshold | 50+ employees in 75-mile radius | **1+ employee in CT** |
| Employee eligibility | 12 months service + 1,250 hours | **3 months of service** |
| Leave entitlement | 12 weeks in 12 months | **12 weeks in 12 months + 2 weeks pregnancy-related incapacitation** |
| Job protection | Yes, with restoration | Yes, with restoration |
| Pay status | Unpaid | Unpaid (but CTPL benefit may apply) |

- **Example of small employer exposure** — A small employer (say, a 5-person CT design studio) is exempt from federal FMLA entirely but is fully subject to CT FMLA. The employee with 3 months of service has the same 12-week job-protected leave right as an employee of a 5,000-person employer.

### 10.2 Permitted reasons

- **CT FMLA permitted reasons** — - Birth, adoption, or foster placement of a child. - Serious health condition of the employee or a covered family member. - Qualifying exigency from a family member's military service. - Service-member family leave (26 weeks for caregiver of an injured servicemember). - **Family violence** — CT FMLA uniquely includes up to 12 days of leave for an employee victim of family violence (Conn. Gen. Stat. §31-51ss).  _(Conn. Gen. Stat. §31-51ss)_

### 10.3 Interaction with CTPL

- **CT FMLA and CTPL coordination** — CT FMLA is the **leave entitlement** (right to take time off and return to job); CTPL is the **wage replacement** benefit. The two are independent statutes that coordinate in practice. Most employees taking CT FMLA also file a CTPL claim with the Authority to receive partial wage replacement during the leave.

## 11. Worker Classification — the ABC Test

### 11.1 Why classification matters for payroll

- **Employee vs contractor obligations** — If a worker is an **employee**, the employer must withhold CT PIT, pay CT UI, withhold CTPL, and provide paid sick leave (where headcount is met). If the worker is an **independent contractor**, none of the above applies, but the employer must issue Form 1099-NEC (and file CT-1096) when payments meet the federal $600 threshold (rising to $2,000 in 2026 under OBBBA — see `us-1099-nec-issuance`). CTDOL is aggressive about reclassification. A single audit can reclassify dozens of contractors as employees retroactively, generating UI tax assessments, CTPL contributions, paid sick leave damages, and the W-2 withholding underpayment.

### 11.2 The CT ABC test (Conn. Gen. Stat. §31-222(a)(1)(B)(ii))

- **ABC test prongs** — For UI purposes, a worker is presumed to be an **employee** unless the putative employer proves **all three** of the following prongs: > **A.** The worker is free from control and direction in connection with the performance of the service, both under the contract for the performance of service and in fact; AND > > **B.** The service is performed either outside the usual course of the business for which the service is performed or outside of all the places of business of the enterprise for which the service is performed; AND > > **C.** The worker is customarily engaged in an independently established trade, occupation, profession or business of the same nature as that involved in the service performed. All three prongs must be proven, by the employer, by a preponderance of the evidence. Failure on any single prong means the worker is an employee.  _(Conn. Gen. Stat. §31-222(a)(1)(B)(ii))_

### 11.3 Prong-by-prong audit checklist

**Prong A — Control:**

- Does the worker set their own schedule?
- Does the worker provide their own tools and equipment?
- Does the worker decide the method and means of performing the work?
- Is the worker subject to performance reviews like an employee?
- Does the worker receive training from the putative employer?

The presence of "method and means" control is fatal. The classic giveaway is a "contractor" who shows up at the employer's office every day at 9:00 a.m., uses the employer's laptop, and is supervised by an employer manager.

**Prong B — Course of business or place of business:**

- Is the service the worker provides part of the **usual course of business** of the putative employer?
- Or, alternatively, is the service performed outside all the places of business of the putative employer?

A web developer for a web development agency fails Prong B even if working from home — web development is the agency's usual course of business. Connecticut applies Prong B strictly; the "place of business" alternative is rarely available because remote work means anywhere can become a place of business.

**Prong C — Independently established:**

- Does the worker have their own business name, EIN, business cards, marketing?
- Does the worker have other clients besides the putative employer?
- Does the worker bear business risk (profit and loss)?
- Has the worker filed Schedule C in prior years?

A worker with one client, no marketing, and no incorporation almost always fails Prong C.

### 11.4 CTDOL audit triggers

- **CTDOL audit triggers list** — - Form 1099-NEC issued for amounts that look like full-time wages ($60,000+ per year to one worker). - Unemployment claim filed by a "former contractor." - Workers' compensation claim filed by a "contractor." - Routine 5-year audit cycle. - Whistleblower complaint to CTDOL Wage & Workplace Standards Division.

### 11.5 Federal/state mismatch

- **Federal vs CT classification mismatch and AUDIT FLASH POINT** — Federal IRS uses the multi-factor common-law test (the "20-factor test" or the modern "behavioral, financial, type-of-relationship" framework). The ABC test is **stricter**. It is therefore possible to be a federal contractor but a CT employee. In that scenario, the employer pays CT UI, withholds CT PIT, and withholds CTPL, while still issuing a 1099-NEC for federal purposes — a documentation nightmare that is best avoided by harmonizing the classification. > **AUDIT FLASH POINT.** The ABC test is the single most common cause of multi-six-figure CTDOL audit assessments against small CT employers. Software companies, design agencies, marketing firms, and home-care businesses that "use 1099 contractors" are the highest-risk industries. Where the worker fails any prong, retroactive assessment can go back 3 years for UI and potentially longer for PIT withholding under the §12-735 fraud window.  _(Conn. Gen. Stat. §12-735)_

## 12. Final Pay and Wage Payment

### 12.1 When final wages are due

- **Final wages timing rules** — Conn. Gen. Stat. §31-71c governs the timing of final wages: **Discharged employee (involuntary termination):** Wages are due **on the business day next succeeding the date of discharge**. If discharged Tuesday, final pay is due Wednesday. **Voluntary quit:** Wages are due on the **next regular payday**. **Layoff:** Same as voluntary quit — by next regular payday. This is one of the strictest discharge-pay timelines in the country. Wage payment violations are subject to **double damages** under Conn. Gen. Stat. §31-72 if the violation is willful. A "willful" violation includes knowing failure to pay, not just intentional bad faith.  _(Conn. Gen. Stat. §31-71c; Conn. Gen. Stat. §31-72)_

### 12.2 What counts as final wages

- **Final wages composition** — - Earned regular wages through the last day worked. - Accrued unused vacation, **if** the employer's policy or contract provides for vacation payout at termination. Connecticut does **not** require vacation payout by statute; it follows the contract or policy. (This is different from California, where vacation must be paid out.) A clear written policy disclaiming payout is enforceable. - Earned but unpaid commissions, per the commission agreement. - Bonuses **only if** the bonus has vested per the bonus plan terms by termination.

### 12.3 Method of final payment

- **Final payment method rule** — The same method the employee was being paid (direct deposit or paper check). The employer cannot force a paper check if the employee was on direct deposit, and cannot force direct deposit if the employee asks for a paper check.

### 12.4 Mailed payment

- **Mailed final wages rule** — An employer may mail the final wages to the employee's last known address. The wages are deemed "paid" on the date of mailing (postmark) for purposes of the §31-71c deadline, not on the date of receipt — though prudent practice is to mail at least one business day before the deadline.  _(Conn. Gen. Stat. §31-71c)_

## 13. Worked Example 1 — CT Employer with NY Commuters

**Facts.** Cobalt Analytics LLC is a Hartford, Connecticut-based data analytics consultancy with 35 employees. Twelve employees live in Westchester County, New York, and commute daily to the Hartford office. None of the NY-resident employees work from home for Cobalt; they all work in the Hartford office five days a week. Two CT-resident employees work in Cobalt's small satellite office in midtown Manhattan and commute the other direction. Annual wages range from $80,000 to $250,000.

**Question.** How does Cobalt handle payroll for the NY commuters (NY residents working in CT) and for the CT commuters (CT residents working in NY)?

**Analysis — NY residents commuting into CT.**

1. **CT-W4.** Each NY resident employee files a CT-W4 marked "nonresident" with Line 5 showing 100% of services performed in CT (because they all work in the Hartford office). The withholding code is selected based on their filing status.
2. **CT withholding.** Cobalt withholds CT PIT on the full wages, because the wages are CT-source under the physical-presence rule (services performed in CT).
3. **NY withholding.** New York requires withholding on wages paid to NY residents regardless of where the work is done, **but** the NY employer must register as a NY withholding agent. If Cobalt is not registered in NY and has no NY presence other than the satellite office, the NY residents must make their own NY estimated payments — the employer is not required to withhold for NY unless registered there. Because Cobalt has a NY satellite, it likely **is** registered in NY and **must** withhold NY tax on the wages of NY residents (NY treats all wages of NY residents as NY-source for residency purposes).
4. **Reciprocal credit.** On Form IT-201 (NY resident return), the NY residents claim a **NY credit for tax paid to CT** under N.Y. Tax Law §620 for the CT tax actually paid on the CT-source wages. The credit is limited.
5. **Net result for NY-resident employee.** Employee pays whichever is **higher** — the NY tax rate or the CT tax rate — because the higher state effectively keeps the difference. For a $150,000 earner, CT's marginal rate is about 6.0% and NY's is about 6.85% — so NY keeps ~0.85% net after credit.

**Analysis — CT residents commuting into NY (the satellite office).**

1. **NY withholding.** NY requires withholding on the **NY-source portion** of wages of a nonresident, which for a physical commuter is 100%. Cobalt withholds NY tax on these wages.
2. **CT withholding.** Connecticut requires withholding on wages of a CT resident regardless of where earned. So Cobalt also withholds CT PIT on the full wages.
3. **Apparent double withholding.** Without coordination, both states are withholding on the same wages. The employer should **not** reduce CT withholding to zero — Connecticut requires the employer to withhold on CT-resident wages and credit is claimed on the resident's CT-1040, not at the withholding stage. (Form CT-W4 line 5 is for nonresidents, not for CT residents working out of state.)
4. **CT-1040 credit.** On Form CT-1040 Schedule 2, the CT resident claims a credit for the NY tax paid. The credit is limited to the lesser of (a) NY tax on the NY-source income or (b) CT tax on that same income. Because NY's rate is higher, the credit equals the full CT tax on those wages, effectively zeroing out CT's claim. CT does not refund the NY excess; the employee absorbs the difference.
5. **Practical employer guidance.** Recommend that the CT-resident commuter file a CT-W4 with reduced withholding (Line 3) — they can use IP 2024(8) to compute the reduction such that CT withholding approximates the net CT liability after credit (which may be zero on these wages). However, getting Line 3 reduction approved requires substantiation and is often more trouble than just letting the employee receive a CT refund at filing.

**Connecticut withholding totals for Cobalt's payroll.** Cobalt withholds CT PIT on:

- 21 CT residents (CT office or satellite-commuter) — full wages.
- 12 NY residents physically working in CT — full wages (CT-source).
- 2 CT residents working at NY satellite — full wages (CT taxes residents on worldwide income).

Cobalt's CT-941 reflects withholding on all 35 employees. Its Form NY-IT-2104 (NY counterpart withholding) reflects withholding on the 14 NY-source employees (12 NY residents + 2 CT residents whose work is NY-source).

**CTPL.** Cobalt withholds the 0.5% CTPL contribution from every employee **physically working in CT**, because CTPL coverage follows the location of work. The 2 CT residents working in the NY satellite — these wages are NY-source for CTPL purposes and not subject to CT Paid Leave contribution. The 12 NY residents working in Hartford — these wages **are** subject to CTPL, even though the employee is a NY resident.

**CT UI.** Cobalt reports the 12 NY residents working in CT to **Connecticut** for UI (work performed in CT), and reports the 2 CT residents working in NY to **New York** for UI (work performed in NY). UI follows the physical location of work under the multi-state "localization of work" test.

## 14. Worked Example 2 — CT Employer with TX Remote Workers

**Facts.** Lighthouse Software Inc. is a Stamford, Connecticut C-corporation with a 100-person headquarters. In 2025, Lighthouse opens a fully remote engineering position. It hires Priya Sharma, a Texas resident in Austin. Priya works exclusively from her home in Austin. She visits the Stamford office twice a year for company offsites (3 days each). Her salary is $180,000.

**Question.** Does Lighthouse withhold CT income tax on Priya's wages? CTPL? Report her to CT UI?

**Analysis.**

1. **CT PIT withholding — convenience-of-employer rule analysis.**
   - Priya is a Texas resident. Texas has **no state income tax** and no convenience-of-employer rule of its own. Connecticut's reciprocal-trigger formulation means CT's CofE rule generally **does not** apply to TX remote workers — there's no TX rule to reciprocate against.
   - Priya's wages are sourced based on **physical place of performance**: Austin, TX, for 359 days; Stamford, CT, for 6 days (2 offsites × 3 days).
   - CT may assert that the 6 Stamford days create CT-source wages: $180,000 × 6/365 ≈ $2,959 of CT-source compensation.
   - For amounts under the de minimis threshold (CT's 14-day rule for nonresident business travelers under Conn. Gen. Stat. §12-711(b)(2)(D) for certain industries), or under the practical materiality threshold DRS applies, Lighthouse may treat the 6-day allocation as immaterial and not withhold. But the safer position is to withhold CT PIT on the 6-day CT-source portion via Priya filing a CT-W4 as a nonresident with Line 5 = 1.65%.
   - **Conclusion:** Lighthouse does **not** withhold CT PIT on the bulk of Priya's wages. It may, conservatively, withhold on the CT-source offsite days. Priya files a CT-1040NR/PY if she has CT-source income above the filing threshold.

2. **CTPL contribution.**
   - CTPL coverage follows the physical place where the employee works for the employer. Priya works in TX, so her wages are not subject to CTPL contribution. Lighthouse does not withhold the 0.5% on Priya's pay.

3. **CT UI.**
   - UI follows the "localization of work" test from the Federal Unemployment Tax Act §3306. Priya's work is localized in Texas (she works there continuously; the CT offsites are incidental). Lighthouse reports Priya to **Texas Workforce Commission** for UI, not to CTDOL.
   - Lighthouse must register as a TX employer with TWC for this single employee — an annoyance, but unavoidable.

4. **CT paid sick leave.**
   - Lighthouse has 100 employees, so it is over the 25-employee 2025 threshold. But the paid sick leave statute applies to employees working in Connecticut. Priya works in Texas — she is not entitled to CT paid sick leave. (She may have rights under any Texas or local law — but TX has no state paid sick leave statute, and Austin's local ordinance is preempted.)

5. **Convenience-of-employer audit risk.**
   - If DRS audits Lighthouse and asserts the CofE rule against Priya, it would need to show that Priya's remote arrangement is for her own convenience, not Lighthouse's necessity. Lighthouse should **document** that the remote arrangement is a business necessity — e.g., the role requires expertise that is unavailable in the Stamford labor market, and the position was posted as remote-first, with the offer contingent on a remote arrangement. A well-documented necessity defeats the CofE assertion.
   - If Lighthouse loses the audit, DRS would assert CT PIT on all $180,000 of Priya's wages, plus interest and penalties. With a top marginal CT rate of ~6.5% on her income level, the exposure is roughly $11,700/year per year audited. Over a 3-year audit, ~$35,000 plus interest.

> **AUDIT FLASH POINT.** Maintain a written **remote work agreement** with each out-of-state remote employee specifying that the remote arrangement is a business necessity for the employer (recruiting reach, specific expertise unavailable locally, business continuity). Without this, the CofE rule audit becomes much harder to defeat. This is especially important for high-income remote employees where the dollar exposure is large.

## 15. Worked Example 3 — Contractor Classification under the ABC Test

**Facts.** Nutmeg Design Studio LLC is a small CT-based graphic design firm with 4 W-2 employees. In 2025 it engages "Jordan," a freelance illustrator, for a 9-month book illustration project. Jordan is paid $90,000 over the engagement on 1099-NEC. Jordan works from his home in New Haven, CT, on his own laptop and tools, sets his own hours, has 4 other clients during the year, runs an LLC called "Jordan Illustration LLC" with his own EIN, and bills Nutmeg by invoice every two weeks. Nutmeg gives Jordan project specs at the start of each chapter but does not supervise his day-to-day work.

In 2026, Jordan files for unemployment in CT after Nutmeg ends the engagement. CTDOL opens a contractor-classification audit of Nutmeg.

**Question.** Will Jordan be reclassified as an employee under the ABC test?

**Analysis.**

**Prong A — Control.**

- Jordan sets his own schedule: **passes**.
- Jordan uses his own tools (laptop, Wacom tablet, Adobe software on his license): **passes**.
- Nutmeg provides project specs but does not direct method or means: **passes**.
- No performance reviews; just invoice-and-deliverable: **passes**.

Conclusion on Prong A: Nutmeg likely passes.

**Prong B — Outside usual course of business OR outside places of business.**

- Nutmeg is a graphic design firm. Book illustration is graphic-design-adjacent. Is illustration "outside the usual course of business" of a graphic design firm?
- This is the **danger prong**. Most CTDOL hearing officers would view illustration as **within** the usual course of business of a graphic design firm. Even though Nutmeg's 4 W-2 employees are general designers (not illustrators), the firm holds itself out as offering design services that include illustration.
- Alternative test: outside the places of business. Jordan works from his New Haven home, not from Nutmeg's office. If "places of business" is read narrowly (Nutmeg's office only), Jordan **passes** under the alternative.
- CTDOL's interpretation has been mixed. The CT Supreme Court in *Standard Oil of Connecticut, Inc. v. Administrator* (2016) held that the disjunctive "or" in Prong B is real — meeting **either** alternative satisfies the prong. So Jordan working from his home, not from Nutmeg's office, **may** satisfy Prong B's "outside the places of business" alternative.
- **Conclusion on Prong B:** Pass under the *Standard Oil* alternative-place reading, but this is the audit battleground.

**Prong C — Independently established business.**

- Jordan has an LLC with EIN: **passes**.
- Jordan has 4 other clients: **passes strongly**.
- Jordan markets his services (own website, portfolio): **passes**.
- Jordan bears business risk (could lose money if project goes over budget on a flat fee): **passes**.
- Jordan files Schedule C: **passes**.

Conclusion on Prong C: clean pass.

**Overall.** Jordan is **likely** correctly classified as an independent contractor. Prongs A and C are clean. Prong B is the only risk, and *Standard Oil* gives Nutmeg a defensible position. CTDOL will probably find for Nutmeg on this fact pattern — but the audit will be a non-trivial defense.

**Counterfactual.** Suppose Jordan had **only Nutmeg** as a client and worked exclusively for Nutmeg for 9 months. Prong C now fails (no independently established business — Jordan is functionally a Nutmeg employee), and the entire analysis collapses regardless of Prong A and B. Jordan is reclassified as an employee, and Nutmeg owes:

- CT UI tax on $90,000 (× 2.5% new-employer-equivalent or Nutmeg's actual rate) ≈ $2,250 — but only on the wage base of $25,000, so actual UI ≈ $625.
- CTPL contribution (0.5% × $90,000) = $450 — but this was the employee's contribution, not the employer's. CTDOL might still assess against Nutmeg under failure-to-withhold theory.
- CT PIT withholding underpayment — could be substantial if Jordan didn't pay quarterly estimates. Penalties under §12-735.
- Federal employment tax exposure (FICA, FUTA) — separate IRS exposure.
- Paid sick leave back-damages — Nutmeg has 5 employees including Jordan now, still below the 2025 threshold of 25, so no exposure there for 2025 specifically.

> **AUDIT FLASH POINT.** The single-client contractor is the **highest-risk** fact pattern. Even with a clean Prong A and a strong LLC structure on Prong C, a contractor whose entire income comes from one putative employer will fail Prong C in any rigorous audit. Diversify or convert to employment.

## 16. Self-Checks

Before delivering a Connecticut payroll work product to the reviewer, confirm each of the following:

1. [ ] Each Connecticut employee has a current **CT-W4** on file (federal W-4 alone is insufficient).
2. [ ] The withholding code (A through F) selected on the CT-W4 matches the employee's filing status and is propagated correctly into the payroll system.
3. [ ] CT PIT withholding deposits are made via myconneCT under the correct remitter category (weekly / monthly / quarterly) based on the prior-year look-back.
4. [ ] Form **CT-941** has been filed for each completed quarter by the last day of the following month.
5. [ ] Form **CT-W3** with W-2 Copy 1s is filed by January 31 following the wage year.
6. [ ] CTDOL **UC-2 and UC-5A** quarterly returns are filed in ReEmployCT; UI tax is computed on the **$25,000** 2025 wage base.
7. [ ] **CTPL 0.5%** is withheld from every CT-working employee's pay, capped at the Social Security wage base, and remitted quarterly to ctpaidleave.org.
8. [ ] For employers with **25+ employees in 2025** (or 11+ in 2026, 1+ in 2027), the paid sick leave policy and accrual tracking are in place.
9. [ ] For each remote out-of-state worker of a CT employer, a **written necessity-of-employer documentation** is on file to defeat any future CofE audit.
10. [ ] Every Form 1099-NEC contractor relationship has been tested against the **ABC test** with documented Prong A, B, and C analysis.
11. [ ] Final pay is processed within Conn. Gen. Stat. §31-71c timelines: next business day for discharge, next regular payday for quit.
12. [ ] For CT-resident employees commuting to NY, the **CT-1040 Schedule 2 credit** mechanism is understood — CT withholding is NOT reduced to zero at source.
13. [ ] For NY-resident employees commuting to CT, the **CT-W4 nonresident** box and Line 5 allocation are completed properly.
14. [ ] **CT-1096** is filed where the employer paid CT-source 1099 income to a CT resident or withheld CT tax from a 1099 payment.

## 17. Summary Table — Connecticut Payroll Obligations at a Glance

**Summary table of CT payroll obligations**

| Obligation | Form/Channel | Frequency | Due Date |
| --- | --- | --- | --- |
| CT PIT deposit (weekly remitter) | myconneCT EFT | Per pay | Wednesday after payday |
| CT PIT deposit (monthly) | myconneCT EFT | Monthly | 15th of following month |
| CT PIT reconciliation | CT-941 via myconneCT | Quarterly | Last day of month after quarter |
| Annual CT PIT reconciliation | CT-W3 + W-2 Copy 1 | Annual | January 31 |
| 1099 reconciliation | CT-1096 + 1099 Copy 1 | Annual | January 31 |
| CT UI quarterly | UC-2 + UC-5A in ReEmployCT | Quarterly | Last day of month after quarter |
| CT Paid Leave | ctpaidleave.org | Quarterly | Last day of month after quarter |
| Paid Sick Leave accrual | Internal tracking | Per pay | N/A (poster + records required) |
| New hire reporting | CT New Hire Reporting | Per hire | Within 20 days of hire |
| Final wages — discharge | Direct deposit / check | One-time | Next business day |
| Final wages — voluntary quit | Direct deposit / check | One-time | Next regular payday |

## 18. Statutory and Regulatory Citation Index

- Conn. Gen. Stat. §12-700 — CT personal income tax imposition.
- Conn. Gen. Stat. §12-705 — Employer withholding requirement.
- Conn. Gen. Stat. §12-711(b)(2)(C) — Convenience-of-employer rule for nonresidents.
- Conn. Gen. Stat. §12-735 — Penalty for failure to file/pay withholding.
- Conn. Gen. Stat. §31-57r through §31-57w — Paid Sick Leave.
- Conn. Gen. Stat. §31-49e through §31-49t — CT Paid Leave (CTPL).
- Conn. Gen. Stat. §31-51kk through §31-51qq — CT FMLA.
- Conn. Gen. Stat. §31-71c — Final wages timing.
- Conn. Gen. Stat. §31-72 — Double damages for wage violations.
- Conn. Gen. Stat. §31-222(a)(1)(B)(ii) — ABC test for UI.
- Conn. Gen. Stat. §31-225 — UI experience rating; successor employer.
- Public Act 11-52 (2011) — Original Paid Sick Leave Act.
- Public Act 19-25 (2019) — Paid Family and Medical Leave Insurance Act.
- Public Act 21-200 (2021) — UI Trust Fund Solvency, wage base increases.
- Public Act 23-204 (2023) — 2024+ rate reductions to 2.0% / 4.5%.
- Public Act 24-8 (2024) — Paid Sick Leave expansion to all industries, phased headcount reduction.
- DRS Informational Publication 2025(1) — Connecticut Employer's Tax Guide.
- DRS Informational Publication 2025(7) — Withholding Calculation Rules.
- *Standard Oil of Connecticut, Inc. v. Administrator, Unemployment Compensation Act*, 320 Conn. 611 (2016) — ABC test Prong B "or" disjunctive reading.

## 19. Refusals

- **Skill refusal scope** — This skill does **not** produce final filings. It produces reviewer briefs and worksheets that a Connecticut-credentialed reviewer (CPA, EA, or attorney) signs off on before any return reaches DRS, CTDOL, or the CT Paid Leave Authority. This skill does **not** advise on: - Connecticut tribal employment. - Multi-state apportionment for employees working in 3+ states regularly. - Connecticut nonresident athlete or entertainer withholding (separate regime). - Wage garnishment computation under specific court orders. - Workers' compensation classification (separate from UI ABC analysis; defer to a CT WC attorney). - Public Act 25 or later changes that may post-date the 2025-11-15 last-updated date — verify against current DRS and CTDOL guidance before filing.

## End of Connecticut Payroll Skill, version 0.1, last updated 2025-11-15.

End of Connecticut Payroll Skill, version 0.1, last updated 2025-11-15.

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
