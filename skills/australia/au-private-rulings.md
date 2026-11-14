---
name: au-private-rulings
description: >
  Use this guide to prepare an Australian private ruling application under Division
  359 of Schedule 1 to the Taxation Administration Act 1953, on the law at 2 November
  2026 (the 2026-27 income year), for individuals, companies, trusts and super funds.
  Covers whether a private ruling fits, the scheme description and fact-to-document
  matrix, neutral yes-or-no questions, contentions, the ruling period and binding
  effect, the 60-day delay notice and objection, revised and inconsistent rulings and
  the route to object. Trigger on 'private ruling', 'private binding ruling', 'PBR',
  'ATO ruling application', 'Division 359' or 'object to a private ruling'.
jurisdiction: AU
category: international
tax_year: 2026
tax_year_notes: "2026-27"
tier: 2
last_updated: 2026-11-11
version: 0.1
review_status: pending_review
verified_by: pending
license: FSL-1.1-ALv2
depends_on:
  - workflow-base
---

# Australian Private Ruling Applications v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

This guide prepares a draft private ruling application for a registered agent to review, sign and lodge, and explains what happens after lodgment. It loads on top of `workflow-base`.

**Covered:** whether a private ruling is the right product (ss 357-55, 359-5 and 359-35 of Schedule 1 to the *Taxation Administration Act 1953* (TAA)); the scheme description, entity map, questions and contentions; the application requirements (s 359-10 and the ATO form); a ruling's contents, period and binding effect (ss 357-60 to 357-80, 359-20, 359-25, 359-30); revised rulings (s 359-55); the delay notice (s 359-50); and the right to object against a ruling or a delay (ss 359-50(3), 359-60, 359-65, 359-70, 14ZVA).

**Not covered (routed elsewhere):**

- Objections themselves, including lodgment periods, extensions of time and review or appeal: `au-objections`.
- Correcting a lodged return: `au-amending-individual-income-tax-return-period` for an individual; for a company, trust or fund, its own topic guide, or an objection against the assessment through `au-objections`.
- Penalties, reasonable care and reasonably arguable positions: `au-lodgment-deadlines-penalties`.
- The substantive tax answer to each question: the topic guide (for example `au-capital-gains`, `au-div7a` or `au-trust-distributions`).
- Public rulings, oral rulings, and GST, other indirect tax and excise rulings, which have their own rules (refusals below).

**Period coverage.** Law as at 2 November 2026: TAA compilation 227 (in force from 1 October 2026). The Federal Register lists later TAA compilations from 1 July 2027 that were not yet published when read; recheck before relying on this guide after that date.

## Ask the client first

1. The arrangement, step by step, with each date, amount and party, and whether it has begun. A signed contract means the scheme has begun (s 357-80).
2. The documents that evidence it: contracts, deeds, loan agreements, valuations, minutes and financial statements.
3. Every related entity, its relationship to the applicant and its role, and which of them the ruling should cover.
4. The income years or other periods to be covered, and whether an assessment already exists for any of them.
5. The questions the applicant wants answered and its view of each answer.
6. Earlier ATO audits, reviews, rulings, advice or objections on the issue, with reference numbers and dates.
7. The agent's authority to act and registered agent number, and how the application will be lodged.

## The method, step by step

### Key figures

Every figure below was read on 2 November 2026 in TAA Schedule 1, compilation 227, unless another source is named; full URLs are in Sources.

