---
name: cc-super-guarantee
description: >
  Selected Cocos (Keeling) Islands employer superannuation guarantee rules for
  2026-27. Covers territorial application, employee and labour-contractor
  status, qualifying earnings and exclusions, annual employer ceiling,
  salary sacrifice, fund choice, employer readiness, SuperStream, STP
  transition/corrections, contribution receipt, conditional deadlines and the
  Payday Super changeover. Use for island employer super, low
  earnings, annual-base crossings, new funds, out-of-cycle payments or
  late-contribution questions. Includes primary legislation, ATO guidance,
  fictional component calculations, remittance patterns and reviewer
  controls. This source-cited draft preserves both workflow bases and
  identifies missing programmes and operational requirements; it does not
  complete a payroll run, social-contribution engagement or country pack.
jurisdiction: CC
category: international
tax_year: 2026
tax_year_notes: "Primarily QE days from 1 July 2026 to 30 June 2027; saved old quarterly liabilities remain separate"
tier: 2
last_updated: 2026-10-21
version: 0.5
review_status: pending_review
depends_on:
  - workflow-base
  - social-contributions-workflow-base
  - cc-tax-system
verified_by: pending
---

# Cocos (Keeling) Islands: employer super guarantee for 2026-27

Load `workflow-base`, `social-contributions-workflow-base` and
`cc-tax-system`. Preserve profile confirmation, source and period gates,
refusals, the 4 universal outputs, all 5 social-domain outputs and their
checks. This selected employer superannuation guarantee (SG) companion
supports component working papers for a credentialed reviewer. Missing
mandatory sources, country slots, facts or runtime capabilities prevent a
complete financial deliverable. A payroll run also needs its payroll base
and country payroll rules. No comprehensive-country acceptance or
professional sign-off is claimed.

## Territorial application and period

Section 8E of the Cocos (Keeling) Islands Act 1955 extends Commonwealth
Acts of their own force unless an Act expressly provides otherwise. Its
territory framework is compilation 13 of 18 December 2020. [TERRITORY]

The SG Act extends to external territories included in its definition of
Australia. Section 6 adopts the income-tax meaning of geographical
Australia; section 960-505(1)(e) of the 1997 Act expressly includes
Cocos (Keeling) Islands. Work on the island is therefore not work outside
Australia merely because it is offshore from the mainland. Residence,
worker status and the particular payment still require their own tests.
[SG, sections 4, 6 and 8][SG]; [DICT, section 960-505][DICT]

The dictionary capture is compilation 267, effective 27 August to
30 September 2026, rather than a complete current consolidation. Selected
October amendment targets in Acts 71 and 86 of 2026 were checked and do
not replace the geographical definition used here. Reconcile operative
law for the engagement period and other tax regimes separately. An editing
date does not certify a complete current statute. [DICT]; [AMEND71]; [AMEND86]

For QE days from **1 July 2026**, Payday Super uses qualifying earnings
(QE) paid to or for an employee. The payment day controls even if the
work or arrangement predates commencement. Old quarters ending before
1 July 2026 retain their saved rules; see the transition section.
This guide's primary year is **1 July 2026 to 30 June 2027**, in AUD.
Do not roll its annual base into a later financial year. [PAYDAY, section 2
and Schedule 1 item 182][PAYDAY]; [RATES]

## Programmes and selected figures

Keep SG separate from income tax, Medicare, PAYG withholding, workers'
compensation, paid parental leave and any local or employment obligation.
Their coverage is not established by this SG calculation. The island's
GST geography also does not determine its SG geography. Route income-tax
and Medicare questions to `cc-income-tax` and territory boundaries to
`cc-tax-system`; those guides retain their own incomplete slots.

| Programme or parameter | Selected 2026-27 treatment | Primary source |
|---|---|---|
| Ordinary employer SG | 12% of eligible QE after the annual-base rule; employer obligation, without an employee SG matching-share calculation in this guide | SG section 17A; RATES |
| Annual maximum contributions base | AUD 270,830 per employee, per employer, per financial year | SG section 10A(5)-(6); RATES |
| General earnings floor | No minimum earnings amount for an otherwise eligible adult worker; age and other exclusions still apply | ELIGIBILITY; SG; REG |
| Normal contribution period | Each QE day; fund receipt normally by the 7th business day after that day | SG sections 6 and 18C; DEADLINES |
| First eligible contribution extension | Conditional period ending on the 20th business day after the QE day | SG sections 6 and 18C(2) item 1 |
| Basic administrative uplift | 60% of the combined final shortfalls and notional earnings, subject to statutory reductions | SG section 19B; REG regulations 13A-13D |
| Choice loading | 25% of relevant non-compliant contributions, limited under section 20C | SG sections 20A and 20C |

Sources for this table: [SG]; [REG]; [RATES]; [ELIGIBILITY]; [DEADLINES].
The 12% rate is not Norfolk Island's conditional 2026-27 transition.
Item 189 of the Payday Super Act defines a Norfolk earnings subset;
it does not create an 11% concession for Christmas Island or Cocos
employment. If an engagement actually includes Norfolk earnings, resolve
that subset and its interaction with the cap separately. [PAYDAY, item 189][PAYDAY]

## Establish the contributor and earnings

Use a stable contributor reference. Establish the employer, actual
employment relationship, age at the relevant time, weekly hours where
required, residence, work locations, payment dates, earnings components,
annual earnings history and any applicable certificate. Confirm readiness
of reviewer-held registrations and fund details. Do not request TFNs,
bank details or identity documents through this workflow.

### Employee, contractor and self-employed status

Section 12 starts with ordinary employment and extends to specified
directors, labour contracts, performers, related services and office
holders. A contract wholly or principally for a person's labour can make
that person an SG employee. An invoice, ABN, contractor label or PAYG
classification alone does not settle SG status. Preserve the contract,
actual duties and labour/non-labour split for review. [SG, section 12][SG]

An otherwise eligible employee aged **18 or over** is covered regardless
of hours or amount earned. For someone under 18, the part-time exclusion
uses **not more than 30 hours per week**. The ATO requires actual weekly
hours, rather than averaging across a fortnight or month. Exactly 30
hours is not more than 30. Domestic or private work also has a separate
not-more-than-30-hours exclusion, regardless of age. Do not apply the
business-employee rule to a private household without that check.
[SG, sections 6 and 12(11)][SG]; [REG, regulations 11(f) and 12(1)(j)][REG];
[ELIGIBILITY]

A sole trader or partner does not owe employer SG merely on their own
business profit or drawings. That does not exempt employees they engage,
or a worker whose actual relationship meets section 12. A company paying
its working director needs the director/employee test; it is not the
same as sole-trader drawings. Personal or voluntary contribution rules
and their deduction/cap conditions are separate and remain uncomputed.
[SG, section 12][SG]; [ELIGIBILITY]

Temporary residence alone is not an exemption. Regulation 11 contains
narrow visa, appointment, seniority and other conditions for certain
foreign workers. Regulation 12 also addresses covered international
social security agreements and particular work outside Australia. Verify
the exact instrument, certificate, employer/employee residence and work
period before excluding anything. A bilateral agreement's existence or an
island address is insufficient. Where a cross-border decision is needed,
load its domain base and applicable country/agreement sources first.
[SG, sections 8, 12 and 15C][SG]; [REG, regulations 11-12][REG]; [ELIGIBILITY]

