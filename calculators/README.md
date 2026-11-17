# Calculators

OpenAccountants calculations run on our servers, through the `compute` tool of the OpenAccountants plugin. Their code is not published here.

## Lines the calculations rely on

[`quoted-lines.json`](quoted-lines.json) lists, for every figure an OpenAccountants calculation uses, the skill it comes from, the section and the skill's own words. The calculation refuses to run when its skill no longer states that line, so `scripts/check-calculator-quotes.py` fails a pull request that drops or rewords one. Keep each line word for word when you edit its skill, or ask for the calculation to be updated first.

## Contributed checks

| Calculator | Question | Skills behind it |
|---|---|---|
| [`au-div7a-repayment`](au-div7a-repayment/) | For an existing complying amalgamated loan, do the supplied repayments cover the minimum yearly repayment formula? | `au-div7a`; ITAA 1936 ss 109E, 109N and 109R |
