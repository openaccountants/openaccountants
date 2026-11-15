---
name: nz-kiwisaver-esct
description: >
  Use this skill for New Zealand KiwiSaver administration by an employer from 1 April 2026 and employer superannuation contribution tax (ESCT): automatic enrolment and its exceptions, employee deduction rates (3.5% default from 1 April 2026, the retained 4% default, temporary rate reductions), the gross salary or wages base, compulsory employer contributions, savings suspensions, unpaid leave and ACC, opt-outs and refunds, the ESCT rate threshold table and how to calculate ESCT on each contribution. Trigger on KiwiSaver employer, KiwiSaver deduction, employer contribution, opt out, savings suspension, ESCT, employer superannuation contribution tax. PAYE itself is in nz-employer-payroll.
version: 1.0
jurisdiction: NZ
tax_year: 2026
last_updated: 2026-11-14
category: payroll
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: payroll
type: computation
---

# New Zealand KiwiSaver for employers and ESCT (2026-27)

Figures are for tax year 2026, meaning payroll paid from 1 April 2026 to 31 March 2027 (the New Zealand 2026-27 tax year, which Inland Revenue calls the 2027 income year). All amounts are New Zealand dollars. Written by Ryan Duguid on his fork (ryanduguid/openaccountants, rules checked 12 and 13 November 2026) and imported on 14 November 2026. It has not been reviewed by an accountant.

## Scope and who this is for

This skill covers what a New Zealand employer does for KiwiSaver from 1 April 2026: enrolment, employee deductions, compulsory employer contributions, suspensions, opt-outs and refunds, and the ESCT deducted from each employer contribution.

- **Companions:** PAYE, payday filing and penalties are in `nz-employer-payroll`; employee share schemes in `nz-employee-share-schemes`.
- **Does not cover:** complying funds other than as named below, scheme provider rules, cross-border employment and an agreed PAYE alternative to ESCT.

## Ask the client first

- Gross pay and each payment's character. Determine PAYE income and KiwiSaver gross salary or wages separately; allowances, reimbursements and special payments need their own treatment.
- KiwiSaver membership and eligibility, valid deduction-rate instruction, employer contribution agreement (including whether it promises a gross or net-of-ESCT amount) and any valid opt-out, savings-suspension or temporary-rate-reduction notice.
- For ESCT, employment start date, whether the employee worked for this employer throughout the preceding tax year and the relevant salary/wages plus gross employer superannuation contributions.
- Annual PAYE and ESCT figures, any connected employers and the established filing and payment schedules. The $50,000 electronic filing test and $500,000 remittance test serve different purposes.
- Has the employee asked for a temporary rate reduction, or given a savings suspension or opt-out notice, and when?

## The method, step by step

1. **Establish membership and eligibility** for automatic enrolment, with the exceptions.
2. **Fix the employee rate** from a valid instruction, the 3.5% default or the retained 4% default.
3. **Identify the contribution base** (gross salary or wages, which is not the same as PAYE income).
4. **Work out the compulsory employer contribution**, then its ESCT at the employee's ESCT rate.
5. **Handle suspensions, leave, ACC, opt-outs and refunds** as set out below.
6. **Report and pay** with the employment information for the payday (see `nz-employer-payroll`).

### Rates, bands and thresholds

Key figures for payroll paid from 1 April 2026 to 31 March 2027. The detail and conditions are in the sections below.

| Item | Figure | Condition | Source |
| --- | --- | --- | --- |
| Default employee KiwiSaver rate | 3.5% | From 1 April 2026 (was 3%); a 4% default is kept in the cases set out below | https://www.ird.govt.nz/kiwisaver-changes |
| Compulsory employer contribution | 3.5% of gross salary or wages | From 1 April 2026; may match an approved temporary rate reduction | https://www.ird.govt.nz/kiwisaver-changes |
| Default rate from 1 April 2028 | 4% | Employee and employer | https://www.ird.govt.nz/kiwisaver-changes |
| Temporary rate reduction | 3 to 12 months | Employee applies to Inland Revenue | https://www.ird.govt.nz/kiwisaver-changes |
| ESCT rate, threshold amount $0 to $18,720 | 10.5% | From 1 April 2025; threshold amount is salary or wages plus gross employer contributions | https://www.ird.govt.nz/-/media/project/ir/home/documents/digital-service-providers/software-providers/payroll-calculations-business-rules-specifications/payroll-calculations-and-business-rules-specification.pdf?modified=20260401012317 |
| ESCT rate, $18,721 to $64,200 | 17.5% | same | https://www.ird.govt.nz/-/media/project/ir/home/documents/digital-service-providers/software-providers/payroll-calculations-business-rules-specifications/payroll-calculations-and-business-rules-specification.pdf?modified=20260401012317 |
| ESCT rate, $64,201 to $93,720 | 30% | same | https://www.ird.govt.nz/-/media/project/ir/home/documents/digital-service-providers/software-providers/payroll-calculations-business-rules-specifications/payroll-calculations-and-business-rules-specification.pdf?modified=20260401012317 |
| ESCT rate, $93,721 to $216,000 | 33% | same | https://www.ird.govt.nz/-/media/project/ir/home/documents/digital-service-providers/software-providers/payroll-calculations-business-rules-specifications/payroll-calculations-and-business-rules-specification.pdf?modified=20260401012317 |
| ESCT rate, $216,001 upwards | 39% | same | https://www.ird.govt.nz/-/media/project/ir/home/documents/digital-service-providers/software-providers/payroll-calculations-business-rules-specifications/payroll-calculations-and-business-rules-specification.pdf?modified=20260401012317 |


### KiwiSaver from 1 April 2026

