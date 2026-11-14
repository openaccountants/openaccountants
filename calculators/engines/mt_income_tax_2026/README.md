# mt_income_tax_2026

Malta resident income tax on chargeable income for basis year 2026 (year of assessment 2027) or basis year 2025 (year of assessment 2026): picks the single, married or parent table, including the 2026 qualifying-child tables, from the person's facts.

Jurisdiction MT. Tax years 2025 and 2026. Engine version 1.0.0.

This is the same code that answers the compute tool of the OpenAccountants plugin. It is generated from `src/lib/engines/mt-income-tax-2026.ts` in the OpenAccountants platform at commit `c2e3c2b9`; do not edit it here. The compute tool's answer links to this folder (`inspect.code_url`), so anyone can read the code, the figures and the tests behind it and run them again.

## Files

| File | What it is |
|---|---|
| `index.mjs` | The engine as one ES module with no dependencies (Node 20+). Exports `run(facts)`, `spec`, `rules`, `anchors`, `receiptId`, `quoteFound`, `normaliseLines`. |
| `source/` | The TypeScript files bundled into `index.mjs`, unchanged, with their comments. Read these. |
| `rules.json` | The spec and every figure the engine uses, each with the skill, section and line it was quoted from. |
| `cases.json` | 5 test cases with the exact output the engine gives (3 ok, 1 missing_rule, 1 needs_input). |
| `index.test.mjs` | The tests: `node --test calculators/engines/mt_income_tax_2026/`. |

`index.mjs` is the files in `source/` with the types removed and bundled together; the bundler may print numbers in short form (`2e5` is 200,000, `.19` is 0.19).

## Run it

```sh
node --test calculators/engines/mt_income_tax_2026/
```

```js
import { run } from "./calculators/engines/mt_income_tax_2026/index.mjs";
console.log(JSON.stringify(run({"chargeable_income":31625,"status":"single","resident":true,"tax_paid":3500,"tax_year":"2026"}), null, 2));
```

To check an answer from the plugin, pass the same facts: `run(facts)` returns the same result, steps and constants, and `receiptId("mt_income_tax_2026", "1.0.0", facts, run(facts))` equals the `receipt.id` it returned.

## Inputs

| Fact | Type | Required | Default | Description |
|---|---|---|---|---|
| `chargeable_income` | number | yes |  | EUR, after allowable expenses and capital allowances, and WITHOUT income taxed at a final rate (part-time 10%, rent on the 15% option, property transfers). For a joint return, the couple's combined chargeable income |
| `resident` | boolean | yes |  | resident in Malta in the basis year (non-residents are refused) |
| `status` | `single`, `married_joint`, `parent`, `single_parent_sole_custody` | yes |  | status in the basis year: single; married_joint (married, living together, joint return, the default for a couple); parent (has custody of, or pays maintenance for, a child not over 18, or not over 23 in full-time education); single_parent_sole_custody (refused for now). Spouses filing separately (art. 49A or 50): run once per spouse as single or parent |
| `children` | number | no |  | needed for married_joint and parent: how many children the person or couple had custody of or paid maintenance for, each not over 18, or not over 23 and in full-time education |
| `eu_eea_or_long_term_resident` | boolean | no |  | needed when there are children in basis year 2026: the individual or their spouse is an EU/EEA national or holds long-term resident status |
| `children_born_and_resident_in_malta` | number | no |  | needed only when nobody is an EU/EEA national or long-term resident: how many of those children were born in Malta and are resident in Malta |
| `tax_paid` | number | no | `0` | EUR already paid for the year: FSS tax deducted by employers plus provisional tax |
| `tax_year` | `2025`, `2026` | yes |  | the BASIS year: the calendar year the income was earned (2026 income is year of assessment 2027). This engine has figures for basis years 2025 and 2026 only; any other year is refused |

A fact left out takes its default, and the output lists it in `defaults_assumed`. A fact with no default must be given.

## Outputs

`run(facts)` returns one of three statuses:

- `ok`: `headline` (label, value, currency), `lines`, `steps`, `inputs_used`, `constants_used` (every figure used, with its skill line), `assumptions`, `skill_anchors_reproduced`, `notes`, `defaults_assumed`, `tax_year`.
- `missing_rule`: the engine refuses because no OpenAccountants skill serves a figure it would need. It says `what` is missing and `why`, and never guesses.
- `needs_input`: a fact is missing or invalid. It says `what` and returns the `schema` of the facts.

| Line | Unit |
|---|---|
| `chargeable_income` | EUR |
| `table` | rate table used |
| `tax` | EUR |
| `tax_paid` | EUR |
| `balance_due` | EUR (negative = refund) |

## What it refuses

- Any tax year other than 2025 and 2026 (`missing_rule`). It never applies one year's figures to another year.
- A missing, negative or wrongly typed fact (`needs_input`).

## Figures

