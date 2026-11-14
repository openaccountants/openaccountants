---
name: cc-income-tax
description: >
  Selected Cocos (Keeling) Islands individual income-tax rules for 2026-27.
  Establishes the Australian territorial bridge, residence and income-year
  gates, ordinary resident and foreign-resident personal rates, conditional
  part-year threshold, low income tax offset, standard work-expense deduction,
  substantiation changes, special-area zone relief and ordinary Medicare
  reductions, single-person, family/period and ordinary surviving spouse
  surcharge components, bounded reportable-super inputs and ordinary concessional
  cap/carry-forward excess and ordinary personal-super deduction worksheets. Use for
  Cocos (Keeling) Islands personal tax, ordinary annual rates, mainland moves or
  levy-exemption questions. Includes primary legislation, fictional component
  calculations, required intake, refusals and reviewer checks. This source-cited
  draft accepts taxable income only after all applicable income and deduction
  rules are resolved; it does not complete a return or the country pack.
jurisdiction: CC
category: international
tax_year: 2026
tax_year_notes: "Selected ordinary personal rates for 1 July 2026 to 30 June 2027; adjacent years and Medicare conditions require their separately identified sources"
tier: 2
last_updated: 2026-10-23
version: 1.1
review_status: pending_review
depends_on:
  - workflow-base
  - income-tax-workflow-base
verified_by: pending
---

# Cocos (Keeling) Islands: selected individual income tax for 2026-27

Establish Australian tax residence, the income year and the character of
every income component before selecting a personal rate. A Cocos (Keeling) Islands
address, citizenship or bank account does not settle those questions.

Load `workflow-base`, `income-tax-workflow-base` and `cc-tax-system`.
Preserve their source and period gates, confirmed profile, refusals, outputs
and checks. This companion supports selected component working papers for
a credentialed reviewer. Its incomplete income-tax slots prevent a complete
financial deliverable until the missing law, evidence and runtime capability
are supplied. No comprehensive-country acceptance or professional sign-off
is claimed.

## Territorial application, residence and income

Section 8E of the Cocos (Keeling) Islands Act 1955 extends Commonwealth Acts of
their own force unless an Act expressly provides otherwise. The income-tax
definition of geographical Australia expressly includes Cocos (Keeling) Islands
under section 960-505(1)(e) of the 1997 Act. This bridge does not extend the
GST indirect tax zone or decide a person's residence. [TERRITORY]; [DICT]

For an individual, section 6(1) of the 1936 Act includes ordinary residence,
the domicile test with its permanent-place-of-abode exception, presence for
more than half the income year with its usual-abode/intention exception,
and specified Commonwealth-superannuation connections. A simple day count
or immigration label cannot replace the complete applicable tests. The
1997 Act's resident definition connects to that provision. Resolve treaty
residence and temporary-resident exceptions separately before inclusion or
rate selection. [RESIDENCE]; [DICT, section 995-1][DICT]

Sections 6-5 and 6-10 distinguish a resident's worldwide ordinary/statutory
income from a foreign resident's Australian-source income and other
statutory inclusions. Section 6-15 preserves exempt and non-assessable
non-exempt income. An island receipt is not automatically exempt, and a
foreign account is not automatically outside assessable income. Source,
derivation, specific exemptions and treaty limits need their own evidence.
[CORE, sections 6-5, 6-10 and 6-15][CORE]

For an ordinary individual using the standard year, **2026-27 runs from
1 July 2026 to 30 June 2027**. The financial-year definition and section
4-10 must be read with any permitted substituted accounting period under
1936 Act section 18. Do not derive a return or payment deadline from the
year end. [CORE]; [DICT, section 995-1][DICT]; [RESIDENCE]

Use `cc-super-guarantee` for selected 2026-27 employer SG rules. SG
computation is separate from taxable-income and Medicare calculations;
that companion preserves its own missing programme and operational slots.

## Period figures and ordinary personal rates

All money figures are **Australian dollars**. The following selected
figures were checked on **21 October 2026**. Rates Act compilation 66 of
1 July 2026 was shown as latest by its live Register record. [RATES-RECORD]

The resident table applies only to an **adult Australian resident for the
whole 2026-27 income year**, with the full tax-free threshold and ordinary
taxable income. It excludes offsets, Medicare and other adjustments.
Section 3 defines the threshold as **$18,200**; section 12 and Schedule 7
Part I clause 1 supply the marginal rates. [RATES]

| Ordinary taxable income | Basic income tax for 2026-27 |
|---|---|
| $0 to $18,200 | Nil |
| Over $18,200 to $45,000 | 15% of the excess over $18,200 |
| Over $45,000 to $135,000 | $4,020 plus 30% of the excess over $45,000 |
| Over $135,000 to $190,000 | $31,020 plus 37% of the excess over $135,000 |
| Over $190,000 | $51,370 plus 45% of the excess over $190,000 |

The ordinary **whole-year foreign-resident** table has no tax-free
threshold. Establish the Australian taxable amount first; do not apply
these rates to all worldwide receipts merely because a bank statement
contains them. [RATES, section 3 and Schedule 7 Part II clause 1][RATES]

| Ordinary taxable income | Basic income tax for 2026-27 |
|---|---|
| $0 to $135,000 | 30% of that amount |
| Over $135,000 to $190,000 | $40,500 plus 37% of the excess over $135,000 |
| Over $190,000 | $60,850 plus 45% of the excess over $190,000 |

The first resident taxable band is **16% for 2025-26**, **15% for 2026-27**
and **14% for 2027-28 and later years** in the checked compilation. Keep
those tables separate. A withholding scale is not this annual liability
table. [RATES, Schedule 7 Part I][RATES]

Special income components, working-holiday taxable income, prescribed
minors, trustees, superannuation and termination remainders, primary
producer averaging and professional-income averaging require their own
rules. A treaty may also affect a branch. Neither ordinary table approves
those computations. [RATES, sections 3, 3A and 12-15 and Schedule 7][RATES]

### Part-year threshold

Sections 16, 18 and 20 define qualifying part-year residency periods,
including the relevant starting or ending month and the eligible-pensioner
and whole-year exclusions. For an ordinary individual to whom section
20(1) applies, the threshold is:

`$13,464 + ($4,736 × qualifying months / 12)`.

This is the statutory $18,200 threshold less $4,736, plus the month-based
component. The official HTML's formula image alternative text was checked
alongside the section; the plain-text extraction omits the image. This is
not a daily fraction of $18,200. Multiple periods need the actual statutory
month count. Trustee computations have separate subsections. [RATES,
sections 16, 18 and 20][RATES]

A continuing Australian tax resident who moves between Cocos (Keeling) Islands
and the mainland does not become a part-year resident solely because of
that move. Establish an actual residence change before altering the
threshold or income inclusion. [RESIDENCE]; [RATES]

## Taxable income, deductions and the low income tax offset

Under sections 4-10 and 4-15, establish assessable income and all allowable
deductions before taxable income, apply the correct basic-tax rules, then
apply offsets in their statutory order. Deductions exceeding assessable
income do not produce negative taxable income. Loss utilisation is a
separate question. A deduction reduces income; an offset reduces tax.
[CORE]

General deductions under section 8-1 require the stated income-producing
or business connection and exclude capital, private/domestic, exempt-income
and non-assessable non-exempt income components, and amounts another rule
prevents. Section 8-5 preserves specific deductions/restrictions and section
8-10 prevents double deductions. These provisions alone do not settle
every work expense, asset, rental loss or business loss. Apply the selected
2026-27 reform below and obtain the remaining operative rules before
accepting taxable income. [CORE, Division 8][CORE]

### Standard work-expense deduction from 2026-27

Section 25-130 applies to an individual who is Australian resident at any
time in the income year and derives assessable labour income. For 2026-27,
work out the additional deduction as:

`max(0, min($1,000, assessable labour income) − specified deductions)`.

This is a deduction from assessable income, not a $1,000 tax offset or a
$1,000 addition to every actual-expense claim. No actual expense is needed
to generate the standard amount, but residence, qualifying income and the
amounts reducing it need evidence. Whole-year foreign residents fail its
residence condition. [CORE, section 25-130][CORE]; [REFORM, Schedule 4
items 3 and 17][REFORM]

Assessable labour income means an assessable payment from which withholding
is required under Schedule 1 to the Taxation Administration Act 1953:
sections 12-35, 12-40, 12-45, 12-47 or 12-50; Subdivision 12-C; or paragraph
12-110(1)(ca). These cover the specified employee, director, office-holder,
religious-practitioner, return-to-work, retirement/termination and parental
leave payments. The definition applies even if the amount was not actually
withheld. Do not include all business receipts, personal services income or
benefits merely because they are income; establish the exact statutory
withholding category and assessability first. [CORE, section 25-130(4)][CORE]

The reducing amounts are allowable deductions, not all cash spending:

| Section 25-130(2) branch | Amount reducing the standard deduction |
|---|---|
| (c), section 8-1 | Each deduction to the extent the outgoing was incurred in gaining or producing assessable labour income, subject to subsection (3). |
| (d), Division 28 | Car deductions to the extent they arise from gaining or producing assessable labour income. |
| (e), section 25-100 | Travel-between-workplaces deduction where either specified workplace activity was undertaken to gain or produce assessable labour income. |
| (f), section 25-10 and Subdivisions 40-B/40-D | Repair, decline-in-value and balancing-adjustment deductions to the extent the asset is used to produce assessable labour income. |
| (g), section 25-125 | Each allowable COVID-19 test deduction; paragraph (g) has no added labour-income apportionment condition. |

For branch (c) only, disregard the portion of a section 8-1 deduction for
income-protection, personal-sickness or accident-insurance premiums, or
membership of a trade, business or professional association. Those
exceptions do not establish deductibility, waive evidence requirements or
exclude an amount independently covered by another reducing branch. Keep
other income-related deductions separate and prevent duplicate deductions
under section 8-10. [CORE, sections 8-10 and 25-130(2)-(3)][CORE]

Schedule 4 Part 1 of Act 49 of 2026 commenced on 1 July 2026 and applies to
assessments for **2026-27 and later income years**. Do not apply this rule
to 2025-26. The same Part repeals section 28-180, sections 900-35 to 900-45
and Subdivision 900-I. Prior-year substantiation exceptions in those
provisions cannot be carried forward. [REFORM, section 2 and Schedule 4
items 4, 10-12 and 17][REFORM]

### Actual-expense evidence and asset transitions

For an actual work-expense deduction, section 900-15 requires an independent
deduction entitlement and written evidence, subject to the applicable
exceptions. Section 900-115 generally requires a supplier document showing
the supplier, amount and original currency, nature of supply, expense date
and document date. Its stated alternatives can supply a missing expense
date or description; a bank label alone does not supply every requirement.
Asset acquisition evidence has its own section 900-120 requirements.
[DICT, sections 900-15, 900-110, 900-115 and 900-120][DICT]

For travel involving **6 or more consecutive nights** away from ordinary
residence, section 900-20 requires travel records, subject to the applicable
exception. Record the activity, location, start day/approximate time and
duration contemporaneously as section 900-150 requires. Under section
900-25, retain the required evidence and travel records for **5 years from
the return's due date, or actual lodgement if later**; a relevant dispute
can extend retention. Do not confuse that retention rule with a filing
deadline. [DICT, sections 900-20, 900-25 and 900-150][DICT]

Sections 900-50 to 900-65, Subdivision 900-E and Subdivision 900-H preserve
conditional evidence alternatives or relief. They do not themselves make
private spending deductible. Resolve the exact exception, allowance,
reasonable-amount determination and evidence before approving a claim;
this guide supplies no current travel, car or home-working rate.
[DICT, Division 900][DICT]

Asset treatment also needs a separate calculation. Section 40-291A permits
a **50% reduction of the balancing-adjustment amount instead of the
section 40-290/40-291 reduction** only where the asset has been used to gain
or produce assessable labour income, a section 25-130 deduction has been claimed for
an income year and the asset's effective life overlaps that year. Section
40-425(9) restricts new low-value-pool allocations where the asset was
reasonably expected to be used mainly for assessable labour income at
first use or installation ready for use. Act 49 preserves allocations
already made for 2025-26 or earlier. Do not apply the restriction to an
existing pool indiscriminately or claim the 50% option without its facts.
[OFFSETS, sections 40-291A and 40-425(9)][OFFSETS]; [REFORM, Schedule 4
items 7-8 and 17(2)][REFORM]

Schedule 4 Part 2 changes selected FBT rules only for **FBT years starting
on or after 1 April 2027**. Do not treat the personal-income-tax start date
as the FBT application date or infer salary-packaging relief. Complete FBT,
asset/CGT, reimbursement, special-deduction and business-loss treatment
remain outside this selected computation. [REFORM, Schedule 4 items 18-20][REFORM]

### Low income tax offset

For an ordinary adult individual, section 61-110 provides LITO where the
person is Australian resident at any time in the income year and taxable
income does not exceed **$66,667**. Whole-year foreign residents do not meet
that residence condition. Section 61-115 provides the following amount
before applicable limitations. [OFFSETS]

| Relevant taxable income | LITO for an otherwise eligible ordinary adult |
|---|---|
| At or below $37,500 | $700 |
| Over $37,500 to $45,000 | $700 less 5% of the excess over $37,500 |
| Over $45,000 to $66,667 | $325 less 1.5% of the excess over $45,000 |
| Above $66,667 | No entitlement under section 61-110 |

Prescribed minors and trustee cases have additional caps and rules under
section 61-115(2)-(4), including the specified benefit-offset interaction.
Those cases are outside this ordinary adult calculation. Near the upper
cutoff, verify exact assessment precision and rounding; do not produce
negative relief from a fractional-cent formula result. [OFFSETS]

Apply offsets against available basic income tax in section 63-10's order.
Unused LITO is non-refundable, non-transferable and cannot be carried
forward. It is not a separate payment or an automatic discharge of Medicare
levy. The ATO works it out after lodgement and records it as a non-refundable
offset on the assessment. Other credits or withholding can affect a refund
separately. [OFFSETS]; [ATO-LITO]

## Zone relief: local classification and actual residence

Schedule 2 Part I items 7 and 8 of the 1936 Act place Cocos (Keeling)
Islands and Christmas Island in Zone A. The current ATO Western Australia
list, checked on 21 October 2026, explicitly labels **both islands
'A (special area)'**. This is a tax-zone listing, not a statement that the
territories form part of Western Australia. [ZONES]; [ATO-ZONES]

