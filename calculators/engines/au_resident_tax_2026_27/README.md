# au_resident_tax_2026_27

Australia, resident for the full 2026-27 year: income tax on taxable income less LITO, plus 2% Medicare levy, plus MLS check; take-home = gross income less those.

Jurisdiction AU. Tax year 2026-27. Engine version 1.4.0.

This is the same code that answers the compute tool of the OpenAccountants plugin. It is generated from `src/lib/engines/au-resident-tax-2026-27.ts` in the OpenAccountants platform at commit `c2e3c2b9`; do not edit it here. The compute tool's answer links to this folder (`inspect.code_url`), so anyone can read the code, the figures and the tests behind it and run them again.

## Files

| File | What it is |
|---|---|
| `index.mjs` | The engine as one ES module with no dependencies (Node 20+). Exports `run(facts)`, `spec`, `rules`, `anchors`, `receiptId`, `quoteFound`, `normaliseLines`. |
| `source/` | The TypeScript files bundled into `index.mjs`, unchanged, with their comments. Read these. |
| `rules.json` | The spec and every figure the engine uses, each with the skill, section and line it was quoted from. |
| `cases.json` | 23 test cases with the exact output the engine gives (17 ok, 4 missing_rule, 2 needs_input). |
| `index.test.mjs` | The tests: `node --test calculators/engines/au_resident_tax_2026_27/`. |

`index.mjs` is the files in `source/` with the types removed and bundled together; the bundler may print numbers in short form (`2e5` is 200,000, `.19` is 0.19).

## Run it

```sh
node --test calculators/engines/au_resident_tax_2026_27/
```

```js
import { run } from "./calculators/engines/au_resident_tax_2026_27/index.mjs";
console.log(JSON.stringify(run({"gross_income":100000,"has_private_hospital_cover":true,"has_help_debt":false,"has_salary_or_wage_income":true,"tax_year":"2026-27"}), null, 2));
```

To check an answer from the plugin, pass the same facts: `run(facts)` returns the same result, steps and constants, and `receiptId("au_resident_tax_2026_27", "1.4.0", facts, run(facts))` equals the `receipt.id` it returned.

## Inputs

| Fact | Type | Required | Default | Description |
|---|---|---|---|---|
| `gross_income` | number | yes |  | AUD (salary etc.) |
| `other_deductions` | number | no | `0` | AUD |
| `has_salary_or_wage_income` | boolean | yes |  | does the person earn salary or wages (labour income)? The engine then applies the $1,000 standard work deduction top-up itself |
| `labour_income` | number | no |  | AUD qualifying labour income (salary and wages) within gross_income; business or PSI income does not count. Taken as gross_income when not given |
| `actual_work_expenses_claimed` | number | no | `0` | work-related expenses the person chooses to claim with records |
| `has_private_hospital_cover` | boolean | yes |  | private patient hospital cover for the full year |
| `has_help_debt` | boolean | no | `false` | HELP (study loan) debt |
| `tax_year` | `2026-27` | yes |  | the tax year the question is about, written YYYY-YY. This engine has figures for 2026-27 only; any other year is refused |

A fact left out takes its default, and the output lists it in `defaults_assumed`. A fact with no default must be given.

## Outputs

`run(facts)` returns one of three statuses:

- `ok`: `headline` (label, value, currency), `lines`, `steps`, `inputs_used`, `constants_used` (every figure used, with its skill line), `assumptions`, `skill_anchors_reproduced`, `notes`, `defaults_assumed`, `tax_year`.
- `missing_rule`: the engine refuses because no OpenAccountants skill serves a figure it would need. It says `what` is missing and `why`, and never guesses.
- `needs_input`: a fact is missing or invalid. It says `what` and returns the `schema` of the facts.

| Line | Unit |
|---|---|
| `taxable_income` | AUD |
| `gross_tax` | AUD |
| `lito` | AUD |
| `income_tax_after_offsets` | AUD |
| `medicare_levy` | AUD |
| `medicare_levy_surcharge` | AUD |
| `income_tax_plus_medicare` | AUD |
| `take_home_pay` | AUD |

## What it refuses

- Any tax year other than 2026-27 (`missing_rule`). It never applies one year's figures to another year.
- A missing, negative or wrongly typed fact (`needs_input`).
- Medicare levy reduction in the low-income range (`missing_rule`)
- MLS 2026-27 tiers (`missing_rule`)
- HELP repayment 2026-27 thresholds (`missing_rule`)

## Figures

Every figure is quoted from an OpenAccountants skill. The skill is the authority on the method; the official source it names is the authority on the number. The exact line each figure was quoted from is its `quote` in [`rules.json`](rules.json), and a daily check in the platform confirms each quoted line is still in the skill as served.

| Name | Value | Skill | Section |
|---|---|---|---|
| `RESIDENT_BRACKETS_2026_27` | `[[0,18200,0],[18200,45000,0.15],[45000,135000,0.3],[135000,190000,0.37],[190000,null,0.45]]` | [au-rates-2026-27](https://www.openaccountants.com/skills/au-rates-2026-27) | Individual income tax / Resident brackets |
| `LITO` | `{"max":700,"t1":37500,"taper1":0.05,"t2":45000,"taper2":0.015,"nil_at":66667}` | [au-rates-2026-27](https://www.openaccountants.com/skills/au-rates-2026-27) | Individual income tax / Offsets and deductions |
| `MEDICARE_LEVY_RATE` | `0.02` | [au-rates-2026-27](https://www.openaccountants.com/skills/au-rates-2026-27) | Medicare |
| `MEDICARE_LOW_INCOME_SINGLE_2026_27` | `[28011,35013]` | [au-rates-2026-27](https://www.openaccountants.com/skills/au-rates-2026-27) | Medicare |
| `MLS_BASE_TIER_SINGLE` | `101000` | [au-rates-2026-27](https://www.openaccountants.com/skills/au-rates-2026-27) | Medicare |
| `STANDARD_WRE_DEDUCTION` | `1000` | [au-rates-2026-27](https://www.openaccountants.com/skills/au-rates-2026-27) | Individual income tax / Offsets and deductions |

Skills behind it: [au-rates-2026-27](https://www.openaccountants.com/skills/au-rates-2026-27).

## Worked examples it reproduces

- Tax on full bands 2026-27: $4,020 / $31,020 / $51,370
- au-deductions-offsets example: TI $88,340 -> gross tax $17,022, Medicare $1,766.80
- LITO nil at $66,667

The platform's tests recompute these from the skills' own worked examples (`worked-examples.test.ts`, not published here because it calls the engine's internal helpers).

## Licence

Code (`index.mjs`, `index.test.mjs`, `source/`): AGPL-3.0-only, like every calculator in this repository. Figures and wording in `rules.json`: the OpenAccountants Guide License v1.0, like the skills. See [LICENSING.md](../../../LICENSING.md).

Source commit: `c2e3c2b9` (OpenAccountants platform, `src/lib/engines`).
