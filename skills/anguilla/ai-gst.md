---
name: ai-gst
description: >
  Anguilla General Services Tax for ordinary domestic taxable services,
  using the enacted 2025 legislative baseline. Covers registration tests,
  the positive rate, invoice arithmetic, supported input credits, monthly
  returns and payment. Use for Anguilla GST, service invoices, taxable
  turnover, GST registration or input tax. Separates Goods Tax from services
  tax and identifies imported services as a separate obligation. Includes
  hypothetical positions, source checks and reviewer controls. Later
  amendments and complete specialised classifications remain unresolved.
  This source-cited draft requires period-specific legal verification and
  professional review before calculating an engagement liability or acting.
jurisdiction: AI
category: international
tax_year: 2025
tax_year_notes: "Enacted 2025 baseline; later amendments require verification"
tier: 2
last_updated: 2026-10-12
version: 0.2
review_status: pending_review
verified_by: pending
depends_on:
  - workflow-base
---

# Anguilla General Services Tax: ordinary services

## Scope

Establish the applicable period law and supply classification before calculating GST. This companion supplies substantive rules for an ordinary domestic taxable service, an ordinary registration test and a supported domestic input credit. Load `workflow-base` for procedure, outputs and universal refusals. The reviewer receives working papers for professional review.

Specialised supplies, exports, exemption schedules, accommodation, mixed activities beyond the stated allocation rule, imported-service valuation, tariffs, assessments, penalties and refunds require their complete applicable provisions. Goods Tax, Social Security and Universal Social Levy are separate obligations. No general absence of income, corporate, withholding or capital gains tax is established here.

## Period coverage and source currency

The figures below describe the [*General Services Tax Act, 2025*][G1] as enacted, with commencement on 1 August 2025 under s 107. The captured Act and regulations were read on 11 October 2026. A complete later amendment chain has not been verified. The editing date does not certify current 2026 liability.

Before an engagement calculation, record the requested period, operative statutory version, applicable amendments and regulations, registration notice and evidence establishing the ordinary supply classification. If those cannot be verified, fire `R-AI-GST-PERIOD`; do not produce a payable estimate from this baseline. The worked examples illustrate stated legislative assumptions and cannot establish an actual liability. Apply this source check when using any rate or computation section separately.

## Period-specific figures

All monetary examples use Eastern Caribbean dollars, XCD, consistent with the [official GST return][G4]. Amounts in this table are the enacted 2025 baseline, subject to the period check above.

| Rule | Figure or period | Primary provision |
|---|---|---|
| Ordinary positive GST rate | 13% | [Act][G1] s 8(1) |
| Actual taxable-supply registration test | At least XCD 300,000 in 12 or fewer months | [Act][G1] s 10(1)(a) |
| Expected taxable-supply registration test | At least XCD 300,000 in an expected 12-month period | [Act][G1] s 10(1)(b) |
| Actual-test application | Within 15 days of the end of the tested period | [Act][G1] s 10(1)(a) |
| Expected-test application | Within 15 days of the beginning of the tested period | [Act][G1] s 10(1)(b) |
| Ordinary tax period | Calendar month as notified by the Comptroller | [Act][G1] s 30 |
| Return, including a nil return | Within 20 days after the tax period | [Act][G1] s 31 |
| Ordinary period payment | By the return due date | [Act][G1] s 43(1)(a) |
| Imported-service return and payment | Within 20 days after import, or another time allowed by the Comptroller | [Act][G1] s 22 |
| GST record retention | Seven years after the end of the relevant tax period | [Act][G1] s 61(2) |

## Primary source library

Use the [Act][G1], [*General Services Tax Regulations, 2025*][G2], [*Goods Tax Act, 2025*][G3] and [blank GST return][G4]. Read statutory conditions in context; a form summarises reporting and does not settle every penalty or credit entitlement. [The IRD document library][G5] is discovery evidence, not proof of an unchanged amendment chain. `references.md` records source hashes, selected-page checks and remaining pack gaps.

## Position rules

### Registration

Reconcile taxable supplies for the actual and expected tests separately. Equality satisfies each XCD 300,000 test. [Act ss 9 to 11][G1] also govern persons required to register, compulsory registration and effective dates. A person required to register is a taxable person even before receiving a certificate.

The actual-test ordinary effective date is the beginning of the following tax period under s 11(4)(a). The expected-test date is the beginning of the tested 12-month period under s 11(4)(b). Where a person required to register fails to apply, the Comptroller may register the person from the date determined by the Comptroller under s 11(3).

State/statutory-body, auctioneer and accommodation-provider cases have special registration treatment under ss 10(6), (7), (8). Under s 10(2), the Comptroller may have regard to related persons or persons acting in concert; s 10(3) values supplies under s 15. The cessation or capital-replacement condition in s 10(4) requires the Comptroller to be satisfied before the ordinary registration requirement is displaced. Voluntary registration has conditions under s 10(5) and the [regulations][G2]. Do not treat these as automatic exclusions from turnover. Refer a special case before applying an ordinary threshold calculation.

