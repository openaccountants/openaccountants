# Australian super guarantee charge for one QE day

For one employee and one QE day, what super guarantee charge does a late or missing contribution
bring?

This is an offline preparation aid for qualifying earnings paid from **1 July 2026 to 30 June
2027**, under Payday Super. It works out the individual final shortfall, the notional earnings and
the administrative uplift: 3 of the 4 components in SGAA s 16B(2). It leaves out the choice
loading. A quarter ending by 30 June 2026 stays under the old Act (Payday Super Act Sch 1 item
182(3)) and is refused, as is a QE day after 30 June 2027, whose maximum contributions base had not
been published on the check date.

```js
import { assessSuperGuaranteeCharge } from "./index.mjs";

const result = assessSuperGuaranteeCharge({
  qeDay: "2026-07-30",
  sgRateSchedule: "general",
  qualifyingEarnings: "1000",
  earlierQualifyingEarningsThisYear: "0",
  onTimeContributions: "0",
  lateContributions: [{ receivedDay: "2026-08-25", amount: "120" }],
  assessmentDay: "2026-12-01",
  noCommissionerInitiatedAssessmentOrEstimate: true,
});
// verdict: "charge_estimated"
// latestReceiptDay: "2026-08-11" (the Picnic Day holiday in the NT adds a day)
// sgAmount: "120.00", baseShortfall: "120.00", finalShortfall: "0.00"
// notionalEarningsDays: 14, notionalEarnings: "0.53"
// upliftPercent: 40, administrativeUplift: "0.21", chargeBeforeChoiceLoading: "0.74"
```

## Inputs and scope

Money is a non-negative AUD decimal string with at most 2 decimal places; `"0"` when there is
none. Dates are `YYYY-MM-DD` strings. Every input is the caller's attestation, which the
calculator does not verify.

| Input | Required meaning |
| --- | --- |
| `qeDay` and the optional extension inputs | As for [au-payday-super-timing](../au-payday-super-timing/README.md), which works out the last day for an on-time contribution |
| `sgRateSchedule` | `general` when the QE day contains no Norfolk Island salary or wages under Sch 1 item 189. Use `norfolk_island_transitional` when all the earnings fall under item 189 and `mixed` when some do. Supply the classification after checking the underlying facts |
| `qualifyingEarnings` | Qualifying earnings paid to or for the employee on the QE day, above nil (s 17A(2)) |
| `earlierQualifyingEarningsThisYear` | Qualifying earnings this employer paid to or for the employee earlier in 2026-27 (s 10A(6)) |
| `onTimeContributions` | Eligible contributions applied to this QE day under s 18C(1): received in the usual period, the 12 months before the QE day or an applicable s 18C(2) period |
| `lateContributions` | Eligible contributions received in the late period and applied to this QE day under s 18D(2), each `{ receivedDay, amount }`; `[]` when none |
| `assessmentDay` | Day the ATO makes the assessment. Required when the base shortfall is above nil |
| `noCommissionerInitiatedAssessmentOrEstimate` | `true` only if reg 13C applies: no Commissioner-initiated assessment made in the 24 months ending on the QE day is in force on it, and no SG charge estimate was made in that time. The 24 months start no earlier than 1 July 2026. Required when the base shortfall is above nil |
| `voluntaryDisclosureLodgedDay` | Optional. Day a voluntary disclosure statement in the approved form was lodged, from the QE day to the day before the assessment (s 33(2), reg 13D) |
| `assumedGicAnnualPercent` | Required only when the late period runs past 31 December 2026, the last published GIC quarter on the check date: the annual rate to assume, such as `"11.51"` |