Section 79A(1) excludes a company or trustee and requires residence in the
prescribed area as defined for that section. Zone residence is a separate
question from Australian tax residence. Under section 79A(3B)(a), the
usual place of residence must be in the prescribed area for **more than
half the income year**. For the ordinary 365-day 2026-27 year, 183 days
exceed half; 182 do not. Working or visiting on an island for that many
days does not prove usual residence. A FIFO worker whose usual home
remains outside the zones does not qualify on workdays alone.
[RESIDENCE, section 79A(1) and (3B)][RESIDENCE]; [ATO-ZONE]

The death, consecutive-part-year and longer continuous-residence branches
in section 79A(3B)(c)-(e), with aggregation under subsection (3C), can change
that result. They have distinct current/prior-year, unclaimed-year,
first-day, continuity and excluded-service conditions. Do not automatically
reject a shorter current-year period or claim it by adding arbitrary past
visits. Resolve the applicable statutory branch with the complete dates,
prior claims and service records before calculating it. Those complex
branches are held for review here. [RESIDENCE, section 79A(3B)-(3C)][RESIDENCE]

For a qualifying person resident in the special area of Zone A or B,
section 79A(2)(a) provides **$1,173 plus 50% of the relevant rebate amount**,
subject to subsection (2A), the Defence-force interactions and other stated
limits. Ordinary Zone A's $338 and Zone B's $57 are different branches;
neither is the listed special-area base for these islands. The relevant
rebate amount is the statutory sum of the specified invalid/dependant and
notional offsets, not all family spending or any arbitrary dependant
allowance. Those additions need their own complete eligibility and amount
rules. [RESIDENCE, section 79A(2) and (4)][RESIDENCE]; [ATO-ZONE]

Reduce the zone rebate by the prescribed remote area allowance paid for
the year under section 79A(2A). Section 79A(4) identifies the relevant
Social Security Act or Veterans' Entitlements Act remote-area component.
Check the actual allowance record and relevant rebate amount; an unknown
amount is not nil. Sections 23AB and 79B, including 79B(4)-(4A), prevent
unrestricted stacking with service rebates. Hold any overlapping-service,
mixed-zone, Commissioner-discretion, uncertain reduction or dependant
case until the complete governing rules are resolved. [RESIDENCE]

The special-area definition uses the statutory **1 November 1981** distance
position and the specified **30 June 1981 census** definitions. Do not
reclassify an island using today's population, an air distance or the
shorter overview alone. Section 79A(3E) also gives the Commissioner a
specified adjacent-area discretion. The ATO list corroborates the local
classification; it does not replace the personal eligibility tests.
[RESIDENCE, section 79A(3D)-(4)][RESIDENCE]; [ATO-ZONES]

Apply zone relief against available basic income tax under section 63-10.
It is non-refundable, non-transferable and cannot be carried forward; it
does not independently eliminate Medicare. Withholding may separately
create a refund. Seniors, foreign-tax, franking, small-business and other
offsets, dependant additions and the complete return balance still need
their own rules. [OFFSETS, section 63-10][OFFSETS]

## Medicare: ordinary levy, reductions and prescribed periods

Establish the charge under section 251S before calculating a levy. A
whole-year prescribed person can have no ordinary levy under section 251T,
but an island address alone does not establish that status. These rules
cover an ordinary adult individual only. Trustees, special superannuation
adjustments under section 251S(1A), arrears under Levy Act section 9A and
surcharge require their complete separate rules. [MEDICARE]; [LEVY]

### Source period and individual reduction

The Medicare Levy Act compilation 53 of 1 July 2026 was checked on
**23 October 2026**. Act 58 of 2026, Schedule 5, commenced on 1 July 2026;
item 14 applies its threshold amendments to **2025-26 assessments and later
years**. The following are the amounts in that checked law for the selected
2026-27 reference, subject to subsequent amendments and the engagement
source gate. The ATO reduction pages corroborate these figures but expressly
label their guidance **2025-26**; their year label is not changed here.
[LEVY-RECORD]; [LEVY]; [LEVY-AMEND]; [ATO-LEVY-SINGLE]; [ATO-LEVY-FAMILY]

| Individual branch | Lower threshold H | Statutory phase-in limit U |
|---|---|---|
| Entitled to the section 160AAAA seniors and pensioners rebate | $44,268 | $55,335 |
| Every other ordinary individual | $28,011 | $35,013 |

Use the higher branch only after actual section 160AAAA entitlement is
established. Age or general pension eligibility alone is insufficient.
That entitlement includes the statutory conditions, rebate-income rules,
regulations and section 160AAA interaction. This guide does not compute
SAPTO; an unresolved entitlement is Needs Input. [SAPTO]; [LEVY, section 3][LEVY]

Let x be the established ordinary taxable income. Sections 6 and 7 give
the amount B before family and prescribed-period reductions:

- If x is at or below H, B is nil.
- If H < x <= U, B is the smaller of 2% of x and 10% of (x minus H).
- If x > U, B is 2% of x.

Use the statutory U, not an extrapolated algebraic crossing point. Apply
section 8 next and section 9 last. Do not reduce taxable income by an
exempt-day fraction or offset basic income tax against this levy.
[LEVY, sections 6-9][LEVY]

### Family reduction and allocation

Section 8 applies where the person was married on the last day of the year,
or has the specified child offset under Subdivision 61-A or sole-parent
notional offset under Subdivision 961-B. Registered and genuine domestic
couple relationships can count under section 251R(2)-(2A). Levy Act section
3(3) addresses living separately and apart and the death of the last spouse
during the year. Establish that statutory status and the complete dates;
do not equate the filing unit with a joint income-tax return. [MEDICARE];
[LEVY]; [OFFSETS, Subdivision 61-A][OFFSETS]; [DICT, Subdivision 961-B][DICT]

For a person married at year end, family income F is the sum of both
spouses' annual taxable incomes. Otherwise F is the relevant person's
taxable income. The family threshold T is **$47,238**, or **$61,623** for
a person actually entitled to the section 160AAAA rebate, plus **$4,338**
for each qualifying person under section 8(5). [LEVY, section 8(5)-(7)][LEVY]

A child is not automatically a qualifying threshold addition. Establish
section 961-5(1)(c), the relevant person's or spouse's Subdivision 961-A
notional entitlement, age/student status, residence or domicile, maintenance,
apportionment and adjusted-taxable-income conditions. For a person not
married at year end, section 8(6) also requires family tax benefit payable
for the child during at least part of the year. Sole-parent and invalid/carer
eligibility have their own complete rules. Those entitlement computations,
including the underlying benefit and ATI rules, remain held here unless
separately verified; an unknown qualifying-child count is not zero.
[LEVY]; [DICT, Subdivisions 961-A and 961-B][DICT]; [OFFSETS, Subdivision 61-A][OFFSETS]

For an established section 8 case:

1. If F <= T, the person's ordinary levy is nil.
2. If F > T, calculate the available reduction R as
   max(0, 0.02 × T minus 0.08 × (F minus T)). This is a subtraction from
   the post-section-7 levy, not a 10% levy on combined family income.
3. Where both spouses would owe levy before sections 8 and 9, section 8(3)
   allocates the relevant person's R in the proportion x/F. Otherwise a
   leviable person uses the full applicable R. Calculate each spouse's
   entitlement and threshold separately; SAPTO can make them different.
4. Apply section 8(4): where that allocated reduction exceeds the person's
   pre-section-8 levy, transfer the excess to reduce the spouse's levy.
   Reconcile both computations together and floor levy at nil. A spouse
   whose section 7 levy is already nil does not create another transferable
   reduction. Do not apply the full reduction independently to both spouses.

The statutory formula is an image in the official HTML; its alternative
text supplies the expression above. The plain-text extraction omits it.
The ATO family page's introductory individual-income screen must not become
an additional statutory prerequisite: its own Ashton example applies a
family reduction below the SAPTO phase-in limit. Sections 7 and 8 and that
worked example support the sequence above. [LEVY, section 8][LEVY]; [ATO-LEVY-FAMILY]

### Whole and part-year prescribed persons

Resolve section 251U's category, evidence, dates and dependant conditions
before counting any prescribed period. In particular, paragraph (1)(f)
requires the Health Minister's stated certificate concerning absence of
Medicare-benefit entitlement. A remote address, limited local services or
an assertion of no benefits is insufficient. Subsection (2) generally
requires every dependant to be prescribed, or to qualify but for that
subsection. [MEDICARE, sections 251R and 251U][MEDICARE]

Section 251R(3)-(6) addresses resident dependants, maintenance, student
notional entitlement and shared care. Subsections (6B)-(6D) can remove
specified dependants where the levy-payability conditions and, for (6D),
the family agreement are met. An agreement must meet the lodgement timing
and retention conditions in (6E)-(6H). Obtain the records and complete
applicable eligibility rules before accepting the period; a certificate
alone does not settle a dependant condition. [MEDICARE]

The half-period fallback in section 251U(3) applies only to categories
(1)(a), (b), (ca), (caa) and (cb) when its conditions are met. It does not
extend to (cc), non-residence, diplomatic status or the paragraph (f)
certificate. For disjoint fully prescribed periods f and eligible
half-treated periods h, count P = f + h/2. Preserve an exact half-day
fraction; do not invent a whole-day rounding rule. [MEDICARE]

A person prescribed for the whole year is exempt from ordinary levy under
section 251T. Otherwise section 9 reduces the amount L after section 8 to
L × (D minus P) / D, where D is the actual number of days in that income
year. Do not apply a second reduction to a levy already nil. This does not
resolve surcharge: sections 251V and 251VA reverse specified dependant and
half-period concessions for that separate calculation. [MEDICARE]; [LEVY]

### Precision and remaining levy branches

Retain exact fractions or sufficient decimal precision through section 7,
family allocation, excess transfer and the prescribed-period calculation.
TAA section 16B decreases an applicable assessed or penalty tax-related
liability to a multiple of 5 cents, with stated exclusions. Schedule 1
sections 90-1 and 255-1 and the assessment definition provide context;
section 16B is not permission to round every Medicare intermediate to
5 cents. The final assessment liability unit, processing precision and
rounding stage remain an engagement source condition here. The examples
below are unrounded components, not approved assessment amounts.
[TAA]; [TAA-SCHEDULE]; [RESIDENCE, section 6(1)][RESIDENCE]

The ordinary single-person and family/relationship-period surcharge
components follow below. Special surcharge income/benefit adjustments,
arrears and special superannuation adjustments remain unresolved.
Unknown cover does not mean no cover, and nil ordinary levy does not prove
nil surcharge. Do not use historical island guidance to override the
checked current charge and conditional exemption rules.

## Medicare surcharge: ordinary single adult

This section supports a 2026-27 component working paper for an adult who
is an Australian tax resident, unmarried and without surcharge dependants
throughout the income year. Establish those facts for every day before using
this branch. A spouse or dependant at any time routes to the family/period
section below, even if the person is single at year end. Registered
and genuine domestic relationships can count as marriage; living separately
and apart and a spouse's death have statutory consequences. A return label
of 'single' alone does not settle them. [MEDICARE, sections 251R/251V][MEDICARE];
[LEVY, sections 3/3A/8B][LEVY]; [MLS-FB, sections 5-8/12][MLS-FB]

The separate benefits charge extends to the external Territories in the
imported geographical Australia definition and uses the section 6(1)
residence definition. The territorial bridge above therefore also needs
verification for this charge; an island address alone settles neither
residence nor exemption. [MLS-FB, sections 3/9/10][MLS-FB]; [DICT, section
960-505][DICT]; [RESIDENCE, section 6(1)][RESIDENCE]

### Annual inputs and special-branch gates

Keep 3 amounts separate, with their evidence and reconciliation:

- **I:** annual income for surcharge purposes under section 995-1. For the
  selected ordinary case, with all other special adjustments established absent,
  this is taxable income plus reportable fringe benefits, reportable
  superannuation contributions and total net investment loss. It selects
  the annual threshold and rate, rather than the charge base.
- **C:** annual taxable income for the sections 8B-8D charge. Section 3(2A)
  disregards Schedule 2F subsection 271-105(1); do not simply copy a return's
  taxable-income label where a trust-distribution adjustment applies.
- **B:** annual reportable fringe benefits total, independently reconciled
  across employers under FBTAA section 135N. It has a separate charge under
  sections 10-16 of the fringe-benefits surcharge Act.

For these ordinary inputs, require non-negative amounts and an I worksheet
reconciling C + B + separately established reportable super (RSC) + total net
investment loss. Use the bounded RSC worksheet below for that subcomponent.
An unexplained difference is Needs Input. Unknown
classifications cannot be supplied as zero.

The statutory I definition adjusts taxable income for assessable FHSS
released amounts and the specified trust rule, adds the separately defined
superannuation and investment-loss amounts and retains a conditional
section 301-20 reduction. Reportable super is itself subject to the
statutory excess-concessional-contribution adjustment. Do not equate I, C,
B, gross pay, cash received or ordinary levy income. [DICT, section 995-1][DICT];
[LEVY, sections 3/8B][LEVY]; [MLS-FB, sections 3/10-12][MLS-FB]

This branch requires independently reconciled I, C and B. Independently
established DedSuper and ECC may enter the bounded RSC worksheet only when
their taxable-income effects are already reconciled in C. Unknown deduction
entitlement, cap, excess or reconciliation remains **Needs Input**. Foreign
employment/exempt foreign income, FHSS releases, trust-distribution
adjustments, arrears and special superannuation benefits still require
evidence that no further rule applies. Unknown or applicable unresolved
special items are **Needs Input** for this computation. The ATO's
foreign-employment qualification and its historical super lump-sum
qualification must not be silently omitted or imported into 2026-27 without
the operative law. This section does not calculate those branches.
[MLS-ATO]; [DICT]; [IT97-SUPER]

Obtain each employer's actual income statement/reporting reconciliation and
confirm the FBT year ending on 31 March within the income year. Section
135P's greater-than-$2,000 individual-benefits test is a reporting condition,
not a deduction from B; section 135Q supplies a separate special-employer
path. An employer's FBT exemption or an island address does not prove nil B.
Do not gross up a supplied taxable value with an assumed factor or replace
reported benefits with salary packaging deductions. Underlying valuation,
exclusion, gross-up-rate and reporting-precision questions require the
complete applicable rules before B is accepted. [FBT-REPORTING, sections
135N-Q][FBT-REPORTING]; [FBT-VALUES, sections 5E/5F][FBT-VALUES]