| Item | Value | Source |
| --- | --- | --- |
| Delay notice | The applicant may give written notice requiring the ruling if, at the end of 60 days after the application was made, the Commissioner has neither made the ruling nor declined to make it | s 359-50(1) |
| Extensions of the 60 days | Extended by the days from a request for further information to its receipt, from notice of proposed assumptions to the applicant's response, from notice of third-party information to the applicant's response, and from notice of a valuation referral to notice that the valuer has finished, where the request or notice is given during the 60 day period; overlapping periods count once | s 359-50(2) |
| Objection for delay | If the ruling is not made within 30 days of the notice and has not been declined, the applicant may object under Part IVC, lodging a draft private ruling with the objection | s 359-50(3)-(4) |
| Default period of a ruling | No start time: applies from when made. No end time (other than an indirect tax or excise ruling): ceases at the end of the income year or other accounting period in which it started to apply | s 359-25(3)-(4) |
| Objection against a ruling | Available if dissatisfied, but not once there is an assessment for the income year or other period the ruling relates to, not once withholding tax or mining withholding tax the ruling relates to has become due and payable, and not for an excise ruling once the Commissioner has made a reviewable decision about the duty on those goods | s 359-60(1), (3) |
| Obligations continue | Applying for a ruling or objecting against one does not affect the obligation to lodge a return, or the Commissioner's power to assess | s 357-125; ATO, Applying for a private ruling |

### Step 1: Confirm a private ruling is the right product

1. Each question must concern how a 'relevant provision' applies to the applicant in relation to a specified scheme (s 359-5). The relevant provisions are those listed in s 357-55, including tax, Medicare levy, FBT, franking tax, withholding tax and their administration.
2. The scheme must be real. If it is a proposal, its facts must still be reasonably certain; the ATO does not rule on hypothetical situations (ATO, Applying for a private ruling).
3. Record any ground on which the Commissioner may decline: prejudice to or undue restriction of the administration of a taxation law; a matter already being, or already, considered for the applicant (for example in an audit); certain Pillar Two (Australian IIR/UTPR or DMT tax) questions; how a power would be exercised where the Commissioner has decided or decides whether to exercise it (s 359-35(2)-(3)); further information not given within a reasonable time (s 357-105(2)); and a ruling whose correctness would depend on assumptions about a future event or other matter (s 357-110(1)).
4. If an assessment already exists for a period, the applicant cannot later object against a ruling for that period (s 359-60(3)(a)). The same bar applies once withholding tax or mining withholding tax the ruling relates to has become due and payable (s 359-60(3)(b)), and to an excise ruling once the Commissioner has made a reviewable decision about the duty on those goods (s 359-60(3)(c)). Consider an amendment or objection instead and route it.
5. Disclose every earlier ruling on the matter. If a later private ruling is inconsistent with an earlier private ruling, the earlier one is taken not to have been made only if the Commissioner was told about it when the later ruling was applied for; otherwise the later one is taken not to have been made (s 357-75(1) item 2).

### Step 2: Describe the scheme from the documents

Describe all material facts, transaction dates and the other parties actively involved, without opinion or contested statements (ATO, How to complete the private ruling application form). The ruling will not apply if what is done differs substantially from what was described (ATO, Applying for a private ruling). Build a fact-to-document matrix: every transaction, balance, loan, guarantee, security and related-party dealing that the documents show appears in the facts, or in an exceptions list with the reason it is left out. Add no fact the documents do not support. Include an assumption only where an issue requires a fact that cannot be verified with reasonable certainty, and state why (ATO form guidance).

### Step 3: Map the entities

Record each taxpayer the ruling should cover; the form allows several (ATO form guidance, Section A). A ruling given to the trustee of a trust about the trust's affairs also applies to the beneficiaries (unless it is an indirect tax or excise ruling) and to a replacement trustee (s 359-30).

### Step 4: Frame the questions

Write one issue per question, structured for a yes or no answer, naming the provision where the application gives its own reasoning (ATO form guidance, Section D). Test each question for a premise that assumes the answer or a disputed fact, such as a question that treats a payment as capital when its character is the issue. Rewrite it neutrally or add a preliminary question, and tie each question to the facts and provisions it depends on.

### Step 5: Draft the contentions

For each question give the proposed answer, a short statement of the decision and detailed reasoning that starts with the legislation, case law and the Commissioner's published views and applies them to the stated facts (ATO form guidance, Section D). Record any contrary view. The substantive analysis comes from the topic guide.

### Step 6: Record the period and binding effect

