---
name: nf-imports
description: "Classify selected Norfolk Island import, customs-entry and biosecurity obligations for 2026. Use for island cargo, low-value consignments, imports from the mainland, advance goods notices, permits or biosecurity charge questions. Covers the affirmative ordinary-duty exclusion, applied customs law, current entry thresholds, notice timing and exceptions, Norfolk goods conditions, and separate charge and fee exemptions. Includes primary legislation, current amendments, authority guidance and fictional boundary checks. Preserves valuation, goods classification, form and release requirements, and separates mainland return movements and private costs. This source-cited reference leaves actual clearance, special regimes and complete country and workflow outputs open."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/nf-imports"
  jurisdiction: "NF"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# Norfolk Island: imports, customs entry and biosecurity costs v0.1
> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

Establish each movement's origin, destination, transport, first arrival,
goods, value, consignor/consignee, purpose and event date. A mainland sale
and an island import have separate tax and border questions. Use `nf-gst`
for the supplier's GST export conditions and other mainland connections.

Load `workflow-base`, `vat-workflow-base` and the Norfolk scope guide.
Preserve their source and period gates, confirmed profile, refusals,
universal outputs and applicable domain outputs and checks. This reference
supplies selected import parameters; it does not fill every country slot
or establish a complete VAT, customs or financial deliverable. Missing
mandatory facts remain Needs Input and unresolved rules remain held.
Nothing here authorises payment, lodging a declaration or collecting
personal identifiers, bank details or real client records.

## Ask the client first

- Direction of movement: into Norfolk Island from the mainland or overseas, or from Norfolk into the mainland.
- Postal or non-postal, and the statutory value of the whole consignment.
- Ship or aircraft, the first estimated arrival time and, for sea, the voyage length.
- What the goods are, and any permit or biosecurity condition that attaches to them.

## The method, step by step

### Key figures

