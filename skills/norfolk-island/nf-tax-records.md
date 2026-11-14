---
name: nf-tax-records
description: >
  Establish selected Australian tax-record obligations for Norfolk Island
  taxpayers in 2026. Use for business records, expense substantiation,
  capital gains evidence, mainland-connected GST, electronic retention and
  record failures. Covers distinct five-year clocks, extended review
  periods, delayed credits, the Norfolk acquisition-date exception, loss
  reconstruction and separate administrative penalties. Includes primary
  legislation, current authority guidance and fictional boundary cases.
  Requires the actual entity, obligation, transaction, return and dispute
  dates before selecting a retention period. Preserves applicable workflow
  controls and routes company, employment, superannuation and specialist
  records to their own references. This draft does not authorise record
  disposal or complete the country pack.
jurisdiction: NF
category: international
tax_year: 2026
tax_year_notes: "Selected law and guidance checked 18 October 2026; retention depends on the obligation and actual event, return and review dates"
tier: 2
last_updated: 2026-10-18
version: 0.1
review_status: pending_review
depends_on:
  - workflow-base
  - nf-tax-system
  - nf-return-filing
  - nf-tax-amendments-objections
---

# Norfolk Island: tax records and retention

Establish the person/entity and capacity, business activities, tax and
territorial application, income year, transaction completion, record creation
and receipt, return due and actual lodgement dates, assessments, amendments,
review periods, disputes, asset history and other retention obligations.
Use redacted descriptions and reviewer-held evidence references. Keep tax
identifiers, identity documents, bank details, passwords, encryption keys,
signing credentials and unredacted client records outside agent inputs.

Load workflow-base, nf-tax-system and every applicable domain base and
substantive reference. Preserve their source/period gates, confirmed profile,
refusals, four universal outputs and every required domain output and check.
This reference supports a reviewer-held retention schedule; it does not
complete bookkeeping, a return, a company pack or country coverage. The
reviewer handles actual production, authentication, submissions and disposal.

## Application, sources and record contents

Australian income-tax application follows the Norfolk reforms and exceptions
in nf-tax-system. An island address does not make every Australian indirect
tax, employment or company rule applicable. Use nf-gst for island versus
mainland-connected transactions; an island GST exclusion does not remove
income-tax records. Establish the actual law for each record class first.

The current 1936 Assessment Act compilation is **C193**, effective **1 October
2026**. The latest published 1997 Act **C267** and TAA **C226** compilations
cover **27 August-30 September 2026**. Their records/version grids identify
unincorporated October Acts **71 and 86**. Those amendment targets do not
replace the selected ordinary record provisions below. Read the compilations
with that overlay; an editing date alone is not all-law currency proof.
[1936-RECORD]; [1997-RECORD]; [1997-VERSIONS]; [TAA-RECORD]; [TAA-VERSIONS];
[REFORM2]; [OCTOBER]

**Business records:** section **262A** requires a person carrying on a business
to keep records explaining relevant transactions and acts. Include income,
expenses, underlying documents and particulars of elections, choices,
estimates and calculations, with the calculation basis and method. Full
self-assessment entities also retain the stated return and ascertainment
basis. Records must be in English or readily accessible and convertible
into English, and enable liability to be readily ascertained. PAYG Divisions
**12, 13 and 14** have the section's additional record gate; an ABN exception
does not establish a withholding-record exception. [1936, section 262A][1936]

**Expense substantiation:** Division **900** applies to individuals and
partnerships containing at least one individual, not every entity. Its work,
car and business-travel rules are separate from whether an expense is
substantively deductible. Supplier evidence, work purpose, apportionment,
travel and logbook/odometer records require their relevant rules. A bank
statement alone does not automatically meet written-evidence requirements
or prove a deduction. Receipt exceptions do not remove the requirement that
the expense was actually incurred and deductible. This reference does not
supply every allowance, receipt exception or car-method rule. [1997-10,
sections 900-5 to 900-90][1997-10]; [INDIVIDUAL]

**Capital gains:** section **121-20** covers acts, transactions, events and
circumstances reasonably expected to matter to a past or future CGT gain or
loss. Preserve nature, date, parties, amounts, proceeds, bases, adjustments,
valuations and relevant history. Reconstruct required records that do not
already exist. Use nf-cgt for substantive events and relief. [1997-3]

## Retention: choose the obligation before the clock

All periods below are conditional statutory or guidance rules, not authority
to destroy records at the first computed anniversary.

