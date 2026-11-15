---
name: cc-income-tax
description: >
  Selected Cocos (Keeling) Islands individual income-tax rules for 2026-27.
  Establishes the Australian territorial bridge, residence and income-year
  gates, ordinary resident and foreign-resident personal rates, conditional
  part-year threshold, low income tax offset, standard work-expense deduction,
  substantiation changes, special-area zone relief and ordinary Medicare
  reductions, single-person, family/period and ordinary surviving spouse
  surcharge screening (the surcharge, reportable-super and concessional-cap
  worksheets are in cc-medicare-levy-surcharge). Use for
  Cocos (Keeling) Islands personal tax, ordinary annual rates, mainland moves or
  levy-exemption questions. Includes primary legislation, fictional component
  calculations, required intake, refusals and reviewer checks. This source-cited
  draft accepts taxable income only after all applicable income and deduction
  rules are resolved; it does not complete a return or the country pack.
jurisdiction: CC
category: international
tax_year: 2026
type: computation
tax_year_notes: "2026-27: selected ordinary personal rates for 1 July 2026 to 30 June 2027; adjacent years and Medicare conditions require their separately identified sources"
tier: 2
last_updated: 2026-11-14
version: 1.2
depends_on:
  - workflow-base
  - income-tax-workflow-base
---

# Cocos (Keeling) Islands: selected individual income tax for 2026-27 (v1.2)

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

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

Christmas Island and the Cocos (Keeling) Islands are Australian external territories inside geographical Australia for income tax (ITAA 1997 section 960-505(1)(d)-(e)), so the Australian Commonwealth figures apply there. The Australian 2026-27 rates card is `au-rates-2026-27` and the Australian individual return method is `au-individual-return`; this skill restates the figures it needs with their Australian source on each row. The Medicare levy surcharge, reportable superannuation and concessional-cap worksheets were split into `cc-medicare-levy-surcharge` on 2026-11-14 to keep each file under the size limit.

### Territorial application, residence and income

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

## Ask the client first

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

## The method, step by step

### Period figures and ordinary personal rates

All money figures are **Australian dollars**. The following selected
figures were checked on **21 October 2026**. Rates Act compilation 66 of
1 July 2026 was shown as latest by its live Register record. [RATES-RECORD]

The resident table applies only to an **adult Australian resident for the
whole 2026-27 income year**, with the full tax-free threshold and ordinary
taxable income. It excludes offsets, Medicare and other adjustments.
Section 3 defines the threshold as **$18,200**; section 12 and Schedule 7
Part I clause 1 supply the marginal rates. [RATES]

| Ordinary taxable income | Basic income tax for 2026-27 | Official URL |
|---|---|---|
| $0 to $18,200 | Nil | https://www.legislation.gov.au/C2004A03348/2026-07-01/2026-07-01/text/original/epub/OEBPS/document_1/document_1.html |
| Over $18,200 to $45,000 | 15% of the excess over $18,200 | https://www.legislation.gov.au/C2004A03348/2026-07-01/2026-07-01/text/original/epub/OEBPS/document_1/document_1.html |
| Over $45,000 to $135,000 | $4,020 (derived) plus 30% of the excess over $45,000 | https://www.legislation.gov.au/C2004A03348/2026-07-01/2026-07-01/text/original/epub/OEBPS/document_1/document_1.html |
| Over $135,000 to $190,000 | $31,020 (derived) plus 37% of the excess over $135,000 | https://www.legislation.gov.au/C2004A03348/2026-07-01/2026-07-01/text/original/epub/OEBPS/document_1/document_1.html |
| Over $190,000 | $51,370 (derived) plus 45% of the excess over $190,000 | https://www.legislation.gov.au/C2004A03348/2026-07-01/2026-07-01/text/original/epub/OEBPS/document_1/document_1.html |

The ordinary **whole-year foreign-resident** table has no tax-free
threshold. Establish the Australian taxable amount first; do not apply
these rates to all worldwide receipts merely because a bank statement
contains them. [RATES, section 3 and Schedule 7 Part II clause 1][RATES]

| Ordinary taxable income | Basic income tax for 2026-27 | Official URL |
|---|---|---|
| $0 to $135,000 | 30% of that amount | https://www.legislation.gov.au/C2004A03348/2026-07-01/2026-07-01/text/original/epub/OEBPS/document_1/document_1.html |
| Over $135,000 to $190,000 | $40,500 (derived) plus 37% of the excess over $135,000 | https://www.legislation.gov.au/C2004A03348/2026-07-01/2026-07-01/text/original/epub/OEBPS/document_1/document_1.html |
| Over $190,000 | $60,850 (derived) plus 45% of the excess over $190,000 | https://www.legislation.gov.au/C2004A03348/2026-07-01/2026-07-01/text/original/epub/OEBPS/document_1/document_1.html |

