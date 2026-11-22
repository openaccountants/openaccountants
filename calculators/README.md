# Calculators

OpenAccountants calculations run on our servers, through the `compute` tool of the OpenAccountants plugin. Their code is not published here.

## Lines the calculations rely on

[`quoted-lines.json`](quoted-lines.json) lists, for every figure an OpenAccountants calculation uses, the skill it comes from, the section and the skill's own words. The calculation refuses to run when its skill no longer states that line, so `scripts/check-calculator-quotes.py` fails a pull request that drops or rewords one. Keep each line word for word when you edit its skill, or ask for the calculation to be updated first.

## Contributed checks

| Calculator | Question | Skills behind it |
|---|---|---|
| [`au-div7a-repayment`](au-div7a-repayment/) | For an existing complying amalgamated loan, do the supplied repayments cover the minimum yearly repayment formula? | `au-div7a`; ITAA 1936 ss 109E, 109N and 109R |
| [`au-payg-withholding`](au-payg-withholding/) | What should be withheld for a supported Australian pay, net-pay gross-up or current-year back payment? | `australia-payroll`; ATO PAYG withholding schedules |
| [`au-fhss`](au-fhss/) | How do eligible contributions and deemed earnings affect an FHSS release estimate? | `au-fhss`; Taxation Administration Act 1953 Sch 1 Div 138 |

## Australian fork worksheet imports

These standalone worksheets run locally. Each README lists supported inputs, authorities and limitations.

| Worksheet | Use |
| --- | --- |
| [`au-ato-benchmarks`](au-ato-benchmarks/) | Compare a small business with its applicable ATO benchmark range. |
| [`au-base-rate-entity`](au-base-rate-entity/) | Check the base rate entity conditions and calculate company tax. |
| [`au-contribution-caps`](au-contribution-caps/) | Check supported concessional and non-concessional contribution caps. |
| [`au-division-293`](au-division-293/) | Estimate Division 293 tax for supported income and contributions. |
| [`au-division-296`](au-division-296/) | Estimate member-level Division 296 tax within the supported scope. |
| [`au-fbt-car-taxable-value`](au-fbt-car-taxable-value/) | Estimate a car fringe benefit under the supported statutory formula. |
| [`au-lodgment-due-dates`](au-lodgment-due-dates/) | Find supported lodgment dates for Australian obligations. |
| [`au-payday-super-timing`](au-payday-super-timing/) | Check payment timing for supported super guarantee cases. |
| [`au-super-guarantee-charge`](au-super-guarantee-charge/) | Estimate the super guarantee charge within the supported scope. |
