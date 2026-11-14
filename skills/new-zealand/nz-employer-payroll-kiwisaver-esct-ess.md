---
name: nz-employer-payroll-kiwisaver-esct-ess
description: >
  Companion to nz-employer-payroll for New Zealand employer payroll paid from
  1 April 2026 to 31 March 2027. Covers KiwiSaver membership and automatic
  enrolment, the 3.5% default employee rate and compulsory employer contribution,
  temporary rate reductions, the contribution base, savings suspensions, opt-outs
  and refunds, employer superannuation contribution tax (ESCT) rates and the
  whole-dollar calculation, and selected employee share scheme (ESS) benefits,
  exempt ESS conditions, withholding, funding and reporting. Trigger on
  KiwiSaver employer contributions, ESCT, employee share schemes, exempt ESS,
  IR1211 or IR1212. Load nz-employer-payroll first for PAYE, ACC, filing and payment.
jurisdiction: NZ
category: payroll
tax_year: 2026
tax_year_notes: "2026-27: payroll paid 1 April 2026 to 31 March 2027 (Inland Revenue's 2027 income year); selected ordinary special-code, ESS, filing and payment rules checked 12 and 13 November 2026"
tier: 2
last_updated: 2026-11-14
version: 1.2
domain: tax
type: computation
depends_on:
  - nz-employer-payroll
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# New Zealand employer payroll: KiwiSaver, ESCT and employee share schemes v1.2

> **General reference only.** This is a source-cited draft awaiting qualified review. Confirm the employee's facts and the rules for the actual payday before filing, paying or relying on a calculation.

## Scope

**Tax year:** 2026, meaning payroll paid in the New Zealand 2026-27 year, 1 April 2026 to 31 March 2027 (Inland Revenue calls it the 2027 income year). Payroll rules apply by payday: a pay period that straddles 1 April uses the rules for the payday.

This companion covers KiwiSaver, employer superannuation contribution tax (ESCT) and selected employee share schemes (ESS) for a New Zealand employer in NZD. It was split out of `nz-employer-payroll` version 1.1 unchanged, because the whole guide exceeded the website's size limit. Load `nz-employer-payroll` first: it holds the PAYE codes, ACC earners' levy, student-loan and deduction-notice rules, payday filing, payment, corrections, records and penalties these rules rely on. It provides selected tax, contribution and filing rules, not complete employment-law or whole-topic coverage. Worked cases keep their version 1.1 numbers.

## Ask the client first

Obtain the following before calculating:

- Employer registration, actual payday, pay frequency and period covered. [Register as an employer as soon as you start employing staff][S3].
- Gross pay and each payment's character. Determine PAYE income and KiwiSaver gross salary or wages separately; allowances, reimbursements and special payments need their own treatment.
- KiwiSaver membership and eligibility, valid deduction-rate instruction, employer contribution agreement (including whether it promises a gross or net-of-ESCT amount) and any valid opt-out, savings-suspension or temporary-rate-reduction notice.
- For ESCT, employment start date, whether the employee worked for this employer throughout the preceding tax year and the relevant salary/wages plus gross employer superannuation contributions.
- Annual PAYE and ESCT figures, any connected employers and the established filing and payment schedules. The $50,000 electronic filing test and $500,000 remittance test serve different purposes.

For ESS, also obtain the scheme and offer terms, employment connection, beneficiary and associate details, issue, transfer, vesting and cancellation dates, market values, consideration and any withholding election (see "Employee share schemes: establish the benefit first" below). An unknown membership, contribution base or notice is an input gap; do not invent it.

## Rates, bands and thresholds

The key 2026-27 figures this skill uses, each with the Inland Revenue page that states it. The method below gives each figure's conditions and algorithm.

| Item | Value | Condition | Source |
| --- | --- | --- | --- |
| KiwiSaver default employee rate and minimum compulsory employer contribution | 3.5% for paydays on or after 1 April 2026 (was 3%) | Ordinary post-2009 default cases; existing elections of 4%, 6%, 8% or 10% remain | https://www.ird.govt.nz/kiwisaver-changes |
| Next scheduled default rate | 4% from 1 April 2028 | Not in force for 2026-27; shown so it is not applied early | same |
| Temporary rate reduction | 3% for 3 to 12 months | Approved by Inland Revenue; the employer may choose to match the reduced rate | same |
| 16- and 17-year-old members | Employer contributions of 3.5% of pay from 1 April 2026 | If the other eligibility requirements are met | same |
| ESCT rate, threshold amount $0 to $18,720 | 10.5% | Single rate on the employer contribution, set by the last whole dollar of salary/wages plus gross employer contributions | https://www.ird.govt.nz/-/media/project/ir/home/documents/digital-service-providers/software-providers/payroll-calculations-business-rules-specifications/payroll-calculations-and-business-rules-specification.pdf?modified=20260401012317 |
| ESCT rate, $18,721 to $64,200 | 17.5% | same | same |
| ESCT rate, $64,201 to $93,720 | 30% | same | same |
| ESCT rate, $93,721 to $216,000 | 33% | same | same |
| ESCT rate, $216,001 upwards | 39% | same | same |

## The method, step by step

### KiwiSaver from 1 April 2026

For ordinary post-2009 default cases, the employee deduction and minimum compulsory employer contribution increased from 3% to **3.5% for paydays on or after 1 April 2026**. The payday determines the rate for the whole payment when a period straddles 1 April; do not prorate by days worked. A surviving historical 4% employee default is addressed below. Existing valid elections of 4%, 6%, 8% or 10% remain available. [S7], [S45, subsection (3B)][S45], [S50, subsection (4B)][S50]

#### Establish membership and automatic-enrolment eligibility

Membership, automatic enrolment and compulsory employer-contribution eligibility are separate questions. For the ordinary case, establish that the person normally lives in New Zealand and is a citizen or entitled to remain indefinitely, and that the employer is within the Act. A temporary visitor, student or work permit does not establish indefinite entitlement. The State services overseas exception and other cross-border cases need their own checks. [S41], [KS4, PDF page 6][S33]

Automatic enrolment ordinarily concerns a new employee aged **18 or older and under 65** at the start of employment, with a non-exempt employer and no applicable exception. It does not automatically enrol a 16- or 17-year-old. An under-18 person joins through a provider; an existing member supplies their membership and deduction information rather than being enrolled again. Membership can continue beyond 65 even where compulsory employer contributions cease. [S42], [S44], [KS4, PDF pages 6–11][S33]

Check the exceptions before treating any new starter as automatically enrolled. A contract for no more than 28 continuous days is temporary for this purpose; count calendar days of employment, not shifts. If that employment continues, the temporary exclusion ends on day 29, described in section 12(2)(b) as the 28th day after employment started. Casual agricultural employment and qualifying irregular/intermittent employment with holiday pay have separate statutory tests. Section 14 also excludes existing members and specified situations such as private domestic service, election-day work and employment without required PAYE withholding. This is not an exhaustive classification checklist; resolve the actual section 12/14 exception, secondment or exempt-employer status first. [S43], [S44], [KS4, PDF page 7][S33]

Give a person who is automatically enrolled the KiwiSaver information pack within **7 days** of starting. Collect the applicable KS2 deduction information and retain it; do not send KS2 to IRD. Give IRD the applicable new-employee KiwiSaver details using IR346K/myIR or payroll software no later than the first employment-information return is due. Coordinate this with the separate new-employee information deadline in `nz-employer-payroll` (Filing, remitting and records). Start required deductions from the first payment for an automatically enrolled employee; for an existing member or an IRD direction, section 60 applies to payments calculated after the employer receives the relevant notice. Obtain a valid savings-suspension notice before omitting otherwise required deductions. [S34], [S35], [S49], [KS4, PDF pages 8–11][S33]

#### Employee rates, changes and temporary reductions

Use the valid KS2, written rate instruction or IRD notice. The ordinary elected choices are **3.5%, 4%, 6%, 8% and 10%** of KiwiSaver gross salary or wages. Apply a valid change to the first payment calculated after receipt; ordinary changes must be at least **92 days** apart unless the employer agrees to a shorter interval. Do not backdate missed employee deductions when acting on IRD's start instruction. A possible employer-contribution arrears obligation is a separate question and is not cancelled by that employee-deduction instruction. [S8], [S45, subsections (2)–(4)][S45], [KS4, PDF page 14][S33]

Do not assume every employee without a new election defaults to 3.5%. Section 64(1)(ab) retains a **4% default** where section 60(1)(a), (b) or (c) first applied to this employer in respect of this employee before 1 April 2009, subject to the statutory alternatives and any overriding election or valid temporary reduction. Section 64(1)(a) also preserves separate treatment for former section 66A transitional cases and certain pre-April-2013 2% elections. Check historical employment and rate records; the member's original joining date alone does not establish a legacy 4% case. The general IRD web/KS4 default summaries omit this surviving statutory limb. [S45, subsections (1)–(2)][S45], [S49]

A valid IRD temporary rate reduction permits **3%**. The requested approval period must be **at least 92 days and no more than 1 year**; further reductions can follow. Use the actual approval's start/end dates and the notice for the relevant employer, rather than treating one employer's notification as an instruction for every job. Track expiry and any renewed approval. A person cannot use a temporary reduction whilst on a savings suspension. An informal request does not replace approval. [S39], [S46], [S47]

An employee may revoke the temporary reduction for an employer and resume the applicable ordinary/default/elected rate. Using it for fewer than **92 days requires that employer's agreement**. Retain that agreement; a request alone does not prove consent. The payroll specification's PDF page 13 sample letter says a reduction cannot end in its first 3 months, but omits the statutory agreement exception. Follow section 101S and the consistent KS4 instruction rather than implementing an absolute ban. A later reduction for that employer requires a new application. [S48], [S39], [KS4, PDF page 18][S33]

#### Identify the contribution base

Classify each payment before applying a rate. The following are selected ordinary inclusions/exclusions, not a complete ruling on an actual payment. [S38], [KS4, PDF page 12][S33], [S2, section 4.5][S2]