- State the periods the ruling should cover (s 359-25; ATO form guidance, Section C).
- A ruling binds the Commissioner where it applies to the entity and the entity relies on it by acting, or omitting to act, in accordance with it (s 357-60(1)). The entity may stop relying on it, and rely on it again, subject to time limits (s 357-65). The Commissioner may apply the law instead where that is more favourable (s 357-70).
- The ruling must state that it is a private ruling, identify the entity, and specify the scheme and the relevant provision (s 359-20). It covers only that scheme.
- The Commissioner may revise a ruling (other than an indirect tax or excise ruling) only before the scheme has begun and, if the ruling relates to a period, before that period has begun (s 359-55(1)).

### Step 7: Check the application before the agent signs

- The application must be in the approved form (s 359-10(2)). The ATO's private ruling application form or a letter containing the same information may be used (ATO, Applying for a private ruling).
- Check each section of the form: taxpayer details for each taxpayer covered; contact details, with the registered agent number and practice name for a tax professional; earlier ATO interactions with reference numbers; the subject and periods; the questions, facts, assumptions, provisions and reasoning; and the declaration, which is signed for fax or post lodgment and typed for online lodgment (ATO form guidance, Sections A to F).
- Lodge separately from any tax return; returns and activity statements remain due on their usual dates (ATO, Applying for a private ruling).
- Mark each item present, missing or for the agent to decide. Whether to apply, the final facts and questions, the declaration, signing and lodgment are for the agent and the applicant.

### Step 8: After lodgment (information for the reviewer)

The applicant may withdraw the application at any time before the ruling is made (s 359-10(3)). The Commissioner must request any further information needed (s 357-105(1)), must tell the applicant about proposed assumptions and third-party information and give a reasonable opportunity to respond (ss 357-110(2), 357-120), and must give written reasons for declining (s 359-35(4)). Track the 60-day period and its extensions (Cases 1 and 2). On an objection against a ruling, the Commissioner may consider new information; if it shows a materially different scheme, the applicant is asked to apply again and the objection is taken not to have been made (s 359-65). An objection against a ruling also limits later objection grounds against an assessment on the same matter to grounds that neither were nor could have been raised against the ruling (TAA s 14ZVA). Route the objection itself to `au-objections`.

### Permitted factual defaults

| Missing fact | Default | Disclose |
| --- | --- | --- |
| How to count the days in an extension period | Count both the first and last days, which gives the later notice date | A notice given on the earlier count could be premature |
| A document fact whose relevance is unclear | Include it in the scheme description | Omitting a material fact can stop the ruling applying |

No default is permitted for the scheme's facts, the periods, the existence of an assessment or an earlier ruling. Return Needs Input for each.

### Working paper additions

Add to the base outputs: (1) the fact-to-document matrix with its exceptions list; (2) the entity map; (3) the question list with the neutrality test for each; (4) the contentions; (5) the periods; (6) the application checklist; and (7) a timeline of the 60-day period, its extensions and the notice and objection dates.

## Worked cases

All facts are hypothetical. Dates are counted as day numbers from the day the application was made (day 0).

### Case 1: The 60-day period with a further-information request (2027)

An application is made on 1 March 2027 (day 0). The ATO requests further information on 21 March 2027 (day 20) and receives it on 19 April 2027 (day 49). No other extension applies.

```oa-check
name: Private ruling 60-day period with a further-information extension 2027 day numbers
inputs:
  application_day: 0
  statutory_days: 60
  information_requested_day: 20
  information_received_day: 49
  notice_response_days: 30
steps:
  - extension_days: information_received_day - information_requested_day + 1
  - extended_period_last_day: application_day + statutory_days + extension_days
  - earliest_notice_day: extended_period_last_day + 1
  - ruling_window_last_day: earliest_notice_day + notice_response_days
  - earliest_objection_day: ruling_window_last_day + 1
expected:
  extension_days: 30
  extended_period_last_day: 90
  earliest_notice_day: 91
  ruling_window_last_day: 121
  earliest_objection_day: 122
```

