# ca_income_tax_2026

Canada personal income tax for 2026 or 2025 for a single person resident in Ontario, British Columbia or Alberta on 31 December: CPP and EI, net and taxable income, federal tax (basic personal amount with its phase-down, Canada employment amount), provincial tax (Ontario surtax, tax reduction, LIFT and Health Premium; BC tax reduction; Alberta 8% band and supplemental credit), the balance owing or refund against tax already paid, and what more RRSP saves. Quebec, dividends, a spouse or dependants, age 65 or over, and employment plus self-employment together are refused.

Jurisdiction CA. Tax years 2025 and 2026. Engine version 2.0.0.

This is the same code that answers the compute tool of the OpenAccountants plugin. It is generated from `src/lib/engines/ca-income-tax-2026.ts` in the OpenAccountants platform at commit `c2e3c2b9`; do not edit it here. The compute tool's answer links to this folder (`inspect.code_url`), so anyone can read the code, the figures and the tests behind it and run them again.

## Files

| File | What it is |
|---|---|
| `index.mjs` | The engine as one ES module with no dependencies (Node 20+). Exports `run(facts)`, `spec`, `rules`, `anchors`, `receiptId`, `quoteFound`, `normaliseLines`. |
| `source/` | The TypeScript files bundled into `index.mjs`, unchanged, with their comments. Read these. |
| `rules.json` | The spec and every figure the engine uses, each with the skill, section and line it was quoted from. |
| `cases.json` | 7 test cases with the exact output the engine gives (3 ok, 3 missing_rule, 1 needs_input). |
| `index.test.mjs` | The tests: `node --test calculators/engines/ca_income_tax_2026/`. |

`index.mjs` is the files in `source/` with the types removed and bundled together; the bundler may print numbers in short form (`2e5` is 200,000, `.19` is 0.19).

## Run it

```sh
node --test calculators/engines/ca_income_tax_2026/
```

```js
import { run } from "./calculators/engines/ca_income_tax_2026/index.mjs";
console.log(JSON.stringify(run({"province":"ON","employment_income":90000,"rrsp_deduction":5000,"tax_withheld":18000,"tax_year":"2026"}), null, 2));
```

To check an answer from the plugin, pass the same facts: `run(facts)` returns the same result, steps and constants, and `receiptId("ca_income_tax_2026", "2.0.0", facts, run(facts))` equals the `receipt.id` it returned.

## Inputs

| Fact | Type | Required | Default | Description |
|---|---|---|---|---|
| `province` | `ON`, `BC`, `AB`, `QC` | yes |  | province of residence on 31 December, two-letter code (QC is refused: Quebec tax is on a separate TP-1 return) |
| `employment_income` | number | no | `0` | CAD, T4 employment income from one employer for the whole year (CPP and EI are computed from it) |
| `self_employment_net_income` | number | no | `0` | CAD, net self-employment profit (T2125); a loss is not supported |
| `other_income` | number | no | `0` | CAD, other fully taxable income with no credit of its own (interest, net rent) |
| `eligible_dividends` | number | no | `0` | CAD, actual eligible dividends received (refused if more than 0) |
| `other_dividends` | number | no | `0` | CAD, actual other-than-eligible dividends received (refused if more than 0) |
| `rrsp_deduction` | number | no | `0` | CAD, RRSP deduction claimed for the year (within the limit on the notice of assessment) |
| `tax_withheld` | number | no | `0` | CAD, income tax already deducted at source (T4 box 22) plus instalments paid for the year |
| `has_spouse_or_partner` | boolean | no | `false` | had a spouse or common-law partner on 31 December (refused if true: spouse credits and family tests are not computed) |
| `dependants` | number | no | `0` | dependants supported (refused if more than 0) |
| `age_65_or_over` | boolean | no | `false` | 65 or older on 31 December (refused if true: age and pension credits are not computed) |
| `tax_year` | `2025`, `2026` | yes |  | the tax year the question is about. This engine has figures for 2025 and 2026 only; any other year is refused |

A fact left out takes its default, and the output lists it in `defaults_assumed`. A fact with no default must be given.

## Outputs

`run(facts)` returns one of three statuses:

- `ok`: `headline` (label, value, currency), `lines`, `steps`, `inputs_used`, `constants_used` (every figure used, with its skill line), `assumptions`, `skill_anchors_reproduced`, `notes`, `defaults_assumed`, `tax_year`.
- `missing_rule`: the engine refuses because no OpenAccountants skill serves a figure it would need. It says `what` is missing and `why`, and never guesses.
- `needs_input`: a fact is missing or invalid. It says `what` and returns the `schema` of the facts.

| Line | Unit |
|---|---|
| `taxable_income` | CAD |
| `basic_federal_tax` | CAD |
| `provincial_tax` | CAD |
| `total_income_tax` | CAD |
| `cpp_payable_with_return` | CAD (self-employed only) |
| `balance_owing` | CAD (negative = refund) |
| `rrsp_saving_next_1000` | CAD of income tax saved by CAD 1,000 more RRSP deduction |
| `federal_saving_per_extra_rrsp_dollar` | CAD per CAD |

## What it refuses

- Any tax year other than 2025 and 2026 (`missing_rule`). It never applies one year's figures to another year.
- A missing, negative or wrongly typed fact (`needs_input`).
- Quebec income tax for 2026 (`missing_rule`)
- credits for a spouse or partner, dependants, or age 65 or over (`missing_rule`)

## Figures

Every figure is quoted from an OpenAccountants skill. The skill is the authority on the method; the official source it names is the authority on the number. The exact line each figure was quoted from is its `quote` in [`rules.json`](rules.json), and a daily check in the platform confirms each quoted line is still in the skill as served.

