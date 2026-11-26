---
name: qc-qst-return
description: >
  Prepare an ordinary Quebec general-system QST return workpaper: classify
  supported sales and ITRs, reconcile the actual return fields, calculate an
  eligible quick-method service example and distinguish filing from payment.
  Refer unresolved registration, supply, import and specialist applications.
version: 3.2
jurisdiction: CA-QC
tax_year: 2026
last_updated: 2026-11-26
depends_on:
  - vat-workflow-base
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: vat-gst
type: computation
---

# Quebec QST return v3.2

## Scope

Prepare a CAD workpaper for an ordinary sole proprietor or small business registered under the general QST system. Keep federal GST/HST calculations separate; read `canada-gst-hst` for that work. A combined GST/HST-QST return is permitted. FPZ-2034.CD-V provides detailed calculation fields supporting the actual return; establish the account and filing route before transfer. [RQ reporting](https://www.revenuquebec.ca/en/businesses/consumption-taxes/gsthst-and-qst/reporting-gsthst-and-qst/), [FPZ instructions](https://www.revenuquebec.ca/en/online-services/forms-and-publications/fpz-2034-g-v/guide-to-detailed-gst/hst-and-qst-calculations-and-the-return-respecting-taxable-real-property-immovables-taxable-carbon-emission-allowances-and-imported-taxable-supplies/).

Contributor: Open Accountants Community. This workflow produces proposed calculations and postings. It does not register, submit, pay or approve a return.

## Ask the client first

Obtain the legal entity, activities, residence, registration system/numbers/effective dates, actual filing confirmation and reporting period. Obtain invoice-level sales, tax-inclusive/exclusive amounts, supply/place evidence, unpaid invoices, credits and adjustments. For inputs obtain the legal purchaser, invoices, supplier status, tax paid/payable, commercial use, operating/capital category and previous claims. Obtain meals revenue limits, actual instalments, election confirmation and annual credit already used.

Preserve raw Desjardins, RBC, TD, BMO, Scotiabank and National Bank CSV/PDF exports where supplied. Parse actual dates, descriptions, debit/credit or signed amounts, currency and balances; reconcile transfers, duplicates and totals before tax classification. These are possible intake formats, not verified fixed bank schemas. Do not infer a taxable sale or an ITR from a bank line alone. Keep unsupported rows pending and name the missing determination.

## The method, step by step

### Registration and sales

For the ordinary small-supplier test, compare worldwide taxable supplies, including zero-rated supplies and associates, against **$30,000** for a single calendar quarter and the preceding four-quarter population. Exclude GST/HST and QST, financial services, sales of capital property and the business-goodwill consideration covered by Act article 75.2; article 294 also excludes movable-property supplies deemed outside commercial activities for federal purposes. Gambling, public service bodies and mandatory-registration exceptions are referred below. [RQ small suppliers](https://www.revenuquebec.ca/en/businesses/consumption-taxes/gsthst-and-qst/registering-for-the-gst-and-qst/small-suppliers/), [Act 294–295](https://www.legisquebec.gouv.qc.ca/fr/document/lc/T-0.1).

A single-quarter excess ends small-supplier status immediately, including the crossing supply and subsequent supplies. The rolling four-quarter route generally ends status at the end of the following calendar month. Use the actual dates, registration and transactions. [RQ timing](https://www.revenuquebec.ca/en/businesses/consumption-taxes/gsthst-and-qst/registering-for-the-gst-and-qst/small-suppliers/).

| Rate or use rule | Ordinary application | Official source |
|---|---|---|
| QST 9.975%; GST comparator 5% | Supported ordinary taxable supply; exempt and zero-rated supplies differ; GST/HST place rules remain separate | [RQ taxable supplies](https://www.revenuquebec.ca/en/businesses/consumption-taxes/gsthst-and-qst/basic-rules-for-applying-the-gsthst-and-qst/types-of-supplies/taxable-supplies/) |
| Two-step QST calculation | Sale price × 0.09975, excluding GST; a $100 exclusive sale has $5 GST and $9.98 QST after cent rounding | [RQ calculation and rounding](https://www.revenuquebec.ca/en/businesses/consumption-taxes/gsthst-and-qst/collecting-gst-and-qst/calculating-the-taxes/) |
| Operating inputs: ≤10%, >10% to <90%, ≥90% commercial use | Respectively nil, proportionate, full for services/non-capital personal property; do not extend this table to capital assets | [RQ operating expenses](https://www.revenuquebec.ca/en/businesses/consumption-taxes/gsthst-and-qst/itcs-and-itrs/claiming-itcs-and-itrs/operating-expenses/) |
| Ordinary meals: 50% of eligible tax | Current-half method; actual commercial use, expense ceiling and exceptions still apply | [RQ meals](https://www.revenuquebec.ca/fr/entreprises/taxes/tpstvh-et-tvq/situations-particulieres-liees-a-la-tpstvh-et-a-la-tvq/frais-de-repas-et-de-representation-cti-et-rti/) |
| Meals expense ceiling: revenue ≤$32,500: 2%; >$32,500 and <$52,000: $650; ≥$52,000: 1.25% | Ceiling on expenses supporting QST ITRs, not a maximum refund in dollars | [RQ meals expense limits](https://www.revenuquebec.ca/fr/entreprises/taxes/tpstvh-et-tvq/situations-particulieres-liees-a-la-tpstvh-et-a-la-tvq/frais-de-repas-et-de-representation-cti-et-rti/) |

Round half a cent or more up to the next cent; when several items are sold, taxes may be calculated on their total price before rounding. Reconcile actual invoice rounding rather than substitute a rounded tax rate. Currency conversion and other calculation methods are referred below. [RQ rounding](https://www.revenuquebec.ca/en/businesses/consumption-taxes/gsthst-and-qst/collecting-gst-and-qst/calculating-the-taxes/).

### Inputs and return fields

For the general method, establish registrant status in the period tax was paid or became payable and eligible commercial use. Personal/exempt-use purchases do not create ordinary ITRs. Supporting-document, supplier-status and special-input issues go to the referral table. [RQ ITR entitlement](https://www.revenuquebec.ca/en/businesses/consumption-taxes/gsthst-and-qst/itcs-and-itrs/).

The general ITR claim period is **four years from the filing deadline of the return in which it could first be claimed**. Two-year claimant classes and their exceptions exist; do not apply four years universally. Establish claimant category, first eligible period and previous claims before proceeding. [RQ claim periods](https://www.revenuquebec.ca/en/businesses/consumption-taxes/gsthst-and-qst/itcs-and-itrs/claiming-itcs-and-itrs/).

Use the detailed fields as a workpaper, then transfer to the actual account's return:

| Field | Meaning | Official source |
|---|---|---|
| 101 | Total value of supplies excluding GST/HST and QST; under the quick method include GST/HST | [FPZ 2.1](https://www.revenuquebec.ca/en/online-services/forms-and-publications/fpz-2034-g-v/guide-to-detailed-gst/hst-and-qst-calculations-and-the-return-respecting-taxable-real-property-immovables-taxable-carbon-emission-allowances-and-imported-taxable-supplies/) |
| 203 | QST collected, payable to the registrant or deemed collected, including tax collected in error and applicable taxable imports; immovable/emission-allowance acquisitions are separate | [FPZ 2.3](https://www.revenuquebec.ca/en/online-services/forms-and-publications/fpz-2034-g-v/guide-to-detailed-gst/hst-and-qst-calculations-and-the-return-respecting-taxable-real-property-immovables-taxable-carbon-emission-allowances-and-imported-taxable-supplies/) |
| 204 / 207 | Supported additions to collectible tax / deductible adjustments; entitlement to a bad-debt or credit-note adjustment is referred | [FPZ 2.3](https://www.revenuquebec.ca/en/online-services/forms-and-publications/fpz-2034-g-v/guide-to-detailed-gst/hst-and-qst-calculations-and-the-return-respecting-taxable-real-property-immovables-taxable-carbon-emission-allowances-and-imported-taxable-supplies/) |
| 206 | Eligible current or previously unclaimed ITRs on taxable/zero-rated activity; excludes exempt-use tax and tax on motor vehicles purchased for resale | [FPZ 2.3](https://www.revenuquebec.ca/en/online-services/forms-and-publications/fpz-2034-g-v/guide-to-detailed-gst/hst-and-qst-calculations-and-the-return-respecting-taxable-real-property-immovables-taxable-carbon-emission-allowances-and-imported-taxable-supplies/) |
| 209 | (203 + 204) − (206 + 207); positive net tax is owing, negative is a refund position | [FPZ calculation form](https://www.revenuquebec.ca/documents/en/formulaires/fpz/FPZ-2034.CD-V(2026-09).pdf), [RQ net tax](https://www.revenuquebec.ca/en/businesses/consumption-taxes/gsthst-and-qst/reporting-gsthst-and-qst/) |
| 210 | Actual QST instalments paid | [FPZ 2.3](https://www.revenuquebec.ca/en/online-services/forms-and-publications/fpz-2034-g-v/guide-to-detailed-gst/hst-and-qst-calculations-and-the-return-respecting-taxable-real-property-immovables-taxable-carbon-emission-allowances-and-imported-taxable-supplies/) |

Tax billed but unpaid is included when collectible; bank deposits alone are insufficient. A calculated refund is not proof of an accepted or paid refund. Rebates, offsets and fields 211/213/214/216 require the determinations in the referral table. [RQ net tax](https://www.revenuquebec.ca/en/businesses/consumption-taxes/gsthst-and-qst/reporting-gsthst-and-qst/).

### Quick method

Do not use quick remittance rates as customer tax rates. Before using this method, obtain the actual valid election and confirm eligibility. RQ's ceiling is **$400,000 including GST/HST, or $418,952 including QST**, using worldwide taxable sales including zero-rated sales and associates for any **four consecutive** fiscal quarters within the five most recent quarters. Exclude exempt sales, financial services, real property, capital assets and goodwill. [RQ eligibility](https://www.revenuquebec.ca/en/businesses/consumption-taxes/gsthst-and-qst/reporting-gsthst-and-qst/the-quick-method-of-accounting-for-calculating-gst-and-qst-remittances/who-can-use-the-quick-method/).

Excluded entities include listed financial institutions, charities, qualifying non-profits, selected public service bodies, legal/accounting/actuarial practices, fiscal/financial consultants, bookkeepers and tax-return preparers. Election commencement, commercial-activity/revocation history, new registrants and the goods-route eligibility test require the referral below; a small service business is not automatically eligible. [RQ exclusions](https://www.revenuquebec.ca/en/businesses/consumption-taxes/gsthst-and-qst/reporting-gsthst-and-qst/the-quick-method-of-accounting-for-calculating-gst-and-qst-remittances/who-can-use-the-quick-method/), [regulation 434R0.11/.15](https://www.legisquebec.gouv.qc.ca/fr/document/rc/T-0.1,%20r.%202).

For a business already established as eligible for the ordinary service route, use **6.6% of eligible QST-inclusive sales** in ordinary business transactions. Zero-rated sales and special capital/property transactions require separate treatment; do not apply the rate to all deposits. Do not deduct ordinary operating ITRs again. [RQ rates and transaction boundary](https://www.revenuquebec.ca/fr/entreprises/taxes/tpstvh-et-tvq/declaration-de-la-tps-et-de-la-tvq/methode-rapide-de-calcul-des-montants-de-la-tps-et-de-la-tvq-a-remettre/taux-applicables/), [FPZ 2.3](https://www.revenuquebec.ca/en/online-services/forms-and-publications/fpz-2034-g-v/guide-to-detailed-gst/hst-and-qst-calculations-and-the-return-respecting-taxable-real-property-immovables-taxable-carbon-emission-allowances-and-imported-taxable-supplies/).

The **1% credit** applies to the first **$31,421** of eligible QST-inclusive taxable sales excluding zero-rated sales **per fiscal year**, cumulatively across returns, with no unused credit carried into the next fiscal year. The election must have been in force from fiscal-year start, or from registration day where registration began during that fiscal year. Confirm the remaining annual eligible base; report the credit at 207. A fresh allowance each return would be wrong. [RQ annual credit](https://www.revenuquebec.ca/fr/entreprises/taxes/tpstvh-et-tvq/declaration-de-la-tps-et-de-la-tvq/methode-rapide-de-calcul-des-montants-de-la-tps-et-de-la-tvq-a-remettre/taux-applicables/), [regulation 434R0.13 D(a)–(c)](https://www.legisquebec.gouv.qc.ca/fr/document/rc/T-0.1,%20r.%202).

### Filing and payment

Use the frequency shown on the registration confirmation, based on the registrant's and associates' expected Canadian taxable sales; obtain actual elections rather than infer a period from bank activity. [RQ frequency](https://www.revenuquebec.ca/en/businesses/consumption-taxes/gsthst-and-qst/reporting-gsthst-and-qst/filing-frequency/).

Monthly/quarterly returns are due within **one month after period end**; ordinary annual returns generally within **three months**. An individual registrant with business income other than property income, annual frequency and a **31 December** fiscal year files by **15 June** of the following year but pays by **30 April**. For the 2026 period these ordinary dates are **15 June 2027** and **30 April 2027**; account for applicable non-business-day adjustments. [RQ deadlines](https://www.revenuquebec.ca/en/businesses/consumption-taxes/gsthst-and-qst/reporting-gsthst-and-qst/filing-frequency/), [FPZ filing rule](https://www.revenuquebec.ca/en/online-services/forms-and-publications/fpz-2034-g-v/guide-to-detailed-gst/hst-and-qst-calculations-and-the-return-respecting-taxable-real-property-immovables-taxable-carbon-emission-allowances-and-imported-taxable-supplies/).

Registrants must file for each reporting period even where no amount is payable; obtain confirmation of any designated-period exception. Ordinary registrants other than charities must file electronically under the rule effective **1 January 2024**. Use the actual account's filing channel and retain its acknowledgement. Payments of **$10,000 or more** must be electronic unless a specific reason prevents this. Filing and payment are separate actions; retain the payment processing/receipt evidence as well. [RQ reporting](https://www.revenuquebec.ca/en/businesses/consumption-taxes/gsthst-and-qst/reporting-gsthst-and-qst/), [FPZ receipt/payment instructions](https://www.revenuquebec.ca/en/online-services/forms-and-publications/fpz-2034-g-v/guide-to-detailed-gst/hst-and-qst-calculations-and-the-return-respecting-taxable-real-property-immovables-taxable-carbon-emission-allowances-and-imported-taxable-supplies/).

Records and supporting documents generally must be retained **six years after the end of the last year they cover**. Electronic records must remain readable and their integrity maintained. Extended retention and actual penalties/interest/relief are referred below. [FPZ 1.2](https://www.revenuquebec.ca/en/online-services/forms-and-publications/fpz-2034-g-v/guide-to-detailed-gst/hst-and-qst-calculations-and-the-return-respecting-taxable-real-property-immovables-taxable-carbon-emission-allowances-and-imported-taxable-supplies/).

## Worked cases

### Case 1: ordinary quarterly workpaper

Assume general method, tax-exclusive amounts, correct period and established classifications: $25,000 ordinary taxable sales, $2,000 zero-rated sales, $600 eligible documented ITRs, no adjustments, instalments or other rebates. Line 101 is $27,000; 203 is $2,493.75; 206 is $600; net 209 is **$1,893.75 owing**. [Rates](https://www.revenuquebec.ca/en/businesses/consumption-taxes/gsthst-and-qst/basic-rules-for-applying-the-gsthst-and-qst/types-of-supplies/taxable-supplies/), [fields](https://www.revenuquebec.ca/en/online-services/forms-and-publications/fpz-2034-g-v/guide-to-detailed-gst/hst-and-qst-calculations-and-the-return-respecting-taxable-real-property-immovables-taxable-carbon-emission-allowances-and-imported-taxable-supplies/).

```oa-check
name: Quebec ordinary quarterly original amounts with correct QST field mapping
inputs:
  standard_rate_sales: 25000
  supported_zero_rated_sales: 2000
  eligible_documented_itrs: 600
steps:
  - tax_exclusive_supplies_101: standard_rate_sales + supported_zero_rated_sales
  - qst_collectible_203: standard_rate_sales * 0.09975
  - eligible_itrs_206: eligible_documented_itrs
  - net_qst_209: qst_collectible_203 - eligible_itrs_206
expected:
  tax_exclusive_supplies_101: 27000
  qst_collectible_203: 2493.75
  eligible_itrs_206: 600
  net_qst_209: 1893.75
```

### Case 2: supported exporter/refund workpaper

Assume $5,000 ordinary taxable sales, $40,000 exports independently established as zero-rated, $1,500 eligible ITRs and no adjustments. Export status is a supplied assumption for this example, not inferred from a foreign address. Line 101 is $45,000; collectible QST is $498.75; net QST is **−$1,001.25**, a refund position. Refer the actual export/place classification before use. [Rate](https://www.revenuquebec.ca/en/businesses/consumption-taxes/gsthst-and-qst/basic-rules-for-applying-the-gsthst-and-qst/types-of-supplies/taxable-supplies/), [net calculation](https://www.revenuquebec.ca/en/businesses/consumption-taxes/gsthst-and-qst/reporting-gsthst-and-qst/).

```oa-check
name: Quebec original supported exporter refund scenario
inputs:
  standard_rate_sales: 5000
  independently_supported_zero_rated_exports: 40000
  eligible_itrs: 1500
steps:
  - total_supplies_101: standard_rate_sales + independently_supported_zero_rated_exports
  - qst_collectible_203: standard_rate_sales * 0.09975
  - net_qst_209: qst_collectible_203 - eligible_itrs
expected:
  total_supplies_101: 45000
  qst_collectible_203: 498.75
  net_qst_209: -1001.25
```

### Case 3: ordinary meals

Assume $2,000 eligible business meals, $199.50 QST, sufficient remaining expense-ceiling capacity, no exception or previous claim and current-half method. The ITR is **$99.75**. Refer other methods and exception cases. [RQ meals](https://www.revenuquebec.ca/fr/entreprises/taxes/tpstvh-et-tvq/situations-particulieres-liees-a-la-tpstvh-et-a-la-tvq/frais-de-repas-et-de-representation-cti-et-rti/).

```oa-check
name: Quebec original meals ordinary half-claim scenario
inputs:
  supported_eligible_meals_price: 2000
steps:
  - qst_on_invoice: supported_eligible_meals_price * 0.09975
  - current_half_itr: qst_on_invoice * 0.5
expected:
  qst_on_invoice: 199.50
  current_half_itr: 99.75
```

### Case 4: established eligible cleaning-service quick method

Assume the cleaning business is already eligible for the 6.6% service route, its valid election was in force from fiscal-year start, and $21,995 is its eligible QST-inclusive sales base with the full $31,421 annual credit base still unused. No capital inputs, special transactions or other adjustments apply. Gross remittance is $1,451.67, credit $219.95 and net **$1,231.72**. These assumptions do not establish eligibility for an actual business. [RQ rates/example](https://www.revenuquebec.ca/fr/entreprises/taxes/tpstvh-et-tvq/declaration-de-la-tps-et-de-la-tvq/methode-rapide-de-calcul-des-montants-de-la-tps-et-de-la-tvq-a-remettre/taux-applicables/), [credit conditions](https://www.legisquebec.gouv.qc.ca/fr/document/rc/T-0.1,%20r.%202).

```oa-check
name: Quebec quick-method eligible cleaning-service scenario
inputs:
  eligible_qst_inclusive_sales: 21995
  verified_remaining_annual_reduction_base: 31421
steps:
  - before_reduction: round(eligible_qst_inclusive_sales * 0.066, 2)
  - permitted_reduction: round(min(eligible_qst_inclusive_sales, verified_remaining_annual_reduction_base) * 0.01, 2)
  - net_quick_qst: before_reduction - permitted_reduction
expected:
  before_reduction: 1451.67
  permitted_reduction: 219.95
  net_quick_qst: 1231.72
```

### Short-period instalment arithmetic

Retain the diagnostic inputs: current-period net tax $4,000, preceding net tax $200 and covered days 20. For a fiscal-year reporting period outside article 461.1 and special financial-institution rules, Act 458.0.2 compares current net tax with annualised preceding-period tax. C is total net tax for reporting periods ending in the preceding 12 months; D is days from the start of the earliest to the end of the latest of those periods. A base below $3,000 is deemed nil. With those definitions assumed satisfied, $200 × 365 / 20 = $3,650; the lesser base is $3,650 and a quarter is $912.50. This arithmetic is not an actual instalment assessment; duty, unusual periods and due dates are referred. [Act 458.0.1–458.0.3](https://www.legisquebec.gouv.qc.ca/fr/document/lc/T-0.1).

```oa-check
name: QST prior short-period annualisation diagnostic, eligibility assumed
inputs:
  current_period_net_tax: 4000
  prior_net_tax: 200
  covered_days: 20
steps:
  - annualised_prior: prior_net_tax * 365 / covered_days
  - lesser_base: min(current_period_net_tax, annualised_prior)
  - quarter: lesser_base / 4
expected:
  annualised_prior: 3650
  lesser_base: 3650
  quarter: 912.50
```

## When to refuse or refer

For each point below, use: **Check this point with one of our partner accountants.** Do not turn a referred point into usable filing advice. Complete supported ordinary rows separately.

| Point | Action |
|---|---|
| Currency conversion; alternative invoice/cash-register calculation methods | Check this point with one of our partner accountants. |
| Voluntary/mandatory registration, taxi/admission/specified-product exceptions, public service bodies, gambling and business disposals | Check this point with one of our partner accountants. |
| Place of supply, exports and HST interaction; basic groceries, prescription drugs, residential rent, financial services, printed books/ISBN/electronic bundles, children's clothing versus diapers/accessories | Check this point with one of our partner accountants. |
| Discounts, returns, credit notes, bad-debt write-offs/recoveries, their timing and duplicate-recovery prevention | Check this point with one of our partner accountants. |
| Invoice-information thresholds, supplier validation, special/two-year claimants, capital assets, vehicles and home office | Check this point with one of our partner accountants. |
| Foreign SaaS/imports, non-residents, platforms, specified-system tax and general-system ITR treatment (R-QC-QST-3); financial-institution status and allocations (R-QC-QST-1) | Check this point with one of our partner accountants. |
| Full-current-year meals method, later adjustment and truck-driver/charity/public-institution exceptions | Check this point with one of our partner accountants. |
| Property/self-supply, housing rebates, change of use, emission allowances (R-QC-QST-2); return rebates, fields 211/213/214/216, VD-403.E vehicle-export rebate and cross-tax offsets | Check this point with one of our partner accountants. |
| Quick election/revocation deadlines and history, new registrants, capital transactions, 3.4% goods route and its defined 40% numerator/period/base | Check this point with one of our partner accountants. |
| Assigned-frequency threshold/special-entity choices, designated periods and supplementary return channels | Check this point with one of our partner accountants. |
| Actual instalment duty/amount, article 461.1 periods, mid-month quarter (including a 15 June quarter end) and non-business-day due dates | Check this point with one of our partner accountants. |
| Extended records retention, penalties, current interest, relief and appeals | Check this point with one of our partner accountants. |

## Completion checklist

Reconcile the two taxes separately, preserve source documents and every original example input, identify pending classifications, prevent duplicate claims and distinguish proposed journals from authorised postings. Obtain professional review and actual human filing authority. An account login or saved workpaper is not a filing or payment receipt.

## Sources

Completed unchanged official HTML reads from 23 November are reused; new reads resolve specific quotation gaps. The Act and regulation reads cover selected provisions, not the whole legislation. The rewritten IN-203 reader summary is not used as proof of retained tax rules.

| Official source and scope | URL | Read on |
|---|---|---|
| Read for Taxable-supply rate | https://www.revenuquebec.ca/en/businesses/consumption-taxes/gsthst-and-qst/basic-rules-for-applying-the-gsthst-and-qst/types-of-supplies/taxable-supplies/ | 2026-11-23 |
| Read for Small-supplier scope/timing | https://www.revenuquebec.ca/en/businesses/consumption-taxes/gsthst-and-qst/registering-for-the-gst-and-qst/small-suppliers/ | 2026-11-23; 2026-11-26 |
| Read for FPZ detailed fields, receipt, records and payment | https://www.revenuquebec.ca/en/online-services/forms-and-publications/fpz-2034-g-v/guide-to-detailed-gst/hst-and-qst-calculations-and-the-return-respecting-taxable-real-property-immovables-taxable-carbon-emission-allowances-and-imported-taxable-supplies/ | 2026-11-23; header follow-up 2026-11-25 |
| Read for Reporting, electronic filing and net tax | https://www.revenuquebec.ca/en/businesses/consumption-taxes/gsthst-and-qst/reporting-gsthst-and-qst/ | 2026-11-26 |
| Read for Calculation and invoice rounding | https://www.revenuquebec.ca/en/businesses/consumption-taxes/gsthst-and-qst/collecting-gst-and-qst/calculating-the-taxes/ | 2026-11-26 |
| Read for ITR entitlement, operating-use bands and claim clock | [Entitlement](https://www.revenuquebec.ca/en/businesses/consumption-taxes/gsthst-and-qst/itcs-and-itrs/); [operating](https://www.revenuquebec.ca/en/businesses/consumption-taxes/gsthst-and-qst/itcs-and-itrs/claiming-itcs-and-itrs/operating-expenses/); [clock](https://www.revenuquebec.ca/en/businesses/consumption-taxes/gsthst-and-qst/itcs-and-itrs/claiming-itcs-and-itrs/) | 2026-11-23 |
| Read for Meals method and expense ceilings | https://www.revenuquebec.ca/fr/entreprises/taxes/tpstvh-et-tvq/situations-particulieres-liees-a-la-tpstvh-et-a-la-tvq/frais-de-repas-et-de-representation-cti-et-rti/ | 2026-11-23 |
| Read for Quick eligibility and rates/annual credit | [Eligibility](https://www.revenuquebec.ca/en/businesses/consumption-taxes/gsthst-and-qst/reporting-gsthst-and-qst/the-quick-method-of-accounting-for-calculating-gst-and-qst-remittances/who-can-use-the-quick-method/); [rates](https://www.revenuquebec.ca/fr/entreprises/taxes/tpstvh-et-tvq/declaration-de-la-tps-et-de-la-tvq/methode-rapide-de-calcul-des-montants-de-la-tps-et-de-la-tvq-a-remettre/taux-applicables/) | 2026-11-23 |
| Read for Actual frequency and filing/payment split | https://www.revenuquebec.ca/en/businesses/consumption-taxes/gsthst-and-qst/reporting-gsthst-and-qst/filing-frequency/ | 2026-11-23 |
| Read for Act 294–295; 458.0.1–458.0.3, selected 15 October 2026 consolidation | https://www.legisquebec.gouv.qc.ca/fr/document/lc/T-0.1 | 2026-11-23 |
| Read for Regulation 434R0.8/.11/.13/.15, selected 1 July 2026 consolidation | https://www.legisquebec.gouv.qc.ca/fr/document/rc/T-0.1,%20r.%202 | 2026-11-23; 2026-11-25; 2026-11-26 |
| Read for Detailed form: net-tax field 209 | https://www.revenuquebec.ca/documents/en/formulaires/fpz/FPZ-2034.CD-V(2026-09).pdf | 2026-11-26 |

Not yet confirmed: all applications routed to partner accountants above, including later changes affecting specialist provisions. No actual registration, election, filing, payment, refund approval or professional sign-off is inferred.
