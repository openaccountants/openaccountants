---
name: nf-income-tax
description: >
  Classify Norfolk Island individual income tax residence, income and
  deductions before applying the Australian ordinary personal rates for
  2026–27. Covers territorial application, worldwide income, full-year and
  part-year thresholds, the conditional standard work-expense deduction,
  the low income tax offset, and Norfolk zone offset conditions. Use for Norfolk
  personal tax, resident rates, work deductions, mainland moves or zone
  offset questions. Includes statutory citations, fictional computations,
  classification patterns and reviewer checks. This source-cited reference
  preserves unresolved Medicare, other offsets, special income and filing
  requirements; it does not complete an individual return or the country pack.
jurisdiction: NF
category: international
tax_year: 2026
tax_year_notes: "Primary rate table: Australian 2026–27 income year, 1 July 2026 to 30 June 2027; selected adjacent-year changes separately labelled"
tier: 2
last_updated: 2026-10-17
version: 0.2
review_status: pending_review
depends_on:
  - workflow-base
  - income-tax-workflow-base
---

# Norfolk Island: individual income tax, deductions and zone offset

Use `nf-tax-system` for the post-2016 territorial reforms and conditional
pre-reform capital-gains transition. This guide supplies selected rules for
individuals taxed at personal rates. A company or trustee requires its own
analysis; an NF address does not select a tax computation.

Load `workflow-base` and `income-tax-workflow-base`. Preserve their source
and period gates, confirmed profile, refusals, four universal outputs and
all domain outputs and checks. This Tier 2 reference does not fill every
country slot. Missing mandatory rules, records or runtime capability still
prevent a deliverable financial result. Keep an unknown required fact as
Needs Input and an unresolved legal treatment on hold.

## Residence and territorial scope

Income Tax Assessment Act 1936 section 6 adopts the 1997 Act's meaning of
Australia. Section 960-505(1)(a) of the latter expressly includes Norfolk
Island geographically. Apply the current definitions rather than relying
on the old section 7A citation in historical Norfolk material. [ITAA36,
section 6][ITAA36]; [DICT, sections 960-505 and 995-1][DICT]

For an individual, section 6(1)'s residence definition covers ordinary
residence and includes these additional branches:

- Australian domicile, unless the Commissioner is satisfied that the
  permanent place of abode is outside Australia.
- Actual presence in Australia for more than half the income year, unless
  the Commissioner is satisfied both that the usual place of abode is
  outside Australia and that there is no intention to take up Australian
  residence.
- Membership of the specified Commonwealth superannuation scheme or
  eligible employment under the specified legislation, and the specified
  spouse or child under 16 relationship. This is not a test of membership
  of any Australian super fund. [ITAA36, section 6(1)][ITAA36]

Establish the actual residence history and applicable tests. Nationality,
a postal address or holiday days alone are insufficient. Moving between
Norfolk and the Australian mainland does not itself establish cessation
or commencement of Australian tax residence: both are within the income-tax
geographical definition. Residence for the zone offset, Medicare, SG or
immigration has a different statutory purpose.

Under sections 6-5 and 6-10, an Australian resident generally brings in
ordinary and statutory income from all sources. A foreign resident instead
has Australian-source income and other amounts included on a statutory
basis other than source. Test exemptions and non-assessable non-exempt
income separately; the territorial inclusion does not abolish them.
Temporary-resident concessions, treaties, dual residence, foreign tax
offsets and source disputes need further primary analysis. Do not infer
that every foreign receipt is taxable or exempt. [CORE, sections 6-5–6-23][CORE]

The ATO Norfolk page lists employment, pensions and other super receipts,
investments, business/partnership/trust income, foreign sources and
crowdfunding. Those labels are intake prompts, not interchangeable tax
categories. Identify the legal character, derivation date and applicable
inclusion or exclusion for each item. [INDIVIDUAL]

## Taxable income and ordinary resident rates

Under sections 4-10 and 4-15, establish assessable income and allowable
deductions before taxable income; then apply the appropriate rates and
special provisions to find basic income tax, followed by tax offsets.
Deductions equalling or exceeding assessable income do not produce
negative taxable income. Any loss has its own utilisation rules. A
deduction reduces income; an offset reduces tax. [CORE]

The following derived table applies only to **ordinary taxable income of
an adult Australian resident for the full 2026–27 income year**, using the
full $18,200 tax-free threshold. Amounts are Australian dollars and exclude
offsets, Medicare levy/surcharge and other adjustments. [RATES, sections
3 and 12, Schedule 7 Part I clause 1][RATES]

