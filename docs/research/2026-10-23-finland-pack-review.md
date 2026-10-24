# Finland independent full-pack source and arithmetic review

**Final correction closure, 23 October 2026:** all six original findings and the narrow correction regression are closed at `c83ca9f5455b9560937c797c20ecd1b7b102b363`. All 33 controls independently recompute. The source/editorial review gate is satisfied for the exact country blobs listed in the final addendum, subject to preserving those blobs in publication. All seven domains remain partial and named Finnish accountant review remains open. Final repository checks and pushed-head CI are separate.

Read on 23 October 2026. Reviewer: fresh Codex review agent, separate from the country writer. This is an independent editorial/source review, not Finnish accountant approval or an attestation.

## Decision at the reviewed checkpoint

**Corrections required before the country content push.** Six actionable findings are set out below. All 33 executable examples independently recompute, but correct arithmetic does not cure the source and scope defects. No other actionable defect was identified in the examined material within the source-review limits below. The seven tax domains must remain partial, all Guides tier 2, and named professional review pending.

## Exact identity and scope

- Source checkpoint: `b7b4a75f53c5a0aba3cb5ff994ece7cae6f20bf4`.
- Published comparison baseline: `915c5118`.
- Checkout inspected: `/private/tmp/oa-world-support`, branch `codex/finland-country-completion`.
- Working HEAD at initial inspection: `20dcd696bc9515e23d3beebdb90e1891dc0e2e59`. The Finland tree was identical to the frozen source checkpoint (`git diff` for the country directory was empty). The review is attributed to the source checkpoint, not to mutable HEAD.
- Read the handoff brief first, GOAL.md, OWNERS.md's country-batch/review rules, README and all twelve source Guides, including earlier operational paragraphs, worked decision cases, scope/referral statements, sources, metadata and CTA blocks. This was a whole-pack reading, not merely a diff review.
- Read the review brief and all eight Finland narrative research records plus the direct-statute and reachability evidence. Their evolving historical counts are treated as dated preparation records, not current verification or independent proof.
- No source Guide, README, OWNERS, another country, commit or remote was modified by this reviewer.

The exact examined manifest is recorded at the end. There are twelve source Guides plus README; eleven Guides contain calculations and the overview is a router. Every source Guide has `tax_year: 2026` and `tier: 2`. No named Finnish credential or accountant approval is claimed. README's seven `partial` entries and the router's limits are consistent with the actual unfinished coverage.

## Findings requiring correction

### FI-1, P1: replace the erroneous health-care contribution base explanation

**File/lines:** `skills/international/finland/fi-yel-social.md:34` and `:117` at the frozen checkpoint.

The table and health paragraph describe health care as based on wage/work income “as taxed”, and the paragraph singles out the daily allowance contribution as the one tied to YEL. This creates the wrong distinction for a YEL-insured entrepreneur. The confirmed YEL/MYEL work income also replaces the relevant income from business activities for health-care-contribution assessment; other earned income not replaced remains relevant. It is not a calculation on ordinary taxable business profit in addition to YEL. Own-company wages also need the statutory substitution treatment rather than ordinary wage treatment.

