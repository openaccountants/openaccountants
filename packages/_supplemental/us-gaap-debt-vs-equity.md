---
name: us-gaap-debt-vs-equity
description: "Issuer financial-instrument working papers using official ASU 2020-06 and ASU 2024-04 amendment-basis checks, with original ASC 480, own-equity, mezzanine and treasury-stock topics individually retained pending current authoritative Codification access. Load financial-reporting-workflow-base."
version: 0.3
jurisdiction: US
last_updated: 2026-11-16
depends_on:
  - financial-reporting-workflow-base
category: financial-statements
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: financial-reporting
type: computation
standard: "ASC 470-20 and ASC 815-40 (ASU 2024-04 and ASU 2020-06 amendment basis)"
effective_date: 2025-12-16
source_checked: 2026-11-16
---

# US GAAP debt versus equity v0.3

**General reference only.** Working papers and reviewer brief only; not an audit or assurance opinion. Tier 2; not approved by an accountant.

## Scope

**Standard and effective-date basis:** ASC 470-20 and ASC 815-40 (ASU 2024-04 and ASU 2020-06 amendment basis); effective-date key **2025-12-16**. It identifies the first possible annual-period start after 15 December 2025 for ASU 2024-04, including interim periods therein. Earlier adoption requires adoption of ASU 2020-06; use the specified prospective or retrospective transition. ASU 2020-06 applies to SEC-filer PBEs other than entities eligible to be smaller reporting companies, determined from the most recent determination as of 5 August 2020, for fiscal years beginning after 15 December 2021, and to all others after 15 December 2023, including interim periods therein; the general early-adoption rule cannot precede fiscal years beginning after 15 December 2020 and is at the annual-year beginning. A narrow exception permits entities that have not adopted ASU 2017-11 to early adopt the convertible-instrument down-round amendments for fiscal years beginning after 15 December 2019; apply the specific transition conditions, not a general earlier adoption of all amendments. Establish actual adoption and transition before use. [ASU 2024-04 transition summary](https://storage.fasb.org/ASU%202024-04.pdf); [ASU 2020-06 transition summary](https://storage.fasb.org/ASU%202020-06.pdf).

Load `financial-reporting-workflow-base`. This issuer/transaction worksheet retains the complete original topic coverage, but separates the actually read amendment-basis computations from unrecovered current authoritative guidance. It does not cover the holder's accounting, control or valuation methodologies beyond the explicit steps.

**Source boundary for 2026 work.** This is a source-bounded research and computation worksheet. Current authoritative ASC text was attempted through the official site and an ordinary browser on 15 November 2026 but did not render. The FASB amendments below were opened and their stated operative paragraphs read. Each Update expressly distinguishes itself from the authoritative Codification; reading an ASU does not establish that every intervening amendment is incorporated. Consequently, the method explains only the stated amendment-basis checks. Do not use it to sign a current-ASC conclusion until the authoritative, entity-applicable text is recovered. The official ASC web attempt on 16 November 2026 likewise returned no operative text. Broader unresolved rules are individually reserved under Sources.

## Ask the client first

- Reporting framework, reporting-period start, SEC/PBE status, the most recent smaller-reporting-company determination as of 5 August 2020 for the ASU 2020-06 transition bucket, and actual adoption dates.
- All instrument/side-agreement terms, freestanding versus embedded assessment, settlement currency/options and redemption/dividend obligations.
- Proceeds, coupon, maturity, conversion ratios, premiums, transaction costs and fair-value option/embedded-derivative conclusions.
- Authorised shares and competing commitments, cash-settlement, registration, make-whole and counterparty rights.
- For induced conversion: original/current terms, limited offer period, acceptance date, prior-year modifications, share fair value and substantive-conversion-feature evidence.

## The method, step by step

1. **Establish the source and scope gate.** Obtain current authoritative ASC 480/815-15/815-40/470-20/505 conclusions for every feature, including freestanding versus embedded, fair-value option, settlement and SEC temporary-equity scope. Do not classify a whole instrument from its legal name. The complete original sequence and all 3 ASC 480 classes remain individually reserved below pending the actual current text.
2. **ASU 2020-06 conversion-debt basis.** Under amended ASC 470-20-25-1/-25-12, consider the fair-value option and embedded-derivative guidance first. A debt with an embedded conversion feature is otherwise a single liability; separation persists for a bifurcated embedded derivative and the substantial-premium presumption in -25-13. Other stated/unstated rights may require allocation under -25-15. Consequently the old $1,000,000 bond calculation below assumes no such separate component or designation, no issue costs and issue at par. [Official amendment](https://storage.fasb.org/ASU%202020-06.pdf).
3. **Correct the old own-equity Gate 2 list.** ASU 2020-06 removes the unregistered-share, higher-counterparty-right and collateral conditions. Amended ASC 815-40-25-10/-25-10A retains sufficient authorised/unissued shares after other commitments, an explicit share limit, no required net cash settlement for untimely SEC filings, and no cash-settled top-off/make-whole provisions. A mere cash penalty is not automatically net cash settlement. A requirement for registered shares alone does not disqualify, but an explicit cash fallback if they are unavailable can. The full indexation analysis and other settlement exceptions must still be sourced; this is not a complete equity-classification checklist. [Official amendment](https://storage.fasb.org/ASU%202020-06.pdf).
4. **ASU 2024-04 induced-conversion basis for applicable 2026 periods.** Effective for all entities for annual periods beginning after 15 December 2025 and interim periods therein, with prospective or retrospective transition as specified. Under amended ASC 470-20-40-13/-40-13A, require a limited offer period, preservation of conversion consideration in form and amount, and a substantive conversion feature at issuance and offer acceptance even if not currently convertible. Assess at acceptance; for relevant non-substantial exchanges/modifications in the preceding 1 year, compare the terms 1 year before acceptance. Use acceptance-date share fair value for future-price/VWAP comparisons. Changes to non-share-price indexation can change the form of settlement. Expense the excess fair value of the inducement consideration under -40-16. [Official amendment](https://storage.fasb.org/ASU%202024-04.pdf).
5. **Prepare the reviewer brief.** Show the scope/version decisions and each surviving source request. Do not use the old broad foreign-currency-strike statement as an unconditional exemption: its precise indexation exceptions remain unrecovered. Preserve the ASC 480 classes, mezzanine accretion, treasury shares, down-round and cross-framework questions as distinct open items rather than inferring their answers from the specifically read Updates.

### Verified corrections and remaining boundary

The old blanket PBE effective-date statement was too broad: ASU 2020-06 uses fiscal years beginning after 15 December 2021 for SEC-filer PBEs excluding eligible smaller reporting companies, and after 15 December 2023 for all others (transition summary). The original Gate 2 wrongly retained conditions removed by ASU 2020-06 and overstated a cash-penalty ban. The original currency-strike exemption is not blanket verified guidance. Its exact scope, all ASC 480 deferrals, temporary-equity measurement, treasury stock, down-round treatment, issue costs and IFRS comparison remain individually reserved. The complete original monetary example is retained and independently recomputed; a normal book-value maturity conversion and an induced conversion are separate cases.


### Later issued amendments: adoption gates

**PIK preferred dividends, ASU 2026-01.** The read amendment to ASC 505-10 covers PIK dividends on equity-classified preferred stock, including temporary equity: additional preferred stock with the same terms, or an increase in the preferred stock's value under the agreement, such as its liquidation value. The measurement rule applies where monetary value varies with the additional shares or liquidation-value increase. The Subtopic separately excludes convertible preferred awards within Topic 718 unless modified so they are no longer subject to that Topic; recover award and embedded-feature classification first. It excludes fixed monetary dividends settled with a variable number of preferred shares and deemed dividends such as certain redemptions. Measure an in-scope PIK dividend using the stated contractual PIK dividend rate; the Update does not determine when recognition occurs. It applies to annual periods beginning after 15 December 2026 and interim periods within them. Early adoption is allowed for financial statements not issued or available for issuance; interim adoption applies from the annual-period beginning. Choose prospective application to PIK dividends recognised on or after initial application, or modified retrospective application to preferred shares outstanding then, with the specified comparative recasting and opening-equity adjustment. Apply the corresponding transition disclosures. This future or early-adopted amendment does not resolve liability/equity classification. [ASU 2026-01, 505-10-15-1 to -15-4, -30-1 and -65-1](https://storage.fasb.org/ASU%202026-01.pdf).

**Retirement of treasury shares, ASU 2025-12.** The read amendment to ASC 505-30-30-8 adds an option to charge the excess of repurchase price over par or stated value entirely to additional paid-in capital, provided that account does not become negative. The paragraph also retains allocation between additional paid-in capital and retained earnings subject to its same-issue limitation, or charging entirely to retained earnings. This is a retirement/constructive-retirement paragraph; it does not establish every reacquisition or reissuance rule. The Update also removes an obsolete pooling-of-interests reference from ASC 815-40-55-5. These amendments apply to annual periods beginning after 15 December 2026 and interim periods within them. Early adoption is permitted for unissued/not-available financial statements, at the annual-period beginning if adopted in an interim period. Prospective or retrospective transition and the associated disclosures apply; the treasury-share and own-equity amendments can have separate early-adoption and transition elections. [ASU 2025-12, 505-30-30-8, 815-40-55-5 and 105-10-65-10](https://storage.fasb.org/ASU%202025-12.pdf).

## Worked cases

All case values and rates are illustrative input facts. Classification/application gates are stated in each case; arithmetic does not verify those gates.

On 1 January 20X1, the preserved convertible bond facts are $1,000,000 proceeds and par, 3 years, 5% annual coupons and conversion into a fixed number of the issuer's own shares. A comparable non-convertible yield of 8% is not used to split a conversion option under the stated single-liability basis; assume no bifurcated derivative, substantial premium, other right, cost or fair-value designation. Record Dr cash/Cr debt $1,000,000; at each year end in 20X1, 20X2 and 20X3, Dr interest/Cr cash $50,000. A normal conversion at par is not an inducement. At maturity on 31 December 20X3, the original journal is retained as a conditional working-paper proposal: Dr debt $1,000,000 / Cr common stock and additional paid-in capital $1,000,000, with no gain or loss, only if the separately sourced current ordinary-conversion rule permits that book-value treatment. It is not a cleared current-ASC instruction. For the separate IAS 32 compound-instrument case, assume all IAS 32 liability/equity conditions hold: discounting the same coupons and principal at 8% gives liability $922,687 and residual equity $77,313; successive effective interest rounds to $73,815, $75,720 and $77,778, against the US case's $50,000 each year. This comparison does not imply that IAS 32 splits every convertible instrument. See `ias32-debt-vs-equity` for the actual classification conditions.

```oa-check
name: Preserved par convertible bond under the stated single-liability basis
inputs:
  proceeds: 1000000
  principal: 1000000
  coupon_rate: 0.05
  years: 3
steps:
  - initial_liability: proceeds
  - annual_coupon: principal * coupon_rate
  - annual_interest: initial_liability * coupon_rate
  - total_coupon: annual_coupon * years
  - liability_after_coupon: initial_liability + annual_interest - annual_coupon
expected:
  initial_liability: 1000000
  annual_coupon: 50000
  annual_interest: 50000
  total_coupon: 150000
  liability_after_coupon: 1000000
```

An induced-conversion edge case assumes all amended conditions above hold, no prior-year modification and no embedded derivative: original terms deliver 50,000 shares, the limited accepted offer delivers 55,000 of the same shares, and acceptance-date fair value is $20 each. Original consideration is $1,000,000; offer consideration is $1,100,000; the excess expense is $100,000. If instead the offered form or amount fails preservation, this expense shortcut does not decide the accounting; apply the current extinguishment guidance after source recovery.

```oa-check
name: Limited inducement preserving original share consideration
inputs:
  original_shares: 50000
  offered_shares: 55000
  share_fair_value: 20
steps:
  - original_value: original_shares * share_fair_value
  - offered_value: offered_shares * share_fair_value
  - extra_expense: offered_value - original_value
expected:
  original_value: 1000000
  offered_value: 1100000
  extra_expense: 100000
```

## When to refuse or refer

Refuse a final current-US-GAAP accounting conclusion while authoritative ASC text or required contracts/adoption facts are unavailable. Do not treat a readable ASU as full current Codification access. Refer scope, complex own-equity/lease/acquisition classifications, valuation, enforceability, impairment, SEC presentation and tax effects to the appropriate specialist. Return the source gap and proposed arithmetic working paper, not a signed financial statement or assurance conclusion. Exclude holder accounting, EPS computation under ASC 260, share-based payment under ASC 718 and embedded-derivative valuation methodology. For dual reporters prepare both framework answers using `ias32-debt-vs-equity`; do not substitute a US conclusion for the IFRS assessment.

## Disclaimer

Provides computational and interpretive guidance on ASC 480 / 470-20 / 815-40 / 505 only. Not an audit and not assurance. Classifying instruments as liabilities, equity, or temporary equity turns heavily on the specific contractual terms, registrant status, and significant judgement. Have outputs reviewed and signed by a qualified accountant before they are reflected in financial statements relied upon by third parties.

## Sources

| Source | Official URL | Actual read scope and date |
|---|---|---|
| ASU 2020-06 | [ASU 2020-06](https://storage.fasb.org/ASU%202020-06.pdf) | Read for summary, ASC 470-20-25-1/-25-12 through -25-15, ASC 815-40-25-1 through -25-10A, related conventional-hybrid exceptions and transition summary; actual official PDF; 2026-11-15 |
| ASU 2024-04 | [ASU 2024-04](https://storage.fasb.org/ASU%202024-04.pdf) | Read for scope/effective-date summary, ASC 470-20-40-13 through -40-17 and neighbouring substantive-feature guidance; actual official PDF; 2026-11-15 |
| Current authoritative Codification | [ASC](https://asc.fasb.org/) | Attempted 2026-11-15; web root returned no readable lines; ordinary Brave visit reached /Login but rendered only a stalled loader. Not read; no current-authority claim. |


| ASU 2026-01 | [Official PDF](https://storage.fasb.org/ASU%202026-01.pdf) | Summary and operative ASC 505-10-15-1 through -15-4, -30-1 and -65-1 with neighbouring scope and transition; read 2026-11-16. |
| ASU 2025-12 | [Official PDF](https://storage.fasb.org/ASU%202025-12.pdf) | ASC 505-30-30-8, ASC 815-40-55-5 and ASC 105-10-65-10 with neighbouring amendments and transition elections; read 2026-11-16. |

### Not yet confirmed: individual current-ASC source requests

Each row preserves a specific original question or condition. The official current Codification did not yield operative text; these are source requests, not accounting instructions. The read ASU corrections and the later-amendment gates above control their stated topics.

| Original topic retained | Current source still required before execution |
|---|---|
| Scope and analysis order | Distinguish freestanding instruments from embedded features; apply ASC 480 and the relevant own-equity/convertible-debt guidance before the SEC temporary-equity presentation screen. Obtain the precise current ordering and scope; do not run mezzanine presentation before deciding liability/equity. |
| ASC 480 class 1 | Unconditional asset-transfer redemption at a specified/determinable date or event certain to occur, including legally preferred equity; verify liquidation-only and non-SEC deferrals before treating mandatory redemption as a liability. |
| ASC 480 class 2 | Obligations to repurchase own shares, or indexed obligations, that may require asset transfer, including written puts and forwards; preserve the liquidation/termination qualification. |
| ASC 480 class 3 | Unconditional obligations, or non-outstanding-share instruments potentially settled in variable shares, whose inception monetary value is predominantly fixed, linked to a non-share variable, or inversely linked to own-share price. Verify all 3 alternatives and the outstanding-share distinction. |
| Embedded derivative separation | Current ASC 815-15 standalone-derivative, clearly-and-closely-related and own-equity-exception conditions, host measurement, initial fair value and subsequent earnings effects. The ASU single-liability default does not clear these separate gates. |
| Own-equity indexation | For warrants, written options, forwards and other own-equity contracts, both exercise-contingency and settlement tests, including permitted own-operations/stock contingencies and fixed-share/fixed-amount inputs; the precise foreign-currency-strike exception in ASC 815-40-15-7I is not a blanket exemption. |
| Settlement consequences and share sequencing | Current exceptions and whether a failed gate produces an asset/liability or derivative with fair-value changes in earnings; allocation of available authorised shares among competing contracts. The actual ASU 2020-06 removals and retained conditions are stated above, not the superseded unregistered-share/collateral/bankruptcy-ranking list. |
| SEC temporary equity | Equity-classified redeemable preferred or NCI redeemable on a fixed/determinable date/price, at holder option or on an event outside issuer control; registrant scope, separate mezzanine caption and the exact accretion eligibility, earliest-redemption timing and immediate-versus-over-time methods. |
| Own-equity presentation | Permanent-equity/additional-paid-in-capital presentation for qualifying warrants or separated substantial-premium rights; no classification from labels alone. |
| Treasury stock beyond the read retirement amendment | Cost versus par-value methods, equity deduction, reacquisition/reissuance differences and the no-earnings assertion; obtain current ASC 505-30 and entity adoption before posting. The later retirement option is not a universal treasury-stock method. |
| Distributions | Interest/expense treatment for liability-classified preferred versus retained-earnings distributions for equity; precise recognition and presentation, including when a declared dividend becomes payable. The PIK measurement amendment does not answer recognition timing. |
| Down-round features | ASU 2017-11 instrument scope, indexation consequences, trigger measurement, deemed-dividend treatment and EPS interaction; do not apply a deemed dividend to every triggered feature. |
| Issue costs | Allocation where debt, an embedded derivative, a premium-related equity amount or another right is recognised; amortised-cost/effective-interest treatment. Do not allocate all costs to debt regardless of surviving components. |
| Ordinary conversion, repurchase and extinguishment | Current ASC 470-20-40 ordinary book-value conversion conditions and journals, repurchase/extinguishment rules and interaction with bifurcated derivatives. The original maturity journal above is conditional; the separately read induced-conversion route is not universal. |
| IFRS comparison: convertible debt | Retain the 3-year $1,000,000 / 5% / 8% conditional calculation above; IAS 32 liability/equity classification is required before any split. Obtain current ASC classification for an actual instrument. |
| IFRS comparison: redeemable and puttable instruments | Compare the actual ASC 480/SEC scope with IAS 32 mandatory-redemption, puttable and liquidation exceptions; do not infer a universal US no-exception rule or a universal IFRS liability from mezzanine presentation. |
| IFRS comparison: own-equity and distributions | Compare the precise ASC indexation/foreign-currency exceptions and IAS 32 fixed-for-fixed conditions, and liability-preferred interest versus equity distributions. Do not claim identical EPS or presentation mechanics. |
| ASC 480 disclosures | Nature, terms, redemption requirements, settlement alternatives and potential shares; mandatorily redeemable settlement amount and share number as if settled at reporting date. Verify scope and exact required amounts. |
| Convertible-debt disclosures | Principal, coupon, conversion terms/price, shares deliverable and any if-converted EPS disclosure; EPS computation remains outside this Guide. |
| Own-equity disclosures | Instrument terms, equity/liability classification and liability-contract fair-value/remeasurement information. |
| Mezzanine disclosures | Separate caption, redemption terms, accretion method and amounts. |
| Treasury and down-round disclosures | Shares held, cost/par method, trigger/deemed-dividend information and any EPS effect, subject to precise instrument scope. |
| Defaults and covenants | Current reporting requirements for liability-instrument defaults and breaches. |

### Retained execution and reviewer checks

For each instrument: (1) settle freestanding/embedded scope with an actual paragraph; (2) document each relevant ASC 480 class and exception; (3) for convertible debt record the single-liability or separately supported component conclusion; (4) test both own-equity gates, foreign-currency terms, available shares and settlement exceptions; (5) screen eligible SEC equity for temporary presentation and source its accretion; (6) prepare initial and subsequent journals, effective interest, any derivative fair-value movements and any mezzanine movements; (7) source the distribution/down-round conclusion; (8) assemble every applicable disclosure above and the reviewer brief. These are completion checks: unresolved source rows prevent the corresponding booking or presentation conclusion.

The retained 9 topic self-checks are: scoping; the 3 ASC 480 classes; convertible separation exceptions; both own-equity gates and precise FX scope; SEC temporary equity and accretion; subsequent measurement; distributions and triggered features; treasury-stock presentation; and a separately sourced IAS 32 comparison. No successful arithmetic check closes an unresolved legal accounting condition.
