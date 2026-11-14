---
name: bd-tax-overview
description: "Route Bangladesh tax work for 2026 to the individual, corporate, VAT, payroll and cross-border rules, distinguishing income years from assessment years and primary law from proposals."
jurisdiction: BD
tax_year: 2026
last_updated: 2026-11-14
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
version: 0.1
type: router
category: orchestrator
---

# Bangladesh tax overview and routing v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

Bangladesh tax-system entry point. Currency is BDT; income tax and VAT are administered through NBR. This overview routes work and keeps amounts in their computation homes.

## Ask the client first

- Legal form, residence/citizenship and business locations.
- Income year, assessment year and any approved non-standard accounting period.
- Activities, turnover, employees, foreign receipts/payments and registrations.

## The method, step by step

1. Record both the earning period and assessment period. The Income Tax Act definitions and scope provisions govern residence, normal income years and exceptions for banks, insurers, finance companies and eligible foreign-parent subsidiaries; do not infer period or residence from the payment currency (https://bdlaws.minlaw.gov.bd/act-1429.html).
2. Load [PIT](bangladesh-pit.md) for individuals, including ordinary bands, category thresholds, salary exemption, investment rebate, minimum tax and filing windows. Load [corporate tax](bd-corporate-income-tax.md) for companies and withholding. Residents' worldwide-income rules and non-residents' Bangladesh-source rules require the Act's scope and exemption analysis, not an assumption that every remittance is taxable.
3. Load [VAT](bangladesh-vat.md) for registration/enlistment, rates, invoices, credits and returns; payroll withholding belongs to [payroll](bd-payroll.md), employment benefit duties to [payroll/social](bd-payroll-social.md), and pension choice to [social contributions](bd-social-contributions.md).
4. Use [freelancer relief](bd-it-freelancer-tax.md) for the conditional services exemption, [formation](bd-formation.md) for registrations, and [company formation](bd-company-formation.md) for incorporation. Keep bookkeeping, fiscal invoices and statutory financial statements separate.
5. Cross-border and transfer-pricing work needs current treaty, source, permanent-establishment and associated-enterprise analysis under the Income Tax Act. This pack has no full standalone treaty-rate or transfer-pricing computation; refer before applying a treaty reduction or pricing adjustment.
6. Start with the enacted Finance Act and consolidated section pages. Budget proposals are not the enacted rates. Current filing rules are in section 170 (https://bdlaws.minlaw.gov.bd/act-1429/section-52000.html); headline amounts are intentionally linked to their home skills.

## When to refuse or refer

Refer non-standard periods, disputed residence, permanent establishments, treaty claims, transfer pricing, sector regimes and foreign tax credits where the applicable instrument has not been read. Do not quote a proposal as law.

## Sources

| Source and sections actually read | Official URL | Read on |
|---|---|---|
| Read for definitions and scope, Income Tax Act contents and linked provisions | https://bdlaws.minlaw.gov.bd/act-1429.html | 2026-11-14 |
| Read for enacted Finance Act structure and assessment-year rate authority | https://bdlaws.minlaw.gov.bd/act-1725.html?lang=en | 2026-11-14 |
| Read for filing windows, section 170 | https://bdlaws.minlaw.gov.bd/act-1429/section-52000.html | 2026-11-14 |

Not yet confirmed: Full treaty-by-treaty and transfer-pricing coverage remains outside this overview; approved alternative accounting periods and taxpayer-specific international relief require further source review.
