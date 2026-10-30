---
name: li-tax-overview
description: >
  Route 2026 Liechtenstein tax questions to the applicable source Guide and
  country gap register. Use for individual wealth-and-income tax, corporate profit,
  VAT, payroll/social contributions, transfer pricing, cross-border and formation
  intake. Identify the person, entity, country and period before choosing a method.
  This overview replaces the earlier approximate rate/deadline summary with a
  routing map; it supplies no standalone liability, treaty entitlement or filing
  instruction. The linked Guides contain the actual rules, sources, calculations
  and limits. All remain source-cited drafts with partial domain coverage, pending
  named Liechtenstein accountant review; presence is
  not proof of completeness.
jurisdiction: LI
tax_year: 2026
last_updated: 2026-10-30
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
category: international
version: 0.3
---

# Liechtenstein tax overview v0.3

Independent source/editorial review evidence and correction status are in the [dated whole-pack review record](../../../docs/research/2026-10-24-liechtenstein-pack-review.md). Apply its exact revision and scope limits. Named Liechtenstein accountant review remains open.

## Start with the question

This is a router for the 2026 source-cited country draft, not a standalone tax calculation. Establish legal person/entity, residence and activity countries, dates, income/supply/payment category, existing registrations, records and the authority decision before selecting a workpaper. The [country README](README.md) declares all seven applicable domains partial.

| Work | Read first | Key boundary |
|---|---|---|
| Individual income and wealth | [li-income-tax](li-income-tax.md) | Established taxable income/wealth, family tariff and actual annual municipality rate |
| Corporate profit | [li-corporate-income-tax](li-corporate-income-tax.md) | Tax adjustments, modified equity, losses and minimum-tax eligibility |
| VAT | [liechtenstein-vat](liechtenstein-vat.md) | Actual authority/registration, supply evidence, deduction entitlement and method |
| Employee withholding and insurance | [li-payroll-social](li-payroll-social.md) | Separate tax/social bases, 2026 Liechtenstein rates and coverage |
| Related parties and PEs | [li-transfer-pricing](li-transfer-pricing.md) | Actual relationship, documentation route and supported arm's-length method |
| Migration, foreign income and relief | [li-cross-border](li-cross-border.md) | Domestic liability, actual treaty and claim/deferral procedure |
| Entity setup | [li-company-formation](li-company-formation.md) | Selected form, contributions, actual register/governance and licensing evidence |

The earlier summary's rates/deadlines, Swiss-derived payroll/VAT assumptions and secondary citations remain in Git history. They are not substitutes for the current topic's source check. The [Liechtenstein Tax Administration](https://www.llv.li/de/landesverwaltung/steuerverwaltung) and the [official legislation collection](https://www.gesetze.li) are source entry points; the exact Acts/sections and read limits are linked in each Guide.

## Evidence and unresolved work

The original country batch was prepared on `codex/liechtenstein-country-completion` under [issue #406](https://github.com/openaccountants/openaccountants/issues/406). Preserve the original six Guides and research history; the missing TP and XB methods have been added in this batch. This router intentionally has no calculation blocks because it supplies no independent tax formula.

No named local accountant review, complete tax-domain coverage, filing acceptance or production ingestion is asserted. The dated independent review record identifies source scope and correction closure. The current continuation uses `codex/liechtenstein-persistent` and existing country [PR#785](https://github.com/openaccountants/openaccountants/pull/785), split from historical consolidated PR#514. Complete the remaining ordinary/source questions in README, freeze the whole country, obtain a fresh independent pack review and fix its findings before one country push. Verify exact published-head checks there. The30October writer ledgers and controls do not extend the24October review or supply accountant attestation.

<!-- openaccountants-cta-block -->

---

## Talk to an accountant

Find the current Guide and professional-review status at [OpenAccountants](https://www.openaccountants.com).
