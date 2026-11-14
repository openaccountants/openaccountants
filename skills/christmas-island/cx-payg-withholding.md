---
name: cx-payg-withholding
description: >
  Apply selected Christmas Island PAYG withholding, registration and reporting
  rules for payments from July 2026. Separates employee withholding from
  territorial supplier ABN exceptions, declaration status, ordinary recurring
  pay coefficients, no-TFN rates, remittance cycles and STP finalisation.
  Use for territory salary withholding, PAYG, employee declarations, payroll
  reporting or payment-summary questions. Includes primary legislation,
  period conversion, statutory rounding, fictional component examples and
  reviewer checks. Keeps super separate from employee deductions and
  preserves unresolved special payments, employment standards and payroll
  country slots. This source-cited reference does not complete a payslip,
  filing calendar, payroll engagement or country pack.
jurisdiction: CX
category: payroll
tax_year: 2026
tax_year_notes: "Selected PAYG instrument applies from 1 July 2026; reporting and payment periods must be established separately; checked 24 October 2026"
tier: 2
last_updated: 2026-10-24
version: 0.1
review_status: pending_review
depends_on:
  - workflow-base
  - payroll-workflow-base
  - cx-tax-system
verified_by: pending
---

# Christmas Island: PAYG withholding and payroll reporting

Use `cx-tax-system` for the territory framework and separate tax regimes.
The Taxation Administration Act 1953 (TAA) extends to external territories
in its geographical definition of Australia. Section 2 adopts the income-tax
meaning; section 3AA applies that meaning to Schedule 1. Section 960-505 of
the 1997 Act expressly includes Christmas Island under paragraph 960-505(1)(d).
Island work is therefore not outside Australia merely because it is
offshore. Residence, employment and each payment still require their own
tests. GST geography has a separate exclusion. [TAA, sections 2, 3 and
3AA][TAA]; [DICT, section 960-505][DICT]; [GST, section 195-1][GST]

This guide does not establish actual gross wage entitlement, award
coverage, minimum wages, leave, overtime or payslip duties. Resolve those
rules independently before producing payroll outputs.

Load `workflow-base` and `payroll-workflow-base`. Preserve their source and
period gates, confirmed profile, refusal messages, four universal outputs
and every payroll output and check. This reference does not fill all
mandatory payroll country slots. Missing sources, fields or runtime
capabilities prevent a deliverable financial result. Unknown required
facts remain Needs Input; unresolved law remains on hold. No missing-fact
default is authorised here.

## Classify the payment before choosing a rate

Schedule 1 section 12-35 requires withholding from salary, wages,
commissions, bonuses and allowances paid to an individual as an employee,
including an employee of another entity. Sections 12-40 and 12-45 have
separate director and office-holder rules. Sections 12-55 and 12-60 address
qualifying voluntary agreements and labour-hire arrangements; a voluntary
agreement requires its approved form, an in-force quoted ABN and no other
Division 12 withholding requirement. It is not an alternative to employee
withholding. [TAA, Schedule 1 Subdivision 12-B][TAA]

Section 12-1 contains whole-payment exempt and non-assessable non-exempt
exceptions and specified benefit exclusions. Do not assume an allowance,
reimbursement or noncash benefit has ordinary wage treatment. Section
12-5's priority rules select one withholding provision when several cover
a payment. Employee withholding takes priority over labour hire and
supplier no-ABN withholding; do not deduct both. Alienated personal
services and noncash benefits have separate Divisions 13 and 14. Their
actual computations remain held. [TAA, sections 12-1 to 12-10][TAA]

### Supplier ABN exception is not an employee exception

Section 12-190(1) concerns a supply in an enterprise carried on in Australia
by the supplier. Subsection (4)(a) separately excludes payments outside an
enterprise carried on in Australia by the payer. For **both** predicates,
subsection (7) ignores parts of Australia outside the indirect tax zone,
which excludes Christmas Island. An island-only supplier enterprise therefore
does not satisfy subsection (1)(a); an island-only payer enterprise can
engage subsection (4)(a). An island address alone does not settle enterprises
that also operate on the mainland. [TAA, section 12-190][TAA]; [GST,
section 195-1][GST]

