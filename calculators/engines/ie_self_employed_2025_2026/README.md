# ie_self_employed_2025_2026

Ireland, self-employed sole trader, tax year 2025 or 2026: income tax (bands, personal, earned income and employee credits, pension relief), USC, PRSI Class S, the Form 11 balance, and the minimum preliminary tax for the next year (lowest of 90% of next year, 100% of this year, 105% of the year before for direct debit).

Jurisdiction IE. Tax years 2025 and 2026. Engine version 1.0.0.

This is the same code that answers the compute tool of the OpenAccountants plugin. It is generated from `src/lib/engines/ie-self-employed-2025-2026.ts` in the OpenAccountants platform at commit `c2e3c2b9`; do not edit it here. The compute tool's answer links to this folder (`inspect.code_url`), so anyone can read the code, the figures and the tests behind it and run them again.

## Files

| File | What it is |
|---|---|
| `index.mjs` | The engine as one ES module with no dependencies (Node 20+). Exports `run(facts)`, `spec`, `rules`, `anchors`, `receiptId`, `quoteFound`, `normaliseLines`. |
| `source/` | The TypeScript files bundled into `index.mjs`, unchanged, with their comments. Read these. |
| `rules.json` | The spec and every figure the engine uses, each with the skill, section and line it was quoted from. |
| `cases.json` | 2 test cases with the exact output the engine gives (1 ok, 1 missing_rule, 0 needs_input). |
| `index.test.mjs` | The tests: `node --test calculators/engines/ie_self_employed_2025_2026/`. |

`index.mjs` is the files in `source/` with the types removed and bundled together; the bundler may print numbers in short form (`2e5` is 200,000, `.19` is 0.19).

## Run it

```sh
node --test calculators/engines/ie_self_employed_2025_2026/
```

```js
import { run } from "./calculators/engines/ie_self_employed_2025_2026/index.mjs";
console.log(JSON.stringify(run({"tax_year":"2025","status":"single","trading_profit":36500}), null, 2));
```

To check an answer from the plugin, pass the same facts: `run(facts)` returns the same result, steps and constants, and `receiptId("ie_self_employed_2025_2026", "1.0.0", facts, run(facts))` equals the `receipt.id` it returned.

## Inputs

| Fact | Type | Required | Default | Description |
|---|---|---|---|---|
| `tax_year` | `2025`, `2026` | yes |  | the tax year the question is about. This engine has figures for 2025 and 2026 only; any other year is refused |
| `status` | `single`, `married_one_income`, `married_two_incomes`, `single_parent` | yes |  | single (not widowed); single_parent (single and qualifies for the Single Person Child Carer Credit); married_one_income (married or civil partners, jointly assessed, the spouse has no income); married_two_incomes (jointly assessed, the spouse has a PAYE salary) |
| `trading_profit` | number | yes |  | EUR, this person's adjusted Case I or II trading profit for the year after capital allowances, before pension contributions (an active sole trader) |
| `capital_allowances` | number | no | `0` | EUR capital allowances already deducted in trading_profit (used only for the PRSI EUR 5,000 floor, which is tested before capital allowances) |
| `other_income` | number | no | `0` | EUR this person's other taxable income: a PAYE salary (set other_income_is_paye true) or non-PAYE income such as Irish rental profit. Leave out social welfare payments, DIRT-paid deposit interest and other income exempt from USC or PRSI |
| `other_income_is_paye` | boolean | no |  | needed when other_income is more than 0: true if it is a PAYE salary from an employment |
| `spouse_income` | number | no |  | needed for married_two_incomes: EUR the spouse's PAYE salary for the year |
| `spouse_income_is_paye` | boolean | no |  | needed for married_two_incomes: true if the spouse's income is all PAYE salary (any other spouse income is refused) |
| `paye_income_tax_deducted` | number | no |  | needed when a PAYE salary is included: EUR income tax deducted under PAYE in the year from the salaries in this assessment (this person's and, for married_two_incomes, the spouse's) |
| `paye_usc_deducted` | number | no |  | needed when this person has a PAYE salary: EUR USC deducted from it in the year |
| `pension_contributions` | number | no | `0` | EUR this person paid into a personal pension (RAC or PRSA) for the year; relieved for income tax only, within the age limit (2026 only) |
| `age` | number | no |  | needed when pension_contributions is more than 0: this person's age, for the pension relief percentage |
| `age_65_plus` | boolean | no | `false` | this person or the spouse is aged 65 or over in the year (refused: the skills do not settle these cases) |
| `medical_card` | boolean | no | `false` | this person held a full medical card (not a GP visit card) at any time in the year and told Revenue |
| `home_carer_credit` | boolean | no | `false` | the couple claims the Home Carer Tax Credit (refused: the skill states only its maximum) |
| `preliminary_tax_paid` | number | no | `0` | EUR preliminary tax already paid for tax_year |
| `next_year_liability_estimate` | number | no |  | EUR expected income tax + USC + PRSI for the year after tax_year, after credits and tax deducted at source (for the 90% test). For 2026, run this engine for tax_year 2026 with the expected 2026 figures. Left out, the 90% test is not used |
| `pays_by_direct_debit` | boolean | no | `false` | pays next year's preliminary tax by monthly direct debit (the 105% test applies only then) |
| `liability_year_before` | number | no |  | EUR final income tax + USC + PRSI for the year before tax_year (2024 for tax_year 2025), after credits and tax deducted at source; needed for the 105% direct debit test |

