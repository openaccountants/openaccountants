# mt_household_comparison_2026

Malta resident married couple, basis year 2026 (year of assessment 2027) or basis year 2025 (year of assessment 2026): compares the joint computation on the married table, separate computation (article 49A or 50) with each spouse on the single or parent table, and either of those with spouse B's part-time self-employment profit taxed at the final 10% (article 90A, up to EUR 12,000), and says which gives the least tax.

Jurisdiction MT. Tax years 2025 and 2026. Engine version 1.0.0.

This is the same code that answers the compute tool of the OpenAccountants plugin. It is generated from `src/lib/engines/mt-household-comparison-2026.ts` in the OpenAccountants platform at commit `c2e3c2b9`; do not edit it here. The compute tool's answer links to this folder (`inspect.code_url`), so anyone can read the code, the figures and the tests behind it and run them again.

## Files

| File | What it is |
|---|---|
| `index.mjs` | The engine as one ES module with no dependencies (Node 20+). Exports `run(facts)`, `spec`, `rules`, `anchors`, `receiptId`, `quoteFound`, `normaliseLines`. |
| `source/` | The TypeScript files bundled into `index.mjs`, unchanged, with their comments. Read these. |
| `rules.json` | The spec and every figure the engine uses, each with the skill, section and line it was quoted from. |
| `cases.json` | 2 test cases with the exact output the engine gives (1 ok, 1 missing_rule, 0 needs_input). |
| `index.test.mjs` | The tests: `node --test calculators/engines/mt_household_comparison_2026/`. |

`index.mjs` is the files in `source/` with the types removed and bundled together; the bundler may print numbers in short form (`2e5` is 200,000, `.19` is 0.19).

## Run it

```sh
node --test calculators/engines/mt_household_comparison_2026/
```

```js
import { run } from "./calculators/engines/mt_household_comparison_2026/index.mjs";
console.log(JSON.stringify(run({"spouse_a_chargeable_income":94070.42,"spouse_b_chargeable_income":3986,"married_resident_living_together":true,"children":2,"eu_eea_or_long_term_resident":true,"separate_computation_available":true,"spouse_a_parent":true,"spouse_b_parent":true,"spouse_b_part_time_profit":3986,"part_time_eligible":true,"separate_route":"article_50","tax_year":"2026"}), null, 2));
```

To check an answer from the plugin, pass the same facts: `run(facts)` returns the same result, steps and constants, and `receiptId("mt_household_comparison_2026", "1.0.0", facts, run(facts))` equals the `receipt.id` it returned.

## Inputs

| Fact | Type | Required | Default | Description |
|---|---|---|---|---|
| `spouse_a_chargeable_income` | number | yes |  | EUR, spouse A's own chargeable income (after their own expenses and capital allowances), without income taxed at a final rate (15% rent option, property transfers) |
| `spouse_b_chargeable_income` | number | yes |  | EUR, spouse B's own chargeable income on the same basis, INCLUDING any part-time self-employment profit given in spouse_b_part_time_profit |
| `married_resident_living_together` | boolean | yes |  | the two spouses were married to each other, both resident in Malta, and living together in the basis year (anything else is refused) |
| `children` | number | no |  | how many children the couple kept in their custody in the basis year, each not over 18, or not over 23 and in full-time education (0 if none). Maintenance alone does not count for the married tables |
| `eu_eea_or_long_term_resident` | boolean | no |  | needed when there are children in basis year 2026: at least one spouse is an EU/EEA national or holds long-term resident status |
| `children_born_and_resident_in_malta` | number | no |  | needed only when neither spouse is an EU/EEA national or long-term resident: how many of those children were born in Malta and are resident in Malta |
| `separate_computation_available` | boolean | no |  | needed: the couple can be taxed separately this year (the responsible spouse may opt for a separate computation under article 50, or a separate return election under article 49A is open to them). If false, only the joint options are compared |
| `spouse_a_parent` | boolean | no |  | needed for separate computation when there are children: spouse A kept those children in custody (own child, spouse's child or certified cohabitant's child) or paid maintenance for their own child under article 12(1)(t) |
| `spouse_b_parent` | boolean | no |  | needed for separate computation when there are children: the same test for spouse B |
| `spouse_b_part_time_profit` | number | no | `0` | EUR, the part of spouse_b_chargeable_income that is part-time SELF-EMPLOYMENT profit (article 4(1)(a)). Part-time employment income is not handled |
| `part_time_eligible` | boolean | no |  | needed when there is part-time profit: spouse B meets the skill's part-time conditions (resident; in full-time employment registered with Jobsplus, a pensioner taxed in Malta, or a full-time student or apprentice, or living with a spouse who is; the work registered with Jobsplus, at most two part-time employees, proper books, done for someone other than the full-time employer, VAT-registered unless not required or exempt) |
| `separate_route` | `article_50`, `article_49A` | no |  | needed when separate computation and the part-time 10% are both in play: article_50 (the responsible spouse opts for a separate computation) or article_49A (a separate return election) |
| `spouse_b_part_time_in_own_right` | boolean | no |  | needed for the article_49A route with part-time profit: spouse B is in full-time employment registered with Jobsplus, a pensioner taxed in Malta, or a full-time student or apprentice, and does not qualify only as the spouse of such a person |
| `income_or_deductions_to_allocate` | boolean | no | `false` | either spouse has income other than their own employment or business income (rent, interest, dividends, jointly owned income) or a deduction not tied to one spouse's own income. The skill does not say how these are allocated on separate computation, so the separate options are then refused |
| `credits_or_other_deductions` | boolean | no | `false` | a spouse claims a tax credit (for example a pension or personal retirement scheme credit) or a deduction not already taken off the chargeable incomes above (for example a child or school-fee deduction). Not in the skill, so the whole comparison is refused |
| `tax_year` | `2025`, `2026` | yes |  | the BASIS year: the calendar year the income was earned (2026 income is year of assessment 2027). This engine has figures for basis years 2025 and 2026 only; any other year is refused |

