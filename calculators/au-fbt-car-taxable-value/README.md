# Australian FBT car fringe benefit taxable value

What is the taxable value of the car fringe benefits one car gave in the FBT year ending 31 March
2027, by the statutory formula or the operating cost method?

This is an offline preparation aid. It values car fringe benefits the caller has already
established: it does not decide whether a car benefit arises (FBTAA s 7) or is exempt (s 8,
including the s 8A electric car exemption), and does not gross up or compute FBT. It refuses
other FBT years and a commitment made before 7.30 pm AEST on 10 May 2011.

```js
import { assessCarFringeBenefit } from "./index.mjs";

const result = assessCarFringeBenefit({
  fbtYear: 2027,
  method: "statutory",
  commitmentBefore10May2011: false,
  carValue: "40000",
  earliestHoldingDate: "2026-04-01",
  laterAccessoriesCost: "0",
  privateUseDays: 365,
  recipientsPayment: "1000",
});
// verdict: "taxable_value_calculated"
// method: "statutory"
// baseValue: "40000.00", statutoryValue: "7000.00", taxableValue: "7000.00"
```

## Inputs and scope

Money is an AUD decimal string with at most 2 decimal places; `"0"` is valid where nil is
possible, and a missing amount is never read as nil. Dates are `YYYY-MM-DD` strings. Days and
kilometres are whole numbers.

| Input | Required meaning |
| --- | --- |
| `fbtYear` | `2027`, the FBT year ending 31 March 2027 |
| `method` | `"statutory"`, or `"operating_cost"` where the employer elects s 10 for this car |
| `commitmentBefore10May2011` | Whether the last commitment by the employer, the employee or an associate to the car's application or availability for the period was made before 7.30 pm AEST on 10 May 2011 (Tax Laws Amendment (2011 Measures No. 5) Act 2011, Sch 5 item 8(2)); `true` is refused, as the earlier statutory percentages apply |
| `carValue` | Cost price (s 136(1)) if the provider or an associate owned the car at the earliest holding time, otherwise its leased car value at that time: GST, luxury car tax and non-business accessories fitted at or about acquisition included; registration and stamp duty excluded |
| `earliestHoldingDate` | Day the provider or an associate first held the car (s 9(2)(b)) |
| `laterAccessoriesCost` | Cost price of non-business accessories fitted after that time and before the year ended, still fitted at a time in the year when the provider held the car (s 9(2)(a)(iii)) |
| `privateUseDays` | Days in the year on which the car was used or taken to be available for private use |
| `recipientsPayment` | Recipient's payment under ss 9(2)(e) and 10(3)(c): consideration paid for the benefits, and car expenses borne with the declaration or documentary evidence the Act requires, each less reimbursements |

The operating cost method also needs:

| Input | Required meaning |
| --- | --- |
| `operatingCost` | Operating cost for the holding period (s 10(3)(a)), above nil: running costs, registration and insurance, plus deemed depreciation and deemed interest for an owned car or lease charges for a leased one |
| `businessKilometres`, `totalKilometres` | The employer's reasonable estimate of business kilometres (s 162F) and the total for the holding period; supplying them stands for the employer specifying that estimate and the business use percentage (ss 10A(d), (e), 10B(b), (c)) |

Where `businessKilometres` is above nil, each condition for the business use reduction is a
separate input stated as `true` or `false`; one left unstated gives no figure:

| Input | When required | Condition |
| --- | --- | --- |
| `logBookYear` | Always | The year is a log book year (s 162G) |
| `odometerRecordsMaintained` | Always | Odometer records were maintained for the holding period (ss 10A(b), 10B(a)) |
| `providerIsEmployer` | Always | The employer is the provider |
| `logBookRecordsMaintained` | In a log book year | Log book and odometer records were maintained for an applicable log book period (ss 10A(a), 162H) |
| `recordsGivenBeforeDeclarationDate` | Where the provider is not the employer | Those records were given to the employer before the declaration date (ss 10A(c), 10B(a)) |

