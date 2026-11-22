# ATO small business benchmarks comparison, 2023-24

Where do a business's tax return ratios sit against the ATO's small business benchmark ranges for
its industry and turnover?

This is an offline preparation aid. It applies the ATO's ratio rules to whole-dollar tax return
amounts, picks the industry's turnover band and says whether each ratio is below, within or above
the published range. It is a comparison, not a finding: the ATO uses the benchmarks with other
risk indicators and says 'We never use the benchmarks in isolation when deciding to review a
business or when looking at the business's records.'

```js
import { compareWithAtoBenchmarks } from "./index.mjs";

const result = compareWithAtoBenchmarks({
  benchmarkYear: "2023-24",
  industry: "Coffee shops",
  totalBusinessIncome: 705200,
  costOfSales: 253300,
  salaryAndWagesInCostOfSales: false,
  totalExpenses: 675500,
  paymentsToAssociatedPersons: 50000,
});
// verdict: "compared"
// band: { label: "More than $600,000", from: 600001, to: null }
// keyRatio: "cost_of_sales"
// ratios[0]: { ratio: "total_expenses", key: false, amount: 625500, percent: 88.7, range: { min: 86, max: 93 }, position: "within" }
// ratios[1]: { ratio: "cost_of_sales", key: true, amount: 253300, percent: 35.92, range: { min: 33, max: 38 }, position: "within" }
```

## Inputs

Amounts are whole dollars, 0 or more, as reported on the tax return. Each ratio is compared only
when every amount it needs is supplied.

| Input | Meaning |
| --- | --- |
| `benchmarkYear` | `2023-24`, the only year held |
| `industry` | The industry name exactly as a key of `industries` in [ato-pages-2023-24.json](ato-pages-2023-24.json) (99 industries) |
| `totalBusinessIncome` | Required, more than 0 |
| `salesOfGoodsAndServices` | Optional; omitted means blank |
| `totalExpenses`, `paymentsToAssociatedPersons` | Total expenses ratio; payments to associated persons also feed labour |
| `costOfSales`, `salaryAndWagesInCostOfSales` | Cost of sales ratio; the boolean is `true` where the total salary and wages code is C |
| `totalSalaryAndWages` | Labour, and cost of sales where the code is C |
| `contractorExpenses`, `w1` | Labour; `w1` is the activity statements' W1 for the year, optional |
| `rentExpenses`, `motorVehicleExpenses` | Rent and motor vehicle ratios |

[rules.json](rules.json) lists each amount's tax return labels for companies, partnerships and
trusts, and individuals, as the ATO gives them.

## Calculation

The ATO's 'How we calculate benchmark ratios' (QC81799) sets the rules:

- Turnover is sales of goods and services, or total business income where sales are blank, zero
  or less than 50% of it. Sales of exactly half count.
- Total expenses is total expenses minus payments to associated persons.
- Cost of sales excludes salary and wages: where the code is C, total salary and wages come out.
- Labour is total salary and wages plus contractor, subcontractor and commission expenses, minus
  payments to associated persons; W1 replaces total salary and wages where it is greater.
- Rent and motor vehicle are the expense amounts.

Each ratio is the amount divided by turnover. `percent` shows it to 2 places, half up, as the
ATO's examples do (35.92%), and `position` compares that figure with the published bounds,
inclusive, as those examples compare 88.70% with 86% to 93%. The ATO publishes whole percentages
and says nothing more about rounding, so this convention is the calculator's own: 86.004% shows
as 86% and is within a range ending at 86%; 86.01% is above it. A range printed as a single
figure, such as 1%, is both bounds, so only a ratio that rounds to 1.00% (0.995% up to but not
including 1.005%) is within it. 35 ranges are single figures, all motor vehicle: 29 of 1%, 1 of 2%
and 5 of 0%. A 0% range holds only ratios under 0.005% of turnover.

The band is the one whose printed limits contain turnover: '$400,001 - $750,000' starts at
$400,001, and 'More than $750,000' at $750,001. Turnover below the lowest band is refused.

The key range is the one the industry's page names. Where it is cost of sales and no cost of
sales is reported (omitted or 0), total expenses becomes the key range, as the ATO directs. The
ATO also says to switch where cost of sales is 'only a small amount' but does not say how small.
This calculator assumes that any cost of sales above 0 keeps the cost of sales key range; that
assumption is its own, not the ATO's. It shows both ratios and the reason code
`cost_of_sales_small_unquantified`, leaving the judgement to the reader.

## Outputs and limits