For ordinary post-2009 default cases, the employee deduction and minimum compulsory employer contribution increased from 3% to **3.5% for paydays on or after 1 April 2026**. The payday determines the rate for the whole payment when a period straddles 1 April; do not prorate by days worked. A surviving historical 4% employee default is addressed below. Existing valid elections of 4%, 6%, 8% or 10% remain available. [S7](https://www.ird.govt.nz/kiwisaver-changes), [S45, subsection (3B)](https://www.legislation.govt.nz/act/public/2006/40/en/latest/sections/DLM379037/), [S50, subsection (4B)](https://www.legislation.govt.nz/act/public/2006/40/en/latest/sections/DLM1233474/)

### Establish membership and automatic-enrolment eligibility

Membership, automatic enrolment and compulsory employer-contribution eligibility are separate questions. For the ordinary case, establish that the person normally lives in New Zealand and is a citizen or entitled to remain indefinitely, and that the employer is within the Act. A temporary visitor, student or work permit does not establish indefinite entitlement. The State services overseas exception and other cross-border cases need their own checks. [S41](https://www.legislation.govt.nz/act/public/2006/40/en/latest/sections/DLM378821/), [KS4, PDF page 6](https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir1---ir99/ks4/ks4.pdf?modified=20260129195326)

Automatic enrolment ordinarily concerns a new employee aged **18 or older and under 65** at the start of employment, with a non-exempt employer and no applicable exception. It does not automatically enrol a 16- or 17-year-old. An under-18 person joins through a provider; an existing member supplies their membership and deduction information rather than being enrolled again. Membership can continue beyond 65 even where compulsory employer contributions cease. [S42](https://www.legislation.govt.nz/act/public/2006/40/en/latest/sections/DLM378830/), [S44](https://www.legislation.govt.nz/act/public/2006/40/en/latest/sections/DLM378843/), [KS4, PDF pages 6-11](https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir1---ir99/ks4/ks4.pdf?modified=20260129195326)

Check the exceptions before treating any new starter as automatically enrolled. A contract for no more than 28 continuous days is temporary for this purpose; count calendar days of employment, not shifts. If that employment continues, the temporary exclusion ends on day 29, described in section 12(2)(b) as the 28th day after employment started. Casual agricultural employment and qualifying irregular/intermittent employment with holiday pay have separate statutory tests. Section 14 also excludes existing members and specified situations such as private domestic service, election-day work and employment without required PAYE withholding. This is not an exhaustive classification checklist; resolve the actual section 12/14 exception, secondment or exempt-employer status first. [S43](https://www.legislation.govt.nz/act/public/2006/40/en/latest/sections/DLM378834/), [S44](https://www.legislation.govt.nz/act/public/2006/40/en/latest/sections/DLM378843/), [KS4, PDF page 7](https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir1---ir99/ks4/ks4.pdf?modified=20260129195326)

Give a person who is automatically enrolled the KiwiSaver information pack within **7 days** of starting. Collect the applicable KS2 deduction information and retain it; do not send KS2 to IRD. Give IRD the applicable new-employee KiwiSaver details using IR346K/myIR or payroll software no later than the first employment-information return is due. Coordinate this with the separate new-employee information deadline in Section 5. Start required deductions from the first payment for an automatically enrolled employee; for an existing member or an IRD direction, section 60 applies to payments calculated after the employer receives the relevant notice. Obtain a valid savings-suspension notice before omitting otherwise required deductions. [S34](https://www.ird.govt.nz/kiwisaver/kiwisaver-for-employers/starting-employees-in-kiwisaver), [S35](https://www.ird.govt.nz/kiwisaver/kiwisaver-for-employers/starting-employees-in-kiwisaver/auto-enrol-employees-into-kiwisaver), [S49](https://www.legislation.govt.nz/act/public/2006/40/en/latest/sections/DLM379032/), [KS4, PDF pages 8-11](https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir1---ir99/ks4/ks4.pdf?modified=20260129195326)

### Employee rates, changes and temporary reductions

Use the valid KS2, written rate instruction or IRD notice. The ordinary elected choices are **3.5%, 4%, 6%, 8% and 10%** of KiwiSaver gross salary or wages. Apply a valid change to the first payment calculated after receipt; ordinary changes must be at least **92 days** apart unless the employer agrees to a shorter interval. Do not backdate missed employee deductions when acting on IRD's start instruction. A possible employer-contribution arrears obligation is a separate question and is not cancelled by that employee-deduction instruction. [S8](https://www.ird.govt.nz/kiwisaver/kiwisaver-for-employers/contributions-and-deductions/kiwisaver-deductions-from-employee-pay), [S45, subsections (2)-(4)](https://www.legislation.govt.nz/act/public/2006/40/en/latest/sections/DLM379037/), [KS4, PDF page 14](https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir1---ir99/ks4/ks4.pdf?modified=20260129195326)

Do not assume every employee without a new election defaults to 3.5%. Section 64(1)(ab) retains a **4% default** where section 60(1)(a), (b) or (c) first applied to this employer in respect of this employee before 1 April 2009, subject to the statutory alternatives and any overriding election or valid temporary reduction. Section 64(1)(a) also preserves separate treatment for former section 66A transitional cases and certain pre-April-2013 2% elections. Check historical employment and rate records; the member's original joining date alone does not establish a legacy 4% case. The general IRD web/KS4 default summaries omit this surviving statutory limb. [S45, subsections (1)-(2)](https://www.legislation.govt.nz/act/public/2006/40/en/latest/sections/DLM379037/), [S49](https://www.legislation.govt.nz/act/public/2006/40/en/latest/sections/DLM379032/)

A valid IRD temporary rate reduction permits **3%**. The requested approval period must be **at least 92 days and no more than 1 year**; further reductions can follow. Use the actual approval's start/end dates and the notice for the relevant employer, rather than treating one employer's notification as an instruction for every job. Track expiry and any renewed approval. A person cannot use a temporary reduction whilst on a savings suspension. An informal request does not replace approval. [S39](https://www.ird.govt.nz/kiwisaver/kiwisaver-individuals/making-changes-to-my-kiwisaver/changing-my-kiwisaver-contribution-rate/temporary-rate-reduction), [S46](https://www.legislation.govt.nz/act/public/2006/40/en/latest/sections/LMS1569986/), [S47](https://www.legislation.govt.nz/act/public/2006/40/en/latest/sections/LMS1569987/)

An employee may revoke the temporary reduction for an employer and resume the applicable ordinary/default/elected rate. Using it for fewer than **92 days requires that employer's agreement**. Retain that agreement; a request alone does not prove consent. The payroll specification's PDF page 13 sample letter says a reduction cannot end in its first 3 months, but omits the statutory agreement exception. Follow section 101S and the consistent KS4 instruction rather than implementing an absolute ban. A later reduction for that employer requires a new application. [S48](https://www.legislation.govt.nz/act/public/2006/40/en/latest/sections/LMS1569995/), [S39](https://www.ird.govt.nz/kiwisaver/kiwisaver-individuals/making-changes-to-my-kiwisaver/changing-my-kiwisaver-contribution-rate/temporary-rate-reduction), [KS4, PDF page 18](https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir1---ir99/ks4/ks4.pdf?modified=20260129195326)

### Identify the contribution base

Classify each payment before applying a rate. The following are selected ordinary inclusions/exclusions, not a complete ruling on an actual payment. [S38](https://www.ird.govt.nz/kiwisaver/kiwisaver-employers/contributions-and-deductions/gross-pay-for-kiwisaver-and-complying-funds), [KS4, PDF page 12](https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir1---ir99/ks4/ks4.pdf?modified=20260129195326), [S2, section 4.5](https://www.ird.govt.nz/-/media/project/ir/home/documents/digital-service-providers/software-providers/payroll-calculations-business-rules-specifications/payroll-calculations-and-business-rules-specification.pdf?modified=20260401012317)

| Payment already correctly classified | KiwiSaver gross salary or wages | Complying-fund gross base salary or wages | Source |
|---|---|---|---|
| Ordinary salary, wages and overtime | Included | Included, subject to the fund's applicable definition | https://www.ird.govt.nz/kiwisaver/kiwisaver-employers/contributions-and-deductions/gross-pay-for-kiwisaver-and-complying-funds |
| Bonus and commission | Included | Excluded | https://www.ird.govt.nz/kiwisaver/kiwisaver-employers/contributions-and-deductions/gross-pay-for-kiwisaver-and-complying-funds |
| Redundancy payment | Excluded | Excluded | https://www.ird.govt.nz/kiwisaver/kiwisaver-employers/contributions-and-deductions/gross-pay-for-kiwisaver-and-complying-funds |
| Board/lodging, use of a house or an allowance instead | Excluded | Excluded | https://www.ird.govt.nz/kiwisaver/kiwisaver-employers/contributions-and-deductions/gross-pay-for-kiwisaver-and-complying-funds |
| Overseas accommodation/living-cost allowance or reimbursement within the stated exclusion | Excluded | Excluded | https://www.ird.govt.nz/kiwisaver/kiwisaver-employers/contributions-and-deductions/gross-pay-for-kiwisaver-and-complying-funds |
| Qualifying voluntary bonding payment or employee-share-scheme shares within the stated exclusion | Excluded | Excluded | https://www.ird.govt.nz/kiwisaver/kiwisaver-employers/contributions-and-deductions/gross-pay-for-kiwisaver-and-complying-funds |

Check the complying fund's trust deed for other excluded amounts. KiwiSaver also excludes the specified Fire and Emergency New Zealand volunteer honoraria. Keep evidence supporting an exclusion. These exclusions do not determine PAYE, FBT, ESS, employment-law or cross-border treatment. For a person contributing to both KiwiSaver and a complying fund, establish each employee deduction rate and its own base; do not silently reuse one base for both. [S38](https://www.ird.govt.nz/kiwisaver/kiwisaver-employers/contributions-and-deductions/gross-pay-for-kiwisaver-and-complying-funds), [KS4, PDF pages 12 and 23](https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir1---ir99/ks4/ks4.pdf?modified=20260129195326)

### Compulsory employer contributions

The ordinary minimum is 3.5% of qualifying gross salary or wages for an eligible contributing member. From 1 April 2026 this includes eligible **16- and 17-year-old members**. The ordinary conditions include age 16 to under 65, membership, required employee deductions and no disqualifying defined-benefit arrangement. Check the actual circumstances; membership alone does not establish liability. [S7](https://www.ird.govt.nz/kiwisaver-changes), [S9](https://www.ird.govt.nz/kiwisaver/kiwisaver-for-employers/contributions-and-deductions/employer-contributions-to-kiwisaver-and-complying-funds)

If an employee has an approved temporary 3% deduction rate, the employer **may choose** the 3% employer rate; it need not reduce its contribution. Record its choice and any contract requiring more. The statutory CEC rate is otherwise 3.5%. Reaching 65 may end the statutory obligation, but an agreement or voluntary contribution can continue and ESCT may still apply. Use the applicable stop instruction and evidence rather than assuming a birthday cancels all contractual obligations. [S9](https://www.ird.govt.nz/kiwisaver/kiwisaver-for-employers/contributions-and-deductions/employer-contributions-to-kiwisaver-and-complying-funds), [S50, subsection (4)](https://www.legislation.govt.nz/act/public/2006/40/en/latest/sections/DLM1233474/)

For a person contributing to both a KiwiSaver scheme and a complying fund, the ordinary employer minimum is shared between the funds, not an additional 3.5% minimum for each. Establish the relevant bases and agreed allocation. Do not deduct an unrelated superannuation contribution as an automatic credit: section 101D's other-contribution and hybrid-scheme offsets have detailed scheme, employment/agreement and vesting conditions. Their application remains an actual-case check here. [S9](https://www.ird.govt.nz/kiwisaver/kiwisaver-for-employers/contributions-and-deductions/employer-contributions-to-kiwisaver-and-complying-funds), [S50](https://www.legislation.govt.nz/act/public/2006/40/en/latest/sections/DLM1233474/)

Employer contributions are normally additional to salary or wages. An agreed total-remuneration arrangement needs a genuine agreement and must still satisfy minimum-wage requirements excluding the employer contribution. Do not reduce contracted pay automatically. Deduct ESCT from the gross employer contribution unless employer and employee have agreed to the separate PAYE treatment. The employee's own KiwiSaver deduction is not subject to ESCT. KiwiSaver employer contributions go through IRD; complying-fund contributions go directly to that fund. [S9](https://www.ird.govt.nz/kiwisaver/kiwisaver-for-employers/contributions-and-deductions/employer-contributions-to-kiwisaver-and-complying-funds), [S10](https://www.ird.govt.nz/esct)

Check whether an agreed employer contribution is gross or net of ESCT. A promised net contribution requires grossing up under IR335's method before the ordinary ESCT calculation. Reconcile the promised net after the required truncation; do not treat a contractual net percentage as the gross statutory minimum. This guide does not work a contractual gross-up example. [IR335, page 27](https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir300---ir399/ir335/ir335.pdf?modified=20250811232131)

### Savings suspensions, ACC and leave

Require a valid savings-suspension notice and track its dates. An unsupported statement that the employee is on a suspension does not justify stopping deductions. Apply IRD's restart instruction when it ends. A suspension ordinarily stops required employee deductions and compulsory employer contributions, but an agreement or voluntary employer contribution can continue; apply the appropriate ESCT or agreed PAYE treatment. Approval eligibility, including early hardship applications, is not determined here. [S8](https://www.ird.govt.nz/kiwisaver/kiwisaver-for-employers/contributions-and-deductions/kiwisaver-deductions-from-employee-pay), [S9](https://www.ird.govt.nz/kiwisaver/kiwisaver-for-employers/contributions-and-deductions/employer-contributions-to-kiwisaver-and-complying-funds), [S2, section 4.1](https://www.ird.govt.nz/-/media/project/ir/home/documents/digital-service-providers/software-providers/payroll-calculations-business-rules-specifications/payroll-calculations-and-business-rules-specification.pdf?modified=20260401012317), [KS4, PDF page 18](https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir1---ir99/ks4/ks4.pdf?modified=20260129195326)

If the employer continues paying under an ACC partnership programme or employer reimbursement agreement, continue employee KiwiSaver deductions unless a valid suspension applies; employer contributions in that situation are voluntary. When ACC pays weekly compensation directly, the employer can stop its own deductions and contributions. If the employer continues salary or wages during parental leave, continue required employee and employer contributions unless a valid suspension applies. This does not determine deductions from government parental-leave payments or leave entitlements. [S40](https://www.ird.govt.nz/kiwisaver/kiwisaver-employers/contributions-and-deductions/employees-with-special-circumstances), [S2, section 4.5.3](https://www.ird.govt.nz/-/media/project/ir/home/documents/digital-service-providers/software-providers/payroll-calculations-business-rules-specifications/payroll-calculations-and-business-rules-specification.pdf?modified=20260401012317)

Contributions normally stop on unpaid leave, but the employer may contribute voluntarily. IRD's current instructions permit including the contribution in employment information with **zero gross earnings**, or paying a lump sum through IRD after the employee returns. ESCT still applies unless the agreed salary/wages treatment applies. For a voluntary $52.50 contribution with an established 30% ESCT rate, the whole-dollar base is $52, tax is $15.60 and the fund receives $36.90. The specification's page 19 table wrongly switches its tax base to $45; use the current dedicated web example and Section 4's algorithm. [S40](https://www.ird.govt.nz/kiwisaver/kiwisaver-employers/contributions-and-deductions/employees-with-special-circumstances), [S2, section 4.5.4](https://www.ird.govt.nz/-/media/project/ir/home/documents/digital-service-providers/software-providers/payroll-calculations-business-rules-specifications/payroll-calculations-and-business-rules-specification.pdf?modified=20260401012317)

### Opt-outs and separate refund streams

Only an automatically enrolled employee can use the ordinary opt-out process. A timely request is made on **days 14 to 56 inclusive** after starting employment, using KS10. Send the request/details to IRD and stop deductions/contributions under the valid opt-out instruction. A voluntary joiner or existing member cannot use KS10 merely because they started a new job. A qualifying later withdrawal or KS51 stop instruction is a separate process. [S36](https://www.ird.govt.nz/kiwisaver/kiwisaver-employers/employees-who-want-to-opt-out-of-kiwisaver), [KS4, PDF page 18](https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir1---ir99/ks4/ks4.pdf?modified=20260129195326)

After day 56, IRD decides whether to accept a late request. Its stated window is up to 3 months **after IRD received the first contribution**, subject to its specified reasons; it is not a blanket 3-month extension from employment commencement. Continue employee deductions, employer contributions and ESCT until IRD's acceptance/stop instruction applies. Do not approve the late request yourself. [S37](https://www.ird.govt.nz/kiwisaver/kiwisaver-employers/employees-who-want-to-opt-out-of-kiwisaver/employees-who-opt-out-late-from-kiwisaver)

Reconcile each stream before refunding. If employee deductions have not been filed and paid to IRD, the employer may refund them and report the amounts actually deducted/retained. If they have already been sent, IRD refunds the employee; avoid a second employer refund. Reconcile mixed or partly forwarded amounts with IRD before acting. Employer contributions already sent are refunded to the employer subject to amounts owing to IRD. **ESCT is a separate refund request**, using the applicable IR344 amendment/contact route; do not assume an automatic employer-contribution refund also refunds ESCT. Retain the accepted request, filing amendments, employee refund and employer/ESCT reconciliation. [S36](https://www.ird.govt.nz/kiwisaver/kiwisaver-employers/employees-who-want-to-opt-out-of-kiwisaver), [S2, section 5.21.5](https://www.ird.govt.nz/-/media/project/ir/home/documents/digital-service-providers/software-providers/payroll-calculations-business-rules-specifications/payroll-calculations-and-business-rules-specification.pdf?modified=20260401012317)

The announced 4% ordinary default from 1 April 2028 is a future change, not the ordinary new-default rate for 2026-27 payroll. [S7](https://www.ird.govt.nz/kiwisaver-changes)


### ESCT rate and calculation

### Set the employee's rate

If the employee worked for this employer for the whole preceding tax year, use that year's salary/wages **plus gross employer superannuation contributions before ESCT**. Otherwise estimate both amounts for the **current tax year**. A part-year new starter is not automatically assigned a full 12 months of earnings beyond 31 March. Recalculate for the next tax year; ordinary salary changes during the year do not reset the rate. [S2, sections 5.20.4-5.20.5](https://www.ird.govt.nz/-/media/project/ir/home/documents/digital-service-providers/software-providers/payroll-calculations-business-rules-specifications/payroll-calculations-and-business-rules-specification.pdf?modified=20260401012317)

| ESCT rate threshold amount, last whole dollar | ESCT rate | Source |
|---|---:|---|
| $0 to $18,720 | 10.5% | https://www.ird.govt.nz/-/media/project/ir/home/documents/digital-service-providers/software-providers/payroll-calculations-business-rules-specifications/payroll-calculations-and-business-rules-specification.pdf?modified=20260401012317 |
| $18,721 to $64,200 | 17.5% | https://www.ird.govt.nz/-/media/project/ir/home/documents/digital-service-providers/software-providers/payroll-calculations-business-rules-specifications/payroll-calculations-and-business-rules-specification.pdf?modified=20260401012317 |
| $64,201 to $93,720 | 30% | https://www.ird.govt.nz/-/media/project/ir/home/documents/digital-service-providers/software-providers/payroll-calculations-business-rules-specifications/payroll-calculations-and-business-rules-specification.pdf?modified=20260401012317 |
| $93,721 to $216,000 | 33% | https://www.ird.govt.nz/-/media/project/ir/home/documents/digital-service-providers/software-providers/payroll-calculations-business-rules-specifications/payroll-calculations-and-business-rules-specification.pdf?modified=20260401012317 |
| $216,001 upwards | 39% | https://www.ird.govt.nz/-/media/project/ir/home/documents/digital-service-providers/software-providers/payroll-calculations-business-rules-specifications/payroll-calculations-and-business-rules-specification.pdf?modified=20260401012317 |

These are single rates on the relevant employer contribution, not progressive bands applied to salary. [Income Tax Act 2007, Schedule 1 Part D](https://www.legislation.govt.nz/act/public/2007/97/en/latest/parts/DLM1523173/) says to select the band for the **last dollar** of the threshold amount. Do not round a fractional dollar up into the next band. The current technical specification reproduces the table in section 5.20.4. Defined-benefit funds and certain past-employee contributions have separate rules and are outside the ordinary case here. [S2](https://www.ird.govt.nz/-/media/project/ir/home/documents/digital-service-providers/software-providers/payroll-calculations-business-rules-specifications/payroll-calculations-and-business-rules-specification.pdf?modified=20260401012317), [S11](https://www.legislation.govt.nz/act/public/2007/97/en/latest/parts/DLM1523173/)

### Calculate each contribution

Under [the 2026-27 specification, sections 5.20.6 and 5.21.3](https://www.ird.govt.nz/-/media/project/ir/home/documents/digital-service-providers/software-providers/payroll-calculations-business-rules-specifications/payroll-calculations-and-business-rules-specification.pdf?modified=20260401012317), and [Inland Revenue's deduction instructions](https://www.ird.govt.nz/employing-staff/deductions-from-income/employer-superannuation-contribution-tax/deduct-esct-from-each-employer-contribution):

1. Calculate the gross employer contribution using dollars and cents.
2. Drop cents from that contribution to obtain the whole-dollar ESCT base. **Do not round up.**
3. Multiply that whole-dollar base by the employee's ESCT rate.
4. Truncate the tax to cents, rather than rounding it to the nearest cent.
5. Subtract that tax from the **original contribution including cents** to obtain the net employer contribution.

The September 2026 IR335 employer guide's page 27 Matthew example taxes $204.17 directly at 17.5%, despite its page 26 whole-dollar instruction. Do not copy that example's $35.73 tax. The technical algorithm and [the dedicated deduction page](https://www.ird.govt.nz/employing-staff/deductions-from-income/employer-superannuation-contribution-tax/deduct-esct-from-each-employer-contribution) require a whole-dollar base; $204.17 at 17.5% gives **$35.70 ESCT and $168.47 net contribution**. This is a recorded source discrepancy, not an alternative method. [IR335, pages 26-27](https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir300---ir399/ir335/ir335.pdf?modified=20250811232131)


## Worked cases

These fictional cases assume the stated code, eligibility, contribution base and notices have already been established. They check the arithmetic of the selected rules, not an actual person's liability. Tolerance is zero, so a cent error fails.

**Case 1: truncating a half-cent tax result.** Qualifying gross salary of $3,000 at 3.5% gives a $105.00 gross employer contribution. At a confirmed 17.5% ESCT rate, $18.375 truncates to **$18.37** and the fund receives **$86.63**.

```oa-check
name: nz-2026-employer-esct-half-cent
tolerance: 0
inputs:
  salary: 3000
  contribution_rate: 3.5
  esct_rate: 17.5
steps:
  gross_contribution: pct(salary, contribution_rate)
  esct_base: floor(gross_contribution)
  esct: floor(pct(esct_base, esct_rate) * 100) / 100
  net_contribution: gross_contribution - esct
expected:
  gross_contribution: 105
  esct: 18.37
  net_contribution: 86.63
```

**Case 2: retaining contribution cents.** A confirmed $204.17 gross employer contribution at 17.5% uses a $204 ESCT base. Tax is **$35.70**, leaving **$168.47**. Dropping the contribution's cents from the amount paid to the fund would also be wrong.

```oa-check
name: nz-2026-employer-esct-whole-dollar-base
tolerance: 0
inputs:
  gross_contribution: 204.17
  esct_rate: 17.5
steps:
  esct_base: floor(gross_contribution)
  esct: floor(pct(esct_base, esct_rate) * 100) / 100
  net_contribution: gross_contribution - esct
expected:
  esct_base: 204
  esct: 35.70
  net_contribution: 168.47
```

**Case 3: different contribution bases.** Assume $1,000 ordinary wages, $50 overtime, $200 bonus, $100 commission, $300 redundancy and $100 accommodation all validly classified as above. At a stated 3.5% employee rate, the KiwiSaver base is $1,350 and the complying-fund base is $1,050. The complying fund has no additional deed exclusions. These are alternative base calculations, not an instruction to enrol in both funds. [S38](https://www.ird.govt.nz/kiwisaver/kiwisaver-employers/contributions-and-deductions/gross-pay-for-kiwisaver-and-complying-funds), [S33](https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir1---ir99/ks4/ks4.pdf?modified=20260129195326)

```oa-check
name: nz-2026-kiwisaver-distinct-bases
tolerance: 0
inputs:
  ordinary: 1000
  overtime: 50
  bonus: 200
  commission: 100
  redundancy: 300
  accommodation: 100
  rate: 0.035
steps:
  total_pay: ordinary + overtime + bonus + commission + redundancy + accommodation
  kiwisaver_base: total_pay - redundancy - accommodation
  complying_base: kiwisaver_base - bonus - commission
  kiwisaver_deduction: kiwisaver_base * rate
  complying_deduction: complying_base * rate
expected:
  total_pay: 1750
  kiwisaver_base: 1350
  complying_base: 1050
  kiwisaver_deduction: 47.25
  complying_deduction: 36.75
```

**Case 4: established historical default.** Assume records establish a surviving section 64(1)(ab) case for this employer/employee, with no overriding election or temporary reduction. The $1,000 KiwiSaver base produces a $40 employee deduction, not $35. The example does not infer eligibility from a joining date alone. [S45](https://www.legislation.govt.nz/act/public/2006/40/en/latest/sections/DLM379037/), [S49](https://www.legislation.govt.nz/act/public/2006/40/en/latest/sections/DLM379032/)

```oa-check
name: nz-2026-kiwisaver-legacy-default
tolerance: 0
inputs:
  base: 1000
  rate: 0.04
steps:
  employee: base * rate
expected:
  employee: 40
```

**Case 5: valid election overrides the legacy default.** For the same established historical case, assume the employer has received a valid election of 3.5% applying to this calculated payment. On a $1,000 base, deduct $35. [S45, subsections (2)-(3)](https://www.legislation.govt.nz/act/public/2006/40/en/latest/sections/DLM379037/)

```oa-check
name: nz-2026-kiwisaver-legacy-election
tolerance: 0
inputs:
  base: 1000
  rate: 0.035
steps:
  employee: base * rate
expected:
  employee: 35
```

**Case 6: temporary reduction with unchanged employer rate.** Assume an approved 3% employee reduction applies and the employer retains 3.5%, with a shared $1,000 base and an established 17.5% ESCT rate. Employee $30, gross employer $35, ESCT $6.12 and net employer $28.88 remain separate amounts. [S9](https://www.ird.govt.nz/kiwisaver/kiwisaver-for-employers/contributions-and-deductions/employer-contributions-to-kiwisaver-and-complying-funds), [S50](https://www.legislation.govt.nz/act/public/2006/40/en/latest/sections/DLM1233474/), [S12](https://www.ird.govt.nz/employing-staff/deductions-from-income/employer-superannuation-contribution-tax/deduct-esct-from-each-employer-contribution)

```oa-check
name: nz-2026-kiwisaver-trr-employer-unchanged
tolerance: 0
inputs:
  base: 1000
  employee_rate: 0.03
  employer_rate: 0.035
  esct_rate: 0.175
steps:
  employee: base * employee_rate
  employer_gross: base * employer_rate
  esct: floor(floor(employer_gross) * esct_rate * 100) / 100
  employer_net: employer_gross - esct
expected:
  employee: 30
  employer_gross: 35
  esct: 6.12
  employer_net: 28.88
```

**Case 7: employer chooses the permitted reduced rate.** Assume the same valid temporary reduction and base, but the employer chooses 3% and no agreement requires more. At 17.5% ESCT, gross employer $30 becomes $24.75 net after $5.25 ESCT. [S50](https://www.legislation.govt.nz/act/public/2006/40/en/latest/sections/DLM1233474/), [S12](https://www.ird.govt.nz/employing-staff/deductions-from-income/employer-superannuation-contribution-tax/deduct-esct-from-each-employer-contribution)

```oa-check
name: nz-2026-kiwisaver-trr-employer-reduced
tolerance: 0
inputs:
  base: 1000
  employer_rate: 0.03
  esct_rate: 0.175
steps:
  employer_gross: base * employer_rate
  esct: floor(floor(employer_gross) * esct_rate * 100) / 100
  employer_net: employer_gross - esct
expected:
  employer_gross: 30
  esct: 5.25
  employer_net: 24.75
```

**Case 8: shared employer minimum across 2 funds.** Assume both funds qualify, each relevant base is $1,000, the ordinary minimum is 3.5% and a valid allocation contributes 2.5% to one fund and 1% to the other. Gross contributions of $25 and $10 meet the $35 aggregate minimum. This does not establish the employee deduction rates or any legacy offset. [S9](https://www.ird.govt.nz/kiwisaver/kiwisaver-for-employers/contributions-and-deductions/employer-contributions-to-kiwisaver-and-complying-funds), [S50](https://www.legislation.govt.nz/act/public/2006/40/en/latest/sections/DLM1233474/)

```oa-check
name: nz-2026-kiwisaver-two-fund-minimum
tolerance: 0
inputs:
  base: 1000
  minimum_rate: 0.035
  first_rate: 0.025
  second_rate: 0.01
steps:
  minimum: base * minimum_rate
  first: base * first_rate
  second: base * second_rate
  total: first + second
  shortfall: max(0, minimum - total)
expected:
  minimum: 35
  first: 25
  second: 10
  total: 35
  shortfall: 0
```

**Case 9: voluntary unpaid-leave contribution.** Assume zero actual wages, a voluntary employer contribution of 3.5% of usual weekly pay of $1,500 and an established 30% ESCT rate. The $52.50 contribution uses a $52 ESCT base, producing $15.60 tax and $36.90 net. Usual pay is not reported as actual gross earnings. [S40](https://www.ird.govt.nz/kiwisaver/kiwisaver-employers/contributions-and-deductions/employees-with-special-circumstances), [S12](https://www.ird.govt.nz/employing-staff/deductions-from-income/employer-superannuation-contribution-tax/deduct-esct-from-each-employer-contribution)

```oa-check
name: nz-2026-kiwisaver-unpaid-leave
tolerance: 0
inputs:
  usual_pay: 1500
  contribution_rate: 0.035
  esct_rate: 0.3
steps:
  employer_gross: usual_pay * contribution_rate
  esct_base: floor(employer_gross)
  esct: floor(esct_base * esct_rate * 100) / 100
  employer_net: employer_gross - esct
expected:
  employer_gross: 52.5
  esct_base: 52
  esct: 15.6
  employer_net: 36.9
```

**Case 10: voluntary employer contribution during a suspension.** Assume an approved suspension stops required employee deductions and the employer voluntarily contributes $30. With an established 17.5% ESCT rate and no agreed PAYE treatment, tax is $5.25 and net employer contribution $24.75. Suspension does not make the voluntary contribution tax free. [S9](https://www.ird.govt.nz/kiwisaver/kiwisaver-for-employers/contributions-and-deductions/employer-contributions-to-kiwisaver-and-complying-funds), [S33](https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir1---ir99/ks4/ks4.pdf?modified=20260129195326), [S12](https://www.ird.govt.nz/employing-staff/deductions-from-income/employer-superannuation-contribution-tax/deduct-esct-from-each-employer-contribution)

```oa-check
name: nz-2026-kiwisaver-suspension-voluntary
tolerance: 0
inputs:
  employer_gross: 30
  esct_rate: 0.175
steps:
  esct: floor(floor(employer_gross) * esct_rate * 100) / 100
  employer_net: employer_gross - esct
expected:
  esct: 5.25
  employer_net: 24.75
```

**Case 11: unforwarded employee deductions refunded once.** Assume a valid timely opt-out and 2 employee deductions of $35 each, neither filed nor paid to IRD. An employer refund of $70 clears this employee-deduction balance. It does not give the employee the employer contribution or ESCT. [S36](https://www.ird.govt.nz/kiwisaver/kiwisaver-employers/employees-who-want-to-opt-out-of-kiwisaver)

```oa-check
name: nz-2026-kiwisaver-optout-unforwarded
tolerance: 0
inputs:
  first: 35
  second: 35
  refund: 70
steps:
  held: first + second
  remaining: held - refund
expected:
  held: 70
  remaining: 0
```

**Case 12: reconcile employer contribution and ESCT separately.** Assume an accepted opt-out and 2 previously remitted gross employer contributions of $35, each with $6.12 ESCT and $28.88 net to the fund. The employer-side gross total $70 reconciles to $57.76 fund contributions plus $12.24 ESCT. These are separate refund/amendment streams, subject to IRD processing and debts; they are not an employee refund and no automatic ESCT refund is assumed. [S36](https://www.ird.govt.nz/kiwisaver/kiwisaver-employers/employees-who-want-to-opt-out-of-kiwisaver), [S12](https://www.ird.govt.nz/employing-staff/deductions-from-income/employer-superannuation-contribution-tax/deduct-esct-from-each-employer-contribution)

```oa-check
name: nz-2026-kiwisaver-optout-employer-streams
tolerance: 0
inputs:
  count: 2
  per_contribution: 35
  per_esct: 6.12
  per_net: 28.88
steps:
  gross_total: count * per_contribution
  fund_total: count * per_net
  esct_total: count * per_esct
  reconciled: fund_total + esct_total
expected:
  gross_total: 70
  fund_total: 57.76
  esct_total: 12.24
  reconciled: 70
```

## When to refuse or refer

Refer: complying funds and legacy scheme offsets, historical rate evidence, mixed or late refunds, enrolment exceptions beyond those listed, and any agreed alternative to ESCT. An unknown classification, contribution base or notice is an input gap. Do not invent a resident tax code, a pension exemption or a flat PAYE percentage. Ordinary salary rules do not establish the treatment of contractors, non-residents, offshore employers, IR56 workers, benefits or paid parental leave. The selected extra-pay methods below require an established payment classification; they do not determine employment-law entitlements.


## Sources

| Source | URL | Read on | What was read |
| --- | --- | --- | --- |
| KiwiSaver changes | https://www.ird.govt.nz/kiwisaver-changes | 2026-11-14 | Read for KiwiSaver from 1 April 2026, Compulsory employer contributions, Opt-outs and separate refund streams; reopened on 2026-11-14 for the 3.5% default rate from 1 April 2026, the 4% rate from 1 April 2028, temporary rate reductions and the government contribution |
| 64 Contribution rate, current copy 1 April 2026 | https://www.legislation.govt.nz/act/public/2006/40/en/latest/sections/DLM379037/ | 2026-11-13 | Read for KiwiSaver from 1 April 2026, Employee rates, changes and temporary reductions, Worked cases (read by Ryan Duguid) |
| KiwiSaver Act section 101D, current copy 1 April 2026 | https://www.legislation.govt.nz/act/public/2006/40/en/latest/sections/DLM1233474/ | 2026-11-13 | Read for KiwiSaver from 1 April 2026, Compulsory employer contributions, Worked cases (read by Ryan Duguid) |
| 6 Application, current copy 1 April 2026 | https://www.legislation.govt.nz/act/public/2006/40/en/latest/sections/DLM378821/ | 2026-11-13 | Read for Establish membership and automatic-enrolment eligibility (read by Ryan Duguid) |
| KS4 employer guide, cover April 2026, selected pages | https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir1---ir99/ks4/ks4.pdf?modified=20260129195326 | 2026-11-13 | Read for Establish membership and automatic-enrolment eligibility, Employee rates, changes and temporary reductions, Identify the contribution base, Savings suspensions, ACC and leave (read by Ryan Duguid) |
| 10 Who automatic enrolment rules apply to, current copy 1 April 2026 | https://www.legislation.govt.nz/act/public/2006/40/en/latest/sections/DLM378830/ | 2026-11-13 | Read for Establish membership and automatic-enrolment eligibility (read by Ryan Duguid) |
| 14 Other situations when automatic enrolment rules do not apply, current copy 1 April 2026 | https://www.legislation.govt.nz/act/public/2006/40/en/latest/sections/DLM378843/ | 2026-11-13 | Read for Establish membership and automatic-enrolment eligibility (read by Ryan Duguid) |
| 12 Temporary employment, current copy 1 April 2026 | https://www.legislation.govt.nz/act/public/2006/40/en/latest/sections/DLM378834/ | 2026-11-13 | Read for Establish membership and automatic-enrolment eligibility (read by Ryan Duguid) |
| Starting employees, updated 21 October 2026 | https://www.ird.govt.nz/kiwisaver/kiwisaver-for-employers/starting-employees-in-kiwisaver | 2026-11-13 | Read for Establish membership and automatic-enrolment eligibility (read by Ryan Duguid) |
| Automatic enrolment, updated 21 October 2026 | https://www.ird.govt.nz/kiwisaver/kiwisaver-for-employers/starting-employees-in-kiwisaver/auto-enrol-employees-into-kiwisaver | 2026-11-13 | Read for Establish membership and automatic-enrolment eligibility (read by Ryan Duguid) |
| KiwiSaver Act section 60, current copy 1 April 2026 | https://www.legislation.govt.nz/act/public/2006/40/en/latest/sections/DLM379032/ | 2026-11-13 | Read for Establish membership and automatic-enrolment eligibility, Employee rates, changes and temporary reductions, Worked cases (read by Ryan Duguid) |
| Employee KiwiSaver deductions | https://www.ird.govt.nz/kiwisaver/kiwisaver-for-employers/contributions-and-deductions/kiwisaver-deductions-from-employee-pay | 2026-11-13 | Read for Employee rates, changes and temporary reductions, Savings suspensions, ACC and leave (read by Ryan Duguid) |
| Temporary rate reduction, updated 1 April 2026 | https://www.ird.govt.nz/kiwisaver/kiwisaver-individuals/making-changes-to-my-kiwisaver/changing-my-kiwisaver-contribution-rate/temporary-rate-reduction | 2026-11-13 | Read for Employee rates, changes and temporary reductions (read by Ryan Duguid) |
| 101L How to apply for rate reduction, current copy 1 April 2026 | https://www.legislation.govt.nz/act/public/2006/40/en/latest/sections/LMS1569986/ | 2026-11-13 | Read for Employee rates, changes and temporary reductions (read by Ryan Duguid) |
| 101M Grant of rate reduction, current copy 1 April 2026 | https://www.legislation.govt.nz/act/public/2006/40/en/latest/sections/LMS1569987/ | 2026-11-13 | Read for Employee rates, changes and temporary reductions (read by Ryan Duguid) |
| 101S Revocation of rate reduction, current copy 1 April 2026 | https://www.legislation.govt.nz/act/public/2006/40/en/latest/sections/LMS1569995/ | 2026-11-13 | Read for Employee rates, changes and temporary reductions (read by Ryan Duguid) |
| KiwiSaver and complying-fund gross pay, updated 28 April 2021 | https://www.ird.govt.nz/kiwisaver/kiwisaver-employers/contributions-and-deductions/gross-pay-for-kiwisaver-and-complying-funds | 2026-11-13 | Read for Identify the contribution base, Worked cases (read by Ryan Duguid) |
| 2026-27 payroll specification, selected sections | https://www.ird.govt.nz/-/media/project/ir/home/documents/digital-service-providers/software-providers/payroll-calculations-business-rules-specifications/payroll-calculations-and-business-rules-specification.pdf?modified=20260401012317 | 2026-11-14 | Read for Identify the contribution base, Savings suspensions, ACC and leave, Opt-outs and separate refund streams, Set the employee's rate; reopened on 2026-11-14 for the annual PAYE formula, earners' levy, student-loan threshold, NSW rate and ESCT table (2026-27 specification dated 24 March 2026, version 1.0) |
| Employer contributions | https://www.ird.govt.nz/kiwisaver/kiwisaver-for-employers/contributions-and-deductions/employer-contributions-to-kiwisaver-and-complying-funds | 2026-11-13 | Read for Compulsory employer contributions, Savings suspensions, ACC and leave, Worked cases (read by Ryan Duguid) |
| ESCT scope and methods | https://www.ird.govt.nz/esct | 2026-11-13 | Read for Compulsory employer contributions (read by Ryan Duguid) |
| IR335 employer guide, September 2026, selected pages | https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir300---ir399/ir335/ir335.pdf?modified=20250811232131 | 2026-11-13 | Read for Compulsory employer contributions, Calculate each contribution (read by Ryan Duguid) |
| Special employee circumstances, updated 1 October 2026 | https://www.ird.govt.nz/kiwisaver/kiwisaver-employers/contributions-and-deductions/employees-with-special-circumstances | 2026-11-13 | Read for Savings suspensions, ACC and leave, Worked cases (read by Ryan Duguid) |
| Employee opt-outs, updated 28 July 2026 | https://www.ird.govt.nz/kiwisaver/kiwisaver-employers/employees-who-want-to-opt-out-of-kiwisaver | 2026-11-13 | Read for Opt-outs and separate refund streams, Worked cases (read by Ryan Duguid) |
| Late opt-outs, updated 28 April 2021 | https://www.ird.govt.nz/kiwisaver/kiwisaver-employers/employees-who-want-to-opt-out-of-kiwisaver/employees-who-opt-out-late-from-kiwisaver | 2026-11-13 | Read for Opt-outs and separate refund streams (read by Ryan Duguid) |
| Income Tax Act 2007, Schedule 1 Part D, current copy dated 4 September 2026 | https://www.legislation.govt.nz/act/public/2007/97/en/latest/parts/DLM1523173/ | 2026-11-13 | Read for Set the employee's rate (read by Ryan Duguid) |
| Deducting ESCT | https://www.ird.govt.nz/employing-staff/deductions-from-income/employer-superannuation-contribution-tax/deduct-esct-from-each-employer-contribution | 2026-11-13 | Read for Calculate each contribution, Worked cases (read by Ryan Duguid) |

Not yet confirmed: the rows below were read by Ryan Duguid on 12 and 13 November 2026, and only the spot-checked figures listed in the PR were reopened on 14 November 2026. Inherited sources checked 12 November 2026; selected ESS sources checked 13 November 2026. Selected District Court Act sections use the current copy dated 17 February 2026; Tax Administration Act section 157 uses the current copy dated 1 October 2026. SPS 21/01 is dated 12 April 2021 and remains linked by IRD's arrears page updated 16 April 2026. Extra-pay and deduction examples are recalculated from the stated rules; known inconsistent printed examples and boundary wording are recorded in the verification log. The technical specification is dated 24 March 2026, version 1.0, and expressly covers 1 April 2026 to 31 March 2027. IR335's cover says September 2026. KS4's cover says April 2026. Selected KiwiSaver Act provisions use the current copy dated 1 April 2026. The verification log records the selected native/image page scope, the surviving legacy default and conflicting sample-letter/example wording. The selected correction regulations use the 30 March 2026 consolidation. Selected TAA record, assessment and penalty provisions use the 1 October 2026 copy. Its full-Act page flags unincorporated amendments; the selected amendment-impact check is recorded in the verification log. SPS19/04 is dated 30 May 2019. Current statutory wording controls the affected-employee penalty base and inclusive $100 exemption. These checks do not claim full PDF or statute review. Employer ACC Work and Working Safer levy invoices are not calculated.