| Payment already correctly classified | KiwiSaver gross salary or wages | Complying-fund gross base salary or wages |
|---|---|---|
| Ordinary salary, wages and overtime | Included | Included, subject to the fund's applicable definition |
| Bonus and commission | Included | Excluded |
| Redundancy payment | Excluded | Excluded |
| Board/lodging, use of a house or an allowance instead | Excluded | Excluded |
| Overseas accommodation/living-cost allowance or reimbursement within the stated exclusion | Excluded | Excluded |
| Qualifying voluntary bonding payment or employee-share-scheme shares within the stated exclusion | Excluded | Excluded |

Check the complying fund's trust deed for other excluded amounts. KiwiSaver also excludes the specified Fire and Emergency New Zealand volunteer honoraria. Keep evidence supporting an exclusion. These exclusions do not determine PAYE, FBT, ESS, employment-law or cross-border treatment. For a person contributing to both KiwiSaver and a complying fund, establish each employee deduction rate and its own base; do not silently reuse one base for both. [S38], [KS4, PDF pages 12 and 23][S33]

#### Compulsory employer contributions

The ordinary minimum is 3.5% of qualifying gross salary or wages for an eligible contributing member. From 1 April 2026 this includes eligible **16- and 17-year-old members**. The ordinary conditions include age 16 to under 65, membership, required employee deductions and no disqualifying defined-benefit arrangement. Check the actual circumstances; membership alone does not establish liability. [S7], [S9]

If an employee has an approved temporary 3% deduction rate, the employer **may choose** the 3% employer rate; it need not reduce its contribution. Record its choice and any contract requiring more. The statutory CEC rate is otherwise 3.5%. Reaching 65 may end the statutory obligation, but an agreement or voluntary contribution can continue and ESCT may still apply. Use the applicable stop instruction and evidence rather than assuming a birthday cancels all contractual obligations. [S9], [S50, subsection (4)][S50]

For a person contributing to both a KiwiSaver scheme and a complying fund, the ordinary employer minimum is shared between the funds, not an additional 3.5% minimum for each. Establish the relevant bases and agreed allocation. Do not deduct an unrelated superannuation contribution as an automatic credit: section 101D's other-contribution and hybrid-scheme offsets have detailed scheme, employment/agreement and vesting conditions. Their application remains an actual-case check here. [S9], [S50]

Employer contributions are normally additional to salary or wages. An agreed total-remuneration arrangement needs a genuine agreement and must still satisfy minimum-wage requirements excluding the employer contribution. Do not reduce contracted pay automatically. Deduct ESCT from the gross employer contribution unless employer and employee have agreed to the separate PAYE treatment. The employee's own KiwiSaver deduction is not subject to ESCT. KiwiSaver employer contributions go through IRD; complying-fund contributions go directly to that fund. [S9], [S10]

Check whether an agreed employer contribution is gross or net of ESCT. A promised net contribution requires grossing up under IR335's method before the ordinary ESCT calculation. Reconcile the promised net after the required truncation; do not treat a contractual net percentage as the gross statutory minimum. This guide does not work a contractual gross-up example. [IR335, page 27][S13]

#### Savings suspensions, ACC and leave

Require a valid savings-suspension notice and track its dates. An unsupported statement that the employee is on a suspension does not justify stopping deductions. Apply IRD's restart instruction when it ends. A suspension ordinarily stops required employee deductions and compulsory employer contributions, but an agreement or voluntary employer contribution can continue; apply the appropriate ESCT or agreed PAYE treatment. Approval eligibility, including early hardship applications, is not determined here. [S8], [S9], [S2, section 4.1][S2], [KS4, PDF page 18][S33]

If the employer continues paying under an ACC partnership programme or employer reimbursement agreement, continue employee KiwiSaver deductions unless a valid suspension applies; employer contributions in that situation are voluntary. When ACC pays weekly compensation directly, the employer can stop its own deductions and contributions. If the employer continues salary or wages during parental leave, continue required employee and employer contributions unless a valid suspension applies. This does not determine deductions from government parental-leave payments or leave entitlements. [S40], [S2, section 4.5.3][S2]

Contributions normally stop on unpaid leave, but the employer may contribute voluntarily. IRD's current instructions permit including the contribution in employment information with **zero gross earnings**, or paying a lump sum through IRD after the employee returns. ESCT still applies unless the agreed salary/wages treatment applies. For a voluntary $52.50 contribution with an established 30% ESCT rate, the whole-dollar base is $52, tax is $15.60 and the fund receives $36.90. The specification's page 19 table wrongly switches its tax base to $45; use the current dedicated web example and the ESCT algorithm below (Calculate each contribution). [S40], [S2, section 4.5.4][S2]

#### Opt-outs and separate refund streams

Only an automatically enrolled employee can use the ordinary opt-out process. A timely request is made on **days 14 to 56 inclusive** after starting employment, using KS10. Send the request/details to IRD and stop deductions/contributions under the valid opt-out instruction. A voluntary joiner or existing member cannot use KS10 merely because they started a new job. A qualifying later withdrawal or KS51 stop instruction is a separate process. [S36], [KS4, PDF page 18][S33]

After day 56, IRD decides whether to accept a late request. Its stated window is up to 3 months **after IRD received the first contribution**, subject to its specified reasons; it is not a blanket 3-month extension from employment commencement. Continue employee deductions, employer contributions and ESCT until IRD's acceptance/stop instruction applies. Do not approve the late request yourself. [S37]

Reconcile each stream before refunding. If employee deductions have not been filed and paid to IRD, the employer may refund them and report the amounts actually deducted/retained. If they have already been sent, IRD refunds the employee; avoid a second employer refund. Reconcile mixed or partly forwarded amounts with IRD before acting. Employer contributions already sent are refunded to the employer subject to amounts owing to IRD. **ESCT is a separate refund request**, using the applicable IR344 amendment/contact route; do not assume an automatic employer-contribution refund also refunds ESCT. Retain the accepted request, filing amendments, employee refund and employer/ESCT reconciliation. [S36], [S2, section 5.21.5][S2]

The announced 4% ordinary default from 1 April 2028 is a future change, not the ordinary new-default rate for 2026-27 payroll. [S7]

### ESCT rate and calculation

#### Set the employee's rate

If the employee worked for this employer for the whole preceding tax year, use that year's salary/wages **plus gross employer superannuation contributions before ESCT**. Otherwise estimate both amounts for the **current tax year**. A part-year new starter is not automatically assigned a full 12 months of earnings beyond 31 March. Recalculate for the next tax year; ordinary salary changes during the year do not reset the rate. [S2, sections 5.20.4-5.20.5][S2]

| ESCT rate threshold amount, last whole dollar | ESCT rate |
|---|---:|
| $0 to $18,720 | 10.5% |
| $18,721 to $64,200 | 17.5% |
| $64,201 to $93,720 | 30% |
| $93,721 to $216,000 | 33% |
| $216,001 upwards | 39% |

These are single rates on the relevant employer contribution, not progressive bands applied to salary. [Income Tax Act 2007, Schedule 1 Part D][S11] says to select the band for the **last dollar** of the threshold amount. Do not round a fractional dollar up into the next band. The current technical specification reproduces the table in section 5.20.4. Defined-benefit funds and certain past-employee contributions have separate rules and are outside the ordinary case here. [S2], [S11]

#### Calculate each contribution