Every figure is quoted from an OpenAccountants skill. The skill is the authority on the method; the official source it names is the authority on the number. The exact line each figure was quoted from is its `quote` in [`rules.json`](rules.json), and a daily check in the platform confirms each quoted line is still in the skill as served.

| Name | Value | Skill | Section |
|---|---|---|---|
| `SINGLE_2026` | `{"zero":12000,"bands":[[16000,0.15,1800],[60000,0.25,3400],[null,0.35,9400]]}` | [malta-income-tax](https://www.openaccountants.com/skills/malta-income-tax) | Resident rate tables, basis year 2026 (year of assessment 2027) |
| `MARRIED_NO_CHILD_2026` | `{"zero":15000,"bands":[[23000,0.15,2250],[60000,0.25,4550],[null,0.35,10550]]}` | [malta-income-tax](https://www.openaccountants.com/skills/malta-income-tax) | Resident rate tables, basis year 2026 (year of assessment 2027) |
| `PARENT_2026` | `{"zero":13000,"bands":[[17500,0.15,1950],[60000,0.25,3700],[null,0.35,9700]]}` | [malta-income-tax](https://www.openaccountants.com/skills/malta-income-tax) | Resident rate tables, basis year 2026 (year of assessment 2027) |
| `MARRIED_1_CHILD_2026` | `{"zero":17500,"bands":[[26500,0.15,2625],[60000,0.25,5275],[null,0.35,11275]]}` | [malta-income-tax](https://www.openaccountants.com/skills/malta-income-tax) | Resident rate tables, basis year 2026 (year of assessment 2027) |
| `MARRIED_2_CHILDREN_2026` | `{"zero":22500,"bands":[[32000,0.15,3375],[60000,0.25,6575],[null,0.35,12575]]}` | [malta-income-tax](https://www.openaccountants.com/skills/malta-income-tax) | Resident rate tables, basis year 2026 (year of assessment 2027) |
| `PARENT_1_CHILD_2026` | `{"zero":14500,"bands":[[21000,0.15,2175],[60000,0.25,4275],[null,0.35,10270]]}` | [malta-income-tax](https://www.openaccountants.com/skills/malta-income-tax) | Resident rate tables, basis year 2026 (year of assessment 2027) |
| `PARENT_2_CHILDREN_2026` | `{"zero":18500,"bands":[[25500,0.15,2775],[60000,0.25,5325],[null,0.35,11325]]}` | [malta-income-tax](https://www.openaccountants.com/skills/malta-income-tax) | Resident rate tables, basis year 2026 (year of assessment 2027) |
| `SINGLE_2025` | `{"zero":12000,"bands":[[16000,0.15,1800],[60000,0.25,3400],[null,0.35,9400]]}` | [malta-income-tax](https://www.openaccountants.com/skills/malta-income-tax) | 2025 income (year of assessment 2026) |
| `MARRIED_2025` | `{"zero":15000,"bands":[[23000,0.15,2250],[60000,0.25,4550],[null,0.35,10550]]}` | [malta-income-tax](https://www.openaccountants.com/skills/malta-income-tax) | 2025 income (year of assessment 2026) |
| `PARENT_2025` | `{"zero":13000,"bands":[[17500,0.15,1950],[60000,0.25,3700],[null,0.35,9700]]}` | [malta-income-tax](https://www.openaccountants.com/skills/malta-income-tax) | 2025 income (year of assessment 2026) |
| `NO_CHILD_TABLES_2025` | `true` | [malta-income-tax](https://www.openaccountants.com/skills/malta-income-tax) | 2025 income (year of assessment 2026) |
| `QUALIFYING_CHILD_NATIONALITY` | `true` | [malta-income-tax](https://www.openaccountants.com/skills/malta-income-tax) | Who gets which table |
| `PARENT_1_CHILD_35_ACT_FIGURE` | `10270` | [malta-income-tax](https://www.openaccountants.com/skills/malta-income-tax) | Resident rate tables, basis year 2026 (year of assessment 2027) |

Skills behind it: [malta-income-tax](https://www.openaccountants.com/skills/malta-income-tax).

## Worked examples it reproduces

- malta-income-tax Case 1: single, chargeable EUR 31,625 -> tax EUR 4,506.25, balance EUR 1,006.25 after EUR 3,500 paid
- malta-income-tax Case 2: married, two children, EUR 40,000 -> EUR 3,425 (2026) against EUR 5,450 (2025)

The platform's tests recompute these from the skills' own worked examples (`worked-examples.test.ts`, not published here because it calls the engine's internal helpers).

## Licence

Code (`index.mjs`, `index.test.mjs`, `source/`): AGPL-3.0-only, like every calculator in this repository. Figures and wording in `rules.json`: the OpenAccountants Guide License v1.0, like the skills. See [LICENSING.md](../../../LICENSING.md).

Source commit: `c2e3c2b9` (OpenAccountants platform, `src/lib/engines`).