On the guide's conservative count, the 60 days end on day 90 (30 May 2027), so a s 359-50(1) notice given on 31 May 2027 (day 91) or later is safe. If the notice is given on day 91 and no ruling is made or declined within the following 30 days (to day 121), the applicant may object from 1 July 2027 (day 122), lodging a draft ruling with the objection (s 359-50(3)-(4)). The reviewer confirms the day count before any notice is given.

### Case 2: Overlapping extensions count once

During the 60 days the ATO requests further information on day 10 (received day 40) and, on day 30, tells the applicant about assumptions it proposes to make (response received day 50).

```oa-check
name: Overlapping private ruling extensions counted once day numbers
inputs:
  information_requested_day: 10
  information_received_day: 40
  assumptions_notified_day: 30
  assumptions_response_day: 50
  statutory_days: 60
steps:
  - information_extension: information_received_day - information_requested_day + 1
  - assumptions_extension: assumptions_response_day - assumptions_notified_day + 1
  - overlap_days: max(0, min(information_received_day, assumptions_response_day) - max(information_requested_day, assumptions_notified_day) + 1)
  - total_extension: information_extension + assumptions_extension - overlap_days
  - extended_period_last_day: statutory_days + total_extension
expected:
  information_extension: 31
  assumptions_extension: 21
  overlap_days: 11
  total_extension: 41
  extended_period_last_day: 101
```

Days 30 to 40 fall in both periods and count once (s 359-50(2)), so the extension is 41 days, not 52.

### Case 3: A question that assumes its answer

A draft asks 'Is the $200,000 capital payment received on 1 May 2027 assessable as a capital gain under Part 3-1?' The payment's character is the issue. Rewrite it as 'Is the $200,000 payment received on 1 May 2027 assessable as ordinary income under section 6-5 of the ITAA 1997?' and, if no, 'Does a CGT event happen to the applicant when it receives the payment?', followed, if yes, by one yes-or-no question naming each CGT event the facts point to, each tied to the facts that decide it.

### Case 4: A trustee ruling and the beneficiaries

The trustee of a discretionary trust applies about the trust's sale of a business. The ruling also applies to the beneficiaries and to any replacement trustee (s 359-30), so list the beneficiaries who may be affected in the entity map. A question about a beneficiary's own affairs still needs that beneficiary's own application.

### Case 5: The assessment has already issued

The applicant's 2025-26 return was assessed in September 2026, and it now wants a ruling on a 2025-26 deduction. A ruling could still be sought, but the applicant could not object against it (s 359-60(3)(a)). Route an amendment request (for an individual, through `au-amending-individual-income-tax-return-period`) or an objection against the assessment (through `au-objections`), and tell the agent why.

### Case 6: The draft omits a document fact

The financial statements attached to a draft show a related-party loan that the scheme description does not mention. Add the loan to the facts, or list it in the exceptions with the reason it is irrelevant, and keep the application in draft for the agent.

## When to refuse or refer

Stop the affected work where a fact, condition or source in this guide is unresolved, and return Needs Input or refer it for qualified review.

| Code | Trigger | Message (verbatim) |
| --- | --- | --- |
| R-AU-PR-1 | A request to decide whether to apply, to sign or lodge, or to give the declaration | 'I prepare the draft only. Whether to apply, the final facts and questions, the declaration, signing and lodgment are for the registered agent and the applicant.' |
| R-AU-PR-2 | A hypothetical or speculative scheme | 'The ATO does not rule on hypothetical situations, and a proposal's facts must be reasonably certain. Settle the facts before drafting.' |
| R-AU-PR-3 | The matter is under audit or review, or already considered by the ATO for the applicant | 'The Commissioner may decline because the matter is already being, or has been, considered for the applicant. Refer the choice of approach to the agent.' |
| R-AU-PR-4 | A dispute about a decision already made, or a period already assessed | 'This is a review of an existing decision, not a ruling. Route to au-objections or au-amending-individual-income-tax-return-period.' |
| R-AU-PR-5 | A GST, other indirect tax or excise ruling, or an oral ruling | 'Indirect tax, excise and oral rulings follow different rules on binding effect, inconsistency and period. Refer to a specialist.' |
| R-AU-PR-6 | A question about Australian IIR/UTPR tax or Australian DMT tax | 'Pillar Two ruling questions have their own grounds for declining and specialist analysis. Refer to a specialist.' |