### Reconcile reportable superannuation contributions

For the corresponding income and financial year, independently establish:

- **RESC:** reportable employer superannuation contributions under TAA
  Schedule 1 section 16-182. Establish the employer or associate, fund or
  RSA, benefit, influence and exclusion conditions. Amounts assessable to
  the individual are excluded to that extent. The industrial instrument or
  fund rule exception addresses paragraph (1)(c), not paragraph (1)(d).
  Apply the expanded SGAA section 12 employer meaning with subsection
  12(11) disregarded. Disregard whether benefits are payable to a SIS
  dependant if the individual dies before or after entitlement. A gross
  deposit or SG label alone does not establish RESC. [TAA, Schedule 1
  section 16-182][TAA]
- **DedSuper:** the actual allowable Subdivision 290-C deduction, after all
  applicable conditions and limitations. For a claimed deduction, establish
  the contribution year,
  fund conditions, age and work conditions, excluded contribution types,
  valid timely notice, acknowledgment, variations and other denial or
  reduction provisions. The notice amount is an upper bound; a deposit,
  notice or acknowledgment alone does not establish the deduction.
  The ordinary personal-super worksheet below can establish DedSuper only
  within its stated branch, including the section 26-55 limit.
  [IT97-SUPER, sections 290-150 to 290-180][IT97-SUPER]; [CORE, section 26-55][CORE]
- **ECC:** final statutory excess concessional contributions for the
  corresponding financial year, after the applicable cap, carry-forward,
  contribution classification, defined benefit and Commissioner rules.
  Neither an assumed cap nor gross deposits establish ECC. Contributions
  for cap purposes have their own section 291-25 classification; they are
  not necessarily RESC + DedSuper. ECC can exceed that sum. Unknown or
  provisional inputs remain held. The ordinary cap worksheet below can
  establish this component when all its applicable prerequisites are met.
  [IT97-SUPER, Division 291][IT97-SUPER]

These names do not replace R for the ordinary Medicare reduction or D for
surcharge days. Calculate:

**RSC = max(0, RESC + DedSuper - ECC).**

Keep the input evidence, year correspondence and zero floor. Unknown
classifications or amounts, including an unproved zero, are **Needs Input**.
[DICT, section 995-1][DICT]

Section 291-15 separately includes ECC in assessable income and provides a
15% offset that cannot be refunded, transferred or carried forward. Use C
already reconciled with actual DedSuper and assessable ECC: do not deduct
DedSuper or include ECC again, subtract ECC from C, or treat the offset as a
deduction. The fictional pre-adjustment amount in the examples illustrates
those effects; it is not a replacement method for establishing taxable
income. Add RSC when reconciling I, without adding RSC itself to C or B.
A known RSC does not clear a missing C, B or other I adjustment.
[IT97-SUPER, section 291-15][IT97-SUPER]; [DICT]

This RSC worksheet takes established statutory inputs. The ordinary
2026-27 cap/excess worksheet below can supply ECC only after its own
applicable prerequisites are met. The personal-super worksheet below can
establish bounded DedSuper entitlement. Neither of these input worksheets
determines special-case ECC, complete offset ordering, release
instructions or a final assessment. Every other income, benefit,
relationship, cover, day and complete-output gate remains.
[IT97-SUPER]; [TAA]; [DICT]

### Ordinary 2026-27 concessional-cap and excess worksheet

This worksheet calculates the ordinary ECC subcomponent for 1 July 2026 to
30 June 2027. Independently establish **Q**, the total statutory concessional
contributions for that financial year under section 291-25, across relevant
funds. Q has its own contribution, complying-plan, provider-assessability,
exclusion, refund and allocation conditions; it is not gross deposits,
RESC + DedSuper or a notice amount. A supplied fund total does not settle
those conditions. [IT97-SUPER, section 291-25][IT97-SUPER]

Use this ordinary worksheet only after establishing that defined-benefit,
constitutionally protected fund, notional/transitional contribution and
Commissioner disregard or reallocation rules do not modify the computation.
Unknown applicability, an unresolved determination or a disputed financial
year is **Needs Input**, even when a gross contribution total is known.
This worksheet does not calculate those special branches. [IT97-SUPER,
sections 291-165/291-370/291-465][IT97-SUPER]

For 2026-27 the general cap **G is $32,500**, as expressly published by the
ATO from 1 July 2026. The statutory base is $25,000 for 2017-18, indexed
under section 960-285, with rounding down to a $2,500 multiple. Keep the
period-labelled source with the working paper; do not import another year's
cap. [CC-CAP-ATO]; [IT97-SUPER, section 291-20(2)][IT97-SUPER];
[DICT, sections 960-265/960-285][DICT]

1. Calculate the ordinary excess before carry-forward, **X = max(0, Q - G)**.
   If Q is at or below G, **ECC is nil** and no unused prior cap is applied.
   Prior balance and unused-cap evidence are not needed to establish that
   narrow result. It does not establish either ledger or any other input.
2. If Q exceeds G but all 5 eligible previous-year unused amounts are
   independently proved nil, no carry-forward can apply: **ECC = X**.
   The prior balance is not needed for that narrow result. Otherwise,
   establish the statutory total superannuation balance
   immediately before the financial year, at 30 June 2026. If it is
   **$500,000 or more**, carry-forward is unavailable: no prior cap is applied
   and **ECC = X**. An unused-cap ledger is unnecessary for this result.
   If the required balance is unknown, hold ECC; do not assume ineligibility.
3. If Q exceeds G and the proved balance is **less than $500,000**, establish
   the previously unapplied unused-cap amounts for each of **2021-22,
   2022-23, 2023-24, 2024-25 and 2025-26**. Reconcile the original yearly
   entitlement and earlier use; an unexplained or unproved zero is not a
   complete ledger. Unused 2020-21 amounts have expired for this year.
   Current-year or future amounts are not part of the previous 5 years.
4. Apply eligible amounts from the **earliest year first**, stopping when X
   is covered or the eligible ledger is exhausted. Do not apply more than X.
   Record the amount applied from each year and its unapplied remainder.
   If their applied total is A, the effective cap is **G + A** and
   **ECC = max(0, Q - (G + A))**. A missing required ledger holds this step;
   gross contributions and an assumed unused balance cannot replace it.

These steps apply section 291-20(1), (3)-(7). Ledger remainders are recorded
before expiry; they are not a promise of availability next year. In
particular, a remaining 2021-22 amount is outside the previous 5 years for
2027-28. Future balance and eligibility conditions also need their own
evidence. [IT97-SUPER, section 291-20][IT97-SUPER]; [CC-CAP-ATO]

Keep Q, G, the required balance evidence, eligible-year ledger, per-year
application, effective cap and ECC in the working paper. Only a completed
ordinary calculation with these applicable prerequisites can supply ECC to
the RSC worksheet. Independently establish DedSuper and reconcile the actual
assessable excess and deduction in C exactly once. An ECC result does not
establish RESC, personal-deduction entitlement, B, another I adjustment,
complete offset ordering, release procedure or final assessment. [IT97-SUPER,
sections 290-150/291-15/291-20][IT97-SUPER]; [DICT]


### Ordinary personal-super deduction: validate a chosen claim

For 1 July 2026 to 30 June 2027, this worksheet can establish an ordinary
personal deduction, **DedSuper**, for a chosen claim that passes every gate
below. It covers direct personal cash or electronic contributions to one
complying superannuation fund, for the individual's own benefits. It does
not cover RSAs, employer or spouse contributions, in-specie contributions,
rollovers, foreign-super amounts, KiwiSaver transfers or other special
transfers. Section 290-10 supplies no alternative general deduction for a
failed contribution. [IT97-SUPER, sections 290-5/290-10/290-150/312-15][IT97-SUPER]

#### Establish entitlement and the original notice

1. Record the contribution amount **P**, fund identity, receipt evidence and
   contribution year. Cash must actually reach the provider; an electronic
   payment must be credited to its account. Initiating a transfer before
   30 June does not establish that year's contribution. Keep the receipt
   date, not only the payment instruction. [TR-CONTRIB, paragraphs 12-13][TR-CONTRIB]
2. Establish that the individual was **at least 18 at income-year end** and
   **under 67 when contributing**. An individual turning 67 later in that
   year is not excluded from this branch for an earlier contribution.
   Under-18 and contributions from age 67 require their separate statutory
   conditions and remain held here. [IT97-SUPER, section 290-165][IT97-SUPER]
3. Establish actual complying status for the **fund's income year** in which
   it received the contribution. Resolve all section 290-155 exclusions:
   the Commonwealth public-sector/defined-benefit exclusion; a fund that
   would not include the contribution under section 295-190, disregarding
   Subdivision 295-D; and both prescribed-fund/contribution elections.
   A public complying-fund record or reasonable belief alone is insufficient.
   [IT97-SUPER, section 290-155][IT97-SUPER]
4. For regulation 290-155.01, check whether **any member** has a defined
   benefit interest and the trustee made the qualifying fund-wide election.
   The taxpayer's accumulation interest does not clear that gate. Separately
   resolve regulation 290-155.05 for contributions to a defined benefit
   interest. Check each applicable election's approved notification,
   making/revocation dates before the start of the fund's relevant income
   year and qualifying old-regulation elections saved by section 1000-1.04.
   Unknown election facts hold entitlement; absence from a public list is
   not proof of no election. [SUPER-REGS, sections 290-155.01/290-155.05/1000-1.04][SUPER-REGS]
5. Establish that no section 290-150(4) CGT retirement-exemption attribution
   applies. Its under-55 tests refer respectively to immediately before the
   individual's exemption choice or the company/trust contribution; they
   are not the worksheet's ordinary age gate. Hold all such cases here.
   Prove that P is not a downsizer, notified FHSS re-contribution or COVID-19
   re-contribution under sections 290-167 to 290-169. Resolve any other
   applicable denial or reduction provision before continuing.
   [IT97-SUPER, sections 290-150/290-167/290-168/290-169][IT97-SUPER]
6. Obtain the original **approved-form** notice for this contribution and
   its amount **N**. Verify required information and actual delivery to the
   trustee. For this branch there is no earlier overlapping notice, notice
   variation, attempted revocation or additional notice. The notice alone
   does not prove entitlement. [IT97-SUPER, sections 290-170/290-175/290-180][IT97-SUPER]; [SUPER-NOTICE]
7. Establish the statutory endpoint: if the contribution-year return was
   lodged before the end of the next income year, give the notice **before
   the end of that lodgment day**; otherwise give it **before the end of the
   next income year**. For an ordinary 30 June 2027 year end with no earlier
   lodgment, that endpoint is the end of **30 June 2028**. Preserve the
   actual dates and sequence. The ATO instructs taxpayers to give notice
   and receive acknowledgment before claiming; an already-claimed return
   without these facts needs separate correction work and is held here.
   [IT97-SUPER, section 290-170(1)][IT97-SUPER]; [SUPER-NOTICE]
8. At notice delivery, prove continued membership, the fund still holding
   the whole contribution and no income stream based wholly or partly on
   it. Also recheck section 290-155. This branch holds every withdrawal,
   rollover, release, transfer, successor fund, changed interest and
   contributions-splitting application. Statutory splitting invalidity
   concerns a prior application that has **not been rejected**; a rejected
   application still needs separate work outside this branch.
   [IT97-SUPER, section 290-170(2)/(5)][IT97-SUPER]; [TR-CONTRIB, paragraphs 67-72][TR-CONTRIB]; [SUPER-REGS, section 290-170.01][SUPER-REGS]
9. Obtain the fund's **actual acknowledgment** before accepting the claim.
   A fund may refuse acknowledgment if the end-of-receipt-day interest value
   is below the tax arising on the contribution; a sent notice or assumed
   acknowledgment cannot pass this gate. Hold returned/refunded contributions
   and direct or indirect returns of deductible contributions or earnings:
   section 290-100 can separately include a non-superannuation-benefit return
   in assessable income. [IT97-SUPER, sections 290-100/290-170(1)/(4)][IT97-SUPER]; [SUPER-NOTICE]

#### Check the chosen amount and reconcile it

Record a taxpayer-chosen whole-dollar claim **S**. In this first branch,
**N must equal S**: a notice greater than the chosen claim needs separate
fund-assessability and contribution-classification work. A notice exceeding
an allowance is not automatically varied or withdrawn by this worksheet.
[IT97-SUPER, sections 290-175/290-180/295-190/292-90][IT97-SUPER]

Establish **AI**, assessable income for the contribution year, and **OD**,
allowable deductions outside the section 26-55 specified pool. Independently
prove that the other specified-pool deductions, tax losses and farm management
deposit deductions are nil. Mixed pools, losses and FMDs remain held.
Under that bounded construction, calculate **H = max(0, AI - OD)**.
Paragraph 26-55(2)(b) was expressly repealed in 1999: do not restore it or
subtract the specified pool from itself and halve H. [CORE, section 26-55][CORE];
[SUPER-REPEAL, Schedule 3 items 1/7][SUPER-REPEAL]; [SUPER-REPEAL-EM]

AI must identify any assessable **ECC** already included. Independently
classify statutory **Q** for this same chosen notice/claim and establish
ordinary ECC under the preceding worksheet, or separately resolve every
applicable special rule. A fund's assessable contribution and Q do not
follow automatically from RESC + S. Unknown or circular AI/Q/ECC inputs hold
the claim. Changing S or the notice requires rechecking fund assessability,
Q, ECC and AI; do not reuse inconsistent amounts or optimise the claim by
an assumed cap. [IT97-SUPER, sections 291-15/291-25/295-190][IT97-SUPER]

With all entitlement gates met, calculate the whole-dollar bound
**W = floor(min(P, N, H))** and accept **DedSuper = S** only when S is a
nonnegative whole dollar, **S = N** and **S <= W**, with every other
applicable limit established. A failed bound holds the proposed deduction;
it does not silently replace S or change a valid notice. Retain cents in P,
AI, OD, H, Q and ECC. Whole-dollar claiming is the ATO notice/claim instruction,
not a rule to round an allowance upwards or a final-assessment rounding
rule. Residual contribution cents remain subject to their separately
established non-concessional classification and cap. [SUPER-NOTICE];
[IT97-SUPER, sections 290-150/290-175][IT97-SUPER]; [CORE]