### Reconcile qualifying earnings

For each payment, reconcile gross-pay components to the actual section
10A categories and regulation 12 exclusions. Include overlapping categories
once. Ordinary time earnings (OTE) are not a universal synonym for gross
pay, taxable income or QE. [SG, sections 6 and 10A][SG]

| Component | Classification control |
|---|---|
| Ordinary hours, over-award payments, shift loading or commission | Test the section 6 OTE definition and section 10A categories. |
| Commissions, specified director remuneration and qualifying labour-contract payments | Section 10A expressly includes the specified categories; do not omit them solely because an old OTE report did. |
| Salary sacrifice reduction of qualifying earnings | Include the qualifying reduction under section 10A(1)(h), subject to its exclusions; do not count the same earnings twice. |
| Payment reversing a sacrificed contribution | Excluded under section 10A(3)(a). |
| Separately identified genuine overtime | Do not assume every payment is QE; reconcile ordinary hours and every other possible section 10A category before exclusion. |
| Unused sick, annual or long service leave lump sum on termination | Section 6 excludes the listed termination payments from OTE. Check whether another QE category applies before concluding. |
| Parental leave period payment | Regulation 12(1)(a) exclusion; a separate government contribution programme is not computed here. |
| Fringe benefit | Regulation 12(1)(f) exclusion using the FBT Act meaning; do not classify every cash allowance as a fringe benefit. |
| Community service or Australian Defence Force absence payment from the usual employer | Regulations 12(1)(b)-(c), (2)-(3) contain conditions and exceptions; annual, sick or long service leave relating to the period is not automatically excluded. |
| Particular overseas work, reserve remuneration or prescribed grant-funded payment | Verify the specific regulation 12 provision and evidence; do not extend its exclusion to all foreign, public sector or care-sector pay. |

[SG, sections 6 and 10A][SG]; [REG, regulations 11-12][REG]. An exclusion
from QE does not establish income-tax exemption, zero PAYG withholding,
absence of another programme or permission to ignore an employment award.
For an invoice, isolate the proved labour component. Do not apply 12%
mechanically to goods, expenses and labour combined. [ELIGIBILITY]

## Annual base and individual SG amount

Section 10A(5) derives the maximum from the basic concessional contributions
cap and charge percentage, then rounds it down to a multiple of **AUD 10**.
The ATO's applicable **2026-27 annual base is AUD 270,830**. This is an
employer SG base, not a person's combined concessional-contribution cap
across every employer and voluntary contribution. [SG]; [RATES]

Under section 10A(6), use the earnings history for **that employee and
that employer in the same financial year**. For the payment that would
cross the base, only the remaining amount up to the annual maximum counts
for the specified SG purposes. Subsequent payments are treated as nil
for those purposes, not as non-existent for income tax or every payroll
obligation. Keep pre-limit earnings and the applied limit visible.
Do not reuse the old quarterly maximum or invent a monthly cap or
starter/leaver proration. [SG, section 10A(6)][SG]

For an ordinary covered accumulation-fund case with all facts established:

1. Confirm the contributor profile, applicable law and QE payment day.
2. Classify each payment component, exclusions and salary sacrifice.
3. Total QE paid to or for that employee by that employer on the same day,
   without double counting overlapping categories.
4. Apply the annual-base crossing rule using the verified earnings ledger.
5. Multiply the resulting QE by **12%** for the individual SG amount.
6. Apply eligible contributions to the earliest unpaid QE day in receipt
   order under the statutory rules. Do not choose a later payday or reuse
   an amount already applied to an earlier QE day.
7. Reconcile any base shortfall, late allocation and remaining final
   shortfall separately from notional earnings, uplift and choice loading.
8. Verify fund choice, allocation information, actual receipt, calendar
   and any permitted longer period before assessing payment compliance.

[SG, sections 10A and 17A-18D][SG]. Missing year-to-date history means
Needs Input. Neither assume the employee is below the cap nor stop SG
on an unverified claim that the annual base has been reached.

An actual employer shortfall exemption certificate in force for the
employer, employee and QE day can invoke section 17B. A certificate for
another employer does not exempt this employer. High income or multiple
jobs alone does not supply a certificate. This guide does not prepare
an exemption application or infer its approval. [SG, section 17B][SG];
[ELIGIBILITY]

## Fund choice, receipt and allocation

An eligible employer contribution ordinarily needs a complying fund or
RSA and sufficient information to allocate it to the employee. Sacrificed
contributions are excluded from the eligible employer-contribution
definition even though sacrificed earnings can enter QE. A trustee's
compliance statement addresses only its statutory presumption and has
exceptions; it does not prove timely receipt or correct allocation.
Defined-benefit, deceased-employee representative and conversion-notice
branches need their own section 18A-18B conditions. [SG]

For ordinary choice-covered accumulation contributions, establish:

- the employee's valid chosen fund; or
- if there is no chosen fund, the latest relevant Commissioner notification
  identifying a stapled fund; or
- if that notification says there is no stapled fund, the eligible employer
  default-fund route, including the applicable standard-choice-form,
  MySuper and insurance requirements.

Section 32C contains further public sector, successor-fund and instrument
branches. Verify the applicable branch rather than treating the above as
an exhaustive rule for every employee. Failure to provide a required
standard choice form on time can defeat the stapled/default compliance
route until the form is provided. [SG, sections 32C-32D and 32N-32NA][SG];
[REG, regulations 14-17][REG]

Section 32N generally requires a standard choice form within **28 days
of first commencing employment**, and identifies further request, ceased
choice and employer-fund-change events. Section 32NA contains exceptions,
including a valid timely choice and specified temporary-visa or scheme
cases. Do not assume every employee needs a new form every year or that
no form is ever needed because a fund account exists. Record the trigger,
applicable exception if any, form date and evidence. [SG]

A bank debit or clearing-house receipt is not proof that the employee's
fund received an allocatable contribution. Reconcile the remittance,
clearing-house report, fund acceptance, employee allocation and refunds
separately. A rejected, returned or unallocated amount cannot be marked
compliant merely because cash left the employer's account. [SG, sections
18A and 18C][SG]; [DEADLINES]

Section 18C can apply unused eligible contributions received in the
**12-month period ending the day before the QE day**, subject to all its
conditions. Apply contributions in receipt order and prevent double use
across QE days or late-period allocations. A contribution exceeding one
payday's amount is not a refund or automatically available credit for
every later payday. [SG, section 18C(1)][SG]

The ATO confirms that eligible contributions apply automatically to the
earliest QE day whose minimum SG remains unpaid. A payment received in
time for the current payday can therefore discharge an older unpaid
QE day first and leave the current day short. The employer cannot elect
a different allocation merely by labelling the remittance. Preserve
earlier base shortfalls and late-period history after principal is paid.
[SG, sections 18C-18D][SG]; [HOWTO]

Additional super required by an award, enterprise agreement or contract
remains payable under that instrument. Carrying an excess amount forward
for statutory minimum SG does not cancel the separate contractual amount
for a later payday. Verify those obligations before reducing a remittance
because an SG credit or annual-base limit is available. [HOWTO]

