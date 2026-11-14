---
name: nf-tax-amendments-objections
description: >
  Establish selected Norfolk Island income-tax assessment correction and
  objection routes under current Australian law. Use for amendment periods,
  eligible business self-amendments, amended notices, nil assessments,
  late objections, delayed decisions and external review. Covers the
  distinct two-year and four-year clocks, retained prior-year regulations,
  prescribed exclusions, grounds, evidence and payment separation. Includes
  current primary legislation, authority guidance and fictional boundary
  components. Requires taxpayer capacity, income year, original and amended
  notices, giving or service evidence and verified route-specific dates.
  Preserves applicable workflow outputs and holds actual filings, complex
  disputes and unresolved facts. This draft does not complete the compliance
  or country pack.
jurisdiction: NF
category: international
tax_year: 2026
tax_year_notes: "Procedural sources checked 18 October 2026; each assessment income year, original/amended notice and applicable transitional regulation must be identified separately"
tier: 2
last_updated: 2026-10-18
version: 0.1
review_status: pending_review
depends_on:
  - workflow-base
  - nf-tax-system
  - nf-return-filing
  - nf-income-tax
  - nf-company-tax
  - nf-foreign-income
---

# Norfolk Island: income-tax amendments, objections and review

Establish the person or entity and capacity, income year, assessment type,
correct substantive treatment, original and every amended notice, giving
or service evidence, requested change, earlier applications/objections,
review status and payment position. Keep private identifiers, bank details,
signing credentials and unredacted client records with the reviewer.

Load workflow-base, nf-tax-system and the applicable individual or corporate
workflow base and country references. Preserve their source and period
gates, confirmed profile, refusals, four universal outputs and every
applicable domain output and check. A deadline register or correction
schedule is supporting work, not a completed financial package or a filed
objection. Mandatory unknown facts remain Needs Input; unresolved law
remains held. The reviewer personally handles declarations, submission,
representation and payment.

## Current sources and distinct decisions

The 1936 Assessment Act source is **C193, effective 1 October 2026**. The
latest published TAA compilation is **C226, 27 August-30 September 2026**;
its versions page identifies the unincorporated October Acts 71 and 86.
Their TAA amendment targets do not replace the selected Part IVC or
Division 255 provisions. Use the selected text with that amendment check,
not C226 alone as all-law current. [ASSESS-RECORD]; [ADMIN-RECORD];
[ADMIN-VERSIONS]; [REFORM2]; [OCTOBER]

An amendment request, objection against an assessment, objection against
another decision, late-objection request, ART review and court appeal are
different routes. Part IVC applies where the relevant law grants a right
to object; it does not make every ATO action objectionable. For ordinary
income-tax assessments, section **175A** supplies the right and Part IVC
the process. Sections **173-174** address amended assessments and notice.
[ASSESS]; [ADMIN, sections 14ZL-14ZS][ADMIN]

Section 175A(2) restricts objections against an assessment of no taxable
income or taxable income with no tax payable. Subsection (3) preserves an
objection seeking an **increase** in liability or total tax-offset refunds.
A nil assessment is therefore neither universally objectionable nor
universally excluded. Establish the actual decision and relief sought.
[ASSESS]

## Select the assessment amendment period

Section **170(1)** has different items, qualifications and exceptions. Test
them for the actual income year and taxpayer capacity before selecting a
period. The original assessment date is not automatically replaced by the
most recent amended notice. [ASSESS]

| Selected section 170 branch | Ordinary rule and conditions |
|---|---|
| Item 1: individual | **2 years after the day notice is given**, subject to the business, partnership, trustee, trust-beneficiary, scheme and prescribed-regulation exclusions. An individual address or sole-trader label alone does not establish this branch. |
| Items 2-3: qualifying company or trustee | **2 years** for the specified small/medium business entity, subject to the item's qualifications. Establish the entity and statutory business classification for that year. Do not substitute a corporate tax-rate test. |
| Item 3A: qualifying taxpayer-requested business amendment | Conditional **4-year** application route after the applicable ordinary **2-year** period has ended; see below. |
| Item 4: items 1-3 do not apply | Ordinary **4-year** amendment power, subject to the section's other rules. This is separate from item 3A. |
| Items 5-6 and other special provisions | Fraud/evasion opinion, giving effect to review/appeal, objections and specified other adjustments have their own powers. An ordinary period is not an absolute bar to every later amendment. |

All rows cite section 170, including its complete qualifications, rather
than an unqualified authority summary. Its medium-business definition
modifies the small-business tests using **A$50 million** in place of
**A$10 million** and excludes an entity already a small business. Aggregation,
connections, affiliates and the other statutory tests must be established;
turnover alone is not a classification here. Actual entity-status and
special-regime calculations remain held. [ASSESS, section 170(14)][ASSESS]