The concessional cap is **not automatically a deduction ceiling**. A claim
above it can satisfy these deduction gates whilst producing ECC. Keep the
cap, carry-forward, contribution classification and deduction workings
separate. After accepting the deduction, reconcile **C = max(0, AI - OD - DedSuper)**
only for this established ordinary no-other-pool/no-loss fixture; AI already
contains any assessable ECC. For real C, independently reconcile every
remaining taxable-income item. Feed DedSuper and ECC into RSC exactly once,
then reconcile I with its remaining adjustments. Unknown RESC, B or another
I item still holds the downstream result. No offset, release, final return,
filing or payment decision is supplied here. [CORE, sections 4-15/26-55][CORE]; [IT97-SUPER, sections 290-150/291-15][IT97-SUPER]; [DICT]

### Annual single thresholds and charge periods

The ATO expressly labels the following thresholds for **2026-27**. The
statutory comparisons are 'exceeds' and 'does not exceed'; preserve exact
intermediates and the applicable assessment precision rather than assuming
that an administrative whole-dollar range fills every precision question.
[MLS-ATO]; [PHI, sections 22-30/22-35/22-45][PHI]

| Annual I for this full-year single/no-dependant branch | Surcharge rate r |
|---|---|
| I no more than $105,000 | 0% |
| I above $105,000 and no more than $123,000 | 1% |
| I above $123,000 and no more than $164,000 | 1.25% |
| I above $164,000 | 1.5% |

This is a flat rate on the relevant charge bases once the annual threshold
is exceeded, not a marginal charge only on the excess. Sections 3A and 6
modify the PHI family test for surcharge. The singles table here assumes no
spouse or surcharge dependant throughout the year; use the family/period
section for other established relationship/dependant histories. [LEVY, sections
3A/8B][LEVY]; [MLS-FB, sections 6/12][MLS-FB]; [PHI, section 22-30][PHI]

For each day, establish both qualifying private patient hospital cover and
prescribed-person status. Qualifying cover requires a complying policy
covering hospital treatment, with the applicable excess no more than $750
for a policy insuring only one person or $1,500 otherwise in any 12 month
period. Compliance includes the PHI requirements and applicable Rules; this
guide does not certify an insurer's product. Confirm the actual insurer,
policy, insured people, excess terms, start/end dates and suspensions.
Extras alone, travel insurance and an overseas fund do not establish
qualifying hospital cover. [LEVY, section 3(5)][LEVY]; [MLS-FB, section 4][MLS-FB];
[PHI, sections 45-1/63-10/69-1/69-5/121-5][PHI]; [MLS-COVER]

Prescribed-person status requires the actual section 251U conditions and
applicable evidence, including any required certificate and dependant
condition. Sections 251V/251VA and the fringe-benefits Act's sections 5/8
reverse specified ordinary-levy dependant and half-period concessions.
Do not copy the ordinary levy's full/half-day count into the surcharge.
An unproved exemption, unknown cover or missing date is Needs Input.
[MEDICARE, sections 251R/251U/251V/251VA][MEDICARE]; [MLS-FB, sections 5/8][MLS-FB]

For this branch let D be the number of distinct days on which the person is
both without qualifying cover and not a surcharge prescribed person.
Build the dated day sets and their intersection; overlapping cover and
prescribed days are excluded once, rather than deducted twice. The selected
2026-27 year has 365 days. Use the same independently established annual
rate and charge bases for the statutory day fractions:

- Taxable-income surcharge component: **C × r × D / 365**.
- Reportable-benefits surcharge component: **B × r × D / 365**.
- Combined unrounded surcharge component: their sum, kept separate from
  ordinary levy, income tax, offsets, private health rebate and withholding.

At the base tier, or with D = 0 after all conditions are proved, these
selected surcharge components are nil. For D = 365 the full annual amounts
apply. Do not allocate C or B to the dates salary or benefits happened to be
received. Preserve each exact fraction before the still-unresolved final
assessment rounding stage. The separate charging provisions, including
their formula image alternatives, support these fractions. [LEVY, section
8B][LEVY]; [MLS-FB, sections 10-12][MLS-FB]

## Medicare surcharge: family and relationship periods

Use this component for a 2026-27 full-year resident adult with independently
established ordinary I/C/B as above, an established relationship/dependant
history and proved hospital-cover and prescribed-person facts. It supports
unmarried dependant periods, marriage throughout the year and marriage for
part of the year, including an established separation/reunion timeline with
one identified spouse. The supported surviving-spouse branch below retains
whole-year marriage only with its complete facts. It does not calculate the
special income/base or benefit-valuation branches held above, a deceased person's return, competing
or successive spouse cases or unresolved changing child-count thresholds.
Those cases require the missing rules and evidence before computation.

### Establish relationships, dependants and annual classification

Record the actual dates of legal marriage, prescribed registered relationship,
genuine domestic relationship and living separately and apart. A temporary
absence or different address alone does not prove separation. The competing
relationship provisions can displace a legal/registered relationship. If the
last spouse dies while they are married, MLA section 3(3A) and the benefits
Act section 7(3) continue marriage through 30 June. Do not create unmarried
post-death days or substitute MLA's general last-day death deeming for the
benefits Act definition used by the annual PHI test. The ordinary survivor
branch below applies only with its complete timeline, statutory cover and
input facts. Other death or competing/successive cases remain Needs Input.
[MEDICARE, section 251R(2)/(2A)][MEDICARE];
[LEVY, section 3(3)/(3A)][LEVY]; [MLS-FB, section 7][MLS-FB]; [MLS-FAMILY]

A surcharge dependant requires Australian residence, maintenance and the
specified relationship: spouse, child under 21 or child aged 21 to 24 receiving
full-time education at a school, college or university. Establish the statutory
child relationship; an insurance policy's dependent-person label is not enough.
Cohabitation creates a rebuttable maintenance rule. For surcharge, disregard
ordinary-levy subsections 251R(4), (5), (6B), (6C) and (6D): do not remove a
student for lack of the ordinary notional offset, prorate shared care by the
ordinary FTB rule or import an ordinary family-agreement removal. A working
spouse can still be maintained. [MEDICARE, sections 251R/251V][MEDICARE];
[MLS-FB, section 5][MLS-FB]; [DICT, sections 995-1/960-255][DICT]; [MLS-FAMILY]

First select the **annual** tier 2/tier 3 classification, separately from the
charging tests below:

1. If married on 30 June under the benefits Act definition, use the family
   table and add that spouse's full annual I to own annual I. Do not allocate
   the spouse's income only to married days.
2. Otherwise, if a non-spouse surcharge dependant existed on any day, use the
   family table with own annual I. This is the surcharge modification to PHI
   section 22-30(1)(b), not its unmodified private-health-rebate test.
3. Otherwise use the singles table with own annual I, even if there were
   married days earlier in the year. [LEVY, section 3A][LEVY]; [MLS-FB, section
   6][MLS-FB]; [PHI, section 22-30][PHI]

For the established constant number n of qualifying dependant children,
**F1 = $210,000 + $1,500 × max(n - 1, 0)**, **F2 = $246,000 + the same
increment** and **F3 = $328,000 + the same increment**. Thus 0 or 1 child
leaves the thresholds unchanged; 2 gives $211,500/$247,500/$329,500 and 3
gives $213,000/$249,000/$331,000. A proved timeline with no more than one
identified qualifying child also leaves the thresholds unchanged. Where
changing counts involving 2 or more children affect the increment, hold the
threshold until its temporal application is resolved; do not invent a maximum,
year-end or daily-prorated counting rule. These are surcharge dependants, not
ordinary levy qualifying children or everyone on the policy. [PHI, section
22-40][PHI]; [MLS-ATO]

Let A be the annual classification income from steps 1-3. Use F2/F3 if the
family table applies, or $123,000/$164,000 if the singles table applies.
The **conditional charging rate r is 1.5% if A exceeds the applicable tier 3
threshold, 1.25% if A exceeds tier 2 but not tier 3, otherwise 1%**. The
last case includes annual income below the family tier 1 threshold. It does
not establish a charge by itself: each period must pass its own income test.
In particular, do not apply a global 0% merely because A is below F1; a
child-free unmarried period can still pass the singles charging test.
[LEVY, sections 8B(2)-(4)/8C(3)-(5)/8D(3)-(4B)][LEVY]; [MLS-FB, sections
12-16][MLS-FB]; [PHI, section 22-30][PHI]

### Apply each period's income, cover and prescribed-person tests

Partition the year into disjoint dated sets. For each set use the actual
relationship/dependant classification and the following annual-income screen.
All comparisons are strict: equality fails that screen.

| Period classification | Annual-income screen before any component can be charged |
|---|---|
| Unmarried, no surcharge dependants: MLA 8B / benefits Act 12 | Own I > $105,000. |
| Unmarried, at least one surcharge dependant: MLA 8C / benefits Act 13 | Own I > own F1. |
| Married, with marriage throughout the entire income year: MLA 8D(3)/(4)(a) / benefits Act 15/16(2) | Combined spouses' annual I > own F1 **and** own annual I > $28,011. |
| Married for only part of the income year: MLA 8D(4)(b) / benefits Act 16(3) | Own annual I > own F1; combined income alone does not pass this test. |

A whole-year marriage with only some chargeable cover days still uses the
whole-year-marriage screen. The $28,011 screen is own **I**, not C, ordinary
levy taxable income or a SAPTO threshold. Act 58's amendments apply for
2025-26 and later assessments. Spouse-income tests have specific section 98
trust-share inclusions and trust-rule modifications; do not compute an actual
trust case from these ordinary inputs. [LEVY, sections 8B-8D][LEVY]; [MLS-FB,
sections 12-16][MLS-FB]; [LEVY-AMEND, Schedule 5 items 1/10/11/14][LEVY-AMEND]

For unmarried/no-dependant days, cover fails when the taxpayer is uncovered.
For the dependant and married branches, it fails when the taxpayer **or at
least one relevant dependant** is uncovered. Form the union of those uncovered
day sets, rather than adding overlaps or checking only the taxpayer's policy.
For this cover test only, disregard a dependant who is prescribed or would
be prescribed apart from section 251U(2). That exclusion does not remove the
dependant from annual family classification or the qualifying-child count.
Prove each person's status and dates, including residence, maintenance and
any certificate/underlying entitlement. Unknown status is Needs Input.
[LEVY, sections 8B(1)/8C(1)/8D(1)][LEVY]; [MLS-FB, sections 12-14][MLS-FB]

The taxpayer must also be non-prescribed under the surcharge rules. There
is a limited further cover deeming: where ITAA36 section 251VA removes an
ordinary half-period prescribed concession, MLA sections 8C(2)/8D(2) deem
that taxpayer covered **only for the family cover test**. The benefits Act
sections 13(2)(a)/14(2)(a) expressly list the corresponding section 251U(1)(a),
(b), (ca), (caa) and (cb) categories, apart from the dependant condition in
251U(2). This does not create a global prescribed exemption: an uncovered
non-excluded dependant can still cause chargeable days. Do not extend the
listed cover deeming to every exemption category or copy the ordinary half-day
concession. Actual entitlement must be independently established; the category
name alone is insufficient. [MEDICARE, sections 251U/251VA][MEDICARE]; [LEVY,
sections 8C(2)/8D(2)][LEVY]; [MLS-FB, sections 8/13(2)/14(2)][MLS-FB]

For each branch j, retain separate supported day counts D-C-j and D-B-j for
the taxable-income and benefits charges after all relationship, dependant,
cover and prescribed-person conditions. A failed income screen contributes
zero. Where it passes, compute **C × r × D-C-j / 365** and **B × r × D-B-j /
365**. Sum each charge's disjoint branch components, then report both and
their combined unrounded component separately from ordinary levy and other
taxes/offsets. Reconcile both statutory day ledgers before using identical
counts. Do not double count overlapping uninsured people or assign annual
income to receipt dates. Preserve exact fractions and the final assessment
rounding hold. [LEVY, sections 8B-8D][LEVY]; [MLS-FB, sections 11-16][MLS-FB]

### Surviving spouse: established whole-year marriage and own uncovered status

This ordinary branch applies only when all of the following are independently
established for the survivor:

- The same statutory marriage existed on 1 July and continued until the spouse
  died whilst they were married. They were not living separately and apart,
  and there is no competing relationship or later spouse in the income year.
- The full-year resident adult, territorial and ordinary I/C/B gates above
  hold. Own annual I/C/B and the deceased spouse's actual annual I are proved.
  Do not annualise the deceased's income or replace an unknown amount with nil.
- The survivor is nonprescribed and uncovered under **both statutory cover
  tests on every day**. Neither section 251VA/MLA 8D(2) nor benefits Act
  14(2)(a) deems the survivor covered. Physical lack of a policy alone is
  insufficient. Ordinary half-period status is not proof of this condition.
- The qualifying-child threshold basis is proved throughout: a constant
  qualifying count, or a dated count proved never to exceed 1. Each child's
  relationship, residence, maintenance and age/study qualification must remain
  proved after death. Do not infer continuing qualification solely because
  the child was the deceased spouse's child. Changing counts involving 2 or
  more remain held.

MLA 3(3A) and benefits Act 7(3) continue that existing marriage from the death
through 30 June. The survivor is therefore married throughout the year and
on 30 June for the PHI test. Use the family table, own annual I plus the
deceased spouse's actual annual I, and the supported child thresholds above.
Do not create a single-person period or end the survivor's chargeable period
on the spouse's death. [LEVY, sections 3(2)/(3A)/8D][LEVY]; [MLS-FB, sections
5/7(3)/14-16][MLS-FB]; [PHI, sections 22-30/22-40][PHI]

The survivor's own statutory uncovered status satisfies the cover condition
throughout. These facts do not require an assumption about the deceased's
post-death status as a cover-test dependant. There are 365 potential days
before income screening. Apply both strict whole-year-marriage screens:
**combined annual I > own F1 and own annual I > $28,011**. If either fails,
record **D-C = D-B = 0** and both selected components are nil. If both pass,
record **D-C = D-B = 365** and compute C × r and B × r separately, using the
annual conditional rate above. Retain exact amounts and the final assessment
rounding hold. [LEVY, section 8D(1)-(4B)][LEVY]; [MLS-FB, sections 14/15][MLS-FB]