| Item | Figure | Applies to | Source |
|---|---|---|---|
| Low-value entry exception, non-postal goods | Value not exceeding A$1,000 | One person's consignment to another on one ship or aircraft, not prescribed goods | [CREG](https://www.legislation.gov.au/F2015L00375/2026-07-01/text) |
| Low-value entry exception, postal goods | Value not exceeding A$1,000 | Consignment through the Post Office, not prescribed goods | [CUSTOMS](https://www.legislation.gov.au/C1901A00006/2026-09-29/text) |

### Ordinary customs duty and the law that still applies

Customs Tariff Act 1995 section 3A excludes Norfolk Island. Section 7 of
the Customs (Norfolk Island) Ordinance 2016 applies the Customs Act 1901,
Customs Regulation 2015, Customs (International Obligations) Regulation
2015 and other customs regulations, as in force from time to time, except
to the extent they deal with customs duties. ABF confirms that ordinary
customs duties are not assessed on goods imported into Norfolk Island.
This is affirmative territorial support; it does not depend on a shipment
being worth less than a mainland duty threshold. [TARIFF]; [ORD]; [ABF]

Customs Act section 6 ordinarily excludes external territories. Its
Norfolk application comes through the Ordinance, which commenced on
**1 July 2016**, rather than its May registration date. Section 8 generally
reads references to Australia or the Commonwealth in the applied laws as
references to the Territory, subject to the Ordinance's modifications.
Keep that applied-law reading separate from the unmodified mainland leg.
[CUSTOMS]; [ORD, sections 2, 7 and 8][ORD]

The Ordinance retains customs reporting, entries, classification and
approved forms with specified modifications in its three Schedules. Under
section 7(4), an actual Norfolk approved form or statement prevails over
the parallel Commonwealth one. Schedule 2 omits Regulation Part 13, which
concerns agents and customs brokers. That omission does not remove every
fee or authorisation requirement. Nor does the customs-duty exclusion
delete all of Part VIII for every non-duty purpose. [ORD]; [CREG]

ABF treats mainland-to-island and island-to-mainland movements as separate
export/import movements, including associated vessel or aircraft reporting.
An island purchase is not proof of Norfolk origin for mainland preference.
Obtain the applicable origin, mainland duty/GST, reporting and biosecurity
rules for that return leg. This guide does not select a preference or
clearance merely because the goods were bought or stored on Norfolk.
[ABF]; [DAFF]

### Entry thresholds are conditional procedural rules

As applied, Customs Act section 68 distinguishes goods needing an entry
for home consumption or, where permitted, warehousing from specified
exceptions. An entry for home consumption is communicated by an import
declaration. The following selected exceptions do not abolish other
reporting, restricted-goods, biosecurity or release requirements. [CUSTOMS,
section 68][CUSTOMS]

| Selected section 68 branch | Conditions to retain |
|---|---|
| Postal goods, paragraph (1)(e) | Other than prescribed goods; included in a consignment through the Post Office from one person to another; value not exceeding **A$1,000**, subject to any different prescribed amount. |
| Non-postal goods, paragraph (1)(f) | Other than prescribed goods; one person's consignment to another; all carried in the same ship or aircraft; value not exceeding **A$1,000** under current Regulation 26. |
| Personal or household effects, paragraph (1)(d) | Accompanied or unaccompanied passenger/crew effects, subject to subsection (4)'s quantity and trading exclusions. |

The current non-postal amount is A$1,000, replacing the Act's A$250
fallback. Section 68(5) requires valuation under Division 2 of Part VIII;
an invoice total or a currency conversion chosen without that analysis
does not settle the statutory value. Establish the actual consignment,
valuation method and prescribed-goods position before using an exception.
Do not split, combine or relabel consignments to manufacture eligibility.
[CUSTOMS]; [CREG, section 26][CREG]

Section 68(4) excludes from the personal-effects branch unreasonable
quantities for the person's own use and goods known or believed to be for
sale or trading. Regulation 25 separately exempts certain **accompanied**
goods that would be personal/household effects but for subsection (4),
where their value does not exceed the prescribed amount. Therefore,
failing the personal-effects test is not by itself proof that every other
entry exception fails. No actual traveller's concession is determined
here. [CUSTOMS]; [CREG, section 25][CREG]

Section 71A permits documentary or electronic import declarations and
retains powers to require the underlying permission. Section 71B has a
distinct processing-charge liability and exemption mechanism. This guide
does not establish whether that charge applies to a particular Norfolk
entry or select a current amount. Check the applied laws, charge law,
exemption instrument, current Norfolk forms and authority instructions
before quoting a processing cost or preparing an entry. [CUSTOMS]; [ORD]

### Biosecurity applies, including movements from the mainland

Biosecurity Act 2015 section 7(2), together with Biosecurity Regulations
2026 section 4, extends the Act, other than its separately extended ballast
water chapter, to Norfolk Island. The new Regulations commenced on
**1 October 2026**. The consequential Regulations repealed the 2016
Regulation on that date. Do not treat the old Regulation as the current
default or confuse registration with operative commencement. [BIO];
[BREG]; [REMAKE]

DAFF explains that these movements are managed like international border
movements because the territories have distinct pest and disease status.
The Norfolk goods determination section 4 applies to arrivals from both
outside Australian territory and another part of Australian territory.
Mainland origin, a customs-entry exception and a duty exclusion each
leave the separate biosecurity question open. [DAFF]; [GOODS]; [AMEND]

#### Advance notice of goods

Act section 120 requires a notice for the covered unloading of goods,
subject to statutory and prescribed exceptions. Regulation 13 supplies the
Norfolk branch. It covers goods arriving by aircraft or vessel from outside
the relevant territory, including another part of Australian territory,
and intended for unloading there. Section 120(5)'s contravention includes
the condition that no other person gives a compliant notice; appointing
an agent without confirming delivery is not evidence that notice was
given. [BIO]; [BREG]

Regulation 13(2) prescribes the operator, relevant slot charterers, freight
forwarders, persons responsible for arranging the movement and customs
brokers. Record who will provide the compliant notice and obtain its
acknowledgement. Use the Director's approved form, delivered in writing,
including electronically, to a biosecurity official or customs officer,
or through the Commonwealth technology made available for that purpose.
A customs entry alone does not prove this separate notice is complete.
[BIO, section 120(2)–(5)][BIO]; [BREG, section 13][BREG]

The notice includes the information known or reasonably expected to be
known under Regulation 13(3): aircraft/vessel and flight/voyage; loading,
first arrival and unloading places; estimated arrivals; notifier contact;
waybill/bill of lading; description and origin/manufacture; personal-effects
status; applicable container, bulk, hazard and transhipment information;
packages/containers; and animal permit, species and intended location
details where applicable. Confirm the approved form's complete current
fields. Keep personal data with the authorised reviewer, outside this
repository and any agent evidence bundle. [BREG]

| Transport to Norfolk Island | Regulation 13(5) latest notice time |
|---|---|
| Aircraft | **2 hours before** estimated arrival at the first island landing place. |
| Vessel, voyage at least 60 hours | **60 hours before** estimated arrival at the first island port. |
| Vessel, voyage strictly shorter than 60 hours | **24 hours before** estimated arrival at the first island port. |

Use actual estimated arrivals with time zones and preserve evidence of
delivery by the deadline. The short-voyage branch is strictly less than
60 hours. A voyage exactly 60 hours long stays in the 60-hour branch.
These are goods-notice times, not a substitute for conveyance reporting,
import entry, permits or authority to unload/release. [BREG]

Regulation 14 has exceptions, including baggage other than baggage
containing animals, animal reproductive material or fertile eggs, and
postal consignments to which Customs Act paragraph 68(1)(e) applies.
It also addresses waste and specific exposed-conveyance, fish, return and
Torres Strait cases with their own conditions. A low-value **non-postal**
consignment is not automatically within the postal exception. Do not infer
that all baggage is exempt or that a notice exception removes goods
conditions or reportable-incident requirements. [BREG, section 14][BREG]

#### Goods conditions and permits

Act sections 173 and 174 distinguish prohibited goods from conditionally
non-prohibited goods. Sections 176 and 177 provide the relevant permit
application route. A conditional import may require a granted permit;
an application, a fee exemption or a broker booking is not a permit.
[BIO]

The Register displayed the Norfolk determination's C10 compilation through
30 September 2026 when checked. Read it with the **1 October 2026**
amendments in Schedule 2 items 17 to 23 of F2026L01292. These update movement
references and import definitions from the **2021** general goods
determination as in force from time to time. The old compilation's 2016
definition references alone do not supply current meanings. Its Register
record lists a changed sunset of **1 October 2031**, not automatic repeal
on 1 October 2026. Recheck current amendments and any incorporated list
when classifying actual goods. [GOODS]; [AMEND]; [GOODS-RECORD]

For Division 1 goods, section 7 generally requires a permit or compliance
with an applicable alternative-condition branch. Its mixed-goods rules
matter: a component with a permit-only requirement can require a permit
for the composite goods. Where alternatives exist, subsections (4) and
(5) distinguish an alternative for the complete goods from satisfying
each component's conditions. Section 6 has class definitions and
exceptions, and other Divisions impose further conditions. No particular
food, seed, machinery, animal or other commodity is approved here.
[GOODS, sections 4–7][GOODS]; [AMEND]

Select Norfolk Island and the actual goods scenario in DAFF's BICON
process, retaining the current determination, incorporated definitions and
lists, treatment/certification and permit conditions. DAFF's guidance
requires a permit for goods not covered in the determination and says it
must be granted before the goods leave the mainland. Obtain the full
applicable conditions before dispatch; this reference makes no actual
permit application or release decision. [DAFF]

### Separate biosecurity tax charges, fees and other costs

The Customs and General Biosecurity Charges Imposition Regulations 2016
remain separate instruments, each at the **1 October 2026** compilation.
The former is confined to charges that are duties of customs for
Constitution section 55; the latter to charges that are neither customs
nor excise duties. Do not add both instruments' tables as if they were
two compulsory charges for the same matter. [BC]; [BG]

Both instruments' section 10(2) expressly makes their section 9 charge
**not payable** for biosecurity matters relating to goods brought or
intended to be brought into Norfolk Island; specified proposed/approved
biosecurity arrangements there; or conveyances there. Apply the precise
branch to the matter. Their charge amounts and annual indexation do not
override an applicable exemption. This guide does not quote old base
amounts as current payable Norfolk rates. [BC]; [BG]

There is also a distinct **fee** exemption. Biosecurity Regulations 2026
section 85(4) says a fee must not be charged for activities relating to
goods brought/imported into Norfolk, conveyances there, assessment of a
Norfolk import-permit application, specified arrangement approvals for
goods/conveyances/other things brought there, and activities carried out
there. Record which statutory branch applies to each proposed fee.
An exemption for a tax charge and an exemption for a fee need separate
source entries, even when both produce no payable Commonwealth amount.
[BREG]

This does not establish that freight, storage, treatment providers,
brokers, port/airport services or local-government charges are free.
Establish any separate contract or statutory basis before computing them.
Norfolk exemptions do not automatically carry over to a mainland import
leg. Regulation 105 also preserves the old cost-recovery provisions for
charges already due and payable before commencement and addresses old
charges becoming payable afterwards. Do not erase an historical debt by
applying a new instrument without its transition. [BREG]; [ABF]

## Worked cases

### Fictional cases and checks

These are component and routing checks, not actual clearance results.
All times below use the same stipulated time zone and all low-value cases
stipulate that the statutory value and other stated conditions are met.

| Fictional facts | Component result |
|---|---|
| Non-postal goods from one person to another, same ship, not prescribed goods, statutory value A$1,000 | At the section 68(1)(f)/Regulation 26 boundary; this selected entry exception applies. Other obligations remain to be checked. |
| Same facts but A$1,000.01 | The selected low-value exception fails; investigate other branches and required entry. Ordinary Norfolk duty is not thereby created. |
| Two invoices of A$600 and A$450 are stipulated to be one statutory consignment, with no valuation adjustments | A$1,050 exceeds the threshold. Each invoice is not a separate A$1,000 allowance. |
| A$900 non-postal air cargo | A customs-entry exception alone does not establish a Regulation 14 biosecurity-notice exception. |
| Air arrival estimated at 16:00 on 20 October 2026 | Goods notice due no later than 14:00 that day, unless a valid exception applies. |
| Sea arrival 12:00 on 20 October; voyage 60 hours | 60-hour branch: notice due 00:00 on 18 October. |
| Same arrival, voyage 59 hours 59 minutes | Short-voyage branch: notice due 12:00 on 19 October. |
| Permit assessment is for goods imported into Norfolk | Identify the Regulation 85(4)(c) fee exemption; do not treat the absence of a fee as a permit grant. |
| Goods are imported from Norfolk into the mainland | Reopen mainland duty, GST, origin and biosecurity conditions. Island purchase alone establishes no preference. |

Check territory and direction; event and compilation dates; all entry
exception conditions and statutory value; approved form priority; actual
notifier, delivery evidence and first estimated arrival; the strict
short-voyage boundary; current goods definitions, mixed components and
permits; separate tax-charge/fee exemptions; and historical debts.
An unknown goods condition or form is a hold, not a default clearance.

### Recomputed checks

```oa-check
name: Two invoices forming one consignment
inputs:
  invoice_1: 600
  invoice_2: 450
  threshold: 1000
steps:
  - consignment: invoice_1 + invoice_2
  - over_threshold: consignment - threshold
expected:
  consignment: 1050
  over_threshold: 50
```

```oa-check
name: Sea arrival 12:00 on 20 October; notice lead time by voyage length
inputs:
  arrival_hour: 468
steps:
  - long_voyage_due_hour: arrival_hour - 60
  - short_voyage_due_hour: arrival_hour - 24
expected:
  long_voyage_due_hour: 408
  short_voyage_due_hour: 444
```

## When to refuse or refer

- Do not lodge a customs entry or biosecurity notice; this skill gives the thresholds and clocks only.
- Refer to the biosecurity authority for permits; the absence of a fee is not a permit.
- Do not split a single statutory consignment into invoices to stay under A$1,000.

## Sources

Read on dates are Ryan Duguid's reads of each page when he wrote this skill (October 2026). Each label is the reference tag used in the text above.

| Source | URL | Read on |
|---|---|---|
| TARIFF. Read for: Ordinary customs duty and the law that still applies; Sources and remaining coverage | https://www.legislation.gov.au/C2004A04997/2026-07-04/text | 2026-10-18 |
| ORD. Read for: Ordinary customs duty and the law that still applies; Entry thresholds are conditional procedural rules; Sources and remaining coverage | https://www.legislation.gov.au/F2016L00736/asmade | 2026-10-18 |
| CUSTOMS. Read for: Ordinary customs duty and the law that still applies; Entry thresholds are conditional procedural rules; Sources and remaining coverage | https://www.legislation.gov.au/C1901A00006/2026-09-29/text | 2026-10-18 |
| CREG. Read for: Ordinary customs duty and the law that still applies; Entry thresholds are conditional procedural rules; Sources and remaining coverage; Key figures | https://www.legislation.gov.au/F2015L00375/2026-07-01/text | 2026-10-18 |
| ABF. Read for: Ordinary customs duty and the law that still applies; Separate biosecurity tax charges, fees and other costs; Sources and remaining coverage | https://www.abf.gov.au/help-and-support-subsite/CustomsNotices/2026-11.pdf | 2026-10-18 |
| BIO. Read for: Biosecurity applies, including movements from the mainland; Sources and remaining coverage | https://www.legislation.gov.au/C2015A00061/2026-09-16/text | 2026-10-18 |
| BREG. Read for: Biosecurity applies, including movements from the mainland; Separate biosecurity tax charges, fees and other costs; Sources and remaining coverage | https://www.legislation.gov.au/F2026L01194/asmade | 2026-10-18 |
| REMAKE. Read for: Biosecurity applies, including movements from the mainland; Sources and remaining coverage | https://www.legislation.gov.au/F2026L01195/asmade | 2026-10-18 |
| BC. Read for: Separate biosecurity tax charges, fees and other costs; Sources and remaining coverage | https://www.legislation.gov.au/F2016L00723/2026-10-01/text | 2026-10-18 |
| BG. Read for: Separate biosecurity tax charges, fees and other costs; Sources and remaining coverage | https://www.legislation.gov.au/F2016L00727/2026-10-01/text | 2026-10-18 |
| GOODS. Read for: Biosecurity applies, including movements from the mainland; Sources and remaining coverage | https://www.legislation.gov.au/F2016L01061/2019-09-25/text | 2026-10-18 |
| AMEND. Read for: Biosecurity applies, including movements from the mainland; Sources and remaining coverage | https://www.legislation.gov.au/F2026L01292/asmade | 2026-10-18 |
| GOODS-RECORD. Read for: Biosecurity applies, including movements from the mainland; Sources and remaining coverage | https://www.legislation.gov.au/F2016L01061/latest/details | 2026-10-18 |
| DAFF. Read for: Ordinary customs duty and the law that still applies; Biosecurity applies, including movements from the mainland; Sources and remaining coverage | https://www.agriculture.gov.au/import/goods/external-territories | 2026-10-18 |

### Sources and remaining coverage

Checked on **18 October 2026**: selected current Tariff Act section 3A;
Customs Act sections 6, 68 and 71A–71BA; the full Norfolk Ordinance and
selected current Customs Regulation provisions; selected Biosecurity Act
and 2026 Regulations provisions; both charge regulations' scope and
Norfolk exemptions; selected goods-determination sections with the October
amendments; and the authority guidance below. Whole Acts and commodity
tables were not all reviewed. ABF Notice 2026/11 is dated 21 April 2026;
DAFF's external-territories page was updated 28 January 2026 and is read
with the current legislation, not as a later legislative compilation.

Actual valuation, prescribed goods, approved Norfolk forms, complete
conveyance/cargo/entry/release procedures, commodity conditions, other
costs, offences/remedies, mainland preferences, production excise and local
charges remain to be established. Other tax, payroll, formation, reporting,
cross-border, property, compliance and special-regime gaps remain open.
No practitioner sign-off, model engagement benchmark, complete-domain
output or comprehensive-country acceptance is claimed.

Not yet confirmed: ato.gov.au and the Norfolk Island Regional Council site (nirc.gov.au) refused scripted access on 14 November 2026, so their pages were not re-read for this import; figures taken from them rest on Ryan Duguid's October 2026 read. Hours in the second check count from 00:00 on 1 October 2026 (hour 468 is 12:00 on 20 October; 408 is 00:00 on 18 October; 444 is 12:00 on 19 October), as derived from Ryan's examples. ABF and DAFF pages were not re-read for this import.

[TARIFF]: https://www.legislation.gov.au/C2004A04997/2026-07-04/text
[ORD]: https://www.legislation.gov.au/F2016L00736/asmade
[CUSTOMS]: https://www.legislation.gov.au/C1901A00006/2026-09-29/text
[CREG]: https://www.legislation.gov.au/F2015L00375/2026-07-01/text
[ABF]: https://www.abf.gov.au/help-and-support-subsite/CustomsNotices/2026-11.pdf
[BIO]: https://www.legislation.gov.au/C2015A00061/2026-09-16/text
[BREG]: https://www.legislation.gov.au/F2026L01194/asmade
[REMAKE]: https://www.legislation.gov.au/F2026L01195/asmade
[BC]: https://www.legislation.gov.au/F2016L00723/2026-10-01/text
[BG]: https://www.legislation.gov.au/F2016L00727/2026-10-01/text
[GOODS]: https://www.legislation.gov.au/F2016L01061/2019-09-25/text
[AMEND]: https://www.legislation.gov.au/F2026L01292/asmade
[GOODS-RECORD]: https://www.legislation.gov.au/F2016L01061/latest/details
[DAFF]: https://www.agriculture.gov.au/import/goods/external-territories

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `nf-imports` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/nf-imports. If neither is available, confirm every figure against the official source pages cited above before relying on it.