### Ordinary output GST

After the period and classification checks, establish the taxable person's domestic taxable service and its value under [Act ss 8, 13 to 15][G1]. The tax point generally uses the earliest completion, invoice or receipt of consideration under s 13(1); periodic and other supplies have distinct rules. Supplier location alone does not settle every service: s 14 contains benefit-location and other exceptions, including professional services.

For an established positive-rate service valued excluding tax, output GST is value x 13 / 100. For a tax-inclusive consideration, contained GST is gross x 13 / 113. Do not add 13% to an already inclusive price. The [official return][G4] confirms the inclusive fraction. Discounts, related parties, deposits, vouchers and adjustments need their applicable provisions before changing the value or tax point.

### Supported input tax and period reconciliation

[Act ss 23 to 25][G1] require deductible input tax, taxable use and the applicable documentary evidence. Purchase value is not the credit. Record actual eligible GST separately from the price. A tax invoice or relevant note ordinarily must be held when filing under s 24(2). The Comptroller's exception in s 24(3) needs reasonable efforts, absence of purchaser fault and the correctly due amount; do not assume permission.

Direct taxable-use input may qualify; direct exempt-use input does not. For common input, s 25(3)(c) ordinarily allocates A x B / C. A is eligible period input tax less input directly allocated to taxable or exempt supplies; B is the value of taxable supplies made during the period; C is the value of all supplies made during the period. The special comparisons in s 25(4) are strict: a taxable share above 0.90 permits the specified full common credit; below 0.10 permits none. At exactly 0.90 or 0.10, apply the ordinary formula. Confirm all statutory categories, blocked credits and any approved alternative before using this allocation. A zero denominator needs source-supported treatment; do not divide by zero or invent an allocation.

For the bounded ordinary case, net period GST is output GST less supported deductible input GST under s 23. Reconcile adjustments, imported services and prior credits separately. An excess input amount is not an automatic cash refund; s 35 imposes carry-forward and refund conditions. An opening credit cannot be deducted twice through both current input and the prior-credit line on the [return][G4].

The [Goods Tax Act][G3] uses the relevant Goods Tax column in the Integrated Customs Tariff for imported goods. A goods import value or Goods Tax payment is not automatically deductible General Services Tax. [Act ss 21 and 22][G1] impose a distinct imported-service obligation; ordinary registration turnover does not create a universal exemption from it. Imported-service calculations are outside this companion's bounded computation.

### Returns, payment and records

Use the notified monthly period and retain nil-return obligations under [Act ss 30 and 31][G1]. A filing extension under s 32 does not itself extend payment. Section 43(3) payment arrangements do not change the due date used for interest. Do not roll a nominal deadline over weekends or holidays without the applicable authority decision or law.

[Act s 61][G1] requires a GST account and relevant original invoices, notes, import/export and accounting records in Anguilla, in English, for the stated retention period. Its retail point-of-sale requirement needs separate attention for a retail supplier. This guide supplies no automatic penalty, interest or refund amount.

## Topical refusal catalogue

Use these messages verbatim when their trigger applies, together with the universal catalogue in `workflow-base`.

| Code | Trigger | Output message |
|---|---|---|
| R-AI-GST-PERIOD | Applicable period law, amendments or relevant regulatory conditions cannot be verified | I cannot calculate an Anguilla GST liability until the applicable period law and required source conditions are verified. Obtain the operative legislation and professional review. |
| R-AI-GST-SPECIAL | The calculation needs an unsupported import, export, exemption, accommodation, special valuation, adjustment, penalty or refund rule | This Anguilla GST companion does not establish the rules needed for this specialised calculation. Load the applicable primary provisions and a suitable companion, or consult an Anguilla tax professional. |
| R-AI-GST-AMBIGUITY | More than ten unresolved grouped fact questions remain after the base's filtering rules | The Anguilla GST records contain more unresolved grouped questions than this workflow can handle. Obtain a reconciled fact schedule and professional review before calculation. |

## Conservative defaults

These are disclosed working-paper treatments inside verified law, subject to the base's questions and refusal procedure. They do not replace statutory evidence.

| Missing fact | Treatment and disclosure | Primary condition |
|---|---|---|
| Documentary entitlement to an otherwise identified input credit | Claim zero pending evidence; disclose the potential credit and tax difference; obtain the document or actual Comptroller permission | [Act s 24(2), (3)][G1] |
| Business/taxable use of a purchase is unsubstantiated | Use zero deductible credit pending evidence and disclose the possible difference | [Act ss 24 and 25][G1] |
| Claimed exemption or zero rating lacks its applicable classification evidence | Stop the affected engagement under R-AI-GST-SPECIAL; a foreign customer or untaxed invoice does not establish the classification | [Act ss 8, 14, 21][G1] |
| Rate, operative law, deadline or registration status is unresolved | Needs input and the relevant refusal; no invented higher rate, cap or date | [Act ss 8 to 11, 30 to 32, 43][G1] |

