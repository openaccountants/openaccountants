# ca_cpp_ei_employee_2026

Canada (outside Quebec) employee CPP (base + first additional), CPP2 and EI premiums for a full calendar year 2026 with one employer.

Jurisdiction CA. Tax year 2026. Engine version 1.2.0.

This is the same code that answers the compute tool of the OpenAccountants plugin. It is generated from `src/lib/engines/ca-cpp-ei-employee-2026.ts` in the OpenAccountants platform at commit `c2e3c2b9`; do not edit it here. The compute tool's answer links to this folder (`inspect.code_url`), so anyone can read the code, the figures and the tests behind it and run them again.

## Files

| File | What it is |
|---|---|
| `index.mjs` | The engine as one ES module with no dependencies (Node 20+). Exports `run(facts)`, `spec`, `rules`, `anchors`, `receiptId`, `quoteFound`, `normaliseLines`. |
| `source/` | The TypeScript files bundled into `index.mjs`, unchanged, with their comments. Read these. |
| `rules.json` | The spec and every figure the engine uses, each with the skill, section and line it was quoted from. |
| `cases.json` | 19 test cases with the exact output the engine gives (15 ok, 3 missing_rule, 1 needs_input). |
| `index.test.mjs` | The tests: `node --test calculators/engines/ca_cpp_ei_employee_2026/`. |

`index.mjs` is the files in `source/` with the types removed and bundled together; the bundler may print numbers in short form (`2e5` is 200,000, `.19` is 0.19).

## Run it

```sh
node --test calculators/engines/ca_cpp_ei_employee_2026/
```

```js
import { run } from "./calculators/engines/ca_cpp_ei_employee_2026/index.mjs";
console.log(JSON.stringify(run({"annual_pensionable_earnings":60000,"province":"ON","tax_year":"2026"}), null, 2));
```

To check an answer from the plugin, pass the same facts: `run(facts)` returns the same result, steps and constants, and `receiptId("ca_cpp_ei_employee_2026", "1.2.0", facts, run(facts))` equals the `receipt.id` it returned.

## Inputs

| Fact | Type | Required | Default | Description |
|---|---|---|---|---|
| `annual_pensionable_earnings` | number | yes |  | CAD (salary) |
| `province` | string | yes |  | province of employment, two-letter code, e.g. ON (QC is refused: Quebec uses QPP) |
| `months_employed` | number | no | `12` | integer 1-12 |
| `tax_year` | `2026` | yes |  | the tax year the question is about. This engine has figures for 2026 only; any other year is refused |

A fact left out takes its default, and the output lists it in `defaults_assumed`. A fact with no default must be given.

## Outputs

`run(facts)` returns one of three statuses:

- `ok`: `headline` (label, value, currency), `lines`, `steps`, `inputs_used`, `constants_used` (every figure used, with its skill line), `assumptions`, `skill_anchors_reproduced`, `notes`, `defaults_assumed`, `tax_year`.
- `missing_rule`: the engine refuses because no OpenAccountants skill serves a figure it would need. It says `what` is missing and `why`, and never guesses.
- `needs_input`: a fact is missing or invalid. It says `what` and returns the `schema` of the facts.

| Line | Unit |
|---|---|
| `cpp_base_and_first_additional` | CAD |
| `cpp2` | CAD |
| `ei_premium` | CAD |
| `total` | CAD |

## What it refuses

- Any tax year other than 2026 (`missing_rule`). It never applies one year's figures to another year.
- A missing, negative or wrongly typed fact (`needs_input`).
- Quebec QPP rates (`missing_rule`)
- part-year basic exemption proration (`missing_rule`)

## Figures

Every figure is quoted from an OpenAccountants skill. The skill is the authority on the method; the official source it names is the authority on the number. The exact line each figure was quoted from is its `quote` in [`rules.json`](rules.json), and a daily check in the platform confirms each quoted line is still in the skill as served.

| Name | Value | Skill | Section |
|---|---|---|---|
| `CPP_EMPLOYEE_RATE` | `0.0595` | [canada-payroll](https://www.openaccountants.com/skills/canada-payroll) | Rates and thresholds / Payroll |
| `BASIC_EXEMPTION` | `3500` | [canada-payroll](https://www.openaccountants.com/skills/canada-payroll) | Rates and thresholds / Payroll |
| `YMPE_2026` | `74600` | [canada-payroll](https://www.openaccountants.com/skills/canada-payroll) | Rates and thresholds / Payroll |
| `YAMPE_2026` | `85000` | [canada-payroll](https://www.openaccountants.com/skills/canada-payroll) | Rates and thresholds / Payroll |
| `CPP2_EMPLOYEE_RATE` | `0.04` | [canada-payroll](https://www.openaccountants.com/skills/canada-payroll) | Section 3 -- Social Security: Employee Deductions / Canada Pension Plan (CPP) -- 2026 |
| `EI_EMPLOYEE_RATE_NON_QC` | `0.0163` | [canada-payroll](https://www.openaccountants.com/skills/canada-payroll) | Rates and thresholds / Payroll |
| `EI_MAX_INSURABLE_EARNINGS` | `68900` | [canada-payroll](https://www.openaccountants.com/skills/canada-payroll) | Rates and thresholds / Payroll |

Skills behind it: [canada-payroll](https://www.openaccountants.com/skills/canada-payroll).

## Worked examples it reproduces

- Max CPP 2026 $4,230.45 and max CPP2 $416.00 reproduced
- Max EI premium $1,123.07 reproduced
- Pattern 1 (biweekly $2,884.62): EI $47.02 exact; CPP $163.60 stated vs $163.625 from the skill's own inputs (skill arithmetic off ~3 cents)

The platform's tests recompute these from the skills' own worked examples (`worked-examples.test.ts`, not published here because it calls the engine's internal helpers).

## Licence

Code (`index.mjs`, `index.test.mjs`, `source/`): AGPL-3.0-only, like every calculator in this repository. Figures and wording in `rules.json`: the OpenAccountants Guide License v1.0, like the skills. See [LICENSING.md](../../../LICENSING.md).

Source commit: `c2e3c2b9` (OpenAccountants platform, `src/lib/engines`).
