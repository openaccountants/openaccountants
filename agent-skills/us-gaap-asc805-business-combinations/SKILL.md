---
name: us-gaap-asc805-business-combinations
description: "ASC 805 acquisition working-paper source-recovery and amendment-basis computations. Covers acquired revenue-contract balances and measurement-period checks from official FASB Updates; broader legacy purchase accounting and goodwill topics are preserved but withheld pending current authoritative ASC access. Load financial-reporting-workflow-base."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/us-gaap-asc805-business-combinations"
  jurisdiction: "US"
  last_updated: "2026-11-16"
---

# US GAAP ASC 805 business combinations v0.3

**General reference only.** Working papers and reviewer brief only; not an audit or assurance opinion. Tier 2; not approved by an accountant.

## Scope

**Standard and effective-date basis:** ASC 805 Business Combinations (ASU 2021-08 amendment basis); effective-date key **2023-12-16**. This is the first possible fiscal-year start after 15 December 2023 for entities other than public business entities, not a universal transaction date. ASU 2021-08 applies to PBEs for fiscal years beginning after 15 December 2022 and to other entities after 15 December 2023, including interim periods therein, prospectively to combinations after adoption. Early adoption is permitted, with the specified acquisition-year treatment if adopted in an interim period; establish the actual adoption date (805-20-65-3). [Official ASU 2021-08](https://storage.fasb.org/ASU%202021-08.pdf).

Load `financial-reporting-workflow-base`. This issuer/transaction worksheet retains the complete original topic coverage, but separates the actually read amendment-basis computations from unrecovered current authoritative guidance. It does not cover the holder's accounting, control or valuation methodologies beyond the explicit steps.

**Source boundary for 2026 work.** This is a source-bounded research and computation worksheet. Current authoritative ASC text was attempted through the official site and an ordinary browser on 15 November 2026 but did not render. The FASB amendments below were opened and their stated operative paragraphs read. Each Update expressly distinguishes itself from the authoritative Codification; reading an ASU does not establish that every intervening amendment is incorporated. Consequently, the method explains only the stated amendment-basis checks. Do not use it to sign a current-ASC conclusion until the authoritative, entity-applicable text is recovered. A further official ASC web attempt on 16 November 2026 returned no operative text. Broader unresolved rules are individually reserved under Sources.

## Ask the client first

- Reporting-period start, entity type, adopted Updates and any early adoption of ASU 2025-03.
- Complete agreement, control/business/acquirer analysis, prior interest, NCI and separate-transactions assessment.
- Acquired customer contracts, transaction-price allocation, performance history, modifications, collectibility and any Topic 606 expedients.
- Provisional purchase-price allocation, valuation information dates, remaining measurement-period items and related depreciation effects.
- Every consideration, earn-out/employment, tax, benefit, lease, indemnity, intangible and goodwill fact for the withheld full-ASC handoff.

## The method, step by step

1. **Gate the transaction.** Obtain a documented conclusion that the transaction is a business combination in ASC 805 scope and identify the accounting acquirer/date from current authoritative text. This worksheet does not substitute for ASC 810 control, asset-acquisition, common-control, NFP, joint-venture or reverse-acquisition analysis. All original scope exceptions and those topics remain in the individual source requests below.
2. **Acquired customer-contract balances: ASU 2021-08 basis.** Its amendments to ASC 805-20-25-28C and -30-27/-30-28 use Topic 606 recognition and measurement as if the acquirer originated the acquired contract; do not automatically copy an acquiree balance if its application was wrong. Make inception-date and recurring assessments at the dates Topic 606 requires. This is an exception for contract assets/liabilities, not an exemption from valuing separately identifiable customer-related intangible assets. [Official amendment](https://storage.fasb.org/ASU%202021-08.pdf).
3. **Apply only documented acquired-contract expedients.** ASC 805-20-30-29 permits an aggregate pre-acquisition-modification assessment for specified performance-obligation/price/allocation steps, and acquisition-date standalone selling prices for allocation. Elect per acquisition, apply consistently to all acquired contracts, and disclose the expedient and reasonably possible qualitative effect (-30-30; -50-5). [Official amendment](https://storage.fasb.org/ASU%202021-08.pdf).
4. **Separate measurement-period information from later events.** ASU 2015-16 amends ASC 805-10-25-13/-25-17: use acquisition-date facts, close the period when information is obtained or unobtainable, and never exceed 1 year from acquisition (-25-14, in words on the page). Recognise the provisional adjustment and goodwill effect in the period determined, with the cumulative depreciation/amortisation/income effect in current-period earnings as if acquisition accounting had been complete. Disclose the prior-period portion by line item. The old skill's label -25-17A and instruction to retrospectively restate issued comparatives are not supported by this amendment. [Official amendment](https://storage.fasb.org/ASU%202015-16.pdf).
5. **Future acquirer change.** ASU 2025-03 applies to annual reporting periods beginning after 15 December 2026 and interim periods within them; early adoption is permitted as of the beginning of the adopted interim/annual period, with prospective application. In the specified primarily-equity exchange acquiring a VIE business, use ASC 805-10-55-12 through -55-15 factors rather than automatically equating primary beneficiary with acquirer. Record adoption before selecting a version; do not apply the future rule automatically to every 2026 transaction. [Official amendment, ASC 805-10-65-5](https://storage.fasb.org/ASU%202025-03.pdf).
6. **Reviewer output.** Supply the acquired-contract rollforward, any expedient, the measurement-period evidence chronology, proposed balanced adjustment and outstanding authoritative-source requests. The complete general acquisition/goodwill/disclosure procedure, all original monetary cases and every exception are preserved below for source recovery.

### Verified corrections and remaining boundary

The original measurement-period description mixed retrospective adjustment with current-period recognition and cited -25-17A. The read ASU amends -25-17; current-period catch-up and related disclosure are the stated amendment basis. The original goodwill, NCI, step-interest, earn-out, cost, IPR&D, impairment and private-company/NFP rules cannot be declared fully current from these scoped sources. The new source-read exceptions inventory additionally identifies purchased credit-deteriorated assets; specialist current-ASC recovery remains required.

## Worked cases

All case values and rates are illustrative input facts. Classification/application gates are stated in each case; arithmetic does not verify those gates.

The first case uses illustrative supplied Topic 606 conclusions: a $30,000 prepaid 24-month stand-ready service, evenly delivered, with 12 months elapsed at acquisition, no modification, price change or financing issue. ASU 2021-08's origination-basis measurement gives a remaining contract liability of $15,000, recognised as the remaining service is delivered. An assumed $9,000 fair-value estimate is not substituted for that Topic 606 balance. The service/timing conclusions must be independently established under Topic 606; this case computes their consequences. [ASC 805-20-30-27/-30-28 amendment](https://storage.fasb.org/ASU%202021-08.pdf).

```oa-check
name: Acquired prepaid service, origination-basis contract liability
inputs:
  prepayment: 30000
  months: 24
  delivered: 12
  assumed_fv: 9000
steps:
  - monthly_revenue: prepayment / months
  - recognised_before_acquisition: monthly_revenue * delivered
  - remaining_liability: prepayment - recognised_before_acquisition
  - difference_from_fv: remaining_liability - assumed_fv
expected:
  monthly_revenue: 1250
  remaining_liability: 15000
  difference_from_fv: 6000
```

For a measurement-period adjustment, a $100,000 increase in equipment value is established 9 months after acquisition from acquisition-date evidence. Assume the value was provisional, the acquisition-date remaining life was 5 years, straight-line depreciation, no residual value or tax effect, and the first 6 months fall in an already-issued prior period. Record the $100,000 asset increase and goodwill decrease in the current period, plus cumulative extra depreciation of $15,000 (9/12 of $20,000), including $10,000 attributable to that prior period. Do not restate that prior issued period under the ASU 2015-16 basis. This is not a 9-month safe harbour: the period ends earlier once necessary information is obtained or unobtainable. [ASC 805-10-25-13 through -25-17 amendment](https://storage.fasb.org/ASU%202015-16.pdf).

```oa-check
name: Measurement-period asset adjustment and current-period catch-up
inputs:
  fair_value_increase: 100000
  life_years: 5
  elapsed_months: 9
  prior_period_months: 6
steps:
  - annual_extra_depreciation: fair_value_increase / life_years
  - cumulative_expense: annual_extra_depreciation * elapsed_months / 12
  - prior_period_portion: annual_extra_depreciation * prior_period_months / 12
  - net_asset_increase: fair_value_increase - cumulative_expense
expected:
  annual_extra_depreciation: 20000
  cumulative_expense: 15000
  prior_period_portion: 10000
  net_asset_increase: 85000
```


### Preserved original acquisition scenarios: conditional working papers

These retain the original facts and arithmetic; their booking depends on recovery of the specific current-source conditions listed below.

- **80% cash acquisition and NCI.** Acquirer buys 80% of Target. Assume the current applicable rules require fair-value NCI and the supplied acquisition-date values are correct: cash consideration $800,000, identifiable net assets $700,000, NCI fair value $190,000 and no prior interest. Goodwill is $800,000 + $190,000 - $700,000 = $290,000. Proposed entry: Dr identifiable net assets $700,000; Dr goodwill $290,000; Cr cash $800,000; Cr NCI $190,000. Debits and credits both equal $990,000. Supplied advisory and legal acquisition costs of $25,000 give a separate proposed Dr expense / Cr cash $25,000 only if the current expense rule applies and these are not debt/equity issue costs.
- **IFRS partial-NCI contrast.** For a separately eligible and elected IFRS proportionate-interest case, 20% × $700,000 gives NCI $140,000 and goodwill $240,000. The $50,000 difference from the fair-value-NCI case is the arithmetic difference between the supplied measurements; it is not automatically the IAS 36 notional NCI-goodwill gross-up. Run `ifrs3-business-combinations` for its actual conditions.
- **Acquisition in stages.** A prior 10% interest has carrying amount $60,000 and supplied acquisition-date fair value $95,000; the additional acquisition is 70% for cash, with no cash price supplied. The proposed entry is Dr investment in Target / Cr remeasurement gain in profit or loss $35,000; debits equal credits. That gain is $35,000 and $95,000 enters the goodwill formula, conditional on the current step-acquisition and OCI requirements. Do not invent a price for the additional interest or a resulting goodwill total.
- **Contingent consideration.** Given a separately established liability-classified earn-out initially valued at $120,000, its proposed acquisition entry is Dr goodwill / Cr contingent liability $120,000. A subsequent supplied value of $150,000 produces a $30,000 proposed fair-value loss and liability increase if the current subsequent-measurement rule applies. Distinguish later events from acquisition-date measurement-period evidence; continued-employment compensation and equity classification can change the answer.

## When to refuse or refer

Refuse a final current-US-GAAP accounting conclusion while authoritative ASC text or required contracts/adoption facts are unavailable. Do not treat a readable ASU as full current Codification access. Refer scope, complex own-equity/lease/acquisition classifications, valuation, enforceability, impairment, SEC presentation and tax effects to the appropriate specialist. Return the source gap and proposed arithmetic working paper, not a signed financial statement or assurance conclusion. Exclude asset acquisitions and common-control transactions under ASC 805-50, NFP combinations under ASC 958-805, consolidation/control procedures under ASC 810 and pushdown accounting beyond its scope reference. For dual reporters prepare a separate `ifrs3-business-combinations` assessment.

## Disclaimer

Provides computational and interpretive guidance on ASC 805 / ASC 350 only. Not an audit and not assurance. Business-combination accounting turns heavily on entity-specific facts and significant judgment  -  fair-value measurement of intangibles and contingent consideration, identification of the acquirer, the business-vs-asset determination, and goodwill impairment all require specialist input. Have outputs reviewed and signed by a qualified accountant before they are reflected in financial statements relied upon by third parties.

## Sources

| Source | Official URL | Actual read scope and date |
|---|---|---|
| ASU 2021-08 | [ASU 2021-08](https://storage.fasb.org/ASU%202021-08.pdf) | Read for ASC 805-20-25-16/-25-28C, -30-10 through -30-30, -50-5, -65-3 and adjacent exceptions; actual official PDF; 2026-11-15 |
| ASU 2015-16 | [ASU 2015-16](https://storage.fasb.org/ASU%202015-16.pdf) | Read for ASC 805-10-25-13 through -25-17 and measurement-period disclosure changes; actual official PDF; 2026-11-15 |
| ASU 2025-03 | [ASU 2025-03](https://storage.fasb.org/ASU%202025-03.pdf) | Read for summary, ASC 805-10-25-5, -55-12 through -55-15, -65-5 and adjacent VIE/pushdown changes; actual official PDF; 2026-11-15 |
| Current authoritative Codification | [ASC](https://asc.fasb.org/) | Attempted 2026-11-15; web root returned no readable lines; ordinary Brave visit reached /Login but rendered only a stalled loader. Not read; no current-authority claim. |


### Not yet confirmed: individual current-ASC source requests

Each item needs current authoritative text and entity/version facts before execution; the operative ASU checks above answer only their stated questions. The initial official Codification recovery failed, so the following are individually retained source requests, not cleared US-GAAP rules.

| Original topic retained | Exact question or condition to resolve |
|---|---|
| Business-combination scope and 4-step acquisition method | Whether control of a business is obtained; identify acquirer, acquisition date, recognised assets/liabilities/NCI and goodwill or bargain gain. Keep JV formation, asset acquisition, common control and NFP scope distinct. |
| Voting-interest and VIE control | Verify the original generally-more-than-50% voting indicator and the ASC 810 primary-beneficiary test rather than using either as an unconditional acquirer test. The future/early ASU 2025-03 equity-exchange exception is stated above. |
| Acquirer indicators | Cash/assets transferred or liabilities incurred; equity issuer versus reverse acquirer; relative votes, a large minority interest, governing body, senior management, relative size and exchange terms. Document private-company/public-shell and SPAC/de-SPAC facts without assuming every such deal is a business combination. |
| Reverse acquisition | Which entity is the accounting continuation, which net assets receive acquisition accounting and the correct statement presentation; legal parent/subsidiary labels do not settle it. |
| Acquisition date and post-acquisition results | Control date versus legal closing, written terms and facts supporting an earlier/later date; when results enter consolidation. |
| Recognition perimeter | Definitions of acquired assets/assumed liabilities, separately identified transactions and items not previously recognised by the acquiree. |
| Identifiable intangibles | Contractual/legal or separability tests; customer relationships, trade names, technology, order backlog and non-competes. Determine which are separately recognised and measure them under current applicable exceptions. |
| Fair-value valuation | Current ASC 820 basis, NCI fair value/full-goodwill scope and specialist valuation. Relief-from-royalty, MPEEM, growth, attrition, discount rates and WACC/IRR cross-checks are proposed valuation work, not universally prescribed models. |
| Income taxes | Correct exception is ASC 740, not a purported ASC 805-740; preserve the original deferred-tax-not-at-fair-value proposal, subject to current recognition/measurement, goodwill effects and tax-deductibility analysis. |
| Employee benefits | ASC 715/712 recognition and measurement exceptions, including the actual plan scope and acquisition-date obligations. |
| Indemnification assets | Matching basis to the indemnified item, contractual limitations and collectibility conditions. |
| Reacquired rights and settlement | The original proposal values the reacquired right over its remaining contractual term, ignoring renewals, with separate settlement of pre-existing relationships and later amortisation/disposal; recover current conditions before execution. |
| Replacement awards | ASC 718 allocation and requisite pre/post-service conditions: preserve the original proposal that the pre-combination-service portion enters consideration and the post-combination-service portion is compensation expense, subject to current scope and measurement proof. |
| Held-for-sale assets | ASC 360 classification and the original proposed fair-value-less-costs-to-sell measurement, individually unconfirmed until applicable current classification and measurement exceptions are recovered; do not substitute automatic fair value. |
| Contingent assets and liabilities | Fair value if determinable versus any applicable ASC 450 fallback and later accounting; recognition and measurement conditions must be read separately. |
| Acquired revenue contracts | Current Topic 606 underlying judgments remain separate from the actually read ASU 2021-08 origination-basis exception and expedients above. |
| Acquired leases | Preserve the original proposals to retain acquired lease classification unless modified and to measure the liability at the present value of remaining payments, with right-of-use asset and favourable/unfavourable terms treatment; actual current carryover, modification and measurement conditions remain unconfirmed. |
| Purchased credit-deteriorated assets and other exceptions | Recover the applicable financial-asset exception and all amendments relevant to the acquisition; do not assume the older ASU exception list establishes the complete 2026 perimeter. |
| Goodwill | Consideration plus measured NCI plus acquisition-date prior-interest value less recognised net assets; verify each component and exception before posting the conditional scenario. |
| Bargain purchase | The original proposal recognises a residual bargain-purchase gain in profit or loss at acquisition, attributed to the acquirer, only after reassessment of identification, measurement and circumstances; current recognition conditions, reporting line and disclosure remain unconfirmed. |
| Consideration transferred | Preserve the original proposed acquisition-date fair-value sum of assets transferred, liabilities incurred to former owners and equity issued, including contingent consideration; included versus separate transactions and current measurement conditions remain unconfirmed. |
| Earn-out classification and remeasurement | Liability/equity tests under ASC 480/815; preserve the original proposals of later liability fair-value changes through earnings versus no equity remeasurement and settlement within equity, subject to current proof. Retain continued-employment compensation analysis, acquisition-date versus later-event distinction, Monte Carlo/option valuation, revenue or EBITDA target inputs and recurring Level 3 ASC 820 disclosure research; none is cleared current execution guidance. |
| Acquisition costs | The original proposal expenses acquisition costs as incurred in the periods the services are received, with debt/equity issuance costs allocated against the relevant instrument instead. Advisory, legal, accounting, valuation, finder and general administrative categories, income-statement classification and the $25,000 scenario remain specific research inputs; recover applicable current conditions before posting. |
| Measurement period | The ASU 2015-16 current-period adjustment and maximum 1-year conditions above supersede the original retrospective-restatement instruction and erroneous -25-17A citation. Source remaining unaddressed current conditions separately. |
| Step acquisition | Acquisition-date remeasurement of prior interest, gain/loss and any OCI reclassification or transfer; retain 10%/70% and $60,000/$95,000/$35,000 facts above. |
| Business definition and concentration screen | ASU 2017-01 screen, gross-assets concentration, inputs and substantive-process conditions. Preserve the original proposals that concentration of substantially all fair value in a single identifiable asset or group of similar identifiable assets means the acquired set is not a business, and that an asset acquisition has no goodwill and capitalises transaction costs; each consequence needs its own current scope and measurement conditions. |
| Acquired IPR&D | Acquisition recognition/fair value, indefinite-life/non-amortisation assertion and impairment during development; preserve the original completion proposal to begin amortisation over useful life. Completion and abandonment recognition/measurement conditions remain individually unconfirmed; do not infer the IFRS answer or a universal zero value on abandonment. |
| Goodwill impairment | The original default goodwill-not-amortised assertion remains unconfirmed outside a supported eligible alternative. Reporting-unit allocation, annual test and trigger examples of share-price decline, loss of a major customer and adverse regulation; retain income-versus-market valuation and headroom/sensitivity work. The original optional qualitative proposal skips further testing if it is not more likely than not that fair value is below carrying value; the quantitative single-step proposal recognises carrying value over fair value, capped at allocated goodwill. These specific outcomes, ASU 2017-04 adoption and no-reversal conditions remain individually unconfirmed under current ASC. |
| Private-company/NFP goodwill alternative | Eligibility and policy choice; the original 10-year-or-shorter useful-life amortisation, straight-line method, trigger-only testing and entity/reporting-unit election require actual current scope and conditions. Preserve the proposed single-step excess of carrying value over fair value capped at goodwill, subject to that alternative's actual current conditions. |
| Private-company/NFP intangible alternative | Eligibility and ASU 2014-18 treatment of non-compete agreements and customer-related intangibles not independently saleable/licensable; do not absorb all customer intangibles indiscriminately or import the alternative into IFRS. |
| Disclosure: transaction identity | Acquiree name/description, date, voting percentage, reasons and how control was obtained. |
| Disclosure: consideration and contingencies | Total and each class, contingent amount/range/basis, subsequent movements and compensation distinction. |
| Disclosure: allocation and goodwill | Major asset/liability classes, goodwill factors and tax deductibility; bargain gain, line and reasons; NCI amount/basis/valuation inputs and prior-interest remeasurement gain and line. |
| Disclosure: costs and provisional amounts | Acquisition costs and income-statement line, incomplete items, measurement-period adjustments and prior-period earnings portions. The read 2015 amendment answers its specified catch-up disclosure only. |
| Disclosure: results and rollforward | Revenue and profit since acquisition, beginning-of-period pro forma results and any practicability qualifications; goodwill gross amount, accumulated impairment and losses in the rollforward by reportable segment; private-alternative amortisation period and policy. |

| Original comparison | Exact current source still required |
|---|---|
| IFRS comparison: impairment unit and measurement | Recover the original US operating-segment-or-1-level-below reporting-unit definition and current goodwill-capped fair-value test before comparing with the separately supported IAS 36 CGU/group, higher-of-recoverable-amount and goodwill-first allocation rules. |
| IFRS comparison: reversals and alternatives | Recover both the US no-goodwill-reversal and other-asset reversal restrictions, and the eligible private/NFP amortisation alternative; do not infer either from IAS 36, which bars goodwill reversal but permits qualified other-asset reversals. |
| IFRS comparison: acquisition rules | Compare actual NCI scope, business screen versus optional IFRS concentration test, contingent-consideration classification, expense versus issue-cost exception, acquired contract balances and current-period versus retrospective measurement-period adjustments under each edition. The readable US amendments answer their scoped topics only. |

### Retained execution and self-checks

The original 12-step work programme remains a completion contract: gate scope/business; identify acquirer/control and reverse-acquisition facts; fix control date; inventory assets, liabilities and exceptions; obtain valuation; determine consideration and separate compensation/costs; measure NCI; account for prior interests; compute goodwill/reassess a bargain; track provisional information and current-period catch-up; establish goodwill/IPR&D/private-alternative subsequent accounting; then reconcile disclosures and submit the reviewer brief. Refer each unresolved step to its individual source request above.

The retained 13 checks cover scope/business and exceptions; acquirer/reverse acquisition; acquisition date; recognition/intangibles; exception-by-exception measurement; consideration/earn-outs; NCI basis; prior-interest gain and OCI; goodwill/bargain recheck; costs and separate transactions; provisional-period chronology; IPR&D/goodwill impairment or eligible alternative; and complete disclosure/reconciled journals. They do not authorise an unsupported accounting conclusion.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-16. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `us-gaap-asc805-business-combinations` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/us-gaap-asc805-business-combinations. If neither is available, confirm every figure against the official source pages cited above before relying on it.