The ATO day instructions for **2025-26** corroborate whole-year spouse
treatment where there was a spouse on 1 July and no replacement spouse.
Their historical thresholds do not supply the 2026-27 amounts here; the
current Acts and expressly labelled 2026-27 table do. This is a statutory
application, not an ATO worked death example or a deceased person's return.
[MLS-DEATH-DAYS]; [LEVY]; [MLS-FB]; [MLS-ATO]

If the marriage started later, separation preceded death, a later/competing
spouse exists or the survivor's statutory cover status is unknown or covered,
this shortcut cannot establish the whole-year charge. Obtain the complete
relationship, dependant, cover and income evidence and separately supported
rules; do not choose a higher-tax default or assume nil. The deceased's
return, special adjustments and final assessment remain outside this branch.

## Intake, patterns, defaults and refusals

Confirm the person's legal capacity, year and accounting period; residence
history and evidence under each relevant test; treaty/temporary-resident
questions; income categories, sources and derivation; complete deductions
and losses; special-rate components; all offsets; withholding and prepayments;
year-end family status, both spouses' annual taxable incomes and separate
surcharge I amounts, actual marriage/separation and dependant timelines,
qualifying-child count/threshold worksheet, including post-death qualification;
for a survivor, marriage on 1 July through death, no later/competing spouse,
actual deceased spouse annual I and proof that no taxpayer cover deeming
applies to the survivor; separately
verified SAPTO/qualifying-child entitlements, dependant maintenance, Medicare
entitlement/certificate and full/half prescribed and cover periods;
separate surcharge I/C/B worksheets, every employer's reportable-benefits
reconciliation, RESC classification, actual allowable DedSuper (receipt, age,
fund-income-year status, both prescribed elections and saved elections, excluded
contribution types, original approved notice, delivery, acknowledgment, chosen
claim and precise single-pool headroom), final ECC,
RSC/C year correspondence, ordinary statutory Q and any required prior
balance/eligible unused-year ledger, investment-loss classifications, actual
hospital policy/excess/suspension records, each relevant dependant's status and
distinct surcharge day sets for both charges, with each income screen;
qualifying labour-income/withholding categories, allowable reducing expenses,
asset use and pool history, usual zone residence dates, prior zone claims,
remote area allowances and overlapping service; foreign currency records;
and the actual filing/payment calendar.

| Observed item or missing fact | Required classification or default |
|---|---|
| Employer pay record with gross salary and withholding category | Verify section 25-130(4), assessability, period and residence; a net deposit alone cannot establish qualifying labour income. |
| Supplier invoice, travel diary, insurance premium or membership payment | Prove deductibility, evidence, private-use apportionment and the correct reducing branch or exception; do not classify by payee alone. |
| Employer deposit, interest, rent, dividend or business receipt | An intake clue only. Reconcile gross amounts, legal character and inclusion with primary records. |
| ATO payment or refund | Reconcile the assessment/account; do not treat the bank label as income, a deduction or proof of an exempt levy. |
| Island-to-mainland move | Establish tax residence continuously; do not automatically prorate the threshold. |
| Unknown residence, income source or special-rate status | Needs Input; no rate table selected. |
| Unknown labour-income category, reducing expense, zone residence, allowance, offset or levy condition | Needs Input; hold that component rather than assume entitlement or nil. |
| Unknown surcharge I/C/B, special adjustment, relationship/dependant history, policy or day set | Needs Input; no assumed nil income, cover or exemption and no annual-tier/charge-base shortcut. |
| Missing withholding, credit or due date | Hold the balance and calendar. No refund or payment instruction. |
| Missing exchange rate or rounding rule | Retain original amounts and hold the affected final number. |

| Code | Trigger | Verbatim output message |
|---|---|---|
| R-CC-IT-01 | Unresolved residence, treaty, temporary-resident or part-year facts | "Cocos (Keeling) Islands tax residence and period conditions are unresolved. No personal-rate or income-scope determination can be delivered until a qualified reviewer resolves them." |
| R-CC-IT-02 | Special-rate income, a trustee, prescribed minor or unresolved Medicare exemption | "This case needs rules beyond the selected ordinary individual reference. Hold the affected computation and obtain the complete applicable sources and professional review." |
| R-CC-IT-03 | A required income-tax slot, source, record or runtime capability is absent | "The country income-tax companion is incomplete for this result. Do not deliver a final liability, refund, filing calendar or payment instruction until the missing requirements are supplied." |

The reviewer attention threshold for a proposed tax component is **AUD 0**:
every non-zero component and adjustment requires review. Flag residence,
treaty, exemption, transition, source-version and missing-slot issues even
when their cash effect is unknown or zero. There is no factual default that
converts missing evidence into a tax position.

## Fictional component calculations

These are stipulated arithmetic and classification cases, not complete
employee, self-employed or mixed-income returns. All ordinary-rate examples
use 2026-27, with taxable income already established under all applicable
rules and no special-rate component. [RATES]; [OFFSETS]; [LEVY]

| Stipulated facts | Component result and limit |
|---|---|
| Full-year adult resident; ordinary taxable income $18,200 | Basic income tax is nil. This does not decide deductions, all credits, Medicare or filing. |
| Same ordinary scope; $45,000 | Basic income tax: ($45,000 − $18,200) × 15% = **$4,020**. |
| Same ordinary scope; $60,000; ordinary LITO eligibility confirmed | Basic tax **$8,520**; LITO **$100**; those 2 components leave **$8,420** before other offsets, levies and credits. |
| Same ordinary resident scope; $200,000 | $51,370 + ($10,000 × 45%) = **$55,870** basic tax. |
| Whole-year foreign resident; ordinary Australian taxable income $60,000; no special branch | $60,000 × 30% = **$18,000** basic tax. No LITO: the residence condition fails. This does not decide treaty or source facts. |
| Same foreign-resident ordinary scope; $200,000 | $60,850 + ($10,000 × 45%) = **$65,350** basic tax. |
| Qualifying section 20(1) period from January through June; all exceptions checked | Six months: $13,464 + ($4,736 × 6 / 12) = **$15,832** threshold. This is not a determination of income inclusion or final tax. |
| Eligible ordinary adult at $40,000 | LITO: $700 − ($2,500 × 5%) = **$575**, subject to available tax and ordering. |
| Ordinary levy applies for the whole year without reduction or base adjustment; taxable income $60,000 | $60,000 × 2% = **$1,200** ordinary levy only. Those stipulated conditions must be proved in an actual case; surcharge remains separate. |
| Continuing Australian resident moves from Cocos (Keeling) Islands to Perth in January | The move alone does not establish a section 18 part-year residency period. Keep the residence question separate from location. |
| Island resident asserts no Medicare services were used, without exemption evidence | Needs Input. Do not convert service usage into prescribed-person status. |
| Only net salary deposits are available | Needs Input. Gross income, withholding, deductions and the rest of the return remain unresolved. |

### Deduction and zone boundary cases

These additional cases stipulate each stated legal condition and evidence.
They test selected components only, not a complete return. The deduction
cases use section 25-130 for 2026-27; actual deductions are already found
allowable under their governing rules. [CORE]; [REFORM]; [RESIDENCE];
[ATO-ZONES]; [ATO-ZONE]

| Stipulated facts | Component result and limit |
|---|---|
| Eligible resident; assessable labour income $60,000; no reducing deduction | Standard deduction **$1,000**. It reduces income, not tax by that amount. |
| Same scope; $320 of branch (c) deductions | Standard deduction: $1,000 − $320 = **$680**. Together these deductions total **$1,000**. |
| Same scope; $1,800 of reducing deductions | Standard deduction **nil**; the allowable $1,800 is not capped at $1,000 by section 25-130. |
| Eligible resident; assessable labour income $600; $200 of reducing deductions | Standard deduction: $600 − $200 = **$400**. Do not use a $1,000 starting cap. |
| Eligible resident; qualifying labour income $60,000; allowable income-protection premium $400 and professional membership $250, both solely within the branch (c) exceptions; no other reducing deductions | Standard deduction **$1,000**; together with those separately allowable deductions, the selected total is **$1,650**. The exceptions alone cannot prove either actual deduction. |
| Eligible resident; qualifying labour income $60,000; allowable section 25-125 deduction $100 and no other reducing deduction | Standard deduction **$900**. Do not disregard branch (g). |
| Eligible resident; qualifying labour income $60,000; allowable investment-interest deduction $200, wholly unrelated to labour income and outside every reducing branch | Standard deduction remains **$1,000**. The separate investment deduction does not become a labour expense. |
| Resident has only business receipts; no amount meets section 25-130(4) | No standard deduction under section 25-130. Other business deductions remain a separate question. |
| Whole-year foreign resident receives Australian employment income | No section 25-130 deduction: its resident-at-any-time condition fails. |
| Qualifying assessable employee payment required withholding, but the payer withheld nothing | Actual non-withholding alone does not remove the payment from the statutory labour-income definition. Prove the category and all other facts. |
| A claim relates to 2025-26 | Do not apply the new standard deduction or the 2026-27 repeal merely because the return is prepared later. |
| Qualifying person; usual residence throughout 2026-27 in Cocos (Keeling) Islands; no relevant rebate amount, prescribed allowance or service interaction; sufficient available basic tax | Selected special-area zone component **$1,173**. The island address alone would not prove these conditions. |
| Same zone scope; prescribed allowance $200 and no relevant rebate amount | Selected zone component: $1,173 − $200 = **$973**, subject to available basic tax. |
| Usual residence in the listed special area for 183 days in the ordinary 365-day year; remaining conditions confirmed | Section 79A(3B)(a)'s more-than-half test is met. |
| Only 182 days of usual zone residence; prior-year and other branch facts unknown | Paragraph (a) is not met; hold entitlement whilst checking the other statutory branches. Do not silently deny or approve the offset. |
| Island workdays total 200, but usual residence is Perth outside the zones | Workdays alone do not satisfy the usual-residence test. |
| Asset already allocated to a low-value pool for 2025-26 | Act 49 item 17(2) preserves that earlier allocation from the new item 8 restriction. It does not settle other pool rules. |
| Salary-packaged benefit provided in the FBT year starting 1 April 2026 | Do not apply Schedule 4 Part 2 merely because the individual income year is 2026-27; Part 2 starts with FBT years from 1 April 2027. |

### Ordinary Medicare component boundaries

These fictional cases use the checked statutory thresholds and the ordinary
2026-27 year of 365 days. Unless stated otherwise, the adult is resident,
not entitled to SAPTO, has no qualifying children or prescribed days and
has no arrears or special adjustments. Taxable income and every stated
eligibility fact are established. Results precede final assessment rounding,
offsets, surcharge and any return balance. [LEVY]; [MEDICARE]; [LEVY-AMEND]

| Established facts | Unrounded ordinary component or required hold |
|---|---|
| Single; x = $28,011 | Nil under section 7(1). |
| Single; x = $28,012 | 10% × $1 = **$0.10**. |
| Single; x = $35,013 | min($700.26, $700.20) = **$700.20**. |
| Single; x = $35,014 | Above the statutory phase-in limit: 2% × $35,014 = **$700.28**. |
| Married at year end; taxable incomes $40,000 and $15,000 | F = $55,000; R = $944.76 minus $620.96 = $323.80. Components **$476.20 and nil**. The lower earner has no section 7 levy and creates no second reduction. |
| Married; taxable incomes $40,000 and $10,000 | R = $723.80; components **$76.20 and nil**. |
| Married; taxable incomes $40,000 and $18,000 | R = $83.80; components **$716.20 and nil**. |
| Married; taxable incomes $30,000 and $28,012; both have positive section 7 levy | B amounts $198.90 and $0.10; F = $58,012; R = $82.84. Allocate under section 8(3), then transfer the low earner's excess under (4). Components **$116.16 and nil**. Preserve exact fractions during allocation. |
| Married; taxable incomes $30,000 and $17,238 | F equals $47,238: both ordinary components **nil** under section 8(1). |
| Married; taxable incomes $40,000 and $11,000; one child separately established to qualify under section 8(5) | T = $51,576 and F = $51,000: ordinary component **nil**. An unverified child entitlement instead requires Needs Input. |
| Section 160AAAA entitlement separately established; taxable income $49,700; year-end spouse taxable income $21,700; no qualifying children | B = $543.20; T = $61,623; F = $71,400; R = $450.30. Component **$92.90**, even though x is below $55,335. This reproduces the ATO's labelled 2025-26 Ashton example using the same checked thresholds; it does not compute SAPTO entitlement. |
| The $476.20 post-family component; 200 fully prescribed days, no overlaps | $476.20 × 165/365 = **$215.2684931506849...**, retained as the exact fraction **$78,573/365**. Hold final assessment rounding. |
| The same $476.20 component; half-period fallback lawfully applies throughout the year | P = 365/2; component **$238.10**. |
| Actual prescribed-person status established for the whole year | Ordinary levy **nil** under section 251T; surcharge remains separate. |
| Paragraph (1)(f) certificate for the year, but dependant condition unresolved | Needs Input. Do not infer full exemption or apply the category-limited half fallback. |
| Required SAPTO, child, family, certificate, period or final-rounding evidence is absent | Hold the affected component or final result; do not choose a higher-tax factual default. |

### Reportable-super input component boundaries

These fictional 2026-27 cases stipulate independently established RESC,
DedSuper and ECC. The ordinary taxable amount before DedSuper and assessable
ECC is $100,000, with no other taxable adjustments. B and total net
investment loss are nil unless stated. Thus C = $100,000 - DedSuper + ECC
for these cases only, and I = C + B + RSC + total net investment loss.
They test the dictionary add-back and reconciliation, not entitlement,
actual cap/excess, surcharge rates or days, offset ordering or final tax.
[DICT, section 995-1][DICT]; [IT97-SUPER, sections 290-150/291-15][IT97-SUPER]

