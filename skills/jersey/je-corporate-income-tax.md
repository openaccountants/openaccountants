---
name: je-corporate-income-tax
description: >
  Jersey ordinary corporate income tax for 2026, including company residence,
  sector rates, large corporate retailer calculations, tax return duties and
  the distinction between zero rating and exemption. Use for Jersey company
  tax, zero ten, retail taper, financial services or corporate tax filing.
  Includes a statutory retail calculation for a standalone annual period
  and identifies associated-company and period-length adjustments. Pillar Two
  is covered separately. Adds ordinary deduction, capital allowance, loss, group-relief and
  company-payment rules with bounded examples. Distribution allocations and
  specialist adjustments need transaction-specific verification. This source-cited
  draft awaits professional review and must not be used to infer that every
  Jersey company pays no tax.
jurisdiction: JE
category: international
tax_year: 2026
tier: 2
last_updated: 2026-10-15
version: 1.2
review_status: pending_review
depends_on:
  - workflow-base
  - corporate-income-tax-workflow-base
---

# Jersey corporate income tax: 2026

## Scope and registration

Under [Income Tax Law, Article 123](https://www.jerseylaw.je/laws/current/l_29_1961), a Jersey incorporated company is generally Jersey resident. The exception requires central management and control abroad, residence there, and a jurisdiction whose highest company tax rate meets the statutory 10% test. A foreign incorporated company managed and controlled in Jersey is Jersey resident. Confirm the actual facts and any treaty before changing residence treatment.

JFSC incorporation passes company details to Revenue Jersey for automatic corporate tax registration. A foreign company must notify Revenue Jersey within 6 months of becoming resident or acquiring a potentially taxable Jersey income source. Ordinary annual company return duties include companies paying tax at zero. See [company tax guidance](https://www.gov.je/Industry/BusinessAdviceHub/BusinessTaxesSocialSecurity/pages/companytax.aspx), subject to the statutory multinational exception below.

[Income Tax Law, Articles 120AB and 120AC](https://www.jerseylaw.je/laws/current/l_29_1961) qualify that generic guidance. Article 120AB exempts income, profits and gains of a relevant MNE group entity from ordinary income tax. The entity must be a Jersey constituent entity for the relevant whole or part of the assessment year, and its group must be a chargeable MNE group under the MCIT Law for a fiscal year ending in that assessment year. Part-year status requires apportionment under Article 120AB(3). Article 120AC disapplies the specified ordinary company-return requirement for the year or period in which the company meets that status. Establish these conditions and the separate MCIT obligations before deciding which return is required; registration alone does not establish exemption. See `je-pillar-two`.

## Rate classification

Classify each source and company under the applicable provisions before applying a rate. A zero rate is not statutory exemption. The [company guidance](https://www.gov.je/Industry/BusinessAdviceHub/BusinessTaxesSocialSecurity/pages/companytax.aspx), [corporate return notes](https://www.gov.je/TaxesMoney/IncomeTax/Companies/CompanyTaxGuidance/pages/companytaxreturnnotes.aspx) and [Income Tax Law, Articles 123C to 123DA](https://www.jerseylaw.je/laws/current/l_29_1961) identify the ordinary structure:

| 2026 classification | Ordinary treatment |
|---|---|
| Company without an applicable exception | 0% |
| Qualifying financial services company | 10% |
| Utility company | 20% |
| Specified Jersey property income, hydrocarbon trade and quarrying | 20% under the relevant income provisions |
| Company in the statutory cannabis industry category | 20% |
| Large corporate retailer | Retail computation below |

Definitions, deductions and source rules determine whether an exception applies. First check relevant MNE group status and the ordinary-tax exemption above. The separate multinational computation in `je-pillar-two` is not a flat surcharge on this table.

## Large corporate retailer computation

[Income Tax Law, Articles 123H to 123L](https://www.jerseylaw.je/laws/current/l_29_1961) and [retailer guidance](https://www.gov.je/TaxesMoney/IncomeTax/Companies/Guidelines/Pages/LargeCorporateRetailers.aspx) require Jersey residence or a permanent establishment, qualifying gross Jersey retail turnover and the retail proportion test. The ordinary 12-month turnover threshold is GBP 2 million and retail must represent at least 60% of the company's Jersey trading turnover.

Article 123J adjusts the turnover eligibility threshold to GBP 2 million x days / 365 when the relevant financial period differs from 12 months. Associated companies aggregate their qualifying retail turnover. Under Article 123J(4), the adjusted threshold uses their common period length when all periods have the same length, or the shortest relevant period when their lengths differ. Establish the statutory associations and periods before deciding eligibility. This turnover adjustment is separate from Article 123L's profit-threshold adjustment.

Bounded eligibility checks assume the residence, retail definitions and 60% test are already satisfied. A standalone 182-day period with GBP 1 million qualifying turnover passes because GBP 1 million exceeds GBP 2 million x 182 / 365. A standalone 548-day period with GBP 2.5 million turnover fails because that turnover is below GBP 2 million x 548 / 365. Two associated companies with 182-day and 365-day relevant periods and GBP 600,000 qualifying turnover each use aggregated GBP 1.2 million and the 182-day threshold under Article 123J(3) and (4). These comparisons use exact fractions and do not determine the group's profit base or payable tax.

For a standalone retailer with an ordinary 12-month relevant financial period, let A be the Article 123L Schedule D amount after applicable allowances and reliefs, excluding the deductions and credits that Article 123L(1) tells the reader to disregard:

1. If A is below GBP 500,000, Schedule D tax is zero.
2. If A exceeds GBP 750,000, compute A x 20%.
3. From GBP 500,000 through GBP 750,000 inclusive, compute B = A x 20%, C = (GBP 750,000 - A) x 40%, then tax D = B - C.
4. The corresponding tapered rate is D / A x 100. This is derived from the tax amount, not a linear interpolation of the rate.

Illustrative 2026 results, with eligibility and the Article 123L profit base already established:

| A (GBP) | Tax (GBP) | Effective rate |
|---:|---:|---:|
| 500,000 | 0 | 0% |
| 600,000 | 60,000 | 10% |
| 750,000 | 150,000 | 20% |
| 800,000 | 160,000 | 20% |

For A = GBP 600,000, B = GBP 120,000 and C = GBP 60,000. The difference is GBP 60,000. The [statutory computation](https://www.jerseylaw.je/laws/current/l_29_1961) governs each row.

Article 123L adjusts both profit thresholds by days / 365 for financial periods differing from 12 months. Associated-company calculations aggregate relevant profits, treat a group member's loss as zero for this aggregation, apply the period rules and apportion tapered tax. The simple table is unavailable for those cases until the group and periods are established. Retail loss carryforward, group relief and capital allowances have additional restrictions; see the [retailer guidance](https://www.gov.je/TaxesMoney/IncomeTax/Companies/Guidelines/Pages/LargeCorporateRetailers.aspx).

## Deductions and capital allowances

Reconcile approved accounting profit to the statutory tax base before applying a sector rate. [Income Tax Law, Article 70](https://www.jerseylaw.je/laws/current/l_29_1961) requires business expenditure to be wholly and exclusively for the trade or profession and contains specific disallowances for private expenditure, capital, unrelated losses, insurance-recoverable amounts, certain interest, annual payments and patent royalties. Bad and doubtful debts have their own evidence conditions. This is not a general permission to deduct every expense in the accounts. Establish the applicable exceptions before treating interest or another listed item as deductible.

[Article 70F](https://www.jerseylaw.je/laws/current/l_29_1961) permits accounting-service fees attributed to the accounting period for which they were incurred, or final accounts before cessation. [Article 70E](https://www.jerseylaw.je/laws/current/l_29_1961) permits a deduction of 150% of eligible regulatory-compliance expenditure from assessment year 2024: computer hardware, software including subscriptions/licences, and external-provider hardware/software training. [Article 3AF](https://www.jerseylaw.je/laws/current/l_29_1961) limits regulatory compliance activity to listed financial-crime, data/cyber-risk, JFSC risk/conduct and related reporting/compliance activities carried out by an eligible entity. That entity must be a JFSC-registered financial services business within the Proceeds of Crime Law and a financial services company taxed under Article 123D. Ordinary IT expenditure or registration alone does not establish eligibility. A regulated financial institution still fires the corporate base refusal and requires the sector companion.

For qualifying plant and machinery, [Articles 106A to 106C](https://www.jerseylaw.je/laws/current/l_29_1961) and the [capital allowance explanation](https://www.gov.je/TaxesMoney/IncomeTax/BusinessesSelfEmployed/CapitalAllowances/pages/explanation.aspx) require the ownership/use and basis-period conditions:

| Ordinary pool step | Treatment |
|---|---|
| Qualifying expenditure | Unrelieved balance brought forward plus qualifying additions not already included |
| Disposal adjustment | Subtract statutory disposal values, including applicable insurance, compensation or market-value rules |
| Positive excess, ordinary 12-month financial period | Allowance of 25%; carry the unallowed balance forward |
| Other financial-period length | Proportionately adjust the percentage under Article 106A(2A) |
| Disposal values exceed qualifying expenditure | Balancing charge equal to that excess |
| Permanent cessation | Ordinarily a balancing allowance for the whole positive excess; check the succession exception |
| Glasshouses | Separate Article 106B treatment substitutes 10% and has a specific transfer rule |

Article 106A(7) and (8) requires separate, just-and-reasonable treatment for mixed business/private use. Article 106C excludes States-funded expenditure, prevents a second deduction for the same capital expenditure and carries forward allowances that cannot be used against trade profits. A recorded asset purchase or accounting depreciation does not itself establish the tax allowance. Succession under Article 106AB and changes of use require their specific rules.

[Article 106BA](https://www.jerseylaw.je/laws/current/l_29_1961) separately substitutes 150% for qualifying regulatory-compliance hardware/software capital expenditure from assessment year 2024. Expenditure deducted under Article 70E cannot also use this provision. The pre-2024 connected-person transfer exclusion and disposal clawbacks must be tested: an ordinary disposal generally recaptures 100% of the statutory disposal value; a connected-person disposal uses market value and recaptures 150% if fewer than 3 financial periods have elapsed, or 100% from 3 periods. Keep the enhanced schedule distinct to prevent duplicate expenditure or relief; a 150% label alone does not establish eligibility.

## Losses and group relief

[Article 108](https://www.jerseylaw.je/laws/current/l_29_1961) carries an unrelieved trading/professional loss forward against the same trade or profession, using the earliest subsequent assessment as far as possible. Keep a year-by-year register of the original loss, relief already given, surrender and balance. The same loss cannot be relieved twice. This provision does not authorise use against unrelated income.

[Articles 107 and 107A](https://www.jerseylaw.je/laws/current/l_29_1961) provide current-year adjustment and immediately preceding-year carryback on written claims within their respective 2-year periods. Both exclude companies within Articles 123C or 123D; Article 123P also excludes large corporate retailers. Do not present carryback as available to an ordinary zero-rated company. Article 110B permits an election treating an Article 106A(2) capital allowance as a loss for Articles 107/107A and disapplies the ordinary allowance carryforward for that elected amount. An election does not remove the claimant restrictions in those loss provisions.

Under [Article 123F](https://www.jerseylaw.je/laws/current/l_29_1961), the claimant and surrenderer must be members of the same statutory group and both within Article 123C, or both within Article 123D, throughout the surrender period. The claimant applies no later than 1 year after the end of the relevant assessment year and supplies the surrenderer's declaration, including previous surrenders. Different financial periods restrict surrender to the overlap. Schedule A property-rental profits and losses under Article 51(1)(a) are excluded; development and quarrying categories have matching-source restrictions under Article 123F(9).

The Article 123F control definition requires the power to secure the controlled company's affairs through one or more of the listed share, voting or constitutional powers of **more than 50%**, together with rights to **more than 50% of profits and gains**. Establish direct/indirect rights and the ultimate holding company from the legal documents. A percentage of ordinary shares alone does not prove the group. [Article 123S](https://www.jerseylaw.je/laws/current/l_29_1961) modifies the permitted group composition for retailers, but both claimant and surrenderer must be large corporate retailers; a zero-rated member cannot surrender to a retailer merely because it is in the wider group.

## Distributions and vouchers

Corporate profits are computed before dividends under [Article 88](https://www.jerseylaw.je/laws/current/l_29_1961). It permits deductions associated with profits taxed at 20% or 10% subject to its exceptions, and prohibits a tax deduction on a dividend from Article 123C profits taxed at 0%. Recipient credits have separate conditions and limits. A recipient's liability is not established by subtracting a flat corporate rate from 20%.

Classify the transaction under Articles 3AE, 78 and the relevant Case III/IX provisions before allocating a distribution. A capital label alone does not establish the Article 78 exemption. Full distribution allocation, Case IX/participator rules, MCIT distribution credits and non-resident treatment remain outside the supplied computation; use Needs Input until their complete applicable provisions and facts are verified.

[Article 89](https://www.jerseylaw.je/laws/current/l_29_1961) specifies vouchers showing the relevant gross portions, corporate rates, deductions and net payments, with exceptions. For distributions within Article 89(1A), provide the individual statement within 1 month after the assessment year ends; Article 89(1B) requires the company-recipient statement at distribution or as soon as reasonably practicable afterwards. The [distribution guidance](https://www.gov.je/taxesmoney/incometax/companies/reportingcompanies/pages/distributionsextension.aspx) separately states a penalty concession if information is supplied by 31 December of the following year. That concession does not rewrite the statutory deadline or establish exemption of every capital distribution.

## Company instalments and balance

For Jersey resident companies and Jersey permanent establishments within ordinary income tax, [Articles 39 and 41AB](https://www.jerseylaw.je/laws/current/l_29_1961) set the following dates in the year following the assessment year:

| Company classification | Instalment | Balance |
|---|---|---|
| Other than large company | 50% of the reasonable estimated liability by midnight 31 May | 30 November |
| Large company under Article 41AB(7) | 50% of the reasonable estimated liability by midnight 31 March | 30 September |

A large company must notify the Comptroller by 31 March if the estimated instalment is zero. The duty does not depend on an assessment having been raised, subject to that notification. Reconcile the final assessed liability, credits and evidenced payments once before calculating the remaining balance. Return filing remains a separate obligation.

Article 41AB(7) includes liability **equal to or above GBP 500,000 in each of the 2 assessment years immediately preceding the assessment year in which the instalment is payable**. The [payment guidance](https://www.gov.je/TaxesMoney/IncomeTax/Companies/ReportingCompanies/Pages/CompanyTaxPaymentDates.aspx) uses a broad 'exceeds' description and a different look-back description. Use the statute's inclusive boundary and exact year reference. The guide's second historical example also changes its assessment-year label mid-example; it is not used to establish a period rule here. Obtain both relevant liabilities and the payment year before classifying a company.

## Additional hypothetical positions

These 2026 examples assume the stated eligibility, ordinary 12-month periods, validated inputs and no other credits or adjustments. They are arithmetic or classification checks, not executed financial outputs.

| Position | Inputs and rule | Result |
|---|---|---|
| Ordinary capital pool | GBP 120,000 qualifying expenditure less GBP 20,000 statutory disposals; Article 106A | GBP 100,000 excess x 25% = GBP 25,000 allowance; GBP 75,000 unallowed balance |
| Balancing charge | GBP 10,000 qualifying expenditure and GBP 14,000 disposals; Article 106A(3) | GBP 4,000 charge; no positive ordinary allowance |
| Same-trade loss | GBP 30,000 validated unused loss and GBP 20,000 subsequent same-trade profit; Article 108 | GBP 20,000 loss used; taxable amount zero; GBP 10,000 remains, subject to the continuing rules |
| Ordinary company instalment | Reasonable estimate GBP 50,000 for assessment year 2026, final liability GBP 60,000, no other credit/payment; Articles 39/41AB | GBP 25,000 by 31 May 2027; GBP 35,000 balance by 30 November 2027 |
| Inclusive large-company boundary | Instalment payable in 2027; liabilities for 2025 and 2026 each GBP 500,000; Article 41AB(7) | Large-company timetable applies: 31 March/30 September 2027 for assessment year 2026 |
| Incomplete group evidence | Shares 60%; voting/constitutional control and profit rights unverified; Article 123F | Needs Input; no group-relief amount or complete package |

## Reviewer controls and intake

Load the universal and corporate workflow bases. This source-cited guide remains an incomplete operational companion for a full company return: all base slots, applicable credits, anti-avoidance, distribution, foreign-tax and specialist regimes must be populated and verified before a complete financial result. Missing scope or law is not permission to select a higher tax amount. Base refusals, including regulated financial institutions and active controversy, still apply.

Obtain residence/PE and MNE status; income by statutory source; approved accounts and tax reconciliation; asset ownership, use, additions, disposals, grants and period lengths; loss origins and prior use; legal group rights and overlap periods; distribution character and recipient status; payment-year look-back liabilities, estimates, notices and receipts. Use redacted references; the reviewer retains actual identifiers and portal access.

| Local refusal | Trigger | Verbatim message |
|---|---|---|
| R-JE-CIT-1 | Applicable residence, exemption, source, period or special-regime conditions are unresolved | R-JE-CIT-1: Needs Input. Establish the applicable Jersey company regime and period before accepting dependent results. |
| R-JE-CIT-2 | Deduction, allowance, loss, surrender, distribution, credit or payment classification is unsupported | R-JE-CIT-2: Needs Input. Obtain the supporting facts and complete applicable provisions; withhold dependent totals and the complete package. |
| R-JE-CIT-3 | Required base content, producer, tool, output or check is missing or invalid | R-JE-CIT-3: Needs Input. Complete and validate the required companion inputs and outputs before delivering a financial result. |

No missing-fact defaults are authorised for these ambiguities. Preserve unknown amounts as unknown; establish any N/A with evidence. Review every election, classification, adjustment, relief and deadline regardless of amount; this is a workflow review rule, not a statutory materiality exemption.

Extend the base reviewer brief and working papers with the PBT-to-tax reconciliation, separate ordinary/enhanced asset schedules, loss utilisation and surrender register, distribution-source/voucher evidence, and payment-year calendar. Identify every source, period, uncertainty and held output. Carry a credit or payment into its prescribed stage once. Do not file, amend, sign, authenticate or pay on the taxpayer's behalf.

## Filing and checks

The ordinary corporate return must be delivered online by midnight 30 November following the year of assessment. The [company guidance](https://www.gov.je/Industry/BusinessAdviceHub/BusinessTaxesSocialSecurity/pages/companytax.aspx) establishes this return deadline; it does not establish every payment deadline. Tax-resident companies and Jersey permanent establishments attach the accounts required by the [return notes](https://www.gov.je/TaxesMoney/IncomeTax/Companies/CompanyTaxGuidance/pages/companytaxreturnnotes.aspx).

Check residence, income source, sector classification, period length, associations and deductions before computing tax. Keep registry confirmations, corporate returns, substance reporting and Pillar Two separate. Complete distribution allocation, withholding, foreign-tax credits, anti-avoidance, specialist asset transfers and operational rounding remain research gaps. See je-income-tax-compliance for ordinary income-tax penalties, corrections and appeals.

## Self-checks and provenance

- Confirm every base content slot, refusal and source condition before accepting a financial result.
- Keep book depreciation and tax allowances distinct; reconcile each pool and disposal.
- Check loss eligibility, earliest use, overlap and previous relief or surrender.
- Keep retail association, Article 123F group control and company payment-size tests separate.
- Verify both look-back years, the instalment year and the filing/payment calendars.
- Reconcile utilised credits and payments once; complete all required base outputs and checks.

Revision 1.2 adds the above statutory rules and controls on 15 October 2026; version 1.1 covered residence, sector and retail classification.

Core residence, sector and retail provisions were checked on 11 October 2026. The added deduction, allowance, loss, distribution-statement and payment provisions and cited guidance were checked on 15 October 2026 against the current Income Tax Law snapshot effective from 17 June 2026. Use the applicable historical version for an earlier period or transaction. See `references.md`; this draft has no professional sign-off.

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
