---
name: ro-tax-overview
description: "Use this skill for a first map of the Romanian tax system in tax year 2026: the calendar tax year, ANAF, worldwide taxation of residents, the flat 10% income tax, employee CAS 25% and CASS 10%, employer CAM 2.25%, the 16% profit tax, the 1% micro-enterprise tax and its EUR 100,000 revenue ceiling, 16% dividend tax from 2026, VAT at 21% and 11%, the Declarația unică due 25 May 2027, the D101 profit tax return due 25 June 2027, and the transfer pricing file under ANAF Order 828/2026. Every figure is taken from the Fiscal Code and Fiscal Procedure Code as consolidated by ANAF. Trigger phrases: Romania tax overview, Romanian tax system, tax in Romania 2026, ANAF basics. Out of scope: detail and computations, which are in ro-income-tax, ro-employee-income-tax, ro-cas-cass, ro-payroll-social, ro-corporate-income-tax, ro-transfer-pricing, ro-cross-border and ro-vat-return."
jurisdiction: RO
category: international
tax_year: 2026
tier: 2
last_updated: 2026-10-23
version: 0.2
verified_by: pending
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Romania tax overview (2026)

This is a short map. Each line points to the skill that holds the detail. The law is Legea 227/2015 (Codul fiscal, "the Fiscal Code") and Legea 207/2015 (Codul de procedură fiscală, "the Procedure Code"), read on 23 October 2026 in ANAF's consolidated texts. ANAF notes these consolidations are not an official republication.

## The Romanian tax system at a glance

| Item | 2026 position | Law | Detail in |
|---|---|---|---|
| Tax year, individuals | Calendar year | Fiscal Code art. 65(1) | ro-income-tax |
| Tax year, companies | Calendar year; a company with a different financial year may opt for a modified tax year | art. 16(1) and (5) | ro-corporate-income-tax |
| Tax authority | ANAF (Agenția Națională de Administrare Fiscală) | Procedure Code | all |
| Currency | Romanian leu (RON) | | |
| Who is taxed on what | A resident individual is taxed on income from any source, in Romania and abroad; a non-resident only on Romanian income | art. 59(1) | ro-cross-border |
| Individual income tax | 10% flat rate | art. 64(1) | ro-income-tax, ro-employee-income-tax |
| Pension contribution (CAS) | 25% | art. 138(a) | ro-cas-cass, ro-payroll-social |
| Health contribution (CASS) | 10% | art. 156 | ro-cas-cass, ro-payroll-social |
| Employer work insurance contribution (CAM) | 2.25% | art. 220^3(1) | ro-payroll-social |
| Profit tax | 16% of taxable profit | art. 17 | ro-corporate-income-tax |
| Micro-enterprise tax | 1% of revenue, for a company whose revenue for the previous year was not above the RON equivalent of EUR 100,000, among other conditions | art. 47(1)(c), art. 51(1) | ro-corporate-income-tax |
| Dividend tax | 16% on dividends distributed from 1 January 2026 (for a modified tax year, from its first day in 2026), to Romanian companies and to resident individuals; final for individuals. A Romanian company holding at least 10% for a full year, among other conditions, is exempt. Dividends distributed from 2025 interim accounts stay at 10% | art. 43(2) and (4), art. 97(7); Legea 141/2025 art. VII(1)(a) and (c) and (2) | ro-corporate-income-tax, ro-employee-income-tax |
| VAT | Standard rate 21%; reduced rate 11%, both since 1 August 2025 (Legea 141/2025, which replaced 19%, 9% and 5%) | art. 291(1) and (2); Legea 141/2025 art. II pt. 42 and art. VII(1) | ro-vat-return |
| Annual individual return (Declarația unică) for 2026 income | File by 25 May 2027 | art. 122(3) | ro-income-tax, ro-employee-income-tax |
| Annual profit tax return (D101) for 2026 | File by 25 June 2027 (modified tax year: the 25th of the sixth month after the year ends; the taxpayers in art. 41(16) and (17) have their own deadlines) | art. 42(1) and (2) | ro-corporate-income-tax |
| Transfer pricing file | Large taxpayers prepare it each year, from 2026 transactions, for transactions with each affiliated person at or above the thresholds, by the profit tax return deadline. Small and medium taxpayers prepare it only when ANAF asks during a tax control | ANAF Order 828/2026 art. 2(1), (2) and (7), art. 15(1) | ro-transfer-pricing |
| EU context | Romania is an EU member state; VAT follows Directive 2006/112/EC | | ro-vat-return |

## Fines for late filing

- An individual who files the Declarația unică or another income return late is fined RON 50 to 500 (Procedure Code art. 336(3)).
- A company that files a return late, or anyone who files a registration late, is fined RON 1,000 to 5,000 if it is a medium or large taxpayer and RON 500 to 1,000 for other companies and for individuals (art. 336(1)(a)-(b) and (2)(d)).
- Interest and penalties on late payment are in each skill above.

## Sources

| Source | URL | Read on |
|---|---|---|
| Fiscal Code, Legea 227/2015, ANAF consolidated text: art. 16, 17, 42, 43, 47, 51, 59, 64, 65, 97, 122, 138, 156, 220^3, 291 | https://static.anaf.ro/static/10/Anaf/legislatie/Cod_fiscal_norme_2023.htm | 2026-10-23 |
| Fiscal Procedure Code, Legea 207/2015, ANAF consolidated text: art. 336 | https://static.anaf.ro/static/10/Anaf/cod_procedura/Cod_Procedura_Fiscala_2023.htm | 2026-10-23 |
| ANAF Order 828/2026 (transfer pricing file), Monitorul Oficial nr. 543 of 2 July 2026, ANAF copy: art. 2, 15 | https://static.anaf.ro/static/10/Anaf/legislatie/OPANAF_828_2026.pdf | 2026-10-23 |
| Legea 141/2025 (Monitorul Oficial nr. 699 of 25 July 2025), ANAF copy: art. II pt. 1, 5 and 42, art. VII | https://static.anaf.ro/static/10/Anaf/legislatie/L_141_2025.pdf | 2026-10-23 |

Not yet confirmed: nothing beyond the open points listed in each linked skill.