| Independently established fictional inputs | RSC, C and I |
|---|---|
| RESC = $0; DedSuper = $5,000; ECC = $0 | RSC **$5,000**; C **$95,000**; I **$100,000**. |
| RESC = $10,000; DedSuper = $5,000; ECC = $0 | RSC **$15,000**; C **$95,000**; I **$110,000**. |
| RESC = $10,000; DedSuper = $5,000; ECC = $2,000 | RSC **$13,000**; C **$97,000**; I **$110,000**. |
| RESC = $10,000; DedSuper = $5,000; ECC = $15,000 | RSC **nil**; C **$110,000**; I **$110,000**. |
| RESC = $10,000; DedSuper = $5,000; ECC = $20,000 | RSC **nil**, with no negative add-back; C **$115,000**; I **$115,000**. |
| RESC = $0; DedSuper = $0; ECC = $2,000 | RSC **nil**; C **$102,000**; I **$102,000**. |
| RESC = $12,000; DedSuper = $8,000; ECC = $5,000 | RSC **$15,000**; C **$97,000**; I **$112,000**. |
| RESC = $12,000; DedSuper = $8,000; ECC = $25,000 | RSC **nil**; C **$117,000**; I **$117,000**. |
| Gross personal deposit and notice each $10,000; actual DedSuper independently established as $6,000; RESC = ECC = $0 | RSC **$6,000**; C **$94,000**; I **$100,000**. Neither gross amount replaces DedSuper. |
| Gross employer deposits $19,000, independently classified as RESC $6,000 and nonreportable remainder $13,000; DedSuper = ECC = $0 | RSC **$6,000**; C **$100,000**; I **$106,000**. Gross deposits do not establish RESC. |
| RESC = $12,000; DedSuper = $8,000; ECC = $5,000; B = $3,000; total net investment loss = $4,000 | RSC **$15,000**; C **$97,000**; I **$119,000**. Neither B nor the loss add-back is added to stipulated C. |
| Gross employer deposits or an SG label, with influence/exclusion classification unresolved | **Needs Input** for RESC; no automatic zero or gross-deposit substitution. |
| Personal deposit, notice or acknowledgment without actual allowable deduction, including an unresolved section 26-55 limit | **Needs Input** for DedSuper; the notice is not an entitlement calculation. |
| Provisional ECC, unknown required cap/carry-forward/balance evidence or unresolved defined benefit/Commissioner modification | **Needs Input** for ECC; no assumed cap or zero excess. |
| Known RSC, but C/B or another I adjustment is unreconciled | **Needs Input** for downstream surcharge; do not deduct DedSuper or include ECC twice. |
| Contribution income year and corresponding excess financial year are unproved or mismatched | **Needs Input** for the affected year and input; no cross-year netting. |
| Complete deduction, special-case excess determination, final offset/payment or country return requested from these input examples | **Needs Input** for the remaining law, mandatory slots and qualified review. |

### Ordinary concessional-cap and carry-forward boundaries

These fictional 2026-27 cases stipulate independently classified ordinary Q
and that no defined-benefit, protected/notional/transitional or Commissioner
modification applies. G is $32,500. A listed unused amount is proved eligible
and previously unapplied unless expressly expired; every other amount in
the previous-five-year ledger is established nil where that ledger is
required. Missing balance or ledger evidence is marked explicitly, rather
than silently supplied as zero. These are cap/ECC components, not deduction
entitlement, release instructions or final tax. [IT97-SUPER, section
291-20][IT97-SUPER]; [CC-CAP-ATO]

| Established ordinary inputs | Applied prior cap, effective cap and ECC |
|---|---|
| Q = $32,000; prior balance and ledger unknown | Apply **nil**; cap **$32,500**; ECC **nil**. The unknown ledger is not determined or consumed. |
| Q = $32,500; prior balance and ledger unknown | Apply **nil**; cap **$32,500**; ECC **nil** at equality. |
| Q = $32,500.01; prior balance exactly $500,000; ledger unknown | Apply **nil**; cap **$32,500**; ECC **$0.01**. No rounding of Q to whole dollars is assumed. |
| Q = $32,501; prior balance $600,000; ledger unknown | Apply **nil**; cap **$32,500**; ECC **$1**. |
| Q = $40,000; prior balance $499,999; unused 2021-22 $3,000 and 2022-23 $5,000 | Apply **$3,000 then $4,500**; cap **$40,000**; ECC **nil**. The 2022-23 remainder is **$500** before expiry. |
| Q = $40,500; same proved balance and unused amounts | Apply **$3,000 then $5,000**; cap **$40,500**; ECC **nil** at exact exhaustion. |
| Q = $41,000; same proved balance and unused amounts | Apply **$3,000 then $5,000**; cap **$40,500**; ECC **$500**. |
| Q = $40,000; prior balance exactly $500,000; ledger unknown | Apply **nil**; cap **$32,500**; ECC **$7,500**. Equality fails the less-than condition. |
| Q = $40,000; prior balance unknown; all 5 eligible previous-year unused amounts proved nil | Apply **nil**; cap **$32,500**; ECC **$7,500**. A proved nil ledger makes the balance immaterial to this component. |
| Q = $40,000; prior balance $499,999; only an expired 2020-21 record of $10,000, with the previous 5 years proved nil | Apply **nil**; cap **$32,500**; ECC **$7,500**. The expired record cannot increase the cap. |
| Q = $34,000; prior balance $499,999; unused 2021-22 $3,000 and 2022-23 $5,000 | Apply **$1,500 from 2021-22 only**; cap **$34,000**; ECC **nil**. The 2021-22 remainder **$1,500** expires after this year; the 2022-23 remainder is **$5,000** before its own expiry. |
| Q = $40,000; prior balance $499,999; expired 2020-21 record $10,000 and eligible 2025-26 amount $7,500 | Apply **$7,500 from 2025-26 only**; cap **$40,000**; ECC **nil**. |
| Q = $32,501; prior balance $499,999; eligible unused 2021-22 amount $1 | Apply **$1 from 2021-22**; cap **$32,501**; ECC **nil**. |

The following 2 fictional reconciliation cases also independently establish
RESC = $12,000 and actual allowable DedSuper = $8,000. Their classified
Q = $40,000 includes a further $20,000 of ordinary concessional contributions
that are not RESC or DedSuper. The taxable amount before DedSuper and
assessable ECC is $100,000, with all other C/I adjustments and B nil. Thus
C = $100,000 - $8,000 + ECC for these cases only. [DICT]; [IT97-SUPER,
sections 290-150/291-15/291-25][IT97-SUPER]

| Additional established balance/ledger facts | ECC and RSC/C/I reconciliation |
|---|---|
| Prior balance $600,000; no carry-forward available | ECC **$7,500**; RSC **$12,500**; C **$99,500**; I **$112,000**. Do not substitute RESC + DedSuper = $20,000 for Q. |
| Prior balance $499,999; eligible unused 2021-22 $3,000 and 2022-23 $5,000 | Apply **$3,000 then $4,500**; ECC **nil**; RSC **$20,000**; C **$92,000**; I **$112,000**. |

| Missing or unresolved input | Required hold |
|---|---|
| Gross deposits, an SG label or RESC + DedSuper without statutory Q classification | **Needs Input** for Q; do not substitute that total. |
| Defined-benefit, protected/notional/transitional or Commissioner modification is unknown or unresolved | **Needs Input** for the applicable excess computation; the ordinary worksheet cannot settle it. |
| Q exceeds G, the eligible ledger is not proved nil and required prior total superannuation balance is unknown | **Needs Input**; do not default to the higher-tax no-carry result. |
| Q exceeds G, prior balance is below $500,000 and a required unused-year entitlement, zero or prior-use record is unproved | **Needs Input** for the eligible ledger and ECC; do not count current/future amounts or use a provisional carry-forward figure. |
| Contribution year, prior-balance date or ledger year cannot be reconciled | **Needs Input** for the affected input; no cross-year substitution. |
| ECC is computed but actual DedSuper, RESC, C/B or another I adjustment remains unknown | **Needs Input** for the downstream RSC/surcharge result; a known ECC clears none of those gaps. |
| A complete deduction, special-case excess, offset/release/payment or country return is requested | **Needs Input** for remaining operative rules, mandatory outputs and qualified review. |


### Ordinary personal-super deduction boundaries

These hypothetical fixtures use dollars. Every unmentioned entitlement,
receipt, original approved-form notice, acknowledgment and ordinary-branch
gate above is independently satisfied, including nil other specified-pool
deductions, losses and FMDs. N equals the chosen S in every numeric row.
AI is the established assessable amount **including any ECC**; Q/ECC have
been independently reconciled for that exact notice/claim. All other limits
are proved inapplicable. W is a bound for these inputs, not a claim optimiser.

| P | N = S | AI | OD | H | W | Proposed deduction result |
|---:|---:|---:|---:|---:|---:|---|
| $5,000.00 | $5,000 | $100,000.00 | $10,000.00 | $90,000.00 | $5,000 | DedSuper **$5,000**. |
| $5,000.99 | $5,000 | $100,000.00 | $10,000.00 | $90,000.00 | $5,000 | DedSuper **$5,000**; retain the $0.99 contribution remainder. |
| $5,000.99 | $4,000 | $100,000.00 | $10,000.00 | $90,000.00 | $4,000 | DedSuper **$4,000**; the chosen notice is below P. |
| $10,000.00 | $6,000 | $10,000.75 | $4,000.00 | $6,000.75 | $6,000 | DedSuper **$6,000**; H cents are preserved. |
| $10,000.00 | $6,001 | $10,000.75 | $4,000.00 | $6,000.75 | $6,000 | **Needs Input**; S exceeds precise headroom. |
| $1.99 | $1 | $2.00 | $0.01 | $1.99 | $1 | DedSuper **$1**; no upward rounding. |
| $0.99 | $1 | $100.00 | $0.00 | $100.00 | $0 | **Needs Input**; S exceeds P. |
| $100.00 | $1 | $100.00 | $100.00 | $0.00 | $0 | **Needs Input**; no headroom. |
| $100.00 | $1 | $99.99 | $100.00 | $0.00 | $0 | **Needs Input**; floor negative headroom at nil. |
| $10,000.00 | $6,000 | $10,000.00 | $4,000.00 | $6,000.00 | $6,000 | DedSuper **$6,000**; equality is allowed. |
| $10,000.00 | $6,000 | $9,999.99 | $4,000.00 | $5,999.99 | $5,999 | **Needs Input**; one cent below the required headroom. |
| $40,000.00 | $40,000 | $117,500.00 | $10,000.00 | $107,500.00 | $40,000 | DedSuper **$40,000**; the general cap does not truncate this deduction. |

For the last row, independently classified Q is $50,000, comprising the
$40,000 personal contribution included in fund assessable income and $10,000
of other statutory concessional contributions. RESC is separately established
as $10,000. The prior balance is $600,000, so no carry-forward applies:
ECC is $17,500 against the $32,500 general cap. AI comprises $100,000 of other
assessable income plus that $17,500, with OD $10,000. Thus C is **$67,500**,
RSC is **$32,500** and I is **$100,000** when B and all other I adjustments
are independently nil. Include ECC in AI once and deduct DedSuper once.

| Other established facts or gap | Required result |
|---|---|
| Electronic payment initiated 30 June 2027; fund credit 1 July 2027 | Not a 2026-27 contribution; hold the requested 2026-27 deduction and establish 2027-28 separately. |
| No earlier return lodgment; notice delivered 30 June 2028 before day end, acknowledged before claim | Notice timing gate passes; all other gates still apply. |
| No earlier return lodgment; notice first delivered 1 July 2028 | Fails the ordinary 2026-27 notice deadline; no accepted deduction here. |
| Return lodged 31 August 2027; no valid notice delivered before end of that day | Fails statutory timing; do not use the later 30 June 2028 endpoint. |
| Individual turns 67 on 2 July 2027; contribution on 30 June 2027; at least 18 at year end | Ordinary age gate passes; a later birthday does not impose the 67-plus work test on this contribution. |
| Contribution on the 67th birthday, or individual under 18 at year end | Outside this branch; establish the separate age/work conditions. |
| Accumulation member; fund has another member with a defined benefit interest and a qualifying fund-wide election, including an effective saved old election | Section 290-155 exclusion applies; no deduction under this worksheet. |
| Public complying status known, prescribed-election status unknown | **Needs Input**; public status does not prove eligibility. |
| Receipt, approved form, notice delivery, retained contribution or actual acknowledgment unknown | **Needs Input**; no assumed receipt or acknowledgment. |
| P $5,000; N $5,000; chosen S $4,000 | **Needs Input**; unequal notice/claim classification is outside this branch. Do not assume the difference is non-concessional or automatically vary the notice. |
| Any rejected or pending splitting application, variation, withdrawal, rollover, release, transfer, changed interest or income stream | **Needs Input** for this branch; resolve the actual statutory result separately. |
| Downsizer, FHSS/COVID re-contribution, CGT retirement-exemption attribution, foreign-super transfer or other denial unresolved | **Needs Input** for entitlement; no automatic nil classification. |
| Other specified-pool deduction, tax loss or FMD deduction exists or is unknown | **Needs Input**; do not apply the single-pool headroom construction. |
| S $40,000; AI $40,000; OD $10,000; Q/ECC not reconciled for that S | **Needs Input**; unproved ECC cannot be used to manufacture headroom. |

### Single-person surcharge component boundaries

All numeric cases below stipulate the 2026-27 full-year resident adult,
no spouse/dependants throughout, separately reconciled I/C/B, absence of
special adjustments and established surcharge cover/prescribed day sets.
They test unrounded components, rather than a complete return or final
assessed amount. RSC and investment-loss add-backs are not themselves added
to C or B; underlying allowable deductions and assessable excess must
already be reflected in C. [DICT]; [LEVY, section 8B][LEVY];
[MLS-FB, sections 10-12][MLS-FB]; [MLS-ATO]