### Act on a valid choice without delaying SG

For the ordinary accumulation-fund route, record when the employee or
Commissioner gave the written/approved choice notice to the employer.
The fund becomes a chosen fund **2 months after that notice**, or earlier
if the employer determines an earlier time. It must be an eligible choice
fund able to accept that employee's contributions. An employer may refuse
a direct employee notice lacking the prescribed information and acceptance
evidence, or a further choice where another fund was chosen within the
previous **12 months**. That is permission to refuse, not a prohibition on
accepting another valid choice. Defined-benefit restrictions remain
separate. [SG, sections 32D and 32F-32H][SG]; [REG, regulation 16][REG]

The 2-month implementation period does not postpone a contribution's
receipt deadline. Until the new choice takes effect, establish the fund
that lawfully satisfies the applicable choice branch. For a new employee
who commenced **on or after 1 November 2021**, the ATO directs employers
unable yet to pay to the chosen fund to use the stapled fund, or the
eligible default route if the ATO advises there is no stapled fund. Do not
bypass a still-effective existing choice when an established employee
requests a change. For employees who commenced before that date, the ATO
says a stapled request is not required: use their valid chosen fund or the
lawful default route. [SG, sections 32C and 32F-32H][SG]; [WHERE]; [FORM]

A written request for a choice form normally requires provision within
28 days, but section 32N(3) disregards that request if a form was given in
the previous 12 months. Further 28-day triggers include awareness that a
chosen fund cannot accept contributions or ceases to be eligible, a
covered employer default-fund change and discovery that the specified
default cannot accept contributions. Apply the section 32NA exceptions
before treating a form as overdue. [SG, sections 32N-32NA][SG]; [CHOICE]

### Employer and fund readiness

Keep a readiness register using stable employer, contributor and fund
references. The employer or authorised practitioner retains actual
identifiers and supporting documents in their controlled system. This
workflow does not request, receive or submit TFNs, bank details or identity
documents. Record evidence availability, its date and the reviewer-held
location instead. [REG, regulation 16][REG]; [NEWFUND]; [STREAM]

| Readiness item | Evidence to establish before the relevant action |
|---|---|
| Employer and reporting channel | Correct legal employer and ABN where eligible; an ineligible employer may use its WPN for SuperStream. The WPN comes from PAYG withholding registration advice or the activity statement. Verify that registration and channel with the ATO; an island address or payroll installation does not establish readiness. |
| Ordinary fund and member | Fund identity, ABN/USI, member account readiness, compliance and ability to accept this employer's contribution. Check Super Fund Lookup and the applicable statutory trustee evidence. |
| SMSF | Reviewer-held ABN, electronic service address, payment-detail readiness and ATO-regulated/compliance evidence. An SMSF label alone supplies neither allocatability nor a SuperStream exemption. |
| Employer default | Eligible complying/default fund, authorised MySuper product, applicable insurance conditions, current registration and required form particulars. A default selection alone cannot override a chosen or notified stapled fund. |
| Quoted TFN hand-off | Reviewer-held quotation basis/date, applicable statutory deadline and confirmation/evidence that the relevant trustee was informed. Keep the actual TFN outside this workflow; see the conditional test below. |
| Software/service | SuperStream-compliant data and payment path, expected processing time, MVR support, STP/QE capability and authorised access. A data-only product also needs a compliant electronic payment arrangement. |

[SG, sections 18A-18B and 32C-32D][SG]; [REG, regulations 14 and 16][REG];
[DEFAULT]; [NEWFUND]; [STREAM]; [WPN]; [UPGRADE]; [STP].
These are selected readiness checks, not a complete employer, PAYG, payroll
or special-scheme registration manual. Do not invent a separate SG
registration requirement from this table.

### Quoted TFN hand-off

The SIS Act extends to all external territories. For an employee within
its section 15A meaning and a contribution to an eligible superannuation
entity, confirm whether a TFN was quoted in the manner or circumstances
covered by sections 299A, 299C and 299P, including a PAYG quotation on
or after 1 July 2007 and a deemed section 202CG disclosure. An eligible
entity here is a regulated superannuation fund or approved deposit fund.
Do not assume every informal identifier reference is an approved quotation.
[SIS1, sections 8, 10 and 15A][SIS1]; [SIS2, sections 299A, 299C and 299P][SIS2]

Where the employer then contributes for the employee and has not already
informed that entity's trustee, section 299C requires the employer to
inform the trustee of the quoted TFN before the required time:

- Quotation **more than 14 days before** the contribution: by the end of
  the contribution day.
- Otherwise: by the end of the **14th day after** the quotation day.

These are calendar-day conditions, distinct from SG's business-day receipt
rule. Establish the contribution date for this provision; a payroll entry
or attempted bank debit alone does not establish it. Section 299C(3) makes
contravention a strict liability offence with a stated penalty of **10 penalty units**; no AUD penalty assessment is
computed here. If **this employer** previously informed a trustee of the
**same eligible entity** of **this employee’s TFN**, section 299C(1)(c)
does not require that employer to notify again. The trustee merely knowing
the TFN from another employer or the member does not satisfy that test.
If no TFN was quoted, do not fabricate one or treat section 299C as proof
that a fund can accept every contribution. Check the actual fund/channel conditions.
[SIS2, section 299C][SIS2]; [NEWFUND]

The employer or authorised practitioner records the quotation basis/date,
contribution date, applicable deadline, trustee-notification status and
secure evidence reference identifying the notifying employer, entity and
employee reference. They transmit through their authorised channel,
confirm any service-provider authority to share the TFN and keep the
actual number outside this workflow. An unresolved notification check
prevents certifying that hand-off as complete; it does **not** authorise
delaying an otherwise due SG contribution. For an RSA or special scheme,
verify its separate TFN provisions before certifying compliance. [NEWFUND];
[SIS2, section 299C][SIS2]

The current ATO page describes TFN notification using both a general
14-day instruction and a new-employee instruction to provide it more than
14 days before the first contribution. Those statements do not reproduce
section 299C's conditional test above. Escalate an apparent conflict to
the authorised practitioner with the exact dates and source versions; do
not invent a 14-day lead time or postpone a statutory SG deadline.
[NEWFUND]; [SIS2, section 299C][SIS2]

The current ATO form channel identifies **Superannuation standard choice
form, NAT 13080**. Complete the employer/default section before providing
it. The employee may use the downloadable form, a pre-filled ATO online
services/myGov summary returned to the employer, or enabled payroll
software capturing the required information. An alternative must contain
the required equivalent information. Keep the completed form/summary;
**do not send it to the ATO or the fund**. This guide checked the current
HTML instructions, not every field of the downloadable PDF. [FORM]; [CHOICE]

For stapled requests, establish authorised ATO online-services access and
the employment-relationship link described by the ATO, ordinarily through
a processed TFN declaration or STP pay event. The current guidance allows
a new-employee request after acceptance of the employment offer and until
the employee chooses a fund, subject to the channel's prerequisites.
A request does not remove a required choice-form obligation. Retain the
latest ATO notification; the employer does not select its own stapled
fund from an account list. [SG, sections 32Q-32R][SG]; [REG, regulations
17A-17C][REG]; [STAPLED]; [WHERE]