Check the remaining supplier/agent ABN documentation, reasonable-belief,
small-supply, input-taxed, investment/trust-payment and qualifying private
or hobby statement exceptions in subsections (2) to (6). Do not split a
supply's payments to obtain the small-supply exception. This reference
does not select an actual supplier no-ABN rate or payment amount; obtain
the current regulations and all applicable exceptions first. The supplier exception does not remove employee TFN or PAYG duties.
[TAA]

## Registration and declarations

Section 16-140 requires a qualifying withholder to apply in the approved
form by the first day it must withhold or make the specified payment to
the Commissioner, unless the Commissioner allows longer. Registration,
STP reporting, remittance and employer super are separate obligations.
Do not submit registrations or identifiers through this guide. Retain only
a stable reference and reviewer confirmation that necessary identifiers
and valid declarations are held outside the agent. [TAA]

Record tax residence, declaration receipt/effective date, threshold claim,
TFN quotation or exemption/application status, offsets, Medicare variation,
study loans, payment type and any actual Commissioner variation. A new
TFN declaration applies to subsequent payments and replaces the earlier
one; a valid Withholding declaration changes subsequent withholding under
its terms. A person with missing or inconsistent status is not automatically
assigned a guessed resident or foreign rate. [WITHHOLD, Schedule 1,
Payee declarations][WITHHOLD]

There is **no universal 28-day grace period**. Under Schedule 1:

- If no valid TFN declaration arrives within **14 days** of starting the
  payer-payee relationship, notify through the specified STP Phase 2
  employment/tax information with the applicable tax treatment code
  beginning in N, or complete/send the prescribed declaration route.
- Where the payee has neither quoted a TFN, claimed an exemption nor
  advised of an application/enquiry, the no-TFN rates apply.
- The **28 days** relate to a payee's declaration that an application or
  enquiry has been lodged. If the TFN is still absent after that period,
  use the no-TFN rates unless the ATO directs otherwise. Establish the
  actual declaration, dates and applicable interim treatment. [WITHHOLD]

Scale 4 uses **47% for residents** and **45% for foreign residents**, on
earnings of A$1 or more. Ignore cents in earnings, apply the rate, then
ignore cents in the result. Do not apply offsets, a Medicare adjustment or
study-loan withholding under this no-TFN branch. It is different from
supplier no-ABN withholding. [WITHHOLD, Schedule 1 Scale 4 and Payee
declarations][WITHHOLD]

## Ordinary recurring pay from 1 July 2026

The 2026 instrument commenced on **1 July 2026**, repealing the previous
2025 instrument. Its June registration date is not the pay-date start.
Schedule 1 covers specified work/services and benefit payments; it
excludes return-to-work and voluntary-agreement payments from its stated
Subdivision 12-B scope. Working holiday makers require Schedule 15.
Use the actual payment date and payment category. [WITHHOLD, sections 2,
5 to 7 and Schedule 1][WITHHOLD]

The following coefficients are for **Scales 1, 2 and 3 only**, before
separate authorised adjustments. They are withholding coefficients, not
annual marginal tax brackets. Scales 1 and 2 already incorporate Medicare;
do not deduct an annual Medicare calculation again. These scales require
a provided TFN and established applicable declaration status. [WITHHOLD]

### Scale 1: no tax-free threshold claimed

For weekly equivalent x, compute y = a × x − b using this table.
[WITHHOLD, Schedule 1 Scale 1][WITHHOLD]

| Weekly equivalent x, A$ | a | b, A$ |
|---|---|---|
| Below 188 | 0.1500 | 0.1500 |
| At least 188, below 371 | 0.2084 | 11.0185 |
| At least 371, below 515 | 0.1790 | 0.1066 |
| At least 515, below 932 | 0.3227 | 74.1674 |
| At least 932, below 2,246 | 0.3200 | 71.6508 |
| At least 2,246, below 3,303 | 0.3900 | 228.8816 |
| At least 3,303 | 0.4700 | 493.1893 |