| Established fictional inputs or failed gate | Selected surcharge component result |
|---|---|
| I = C = $105,000; B = $0; D = 365 | **Nil** at the base-tier upper boundary. |
| I = C = $105,001; B = $0; D = 365 | Rate 1%; taxable-income component **$1,050.01**. The charge is not 1% of $1. |
| I = C = $123,000; B = $0; D = 365 | Rate 1%; taxable-income component **$1,230**. |
| I = C = $123,001; B = $0; D = 365 | Rate 1.25%; exact taxable-income component **$1,537.5125** before unresolved final assessment rounding. |
| I = C = $164,000; B = $0; D = 365 | Rate 1.25%; taxable-income component **$2,050**. |
| I = C = $164,001; B = $0; D = 365 | Rate 1.5%; exact taxable-income component **$2,460.015** before unresolved final assessment rounding. |
| C = $90,000; B = $27,000; I = $117,000; D = 365 | Rate 1%; components **$900 + $270 = $1,170**. The benefits are separately charged. |
| C = $90,000; B = $0; independently reconciled reportable super $20,000; I = $110,000; D = 365 | Rate 1%; component **$900**, rather than $1,100. RSC enters the I threshold/rate tests; it is not added to stipulated C. |
| C = $90,000; B = $0; independently reconciled total net investment loss $20,000; I = $110,000; D = 365 | Rate 1%; component **$900**. The loss enters the I threshold/rate tests; it is not added to stipulated C. |
| C = $95,001; B = $10,000; I = $105,001; D = 365 | Rate 1%; components **$950.01 + $100 = $1,050.01**. C below the singles threshold does not alone establish nil surcharge. |
| C = $109,500; B = $10,950; I = $120,450; D = 100 | Rate 1%; components **$300 + $30 = $330** after the exact day fractions. |
| Same annual amounts; 200 qualifying-cover days and 20 prescribed days, with 10 days in both sets | D = 365 - (200 + 20 - 10) = 155; components **$465 + $46.50 = $511.50**. |
| Same annual amounts; qualifying cover established for every day; D = 0 | Both selected surcharge components **nil**. Ordinary levy and private health rebate remain separate. |
| Same annual amounts; no qualifying cover or prescribed days; D = 365 | Components **$1,095 + $109.50 = $1,204.50**. Extras alone do not change D. |
| Same annual amounts; D = 1 after the dated-set reconciliation | Exact components **$3 + $0.30 = $3.30**; annual amounts are not reassigned by receipt date. |
| I = C = $150,000; B = $0; D = 146 | Rate 1.25%; component **$750**. |
| I = C = $180,000; B = $0; D = 146 | Rate 1.5%; component **$1,080**. |
| I, B, actual policy terms/dates or prescribed status unknown | **Needs Input**. No assumed zero, no assumed uninsured period and no final component. |
| A spouse or surcharge dependant existed at any time, including a domestic/registered relationship or relevant spouse-death period | Route to the family/period section. This singles-only shortcut cannot select the annual tier or full surcharge; unresolved or held family cases remain **Needs Input**. |
| FHSS, trust-distribution, exempt foreign employment or special super/arrears condition unresolved | **Needs Input** for the relevant adjustment law, annual inputs and charge bases. |

### Family and period surcharge component boundaries

These cases stipulate the ordinary annual inputs, full-year resident adult,
proved classifications and cover/prescribed day sets above. All special
adjustments are established absent. Amounts are unrounded components, not
complete returns. Unless stated otherwise, there are no qualifying children,
the same relevant maintained resident spouse exists throughout the year,
neither person is prescribed, B = $0 and all 365 days pass the cover test.
The spouse's figure is annual I. r is conditional on the separate income
screen; it is not a substitute for that screen. [LEVY, sections 3A/8B-8D][LEVY];
[MLS-FB, sections 5-8/11-16][MLS-FB]; [PHI, sections 22-30/22-40][PHI]; [MLS-ATO]

| Established fictional inputs or failed gate | Selected component result |
|---|---|
| Own I = C = $100,000; spouse I = $110,000 | Combined $210,000 equals F1: **nil**. |
| Same own amounts; spouse I = $110,001 | Combined $210,001; r 1%: **$1,000**. |
| Same own amounts; spouse I = $146,000 | Combined $246,000; r 1%: **$1,000**. |
| Same own amounts; spouse I = $146,001 | Combined $246,001; r 1.25%: **$1,250**. |
| Same own amounts; spouse I = $228,000 | Combined $328,000; r 1.25%: **$1,250**. |
| Same own amounts; spouse I = $228,001 | Combined $328,001; r 1.5%: **$1,500**. |
| Own I = C = $28,011; spouse I = $200,000 | Combined exceeds F1, but own I equals the individual screen: **nil**. |
| Own I = C = $28,012; spouse I = $200,000 | r 1%; taxable-income component **$280.12**. |
| C = $26,000; independently established reportable super $2,012; own I = $28,012; spouse I = $200,000 | r 1%; component **$260**. I, rather than C, passes the individual screen. |
| C = $109,500; B = $10,950; own I = $120,450; spouse I = $109,550 | r 1%; components **$1,095 + $109.50 = $1,204.50**. |
| Same annual amounts; only 100 days pass both charges' cover/prescribed tests | Whole-year marriage screen retained; **$300 + $30 = $330**. |
| Same annual amounts; taxpayer and all relevant dependants covered throughout | Both components **nil**. |
| Same annual amounts; taxpayer uninsured 20 days, spouse uninsured 15, overlap 5 | Distinct union 30 days; **$90 + $9 = $99**. |
| Same annual amounts; taxpayer covered throughout, relevant spouse uncovered 100 days | **$300 + $30 = $330**; personal cover alone does not remove liability. |
| Own I = C = $100,000; 2 qualifying children throughout; spouse I = $111,500 / $111,501 | F1 $211,500: **nil / $1,000**. |
| Same own amounts and 2 children; spouse I = $147,500 / $147,501 | F2 $247,500: r 1% / 1.25%; **$1,000 / $1,250**. |
| Same own amounts; 3 qualifying children throughout; spouse I = $231,000 / $231,001 | F3 $331,000: r 1.25% / 1.5%; **$1,250 / $1,500**. |
| Unmarried throughout; one qualifying child throughout; I = C = $210,000 / $210,001; all uncovered | Own F1 screen: **nil / $2,100.01**. |
| Same unmarried/one-child conditions; I = C = $246,000 / $246,001 | r 1% / 1.25%; **$2,460 / $3,075.0125**. |
| Same unmarried/one-child conditions; I = C = $328,001 | r 1.5%; **$4,920.015**. |
| Unmarried throughout; I = C = $150,000; one qualifying child only for 219 days; all uncovered | Annual family classification below F1 gives no uplift, rather than global 0%. The 146 child-free days pass 8B/12: **$600**; dependant days fail own F1 screen. |
| I = C = $150,000; married for 219 days including 30 June; spouse annual I = $100,000; no dependants in the other 146 unmarried days; all uncovered | Annual family A $250,000 gives r 1.25%; unmarried component **$750**. Married days fail own I > F1 despite combined income exceeding F1. |
| Same amounts and day split, but separated for the final 146 days; no non-spouse dependant on any day | Annual singles A $150,000 gives r 1.25%; unmarried component **$750**. Prior spouse income is not added to A. |
| I = C = $219,000; spouse I = $0; married only 100 days including 30 June; remaining unmarried days covered | Own I > F1 and annual family r 1%; married-period component **$600**. |
| I = C = $210,000; spouse I = $200,000; married only 100 days including 30 June; remaining unmarried days covered | Annual family r 1.5%, but own I equals F1: both selected components **nil**. Combined income alone does not pass the married-period screen. |
| Unmarried throughout; one maintained resident 22-year-old child in full-time university education throughout; no ordinary notional student offset; I = C = $210,001; all uncovered | Surcharge disregards 251R(4); child remains a dependant, F1 $210,000: **$2,100.01**. |
| Unmarried throughout; one qualifying maintained resident child throughout; parents separated, ordinary FTB care share 50%; I = C = $219,000; all uncovered | Do not halve the surcharge dependant period under 251R(5); 365 days gives **$2,190**. |
| C = $219,000; B = $21,900; I = $240,900; unmarried with one child throughout; taxpayer independently established within the listed half-period category, but not prescribed because the child is non-prescribed; child covered except 100 days | Limited deeming covers taxpayer for the family test, but the child's 100 uncovered days give **$600 + $60 = $660**. |
| Same annual amounts and status; child covered throughout | Both components **nil** from the proved cover test, not a global prescribed exemption. |
| Unmarried throughout; I = C = $219,000; one qualifying child throughout independently proved prescribed apart from 251U(2); taxpayer non-prescribed, uncovered 100 days and otherwise covered | Child remains in annual family classification but is disregarded for cover; taxpayer's 100 days give **$600**. |
| Changing qualifying-child counts involving 2 or more, unresolved relationship/death classification outside the supported survivor branch or unproved maintenance/residence/education | **Needs Input** for the affected threshold, period or classification; no assumed annual count or unmarried post-death days. |
| Unknown spouse I, I/C/B reconciliation, policy/member/excess/dates, prescribed entitlement or special adjustment | **Needs Input**; no zero-income, covered, exempt or whole-year-marriage assumption. |
| Complete return, final assessed rounding or trustee/special-income computation requested from these cases | **Needs Input** for the remaining sources, mandatory slots and qualified review. |

### Surviving spouse surcharge component boundaries

All cases stipulate the supported ordinary survivor branch above: the same
spouse from 1 July 2026 until death whilst married on 31 December 2026, no
other spouse, full-year residence, no special adjustments and the survivor
nonprescribed and statutorily uncovered for all 365 days, with neither
taxpayer cover deeming rule applying. Own I/C/B and actual deceased spouse
annual I are independently established; the deceased's I is not annualised.
Unless stated otherwise, there are no qualifying children, B = $0 and I = C.
Any stated child count qualifies throughout, including after death. The
365 potential days become zero chargeable days when an income screen fails.
These are fictional unrounded components, not a complete or deceased return.
[LEVY, sections 3(3A)/8D][LEVY]; [MLS-FB, sections 7(3)/14/15][MLS-FB];
[PHI, sections 22-30/22-40][PHI]; [MLS-ATO]

| Established fictional survivor inputs or failed gate | Selected component result |
|---|---|
| Own I = C = $100,000; actual deceased annual I = $150,000 | Annual family A $250,000, r 1.25%; both screens pass: **$1,250**. No single period arises on death. |
| Own I = C = $28,011 / $28,012; actual deceased annual I = $221,989 / $221,988 | A $250,000 and r 1.25% in both cases; own-I screen gives D-C = D-B **0 / 365** and **nil / $350.15**. |
| Own I = C = $100,000; actual deceased annual I = $110,000 / $110,001 | A equals / exceeds F1 $210,000; D-C = D-B **0 / 365** and **nil / $1,000**. |
| Same own amounts; actual deceased annual I = $146,000 / $146,001 | A equals / exceeds F2 $246,000; r 1% / 1.25% gives **$1,000 / $1,250**. |
| Same own amounts; actual deceased annual I = $228,000 / $228,001 | A equals / exceeds F3 $328,000; r 1.25% / 1.5% gives **$1,250 / $1,500**. |
| C = $219,000; B = $21,900; own I = $240,900; actual deceased annual I = $9,100 | A $250,000, r 1.25%; separate components **$2,737.50 + $273.75 = $3,011.25**. Do not charge I as either base. |
| Own I = C = $100,000; 2 qualifying children throughout; actual deceased annual I = $111,500 / $111,501 | F1 $211,500; D-C = D-B **0 / 365** and **nil / $1,000**. |
| Same own amounts and 2 children; actual deceased annual I = $147,500 / $147,501 | F2 $247,500; r 1% / 1.25% gives **$1,000 / $1,250**. |
| Same own amounts; 3 qualifying children throughout; actual deceased annual I = $231,000 / $231,001 | F3 $331,000; r 1.25% / 1.5% gives **$1,250 / $1,500**. |
| Own/deceased annual I, C/B, actual prescription or statutory cover facts are unknown; or taxpayer cover deeming applies | **Needs Input** for this shortcut. Physical non-insurance does not prove statutory uncovered days, and an unknown deceased income is not nil. |
| Marriage starts after 1 July, separation precedes death or a later/competing spouse exists | **Needs Input** for separately supported relationship/period treatment; do not infer whole-year marriage or an automatic single period. |
| Post-death child qualification is unproved, counts involving 2 or more change or special adjustments apply | **Needs Input** for the affected threshold/input; marriage continuation alone proves none of those facts. |

## Outputs, contract coverage and checks

The universal workbook must identify source/version, territory, period,
residence decision, taxable-income provenance and each component separately.
Its reviewer brief must identify every open slot and refusal; its action list
must request the actual missing evidence; its review checklist must record
the base checks and the additions below. Preserve all 4 universal outputs.

For any eventual complete income-tax computation, also preserve the domain's
transaction register, computation working paper, filing/payment calendar,
reviewer brief and taxpayer action list, plus all 12 domain checks. Shared
components may be combined only as the bases permit. A source gap cannot
be filled with a fictional calendar or a bank-label inference.

| Income-tax mandatory slot | Coverage in this selected companion |
|---|---|
| 1. Year, filing unit and residence | Ordinary individual year and residence screening; complex residence/periods held. |
| 2. Income categories | General inclusion framework only; receipt-specific derivation/exemptions remain open. |
| 3. Rates and levies | Selected ordinary tables, section 7/8/9 levy reductions and ordinary single/family/period and supported survivor surcharge components, plus bounded RSC and ordinary cap/carry-forward excess worksheets; unresolved special adjustments, benefit entitlements and held relationship/child-count branches remain incomplete. |
| 4. Allowances and credits | Ordinary LITO and selected special-area zone eligibility/base; dependant/service branches, other offsets and complete ordering remain open. |
| 5. Expenses | General connection, standard work-expense deduction and selected evidence/asset-transition rules; full expense/asset methods and remaining deductions stay open. |
| 6. Loss relief | Open; no utilisation determination. |
| 7. Withholding and prepayments | Evidence requested; methods, rates and dates remain open. |
| 8. Social contributions | Open; no payroll or contribution computation. |
| 9. Filing | Open; no approved calendar, form mapping or payment instruction. |
| 10. Transaction patterns | Selected intake clues only; full receipt/expense library remains open. |
| 11. Refusals and defaults | Explicit above; no missing-fact tax assumptions authorised. |
| 12. Currency and rounding | AUD and exact levy intermediates; conversion and the final assessed-liability rounding stage remain open. |
| 13. Full examples | Component cases only; complete employee, self-employed and mixed-return ladders remain open. |

