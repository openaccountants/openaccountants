---
name: je-income-tax-compliance
description: >
  Jersey income-tax compliance reference checked in October 2026, covering
  ordinary personal and company return deadlines, late-return penalties,
  abatements, default assessments, correction routes, appeals and late-payment
  surcharges. Use for Jersey tax penalties, assessment appeals, correcting a
  return or distinguishing tax filing from payment. Preserves statutory
  conditions, separate notice periods and the obligation to pay estimated
  tax during an appeal. Includes hypothetical calculations and reviewer
  controls. It does not calculate personal instalment formulas, handle a
  dispute or submit anything. GST, social contributions, MCIT, prosecution
  and complete enforcement procedures require their own verified sources.
jurisdiction: JE
category: international
tax_year: 2026
tax_year_notes: "Current statutory snapshot checked 15 October 2026; use the applicable historical version for earlier events"
tier: 2
last_updated: 2026-10-15
version: 0.1
review_status: pending_review
depends_on:
  - workflow-base
---

# Jersey income-tax compliance

Use this guide to prepare a source-linked compliance calendar and issues schedule for a qualified reviewer. It is a Tier 2 draft, with no practitioner sign-off. It does not authorise filing, correction, litigation, portal access or payment. Load the universal workflow base and the applicable tax-content companions; a missing required source, slot or validated input holds the dependent result and the complete package.

## Scope, period and intake