For a qualifying labour contractor not included in STP, the ATO describes
a separate secure-mail request with the signed contract and **Contractor
stapled super fund request form, NAT 75404**. Have the authorised employer
or practitioner follow the current instructions in their controlled
system. No actual form or contract is requested here. If the employment
link cannot be established before payment is due, use the ATO assistance
route in the cited guidance. Do not manufacture a pay event or defer SG
merely to create a link. [STAPLED]

If the notified stapled account cannot accept the contribution, obtain
a valid alternative choice or request an alternative stapled fund through
the ATO. The ATO directs an employer receiving the same account again, or
no alternative result, to contact it for assistance. A rejection is not
an automatic instruction to use the default fund. Preserve each response
and resolve the applicable choice branch before payment. [WHERE]; [STAPLED]

### SuperStream, verification and errors

SuperStream requires electronic payment and related contribution data in
the standard format. Send the payment and data on the **same day**, linked
by the service's payment reference number (PRN). EFT/BPAY alone or an
emailed spreadsheet does not establish compliant electronic data. Check
the fund's direct-payment agreement where using that route. Personal
contributions and contributions to a related SMSF have specific excepted
contribution treatment; do not extend that exception to every SMSF or
unrelated employee. [STREAM]

The ATO's new-employee/fund guidance requires an MVR before a first SG
contribution to a fund where the software supports it. Its upgrade guide
states that funds must respond within **24 hours**, allowing confirmation
that the member matches an active account and contributions can be
accepted. Check with the provider how to use MVR, including changed
employee details or a prior rejection. Do not send it before every
unchanged regular contribution. If the feature is unavailable or a
response cannot be resolved, record the operational gap and obtain
provider/fund assistance; this does not create a payment extension.
[NEWFUND]; [UPGRADE]

An MVR success is not payment or proof of fund receipt. Reconcile the
payment and data, PRN, fund acceptance, employee allocation, rejected or
returned amounts and actual receipt date. Resolve errors and resubmit
promptly: the deadline does **not reset or extend because of an error**.
Apply only an independently established statutory extension. [SG,
sections 18A and 18C][SG]; [DEADLINES]; [UPGRADE]

The ATO Small Business Superannuation Clearing House **closed from
1 July 2026**. It is not a payment channel for this guide's QE days.
Do not reuse its historical receipt concession or a quarterly deadline
from older text. A commercial clearing-house receipt still requires
proof of timely, allocatable receipt by the employee's fund. [STREAM];
[SG, sections 18A and 18C][SG]

## Deadline calendar and longer periods

The usual period ends on the **7th business day after the QE day**.
The statutory business-day definition excludes Saturday, Sunday and a
public holiday for the whole of **any State, the ACT or the Northern
Territory**. A holiday elsewhere can therefore affect this employer's
calendar. Do not use only the island calendar or treat every local holiday
as a statutory excluded day. Establish authoritative holiday dates before
publishing an actual deadline. [SG, section 6][SG]; [DEADLINES]

| Longer-period branch | Conditions and endpoint |
|---|---|
| First eligible contribution | First to the particular complying fund/RSA after employment commenced/recommenced, or after ceasing eligible contributions to another fund/RSA: extended usual period, ending on business day 20 after the QE day. |
| Determined out-of-cycle QE | Section 18C(2) item 2 plus the determination conditions below: end of the usual period for the first subsequent standard QE day. |
| Exceptional circumstances | Employer and QE day must be covered by a Commissioner determination. Endpoint is the later of the extended usual period and the period of 20 business days starting on the day after the determination. |
| Overlapping due dates | Item 4 requires the relevant earlier contribution to have been applied for an earlier QE day. If the current usual period ends before that contribution's latest permitted receipt day, use that latest day under the statutory conditions. |

[SG, section 18C(2)][SG]; [REG, regulation 13][REG]; [DEADLINES]. These
are receipt periods, not permission to leave fund information unresolved.
Use the latest applicable endpoint where multiple items apply. Keep a
reason and evidence for each extension; do not grant all subsequent
paydays the first contribution's 20-business-day period automatically.

The **2026 out-of-cycle determination** covers specified allowances,
bonuses, commissions, loadings, payments in advance and back payments.
All these conditions must be established:

1. The employer has an established timing, pattern or schedule of QE
   payments for that employee.
2. The specified payment falls outside that established schedule.
3. A subsequent payment that is not out of cycle is actually made on the
   next day consistent with that established schedule.

Several out-of-cycle payments may occur between the first and subsequent
standard payment. An advance must satisfy the determination's definition
and is not a loan. An intermittent invoice, a payment merely labelled
'bonus' or a hoped-for next payday does not establish all conditions.
If the required next standard payment does not occur, do not retain the
extension on the basis of the label alone. [OUTOFCYCLE, sections 4-5][OUTOFCYCLE];
[SG, section 18C(2) item 2][SG]; [DEADLINES]

Natural disasters and widespread contribution-technology outages are
prescribed exceptional circumstances. An employer's individual cash-flow
problem, local delay or disaster label is not itself the required class
and period determination. Verify and retain the actual determination;
this guide does not assert that one covers a particular employer or day.
[REG, regulation 13][REG]; [SG, section 18C(4)][SG]; [DEADLINES]

## Late payments, SGC and disclosures

The individual SG amount, base shortfall, final shortfall and total
superannuation guarantee charge (SGC) are distinct. On-time eligible
allocations reduce the base shortfall. Late eligible allocations within
the statutory late period can reduce the final shortfall, but do not
automatically erase notional earnings, uplift or choice loading. Keep
assessment and receipt dates, historical allocations and changing
shortfall balances. [SG, sections 16B and 18C-19B][SG]; [CHARGE]

The selected SGC structure for a QE day comprises the totals of final
shortfalls, individual notional earnings, administrative uplift and choice
loading. Section 19A uses the GIC rate and its defined notional sum,
including the base shortfall and prior daily amounts. Do not calculate
interest solely on the latest unpaid principal or copy a fixed historical
interest rate. A complete charge needs the actual daily rates and dates,
assessment facts and applicable statutory adjustments. [SG]; [CHARGE]

Section 19B starts the uplift at **60%** of combined final shortfalls and
notional earnings. Regulations 13C-13D permit reductions:

- **20 percentage points** if the regulation's prior-24-month assessment
  and estimate conditions are met, with its transition beginning
  1 July 2026 for QE days through 30 June 2028; and
- **40, 35, 30 or 15 percentage points** for a valid voluntary disclosure
  lodged before assessment, respectively before the end of the 30-day
  period starting on the QE day, in the following period ending on day 60,
  in the following period ending on day 120, or later.

The assessment/estimate exclusions and validity requirements matter. Do
not assume the lowest rate because an employer says this is their first
late payment. Section 33 permits an approved-form voluntary disclosure
before the day of assessment; it is not the old compulsory quarterly SGC
statement. [SG, sections 19B and 33][SG]; [REG, regulations 13B-13D][REG];
[CHARGE]