### Scale 2: tax-free threshold claimed

Use only when the threshold claim and other circumstances select this
scale. Below the first endpoint, the withholding component is zero.
[WITHHOLD, Schedule 1 Scale 2][WITHHOLD]

| Weekly equivalent x, A$ | a | b, A$ |
|---|---|---|
| Below 362 | Zero withholding | Not applicable |
| At least 362, below 538 | 0.1500 | 54.3462 |
| At least 538, below 673 | 0.2500 | 108.2135 |
| At least 673, below 721 | 0.1700 | 54.3473 |
| At least 721, below 865 | 0.1790 | 60.8377 |
| At least 865, below 1,282 | 0.3227 | 185.1935 |
| At least 1,282, below 2,596 | 0.3200 | 181.7319 |
| At least 2,596, below 3,653 | 0.3900 | 363.4627 |
| At least 3,653 | 0.4700 | 655.7704 |

### Scale 3: foreign resident with TFN

This scale does not establish residence or override a special-payment
schedule. Foreign residents cannot claim offsets to reduce this withholding.
[WITHHOLD, Schedule 1 Scale 3 and Payee declarations][WITHHOLD]

| Weekly equivalent x, A$ | a | b, A$ |
|---|---|---|
| Below 2,596 | 0.3000 | 0.3000 |
| At least 2,596, below 3,653 | 0.3700 | 181.7308 |
| At least 3,653 | 0.4500 | 474.0385 |

### Period conversion and rounding

1. Establish earnings and allowances subject to withholding. Allowances
   need their own inclusion rules. Do not put every reimbursement or
   noncash benefit into ordinary earnings.
2. For weekly pay, discard cents from total included earnings, then add
   **A$0.99** to obtain x. For fortnightly pay, divide included earnings by
   two first; for quarterly pay divide by 13 first. Discard resulting cents
   and add A$0.99.
3. For monthly pay, add **A$0.01 if included earnings end in 33 cents**,
   then multiply by three and divide by 13. Discard cents and add A$0.99.
4. Select the row using x. Calculate y directly and round to the nearest
   dollar, with a half-dollar rounded up. Do not round to cents first.
5. Weekly withholding is that rounded amount. For fortnightly pay multiply
   it by two; quarterly by 13. For monthly pay multiply the rounded weekly
   amount by 13, divide by three and round again to the nearest dollar.
6. Apply only the separate adjustments actually authorised by the relevant
   declaration, schedule or variation. Scale 4 instead uses its truncation
   rule and the period's earnings, not this weekly-coefficient process.
   [WITHHOLD, Schedule 1 Using a formula and Working out the weekly
   earnings][WITHHOLD]

For valid offset claims under Scale 2, the specified reduction is the
declared total multiplied by **1.9% weekly, 3.8% fortnightly, 8.3% monthly
or 25% quarterly**, rounded to dollars. Scales 1, 3 and 4 do not permit
these reductions. An annual offset entitlement is not permission to make
an undeclared reduction, or to subtract `cx-income-tax`'s annual relief
again. Establish unusual or excessive adjustment handling before use.
[WITHHOLD, Schedule 1 Tax offsets and Payee declarations][WITHHOLD]

Scales 5/6 and Medicare variation formulas, senior/pensioner withholding,
study-loan additions and special schedules need their complete applicable
rules. A declaration for reduced Medicare and one requesting extra
surcharge withholding have different effects. This reference holds their
actual calculation. Ordinary pro-rata leave loading enters the period's
earnings; lump sum leave loading uses Schedule 5, and termination leave
and other termination lump sums require the distinct schedules. Do not
apply the ordinary table indiscriminately. The instrument also warns that
**53 weekly or 27 fortnightly pays** can leave insufficient withholding;
check its extra-pay guidance and any authorised arrangement before an
uplift. [WITHHOLD, Schedule 1][WITHHOLD]

