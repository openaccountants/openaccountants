# Australian Division 296 tax estimate (2026-27)

From one person's total superannuation balance and total superannuation earnings, what would their
Division 296 tax be for 2026-27?

This is an estimate from the inputs the member supplies, not an assessment. The ATO assesses the
tax from what each fund reports, and the notice of assessment sets the amount. The calculator does
not work out the balance or the earnings: establish both first, from the funds' figures.

```js
import { estimateDivision296 } from "./index.mjs";

const result = estimateDivision296({
  incomeYear: "2026-27",
  totalSuperBalanceAtYearEnd: "12000000",
  totalSuperEarnings: "500000",
  protectedOfficeOrFund: false,
  childRecipient: false,
  structuredSettlementContribution: false,
  diedOnOrBeforeYearEnd: false,
});
// verdict: "estimate_calculated", reason_codes: ["caller_attested_inputs", "liable"]
// largeBalanceSharePercent: "75.00", veryLargeBalanceSharePercent: "16.67"
// taxableSuperannuationEarnings: "375000.00", veryLargeBalanceEarningsComponent: "83350.00"
// taxOnTaxableEarnings: "56250.00", taxOnVeryLargeComponent: "8335.00"
// division296TaxEstimate: "64585.00"
```

## Status of the law

Division 296 is law. The Treasury Laws Amendment (Building a Stronger and Fairer Super System) Act
2026 (No. 8, 2026) and the Superannuation (Building a Stronger and Fairer Super System) Imposition
Act 2026 (No. 9, 2026) received assent on 13 March 2026, and Division 296 of the Income Tax
Assessment Act 1997 commenced on 1 April 2026. It applies from the 2026-27 income year. This
calculator follows the enacted text, not the earlier proposals.

## Inputs and scope

Money is an AUD decimal string with at most 15 whole digits and 2 decimal places, such as
`"4000000"` or `"-1250.50"`. Numbers, grouped digits and exponents are rejected. Every input is the
caller's attestation, which the calculator does not verify.

| Input | Required meaning |
| --- | --- |
| `incomeYear` | `"2026-27"`; other years are refused |
| `totalSuperBalanceAtYearEnd` | Total superannuation balance at the end of 30 June 2027, leaving out any LRBA amount (s 296-260). Not negative |
| `totalSuperEarnings` | Total superannuation earnings for 2026-27 (s 296-55): see below. It can be negative |
| `protectedOfficeOrFund` | `true` if, at any time in 2026-27, the person had an interest in a constitutionally protected fund or a death benefit income stream from one; is or was a judge named in s 296-55(3) items 2 to 4 (High Court, a federal court, or the ACT or NT Supreme Court); is or was a State higher level office holder, such as a State parliamentarian or judge; or received a death benefit income stream because of such a person's death. Refused: s 296-55(3) and Imposition Act s 6, which removes the tax where imposing it would exceed the Commonwealth's legislative power, can reduce or remove the tax |
| `childRecipient` | `true` if the person was a child recipient of a superannuation income stream at any time in 2026-27 (s 296-20) |
| `structuredSettlementContribution` | `true` if a structured settlement contribution was made for the person in 2026-27 or an earlier year (s 296-25) |
| `diedOnOrBeforeYearEnd` | `true` if the person died on or before 30 June 2027 (ITTPA s 296-1(3)) |

Each of the 4 yes-or-no answers must be `true` or `false`; a missing answer gives `unknown`, not an
assumption.

Total superannuation earnings is neither the change in the balance nor an account's investment
return. It is the total of the person's relevant superannuation earnings for each interest they
have at any time in the year and each interest supporting a death benefit income stream they
receive in the retirement phase (s 296-55(1)). For most interests that is a share of the fund's
Division 296 fund earnings (s 296-65), worked out from the fund's taxable income (s 296-60, so
capital gains count when realised, with the ITTPA's transitional CGT adjustments) and taken as nil
if negative (s 296-60(7)). A defined benefit interest not in the retirement phase uses the s 296-70
formula instead, which can give a negative amount, so the total can be negative. The earnings of
foreign funds and of Division 296 excluded interests (s 296-55(3): judges' pension interests and
non-complying plans, for example) count as nil. Supply the total after these rules; the calculator
applies none of them.