Choice loading generally uses **25%** of relevant contributions failing
choice requirements, subject to statutory exceptions and the remaining
**AUD 1,200** limit per employer/employee notice period. That period can
cover multiple QE days; it is not a new annual or per-payday allowance.
Section 20D's failed-stapled-fund protection has specific notification,
no-chosen-fund, rejection and replacement-payment conditions. [SG, sections
20-20D][SG]; [CHARGE]

Before assessment, the ATO directs employers to pay missing contributions
to the fund promptly. After assessment, pay the charge to the ATO; section
36(4) makes it payable on the assessment day. Do not send an assessed
charge to the fund and call the ATO debt discharged. Later non-payment
can create further interest, notice and penalty consequences, which need
their own current sources and facts; no complete penalty computation is
supplied here. The first-year compliance approach does not repeal the
underlying SG obligation. [SG, sections 33 and 36][SG]; [CHARGE]

## Changeover and income-tax interaction

Keep pre-July quarters and new QE-day ledgers separate. Schedule 1 item
182 saves old quarterly liabilities and related rules, with the stated
late-payment-offset limitation. Items 185-186 govern eligible unused
pre-commencement amounts and contributions from **1-28 July 2026** where
the employee still has a June-quarter shortfall: apply the latter first
under the saved old rules, then only the unabsorbed remainder under the
new rules. Do not use the same contribution twice. A July payment for
June work is new-period QE without cancelling an old-quarter debt.
[PAYDAY, items 182-186][PAYDAY]

The annual SG base is not a personal deduction or contribution-cap safe
harbour. Employer contribution deductions, personal voluntary contributions,
salary sacrifice, excess contributions and high-income additional tax
need their own income-tax rules and confirmed facts. The Payday Act
repeals former sections 26-95 and 290-95 of the 1997 Act and contains
saved-old-law application provisions. Do not carry the old blanket SGC
non-deductibility rule into every post-July QE-day charge or infer that
every charge, penalty and interest amount is deductible. No deduction is
calculated by this companion. [PAYDAY, items 80, 92 and 183][PAYDAY]

Current ATO guidance identifies deductions for on-time and late eligible
contributions and payment of SGC for QE days from 1 July 2026. It excludes
late-payment penalties, general interest accruing on unpaid SGC and
quarterly-period SGC assessments. Keep those categories separate, and
verify all applicable income-tax deduction conditions before a claim.
This is a classification route, not a computed deduction. [HOWTO]

## STP reporting, transition and correction controls

For an employer/pay event required to use STP, report on or before each
payday through STP-enabled software. Keep any verified exemption or
special reporting arrangement separate; this guide does not establish
all such cases. Ordinary reporting includes salary/wages, PAYG withholding
and super liability. From 1 July 2026 the Payday Super requirements add
QE reporting. An independent contractor who is an SG employee only under
the labour-contract extension is not mandatorily brought into STP merely
by that status. If the employer voluntarily reports those payments, the
reporting requirements apply. [PAYDAY, Schedule 1 item 178][PAYDAY]; [STP]

### Reconcile 2 distinct year-to-date amounts

| Reported amount | Control |
|---|---|
| QE year to date (YTD) | Reconcile actual QE to the earnings ledger and prior YTD. The increase ordinarily identifies that payday's QE. Exclude non-QE reimbursements/fringe benefits; do not use total taxable pay as a substitute. |
| Annual employer base | After the verified 2026-27 base of AUD 270,830 is reached, the ATO permits QE YTD to remain at that amount for the rest of the year. Keep the unmodified earnings ledger and any separate award/contract obligations. |
| Valid opt-out certificate | A full-year covered employer/employee certificate yields QE YTD of zero from the start. If coverage begins part way through the year, hold the reported QE YTD from the start of the covered period. Verify employer, employee and dates; do not keep it frozen after coverage ends without a lawful basis. |
| Super liability YTD | Report the liability, which includes minimum SG and applicable additional award/enterprise-agreement super. It can include super on a payment excluded from QE, such as stipulated award-covered parental leave. It is not the amount received by the fund. |

[SG, sections 10A and 17B][SG]; [RATES]; [STP].
Preserve the distinction between statutory minimum SG, other contractual
super, reported liability and actual fund receipts. A zero SG amount after
the annual base or during certificate coverage does not cancel every
employment obligation.

### 2026-27 software transition

Ask the digital service provider how to configure QE and super liability.
If the product is not yet updated, **still calculate and pay SG using QE**
and keep each payday's records. Start reporting QE as soon as possible,
including YTD amounts when reporting starts. The ATO accepts super
liability with OTE in pay events until **30 June 2027**, but **once QE
reporting starts, OTE reporting is no longer accepted**. This is a
conditional reporting transition, not a contribution-payment deferral
or permission to treat OTE as the new QE base. [STP]

The ATO says no deferral request is needed where QE reporting can start
during 2026-27; failure to report it during that year increases compliance
risk. From **1 July 2027**, reports missing either QE or super liability
will be rejected and penalties may apply. Confirm the applicable period
and the provider's implementation; do not carry the 2026-27 acceptance
into a later year. [STP]

### Correct reporting without inventing a new payment

Use the provider's STP correction process to fix a lodged YTD amount in
the next pay event or an update event. An omitted/late original report
is not a correction merely because a later report is submitted. Keep
the original QE days, corrected amounts, reason, lodged event/response
and affected contribution/shortfall history. Correcting data does not
change the day earnings were actually paid or reset an SG deadline.
[SG, sections 10A and 18C][SG]; [STPFIX]

For ATO data reconciliation, an update event is not ordinarily a pay
event. The ATO identifies a finalisation-indicator exception when QE
corrections supply the final reported amount. With no change in QE YTD,
no new QE/SG amount is inferred from that event; after a reduction, its
guidance calculates no new QE until a later increase. Reconcile these
data effects to actual pay and corrected records. Do not infer a cash
refund, a fresh 20-business-day period or an election to reallocate older
contributions. Recompute affected liability and retain reviewer holds
where historical corrections remain unresolved. [STPFIX]; [SG]; [HOWTO]

## Worked component examples and classification patterns

All examples are fictional AUD for **2026-27**. Worker, earnings and
ordinary accumulation-fund facts are stipulated. There is no Norfolk
subset, defined benefit, cross-border certificate or rounding difference
unless stated. Examples demonstrate selected amounts or classifications,
not completed engagements. Any unresolved required input remains a hold.

