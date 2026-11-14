---
name: israel-references
jurisdiction: IL
tax_year: 2026
last_updated: 2026-11-14
version: 1.1
description: Primary source references and related open-source projects for this jurisdiction.
tier: 2
type: router
---

# Israel: source and implementation routing

## Scope

Route an Israel tax task to the relevant skill and distinguish primary law from an implementation reference. This is a 2026 source-routing index; it contains no independent tax calculation or filing authority. Retain the package's upstream attribution and existing repository identities. A calculator or code repository is not proof of current Israeli tax law.

## Ask the client first

Identify the tax job, year, taxpayer type/residence, actual documents and requested output. Read the applicable Israel skill and its current Sources/Not yet confirmed boundaries before using an implementation. For code reuse, establish the actual file licence, notices and compatibility for the intended distribution. Do not infer a licence from public availability or a star count.

## The method, step by step

### Load the skill that owns the tax answer

| Job | Skill to load | Source role |
|---|---|---|
| VAT registration, classification and return | [israel-vat](israel-vat.md) | VAT law/regulations and read authority guidance |
| Freelancer records, micro-business, contribution planning | [il-freelancer-ops](il-freelancer-ops.md) | Income Tax Ordinance, VAT status and National Insurance sources |
| Annual return, bands, surtax and credits | [il-income-tax-returns](il-income-tax-returns.md) | Actual tax-year law and correctly labelled filing-cycle forms |
| Company/shareholder extraction | [il-corporate-tax](il-corporate-tax.md) | Company/dividend/withdrawal provisions and actual NI class |
| Employee refund | [il-employee-tax-refund](il-employee-tax-refund.md) | Refund-service eligibility and claim-year relief |
| Crypto | [il-crypto-tax](il-crypto-tax.md) | Asset/capital/business classification and actual disposal reporting |
| Withholding | [il-tax-withholding](il-tax-withholding.md) | Payer duty, payment category and current certificate |
| Customs/import | [il-customs-duty](il-customs-duty.md) | Current product tariff, valuation, origin and import VAT |
| Immigration/returning residence | [il-new-immigrant](il-new-immigrant.md) | Residence, foreign-income relief and reporting transition |

### Keep the upstream projects, with their actual limits

