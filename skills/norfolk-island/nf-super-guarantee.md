---
name: nf-super-guarantee
description: >
  Classify Norfolk Island employer super guarantee earnings and the
  2026–27 transition under Payday Super. Use for Norfolk super, mixed
  mainland work, employee residence, labour contractors, salary sacrifice,
  annual base and contribution timing questions. Explains the statutory
  Norfolk earnings subset, one-twelfth adjustment, 11% versus 12% examples,
  payment-day boundary, eligible fund receipt and separate charge analysis.
  Includes primary sources, fictional computations and refusal conditions.
  This source-cited reference covers selected employer SG rules, requires
  the universal and social contributions workflow bases, and holds missing
  eligibility, instruments, other programmes and operational outputs.
jurisdiction: NF
category: international
tax_year: 2026
tax_year_notes: "Primarily QE days from 1 July 2026 to 30 June 2027; old quarterly liabilities and later years are separate"
tier: 2
last_updated: 2026-10-17
version: 0.1
review_status: pending_review
depends_on:
  - workflow-base
  - social-contributions-workflow-base
  - nf-tax-system
---

# Norfolk Island: employer super guarantee in 2026–27

Load `workflow-base`, `social-contributions-workflow-base` and
`nf-tax-system`. Preserve profile confirmation, source/period gates,
refusals, the four universal outputs, all five social-domain outputs and
all applicable checks. A payroll run also needs its payroll base and
country payroll rules. This selected SG reference does not fill every
country slot or establish every contributor's programme coverage. Missing
mandatory source, fact, slot or output prevents a deliverable financial
result even where an illustrative SG calculation is possible.

## Establish coverage and qualifying earnings first

Record a stable contributor reference, employer and employee residence,
work location for each earnings component, actual payment day, worker
classification, qualifying earnings, year-to-date base, any certificate,
fund eligibility/choice and contribution receipt/allocation evidence.
Keep identifiers with the reviewer; do not collect TFNs or bank details.

The SG Act's employee definition extends beyond ordinary employment.
Section 12(3) includes a person working under a contract wholly or
principally for that person's labour. Other subsections cover specified
directors, performers and office holders, and contain exceptions. A
contractor label, invoice or ABN alone does not exclude SG. Establish the
actual relationship and any prescribed exclusions or international
coverage before computing. [SG, sections 8, 10A and 12][SG]

From **1 July 2026**, the statutory base is **qualifying earnings (QE)**.
Section 10A includes ordinary time earnings, commissions, specified
director payments, labour-contract payments and other listed categories.
It also includes the specified reductions in earnings for sacrificed
contributions. Amounts within more than one category count once.
Subsection (3) and the regulations contain exclusions. Do not equate QE
with every gross-pay item or reuse an old ordinary-time-earnings total
without reconciliation. [SG, section 10A][SG]; [PAYDAY, Schedule 1][PAYDAY]

Section 10A(5)–(6) uses a **financial-year, per-employer maximum
contributions base**, calculated from the basic concessional contributions
cap and the charge percentage and rounded down to a multiple of **$10**.
An excess-causing payment is limited to the amount below the annual base;
later payments are treated as nil for the specified purposes. This guide
does not supply the applicable indexed cap or resolve every interaction
between a limited payment and the Norfolk subset. Hold cap-crossing cases
until those rules and the earnings history are established. Do not copy
a pre-July 2026 quarterly maximum into Payday Super. [SG]

## Norfolk subset and the 2026–27 calculation

Schedule 1 item 189 of the Payday Super Act applies when a QE day falls
in the financial year ending **30 June 2027** and some or all of the
payment is **Norfolk Island salary or wages**. The definition covers
qualifying earnings paid to or for the employee:

- while the employee is a Norfolk resident, for work done on Norfolk
  Island **or outside Australia**; or
- while the employer is a Norfolk resident and the employee an Australian
  resident, for work done on Norfolk Island.

These tests apply to qualifying earnings; the outside-Australia limb does
not override exclusions or coverage rules that determine QE in the first
place. Neither incorporation nor a payroll mailing address substitutes for
the required residence facts. [PAYDAY, Schedule 1 item 189(1) and (3)][PAYDAY]

