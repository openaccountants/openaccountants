---
name: nf-tax-interest
description: >
  Establish selected Australian tax interest and debt treatment for Norfolk
  Island taxpayers in 2026. Use for general interest charge, shortfall
  interest, amended assessments, quarterly rates, payment allocation,
  deduction timing, remission and disputed debt. Covers separate liability,
  accrual and incurred dates, calendar-year divisors, compounding, substituted
  accounting periods, recoupments and review thresholds. Includes primary
  legislation, current authority guidance and fictional boundary components.
  Requires actual assessments, notices, payment receipt and allocation,
  income-year start and verified interest periods. Preserves applicable
  workflow outputs and holds unresolved facts, specialist regimes and actual
  submissions for professional review. This draft does not complete the
  compliance or country pack.
jurisdiction: NF
category: international
tax_year: 2026
tax_year_notes: "Selected rules checked 18 October 2026; published 2026 quarterly rates are calendar-period specific, separately from income-year deduction treatment"
tier: 2
last_updated: 2026-10-18
version: 0.1
review_status: pending_review
depends_on:
  - workflow-base
  - nf-tax-system
  - nf-return-filing
  - nf-tax-amendments-objections
  - nf-tax-penalties-remission
---

# Norfolk Island: tax interest, payments and remission

Establish the person/entity and capacity, tax and territorial application,
income-year start and balance date, original and amended assessments,
notice giving/service, payment due dates, actual payment receipt and
allocation, account history, interest charge periods and prior remission.
Keep private identifiers, bank details, signing credentials and unredacted
client records with the reviewer.

Load workflow-base, nf-tax-system and the applicable domain bases and
substantive references. Preserve their source/period gates, confirmed
profile, refusals, four universal outputs and every applicable domain
output and check. An interest schedule is supporting work, not a completed
return or remission application. Mandatory unknown facts remain Needs
Input; unresolved law remains held. The reviewer personally handles
representations, declarations, submissions and payment.

## Sources and liability gates

The latest published TAA source is **C226** and the 1997 Assessment Act
source is **C267**, both for **27 August-30 September 2026**. Their version
pages identify unincorporated October Acts **71 and 86**. Their amendment
targets do not replace the selected ordinary interest, payment and
recoupment provisions. Read those checks with the compilations, rather
than treating an ended compilation interval as all-law current.
[ADMIN-RECORD]; [ADMIN-VERSIONS]; [ASSESS-RECORD]; [ASSESS-VERSIONS];
[REFORM2]; [OCTOBER]

Under TAA **8AAA-8AAB**, GIC requires an actual statutory provision making
the person liable. A debt label, Norfolk address or late document alone
does not select every interest charge. Income-tax late payment uses
**5-15** of the 1997 Act; an RBA deficit has **8AAZF**; other taxes have
other enabling provisions. Local Norfolk rates, court interest, historical
regimes and specialist superannuation/minimum-tax cases require their
own rules. Do not apply this reference to all local charges. [ADMIN1];
[ASSESS]

Interest and administrative penalties are separate. TAA **280-103** makes
SIC independent of penalty liability. Reasonable care, agent safe harbour,
voluntary disclosure or penalty remission does not itself cancel interest.
Use nf-tax-penalties-remission for the selected penalty rules. [ADMIN2];
[PS-SHORTFALL, paragraphs 7-10][PS-SHORTFALL]

GIC for a day is due at the end of that day under **8AAE**; **8AAF**
permits notification, rather than making a GIC notice a universal condition
of liability. Do not borrow the administrative-penalty notice's payment
period for an interest charge. Assessment prerequisites and the particular
enabling law remain separate. [ADMIN1]; [ASSESS]

## Income-tax payment and interest periods

| Ordinary route | Statutory rule to establish before calculating |
|---|---|
| Original assessment: proved self-assessment entity | Under **5-5(4)**, the first day of the **sixth month after income-year end**; verify the statutory entity classification and applicable deferral/day adjustment. |
| Original assessment: other entity | Under **5-5(5)**, **21 days after the required return day**. Subsection **(6)** instead uses 21 days after notice giving where the return was lodged on/before that return day and the original notice was given after it. |
| Amended assessment: additional income tax | Under **5-5(7)**, **21 days after notice of the amended assessment is given**. |
| SIC itself | Under **5-10**, **21 days after notice of the charge is given**. It is not necessarily the same notice/date as the amended assessment. |