## Calculation

| Value | Formula |
| --- | --- |
| Base value | `carValue` x 2/3 if the year begins later than the fourth anniversary of the earliest holding day, otherwise x 1, plus `laterAccessoriesCost` (s 9(2)(a)) |
| Statutory formula | 20% x base value x `privateUseDays` / 365 - `recipientsPayment` (s 9(1)) |
| Business use percentage | `businessKilometres` / `totalKilometres` (s 136(1)); nil if any records condition is false (s 10(2)) |
| Operating cost method | `operatingCost` x (100% - business use percentage) - `recipientsPayment` (s 10(2)) |

With `method: "operating_cost"`, a higher operating cost value gives way to the statutory formula
(s 10(5) applies only where it 'exceeds', compared before rounding); a tie keeps the election.

A negative value is nil. The Act is silent: ss 9(1) and 10(2) are plain formulas with no floor.
The nil floor follows the ATO's FBT return 2026 instructions for item 23: where contributions
exceed the gross taxable value, show zero, and excess contributions for one benefit type do not
reduce other benefits. The instructions floor each category's total; flooring each car is this
calculator's assumption, and it can give a higher total than netting cars within a category.

The Act prescribes no rounding. By this calculator's convention each value is computed exactly and
rounded half up to the cent once. The ATO's employer guide shows whole dollars and drops the cents
($5,983 for $5,983.56 in its Example 28).

The calculator follows the Act where the ATO's employer guide differs. Its Example 26 leaves a
$1,000 accessory bought with the car out of the one-third reduction ($21,000); s 136(1) puts an
accessory fitted at or about acquisition in the cost price, which s 9(2)(a)(i) reduces, giving
$20,666.67.

## Outputs and limits

Results include the verdict, reason codes, reasons, sources and limits. `unknown` and `refused`
results contain **no figure**. The calculator does not compute deemed depreciation or deemed
interest (s 11), the gross-up, FBT payable, the reportable fringe benefits amount, the otherwise
deductible rule, not-for-profit concessions or the record keeping exemption. Replacement cars
(s 162K) and fleets under PCG 2016/10 are outside scope. To gross up, aggregate taxable values by
class as Rule 1 of [au-fbt](../../skills/australia/au-fbt.md) sets out.

The law sections (Federal Register compilation C2026C00332, in force from 1 July 2026; ss 7 to 13
match compilation C2025C00239, in force from 1 April 2025 to 30 June 2026), the 2011 amending Act, the ATO employer
guide chapter 7 and the FBT return 2026 instructions in [rules.json](rules.json) were read on
18 November 2026. No runtime network or clock is consulted.

## Verification and provenance

Run `node --test calculators/au-fbt-car-taxable-value/` from the repository root on Node 20+ with
JSON import attributes; From the repository root, run `node --test calculators/*/index.test.mjs` to run every calculator suite. Tests reproduce Example 1 and
Test 3 of au-fbt and the ATO employer guide's Examples 28 (to the cent), 29 and 31, take Example
26's dates and its figure under the Act, and cover the fourth anniversary boundary, s 10(5), each
records condition, rounding, day bounds and refusals of malformed or out-of-scope inputs. No
client data is used.

The rules were adapted from Ryan Duguid's independently authored FBT car calculator
([ryanduguid.github.io](https://github.com/ryanduguid/ryanduguid.github.io/blob/main/assets/business-calculators.mjs),
`fbtCar`, at revision `4b7cfc9790b5914dfd77b40b7a704ff80f85f2c4`). Its caller-supplied gross-up,
FBT rate and per-car FBT are not ported. Code and this README: AGPL-3.0-only; `rules.json`: OA
Guide License v1.0, following this repository's licensing policy.

General reference and computational support only. Obtain qualified professional review before
lodging, paying or relying on any result.