| Fictional facts | Recomputed result or classification |
|---|---|
| Adult employee, eligible QE 2,000, prior annual QE 10,000 | Individual SG amount 240. Separate employer funding and receipt still need proof. |
| Eligible adult employee, QE only 100 | Individual SG amount 12; no assumed AUD 450 monthly floor. |
| Under-18 employee, exactly 30 actual hours in a week | Part-time exclusion; no SG on the excluded earnings. Do not average hours with another week. |
| Under-18 employee, 31 actual hours that week, eligible QE 620 | Individual SG amount 74.40, subject to the remaining coverage facts. |
| Private household worker, 30 hours, all work wholly domestic | Section 12(11) exclusion; do not apply the adult business-employee result. |
| Labour contract satisfies section 12(3); eligible labour 600 and separately proved goods 400 | Individual SG amount 72 on labour QE 600; not 120 on the total invoice merely because it is paid together. |
| Cash qualifying pay 1,800 plus qualifying earnings sacrificed 200 | QE 2,000; individual SG amount 240. Sacrificed contribution 200 does not reduce that employer SG amount to 40. |
| Same-day eligible QE payments 1,200 and 800 | QE day total 2,000; individual SG amount 240, without duplicating a commission already included. |
| Prior annual QE 270,000; current otherwise eligible payment 2,000 | Remaining annual base 830; individual SG amount 99.60; keep the payment's unmodified earnings visible. |
| Annual base already reached for that employer; later otherwise eligible QE 1,000 | Nil additional SG amount under the annual-base rule; other obligations remain separate. |
| Fresh annual ledger, eligible QE exactly 270,830 | Individual SG amount 32,499.60; do not round the statutory base up to create SG of 32,500. |
| Employer A has reached its base; employer B pays eligible QE 1,000 with a fresh verified ledger | Employer B's individual SG amount 120, absent its own valid certificate or exclusion. |
| Valid exemption certificate covers only employer A | It does not exempt employer B's payments. Verify each certificate's employer, employee, period and QE day. |
| Sole trader profit 50,000, no employees or qualifying labour/director relationship | No employer SG on the owner's stipulated profit; voluntary contribution and deduction questions remain separate. |
| Individual SG amount 240; on-time eligible contribution 200 | Base shortfall 40. If a later eligible 40 is applied before assessment, final shortfall can become nil; this does not establish nil total SGC. |
| Correct 240 sent to clearing house on the last permitted day; fund receipt unknown | Timing and compliance unresolved; no presumed timely receipt. |
| Unused eligible receipt 300; applied to first QE day's SG amount 240 | Remainder 60 can be considered under the statutory period/allocation conditions; it cannot be reused as 300 for a later day. |
| Earlier QE day has base/final shortfall 120; current day has SG amount 120; eligible receipt 120 is late for the earlier day but timely for the current day | Apply to the earlier unpaid day first: its final shortfall becomes nil, its base/history remain 120 and the current base shortfall is 120. Do not elect the current day or infer nil total SGC. |
| Off-cycle bonus 500 between established scheduled paydays; all determination conditions met | Individual SG amount 60; receipt deadline follows the first subsequent standard QE day's usual period. |
| Same bonus label, but next scheduled standard payment not made | The determination condition fails; do not assume the out-of-cycle extension. |
| New employee's first eligible contribution qualifies for item 1 | Use the 20-business-day endpoint; later paydays require their own item 4 or other extension evidence. |
| Mere irregular contractor invoice, no established pay schedule | Do not classify automatically as determined out-of-cycle QE. |
| Natural disaster affects employer, but no covering determination established | Hold the extension; the disaster label alone is insufficient. |
| Same-day no-interest/other-uplift example: relevant choice-failing contribution 240, full notice-period limit available | Choice loading 60 before any applicable statutory exception; no claim that this is total SGC. |
| Combined final shortfalls and notional earnings 100; no regulation 13 reductions | Basic uplift 60. With proved 20-point history reduction and 40-point valid timely disclosure reduction, uplift becomes nil. |
| Annual earnings history, fund-choice facts or holiday calendar missing | Needs Input for the affected amount or deadline; no default resolves it. |

[SG]; [REG]; [OUTOFCYCLE]; [RATES]; [ELIGIBILITY]; [DEADLINES]; [CHARGE].
For remittance matching, distinguish an allocatable fund receipt, clearing
house settlement, refund, employee salary sacrifice, ATO assessed charge
and unrelated PAYG/Medicare or insurance payment. Match using stable
references, amount, date, fund and contributor evidence. An amount or bank
narrative alone does not establish programme, employee or QE-day allocation.

### Additional employer-operation cases

The following fictional cases test the operational branches above. Receipt
and choice facts are stipulated only where stated; none is an actual
portal submission, bank transfer or completed payroll engagement.

| Fictional facts | Recomputed result or required disposition |
|---|---|
| Valid direct choice notice received 15 October 2026; employer determines no earlier effective date | Chosen-fund effective date 15 December 2026. Earlier SG receipt deadlines still apply through the then-lawful fund route. |
| Another fund was chosen 6 months earlier; otherwise valid new notice | Employer may refuse under section 32FA(2), or accept. Record the decision; do not declare a universal ban on a second choice. |
| Written request for another standard form; form already supplied 6 months earlier | Section 32N(3) disregards this request. Test other triggers and exceptions separately. |
| New employee commenced in 2026; no choice; no ATO stapled response yet | Default-fund authority not established. Resolve the request and payment deadline; no invented default or extension. |
| New employee has no choice; latest ATO response says no stapled fund; default/form/MySuper/insurance conditions all proved | The stipulated ordinary default branch is available. Receipt and amount still need separate proof. |
| Stapled account rejects payment; alternate request returns the same account | Obtain ATO assistance or a valid alternative choice; do not automatically pay a different default account. |
| Employee commenced in 2020; no valid chosen fund; lawful default conditions proved | Current ATO guidance does not require a stapled request merely because Payday Super began. |
| MVR confirms active account; employer debit 240; actual fund receipt unknown | Verification is not remittance. Timeliness/allocatability remain unresolved. |
| EFT 240 sent; employee data only emailed to fund | No demonstrated SuperStream-compliant electronic data. Correct the process without resetting the statutory receipt deadline. |
| Employer proposes the ATO Small Business Superannuation Clearing House for an October 2026 payment | Channel closed from 1 July 2026; choose a current compliant route and verify actual fund receipt. |
| Qualifying labour contractor has QE 600; no other STP status; employer does not report voluntarily | SG amount 72 remains due under the stipulated facts; SG status alone does not make this contractor payment mandatory STP. |
| Verified prior QE YTD 270,000; current otherwise qualifying earnings 2,000; cap reporting option used | Current SG base 830 and amount 99.60. QE YTD reported at 270,830; preserve uncapped earnings ledger 272,000. |
| Valid certificate begins midyear at reported QE YTD 20,000 | Hold QE YTD at 20,000 during the covered period for that employer. Recheck when coverage ends; no other employer is exempted. |
| QE 2,000 plus non-QE paid parental leave 1,000; enterprise agreement expressly requires 12% super on that leave | Minimum SG 240, additional agreement super 120 and super liability 360. Increase QE YTD by 2,000; do not add the leave to QE merely because liability includes its super. |
| Product has not yet switched to QE reporting in 2026-27; valid transition otherwise established | OTE plus super liability can still be accepted until 30 June 2027; actual SG is calculated and paid using QE. Keep YTD and each payday's records. |
| Employer has started QE reporting, then sends OTE in another 2026-27 pay event | OTE reporting is no longer accepted under the stated transition. Correct the report and preserve actual QE-day history. |
| Pay event from 1 July 2027 omits QE or super liability | The ATO says it rejects the report; no extension of the 2026-27 reporting acceptance. Recheck the later year's substantive figures separately. |
| Update event with no QE YTD change and no actual new pay | Do not create a new QE day or SG amount from the event alone; retain the event and reconcile to actual pay. |
| Earlier QE was 2,500 but lodged as 2,000; other facts unchanged; no cap or rounding difference | Correct the earlier records/report: SG component rises from 240 to 300, difference 60. The correction does not make the earnings newly paid or reset their receipt deadline. |
| Approved quotation 1 July 2026; contribution 20 July 2026; same eligible entity; this employer has not previously informed a trustee of that entity | Quotation was 19 days earlier, so section 299C's required time is the end of 20 July 2026. Retain secure notification evidence; no actual TFN belongs in this working paper. |
| Approved quotation 10 July 2026; contribution 15 July 2026; same conditions | Quotation was 5 days earlier, so the required time is the end of 24 July 2026, the 14th day after quotation. The SG receipt endpoint remains separately determined. |
| Approved quotation 1 July 2026; contribution 15 July 2026; same conditions | Exactly 14 days is not more than 14. The otherwise branch gives the end of 15 July 2026; do not add another 14 days from contribution. |
| No TFN quoted; otherwise due SG contribution | Section 299C's quotation condition is not established. Resolve lawful fund/channel acceptance without inventing a TFN or an SG extension; no complete notification certification. |
| Approved quotation and contribution; evidence proves this employer previously informed a trustee of the same eligible entity of this employee’s TFN | Section 299C(1)(c) is false; no repeated notification by this employer under this provision. Retain evidence of the notifying employer, entity and employee reference; test a different employer or entity separately. |
| Approved quotation to the current employer and subsequent eligible contribution; the trustee knows the TFN from another employer or the member, but this employer has never informed a trustee of that entity | Mere trustee knowledge does not satisfy the current employer’s prior-notification condition. Its section 299C hand-off obligation remains, subject to the other statutory conditions and deadline. |

