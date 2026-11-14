---
name: je-pillar-two
description: >
  Jersey Pillar Two reference for the October 2026 statutory snapshot,
  distinguishing Multinational Corporate Income Tax from Income Inclusion Rule
  tax. Covers entity/reporting classification, annual de minimis elections,
  selected income, loss and credit mechanics, registration, returns, payment,
  amendments, penalties and appeals. Use for Jersey MCIT, IIR, GloBE reporting
  or multinational constituent entities. Preserves 2025/2026 law differences,
  dated OECD recognition and conditional administrative concessions. Hypothetical
  calculations require established statutory inputs. Complete GloBE computation,
  safe harbours, delegated instruments and operational filing remain specialist
  gaps. This source-cited draft awaits professional review and is incomplete
  as an operational corporate companion.
jurisdiction: JE
category: international
tax_year: 2026
tax_year_notes: "2026 statutory snapshot; fiscal years beginning on or after 1 January 2025, with separate 2025 MCIT version"
tier: 2
last_updated: 2026-10-15
version: 1.2
review_status: pending_review
depends_on:
  - workflow-base
  - corporate-income-tax-workflow-base
---

# Jersey Pillar Two: enacted rules and administration

## Scope and source periods

Jersey's Multinational Corporate Income Tax (MCIT) is a domestic corporate income tax. Income Inclusion Rule (IIR) tax is a separate parent-entity obligation. MCIT is not a qualified domestic minimum top-up tax (QDMTT); do not apply QDMTT safe-harbour consequences to it or add the two liabilities mechanically. The [technical guidance](https://www.gov.je/TaxesMoney/IncomeTax/PillarTwo/Pages/PillarTwoGuidance.aspx) explains these distinctions and states that MCIT does not use the substance-based income exclusion.

This is a partial statutory reference with hypothetical calculations, not a full GloBE computation or operational corporate companion. Load the workflow bases. Missing eligibility, source rules, producer amounts, rounding or required outputs hold the affected amount and the complete financial package. Do not turn an incomplete scope check into a nil assessment or a filing-ready result.

