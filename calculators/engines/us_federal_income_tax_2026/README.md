# us_federal_income_tax_2026

US federal individual income tax on Form 1040 for tax year 2025 or 2026: AGI, standard or itemized deduction, the simplified QBI deduction, bracket tax with the 0%/15%/20% rates on qualified dividends and long-term gains, the child tax credit, self-employment tax, Additional Medicare Tax and net investment income tax, plus the estimated-tax safe harbour and due dates. Refuses the alternative minimum tax when it cannot be shown to be zero, QBI above the threshold, the child tax credit above its phase-out start, and 2025 married filing separately.

Jurisdiction US. Tax years 2025 and 2026. Engine version 1.1.0.

This is the same code that answers the compute tool of the OpenAccountants plugin. It is generated from `src/lib/engines/us-federal-income-tax-2026.ts` in the OpenAccountants platform at commit `c2e3c2b9`; do not edit it here. The compute tool's answer links to this folder (`inspect.code_url`), so anyone can read the code, the figures and the tests behind it and run them again.

## Files

| File | What it is |
|---|---|
| `index.mjs` | The engine as one ES module with no dependencies (Node 20+). Exports `run(facts)`, `spec`, `rules`, `anchors`, `receiptId`, `quoteFound`, `normaliseLines`. |
| `source/` | The TypeScript files bundled into `index.mjs`, unchanged, with their comments. Read these. |
| `rules.json` | The spec and every figure the engine uses, each with the skill, section and line it was quoted from. |
| `cases.json` | 5 test cases with the exact output the engine gives (2 ok, 2 missing_rule, 1 needs_input). |
| `index.test.mjs` | The tests: `node --test calculators/engines/us_federal_income_tax_2026/`. |

`index.mjs` is the files in `source/` with the types removed and bundled together; the bundler may print numbers in short form (`2e5` is 200,000, `.19` is 0.19).

## Run it

```sh
node --test calculators/engines/us_federal_income_tax_2026/
```

```js
import { run } from "./calculators/engines/us_federal_income_tax_2026/index.mjs";
console.log(JSON.stringify(run({"filing_status":"single","wages":60000,"tax_year":"2026"}), null, 2));
```

To check an answer from the plugin, pass the same facts: `run(facts)` returns the same result, steps and constants, and `receiptId("us_federal_income_tax_2026", "1.1.0", facts, run(facts))` equals the `receipt.id` it returned.

## Inputs