## Paying withheld amounts to the ATO

Withheld amounts must be paid to the Commissioner. Confirm status for the
actual month using sections 16-95 to 16-115, historical withholding,
applicable wholly-owned-group aggregation and Commissioner notices.
The ordinary thresholds are more than **A$1 million** for large status
under the specified historical/group timing rules and more than
**A$25,000** for medium status where not large. Small status applies to
a month with withholding where neither other status applies. The ATO's
annual summaries are not a substitute for those statutory tests. [TAA];
[REMIT]

Section 16-75 gives the following ordinary payment rules, subject to the
stated branches, actual deferrals and applicable calendar rules:

| Established status | Statutory payment rule |
|---|---|
| Medium, not a deferred BAS payer | 21st day of the next month |
| Medium and a deferred BAS payer on the statutory test day | 28th of the next month; December amounts by 28 February |
| Small, not a deferred BAS payer | 21st day of the month after the quarter |
| Small and a deferred BAS payer on the statutory test day | September quarter: 28 October; December: 28 February; March: 28 April; June: 28 July |
| Large: withheld Saturday or Sunday | Second Monday after that day |
| Large: withheld Monday or Tuesday | First Monday after that day |
| Large: withheld Wednesday | Second Thursday after that day |
| Large: withheld Thursday or Friday | First Thursday after that day |

These rules exclude the section's separate closely held trust distributions.
Large withholders must pay electronically; medium/small use electronic
payment or a means approved in writing, subject to actual variations.
Do not infer permission to transfer funds from this reference. [TAA,
sections 16-70 to 16-85][TAA]

The 1997 Act's deferred BAS payer definition excludes specified monthly
GST-return and medium/large-withholding-only or annual-instalment-only
obligations. An island address or absence of GST registration does not
decide this status. Check the actual obligations at the required time.
[DICT, section 995-1][DICT]

Section 8AAZMB moves covered tax debts due on a non-business day to the
next business day, using its particular public-holiday definition. Schedule
1 section 388-52 separately addresses approved-form lodgment. A lodgment
deferral does not itself defer payment: section 388-55 says so. Verify the
actual calendar, notice and payment deferral before giving a dated filing
calendar; do not assume a territory-only holiday moves every ATO due date.
[TAA]; [REPORT]

## STP, finalisation and payments outside STP

The ordinary section 389-5 notification is due on or before the statutory
withholding day, including nil withholding. Its current item 2 separately
covers specified qualifying-earnings payments to an SG employee, expressly
disregarding the labour-contract extension in SG section 12(3). An SG
liability alone does not select every STP branch. Section 389-10 permits
class and individual exemptions; establish the actual instrument or
notice. Territory location, small size and closely held status do not alone
prove an exemption or concession. [REPORT]

The ATO's current Payday Super guidance requires ordinary STP reports on
or before payday and both qualifying earnings and super liability from
1 July 2026. Reconcile applicable earnings, PAYG, super and year-to-date
information with payroll records and the current reporting specification.
Its stated 2026-27 software transition still requires calculating and
paying SG, keeping payday records and starting qualifying-earnings
reporting as soon as possible. It is not a general payment deferral or
permission to omit reporting. Establish the actual software and applicable
concession before using it. [STP]

A report does not pay PAYG or deliver super to a fund. Use
`cx-super-guarantee` for the separate payday SG rules, and keep employer
SG out of employee wage deductions. [REPORT]; [SG]

The ordinary finalisation declaration is due **14 July after the financial
year**. Under section 389-20, the annual report/payment-summary relief is
limited to amounts properly notified, with the required complete
declaration. A single STP event does not replace every payment summary.
Closely held, concessional, deferred and exempt cases need their current
specific authority before a different due date is selected. [REPORT]

For applicable payments outside that STP relief, section 16-155 generally
requires the annual payment summary within **14 days after year-end**;
section 16-153(2) generally requires the specified work/retirement/benefit
annual report by **14 August**. Payment categories, part-year requests,
termination/super payments, other annual reports and actual variations
have separate rules. Verify the current approved form and submission
method for the actual case. No filing-ready form or portal is established
here. Do not use these dates for every supplier or foreign payment. [TAA]

