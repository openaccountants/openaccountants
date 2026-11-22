# Australian base rate entity and company tax rate

For one income year, is the company a base rate entity, and is its tax rate 25% or 30%? From
the previous year's figures, at what rate does it frank distributions, and what is the maximum
franking credit?

This is an offline preparation aid for income years 2021-22 to 2026-27. It applies the base rate
entity test to figures the caller has established; it does not work out aggregated turnover,
classify income or compute tax payable.

```js
import { assessBaseRateEntity } from "./index.mjs";

const result = assessBaseRateEntity({
  incomeYear: "2026-27",
  entityType: "company",
  aggregatedTurnover: "30000000",
  assessableIncome: "30000000",
  baseRateEntityPassiveIncome: "1000",
  previousYear: { existed: true, aggregatedTurnover: "55000000", assessableIncome: "30000000", baseRateEntityPassiveIncome: "1000" },
});
// verdict: "rate_calculated"
// baseRateEntity: true; companyTaxRatePercent: 25
// imputation: { basis: "previous_year_figures", limbs: { passiveIncome: true, aggregatedTurnover: false },
//   corporateTaxRateForImputationPurposesPercent: 30, maximumFrankingCredit: { numerator: 3, denominator: 7 } }
```

## Inputs and scope

Amounts are dollar strings with up to 2 decimal places (`"1250000"` or `"1250000.00"`). Numbers,
negative amounts, separators and exponents are rejected. Each figure is required: a missing or
malformed one gives `unknown` and no rate.

| Input | Required meaning |
| --- | --- |
| `incomeYear` | `"YYYY-YY"`, from 2021-22 to 2026-27 |
| `entityType` | `"company"`: a company, not acting as a trustee, to which only s 23(2) of the Income Tax Rates Act 1986 applies |
| `aggregatedTurnover` | This year's aggregated turnover under ITAA 1997 s 328-115, with connected entities and affiliates, worked out as at the end of the year |
| `assessableIncome` | This year's assessable income |
| `baseRateEntityPassiveIncome` | The part of it that is base rate entity passive income (Rates Act s 23AB), traced through trusts and partnerships; no more than `assessableIncome` |
| `previousYear` | Optional. `{ existed: false }` if the company did not exist in the previous income year; otherwise `existed: true` and that year's 3 figures, as above |

Refused, by `entityType`: `company_as_trustee` (s 23(1)), `rsa_provider` (s 23(3)),
`pooled_development_fund` (s 23(4) and (5)), `life_insurance_company` (s 23A), `non_profit_company`
(s 23(6)), `recognised_medium_credit_union` (s 23(7)) and `public_trading_trust` (s 25). A
non-profit company's or recognised medium credit union's rate is still 25% or 30% under s 23(2),
but s 23(6) or (7) caps its tax, which this calculator does not apply. Income
years before 2021-22, when the base rate entity rate was 27.5% or 26%, and after 2026-27 are
refused.

## Calculation

A company is a base rate entity when both limbs of Rates Act s 23AA are met: base rate entity
passive income is no more than 80% of assessable income (paragraph (a)), and aggregated turnover is
less than $50 million (paragraph (b)). Exactly 80% passes and exactly $50 million fails. Nil
assessable income with nil passive income passes paragraph (a), as LCR 2019/5 Example 2.2 (Swan
Co) concludes. The comparison is exact to the cent; no percentage is rounded. A base rate entity's rate is 25% and
any other covered company's 30% (s 23(2)).

The corporate tax rate for imputation purposes (ITAA 1997 s 995-1) runs the same test on the
previous year's 3 figures against this year's law, or is 25% when the company did not exist in
the previous year. It is never taken from this year's result: without `previousYear` the result
has `imputation: null` and the reason `previous_year_not_supplied`. The maximum franking credit
(s 202-60(2)) is the frankable distribution times `numerator / denominator`: 1/3 at 25% and 3/7 at
30%. Multiply and round as your franking records require; s 202-65 limits a stated credit to that
maximum.

## Outputs and limits

Results include the verdict (`rate_calculated`, `unknown` or `refused`), reason codes, reasons,
sources, the covered years and the limits. `limbs` shows which limb failed. `unknown` and `refused`
results contain **no rate**. Tax payable, offsets, the franking account, the benchmark rule and
franking deficit tax are not computed.

The Income Tax Rates Act 1986 (Compilation No. 66, in force 1 July 2026), ITAA 1997 ss 202-60,
328-115 and 995-1, LCR 2019/5 and the ATO's company tax rate (last updated 4 September 2026) and
franking credit pages were read on 18 November 2026; the sources are in [rules.json](rules.json). Review
later amendments before relying on a result. No runtime network or clock is consulted.

## Verification and provenance

Run `node --test calculators/au-base-rate-entity/` from the repository root on Node 20+ with JSON
import attributes; From the repository root, run `node --test calculators/*/index.test.mjs` to run every calculator suite. Tests reproduce the ATO's 5 base rate
entity examples, Dillmore Manufacture's imputation rate, LCR 2019/5's Swan Co, the
`au-company-tax` guide's Examples 1 and 4 and Test 6, both limbs' boundaries to the cent, and
refusals of missing, malformed and out-of-scope inputs. Other figures are invented; no client data is used.

The rules were adapted from Ryan Duguid's independently authored company tax calculator in
[ryanduguid.github.io](https://github.com/ryanduguid/ryanduguid.github.io/blob/4b7cfc9790b5914dfd77b40b7a704ff80f85f2c4/assets/company-tax.mjs)
at revision `4b7cfc9790b5914dfd77b40b7a704ff80f85f2c4`. Its tax amount, franking credit amounts and
shareholder tax are not ported. Code and this README: AGPL-3.0-only; `rules.json`: OA Guide License
v1.0, following this repository's licensing policy.

General reference and computational support only. Obtain qualified professional review before
filing, franking or relying on any result.