A fact left out takes its default, and the output lists it in `defaults_assumed`. A fact with no default must be given.

## Outputs

`run(facts)` returns one of three statuses:

- `ok`: `headline` (label, value, currency), `lines`, `steps`, `inputs_used`, `constants_used` (every figure used, with its skill line), `assumptions`, `skill_anchors_reproduced`, `notes`, `defaults_assumed`, `tax_year`.
- `missing_rule`: the engine refuses because no OpenAccountants skill serves a figure it would need. It says `what` is missing and `why`, and never guesses.
- `needs_input`: a fact is missing or invalid. It says `what` and returns the `schema` of the facts.

| Line | Unit |
|---|---|
| `options` | each option: status (computed, not_available, missing_rule), the table(s), chargeable income, tax on the return, the 10% final tax, total |
| `lowest` | the option key(s) with the least total tax |
| `lowest_tax` | EUR |
| `saving_against_joint` | EUR, joint total less the lowest total |

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
| `SEPARATE_COMPUTATION_TABLES` | `true` | [malta-income-tax](https://www.openaccountants.com/skills/malta-income-tax) | Who gets which table |
| `PARENT_TABLE_TEST` | `true` | [malta-income-tax](https://www.openaccountants.com/skills/malta-income-tax) | Who gets which table |
| `MARRIED_CHILD_TABLES_CUSTODY` | `true` | [malta-income-tax](https://www.openaccountants.com/skills/malta-income-tax) | Who gets which table |
| `PARENT_CHILD_TABLES_CUSTODY` | `true` | [malta-income-tax](https://www.openaccountants.com/skills/malta-income-tax) | Who gets which table |
| `CHILD_TABLES_FALLBACK` | `true` | [malta-income-tax](https://www.openaccountants.com/skills/malta-income-tax) | Who gets which table |
| `PART_TIME_FINAL_RATE` | `0.1` | [malta-income-tax](https://www.openaccountants.com/skills/malta-income-tax) | Part-time work final tax |
| `PART_TIME_SELF_EMPLOYED_CAP` | `12000` | [malta-income-tax](https://www.openaccountants.com/skills/malta-income-tax) | Part-time work final tax |
| `PART_TIME_SPOUSE_EXTENSION` | `true` | [malta-income-tax](https://www.openaccountants.com/skills/malta-income-tax) | Part-time work final tax |
| `PART_TIME_OPT_OUT` | `true` | [malta-income-tax](https://www.openaccountants.com/skills/malta-income-tax) | Part-time work final tax |
| `PART_TIME_PAYMENT_DATE` | `"30 April"` | [malta-income-tax](https://www.openaccountants.com/skills/malta-income-tax) | Part-time work final tax |

Skills behind it: [malta-income-tax](https://www.openaccountants.com/skills/malta-income-tax).

## Worked examples it reproduces

- malta-income-tax Case 2: married, two children, EUR 40,000 joint -> EUR 3,425 (2026) against EUR 5,450 (2025)
- malta-income-tax Case 3: part-time profit EUR 15,000 -> final tax EUR 1,200 on EUR 12,000, EUR 3,000 into the return

The platform's tests recompute these from the skills' own worked examples (`worked-examples.test.ts`, not published here because it calls the engine's internal helpers).

## Licence

Code (`index.mjs`, `index.test.mjs`, `source/`): AGPL-3.0-only, like every calculator in this repository. Figures and wording in `rules.json`: the OpenAccountants Guide License v1.0, like the skills. See [LICENSING.md](../../../LICENSING.md).

Source commit: `c2e3c2b9` (OpenAccountants platform, `src/lib/engines`).