| Record class and trigger | Selected rule |
|---|---|
| Ordinary business records under 262A(4)(a) | Generally **five years after preparation/receipt or transaction/act completion, whichever is later**. Check special provisions and overlapping obligations. [1936]; [BUSINESS] |
| Section 262A records related to an assessment whose review period is extended under 170(7) | Retain until the **later** of the ordinary period and the extended period of review. Section 262A(4AAA) excludes Schedule 1 TAA records from subsection (4); use their own provision. [1936] |
| Division 900 work evidence/travel, car evidence/odometer or business-travel evidence | Sections **900-25, 900-75 and 900-90** generally require **five years from the return due day**, or **actual lodgement day if later**. Early lodgement does not advance the statutory start. The dispute extension also applies. [1997-10] |
| CGT records under 121-25 | Retain until the end of **five years after it becomes certain that no relevant CGT event or further event can happen**. This overrides the different 262A(4) period. A long-held asset's invoice is not disposable merely because it is old. [1997-3] |
| Covered indirect-tax transactions under TAA 382-5(1) | Retain for the **longest** of five years after completion, the relevant assessment review period, and the applicable **four-year refreshed review period for the latest qualifying amendment** under 155-70(2)(a). [TAA3] |
| Delayed input/fuel credits within 382-5(3)'s exact attribution provisions | Keep the relevant transaction records for at least **five years after the return is given**. Test 29-10(5)/65-5(5), not every credit or BAS. Other applicable clocks remain relevant. [TAA3] |
| Indirect-tax elections, choices, estimates, determinations and calculations | Keep particulars, calculation basis and method. If the law specifies when the item ceases to have effect, retain at least **five years after cessation**; otherwise at least **five years after making it**. Special agency/non-profit records have separate 382-5(5)-(7) conditions. [TAA3] |

Business closure does not itself end retention. The precise Commissioner
notification and finally-ceased/dissolved company exceptions differ between
sections **262A, 121-25 and 382-5**. Establish the actual exception rather than
treating deregistration, inactivity or a proposed liquidation as sufficient.
[1936]; [1997-3]; [TAA3]

### Disputes and information reused later

Under **900-170**, when the ordinary period ends, a related objection,
review/appeal arising from an objection, or request to amend an assessment
extends retention **until the dispute is resolved**. Section 900-170 does
not itself prescribe five more years after resolution. [1997-10]

The ATO individual-record page recommends retaining disputed records for the
later of **five years from lodgement** and **five years from resolution**.
Record that as the authority's guidance, separately from the narrower
statutory mechanism. Do not replace the due-day rule with an early lodgement
or treat the statutory extension as a disposal instruction. Preserve the
records pending reviewer reconciliation of all applicable obligations,
notices, later claims and litigation holds. [INDIVIDUAL]; [1997-10]

The ATO also recommends retaining information reused in a later return until
that later return's review period ends. Loss carry-forwards, borrowing costs,
depreciating assets, pools and rollovers can require substantially longer
records. Its longer-record page describes general asset retention and
special PRRT/minimum-tax periods; those summaries do not replace their
operative provisions or decide an actual disposal date. [LONGER]

### Norfolk CGT exception and other CGT relief

Transitional Act **102-25(3)(b)** removes the acquisition-date record
requirement for an asset to which **102-25(2)** actually applies. All four
conditions remain necessary: historical prescribed-person status because
of Norfolk residence on or before **23 October 2015**, acquisition on or
before that date, no existing pre-CGT status, and the hypothetical
pre-**24 October 2015** gain/loss disregard because of prescribed status.
Residence or an old acquisition date alone is insufficient. [TRANS]

The exception does not waive all capital-gains evidence, substantiate
unknown historical facts or copy the Cocos market-value rule. The subsection
(4) election concerns Cocos subsection (1), not Norfolk subsection (2).
Section **121-30** has separate all-relevant-events disregard conditions,
an exception for specified foreign fixed-trust cases, and no general
rollover shortcut. [TRANS]; [1997-3]

Section **121-35** permits a compliant asset-register entry or combination
with records, preserving all required information. Another registered tax
agent or Commissioner-approved person must certify the transcription in the
register. Keep the underlying entered records for at least **five years
after certification**, and the compliant entry for the applicable retention
period. An ordinary spreadsheet is not automatically a certified replacement
and an AI-generated summary does not supply that certification. [1997-3]

## Formats, production and missing evidence

Current ATO business guidance permits paper/electronic records subject to
integrity, accessibility and reconstruction requirements. Preserve source
meaning, dates, amounts, purpose, parties and the calculation trail. Protect
against alteration and accidental loss, test retrieval, keep suitable backups
and preserve usable exports/system documentation when changing systems.
A readable scan may help; incomplete OCR output is not a complete source
record. Check any requirement to retain the original. [BUSINESS]

Public guidance about ATO access to passwords or encrypted records is not
permission for an agent to obtain credentials or access private accounts.
The reviewer assesses the lawful notice, privilege, production format and
secure response personally. This reference does not decide the validity or
full procedural requirements of an information-gathering notice.

