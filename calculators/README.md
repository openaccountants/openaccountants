# Calculators

Small, open decision checks built on the skills in this repository. A skill is written for an AI; a calculator takes a person's own numbers and answers one question. The hosted versions live at openaccountants.com/tools; the logic lives here so anyone can read it, test it or embed it.

Each calculator is a folder with:

- `rules.json`: the figures it uses, each with its legal basis, its official source and the date they were checked (`as_of`).
- `index.mjs`: one pure function. No network, no clock, no tracking. Node 20+ (JSON import attributes).
- `index.test.mjs`: `node --test calculators/<name>/`.
- `README.md`: the question, the inputs, the outputs, what it does not cover.

| Calculator | Question | Skills behind it |
|---|---|---|
| [`eu-vat-registration`](eu-vat-registration/) | I sell to customers in other EU countries. Do I have to register for VAT elsewhere, and whose VAT do I charge? | `eu-oss-digital`, `cross-border-vat-gst`, `eu-reverse-charge` |
| [`au-div7a-repayment`](au-div7a-repayment/) | For an existing complying amalgamated loan, do the supplied repayments cover the minimum yearly repayment formula? | `au-div7a`; ITAA 1936 ss 109E, 109N and 109R |

## Tax engines

[`engines/`](engines/) holds the calculation engines behind the compute tool of the OpenAccountants plugin: the same code that answers it, generated from the OpenAccountants platform, so anyone can read it, check each figure against the skill it was quoted from, and rerun the tests. A compute answer links to its engine's folder. Each folder has `index.mjs` (`run(facts)`), `source/` (the TypeScript it was built from), `rules.json` (every figure with its skill, section and quoted line), `cases.json`, `index.test.mjs` and a README. The folders are generated: do not edit them by hand. Run them all with `node --test calculators/engines/`.

| Engine | Jurisdiction | Tax years | What it computes |
|---|---|---|---|
| [`au_resident_tax_2026_27`](engines/au_resident_tax_2026_27/) | AU | 2026-27 | Australia, resident for the full 2026-27 year: income tax on taxable income less LITO, plus 2% Medicare levy, plus MLS check; take-home = gross income less those. |
| [`au_sbito_2026_27`](engines/au_sbito_2026_27/) | AU | 2026-27 | Australia 2026-27 small business income tax offset for an individual resident: 16% of the tax on net small business income, capped at $1,000, aggregated turnover under $5m. |
| [`ca_cpp_ei_employee_2026`](engines/ca_cpp_ei_employee_2026/) | CA | 2026 | Canada (outside Quebec) employee CPP (base + first additional), CPP2 and EI premiums for a full calendar year 2026 with one employer. |
| [`de_est_tariff_2026`](engines/de_est_tariff_2026/) | DE | 2026 | Germany 2026 income tax from the § 32a EStG tariff on taxable income (zu versteuerndes Einkommen), Grundtarif or splitting. Excludes solidarity surcharge and church tax. |
| [`ie_income_tax_usc_2026`](engines/ie_income_tax_usc_2026/) | IE | 2026 | Ireland 2026: income tax (after personal + PAYE credits) and USC for a single PAYE employee for the full year, cumulative basis. |
| [`mt_income_tax_2026`](engines/mt_income_tax_2026/) | MT | 2025, 2026 | Malta resident income tax on chargeable income for basis year 2026 (year of assessment 2027) or basis year 2025 (year of assessment 2026): picks the single, married or parent table, including the 2026 qualifying-child tables, from the person's facts. |
| [`mt_household_comparison_2026`](engines/mt_household_comparison_2026/) | MT | 2025, 2026 | Malta resident married couple, basis year 2026 (year of assessment 2027) or basis year 2025 (year of assessment 2026): compares the joint computation on the married table, separate computation (article 49A or 50) with each spouse on the single or parent table, and either of those with spouse B's part-time self-employment profit taxed at the final 10% (article 90A, up to EUR 12,000), and says which gives the least tax. |
| [`nl_vpb_2026`](engines/nl_vpb_2026/) | NL | 2026 | Netherlands corporate income tax (vennootschapsbelasting) for 2026 on a BV/NV's taxable amount (after loss offset and exemptions). |
| [`pt_ss_independent_2026`](engines/pt_ss_independent_2026/) | PT | 2026 | Portugal 2026: monthly social security contribution of a self-employed worker (quarterly regime) from the quarter's declared service/goods income; applies to the declaration month and the next two. |
| [`uk_ani_pension_target_2026_27`](engines/uk_ani_pension_target_2026_27/) | GB | 2026-27 | UK 2026-27: how much to pay (net) into a relief-at-source personal pension to bring adjusted net income down to a limit. Targets: personal_allowance_taper (GBP 100,000), child_benefit_charge_nil (GBP 60,000), tax_free_childcare (limit not served by any skill: always returns missing_rule until a skill serves it). |
| [`uk_paye_take_home_2026_27`](engines/uk_paye_take_home_2026_27/) | GB | 2026-27 | UK employee annual income tax (rUK rates: England, Wales, Northern Ireland) and employee Class 1 NIC (category A) on salary for 2026-27, and take-home pay. Annual basis. |
| [`us_se_tax`](engines/us_se_tax/) | US | 2025, 2026 | US self-employment tax (Schedule SE regular method) for tax year 2025 or 2026: 92.35% of net profit, 12.4% social security up to the wage base less W-2 SS wages, 2.9% Medicare uncapped. Excludes the 0.9% Additional Medicare Tax (Form 8959). |

Results are estimates from the rules in `rules.json`, not advice on anyone's situation. The nightly source watch on openaccountants.com checks the official pages the hosted EU VAT calculator cites; when a figure moves, `rules.json` is updated here and the hosted page follows.

The Division 7A calculator runs offline. Its rates are pinned to the recorded source-check date and require manual review against current official sources. Hosting and automatic source monitoring require separate integration.

Licence: the code is AGPL-3.0-only; the figures and wording in `rules.json` are under the OpenAccountants Guide License v1.0, like the skills.