Section 389-25 uses a correction period determined under that section;
there is no universal correction grace period established here. For QE
errors, the current ATO procedure distinguishes next-pay or update events
and requires records linking corrections to affected paydays. An update
event is not itself another QE payment; a finalisation indicator has a
specific reconciliation role. Follow the complete applicable procedure
before correcting actual reports. Other reporting corrections outside
the selected QE and finalisation procedures remain held.
Reconcile STP, activity statements, payment summaries and PAYG liabilities
without duplicate charges. No actual submission or remittance is
authorised by this reference. [QE-FIX]; [REPORT, section 389-25][REPORT]

For an error after finalisation, current ATO guidance says to lodge a
correcting update event as soon as possible. If corrected details cannot
be lodged straight away, lodge an update event removing the finalisation
indicator from the existing details; if correct finalisation cannot be
lodged by its due date, apply for a deferral. Once correct details and the
indicator are lodged, revise activity-statement W1/W2 information where
required. This procedure does not establish that an actual form, schema,
concession or correction period applies to an engagement. [FINALISE]

The current ATO procedure requires correcting errors within **14 days of
detection**, or by the next regular pay event when the pay cycle exceeds
14 days and that event is within the same financial year. For a prior
financial year, correct by **14 July immediately after that year**; if
that date has passed, correct as soon as possible. These branches are
not a universal permission to wait 14 days or a new period to amend a
tax assessment. Check the applicable authority, actual dates and any
valid deferral. [FINALISE]

| Timing case | Stipulated facts, with no applicable extension | Selected correction timing |
|---|---|---|
| F01 | Current-year error detected 5 August 2026; weekly pay cycle | Within 14 days of detection: 19 August 2026. |
| F02 | Current-year error detected 5 August 2026; pay cycle exceeds 14 days; next regular pay event is 2 September 2026 in the same financial year | By 2 September 2026, using the longer-cycle branch. |
| F03 | Error for 2025-26 detected 1 July 2026 | By 14 July 2026 under the prior-year branch. |
| F04 | Error for 2025-26 detected 1 August 2026, after 14 July | As soon as possible; no new 14-day or 5-year grace period. |

These are fictional correction-timing components. They do not establish
an engagement calendar, actual concessions or permission to submit.

## Fictional component examples and checks

Amounts are AUD. All examples stipulate ordinary recurring cash earnings,
the stated valid declaration/status and no other adjustment unless shown.
They are withholding components, not complete payslips or tax assessments.

| Case | Stipulated 2026-27 case | Component result |
|---|---|---|
| P01 | Weekly A$1,000.75, Scale 2 | x is 1,000.99; y is 137.825973; withhold A$138. |
| P02 | Weekly A$361.90 then A$362.00, Scale 2 | x values 361.99 and 362.99 select different rows; rounded withholding is A$0 in both cases. Band selection still matters. |
| P03 | Fortnightly A$2,000, Scale 2 | Weekly x 1,000.99; weekly A$138; fortnightly A$276. |
| P04 | Monthly A$4,333.33, Scale 2 | Add A$0.01 before conversion; weekly x 1,000.99; A$138 × 13 ÷ 3 gives A$598. |
| P05 | Quarterly A$13,000, Scale 2 | Weekly x 1,000.99; A$138 × 13 gives A$1,794. |
| P06 | Weekly A$1,000.75, Scale 1 | x 1,000.99; y 248.6660; withhold A$249. |
| P07 | Weekly A$1,000.75, Scale 3 | x 1,000.99; y 299.997; withhold A$300. |
| P08 | Resident no-TFN branch, A$1,000.99 earnings | Ignore 99 cents; 47% of A$1,000 is A$470; withhold A$470. |
| P09 | Foreign no-TFN branch, A$1,001.99 earnings | Ignore 99 cents; 45% of A$1,001 is A$450.45; discard result cents and withhold A$450. |
| P10 | Weekly A$1,000.75, Scale 2 and valid A$1,000 declared offset claim | Base A$138; declared reduction A$19; withhold A$119. This does not establish the underlying offset entitlement. |
| P11 | Monthly A$5,400.33, Scale 2 and valid A$1,365 declared offset claim | Weekly x 1,246.99; y 217.210173 rounds to A$217; monthly A$940; offset A$113; withholding A$827. |
| P12 | Island-only supplier enterprise with no ABN | The 12-190(1)(a)/(7) enterprise predicate fails. This does not remove withholding on an employee payment. |
| P13 | Weekly ordinary own employee: Scale 2 earnings and independently established eligible QE both A$1,000.75; full 12% SG and sufficient annual base; no extra adjustments | PAYG A$138; separate employer SG A$120.09. These do not establish cash net wages or total employer cost. |