[*Multinational Corporate Income Tax (Jersey) Law 2025*, Article 3](https://www.jerseylaw.je/laws/current/l_7_2025) and [*Multinational Taxation (Global Anti-Base Erosion – IIR Tax) (Jersey) Law 2025*, Article 4](https://www.jerseylaw.je/laws/current/l_8_2025) apply for fiscal years beginning on or after 1 January 2025. Each imports Model Rule 1.1.1 with the applicable Rules 1.1.2 and 6.1 modifications and requires at least one constituent entity located in Jersey at some time in that fiscal year. [Model Rules 1.1 to 1.4](https://www.oecd.org/content/dam/oecd/en/publications/reports/2021/12/tax-challenges-arising-from-digitalisation-of-the-economy-global-anti-base-erosion-model-rules-pillar-two_eed81a23/782bac33-en.pdf), published 20 December 2021, require at least EUR 750 million UPE consolidated revenue in at least two of the four fiscal years immediately preceding the tested year. For each relevant non-twelve-month year, adjust that threshold proportionately; detailed merger/demerger and proration application still needs the governing provisions. An MNE group includes the required foreign entity/PE dimension. Consolidation includes the specified size, materiality and held-for-sale omissions, and a qualifying standalone entity/foreign-PE group has its own branch. Constituent PEs are treated separately; excluded entities are not constituent entities. Do not infer scope solely from incorporation or the absence of prepared consolidated accounts. Article 10.1 defines the fiscal year by the UPE consolidated accounting period, with a calendar-year branch for deemed statements.

The current MCIT consolidation applies from 1 January 2026. Its Article 1 names the OECD commentary published 9 May 2025, and Article 7(2) uses its Chapter 10 paragraphs 148.2 and 148.3 securitisation definition. The [2025 version](https://www.jerseylaw.je/laws/current/l_7_2025_20251231) uses earlier commentary/June 2024 guidance references. The technical page still quotes that older securitisation reference; use the applicable statutory version. The IIR consolidation applies from 1 January 2025 and has its own commentary definition. A statement of policy intention does not amend either Law.

The [OECD updated central record](https://www.oecd.org/content/dam/oecd/en/topics/policy-sub-issues/global-minimum-tax/updated-central-record-for-purposes-of-the-global-minimum-tax.pdf), approved 11 May 2026 and current to 1 May 2026, lists Jersey's IIR Law with **transitional qualified status effective 1 January 2025**. This is dated recognition, not permanent status or an independently verified October 2026 list. Recheck the applicable jurisdictions and periods for an actual IIR ordering decision.

## MCIT entities and reporting responsibility

[MCIT Articles 4 and 7 to 9](https://www.jerseylaw.je/laws/current/l_7_2025) apply modified location rules, including Jersey flow-through/reverse-hybrid and permanent-establishment branches. A Jersey constituent entity is located in Jersey and is not an investment entity, insurance investment entity or securitisation entity under the applicable definitions. Do not equate every Jersey-incorporated entity, fund or trust with a Jersey constituent entity.

Article 8 selects the Jersey constituent entity that is the ultimate parent; otherwise the **sole** Jersey constituent entity that is an intermediate parent; otherwise an entity designated by the Comptroller, having regard to the group's nomination. Multiple Jersey intermediate parents do not authorise choosing one automatically. The [registration guidance](https://www.gov.je/TaxesMoney/IncomeTax/PillarTwo/Pages/MCITRegistration.aspx) describes a single group registration with valid Jersey TINs; the separately declared reporting entity must not also be duplicated in the constituent-entity section. Existing authority for another tax does not appoint an MCIT agent: use the specified MCIT authority process.

[Article 23](https://www.jerseylaw.je/laws/current/l_7_2025) requires the reporting entity of an **in-scope** group to register each Jersey constituent entity, even where an exemption election removes MCIT chargeability. Initial registration is before the first applicable fiscal year ends. A later entrant must be registered before the end of six months beginning on entry; registered-information changes, including departure, must be notified no later than six months after the change. Apply the actual statutory starting wording and prescribed form/manner. Entity exclusion and annual exemption are different branches.

## Annual MCIT exemption and ordinary income tax

[MCIT Articles 5 and 6](https://www.jerseylaw.je/laws/current/l_7_2025) require an annual election and either Condition A or B. No automatic exemption follows from a small tax estimate.

| Branch | Required boundary |
|---|---|
| Condition A | Average Jersey GloBE revenue below EUR 10 million **and** average Jersey GloBE income/loss is a loss or below EUR 1 million, subject to Rule 5.5 and Article 5(5)'s modifications |
| Condition B | Article 12(1)(d) income less losses **before Article 20 relief** is below GBP 100,000 |
| Election | Written notice in the prescribed form/manner on or before the fiscal year's return due date; effective for that fiscal year and the ordinary assessment year in which it ends |

The [Minimum Threshold Order, Article 1](https://www.jerseylaw.je/laws/current/ro_77_2024) fixes GBP 100,000 from 1 January 2025. Equality fails Condition B. A low post-carryforward amount or tax liability is not its statutory test. For A, Rule 5.5.2 averages the current and two preceding fiscal years, omitting an earlier year where the rule's no-constituent-entity-with-GloBE-revenue/losses condition is met. It does not use the four-year revenue-scope window. Apply Article 5(5)'s substituted pre-Article-20 income measure and omission of Rule 5.5.3(b). Rule 5.5.4 removes stateless and investment entities from the relevant election/computations. Establish the included entities, comparable currencies and period data before averaging; do not substitute one year's headline sales.

The [current return guidance](https://www.gov.je/TaxesMoney/IncomeTax/PillarTwo/Pages/HowToCompleteMCITReturn.aspx), updated 30 September 2026, directs the reporting entity to select Condition A and/or B in the MCIT return and complete the legal declaration. An electing exempt group need not complete the later calculation fields or submit supporting de minimis calculations with that election; eligibility must still be established and evidenced. The guidance says each relevant Jersey constituent entity then files the relevant ordinary Income Tax Law return. This process does not remove MCIT registration.

[Income Tax Law Articles 120AB and 120AC](https://www.jerseylaw.je/laws/current/l_29_1961) separately establish relevant-MNE-entity ordinary-tax exemption and disapply specified returns for the qualifying assessment year/period, including part-year apportionment. Establish chargeable-group/entity status and periods before applying them. Generic ordinary-company return guidance and MCIT registration alone do not settle those conditions.

## MCIT income, loss and credit sequence

Use [Articles 11 to 22](https://www.jerseylaw.je/laws/current/l_7_2025), with their incorporated Model Rules:

1. Establish each Jersey constituent entity's GloBE income or loss under Rules 3.1 to 3.5 and the applicable Article 13 transition/restructuring/distribution provisions.
2. Aggregate incomes and deduct aggregate losses under Article 12(1)(d). This is the pre-Article-20 amount used for Condition B.
3. Apply available Article 20 losses without reducing income below zero; a negative aggregate produces nil MCIT net GloBE income. Articles 21 and 22 distinguish qualifying acquired ITL losses from combined carryforward and prevent amounts already relieved or reflected through Rule 9.1 being counted again.
4. Calculate 15% of established MCIT net GloBE income. Reduce that amount by Article 14 creditable tax, comprising Article 15 basic covered taxes and any eligible Article 17 blended-CFC credit. Credits are not deductions in the GloBE income base.
5. Establish the covered-tax inclusions/exclusions and allocation before using a credit. Article 15 excludes specified PE/CFC/hybrid/reverse-hybrid/distribution taxes and MCIT itself, with the specified transparent-entity inclusion. An ordinary foreign tax payment is not automatically creditable.
6. Where Article 16 applies, Article 17's creditable blended-CFC amount is the lower of the group's qualifying blended-CFC amount and **7.5% of the group's MCIT net GloBE income**. Do not apply the cap separately to each entity or substitute a generic credit for all foreign tax.

The technical page's comparison table can blur credits and income adjustments; the statute supplies their separate steps. These selected rules do not reconstruct all GloBE adjustments, exclusions, deferred taxes, transition rules, restructurings or joint ventures. Unestablished inputs, an apparent negative tax result or a refund require further applicable sources; no unsupported cap, refund or loss attribute is inferred.

## Payments, returns and currency

[MCIT Articles 18, 19, 24 and 25](https://www.jerseylaw.je/laws/current/l_7_2025) require:

| MCIT obligation | Statutory rule |
|---|---|
| Instalment | Five months after fiscal year end; 50% of the reporting entity's reasonable estimate |
| Return | Twelve months after fiscal year end, containing the self-assessment, each Jersey constituent entity's financial statements and other reasonably required information in prescribed form/manner |
| Balance | Actual Article 11 liability **less instalment paid**, due on the return due date |

A changed estimate means the balance need not equal 50% of final liability. The [payment guidance](https://www.gov.je/TaxesMoney/IncomeTax/PillarTwo/Pages/PayMultinationalCorporateIncomeTax.aspx), updated 29 April 2026, requires the previous working day where payment falls on a weekend, bank or public holiday. Its nominal 31 May 2026 example is not a verified adjusted instruction. Verify the holiday calendar and applicable date rules before supplying a dated payment action.

The current return/payment guidance uses the ultimate parent's consolidated accounting currency for GloBE amounts and GBP payment, with the Bank of England rate for the last accounting-period day to convert liability. Return guidance uses a different date for acquired ITL loss conversion: the first accounting-period day, or the acquisition date for an entity acquired during the period. Establish the source rate, quote convention and prescribed treatment where a rate is unavailable; do not use one rate/date for every item.

The [return guidance](https://www.gov.je/TaxesMoney/IncomeTax/PillarTwo/Pages/HowToCompleteMCITReturn.aspx) requires constituent-entity income/loss, financial statements and economic-substance details, and identifies supporting calculation, loss, credit, joint-venture and election sections. It specifies financial statements as PDF, maximum 30 MB per entity, and optional calculation support as XLSX, maximum 5 MB. [Submission guidance](https://www.gov.je/TaxesMoney/IncomeTax/PillarTwo/Pages/CompleteMCITreturn.aspx) routes returns through the Pillar Two Platform. Portal operation, attachments and payment are not tested or performed here.

## IIR is a separate liability and return

[IIR Articles 6 to 12](https://www.jerseylaw.je/laws/current/l_8_2025) disapply UTPR Rules 2.4 to 2.6 and 9.3. Article 10's Jersey qualifying entity must be non-excluded, own an interest in a non-Jersey constituent entity at some point in the fiscal year and meet the ultimate-parent, intermediate-parent or partially-owned-parent branch. The intermediate-parent branch examines qualified IIR application above it; the partially-owned-parent branch has its own ownership exception. Do not replace the complete statutory test with a general assertion that any parent in a qualified-IIR country removes Jersey obligations.

Article 11 calculates GloBE income, adjusted covered taxes, attributed top-up tax and allocable shares under its specified Rules. Article 12 charges the qualifying entity's total allocable share, payable by the IIR return due date. No IIR amount is derived from MCIT liability alone.

[IIR Articles 13 to 20](https://www.jerseylaw.je/laws/current/l_8_2025) distinguish annual notification, GloBE information return (GIR) and IIR self-assessment. Notification identifies whether the reporting entity is the qualifying entity and, where it is not, the intended GIR filer and relevant jurisdictions. A qualifying entity's GIR duty is subject to Rule 8.1.2. That relief requires a GIR conforming to Rules 8.1.4 to 8.1.6 already filed by the UPE or designated filing entity, located in a jurisdiction with a qualifying automatic-GIR-exchange agreement effective with Jersey for the reporting fiscal year. Intention, agreement signature or foreign qualified-IIR status alone is insufficient. Rule 8.1.3 retains filer identity/location notification; Jersey's separate IIR return/payment and statutory notification must also be checked. Other-language GIRs need an English translation. Article 17 Model Rule elections are made by written notice in the GIR. The separate IIR return includes self-assessment and reasonably required information.

The notification, GIR and IIR return/payment deadlines are **18 months after the first applicable fiscal year ends**, then **15 months** for later fiscal years. These are not the MCIT twelve-month deadline. Verify filing-relief, forms, exchange relationships and date adjustments for the actual period.

## Amendments, defaults, penalties and appeals

[MCIT Articles 26 to 38](https://www.jerseylaw.je/laws/current/l_7_2025) and [IIR Articles 21 to 33](https://www.jerseylaw.je/laws/current/l_8_2025) create separate routes from ordinary income tax:

- Taxpayer amendments: within five years beginning with the applicable return due date, in prescribed form/manner.
- Authority amendments: ordinarily two years, or five for careless inaccuracy, from the statutory return-submission date. That date is the latest of due date, actual submission and relevant taxpayer amendment. Deliberate inaccuracy and specified later foreign-tax changes permit amendment at any time. The foreign-tax-change request route is not a general extension for every late error claim.
- Missing-return default assessments: no appeal against that assessment; a return for the same fiscal year within twelve months beginning with the date on which notice of that assessment is given displaces it, subject to the authority's amendment powers. Default assessments can be amended/additional at any time.
- MCIT registration/change failures: GBP 3,000 for one or more specified failures by the reporting entity in a fiscal year. MCIT late return: GBP 300 basic plus the statutory GBP 100 complete-month increments after the initial one-month period, capped at GBP 1,200.
- IIR notification failure: Comptroller-determined penalty up to GBP 3,000. Each GIR or IIR late-return failure: GBP 1,000 basic plus statutory GBP 1,000 complete-month increments after the initial one-month period, capped at GBP 12,000. Do not merge two distinct filing failures into one.
- Materially inaccurate MCIT/IIR returns: each incorrect material particular has a behaviour-based penalty. Ordinary careless conduct is up to 30% of the statutory difference; deliberate conduct 30% to 100%. Qualifying voluntary admission outside discovery/likely imminent discovery changes these to up to 10%, or 10% to 80%, respectively. Do not choose a discretionary point in a range automatically.
- Penalty payment is no later than 40 days after service, subject to the statutory appeal provision. Written exceptional-circumstances waiver applications for specified registration/notification/filing penalties have their own 40-day service-based period. The waiver is discretionary and does not extend to every inaccuracy penalty.
- Appeals against the listed amendment, rejection, penalty or waiver-refusal decisions use the 40-day period beginning with the day notice is given. A penalty/waiver appeal makes that penalty notice ineffective until final determination or withdrawal. Do not infer a general tax collection stay or a default-assessment appeal.

MCIT Article 30 and IIR Article 25 condition late-payment simple interest on Regulations specifying a rate. No operative rate instrument is verified here; no amount is calculated and no absence of liability is inferred. MCIT Article 40 enables QRTC Regulations. The technical guidance says no QRTC currently operates, but a complete absence of later legislation is not established by that statement or a search.

## Conditional concessions and remaining technical work

Model Rule 1.5.1 excludes the defined governmental entity, international organisation, nonprofit organisation and pension fund, plus an investment fund or real-estate investment vehicle **that is the UPE**. Rule 1.5.2's ownership extensions require at least 95% of **value** through eligible excluded owners plus the exclusive/almost-exclusive holding/investment or ancillary-activity condition, or at least 85% of value plus substantially all the specified excluded dividend/equity income. Pension services entities are excluded as qualifying owners in these branches. Rule 1.5.3 permits an opt-out for a 1.5.2 entity as a five-year election. Article 10.1's definitions impose further cumulative conditions; a label or percentage alone is insufficient. Trace the ownership path, activities/income and any election. Jersey's Article 7 exclusions are a separate layer.

Its employee-benefit-trust easement keeps registration but dispenses with specified own-income MCIT/ordinary returns only where all registered Jersey constituent entities are EBTs and no MCIT liability arises. Its JPUT concession requires income entitlement as it arises and at least 75% of gross asset value in the specified rental immovable property/ancillary assets. The stated fiscal-year boundary is **ending before 31 December 2026**. Do not include an end date of 31 December 2026 or treat an intention to legislate from January 2027 as enacted law. Other exclusions still need analysis.

Other Model Rule elections require their actual eligibility and duration rules. The technical guidance asks for notification by/with the MCIT return, confirmation of GIR consistency from the ultimate/intermediate parent and supporting analysis. Its listed elections described as unlikely to be required are not categorically prohibited. IIR elections follow its separate Article 17. Complete election, safe-harbour, excluded-entity, restructuring, joint-venture and return-notice mechanics remain open.

## Hypothetical worked positions

These use established statutory stage inputs and exact arithmetic. They do not validate how accounting data becomes those inputs, operational rounding or consumer execution.

1. **Condition B before carryforward.** Established Article 12(1)(d) income is GBP 120,000; eligible Article 20 losses are GBP 50,000. Income after relief is GBP 70,000, but Condition B fails because the pre-relief amount is not below GBP 100,000. Condition A and all other facts are separate. At GBP 100,000 pre-relief, B still fails; GBP 99,999 meets B's amount test but needs a valid election. Sources: Articles 5, 6, 12 and 20 and Threshold Order.
2. **Selected MCIT stages.** In a chargeable group with no other relevant adjustment, established Article 12(1)(d) income GBP 1,000,000 less available Article 20 losses GBP 200,000 gives GBP 800,000 MCIT net GloBE income. At 15%, the gross amount is GBP 120,000. Established Article 15 basic covered taxes GBP 20,000 and no eligible blended-CFC credit give GBP 100,000 MCIT. Sources: Articles 11 to 15 and 20. No IIR amount follows from this example.
3. **Group CFC cap.** On established GBP 800,000 MCIT net GloBE income, the cap is 7.5% x GBP 800,000 = GBP 60,000. If Article 16 applies and the qualifying group blended-CFC amount is GBP 70,000, the creditable amount is GBP 60,000. With established basic covered taxes GBP 20,000, total creditable tax is GBP 80,000 and the selected Article 11 result is GBP 40,000. Sources: Articles 11 and 14 to 17. All eligibility/allocation is assumed established, not inferred from a foreign tax bill.
4. **Changed estimate.** A reasonable MCIT estimate GBP 100,000 gives a GBP 50,000 instalment. Final established liability GBP 120,000 leaves GBP 70,000 before other payments, not half the final liability. Five-/twelve-month date rules and holiday adjustment remain to be mapped. Sources: Articles 18, 19 and 24 and payment guidance.
5. **Registration and reporting entity.** An in-scope group has two Jersey intermediate parents and no Jersey ultimate parent. Article 8's sole-intermediate-parent branch fails; Comptroller designation is required. An eligible annual exemption election can remove chargeability but not Article 23 registration. Establish the entity and prescribed election process; do not choose a parent or skip registration by default. Sources: Articles 5 to 8 and 23.
6. **Different late-return amounts.** Assume the statutory initial period has elapsed and the verified count is two additional complete months, with a relevant notice and no waiver/appeal. MCIT: GBP 300 + 2 x GBP 100 = GBP 500. Each relevant IIR/GIR filing failure: GBP 1,000 + 2 x GBP 1,000 = GBP 3,000. Calendar counts are assumed facts; the two Laws' caps and separate duties still apply. Sources: MCIT Article 33 and IIR Article 28.

7. **Condition A uses three years.** Assume the group is in scope, every relevant included entity/year and currency conversion is established, no omission under Rule 5.5.2 or exclusion under 5.5.4 applies, and the comparable current/two-prior-year values are supplied. Jersey GloBE revenue EUR 9 million, EUR 10 million and EUR 8 million averages EUR 9 million. The corresponding Article 12(1)(d) pre-Article-20 income amounts EUR 0.9 million, EUR 1 million and EUR 0.8 million average EUR 0.9 million. Both strict average limits pass; an annual election is still required. This is not the separate two-of-four global revenue test. Sources: MCIT Articles 5 and 6 and Model Rule 5.5.

## Intake, holds and reviewer checks

Obtain group structure and ownership, ultimate-parent accounts/period/currency, revenue history and short-year/restructuring facts, all entity/location/exclusion facts, reporting designation, registration/change dates, ordinary-tax periods, elections, GloBE computations, tax allocations and loss history, payment evidence, notices and service dates. Missing facts and upstream amounts remain unknown, never zero or an assumed exemption.

| Code and trigger | Verbatim response |
|---|---|
| R-JE-MNE-1: incomplete entity, group, period or election conditions | Needs Input: establish the Jersey Pillar Two scope, entity classification, period and election before determining this obligation. |
| R-JE-MNE-2: unsupported GloBE, tax-credit, loss or IIR allocation input | Needs Input: obtain the governing computation and source evidence before calculating the affected MCIT or IIR amount. |
| R-JE-MNE-3: missing rate, date adjustment, instrument or recognition evidence | Needs Input: verify the applicable instrument, period and source condition before producing this amount or deadline. |
| R-JE-MNE-4: incomplete mandatory corporate companion or output package | Needs Input: the complete Jersey Pillar Two companion and financial package are not ready. |

Every amount and scope/election/filing decision requires reviewer attention, regardless of cash value; this is review policy. Extend the reviewer brief with source versions, entity hierarchy, exemption/ordinary-tax interaction, computation lineage, loss/credit reconciliation, currency dates, registration and separate MCIT/IIR/GIR calendars. Recheck pre-relief thresholds, group-level credit caps, non-duplication, final-liability balance and statutory notice starting dates across all outputs. Required missing rules or outputs hold the complete package.

## Sources and revision

The source library and remaining coverage are in references.md. Current MCIT, its separate 2025 version, IIR Law, Threshold Order and selected official technical/registration/return/payment guidance were read on 15 October 2026. The administrative guide is November 2025 version 1.0 and does not replace later return instructions. Version 1.2 replaces preliminary-only statements with selected enacted mechanics and explicit source conflicts. Selected 2021 Model Rules scope, exclusion, averaging, GIR-relief and definition provisions were checked using native text and targeted OCR for image-based numbering. Complete computation/incorporated Rules, operational outputs, safe harbours, delegated instruments, later recognition and practitioner sign-off remain unverified.

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