The first resident taxable band is **16% for 2025-26**, **15% for 2026-27**
and **14% for 2027-28 and later years** in the checked compilation. Keep
those tables separate. A withholding scale is not this annual liability
table. [RATES, Schedule 7 Part I][RATES]

Special income components, working-holiday taxable income, prescribed
minors, trustees, superannuation and termination remainders, primary
producer averaging and professional-income averaging require their own
rules. A treaty may also affect a branch. Neither ordinary table approves
those computations. [RATES, sections 3, 3A and 12-15 and Schedule 7][RATES]

#### Part-year threshold

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

### Taxable income, deductions and the low income tax offset

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

#### Standard work-expense deduction from 2026-27

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

| Section 25-130(2) branch | Amount reducing the standard deduction | Official URL |
|---|---|---|
| (c), section 8-1 | Each deduction to the extent the outgoing was incurred in gaining or producing assessable labour income, subject to subsection (3). | https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_1/document_1.html |
| (d), Division 28 | Car deductions to the extent they arise from gaining or producing assessable labour income. | https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_1/document_1.html |
| (e), section 25-100 | Travel-between-workplaces deduction where either specified workplace activity was undertaken to gain or produce assessable labour income. | https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_1/document_1.html |
| (f), section 25-10 and Subdivisions 40-B/40-D | Repair, decline-in-value and balancing-adjustment deductions to the extent the asset is used to produce assessable labour income. | https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_1/document_1.html |
| (g), section 25-125 | Each allowable COVID-19 test deduction; paragraph (g) has no added labour-income apportionment condition. | https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_1/document_1.html |

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

#### Actual-expense evidence and asset transitions

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

#### Low income tax offset

For an ordinary adult individual, section 61-110 provides LITO where the
person is Australian resident at any time in the income year and taxable
income does not exceed **$66,667**. Whole-year foreign residents do not meet
that residence condition. Section 61-115 provides the following amount
before applicable limitations. [OFFSETS]

| Relevant taxable income | LITO for an otherwise eligible ordinary adult | Official URL |
|---|---|---|
| At or below $37,500 | $700 | https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_2/document_2.html |
| Over $37,500 to $45,000 | $700 less 5% of the excess over $37,500 | https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_2/document_2.html |
| Over $45,000 to $66,667 | $325 less 1.5% of the excess over $45,000 | https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_2/document_2.html |
| Above $66,667 | No entitlement under section 61-110 | https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_2/document_2.html |

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

### Zone relief: local classification and actual residence

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

### Medicare: ordinary levy, reductions and prescribed periods

Establish the charge under section 251S before calculating a levy. A
whole-year prescribed person can have no ordinary levy under section 251T,
but an island address alone does not establish that status. These rules
cover an ordinary adult individual only. Trustees, special superannuation
adjustments under section 251S(1A), arrears under Levy Act section 9A and
surcharge require their complete separate rules. [MEDICARE]; [LEVY]

#### Source period and individual reduction

The Medicare Levy Act compilation 53 of 1 July 2026 was checked on
**23 October 2026**. Act 58 of 2026, Schedule 5, commenced on 1 July 2026;
item 14 applies its threshold amendments to **2025-26 assessments and later
years**. The following are the amounts in that checked law for the selected
2026-27 reference, subject to subsequent amendments and the engagement
source gate. The ATO reduction pages corroborate these figures but expressly
label their guidance **2025-26**; their year label is not changed here.
[LEVY-RECORD]; [LEVY]; [LEVY-AMEND]; [ATO-LEVY-SINGLE]; [ATO-LEVY-FAMILY]

| Individual branch | Lower threshold H | Statutory phase-in limit U | Official URL |
|---|---|---|---|
| Entitled to the section 160AAAA seniors and pensioners rebate | $44,268 | $55,335 | https://www.legislation.gov.au/C2004A03351/2026-07-01/2026-07-01/text/original/epub/OEBPS/document_1/document_1.html |
| Every other ordinary individual | $28,011 | $35,013 | https://www.legislation.gov.au/C2004A03351/2026-07-01/2026-07-01/text/original/epub/OEBPS/document_1/document_1.html |

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

#### Family reduction and allocation

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

#### Whole and part-year prescribed persons

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