**Primary authority read:** Vero, [Which types of income are subject to prepayments?](https://vero.fi/en/businesses-and-corporations/taxes-and-charges/tax-prepayment/how-is-the-current-years-total-of-prepayments-calculated/), updated 1 January 2026, section “YEL and MYEL income as the basis for prepayments”, paragraphs 2–3. The key passage says “YEL or MYEL work income replaces income from business activities.” Its next sentence includes work income and other earned income not replaced. The following paragraph separately explains the daily allowance contribution and YEL increase. Corroboration: [Incomes Register health insurance contribution guidance](https://www.vero.fi/en/incomes-register/companies-and-organisations/employers/earnings-payment-data/employers-are-obliged-to-insure-their-employees/health-insurance-contribution/), employee-health section, and the [2026 pension-provider reporting specification](https://www.vero.fi/contentassets/4be5ede7345a4b32a394d7a230ae807c/finnish-tax-administration_description-of-the-data-file_vktyosva_2026.pdf), statutory-background discussion referring to Health Insurance Act chapter 18 section 14.

**Correction:** retain verified 2026 rates, remove the suggestion that only daily allowance uses YEL, state the health-care substitution explicitly, and preserve other-income/deduction and assessment checks. Add the actual substitution source. The rate table alone does not establish the base.

### FI-2, P1: add place-of-supply and purchaser-liability gates to foreign-service rows

**File/lines:** `skills/international/finland/finland-vat-return.md:118–119`, and Case G `:219`.

The EU row explicitly lists passenger transport among Finnish supplies that the purchaser should enter as self-accounted domestic-output VAT. But passenger transport is a statutory exception to the foreign-seller reverse charge: the seller remains liable. The non-EU row and Case G also make foreign establishment effectively sufficient for Finnish self-assessment, regardless of the general/special place-of-supply rule. A foreign hotel stay is a concrete counterexample: property-location rules can put it outside Finland. Even a Finnish supply needs a separate liability screen, including the seller's Finnish registration/participating establishment and the passenger/event exceptions. The general introductory caution and specialist-referral row do not cure these specific positive instructions.

**Primary law independently fetched and read:** [VAT Act 1501/1993](https://www.finlex.fi/fi/lainsaadanto/1993/1501), section 9(1) (foreign-seller/purchaser-liability conditions), section 9(2)(4) (seller liability for passenger transport and section 69d services), section 9(4) (nonparticipating Finnish establishment), section 65 (general B2B place), section 67 (property, including accommodation), and section 69d (event admission, with the displayed virtual-participation amendment distinguished).

**Authority corroboration:** [Vero cross-border supply and acquisition of services](https://www.vero.fi/en/detailed-guidance/guidance/48679/value-added-taxation-of-cross-border-supply-and-acquisition-of-services/), general remarks and sections 6/6.1. Section 6 excludes a foreign seller's voluntary Finnish VAT registration or participating Finnish establishment from reverse charge; section 6.1 expressly excludes passenger transport and physical event admission. The return instructions' domestic-output list is itself conditional on foreign sellers not being liable because reverse charge applies: [Vero VAT return instructions](https://www.vero.fi/en/businesses-and-corporations/taxes-and-charges/vat/when-to-file-and-pay/), “Tax on domestic sales by tax rate”.

**Correction:** only prescribe these purchaser entries after establishing a Finnish taxable supply and the buyer's liability. Remove passenger transport as an ordinary purchaser-reverse-charge example. Keep construction/scrap and other special routes separate. Make Case G expressly assume both Finnish place and applicable reverse charge; supplier geography and rate alone are insufficient. An extensive new cross-border chapter is unnecessary.

### FI-3, P2: state YEL's month-after-birthday lower-age boundary

**File/line:** `skills/international/finland/fi-yel-social.md:56` (and align the intake at `:40` if needed).

The stated conjunction uses only age “at least 18” and four months after turning 18. It does not identify the earliest insured-work date. YEL Act section 4(1)(1) excludes activity before the start of the calendar month following the eighteenth birthday, which matters when arranging a backdated policy after the duration condition is established. For an eighteenth birthday on 15 July, the lower-age boundary is 1 August, not 15 July. This is a date boundary, not a change to the contribution rate or the upper-age cohorts.

**Primary law read:** [YEL Act 1272/2006](https://www.finlex.fi/fi/lainsaadanto/2006/1272), section 4(1)(1). The Finnish text explicitly specifies the next calendar month's beginning. ETK/Työeläke's abbreviated English eligibility lists do not override that provision.

**Correction:** add the exact lower-age start rule while retaining four-month duration, coverage and birthday-month upper-age checks. No broad international rewrite is required.

### FI-4, P2: preserve the disability exception in the changed-business example

**File/line:** `skills/international/finland/fi-yel-social.md:147`, compared with the correct exception earlier in the Guide.

The example tells the reader not to seek any retrospective confirmed-income amendment, without excluding a disability-pension award. Section 112a expressly permits retrospective amendment in that case. The Guide correctly states the exception in its earlier general narrative, so the isolated worked case is internally inconsistent. Readers and retrievals can encounter the case separately.

**Primary law read:** [YEL Act](https://www.finlex.fi/fi/lainsaadanto/2006/1272), section 112a(1): ordinary changes are prospective, with a disability-pension exception from the pension-event date.

**Correction:** make this an ordinary change case with no disability-pension award, or cross-reference the exception in the instruction. Retain the distinction from late arrangement of insurance.

### FI-5, P2: distinguish the EUR 1,500 employer threshold from employee deductions

**File/lines:** `skills/international/finland/fi-employer-payroll.md:42–56`.

The liability introduction couples employee age and employer payroll above EUR 1,500, and only clarifies that the threshold does not remove reporting. It omits an operationally important second distinction: employee unemployment contributions must still be deducted from liable employees when annual payroll is EUR 1,500 or less. The general later sentence that the employee share is deducted does not resolve the apparent threshold gate in the opening eligibility instruction. A payroll preparer could skip employee deductions on a small employer's payroll.

**Primary authority read:** [Employment Fund payment guidance](https://www.tyollisyysrahasto.fi/en/Unemploymentinsurancecontribution/paying-unemployment-insurance-contributions/), opening three paragraphs, before the contribution percentages. They require employee deductions even below EUR 1,500; where the employer's payment threshold is not exceeded, the employer keeps the deductions, and pay is reported as liable so the Fund can monitor the threshold. The 2026 section separately confirms the rates used in the Guide.

**Correction:** explicitly state the employee-withholding rule below the employer threshold, how the below-threshold amounts are treated, and the reporting distinction. Preserve statutory employee exclusions and Fund invoicing. No additional computational example is needed to establish this legal point.

### FI-6, P3: align VAT scope exclusions with the penalty calculation already provided

**File/lines:** `skills/international/finland/finland-vat-return.md:93`, `:299–326`, `:338`.

The earlier paragraph says quantifying filing/payment charges is outside scope, and the referral list broadly excludes penalties, but the later section deliberately quantifies an original VAT return's filing charge and describes replacement-return treatment. That scope conflict can cause the example to be ignored or imply a wider completed penalty treatment than supplied.

**Source comparison:** [Vero self-assessed-tax late-filing guidance](https://www.vero.fi/en/businesses-and-corporations/taxes-and-charges/self-assessed-taxes/late-penalty-charges/) supports the scoped original-return formula. The assumed 50-day/EUR 4,000 case correctly gives EUR 135 plus EUR 80 = EUR 215, subject to the stated cap and no special waiver. The replacement route differs. This is a wording defect, not an arithmetic failure.

**Correction:** identify the limited filing-penalty screen below while leaving late-payment, waiver, nonfiling/estimated-assessment and other specialist procedures open. Do not imply that all penalties have now been resolved.

## Review method and evidence

### Direct statute corroboration

The browser extractor returned navigation-only shells for some Finlex URLs and failed on two large pages. I did not treat those as legal verification. I audited `/private/tmp/oa-finlex-statutes.py`'s extraction mechanism, then made fresh direct HTTPS requests to all ten official Finlex URLs. The extractor selects the Finnish `akomaNtoso` statutory-body section, resolves public server-rendered record references, preserves numeric child/table values and uses structural section headings. I independently read the selected statutory language against the Guide assertions; I did not use the writer's interpretation as proof. Reuse of the inspected extraction utility is disclosed because this was not an independently implemented second parser.

Fresh copies are `/private/tmp/independent-fi-YEAR-NUMBER.html` and `.txt`; `/private/tmp/independent-fi-statutes.json` records fresh raw/text SHA-256 hashes. All ten raw and extracted hashes matched the writer's snapshots, so there was no source-content drift between the independent retrieval and the recorded research. Matching hashes establish identity, not legal correctness.

| Primary law | Provisions substantively read in this review |
|---|---|
| [Income Tax Act 1535/1992](https://www.finlex.fi/fi/lainsaadanto/1992/1535) | 9, 11, 30a, 38, 41, 96, 119, 122, 124. Distinguished the section 9 PE amendment commencing in 2027 and historical/future text from 2026 rules. |
| [2026 scale Act 1140/2025](https://www.finlex.fi/fi/lainsaadanto/2025/1140) | Entire two-section Act: all five numeric rows, tax-year application and 1 January 2026 commencement. |
| [Assessment Procedure Act 1558/1995](https://www.finlex.fi/fi/lainsaadanto/1995/1558) | 14a–14e, 31, 32, 32a, 33: SME/full/reduced documentation, actual transaction, CbCR scope/deadlines/refusal/surrogates, scoped sanctions. |
| [Business Income Tax Act 360/1968](https://www.finlex.fi/fi/lainsaadanto/1968/360) | 7, 8, 16, including the visible 2026 membership-fee changes and nonoperative 2027 PE-expense addition. This is not a complete deduction audit. |
| [Prepayment Act 1118/1996](https://www.finlex.fi/fi/lainsaadanto/1996/1118) | 9, 11, 13: withholding duty/exceptions, payment and cash cap, wage definition. |
| [VAT Act 1501/1993](https://www.finlex.fi/fi/lainsaadanto/1993/1501) | 3, 9, 65, 67, 69d, 84, 85, 85a, 102, 114. Distinguished historical text and effective 2026 reduced/publication wording. |
| [YEL Act 1272/2006](https://www.finlex.fi/fi/lainsaadanto/2006/1272) | 4, 89, 109, 112–112a, 114–115, 122, 143 and displayed commencement/review-transition text of 1157/2022 and 1400/2025. |
| [Transfer Tax Act 931/1996](https://www.finlex.fi/fi/lainsaadanto/1996/931) | 4, 6, 7, 15, 20, 21: rates, debt base, payment triggers and contingent consideration. |
| [Amending Act 1143/2025, official PDF](https://www.finlex.fi/api/media/statute/896509/mainPdf/main.pdf?timestamp=2025-12-11T05%3A12%3A12.000Z) | Both pages, including the 1 January 2026 contract-date transition, independently opened separately from consolidated law. |
| [Companies Act 624/2006](https://www.finlex.fi/fi/lainsaadanto/2006/624) | 1:2–3, 2:8–9, 5:3, 6:8/10/19, 8:10. |
| [Auditing Act 1141/2015](https://www.finlex.fi/fi/lainsaadanto/2015/1141) | 2:2, including the positive omission test in each period, startup rule, articles and securities-holding exception. |

### Authority/provider source content independently consulted

The following administrative sources were independently opened/read for the specified subjects. This inventory distinguishes them from the 98-URL reachability scan, which I did not reclassify as a 98-source legal audit.

- Individual: [Vero capital/tax bases](https://www.vero.fi/en/individuals/tax-cards-and-tax-returns/tax_card/tax-rate-and-income-ceiling/tax-bases/), [entrepreneur deduction](https://www.vero.fi/en/businesses-and-corporations/taxes-and-charges/taxation-of-self-employed-individuals/deductions/deduction-for-entrepreneurs/), [Form 5 instructions](https://www.vero.fi/en/businesses-and-corporations/taxes-and-charges/taxation-of-self-employed-individuals/instructions-for-filing/), [individual sanctions](https://www.vero.fi/en/individuals/tax-cards-and-tax-returns/your_tax_return_and_tax_assessment_deci/forgotten-to-report-important-details/late-fee-and-tax-increase/). Rates, deduction ordering and return/base distinctions align with the cited selected statutes. No 2027 allocated personal filing deadline was supplied or independently established.
- Corporate: [income/base and accounting-period tax years](https://www.vero.fi/en/businesses-and-corporations/taxes-and-charges/limited-companies-and-cooperatives/income-tax/), [return requirements](https://www.vero.fi/en/businesses-and-corporations/taxes-and-charges/limited-companies-and-cooperatives/tax-return/), [future changes](https://www.vero.fi/en/About-us/newsroom/changes-in-taxation/), [nonresident dividend/interest/royalty guidance](https://www.vero.fi/en/detailed-guidance/guidance/49133/payments-of-dividends-interest-and-royalties-to-nonresidents3/), especially 3.4.1. Current 20%/ten-year rules are distinguished correctly from proposals; 35% unidentified and 30% insufficient-corporate-identification routes are not interchangeable.
- Payroll: [Vero insurance table and scope](https://www.vero.fi/en/businesses-and-corporations/taxes-and-charges/being-an-employer/social-insurance-contributions/), [Employment Fund payment/2026 rates](https://www.tyollisyysrahasto.fi/en/Unemploymentinsurancecontribution/paying-unemployment-insurance-contributions/), [Ilmarinen contribution calculation](https://www.ilmarinen.fi/en/employer/managing-tyel-insurance/determining-the-tyel-contribution/), [Incomes Register deadlines](https://www.vero.fi/en/incomes-register/companies-and-organisations/deadlines-for-reporting/). Reporting versus payment, average insurer pricing versus actual invoice and ordinary age/base distinctions remain material assumptions.
- Residence/relief: [Vero residence guidance](https://www.vero.fi/en/detailed-guidance/guidance/48999/tax-residency-nonresidency-and-residency-in-accordance-with-a-tax-treaty--natural-persons4/) and [foreign-credit guidance](https://vero.fi/en/detailed-guidance/guidance/77657/relief-for-international-double-taxation-in-natural-persons-tax-assessment/), especially 3.2.6. The five-year same-source/category carryover and older-credit-first ordering agree with the preparation examples; no particular treaty or gross-receipt limitation is assumed.
- Prepayments: [instalment table](https://www.vero.fi/en/businesses-and-corporations/taxes-and-charges/tax-prepayment/instructions-for-making-prepayments/how-many-instalments/), [additional prepayments](https://www.vero.fi/en/businesses-and-corporations/taxes-and-charges/tax-prepayment/additional-prepayment/), [interest with relief](https://www.vero.fi/en/businesses-and-corporations/taxes-and-charges/tax-prepayment/additional-prepayment/late-payment-interest-with-relief/), [YEL/MYEL basis](https://vero.fi/en/businesses-and-corporations/taxes-and-charges/tax-prepayment/how-is-the-current-years-total-of-prepayments-calculated/), [back-tax payment instructions](https://www.vero.fi/en/individuals/payments/back-taxes/payment-instructions/) and [late prepayment instructions](https://www.vero.fi/en/businesses-and-corporations/taxes-and-charges/tax-prepayment/instructions-for-making-prepayments/if-you-pay-late/). The January due-date weekend trap is supported, with 2027 rates correctly left open.
- VAT: [return entries/corrections/deadlines](https://www.vero.fi/en/businesses-and-corporations/taxes-and-charges/vat/when-to-file-and-pay/), [tax periods](https://www.vero.fi/en/businesses-and-corporations/taxes-and-charges/vat/when-to-file-and-pay/tax-period/), [small-business guidance](https://www.vero.fi/en/detailed-guidance/guidance/48658/vat-exemption-for-small-businesses/), [purchase deductions](https://www.vero.fi/en/businesses-and-corporations/taxes-and-charges/vat/deducting-vat-on-purchases/), [vehicles](https://www.vero.fi/en/businesses-and-corporations/taxes-and-charges/vat/vat-on-vehicles/), [cross-border services](https://www.vero.fi/en/detailed-guidance/guidance/48679/value-added-taxation-of-cross-border-supply-and-acquisition-of-services/), [filing penalties](https://www.vero.fi/en/businesses-and-corporations/taxes-and-charges/self-assessed-taxes/late-penalty-charges/). FI-2/FI-6 apply; current/prior-year threshold, crossing sale, deduction/vehicle/entertainment and EUR 500 replacement alternatives were examined, not just the three added arithmetic blocks.
- TP: [obligation guidance](https://www.vero.fi/en/businesses-and-corporations/business-operations/transfer-pricing/transfer-pricing-documentation/obligation-to-compile-a-transfer-pricing-documentation/), [detailed documentation guidance](https://www.vero.fi/en/detailed-guidance/guidance/47978/transfer-pricing-documentation/), especially 4.3/4.4 and 6.6/6.7. The statutory inclusive SME ceilings, counterparty aggregation, loan treatment, content simplification, reliable-method preference and gross/net distinctions are retained accurately at this level.
- CbCR: [full-report instructions](https://www.vero.fi/en/businesses-and-corporations/business-operations/transfer-pricing/countrybycountry-report-and-notification/country-by-country-report---how-to-file-the-report-in-mytax/) and [notification instructions](https://www.vero.fi/en/businesses-and-corporations/business-operations/transfer-pricing/countrybycountry-report-and-notification/notification-of-the-reporting-entity-how-to-file-the-notification-in-mytax/). Equality at EUR 750m, separate notification/report obligations and current CSV-entry capability align with the Guide; actual exchange/schema application remains open.
- Property: [deadline table](https://www.vero.fi/en/individuals/property/transfer-tax/instructions-for-filing-and-paying-transfer-tax/table-of-filing-and-payment-deadlines/) and [housing shares](https://www.vero.fi/en/individuals/property/transfer-tax/buyer-of-a-flat/). Compared debt-free price, signing versus ownership triggers and agent responsibilities to selected current statutory text and the separate transition PDF.
- Formation: [current PRH setup](https://www.prh.fi/en/companiesandorganisations/yrityksen_perustaminen/osakeyhtio.html), [foreign-person permits](https://www.prh.fi/en/companiesandorganisations/ulkomaalaisluvat.html), [2026 late-filing notice](https://www.prh.fi/en/presentation_and_duties/uutislistaus/news/2026/financial-statements-submitted-late-27.5.2026.html). EUR 300/400 routes, separate ordinary/deputy residence tests and fee escalation are source-supported; the two-month adoption clock is separately supported by company law.
- YEL: [ETK FAQs](https://www.etk.fi/en/finnish-pension-system/pensions/pension-coverage-and-insurance/faqs-on-yel-insurance/), [2026 ETK booklet](https://www.etk.fi/wp-content/uploads/2026/02/pension-insurance-of-the-self-employed.pdf), [Työeläke eligibility](https://www.tyoelake.fi/en/pensions-for-the-self-employed/when-do-i-need-insurance/), [confirmed-income method and limits](https://www.tyoelake.fi/en/pensions-for-the-self-employed/what-is-yel-income/), [social-security preparation](https://www.tyoelake.fi/en/pensions-for-the-self-employed/social-security-of-the-self-employed-based-on-confirmed-income/). Checked ordinary thresholds, owner/spouse conditions, work-input recommendation and benefit reference period against provider/statutory evidence; FI-1/FI-3/FI-4 remain corrections.

## Independent arithmetic and assumption review

All 33 frozen-checkpoint blocks were parsed and evaluated using a separate local AST evaluator written for this review, not by invoking the repository's arithmetic checker or relying on its reported success. Inputs/steps/expected results were compared at numeric precision. Machine-readable results are in `/private/tmp/independent-fi-arithmetic.json`.

The assumptions were also read: established taxable income is not gross receipts; hypothetical prices/rates are marked; eligibility is not inferred from passing multiplication; net pay is distinguished from withholding and employer liabilities; threshold examples do not determine filer identity; capital allocation and audit counts are not universal legal engines. In particular, the audit example correctly fails the positive omission rule when one period has two exceedances even though the preceding period has zero.

The full recomputation table follows. Additional non-block VAT cases were also recalculated: EUR 1,020, EUR 108, EUR 229.50, EUR 255, EUR 510, EUR 27 and EUR 20.40 agree with their stated inputs/rates.

| # | Guide/control | Independently computed expected results |
|---|---|---|
| 1 | `fi-company-formation.md`: Finland assumed Oy capital and authority fee separation | combined_cash_funding=10400; authority_fee_only=400 |
| 2 | `fi-company-formation.md`: Finland assumed separate period audit trigger counts | current_trigger_count=2; previous_trigger_count=0; highest_period_count=2 |
| 3 | `fi-corporate-income-tax.md`: Finland assumed corporate book to tax bridge | adjusted_profit=103000; taxable_income=83000; corporate_income_tax=16600 |
| 4 | `fi-corporate-income-tax.md`: Finland assumed corporate loss balance | loss_used=50000; remaining_loss=30000; taxable_income=0; corporate_income_tax=0 |
| 5 | `fi-corporate-income-tax.md`: Finland assumed corporate assessment payment reconciliation | computed_income_tax=20000; principal_uncovered=4000 |
| 6 | `fi-country-by-country-reporting.md`: Finland CbCR assumed consolidation threshold | before_eliminations=800000000; consolidated_revenue=760000000; excess_over_threshold=10000000 |
| 7 | `fi-country-by-country-reporting.md`: Finland CbCR exact assumed euro threshold | difference_from_threshold=0 |
| 8 | `fi-employer-payroll.md`: Finland 2026 employer health contribution | employer_health_contribution=382 |
| 9 | `fi-employer-payroll.md`: Finland assumed tax card ceiling crossing | remaining_ceiling=2000; basic_rate_wages=2000; additional_rate_wages=2000; withheld_tax=1200 |
| 10 | `fi-employer-payroll.md`: Finland assumed missing wage card withholding | withheld_tax=1200; remainder_before_other_deductions=800 |
| 11 | `fi-employer-payroll.md`: Finland 2026 ordinary employer unemployment bands | lower_band_wages=2509500; upper_band_wages=490500; lower_contribution=7779.45; upper_contribution=6033.15; employer_total=13812.6 |
| 12 | `fi-employer-payroll.md`: Finland assumed employee payroll deduction reconciliation | tax_withheld=600; employee_pension=219; employee_unemployment=26.7; employee_cash=2154.3; employer_health_separately=57.3 |
| 13 | `fi-employer-payroll.md`: Finland assumed cash limit on wage withholding | taxable_wage_base=2000; uncapped_withholding=800; cash_limited_withholding=500; difference_from_uncapped_amount=300 |
| 14 | `fi-income-tax.md`: Finland 2026 state earned income scale top band | excess=27900; state_scale_tax=21516.05 |
| 15 | `fi-income-tax.md`: Finland taxable capital income bands | lower_base=30000; upper_base=15000; capital_income_tax=14100 |
| 16 | `fi-income-tax.md`: Finland assumed sole trader deduction and split | business_profit=60000; profit_after_losses=50000; entrepreneur_deduction=2500; distributable_income=47500; capital_portion=4000; earned_portion=43500 |
| 17 | `fi-individual-cross-border-residence.md`: Finland assumed departure residence window | last_year_of_ordinary_window=2029; year_after_window=2030 |
| 18 | `fi-individual-cross-border-residence.md`: Finland assumed foreign tax credit ceiling | credit_used=1200; unused_credit=400 |
| 19 | `fi-individual-cross-border-residence.md`: Finland assumed credit vintage ordering | prior_used=400; remaining_limit=300; current_used=300; current_unused=200 |
| 20 | `fi-prepayments.md`: Finland assumed individual six prepayment instalments | instalment_amount=300; reconciled_total=1800 |
| 21 | `fi-prepayments.md`: Finland assumed individual monthly prepayment instalments | instalment_amount=1000; reconciled_total=12000 |
| 22 | `fi-property-transfer-tax.md`: Finland housing share debt free price | established_base=240000; transfer_tax=3600; cash_only_tax=2700; omitted_tax=900 |
| 23 | `fi-property-transfer-tax.md`: Finland assumed direct real estate transfer tax | transfer_tax=7500 |
| 24 | `fi-property-transfer-tax.md`: Finland assumed contingent real estate consideration tax | original_tax=7500; additional_tax=1500; combined_tax=9000 |
| 25 | `fi-transfer-pricing.md`: Finland assumed controlled sale price reconciliation | booked_revenue=210000; supported_revenue=240000; assumed_adjustment=30000 |
| 26 | `fi-transfer-pricing.md`: Finland documentation counterparty aggregation | counterparty_total=530000; excess_over_limit=30000 |
| 27 | `fi-transfer-pricing.md`: Finland assumed gross cost plus computation | gross_profit=8000; transaction_revenue=108000; sales_margin_percent=7.40740740741 |
| 28 | `fi-yel-social.md`: Finland assumed eligible YEL review cap without higher consent | proposed_increase=7000; capped_increase=4000; capped_review_income=24000 |
| 29 | `fi-yel-social.md`: Finland 2026 assumed standard YEL contribution | annual_contribution=7320; monthly_equivalent=610 |
| 30 | `fi-yel-social.md`: Finland assumed eligible YEL startup reduction | standard_contribution=7320; contribution_after_reduction=5709.6 |
| 31 | `finland-vat-return.md`: Finland assumed 2026 restaurant separate rates | food_vat=94.5; wine_vat=25.5; output_vat=120 |
| 32 | `finland-vat-return.md`: Finland assumed reverse charge mixed use | reverse_charge_vat=255; deductible_vat=178.5; net_vat_cost=76.5 |
| 33 | `finland-vat-return.md`: Finland assumed original VAT return late filing penalty | daily_component=135; percentage_component=80; filing_penalty=215 |

Calendar checks independently used Python date arithmetic: 31 January 2027 and 28 February 2027 are Sundays; 29 January 2027 is Friday and 1 March 2027 is Monday. The corporate ordinary example date 31 July 2026 is Friday. All five state-scale rows were matched to the Scale Act and successive boundary amounts recomputed; the bands are continuous.

## Unresolved review limits and publication conditions

- This is a full-pack editorial/source review with selected legal verification. It is not an exhaustive audit of every cited statute, amendment chain, source URL or possible exception. No claim that all 98 reachable URLs received independent legal-content verification is made.
- No Finnish accountant credential is held out. Named Finnish accountant review, any statutory responsibility and tier-1 approval remain separate and open. Review status must not be changed to professional approval.
- Annual decrees/insurance-specific terms, full health-contribution deduction/assessment mechanics, detailed benefit eligibility, every special insurance category, all treaty/PE/CFC/exit/minimum-tax rules, benchmarking and transaction-specific entitlement remain open as the pack describes.
- The 2027 personal filing calendar, current CbCR exchange/schema/authorisation application, exceptional property/correction calendars, live MyTax/report/payment procedures and unusual entity/sector rules were not established. No live filing, payment or client case was tested.
- Source rules in unofficial English administrative translations remain subject to official Finnish/Swedish language. Statutory excerpts were read in Finnish; this is not a certified translation.
- Repository test success and the 98-URL snapshot were inspected as evidence only; the reviewer did not rerun the entire 129-test repository suite or independently rerun every reachability request. Independent arithmetic was rerun for all 33 blocks. No evidence is supplied here for any future pushed head's CI.
- Resolve FI-1 through FI-6 together, advance substantive source versions, update precise source/read records and obtain independent closure against the corrected checkpoint before the one-country content push. Preserve all seven partial flags, issue #392 open, draft PR #514 and pending named-accountant review. Any new legal claim beyond these fixes requires corresponding source checking.


## Frozen source manifest: all files examined

| File | Exact Git blob |
|---|---|
| `skills/international/finland/README.md` | `aeb574ad6cab913d3d7ec84143487d49d9679a27` |
| `skills/international/finland/fi-company-formation.md` | `c1085275a205c97e401071a31f87894ef23c506d` |
| `skills/international/finland/fi-corporate-income-tax.md` | `81e683462c429d75c8d767790e9d85ada92bf740` |
| `skills/international/finland/fi-country-by-country-reporting.md` | `5c8f2da6a6aa51b7465a99f764b23543f5422310` |
| `skills/international/finland/fi-employer-payroll.md` | `4727ca37f0e1226875ee55b9547e4c9c5fd5b948` |
| `skills/international/finland/fi-income-tax.md` | `6e925c7e367e6d62e49be71b73ee553ee86f7738` |
| `skills/international/finland/fi-individual-cross-border-residence.md` | `8792b6c359837cf8f4efec0a0d47f90b6a571e6d` |
| `skills/international/finland/fi-prepayments.md` | `b13b83dffef33a1d6ada777747296f78ea9d911e` |
| `skills/international/finland/fi-property-transfer-tax.md` | `53ae8c25e21f04d0fd96a245c6b1e42d31f5df99` |
| `skills/international/finland/fi-tax-overview.md` | `c1f3305489f40d0fdc459a51d4e8965aacd28028` |
| `skills/international/finland/fi-transfer-pricing.md` | `782ccd9ab3056ecb5c93974c4c7e1b2c9262919f` |
| `skills/international/finland/fi-yel-social.md` | `5c06ddccc04a8a485d6088ce8e2d9a3bedb2be77` |
| `skills/international/finland/finland-vat-return.md` | `b0ea89e766deaddf7c3cb74dbbc0e1b2d68a8194` |

## Final correction closure addendum

**Final source/status checkpoint:** `c83ca9f5455b9560937c797c20ecd1b7b102b363`, reviewed 23 October 2026. This addendum supersedes the initial corrections-required decision above for the exact final source blobs below. The original review record remains intact so the defects, evidence and fixes can be traced.

I reviewed the complete corrective diffs at `a357563cbd028d76f267df761c3e798d628535a4`, the narrow VAT revision at `1b02f2f2cf1d3e49310f0134ca6308cb6ef8c08d`, the status/evidence pass at `6a251b92a1d4c580e83e39bedb3ae57aa3163d02` and the final payroll/prepayment status revision at the final checkpoint.

| Finding | Closure evidence and result |
|---|---|
| FI-1 | YEL table and section 5a now state the health-care substitution for relevant business income/own-company wages, retain other nonreplaced earned income, distinguish daily allowance and employer liabilities, and cite the substitution source. Closed. |
| FI-2 | EU/non-EU service rows now require Finnish supply and purchaser liability; passenger transport is correctly excluded. A separate gate covers seller registration/participating establishment. Cases F/G and the mixed-use block's assumptions refer to those gates. No Finnish tax is inferred from a hotel/supplier abroad. Closed. |
| FI-3 | YEL eligibility now expressly begins no earlier than the calendar month after the eighteenth birthday; the statutory citation is supplied. Closed. |
| FI-4 | Changed-business example preserves prospective ordinary changes and explicitly refers disability-pension cases to section 112a before ruling out retrospective amendment. Closed. |
| FI-5 | Payroll expressly requires liable employee deductions below the employer payment threshold, states retention of those deductions in the below-threshold case and requires reporting. Closed. |
| FI-6 | VAT introductory/referral scope now distinguishes the provided filing-penalty screen from open late-payment/other sanctions. Closed. |

**Narrow corrective regression:** the first correction used an unqualified event-admission example among reverse-charge exclusions. I checked VAT Act section 69d(2), whose virtual B2B participation carveout applies from 1 January 2025, and requested removal/narrowing of that example. The writer removed it at `1b02f2f2`; the final row keeps only passenger transport as its example. No blanket virtual-admission exclusion remains. Closed.

**Final status consistency:** I read every country status/version diff. The final pass preserves legal and specialist gaps, all seven README partial flags, all source `tier: 2` values and the tax year. It replaces stale pending-independent-review language with the record pointer or pending named Finnish accountant review. The two missed payroll/prepayment phrases at the preceding checkpoint were corrected at the final checkpoint. No new legal assertion was introduced in that last status pass. Existing generated CTA/provenance was preserved.

All 33 calculation blocks are byte-identical to the initial reviewed checkpoint. I nevertheless ran `/private/tmp/independent-fi-check.py` against the final checkpoint: **33/33 pass across eleven Guides**. Final results, including the checkpoint, are retained in `/private/tmp/independent-fi-arithmetic-final.json`. All thirteen final source-file SHA-256 hashes also match the updated reachability evidence's source identities. The writer's reachability inventory now contains 101 URLs; the new total is a reachability count, not an independent audit of 101 legal sources.

**Final disposition:** no actionable review finding remains open for these final country blobs within the stated editorial/source-review scope. The country can proceed through final repository checks and its one-country content publication gate with this record included. This does not assert complete country coverage, Finnish professional approval, live filing readiness, future CI success or a merge decision. The source/evidence report must be copied to `docs/research/2026-10-23-finland-pack-review.md` before publication to fulfil README's link. A later evidence-only commit can retain this closure only if all thirteen country blobs below remain identical; any later substantive source change needs its own review.

### Final country blob manifest

| File | Version | Git blob at final checkpoint |
|---|---:|---|
| `skills/international/finland/README.md` | 0.9 | `61a5ca7e4ffe4b8d899f21f609d00b37a1a89135` |
| `skills/international/finland/fi-company-formation.md` | 0.2 | `7f1771a51549e93c169a1fe8b12816d8d60ff94b` |
| `skills/international/finland/fi-corporate-income-tax.md` | 1.2 | `34477c09730862ce28c0515c313277dc83d33601` |
| `skills/international/finland/fi-country-by-country-reporting.md` | 0.4 | `902dfaeebb43a9d6b31f910e80d5fbda93d8a3bd` |
| `skills/international/finland/fi-employer-payroll.md` | 0.7 | `3d09ba38418c3d3c18ec0ed42ae463c325a899f3` |
| `skills/international/finland/fi-income-tax.md` | 1.3 | `a7d3cb277b13521f1b5c686fd06c1f48f2de0469` |
| `skills/international/finland/fi-individual-cross-border-residence.md` | 0.4 | `121ed1266bf81c6eefbd707cf48cf052411ae9e0` |
| `skills/international/finland/fi-prepayments.md` | 1.2 | `dde78c86b61e9c823d6778c9fe2c6761687df262` |
| `skills/international/finland/fi-property-transfer-tax.md` | 0.3 | `bd533c32979dc566b43207be9f70cfa4d24a1778` |
| `skills/international/finland/fi-tax-overview.md` | 0.3 | `3e1c772b6acc30244e6436a3347381ad958be824` |
| `skills/international/finland/fi-transfer-pricing.md` | 0.5 | `2bad9418efd0c19ce3543541724fb7d40c712b95` |
| `skills/international/finland/fi-yel-social.md` | 1.4 | `11ef60301ade8c74281f518802b14aaeccc76474` |
| `skills/international/finland/finland-vat-return.md` | 2.5 | `579aaf239d685eda56c8970656fb90b57dc8d1c0` |