Recheck every coefficient, endpoint, x conversion and rounding stage;
declaration validity; payment category; territorial enterprise facts;
withholder status and notices; calendar and concessions; STP coverage and
finalisation; and separate employer liabilities. A correct withholding
component does not establish lawful gross wages, cash net pay, employer
cost or a balanced payroll journal without all remaining inputs and rules.

## Held component cases

These are required outcomes. A number in another component cannot release
a held result. Needs Input identifies missing engagement facts; legal or
scope gaps require the specified source or separate guide.

| Case | Trigger | Required result |
|---|---|---|
| H01 | Tax residence or applicable declaration is unknown | Needs Input; withholding held. Do not guess Scale 1, 2, 3 or 4. |
| H02 | TFN application/enquiry is claimed but declaration and elapsed dates are missing | Needs Input; withholding held. Do not treat 28 days as a universal grace period. |
| H03 | Study loan, Medicare variation, working holiday maker, senior/pensioner or special payment applies | Ordinary result held; obtain the complete applicable schedule and inputs. |
| H04 | Declared offset reduction exceeds ordinary withholding or has unusual terms | Adjusted withholding held; establish authorised handling, with no invented negative deduction. |
| H05 | An island address is known but payer/supplier enterprise locations are not | Needs Input; supplier no-ABN result held. Employee PAYG remains a separate test. |
| H06 | Withholder class, group history or Commissioner notice is missing | Needs Input; dated remittance result held. |
| H07 | Deferred BAS status, relevant holidays or actual payment deferral is unresolved | Dated calendar held; STP or lodgment extension does not itself extend payment. |
| H08 | An SG labour-contract worker is assumed to be an ordinary STP employee solely from SG section 12(3) | STP result held; establish section 389-5 coverage separately. |
| H09 | A single STP event is offered as proof that every annual amount was finalised | Annual-report/payment-summary relief held until all relevant notified amounts and the complete declaration are established. |
| H10 | Actual gross entitlement, awards, payslip law or other compulsory deductions are unresolved | Complete payslip, net wages, employer cost and balanced payroll outputs held. |
| H11 | QE, annual employer base, SG status, fund choice or receipt deadline is missing | Employer SG or payment-deadline result held; use the SG companion and its inputs. |
| H12 | Special STP concession, approved form, filing specification or finalisation repair procedure is unverified | Affected filing or correction held; obtain current specific authority and runtime capability. |

## Payroll country contract

The payroll base requires all 12 mandatory slots. Coverage below records
this reference and its companions without certifying a complete country
payroll skill. No absent rule or missing programme is treated as zero.

