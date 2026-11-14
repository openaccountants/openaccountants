# us_se_tax

US self-employment tax (Schedule SE regular method) for tax year 2025 or 2026: 92.35% of net profit, 12.4% social security up to the wage base less W-2 SS wages, 2.9% Medicare uncapped. Excludes the 0.9% Additional Medicare Tax (Form 8959).

Jurisdiction US. Tax years 2025 and 2026. Engine version 1.3.0.

This is the same code that answers the compute tool of the OpenAccountants plugin. It is generated from `src/lib/engines/us-se-tax.ts` in the OpenAccountants platform at commit `c2e3c2b9`; do not edit it here. The compute tool's answer links to this folder (`inspect.code_url`), so anyone can read the code, the figures and the tests behind it and run them again.

## Files

| File | What it is |
|---|---|
| `index.mjs` | The engine as one ES module with no dependencies (Node 20+). Exports `run(facts)`, `spec`, `rules`, `anchors`, `receiptId`, `quoteFound`, `normaliseLines`. |
| `source/` | The TypeScript files bundled into `index.mjs`, unchanged, with their comments. Read these. |
| `rules.json` | The spec and every figure the engine uses, each with the skill, section and line it was quoted from. |
| `cases.json` | 12 test cases with the exact output the engine gives (11 ok, 1 missing_rule, 0 needs_input). |
| `index.test.mjs` | The tests: `node --test calculators/engines/us_se_tax/`. |

`index.mjs` is the files in `source/` with the types removed and bundled together; the bundler may print numbers in short form (`2e5` is 200,000, `.19` is 0.19).

## Run it

```sh
node --test calculators/engines/us_se_tax/
```

```js
import { run } from "./calculators/engines/us_se_tax/index.mjs";
console.log(JSON.stringify(run({"schedule_c_net_profit":120000,"tax_year":"2026"}), null, 2));
```

To check an answer from the plugin, pass the same facts: `run(facts)` returns the same result, steps and constants, and `receiptId("us_se_tax", "1.3.0", facts, run(facts))` equals the `receipt.id` it returned.

## Inputs

| Fact | Type | Required | Default | Description |
|---|---|---|---|---|
| `schedule_c_net_profit` | number | yes |  | USD (total of all Schedule C/F) |
| `w2_social_security_wages` | number | no | `0` | USD |
| `tax_year` | `2025`, `2026` | yes |  | the tax year the question is about. This engine has figures for 2025 and 2026 only; any other year is refused |

A fact left out takes its default, and the output lists it in `defaults_assumed`. A fact with no default must be given.

## Outputs

`run(facts)` returns one of three statuses:

- `ok`: `headline` (label, value, currency), `lines`, `steps`, `inputs_used`, `constants_used` (every figure used, with its skill line), `assumptions`, `skill_anchors_reproduced`, `notes`, `defaults_assumed`, `tax_year`.
- `missing_rule`: the engine refuses because no OpenAccountants skill serves a figure it would need. It says `what` is missing and `why`, and never guesses.
- `needs_input`: a fact is missing or invalid. It says `what` and returns the `schema` of the facts.

| Line | Unit |
|---|---|
| `net_earnings_from_se` | USD |
| `social_security_part` | USD |
| `medicare_part` | USD |
| `se_tax` | USD |
| `deductible_half` | USD |

## What it refuses

- Any tax year other than 2025 and 2026 (`missing_rule`). It never applies one year's figures to another year.
- A missing, negative or wrongly typed fact (`needs_input`).

## Figures

Every figure is quoted from an OpenAccountants skill. The skill is the authority on the method; the official source it names is the authority on the number. The exact line each figure was quoted from is its `quote` in [`rules.json`](rules.json), and a daily check in the platform confirms each quoted line is still in the skill as served.

| Name | Value | Skill | Section |
|---|---|---|---|
| `NET_EARNINGS_FACTOR` | `0.9235` | [us-schedule-c-and-se-computation](https://www.openaccountants.com/skills/us-schedule-c-and-se-computation) | Rates, bands and thresholds |
| `MIN_NET_EARNINGS` | `400` | [us-schedule-c-and-se-computation](https://www.openaccountants.com/skills/us-schedule-c-and-se-computation) | Rates, bands and thresholds |
| `SS_RATE` | `0.124` | [us-schedule-c-and-se-computation](https://www.openaccountants.com/skills/us-schedule-c-and-se-computation) | Rates, bands and thresholds |
| `WAGE_BASE` | `{"2025":176100,"2026":184500}` | [us-tax-workflow-base](https://www.openaccountants.com/skills/us-tax-workflow-base) | Figures for 2026, with years |
| `MEDICARE_RATE` | `0.029` | [us-schedule-c-and-se-computation](https://www.openaccountants.com/skills/us-schedule-c-and-se-computation) | Rates, bands and thresholds |
| `DEDUCTIBLE_SHARE` | `0.5` | [us-schedule-c-and-se-computation](https://www.openaccountants.com/skills/us-schedule-c-and-se-computation) | Rates, bands and thresholds |

Skills behind it: [us-schedule-c-and-se-computation](https://www.openaccountants.com/skills/us-schedule-c-and-se-computation), [us-tax-workflow-base](https://www.openaccountants.com/skills/us-tax-workflow-base).

## Worked examples it reproduces

- us-tax-workflow-base Case 1 (2026): profit $60,000 -> SE tax $8,477.73
- us-schedule-c-and-se-computation Case 2 (2026): profit $120,000, W-2 wages $100,000 -> SE tax $13,691.78, half $6,845.89

The platform's tests recompute these from the skills' own worked examples (`worked-examples.test.ts`, not published here because it calls the engine's internal helpers).

## Licence

Code (`index.mjs`, `index.test.mjs`, `source/`): AGPL-3.0-only, like every calculator in this repository. Figures and wording in `rules.json`: the OpenAccountants Guide License v1.0, like the skills. See [LICENSING.md](../../../LICENSING.md).

Source commit: `c2e3c2b9` (OpenAccountants platform, `src/lib/engines`).
