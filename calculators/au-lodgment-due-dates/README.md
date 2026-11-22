# Australian activity statement due dates, 2026-27

For one monthly or quarterly activity statement, on what day are lodgment and payment due?

This is an offline preparation aid for the ATO's 2026-27 lodgment program. It covers due dates
from 1 July 2026 to 30 June 2027, the span of the ATO's 2026-27 weekend and public holiday
tables, and refuses any statement whose date falls outside it. The due date shown on the
statement, or the ATO's record for the client, governs.

```js
import { assessActivityStatementDueDate } from "./index.mjs";

const result = assessActivityStatementDueDate({ form: "quarterly", period: "2026-12" });
// verdict: "due_date_calculated"
// rule: "original"
// nominalDueDate: "2027-02-28"
// dueDate: "2027-03-02"
// holidaysPassed: [{ date: "2027-03-01", name: "Labour Day (WA)", ato_first_business_day: "2027-03-02" }]
```

## Inputs and scope

| Input | Meaning |
| --- | --- |
| `form` | `monthly`, `quarterly`, or `head_company_payg_instalment` for a consolidated group head company's quarterly PAYG instalment activity statement |
| `period` | `YYYY-MM`: the calendar month, or the last month of a standard quarter (March, June, September or December) |
| `concession` | Optional: `none` (the default), `online` or `agent`. The caller states that the statement qualifies; not verified |
| `turnoverUpTo10Million`, `reportsGstMonthly`, `deferredGst` | Booleans, required for a December monthly statement with `agent` and ignored otherwise: annual turnover is up to $10 million, GST is reported monthly, the business is registered for deferred GST |

`online` claims the 2-week concession for a quarterly activity statement received and lodged
online. It excludes monthly statements, monthly GST payers with quarterly roles, head companies'
quarterly PAYG instalments, large business clients with substituted accounting periods and
instalment notices.

`agent` claims the registered agent program date for a statement lodged electronically through
Online services for agents or the Practitioner lodgment service after the client's previous
statement was lodged electronically. For a quarterly statement it excludes one with a monthly PAYG
instalment obligation, a consolidated head entity's PAYG instalment statement, a monthly GST
cycle and instalment notices. For a December monthly business activity statement the 21 February
date also requires up to $10 million annual turnover, monthly GST reporting and no deferred GST
registration: each must be stated, or the result is `unknown` with no date, and one that is not
met returns 21 January.

Where a claimed concession gives that form or period no later date, the original date is returned
with the reason code `concession_not_applicable`. Omitting a concession can only make the result
earlier.

## Calculation

| Form | Original date | Online | Agent |
| --- | --- | --- | --- |
| Monthly | 21st of the following month (GST Act s 31-10(1)) | none | December only: 21 February |
| Quarterly | 28 October, 28 February, 28 April, 28 July (GST Act s 31-8(1)) | 14 days later, except quarter 2: 11 August 2026, 11 November 2026, 12 May 2027 | 25 August 2026, 25 November 2026, 26 May 2027; none for quarter 2 |
| Head company PAYG instalment | 21st of the month after the quarter (TAA 1953 Sch 1 s 45-715(1)) | none | none |

A date that is not a business day moves to the first business day after it (TAA 1953 s 8AAZMB
for payment, Sch 1 s 388-52 for the approved form). A business day is any day other than a
Saturday, a Sunday or a public holiday for the whole of any State, the ACT or the NT. The holiday
list is the ATO's tables for the 2026-27 program, including the Melbourne Cup and the Christmas Eve
and New Year's Eve evening holidays the ATO applies. One row is left out: the tables give 28
September 2026 both as the first business day after 25 September and as WA's King's Birthday, and
that day was not a holiday in Karratha or Port Hedland. [rules.json](rules.json) records each row,
the ATO's first business day for it and the reason for the exclusion. No covered statement is due
on, or moves across, any of these 4 days; a test checks every covered result.

`nominalDueDate` is the date the law or program names, `dueDate` the date after any move, `rule`
which date applied (`original`, `online_concession`, `agent_program` or `december_agent`) and
`holidaysPassed` the listed holidays from the nominal date up to the due date.

## Outputs and limits

Results include the verdict, reason codes, reasons, the program year, the covered span, sources
and limits. `unknown` and `refused` results contain **no date**. Refused: a quarter that does not
end in March, June, September or December; any date outside 1 July 2026 to 30 June 2027, which
includes the June 2027 monthly and quarter 4 2026-27 statements (the ATO has not confirmed the
agent date for quarter 4).

A large withholder pays withheld amounts earlier than the 21st (TAA 1953 Sch 1 s 16-75(1)), and a
deferred BAS payer's later dates (ss 16-75(2A) and 45-61(2)) are not applied.

Out of scope: annual GST returns, instalment notices (forms N, R, S and T), deferred GST amounts
on imports (a deferred GST registration is used only to withhold the December 21 February date),
substituted accounting periods, tax periods that are not calendar months or standard quarters,
income tax, FBT and other returns, and deferrals the Commissioner grants, including disaster
extensions. Holidays the ATO changes after 18 November 2026 are not reflected.

The ATO pages and law sections in [rules.json](rules.json) were read on 18 November 2026. No
runtime network or clock is consulted.

## Verification and provenance

Run `node --test calculators/au-lodgment-due-dates/` from the repository root on Node 20+ with
JSON import attributes; From the repository root, run `node --test calculators/*/index.test.mjs` to run every calculator suite. Tests cover every covered month
and quarter under each concession, the Section 3 example of
[au-lodgment-deadlines-penalties](../../skills/australia/au-lodgment-deadlines-penalties.md)
(28 February 2027 to 2 March 2027), each ATO first business day the holiday list reproduces, a
cross-check against the Payday Super calculator's whole-state calendar, and refusals of malformed
or out-of-scope inputs. No client data is used.

The rules were adapted from Ryan Duguid's independently authored BAS due dates page
([ryanduguid.github.io](https://github.com/ryanduguid/ryanduguid.github.io/tree/main/tools/bas-due-dates)
at revision `f4d1710f3628e54fecd5bb8ea0e49be3eab9a7b3`) and the activity statement due dates and
holiday list of [au-fpa-pack](https://github.com/ryanduguid/au-fpa-pack) at revision
`d84e9a9dda1b83957b130e13fb978827c0297ac6`. Code and this README: AGPL-3.0-only; `rules.json`: OA
Guide License v1.0, following this repository's licensing policy.

General reference and computational support only. Obtain qualified professional review before
lodging, paying or relying on any result.
