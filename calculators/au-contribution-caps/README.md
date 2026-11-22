# Australian contributions caps

For one person and income year, what are the concessional and non-concessional contributions
caps, how much unused concessional cap from earlier years is carried in and applied, and what
is over each cap?

This is an offline preparation aid for 2024-25, 2025-26 and 2026-27. It works out the unused
concessional cap year by year from 2018-19 (ITAA 1997 s 291-20(3) to (7)) and the first year of
a non-concessional bring forward (s 292-85(2) to (5)). It does not decide what to contribute,
issue a determination or work out the tax on an excess.

```js
import { assessContributionCaps } from "./index.mjs";

const result = assessContributionCaps({
  incomeYear: "2024-25",
  totalSuperBalanceBeforeYear: "450000",
  concessionalContributions: "97500",
  nonConcessionalContributions: "0",
  under75AtAnyTimeInYear: true,
  definedBenefitInterest: false,
  constitutionallyProtectedFund: false,
  earlierBringForwardCoversYear: false,
  earlierYears: [
    { incomeYear: "2019-20", concessionalContributions: "11000" },
    { incomeYear: "2020-21", concessionalContributions: "12000" },
    { incomeYear: "2021-22", concessionalContributions: "13000" },
    { incomeYear: "2022-23", concessionalContributions: "14000" },
    { incomeYear: "2023-24", concessionalContributions: "15000" },
  ],
});
// verdict: "caps_calculated"
// concessional: { generalCap: "30000.00", unusedCapCarriedIn: "67500.00",
//   capIncrease: "67500.00", cap: "97500.00", excess: "0.00", ... }
```

That is the ATO's example of Sam, whose balance the ATO gives only as below $500,000.

## Inputs and scope

Amounts are non-negative AUD decimal strings with at most 2 decimal places; a missing amount is
not zero. Every input is supplied by the caller, and the calculator does not verify it.

| Input | Required meaning |
| --- | --- |
| `incomeYear` | `2024-25`, `2025-26` or `2026-27` |
| `totalSuperBalanceBeforeYear` | Total superannuation balance just before the start of the year (at 30 June before it) |
| `concessionalContributions` | The year's concessional contributions (s 291-25) |
| `nonConcessionalContributions` | The year's contributions and amounts under s 292-90(1)(a) and (aa); the calculator adds any excess concessional contributions itself (s 292-90(1)(b)) |
| `under75AtAnyTimeInYear` | `true` or `false`: under 75 at any time in the year (s 292-85(3)(c)) |
| `definedBenefitInterest` | `true` or `false`: a defined benefit interest in the year or an earlier year given. `true` is refused (Subdivision 291-C) |
| `constitutionallyProtectedFund` | `true` or `false`: an interest in a constitutionally protected fund. `true` is refused (ss 291-25(4)(a), 292-90(2)(c)(iv)) |
| `earlierBringForwardCoversYear` | `true` or `false`: s 292-85(6) or (7) sets this year's cap, because a bring forward started in one of the 2 previous years makes it the second year, or the third year of a 3-year bring forward. `true` is refused. After a 2-year bring forward the third year's cap is the general cap (s 292-85(4)), so state `false` for it |
| `earlierYears` | Required when the balance is below $500,000; optional otherwise. Each of the previous 5 years once, with `incomeYear` and `concessionalContributions`, and earlier years back to 2018-19 without a gap. A year whose contributions exceed its cap also needs its `totalSuperBalanceBeforeYear`, and then every year from 5 before it (or 2018-19) |
| `excessConcessionalReleased` | Required only when the concessional contributions exceed the cap available. `false` counts the whole excess as non-concessional; `true` is refused, as s 292-90(1A) reduces the count by each amount released divided by 85% |

A missing or malformed input gives `unknown` with no figures; a case outside these rules gives
`refused` with no figures. Other years are refused: the 2027-28 caps are not published.

## Calculation

Concessional (s 291-20):

- The general cap for each year is the ATO's published indexed amount, from $25,000 for 2018-19
  to $32,500 for 2026-27.
- A year's unused cap is its shortfall below its cap; there is none before 2018-19 (s 291-20(6)
  and (7)).