[SG]; [REG]; [WHERE]; [CHOICE]; [FORM]; [STAPLED]; [NEWFUND]; [STREAM];
[UPGRADE]; [STP]; [STPFIX]; [SIS1]; [SIS2]; [SISJULY].

## Reviewer outputs, checks and remaining slots

Preserve all universal and social-domain outputs. For a supported component
working paper, identify the following rather than implying that a correct
percentage supplies the whole engagement:

| Required output | Minimum SG-specific evidence |
|---|---|
| Contribution computation schedule | Stable contributor/employer reference, classification, period, QE components/exclusions, unmodified annual ledger, capped QE and individual SG amount. |
| Remittance reconciliation | Expected amount, actual eligible receipt, allocation order, clearing-house status, refunds, unused credits, base/final shortfalls and unmatched items. |
| Filing and payment calendar | Actual QE day, normal endpoint, each evidenced extension, holiday sources, receipt status and any assessment/disclosure event. |
| Reviewer brief | Source versions, unresolved eligibility, other programmes, missing facts, assumptions, charge/choice/deduction holds and decisions required. |
| Contribution register | Contributor status, employer, programme, confirmed periods, certificate, choice/form dates, effective fund, latest stapled notification and reviewer-held registration/identifier readiness, TFN quotation/deadline and notification-evidence status; no sensitive identifiers. |

Check every amount against source and year; age/hours; employee/contractor
status; geography/residence; QE and exclusions; annual limit per employer;
same-day totals; sacrifice included once but excluded as eligible employer
funding; certificates; fund choice; receipt/allocatability; contribution
order and no double use; deadlines/extensions; separate shortfall/charge;
changeover; currency/rounding; all outputs and outstanding slots.

Keep the earnings and contribution ledgers, choice notices/forms and
exceptions, secure TFN-notification evidence references, stapled outcomes,
MVR and error responses, payment/data PRNs,
fund receipts/returns and each STP lodged event, correction and response.
The ATO specifically calls for evidence of first contributions, changed
funds, out-of-cycle payments, exceptional determinations, overpayments,
corrections and failed/incomplete reporting. A clearing house does not
replace the employer's own records. Keep electronic records accessible.
[RECORDS]; [CHOICE]; [STPFIX]

Section 79 requires records explaining transactions and acts, including
shortfall documents. Keep them in English or readily convertible into
English so liability can be readily ascertained. Retain them for **5 years after
preparation/obtaining or completion of the related transactions/acts,
whichever is later**, subject to its statutory exceptions. This is not
permission to collect sensitive identifiers in the working conversation
or to delete records automatically at that point. [SG, section 79][SG]

| Mandatory social-country slot | Verified scope and outstanding work |
|---|---|
| 1. Programmes and shares | Employer SG rate and selected charge components supplied. Complete inventory and treatment of health, unemployment, accident and other programmes remains open. |
| 2. Bases | Selected QE/OTE, employee and exclusion rules supplied. Personal/voluntary and other programme bases remain open. |
| 3. Floors and ceilings | Selected earnings-floor, annual SG base and employer separation supplied. Cross-border, certificate application and special-scheme interactions need case-specific sources. |
| 4. Contributor categories | Ordinary employees, selected contractors/directors, age/domestic exclusions and self-employed distinction supplied. Full foreign-worker and special-scheme determinations remain conditional. |
| 5. Registration | Selected ABN/WPN, fund/member, SMSF, default, quoted-TFN hand-off and authorised-channel readiness supplied. Full employer/PAYG registration and special-scheme procedures remain open; actual identifiers stay reviewer-held. |
| 6. Declarations and payment | Selected choice/stapled form channels, SuperStream, MVR, STP YTD/transition/corrections, receipt deadlines, extensions and disclosure/assessment distinction supplied. Actual holiday mapping, complete filing/exemption/SGC forms and other programmes remain open. |
| 7. Penalties and interest | Selected SGC structure, uplift, choice controls and section 299C TFN-notification offence supplied. Actual daily rates, complete penalty/notice machinery and remedies remain open. |
| 8. Income-tax interaction | Selected ATO deduction categories and exclusions, transition and separate income-tax source gate supplied. Actual deduction/cap calculations remain open. |
| 9. Payment patterns | Selected fund/clearing-house/refund/charge patterns supplied; ambiguous remittances require evidence. |
| 10. Refusals and defaults | Missing law, QE, annual history, certificate, fund, receipt or deadline inputs require Needs Input/hold. No country default is authorised. |
| 11. Currency and rounding | Examples use AUD and exact cents; statutory annual base rounds down to AUD 10. Operational fractional-cent contribution/charge rules and any foreign-currency conversion remain unverified. |
| 12. Worked cases | Employee, low earnings, annual ceiling, self-employed, remittance and employer-operation/STP boundaries supplied. No model-executed full contribution engagement, multi-programme or filing test is claimed. |

The selected rules do not satisfy every mandatory slot. Obtain the missing
primary law, facts, forms and capabilities before a complete financial
result. Preserve exact tool-unavailable refusal messages from the bases
where they apply. Do not fill gaps with a mainland assumption, an invented
island exemption, a zero rate or a claim of comprehensive coverage.

## Sources and verification limits