**Skills IL, Tax and Finance:** [skills-il/tax-and-finance](https://github.com/skills-il/tax-and-finance). The existing adaptation notices identify this project as upstream for freelancer operations, withholding, annual returns, company extraction, employee refunds, crypto and customs. Its repository description covers Israeli tax, invoicing, VAT and financial systems, and its [licence file](https://github.com/skills-il/tax-and-finance/blob/master/LICENSE) is MIT. Preserve required attribution/licence notices. The old payroll calculator, VAT reporting, invoice organizer and pension-advisor coverage descriptions are discovery cues, not a claim every module is current or complete. Monitor a relevant upstream change, then verify rates/conditions against primary law before updating a skill.

**Income Tax Form 134 calculator:** [tomerip/income_tax_t134](https://github.com/tomerip/income_tax_t134). Its README describes a Python/YAML calculator and PDF output for the annual-return annex, and discloses missing footnote/benefit/specific-section handling. The repository [licence](https://github.com/tomerip/income_tax_t134/blob/main/LICENSE) is Apache-2.0. The earlier index incorrectly described this as an advance-tax reduction request. Form 134 concerns excess employer study-fund/provident-fund payments and relevant disability-insurance calculations, as described in the official 2025-2026 filing-cycle guide. Do not validate Mikdamot reduction logic with the wrong form. Route pension/annual-return work to the annual-return skill and advance-payment requests to the actual authority process ([official rights guide, Form134 explanation](https://www.gov.il/BlobFolder/generalpage/income-tax-guide-knowyourright/he/Guides_IncomeTax_da-2025.pdf)).

**Tax forms generator:** [talmiller2/tax_forms_generator](https://github.com/talmiller2/tax_forms_generator). Its README describes Python generation of Israeli capital-gain/loss tables from Interactive Brokers exports, including trades, dividends, interest, fees and withholding data. Treat it as reference-only until the actual licence is confirmed. Its parsing/field-mapping and NIS-conversion approaches may be inspected as implementation ideas; no output is accepted without an independent reconciliation and the actual year/form. The old Form 1325 link concerns securities, not a universal crypto filing route. The crypto skill's asset-reporting method controls crypto. A future working-paper-to-form exporter remains an unbuilt possibility, not a present product capability.

**Israel Tax Calculator:** [israeltaxcalculator/israeltaxcalculator.github.io](https://github.com/israeltaxcalculator/israeltaxcalculator.github.io). The old index described a JavaScript/Hebrew calculator for bands, credit points and NI tiers. Repository metadata is reachable, but its README was not found and its licence/current implementation were not verified. Keep it reference-only. Any comparison with the annual-return skill is a test candidate, not proof either result is legally correct. Do not repeat the old star counts as a quality or current-use claim.

### Validate an implementation against an established answer

First establish tax-year inputs, legal conditions and expected results from the relevant skill's primary sources. Then inspect the actual code/data version, licence and unsupported cases; recompute examples independently, compare outputs and investigate differences. Preserve original ownership/attribution if permitted code is incorporated. Do not treat a matching result from two implementations sharing old constants as independent legal validation. No external code was executed or incorporated by this index rewrite.

## When to refuse or refer

Refer tax questions to the substantive skill and professional review where its scope requires it. Refuse unlicensed/unconfirmed code reuse, unknown source-year constants, unsupported form mappings, missing cases and any attempt to use a third-party calculator as filing authority. The prior blanket MIT/Apache-to-AGPL compatibility statements are not a substitute for reviewing the actual files, notices and intended reuse.

## Completion checklist

Identify job/year; load the owning skill; read primary-source boundaries; confirm exact implementation version and licence where relevant; preserve provenance; reconcile independently; record unresolved conditions and hand off the tax result for appropriate review.

## Sources

| Source | URL | Read on |
|---|---|---|
| ITA 2025 rights guide, 2025-2026 filing cycle; Read for Form134 purpose and securities-versus-other-asset schedules, not tax-year2026 form specifications | https://www.gov.il/BlobFolder/generalpage/income-tax-guide-knowyourright/he/Guides_IncomeTax_da-2025.pdf | 2026-11-14 |
| Skills IL repository/licence, primary provenance source only; Read for repository description and MIT licence conditions | https://github.com/skills-il/tax-and-finance/blob/master/LICENSE | 2026-11-14 |
| Form134 implementation README/licence, primary implementation source only; Read for annual-annex calculation/PDF workflow and admitted missing cases, Apache licence | https://github.com/tomerip/income_tax_t134/blob/main/README.md | 2026-11-14 |
| Form134 implementation licence; Read for distribution/notice conditions, not a tax rule or compatibility opinion | https://github.com/tomerip/income_tax_t134/blob/main/LICENSE | 2026-11-14 |
| Tax forms generator README, primary implementation source only; Read for IB export/table-generation scope, not legal tax rates | https://github.com/talmiller2/tax_forms_generator/blob/master/README.md | 2026-11-14 |
| IsraelTaxCalculator repository metadata, primary identity source only; Read for existence/default branch; README unavailable and no current-code validation | https://github.com/israeltaxcalculator/israeltaxcalculator.github.io | 2026-11-14 |

Not yet confirmed: tax-year2026 Form134/1325 specifications and every external implementation's current rate/condition correctness; tax_forms_generator and IsraelTaxCalculator licences, the latter's current JavaScript/Hebrew/rate/NI coverage, and old14/9starcounts. Existing MIT/Apache provenance is preserved, but file-specific reuse/compatibility and notices require review before incorporation. The old Form134-as-advance-reduction description is corrected, and Form1325 is not treated as the universal crypto schedule. No repository is an official tax-law source.
