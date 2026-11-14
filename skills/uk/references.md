---
name: uk-references
jurisdiction: GB
tax_year: 2026
last_updated: 2026-11-14
version: "2.0"
type: router
description: "Open-source projects that implement UK tax rules (income tax, National Insurance, PAYE, student loans, crypto capital gains matching), with their licences, what each covers, and how an AI or developer may use them to cross-check a figure for tax year 2026/27. None of them is a source of law. The figures themselves come from the UK pack skills and HMRC."
tier: 2
---

# United Kingdom: related open-source projects

> **General reference only.** This skill is general reference material for AI-assisted workflows. It is not a source of tax law and has not been reviewed for any specific person's facts. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional.

OpenAccountants is AGPL-3.0. The projects below have licences that can be used with it, as noted on each. Their state was read on GitHub on 14 November 2026.

## The method, step by step

1. **Answer the tax question from the UK pack first.** Rates, bands and thresholds for 2026/27 live in the pack skills (for example `uk-income-tax-sa100`, `uk-national-insurance`, `uk-payroll`, `uk-student-loan-repayment`, `uk-crypto-tax`), each linked to HMRC. A project below never overrides them.
2. **Use a project only to cross-check arithmetic.** If a computed figure and a project's output differ, find out why (tax year selected, Scottish or rUK bands, category letter, plan type). The HMRC page cited in the pack skill decides, not the code.
3. **Pick the project by job:**

| Job | Project | Repository | Licence | Notes |
| --- | --- | --- | --- | --- |
| Take-home pay: income tax, National Insurance, student loan | HMRC Tax Kalculator (official HMRC repository, Kotlin Multiplatform) | https://github.com/hmrc/tax-kalculator | Apache-2.0 | HMRC's own open-source calculator; last pushed August 2026 |
| Income tax, employee and employer NI, student loans, Scottish rates | SavingTool hmrc-income-tax (TypeScript) | https://github.com/SavingTool/hmrc-income-tax | MIT | README gives 2026/27 as the default tax year; last pushed November 2026 |
| PAYE estimation | HMRC PAYE Estimator (official HMRC repository, Scala.js) | https://github.com/hmrc/paye-estimator | Apache-2.0 | Last pushed March 2023: treat its rates as out of date for 2026/27 |
| Crypto capital gains: same-day, 30-day (bed and breakfast) and section 104 matching, PDF reports | BittyTax (Python) | https://github.com/BittyTax/BittyTax | AGPL-3.0 | Useful to cross-check the matching order in `crypto-accounting` and `uk-crypto-tax` |

4. **Licences.** Apache-2.0 and MIT code may be adapted into AGPL-3.0 work with attribution and the licence notice kept. AGPL-3.0 code (BittyTax) is compatible as-is. Copy logic, not figures: figures still come from HMRC.
5. **Hand back** to the pack skill for the answer, its sources and its trust label.

## When to refuse or refer

- Never cite a repository, its README or its test data as the authority for a rate, threshold or rule: cite the HMRC or legislation.gov.uk page named in the pack skill.
- Do not use HMRC PAYE Estimator figures for 2026/27 without checking each against HMRC: the repository has not been updated since March 2023.
- If a project disagrees with HMRC, follow HMRC and say so; do not average or pick the friendlier figure.
- Questions about filing, penalties or a client's position go to the relevant pack skill, then to a qualified accountant.

## Sources

| Source | What was read | URL | Read on |
| --- | --- | --- | --- |
| GitHub, hmrc/tax-kalculator | Read for the licence (Apache-2.0), language, scope and last push date | https://github.com/hmrc/tax-kalculator | 2026-11-14 |
| GitHub, SavingTool/hmrc-income-tax | Read for the licence (MIT), scope and the README default tax year 2026/27 | https://github.com/SavingTool/hmrc-income-tax | 2026-11-14 |
| GitHub, hmrc/paye-estimator | Read for the licence (Apache-2.0) and the last push date (March 2023) | https://github.com/hmrc/paye-estimator | 2026-11-14 |
| GitHub, BittyTax/BittyTax | Read for the licence (AGPL-3.0), scope and last push date | https://github.com/BittyTax/BittyTax | 2026-11-14 |

Not yet confirmed: whether each project's built-in 2026/27 figures match HMRC (not tested here; use them only as a cross-check).