All rows cite the complete relevant **5-5/5-10** branches. Filing and
payment dates are distinct. Sections **5-5(2)-(3)** require an assessment
for income tax to be due/payable but allow it to be taken as due before
assessment. An original late assessment does not always create a fresh
prospective payment period. Actual notices and any deemed giving/service
must be established. [ASSESS]

If income tax or SIC remains unpaid after its due time, **5-15** imposes
GIC for its specified period, starting at the **beginning of the due day**
and ending at the end of the last day when, at day end, relevant tax/SIC
or GIC remains unpaid. This is conditional on nonpayment; paying by the
actual due time does not itself create a late-payment charge. Principal
payment alone may leave interest outstanding. Establish the actual
charge days and closing balance rather than assuming a bank instruction
or principal payment closes every liability. [ASSESS]; [ADMIN1]

Under TAA **8AAZMB**, an applicable tax-debt payment day that is not a
business day moves to the first business day after it. Its definition
excludes weekends and a public holiday for the **whole of any State, ACT
or NT**; it expressly excludes **GIC itself** from tax debt for this
section. Do not substitute any local holiday, move every daily GIC charge
to a working day or reuse a filing adjustment without checking the payment
rule. Actual calendars and route-specific provisions remain required.
[ADMIN1]

### Ordinary income-tax SIC

Under **280-100(1)-(2)**, an additional income-tax amount from an amended
assessment attracts SIC for each day from the **original assessment's
payment due day**, including a hypothetical due day if the original was
nil, through the **day before notice of the amendment is given**.
Subsection **(3)** has a separate start where an amendment reinstates a
particular liability previously reduced. Subsection **(5)** has a
conditional look-through earnout exception. Do not apply the ordinary
start mechanically to every later assessment. [ADMIN2]

The relevant additional tax is not simply omitted income or the account's
net cash payable. Credits, a penalty shortfall under **284-80**, excessive
offset refunds and other specialist SIC branches can differ. Actual
special-tax, credit and amended-history cases need their own provisions.
[ADMIN2]; [PS-SHORTFALL, footnote 1 and paragraphs 86-90][PS-SHORTFALL]

SIC's statutory period does **not automatically stop on advance payment**.
PS LA 2006/8 paragraphs **72-78** distinguish the calculated SIC from
remission for early full/part payment and any interest-on-early-payment
entitlement. Keep those separate; do not reduce the SIC principal or net
an unverified credit merely because money was sent before the amendment.
Actual remission and credit-interest amounts require their own authority
and account evidence. [ADMIN2]; [PS-SHORTFALL]

## Rates, compounding and calculation sequence

TAA **8AAD(1)** gives ordinary GIC's daily rate as the statutory base rate
plus **7 percentage points**, divided by the number of days in the
**calendar year**. Section **280-105(2)** uses base plus **3 percentage
points** for SIC. Its official author-provided accessible formula text
was checked. Calendar-year division means **365 or 366**, not the length
of an income year. The special Division 296 GIC rule in **8AAD(1A)** also
uses a different uplift; do not universalise the ordinary 7-point rule.
[ADMIN1]; [ADMIN2]

Under **8AAD(2)-(4)**, the base comes from the Reserve Bank of Australia's monthly average
90-day Bank Accepted Bill yield for the specified earlier month:
**November, February, May and August** for the following January, April,
July and October quarters respectively. There is a fallback if not
published before the quarter and base-rate rounding to **two decimal
places, .005 upwards**. This is not permission to forecast an unpublished
quarter or use a current bank lending rate. [ADMIN1]

The ATO pages, updated **4 September 2026**, publish these ordinary rates:

| Calendar quarter | GIC annual | SIC annual |
|---|---|---|
| January-March 2026 | **10.65%** | **6.65%** |
| April-June 2026 | **10.96%** | **6.96%** |
| July-September 2026 | **11.43%** | **7.43%** |
| October-December 2026 | **11.51%** | **7.51%** |

