# uk_ani_pension_target_2026_27

UK 2026-27: how much to pay (net) into a relief-at-source personal pension to bring adjusted net income down to a limit. Targets: personal_allowance_taper (GBP 100,000), child_benefit_charge_nil (GBP 60,000), tax_free_childcare (limit not served by any skill: always returns missing_rule until a skill serves it).

Jurisdiction GB. Tax year 2026-27. Engine version 1.2.0.

This is the same code that answers the compute tool of the OpenAccountants plugin. It is generated from `src/lib/engines/uk-ani-pension-target-2026-27.ts` in the OpenAccountants platform at commit `c2e3c2b9`; do not edit it here. The compute tool's answer links to this folder (`inspect.code_url`), so anyone can read the code, the figures and the tests behind it and run them again.

## Files

| File | What it is |
|---|---|
| `index.mjs` | The engine as one ES module with no dependencies (Node 20+). Exports `run(facts)`, `spec`, `rules`, `anchors`, `receiptId`, `quoteFound`, `normaliseLines`. |
| `source/` | The TypeScript files bundled into `index.mjs`, unchanged, with their comments. Read these. |
| `rules.json` | The spec and every figure the engine uses, each with the skill, section and line it was quoted from. |
| `cases.json` | 10 test cases with the exact output the engine gives (4 ok, 4 missing_rule, 2 needs_input). |
| `index.test.mjs` | The tests: `node --test calculators/engines/uk_ani_pension_target_2026_27/`. |

`index.mjs` is the files in `source/` with the types removed and bundled together; the bundler may print numbers in short form (`2e5` is 200,000, `.19` is 0.19).

## Run it

```sh
node --test calculators/engines/uk_ani_pension_target_2026_27/
```

```js
import { run } from "./calculators/engines/uk_ani_pension_target_2026_27/index.mjs";
console.log(JSON.stringify(run({"total_taxable_income":110000,"target":"tax_free_childcare","tax_year":"2026-27"}), null, 2));
```

To check an answer from the plugin, pass the same facts: `run(facts)` returns the same result, steps and constants, and `receiptId("uk_ani_pension_target_2026_27", "1.2.0", facts, run(facts))` equals the `receipt.id` it returned.

## Inputs

| Fact | Type | Required | Default | Description |
|---|---|---|---|---|
| `total_taxable_income` | number | yes |  | GBP |
| `existing_gross_ras_contributions` | number | no | `0` | GBP |
| `gross_gift_aid` | number | no | `0` | GBP |
| `target` | `personal_allowance_taper`, `child_benefit_charge_nil`, `tax_free_childcare` | yes |  | personal_allowance_taper\|child_benefit_charge_nil\|tax_free_childcare |
| `tax_year` | `2026-27` | yes |  | the tax year the question is about, written YYYY-YY. This engine has figures for 2026-27 only; any other year is refused |

A fact left out takes its default, and the output lists it in `defaults_assumed`. A fact with no default must be given.

## Outputs

`run(facts)` returns one of three statuses:

- `ok`: `headline` (label, value, currency), `lines`, `steps`, `inputs_used`, `constants_used` (every figure used, with its skill line), `assumptions`, `skill_anchors_reproduced`, `notes`, `defaults_assumed`, `tax_year`.
- `missing_rule`: the engine refuses because no OpenAccountants skill serves a figure it would need. It says `what` is missing and `why`, and never guesses.
- `needs_input`: a fact is missing or invalid. It says `what` and returns the `schema` of the facts.

| Line | Unit |
|---|---|
| `adjusted_net_income_now` | GBP |
| `limit` | GBP |
| `gross_contribution_needed` | GBP |
| `net_payment_needed` | GBP |
| `basic_rate_relief_added_by_provider` | GBP |

## What it refuses

- Any tax year other than 2026-27 (`missing_rule`). It never applies one year's figures to another year.
- A missing, negative or wrongly typed fact (`needs_input`).
- Tax-Free Childcare adjusted net income limit (UK, 2026-27) (`missing_rule`)

## Figures

Every figure is quoted from an OpenAccountants skill. The skill is the authority on the method; the official source it names is the authority on the number. The exact line each figure was quoted from is its `quote` in [`rules.json`](rules.json), and a daily check in the platform confirms each quoted line is still in the skill as served.

| Name | Value | Skill | Section |
|---|---|---|---|
| `RAS_NET_TO_GROSS` | `0.8` | [uk-income-tax-sa100](https://www.openaccountants.com/skills/uk-income-tax-sa100) | Worked examples / Example 2: Personal Allowance taper and the Child Benefit charge, England, 2026-27 |
| `ANI_DEFINITION` | `"total taxable income less reliefs, less grossed-up Gift Aid and grossed-up relief-at-source pension contributions"` | [uk-income-tax-sa100](https://www.openaccountants.com/skills/uk-income-tax-sa100) | The taxable base / Step 3: adjusted net income (ITA 2007 s.58) |
| `PA_TAPER_START` | `100000` | [uk-income-tax-sa100](https://www.openaccountants.com/skills/uk-income-tax-sa100) | Rates, bands and thresholds |
| `HICBC_START` | `60000` | [uk-income-tax-sa100](https://www.openaccountants.com/skills/uk-income-tax-sa100) | Rates, bands and thresholds |

Skills behind it: [uk-income-tax-sa100](https://www.openaccountants.com/skills/uk-income-tax-sa100).

## Worked examples it reproduces

- uk-income-tax-sa100 Example 2: net GBP 4,000 -> gross GBP 5,000; ANI GBP 107,000; further gross GBP 7,000 restores the allowance at GBP 100,000

The platform's tests recompute these from the skills' own worked examples (`worked-examples.test.ts`, not published here because it calls the engine's internal helpers).

## Licence

Code (`index.mjs`, `index.test.mjs`, `source/`): AGPL-3.0-only, like every calculator in this repository. Figures and wording in `rules.json`: the OpenAccountants Guide License v1.0, like the skills. See [LICENSING.md](../../../LICENSING.md).

Source commit: `c2e3c2b9` (OpenAccountants platform, `src/lib/engines`).