A fact left out takes its default, and the output lists it in `defaults_assumed`. A fact with no default must be given.

## Outputs

`run(facts)` returns one of three statuses:

- `ok`: `headline` (label, value, currency), `lines`, `steps`, `inputs_used`, `constants_used` (every figure used, with its skill line), `assumptions`, `skill_anchors_reproduced`, `notes`, `defaults_assumed`, `tax_year`.
- `missing_rule`: the engine refuses because no OpenAccountants skill serves a figure it would need. It says `what` is missing and `why`, and never guesses.
- `needs_input`: a fact is missing or invalid. It says `what` and returns the `schema` of the facts.

| Line | Unit |
|---|---|
| `taxable_income` | EUR |
| `rate_band` | EUR at 20% |
| `gross_income_tax` | EUR |
| `tax_credits` | EUR |
| `income_tax` | EUR |
| `usc` | EUR |
| `prsi_class_s` | EUR |
| `total_liability` | EUR |
| `tax_deducted_at_source` | EUR |
| `net_liability` | EUR |
| `balance_due` | EUR (negative = overpaid) |
| `preliminary_tax` | options, minimum and due date for the next year |
| `pay_by_return_date` | EUR balance due plus minimum preliminary tax |

## What it refuses

- Any tax year other than 2025 and 2026 (`missing_rule`). It never applies one year's figures to another year.
- A missing, negative or wrongly typed fact (`needs_input`).

## Figures

Every figure is quoted from an OpenAccountants skill. The skill is the authority on the method; the official source it names is the authority on the number. The exact line each figure was quoted from is its `quote` in [`rules.json`](rules.json), and a daily check in the platform confirms each quoted line is still in the skill as served.

