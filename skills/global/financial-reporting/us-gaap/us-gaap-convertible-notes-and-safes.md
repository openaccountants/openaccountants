---
name: us-gaap-convertible-notes-and-safes
description: "Draft issuer transaction working paper for convertible notes and SAFEs under ASC 470, 480 and 815. Extracts contract terms, sequences classification questions, illustrates the ASU 2020-06 single-liability debt basis and contractual conversion arithmetic, and holds unresolved SAFE classification. Load financial-reporting-workflow-base and us-gaap-debt-vs-equity."
jurisdiction: US
category: financial-statements
domain: financial-reporting
type: computation
standard: "ASC 470-20 Debt with Conversion and Other Options; ASC 480 and ASC 815 (ASU 2020-06 and ASU 2024-04 amendment basis)"
effective_date: 2025-12-16
tier: 2
status: needs_sources
last_updated: 2026-11-22
version: 0.1
depends_on:
  - financial-reporting-workflow-base
  - us-gaap-debt-vs-equity
---

# US GAAP convertible notes and SAFEs v0.1

> **General reference only.** Draft working papers for AI-assisted accounting; no accountant has approved this version. Outputs need a qualified professional's review for the entity's actual facts.

## Scope

**Publication hold.** Current authoritative Codification access is unresolved. This file is held with `status: needs_sources`; do not publish it as a complete current-US-GAAP method. The specifically cited FASB Updates support the amendment-basis research below, not an assertion that every intervening amendment has been incorporated. Unrecovered conclusions are listed individually under Sources and are not usable instructions.

Load `financial-reporting-workflow-base`. Prepare a source-linked working paper, proposed balanced journal entries, disclosure checklist and reviewer brief. Keep assumptions separate from source-confirmed rules. Do not issue financial statements, an audit opinion or a tax return from this file.

This is a contract-to-working-paper job for the issuer, distinct from `us-gaap-debt-vs-equity`, which owns the general instrument-classification analysis. Load that Guide too. A SAFE's legal name, absence of interest or absence of a stated maturity does not establish equity classification. Holder accounting, tax and securities-law advice are outside this job.

