---
name: nf-payg-withholding
description: >
  Apply selected Norfolk Island PAYG withholding, registration and reporting
  rules for payments from July 2026. Separates employee withholding from
  territorial supplier ABN exceptions, declaration status, ordinary recurring
  pay coefficients, no-TFN rates, remittance cycles and STP finalisation.
  Use for Norfolk salary withholding, PAYG, employee declarations, payroll
  reporting or payment-summary questions. Includes primary legislation,
  period conversion, statutory rounding, fictional component examples and
  reviewer checks. Keeps super separate from employee deductions and
  preserves unresolved special payments, employment standards and payroll
  country slots. This source-cited reference does not complete a payslip,
  filing calendar, payroll engagement or country pack.
jurisdiction: NF
category: payroll
tax_year: 2026
tax_year_notes: "Selected PAYG instrument applies from 1 July 2026; reporting and payment periods must be established separately; checked 17 October 2026"
tier: 2
last_updated: 2026-10-17
version: 0.2
review_status: pending_review
depends_on:
  - workflow-base
  - payroll-workflow-base
---

# Norfolk Island: PAYG withholding and payroll reporting

Use `nf-tax-system` to establish Australian tax application and territorial
exceptions. Norfolk income-tax inclusion does not mean that every
mainland indirect-tax rule applies. This reference concerns selected PAYG
rules, not a separate Norfolk income-tax system. [TAA, sections 3 and
3AA][TAA]; [DICT, section 960-505][DICT]

Use `nf-employment-pay` for selected wage floors, Norfolk service rules,
leave, notice/redundancy and payslip/record duties. Neither reference fills
every payroll country slot or establishes an actual gross wage entitlement.

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
which excludes Norfolk Island. An island-only supplier enterprise therefore
does not satisfy subsection (1)(a); an island-only payer enterprise can
engage subsection (4)(a). An NF address alone does not settle enterprises
that also operate on the mainland. [TAA, section 12-190][TAA]; [GST,
section 195-1][GST]

Check the remaining supplier/agent ABN documentation, reasonable-belief,
small-supply, input-taxed, investment/trust-payment and qualifying private
or hobby statement exceptions in subsections (2) to (6). Do not split a
supply's payments to obtain the small-supply exception. This reference
does not select an actual supplier no-ABN rate or payment amount; obtain
the current regulations and all applicable exceptions first. The ATO's
Norfolk supplier guidance does not remove employee TFN or PAYG duties.
[TAA]; [WORKERS]

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
an undeclared reduction, or to subtract `nf-income-tax`'s annual relief
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
calendar; do not assume a Norfolk-only holiday moves every ATO due date.
[TAA]; [REPORT]

## STP, finalisation and payments outside STP

The ordinary section 389-5 notification is due on or before the statutory
withholding day, including nil withholding. Its current item 2 separately
covers specified qualifying-earnings payments to an SG employee, expressly
disregarding the labour-contract extension in SG section 12(3). An SG
liability alone does not select every STP branch. Section 389-10 permits
class and individual exemptions; establish the actual instrument or
notice. Norfolk location, small size and closely held status do not alone
prove an exemption or concession. [REPORT]

The ATO's Norfolk page requires ordinary STP reporting on or before payday.
Reconcile the applicable earnings, PAYG, super and year-to-date information
with the payroll records and current reporting specification. A report
does not pay PAYG or deliver super to a fund. Use `nf-super-guarantee` for
the separate payday SG rules, and keep employer SG out of employee wage
deductions. [WORKERS]; [REPORT]; [SG]

The ordinary finalisation declaration is due **14 July after the financial
year**. Under section 389-20, the annual report/payment-summary relief is
limited to amounts properly notified, with the required complete
declaration. A single STP event does not replace every payment summary.
Closely held, concessional, deferred and exempt cases need their current
specific authority before a different due date is selected. [REPORT];
[FINALISE]

For applicable payments outside that STP relief, section 16-155 generally
requires the annual payment summary within **14 days after year-end**;
section 16-153(2) generally requires the specified work/retirement/benefit
annual report by **14 August**. Payment categories, part-year requests,
termination/super payments, other annual reports and actual variations
have separate rules. The worker page identifies NAT 3447 for its payment
summary statement route; verify the current approved form and submission
method for the actual case. Do not use these dates for every supplier or
foreign payment. [TAA]; [WORKERS]

Correct incomplete or erroneous finalisation promptly under the current
ATO procedure and applicable correction period. The ATO describes update
events, removing an incorrect finalisation indicator and revising affected
activity-statement information. Reconcile STP, the applicable activity
statement, payment summaries and the PAYG liability without duplicating
the charge. No correction, submission or actual remittance is authorised
by this reference. [FINALISE]; [REPORT, sections 389-20 and 389-25][REPORT]

## Fictional component examples and checks

