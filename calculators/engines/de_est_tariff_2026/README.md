# de_est_tariff_2026

Germany 2026 income tax from the § 32a EStG tariff on taxable income (zu versteuerndes Einkommen), Grundtarif or splitting. Excludes solidarity surcharge and church tax.

Jurisdiction DE. Tax year 2026. Engine version 1.2.0.

This is the same code that answers the compute tool of the OpenAccountants plugin. It is generated from `src/lib/engines/de-est-tariff-2026.ts` in the OpenAccountants platform at commit `c2e3c2b9`; do not edit it here. The compute tool's answer links to this folder (`inspect.code_url`), so anyone can read the code, the figures and the tests behind it and run them again.

## Files

| File | What it is |
|---|---|
| `index.mjs` | The engine as one ES module with no dependencies (Node 20+). Exports `run(facts)`, `spec`, `rules`, `anchors`, `receiptId`, `quoteFound`, `normaliseLines`. |
| `source/` | The TypeScript files bundled into `index.mjs`, unchanged, with their comments. Read these. |
| `rules.json` | The spec and every figure the engine uses, each with the skill, section and line it was quoted from. |
| `cases.json` | 24 test cases with the exact output the engine gives (21 ok, 1 missing_rule, 2 needs_input). |
| `index.test.mjs` | The tests: `node --test calculators/engines/de_est_tariff_2026/`. |

`index.mjs` is the files in `source/` with the types removed and bundled together; the bundler may print numbers in short form (`2e5` is 200,000, `.19` is 0.19).

## Run it

```sh
node --test calculators/engines/de_est_tariff_2026/
```

```js
import { run } from "./calculators/engines/de_est_tariff_2026/index.mjs";
console.log(JSON.stringify(run({"taxable_income_zve":50000,"assessment":"single","tax_year":"2026"}), null, 2));
```

To check an answer from the plugin, pass the same facts: `run(facts)` returns the same result, steps and constants, and `receiptId("de_est_tariff_2026", "1.2.0", facts, run(facts))` equals the `receipt.id` it returned.

## Inputs

| Fact | Type | Required | Default | Description |
|---|---|---|---|---|
| `taxable_income_zve` | number | yes |  | EUR |
| `assessment` | `single`, `joint` | yes |  | single (Grundtarif) or joint (splitting) |
| `tax_year` | `2026` | yes |  | the tax year the question is about. This engine has figures for 2026 only; any other year is refused |

A fact left out takes its default, and the output lists it in `defaults_assumed`. A fact with no default must be given.

## Outputs

`run(facts)` returns one of three statuses:

- `ok`: `headline` (label, value, currency), `lines`, `steps`, `inputs_used`, `constants_used` (every figure used, with its skill line), `assumptions`, `skill_anchors_reproduced`, `notes`, `defaults_assumed`, `tax_year`.
- `missing_rule`: the engine refuses because no OpenAccountants skill serves a figure it would need. It says `what` is missing and `why`, and never guesses.
- `needs_input`: a fact is missing or invalid. It says `what` and returns the `schema` of the facts.

| Line | Unit |
|---|---|
| `zve` | EUR (whole euros) |
| `zone` | tariff zone 1-5 |
| `income_tax` | EUR (whole euros) |

## What it refuses

- Any tax year other than 2026 (`missing_rule`). It never applies one year's figures to another year.
- A missing, negative or wrongly typed fact (`needs_input`).

## Figures

Every figure is quoted from an OpenAccountants skill. The skill is the authority on the method; the official source it names is the authority on the number. The exact line each figure was quoted from is its `quote` in [`rules.json`](rules.json), and a daily check in the platform confirms each quoted line is still in the skill as served.

| Name | Value | Skill | Section |
|---|---|---|---|
| `ZONE1_GRUNDFREIBETRAG` | `12348` | [germany-income-tax](https://www.openaccountants.com/skills/germany-income-tax) | Rates, bands and thresholds |
| `ZONE2` | `{"top":17799,"a":"914.51","b":"1400"}` | [germany-income-tax](https://www.openaccountants.com/skills/germany-income-tax) | Rates, bands and thresholds |
| `ZONE3` | `{"top":69878,"a":"173.10","b":"2397","c":"1034.87"}` | [germany-income-tax](https://www.openaccountants.com/skills/germany-income-tax) | Rates, bands and thresholds |
| `ZONE4` | `{"top":277825,"r":"0.42","c":"11135.63"}` | [germany-income-tax](https://www.openaccountants.com/skills/germany-income-tax) | Rates, bands and thresholds |
| `ZONE5` | `{"r":"0.45","c":"19470.38"}` | [germany-income-tax](https://www.openaccountants.com/skills/germany-income-tax) | Rates, bands and thresholds |
| `ROUNDING` | `"floor x and tax to whole euros"` | [germany-income-tax](https://www.openaccountants.com/skills/germany-income-tax) | Rates, bands and thresholds |
| `SPLITTING` | `"2 x tariff(x/2)"` | [germany-income-tax](https://www.openaccountants.com/skills/germany-income-tax) | Rates, bands and thresholds |

Skills behind it: [germany-income-tax](https://www.openaccountants.com/skills/germany-income-tax).

## Worked examples it reproduces

- germany-income-tax Example 1: zvE EUR 49,844 -> EUR 10,493
- Example 2: zvE EUR 79,964 -> EUR 22,449

The platform's tests recompute these from the skills' own worked examples (`worked-examples.test.ts`, not published here because it calls the engine's internal helpers).

## Licence

Code (`index.mjs`, `index.test.mjs`, `source/`): AGPL-3.0-only, like every calculator in this repository. Figures and wording in `rules.json`: the OpenAccountants Guide License v1.0, like the skills. See [LICENSING.md](../../../LICENSING.md).

Source commit: `c2e3c2b9` (OpenAccountants platform, `src/lib/engines`).