The date key 2025-12-16 marks the first possible annual-period start after 15 December 2025 for ASU 2024-04, including interim periods. Early adoption requires ASU 2020-06 adoption and the stated transition choice. For the latter, distinguish SEC-filer PBEs other than eligible smaller reporting companies from all other entities; the ordinary effective-year boundaries are after 15 December 2021 and after 15 December 2023 respectively. [ASU 2024-04 transition summary](https://storage.fasb.org/ASU%202024-04.pdf); [ASU 2020-06 transition summary](https://storage.fasb.org/ASU%202020-06.pdf).

## Ask the client first

- Full signed instruments, side letters, amendments, investor rights and all related issuances.
- PBE/SEC status, smaller-reporting-company transition facts, period and actual amendment adoption.
- Proceeds, face amount, coupon, maturity, discounts/caps and precise pre-money/post-money capitalization definitions.
- Qualified-financing, liquidity, dissolution, cash-settlement, redemption, foreign-currency and indexation terms.
- Shares authorized/committed, settlement alternatives, fair-value elections and valuation reports.
- Transaction fees, modifications, conversion offers, acceptance date and historical entries.

## The method, step by step

1. **Build the term matrix.** Separate each freestanding instrument and embedded feature; list all events and settlement outcomes. Link the precise clause for each cash/share right, including contingent and investor-choice outcomes. Do not reduce a long contract to only its cap and discount. Obtain current ASC 480/815 and debt/equity scope conclusions from the companion working paper before booking.
2. **Apply only the cleared debt basis.** In the read ASU 2020-06 amendment, after considering the fair-value option and embedded-derivative guidance, convertible debt is generally one liability unless a separation requirement survives. Bifurcated derivatives, the substantial-premium presumption and other stated/unstated rights require separate analysis. Do not split out an equity option merely by valuing comparable straight debt. [ASU 2020-06, 470-20-25-1 and -25-12 through -25-15](https://storage.fasb.org/ASU%202020-06.pdf).
3. **Prepare the debt rollforward.** Reconcile opening carrying amount, proceeds, interest, payments, conversions, fees and any separately measured components. The par/no-fee case below uses its stated coupon as the effective interest input. Discounted issuance, transaction costs, noncash interest and modifications require separately sourced measurement; do not use the par shortcut for them.
4. **For a SAFE, finish classification before the journal.** Require current conclusions for ASC 480 obligations, ASC 815 derivative scope/indexation and settlement provisions, and applicable equity/temporary-equity presentation. The read own-equity amendment removes some old disqualifiers, but does not establish that a particular SAFE qualifies. Its remaining share-availability, share-limit and cash-settlement conditions are not a substitute for the whole indexation test. SAFE classification/measurement remains held under Sources. [ASU 2020-06, 815-40-25-10/-25-10A](https://storage.fasb.org/ASU%202020-06.pdf).
5. **Recompute the actual conversion contract.** Only after reading the definitions, calculate each candidate share price, identify the contractual comparison rule, apply any accrued-interest conversion clause and reconcile the resulting share count to the cap table. Pre-money and post-money definitions may produce different equations. This is contract arithmetic; it neither measures fair value nor clears the accounting entry.
6. **Separate ordinary and induced conversions.** For an adopted ASU 2024-04 induced-conversion analysis, inspect the limited offer period, preservation of conversion consideration in form/amount and substantive conversion feature at issuance and acceptance. If a non-substantial exchange or modification occurred in the one year before acceptance, compare against the conversion privileges existing one year before acceptance. Where either settlement formula depends on future share prices, use acceptance-date share fair value; indexing to something other than future issuer share price changes settlement form. If the conditions hold, the read rule expenses the inducement's excess fair value. Failure is not permission to use the shortcut; obtain the applicable extinguishment analysis. [ASU 2024-04, 470-20-40-13/-40-13A and -40-16](https://storage.fasb.org/ASU%202024-04.pdf).

## Worked cases

All amounts, rates and contractual definitions are hypothetical. Source and classification holds still apply.

**Par convertible debt.** Assume separately cleared single-liability classification, $250,000 proceeds and face value, a 6% annual cash coupon, no separate feature, fees, premium or discount and one full year outstanding. Dr cash / Cr debt $250,000 initially; Dr interest expense / Cr cash $15,000 after the year. Closing debt remains $250,000. An ordinary conversion's accounting entry is separately held; it is not an induced conversion just because shares are issued.

```oa-check
name: Par convertible-note coupon without fees or separate components
inputs:
  proceeds: 250000
  principal: 250000
  annual_coupon_rate: 0.06
steps:
  - initial_debt: proceeds
  - interest_expense: principal * annual_coupon_rate
  - cash_coupon: principal * annual_coupon_rate
  - closing_debt: initial_debt + interest_expense - cash_coupon
expected:
  initial_debt: 250000
  interest_expense: 15000
  cash_coupon: 15000
  closing_debt: 250000
```

**SAFE contractual cap-versus-discount comparison.** The hypothetical signed contract explicitly defines its cap price as a $6,000,000 pre-money cap divided by a fixed 3,000,000-share capitalization base; the base excludes this SAFE and no other conversion changes it. It converts $300,000 at the lower of that price and 70% of a $4 financing price. Cap price $2; discount price $2.80; conversion price $2; shares 150,000. With no cap under a separate comparison contract, the discount-only quantity would be about 107,142.86 shares before the contract's fractional-share rule. Do not reuse this formula for a post-money SAFE or infer any journal/classification from it.

```oa-check
name: Supplied SAFE contract arithmetic with fixed pre-money denominator
inputs:
  investment: 300000
  valuation_cap: 6000000
  defined_capitalization: 3000000
  financing_price: 4
  discount_multiplier: 0.70
steps:
  - cap_price: valuation_cap / defined_capitalization
  - discount_price: financing_price * discount_multiplier
  - contractual_price: min(cap_price, discount_price)
  - conversion_shares: investment / contractual_price
  - discount_only_shares: round(investment / discount_price, 2)
expected:
  cap_price: 2
  discount_price: 2.8
  contractual_price: 2
  conversion_shares: 150000
  discount_only_shares: 107142.86
```

## When to refuse or refer

Do not book a SAFE from the illustrative share count. Hold incomplete contracts, unsettled indexation, redemption or cash rights, unclear capitalization definitions and missing valuation. Refer multi-instrument allocations, embedded derivatives, post-money circular equations, modification/extinguishment, substantial premiums, SEC presentation and tax. The existing classification Guide is a required dependency, not an implied clearance.

## Sources

| Official source | Passages actually read | Read date |
|---|---|---|
| [ASU 2020-06](https://storage.fasb.org/ASU%202020-06.pdf) | 470-20-25-1, -25-12 through -25-15; 815-40-25-10/-25-10A; transition summary. | 2026-11-22 |
| [ASU 2024-04](https://storage.fasb.org/ASU%202024-04.pdf) | 470-20-40-13/-40-13A, -40-16 and transition summary. Induced conversions only. | 2026-11-22 |

**Not yet confirmed:** Complete current ASC 480/815 classification/indexation and deferrals; SAFE-specific initial/subsequent measurement and presentation; ordinary conversion entries; fees, discounts, fair-value elections and embedded-derivative valuation; all later-amendment applicability. The SAFE worked case is arithmetic on assumed contract definitions, not an official FASB SAFE classification example. Current ASC browser access attempted 2026-11-21 stopped at CAPTCHA/terms. All listed source gaps remain non-usable.