| Taxable income | Basic income tax for 2026–27 |
|---|---|
| $0–$18,200 | Nil |
| Over $18,200 to $45,000 | 15% of the excess over $18,200 |
| Over $45,000 to $135,000 | $4,020 plus 30% of the excess over $45,000 |
| Over $135,000 to $190,000 | $31,020 plus 37% of the excess over $135,000 |
| Over $190,000 | $51,370 plus 45% of the excess over $190,000 |

Apply each marginal rate only to its band. At exactly $45,000 the basic tax
is $4,020; at exactly $135,000 it is $31,020; at exactly $190,000 it is
$51,370. These are basic-tax amounts, not a return balance or withholding
schedule.

The first taxable band is **16% for 2025–26**, **15% for 2026–27** and
**14% for 2027–28 and later years** under the checked compilation. Keep the
income year attached to the figures. The other displayed marginal bands
remain 30%, 37% and 45% in those statutory tables. Recheck later amendments
before future-year use. [RATES, Schedule 7 Part I][RATES]

The ordinary table does not resolve working-holiday taxable income,
prescribed minors' income, special income components, superannuation or
employment-termination remainders, primary-producer averaging, professional
income averaging, trustees or prescribed non-resident cases. The Act has
separate definitions and rules for those branches. Do not apply a resident
table merely because the taxpayer receives money in Norfolk. [RATES,
sections 3, 3A, 13–15 and Schedule 7][RATES]

### Part-year residence

For qualifying part-year residency periods, section 20(1) replaces the
threshold with:

`$13,464 + ($4,736 × qualifying months / 12)`.

This follows from the statutory formula `$18,200 − $4,736` plus the
month-based component. It is not $18,200 multiplied by a day or month
fraction. Section 18 includes the month in which residence begins or ends
within its defined periods. It excludes a whole-year period and the
specified eligible-pensioner cases. Identify all periods and exceptions
before choosing a month count. [RATES, sections 16, 18 and 20][RATES]

For a stipulated qualifying period from January to June, six months give
$13,464 + $2,368 = **$15,832**. This threshold example does not determine
the person's residence, income inclusion, offset entitlement or final tax.
Do not reset the threshold merely because an Australian resident moves
between Norfolk and the mainland.

## Deductions and the 2026–27 standard work-expense rule

General deductions under section 8-1 require the income-producing or
business connection. They exclude capital, private/domestic, exempt-income
and non-assessable non-exempt income components, and amounts another rule
prevents. Specific deductions and restrictions require their own rules;
section 8-10 prevents double deductions. Mixed expenses need support and
apportionment. These principles do not themselves approve a business
asset, rental loss, donation or super contribution claim. [CORE, Division 8][CORE]

Section 25-130 applies from **2026–27 assessments**. It requires an
individual who is an Australian resident at some time in the income year
and derives assessable labour income that year. The statutory definition
refers to amounts included in assessable income from which withholding is
required, even if not actually withheld, under these Schedule 1 Taxation
Administration Act provisions:

- Sections 12-35, 12-40, 12-45, 12-47 and 12-50: employee, director,
  office-holder, religious-practitioner and return-to-work payments.
- Subdivision 12-C: retirement or termination payments.
- Paragraph 12-110(1)(ca): parental leave pay. [CORE, section 25-130(1),
  (4)][CORE]; [REFORM1, Schedule 4 item 17][REFORM1]

A label such as contractor, investment income or government payment does
not by itself meet that definition. The inclusion of termination payments
here does not make their tax rates ordinary wage rates.

The amount starts with the **lesser of $1,000 and assessable labour
income**, reduced, but not below zero, by the deductions specified in
section 25-130(2)(c)–(g). These cover connected general deductions, car
expenses, travel between workplaces where either activity has the required
labour-income purpose, specified asset repairs/depreciation/balancing
adjustments, and COVID-19 tests. Preserve the statutory connections and
extent limitations. [CORE]

For the general-deduction reduction, subsection (3) disregards deductions
to the extent they concern income-protection, personal-sickness or accident
insurance premiums, or trade/business/professional association membership.
Those exclusions do not establish that a premium or membership payment is
itself deductible. The standard amount is not an extra $1,000 on top of all
ordinary work deductions. [CORE]

The same reform repeals sections 900-35–900-45 and Subdivision 900-I for
2026–27 and later assessments. Do not carry an old $300 work-expense or
$150 laundry substantiation exception into this year. Keep evidence of
eligibility, income, actual deductions and apportionment; do not interpret
the standard rule as permission to omit all records. Associated asset,
low-value-pool and salary-packaging amendments require their own analysis.
[REFORM1, Schedule 4 items 8–20][REFORM1]

## Low income tax offset and priority

