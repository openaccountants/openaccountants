# Australian Division 7A minimum yearly repayment

For one existing complying amalgamated loan, what is the minimum yearly repayment formula
amount and do the supplied eligible repayments cover it?

This is an offline preparation aid for Australian private companies with a 30 June income year.
It supports 2021-22 to 2026-27 using the published ATO benchmark table. It refuses other years
and substituted accounting periods. It does not establish loan compliance or approve a return.

```js
import { assessDiv7aRepayment } from "./index.mjs";

const result = assessDiv7aRepayment({
  incomeYear: "2026-27",
  loanIncomeYear: "2025-26",
  standardIncomeYear: true,
  loanStatus: "complying_amalgamated",
  repaymentsReviewed: true,
  openingBalance: "100000.00",
  remainingTermYears: "7",
  eligibleRepayments: "19000.00",
});
// verdict: "shortfall_indicated"
// benchmarkRatePercent: "8.77"
// minimumYearlyRepaymentEstimate: "19715.97"
// repaymentTarget: "19715.97"
// shortfall: "715.97"
```

## Inputs and scope

All amounts are **AUD decimal strings**, non-negative, at most 15 whole digits and 2 decimal
places. Use `"0"` for an established zero; missing values, JavaScript numbers, scientific notation,
separators and whitespace are rejected. Returned monetary values are strings with 2 decimal places.

| Input | Required meaning |
| --- | --- |
| `incomeYear` | Supported year in `YYYY-YY` form |
| `loanIncomeYear` | Year the amalgamated loan was made, earlier than `incomeYear` |
| `standardIncomeYear` | Exactly `true`, confirming the company's 30 June income year |
| `loanStatus` | `"complying_amalgamated"` only after a reviewer establishes the existing s 109N/amalgamated loan and confirms no refinancing, term conversion or other term adjustments; `"not_complying"` is refused and other values remain unknown |
| `repaymentsReviewed` | Exactly `true`, confirming that the supplied repayments were assessed under s 109R, including its exclusions and exceptions |
| `openingBalance` | Amount not repaid at the end of the previous income year on the Division 7A basis; incorporate relevant pre-lodgment-day repayments attributed to the loan year. Do not subtract current-year repayments before applying the formula |
| `remainingTermYears` | Positive decimal string, up to 6 decimal places: longest actual constituent-loan term less elapsed income years under s 109E(6), before statutory rounding up. Use the actual term, not automatically the 7-year or 25-year maximum |
| `eligibleRepayments` | Established amount applied during the selected year after s 109R review |

The rounded remaining term cannot exceed 25 years or imply an original term above 25 years
given the supplied loan year. This bounds computation; it does not establish eligibility for a
25-year secured loan or verify the actual loan terms. Calculate separate amalgamated loans
separately. Unknown facts must remain unknown rather than being replaced with optimistic inputs.

## Calculation and rounding

ITAA 1936 s 109E(5)-(6): `MYR = P*r / (1 - (1/(1+r))^n)`, with the supplied positive remaining
term rounded **up** to a whole year before calculation. The first repayment year has zero elapsed
income years in the statutory term calculation. The current year's published benchmark is used.

The function uses exact `BigInt` rational arithmetic. The statute does not prescribe cents
rounding. `minimumYearlyRepaymentEstimate` uses nearest-cent, half-up rounding for display;
`repaymentTarget` rounds the exact formula amount up to the next cent. `shortfall` is the positive
difference between that target and the supplied cent-denominated repayments. Thus a displayed
estimate rounded down cannot incorrectly indicate that repayments cover the exact formula amount.

For example, $10,000 at 8.77% with 6 years remaining produces a displayed estimate of $2,213.93,
but a target of $2,213.94. Repayments of $2,213.93 leave a positive shortfall rounded up to $0.01.
The rounding conventions are stated in every result and are not presented as ATO rules.

## Outputs and limits

Results include the verdict, reason codes, reasons, source links, rules date, rounding policy
and scope limits. Calculated results include the supplied amounts, rounded term, benchmark,
estimate, target and shortfall. `unknown` and `refused` results contain **no calculated money**.
`no_shortfall_indicated` is conditional on caller-attested inputs, not a compliance determination.

A shortfall is **not a deemed dividend**. Review all relevant conditions, s 109Q exceptions,
s 109Y distributable surplus and any applicable relief separately. The function does not form
amalgamated loans, assess s 109N compliance, decide whether repayments count, calculate annual
interest from changing balances, or produce a closing balance or repayment schedule.

Primary sources and checked dates are in [rules.json](rules.json). The ATO rate page was updated
1 July 2026; all listed sources were checked on 21 October 2026. Review subsequent amendments
and rate publications before using the result. No runtime network or clock is consulted.

## Verification and provenance

Run `node --test calculators/au-div7a-repayment/` from the repository root on Node 20+ with JSON
import attributes. Tests cover published-year mapping, independent one- and two-year formula
forms, fractional terms, cents boundaries, zero/missing inputs, scope refusals and bounded inputs.
All examples are fabricated. No real client data or Xero connection is used.

The contract was adapted from Ryan Duguid's independently authored
[div7a-loan-review](https://github.com/ryanduguid/australian-accounting/tree/main/packages/div7a-loan-review)
at revision `55a037cd90fc29aa7ad5799b37c3c55066464f25`. This JavaScript implementation fits the
existing embeddable calculator format without introducing a separate runtime or dependencies.
The source engine's nearest-cent estimate is retained; the upward payment target is an additional
precaution against a rounded-down estimate. Code: AGPL-3.0-only; figures and wording: OA Guide
License v1.0, following this repository's licensing policy.

General reference and computational support only. Obtain qualified professional review before
filing, paying or relying on any result.