| Name | Value | Skill | Section |
|---|---|---|---|
| `BAND_SINGLE` | `44000` | [ie-income-tax-form11](https://www.openaccountants.com/skills/ie-income-tax-form11) | Rates, bands and thresholds |
| `BAND_SINGLE_PARENT` | `48000` | [ie-income-tax-form11](https://www.openaccountants.com/skills/ie-income-tax-form11) | Rates, bands and thresholds |
| `BAND_MARRIED` | `53000` | [ie-income-tax-form11](https://www.openaccountants.com/skills/ie-income-tax-form11) | Rates, bands and thresholds |
| `BAND_SECOND_INCOME_INCREASE` | `35000` | [ie-income-tax-form11](https://www.openaccountants.com/skills/ie-income-tax-form11) | Rates, bands and thresholds |
| `INCOME_TAX_RATES` | `[0.2,0.4]` | [ie-income-tax-form11](https://www.openaccountants.com/skills/ie-income-tax-form11) | Rates, bands and thresholds |
| `PERSONAL_CREDITS` | `{"single":2000,"married":4000}` | [ie-income-tax-form11](https://www.openaccountants.com/skills/ie-income-tax-form11) | Rates, bands and thresholds |
| `SINGLE_PERSON_CHILD_CARER_CREDIT` | `1900` | [ie-income-tax-form11](https://www.openaccountants.com/skills/ie-income-tax-form11) | Rates, bands and thresholds |
| `EMPLOYEE_CREDIT` | `2000` | [ie-income-tax-form11](https://www.openaccountants.com/skills/ie-income-tax-form11) | Rates, bands and thresholds |
| `EARNED_INCOME_CREDIT` | `{"max":2000,"rate":0.2}` | [ie-income-tax-form11](https://www.openaccountants.com/skills/ie-income-tax-form11) | Rates, bands and thresholds |
| `EARNED_INCOME_CREDIT_SCOPE` | `true` | [ie-income-tax-form11](https://www.openaccountants.com/skills/ie-income-tax-form11) | The taxable base |
| `HOME_CARER_CREDIT_MAX` | `1950` | [ie-income-tax-form11](https://www.openaccountants.com/skills/ie-income-tax-form11) | Rates, bands and thresholds |
| `AGE_CREDIT` | `{"single":245,"married":490}` | [ie-income-tax-form11](https://www.openaccountants.com/skills/ie-income-tax-form11) | Rates, bands and thresholds |
| `PENSION_RELIEF_PERCENT_BY_AGE` | `[[30,0.15],[40,0.2],[50,0.25],[55,0.3],[60,0.35],[null,0.4]]` | [ie-income-tax-form11](https://www.openaccountants.com/skills/ie-income-tax-form11) | Rates, bands and thresholds |
| `PENSION_EARNINGS_LIMIT` | `115000` | [ie-income-tax-form11](https://www.openaccountants.com/skills/ie-income-tax-form11) | Rates, bands and thresholds |
| `RENT_NOT_RELEVANT_EARNINGS` | `true` | [ie-income-tax-form11](https://www.openaccountants.com/skills/ie-income-tax-form11) | The taxable base |
| `USC_PRSI_BEFORE_PENSION` | `true` | [ie-income-tax-form11](https://www.openaccountants.com/skills/ie-income-tax-form11) | The taxable base |
| `USC_BANDS_2026` | `[[12012,0.005],[16688,0.02],[41344,0.03],[null,0.08]]` | [ie-usc](https://www.openaccountants.com/skills/ie-usc) | Rates, bands and thresholds |
| `USC_BANDS_2025` | `[[12012,0.005],[27382,0.02],[70044,0.03],[null,0.08]]` | [ie-income-tax-form11](https://www.openaccountants.com/skills/ie-income-tax-form11) | Rates, bands and thresholds |
| `USC_EXEMPTION_LIMIT_2026` | `13000` | [ie-usc](https://www.openaccountants.com/skills/ie-usc) | Rates, bands and thresholds |
| `USC_MEDICAL_CARD_2026` | `{"limit":60000,"standard_up_to":28700,"rate":0.02}` | [ie-usc](https://www.openaccountants.com/skills/ie-usc) | Rates, bands and thresholds |
| `USC_NON_PAYE_SURCHARGE_2026` | `{"over":100000,"rate":0.03}` | [ie-usc](https://www.openaccountants.com/skills/ie-usc) | Rates, bands and thresholds |
| `CLASS_S_RATE_2026` | `0.042375` | [ie-prsi-class-s](https://www.openaccountants.com/skills/ie-prsi-class-s) | Rates, bands and thresholds |
| `CLASS_S_MINIMUM_2026` | `650` | [ie-prsi-class-s](https://www.openaccountants.com/skills/ie-prsi-class-s) | Rates, bands and thresholds |
| `CLASS_S_FLOOR_2026` | `5000` | [ie-prsi-class-s](https://www.openaccountants.com/skills/ie-prsi-class-s) | Rates, bands and thresholds |
| `CLASS_S_2025` | `{"rate":0.04125,"minimum":650}` | [ie-income-tax-form11](https://www.openaccountants.com/skills/ie-income-tax-form11) | Rates, bands and thresholds |
| `CLASS_S_FLOOR_TEST` | `true` | [ie-prsi-class-s](https://www.openaccountants.com/skills/ie-prsi-class-s) | Who this applies to |
| `CLASS_S_RECKONABLE_INCOME` | `true` | [ie-prsi-class-s](https://www.openaccountants.com/skills/ie-prsi-class-s) | The taxable base |
| `CLASS_S_AGE` | `66` | [ie-prsi-class-s](https://www.openaccountants.com/skills/ie-prsi-class-s) | Who this applies to |
| `PRELIMINARY_TAX_TESTS_2026` | `{"current":0.9,"preceding":1,"pre_preceding":1.05}` | [ie-preliminary-tax](https://www.openaccountants.com/skills/ie-preliminary-tax) | Rates, bands and thresholds |
| `PRELIMINARY_TAX_WORKING_RULE` | `true` | [ie-preliminary-tax](https://www.openaccountants.com/skills/ie-preliminary-tax) | The taxable base |
| `PRELIMINARY_TAX_DUE_2026` | `"2026-10-31"` | [ie-preliminary-tax](https://www.openaccountants.com/skills/ie-preliminary-tax) | Rates, bands and thresholds |
| `PRELIMINARY_TAX_SHORTFALL_2026` | `true` | [ie-preliminary-tax](https://www.openaccountants.com/skills/ie-preliminary-tax) | Penalties and interest |
| `PRELIMINARY_TAX_TESTS` | `{"current":0.9,"preceding":1,"pre_preceding":1.05}` | [ie-income-tax-form11](https://www.openaccountants.com/skills/ie-income-tax-form11) | Rates, bands and thresholds |
| `RETURN_2026_AND_PRELIMINARY_2027` | `"2027-10-31"` | [ie-income-tax-form11](https://www.openaccountants.com/skills/ie-income-tax-form11) | Deadlines and filing |
| `BALANCE_2026_DUE` | `"2027-10-31"` | [ie-preliminary-tax](https://www.openaccountants.com/skills/ie-preliminary-tax) | Rates, bands and thresholds |

Skills behind it: [ie-income-tax-form11](https://www.openaccountants.com/skills/ie-income-tax-form11), [ie-usc](https://www.openaccountants.com/skills/ie-usc), [ie-prsi-class-s](https://www.openaccountants.com/skills/ie-prsi-class-s), [ie-preliminary-tax](https://www.openaccountants.com/skills/ie-preliminary-tax).

## Worked examples it reproduces

- ie-income-tax-form11 Example 1: single, profit EUR 60,000 (2026) -> income tax EUR 11,200, USC EUR 1,332.82, PRSI EUR 2,542.50, total EUR 15,075.32
- ie-income-tax-form11 Example 2: profit EUR 93,500 after capital allowances, rent EUR 12,000, PRSA EUR 8,000 (2026) -> income tax EUR 26,200, USC EUR 4,635.62, PRSI EUR 4,470.56, total EUR 35,306.18
- ie-usc Example 1: income for USC EUR 56,000 -> USC EUR 1,212.82
- ie-prsi-class-s Example 1: reckonable income EUR 80,000 (2026) -> Class S EUR 3,390.00
- ie-prsi-class-s Example 2: 2025 reckonable income EUR 14,000 -> Class S EUR 650 (minimum)
- ie-preliminary-tax Example 1: 2025 liability EUR 18,400, 2026 estimate EUR 21,000 -> minimum EUR 18,400, pay EUR 20,800
- ie-preliminary-tax Example 2: direct debit, 2024 EUR 12,000, 2025 EUR 30,000, 2026 EUR 15,000 -> minimum EUR 12,600

The platform's tests recompute these from the skills' own worked examples (`worked-examples.test.ts`, not published here because it calls the engine's internal helpers).

## Licence

Code (`index.mjs`, `index.test.mjs`, `source/`): AGPL-3.0-only, like every calculator in this repository. Figures and wording in `rules.json`: the OpenAccountants Guide License v1.0, like the skills. See [LICENSING.md](../../../LICENSING.md).

Source commit: `c2e3c2b9` (OpenAccountants platform, `src/lib/engines`).