Confirm the employer and employee residency and where the work was done. The transition can
apply to work on Norfolk Island or outside Australia by a Norfolk Island resident, or to work
on Norfolk Island by an Australian resident employed by a Norfolk Island resident. It applies to the
portion of earnings that qualifies. If the schedule is unresolved, the worksheet returns
`unknown`. Transitional and mixed earnings return `refused` for manual review.
[Payday Super Act Sch 1 item 189](https://www.legislation.gov.au/C2025A00057/asmade/text), [ATO LCR 2026/1](https://www.ato.gov.au/law/view/document?DocID=COG/LCR20261/NAT/ATO/00001).

## Calculation

| Step | Rule |
| --- | --- |
| SG amount | 12% of the qualifying earnings counted (s 17A(2)). Earnings that take the year's total from this employer past the maximum contributions base of $270,830 for 2026-27 count only to it; later payments count as nil (s 10A(5) and (6); ATO Table 23) |
| Base shortfall | The SG amount less on-time contributions, not below nil (s 18C(1)). Nil means no charge for the QE day, before any choice loading |
| Late period | From the day after the last day for an on-time contribution to the day before the assessment (s 6(1)) |
| Final shortfall | The base shortfall less late contributions, applied in the order received and not below nil (s 18D(2)) |
| Notional earnings | For each day of the late period on which the final shortfall is above nil, the GIC rate for the day times the notional sum: the base shortfall plus the earlier days' amounts (s 19A). The daily rate is the annual rate divided by the days in the calendar year (TAA 1953 s 8AAD(1)). The day the fund receives the contribution that clears the shortfall is counted |
| Administrative uplift | 60% of the final shortfall plus the notional earnings (s 19B(1)), less 20 percentage points under reg 13C and 40, 35, 30 or 15 points under reg 13D for a disclosure lodged by day 30, 60 or 120 of the period starting on the QE day, or later. It cannot fall below nil |
| Charge | Final shortfall + notional earnings + uplift (s 16B(2)(a) to (c)) |

The GIC rates held are 11.43% for July to September 2026 and 11.51% for October to December 2026
(ATO, last updated 4 September 2026). Each money result is rounded once to the cent, half up; the
Act sets no rounding, so this is a calculator convention ([rules.json](rules.json)).

The Act counts notional earnings for each day 'on which' the final shortfall is above nil, which
does not settle the receipt day. The calculator counts it, as the ATO does: its Juliet example
gives 25 days of earnings for contributions received 25 days after the due date. The same example
gives 50 days for an assessment '50 days after the due date', which counts the assessment day;
under s 6(1) the late period ends the day before it, and the calculator follows s 6(1). A reviewer
should confirm both against an ATO assessment.

## Outputs and limits

Results include the verdict, reason codes, reasons, sources, the rounding note and the limits.
`no_shortfall` results carry nil components. `unknown` and `refused` results carry no charge.
Other limits include defined benefit interests, employer shortfall exemption certificates, contributions made
from 1 to 28 July 2026 that Payday Super Act Sch 1 item 186 first applies to a June 2026 quarter
shortfall (supply only the remainder), a disclosed contribution with no receipt day (s 36(3)), or
general interest charge and penalties once the charge is payable. The ATO says the charge for QE
days from 1 July 2026 is deductible; that is not computed.

SGAA Compilation No. 78 (1 July 2026), SG Regulations Compilation No. 8 (1 July 2026), the Payday
Super Act as made, TAA s 8AAD and the ATO pages listed in [rules.json](rules.json) were read on 19
November 2026. Review later amendments and GIC rates before using the result. No runtime network or
clock is consulted.

## Verification and provenance

Run `node --test calculators/au-super-guarantee-charge/` from the repository root on Node 20+;
From the repository root, run `node --test calculators/*/index.test.mjs` to run every calculator suite. Tests cover the maximum contributions base, cent
rounding, the receipt-day count, part payments, an s 18C(2) extension, the GIC rate change on 1
October 2026, every reg 13C and 13D combination in the ATO's uplift table at each period boundary,
an assumed rate past the table, an independent floating-point recount of the notional earnings,
and refusals of malformed or out-of-scope inputs. They reproduce the ATO's Juliet example ($24.74 and
$49.65 of notional earnings on $3,600, with uplifts of $14.84 and $2,189.79, at an assumed 10%). The
other inputs are invented; no client data is used.

The rules were adapted from Ryan Duguid's independently authored
[SGC and Payday Super calculator](https://github.com/ryanduguid/ryanduguid.github.io/blob/20b7d885510a764a62f63493ef7b07965435ead8/assets/sgc-payday.mjs)
at revision `20b7d885510a764a62f63493ef7b07965435ead8`. Its quarterly charge, its own business-day
calendar and its page are not ported; this calculator takes the due day from
`au-payday-super-timing` and adds late contributions in several parts. Code and this README:
AGPL-3.0-only; `rules.json`: OA Guide License v1.0, following this repository's licensing policy.

General reference and computational support only. Obtain qualified professional review before
paying, filing or relying on any result.
