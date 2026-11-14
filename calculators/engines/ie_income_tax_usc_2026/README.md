# ie_income_tax_usc_2026

Ireland 2026: income tax (after personal + PAYE credits) and USC for a single PAYE employee for the full year, cumulative basis.

Jurisdiction IE. Tax year 2026. Engine version 1.2.0.

This is the same code that answers the compute tool of the OpenAccountants plugin. It is generated from `src/lib/engines/ie-income-tax-usc-2026.ts` in the OpenAccountants platform at commit `c2e3c2b9`; do not edit it here. The compute tool's answer links to this folder (`inspect.code_url`), so anyone can read the code, the figures and the tests behind it and run them again.

## Files

| File | What it is |
|---|---|
| `index.mjs` | The engine as one ES module with no dependencies (Node 20+). Exports `run(facts)`, `spec`, `rules`, `anchors`, `receiptId`, `quoteFound`, `normaliseLines`. |
| `source/` | The TypeScript files bundled into `index.mjs`, unchanged, with their comments. Read these. |
| `rules.json` | The spec and every figure the engine uses, each with the skill, section and line it was quoted from. |
| `cases.json` | 17 test cases with the exact output the engine gives (13 ok, 3 missing_rule, 1 needs_input). |
| `index.test.mjs` | The tests: `node --test calculators/engines/ie_income_tax_usc_2026/`. |

`index.mjs` is the files in `source/` with the types removed and bundled together; the bundler may print numbers in short form (`2e5` is 200,000, `.19` is 0.19).

## Run it

```sh
node --test calculators/engines/ie_income_tax_usc_2026/
```

```js
import { run } from "./calculators/engines/ie_income_tax_usc_2026/index.mjs";
console.log(JSON.stringify(run({"gross_pay":60000,"status":"single","tax_year":"2026"}), null, 2));
```

To check an answer from the plugin, pass the same facts: `run(facts)` returns the same result, steps and constants, and `receiptId("ie_income_tax_usc_2026", "1.2.0", facts, run(facts))` equals the `receipt.id` it returned.

## Inputs

| Fact | Type | Required | Default | Description |
|---|---|---|---|---|
| `gross_pay` | number | yes |  | EUR |
| `employee_pension_contribution` | number | no | `0` | EUR (relieved for income tax, not USC) |
| `status` | string | yes |  | single, married, etc. (only single without children is computed; others are refused) |
| `age_70_or_full_medical_card` | boolean | no | `false` | aged 70+ or holds a full medical card |
| `tax_year` | `2026` | yes |  | the tax year the question is about. This engine has figures for 2026 only; any other year is refused |

A fact left out takes its default, and the output lists it in `defaults_assumed`. A fact with no default must be given.

## Outputs

`run(facts)` returns one of three statuses:

- `ok`: `headline` (label, value, currency), `lines`, `steps`, `inputs_used`, `constants_used` (every figure used, with its skill line), `assumptions`, `skill_anchors_reproduced`, `notes`, `defaults_assumed`, `tax_year`.
- `missing_rule`: the engine refuses because no OpenAccountants skill serves a figure it would need. It says `what` is missing and `why`, and never guesses.
- `needs_input`: a fact is missing or invalid. It says `what` and returns the `schema` of the facts.

| Line | Unit |
|---|---|
| `taxable_pay` | EUR |
| `gross_income_tax` | EUR |
| `tax_credits` | EUR |
| `income_tax` | EUR |
| `usc` | EUR |
| `income_tax_plus_usc` | EUR |

## What it refuses

- Any tax year other than 2026 (`missing_rule`). It never applies one year's figures to another year.
- A missing, negative or wrongly typed fact (`needs_input`).
- cut-off and credits for status 'married' (`missing_rule`)
- USC reduced rates engine (`missing_rule`)

## Figures

Every figure is quoted from an OpenAccountants skill. The skill is the authority on the method; the official source it names is the authority on the number. The exact line each figure was quoted from is its `quote` in [`rules.json`](rules.json), and a daily check in the platform confirms each quoted line is still in the skill as served.

| Name | Value | Skill | Section |
|---|---|---|---|
| `INCOME_TAX_RATES` | `[0.2,0.4]` | [ie-payroll](https://www.openaccountants.com/skills/ie-payroll) | Rates, bands and thresholds |
| `CUTOFF_SINGLE` | `44000` | [ie-payroll](https://www.openaccountants.com/skills/ie-payroll) | Rates, bands and thresholds |
| `SINGLE_PERSON_CREDIT` | `2000` | [ie-payroll](https://www.openaccountants.com/skills/ie-payroll) | Rates, bands and thresholds |
| `EMPLOYEE_PAYE_CREDIT` | `2000` | [ie-payroll](https://www.openaccountants.com/skills/ie-payroll) | Rates, bands and thresholds |
| `USC_BANDS` | `[[12012,0.005],[16688,0.02],[41344,0.03],[null,0.08]]` | [ie-payroll](https://www.openaccountants.com/skills/ie-payroll) | Rates, bands and thresholds |
| `USC_EXEMPT_LIMIT` | `13000` | [ie-payroll](https://www.openaccountants.com/skills/ie-payroll) | Rates, bands and thresholds |

Skills behind it: [ie-payroll](https://www.openaccountants.com/skills/ie-payroll).

## Worked examples it reproduces

- ie-payroll Example 1: EUR 5,000/month, EUR 4,750 taxable -> income tax EUR 833.33, USC EUR 111.07 a month

The platform's tests recompute these from the skills' own worked examples (`worked-examples.test.ts`, not published here because it calls the engine's internal helpers).

## Licence

Code (`index.mjs`, `index.test.mjs`, `source/`): AGPL-3.0-only, like every calculator in this repository. Figures and wording in `rules.json`: the OpenAccountants Guide License v1.0, like the skills. See [LICENSING.md](../../../LICENSING.md).

Source commit: `c2e3c2b9` (OpenAccountants platform, `src/lib/engines`).
