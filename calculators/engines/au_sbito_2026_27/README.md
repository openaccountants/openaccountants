# au_sbito_2026_27

Australia 2026-27 small business income tax offset for an individual resident: 16% of the tax on net small business income, capped at $1,000, aggregated turnover under $5m.

Jurisdiction AU. Tax year 2026-27. Engine version 1.4.0.

This is the same code that answers the compute tool of the OpenAccountants plugin. It is generated from `src/lib/engines/au-sbito-2026-27.ts` in the OpenAccountants platform at commit `c2e3c2b9`; do not edit it here. The compute tool's answer links to this folder (`inspect.code_url`), so anyone can read the code, the figures and the tests behind it and run them again.

## Files

| File | What it is |
|---|---|
| `index.mjs` | The engine as one ES module with no dependencies (Node 20+). Exports `run(facts)`, `spec`, `rules`, `anchors`, `receiptId`, `quoteFound`, `normaliseLines`. |
| `source/` | The TypeScript files bundled into `index.mjs`, unchanged, with their comments. Read these. |
| `rules.json` | The spec and every figure the engine uses, each with the skill, section and line it was quoted from. |
| `cases.json` | 11 test cases with the exact output the engine gives (9 ok, 1 missing_rule, 1 needs_input). |
| `index.test.mjs` | The tests: `node --test calculators/engines/au_sbito_2026_27/`. |

`index.mjs` is the files in `source/` with the types removed and bundled together; the bundler may print numbers in short form (`2e5` is 200,000, `.19` is 0.19).

## Run it

```sh
node --test calculators/engines/au_sbito_2026_27/
```

```js
import { run } from "./calculators/engines/au_sbito_2026_27/index.mjs";
console.log(JSON.stringify(run({"taxable_income":50000,"net_small_business_income":20000,"aggregated_turnover":100000,"tax_year":"2026-27"}), null, 2));
```

To check an answer from the plugin, pass the same facts: `run(facts)` returns the same result, steps and constants, and `receiptId("au_sbito_2026_27", "1.4.0", facts, run(facts))` equals the `receipt.id` it returned.

## Inputs

| Fact | Type | Required | Default | Description |
|---|---|---|---|---|
| `taxable_income` | number | yes |  | AUD (all income less deductions) |
| `net_small_business_income` | number | yes |  | AUD |
| `aggregated_turnover` | number | yes |  | AUD |
| `tax_year` | `2026-27` | yes |  | the tax year the question is about, written YYYY-YY. This engine has figures for 2026-27 only; any other year is refused |

A fact left out takes its default, and the output lists it in `defaults_assumed`. A fact with no default must be given.

## Outputs

`run(facts)` returns one of three statuses:

- `ok`: `headline` (label, value, currency), `lines`, `steps`, `inputs_used`, `constants_used` (every figure used, with its skill line), `assumptions`, `skill_anchors_reproduced`, `notes`, `defaults_assumed`, `tax_year`.
- `missing_rule`: the engine refuses because no OpenAccountants skill serves a figure it would need. It says `what` is missing and `why`, and never guesses.
- `needs_input`: a fact is missing or invalid. It says `what` and returns the `schema` of the facts.

| Line | Unit |
|---|---|
| `basic_income_tax_liability` | AUD |
| `net_sbi_share_of_taxable_income` | fraction |
| `tax_on_net_small_business_income` | AUD |
| `sbito_before_cap` | AUD |
| `sbito` | AUD |

## What it refuses

- Any tax year other than 2026-27 (`missing_rule`). It never applies one year's figures to another year.
- A missing, negative or wrongly typed fact (`needs_input`).

## Figures

Every figure is quoted from an OpenAccountants skill. The skill is the authority on the method; the official source it names is the authority on the number. The exact line each figure was quoted from is its `quote` in [`rules.json`](rules.json), and a daily check in the platform confirms each quoted line is still in the skill as served.

| Name | Value | Skill | Section |
|---|---|---|---|
| `RESIDENT_BRACKETS_2026_27` | `[[0,18200,0],[18200,45000,0.15],[45000,135000,0.3],[135000,190000,0.37],[190000,null,0.45]]` | [au-rates-2026-27](https://www.openaccountants.com/skills/au-rates-2026-27) | Individual income tax / Resident brackets |
| `SBITO_RATE` | `0.16` | [au-rates-2026-27](https://www.openaccountants.com/skills/au-rates-2026-27) | Individual income tax / Offsets and deductions |
| `SBITO_CAP` | `1000` | [au-rates-2026-27](https://www.openaccountants.com/skills/au-rates-2026-27) | Individual income tax / Offsets and deductions |
| `SBITO_TURNOVER_LIMIT` | `5000000` | [au-rates-2026-27](https://www.openaccountants.com/skills/au-rates-2026-27) | Individual income tax / Offsets and deductions |
| `TAX_ON_NET_SBI_METHOD` | `"basic income tax liability x (net small business income / taxable income)"` | [au-individual-return](https://www.openaccountants.com/skills/au-individual-return) | Section 1 -- Quick Reference / Small Business Income Tax Offset (SBITO) [T1]; Section 4 -- Worked Examples / Example 1 -- Standard Sole Trader (Graphic Designer) |

Skills behind it: [au-rates-2026-27](https://www.openaccountants.com/skills/au-rates-2026-27), [au-individual-return](https://www.openaccountants.com/skills/au-individual-return).

## Worked examples it reproduces

- au-individual-return Example 1: tax $15,070, business 100% of income -> 16% = $2,411, capped at $1,000

The platform's tests recompute these from the skills' own worked examples (`worked-examples.test.ts`, not published here because it calls the engine's internal helpers).

## Licence

Code (`index.mjs`, `index.test.mjs`, `source/`): AGPL-3.0-only, like every calculator in this repository. Figures and wording in `rules.json`: the OpenAccountants Guide License v1.0, like the skills. See [LICENSING.md](../../../LICENSING.md).

Source commit: `c2e3c2b9` (OpenAccountants platform, `src/lib/engines`).