## Reviewer attention and question thresholds

Every position requires professional review, regardless of amount. The cash threshold for an automatic reviewer flag and an unresolved fact question is XCD 0: disclose every nonzero tax difference. This is a companion review policy, not a statutory threshold. Flag source currency, classification, registration, unsupported credits and approaching or disputed deadlines regardless of cash difference. Apply the base's no-effect, description-answered, grouping and ten-question limits.

## Worked hypothetical positions

These examples use the enacted 2025 13% rule, an established ordinary taxable service and a verified illustrative classification. They are not current-law confirmation or an actual return. No opening credit, reverse charge or adjustment exists unless stated. Figures are exact and need no penny-rounding convention.

| Position and supplied hypothetical facts | Computation and result | Rule and review consequence |
|---|---|---|
| 1. Tax-exclusive ordinary service, XCD 1,000 | 1,000 x 13 / 100 = 130 output GST; invoice total 1,130 | [Act ss 8 and 15][G1]; verify ordinary classification and period before engagement use |
| 2. Tax-inclusive ordinary service, XCD 2,260 | 2,260 x 13 / 113 = 260 GST; value excluding tax 2,000 | [Act s 15][G1] and [return][G4]; reconcile gross as 2,000 + 260 |
| 3. Period output XCD 650 and documented eligible domestic input GST XCD 130 | 650 - 130 = 520 net period GST | [Act ss 23 and 24][G1]; input is actual eligible tax, not purchase value |
| 4. Common eligible input A = XCD 100, B = taxable supply value 4,000, C = total relevant supply value 5,000; no alternative allocation | Taxable share 4,000 / 5,000 = 0.80; credit 100 x 4,000 / 5,000 = 80; with output 520, net is 440 | [Act s 25(3)][G1]; verify statutory B/C composition and blocked credits |
| 5. Output XCD 650; potential XCD 130 input credit has no required invoice or Comptroller permission | Provisional input credit zero; net 650. With established entitlement, alternative net 520; difference 130 | [Act s 24(2), (3)][G1]; Assumed, disclose missing invoice and the difference, obtain reviewer evidence |

For a separate registration boundary, verified ordinary taxable supplies of XCD 300,000 in the actual tested period satisfy equality; XCD 299,999 alone does not satisfy that test. The expected test or a special registration rule may still apply. [Act s 10][G1] supplies the tests, not a general below-threshold tax exemption.

## Output extension

Retain all four base outputs. Add a source-currency and registration schedule, supply classification and tax-point columns, tax-exclusive value, output GST, actual input GST, allowed input, documentary reference, allocation and prior-credit reconciliation. The brief states whether source currency was verified and distinguishes a provisional working-paper amount from a payable instruction. The action list and review checklist include every source gap, assumption and refusal clearance. A refused engagement receives the base's refusal output, not a filing-ready workbook.

## Intake additions

Establish the period, reviewer, entity and taxable-person status; actual and expected taxable supplies; special registration facts; supplier/customer location and service category; invoice, completion and consideration dates; inclusive/exclusive pricing; input invoices and taxable use; notified tax periods, opening credits and actual authority decisions. Collect facts through the base's structured form; keep required document requests in the action list. Do not request or submit bank details or actual identity documents through this guide.

## Additional self-checks

Verify the period law before every applied figure. Reconcile inclusive and exclusive prices, check both registration tests and equality, trace every credit to actual GST and entitlement, verify common-input boundaries, separate Goods Tax and imported services, prevent duplicate opening credits, reconcile nil returns and payment dates, and retain every source item once. Check all five example rows independently. Record every universal and topical refusal in the trace. The eighteen base checks and professional sign-off still apply.

## Currency and revisions

Version 0.2, edited 12 October 2026. Corrects registration pinpoints and the fork referral notice in this bounded 2025 legislative reference. Complete post-2025 amendments, specialised schedules, operational rounding, authority notices and calendar exceptions remain unverified. This companion is a Tier 2 draft pending professional review.

[G1]: https://www.ird.gov.ai/Content/documents/Act%208%20-%20General%20Services%20Act,%202025%20-%20G.pdf
[G2]: https://www.ird.gov.ai/Content/documents/22%20-%20General%20Services%20Tax%20Regulations,%202025%20-%20G.pdf
[G3]: https://www.ird.gov.ai/Content/documents/Act%209%20-%20Goods%20Tax%20Act,%202025%20-%20G.pdf
[G4]: https://www.ird.gov.ai/Content/documents/General%20Services%20Tax%20Return%20Form.pdf
[G5]: https://www.ird.gov.ai/MediaCenter/Documents

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
