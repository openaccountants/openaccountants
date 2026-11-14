---
name: nf-fbt
description: >
  Establish selected Norfolk Island employer fringe benefits tax rules for
  the FBT year ending March 2027. Use for employee benefits, private expense
  reimbursements, work items, minor benefits, GST-creditable gross-up,
  reportable benefits, annual returns, instalments and records. Separates
  employer tax from employee reporting and island GST treatment. Includes
  primary sources, fictional computations and strict threshold checks.
  Preserves electric-car application and hybrid savings conditions, the
  April 2027 work-item transition, valuation and evidence gates, universal
  and payroll outputs, and professional review. Actual elections, specialised
  benefits, forms and complete country requirements remain open.
jurisdiction: NF
category: international
tax_year: 2026
tax_year_notes: "FBT year 1 April 2026 to 31 March 2027; sources checked 18 October 2026; separately identified work-item changes apply from the FBT year starting 1 April 2027"
tier: 2
last_updated: 2026-10-18
version: 0.1
review_status: pending_review
depends_on:
  - workflow-base
  - payroll-workflow-base
  - nf-tax-system
  - nf-gst
  - nf-payg-withholding
---

# Norfolk Island: employer fringe benefits tax

Establish the employer, employee or associate, employment connection,
provider and arrangements, benefit type, provision date, FBT year, taxable
value, exemption conditions, GST-credit entitlement and reporting class.
Keep financial-year payroll and FBT-year records distinct. Confirm
reviewer-held evidence readiness; do not obtain private client ledgers,
identifiers, bank details or employee documents through this reference.

Load `workflow-base`, `payroll-workflow-base` and the Norfolk references in
`depends_on`. Preserve the confirmed profile, source and period gates,
refusals, four universal outputs and applicable payroll outputs and checks.
Missing mandatory facts remain Needs Input and unresolved rules remain
held. This reference supplies selected ordinary-employer rules, not an
actual assessment, salary-packaging design or complete payroll/country pack.

## Norfolk application and the correct year

The ATO's Norfolk business guidance expressly identifies FBT registration
when an employer provides fringe benefits, and an ABN requirement for an
employer required to register for FBT. The island's GST exclusion is not
an FBT exclusion. Use `nf-gst` to establish any mainland supply or credit
connection separately. [NI-BUSINESS]

FBT is generally payable by the **employer**, including where another
person provides a benefit under a relevant arrangement. Current, future
and former employees, associates, directors and other statutory categories
need the applicable definitions. A sole trader's or partner's own benefit
is not automatically an employee benefit; the ATO distinguishes these from
employee benefits. Identify the relationship before valuing the item.
[ASSESS, sections 66 and 136][ASSESS]; [OVERVIEW]

The FBT year runs **1 April to 31 March**, separately from the income year.
This guide's primary period is **1 April 2026 to 31 March 2027**. A normal
July–June ledger export does not cover that population. Sections 5B and 5C
separately construct the fringe benefits taxable amount and its components;
do not simply apply a percentage to total staff expenditure. [ASSESS,
sections 5B–5C and 136][ASSESS]; [OVERVIEW]

Salary and wages, qualifying super contributions and specified employee
share, termination and deemed-dividend items have their own statutory
exclusions or regimes. A payment outside FBT can still have income-tax,
PAYG, super, company or reporting consequences. Use `nf-payg-withholding`
and `nf-super-guarantee` where applicable. [ASSESS, section 136][ASSESS]

This ordinary-employer reference does not select the separate Commonwealth
employment legislation, nominated government-body rules, not-for-profit
exemptions/caps/rebates or a trust/owner-benefit classification for an actual
case. Acquire those particular rules rather than assuming an organisation's
name or tax status settles its FBT treatment. [CALCULATING]; [LODGING]

## Taxable value and GST-credit classification

Value each benefit under its own rules before grossing up. Expense payment,
property, residual, car, loan, housing, living-away-from-home and
entertainment benefits do not share one cost or exemption rule. [CALCULATING]

For **external expense payment benefits**, section 20 covers paying a
recipient's third-party obligation and reimbursing expenditure. Subject to
the other applicable rules, section 23 uses the payment or reimbursement
amount, with a recipient-contribution reduction in its **section 20(a)
third-party-payment branch**. Do not subtract an employee's unreimbursed
share a second time from an amount already reimbursed, or assume the
in-house valuation rule is the same. [ASSESS, sections 20 and 23][ASSESS]