For **Division 900** records still within retention, section **900-175**
permits a written production notice allowing **at least 28 days starting
the day after it is given**, or a longer period. Do not generalise that
minimum to every ATO notice. Section **900-185** can deny the deduction and
permit amendment for non-compliance; it expressly separates this particular
non-compliance from an offence under **8C**. [1997-10]

Under **900-205**, a complete copy can stand as the original. Otherwise,
reasonable precautions against loss/destruction are required. For written
evidence, try to obtain a substitute; inability despite that attempt differs
from a replacement being available but not obtained. Other record classes
have different replacement treatment. Sections **900-195/900-200** contain
evidence-quality and reasonable-expectation relief; neither guarantees a
deduction or excuses a missing substantive entitlement. No fabricated or
backdated evidence is acceptable. [1997-10]

## Penalties and separate record regimes

TAA **288-25** sets a selected administrative penalty of **20 penalty units**
for failure to keep or retain records in the manner required by a taxation
law. Its exceptions include FBT Part X evidentiary documents, Division 900
substantiation documents and the specified education-direction treatment.
Division 900 deduction consequences must not be relabelled as an automatic
20-unit penalty. Actual notices, applicable unit value, remission, education
directions, duplicate/criminal consequences and review rights require their
own rules; use nf-tax-penalties-remission where relevant. [TAA2]

Sections **262A, 121-20/121-25 and 382-5** also contain distinct criminal
**30-unit** provisions and their own conditions. Do not stack or convert
these into an actual fine from this reference alone. Record failure is
separate from an incorrect return, a late return or unpaid tax. [1936];
[1997-3]; [TAA3]

Route company financial records to nf-company-administration and employment
records/payslips to nf-employment-pay. Their company and employee record
rules are not replaced by a tax five-year summary. Use nf-payg-withholding,
nf-super-guarantee and nf-fbt for employer tax/super records; a current
reporting concession is not a general record exemption.

TAA **382-20** has a separate minimum-tax group/entity record regime,
including its **eight-year** preparation/completion clocks and extended
review condition. Identify applicable MNE entities, joint ventures and
permanent-establishment branches before applying it. Specialist groups,
TOFA, transfer pricing, charities, trusts, forestry, capital works, PRRT,
archived periods, corporate destruction and local Norfolk records retain
their own source gates. This reference does not complete those regimes.
[TAA3]; [1936]; [LONGER]

## Reviewer schedule and handling rules

1. Classify each record by entity/capacity, tax, territorial connection and
   purpose. One document may support several obligations.
2. Establish the operative provision and period, including amendments.
   Record dates as verified facts, not inferred from a filename.
3. Retain each applicable base clock, extension, later-use requirement,
   notice and hold separately. A short assessment-amendment period does not
   by itself shorten a different retention duty.
4. Compare all applicable endpoints and unresolved holds. A longer clock
   does not waive an original-format or evidence-content requirement.
5. Add evidence readiness, storage format, integrity/retrieval checks,
   responsible reviewer and the next review action. Mark the conclusion
   retain, hold or reviewer decision required; never auto-delete.

| Missing or disputed matter | Handling |
|---|---|
| Entity, record class, relevant dates or historical Norfolk conditions | Needs Input; no factual default. |
| Applicable source, extension, special regime, notice or legal conflict | Hold the affected conclusion until resolved. |
| Missing receipt, damaged file, missing original or unavailable system | Preserve remaining evidence; apply the actual reconstruction/relief rules, not an assumed exemption. |
| Cash impact is small, nil or unknown | No materiality waiver of a record obligation; flag every disposal, substantiation, penalty and unresolved-source decision for the reviewer. |

Add record-class/obligation, source/period, evidence reference, start event,
base period, extensions, overlapping regimes, later use, guidance distinction,
integrity/retrieval result and reviewer decision to the working paper.
Carry every hold and unresolved fact into the reviewer brief, action list
and sign-off checklist, alongside all applicable domain outputs.

**R-NF-RECORDS-DISPOSAL**: Trigger: an instruction asks this reference to
authorise or execute destruction, overwrite or disposal of records. Output:
"This reference does not authorise record disposal. Preserve the records and
have the reviewer confirm every applicable retention duty and hold."

**R-NF-RECORDS-FABRICATION**: Trigger: an instruction asks to fabricate,
backdate, conceal or manipulate required evidence. Output: "I cannot create
false evidence or conceal required records. Preserve the available material
and refer the issue to the reviewer."

Use the loaded universal/domain refusal catalogues for reviewer removal,
content mismatch and other triggers. Missing source/fact conditions remain
Needs Input unless a defined refusal applies. Do not invent a code.

## Fictional boundary positions and self-checks

These stipulated cases select rules; they are not actual expiry or disposal
authorisations and do not establish a person's deduction or penalty.

