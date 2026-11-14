# nl_vpb_2026

Netherlands corporate income tax (vennootschapsbelasting) for 2026 on a BV/NV's taxable amount (after loss offset and exemptions).

Jurisdiction NL. Tax year 2026. Engine version 1.2.0.

This is the same code that answers the compute tool of the OpenAccountants plugin. It is generated from `src/lib/engines/nl-vpb-2026.ts` in the OpenAccountants platform at commit `c2e3c2b9`; do not edit it here. The compute tool's answer links to this folder (`inspect.code_url`), so anyone can read the code, the figures and the tests behind it and run them again.

## Files

| File | What it is |
|---|---|
| `index.mjs` | The engine as one ES module with no dependencies (Node 20+). Exports `run(facts)`, `spec`, `rules`, `anchors`, `receiptId`, `quoteFound`, `normaliseLines`. |
| `source/` | The TypeScript files bundled into `index.mjs`, unchanged, with their comments. Read these. |
| `rules.json` | The spec and every figure the engine uses, each with the skill, section and line it was quoted from. |
| `cases.json` | 14 test cases with the exact output the engine gives (10 ok, 1 missing_rule, 3 needs_input). |
| `index.test.mjs` | The tests: `node --test calculators/engines/nl_vpb_2026/`. |

`index.mjs` is the files in `source/` with the types removed and bundled together; the bundler may print numbers in short form (`2e5` is 200,000, `.19` is 0.19).

## Run it

```sh
node --test calculators/engines/nl_vpb_2026/
```

```js
import { run } from "./calculators/engines/nl_vpb_2026/index.mjs";
console.log(JSON.stringify(run({"taxable_amount":800000,"tax_year":"2026"}), null, 2));
```

To check an answer from the plugin, pass the same facts: `run(facts)` returns the same result, steps and constants, and `receiptId("nl_vpb_2026", "1.2.0", facts, run(facts))` equals the `receipt.id` it returned.

## Inputs

| Fact | Type | Required | Default | Description |
|---|---|---|---|---|
| `taxable_amount` | number | yes |  | EUR, taxable amount after losses/participation exemption/innovation box |
| `tax_year` | `2026` | yes |  | the tax year the question is about. This engine has figures for 2026 only; any other year is refused |

A fact left out takes its default, and the output lists it in `defaults_assumed`. A fact with no default must be given.

## Outputs

`run(facts)` returns one of three statuses:

- `ok`: `headline` (label, value, currency), `lines`, `steps`, `inputs_used`, `constants_used` (every figure used, with its skill line), `assumptions`, `skill_anchors_reproduced`, `notes`, `defaults_assumed`, `tax_year`.
- `missing_rule`: the engine refuses because no OpenAccountants skill serves a figure it would need. It says `what` is missing and `why`, and never guesses.
- `needs_input`: a fact is missing or invalid. It says `what` and returns the `schema` of the facts.

| Line | Unit |
|---|---|
| `tax_at_19pct` | EUR |
| `tax_at_25_8pct` | EUR |
| `vpb_total` | EUR |
| `effective_rate` | fraction |

## What it refuses

- Any tax year other than 2026 (`missing_rule`). It never applies one year's figures to another year.
- A missing, negative or wrongly typed fact (`needs_input`).

## Figures

Every figure is quoted from an OpenAccountants skill. The skill is the authority on the method; the official source it names is the authority on the number. The exact line each figure was quoted from is its `quote` in [`rules.json`](rules.json), and a daily check in the platform confirms each quoted line is still in the skill as served.

| Name | Value | Skill | Section |
|---|---|---|---|
| `BRACKET` | `200000` | [nl-corporate-tax](https://www.openaccountants.com/skills/nl-corporate-tax) | Rates, bands and thresholds |
| `LOW_RATE` | `0.19` | [nl-corporate-tax](https://www.openaccountants.com/skills/nl-corporate-tax) | Rates, bands and thresholds |
| `HIGH_RATE` | `0.258` | [nl-corporate-tax](https://www.openaccountants.com/skills/nl-corporate-tax) | Rates, bands and thresholds |

Skills behind it: [nl-corporate-tax](https://www.openaccountants.com/skills/nl-corporate-tax).

## Worked examples it reproduces

- Rates table: tax at EUR 200,000 = EUR 38,000
- Example 1: EUR 425,000 -> EUR 96,050
- Example 2: EUR 2,020,000 -> EUR 507,560

The platform's tests recompute these from the skills' own worked examples (`worked-examples.test.ts`, not published here because it calls the engine's internal helpers).

## Licence

Code (`index.mjs`, `index.test.mjs`, `source/`): AGPL-3.0-only, like every calculator in this repository. Figures and wording in `rules.json`: the OpenAccountants Guide License v1.0, like the skills. See [LICENSING.md](../../../LICENSING.md).

Source commit: `c2e3c2b9` (OpenAccountants platform, `src/lib/engines`).