This guide covers the selected ordinary income-tax provisions of the [Income Tax (Jersey) Law 1961](https://www.jerseylaw.je/laws/current/l_29_1961), in the official consolidated version effective from 17 June 2026 and checked on 15 October 2026. Check historical law, commencement and any specific notice for the period concerned. An editing date does not establish the rules for an earlier event.

Obtain the taxpayer/entity category; statutory return type; assessment year; filing method and obligation; delivery confirmation; every assessment, penalty, surcharge and refusal notice; notice-issue and receipt dates; tax liability and payments separately from penalties; prior-year earnings proportion; and supporting facts for a correction, claim or possible waiver. Use redacted references. The reviewer retains actual identifiers, correspondence and authentication material.

GST, customs/excise, social contributions, MCIT/Pillar Two, criminal offences, full debt recovery, court procedure and time-computation conventions are outside this guide. A general tax-compliance label does not extend these income-tax rules to another regime. Company exemptions and ordinary-return exceptions require je-corporate-income-tax and je-pillar-two; employer returns require je-payroll.

## Ordinary return and payment calendar

Under [Article 17A(2)](https://www.jerseylaw.je/laws/current/l_29_1961), the ordinary annual return dates in the year following assessment are:

| Return within its statutory category | Specified time |
|---|---|
| Company's own charge to tax | Midnight 30 November |
| LLC return under Article 135C | Midnight 30 November |
| Other annual return delivered electronically | Midnight 31 July |
| Other annual return | Midnight 31 May |

These dates do not replace the separate monthly, employer, benefit or other return provisions in Article 17A(2). First establish that the return is required and which category applies. Retain evidence that delivery was true, complete and correct, not only a portal submission timestamp.

[Article 39](https://www.jerseylaw.je/laws/current/l_29_1961) generally makes income tax payable by 30 November following assessment, or 30 September for a large company under Article 41AB(7), subject to instalments. Company instalment amounts, inclusive size test and payment-year look-back are in [je-corporate-income-tax](je-corporate-income-tax.md). Return and payment dates are separate.

[Article 41A](https://www.jerseylaw.je/laws/current/l_29_1961) governs non-company instalments from assessment year 2021 where prior-year earnings are 25% or less of total income and the prescribed instalment is at least GBP 100. It sets 30 November in the assessment year and 31 May afterwards, with different calculation branches depending on earnings, payments and assessment status. The complete mathematical formula was not present in the captured text extraction. This guide does not supply an instalment amount; obtain the complete formula and validate the inputs before computing it. Part 19 scheme-manager exclusions remain separate.

Under [Article 41AA](https://www.jerseylaw.je/laws/current/l_29_1961), an application to waive or reduce a personal instalment normally must reach the Comptroller at least 1 month before it is due and meet a statutory likely-reduction condition. Late acceptance requires reasonable cause. Refusal may be appealed by written notice within 40 days of the refusal notice's issue; the instalment remains due on its original date pending that process. Do not treat an application or appeal as payment relief already granted.

## Late-return penalties and abatements

[Article 17A](https://www.jerseylaw.je/laws/current/l_29_1961) applies to its defined returns. Ordinary annual personal/company returns have an initial GBP 300 penalty. Returns under Articles 20/20A have an initial GBP 100 penalty and are outside the annual examples below. If a required return remains undelivered at midnight 3 months after its specified time, further monthly penalties apply for at most 9 months:

| Return/person category under Article 17A(2B) | Monthly amount |
|---|---|
| Articles 16/17, person other than a body of persons | GBP 50 |
| Listed Article 20 to 20E/135C categories, or Article 16 body of persons | GBP 100 |

The personal exceptions are conditional. For an Article 16/17 return by a person other than a body of persons:

- Article 17A(3) removes liability under the Article if the Comptroller is satisfied that no tax is payable for the period.
- When the late return is delivered and the Comptroller is satisfied that tax liability is below GBP 300, Article 17A(4) reduces the initial penalty to that tax and requires repayment of an excess penalty already paid.
- If the Comptroller is satisfied that tax liability is below GBP 50, Articles 17A(4A) and (4B) reduce **each** monthly penalty to that tax and require repayment of excess amounts paid.

The [personal penalty summary](https://www.gov.je/taxesmoney/incometax/individuals/yourtaxreturn/pages/personallatefilingfee.aspx) and [corporate penalty guidance](https://www.gov.je/TaxesMoney/IncomeTax/Companies/ReportingCompanies/Pages/HowToAppealAPenalty.aspx) support the ordinary rates. The statute supplies the additional monthly abatement and person/category limits. Do not apply the personal abatements to a company, or assume that a zero-rated company cannot incur a return penalty.

A written penalty notice states the amount and application right. Under Article 17A(5A) and (6), payment is due within 40 days after issue, subject to the application provision, and a written discharge/waiver application may be made within 40 days of issue. The Comptroller may discharge the penalty if satisfied that a true, complete and correct return was delivered on time, or waive it if death, serious illness or another grave and exceptional circumstance prevented timely delivery. A factual excuse or request does not establish an accepted waiver. Refusal can be appealed by notice to the Comptroller within 40 days of the refusal notice's issue, under Part 6 as modified.

Article 17A(11) and (12) makes the penalty non-deductible, treats collection as tax subject to the stated rules, and excludes the penalty from the Article 41I surcharge base. Keep tax, return penalties and payment surcharges in separate ledger fields.

## Default assessments, corrections and relief

[Article 23](https://www.jerseylaw.je/laws/current/l_29_1961) allows a default assessment where a required return was not received. It has **no Part 6 appeal**. A required return delivered no later than 12 months after the date of the assessment sets the default assessment aside and requires a further assessment based on that return. Verify the assessment category and date first; do not use the ordinary 40-day appeal route for this default assessment.

[Article 24](https://www.jerseylaw.je/laws/current/l_29_1961) normally permits the Comptroller to amend or add an assessment within 2 years after the later of the filing due date and actual delivery. The period is 4 years for a careless action and unlimited for deliberate action or inaction. An amended/additional assessment can be appealed as a first assessment. These are the authority's assessment limits, not a general taxpayer amendment window.

For an error in a submitted personal return, [Revenue Jersey's correction guidance](https://www.gov.je/taxesmoney/incometax/individuals/yourtaxreturn/pages/correctingerrorspersonaltaxreturn.aspx) says to provide the error and correction details; do not send a duplicate return. The [company online-return guidance](https://www.gov.je/TaxesMoney/IncomeTax/Companies/CompanyTaxGuidance/Pages/OnlineCompanyReturn.aspx) describes its correction function. The reviewer must establish the applicable route, notice and time limit before taking action.

[Article 37](https://www.jerseylaw.je/laws/current/l_29_1961) gives relief for proven double assessment of the same cause, account and year, including repayment if both were paid. [Article 38](https://www.jerseylaw.je/laws/current/l_29_1961) permits reasonable and just repayment relief for excessive tax paid/borne because of an error or mistake in a return. The claim must be made not later than 5 years after the assessment year ends. Its prevailing-practice exclusion and all relevant circumstances, including other years, must be considered. A correction request alone does not prove entitlement to repayment or preserve an appeal deadline.

## Ordinary assessment appeals

[Articles 25, 27 and 28](https://www.jerseylaw.je/laws/current/l_29_1961) require the assessment notice to state the tax, latest appeal date and payment date in the absence of appeal. An ordinary appeal is written notice to the Comptroller within 40 days of the notice of assessment, with grounds and the appellant's estimate of tax payable on determination. Explain an estimate of nil or an amount above the assessment. The Comptroller may admit a late appeal for absence, sickness or other reasonable cause if made without unreasonable delay; acceptance is not automatic.

If no hearing notice arrives within 90 days after an appeal, Article 27(4) allows direct notice to the Commissioners, who may admit it. Article 29 requires at least 21 days' hearing notice. This is not a complete hearing-procedure guide. See the [general appeal guidance](https://www.gov.je/taxesmoney/incometax/technical/guidelines/pages/howtoappeal.aspx) and [company assessment guidance](https://www.gov.je/TaxesMoney/IncomeTax/Companies/ReportingCompanies/Pages/AppealCompanyAssessment.aspx), subject to Article 23's separate default-assessment route.

**Tax estimated to be due remains payable during an appeal** under Article 28(3). The determination produces a further payment or repayment as applicable. An appeal is not an automatic collection stay.

Under [Article 36A](https://www.jerseylaw.je/laws/current/l_29_1961), a written settlement before determination may be revoked by written notice within 40 days beginning with the agreement day; otherwise it has the effect of a final determination with no further appeal. [Article 36](https://www.jerseylaw.je/laws/current/l_29_1961) provides a Royal Court appeal after a Commissioners' determination, with notice to the Judicial Greffier, Commissioners and other party within 21 days starting on determination and specified further appeal limits. Court proceedings and litigation advice require a qualified practitioner; this guide does not prepare or lodge them.

## Late-payment surcharge

[Article 41I](https://www.jerseylaw.je/laws/current/l_29_1961) generally charges 10% of tax remaining unpaid at midnight 30 November following assessment, or 30 September for a large company, whether or not an assessment has been served. It does not apply to an individual whose earnings exceeded 25% of total income in the year before assessment. Establish that scope and the correct year before calculating.

The Comptroller **may** waive a surcharge of GBP 50 or less, one caused by an unconnected person's action and remedied without unnecessary delay, or one where death, serious illness or another grave and exceptional circumstance prevented payment. The [personal payment page](https://www.gov.je/taxesmoney/incometax/individuals/yourtaxassessment/pages/latepaymentsurcharge.aspx) states that balances of GBP 500 or less are not surcharged. Record that as published administrative practice; the statute expresses a discretionary waiver of a surcharge at or below GBP 50. Do not recast it as an unconditional statutory exemption.

A surcharge notice and any refusal notice start separate periods. Article 41I(5) allows a written waiver application within 40 days of the surcharge notice's issue; Article 41I(7) allows appeal of refusal within 40 days of the refusal notice's issue. Part 6 applies with modifications. Filing a return, requesting a waiver or having a pending correction does not prove that the charge has been cancelled.

## Hypothetical positions

All amounts are GBP. These examples assume the stated statutory category, confirmed facts and Comptroller satisfaction where required. Monthly counts are supplied facts, not date calculations. No example establishes an actual assessment or waiver.

| Position | Calculation or route | Result |
|---|---|---|
| Personal initial and monthly abatement | Article 16/17 non-body taxpayer; late return delivered; tax 40; 2 monthly penalties confirmed; Article 17A(4)/(4B) conditions satisfied | 40 + 2 x 40 = 120, before any separately granted waiver |
| Company with zero tax | Required Article 16 company return; initial penalty and 9 monthly penalties confirmed | 300 + 9 x 100 = 1,200; personal zero-tax exception/abatements do not apply |
| Personal zero liability | Article 16/17 non-body taxpayer; Comptroller satisfied no tax is payable for the period | No Article 17A penalty under paragraph (3), despite late filing |
| Surcharge base | Person within Article 41I; unpaid tax 10,000 plus return penalty 300 at the specified time; no waiver | Surcharge 10,000 x 10% = 1,000; penalty is excluded, so combined unpaid tax/penalty/surcharge is 11,300 |
| Ordinary appeal payment | Assessment 10,000; valid appeal estimates 7,000; no prior payments; determination 8,000 | Estimated 7,000 remains payable while pending; a further 1,000 follows the determination, subject to the applicable notices/dates |
| Default assessment | Missing-return default under Article 23, not an ordinary assessment | No Part 6 appeal; reviewer checks the 12-month return route and date. No unsupported replacement tax amount is computed |

## Refusals, defaults and reviewer attention

| Refusal | Trigger | Verbatim output |
|---|---|---|
| R-JE-COMP-1 | Return/notice category, required date, period, applicable law, formula or evidence is missing | R-JE-COMP-1: Needs Input. Establish the Jersey income-tax category, source and dates before accepting a dependent amount or deadline. |
| R-JE-COMP-2 | An assessment, penalty, surcharge, waiver or appeal is disputed or a court step is requested | R-JE-COMP-2: Refer to the qualified reviewer. Preserve the evidence and statutory periods; do not determine the dispute, submit a response or promise relief. |
| R-JE-COMP-3 | A required base output, companion input, tool or check is absent or invalid | R-JE-COMP-3: Needs Input. Complete and validate the required inputs and outputs; withhold dependent results and the complete package. |

No missing-fact defaults are authorised. An unknown liability, notice date, earnings proportion or waiver outcome remains unknown. Do not substitute zero, assume an extension or calculate an unsupported formula. Every notice, disputed amount, possible missed deadline and waiver/appeal decision requires reviewer attention regardless of cash amount; this is a workflow policy and creates no legal de minimis rule. Pending review is not an accepted tax treatment.

## Outputs and self-checks

Retain the universal outputs and checks. Add a compliance schedule with the statutory category, period, source/version, triggering event, exact source date wording, reviewer-verified due date, tax/penalty/surcharge amounts, receipts, application/appeal status and evidence references. Show held values explicitly. Extend the reviewer brief with every unresolved deadline, disputed charge, correction route and source limitation. A correspondence draft is for reviewer approval only; no filing, authentication, payment or transmission is authorised by this guide.

- Verify that the return is required and distinguish its deadline from payment.
- Distinguish a body of persons from the personal penalty categories.
- Check both initial and monthly abatements, the 9-month cap and required Comptroller satisfaction.
- Separate assessment, default assessment, penalty, surcharge and refusal notices.
- Preserve each period's statutory starting phrase; obtain review of calendar/time-computation rules before fixing an operational deadline.
- Keep estimated tax payable during an appeal and reconcile later payments/refunds once.
- Exclude return penalties from the surcharge base and tax deductions.
- Preserve authority assessment limits separately from taxpayer claims and appeal rights.
- Complete required source, intake, refusal and output checks before delivering a financial result.

## Sources and revision

The linked current law provisions and relevant official guidance pages were captured and their cited text read on 15 October 2026. Captured hashes and the distinctions between guidance and law are in references.md and the dated verification log. The complete personal instalment formula, delegated provisions, full enforcement/court procedure, all other tax regimes and practitioner sign-off remain unverified. These gaps prevent a claim of complete Jersey compliance coverage.

Version 0.1, 15 October 2026: adds the bounded income-tax compliance rules, examples and reviewer controls above. The primary-source library is the cited Income Tax Law and the linked official return, correction, appeal, penalty and payment pages; no secondary tax summary supplies a rule here.

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
