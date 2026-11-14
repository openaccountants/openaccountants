---
name: pn-landing-fee-passenger-levy-reference
description: >
  Source-limited Pitcairn reference for the landing fees and passenger head
  levy stated in the Government's June 2026 notice, with selected enabling
  provisions and 5 hypothetical component calculations. Preserves the
  publication-date conflict, age-boundary differences, repealed older fee
  rules and unresolved assessment and collection conditions. Tier 2 draft
  for professional review; incomplete as an operational country skill.
jurisdiction: PN
category: international
tax_year: 2026
tax_year_notes: "The notice says As of 2 June 2026. Selected complete units of Immigration Control Amendment Ordinance No. 2 of 2026 and the 2014 revised principal were read. The amendment copy gives publication on 27 April 2026, while the live official index gives 5 May 2026; commencement is the day after publication. No commencement date is selected. The vessel guide's filename says March 2026 and its fee sections refer to bookings from 1 April 2020. Later law, authoritative status, actual application and collection remain held. These are dated sources, not a general fiscal year or comprehensive 2026 coverage."
tier: 2
last_updated: 2026-11-02
version: 0.2
review_status: pending_review
verified_by: pending
depends_on:
  - workflow-base
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Pitcairn Landing Fee and Passenger Levy Reference (v0.2)

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

Load with `workflow-base`. This reference explains selected sources for PN, the Pitcairn catalogue area. **It is incomplete as an operational country skill.** Its examples illustrate dated fee components, not an actual liability, invoice, return, payment instruction or permission to visit. Unknown law, an unresolved source condition or an incomplete mandatory companion slot is **HOLD**, before any actual classification or calculation.

This is the selected dated reference described in the source and period records below. Actual work remains subject to its complete companion, source conditions, refusal gates and professional review.

### Scope and period

The narrow subjects are landing fees per island and passenger, and the passenger head levy for cruise ships and chartered tour vessels. Pitcairn Island, Henderson Island, Ducie Island and Oeno Island must remain distinguishable. A fee calculation does not grant entry, vessel permission, landing permission or immigration status. [S1, S2]

This guide does not determine visa or work-permit eligibility or application fees, passport-stamping charges, transport and other service charges, a vessel's whole disbursement account, penalties, refunds or appeals. Income tax, sales tax, payroll, social contributions, land tax, customs, formation, reporting and cross-border treatment need separate content. No absence of a tax or general exemption follows from this reference.

The notice's text says 'As of 2 June 2026'; its filename contains 30 April 2026. Neither is accepted as the amendment's commencement date. The amendment copy's first page states publication on 27 April 2026 (Pitcairn time), but the Government's live laws index states 5 May 2026. Section 1(2) specifies the day after publication. Preserve the conflict and establish the legally relevant publication and application before an actual position. Do not choose either calendar date, or treat the fact that June follows both dates as resolving the source's authority. [S1, S2, S5]

## Ask the client first

1. What obligation and period are requested, and is the work a dated source explanation or an actual engagement?
2. Which person, entity, residence, territorial and establishment facts determine the applicable scope?
3. Which activities, transactions, units, values and event dates are supported by redacted records?
4. Which operative sources, classifications, exemptions, amendments and case-specific decisions have been established?
5. Which prior-period, eligibility, input, deduction, credit, payment and other-component records affect this job?
6. Which complete companion content, professional reviewer, current forms and filing or collection directions are available?

### Intake and output extension

Ask once for the obligation and period, reference-only explanation versus actual preparation, reviewer and complete companion, vessel category, proposed calls/islands and landing activity, verified anonymous counts by age band, boundary cases, status/exemption basis, relevant notice, legal application evidence and any concession decision. Do not ask for passport copies, bank details or raw identity records in this reference's arithmetic intake. An aggregate schedule does not replace a manifest that must be supplied securely to the competent authority under applicable law.

Obtain the current assessment or invoice, form and instructions, charge-unit basis, precision/FX treatment, adjustments and payment/collection requirements before actual preparation. Do not contact an official, submit a manifest, make an application or pay a fee merely because this guide describes the process.

The universal 4 logical outputs remain mandatory when a complete companion and all gates permit an engagement: working paper, reviewer brief, action list and review checklist. Extend the working paper with anonymous source ID, vessel/call, island, charge type, established event unit, verified category/age band, count, notice/source/date, applicable amount, concession authority, Needs Input/refusal state, reviewer flag and reconciliation reference. Use formulas for any permitted calculations and retain a separate nil row. Do not populate filing or payment fields from the hypothetical examples.