| Fact | Type | Required | Default | Description |
|---|---|---|---|---|
| `filing_status` | `single`, `married_filing_jointly`, `married_filing_separately`, `head_of_household` | yes |  | filing status at the end of the year (a qualifying surviving spouse is not covered) |
| `wages` | number | no | `0` | USD, Form W-2 box 1 (taxable wages) |
| `w2_social_security_wages` | number | no |  | USD, Form W-2 box 3. Left out, it is taken as equal to wages. Used only for the self-employment tax wage base |
| `w2_medicare_wages` | number | no |  | USD, Form W-2 box 5. Left out, it is taken as equal to wages. Used only for the Additional Medicare Tax |
| `self_employment_net_profit` | number | no | `0` | USD, Schedule C line 31 net profit (all Schedule C businesses together; a loss is not covered) |
| `self_employed_retirement_and_health_deductions` | number | no | `0` | USD, Schedule 1 lines 16 and 17 for that business: SEP, SIMPLE or solo 401(k) deduction plus self-employed health insurance. They reduce AGI and QBI |
| `other_adjustments` | number | no | `0` | USD, other Schedule 1 adjustments not tied to the business (HSA, IRA, student loan interest, educator expenses) |
| `interest` | number | no | `0` | USD, taxable interest (Form 1040 line 2b) |
| `ordinary_dividends` | number | no | `0` | USD, ordinary dividends (line 3b), qualified dividends included |
| `qualified_dividends` | number | no | `0` | USD, qualified dividends (line 3a), part of ordinary_dividends |
| `short_term_capital_gains` | number | no | `0` | USD, net short-term capital gain (taxed as ordinary income). If short-term losses exceed short-term gains, subtract the net loss from long_term_capital_gains and enter 0 |
| `long_term_capital_gains` | number | no | `0` | USD, net long-term capital gain on assets held more than one year, after any net short-term loss, with no 28% collectibles or 25% section 1250 gain. A net capital loss is not covered |
| `other_ordinary_income` | number | no | `0` | USD, other taxable income that is not investment income (unemployment compensation, taxable pensions and IRA distributions, prizes). Rents, royalties and passive income are not covered |
| `itemized_deductions` | number | no |  | USD, Schedule A total after the SALT cap and every other Schedule A limit. Left out, the standard deduction is used; given, the larger of the two is used |
| `itemized_state_and_local_taxes` | number | no |  | USD, the state and local taxes included in itemized_deductions (after the cap). Used only to show the alternative minimum tax is zero; left out, all itemized deductions are treated as taxes (the cautious reading) |
| `cash_charitable_gifts` | number | no | `0` | USD, cash gifts to public charities. Used only in 2026 when the standard deduction is taken (up to USD 1,000, or USD 2,000 married filing jointly); an itemizer includes gifts in itemized_deductions |
| `dependents_under_17` | number | no | `0` | qualifying children under 17 at the end of the year, each with a social security number (child tax credit) |
| `materially_participates` | boolean | no |  | 2026 only, asked when it changes the answer: the taxpayer materially participates in the Schedule C business (for the USD 400 minimum QBI deduction) |
| `prior_year_tax` | number | no |  | USD, total tax on last year's return (Form 1040 line 24), for the estimated-tax safe harbour. Left out, no safe harbour is computed |
| `prior_year_agi` | number | no |  | USD, last year's AGI (Form 1040 line 11b), needed with prior_year_tax for the 100% or 110% test |
| `tax_year` | `2025`, `2026` | yes |  | the tax year the question is about. This engine has figures for 2025 and 2026 only; any other year is refused |

A fact left out takes its default, and the output lists it in `defaults_assumed`. A fact with no default must be given.

## Outputs

`run(facts)` returns one of three statuses:

- `ok`: `headline` (label, value, currency), `lines`, `steps`, `inputs_used`, `constants_used` (every figure used, with its skill line), `assumptions`, `skill_anchors_reproduced`, `notes`, `defaults_assumed`, `tax_year`.
- `missing_rule`: the engine refuses because no OpenAccountants skill serves a figure it would need. It says `what` is missing and `why`, and never guesses.
- `needs_input`: a fact is missing or invalid. It says `what` and returns the `schema` of the facts.

| Line | Unit |
|---|---|
| `agi` | USD, adjusted gross income |
| `deduction_used` | standard or itemized |
| `deduction` | USD |
| `qbi_deduction` | USD |
| `taxable_income` | USD |
| `ordinary_tax` | USD, bracket tax on ordinary taxable income |
| `preferential_tax` | USD, tax on qualified dividends and long-term gains at 0%/15%/20% |
| `income_tax` | USD, Form 1040 line 16 |
| `child_tax_credit` | USD, the non-refundable part used |
| `se_tax` | USD |
| `additional_medicare_tax` | USD |
| `net_investment_income_tax` | USD |
| `total_tax` | USD, Form 1040 line 24 |
| `estimated_tax` | required annual payment, instalment and due dates (when prior_year_tax is given) |

## What it refuses

- Any tax year other than 2025 and 2026 (`missing_rule`). It never applies one year's figures to another year.
- A missing, negative or wrongly typed fact (`needs_input`).
- alternative minimum tax (`missing_rule`)

## Figures

Every figure is quoted from an OpenAccountants skill. The skill is the authority on the method; the official source it names is the authority on the number. The exact line each figure was quoted from is its `quote` in [`rules.json`](rules.json), and a daily check in the platform confirms each quoted line is still in the skill as served.

