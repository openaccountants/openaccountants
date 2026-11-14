# uk_paye_take_home_2026_27

UK employee annual income tax (rUK rates: England, Wales, Northern Ireland) and employee Class 1 NIC (category A) on salary for 2026-27, and take-home pay. Annual basis.

Jurisdiction GB. Tax year 2026-27. Engine version 1.2.0.

This is the same code that answers the compute tool of the OpenAccountants plugin. It is generated from `src/lib/engines/uk-paye-take-home-2026-27.ts` in the OpenAccountants platform at commit `c2e3c2b9`; do not edit it here. The compute tool's answer links to this folder (`inspect.code_url`), so anyone can read the code, the figures and the tests behind it and run them again.

## Files

| File | What it is |
|---|---|
| `index.mjs` | The engine as one ES module with no dependencies (Node 20+). Exports `run(facts)`, `spec`, `rules`, `anchors`, `receiptId`, `quoteFound`, `normaliseLines`. |
| `source/` | The TypeScript files bundled into `index.mjs`, unchanged, with their comments. Read these. |
| `rules.json` | The spec and every figure the engine uses, each with the skill, section and line it was quoted from. |
| `cases.json` | 26 test cases with the exact output the engine gives (19 ok, 3 missing_rule, 4 needs_input). |
| `index.test.mjs` | The tests: `node --test calculators/engines/uk_paye_take_home_2026_27/`. |

`index.mjs` is the files in `source/` with the types removed and bundled together; the bundler may print numbers in short form (`2e5` is 200,000, `.19` is 0.19).

## Run it

```sh
node --test calculators/engines/uk_paye_take_home_2026_27/
```

```js
import { run } from "./calculators/engines/uk_paye_take_home_2026_27/index.mjs";
console.log(JSON.stringify(run({"annual_salary":60000,"region":"england","nic_category":"A","tax_year":"2026-27"}), null, 2));
```

To check an answer from the plugin, pass the same facts: `run(facts)` returns the same result, steps and constants, and `receiptId("uk_paye_take_home_2026_27", "1.2.0", facts, run(facts))` equals the `receipt.id` it returned.

## Inputs

| Fact | Type | Required | Default | Description |
|---|---|---|---|---|
| `annual_salary` | number | yes |  | GBP |
| `region` | `england`, `wales`, `northern_ireland`, `scotland` | yes |  | where the employee lives for tax: england\|wales\|northern_ireland\|scotland (Scottish taxpayers are refused: no Scottish engine yet) |
| `nic_category` | string | no | `"A"` | A (only A supported) |
| `other_income` | number | no | `0` | GBP, non-savings, no NIC |
| `gross_pension_contributions_ras` | number | no | `0` | GBP gross relief-at-source contributions |
| `tax_year` | `2026-27` | yes |  | the tax year the question is about, written YYYY-YY. This engine has figures for 2026-27 only; any other year is refused |

A fact left out takes its default, and the output lists it in `defaults_assumed`. A fact with no default must be given.

## Outputs

`run(facts)` returns one of three statuses:

- `ok`: `headline` (label, value, currency), `lines`, `steps`, `inputs_used`, `constants_used` (every figure used, with its skill line), `assumptions`, `skill_anchors_reproduced`, `notes`, `defaults_assumed`, `tax_year`.
- `missing_rule`: the engine refuses because no OpenAccountants skill serves a figure it would need. It says `what` is missing and `why`, and never guesses.
- `needs_input`: a fact is missing or invalid. It says `what` and returns the `schema` of the facts.

| Line | Unit |
|---|---|
| `adjusted_net_income` | GBP |
| `personal_allowance` | GBP |
| `taxable_income` | GBP |
| `income_tax` | GBP |
| `employee_nic` | GBP |
| `take_home_pay` | GBP |

## What it refuses

- Any tax year other than 2026-27 (`missing_rule`). It never applies one year's figures to another year.
- A missing, negative or wrongly typed fact (`needs_input`).
- Scottish income tax engine (`missing_rule`)
- NIC category B (`missing_rule`)

## Figures

Every figure is quoted from an OpenAccountants skill. The skill is the authority on the method; the official source it names is the authority on the number. The exact line each figure was quoted from is its `quote` in [`rules.json`](rules.json), and a daily check in the platform confirms each quoted line is still in the skill as served.

| Name | Value | Skill | Section |
|---|---|---|---|
| `PERSONAL_ALLOWANCE` | `12570` | [uk-payroll](https://www.openaccountants.com/skills/uk-payroll) | Rates, bands and thresholds |
| `BASIC_RATE_BAND` | `37700` | [uk-payroll](https://www.openaccountants.com/skills/uk-payroll) | Rates, bands and thresholds |
| `ADDITIONAL_RATE_START` | `125140` | [uk-payroll](https://www.openaccountants.com/skills/uk-payroll) | Rates, bands and thresholds |
| `RATES` | `[0.2,0.4,0.45]` | [uk-payroll](https://www.openaccountants.com/skills/uk-payroll) | Rates, bands and thresholds |
| `TAPER_START` | `100000` | [uk-payroll](https://www.openaccountants.com/skills/uk-payroll) | Rates, bands and thresholds |
| `TAPER_ROUNDING` | `"round reduction up to whole pound"` | [uk-income-tax-sa100](https://www.openaccountants.com/skills/uk-income-tax-sa100) | The taxable base / Step 4: the Personal Allowance |
| `NIC_PRIMARY_THRESHOLD` | `12570` | [uk-payroll](https://www.openaccountants.com/skills/uk-payroll) | Rates, bands and thresholds |
| `NIC_UPPER_EARNINGS_LIMIT` | `50270` | [uk-payroll](https://www.openaccountants.com/skills/uk-payroll) | Rates, bands and thresholds |
| `EE_NIC_MAIN_RATE` | `0.08` | [uk-payroll](https://www.openaccountants.com/skills/uk-payroll) | Rates, bands and thresholds |
| `EE_NIC_UPPER_RATE` | `0.02` | [uk-payroll](https://www.openaccountants.com/skills/uk-payroll) | Rates, bands and thresholds |

Skills behind it: [uk-payroll](https://www.openaccountants.com/skills/uk-payroll), [uk-income-tax-sa100](https://www.openaccountants.com/skills/uk-income-tax-sa100).

## Worked examples it reproduces

- uk-payroll Example 1: £42,000 -> PAYE £490.50/month; ee NIC £196.16/month
- uk-income-tax-sa100 Example 2: salary £112,000, RAS gross £5,000 -> PA £9,070, taxable £102,930, tax £32,632

The platform's tests recompute these from the skills' own worked examples (`worked-examples.test.ts`, not published here because it calls the engine's internal helpers).

## Licence

Code (`index.mjs`, `index.test.mjs`, `source/`): AGPL-3.0-only, like every calculator in this repository. Figures and wording in `rules.json`: the OpenAccountants Guide License v1.0, like the skills. See [LICENSING.md](../../../LICENSING.md).

Source commit: `c2e3c2b9` (OpenAccountants platform, `src/lib/engines`).