The brief must show the publication-date conflict, electronic-copy qualification, applicable notice, source resolutions, separate landing and head-levy units, age decisions, concessions, missing components, operational holds and reviewer attention. The action list and checklist must carry the same unresolved conditions. Before computation, a refusal produces only its message and scope trace, as workflow-base requires.

## The method, step by step

### Stated figures and unresolved boundaries [S1](https://www.government.pn/s/2026-04-30-Immigration-Fees-Notice.pdf) [S4](https://www.government.pn/s/GUIDE-FOR-VISITING-VESSELS-as-of-March-2026.pdf)

All amounts in this table are the notice's **NZ$** figures, retained as NZD. They are not a verified payable amount for an engagement. [S1]

| Component in S1 | Literal amount or condition | Actual-use condition  |
| --- | --- | --- |
| Landing, per island per passenger aged 18 years or over | NZD 100 | S4 instead says over 18. An actual passenger aged exactly 18 remains held until the discrepancy and applicable authority are resolved. [S1](https://www.government.pn/s/2026-04-30-Immigration-Fees-Notice.pdf); [S4](https://www.government.pn/s/GUIDE-FOR-VISITING-VESSELS-as-of-March-2026.pdf) |
| Landing, per island per passenger aged over 5 and under 18 | NZD 50 | Establish age at the legally relevant time; do not round or infer an age. [S1](https://www.government.pn/s/2026-04-30-Immigration-Fees-Notice.pdf) |
| Landing, passengers aged under 5 | NIL | This is the landing component only. It is not an age exemption from the passenger head levy. [S1](https://www.government.pn/s/2026-04-30-Immigration-Fees-Notice.pdf) |
| Landing, passenger aged exactly 5 | Not allocated by S1's wording | S4 says 5 and under pay no charge, whilst its preceding line also runs 'to 5 years'. Do not fill S1's gap by analogy or silently harmonise the documents. [S1](https://www.government.pn/s/2026-04-30-Immigration-Fees-Notice.pdf); [S4](https://www.government.pn/s/GUIDE-FOR-VISITING-VESSELS-as-of-March-2026.pdf) |
| Passenger head levy | NZD 2 per passenger | Cruise ships and chartered tour vessels entering the territorial sea to anchor, land passengers, drift and/or circumnavigate any of the 4 islands. Establish vessel category, passenger scope and the chargeable event. Do not substitute the number going ashore. [S1](https://www.government.pn/s/2026-04-30-Immigration-Fees-Notice.pdf) |

The head levy has no express per-island multiplier in S1. Do not copy the landing fee's per-island unit into it. Repeat calls, re-entry, the counting of crew or other status categories, cancelled landings, partial visits, adjustments and refunds require the applicable authority and instructions; an unspecified treatment is not zero. [S1, S2]

S1 separately lists a NZD 20 passport stamp for a passenger not going ashore. S4 describes the landing fee as including immigration clearance and a passport stamp. These are distinct source descriptions, not authority to add a passport fee to every landing or to calculate a whole service account from this guide. Visa, work-permit and other service amounts are outside its computation scope. [S1; S4 ss 11.2, 13.5, 15.2]

### Authority, exemptions and payment context [S2](https://www.government.pn/s/2026-04-27-Immigration-Control-Amendment-Ordinance-as-published.pdf) [S3](https://www.government.pn/s/Cap-12-Immigration-Ordinance-2014-Rev-Ed.pdf) [S4](https://www.government.pn/s/GUIDE-FOR-VISITING-VESSELS-as-of-March-2026.pdf)

S2 inserts s 2D: the Governor, in consultation with the Island Council, may set the listed application, landing, passport and passenger levy charges and must ensure current fees and levies are published on the Government's website. Section 2D(3) expressly gives discretion to waive or reduce **application fees and landing fees**. It does not expressly extend that particular discretion to the passenger head levy or passport fee. Do not infer that no other power can exist, but obtain its actual authority before using it. [S2, p 4]

S3 s 21 contained family entry/landing concessions and a crew landing-fee waiver power. **S2 amendment s 29 expressly repeals that section.** Do not carry those older concessions into a 2026 calculation without a distinct applicable current authority. Equally, do not treat a visa exemption, a permanent-residence status or the notice's 'regardless of visa category' wording as resolving every fee exemption. The current personal, vessel and statutory scope needs a qualified determination. [S2, p 15; S3, p 11]

The new s 4A excludes specified right-of-abode, permanent-residence and s 15(2) categories from the arrival-procedures Part. It is not itself a general fee-exemption table. S2 also changes s 15. Establish each provision's current scope and interaction before applying an arrival requirement or charge to a person. The right-of-abode legislation and individual exemption instruments have not been qualified here. [S2, pp 10, 14; S3, p 10]

The inserted territorial-sea definition distinguishes Pitcairn and Henderson's coastal low-water line from Ducie and Oeno's seaward reef low-water line and lagoons, with the stated 12-nautical-mile measure. Vessel presence, location and activity need appropriate records and qualified classification. A booking address or a statement that no passenger landed does not decide the levy trigger. [S2, amendment s 4, p 2]

For cases to which the arrival-procedures Part applies, s 4C requires the vessel master to notify the Chief Immigration Officer at least **5 days in advance** for permission to call, and prohibits a call without permission and arrangements to pay applicable fees. This is not a universal instruction to remit every fee 5 days before arrival. New s 5(1)(d) contains a specific visa-prior-to-arrival exception for a short-term visitor who departs on the same vessel, stays 14 days or less, applies on arrival and pays applicable fees on arrival unless the Governor authorises other arrangements. These conditions do not establish a general payment deadline for every levy or vessel. [S2, pp 10-12]

S2 s 2E concerns applications for visas and permanent residence: completion of the relevant form, the application fee unless waived and non-refundable application fees. Do not transpose that non-refund rule to a landing fee or head levy. S4 s 12.2 describes a Disbursement Account form and s 13.7 describes invoicing and transfer for cruise/tour-vessel service fees. Their current form, detailed instructions, interaction with the statute and application to each charge remain unverified. No payment destination, account details, universal due date, automatic refund rule or penalty is supplied here. [S2, p 4; S4, pp 5-6]

### Conditional position method [S1](https://www.government.pn/s/2026-04-30-Immigration-Fees-Notice.pdf) [S2](https://www.government.pn/s/2026-04-27-Immigration-Control-Amendment-Ordinance-as-published.pdf) [S3](https://www.government.pn/s/Cap-12-Immigration-Ordinance-2014-Rev-Ed.pdf)

1. **Establish the complete companion and source conditions.** For an actual calculation, require a complete applicable companion meeting workflow-base Section 7, authoritative operative law, the applicable notice and period, resolved publication/commencement evidence and later changes. This reference alone does not pass that gate. Unknown law produces Needs Input or the defined refusal, before classification.
2. **Separate source items and charge units.** Keep vessel/call, island, landing event, passenger category and head-levy event distinct. Reconcile counts to verified underlying records without storing passport copies in the arithmetic schedule. Distinguish a documented nil landing component from missing age or an unresolved charge.
3. **Resolve scope and boundaries.** Establish vessel category, territorial-sea event, applicable personal scope/exemptions and the legally relevant age. Ages exactly 5 and 18, uncertain age, repeat visits or disputed categories need resolution before an actual amount. The examples below do not authorise an assumption.
4. **Establish concessions and other components.** Retain the actual decision and legal basis for a waiver or reduction, including any valid delegation. A concession is not automatic. Separate landing fees, head levy, passport service, visa/application charges and other services; no whole-account total is available if a material component is unresolved.
5. **Apply only established units and figures.** Once the preceding conditions are genuinely closed by appropriate content and evidence, landing arithmetic is chargeable passenger-island units times the matching applicable amount. Head-levy arithmetic is established chargeable passenger units times its applicable amount, using its own confirmed event basis. Never infer the event frequency from the landing formula.
6. **Reconcile and retain the hold where needed.** Keep NZD amounts and source references, assessment or invoice, authorised adjustments, payments and outstanding balance separate. Establish precision, FX, current form/boxes, collector, recipient and timing independently. Missing operation prevents a payable or completed filing output.

## Boundary and exception table

### Defaults and reviewer attention

| Unknown | Permitted default |
| --- | --- |
| Law, date, applicable notice, vessel/person scope or exemption | None; source or scope refusal |
| Age, count, landing event or head-levy frequency | None; Needs Input or the relevant refusal |
| Waiver, reduction or adjustment | None; obtain applicable authority and decision evidence |
| Precision, FX, form, payment, refund or penalty | None; operational refusal |

For any later authorised engagement calculation, flag every computed position for professional review. The internal cash threshold is **NZD 0**, not a statutory threshold or permission to compute. Source and scope holds always take precedence. Retain an individual decision, underlying count evidence, the rejected alternatives and the cash effect only where the law and facts permit that effect to be calculated.

## Worked cases

### Hypothetical component positions

These are **5 fully worked hypothetical component positions**, not complete trip accounts or tests of actual liability. For the arithmetic only, assume the stated June-notice figures, ordinary non-exempt categories, no waiver and exactly the stated chargeable units. Those assumptions do not resolve this guide's source or operational holds for a real case. All ages are synthetic, away from the disputed boundaries. Other charge components remain outside each exercise, not assigned zero. [S1]

| Position | Complete hypothetical input and arithmetic | Component result and limit |
| --- | --- | --- |
| A. Adult landing units | 2 passengers aged 30 and 45; 1 established landing unit each on 1 island. `2 × 100 = 200`. | NZD 200 landing component. It is not a whole vessel account or a head-levy calculation. |
| B. Child landing units | 2 passengers aged 10 and 17; 1 established landing unit each on 1 island. `2 × 50 = 100`. | NZD 100 landing component. No rule for an actual 5-year-old is inferred. |
| C. Under-5 landing unit | 1 passenger aged 3; 1 established landing unit on 1 island. `1 × 0 = 0`. | NZD 0 landing component, explicitly recorded as nil under the assumed notice. No head-levy exemption follows. |
| D. Head-levy units | 80 passengers within the established levy scope on a qualifying cruise vessel; exactly 1 confirmed levy event. `80 × 2 = 160`. | NZD 160 head-levy component. Count is the chargeable passengers, not only those going ashore. No per-island or repeat-event rule is inferred. |
| E. Mixed landing schedule | 2 adults aged 30 and 45, 3 children aged 8, 10 and 16 and 1 child aged 3; 1 established landing unit each on 1 island. `2 × 100 = 200`; `3 × 50 = 150`; `1 × 0 = 0`; `200 + 150 + 0 = 350`. | NZD 350 landing component. All 6 synthetic passenger units are reconciled, including the nil unit. No overall payable amount is determined. |

For the same group visiting another island, create separate landing records and establish whether an additional chargeable landing unit exists. Do not mechanically double the head levy. A record with age exactly 5 or 18 produces `R-PN-AGE` for an actual calculation; it does not receive a guessed figure or a balancing plug.

### Recompute the retained hypothetical positions

The following blocks recompute 2 of the positions above using exactly their supplied premises. They are separate arithmetic exercises. The original classification, period, source, currency, precision and operational holds remain applicable. A nil or negative arithmetic component does not resolve an unknown liability or establish an exemption, refund or amount to pay.

```oa-check
name: PN position A established adult landing units only
inputs:
  adults: 2
  amount: 100
steps:
  - landing_component: adults * amount
expected:
  landing_component: 200
tolerance: 0.000001
```

```oa-check
name: PN position E mixed established landing schedule with explicit nil unit
inputs:
  adults: 2
  children: 3
  under_five: 1
steps:
  - adult_component: adults * 100
  - child_component: children * 50
  - nil_component: under_five * 0
  - landing_component: adult_component + child_component + nil_component
  - units: adults + children + under_five
expected:
  adult_component: 200
  child_component: 150
  nil_component: 0
  landing_component: 350
  units: 6
tolerance: 0.000001
```

## When to refuse or refer

### Topical refusal catalogue

Load the universal refusal catalogue unchanged. The codes below add to it. A refusal records the scope trace and stops the affected actual computation. It does not create a partially classified return or label unknown law as a conservative assumption.

| Code | Trigger | Verbatim output |
| --- | --- | --- |
| `R-PN-COMPANION` | Actual calculation or filing requested without a complete applicable companion meeting all mandatory Section 7 slots | 'This reference is incomplete as an operational companion. I cannot determine an actual charge or prepare filing or payment output until a complete applicable companion and its source conditions are established.' |
| `R-PN-SOURCE` | Authoritative status, publication, commencement, period, applicable notice, amendment chain or legal application unresolved | 'The applicable Pitcairn charging authority or period is unresolved. I cannot classify or calculate an actual charge. Obtain the authoritative text and resolve the source conditions first.' |
| `R-PN-SCOPE` | Personal, vessel, territorial or exemption classification outside established content | 'The applicable person, vessel, territory or exemption treatment is not established by the loaded content. I cannot infer a charge or exemption for this case.' |
| `R-PN-AGE` | Age missing, relevant age date unresolved or an actual passenger at the 5- or 18-year boundary | 'The applicable age treatment is unresolved. I cannot assign a landing amount by rounding an age or reconciling the source wording myself.' |
| `R-PN-UNIT` | Passenger count, island, landing unit, levy event, repeat-call or re-entry basis unresolved | 'The chargeable units are not established. I cannot replace them with bookings, people going ashore or an assumed per-island levy multiplier.' |
| `R-PN-CONCESSION` | Waiver, reduction, old family/crew concession or adjustment requested without current authority and evidence | 'The proposed concession or adjustment lacks established current authority or decision evidence. I cannot apply it or substitute a guessed higher amount for the missing law.' |
| `R-PN-OPERATION` | Actual assessment, invoice, precision, form, collection, refund, payment or penalty treatment unresolved | 'The operational treatment is not established. I cannot determine a payable amount or produce completed filing or payment instructions from this reference.' |

## Filing and payment

Actual filing, submission, payment and collection remain subject to the specific source conditions, complete companion content and refusal gates in this reference. Use the retained dated administration and form comparisons for explanation; they do not supply missing current directions or authorise an external action.

## Completion checklist

Current format revision: v0.2, edited 2 November 2026. This migration preserves the earlier draft's dated source content and revision records. It does not refresh law or confer professional review. Carry all outstanding source and operational holds through the working paper, reviewer brief, action list and review checklist.

### Self-check additions

1. Complete applicable content and authoritative period/notice evidence exist before an actual calculation. Retrieval and editing dates have not become legal currency dates.
2. Both publication dates are retained until substantively resolved. No current-law conclusion follows solely from the bounded negative search.
3. Old s 21's family and crew provisions have not been carried forward after S2's express repeal. A visa or arrival-procedure exemption has not become a general fee exemption.
4. The exact 5- and 18-year issues are held. A nil landing component has not removed a passenger from the head-levy count by analogy.
5. Counts reconcile by source, island, activity, person category and established event. Head levy does not inherit the landing fee's unit or frequency.
6. Every concession has the appropriate legal basis and decision evidence. S2 s 2D(3) has not become an automatic head-levy or passport waiver.
7. The 5-day notification rule, payment arrangements before a call and the specific short-term-visitor arrival condition remain distinct. No universal payment deadline or non-refund rule has been invented.
8. Other fee and service components, forms, precision, FX and collection remain separate and unresolved where not established. No incomplete component schedule is presented as a whole payable account.
9. Any permitted workbook recalculates without errors; the brief, action list and checklist agree. Source resolution, arithmetic checks and professional sign-off remain distinct.

### Currency and revision

Version 0.1, edited 1 November 2026. Public source files freshly retrieved on 31 October 2026 UTC. This initial source-limited reference records the notice, selected enabling units, administrative contrasts and hypothetical component arithmetic. It has not been tested on an actual engagement, prescribed form, assessment, submission or payment. It does not establish comprehensive PN topic coverage or professional verification.

General reference only. Verify authoritative applicable law and current administration with a qualified professional before reliance. Keep every unresolved condition as Needs Input or the defined refusal.

## Sources

The table records the original reading evidence. A retrieval or capture is not a reading date. A reading bound is not an exact day. The retained library below controls extent, host, translation and source qualifications; formatting adds no new legal-source reading.

| Source | URL | Read on |
| --- | --- | --- |
| S1. Immigration Control Ordinance 2006: Fees and Levies | https://www.government.pn/s/2026-04-30-Immigration-Fees-Notice.pdf | Exact reading day unrecorded; public source files retrieved 2026-10-31 UTC; specified units read |
| S2. Immigration Control Amendment Ordinance 2026, No. 2 of 2026 | https://www.government.pn/s/2026-04-27-Immigration-Control-Amendment-Ordinance-as-published.pdf | Exact reading day unrecorded; public source files retrieved 2026-10-31 UTC; specified units read |
| S3. Immigration Control Ordinance, Chapter 12, Revised Edition 2014 | https://www.government.pn/s/Cap-12-Immigration-Ordinance-2014-Rev-Ed.pdf | Exact reading day unrecorded; public source files retrieved 2026-10-31 UTC; specified units read |
| S4. Guide for Visiting Vessels, file labelled as of March 2026 | https://www.government.pn/s/GUIDE-FOR-VISITING-VESSELS-as-of-March-2026.pdf | Exact reading day unrecorded; public source files retrieved 2026-10-31 UTC; specified units read |
| S5. laws index | https://www.government.pn/laws | 2026-10-31 UTC; bounded independent read-only check |
| S5. policies and forms | https://www.government.pn/government/policies-annexes-and-forms | 2026-10-31 UTC; bounded independent read-only check |
| S5. notices | https://www.government.pn/government/notices | 2026-10-31 UTC; bounded independent read-only check |

### Primary source library and limits

| Source | Text actually read | Qualification and limits |
| --- | --- | --- |
| **S1. [Immigration Control Ordinance 2006: Fees and Levies](https://www.government.pn/s/2026-04-30-Immigration-Fees-Notice.pdf)** | Complete 1-page notice, read natively and against its original image. Fresh HTTPS PDF with verified TLS on 31 October 2026 UTC: 129,184 bytes, SHA256 `a7c1ee82920e4f6a2134a42b5404baf250b112833da3d7a89d0886b9cc45d6a9`. | Officially hosted copy. It describes fees set by the Governor in consultation with the Island Council under s 2D(1). Making, publication history, later settings, actual assessment and the age gaps are not fully resolved. |
| **S2. [Immigration Control Amendment Ordinance 2026, No. 2 of 2026](https://www.government.pn/s/2026-04-27-Immigration-Control-Amendment-Ordinance-as-published.pdf)** | Officially hosted 22-page scan, 3,289,022 bytes, SHA256 `25d10d6820042353b228e021a15bacfe703a40aad53c803ea8cc18952340b5d2`, freshly retrieved with verified TLS. Complete relied units checked against original images: title, making/publication annotations and ss 1-2 on p 1; complete inserted definitions in amendment s 4 on pp 1-2; new s 2D and s 2E on p 4; ss 4A-4C on pp 10-11; new s 5 on p 12; changes to s 15 in amendment ss 20-24 on p 14; repeal of old s 21 in amendment s 29 and new delegation s 18 on p 15. | All pages were OCR processed for location, but only the named units are qualified here. The remaining immigration, enforcement and explanatory provisions are not a complete legal review. Visible signature and date annotations are not authentication or proof resolving the index conflict. |
| **S3. [Immigration Control Ordinance, Chapter 12, Revised Edition 2014](https://www.government.pn/s/Cap-12-Immigration-Ordinance-2014-Rev-Ed.pdf)** | Fresh verified-TLS 12-page PDF, 181,905 bytes, SHA256 `156338a2e3d235f3891af9130fdd0632c1eace348637dfe6fde0b790b999ad62`. Selected complete native units: ss 1-2 on pp 2-3, s 15 on p 10 and s 21 on p 11. | Historical principal context, not a current consolidation. Intervening amendments and all provisions are not qualified. In particular, the older s 21 cannot be treated as current after the express repeal in S2. |
| **S4. [Guide for Visiting Vessels, file labelled as of March 2026](https://www.government.pn/s/GUIDE-FOR-VISITING-VESSELS-as-of-March-2026.pdf)** | Fresh verified-TLS 10-page PDF, 279,242 bytes, SHA256 `1bc64e76f9ae52bca0af72436dd6892f8c2bb5b5db7a7c6c82141353d8a10551`. Complete selected guidance sections 11-13 on pp 5-6 and section 15 on p 6 read natively and against both images. | Administrative guidance, not a substitute for S2 or a later fee setting. Its booking-date language, age wording and service-invoicing directions must not silently replace the June notice or establish its current application. Other safety, marine, immigration and service provisions are outside the qualified extent. |
| **S5. Government [laws index](https://www.government.pn/laws), [policies and forms](https://www.government.pn/government/policies-annexes-and-forms) and [notices](https://www.government.pn/government/notices)** | Independent read-only check on 31 October 2026 UTC: relevant current ordinance entry and legislative disclaimer, fee-notice locator and complete 12-entry notices list. | No body-hashed capture of these pages is supplied. The laws page warns that electronic legislation lacks official status. No later immigration amendment or fees notice was located in the bounded check; that is not an exhaustive current-law determination. |

These are source explanations, not professional sign-off. For actual use, obtain authoritative applicable text and resolve the publication discrepancy, amendment chain and notice status through substantive legal evidence. A reviewer's approval alone does not establish missing law.

Not yet confirmed: the complete operative chain and requested-period application, unresolved source conditions and administrative directions, exact reading days where unrecorded and professional verification. Retain every specific evidence gap, refusal and filing hold identified above.

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