Every row cites [GIC-RATES] and [SIC-RATES]. These calendar quarters span
different income years; the 2026-27 year also contains future quarters
not supplied here. Recheck later publications for the actual charge days.
Published daily percentages are displays; the calculations below use
annual percentage divided by 100 and actual calendar-year days, retaining
intermediate precision. [ADMIN1]; [ADMIN2]

1. Establish the enabling law, actual debt/assessment, charge start/end,
   notice dates and account type. Hold an unproved date or liability.
2. Split at every rate-quarter or calendar-year boundary and every relevant
   payment, credit, amendment or remission event.
3. For ordinary non-RBA GIC, **8AAC(3)** applies the day's rate to unpaid
   original principal plus unpaid prior GIC. For RBA GIC, **8AAC(2)** uses
   the end-of-day RBA deficit; do not add the same interest twice.
4. Under **280-105(1)**, SIC compounds on the specified additional tax plus
   prior SIC. Distinguish statutory accrual from a later remission credit.
5. For one constant-rate, unchanged-principal component, the unrounded
   mathematical interest is **P × ((1 + r)^n − 1)**. For consecutive
   segments without intervening balance changes, multiply their growth
   factors. Otherwise reconcile each day/event to the actual ledger.
6. Keep precision and rounding explicit. **8AAGA** permits the Commissioner
   to round GIC for a period **down to a multiple of 5 cents**; it is not
   an automatic instruction to round every daily charge to cents and is
   not a verified SIC rounding rule. Reconcile the actual posting policy
   and notice before settling an account amount. [ADMIN1]; [ADMIN2]

## Payment receipt, allocation and debt management

TAA **8AAZM** treats payment as made when received by the Commissioner or
a person acting on the Commissioner's behalf. An instruction to a bank
alone is not that receipt evidence. Obtain reviewer-held confirmation of
receipt, effective allocation and account balance. [ADMIN1]

Sections **8AAZA-8AAZH** distinguish RBA debts, credits, surpluses, currently
payable debts, different entities and trustee capacities. Under **8AAZF**,
a deficit at day end attracts GIC and the account is altered by that GIC.
Under **8AAZL-8AAZLE**, there are alternative allocation/application
methods, priority-credit rules and specified discretion for debts under
arrangements or deferred recovery. A taxpayer's allocation instructions
are not binding. Do not assume money reduces the selected principal,
count the RBA credit and non-RBA application twice, or net debts of
separate capacities without authority. Actual allocation/refund disputes
remain subject to their full rules. [ADMIN1]

Payment deferral under **255-10**, an instalment arrangement under
**255-15**, recovery deferral and filing deferral have different effects.
Section 255-15 does not itself change the due-and-payable time. Record the
actual written/class authority, terms, effective dates, allocations and
interest position. A payment plan, remission request or dispute is not an
automatic waiver, changed filing date or recovery stay. Use
nf-tax-amendments-objections for selected dispute/payment distinctions;
actual recovery and relief still need their own rules and orders.
[ADMIN2]

## Deduction and recoupment: use the incurred income year

Act **29 of 2025**, Schedule 2, commenced **1 April 2025** but applies to
assessments for **income years starting on or after 1 July 2025**. It
repealed former **25-5(1)(c) and (7)** and inserted **26-5(1A)**, expressly
denying GIC/SIC deductions under the Act. The statutory application period
is distinct from commencement, charge calculation days, payment date and
the income year of the underlying tax debt. [DEDUCT-ACT]; [ASSESS]

PS LA 2011/12, revised **25 June 2026**, paragraphs **60-72** distinguishes:

- Ordinary late-payment GIC after assessment is incurred as liability arises
  daily. GIC calculated back to an earlier due date on a late original
  assessment is incurred when the notice is served/deemed served; later
  accrual is incurred daily. Accrued calculation periods and incurred
  income years are therefore not always identical.
- SIC is incurred when the amended assessment notice is served, rather than
  allocating its deduction across each historical calculation day.
- A substituted accounting period is itself the income year. Establish its
  actual start before applying Schedule 2; do not replace the statutory
  income-year test with an unqualified calendar-date cutoff.

