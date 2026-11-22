# Australian Payday Super contribution timing

For one QE day, what is the latest day the employee's fund can receive the super guarantee
contribution for it?

This is an offline preparation aid for employers' qualifying earnings paid from 1 July 2026. It
counts business days on a whole-state holiday calendar verified from 1 July 2026 to 31 August
2027 and refuses any count that would pass that horizon. It does not decide whether a
contribution was on time, compute a shortfall or assess the super guarantee charge;
[au-super-guarantee-charge](../au-super-guarantee-charge/README.md) estimates the charge from its result.

```js
import { assessPaydaySuperTiming } from "./index.mjs";

const result = assessPaydaySuperTiming({
  qeDay: "2026-07-09",
  firstContributionToFund: true,
});
// verdict: "latest_receipt_day_calculated"
// periods: { usual_period: "2026-07-20", item_1: "2026-08-07" }
// latestReceiptDay: "2026-08-07"
// governingRule: "item_1"
// holidaysInWindow: [{ date: "2026-08-03", name: "Picnic Day", jurisdictions: ["NT"] }]
```

## Inputs and scope

Dates are `YYYY-MM-DD` strings. Other forms, impossible dates, timestamps, numbers and `Date`
objects are rejected. The optional inputs claim an extension under the s 18C(2) table; each is
supplied by the caller, and the calculator does not verify it.

| Input | Required meaning |
| --- | --- |
| `qeDay` | Day the qualifying earnings were paid to or for the employee, from 1 July 2026 |
| `firstContributionToFund` | Optional `true` or `false`. `true` only for the first eligible contribution to a fund or RSA after the employee commenced or recommenced, or after the employer stopped contributing to another fund or RSA (item 1). Opening another fund alone does not establish it |
| `outOfCycleNextStandardQeDay` | Optional. Only when this QE day's earnings are out-of-cycle under LI 2026/20 s 5: the first later QE day that is not out-of-cycle and falls on the next day consistent with the employee's established pay schedule (item 2). Omit it for a final payment with no later standard QE day |
| `exceptionalCircumstancesDeterminationDay` | Optional. The day the Commissioner made a s 18C(4) determination covering this employer and QE day (item 3) |
| `earlierContributionLatestDueDay` | Optional. The latest due day of an earlier eligible contribution the employer made and applied for an earlier QE day for this employee (item 4, the ATO's 'bunching rule') |

An extension that is not supplied is not applied, so a missing fact can only bring the result
earlier, never later. A QE day before 1 July 2026 is refused: the quarterly due dates apply to
it. Every date supplied and every day counted must lie within the verified calendar.

## Calculation

A business day is any day other than a Saturday, a Sunday or a public holiday for the whole of
any State, the ACT or the NT (SGAA s 6(1)). A territory-wide holiday anywhere delays every
employer; a regional or part-day holiday does not. The calendar's 17 weekday holidays, what it
leaves out and its sources are in [rules.json](rules.json).

Each period ends on the stated business day after the day it counts from:

| Rule | Ends on |
| --- | --- |
| Usual period (s 6(1)) | 7th business day after the QE day |
| Item 1 | 20th business day after the QE day |
| Item 2 | 7th business day after the next standard QE day |
| Item 3 | the later of the 20th business day after the QE day and the 20th business day after the determination day |
| Item 4 | the earlier contribution's latest due day |

`latestReceiptDay` is the latest of the usual period and every claimed item (s 18C(1)(c) and (2)).
`governingRule` names the period that gives it; a tie keeps the usual period. `periods` lists each
period's end, and `holidaysInWindow` the whole-state weekday holidays after the QE day up to the
result.

## Outputs and limits

Results include the verdict, reason codes, reasons, sources, the calendar horizon and the limits.
`unknown` and `refused` results contain **no calculated date**. A contribution counts only if the
fund receives it with the information it needs to allocate it. The calculator does not apply
amounts, the order of application or the 12-month pre-payment window in s 18C(1)(c)(ii), and does
not cover defined benefit interests or constitutionally protected funds.

Primary sources and the calendar check date are in [rules.json](rules.json). The ATO page was
last updated 29 September 2026; SGAA Compilation No. 78 (1 July 2026), LI 2026/20 and the 8
holiday pages were read on 18 November 2026. Review later amendments and holiday changes before
using the result. No runtime network or clock is consulted.

## Verification and provenance

Run `node --test calculators/au-payday-super-timing/` from the repository root on Node 20+ with
JSON import attributes; From the repository root, run `node --test calculators/*/index.test.mjs` to run every calculator suite. Tests reproduce all 6 ATO
examples, holiday and horizon boundaries, an independent business-day recount for every QE day in
the calendar, and refusals of malformed or out-of-scope inputs. The other inputs are invented; no
client data is used.

The rules were adapted from Ryan Duguid's independently authored
[payday-super-checker](https://github.com/ryanduguid/australian-accounting/tree/main/packages/payday-super-checker)
at revision `0fec0886ec1159a3852d26256d3517f1a6c45ecc`. Its item 4 evidence tests, receipt and
amount matching and charge estimate are not ported. Code and this README: AGPL-3.0-only;
`rules.json`: OA Guide License v1.0, following this repository's licensing policy.

General reference and computational support only. Obtain qualified professional review before
paying, filing or relying on any result.