Section 61-110 provides the low income tax offset (LITO) from 2020–21
onward for an individual who is an Australian resident at any time in the
year and whose taxable income does not exceed $66,667. This is a
taxable-income test, not a test of gross wages or zone residence. The Act
has separate trustee/beneficiary rules. [OFFSETS]

Section 61-115's ordinary individual schedule is:

| Relevant taxable income | Statutory LITO amount before applicable caps |
|---|---|
| At or below $37,500 | $700 |
| Over $37,500 to $45,000 | $700 less 5% of the excess over $37,500 |
| Over $45,000 to $66,667 | $325 less 1.5% of the excess over $45,000 |
| Above $66,667 | No entitlement under section 61-110 |

At $40,000 the formula gives **$575**; at $45,000 it gives **$325**;
at $60,000 it gives **$100**. These examples assume an eligible adult
ordinary case. Sections 61-115(2)–(4) cap specified minors' and trustee
cases and address the section 160AAA benefit-offset interaction. Do not
give those cases an unrestricted adult offset. [OFFSETS]

Section 63-10 applies offsets in their statutory order. Its residual
category does not permit a refund, transfer or carry-forward of unused
LITO. The ATO works it out after lodgement and identifies it as a
non-refundable reduction to income tax, not a separate payment. Apply it
against available basic income tax; it does not automatically discharge
Medicare levy. Other offsets have different rules. [OFFSETS]; [ATO-LITO]

Near the upper cutoff, confirm assessment precision and rounding before
delivering an amount. Do not turn a cent-level formula residual into
negative relief or alter the statutory eligibility cutoff. This reference
does not supply the exact assessment-rounding method. The future working
Australians offset has its own conditions and applies from **2027–28**;
do not add it to a 2026–27 computation. [REFORM1, Schedule 3 item 4][REFORM1]

Use `nf-medicare` for selected levy and surcharge rules. All remaining
income, offset, credit, prepayment and filing conditions still require
resolution before a final return balance.

## Norfolk zone tax offset

Schedule 2 Part I of the 1936 Act lists Norfolk Island in Zone A. The ATO
Norfolk individual page identifies **$1,173 as the fixed zone amount most
Norfolk residents can claim**, with possible dependent-related increases.
Section 79A(2)(a) supplies the special-area amount of $1,173 plus 50% of the
statutorily defined relevant rebate amount, subject to its qualifications.
Do not replace that Norfolk guidance with the ordinary Zone A $338 figure
or treat every person visiting the island as eligible. [ZONES]; [ITAA36,
section 79A][ITAA36]; [INDIVIDUAL]

Eligibility concerns the **usual place of residence**, not simply working
or being present in a zone. Section 79A(3B)(a) requires more than half the
income year; subsection (3C) permits aggregated qualifying periods. For
2026–27's 365 days, 183 qualifying days exceed half and 182 do not. Keep
the statutory half-year test for other years rather than assuming a fixed
day count for every year. [ITAA36]

The section also provides separate death, combined consecutive-year and
longer continuous-residence branches. The two-year route has its own
current/prior-year duration, prior entitlement and excluded-service-day
conditions; it is not a free choice to add any two years. The longer route
requires current-year presence including its first day, the specified
earlier year, continuity and the other subsection (3B)(e) conditions. A
short current-year stay therefore requires the actual history, not an
automatic refusal or automatic full offset. [ITAA36, section 79A(3B)–(4)][ITAA36]

Calculate dependent-related additions only after establishing the relevant
actual/notional rebates and income/dependency conditions. Reduce the
otherwise available rebate by the prescribed remote-area allowance under
subsection (2A). Check competing UN/overseas-forces relief under sections
23AB and 79B: the same person cannot simply stack the headline amounts.
These special branches remain held until their complete conditions and
evidence are supplied. [ITAA36]; [INDIVIDUAL]

The ATO identifies the zone offset as non-refundable. Its unused amount
does not itself generate a refund, although withholding or other credits
may separately affect the return balance. Zone residence does not establish
Medicare entitlement, a Medicare exemption or eligibility for the Norfolk
SG transitional rate. [INDIVIDUAL]; `nf-super-guarantee`

## Fictional computations and classification patterns

All figures below are stipulated examples, not taxpayer determinations:

| Stipulated facts | Treatment or result |
|---|---|
| Full-year adult resident; ordinary taxable income $60,000 in 2026–27; no special rate branch | Basic income tax: $4,020 + ($15,000 × 30%) = **$8,520**, before offsets and levies. |
| Same ordinary scope at $200,000 | Basic income tax: $51,370 + ($10,000 × 45%) = **$55,870**. |
| Same $45,000 ordinary taxable income in 2025–26 versus 2026–27 | Basic tax is $4,288 versus $4,020, a **$268** difference. Do not use that difference as the person's final saving. |
| Eligible standard-deduction taxpayer; labour income $50,000; reducing deductions $400; no other reductions | Standard amount **$600**, plus the stipulated $400 reducing deductions: $1,000 combined. |
| Same eligibility; labour income $700; reducing deductions $200 | Standard amount **$500**, not $800 or $1,000. |
| Same eligibility; labour income $50,000; reducing deductions $1,200 | Standard amount **nil**; do not deduct another $1,000. Actual deductions still require their own entitlement and records. |
| Same first standard-deduction case plus an independently allowable $200 association membership deduction, fully within subsection (3) | Membership does not reduce the $600 standard amount; the stipulated total of those deductions is **$1,200**. |
| Zone eligibility and fixed-only $1,173 amount established; remaining basic income tax before that offset stipulated at $900 | That offset reduces that remaining tax to **nil**; the unused **$273** does not itself become a refund. This is not a calculation of other offsets, levies or the return balance. |
| A worker visits Norfolk for 190 days but retains their usual home elsewhere | Visit/work days alone do not establish zone eligibility. Analyse usual residence and the statutory branches. |
| A continuing Australian tax resident moves from Norfolk to the mainland midyear | Do not select part-year residence solely because of that move. Review zone history separately. |
| Only employment wages are known; investment income, deductions or residence history are missing | Needs Input. Do not treat wages as complete taxable income or use the examples as a return. |

Reconcile every income category and deduction, check exact bracket
boundaries and the year, distinguish deduction from offset, and validate
each zone residence branch. Retain withheld tax, PAYG instalments and other
credits separately from basic tax. Never infer a final refund from the
table or from a non-refundable offset alone.

## Sources, currency and remaining work

Checked on 17 October 2026: Rates Act compilation 66, effective 1 July
2026, identified as latest by its live Register record; selected 1936 Act
provisions in compilation 193, effective 1 October 2026, registered
15 October; and selected 1997 Act provisions in compilation 267, whose
recorded interval is 27 August–30 September 2026. The latter is not an
assertion that the whole Act is current beyond that interval.

The later Tax Reform No. 2 Act was checked for commencement and amendment
targets: its schedules commence 1 October 2026 and address corporate loss
carry-back, business asset thresholds, a specified PNG-employment exemption
and future residential-property rules. Those subjects need separate
analysis; they do not replace the selected residence definitions, ordinary
rate table or section 25-130 reproduced in this reference. Apply exemptions
and later amendments to actual facts rather than assuming all employment
income or expenses have ordinary treatment. [REFORM2]

The ATO individual page, updated 5 May 2026, supplies Norfolk context,
the fixed zone amount, non-refundable character and broad lodging guidance.
It predates the standard-deduction reform and does not displace the later
statutory rule. Its general 31 October lodging statement does not settle
an actual year's due date, weekend rule, agent programme or deferral.
[INDIVIDUAL]

Use `nf-medicare` alongside this reference for selected levy and surcharge
rules. Other offsets, temporary
residence/treaties, foreign credits, income-specific regimes, CGT beyond
the scope guide's transition, rentals/business losses/assets, forms,
lodging/payment deadlines, amendments and complete workflow country slots
remain open. No actual return, complete Norfolk pack, independent model
engagement benchmark or practitioner sign-off is claimed. Do not submit
identifiers, documents, a return or payment through this guide.

[RATES]: https://www.legislation.gov.au/C2004A03348/2026-07-01/text
[ITAA36]: https://www.legislation.gov.au/C1936A00027/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_1/document_1.html
[ZONES]: https://www.legislation.gov.au/C1936A00027/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_5/document_5.html
[CORE]: https://www.legislation.gov.au/C2004A05138/2026-08-27/2026-08-27/text/original/epub/OEBPS/document_1/document_1.html
[DICT]: https://www.legislation.gov.au/C2004A05138/2026-08-27/2026-08-27/text/original/epub/OEBPS/document_10/document_10.html
[REFORM1]: https://www.legislation.gov.au/C2026A00049/asmade
[REFORM2]: https://www.legislation.gov.au/C2026A00071/asmade
[INDIVIDUAL]: https://www.ato.gov.au/norfolk-island/norfolk-island-residents-and-individual-tax
[OFFSETS]: https://www.legislation.gov.au/C2004A05138/2026-08-27/2026-08-27/text/original/epub/OEBPS/document_2/document_2.html
[ATO-LITO]: https://www.ato.gov.au/individuals-and-families/income-deductions-offsets-and-records/tax-offsets/low-income-tax-offset

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