Those are selected authority explanations, not a finding about an actual
notice, deemed service or historical deduction. Verify the period's
applicable law and the liability event. Later payment does not move an
already incurred amount to the payment year. [PS-GIC]; [ATO-DEDUCT]

Under **20-25(2A)**, remitted GIC/SIC is treated as a recoupment. Sections
**20-20(3), 20-30 and 20-35/20-40** test whether a deduction was taken **or
could be taken** and control amount/year and prior assessments. Failure to
claim an allowable deduction does not alone make the remission tax free.
A remission of an amount denied a deduction by the new regime does not
acquire assessable-recoupment treatment merely because it was remitted.
Keep mixed pre/post-change components and any partial deduction separate;
other assessability provisions and specialist facts require their own
checks. [ASSESS]; [PS-GIC, paragraphs 73-76][PS-GIC]

## Remission and review

TAA **8AAG** supplies GIC remission powers and conditions. For unpaid debts,
consider the prescribed external-cause/mitigation, taxpayer-cause/fairness,
special-circumstance or otherwise-appropriate branches. SIC **280-160**
requires fairness/reasonableness with its statutory principles: a benefit
below the charge does not alone justify remission, while circumstances
may justify the Commonwealth bearing delayed-payment costs. They are
powers, not guaranteed waivers. [ADMIN1]; [ADMIN2]

The **2023 remedial determination** modifies selected **8AAG(1)/(5)** and
**280-160(1)** powers to cover an entity or relevant class, including
existing/future liabilities, subject to its serious-adversity, minor-amount
or compliance-history classes. Its separate penalty modification concerns
FTL. Do not generalise the determination to all charges or infer automatic
class membership/remission. [REMEDIAL]

PS LA **2011/12** addresses late-payment GIC; PS LA **2006/8**, revised
**30 July 2026**, addresses shortfall-period interest. Both are current
staff instructions marked as under review. Establish the actual cause and
period, mitigation, audit scope/timetable, information supplied, processing
delay and advance payments. A processing target or list of circumstances
is not a universal statutory grace period. Actual remission, early-payment
interest and any conditions must be recorded and reconciled separately.
[PS-GIC, paragraphs 7-33][PS-GIC]; [PS-SHORTFALL, paragraphs 9-19 and
68-90][PS-SHORTFALL]

Under **280-165**, an approved-form SIC remission request engages the
written-reasons requirement for a refusal. Section **280-170** grants a
Part IVC objection against a decision not to remit where the unremitted
SIC on its specified additional-tax branches is **more than 20% of that
additional amount**. Equality fails the threshold. This is not the
more-than-two-penalty-unit remission threshold, an objection against every
GIC decision or a guarantee of successful review. Actual enabling right,
decision, notice, grounds and deadline require verification. [ADMIN2]

## Fictional components and checks

Stipulate ordinary rates, an established liability and confirmed charge
days, unchanged principal, no intervening payments/credits/remission or
special regime. The following interest figures retain intermediate
precision and are **displayed to cents only**, before any actual account
rounding. They are not notices or settled liabilities.

| Component | Result |
|---|---|
| A$10,000 GIC component, 5 confirmed October-December 2026 charge days | **A$15.78** displayed, using 11.51% / 365. |
| Same principal/days, SIC instead | **A$10.29** displayed, using 7.51% / 365. |
| A$10,000 for 30 such GIC days, then 30 such SIC days | Respectively **A$95.04** and **A$61.91** displayed. |
| A$10,000 GIC, 3 July-September 2026 rate days followed by 3 October-December rate days | **A$18.87** displayed; compound consecutive rate segments. |
| Same segmented SIC component | **A$12.29** displayed; do not reuse the GIC uplift. |
| No day established for a required notice, or payment allocation unknown | Needs Input; a receipt or amount alone does not establish the correct interest period/base. |
| SIC unremitted A$200 on an additional A$1,000 of ordinary income tax | Exactly 20%; section 280-170's threshold is not met. |
| Same tax with A$201 unremitted | More than 20%; the threshold is met, subject to actual decision and process. |
| A qualifying SAP starts 1 January 2025; interest is incurred during it | Test retained earlier law for that income year. Its July-December part does not alone select the new income-year regime. |
| Next SAP starts 1 January 2026 | The new starting-on/after-1-July-2025 application condition is met. |
| Backdated GIC calculated over an earlier period becomes incurred on original notice service in a post-change income year | Do not claim a deduction merely because some calculation days predate the change. |
| SIC on an old income-tax year is incurred on amended-notice service in a post-change income year | The old tax-debt year does not by itself preserve deductibility. |
| A$300 validly deductible prior-regime interest was never claimed, then remitted | Test assessable recoupment: could-deduct can suffice; not claiming is not an exemption. |
| An advance payment is made before an amended assessment | Preserve statutory SIC calculation and separately test remission/credit interest; do not stop SIC automatically. |