| Mandatory slot | Established scope and remaining gate |
|---|---|
| 1. Income tax withholding | Ordinary recurring Scales 1-4 from 1 July 2026; special schedules and variations held. Use coefficients and statutory period conversion, not annual income-tax brackets. |
| 2. Social programmes | Selected SG is in `cx-super-guarantee`; other pension, health, unemployment, disability and accident programmes require a separate inventory and authority. |
| 3. Minimum wage | Not established here; current applicable award, classification, age, hours and territorial rules required. |
| 4. Overtime | Not established here; working week, thresholds, multipliers, daily rules and exemptions required. |
| 5. Benefits | Selected PAYG inclusion distinctions only; compulsory benefits and valuation rules remain open. |
| 6. Filings | Selected registration, remittance, STP and annual statutory rules only; actual forms, portals, reporting specification, exemptions and dated calendar required. |
| 7. Payslips | Legal fields and record duties not established here. |
| 8. Pension | Selected SG eligibility, rates, employer ceiling and operations route to the SG companion; no complete retirement-programme or tax-treatment inventory. |
| 9. Pay frequency | Tax conversion does not establish legal pay frequency; contract and employment rules required. |
| 10. Tax codes | Declaration and no-TFN branches above; actual tax-treatment codes and defaults require the current reporting specification and verified facts. |
| 11. Termination | Ordinary tables do not establish notice, severance, leave entitlement or termination withholding. Separate rules required. |
| 12. Currency and rounding | Selected amounts are AUD; PAYG whole-dollar rounding and Scale 4 truncation above. SG follows its companion. Other deductions and net-pay rounding require their own rules. |

The 5 payroll outputs, 4 universal outputs and all base checks remain
mandatory. These component examples cannot substitute for missing
outputs or establish a filing-ready engagement.

## Sources and remaining coverage

Checked on 24 October 2026. The current Register identifies TAA
compilation 227 (C2026C00468), effective 1 October 2026, and the 1997
Act compilation 268 (C2026C00471). Selected TAA Divisions 12, 15, 16 and
389, sections 3/3AA, 8AAZMB and 388-50 to 388-85 were compared with the
previous selected payroll sources and are unchanged after whitespace
normalisation. This is not a whole-Act amendment audit. The full current
withholding instrument matches the retained instrument after whitespace
normalisation, including all 19 selected coefficient rows. Its operative
commencement comes from section 2, not its June registration date.
[TAA-LATEST]; [DICT-LATEST]; [WITHHOLD-LATEST]

Special-payment and variation calculations, all SG/social programmes,
FBT, employment classification disputes, actual awards, overtime,
unaddressed employment standards and benefits, court deductions, workers compensation,
state/local payroll charges and the full payroll country contract remain
open. No blanket absence of another charge, professional sign-off, model
engagement benchmark or comprehensive-country acceptance is claimed.

[TAA]: https://www.legislation.gov.au/C1953A00001/2026-10-01/text
[REPORT]: https://www.legislation.gov.au/C1953A00001/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_3/document_3.html
[DICT-LATEST]: https://www.legislation.gov.au/C2004A05138/latest/details
[TAA-LATEST]: https://www.legislation.gov.au/C1953A00001/latest/details
[WITHHOLD]: https://www.legislation.gov.au/F2026L00716/asmade/2026-06-12/text/original/epub/OEBPS/document_1/document_1.html
[WITHHOLD-LATEST]: https://www.legislation.gov.au/F2026L00716/latest/details
[DICT]: https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_10/document_10.html
[GST]: https://www.legislation.gov.au/C2004A00446/2026-01-01/text
[REMIT]: https://www.ato.gov.au/businesses-and-organisations/hiring-and-paying-your-workers/payg-withholding/paying-and-reporting-withheld-amounts/paying-and-reporting-payg-withholding-amounts-for-small-and-medium-withholders
[STP]: https://www.ato.gov.au/businesses-and-organisations/super-for-employers/paying-super-on-payday/single-touch-payroll-reporting-under-payday-super
[QE-FIX]: https://www.ato.gov.au/businesses-and-organisations/super-for-employers/paying-super-on-payday/single-touch-payroll-reporting-under-payday-super/fixing-single-touch-payroll-errors-in-payday-super
[FINALISE]: https://www.ato.gov.au/businesses-and-organisations/hiring-and-paying-your-workers/single-touch-payroll/finalising-your-stp-data
[SG]: https://www.legislation.gov.au/C2004A04402/2026-07-01/text

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