#### Precision and remaining levy branches

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
components are in `cc-medicare-levy-surcharge`. Special surcharge income/benefit adjustments,
arrears and special superannuation adjustments remain unresolved.
Unknown cover does not mean no cover, and nil ordinary levy does not prove
nil surcharge. Do not use historical island guidance to override the
checked current charge and conditional exemption rules.

## Worked cases

Two cases that recompute (derived from the tables above, 2026-27, AUD). Both stipulate an adult
Australian resident for the whole year with ordinary taxable income and no special-rate component.

**Case 1, the simple case.** Taxable income $60,000. Basic tax is $4,020 plus 30% of the excess over
$45,000; LITO is $325 less 1.5% of the excess over $45,000; ordinary Medicare levy 2% applies in full.
Before other offsets and credits the two income-tax components leave $8,420 (derived).

```oa-check
name: Cocos (Keeling) Islands resident, taxable income AUD 60,000, 2026-27 (basic tax, LITO, ordinary levy)
inputs:
  taxable: 60000
steps:
  - basic_tax: 4020 + (taxable - 45000) * 0.30
  - lito: 325 - (taxable - 45000) * 0.015
  - after_lito: basic_tax - lito
  - medicare: taxable * 0.02
expected:
  basic_tax: 8520
  lito: 100
  after_lito: 8420
  medicare: 1200
```

**Case 2, the edge case: should the employee claim actual expenses or rely on the standard
deduction, and what does zone relief add?** Assessable labour income $60,000 and no other income;
allowable branch (c) work deductions $320. The standard deduction tops the reducing deductions up to
$1,000 (section 25-130), so claiming the $320 actually costs nothing extra and adds nothing extra:
the total deduction is $1,000 either way, and the standard amount alone gives the same $1,000 without
evidence for the $320. Usual residence on Cocos (Keeling) Islands all year qualifies for the special-area zone
offset ($1,173 less the $200 prescribed remote area allowance paid). Result derived.

```oa-check
name: Cocos (Keeling) Islands employee, labour income AUD 60,000, actual deductions 320, zone offset with allowance 200
inputs:
  labour_income: 60000
  actual_reducing: 320
  remote_allowance: 200
steps:
  - standard_deduction: max(0, min(1000, labour_income) - actual_reducing)
  - total_deductions: actual_reducing + standard_deduction
  - taxable: labour_income - total_deductions
  - basic_tax: 4020 + (taxable - 45000) * 0.30
  - lito: 325 - (taxable - 45000) * 0.015
  - zone: 1173 - remote_allowance
  - tax_after_offsets: basic_tax - lito - zone
expected:
  standard_deduction: 680
  total_deductions: 1000
  taxable: 59000
  basic_tax: 8220
  lito: 115
  zone: 973
  tax_after_offsets: 7132
```

### Fictional component calculations

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

#### Deduction and zone boundary cases

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

#### Ordinary Medicare component boundaries

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

## When to refuse or refer

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

## Filing and payment

This skill does not set a filing calendar or a payment instruction (income-tax slot 9 stays open, see the checklist). Cocos (Keeling) Islands residents lodge with the ATO under the same Commonwealth law as the mainland: use `au-individual-return` for the return and `au-lodgment-deadlines-penalties` for lodgment dates, payment and penalties, and confirm the actual calendar there before giving a date.

## Completion checklist

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

## Sources