Check territorial/enabling law, assessment and actual due day, calendar
versus filing adjustments, giving/service and incurred event, all daily
bases and rate boundaries, 365/366 division, allocation and precision,
optional versus mandatory rounding, prior/partial remission, income-year
start, recoupment eligibility, correct review threshold and the applicable
workflow outputs. Reconcile to reviewer-held notices before action.

## Provenance and remaining work

Checked **18 October 2026**: current records and version grids, October
amendment targets, selected complete GIC/RBA/allocation/receipt/holiday
and SIC provisions, 1997 Act **5-5 to 5-15, 20-20 to 20-40, 25-5 and
26-5**, the full 2025 deduction enactment and remedial determination,
published rate pages and the cited portions of current practice statements.
Large captures were read in selected provisions. The SIC rate formula's
author-provided accessibility alternative was checked; the court-judgment
formula and unrelated specialist calculations were not used.

Actual original/amended notice dates, deemed assessments, account postings,
rounding, historical deductions, partial/mixed recoupments, treaties,
specialist taxes, credit/refund interest, recovery and court procedures
retain their own evidence requirements. No actual taxpayer interest,
filed request, payment, practitioner sign-off or comprehensive-country
acceptance is claimed. This reference remains Tier 2 pending review.

[ADMIN1]: https://www.legislation.gov.au/C1953A00001/2026-08-27/2026-08-27/text/original/epub/OEBPS/document_1/document_1.html
[ADMIN2]: https://www.legislation.gov.au/C1953A00001/2026-08-27/2026-08-27/text/original/epub/OEBPS/document_2/document_2.html
[ADMIN-RECORD]: https://www.legislation.gov.au/C1953A00001/latest/details
[ADMIN-VERSIONS]: https://www.legislation.gov.au/C1953A00001/latest/versions
[ASSESS]: https://www.legislation.gov.au/C2004A05138/2026-08-27/2026-08-27/text/original/epub/OEBPS/document_1/document_1.html
[ASSESS-RECORD]: https://www.legislation.gov.au/C2004A05138/latest/details
[ASSESS-VERSIONS]: https://www.legislation.gov.au/C2004A05138/latest/versions
[REFORM2]: https://www.legislation.gov.au/C2026A00071/asmade/2026-08-26/text/original/epub/OEBPS/document_1/document_1.html
[OCTOBER]: https://www.legislation.gov.au/C2026A00086/asmade/2026-09-15/text/original/epub/OEBPS/document_1/document_1.html
[DEDUCT-ACT]: https://www.legislation.gov.au/C2025A00029/asmade/2025-03-27/text/original/epub/OEBPS/document_1/document_1.html
[REMEDIAL]: https://www.legislation.gov.au/F2023L00956/asmade/2023-07-04/text/original/epub/OEBPS/document_1/document_1.html
[GIC-RATES]: https://www.ato.gov.au/tax-rates-and-codes/general-interest-charge-rates
[SIC-RATES]: https://www.ato.gov.au/tax-rates-and-codes/shortfall-interest-charge-rates
[ATO-DEDUCT]: https://www.ato.gov.au/about-ato/new-legislation/in-detail/businesses/deny-deductions-for-ato-interest-charges
[PS-GIC]: https://www.ato.gov.au/law/view/print?DocID=PSR%2FPS201112%2FNAT%2FATO%2F00001
[PS-SHORTFALL]: https://www.ato.gov.au/law/view/print?DocID=PSR%2FPS20068%2FNAT%2FATO%2F00001

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