- When a year's contributions exceed its cap and the balance just before it is less than
  $500,000, the unapplied unused cap of the previous 5 years increases the cap, earliest year
  first, by no more than the excess (s 291-20(3) to (5)). This applies in earlier years too, so
  an amount used in an earlier year is not carried again.
- At $500,000 or more nothing is applied, but the amounts still age: each lapses at the end of
  the fifth year after its own (`expiresAtEndOf`; `expiringAtEndOfYear` is what lapses this year).

Non-concessional (s 292-85):

- The general cap is 4 times the concessional general cap, or nil when the balance equals or
  exceeds the general transfer balance cap ($1.9 million, $2 million and $2.1 million for the 3
  years).
- The first year cap space is that transfer balance cap less the balance. When it exceeds the
  general cap and the person is under 75 at any time in the year, contributions over the general
  cap start a bring forward: twice the general cap (2 years) when the cap space is at most twice
  the general cap, otherwise 3 times (3 years). Until contributions counted exceed the general
  cap, `cap` is the general cap; `firstYearCapIfBringForwardStarts` is the first year cap that
  contributions over it would start, given the stated age and earlier bring forward facts.
- Contributions counted are `nonConcessionalContributions` plus the year's unreleased excess
  concessional contributions.

Amounts are exact in cents; no rounding is needed.

## Outputs and limits

Results include the verdict, reason codes, reasons, sources and limits, with `concessional`
(`balanceBelowCarryForwardThreshold` is the balance condition alone: the cap rises only by
`capIncrease`),
`carryForward` (each of the previous 5 years: unused cap, carried in, applied this year,
remaining and when it lapses; `null` when no earlier years were given) and `nonConcessional`
(general cap, transfer balance cap, contributions counted, the first year cap a bring forward
would give, whether one started and for how many years, cap, remaining and excess). `remaining` in a first bring forward year is the first year's shortfall,
which s 292-85(6) carries to the second year only while the balance stays below the transfer
balance cap.

Out of scope: which contributions are concessional or non-concessional, when a fund received
them, the CGT cap, downsizer and other excluded contributions, reallocation or disregard
decisions, releases, the tax on an excess, Division 293 and Division 296. The caps and the
ATO's tables were read on 18 November 2026; review later indexation and amendments before
relying on the result. The Act was read as compilation 268 (in force 1 October 2026). The
compilation from 1 December 2026 adds only Schedule 1, items 41 to 45 of the Treasury Laws
Amendment (Financial Reporting System Reform) Act 2026 (No. 61, 2026), which amend
ss 25-110(3), 715-375(1)(b), 715-379(1)(b) and 995-1; none of ss 291-20, 291-25, 292-85 or
292-90 changes. No runtime network or clock is consulted.

## Verification and provenance

Run `node --test calculators/au-contribution-caps/` from the repository root on Node 20+ with
JSON import attributes; From the repository root, run `node --test calculators/*/index.test.mjs` to run every calculator suite. Tests reproduce the ATO's Sam
example and the unused amounts of its carry-forward table, the $500,000 boundary at $499,999.99
and $500,000.00, hand-worked histories (an earlier year's increase, a partial application, a
lapse), every bring forward band boundary in the ATO's tables for the 3 years, the transfer
balance cap, an unreleased excess starting a bring forward, and refusals of malformed or
out-of-scope inputs. No client data is used.

The rules were adapted from Ryan Duguid's independently authored `contribution-caps` worksheet in
[australian-tax-calculators](https://github.com/ryanduguid/australian-accounting/tree/main/packages/australian-tax-calculators)
at revision `2e41b018a5a1c5229df2b3fe29de1fe716311fe9`. Its proposed-contribution input and
supplied-total mode are not ported; the excess concessional count (s 292-90(1)(b)), the earlier
bring forward test (s 292-85(3)(d)) and the constitutionally protected fund exclusion are added
from the Act. Code and this README: AGPL-3.0-only;
`rules.json`: OA Guide License v1.0, following this repository's licensing policy.

General reference and computational support only. Obtain qualified professional review before
contributing, lodging or relying on any result.