| Source | URL | Read on |
|---|---|---|
| [TERRITORY] Cocos (Keeling) Islands Act 1955 (compilation in force 2020-12-18, volume 1). Read for the provisions cited as [TERRITORY] in the body | https://www.legislation.gov.au/C1955A00034/2020-12-18/2020-12-18/text/original/epub/OEBPS/document_1/document_1.html | 2026-10-21 to 2026-10-23 (read by Ryan Duguid) |
| [RESIDENCE] Income Tax Assessment Act 1936 (compilation in force 2026-10-01, volume 1). Read for section 79A(1) and (3B); section 79A(3B)-(3C); section 79A(2) and (4); section 79A(3D)-(4); section 6(1) | https://www.legislation.gov.au/C1936A00027/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_1/document_1.html | 2026-10-21 to 2026-10-23 (read by Ryan Duguid) |
| [CORE] Income Tax Assessment Act 1997 (compilation in force 2026-10-01, volume 1). Read for sections 6-5, 6-10 and 6-15; Division 8; section 25-130; section 25-130(4); sections 8-10 and 25-130(2)-(3); section 26-55 | https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_1/document_1.html | 2026-10-21 to 2026-10-23 (read by Ryan Duguid) |
| [DICT] Income Tax Assessment Act 1997 (compilation in force 2026-10-01, volume 10). Read for section 995-1; sections 900-15, 900-110, 900-115 and 900-120; sections 900-20, 900-25 and 900-150; Division 900; Subdivision 961-B; Subdivisions 961-A and 961-B | https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_10/document_10.html | 2026-10-21 to 2026-10-23 (read by Ryan Duguid) |
| [RATES-RECORD] Income Tax Rates Act 1986 (Federal Register of Legislation record, latest compilation). Read for the provisions cited as [RATES-RECORD] in the body | https://www.legislation.gov.au/C2004A03348/latest/text | 2026-10-21 to 2026-10-23 (read by Ryan Duguid) |
| [RATES] Income Tax Rates Act 1986 (compilation in force 2026-07-01, volume 1). Read for section 3 and Schedule 7 Part II clause 1; Schedule 7 Part I; sections 3, 3A and 12-15 and Schedule 7 | https://www.legislation.gov.au/C2004A03348/2026-07-01/2026-07-01/text/original/epub/OEBPS/document_1/document_1.html | 2026-11-14 (re-read for Schedule 7 Parts I and II: 2025-26 16%, 2026-27 15%, 2027-28 14% first band; $18,200 threshold; foreign-resident bands); 2026-10-21 to 2026-10-23 (read by Ryan Duguid) |
| [OFFSETS] Income Tax Assessment Act 1997 (compilation in force 2026-10-01, volume 2). Read for sections 40-291A and 40-425(9); section 63-10; Subdivision 61-A | https://www.legislation.gov.au/C2004A05138/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_2/document_2.html | 2026-10-21 to 2026-10-23 (read by Ryan Duguid) |
| [ATO-LITO] ATO: low income tax offset. Read for the provisions cited as [ATO-LITO] in the body | https://www.ato.gov.au/individuals-and-families/income-deductions-offsets-and-records/tax-offsets/low-income-tax-offset | 2026-10-21 to 2026-10-23 (read by Ryan Duguid) |
| [MEDICARE] Income Tax Assessment Act 1936 (compilation in force 2026-10-01, volume 4). Read for sections 251R and 251U; sections 251R/251V; sections 251R/251U/251V/251VA; section 251R(2)/(2A); sections 251U/251VA | https://www.legislation.gov.au/C1936A00027/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_4/document_4.html | 2026-10-21 to 2026-10-23 (read by Ryan Duguid) |
| [LEVY-AMEND] Treasury Laws Amendment (Delivering an Efficient and Trusted Tax System) Act 2026 (Act 58 of 2026) (as made, volume 1). Read for Schedule 5 items 1/10/11/14 | https://www.legislation.gov.au/C2026A00058/asmade/2026-06-30/text/original/epub/OEBPS/document_1/document_1.html | 2026-10-21 to 2026-10-23 (read by Ryan Duguid) |
| [ATO-LEVY-SINGLE] ATO: medicare levy reduction for low income earners. Read for the provisions cited as [ATO-LEVY-SINGLE] in the body | https://www.ato.gov.au/individuals-and-families/medicare-and-private-health-insurance/medicare-levy/medicare-levy-reduction/medicare-levy-reduction-for-low-income-earners | 2026-10-21 to 2026-10-23 (read by Ryan Duguid) |
| [ATO-LEVY-FAMILY] ATO: medicare levy reduction family income. Read for the provisions cited as [ATO-LEVY-FAMILY] in the body | https://www.ato.gov.au/individuals-and-families/medicare-and-private-health-insurance/medicare-levy/medicare-levy-reduction/medicare-levy-reduction-family-income | 2026-10-21 to 2026-10-23 (read by Ryan Duguid) |
| [SAPTO] Income Tax Assessment Act 1936 (compilation in force 2026-10-01, volume 3). Read for the provisions cited as [SAPTO] in the body | https://www.legislation.gov.au/C1936A00027/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_3/document_3.html | 2026-10-21 to 2026-10-23 (read by Ryan Duguid) |
| [TAA] Taxation Administration Act 1953 (compilation in force 2026-10-01, volume 1). Read for Schedule 1 section 16-182 | https://www.legislation.gov.au/C1953A00001/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_1/document_1.html | 2026-10-21 to 2026-10-23 (read by Ryan Duguid) |
| [TAA-SCHEDULE] Taxation Administration Act 1953 (compilation in force 2026-10-01, volume 2). Read for the provisions cited as [TAA-SCHEDULE] in the body | https://www.legislation.gov.au/C1953A00001/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_2/document_2.html | 2026-10-21 to 2026-10-23 (read by Ryan Duguid) |
| [LEVY-RECORD] Medicare Levy Act 1986 (Federal Register of Legislation record, latest compilation). Read for the provisions cited as [LEVY-RECORD] in the body | https://www.legislation.gov.au/C2004A03351/latest/text | 2026-10-21 to 2026-10-23 (read by Ryan Duguid) |
| [LEVY] Medicare Levy Act 1986 (compilation in force 2026-07-01, volume 1). Read for section 3; sections 6-9; section 8(5)-(7); section 8; sections 3/3A/8B; sections 3/8B | https://www.legislation.gov.au/C2004A03351/2026-07-01/2026-07-01/text/original/epub/OEBPS/document_1/document_1.html | 2026-11-14 (re-read for section 3 low-income thresholds $28,011 and $44,268, phase-in limits $35,013 and $55,335, family threshold $47,238, $61,623 and $4,338 per child); 2026-10-21 to 2026-10-23 (read by Ryan Duguid) |
| [IT97-RECORD] Income Tax Assessment Act 1997 (Federal Register of Legislation record, latest compilation). Read for the provisions cited as [IT97-RECORD] in the body | https://www.legislation.gov.au/C2004A05138/latest/text | 2026-10-21 to 2026-10-23 (read by Ryan Duguid) |
| [REFORM] Treasury Laws Amendment (Tax Reform No. 1) Act 2026 (Act 49 of 2026) (as made, volume 1). Read for Schedule 4 items 3 and 17; section 2 and Schedule 4 items 4, 10-12 and 17; Schedule 4 items 7-8 and 17(2); Schedule 4 items 18-20 | https://www.legislation.gov.au/C2026A00049/asmade/2026-06-26/text/original/epub/OEBPS/document_1/document_1.html | 2026-10-21 to 2026-10-23 (read by Ryan Duguid) |
| [ZONES] Income Tax Assessment Act 1936 (compilation in force 2026-10-01, volume 5). Read for the provisions cited as [ZONES] in the body | https://www.legislation.gov.au/C1936A00027/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_5/document_5.html | 2026-10-21 to 2026-10-23 (read by Ryan Duguid) |
| [ATO-ZONES] ATO: western australia. Read for the provisions cited as [ATO-ZONES] in the body | https://www.ato.gov.au/calculators-and-tools/tax-offsets-australian-zones/western-australia | 2026-10-21 to 2026-10-23 (read by Ryan Duguid) |
| [ATO-ZONE] ATO: zone tax offset. Read for the provisions cited as [ATO-ZONE] in the body | https://www.ato.gov.au/individuals-and-families/income-deductions-offsets-and-records/tax-offsets/zone-or-overseas-forces-tax-offsets/zone-tax-offset | 2026-10-21 to 2026-10-23 (read by Ryan Duguid) |

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