### Conditional four-year self-amendment

Item **3A** requires all of the following:

- The individual, company or trust is a small or medium business entity for
  the relevant year.
- The taxpayer applies in the **approved form before the four-year period
  ends**, measured after the day the Commissioner gives the assessment notice.
- The Commissioner could amend within two years under item 1, 2 or 3.
- That two-year period has ended.

Item 3A expresses a power to amend **within four years**, as well as a
requirement to apply before that period ends. Do not assume a last-minute
request permits an amendment after the four-year deadline. The section
170(14) definition of limited amendment period names items 1-4 and specified
subsection (3) periods, not item 3A; subsection (5) must not be treated as an
automatic extension of item 3A. Submit early and verify the actual available
power. This is not an unrestricted four-year ATO review of everything in
a return. Section 170(2A) retains the four-year **original-assessment**
cap for amended assessments under this item. [ASSESS]

Act **135 of 2024**, Schedule 3, commenced **1 January 2025** and applies
to assessments issued **after commencement** for income years starting
**on or after 1 July 2024**. The same Schedule expressly inserted item 3A
into the **two-year objection** branch of TAA section 14ZW. A four-year
self-amendment opportunity does not create a four-year objection period.
[SELF-AMEND, section 2 and Schedule 3][SELF-AMEND]; [ADMIN]

### Prescribed exclusions and retained regulations

The **2025** regulations commence **1 October 2025**. Sections 22-23 apply
them to income years starting at or after commencement and retain the old
**2015** regulations for income years starting before that time, subject
to their transitional rules. Thus an ordinary **2025-26** year starting
1 July 2025 uses retained rules; an ordinary **2026-27** year starts after
commencement. An approved substituted period needs its actual start date.
Do not select the regulation merely from today's calendar date. [REG2025]

Read the complete applicable section **14** table, not only a business
turnover threshold. It includes specified associate transactions, deemed
private-company dividends, ESS, unidentified foreign income, aggregate
foreign-source income, foreign control/non-residence, specified schemes,
connected entities, R&D, rollovers and foreign-resident gains. Each item
has its own taxpayers, conditions and cross-references. Selected examples:

- The associate-transaction branch combines associates, income-tax
  consequences, one of its non-arm's-length/amount/CGT conditions and
  relevance to an assessment. **A$200,000 or more** is inclusive where the
  relevant monetary condition applies; it is not a universal audit trigger.
- Aggregate assessable foreign-source income of the assessed entity,
  affiliates and connected entities has its own **A$200,000 or more** test.
- The connected/affiliate count branch for its specified company/trust
  items uses **10 or more**, including the at-any-time condition.

The 2025 table renumbers provisions and changes specified ESS wording.
Do not describe both tables as identical. Retained 2015 section 27 also
states the 2022 amendments' assessment-date and income-year conditions.
Use the actual applicable text and underlying statutory definitions.
Actual ESS, Division 7A, scheme and other specialised outcomes remain held.
[REG2015]; [REG2025]

### Amended assessments and special powers

Section **170(2)** limits ordinary items 1-4 by the original limited period;
subsection **(2A)** separately limits item 3A. Subsections **(3)-(4)** allow
specified later changes about particular matters, with conditions about
whether the earlier change increased or reduced liability and whether a
taxpayer statement was accepted. They do not restart an unrestricted
whole-return period every time a notice changes. [ASSESS]

Timely approved-form applications and private-ruling applications have
specified treatment under subsections **(5)-(6)**. Subsections **(7)-(8)**
address court orders or written taxpayer consent during an examination.
Subsections **(9)-(12)** and other provisions preserve additional special
powers. Use nf-foreign-income for its selected foreign-offset amendment
route. A request, informal discussion or pending review does not by itself
establish an extension of every relevant deadline. [ASSESS]

## Objections: grounds, scope and time

Section **14ZU** requires the approved form, lodgment within section 14ZW's
period, and the grounds relied on **fully and in detail**. Establish the
correct assessment and lawful result, not just disagreement with the total.
For an amended assessment, section **14ZV** limits the objection to the
alterations/additions or matters relating to them. Earlier private-ruling,
contribution or other linked objections can impose further limits under
sections 14ZVA-14ZVC. [ADMIN]

| Selected objection route | Period to establish from the actual notice |
|---|---|
| Income-tax assessment under section 175A where item 1, 2, 3 **or 3A** applies | **2 years after notice is given** under section 14ZW(1)(aa)(i). |
| Other section 175A assessment | **4 years after notice is given** under section 14ZW(1)(aa)(ii). |
| Ordinary amended assessment in the two/four-year branches | Compare the relevant base assessment period with **60 days after service of the amended notice** and use the period ending later, subject to sections 14ZW(1B)/(1BA) and limited objection scope. |
| A different taxation decision | Apply its actual section 14ZW branch and enabling law. Do not use an income-tax period for GST, FBT, super, penalties, refunds or a private ruling by analogy. |