For section 17A(2), item 189 reduces the QE amount by **one twelfth of
the Norfolk subset**. Section 17A specifies a charge percentage of **12**.
For a straightforward payment whose complete eligibility, base and subset
are established, with no cap or certificate adjustment:

1. Total all QE paid to or for the employee by that employer on the QE day.
2. Identify the portion meeting item 189(3), preserving component evidence.
3. Subtract one twelfth of that portion from the QE amount.
4. Apply 12% to that adjusted amount to obtain the individual SG amount.
5. Reconcile separately to eligible contributions and their receipt dates;
   the individual SG amount is not the final SGC assessment.

For wholly qualifying Norfolk earnings this produces an effective **11%**;
unadjusted eligible QE uses **12%**. For mixed earnings, apply the adjustment
only to the Norfolk subset. The ATO Norfolk rate table corroborates 11%
for **2026–27**, 10% for **2025–26** and parity at 12% for **2027–28**.
The earlier year's rate does not carry its old payment rules into 2026–27.
[PAYDAY, item 189][PAYDAY]; [SG, section 17A][SG]; [EMPLOYER]

| Stipulated eligible earnings | Item 189 classification |
|---|---|
| Norfolk employee resident; work on Norfolk; employer on Norfolk or mainland | Norfolk subset, subject to the actual statutory residence and QE tests. |
| Norfolk-resident employer; Australian-resident employee; work on Norfolk | Item 189(3)(b) can apply. The ATO summary table does not list every statutory combination. |
| Mainland employer; Australian-resident employee who is not a Norfolk resident; work on Norfolk | Work location alone does not satisfy either Norfolk residence limb. |
| Work on the Australian mainland | Not Norfolk work or work outside Australia; Norfolk residence alone does not qualify that component. |
| Norfolk-resident employee; work outside Australia | Test ordinary QE/coverage first, then item 189(3)(a); do not assume every overseas payment qualifies. |
| Residence or work location unresolved | Hold the subset and resulting amount. |

The item uses the **QE payment day**, whether the payment relates to work
before, during or after 2026–27. June work paid in July does not select
the prior year's Norfolk rate merely because the work was done in June.
Old quarterly liabilities and contributions applied to them remain
separate under the saving provisions. Item 150 ends the earlier reform
Act's quarterly transition before July 2026; item 189 supplies the new
transition. Do not apply the old and new reductions twice.
[PAYDAY, Schedule 1 items 150, 182–186 and 189][PAYDAY]

## Payment, fund and deadline controls

The ATO's current Norfolk guidance requires contributions for each payday.
Normally they must reach the employee's super fund, with information
allowing allocation, within **7 business days after payday**. Paying a
clearing house on that final day does not prove timely fund receipt.
[EMPLOYER]; [DEADLINES]; [SG, sections 6 and 18A–18C][SG]

For the statutory calendar, a business day excludes weekends and a public
holiday for the whole of **any State, the ACT or the Northern Territory**.
The definition does not simply use Norfolk's local calendar. A mainland
jurisdiction's qualifying holiday can matter even where the employer is
elsewhere. Establish actual dates and the complete relevant holiday
calendar before publishing a due date. [SG, section 6][SG]

Section 18C permits longer periods under specific conditions, including
the first eligible contribution after commencement/recommencement or a
change of complying fund/RSA, certain determined out-of-cycle payments,
covered exceptional circumstances and overlapping due dates. The first
contribution branch uses the extended usual period ending on the **20th
business day after the QE day**. It does not give every later payday a
20-day deadline. [SG, sections 6 and 18C][SG]; [DEADLINES]

The out-of-cycle and exceptional-circumstances branches require their
actual applicable instruments and conditions. An irregular contractor
invoice is not automatically an out-of-cycle payment. This batch has not
verified the complete delegated-instrument set or any actual employer's
determination. Hold those branches, actual holiday/date mapping and
multi-payday allocation where evidence is missing. The ATO deadline page
also describes bunching for overlapping dates; do not ignore that rule
when assigning subsequent deadlines. [DEADLINES]; [SG, section 18C][SG]