Version 0.5, 23 October 2026: adds ordinary Medicare reduction order, family
allocation, prescribed-period mechanics and component boundaries; retains
SAPTO/child eligibility, special-adjustment, rounding and complete-return
holds. Updates the selected 1997 Act citations to compilation 268.

Version 0.2, 21 October 2026: adds the standard work-expense deduction,
selected substantiation/asset transitions and verified local special-area
zone rules. Version 0.1 introduced the selected personal-rate, LITO and
Medicare reference. Both retain explicit incomplete-domain holds.

**Revision 0.4, 23 October 2026:** restored routing to the published SG
companion after integration removed it. The version advances beyond the
previously published v0.3. Income-tax rules, source-law verification dates
and outstanding coverage remain unchanged.

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
[REFORM]: https://www.legislation.gov.au/C2026A00049/asmade/2026-06-26/text/original/epub/OEBPS/document_1/document_1.html
[ZONES]: https://www.legislation.gov.au/C1936A00027/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_5/document_5.html
[ATO-ZONES]: https://www.ato.gov.au/calculators-and-tools/tax-offsets-australian-zones/western-australia
[ATO-ZONE]: https://www.ato.gov.au/individuals-and-families/income-deductions-offsets-and-records/tax-offsets/zone-or-overseas-forces-tax-offsets/zone-tax-offset

Not yet confirmed: the ATO pages ([ATO-LITO], [ATO-ZONES], [ATO-ZONE], [ATO-LEVY-SINGLE], [ATO-LEVY-FAMILY]) refused an automated fetch on 2026-11-14 (HTTP 403), so their figures rest on Ryan Duguid's reading of 21-23 October 2026 and on the statute rows re-read on 2026-11-14; the special-area zone base of $1,173 and the LITO bands were not re-read on 2026-11-14; the final assessment rounding stage for Medicare levy; every component the checklist marks open (loss relief, withholding, filing calendar, full examples).