Amounts are AUD. All examples stipulate ordinary recurring cash earnings,
the stated valid declaration/status and no other adjustment unless shown.
They are withholding components, not complete payslips or tax assessments.

| Stipulated 2026–27 case | Component result |
|---|---|
| Weekly A$1,000.75, Scale 2 | x is 1,000.99; y is 137.825973; withhold A$138. |
| Weekly A$361.90 then A$362.00, Scale 2 | x values 361.99 and 362.99 select different rows; rounded withholding is A$0 in both cases. Band selection still matters. |
| Fortnightly A$2,000, Scale 2 | Weekly x 1,000.99; weekly A$138; fortnightly A$276. |
| Monthly A$4,333.33, Scale 2 | Add A$0.01 before conversion; weekly x 1,000.99; A$138 × 13 ÷ 3 gives A$598. |
| Quarterly A$13,000, Scale 2 | Weekly x 1,000.99; A$138 × 13 gives A$1,794. |
| Weekly A$1,000.75, Scale 1 | x 1,000.99; y 248.6660; withhold A$249. |
| Weekly A$1,000.75, Scale 3 | x 1,000.99; y 299.997; withhold A$300. |
| Resident no-TFN branch, A$1,000.99 earnings | Ignore 99 cents; 47% of A$1,000 is A$470; withhold A$470. |
| Foreign no-TFN branch, A$1,001.99 earnings | Ignore 99 cents; 45% of A$1,001 is A$450.45; discard result cents and withhold A$450. |
| Weekly A$1,000.75, Scale 2 and valid A$1,000 declared offset claim | Base A$138; declared reduction A$19; withhold A$119. This does not establish the underlying offset entitlement. |
| Monthly A$5,400.33, Scale 2 and valid A$1,365 declared offset claim | Weekly x 1,246.99; y 217.210173 rounds to A$217; monthly A$940; offset A$113; withholding A$827. |
| Island-only supplier enterprise with no ABN | The 12-190(1)(a)/(7) enterprise predicate fails. This does not remove withholding on an employee payment. |

Recheck every coefficient, endpoint, x conversion and rounding stage;
declaration validity; payment category; territorial enterprise facts;
withholder status and notices; calendar and concessions; STP coverage and
finalisation; and separate employer liabilities. A correct withholding
component does not establish lawful gross wages, cash net pay, employer
cost or a balanced payroll journal without all remaining inputs and rules.

## Sources and remaining coverage

Checked on 17 October 2026. The Register identifies the TAA's latest
available compilation as C2026C00393, effective 27 August to 30 September
2026. The separately commenced Tax Reform No. 2 Act changes section
45-340's PAYG instalment calculation, not the selected payroll provisions.
Do not treat an older compilation as a complete assurance about all
subsequent law. The 2026 withholding instrument's latest record remains
F2026L00716; its operative commencement is taken from section 2. Read
scopes and fictional checks are recorded in the dated verification log.
[TAA-LATEST]; [REFORM2]; [WITHHOLD-LATEST]

Special-payment and variation calculations, all SG/social programmes,
FBT, employment classification disputes, actual awards, overtime,
unaddressed employment standards and benefits, court deductions, workers compensation,
state/local payroll charges and the full payroll country contract remain
open. No blanket absence of another charge, professional sign-off, model
engagement benchmark or comprehensive-country acceptance is claimed.

[TAA]: https://www.legislation.gov.au/C1953A00001/2026-08-27/text
[REPORT]: https://www.legislation.gov.au/C1953A00001/2026-08-27/2026-08-27/text/original/epub/OEBPS/document_3/document_3.html
[TAA-LATEST]: https://www.legislation.gov.au/C1953A00001/latest/details
[WITHHOLD]: https://www.legislation.gov.au/F2026L00716/asmade/2026-06-12/text/original/epub/OEBPS/document_1/document_1.html
[WITHHOLD-LATEST]: https://www.legislation.gov.au/F2026L00716/latest/details
[DICT]: https://www.legislation.gov.au/C2004A05138/2026-08-27/2026-08-27/text/original/epub/OEBPS/document_10/document_10.html
[GST]: https://www.legislation.gov.au/C2004A00446/2026-01-01/text
[WORKERS]: https://www.ato.gov.au/norfolk-island/tax-for-businesses/paying-your-workers
[REMIT]: https://www.ato.gov.au/businesses-and-organisations/hiring-and-paying-your-workers/payg-withholding/paying-and-reporting-withheld-amounts/paying-and-reporting-payg-withholding-amounts-for-small-and-medium-withholders
[FINALISE]: https://www.ato.gov.au/finalisingSTP
[SG]: https://www.legislation.gov.au/C2004A04402/2026-07-01/text
[REFORM2]: https://www.legislation.gov.au/C2026A00071/asmade

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