| Name | Value | Skill | Section |
|---|---|---|---|
| `RATE_SCHEDULE_SINGLE_2026` | `[[12400,0.1],[50400,0.12],[105700,0.22],[201775,0.24],[256225,0.32],[640600,0.35],[null,0.37]]` | [us-federal-income-tax-return-1040](https://www.openaccountants.com/skills/us-federal-income-tax-return-1040) | Tax year 2026 rate schedules |
| `RATE_SCHEDULE_MFJ_2026` | `[[24800,0.1],[100800,0.12],[211400,0.22],[403550,0.24],[512450,0.32],[768700,0.35],[null,0.37]]` | [us-federal-income-tax-return-1040](https://www.openaccountants.com/skills/us-federal-income-tax-return-1040) | Tax year 2026 rate schedules |
| `RATE_SCHEDULE_MFS_2026` | `[[12400,0.1],[50400,0.12],[105700,0.22],[201775,0.24],[256225,0.32],[384350,0.35],[null,0.37]]` | [us-federal-income-tax-return-1040](https://www.openaccountants.com/skills/us-federal-income-tax-return-1040) | Tax year 2026 rate schedules |
| `RATE_SCHEDULE_HOH_2026` | `[[17700,0.1],[67450,0.12],[105700,0.22],[201750,0.24],[256200,0.32],[640600,0.35],[null,0.37]]` | [us-federal-income-tax-return-1040](https://www.openaccountants.com/skills/us-federal-income-tax-return-1040) | Tax year 2026 rate schedules |
| `RATE_SCHEDULE_SINGLE_2025` | `[[11925,0.1],[48475,0.12],[103350,0.22],[197300,0.24],[250525,0.32],[626350,0.35],[null,0.37]]` | [us-form-1040-individual-return](https://www.openaccountants.com/skills/us-form-1040-individual-return) | 2.2 Ordinary income tax brackets — §1(j) (post-TCJA, OBBBA-permanent) |
| `RATE_SCHEDULE_MFJ_2025` | `[[23850,0.1],[96950,0.12],[206700,0.22],[394600,0.24],[501050,0.32],[751600,0.35],[null,0.37]]` | [us-form-1040-individual-return](https://www.openaccountants.com/skills/us-form-1040-individual-return) | 2.2 Ordinary income tax brackets — §1(j) (post-TCJA, OBBBA-permanent) |
| `RATE_SCHEDULE_HOH_2025` | `[[17000,0.1],[64850,0.12],[103350,0.22],[197300,0.24],[250500,0.32],[626350,0.35],[null,0.37]]` | [us-form-1040-individual-return](https://www.openaccountants.com/skills/us-form-1040-individual-return) | 2.2 Ordinary income tax brackets — §1(j) (post-TCJA, OBBBA-permanent) |
| `STANDARD_DEDUCTION_2026` | `{"single":16100,"married_filing_jointly":32200,"married_filing_separately":16100,"head_of_household":24150}` | [us-federal-income-tax-return-1040](https://www.openaccountants.com/skills/us-federal-income-tax-return-1040) | Tax year 2026 deductions, credits and other amounts |
| `STANDARD_DEDUCTION_2025` | `{"single":15750,"married_filing_jointly":31500,"married_filing_separately":15750,"head_of_household":23625}` | [us-form-1040-individual-return](https://www.openaccountants.com/skills/us-form-1040-individual-return) | 2.1 Standard deduction (§63(c)) |
| `NON_ITEMIZER_CASH_GIFTS_2026` | `{"other":1000,"joint":2000}` | [us-federal-income-tax-return-1040](https://www.openaccountants.com/skills/us-federal-income-tax-return-1040) | Changes made by Public Law 119-21 that apply to a tax year 2026 return |
| `ITEMIZED_LIMIT_37_PERCENT_BAND_2026` | `0.05405405405405406` | [us-federal-income-tax-return-1040](https://www.openaccountants.com/skills/us-federal-income-tax-return-1040) | Changes made by Public Law 119-21 that apply to a tax year 2026 return |
| `QBI_RATE` | `0.2` | [us-qbi-deduction](https://www.openaccountants.com/skills/us-qbi-deduction) | Rates, bands and thresholds |
| `QBI_SIMPLIFIED_METHOD` | `true` | [us-qbi-deduction](https://www.openaccountants.com/skills/us-qbi-deduction) | Rates, bands and thresholds; Step 3: where taxable income sits |
| `QBI_DEFINITION` | `true` | [us-qbi-deduction](https://www.openaccountants.com/skills/us-qbi-deduction) | Step 1: qualified business income for each business; Step 2: taxable income before the QBI deduction |
| `QBI_THRESHOLD_2026` | `{"single":201750,"married_filing_jointly":403500,"married_filing_separately":201775,"head_of_household":201750}` | [us-qbi-deduction](https://www.openaccountants.com/skills/us-qbi-deduction) | Rates, bands and thresholds |
| `QBI_THRESHOLD_2025` | `{"single":197300,"married_filing_jointly":394600,"married_filing_separately":197300,"head_of_household":197300}` | [us-qbi-deduction](https://www.openaccountants.com/skills/us-qbi-deduction) | Section 3 — Year-specific figures table for tax year 2025 |
| `QBI_MINIMUM_2026` | `{"minimum":400,"qbi_needed":1000}` | [us-qbi-deduction](https://www.openaccountants.com/skills/us-qbi-deduction) | Rates, bands and thresholds; Step 7: combine, cap, then the minimum |
| `CAPITAL_GAIN_RATES_2026` | `{"rates":[0,0.15,0.2],"ceilings":{"single":[49450,545500],"married_filing_jointly":[98900,613700],"married_filing_separately":[49450,306850],"head_of_household":[66200,579600]}}` | [us-capital-gains](https://www.openaccountants.com/skills/us-capital-gains) | Rates, bands and thresholds |
| `CAPITAL_GAIN_RATES_2025` | `{"rates":[0,0.15,0.2],"ceilings":{"single":[48350,533400],"married_filing_jointly":[96700,600050],"married_filing_separately":[48350,300000],"head_of_household":[64750,566700]}}` | [us-capital-gains](https://www.openaccountants.com/skills/us-capital-gains) | 2025 returns (tax year 2025, extended deadline 15 October 2026) |
| `CAPITAL_GAIN_STACKING` | `true` | [us-capital-gains](https://www.openaccountants.com/skills/us-capital-gains) | Step 5: split the long-term gain into rate groups; Step 6: stack the gain on top of ordinary income |
| `CHILD_TAX_CREDIT_2026` | `{"per_child":2200,"refundable_per_child":1700}` | [us-federal-income-tax-return-1040](https://www.openaccountants.com/skills/us-federal-income-tax-return-1040) | Tax year 2026 deductions, credits and other amounts |
| `CHILD_TAX_CREDIT_2025` | `{"per_child":2200,"refundable_per_child":1700}` | [us-form-1040-individual-return](https://www.openaccountants.com/skills/us-form-1040-individual-return) | 2.9 Other OBBBA changes |
| `CHILD_TAX_CREDIT_PHASEOUT_START` | `{"joint":400000,"other":200000}` | [us-form-1040-individual-return](https://www.openaccountants.com/skills/us-form-1040-individual-return) | 2.9 Other OBBBA changes |
| `CHILD_TAX_CREDIT_PERMANENT` | `true` | [us-2026-federal-tax-changes](https://www.openaccountants.com/skills/us-2026-federal-tax-changes) | Boundary and exception table / Families |
| `AMT_EXEMPTION_2026` | `{"exemption":{"single":90100,"married_filing_jointly":140200,"married_filing_separately":70100,"head_of_household":90100},"phaseout_start":{"single":500000,"married_filing_jointly":1000000,"married_filing_separately":500000,"head_of_household":500000}}` | [us-federal-income-tax-return-1040](https://www.openaccountants.com/skills/us-federal-income-tax-return-1040) | Tax year 2026 deductions, credits and other amounts |
| `AMT_EXEMPTION_2025` | `{"exemption":{"single":88100,"married_filing_jointly":137000,"married_filing_separately":68500,"head_of_household":88100},"phaseout_start":{"single":626350,"married_filing_jointly":1252700,"married_filing_separately":626350,"head_of_household":626350}}` | [us-form-1040-individual-return](https://www.openaccountants.com/skills/us-form-1040-individual-return) | 2.4 AMT exemption — §55(d) (post-TCJA, OBBBA-permanent) |
| `AMT_TOP_RATE` | `0.28` | [us-form-1040-individual-return](https://www.openaccountants.com/skills/us-form-1040-individual-return) | 2.4 AMT exemption — §55(d) (post-TCJA, OBBBA-permanent) |
| `AMT_COMPUTATION_STEPS` | `true` | [us-form-1040-individual-return](https://www.openaccountants.com/skills/us-form-1040-individual-return) | 9.2 AMT computation flow |
| `ADDITIONAL_MEDICARE_2026` | `{"rate":0.009,"threshold":{"single":200000,"married_filing_jointly":250000,"married_filing_separately":125000,"head_of_household":200000}}` | [us-schedule-c-and-se-computation](https://www.openaccountants.com/skills/us-schedule-c-and-se-computation) | Rates, bands and thresholds; Form 8959: Additional Medicare Tax on self-employment income |
| `ADDITIONAL_MEDICARE_2025` | `{"rate":0.009,"threshold":{"single":200000,"married_filing_jointly":250000,"married_filing_separately":125000,"head_of_household":200000}}` | [us-form-1040-individual-return](https://www.openaccountants.com/skills/us-form-1040-individual-return) | 2.6 Additional Medicare Tax — §3101(b)(2) and §1401(b)(2) |
| `NET_INVESTMENT_INCOME_TAX` | `{"rate":0.038,"threshold":{"single":200000,"married_filing_jointly":250000,"married_filing_separately":125000,"head_of_household":200000}}` | [us-capital-gains](https://www.openaccountants.com/skills/us-capital-gains) | Rates, bands and thresholds; Step 8: the net investment income tax |
| `NET_INVESTMENT_INCOME_ITEMS` | `true` | [us-capital-gains](https://www.openaccountants.com/skills/us-capital-gains) | Step 8: the net investment income tax |
| `NIIT_SAME_FOR_2025` | `true` | [us-capital-gains](https://www.openaccountants.com/skills/us-capital-gains) | 2025 returns (tax year 2025, extended deadline 15 October 2026) |
| `SAFE_HARBOUR_2026` | `{"current":0.9,"prior":1,"prior_high":1.1,"agi_limit":150000,"agi_limit_mfs":75000}` | [us-quarterly-estimated-tax](https://www.openaccountants.com/skills/us-quarterly-estimated-tax) | Rates, bands and thresholds; Boundary and exception table |
| `ESTIMATED_TAX_DUE_DATES_2026` | `["2026-04-15","2026-06-15","2026-09-15","2027-01-15"]` | [us-quarterly-estimated-tax](https://www.openaccountants.com/skills/us-quarterly-estimated-tax) | Rates, bands and thresholds |
| `SAFE_HARBOUR_2025` | `{"current":0.9,"prior":1,"prior_high":1.1,"agi_limit":150000,"agi_limit_mfs":75000}` | [us-form-1040-individual-return](https://www.openaccountants.com/skills/us-form-1040-individual-return) | 15. Estimated tax — §6654 |
| `ESTIMATED_TAX_DUE_DATES_2025` | `["2025-04-15","2025-06-16","2025-09-15","2026-01-15"]` | [us-quarterly-estimated-tax](https://www.openaccountants.com/skills/us-quarterly-estimated-tax) | Section 1 -- Quick reference |
| `QUARTERLY_INSTALMENT_SHARE` | `0.25` | [us-quarterly-estimated-tax](https://www.openaccountants.com/skills/us-quarterly-estimated-tax) | Rates, bands and thresholds |
| `ZERO_PRIOR_YEAR_TAX` | `true` | [us-quarterly-estimated-tax](https://www.openaccountants.com/skills/us-quarterly-estimated-tax) | Step 1: is anything required? |
| `NET_EARNINGS_FACTOR` | `0.9235` | [us-schedule-c-and-se-computation](https://www.openaccountants.com/skills/us-schedule-c-and-se-computation) | Rates, bands and thresholds |
| `MIN_NET_EARNINGS` | `400` | [us-schedule-c-and-se-computation](https://www.openaccountants.com/skills/us-schedule-c-and-se-computation) | Rates, bands and thresholds |
| `SS_RATE` | `0.124` | [us-schedule-c-and-se-computation](https://www.openaccountants.com/skills/us-schedule-c-and-se-computation) | Rates, bands and thresholds |
| `WAGE_BASE` | `{"2025":176100,"2026":184500}` | [us-tax-workflow-base](https://www.openaccountants.com/skills/us-tax-workflow-base) | Figures for 2026, with years |
| `MEDICARE_RATE` | `0.029` | [us-schedule-c-and-se-computation](https://www.openaccountants.com/skills/us-schedule-c-and-se-computation) | Rates, bands and thresholds |
| `DEDUCTIBLE_SHARE` | `0.5` | [us-schedule-c-and-se-computation](https://www.openaccountants.com/skills/us-schedule-c-and-se-computation) | Rates, bands and thresholds |

Skills behind it: [us-federal-income-tax-return-1040](https://www.openaccountants.com/skills/us-federal-income-tax-return-1040), [us-form-1040-individual-return](https://www.openaccountants.com/skills/us-form-1040-individual-return), [us-qbi-deduction](https://www.openaccountants.com/skills/us-qbi-deduction), [us-capital-gains](https://www.openaccountants.com/skills/us-capital-gains), [us-2026-federal-tax-changes](https://www.openaccountants.com/skills/us-2026-federal-tax-changes), [us-schedule-c-and-se-computation](https://www.openaccountants.com/skills/us-schedule-c-and-se-computation), [us-quarterly-estimated-tax](https://www.openaccountants.com/skills/us-quarterly-estimated-tax), [us-tax-workflow-base](https://www.openaccountants.com/skills/us-tax-workflow-base).

## Worked examples it reproduces

- us-form-1040-individual-return Example A (2025, single): taxable income $83,400, tax $12,716
- us-form-1040-individual-return Example B (2025, MFJ, itemized $67,300, two children): tax $37,852, CTC $4,400, NIIT $236, Additional Medicare $270, total tax $33,958
- us-form-1040-individual-return Example D (2025, single): regular tax $40,840, NIIT about $1,210 (the ISO AMT is outside this engine)
- us-federal-return-assembly Case A (2025): AGI $86,922.27, QBI deduction $14,234.45, taxable income $56,937.82, SE tax $16,955.46
- us-federal-return-assembly Case C (2026): QBI $1,500 -> $400 minimum; QBI $999 -> $199.80
- us-federal-income-tax-return-1040 worked decision (2026, MFJ, AGI $200,000): standard route $34,200 -> tax $25,900; itemized $30,000 -> $26,824
- us-capital-gains Case 1 (2026, single, taxable income $70,000 with $40,000 gain): $3,082.50 on the gain
- us-capital-gains Case 2 (2026, MFJ, MAGI $300,000, NII $80,000): NIIT $1,900
- us-capital-gains Case 7 (2025, MFJ, taxable income $120,000 with $30,000 gain): $3,495 on the gain
- us-quarterly-estimated-tax Examples 1 and 2: required annual payment $18,000 (quarterly $4,500); $46,200 (quarterly $11,550)

The platform's tests recompute these from the skills' own worked examples (`worked-examples.test.ts`, not published here because it calls the engine's internal helpers).

## Licence

Code (`index.mjs`, `index.test.mjs`, `source/`): AGPL-3.0-only, like every calculator in this repository. Figures and wording in `rules.json`: the OpenAccountants Guide License v1.0, like the skills. See [LICENSING.md](../../../LICENSING.md).

Source commit: `c2e3c2b9` (OpenAccountants platform, `src/lib/engines`).