An eligible employer contribution has separate conditions, including a
complying fund/RSA and the ability to allocate it to the employee.
**Sacrificed contributions are excluded from the employer eligible
contribution definition**, although sacrificed earnings can form part of
QE. Verify the chosen/stapled/default fund requirements separately.
Defined-benefit and representative-payment branches have their own rules
and are outside the examples here. [SG, sections 10A and 18A–18B][SG];
[EMPLOYER]

Late contributions may reduce a charge but do not automatically remove
interest, administrative components or choice loading. An actual SGC
assessment, late-payment allocation, voluntary disclosure, deduction,
penalty or remedy needs the complete current rules and facts. No late
case is certified compliant by this guide. [DEADLINES]; [SG, Parts 3–4][SG]

## Worked examples and boundary cases

All amounts below are fictional AUD QE payments in 2026–27. Eligibility
and residence/work facts are stipulated; earnings are below the applicable
annual base, with no certificate, sacrificed contribution, defined benefit,
overlapping contribution allocation or rounding issue. They demonstrate
the individual SG amount only, not a complete contribution engagement.

| Stipulated payment | Recomputed individual SG amount |
|---|---|
| QE of 1,200, all meeting the Norfolk subset | Reduction 100; adjusted QE 1,100; 12% produces 132, equivalent to 11% of 1,200. |
| QE of 1,200, none meeting the Norfolk subset | No Norfolk reduction; 12% produces 144. |
| QE of 12,000, with 7,200 Norfolk and 4,800 mainland work | Reduction 600; adjusted QE 11,400; 12% produces 1,368. Cross-check: 792 on the Norfolk part plus 576 on the remainder. |
| QE of 2,400, wholly Norfolk, paid in July 2026 for June work | Reduction 200; adjusted QE 2,200; individual SG amount 264. The June work date does not make this 10% of 2,400. |
| Same earnings/residence but payment after 30 June 2027 | Item 189's time condition fails. Establish the rules for the new period; do not continue its one-twelfth reduction. |
| Employer sends the correct amount to a clearing house but fund receipt is unknown | Amount arithmetic is insufficient; payment compliance remains unresolved. |
| Employee salary sacrifice equals the example's SG amount | Do not treat it as the employer's eligible contribution merely because the amounts match. |
| First eligible contribution has an extended due date overlapping a later payday | Apply the actual section 18C conditions and allocation/bunching rules; do not assume a uniform deadline. |

Before reviewer delivery, verify employee/QE status, residence and work
components, actual QE day, annual base, Norfolk subset, adjustment once,
separate employer contribution, eligible fund, receipt/allocation, calendar,
special periods and reconciliation. Keep unverified required conditions
as Needs Input or a legal hold. Do not turn a correct example into an
actual taxpayer result.

## Sources and verification limits

Checked on 17 October 2026: SG Act compilation **78**, effective **1 July
2026**, registered **8 July 2026**, which the live Register identified as
the latest version; selected definitions in section 6, sections 10A, 12,
17A–17B and 18A–18C; the Payday Act's commencement, item 150 and selected
application/transitional provisions; the full ATO Norfolk employer page
and its current deadline guidance, updated **29 September 2026**.

The complete statutory and delegated rules for all exclusions, annual
cap interactions, special due-date instruments, fund choice, SGC amounts,
self-employed/voluntary contributions, health and other programmes have
not been verified here. This is a selected source-cited draft, not a
complete Norfolk social-contributions companion, professional sign-off
or tested payroll/filing system. All mandatory workflow slots and outputs
remain required before a financial deliverable.

[SG]: https://www.legislation.gov.au/C2004A04402/2026-07-01/text
[PAYDAY]: https://www.legislation.gov.au/C2025A00057/asmade
[EMPLOYER]: https://www.ato.gov.au/norfolk-island/super-for-employers
[DEADLINES]: https://www.ato.gov.au/businesses-and-organisations/super-for-employers/paying-super-on-payday/payment-deadlines-for-payday-super

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