**Reviewer attention thresholds.** These are this guide's review settings, not statutory figures. Flag for reviewer attention regardless of confidence:

| Threshold | Why |
| --- | --- |
| Tax at stake of $50,000 or more across the periods covered | The ruling's scope and facts need senior review |
| Any assumption in the application | An assumption can lead the Commissioner to decline, or narrow the ruling |
| Any document fact in the exceptions list | An omitted material fact can stop the ruling applying |
| Any period that already has an assessment | The objection right against the ruling is lost for that period |
| A delay notice or delay objection | The day count must be confirmed before either is given |

## Completion checklist

- [ ] Each question concerns a s 357-55 relevant provision and a specified, non-hypothetical scheme.
- [ ] Every ground for declining and every existing assessment was recorded.
- [ ] Every document fact appears in the scheme description or in the exceptions list with a reason.
- [ ] Each question is neutral, answerable yes or no, and tied to its facts and provision.
- [ ] Each contention gives the answer, the authorities and their application, and any contrary view.
- [ ] Earlier rulings on the matter are disclosed.
- [ ] The periods, the entity map and the form checklist are complete, with each item marked present, missing or for the agent.
- [ ] The 60-day timeline uses the s 359-50(2) extensions with overlaps counted once.
- [ ] Objection questions were routed to `au-objections`.

Change log: v0.1 (2 November 2026), first draft from Divisions 357 and 359 of TAA Schedule 1 and TAA s 14ZVA, compilation 227.

## Sources

All read on 2 November 2026; figures and dates rechecked against the same sources on 11 November 2026.

| Source | URL | Read on |
| --- | --- | --- |
| TAA 1953, compilation 227 (from 1 October 2026), Volume 3: Sch 1 ss 357-55, 357-60, 357-65, 357-70, 357-75, 357-80, 357-105, 357-110, 357-115, 357-120, 357-125 and Division 359 (ss 359-5 to 359-70) | https://www.legislation.gov.au/C1953A00001/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_3/document_3.html | 2 November 2026 |
| TAA 1953, compilation 227, Volume 1: s 14ZVA | https://www.legislation.gov.au/C1953A00001/2026-10-01/2026-10-01/text/original/epub/OEBPS/document_1/document_1.html | 2 November 2026 |
| ATO, Applying for a private ruling (last updated 8 October 2026): form or letter, all relevant information, no hypothetical rulings, substantial difference, online channels, lodge separately, returns still due | https://www.ato.gov.au/about-ato/ato-advice-and-guidance/ato-advice-products-rulings/early-engagement-for-advice/applying-for-a-private-ruling | 2 November 2026 |
| ATO, How to complete the private ruling application form (QC100187, last updated 1 August 2025): Sections A to F, yes-or-no questions, facts, assumptions, reasoning, declaration | https://www.ato.gov.au/about-ato/ato-advice-and-guidance/ato-advice-products-rulings/early-engagement-for-advice/applying-for-a-private-ruling/reference-guide-for-private-rulings/how-to-complete-the-private-ruling-application-form | 2 November 2026 |

Not yet confirmed: PS LA 2008/3 and the ATO's service standards for private rulings were not read for this draft; the objection lodgment period for a private ruling is left to `au-objections`. No accountant has reviewed this draft.

Method adapted by its author from the `au-private-ruling-application` skill in ryanduguid/australian-accounting-skills (commit 3e110da). This guide is licensed under FSL-1.1-ALv2, not the OA Guide License; see LICENSING.md.

Topic chosen from the public Ask Nagaris skill list (names only); no Nagaris text was used.

Copyright 2026 Ryan Duguid. From github.com/ryanduguid/australian-accounting-skills, FSL-1.1-ALv2. Copies and adaptations of this file must keep this notice.

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