Section 24's otherwise-deductible reduction has its own employee-recipient,
hypothetical once-only deduction, documentary evidence, declaration,
travel/car and other conditions. Business purpose alone does not establish
the reduction; associates, depreciation and mixed expenses require their
particular analysis. This reference does not compute a complex section 24
reduction or deem declarations/alternative records satisfied. [ASSESS];
[REFORM-2026, Schedule 4 Part 2][REFORM-2026]

For GST-credit classification, section **149A tests entitlement**, including
specified provider/GST-group and reimbursement branches. A provider's
failure to claim an available credit does not by itself make the benefit
non-creditable. Conversely, a GST registration, an invoice label or Norfolk
address alone does not establish entitlement. Confirm the actual acquisition,
import or reimbursement and applicable GST rules. [ASSESS]; [NI-BUSINESS]

The ATO's ordinary calculation uses these parameters, stated to apply from
the FBT year ending **31 March 2019 onward**. The current imposition Act
sets the tax rate at **47%**; its temporary extra two percentage points
applied only to the FBT years starting in 2015 and 2016. [CALCULATING];
[TAX, sections 5–6A][TAX]

| Ordinary calculation component | Parameter | Condition |
|---|---:|---|
| Type 1 gross-up | 2.0802 | GST-creditable benefit under the applicable entitlement rules |
| Type 2 gross-up | 1.8868 | Benefit outside the Type 1 aggregate |
| Employer FBT rate | 47% | Apply to the combined grossed-up amount, subject to applicable special rules |

For the ordinary selected case:

`FBT = [(Type 1 taxable aggregate × 2.0802) + (Type 2 taxable aggregate × 1.8868)] × 47%`

Include relevant reporting-excluded benefits in the employer's aggregates;
non-reportable does not mean FBT-exempt. GST, if incurred, forms part of the
relevant taxable value under the ATO calculation. Establish concessions,
adjustments and the year's return instructions before choosing rounding or
payable return labels. [ASSESS, sections 5C and 5E][ASSESS]; [CALCULATING]

## Minor benefits and work items: conditions before exemption

Section 58P requires a notional taxable value **less than A$300**, together
with its other conditions and an assessment that treating the benefit as a
fringe benefit would be unreasonable. Assess associated benefits, frequency
and irregularity, total values, valuation difficulty and the circumstances
and purpose of provision. In-house and tax-exempt-body entertainment
branches have additional restrictions. Exactly A$300 fails the numerical
test; a A$299 benefit does not qualify automatically. [ASSESS]

For **2026–27 work items**, read the pre-amendment section 58X with the
2026 amending Act's application clause. Eligible portable electronic devices,
software, protective clothing, briefcases and tools must be primarily for
employment use. The substantially-identical-functions restriction can
apply if an expense payment or property benefit arose for another item
earlier in that FBT year. Replacement items and qualifying portable-device
employers have exceptions; the latter involves the small-business or
modified **A$50 million** test and the specified income-year branches.
Do not reduce that test to raw turnover alone or treat every second device
as automatically exempt. [PREVIOUS, section 58X][PREVIOUS]; [REFORM-2026]

**From the FBT year starting 1 April 2027**, the enacted replacement section
58X removes those subsections and excludes items provided under a salary
packaging arrangement from its eligible work-item definition. New section
24(1A) also restricts the otherwise-deductible rule for specified
salary-packaged standard-deduction expenses. These amendments commenced
in July 2026 but **Schedule 4 item 20 applies them only to FBT years
starting on or after 1 April 2027**. Do not use the latest compilation's
new wording to deny the earlier-year exemption without the application
overlay. Identify the actual year and any later amendments. [REFORM-2026,
section 2 and Schedule 4 items 18–20][REFORM-2026]

## Electric cars and plug-in hybrids

Current section 8A identifies qualifying battery-electric and hydrogen
fuel-cell car benefits for a **current employee**, with the condition that
no luxury car tax has become payable on a supply or importation of the car
before provision. The amending Act separately requires the earliest time
any person both held and used the car to be **on or after 1 July 2022**,
and applies the amendments to benefits provided from that date. A new
lease or second-hand purchase does not restart that first-use test.
Confirm the statutory car and vehicle definitions and actual history.
[ASSESS]; [EV, Schedule 1 item 7][EV]

