---
name: ke-tax-overview
description: 'Route Kenyan tax questions for 2026 to the income tax, corporate tax, VAT, payroll, social contributions, transfer pricing and property-income skills with their required facts and boundaries.'
jurisdiction: KE
tax_year: 2026
last_updated: 2026-11-14
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
version: 0.1
type: router
category: orchestrator
---

# Kenya tax overview (2026)

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

Kenya operates self-assessment through the Kenya Revenue Authority (KRA) and iTax. [ITA ss3-5](https://www.kra.go.ke/images/publications/Income-Tax-Act-2026.pdf) charge income accrued in or derived from Kenya and extend to specified foreign business/employment situations; a resident is not automatically taxed on every foreign receipt. Use Kenyan shillings for ordinary records and returns under [TPA s23](https://www.kra.go.ke/images/publications/Tax-Procedures-Act--2026.pdf), subject to its specific non-resident exceptions.

## The method, step by step

1. Establish the individual/company, residence, business activity, tax year/accounting period, source of income and treaty exposure. A bank account or PIN does not establish residence. The year of income is the calendar year under ITA s2; an entity's accounting period may differ.
2. For resident sole traders, load [ke-income-tax](ke-income-tax.md): progressive bands, highest marginal rate, reliefs, turnover-tax eligibility and annual self-assessment. The old overview's annual individual return deadline is superseded by the Finance Act change addressed there.
3. For employers, load [ke-payroll-paye-nssf-shif-ahl](ke-payroll-paye-nssf-shif-ahl.md): PAYE, monthly deadline, social deductions and housing levy. For self-employed household health and voluntary pension, load [ke-nhif-nssf](ke-nhif-nssf.md).
4. For companies and branches, load [ke-corporate-income-tax](ke-corporate-income-tax.md): ordinary rate, special-status boundaries, source/base, corporation return deadline and earlier balance payment. Do not apply an individual's return timetable to a company.
5. For taxable supplies and imports, load [kenya-vat](kenya-vat.md): standard/zero/exempt treatment, registration, monthly VAT return/payment deadline, credits and input restrictions. A PIN alone is not VAT registration.
6. For related cross-border transactions load [ke-transfer-pricing](ke-transfer-pricing.md); for foreign landlords load [non-resident-rental-income-tax-on-kenyan-property](non-resident-rental-income-tax-on-kenyan-property.md). Other treaty and cross-border withholding matters need a specialist and the operative treaty.
7. For legal setup choose [ke-company-formation](ke-company-formation.md) or the distinct foreign-founder execution workflow [set-up-your-company-in-kenya-we-handle-it-from-abroad](set-up-your-company-in-kenya-we-handle-it-from-abroad.md). Formation, tax registration, bank acceptance and immigration permission are separate.

## When to refuse or refer

Do not quote a rate or deadline from this routing file. Load the responsible skill, read its conditions and source boundary, and collect the inputs it asks for. Refer uncertain residence, treaties, special regimes, litigation, missing source documents and transactions the selected skill excludes. The overview does not prepare or submit a return.

## Sources

| Source and passages actually read | Official URL | Read on |
|---|---|---|
| Read for ITA s2 year of income, ss3-5 source and foreign-income rules, s52B return framework | https://www.kra.go.ke/images/publications/Income-Tax-Act-2026.pdf | 2026-11-14 |
| Read for Finance Act 2026 ss1,18, deferred individual return change | https://www.kra.go.ke/images/publications/Finance-Act-2026.pdf | 2026-11-14 |
| Read for TPA s23 ordinary records/return currency and non-resident exceptions | https://www.kra.go.ke/images/publications/Tax-Procedures-Act--2026.pdf | 2026-11-14 |

Not yet confirmed: Treaty treatment and any rule outside the linked skills; do not infer it from the overview. This router delegates every old headline rate/deadline to its single maintained home and does not invent example rates.