| Name | Value | Skill | Section |
|---|---|---|---|
| `FEDERAL_BRACKETS_2026` | `[[58523,0.14],[117045,0.205],[181440,0.26],[258482,0.29],[null,0.33]]` | [canada-payroll](https://www.openaccountants.com/skills/canada-payroll) | Section 2 -- Income Tax Withholding (Source Deductions) / Federal Tax Brackets (2026) |
| `FEDERAL_BPA_2026` | `{"max":16452,"min":14829}` | [canada-payroll](https://www.openaccountants.com/skills/canada-payroll) | Federal Basic Personal Amount (BPA) -- 2026 |
| `FEDERAL_LOWEST_RATE_2026` | `0.14` | [canada-payroll](https://www.openaccountants.com/skills/canada-payroll) | Federal Tax Brackets (2026) |
| `FEDERAL_CREDIT_RATE_2026` | `0.14` | [ca-fed-cpp-ei](https://www.openaccountants.com/skills/ca-fed-cpp-ei) | 4.5 Tax treatment of self-employed CPP (Tier 1) |
| `SELF_EMPLOYED_CPP_BOTH_HALVES_2026` | `2` | [canada-tax-optimization](https://www.openaccountants.com/skills/canada-tax-optimization) | Section 8 -- CPP/EI & Social Security Optimization / CPP Contributions (2026) |
| `FEDERAL_BRACKETS_2025` | `[[57375,0.145],[114750,0.205],[177882,0.26],[253414,0.29],[null,0.33]]` | [ca-fed-t1-return](https://www.openaccountants.com/skills/ca-fed-t1-return) | Section 1 -- Quick Reference / Federal Tax Brackets (2025) |
| `FEDERAL_BPA_2025` | `{"max":16129,"min":14538}` | [ca-fed-t1-return](https://www.openaccountants.com/skills/ca-fed-t1-return) | Basic Personal Amount (2025) |
| `FEDERAL_BPA_PHASE_DOWN_METHOD` | `"linear between the 29% and 33% bracket thresholds, on net income"` | [ca-fed-t1-return](https://www.openaccountants.com/skills/ca-fed-t1-return) | Section 6 -- Tier 2 Catalogue (Reviewer Judgement Required) / 6.2 BPA Reduction for High Earners |
| `FEDERAL_CREDIT_RATE_2025` | `0.145` | [ca-fed-t1-return](https://www.openaccountants.com/skills/ca-fed-t1-return) | Section 7 -- Excel Working Paper Template |
| `EI_RATE_2025` | `0.0164` | [ca-fed-t1-return](https://www.openaccountants.com/skills/ca-fed-t1-return) | Rates and thresholds / T1 Return |
| `YMPE_2025` | `71300` | [ca-fed-cpp-ei](https://www.openaccountants.com/skills/ca-fed-cpp-ei) | Section 1 -- Quick reference / CPP1 thresholds (2025) |
| `BASIC_EXEMPTION_2025` | `3500` | [ca-fed-cpp-ei](https://www.openaccountants.com/skills/ca-fed-cpp-ei) | Section 1 -- Quick reference / CPP1 thresholds (2025) |
| `CPP_EMPLOYEE_RATE_2025` | `0.0595` | [ca-fed-cpp-ei](https://www.openaccountants.com/skills/ca-fed-cpp-ei) | Section 1 -- Quick reference / CPP1 thresholds (2025) |
| `YAMPE_2025` | `81200` | [ca-fed-cpp-ei](https://www.openaccountants.com/skills/ca-fed-cpp-ei) | Rates and thresholds / CPP-CPP2-EI |
| `CPP2_EMPLOYEE_RATE_2025` | `0.04` | [ca-fed-cpp-ei](https://www.openaccountants.com/skills/ca-fed-cpp-ei) | Rates and thresholds / CPP-CPP2-EI |
| `EI_MAX_INSURABLE_EARNINGS_2025` | `65700` | [ca-fed-cpp-ei](https://www.openaccountants.com/skills/ca-fed-cpp-ei) | Rates and thresholds / CPP-CPP2-EI |
| `CANADA_EMPLOYMENT_AMOUNT` | `{"2025":1471,"2026":1501}` | [ca-fed-t1-return](https://www.openaccountants.com/skills/ca-fed-t1-return) | Rates and thresholds / T1 Return |
| `CPP_BASE_RATE_EACH_SIDE` | `0.0495` | [ca-fed-cpp-ei](https://www.openaccountants.com/skills/ca-fed-cpp-ei) | Rates and thresholds / CPP-CPP2-EI |
| `CPP2_IS_A_DEDUCTION` | `true` | [ca-fed-cpp-ei](https://www.openaccountants.com/skills/ca-fed-cpp-ei) | 4.5 Tax treatment of self-employed CPP (Tier 1) |
| `SELF_EMPLOYED_CPP_SPLIT` | `true` | [ca-fed-t1-return](https://www.openaccountants.com/skills/ca-fed-t1-return) | CPP Self-Employed (2025) |
| `EI_PREMIUM_CREDIT` | `true` | [ca-fed-cpp-ei](https://www.openaccountants.com/skills/ca-fed-cpp-ei) | 4.6 EI for self-employed (Tier 1) |
| `CPP_EMPLOYEE_RATE` | `0.0595` | [canada-payroll](https://www.openaccountants.com/skills/canada-payroll) | Rates and thresholds / Payroll |
| `BASIC_EXEMPTION` | `3500` | [canada-payroll](https://www.openaccountants.com/skills/canada-payroll) | Rates and thresholds / Payroll |
| `YMPE_2026` | `74600` | [canada-payroll](https://www.openaccountants.com/skills/canada-payroll) | Rates and thresholds / Payroll |
| `YAMPE_2026` | `85000` | [canada-payroll](https://www.openaccountants.com/skills/canada-payroll) | Rates and thresholds / Payroll |
| `CPP2_EMPLOYEE_RATE` | `0.04` | [canada-payroll](https://www.openaccountants.com/skills/canada-payroll) | Section 3 -- Social Security: Employee Deductions / Canada Pension Plan (CPP) -- 2026 |
| `EI_EMPLOYEE_RATE_NON_QC` | `0.0163` | [canada-payroll](https://www.openaccountants.com/skills/canada-payroll) | Rates and thresholds / Payroll |
| `EI_MAX_INSURABLE_EARNINGS` | `68900` | [canada-payroll](https://www.openaccountants.com/skills/canada-payroll) | Rates and thresholds / Payroll |
| `ON_BRACKETS_2026` | `[[53891,0.0505],[107785,0.0915],[150000,0.1116],[220000,0.1216],[null,0.1316]]` | [on-individual-return](https://www.openaccountants.com/skills/on-individual-return) | Rates, bands and thresholds |
| `ON_BRACKETS_2025` | `[[52886,0.0505],[105775,0.0915],[150000,0.1116],[220000,0.1216],[null,0.1316]]` | [on-individual-return](https://www.openaccountants.com/skills/on-individual-return) | Rates, bands and thresholds |
| `ON_CREDIT_RATE` | `0.0505` | [on-individual-return](https://www.openaccountants.com/skills/on-individual-return) | Rates, bands and thresholds |
| `ON_BPA_2026` | `12989` | [on-individual-return](https://www.openaccountants.com/skills/on-individual-return) | Rates, bands and thresholds |
| `ON_BPA_2025` | `12747` | [on-individual-return](https://www.openaccountants.com/skills/on-individual-return) | Rates, bands and thresholds |
| `ON_SURTAX_2026` | `[5818,7446]` | [on-individual-return](https://www.openaccountants.com/skills/on-individual-return) | Rates, bands and thresholds |
| `ON_SURTAX_2025` | `[5710,7307]` | [on-individual-return](https://www.openaccountants.com/skills/on-individual-return) | Rates, bands and thresholds |
| `ON_TAX_REDUCTION_2026` | `300` | [on-individual-return](https://www.openaccountants.com/skills/on-individual-return) | Rates, bands and thresholds |
| `ON_TAX_REDUCTION_2025` | `294` | [on-individual-return](https://www.openaccountants.com/skills/on-individual-return) | Rates, bands and thresholds |
| `ON_LIFT_CREDIT` | `{"max":875,"rate":0.0505,"threshold":32500,"clawback":0.05}` | [on-individual-return](https://www.openaccountants.com/skills/on-individual-return) | Rates, bands and thresholds |
| `ON_HEALTH_PREMIUM` | `[[20000,0,0],[25000,0,0.06],[36000,300,0],[38500,300,0.06],[48000,450,0],[48600,450,0.25],[72000,600,0],[72600,600,0.25],[200000,750,0],[200600,750,0.25],[null,900,0]]` | [on-individual-return](https://www.openaccountants.com/skills/on-individual-return) | Rates, bands and thresholds / Ontario Health Premium chart (ON428, line 89) |
| `BC_BRACKETS_2026` | `[[50363,0.056],[100728,0.077],[115648,0.105],[140430,0.1229],[190405,0.147],[265545,0.168],[null,0.205]]` | [bc-individual-return](https://www.openaccountants.com/skills/bc-individual-return) | Rates, bands and thresholds / 2026 brackets and rates |
| `BC_BRACKETS_2025` | `[[49279,0.0506],[98560,0.077],[113158,0.105],[137407,0.1229],[186306,0.147],[259829,0.168],[null,0.205]]` | [bc-individual-return](https://www.openaccountants.com/skills/bc-individual-return) | Rates, bands and thresholds / 2025 figures (for 2025 returns), as printed on Form BC428 2025 |
| `BC_CREDIT_RATE_2026` | `0.056` | [bc-individual-return](https://www.openaccountants.com/skills/bc-individual-return) | Rates, bands and thresholds / 2026 brackets and rates |
| `BC_CREDIT_RATE_2025` | `0.0506` | [bc-individual-return](https://www.openaccountants.com/skills/bc-individual-return) | Rates, bands and thresholds / 2025 figures |
| `BC_BPA_2026` | `13216` | [bc-individual-return](https://www.openaccountants.com/skills/bc-individual-return) | 2026 basic non-refundable credits |
| `BC_BPA_2025` | `12932` | [bc-individual-return](https://www.openaccountants.com/skills/bc-individual-return) | Rates, bands and thresholds / 2025 figures |
| `BC_CPP_EI_CREDITS` | `true` | [bc-individual-return](https://www.openaccountants.com/skills/bc-individual-return) | 2026 basic non-refundable credits |
| `BC_TAX_REDUCTION_2026` | `{"basic":690,"threshold":25570,"rate":0.0356}` | [bc-individual-return](https://www.openaccountants.com/skills/bc-individual-return) | 2026 BC tax reduction and other credits |
| `BC_TAX_REDUCTION_2025` | `{"basic":562,"threshold":25020,"rate":0.0356}` | [bc-individual-return](https://www.openaccountants.com/skills/bc-individual-return) | Rates, bands and thresholds / 2025 figures |
| `AB_BRACKETS_2026` | `[[61200,0.08],[154259,0.1],[185111,0.12],[246813,0.13],[370220,0.14],[null,0.15]]` | [ab-individual-return](https://www.openaccountants.com/skills/ab-individual-return) | Rates, bands and thresholds |
| `AB_BRACKETS_2025` | `[[60000,0.08],[151234,0.1],[181481,0.12],[241974,0.13],[362961,0.14],[null,0.15]]` | [ab-individual-return](https://www.openaccountants.com/skills/ab-individual-return) | Rates, bands and thresholds |
| `AB_CREDIT_RATE` | `0.08` | [ab-individual-return](https://www.openaccountants.com/skills/ab-individual-return) | Rates, bands and thresholds |
| `AB_BPA_2026` | `22769` | [ab-individual-return](https://www.openaccountants.com/skills/ab-individual-return) | Rates, bands and thresholds |
| `AB_BPA_2025` | `22323` | [ab-individual-return](https://www.openaccountants.com/skills/ab-individual-return) | Rates, bands and thresholds |
| `AB_CPP_EI_CREDITS` | `true` | [ab-individual-return](https://www.openaccountants.com/skills/ab-individual-return) | The taxable base |
| `AB_SUPPLEMENTAL_CREDIT_2025` | `{"base":4800,"rate":0.25}` | [ab-individual-return](https://www.openaccountants.com/skills/ab-individual-return) | Rates, bands and thresholds |
| `AB_2026_AMOUNTS_RISE` | `0.02` | [ab-individual-return](https://www.openaccountants.com/skills/ab-individual-return) | Rates, bands and thresholds |
| `AB_SUPPLEMENTAL_BASE_2026_NOT_PRINTED` | `4896` | [ab-individual-return](https://www.openaccountants.com/skills/ab-individual-return) | Rates, bands and thresholds |

Skills behind it: [canada-payroll](https://www.openaccountants.com/skills/canada-payroll), [ca-fed-cpp-ei](https://www.openaccountants.com/skills/ca-fed-cpp-ei), [canada-tax-optimization](https://www.openaccountants.com/skills/canada-tax-optimization), [ca-fed-t1-return](https://www.openaccountants.com/skills/ca-fed-t1-return), [on-individual-return](https://www.openaccountants.com/skills/on-individual-return), [bc-individual-return](https://www.openaccountants.com/skills/bc-individual-return), [ab-individual-return](https://www.openaccountants.com/skills/ab-individual-return).

## Worked examples it reproduces

- ca-fed-cpp-ei Tests 1 to 4 (2025): self-employed CPP, line 22200 deduction and line 31000 credit base
- ca-fed-t1-return Examples 1 to 3 (2025): basic federal tax $7,978.82, $0 and $58,640.54
- on-individual-return Example 1 (2026, employee $34,000): Ontario tax $426.18; Example 2 (2025, $180,000, spouse, donations): $19,722.34
- bc-individual-return Example 1 (2026, $42,000): BC tax $1,506.81; Example 2 (2025, $120,000, spouse, donations): $7,275.24
- ab-individual-return Example 1 (2026, $75,000): Alberta tax $4,102.48; Example 2 (2025, $120,000, supplemental credit $59.30): $5,703.50
- canada-payroll (2026): employee maximums CPP $4,230.45, CPP2 $416.00, EI $1,123.07

The platform's tests recompute these from the skills' own worked examples (`worked-examples.test.ts`, not published here because it calls the engine's internal helpers).

## Licence

Code (`index.mjs`, `index.test.mjs`, `source/`): AGPL-3.0-only, like every calculator in this repository. Figures and wording in `rules.json`: the OpenAccountants Guide License v1.0, like the skills. See [LICENSING.md](../../../LICENSING.md).

Source commit: `c2e3c2b9` (OpenAccountants platform, `src/lib/engines`).