The general plug-in hybrid inclusion ended for benefits from **1 April
2025**. Schedule 2 item 5(2) preserves a particular application/availability
only if all its conditions are met: the relevant car-benefit branch,
pre-April commitment covering the relevant period, absence of a disqualifying
later commitment, and a pre-April car benefit that was exempt under section
8A. Do not infer grandfathering from the car's purchase date or a lease
label. This reference holds an actual lease/recommitment determination,
associated-cost exemptions and benefit valuation. [EV]

Exemption under section 8A does **not** remove the notional car value from
the section 135P reporting analysis. An employer's nil FBT and an employee's
reportable amount can coexist. Future purchases, proposed concessions and
changes outside the selected period require a new source check; no future
vehicle price threshold is selected here. [ASSESS, section 135P(3)][ASSESS];
[REPORTING]

## Employee reporting is a separate calculation

For an ordinary employee, section 135P tests whether the individual's
fringe benefits amount is **more than A$2,000** for the FBT year ending
within the income year. The calculation excludes specified benefits under
section 5E and applicable regulations. The ATO distinguishes, for example,
an employer-provided car-parking benefit from reimbursement of an employee's
parking expense; the latter is not automatically reporting-excluded.
Meal entertainment and pooled/shared cars have their own conditions.
[ASSESS]; [REPORTING]

Once the threshold is met, gross up the **whole reportable individual
amount**, not merely the excess, using the **lower Type 2 rate, 1.8868**.
Do not use the Type 1 factor for RFBA even where it applied to employer
FBT. Allocate shared benefits and associates' benefits correctly. Special
not-for-profit reporting under section 135Q needs its separate analysis.
[ASSESS]; [REPORTING]; [CALCULATING]

Report for the income year ending immediately after the FBT year: benefits
in the year ending **31 March 2027** feed the income year ending **30 June
2027**, subject to the reporting rules. An April–June 2026 leaver can still
need reporting in the income year ending June 2027 even if no wages are
paid to that person in that later income year. RFBA affects specified
income tests; it is not itself part of the employee's assessable income.
Use `nf-payg-withholding` for selected STP timing and verify the applicable
reporting channels, finalisation, corrections and concessions. [REPORTING]

## Returns, instalments and records

The current ATO guidance requires a return if the employer has FBT payable
**or paid FBT instalments**, including where the return reconciles an
overpayment. A registered employer with no return required should use the
applicable notice of non-lodgment by the normal due date; registration or
nil tax alone does not justify ignoring the annual process. The approved
form and actual-year instructions remain required. [LODGING];
[ASSESS, sections 68 and 70][ASSESS]

The ordinary return/payment date is **21 May** following the FBT year.
Current ATO guidance generally allows **25 June** when a tax agent lodges
electronically and the employer was on that agent's FBT client list by
**21 May**. An accepted extension or next-business-day rule can change the
actual date. Establish the applicable program, method, list status and
extension before confirming a calendar deadline. A paper agent return
does not gain the electronic-agent date merely because an agent prepares it.
[ASSESS, section 68][ASSESS]; [LODGING]

FBT of **A$3,000 or more** for a year triggers quarterly instalments in the
**next** year. The activity statement supplies its instalment and due date.
The annual return reconciles instalments to actual FBT, with a shortfall or
refund. Lodge all activity statements for that FBT year, including March,
before the annual return. This reference does not select an instalment
variation or penalty calculation. [LODGING]

Section 132 generally requires records explaining relevant transactions
and acts, retained for **five years after their completion**. Associates
providing/arranging benefits have their own records and copy-to-employer
requirement, generally **within 21 days after the FBT year ends**. English
or readily English-convertible records must permit liability to be
ascertained. Specific exemptions and exceptions need their own conditions;
no record-keeping exemption threshold or penalty-unit dollar value is
selected here. [ASSESS]

## Fictional checks for the year ending 31 March 2027

These examples assume an ordinary taxable employer, established taxable
values and entitlement classes, no additional concessions or adjustments,
and the stated reporting facts. They are calculations of selected
components, not actual returns. [CALCULATING]; [REPORTING]; [LODGING]

1. **Private external reimbursement with no GST-credit entitlement:**
   A$10,000 is reimbursed, with no otherwise-deductible reduction or other
   relief. Type 2 gross-up gives **A$18,868**, and 47% gives **A$8,867.96
   FBT**. The island GST exclusion has not made the benefit FBT-free.