Keep the original and every later notice in a chronological register.
Section 14ZW(1C) expressly addresses repeated amendments for paragraph
(1B)(c). Actual multiple-notice, special-decision, deemed-service and
interacting-clock cases require a full route-specific check; do not
replace that analysis with the newest notice date. The ATO's **3 July 2026**
page summarises the original-period versus amended-notice comparison;
the operative provisions and the actual facts control. [ADMIN]; [ATO-OBJECT]

If the objection period has expired, section **14ZW(2)-(3)** permits an
objection with a written request to treat it as lodged in time, stating
fully and in detail the circumstances and reasons for the delay. Under
section **14ZX**, the Commissioner decides whether to agree or refuse and
gives written notice. A request is not approval; an ordinary amendment
request is not automatically that late-objection package. A refusal can
have an ART review route, whose application requirements and time must be
verified separately. [ADMIN]

## Delayed decisions and external review

Under **14ZY**, the Commissioner decides an in-time objection and serves
written notice. Section **14ZYA** can permit a written demand for a decision
after the applicable initial **60-day** period, with separate timing where
information is requested by written notice. Only after the statutory
conditions and a further **60 days after that demand** without a decision
does its deemed-disallowance rule operate. It is not automatic success or
ordinary disallowance simply because two months have passed. Special
failure-to-rule/assess objections use their own section 14ZYB branch.
[ADMIN]

Section **14ZZ** distinguishes a reviewable objection decision from other
objection decisions. For a reviewable objection decision, section
**14ZZC(1)** provides **60 days after service** to apply to the ART; its
note identifies the section 19 ART-extension route. The application is
written and has its required reasons/information. A direct Federal Court
appeal against an objection decision has a separate **60-day after-service**
rule in section **14ZZN**. Do not replace either with a generic 28-day ART
rule or apply them automatically to an extension-of-time refusal, appeal
from an ART decision or guidance-and-appeals-panel application. Actual
procedure, fees, practice directions, extensions and representation remain
subject to their own current rules. [ADMIN, sections 14ZQ, 14ZZ-14ZZN][ADMIN]

Sections **14ZZK and 14ZZO** generally limit grounds to the taxation
objection unless the tribunal/court orders otherwise. For an assessment,
the applicant/appellant must prove it is excessive or otherwise incorrect
**and what it should have been**; other decisions have their own burden.
A list of asserted deductions without evidence is not that proof. [ADMIN]

## Payment and recovery remain separate

A due and payable tax-related liability is a debt recoverable under
section **255-5**. A payment deferral under **255-10** requires its own
written notice or published class authority and does not defer giving an
approved form. An instalment arrangement under **255-15** does not itself
vary the due-and-payable time. Record debt, payment, interest and dispute
positions separately; no payment action is taken through this guide.
[PAYMENT]

Sections **14ZZM and 14ZZR** preserve recovery while review or appeal is
pending. The limited small-business taxation assessment stay route under
**14ZZB/14ZZH** requires the actual eligibility, application and order;
it is not an automatic pause. The statutory notes distinguish orders that
secure effective review from permanently changing a due date or remitting
interest. Actual debt management, interest and remission calculations
remain held. [ADMIN]

## Preparation sequence and fictional checks

1. Verify the correct substantive tax outcome and all applicable workflow
   sources before quantifying a correction. Keep unsupported amounts held.
2. Classify the decision, taxpayer/capacity, income year, regulations,
   notice chain and available amendment/objection/review route.
3. Record each clock's legal trigger, given/served date, base period,
   later-notice alternative, applicable day adjustment and evidence.
   AIA section 36 excludes a specified day where the period begins after
   it. Check applicable nonbusiness-day, holiday, office and special-tax-law
   provisions for the actual route; do not count 60 days as 60 business days.
   [AIA]; nf-return-filing supplies selected approved-form controls.
4. Prepare the corrected computation, item-level reconciliation, grounds,
   supporting evidence, action list and required universal/domain outputs
   for professional review. Retain the original return, all notices and
   relevant correspondence through redacted references.
5. Record the reviewer's selected route, confirmed deadline, declaration
   readiness and personal submission action. Reconcile the resulting
   decision/assessment to the reviewed correction and payment entries.

These examples stipulate the legal branch and omit actual service,
calendar and substantive-tax selection:

| Component | Result |
|---|---|
| Eligible item 3A business applies in approved form at 2.5 years, with all conditions and application dates satisfied | The four-year application route can be available; its existence does not extend the ordinary two-year objection period. |
| Same application at 4.5 years | Item 3A's ordinary four-year condition is not met; do not assume all special powers or a late-objection request are unavailable. |
| Only one item 3A condition is unknown | Needs Input; a business label does not supply the missing condition. |
| A first amended notice arrives with 80 days remaining in the applicable base objection period | The later comparison is **80 days**, subject to the actual statutory route and day adjustments. |
| Same facts but only 10 days remain | The amended-notice **60-day** alternative ends later; scope remains limited by section 14ZV. |
| No tax is payable, but the requested objection seeks increased total tax-offset refunds | Test section 175A(3); do not reject solely because the assessment is nil. |
| A monetary regulation condition says A$200,000 or more, and the stipulated amount is A$200,000 | Equality satisfies that monetary limb; all other item conditions still need proof. |
| The relevant connected/affiliate count is 9, then 10 | Nine does not meet that count limb; ten does, subject to taxpayer, period and other requirements. |
| A 2025-26 ordinary income year starts 1 July 2025 | Test retained 2015 regulations under 2025 section 23; do not choose the new table solely because the assessment issues in 2026. |
| A reviewer has requested but not obtained a stay or payment deferral | Retain the established payment position; do not mark recovery paused. |

Check original versus later notices, every qualification and exclusion,
strict application dates, approved form, two versus four-year purpose,
later-of comparison, limited grounds, late-request approval, actual
reviewability, after-service clocks, evidence burden and payment separation.

## Provenance and limits

Checked **18 October 2026**: selected complete section 170, sections 173-175A,
Part IVC provisions, Division 255 payment provisions, current records and
October targets, the self-amendment enactment, both applicable regulation
tables and transitions, AIA time rules and cited ATO pages. Large captures
were read in selected provisions. The current individual ATO page's
specific expiry-date example is not used here; statutory relative periods
and actual giving/service/calendar evidence must establish a case deadline.
Older ruling examples were contextual comparison, not a replacement for
current item 3A or tribunal law. [ATO-AMEND]; [ATO-BUSINESS]

Actual notice expiry dates, specialist amendments, historical/multiple
assessments, rulings, litigation documents, penalty/remission and interest
computations, debt action, form submission and full country requirements
remain subject to their own evidence and professional review. Technical
checks do not establish practitioner sign-off or comprehensive-country
acceptance. This guide remains Tier 2 pending review.

[ASSESS]: https://www.legislation.gov.au/C1936A00027/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_3/document_3.html
[ASSESS-RECORD]: https://www.legislation.gov.au/C1936A00027/latest/details
[ADMIN]: https://www.legislation.gov.au/C1953A00001/2026-08-27/2026-08-27/text/original/epub/OEBPS/document_1/document_1.html
[ADMIN-RECORD]: https://www.legislation.gov.au/C1953A00001/latest/details
[ADMIN-VERSIONS]: https://www.legislation.gov.au/C1953A00001/latest/versions
[PAYMENT]: https://www.legislation.gov.au/C1953A00001/2026-08-27/2026-08-27/text/original/epub/OEBPS/document_2/document_2.html
[SELF-AMEND]: https://www.legislation.gov.au/C2024A00135/asmade/2024-12-10/text/original/epub/OEBPS/document_1/document_1.html
[REG2015]: https://www.legislation.gov.au/F2015L01415/2022-12-09/2022-12-09/text/original/epub/OEBPS/document_1/document_1.html
[REG2025]: https://www.legislation.gov.au/F2025L01060/asmade/2025-09-09/text/original/epub/OEBPS/document_1/document_1.html
[REFORM2]: https://www.legislation.gov.au/C2026A00071/asmade/2026-08-26/text/original/epub/OEBPS/document_1/document_1.html
[OCTOBER]: https://www.legislation.gov.au/C2026A00086/asmade/2026-09-15/text/original/epub/OEBPS/document_1/document_1.html
[AIA]: https://www.legislation.gov.au/C1901A00002/2026-03-28/2026-03-28/text/original/epub/OEBPS/document_1/document_1.html
[ATO-AMEND]: https://www.ato.gov.au/individuals-and-families/your-tax-return/amend-your-tax-return/time-limits-on-amendments
[ATO-BUSINESS]: https://www.ato.gov.au/businesses-and-organisations/preparing-lodging-and-paying/fix-a-mistake-or-amend-your-tax-return/request-an-amendment-to-a-business-or-super-tax-return
[ATO-OBJECT]: https://www.ato.gov.au/individuals-and-families/your-tax-return/if-you-disagree-with-an-ato-decision/object-to-a-decision/what-you-can-object-to-and-the-time-limits

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