Results include the verdict, reason codes, reasons, turnover and its basis, the band, the key
ratio, each ratio's amount, percentage, range and position (`below`, `within`, `above`,
`no_published_range` or `not_supplied`), the ATO's own words on what each position may mean,
the attribution, sources and limits. `refused` and `unknown` results contain no comparison.

Refused: any year other than 2023-24, an industry the ATO does not publish, and turnover below the
industry's lowest band. Hardware and building supplies retailing is refused because its industry
page and the dataset give different cost of sales ranges for $400,001 to $1,000,000.

The industry is the caller's choice; the ATO allocates a business by its industry code, main
business activity and trading name. Where total business income or total expenses is blank or
incomplete, the ATO sums other labels, and the caller must supply that sum. The ATO's averages
and the activity statement benchmarks, not produced since 1 July 2017, are not used.

## Data and verification

The 2023-24 benchmarks are the ATO's most current set: 'Performance benchmarks use information
reported on tax returns for the 2023–24 financial year'. The industry pages were last updated on
16 March 2026. Total expenses and cost of sales key ranges come from the ATO's data.gov.au
dataset (2023-24 resource, SHA-256 in [benchmarks-2023-24.json](benchmarks-2023-24.json)); labour, rent, motor vehicle and
non-key cost of sales ranges are copied from each industry's page. Every page's key ranges and
turnover bands were checked against the dataset. All were read on 18 November 2026. No runtime
network or clock is consulted.

Run `node --test calculators/au-ato-benchmarks/` from the repository root on Node 20+ with JSON
import attributes; From the repository root, run `node --test calculators/*/index.test.mjs` to run every calculator suite. Tests cover the ATO's 4 worked
examples (Elizabeth's coffee shop, Robert's plumbing business before and after correction,
Belinda's footwear business and Steff's 30.21%), the bakery page's published ranges, band edges,
the 50% turnover rule, each ratio's deductions, range bounds, the key range fallback, the shape of
every industry's data and refusals of malformed or out-of-scope inputs. No client data is used.

## Data licence

The ATO's benchmark ranges and the ATO guidance this calculator quotes are © Australian Taxation
Office for the Commonwealth of Australia. They sit in 2 files because the ATO released them on 2
sets of terms, and each file stays on its own terms, not under this repository's other licences.

- [benchmarks-2023-24.json](benchmarks-2023-24.json): the turnover bands, the total expenses
  ranges and the key cost of sales ranges, adapted from the ATO's
  [Small Business Benchmarks](https://data.gov.au/data/dataset/small-business-benchmarks) dataset
  (2023-24 Benchmarks), licensed under
  [Creative Commons Attribution 2.5 Australia](https://creativecommons.org/licenses/by/2.5/au/)
  ([LICENSES/CC-BY-2.5-AU.txt](../../LICENSES/CC-BY-2.5-AU.txt)).
- [ato-pages-2023-24.json](ato-pages-2023-24.json): the labour, rent, motor vehicle and other cost
  of sales ranges, the page numbers, each industry's key range and the guidance text, taken from
  the ATO's
  [industry benchmark pages](https://www.ato.gov.au/businesses-and-organisations/income-deductions-and-concessions/small-business-benchmarks/benchmarks-a-z)
  and guidance pages under the ATO's
  [copyright notice](https://www.ato.gov.au/about-ato/using-our-website/copyright-notice)
  ([LICENSES/LicenseRef-ATO-Copyright-Notice.txt](../../LICENSES/LicenseRef-ATO-Copyright-Notice.txt)),
  which lets anyone copy, adapt, modify, transmit and distribute them.

Both are arranged as JSON, with percentages as whole numbers; `index.mjs` joins them by industry
and band.

This README and `index.test.mjs` also quote the ATO's guidance, its worked examples (Elizabeth,
Robert, Belinda and Steff) and the ranges those examples and the bakery page print, © Australian
Taxation Office for the Commonwealth of Australia, from the pages cited, under the same copyright
notice.

The rules were adapted from Ryan Duguid's independently authored
[ato-benchmark-compare](https://github.com/ryanduguid/australian-accounting/tree/main/packages/ato-benchmark-compare)
at revision `2e41b018a5a1c5229df2b3fe29de1fe716311fe9`. Code and this README: AGPL-3.0-only;
`rules.json`: OA Guide License v1.0, following this repository's licensing policy;
`benchmarks-2023-24.json` and `ato-pages-2023-24.json`: the ATO's terms, as above.

General reference and computational support only. Obtain qualified professional review before
lodging, paying or relying on any result.