2. **Confirmed GST-creditable aggregate:** A$10,000 × 2.0802 gives
   **A$20,802**; 47% gives **A$9,776.94 FBT**. Actual entitlement is an
   assumed fact, not inferred from Norfolk residence or GST registration.
3. **Both classes:** A$10,000 in each class gives **A$39,670** combined
   grossed-up value and **A$18,644.90 FBT**. Reporting-excluded benefits
   are not silently removed from the employer's calculation.
4. **RFBA threshold:** an ordinary individual amount of exactly **A$2,000**
   does not cross the section 135P threshold, although employer FBT may
   still arise. A confirmed reportable amount of **A$2,500** is grossed up
   in full: A$2,500 × 1.8868 = **A$4,717 RFBA**. The taxable value is not
   reduced to its A$500 excess.
5. **Instalment boundary:** A$2,999 does not meet this particular
   next-year instalment trigger; **A$3,000 does**. Neither fact alone
   determines whether instalments were required in the current year.
6. **Minor-benefit boundary:** a A$299 notional value passes only the
   numerical limb and still needs all other conditions. **A$300 fails**
   that limb. Repeated A$299 rewards are not automatically exempt.
7. **Period transition:** a work-item benefit in the FBT year ending
   March 2027 uses the earlier section 58X with its application overlay.
   The enacted replacement applies to the FBT year beginning April 2027.
   A July 2026 compilation date does not move that application boundary.

## Review before a financial result

Reconcile the benefit register to the correct April–March population and
preserve separate records of taxable value, exemptions, reductions,
provider/GST-group credit entitlement, employer Type 1/2 aggregates and
employee reporting allocations. Verify elections and evidence before using
them; an unknown contribution, declaration or exemption is not invented.

Check strict A$300 and A$2,000 boundaries and the inclusive A$3,000 trigger.
Keep current-year and next-year instalments separate. Identify the applicable
work-item and vehicle transition before relying on a consolidated section.
Reconcile the annual liability, prior instalments and payable/refund to the
actual return instructions, including required rounding.

Still open: full car, loan, parking, entertainment, housing and
living-away-from-home valuation and elections; specialist employers;
complete otherwise-deductible and alternative-record rules; actual GST
credits, salary packaging, forms, reporting corrections and penalties;
future changes and remaining country topics. A reference check does not
waive the payroll workflow's required outputs or professional review.

## Primary sources and provenance

Checked **18 October 2026**. This is a **Tier 2 source-cited draft pending
professional review**. Current Register records and selected operative
provisions were checked together. The 2026 amendment's application clause
was read with the previous section 58X; the latest compilation was not
treated as the applicable wording for every year. The 2022 electric-car
amending Act was read in full, including both application schedules.

Large statutory captures were read in selected sections. Image formulas
missing from the text capture were not represented as verified: the
selected gross-up parameters and reporting method were checked against
the ATO's readable guidance, with the imposition rate verified in the Act.
Current lodging guidance was updated September 2026. Its link to 2026
return instructions is not proof of a published 2027 form. No private
records were queried and no registration, filing or payment was made.

[NI-BUSINESS]: https://www.ato.gov.au/norfolk-island/tax-for-businesses
[ASSESS]: https://www.legislation.gov.au/C2004A03280/2026-07-01/text
[PREVIOUS]: https://www.legislation.gov.au/C2004A03280/2025-04-01/text
[TAX]: https://www.legislation.gov.au/C2004A03281/2018-06-19/text
[OVERVIEW]: https://www.ato.gov.au/businesses-and-organisations/hiring-and-paying-your-workers/fringe-benefits-tax/how-fringe-benefits-tax-works
[CALCULATING]: https://www.ato.gov.au/businesses-and-organisations/hiring-and-paying-your-workers/fringe-benefits-tax/calculating-your-fbt
[REPORTING]: https://www.ato.gov.au/businesses-and-organisations/hiring-and-paying-your-workers/fringe-benefits-tax/fbt-registration-lodgment-payment-and-reporting/reportable-fringe-benefits
[LODGING]: https://www.ato.gov.au/businesses-and-organisations/hiring-and-paying-your-workers/fringe-benefits-tax/fbt-registration-lodgment-payment-and-reporting/lodging-your-fbt-return-and-paying
[REFORM-2026]: https://www.legislation.gov.au/C2026A00049/asmade
[EV]: https://www.legislation.gov.au/C2022A00086/asmade

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