Additional checks: verify the territorial bridge and exact income year;
resolve residence before rates; reconcile every income/deduction to its
source; distinguish ordinary and special components; recompute every band
and cumulative base; check the exact bracket boundaries; validate part-year
periods/months/exclusions; verify LITO eligibility, caps and non-refundability;
reconcile each section 25-130 reducing branch and its exceptions; verify
substantiation, travel nights, retention and asset history; distinguish zone
classification from usual residence and check allowances/service overlap;
recompute individual caps, family allocation and excess transfers before day
reductions; reconcile annual surcharge I/C/B, annual tier selection and each
period's separate income screen; verify the RSC zero floor, corresponding
income/financial years and C reconciliation without duplicate deduction or
excess inclusion; verify statutory Q, the period-labelled general cap, any
required prior balance and eligible unapplied ledger, the strict balance
limit, oldest-first application only to the excess and remaining-year expiry;
verify the personal deduction intake, original notice/claim equality, exact
headroom, whole-dollar bound and consistent Q/ECC/AI inputs before accepting
DedSuper; verify year-end marriage, any-day non-spouse
dependants, child thresholds and the whole/part-year marriage distinction;
check statutory endpoints, relevant-person uninsured unions, limited cover
deeming and each dated cover/prescribed intersection for both charges; verify benefit
reporting inputs before applying the separate charge bases; keep levy,
surcharge and other offsets separate; substantiate every exemption
period and dependant condition; preserve missing-slot holds; reconcile
withholding/credits without inventing a refund; verify currency/rounding;
and inspect all output components before reviewer delivery.

## Primary sources, currency and remaining work

The territory Act compilation 13 is dated 18 December 2020; the 1936 Act
compilation 193 is dated 1 October 2026. The 1997 Act latest Register
record checked on 23 October 2026 identifies
compilation **268 of 1 October 2026**, C2026C00471. The selected core,
standard-deduction, capital, LITO, offset-ordering, substantiation, geography
and dependant provisions cited here were compared with compilation 267
and are unchanged in the retained current text. This selected comparison
does not verify every income, deduction, definition or operative amendment
for an engagement. [IT97-RECORD]; [CORE]; [OFFSETS]; [DICT]

Only selected provisions were read, not every clause of these Acts. The ATO
LITO and zone-eligibility pages were updated 8 June 2026. The current zone
list was updated 1 July 2026. Act 49 supplies the reform's assessment and
FBT application dates. An old ATO myTax PDF and an incomplete large PDF
download were excluded; no entitlement relies on either. No complete
expense, surcharge, zone/dependant, foreign-income, CGT, payroll, social or
filing regime is certified.
Use `cc-tax-system` for GST/customs geography and historical asset gates.
Other country topics remain open under `docs/country-coverage-plan.md`.

The surcharge reference uses PHI compilation 42 of 19 September 2026,
fringe-benefits surcharge Act compilation 42 of 1 July 2026 and selected
FBTAA compilation 97 provisions of 1 July 2026. The ATO threshold page,
updated 22 June 2026, explicitly labels 2026-27; the cover page was updated
30 April 2026. The family/dependant page was updated 21 August 2026.
The statutory index mechanism was checked, but immutable
first-publication provenance for its ABS inputs is not established here.
The stated amounts therefore rely on the authoritative administration table,
not a claim of independently proven first-published index inputs.
[PHI]; [MLS-FB]; [FBT-REPORTING]; [MLS-ATO]; [MLS-COVER]; [MLS-FAMILY]

The ATO day worksheet, published 1 June 2026, applies to 2025-26. Its
condition of a spouse on 1 July with no replacement spouse corroborates the selected survivor
timeline; historical thresholds and Example 10's overlapping 15 December
endpoints are not adopted. Current legislation governs the 2026-27 statutory
application. [MLS-DEATH-DAYS]; [LEVY]; [MLS-FB]

The RSC worksheet uses TAA compilation 227 of 1 October 2026, Schedule 1
section 16-182, and selected Subdivisions 290-C and 291-B/291-C of ITAA97
compilation 268. Paragraph 26-55(2)(b) was expressly repealed by the 1999 amending Act.
The ordinary personal deduction worksheet applies the bounded combined-pool
construction with other pool deductions, losses and FMDs proved nil.
DedSuper outside that branch and special-case ECC remain independently established
inputs. Ordinary ECC can instead be calculated from independently
established Q and the applicable balance/ledger facts under the bounded
worksheet above. [TAA]; [CORE]; [IT97-SUPER]; [DICT]

The ordinary cap worksheet uses ITAA97 sections 291-20/291-25 and the
section 960-285 index, together with the ATO page updated 2 July 2026 that
expressly publishes $32,500 from 1 July 2026. The selected Original ABS
full-time adult ordinary-time earnings series A85002148L gives $2,051.10
for November 2025 and $1,533.40 for November 2016. Their ratio rounds to
1.338; $25,000 multiplied by 1.338 is $33,450, rounded down to the $2,500
multiple $32,500. The release-specific Table 3 workbooks and pre-release
internal timestamps corroborate these inputs; no explicit numerical revision
history was found, and timestamps alone do not prove immutability. The
stated cap relies on the current authoritative ATO amount, with this
statutory reproduction as corroboration. The page's adjacent quarterly SG
payment text is not adopted as a 2026-27 payment rule. [CC-CAP-ATO];
[ABS-CC-2016]; [ABS-CC-2025]; [DICT, sections 960-265/960-280/960-285][DICT]

Version 1.1, 23 October 2026: adds chosen-claim personal-super deduction
validation, complete ordinary Division 290 intake, prescribed and saved
election gates, precise section 26-55 headroom and notice/claim controls.
The selected receipt/notice passages were compared with ATO's complete
62-page authorised consolidated TR 2010/1 PDF; the current HTML history
identifies the selected consolidation as 24 September 2025. Regulations
compilation 16 of 27 June 2026 supplies the election gates. Appendix
explanations are not part of the ruling's legally binding section.
Unequal notice/claim, special contributions, changed interests, mixed pools
and unresolved statutory inputs remain held. [TR-CONTRIB]; [SUPER-REGS];
[SUPER-REPEAL]; [SUPER-REPEAL-EM]

Version 1.0, 23 October 2026: adds the ordinary concessional-cap,
carry-forward and ECC worksheet, 13 numeric cap cases, 2 RSC/C/I
reconciliations and 7 held-input rows. Carry-forward uses only eligible
previous-five-year amounts, oldest first and only to the extent needed.
Unknown required facts and all special-branch, deduction, final-output and
comprehensive-country holds remain.


Version 0.9, 23 October 2026: adds the bounded RSC zero-floor worksheet,
11 fictional input/reconciliation instances and 6 held-input rows. Distinct
RESC/DedSuper/ECC names preserve existing levy and day notation. Known
inputs may feed I only after their taxable effects are reconciled in C;
unknown deduction/excess entitlement, other special adjustments and all
complete-return/country holds remain.

Version 0.8, 23 October 2026: adds ordinary surviving spouse surcharge
mechanics, statutory cover-deeming exclusions, post-death child qualification
and 16 numeric boundary instances. Actual annual deceased spouse income is
not annualised; potential and post-screen days remain distinct. Other
relationship, special-input, final-precision and complete-return holds remain.

Version 0.7, 23 October 2026: adds ordinary family and relationship-period
surcharge mechanics, separate annual-tier and period-income screens,
constant-child thresholds, relevant-dependant cover unions and limited
cover deeming. Component boundaries include below-family-base unmarried
periods. Special adjustments, uncertain changing child counts, death/competing
relationships, final precision and complete-return holds remain.

Version 0.6, 23 October 2026: adds the ordinary full-year resident single
adult surcharge component, distinct annual income/charge bases, hospital
cover and surcharge day gates, plus 20 component boundary/refusal cases.
Family, special-adjustment, final-precision and complete-return holds remain.

Version 0.5, 23 October 2026: adds ordinary Medicare reduction order, family
allocation, prescribed-period mechanics and component boundaries; retains
SAPTO/child eligibility, special-adjustment, rounding and complete-return
holds. Updates the selected 1997 Act citations to compilation 268.

Version 0.2, 21 October 2026: adds the standard work-expense deduction,
selected substantiation/asset transitions and verified local special-area
zone rules. Version 0.1 introduced the selected personal-rate, LITO and
Medicare reference. Both retain explicit incomplete-domain holds.

[TR-CONTRIB]: https://www.ato.gov.au/law/view/pdf/pbr/tr2010-001c5.pdf
[SUPER-NOTICE]: https://www.ato.gov.au/print/section/070cfb0b-0299-47a3-a81c-c222280ebe90
[SUPER-REGS]: https://www.legislation.gov.au/F2021L00206/2026-06-27/2026-06-27/text/original/epub/OEBPS/document_1/document_1.html
[SUPER-REPEAL]: https://www.legislation.gov.au/C2004A00560/asmade/1999-12-10/text/original/epub/OEBPS/document_1/document_1.html
[SUPER-REPEAL-EM]: https://www.ato.gov.au/law/view/document?DocID=NEM%2FEM99039%2FNAT%2FATO%2F00005
[CC-CAP-ATO]: https://www.ato.gov.au/individuals-and-families/super-for-individuals-and-families/super/growing-and-keeping-track-of-your-super/caps-limits-and-tax-on-super-contributions/concessional-contributions-cap
[ABS-CC-2016]: https://www.ausstats.abs.gov.au/ausstats/meisubs.nsf/0/BF933648CF3B3FF5CA2580CF000D5066/$File/6302003.xls
[ABS-CC-2025]: https://www.abs.gov.au/statistics/labour/earnings-and-working-conditions/average-weekly-earnings-australia/nov-2025/6302003.xlsx
[IT97-SUPER]: https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_6/document_6.html
[MLS-DEATH-DAYS]: https://www.ato.gov.au/individuals-and-families/your-tax-return/instructions-to-complete-your-tax-return/mytax-instructions/2026/medicare-and-private-health-insurance/medicare-levy-surcharge/mytax-2026-number-of-days-you-dont-have-to-pay-the-mls
[MLS-FB]: https://www.legislation.gov.au/C2004A00412/2026-07-01/2026-07-01/text/original/epub/OEBPS/document_1/document_1.html
[PHI]: https://www.legislation.gov.au/C2007A00031/2026-09-19/2026-09-19/text/original/epub/OEBPS/document_1/document_1.html
[MLS-ATO]: https://www.ato.gov.au/individuals-and-families/medicare-and-private-health-insurance/medicare-levy-surcharge/medicare-levy-surcharge-income-thresholds-and-rates
[MLS-FAMILY]: https://www.ato.gov.au/individuals-and-families/medicare-and-private-health-insurance/medicare-levy-surcharge/family-and-dependants-for-medicare-levy-surcharge-purposes
[MLS-COVER]: https://www.ato.gov.au/individuals-and-families/medicare-and-private-health-insurance/medicare-levy-surcharge/paying-the-medicare-levy-surcharge/appropriate-level-of-private-patient-hospital-cover
[FBT-REPORTING]: https://www.legislation.gov.au/C2004A03280/2026-07-01/2026-07-01/text/original/epub/OEBPS/document_2/document_2.html
[FBT-VALUES]: https://www.legislation.gov.au/C2004A03280/2026-07-01/2026-07-01/text/original/epub/OEBPS/document_1/document_1.html

[TERRITORY]: https://www.legislation.gov.au/C1955A00034/2020-12-18/2020-12-18/text/original/epub/OEBPS/document_1/document_1.html
[RESIDENCE]: https://www.legislation.gov.au/C1936A00027/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_1/document_1.html
[CORE]: https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_1/document_1.html
[DICT]: https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_10/document_10.html
[RATES-RECORD]: https://www.legislation.gov.au/C2004A03348/latest/text
[RATES]: https://www.legislation.gov.au/C2004A03348/2026-07-01/2026-07-01/text/original/epub/OEBPS/document_1/document_1.html
[OFFSETS]: https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_2/document_2.html
[ATO-LITO]: https://www.ato.gov.au/individuals-and-families/income-deductions-offsets-and-records/tax-offsets/low-income-tax-offset
[MEDICARE]: https://www.legislation.gov.au/C1936A00027/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_4/document_4.html
[LEVY-AMEND]: https://www.legislation.gov.au/C2026A00058/asmade/2026-06-30/text/original/epub/OEBPS/document_1/document_1.html
[ATO-LEVY-SINGLE]: https://www.ato.gov.au/individuals-and-families/medicare-and-private-health-insurance/medicare-levy/medicare-levy-reduction/medicare-levy-reduction-for-low-income-earners
[ATO-LEVY-FAMILY]: https://www.ato.gov.au/individuals-and-families/medicare-and-private-health-insurance/medicare-levy/medicare-levy-reduction/medicare-levy-reduction-family-income
[SAPTO]: https://www.legislation.gov.au/C1936A00027/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_3/document_3.html
[TAA]: https://www.legislation.gov.au/C1953A00001/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_1/document_1.html
[TAA-SCHEDULE]: https://www.legislation.gov.au/C1953A00001/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_2/document_2.html
[LEVY-RECORD]: https://www.legislation.gov.au/C2004A03351/latest/text
[LEVY]: https://www.legislation.gov.au/C2004A03351/2026-07-01/2026-07-01/text/original/epub/OEBPS/document_1/document_1.html
[IT97-RECORD]: https://www.legislation.gov.au/C2004A05138/latest/text
[AMEND71]: https://www.legislation.gov.au/C2026A00071/asmade/2026-08-26/text/original/epub/OEBPS/document_1/document_1.html
[AMEND86]: https://www.legislation.gov.au/C2026A00086/asmade/2026-09-15/text/original/epub/OEBPS/document_1/document_1.html

[REFORM]: https://www.legislation.gov.au/C2026A00049/asmade/2026-06-26/text/original/epub/OEBPS/document_1/document_1.html
[ZONES]: https://www.legislation.gov.au/C1936A00027/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_5/document_5.html
[ATO-ZONES]: https://www.ato.gov.au/calculators-and-tools/tax-offsets-australian-zones/western-australia
[ATO-ZONE]: https://www.ato.gov.au/individuals-and-families/income-deductions-offsets-and-records/tax-offsets/zone-or-overseas-forces-tax-offsets/zone-tax-offset

**Revision 0.4, 23 October 2026:** restored routing to the published SG
companion after integration removed it. The version advances beyond the
previously published v0.3. Income-tax rules, source-law verification dates
and outstanding coverage remain unchanged.

## Disclaimer

General reference only. This source-cited draft does not determine any
person's liability, entitlement, filing requirement or deadline. A qualified
professional must resolve the complete applicable law and facts and review
and sign off the outputs before anyone files, pays or acts on them.

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