Under [the 2026-27 specification, sections 5.20.6 and 5.21.3][S2], and [Inland Revenue's deduction instructions][S12]:

1. Calculate the gross employer contribution using dollars and cents.
2. Drop cents from that contribution to obtain the whole-dollar ESCT base. **Do not round up.**
3. Multiply that whole-dollar base by the employee's ESCT rate.
4. Truncate the tax to cents, rather than rounding it to the nearest cent.
5. Subtract that tax from the **original contribution including cents** to obtain the net employer contribution.

The September 2026 IR335 employer guide's page 27 Matthew example taxes $204.17 directly at 17.5%, despite its page 26 whole-dollar instruction. Do not copy that example's $35.73 tax. The technical algorithm and [the dedicated deduction page][S12] require a whole-dollar base; $204.17 at 17.5% gives **$35.70 ESCT and $168.47 net contribution**. This is a recorded source discrepancy, not an alternative method. [IR335, pages 26-27][S13]

#### Employee share schemes: establish the benefit first

These selected rules concern an established employee under a contract of service, with an ordinary New Zealand payroll code. Obtain the scheme and offer terms, employment connection, beneficiary and associate details, issue/transfer/vesting/cancellation dates, market values, consideration, any withholding election and the written funding agreement. An incentive labelled a share scheme is not enough. Section CE 7 requires an arrangement with a purpose or effect of issuing or transferring shares, connected to employment or service, and has exclusions for exempt ESS and the specified market-value arrangements. IS25/06 does not establish an independent contractor's or non-executive director's treatment. Section RD 7(1B), effective 21 February 2026, excludes its specified contractors and other statutory non-employees from extra pay. Resolve classification before applying this employee method. [S74], [S75], [S78], [S82]

A scheme that always pays cash and never has a purpose or effect of issuing or transferring shares is ordinarily a phantom scheme with an ordinary cash bonus. A mixed cash/share award does not make its cash entitlement an ESS benefit automatically. For genuine cash settlement, establish that the payment is consideration for transfer or cancellation of shares or related rights and gives rise to a CE 2 benefit. Otherwise check the ordinary bonus rules, including ACC and KiwiSaver, separately. [IS25/06, paragraphs 5-13 and 38-48][S75]

#### Exempt ESS: establish the scheme before excluding payroll

An amount derived from an exempt ESS is exempt income under CW 26B. CW 26C has 2 routes: a scheme with the Commissioner's approval under former DC 12 before its 2018 repeal, or the modern notified arrangement described below. A legacy approval, an IRD receipt or meeting the dollar limits alone does not establish every applicable condition. Keep the approval or notification, complete scheme terms, offer dates, employee/associate evidence, valuations, payments and annual returns. Actual legacy approvals and their continuing effect require separate review. [S100], [S101]

For the modern route, the Commissioner must have been notified under TAA 63B(1), the arrangement must meet CW 26C(2)–(9) and the Commissioner must have **received all forms due** under TAA 63B(2) and (3). Check receipt as well as submission. These provisions do not, by themselves, settle the timing or retrospective effect of a missed form or a later cure; obtain a specific determination before treating a non-compliant scheme as exempt or reclassifying earlier payroll. [S101], [S106]

##### Purchase, value and participation conditions

For offers made **on or after 1 April 2025**, the increased limits apply for the **2025–26 and later income years**. A later purchase under an earlier offer does not establish that these limits apply. Section 27 of 2025 No 9 increased the share-value limit from $5,000 to **$7,500** and the discount limit from $2,000 to **$3,000**; earlier offers and other historical transitions need their own check. [S107, sections 2(34) and 27][S107]

| Condition | Required scheme provision or established input |
|---|---|
| Meaning of share | For CW 26C, CW 26F defines share, for a company whose shares are made available under an exempt ESS, as a **fully paid ordinary share** that **ranks equally with, and has the same designation as, an existing ordinary voting share** in the company. A partly paid share is not a share for CW 26C. Establish the offered shares' terms and designation. [S112] |
| Price and annual amounts | Shares must be available for no more than market value at purchase/subscription. Shares purchased/subscribed for by the employee or a trustee for them have market value of no more than **$7,500 in a year**. That market value less the employee's spending on the shares is no more than **$3,000 in a year**. Aggregate the relevant purchases, rather than testing each grant in isolation. [S101, subsection (2)][S101] |
| Meaning of year | YA 1 defines year as a **12-month period**. Establish the relevant period for the arrangement and its purchases; do not assume a fresh allowance on 1 April merely because the separate annual return uses a tax year. [S98], [S101] |
| Market value | CW 26DB imports YA 1 market value (a)/(b): a quoted share/option ordinarily uses the middle market quotation for the same terms, subject to the fair-reflection qualification; an unquoted one uses the arm's-length willing-purchaser amount, with a commercially acceptable, fair and reasonable valuation method. Appropriate income, cash-flow or asset methods may be relevant. CW 26DB also permits the **5-day volume weighted average price**, another Commissioner-accepted method or a comparable method for quoted shares/options. This guide does not establish an actual valuation or recognised-exchange status. [S98], [S103] |
| Employee and ownership | CW 26D requires employment by the company. It excludes a non-employed director, a company/other body and a person who, with any associated person, holds **10% or more** of issued capital. Exactly 10% is excluded. Establish association and the relevant holdings; an employee's own holding below 10% is insufficient evidence. [S102] |
| Equal participation | A full-time permanent employee receiving an offer must be eligible on an equal basis with **90% or more of other full-time permanent employees whose offers are not subject to foreign security disclosure rules**. If the arrangement applies to part-time employees or seasonal workers, apply the same statutory test separately to that class. Establish the actual comparison pool, foreign-disclosure qualification and equal terms, rather than using an unqualified whole-workforce percentage. [S101, subsection (3)(a)–(c)][S101] |
| Minimum spending/service | A required minimum spend must be no more than **$1,000 in a year**; this limits the required minimum, not an employee's voluntary spending. Any service requirement must be no more than **3 years** of full-time work, or an accumulated equivalent for other employees. [S101, subsection (3)(d)–(e)][S101] |
| Trust dividends | If a trust holds shares for an employee, the trustee must pay dividends directly to the employee and the dividends must be treated as derived by that employee. For CW 26C, CW 26G defines trustee as a group of persons appointed to administer an exempt ESS of a company that employs an employee, and to hold shares under that scheme on trust for the employee during any period of restriction described in CW 26C(7). Exemption of the scheme benefit does not establish exemption of dividends. [S101, subsection (3B)][S101], [S113] |

##### Financing, hardship, restrictions and exit

Where the employee must buy shares for **more than nominal consideration**, the arrangement must make a loan for their cost available or permit regular instalments at intervals of a month or less. Any purchase loan must be free of interest **and other charges**. Loans/regular instalments have terms of **36–60 months**. Loan repayments must be monthly or more frequent, with early repayment in full or part at the employee's discretion. For unpaid or parental leave lasting **more than a month**, regular instalments are suspended whilst on leave and the loan term is extended as appropriate; the direct-instalment alternative is also subject to that suspension provision. Keep this statutory extension qualification when testing the ordinary 60-month limit. [S101, subsection (4)][S101]

If continued participation causes or may cause serious hardship, the arrangement must provide, **with the employee's agreement**, for payment terms to be varied or withdrawal with a **market-value** buyback on the withdrawal day, subject to repayment of the outstanding loan. Ordinary withdrawal instead requires **1 month's notice** and buyback at the **lesser of market value on that day and the employee's cost**, again subject to the outstanding loan. Do not use the hardship price merely because an employee wants to leave. [S101, subsections (5)–(6)][S101]

For shares acquired below market value, the restriction period prohibits disposal except a takeover or similar share reorganisation. Its length is the **shorter** of (a) **3 years from acquisition or the loan repayment period, whichever is longer**, and (b) the period until employment ends with the employer, or the same-group employer following a transfer. A group transfer alone is not the stated employment-end event. For market-value acquisitions, the restriction is **no longer than** the shorter of that statutory period and an arrangement restriction ending on or after all loan repayment obligations cease. Preserve that separate market-value branch rather than imposing the discounted-share period on every purchase. [S101, subsection (7)][S101]

At restriction end, a subsection (8) scheme may provide transfer if needed or, at the employee's choice, buyback at the lesser of cost and then market value. If the scheme does not use that option, subsection (8B) requires that choice for a current employee but requires the lesser-value buyback for someone no longer employed. Subsection (9) overrides both where employment ends through **death, accident, sickness, redundancy or retirement at normal retiring age**: transfer to the former employee/estate as appropriate or, if the employee chooses, the lesser-value buyback. Do not presume every resignation receives that protected-exit treatment. [S101]

CW 26E defines normal retiring age as no less than **60**, with a **55** minimum for its specified female employee whose pre-**1 April 1978** employment contract entitles her to earlier retirement. It also allows an earlier age the Commissioner considers reasonable for the employment/business/occupation. Require the relevant contractual or Commissioner basis; an employee's chosen retirement date alone does not establish it. [S104]

##### Employer deductions and separate annual disclosure

DV 28 denies a party to an exempt ESS a deduction for related expenditure/loss, **except to the extent incurred in establishing or managing the scheme**. That exception removes this particular denial; it does not, by itself, establish positive deduction entitlement under all other rules. Keep acquisition/funding costs separate from evidenced establishment/management costs. [S105], [S99]

Notify Inland Revenue using **IR1211**. The October 2026 blank form requests the registered company name, company IRD number and a signed declaration that the arrangement meets CW 26C(2)–(9). The current IRD process sends that form to its published exempt-ESS address. TAA 63B(1) does not state a fixed 20-day initial deadline; do not import the separate deferred-share deadline. [S106], [S108], [S110]

For each tax year, provide the prescribed annual return **on or before 31 May following that tax year's end**. The October 2026 **IR1212** records the company, period start/end, **total value of shares granted, total employee contributions and number of employee recipients**. Reconcile those aggregates to individual scheme records and retain receipt evidence. The form's aggregate fields do not replace each employee's value/discount eligibility tests. IRD excludes exempt ESS benefits from ordinary employment information; use this separate disclosure process once exemption is established. An annual form submitted but not received is not sufficient evidence of the statutory receipt condition. [S101], [S106], [S109], [S111], [S85]

#### ESS value, taxing date and 2026 deferred shares

Determine the share scheme taxing date under CE 7B from the actual scheme conditions. It is ordinarily the earlier of qualifying beneficial ownership without the stated material risks/protections, or cancellation/transfer to a person outside the specified association. Subsection (2) ignores specified rights, including certain market-value transfer rights and immaterial risks. A vesting label or an ordinary disposal restriction alone does not establish the date. [S80]

Under CE 2, calculate **share value − consideration paid + consideration received − previous income** using the statutory definitions. If transfer/cancellation triggers the taxing date, do not add a market value as share value to the consideration received. Consideration can be paid or payable; replacement-scheme consideration and historic previous income have specific limits. A positive amount is a benefit; a negative amount is dealt with as a deduction under CE 2(3), not automatically negative payroll or a refund. Valuation evidence, historic transitions, replacement schemes and foreign-service allocation require their own actual-case checks. [S79]

For shares issued or transferred on or after **1 April 2026**, EA 4B can defer the taxing date to a qualifying liquidity event. The issuing company must be unlisted and outside a group containing a listed company. Designate qualifying shares **at issue or transfer** and notify **both** the Commissioner and the beneficiary within **20 days**, or by a later date allowed by the Commissioner. An unlisted-company description or a late internal designation does not establish eligibility. [S81], [S91]

The liquidity date is generally the earliest relevant listing, sale/transfer to a person outside the specified association, or cancellation, including company cessation. If that event occurs during a restriction preventing disposal, use the restriction's end date. EA 4B(4)(c) excludes specified share-only exchanges into another qualifying unlisted company. Keep evidence for those conditions and exceptions rather than using every sale or group reorganisation as a trigger. The March 2026 IRD summary is shorter than the enacted conditions; it predates assent and is not an exhaustive eligibility test. [S81], [S83], [S91]

#### Withholding, student loans and funding

| Established payment or benefit | Selected employee payroll treatment |
|---|---|
| Genuine cash-settled CE 2 ESS benefit | Withhold income tax using the applicable extra-pay method; deduct student loan where required. The employer cannot elect out of mandatory cash withholding. No ACC earners' levy or KiwiSaver deductions/employer contributions on the ESS benefit itself. |
| Share-settled benefit | The employer can ordinarily choose whether to withhold. An offer or scheme term requiring withholding creates an irrevocable RD 7B obligation for that benefit/employee and replacement benefits. A valid election requires calculation, payment and timely employment-information disclosure. If withholding applies, use extra-pay income tax and any required student-loan deduction, with no ACC or KiwiSaver on the benefit itself. |
| Share-settled benefit with no withholding | Report where required; the employee deals with income tax through their annual return and provisional tax if applicable. No withholding does not mean tax-free income. |
| Separate employer payment to fund tax or student loan on a share benefit | This is separate extra pay, outside CE 2's ESS benefit value. Establish its income-tax, ACC, student-loan and KiwiSaver treatment independently; the ESS exemptions do not extend to it. |

Sources: [S74], [IS25/06, paragraphs 5-13 and 103-125][S75], [S77], [S82], [IS25/07, paragraphs 35-71][S76], [S88]. The 2025 interpretation statements' illustrative rates are not the 2026-27 rate tables.

Apply the selected extra-pay income-tax method above to the established ESS benefit using the **excluding-ACC** rate. For student loans, first establish the notified SL/TTC code or other required notice and any special deduction certificate. The ordinary primary-pay threshold is available only once in the pay period; secondary SL extra pay has no threshold. Use the complete-dollar and cent rules in the student-loan method above, rather than a universal percentage of every benefit. [S2], [S22], [S24], [S84], [S88]

Document who funds each deduction. An employee-funded tax payment, agreed sale of their shares or agreed deduction from net salary does not itself give the employee an additional employer-funded benefit. An employer-funded payment does. For the latter, first calculate the income tax and any student-loan amount on the ESS benefit that the employer agreed to fund, then gross up that **additional payment**, not the share value. IS25/07 gives **gross additional payment = net funding required ÷ (1 − combined funded deduction rates)**. Include only deductions the employer funds, at their actual applicable rates and bases. Recheck the extra-pay band, ACC cap, loan threshold/certificate, KiwiSaver base/rate and statutory rounding after grossing up; a single flat divisor is insufficient if any boundary changes. Establish compulsory employer contributions and ESCT separately. An agreement to fund income tax alone does not fund the employee's student loan or KiwiSaver automatically. [IS25/07, paragraphs 47-67][S76]

These rules do not authorise a wage deduction or share sale without the required agreement. For child-support or competing notices on an ESS benefit, obtain Inland Revenue's direction; do not extend the ordinary protected-earnings example automatically. [S74], [IS25/06, paragraph 19][S75]

#### ESS income, filing and payment dates

Where CE 2(7)'s employment-information condition applies, CE 2(8)-(9) places income recognition on the **ESS deferral date, 20 days after the share scheme taxing date**. For qualifying employee deferred shares, first substitute the EA 4B liquidity date. A former employee's share benefit without withholding has the stated reporting exclusion and is ordinarily recognised on the taxing date, without this reporting-based deferral. [S79], [S80], [S85], [S86]

Report the ESS benefit in its **employee share scheme earnings** field, also in the **earnings not liable for ACC earners' levy** field. Use the current tax code, not the retired ESS code. Show PAYE and student loan deducted. Keep an employer's separate tax-funding payment in **gross earnings**, outside the ESS field, with its own levy treatment. Do not treat the ESS reporting value as additional cash wages. [S76], [S85]

TAA 23K permits payday reporting using the ESS deferral date or the specified twice-monthly method: deferral dates on the 1st-15th use the 15th; later dates use month end. File within **2 working days** electronically or **10 working days** under allowed paper filing from the applicable reporting day. Exempt ESS benefits are excluded from this reporting regime; establish exemption separately. Former-employee share benefits without withholding are excluded, but withheld benefits must be reported. A cash payment to a former employee is not automatically covered by the share-only operational exception. [S85], [S86]

Filing and paying remain distinct. RD 6(3) supplies the deemed payment date for the elected non-cash benefit; RD 7B links the election to timely disclosure and RD 4 payment. For cash, RA 5(2) requires withholding when payment is made. Do not use an EI reporting concession as blanket authority to delay cash withholding or remittance. A separate funding payment uses its own actual payment facts; IS25/07's same-reporting-date example assumes aligned processing, rather than creating a universal ESS timing rule for the extra cash. Apply the established monthly/twice-monthly remittance schedule in `nz-employer-payroll` (Filing, remitting and records) and reconcile the streams. Unusual differences between cancellation, cash payment, deferral and funding dates need a specific Inland Revenue/qualified review before processing. [S76], [S77], [S87], [S89], [S90]

## Worked cases

These fictional cases assume the stated code, eligibility, contribution base and notices have already been established. They check the selected contribution, PAYE and student-loan arithmetic, not an actual person's liability. Cases 1 and 2 use the ordinary ESCT method rather than an agreed PAYE alternative. Set tolerance to zero so a cent error fails.

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

**Case 37: different contribution bases.** Assume $1,000 ordinary wages, $50 overtime, $200 bonus, $100 commission, $300 redundancy and $100 accommodation all validly classified as above. At a stated 3.5% employee rate, the KiwiSaver base is $1,350 and the complying-fund base is $1,050. The complying fund has no additional deed exclusions. These are alternative base calculations, not an instruction to enrol in both funds. [S38], [S33]

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

**Case 38: established historical default.** Assume records establish a surviving section 64(1)(ab) case for this employer/employee, with no overriding election or temporary reduction. The $1,000 KiwiSaver base produces a $40 employee deduction, not $35. The example does not infer eligibility from a joining date alone. [S45], [S49]

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

**Case 39: valid election overrides the legacy default.** For the same established historical case, assume the employer has received a valid election of 3.5% applying to this calculated payment. On a $1,000 base, deduct $35. [S45, subsections (2)–(3)][S45]

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

**Case 40: temporary reduction with unchanged employer rate.** Assume an approved 3% employee reduction applies and the employer retains 3.5%, with a shared $1,000 base and an established 17.5% ESCT rate. Employee $30, gross employer $35, ESCT $6.12 and net employer $28.88 remain separate amounts. [S9], [S50], [S12]

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

**Case 41: employer chooses the permitted reduced rate.** Assume the same valid temporary reduction and base, but the employer chooses 3% and no agreement requires more. At 17.5% ESCT, gross employer $30 becomes $24.75 net after $5.25 ESCT. [S50], [S12]

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

**Case 42: shared employer minimum across 2 funds.** Assume both funds qualify, each relevant base is $1,000, the ordinary minimum is 3.5% and a valid allocation contributes 2.5% to one fund and 1% to the other. Gross contributions of $25 and $10 meet the $35 aggregate minimum. This does not establish the employee deduction rates or any legacy offset. [S9], [S50]

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

**Case 43: voluntary unpaid-leave contribution.** Assume zero actual wages, a voluntary employer contribution of 3.5% of usual weekly pay of $1,500 and an established 30% ESCT rate. The $52.50 contribution uses a $52 ESCT base, producing $15.60 tax and $36.90 net. Usual pay is not reported as actual gross earnings. [S40], [S12]

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

**Case 44: voluntary employer contribution during a suspension.** Assume an approved suspension stops required employee deductions and the employer voluntarily contributes $30. With an established 17.5% ESCT rate and no agreed PAYE treatment, tax is $5.25 and net employer contribution $24.75. Suspension does not make the voluntary contribution tax free. [S9], [S33], [S12]

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

**Case 45: unforwarded employee deductions refunded once.** Assume a valid timely opt-out and 2 employee deductions of $35 each, neither filed nor paid to IRD. An employer refund of $70 clears this employee-deduction balance. It does not give the employee the employer contribution or ESCT. [S36]

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

**Case 46: reconcile employer contribution and ESCT separately.** Assume an accepted opt-out and 2 previously remitted gross employer contributions of $35, each with $6.12 ESCT and $28.88 net to the fund. The employer-side gross total $70 reconciles to $57.76 fund contributions plus $12.24 ESCT. These are separate refund/amendment streams, subject to IRD processing and debts; they are not an employee refund and no automatic ESCT refund is assumed. [S36], [S12]

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

**Case 59: a positive share-settled benefit.** Assume an established CE 2 benefit with market value $24,000, consideration paid $6,000, no consideration received or historic previous income, valid withholding and a derived 33% extra-pay rate. The benefit is $18,000 and income-tax withholding is $5,940, with no ACC or KiwiSaver on that benefit. This does not verify the market valuation or taxing date. [S74], [S79]

```oa-check
name: nz-2026-ess-share-value
tolerance: 0.001
inputs:
  share_value: 24000
  consideration_paid: 6000
  consideration_received: 0
  previous_income: 0
steps:
  benefit: share_value - consideration_paid + consideration_received - previous_income
  income_tax: benefit * 0.33
expected:
  benefit: 18000
  income_tax: 5940
```

**Case 60: cancellation uses consideration received.** Assume cancellation triggers the taxing date, $15,000 is paid for the rights and $2,000 was paid for them, with no previous income. Share value in this formula is zero; do not add another $15,000 market value. At an established 33% extra-pay rate the $13,000 benefit has $4,290 income tax. [S75], [S79]

```oa-check
name: nz-2026-ess-cancellation-value
tolerance: 0.001
inputs:
  share_value: 0
  consideration_paid: 2000
  consideration_received: 15000
  previous_income: 0
steps:
  benefit: share_value - consideration_paid + consideration_received - previous_income
  income_tax: benefit * 0.33
expected:
  benefit: 13000
  income_tax: 4290
```

**Case 61: a negative formula is preserved for review.** Assume the statutory formula has share value $1,000, consideration paid $2,000 and no other items. The result is negative $1,000, within CE 2(3)'s deduction rule. This arithmetic does not authorise a negative employment-information payment, offset or payroll refund. [S79]

```oa-check
name: nz-2026-ess-negative-formula
tolerance: 0.001
inputs:
  share_value: 1000
  consideration_paid: 2000
  consideration_received: 0
  previous_income: 0
steps:
  formula_result: share_value - consideration_paid + consideration_received - previous_income
expected:
  formula_result: -1000
```

**Case 62: genuine cash settlement with the loan threshold already used.** Assume a $5,000 genuine cash-settled benefit, ordinary 30% extra-pay income-tax rate, required SL deductions and no remaining primary threshold or special certificate. Income tax is $1,500, student loan $600 and net cash $2,900. No ACC, employee KiwiSaver or employer KiwiSaver applies to this benefit. The classification is an input, not established by the calculation. [S74], [S75], [S84], [S88]

```oa-check
name: nz-2026-ess-cash-with-loan
tolerance: 0.001
inputs:
  benefit: 5000
steps:
  income_tax: benefit * 0.30
  student_loan: floor(benefit) * 0.12
  net_cash: benefit - income_tax - student_loan
expected:
  income_tax: 1500
  student_loan: 600
  net_cash: 2900
```

**Case 63: employee-funded withholding creates no employer bonus.** Assume the same $5,000 value is provided in shares, with valid withholding, a 30% rate and SL on the full amount. The employee agrees to fund the $1,500 tax and $600 loan deduction from their own resources. Required funding is $2,100; it is not an additional employer-funded gross payment. No share sale, wage deduction or sufficient cash balance is proved here. [S74], [S76], [S77]

```oa-check
name: nz-2026-ess-employee-funded-withholding
tolerance: 0.001
inputs:
  benefit: 5000
steps:
  income_tax: benefit * 0.30
  student_loan: floor(benefit) * 0.12
  employee_funding: income_tax + student_loan
expected:
  income_tax: 1500
  student_loan: 600
  employee_funding: 2100
```

**Case 64: primary student loan uses only the remaining threshold.** Assume a weekly M SL employee, ordinary pay $300, $464 threshold, no other extra pay or certificate and a $1,000 genuine cash ESS benefit in that pay period. Ordinary four-week pay of $1,200 gives annualised base $15,600, so the extra-pay income-tax rate is 17.5%. Only $164 of threshold remains for the ESS benefit. Income tax is $175, loan $100.32 and net benefit cash $724.68. The regular pay itself has no standard loan deduction. [S2], [S24], [S74], [S84], [S88]

```oa-check
name: nz-2026-ess-main-loan-remaining-threshold
tolerance: 0.001
inputs:
  regular_pay: 300
  weekly_threshold: 464
  benefit: 1000
steps:
  remaining_threshold: max(0, weekly_threshold - regular_pay)
  loan_base: floor(max(0, benefit - remaining_threshold))
  student_loan: loan_base * 0.12
  income_tax: benefit * 0.175
  net_cash: benefit - income_tax - student_loan
expected:
  remaining_threshold: 164
  loan_base: 836
  student_loan: 100.32
  income_tax: 175
  net_cash: 724.68
```

**Case 65: secondary student loan has no threshold.** Assume an S SL employee with derived extra-pay income-tax rate 17.5%, a $1,000 genuine cash ESS benefit and no special certificate. Withhold $175 income tax and $120 loan, leaving $705. Do not subtract the primary weekly threshold from this secondary payment. [S2], [S24], [S74], [S84], [S88]

```oa-check
name: nz-2026-ess-secondary-loan-no-threshold
tolerance: 0.001
inputs:
  benefit: 1000
steps:
  income_tax: benefit * 0.175
  student_loan: floor(benefit) * 0.12
  net_cash: benefit - income_tax - student_loan
expected:
  income_tax: 175
  student_loan: 120
  net_cash: 705
```

**Case 66: the funding payment attracts ACC.** Assume a $4,550 share benefit, valid withholding and an employer agreement to fund its tax and the tax/ACC on the additional payment. Annualised base is $60,000, so the benefit plus the $2,000 funding gross stays in the 30% band and below the ACC cap. There is no SL, KiwiSaver membership or employer contribution obligation. The ESS tax is $1,365. Grossing that funding amount up for 30% tax and 1.75% ACC gives $2,000, including $600 tax and $35 ACC, leaving $1,365 to fund the ESS tax. The benefit remains $4,550 in the ESS field; the $2,000 is separate gross earnings. [S2], [S24], [S74], [S76], [S85]

```oa-check
name: nz-2026-ess-funded-tax-acc-separate
tolerance: 0.001
inputs:
  benefit: 4550
  annualised_base: 60000
steps:
  ess_tax: benefit * 0.30
  funding_gross: ess_tax / (1 - 0.30 - 0.0175)
  funding_tax: funding_gross * 0.30
  funding_acc: funding_gross * 0.0175
  funding_net: funding_gross - funding_tax - funding_acc
  rate_comparison_total: annualised_base + benefit + funding_gross
expected:
  ess_tax: 1365
  funding_gross: 2000
  funding_tax: 600
  funding_acc: 35
  funding_net: 1365
  rate_comparison_total: 66550
```

**Case 67: funding income tax, loan and employee KiwiSaver.** Assume a $9,800 share benefit and valid withholding, annualised base $160,000, ordinary 33% income-tax rate, required 12% SL with the primary threshold already used and a valid 6% employee KiwiSaver instruction. The employer funds both benefit deductions and all applicable deductions on the additional payment. The $9,000 additional gross keeps the combined rate comparison at $178,800, within 33%; ACC is zero because the established annualised base already exceeds $156,641. ESS tax $3,234 plus loan $1,176 needs $4,410 funding. The additional gross has $2,970 tax, $1,080 loan and $540 employee KiwiSaver, leaving $4,410. A separately established 3.5% compulsory employer contribution on that additional gross is $315 before its own ESCT; none is due on the ESS benefit. [S2], [S24], [S74], [S76], [S88]

```oa-check
name: nz-2026-ess-all-deductions-funded
tolerance: 0.001
inputs:
  benefit: 9800
  annualised_base: 160000
  employee_kiwisaver_rate: 0.06
  employer_rate: 0.035
steps:
  ess_tax: benefit * 0.33
  ess_loan: floor(benefit) * 0.12
  net_funding: ess_tax + ess_loan
  funding_gross: net_funding / (1 - 0.33 - 0.12 - employee_kiwisaver_rate)
  funding_tax: funding_gross * 0.33
  funding_loan: floor(funding_gross) * 0.12
  employee_kiwisaver: funding_gross * employee_kiwisaver_rate
  funding_net: funding_gross - funding_tax - funding_loan - employee_kiwisaver
  employer_gross: funding_gross * employer_rate
  rate_comparison_total: annualised_base + benefit + funding_gross
expected:
  ess_tax: 3234
  ess_loan: 1176
  net_funding: 4410
  funding_gross: 9000
  funding_tax: 2970
  funding_loan: 1080
  employee_kiwisaver: 540
  funding_net: 4410
  employer_gross: 315
  rate_comparison_total: 178800
```

**Case 68: tax-only funding above the ACC cap.** Assume annualised base $200,000, an established $6,100 share benefit, valid withholding and an employer agreement to fund all income tax. There is no SL or KiwiSaver obligation and no ACC on the additional payment at this established base. The 39% benefit tax is $2,379; a separate gross payment of $3,900 has $1,521 tax and leaves $2,379. The gross-up applies to the funding payment, not to $6,100 of share value. [S2], [S24], [S74], [S76]

```oa-check
name: nz-2026-ess-tax-only-above-acc-cap
tolerance: 0.001
inputs:
  benefit: 6100
steps:
  ess_tax: benefit * 0.39
  funding_gross: ess_tax / (1 - 0.39)
  funding_tax: funding_gross * 0.39
  funding_net: funding_gross - funding_tax
expected:
  ess_tax: 2379
  funding_gross: 3900
  funding_tax: 1521
  funding_net: 2379
```

**Case 75: modern exempt ESS at both amount limits.** Assume a qualifying post-1 April 2025 offer in the current income year, an established relevant 12-month cap period, market value of $7,500 and voluntary employee spending of $4,500 across all purchases in that period. The discount is $3,000, with no headroom in either limit. A qualifying interest/charge-free $4,500 loan over 36 monthly payments is $125 a month before any statutory leave suspension, assuming equal payments; CW 26C(4)(d) requires regular instalments of a month or less, not equal ones. Assume every other scheme and receipt condition is satisfied; these amounts alone do not prove exemption. [S101], [S107]

```oa-check
name: nz-2026-exempt-ess-exact-limits
tolerance: 0
inputs:
  market_value: 7500
  employee_cost: 4500
  value_limit: 7500
  discount_limit: 3000
  loan_months: 36
steps:
  discount: market_value - employee_cost
  value_headroom: value_limit - market_value
  discount_headroom: discount_limit - discount
  monthly_payment: employee_cost / loan_months
expected:
  discount: 3000
  value_headroom: 0
  discount_headroom: 0
  monthly_payment: 125
```

**Case 76: share-value limit exceeded by a cent.** Under the same modern offer/period assumptions, total share value is $7,500.01 and employee cost is $4,500.01. The $3,000 discount meets its limit, but share value exceeds its separate limit by $0.01. Do not accept the arrangement on the discount test alone. The tax consequences of failed exemption require separate review. [S101], [S107]

```oa-check
name: nz-2026-exempt-ess-value-excess
tolerance: 0
inputs:
  market_value: 7500.01
  employee_cost: 4500.01
  value_limit: 7500
steps:
  discount: market_value - employee_cost
  value_excess: market_value - value_limit
expected:
  discount: 3000
  value_excess: 0.01
```

**Case 77: discount limit exceeded by a cent.** Under the same modern offer/period assumptions, total share value is $7,500 and employee cost is $4,499.99. Value meets its limit, but the $3,000.01 discount exceeds its separate limit by $0.01. Do not treat the value test as sufficient. [S101], [S107]

```oa-check
name: nz-2026-exempt-ess-discount-excess
tolerance: 0
inputs:
  market_value: 7500
  employee_cost: 4499.99
  discount_limit: 3000
steps:
  discount: market_value - employee_cost
  discount_excess: discount - discount_limit
expected:
  discount: 3000.01
  discount_excess: 0.01
```

**Case 78: associated holdings reach the exclusion.** Assume the employee holds 8% and a separately established associated person holds 2% of issued capital, without overlap. The combined holding is exactly 10%, so CW 26D excludes this person. This calculation does not establish association or ownership facts. [S102]

```oa-check
name: nz-2026-exempt-ess-associated-holding
tolerance: 0
inputs:
  employee_percent: 8
  associate_percent: 2
  exclusion_percent: 10
steps:
  combined_percent: employee_percent + associate_percent
  margin_to_exclusion: exclusion_percent - combined_percent
expected:
  combined_percent: 10
  margin_to_exclusion: 0
```

**Case 79: statutory equal-participation pool.** For a particular full-time permanent offeree, assume the legally established pool of other full-time permanent employees is 110, of whom 10 have offers subject to foreign security disclosure rules. Of the remaining 100, 90 are eligible on an equal basis. That is exactly 90%. This conditional pool calculation does not prove the scheme-wide test for every offeree or the separate part-time/seasonal tests. [S101]

```oa-check
name: nz-2026-exempt-ess-other-employee-pool
tolerance: 0
inputs:
  other_employees: 110
  foreign_disclosure: 10
  equal_eligible: 90
steps:
  comparison_pool: other_employees - foreign_disclosure
  eligible_percent: equal_eligible / comparison_pool * 100
expected:
  comparison_pool: 100
  eligible_percent: 90
```

**Case 80: discounted shares and actual group employment end.** Assume discounted shares, a 48-month loan repayment period and actual employment ending 24 months after acquisition, including any same-group employment following transfer. The restriction is the shorter of 48 months (the longer of 36 and 48) and 24 months, hence 24 months. The applicable exit/transfer/buyback rule still needs separate application. [S101, subsections (7)–(9)][S101]

```oa-check
name: nz-2026-exempt-ess-employment-end-restriction
tolerance: 0
inputs:
  three_year_months: 36
  loan_period_months: 48
  employment_end_months: 24
steps:
  longer_period: max(three_year_months, loan_period_months)
  restriction_months: min(longer_period, employment_end_months)
expected:
  longer_period: 48
  restriction_months: 24
```

**Case 81: early repayment does not remove the 3-year limb.** Assume discounted shares, a 36-month loan paid off voluntarily after 12 months, continuing qualifying employment until month 60 and no other exception. Even using the actual 12-month repayment period, the longer-of test retains 36 months; restriction ends at month 36 on these facts. This does not determine the effect of leave extensions or different loan terms. [S101]

```oa-check
name: nz-2026-exempt-ess-early-repayment
tolerance: 0
inputs:
  three_year_months: 36
  actual_repayment_months: 12
  employment_end_months: 60
steps:
  longer_period: max(three_year_months, actual_repayment_months)
  restriction_months: min(longer_period, employment_end_months)
expected:
  longer_period: 36
  restriction_months: 36
```

**Case 82: ordinary and qualifying hardship withdrawal prices.** Assume employee cost of $4,500, withdrawal-day market value of $6,000 and a $1,000 outstanding loan. An ordinary withdrawal with the required notice gives a $4,500 buyback and $3,500 after loan repayment. A separately established serious-hardship withdrawal with the employee agreement required by subsection (5) gives a $6,000 buyback and $5,000 after repayment. These are alternative established cases, not an employee election to claim the higher price without hardship. [S101]

```oa-check
name: nz-2026-exempt-ess-withdrawal-prices
tolerance: 0
inputs:
  employee_cost: 4500
  market_value: 6000
  loan_balance: 1000
steps:
  ordinary_price: min(employee_cost, market_value)
  ordinary_after_loan: ordinary_price - loan_balance
  hardship_price: market_value
  hardship_after_loan: hardship_price - loan_balance
expected:
  ordinary_price: 4500
  ordinary_after_loan: 3500
  hardship_price: 6000
  hardship_after_loan: 5000
```

**Case 83: annual exempt scheme aggregates.** Assume 3 distinct employee recipients in the established tax-year reporting period, shares granted with total values of $7,500, $5,000 and $3,000, and respective employee contributions of $4,500, $3,000 and $1,000. IR1212 reports $15,500 share value, $8,500 contributions and 3 recipients. The $7,000 aggregate difference is a reconciliation amount, not a per-person discount allowance or an ordinary EI amount. Assume all individual eligibility and other scheme conditions have been independently established. [S106], [S111]

```oa-check
name: nz-2026-exempt-ess-annual-aggregates
tolerance: 0
inputs:
  shares_a: 7500
  shares_b: 5000
  shares_c: 3000
  contributions_a: 4500
  contributions_b: 3000
  contributions_c: 1000
  distinct_recipients: 3
steps:
  shares_total: shares_a + shares_b + shares_c
  contributions_total: contributions_a + contributions_b + contributions_c
  aggregate_difference: shares_total - contributions_total
  recipient_count: distinct_recipients
expected:
  shares_total: 15500
  contributions_total: 8500
  aggregate_difference: 7000
  recipient_count: 3
```

## When to refuse or refer

Refer, or hold for separate qualified checks, everything the method does not cover:

Still requiring separate actual-case checks: special PAYE codes beyond the selected ordinary NSW/CAE/EDW, certificate and extra-pay methods; exemption eligibility, recovery notices beyond the selected methods, other irregular pays and unresolved competing-notice/attachment cases; actual ESS scheme eligibility and receipt failures, legacy approvals and historic transitions, difficult valuations, replacement schemes and classification beyond the selected employee methods; schedular payments and payment classification; enrolment exceptions and mixed/late refund cases beyond the selected administration; historical-rate evidence, contribution classifications and legacy scheme offsets; cross-border employment and treaty/social-security questions; FBT; leave, holiday pay, minimum wage and termination entitlements; employer ACC invoices; employment-record requirements beyond selected tax retention; older/exceptional corrections, mixed EMP debt, current interest, other shortfall/criminal penalties and full remission/collection rules. No whole payroll, social-contribution or compliance topic is certified complete by this guide. It remains tier 2 and pending qualified review.

## Sources

| Source | URL | Read for | Read on |
| --- | --- | --- | --- |
| [S2] 2026-27 payroll specification, selected sections | https://www.ird.govt.nz/-/media/project/ir/home/documents/digital-service-providers/software-providers/payroll-calculations-business-rules-specifications/payroll-calculations-and-business-rules-specification.pdf?modified=20260401012317 | Read for 2026-27 payroll specification, selected sections | 2026-11-14 |
| [S7] KiwiSaver changes | https://www.ird.govt.nz/kiwisaver-changes | Read for KiwiSaver changes | 2026-11-14 |
| [S8] Employee KiwiSaver deductions | https://www.ird.govt.nz/kiwisaver/kiwisaver-for-employers/contributions-and-deductions/kiwisaver-deductions-from-employee-pay | Read for Employee KiwiSaver deductions | 2026-11-12 |
| [S9] Employer contributions | https://www.ird.govt.nz/kiwisaver/kiwisaver-for-employers/contributions-and-deductions/employer-contributions-to-kiwisaver-and-complying-funds | Read for Employer contributions | 2026-11-12 |
| [S10] ESCT scope and methods | https://www.ird.govt.nz/esct | Read for ESCT scope and methods | 2026-11-12 |
| [S11] Income Tax Act 2007, Schedule 1 Part D, current copy dated 4 September 2026 | https://www.legislation.govt.nz/act/public/2007/97/en/latest/parts/DLM1523173/ | Read for Income Tax Act 2007, Schedule 1 Part D, current copy dated 4 September 2026 | 2026-11-12 |
| [S12] Deducting ESCT | https://www.ird.govt.nz/employing-staff/deductions-from-income/employer-superannuation-contribution-tax/deduct-esct-from-each-employer-contribution | Read for Deducting ESCT | 2026-11-12 |
| [S13] IR335 employer guide, September 2026, selected pages | https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir300---ir399/ir335/ir335.pdf?modified=20250811232131 | Read for IR335 employer guide, September 2026, selected pages | 2026-11-12 |
| [S22] Non-termination lump-sum PAYE, updated 18 May 2026 | https://www.ird.govt.nz/calculate-lump-sum-paye | Read for Non-termination lump-sum PAYE, updated 18 May 2026 | 2026-11-12 |
| [S24] End-of-employment lump-sum PAYE, updated 20 April 2026 | https://www.ird.govt.nz/employing-staff/payday-filing/non-standard-filing-of-employment-information/lump-sum-payments/calculate-paye-for-a-lump-sum-payment-end-of-employment | Read for End-of-employment lump-sum PAYE, updated 20 April 2026 | 2026-11-12 |
| [S33] KS4 employer guide, cover April 2026, selected pages | https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir1---ir99/ks4/ks4.pdf?modified=20260129195326 | Read for KS4 employer guide, cover April 2026, selected pages | 2026-11-12 |
| [S34] Starting employees, updated 21 October 2026 | https://www.ird.govt.nz/kiwisaver/kiwisaver-for-employers/starting-employees-in-kiwisaver | Read for Starting employees, updated 21 October 2026 | 2026-11-12 |
| [S35] Automatic enrolment, updated 21 October 2026 | https://www.ird.govt.nz/kiwisaver/kiwisaver-for-employers/starting-employees-in-kiwisaver/auto-enrol-employees-into-kiwisaver | Read for Automatic enrolment, updated 21 October 2026 | 2026-11-12 |
| [S36] Employee opt-outs, updated 28 July 2026 | https://www.ird.govt.nz/kiwisaver/kiwisaver-employers/employees-who-want-to-opt-out-of-kiwisaver | Read for Employee opt-outs, updated 28 July 2026 | 2026-11-12 |
| [S37] Late opt-outs, updated 28 April 2021 | https://www.ird.govt.nz/kiwisaver/kiwisaver-employers/employees-who-want-to-opt-out-of-kiwisaver/employees-who-opt-out-late-from-kiwisaver | Read for Late opt-outs, updated 28 April 2021 | 2026-11-12 |
| [S38] KiwiSaver and complying-fund gross pay, updated 28 April 2021 | https://www.ird.govt.nz/kiwisaver/kiwisaver-employers/contributions-and-deductions/gross-pay-for-kiwisaver-and-complying-funds | Read for KiwiSaver and complying-fund gross pay, updated 28 April 2021 | 2026-11-12 |
| [S39] Temporary rate reduction, updated 1 April 2026 | https://www.ird.govt.nz/kiwisaver/kiwisaver-individuals/making-changes-to-my-kiwisaver/changing-my-kiwisaver-contribution-rate/temporary-rate-reduction | Read for Temporary rate reduction, updated 1 April 2026 | 2026-11-12 |
| [S40] Special employee circumstances, updated 1 October 2026 | https://www.ird.govt.nz/kiwisaver/kiwisaver-employers/contributions-and-deductions/employees-with-special-circumstances | Read for Special employee circumstances, updated 1 October 2026 | 2026-11-12 |
| [S41] 6 Application, current copy 1 April 2026 | https://www.legislation.govt.nz/act/public/2006/40/en/latest/sections/DLM378821/ | Read for 6 Application, current copy 1 April 2026 | 2026-11-12 |
| [S42] 10 Who automatic enrolment rules apply to, current copy 1 April 2026 | https://www.legislation.govt.nz/act/public/2006/40/en/latest/sections/DLM378830/ | Read for 10 Who automatic enrolment rules apply to, current copy 1 April 2026 | 2026-11-12 |
| [S43] 12 Temporary employment, current copy 1 April 2026 | https://www.legislation.govt.nz/act/public/2006/40/en/latest/sections/DLM378834/ | Read for 12 Temporary employment, current copy 1 April 2026 | 2026-11-12 |
| [S44] 14 Other situations when automatic enrolment rules do not apply, current copy 1 April 2026 | https://www.legislation.govt.nz/act/public/2006/40/en/latest/sections/DLM378843/ | Read for 14 Other situations when automatic enrolment rules do not apply, current copy 1 April 2026 | 2026-11-12 |
| [S45] 64 Contribution rate, current copy 1 April 2026 | https://www.legislation.govt.nz/act/public/2006/40/en/latest/sections/DLM379037/ | Read for 64 Contribution rate, current copy 1 April 2026 | 2026-11-12 |
| [S46] 101L How to apply for rate reduction, current copy 1 April 2026 | https://www.legislation.govt.nz/act/public/2006/40/en/latest/sections/LMS1569986/ | Read for 101L How to apply for rate reduction, current copy 1 April 2026 | 2026-11-12 |
| [S47] 101M Grant of rate reduction, current copy 1 April 2026 | https://www.legislation.govt.nz/act/public/2006/40/en/latest/sections/LMS1569987/ | Read for 101M Grant of rate reduction, current copy 1 April 2026 | 2026-11-12 |
| [S48] 101S Revocation of rate reduction, current copy 1 April 2026 | https://www.legislation.govt.nz/act/public/2006/40/en/latest/sections/LMS1569995/ | Read for 101S Revocation of rate reduction, current copy 1 April 2026 | 2026-11-12 |
| [S49] KiwiSaver Act section 60, current copy 1 April 2026 | https://www.legislation.govt.nz/act/public/2006/40/en/latest/sections/DLM379032/ | Read for KiwiSaver Act section 60, current copy 1 April 2026 | 2026-11-12 |
| [S50] KiwiSaver Act section 101D, current copy 1 April 2026 | https://www.legislation.govt.nz/act/public/2006/40/en/latest/sections/DLM1233474/ | Read for KiwiSaver Act section 101D, current copy 1 April 2026 | 2026-11-12 |
| [S74] IRD ESS withholding, updated 28 October 2026 | https://www.ird.govt.nz/employing-staff/deductions-from-other-payments/employee-share-schemes/deducting-tax-on-ess-benefits | Read for IRD ESS withholding, updated 28 October 2026 | 2026-11-13 |
| [S75] IS25/06, 31 March 2025; selected paragraphs, employee scope | https://www.taxtechnical.ird.govt.nz/-/media/project/ir/tt/pdfs/interpretation-statements/2025/is-25-06.pdf?modified=20250331012659 | Read for IS25/06, 31 March 2025; selected paragraphs, employee scope | 2026-11-13 |
| [S76] IS25/07, 31 March 2025; selected funding/reporting paragraphs | https://www.taxtechnical.ird.govt.nz/-/media/project/ir/tt/pdfs/interpretation-statements/2025/is-25-07.pdf?modified=20250331012754 | Read for IS25/07, 31 March 2025; selected funding/reporting paragraphs | 2026-11-13 |
| [S77] Income Tax Act RD7B, copy 4 September 2026 | https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM7269557/ | Read for Income Tax Act RD7B, copy 4 September 2026 | 2026-11-13 |
| [S78] Income Tax Act CE7, copy 4 September 2026 | https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1512798/ | Read for Income Tax Act CE7, copy 4 September 2026 | 2026-11-13 |
| [S79] Income Tax Act CE2, copy 4 September 2026 | https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1512781/ | Read for Income Tax Act CE2, copy 4 September 2026 | 2026-11-13 |
| [S80] Income Tax Act CE7B, copy 4 September 2026 | https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/LMS92763/ | Read for Income Tax Act CE7B, copy 4 September 2026 | 2026-11-13 |
| [S81] Income Tax Act EA4B, copy 4 September 2026 | https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/LMS1593301/ | Read for Income Tax Act EA4B, copy 4 September 2026 | 2026-11-13 |
| [S82] Income Tax Act RD7, copy 4 September 2026 | https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1519952/ | Read for Income Tax Act RD7, copy 4 September 2026 | 2026-11-13 |
| [S83] IRD employee deferred shares, updated 16 March 2026; qualify by enacted law | https://www.ird.govt.nz/employing-staff/deductions-from-other-payments/employee-share-schemes/ess-rules/tax-on-employee-deferred-shares | Read for IRD employee deferred shares, updated 16 March 2026; qualify by enacted law | 2026-11-13 |
| [S84] IRD lump sum payments, updated 27 January 2026 | https://www.ird.govt.nz/employing-staff/payday-filing/non-standard-filing-of-employment-information/lump-sum-payments | Read for IRD lump sum payments, updated 27 January 2026 | 2026-11-13 |
| [S85] IRD ESS employment information, updated 28 October 2026 | https://www.ird.govt.nz/employing-staff/payday-filing/non-standard-filing-of-employment-information/employee-share-scheme-benefits | Read for IRD ESS employment information, updated 28 October 2026 | 2026-11-13 |
| [S86] Tax Administration Act23K, copy 1 October 2026 | https://www.legislation.govt.nz/act/public/1994/166/en/latest/sections/LMS191845/ | Read for Tax Administration Act23K, copy 1 October 2026 | 2026-11-13 |
| [S87] Income Tax Act RD6, copy 4 September 2026 | https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1519950/ | Read for Income Tax Act RD6, copy 4 September 2026 | 2026-11-13 |
| [S88] Student Loan Scheme Act2011 s4 and ss36-37, copy 1 April 2026 | https://www.legislation.govt.nz/act/public/2011/62/en/latest/ | Read for Student Loan Scheme Act2011 s4 and ss36-37, copy 1 April 2026 | 2026-11-13 |
| [S89] Income Tax Act RD4, copy 4 September 2026 | https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1519944/ | Read for Income Tax Act RD4, copy 4 September 2026 | 2026-11-13 |
| [S90] Income Tax Act RA5, copy 4 September 2026 | https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1519735/ | Read for Income Tax Act RA5, copy 4 September 2026 | 2026-11-13 |
| [S91] 2026 No8 sections2,10,51,114; selected commencement and application | https://www.legislation.govt.nz/act/public/2026/8/en/latest/ | Read for 2026 No8 sections2,10,51,114; selected commencement and application | 2026-11-13 |
| [S98] Income Tax Act YA 1 selected worker, market value and year definitions, copy 4 September 2026 | https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1520575/ | Read for Income Tax Act YA 1 selected worker, market value and year definitions, copy 4 September 2026 | 2026-11-13 |
| [S99] IRD exempt employee share schemes, updated 13 November 2026; statutory qualifications apply | https://www.ird.govt.nz/employing-staff/deductions-from-other-payments/exempt-employee-share-schemes | Read for IRD exempt employee share schemes, updated 13 November 2026; statutory qualifications apply | 2026-11-13 |
| [S100] Income Tax Act CW26B, copy 4 September 2026 | https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/LMS32342/ | Read for Income Tax Act CW26B, copy 4 September 2026 | 2026-11-13 |
| [S101] Income Tax Act CW26C, copy 4 September 2026 | https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/LMS32492/ | Read for Income Tax Act CW26C, copy 4 September 2026 | 2026-11-13 |
| [S102] Income Tax Act CW26D, copy 4 September 2026 | https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/LMS32494/ | Read for Income Tax Act CW26D, copy 4 September 2026 | 2026-11-13 |
| [S103] Income Tax Act CW26DB, copy 4 September 2026 | https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/LMS328941/ | Read for Income Tax Act CW26DB, copy 4 September 2026 | 2026-11-13 |
| [S104] Income Tax Act CW26E, copy 4 September 2026 | https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/LMS32496/ | Read for Income Tax Act CW26E, copy 4 September 2026 | 2026-11-13 |
| [S105] Income Tax Act DV28, copy 4 September 2026 | https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/LMS33459/ | Read for Income Tax Act DV28, copy 4 September 2026 | 2026-11-13 |
| [S106] Tax Administration Act63B, copy 1 October 2026 | https://www.legislation.govt.nz/act/public/1994/166/en/latest/sections/LMS32667/ | Read for Tax Administration Act63B, copy 1 October 2026 | 2026-11-13 |
| [S107] 2025 No9 sections2(34) and27, offer-date application of exempt ESS limits | https://www.legislation.govt.nz/act/public/2025/9/en/latest/ | Read for 2025 No9 sections2(34) and27, offer-date application of exempt ESS limits | 2026-11-13 |
| [S108] IRD initial exempt ESS notification, updated 22 October 2026 | https://www.ird.govt.nz/employing-staff/deductions-from-other-payments/exempt-employee-share-schemes/report-exempt-ess | Read for IRD initial exempt ESS notification, updated 22 October 2026 | 2026-11-13 |
| [S109] IRD annual exempt ESS reporting, updated 22 October 2026 | https://www.ird.govt.nz/employing-staff/deductions-from-other-payments/exempt-employee-share-schemes/report-employee-shares-under-exempt-ess | Read for IRD annual exempt ESS reporting, updated 22 October 2026 | 2026-11-13 |
| [S110] IR1211 initial exempt ESS notification, October 2026, page1 | https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir1200---ir1299/ir1211/ir1211.pdf?modified=20261022002436 | Read for IR1211 initial exempt ESS notification, October 2026, page1 | 2026-11-13 |
| [S111] IR1212 annual exempt ESS return, October 2026, page1 | https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir1200---ir1299/ir1212/ir1212.pdf?modified=20261022002438 | Read for IR1212 annual exempt ESS return, October 2026, page1 | 2026-11-13 |
| [S112] Income Tax Act CW26F, copy 4 September 2026 | https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/LMS32498/ | Read for Income Tax Act CW26F, copy 4 September 2026 | 2026-11-13 |
| [S113] Income Tax Act CW26G, copy 4 September 2026 | https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/LMS32500/ | Read for Income Tax Act CW26G, copy 4 September 2026 | 2026-11-13 |

Not yet confirmed: legislation.govt.nz refused automated fetches in this conforming pass (2026-11-14), so the Act and regulation sections were not re-opened; their read dates are the writer's checks of 12 and 13 November 2026. Re-read on 2026-11-14: the KiwiSaver changes page (3.5% from 1 April 2026, 4% from 1 April 2028, 3% temporary reduction for 3 to 12 months, 16- and 17-year-olds). The ESCT bands are taken from the 2026-27 payroll specification section 5.20.4; Inland Revenue's ESCT web pages read on 2026-11-14 do not print the table. IR335 page 27's Matthew ESCT example ($35.73) conflicts with the whole-dollar rule and is not followed. No accountant has reviewed this draft.

### Provenance and link references

Inherited sources checked 12 November 2026; selected ESS sources checked 13 November 2026. Selected District Court Act sections use the current copy dated 17 February 2026; Tax Administration Act section 157 uses the current copy dated 1 October 2026. SPS 21/01 is dated 12 April 2021 and remains linked by IRD's arrears page updated 16 April 2026. Extra-pay and deduction examples are recalculated from the stated rules; known inconsistent printed examples and boundary wording are recorded in the verification log. The technical specification is dated 24 March 2026, version 1.0, and expressly covers 1 April 2026 to 31 March 2027. IR335's cover says September 2026. KS4's cover says April 2026. Selected KiwiSaver Act provisions use the current copy dated 1 April 2026. The verification log records the selected native/image page scope, the surviving legacy default and conflicting sample-letter/example wording. The selected correction regulations use the 30 March 2026 consolidation. Selected TAA record, assessment and penalty provisions use the 1 October 2026 copy. Its full-Act page flags unincorporated amendments; the selected amendment-impact check is recorded in the verification log. SPS19/04 is dated 30 May 2019. Current statutory wording controls the affected-employee penalty base and inclusive $100 exemption. These checks do not claim full PDF or statute review.

[S2]: https://www.ird.govt.nz/-/media/project/ir/home/documents/digital-service-providers/software-providers/payroll-calculations-business-rules-specifications/payroll-calculations-and-business-rules-specification.pdf?modified=20260401012317
[S7]: https://www.ird.govt.nz/kiwisaver-changes
[S8]: https://www.ird.govt.nz/kiwisaver/kiwisaver-for-employers/contributions-and-deductions/kiwisaver-deductions-from-employee-pay
[S9]: https://www.ird.govt.nz/kiwisaver/kiwisaver-for-employers/contributions-and-deductions/employer-contributions-to-kiwisaver-and-complying-funds
[S10]: https://www.ird.govt.nz/esct
[S11]: https://www.legislation.govt.nz/act/public/2007/97/en/latest/parts/DLM1523173/
[S12]: https://www.ird.govt.nz/employing-staff/deductions-from-income/employer-superannuation-contribution-tax/deduct-esct-from-each-employer-contribution
[S13]: https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir300---ir399/ir335/ir335.pdf?modified=20250811232131
[S22]: https://www.ird.govt.nz/calculate-lump-sum-paye
[S24]: https://www.ird.govt.nz/employing-staff/payday-filing/non-standard-filing-of-employment-information/lump-sum-payments/calculate-paye-for-a-lump-sum-payment-end-of-employment
[S33]: https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir1---ir99/ks4/ks4.pdf?modified=20260129195326
[S34]: https://www.ird.govt.nz/kiwisaver/kiwisaver-for-employers/starting-employees-in-kiwisaver
[S35]: https://www.ird.govt.nz/kiwisaver/kiwisaver-for-employers/starting-employees-in-kiwisaver/auto-enrol-employees-into-kiwisaver
[S36]: https://www.ird.govt.nz/kiwisaver/kiwisaver-employers/employees-who-want-to-opt-out-of-kiwisaver
[S37]: https://www.ird.govt.nz/kiwisaver/kiwisaver-employers/employees-who-want-to-opt-out-of-kiwisaver/employees-who-opt-out-late-from-kiwisaver
[S38]: https://www.ird.govt.nz/kiwisaver/kiwisaver-employers/contributions-and-deductions/gross-pay-for-kiwisaver-and-complying-funds
[S39]: https://www.ird.govt.nz/kiwisaver/kiwisaver-individuals/making-changes-to-my-kiwisaver/changing-my-kiwisaver-contribution-rate/temporary-rate-reduction
[S40]: https://www.ird.govt.nz/kiwisaver/kiwisaver-employers/contributions-and-deductions/employees-with-special-circumstances
[S41]: https://www.legislation.govt.nz/act/public/2006/40/en/latest/sections/DLM378821/
[S42]: https://www.legislation.govt.nz/act/public/2006/40/en/latest/sections/DLM378830/
[S43]: https://www.legislation.govt.nz/act/public/2006/40/en/latest/sections/DLM378834/
[S44]: https://www.legislation.govt.nz/act/public/2006/40/en/latest/sections/DLM378843/
[S45]: https://www.legislation.govt.nz/act/public/2006/40/en/latest/sections/DLM379037/
[S46]: https://www.legislation.govt.nz/act/public/2006/40/en/latest/sections/LMS1569986/
[S47]: https://www.legislation.govt.nz/act/public/2006/40/en/latest/sections/LMS1569987/
[S48]: https://www.legislation.govt.nz/act/public/2006/40/en/latest/sections/LMS1569995/
[S49]: https://www.legislation.govt.nz/act/public/2006/40/en/latest/sections/DLM379032/
[S50]: https://www.legislation.govt.nz/act/public/2006/40/en/latest/sections/DLM1233474/
[S74]: https://www.ird.govt.nz/employing-staff/deductions-from-other-payments/employee-share-schemes/deducting-tax-on-ess-benefits
[S75]: https://www.taxtechnical.ird.govt.nz/-/media/project/ir/tt/pdfs/interpretation-statements/2025/is-25-06.pdf?modified=20250331012659
[S76]: https://www.taxtechnical.ird.govt.nz/-/media/project/ir/tt/pdfs/interpretation-statements/2025/is-25-07.pdf?modified=20250331012754
[S77]: https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM7269557/
[S78]: https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1512798/
[S79]: https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1512781/
[S80]: https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/LMS92763/
[S81]: https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/LMS1593301/
[S82]: https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1519952/
[S83]: https://www.ird.govt.nz/employing-staff/deductions-from-other-payments/employee-share-schemes/ess-rules/tax-on-employee-deferred-shares
[S84]: https://www.ird.govt.nz/employing-staff/payday-filing/non-standard-filing-of-employment-information/lump-sum-payments
[S85]: https://www.ird.govt.nz/employing-staff/payday-filing/non-standard-filing-of-employment-information/employee-share-scheme-benefits
[S86]: https://www.legislation.govt.nz/act/public/1994/166/en/latest/sections/LMS191845/
[S87]: https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1519950/
[S88]: https://www.legislation.govt.nz/act/public/2011/62/en/latest/
[S89]: https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1519944/
[S90]: https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1519735/
[S91]: https://www.legislation.govt.nz/act/public/2026/8/en/latest/
[S98]: https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/DLM1520575/
[S99]: https://www.ird.govt.nz/employing-staff/deductions-from-other-payments/exempt-employee-share-schemes
[S100]: https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/LMS32342/
[S101]: https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/LMS32492/
[S102]: https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/LMS32494/
[S103]: https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/LMS328941/
[S104]: https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/LMS32496/
[S105]: https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/LMS33459/
[S106]: https://www.legislation.govt.nz/act/public/1994/166/en/latest/sections/LMS32667/
[S107]: https://www.legislation.govt.nz/act/public/2025/9/en/latest/
[S108]: https://www.ird.govt.nz/employing-staff/deductions-from-other-payments/exempt-employee-share-schemes/report-exempt-ess
[S109]: https://www.ird.govt.nz/employing-staff/deductions-from-other-payments/exempt-employee-share-schemes/report-employee-shares-under-exempt-ess
[S110]: https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir1200---ir1299/ir1211/ir1211.pdf?modified=20261022002436
[S111]: https://www.ird.govt.nz/-/media/project/ir/home/documents/forms-and-guides/ir1200---ir1299/ir1212/ir1212.pdf?modified=20261022002438
[S112]: https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/LMS32498/
[S113]: https://www.legislation.govt.nz/act/public/2007/97/en/latest/sections/LMS32500/