| Stipulated facts | Selected result |
|---|---|
| Ordinary business record obtained 1 July 2026; related act completes 18 October 2026; no other facts established | The ordinary five-year start uses the later **18 October 2026** event. Other obligations and extensions remain to be checked. [1936]; [BUSINESS] |
| Division 900 return due 31 October 2026; lodged 1 September 2026 | Use **31 October 2026** as the statutory five-year start. Early lodgement does not advance it. [1997-10] |
| Same due day, but return lodged 20 November 2026 | Use **20 November 2026** as the start. [1997-10] |
| Related objection unresolved when a Division 900 five-year period ends | Section 900-170 extends retention until resolution. Record the ATO's longer guidance separately; preserve the records for reviewer assessment. [1997-10]; [INDIVIDUAL] |
| Covered indirect-tax transaction has stipulated endpoints 31 August 2031 (completion), 30 June 2032 (ordinary review) and 20 January 2033 (qualifying refreshed review) | Select **20 January 2033**, the latest supplied endpoint. A qualifying delayed-credit return may supply an additional clock. [TAA3] |
| Every Norfolk 102-25(2) condition is stipulated met | Apply only the subsection (3)(b) acquisition-date record exception. Preserve other applicable evidence and duties. Unknown prescribed status instead holds the exception. [TRANS] |
| A Division 900 expense receipt is lost; a complete copy survives | Section 900-205 treats the complete copy as the original. Deductibility, scope and other evidence remain separate. [1997-10] |
| The only asserted record failure concerns Division 900 substantiation | Do not automatically impose 288-25's 20 units; its specific exclusion applies. Check the actual deduction and other consequences. [TAA2]; [1997-10] |

Check entity/capacity and territory; every start event; early versus late
lodgement; statutory extensions versus broader guidance; asset history and
Norfolk conditions; all overlapping regimes; original/copy/reconstruction
quality; English/accessibility and system changes; penalty exclusions;
source completeness, privacy and reviewer holds. Do not clear a record for
disposal merely because one clock has elapsed.

## Provenance and outstanding work

Selected provisions and current ATO business/individual guidance were checked
on **18 October 2026**. The CGT transition and current compilation records
reuse still-valid evidence from the earlier Norfolk batches. The public
HTML views of TR 96/7 and TR 2018/2 were read for corroboration only; their
authorised PDF versions were not examined or relied on for this guide.

Version **0.1** adds these selected record rules and boundary examples.
This remains **Tier 2, pending professional review**. It is not a full
bookkeeping, employment, formation, reporting or country companion. No actual
client records, return, notice response, reconstruction claim, remission or
disposal was processed. Specialist records, actual calendars/notices,
privilege, litigation/discovery, local records and complete-country
acceptance remain open.

[1936-RECORD]: https://www.legislation.gov.au/C1936A00027/latest/details
[1936]: https://www.legislation.gov.au/C1936A00027/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_4/document_4.html
[1997-RECORD]: https://www.legislation.gov.au/C2004A05138/latest/details
[1997-VERSIONS]: https://www.legislation.gov.au/C2004A05138/latest/versions
[1997-3]: https://www.legislation.gov.au/C2004A05138/2026-08-27/2026-08-27/text/original/epub/OEBPS/document_3/document_3.html
[1997-10]: https://www.legislation.gov.au/C2004A05138/2026-08-27/2026-08-27/text/original/epub/OEBPS/document_10/document_10.html
[TAA-RECORD]: https://www.legislation.gov.au/C1953A00001/latest/details
[TAA-VERSIONS]: https://www.legislation.gov.au/C1953A00001/latest/versions
[TAA2]: https://www.legislation.gov.au/C1953A00001/2026-08-27/2026-08-27/text/original/epub/OEBPS/document_2/document_2.html
[TAA3]: https://www.legislation.gov.au/C1953A00001/2026-08-27/2026-08-27/text/original/epub/OEBPS/document_3/document_3.html
[REFORM2]: https://www.legislation.gov.au/C2026A00071/asmade/2026-08-26/text/original/epub/OEBPS/document_1/document_1.html
[OCTOBER]: https://www.legislation.gov.au/C2026A00086/asmade/2026-09-15/text/original/epub/OEBPS/document_1/document_1.html
[TRANS]: https://www.ato.gov.au/law/view/print?DocID=PAC%2F19970040%2F102-25
[BUSINESS]: https://www.ato.gov.au/businesses-and-organisations/preparing-lodging-and-paying/record-keeping-for-business/overview-of-record-keeping-rules-for-business
[LONGER]: https://www.ato.gov.au/businesses-and-organisations/preparing-lodging-and-paying/record-keeping-for-business/overview-of-record-keeping-rules-for-business/records-to-keep-longer-than-five-years
[INDIVIDUAL]: https://www.ato.gov.au/individuals-and-families/income-deductions-offsets-and-records/records-you-need-to-keep

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
