---
name: banking-sector
description: "For 2026 banking and payment-sector work: reconcile instruments, IFRS expected credit losses, tax adjustments, bank levies, prudential capital and top-up tax. Includes a sourced UK Bank Levy case; country rates and specialised framework rules are held when not confirmed."
version: 1.0
jurisdiction: GLOBAL
tax_year: 2026
last_updated: 2026-11-14
depends_on:
  - corporate-income-tax-workflow-base
category: vertical
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: tax
type: cross-country-method
---

# Banking sector v1.0

## Scope and quick reference

For 2026 banks, neobanks, payment/e-money institutions and financial holding companies: build a bridge between financial reporting, country tax, levies, prudential capital and top-up tax. A banking licence, payment licence and bank tax classification are different tests. Load `corporate-income-tax-workflow-base`, the relevant country tax jobs and `statutory-audit-workflow-base` if an audit is requested.

This is not a regulatory capital calculator. Detailed Basel calibration, CRR/CRD/FRTB reporting, ICAAP/ILAAP, stress-testing models, MREL/TLAC, resolution plans, consumer protection, MiFID and operational AML compliance require their applicable specialist work. Country financial-services VAT and bank-audit programmes are separate jobs.

| First fork | Instruction | Authority |
| --- | --- | --- |
| Accounting framework | Do not substitute CECL for IFRS expected credit losses or assume all instruments start with the same allowance basis | [AASB 9, paragraphs 5.5.1-5.5.20](https://standards.aasb.gov.au/aasb-9-feb-2025) |
| Accounting impairment versus tax | Establish the local tax provision and exceptions; stage names alone do not determine deductibility | [HMRC CFM33220, Tax treatment](https://www.gov.uk/hmrc-internal-manuals/corporate-finance-manual/cfm33220) |
| Balance sheet levy versus profit surcharge | Keep their entities, bases, allowances and periods separate | [HMRC BKLM154500](https://www.gov.uk/hmrc-internal-manuals/bank-levy-manual/bklm154500), [BKM403100](https://www.gov.uk/hmrc-internal-manuals/banking-manual/bkm403100) |
| Deferred tax recapture | The cited UK top-up-tax recapture rule concerns a non-excluded deferred tax liability, not every deferred tax asset | [HMRC MTT27400; Finance (No.2) Act 2023 sections 182/184](https://www.gov.uk/hmrc-internal-manuals/multinational-top-up-tax-and-domestic-top-up-tax/mtt27400) |

## Ask the client first

- What are the licensed activities, legal entities, branches, tax residences and group perimeter?
- Which accounts framework and reporting dates apply, and which instrument portfolios, ECL approaches and elections are used?
- What do the account balances, maturity split, impairment movements, recoveries and connected-party exposures contain?
- Which countries levy bank, resolution, deposit-guarantee, transaction or profit charges, and which allowances are allocated within the group?
- What supports current and deferred tax recognition, expected reversals and prudential treatment?
- Is the group within the applicable top-up-tax regime, and which legal elections, exclusions and transition rules have actually been established?

## The method, step by step

1. Establish each entity's accounting, licensing, tax and prudential status and period. Keep a separate country workpaper for each charge and a dated source for any current figure.
2. Reconcile instruments to the general ledger. Identify amortised-cost, fair-value-through-other-comprehensive-income and fair-value-through-profit-or-loss measurement under the applicable standard, separately from trading-book or banking-book regulatory classification.
3. Build an impairment movement schedule: opening allowance, originations, repayments, credit-risk changes, modifications, write-offs, recoveries, foreign exchange and closing allowance. Record the selected general, simplified or purchased/originated-credit-impaired approach and its support.
4. Bridge accounting profit to the taxable base instrument by instrument. Identify statutory departures, connected debt, interest limits, foreign exchange, hedges, securitisations and fees. An accounting provision neither guarantees a deduction nor proves a disallowance.
5. Compute levies on their own bases after group allocations and exclusions. Resolution-fund or deposit-guarantee contributions are not interchangeable with a national bank levy. Document the return, payment route and local deadlines from the country source rather than inferring a corporation-tax deadline.
6. Reconcile current/deferred tax to tax accounts, future profit evidence and the prudential capital return. Apply the actual local capital rules; do not insert a generic Basel deduction percentage.
7. Separately perform top-up-tax entity scope, covered-tax, timing, transition and deferred-tax checks. Nominal corporation-tax rates, bank levies and accounting ETRs are not interchangeable inputs.

Accounting steps use [AASB 9, chapters 3-5 and section 5.5](https://standards.aasb.gov.au/aasb-9-feb-2025); country bridges below define which tax points are confirmed. The Australian text incorporates IFRS 9, including its 2026 compilation. Another framework or national adoption must be assessed separately.

## Expected credit losses: use the right approach

| Portfolio or event | Treatment to establish | Source |
| --- | --- | --- |
| General approach, no significant credit-risk increase | Measure the applicable allowance on a 12-month expected-credit-loss basis; do not read that as only defaults expected to result in loss during that period | [AASB 9, paragraphs 5.5.5 and B5.5.43](https://standards.aasb.gov.au/aasb-9-feb-2025) |
| Significant credit-risk increase since origination | Lifetime expected losses apply under the general approach. Consider forward-looking information and the change in lifetime default risk | [AASB 9, paragraphs 5.5.3-5.5.11](https://standards.aasb.gov.au/aasb-9-feb-2025) |
| Past due indicator | More than 30 days past due creates a rebuttable significant-increase presumption; it does not delay earlier recognition supported by information | [AASB 9, paragraph 5.5.11](https://standards.aasb.gov.au/aasb-9-feb-2025) |
| Purchased or originated credit-impaired assets | Recognise cumulative changes in lifetime expected losses since initial recognition under this separate approach | [AASB 9, paragraphs 5.5.13-5.5.14](https://standards.aasb.gov.au/aasb-9-feb-2025) |
| Trade receivables/contract assets without significant financing | Lifetime loss allowance is mandatory under the simplified approach, including the specified practical-expedient cases | [AASB 9, paragraph 5.5.15(a)(i)](https://standards.aasb.gov.au/aasb-9-feb-2025) |
| Specified financed trade receivables/contract assets and lease receivables | Assess and document the permitted lifetime-loss accounting-policy election and consistent portfolio application | [AASB 9, paragraphs 5.5.15-5.5.16](https://standards.aasb.gov.au/aasb-9-feb-2025) |
| Measurement | Use an unbiased probability-weighted outcome, time value and reasonable/supportable past, current and forward-looking information | [AASB 9, paragraph 5.5.17](https://standards.aasb.gov.au/aasb-9-feb-2025) |

Credit-impaired interest recognition, collateral recoveries, model validation, modification/derecognition and write-off policies require the relevant paragraphs and instrument evidence, not just a staging label. Maintain the US ASC 326/CECL comparison as a separate framework question; this guide does not assert that US purchased-credit-deteriorated accounting has been conformed to IFRS POCI. That old equivalence is not usable.

**Conflicting official summary:** HMRC CFM33220's accounting overview refers to falling below investment grade when discussing lifetime ECL. AASB 9 paragraph 5.5.3 makes significant increase the general-approach condition without that extra blanket requirement, and paragraphs 5.5.13-5.5.16 supply exceptions. Use the accounting standard for the accounting conclusion; use CFM33220's tax-treatment section for the UK tax bridge. Do not combine the summary into a new accounting restriction.

## United Kingdom

### Bank Levy

For chargeable periods in 2026, the published rates below apply after establishing the actual Finance Act 2011 Schedule 19 scope, exclusions and chargeable balance sheet. They are not a charge on every liability of every licensed payment business.

| Item | Value and condition | Source |
| --- | --- | --- |
| Chargeable equity and long-term liabilities | 0.05%, for the rate period beginning January 2021 onwards | [HMRC BKLM160000, current rate row](https://www.gov.uk/hmrc-internal-manuals/bank-levy-manual/bklm160000) |
| Short-term chargeable liabilities | 0.10%, for the same rate period | [HMRC BKLM160000](https://www.gov.uk/hmrc-internal-manuals/bank-levy-manual/bklm160000) |
| Allowance | GBP 20 billion, allocated proportionately across the two chargeable balance categories, not a separate full allowance for each category | [HMRC BKLM154500, Schedule 19 paragraph 6(2)](https://www.gov.uk/hmrc-internal-manuals/bank-levy-manual/bklm154500) |

Map covered deposits, non-chargeable equity, territorial/group perimeter, netting, long-term status, any averaging and period apportionment before using those values. This is a method and illustrated rate application, not the full statutory balance-sheet computation or filing instruction.

### Banking surcharge and impairment

Do not obtain surcharge profits merely by multiplying accounting profit by a combined headline rate. HMRC [BKM403100, CTA 2010 section 269DA](https://www.gov.uk/hmrc-internal-manuals/banking-manual/bkm403100) starts with taxable total profits and adjusts for non-banking/pre-period relief and specified transferred gains and credits. The surcharge rate, allowance allocation, period split and any newly announced future change must come from enacted law for the relevant period. The previous combined-rate shortcut and general "nine months plus one day" levy filing instruction are held below.

For creditor loan relationships, HMRC [CFM33220, Tax treatment](https://www.gov.uk/hmrc-internal-manuals/corporate-finance-manual/cfm33220) explains that a correctly recognised impairment debit follows the normal tax computation under either an incurred-loss or expected-loss model, with connected-company debt a main exception. Do not disallow all IFRS Stage 1/2 losses solely because they are expected losses. Identify other statutory exclusions, the actual tax relationship and any transition adjustment before completing the return.

## European Union and other country workpapers

The Single Resolution Fund and national deposit-guarantee schemes require separate current contribution notices, membership, perimeter and national implementation checks. A historic target percentage or target date does not establish the amount due from this bank this year. Retain Germany, France, Italy, Spain, Hungary, Sweden, the Netherlands and Poland as individual levy/profit-tax questions. The old rate matrix, its bases, temporary charge periods and claimed Swedish percentage have not been validated and must not be used as 2026 figures.

For Germany, France and Italy, keep loan-loss tax timing and historic transition schedules distinct from regulatory provisioning. For Australia, Canada and India, obtain their own bad-debt/reserve rules, permitted elections and current prudential interaction. For US entities, retain BEAT, interest-limitation, bad-debt/reserve and CECL tax questions with the existing country jobs; no US thresholds are supplied here. In particular, do not assume bank BEAT rules use a lower gross-receipts threshold simply from the entity being a bank.

## Fees, trading, hedges and securitisations

- **Effective interest and origination fees:** reconcile which fees are integral to the instrument's effective interest rate and which pay for separate services; do not defer all fees under a single bank label. Apply the applicable financial-instrument or revenue standard and separately bridge tax timing.
- **Trading versus banking book:** prudential location does not by itself decide IFRS fair-value measurement or tax mark-to-market. Preserve both classifications and explain differences.
- **Hedging and treasury:** document the hedged item, designation, effectiveness, accounting reserve and current tax rule for the cash flow, fair value or net investment relationship. A movement in OCI does not guarantee an identical tax deferral.
- **Securitisations:** assess consolidation, asset transfer/derecognition, risks/rewards, continuing involvement and tax true-sale/SPV treatment separately. Retaining substantially all risks/rewards prevents accounting derecognition even if legal title passes. [AASB 9, paragraphs 3.2.6-3.2.23](https://standards.aasb.gov.au/aasb-9-feb-2025).
- **Interchange, merchant acquiring and payment services:** separate the actual services, contractual role and recipient. Financial-services VAT relief is not a blanket exemption for everything a bank or processor supplies. Load the country VAT job for classification and recovery.
- **CVA, foreign exchange and financial transaction taxes:** preserve instrument, counterparty, valuation and jurisdiction evidence; do not treat a prudential value adjustment or levy name as proof of an income-tax deduction.

The fee/hedge/CVA and VAT items are classification workpapers. Detailed application and tax results remain held where the relevant instrument paragraph or country source is missing; they are not automatic posting rules.

## Deferred tax, capital and top-up tax

Maintain separate schedules for recognised tax assets/liabilities, regulatory deductions/filters, recoverability and top-up-tax adjustments. A financial-reporting deferred tax asset can be recognised yet receive different prudential treatment. Never use an unverified capital threshold or assume a temporary filter remains effective.

For the UK top-up-tax bridge, [MTT27400](https://www.gov.uk/hmrc-internal-manuals/multinational-top-up-tax-and-domestic-top-up-tax/mtt27400), applying Finance (No.2) Act 2023 sections 182(6)/184, describes recapture of a non-excluded deferred tax liability not reversed by the end of the fifth following accounting period. Recalculate the initial period as required. Excluded-liability categories must be tested before recapture; a bank tax asset is not recaptured by that rule merely because it remains unused. Other countries' enacted implementations, covered-tax classifications, deferred-tax rate adjustments and elections require their own workpapers.

## Worked case: allocate the levy allowance once

Fabricated UK example for a full unchanged rate period. Assume the statutory balance-sheet work has already established GBP 60 billion long-term/equity and GBP 40 billion short-term chargeable balances, before the allowance, with no further adjustment. The allowance is split in the same proportions. Long-term/equity chargeable after allocation is GBP 48 billion and short-term GBP 32 billion. Their levy amounts are GBP 24 million and GBP 32 million, total GBP 56 million. This is not a computation from a raw bank balance sheet.

```oa-check
name: UK Bank Levy allowance allocation
inputs:
  long_balance: 60000000000
  short_balance: 40000000000
  allowance: 20000000000
  long_rate: 0.0005
  short_rate: 0.001
steps:
  total: long_balance + short_balance
  long_net: long_balance - allowance * long_balance / total
  short_net: short_balance - allowance * short_balance / total
  levy_long: long_net * long_rate
  levy_short: short_net * short_rate
  levy: levy_long + levy_short
expected:
  long_net: 48000000000
  short_net: 32000000000
  levy_long: 24000000
  levy_short: 32000000
  levy: 56000000
```

## When to refuse or refer

- Missing instrument data, unsupported ECL staging/model inputs, unresolved securitisation control or an unconfirmed accounting framework: do not finalise the accounts/tax bridge.
- Missing national levy base, temporary-tax commencement, connected-debt exception or prudential filter: leave a named open item, not a global fallback.
- Regulatory returns, stress models, complex hedges, bank restructurings, capital recognition and top-up-tax elections: obtain the applicable specialist conclusion before sign-off.

## Completion checklist

- Instrument and ECL schedules reconcile; general/simplified/POCI distinctions are explicit.
- Every accounting-to-tax adjustment has a current country rule and correct relationship/perimeter.
- Levy, deposit-guarantee and resolution contributions are kept separate and reconcile to notices.
- Fees, interest, treasury, CVA, transaction taxes and securitisations have their own classification records.
- Current/deferred tax, recoverability, capital and top-up-tax schedules reconcile without treating one as the other.
- Every held item remains outside the final computation.

## Sources

| Source | URL | Read on | Read for |
| --- | --- | --- | --- |
| AASB 9, February 2025 compilation, operative 2026 | https://standards.aasb.gov.au/aasb-9-feb-2025 | 2026-11-14 | Read for Sections on derecognition and expected credit losses, paragraphs 3.2.6-3.2.23, 5.5.1-5.5.20 and B5.5.43; exceptions, twelve-month-loss meaning and forward-looking information |
| HMRC BKLM160000 | https://www.gov.uk/hmrc-internal-manuals/bank-levy-manual/bklm160000 | 2026-11-14 | Read for Current rate row and separate long/short-term categories |
| HMRC BKLM154500 | https://www.gov.uk/hmrc-internal-manuals/bank-levy-manual/bklm154500 | 2026-11-14 | Read for Schedule 19 paragraph 6(2), allowance and proportional allocation |
| HMRC BKM403100 | https://www.gov.uk/hmrc-internal-manuals/banking-manual/bkm403100 | 2026-11-14 | Read for Surcharge profit bridge under CTA 2010 section 269DA, not a rate confirmation |
| HMRC CFM33220 | https://www.gov.uk/hmrc-internal-manuals/corporate-finance-manual/cfm33220 | 2026-11-14 | Read for Tax treatment of creditor loan relationships and connected-party exception; accounting overview compared with actual standard |
| HMRC MTT27400 | https://www.gov.uk/hmrc-internal-manuals/multinational-top-up-tax-and-domestic-top-up-tax/mtt27400 | 2026-11-14 | Read for Recapture of deferred tax liabilities, excluded categories and initial-period recalculation |

Not yet confirmed: complete UK Bank Levy scope/exclusions, return and payment deadlines; banking-surcharge current/future rate and allocated allowance; SRF/DGS current contributions; German, French, Italian, Spanish, Hungarian, Swedish, Dutch and Polish bank charge rates/bases/temporary periods; Germany/France/Italy/Australia/Canada/India loan-loss tax rules; US BEAT/interest/bad-debt/CECL details; ASC 326 and purchased-credit-deteriorated comparison; current CRR/Basel/PRA prudential percentages and filters; detailed EIR/fee, hedge, CVA and financial transaction tax application; country interchange VAT exemption/recovery; non-UK top-up-tax/deferred-tax implementation. These are preserved questions, not usable rates or automatic adjustments.