Checked **21 October 2026**: the live Register identified SG Act compilation
**78**, effective **1 July 2026**, and SG Regulations compilation **8**,
effective **1 July 2026**, as latest. Selected provisions were read for
territory/definitions, employee/QE status, annual base, contributions,
shortfalls, choice, disclosure, assessments and records. The out-of-cycle
determination was read in full. ATO eligibility was updated **15 July
2026**, rate/base guidance **17 April 2026**, deadline guidance **29 September
2026** and current-charge guidance **21 June 2026**. The payment/allocation and deduction guide was updated
**20 October 2026** and read in full. Do not use a mixed-year
ATO illustration to override the Act's payment-day commencement.

Current ATO operational pages were checked on the same date. Choice was
updated **17 September 2026**, stapled requests **2 September 2026**,
SuperStream **16 July 2026** and its upgrade guide **21 June 2026**. The
new-employee/fund, STP, correction, record and form instructions are dated
**27 June 2026**. Default-fund guidance is dated **2 December 2024** and
WPN guidance **26 May 2021**; their selected readiness points were checked
against current payment guidance and the relevant SG provisions.
[NEWFUND]; [WHERE]; [STREAM]; [STP]; [DEFAULT]; [CHOICE]; [STAPLED];
[RECORDS]; [UPGRADE]; [STPFIX]; [FORM]; [WPN]

Do not use the older quarterly wording or historical clearing-house
concession retained on the SuperStream page for post-commencement QE
days. Its SMSF/default shorthand also does not displace the current
chosen/stapled/default ordering. MVR's software-support condition is
express in the new-employee/fund page; unavailable software is an
operational issue to resolve, not a statutory payment extension. The
form number and channels above use HTML instructions; the PDF itself and
all DSP-specific fields/technical specifications were not audited.

The SIS Act was checked separately: the live Register identified compilation
**131**, effective **10 August 2026**, as latest. Selected volume 1 sections
8, 10 and 15A establish territorial/entity/employee scope; volume 2 sections
299A, 299C, 299P and 299W supply the selected quotation control. The full
SIS Act, RSA regime and complete TFN rules were not audited. Section 299C
in compilation **130**, effective **1 July 2026**, was also checked and is
identical for the fictional July cases. The ATO timing wording difference
is preserved above for practitioner resolution.
[SIS1]; [SIS2]; [SISJULY]; [NEWFUND]

The historical territory Acts and dictionary limits are stated above.
No full delegated-instrument inventory, all-programme survey, actual
employer determination, return, payroll, declaration, bank transaction,
professional sign-off or complete-country financial review is claimed. Recheck
volatile law and operational guidance before engagement use.

[SG]: https://www.legislation.gov.au/C2004A04402/2026-07-01/2026-07-01/text/original/epub/OEBPS/document_1/document_1.html
[REG]: https://www.legislation.gov.au/F2018L01289/2026-07-01/2026-07-01/text/original/epub/OEBPS/document_1/document_1.html
[PAYDAY]: https://www.legislation.gov.au/C2025A00057/asmade/2025-11-06/text/original/epub/OEBPS/document_1/document_1.html
[OUTOFCYCLE]: https://www.legislation.gov.au/F2026L00784/asmade/2026-06-24/text/original/epub/OEBPS/document_1/document_1.html
[RATES]: https://www.ato.gov.au/tax-rates-and-codes/key-superannuation-rates-and-thresholds/super-guarantee
[DEADLINES]: https://www.ato.gov.au/businesses-and-organisations/super-for-employers/paying-super-on-payday/payment-deadlines-for-payday-super
[ELIGIBILITY]: https://www.ato.gov.au/businesses-and-organisations/super-for-employers/work-out-if-you-have-to-pay-super
[HOWTO]: https://www.ato.gov.au/businesses-and-organisations/super-for-employers/paying-super-on-payday/how-to-work-out-and-pay-super
[CHARGE]: https://www.ato.gov.au/businesses-and-organisations/super-for-employers/missed-or-late-payday-super-payments/what-happens-if-you-dont-pay-super-correctly
[TERRITORY]: https://www.legislation.gov.au/C1955A00034/2020-12-18/2020-12-18/text/original/epub/OEBPS/document_1/document_1.html
[DICT]: https://www.legislation.gov.au/C2004A05138/2026-08-27/2026-08-27/text/original/epub/OEBPS/document_10/document_10.html
[AMEND71]: https://www.legislation.gov.au/C2026A00071/asmade/2026-08-26/text/original/epub/OEBPS/document_1/document_1.html
[AMEND86]: https://www.legislation.gov.au/C2026A00086/asmade/2026-09-15/text/original/epub/OEBPS/document_1/document_1.html
[NEWFUND]: https://www.ato.gov.au/businesses-and-organisations/super-for-employers/paying-super-on-payday/paying-super-for-a-new-employee-or-fund
[WHERE]: https://www.ato.gov.au/businesses-and-organisations/super-for-employers/paying-super-on-payday/where-to-pay-super
[STREAM]: https://www.ato.gov.au/businesses-and-organisations/super-for-employers/paying-super-on-payday/superstream-for-employers
[STP]: https://www.ato.gov.au/businesses-and-organisations/super-for-employers/paying-super-on-payday/single-touch-payroll-reporting-under-payday-super
[DEFAULT]: https://www.ato.gov.au/businesses-and-organisations/super-for-employers/setting-up-super-for-your-business/select-your-default-super-fund
[CHOICE]: https://www.ato.gov.au/businesses-and-organisations/super-for-employers/setting-up-super-for-your-business/offer-employees-a-choice-of-super-fund
[STAPLED]: https://www.ato.gov.au/businesses-and-organisations/super-for-employers/setting-up-super-for-your-business/offer-employees-a-choice-of-super-fund/stapled-super-funds-for-employers
[RECORDS]: https://www.ato.gov.au/businesses-and-organisations/super-for-employers/setting-up-super-for-your-business/record-keeping-for-payday-super
[UPGRADE]: https://www.ato.gov.au/businesses-and-organisations/super-for-employers/paying-super-on-payday/superstream-for-employers/superstream-changes-for-employers
[STPFIX]: https://www.ato.gov.au/businesses-and-organisations/super-for-employers/paying-super-on-payday/single-touch-payroll-reporting-under-payday-super/fixing-single-touch-payroll-errors-in-payday-super
[FORM]: https://www.ato.gov.au/forms-and-instructions/superannuation-standard-choice-form
[SIS1]: https://www.legislation.gov.au/C2004A04633/2026-08-10/2026-08-10/text/original/epub/OEBPS/document_1/document_1.html
[SISJULY]: https://www.legislation.gov.au/C2004A04633/2026-07-01/2026-07-01/text/original/epub/OEBPS/document_2/document_2.html
[SIS2]: https://www.legislation.gov.au/C2004A04633/2026-08-10/2026-08-10/text/original/epub/OEBPS/document_2/document_2.html
[WPN]: https://www.ato.gov.au/businesses-and-organisations/super-for-employers/setting-up-super-for-your-business/withholding-payer-number-super-obligations

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained in the
[ryanduguid/openaccountants fork](https://github.com/ryanduguid/openaccountants).
Check its quality tier, recorded review status and cited sources before use.
Choose a practitioner whose credentials and engagement scope you have verified.
The links below are optional upstream services; they do not publish or verify
this fork's changes.

- Upstream connection service: https://www.openaccountants.com/connect
- Upstream accountant network: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