## Calculation

For 2026-27 only the balance at 30 June 2027 counts (Income Tax (Transitional Provisions) Act 1997
s 296-1(2)); it is nil after death (s 296-50).

| Step | Rule |
| --- | --- |
| Share above a threshold | (balance - threshold) / balance x 100, rounded to 2 decimal places, up from a third decimal place of 5; nil unless the balance is greater than the threshold (ss 296-40(2), (3) and 296-45(2), (3)) |
| Thresholds | $3,000,000 large and $10,000,000 very large for 2026-27 (ss 296-30, 296-35) |
| Taxable superannuation earnings | share above $3,000,000 x earnings, when the balance is greater than $3,000,000 and the earnings greater than nil (s 296-40(1)) |
| Very large component | share above $10,000,000 x earnings (s 296-45(1)); it has no earnings condition, so it keeps a negative sign, but no tax then arises |
| Liability | taxable superannuation earnings, unless s 296-20, s 296-25 or ITTPA s 296-1(3) applies (s 296-15) |
| Tax | 15% of taxable superannuation earnings plus 10% of the very large component (Imposition Act s 5) |

Each amount shown is worked from exact values, not from another rounded amount, and rounded half
away from zero to the cent; the total is the sum of the 2 tax amounts shown. A tax amount can
therefore differ by a cent from the rate applied to the rounded earnings shown. The Acts set no
rounding for these amounts.

## Outputs and limits

Results include the verdict, reason codes, reasons, sources, the rounding note and the limits. The
second reason code says why: `liable`, `share_rounds_to_nil`, `balance_not_above_threshold`,
`earnings_not_above_nil`, `child_recipient`, `structured_settlement_contribution` or
`died_on_or_before_year_end`. `unknown` and `refused` results contain **no calculated figure**; a
refusal's code is `unsupported_year` or `protected_office_or_fund`.

The calculator does not work out the total superannuation balance or the total superannuation
earnings (ss 296-55 to 296-75), and does not cover temporary residents who depart Australia
(Subdivision 296-E), Division 296 debt accounts, release authorities or payment. From 2027-28 the
thresholds are indexed and the balance just before the start of the year also counts; those years
are refused until the indexed thresholds are published. It does not
project balances or compare holding assets inside and outside super.

Primary sources are in [rules.json](rules.json): ITAA 1997 compilation 268 (1 October 2026), ITTPA
1997 compilation 104 (1 October 2026), both Acts as made, Parliament's bill page and the
Explanatory Memorandum, all read on 18 November 2026. Review later amendments before using the
result. No runtime network or clock is consulted.

## Verification and provenance

Run `node --test calculators/au-division-296/` from the repository root on Node 20+ with JSON
import attributes; From the repository root, run `node --test calculators/*/index.test.mjs` to run every calculator suite. Tests reproduce Examples 1.1 ($3,750)
and 1.2 ($64,585) of the Explanatory Memorandum to the Bill, and cover the rounding of each share,
both threshold boundaries, cent rounding, nil and negative earnings, each exception and refusals of
malformed or out-of-scope inputs. The other inputs are invented; no client data is used.

The rules were adapted from Ryan Duguid's independently authored
[Division 296 tax calculator](https://github.com/ryanduguid/ryanduguid.github.io/blob/main/assets/division-296.mjs)
at revision `869d73ee20652be14e0b27a86e3e92bbf7e0681c`, with the thresholds and rates moved from
the caller into `rules.json`. Its page layout and browser tests are not ported. Code and this
README: AGPL-3.0-only; `rules.json`: OA Guide License v1.0, following this repository's licensing
policy.

General reference and computational support only. Obtain qualified professional review before
paying, filing or relying on any result.
