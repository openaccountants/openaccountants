---
name: tj-tax-overview
description: "Route 2026 Tajikistan tax work to the personal income, corporate income, VAT, payroll/social-tax and formation skills. Establish the person, period, source and documents before choosing a computation; no headline rates or duplicated deadline table."
jurisdiction: TJ
tax_year: 2026
last_updated: 2026-11-15
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
category: orchestrator
type: router
version: 0.1
---

# Tajikistan tax workflow overview v0.1

> **General reference only.** This skill prepares a working paper for review by a qualified Tajikistan professional. Confirm the facts, source version and filing procedure before filing, paying or taking a tax position.

**Built from the law. Not yet approved.** Tax year 2026; checked on 2026-11-15.


## Scope

This is the entry point for the Tajikistan pack, not a tax computation. The current Tax Code and its transition provisions govern the applicable period. Read the current official text alongside the owning skill before using a rate; the older English translation is not the current consolidated authority. [Tax Committee legislation index](https://www.andoz.tj/Legislation/TaxCode).

The Code was adopted in 2021 and generally commenced on 1 January 2022, with the separately deferred chapter and subsequent amendments addressed by the law. Use the Tajikistani somoni (TJS) in the working paper. The ordinary annual income-tax periods are calendar years, while employment withholding uses a calendar month; the individual and corporate skills apply the correct period. Tax is administered by the Tax Committee under the Government of the Republic of Tajikistan. [Tax Code arts. 240, 397-399](https://www.andoz.tj/docs/kodex/TaxKodex.pdf).


## Ask the client first

- Individual, company, entrepreneur, foreign establishment or proposed entity.
- Relevant tax period, residence, citizenship, presence, principal management and foreign-source facts.
- Activities, employees, supplies/imports, gross income and tax registrations.
- Accounts, contracts, payroll, invoices, customs and banking evidence.
- Any special regime, exemption, incentive, treaty request or authority notice.
- Whether the request is a computation, registration, filing, payment or dispute.


## The method, step by step

First establish residence and the income source. Resident worldwide exposure and non-resident Tajik-source exposure are the starting distinctions, with permanent-establishment and treaty rules requiring their own analysis. Do not infer residence from the address on an invoice. [Arts. 14, 181-182](https://www.andoz.tj/docs/kodex/TaxKodex.pdf).

| Request | Load and purpose | Handoff boundary |
|---|---|---|
| Individual wages or other personal income | [tj-income-tax](tj-income-tax.md): residence, main/additional-job distinction, personal deductions and individual filing/payment | Special entrepreneurial regimes, foreign credits and detailed non-wage calculations require further work |
| Company profit or payments to foreign recipients | [tj-corporate-income-tax](tj-corporate-income-tax.md): ordinary tax, manufacturing transition, financial/mobile category, advances, annual settlement and limited withholding | Incentives, tax depreciation, related-party prices, permanent-establishment attribution and treaty rates require separate analysis |
| Taxable sales, imports or foreign services | [tj-vat-gst](tj-vat-gst.md): registration, standard/reduced/exempt/zero distinctions, input restrictions and reverse tax | Verify exact supply, documents and special foreign/distance-service rules |
| Employees, social tax or payroll withholding | [tj-payroll-social](tj-payroll-social.md), together with the personal-income-tax skill | Classify budget versus other employer, employee deductions and the earlier applicable payment event |
| New business or legal-form choice | [tj-company-formation](tj-company-formation.md): ordinary LLC dossier, capital, single-window registration and post-registration tax routing | Other vehicles, regulated sectors, immigration, legalisation and accounting framework need their separate assessment |

Do not reuse the old overview's headline rates or annual deadlines. The owning skills preserve the old topics, correct obsolete personal/company/social figures, distinguish reduced/exempt VAT, and separate individual payments from company annual settlement. Load the owner rather than keeping an independent copy of its numbers.

Assemble the result as an input list, source/version record, calculation schedules, evidence gaps and filing/payment checklist. Use the Tax Committee [official site](https://www.andoz.tj/) to obtain the current form/portal route or contact the competent local office. Reconcile the official declaration fields and acceptance/payment evidence before marking a filing complete. None of these source readings constitutes an accountant approval.


## When to refuse or refer

Stop if the taxpayer, period, source, residence or evidence is unresolved. Refer missing transfer-pricing/cross-border jobs, treaties, special regimes, disputed assessments and any transaction outside the owning skill. Do not present this router as a complete return, a deadline calculator or authority for a filing position.


## Sources

| Official source | Read for | Date read |
|---|---|---|
| [Tax Committee legislation index](https://www.andoz.tj/Legislation/TaxCode) | Read for current consolidated-code listing through June 2026 and the separately dated English edition. | 2026-11-15 |
| [Tax Committee, current consolidated Tax Code](https://www.andoz.tj/docs/kodex/TaxKodex.pdf) | Read for arts. 14, 180-182, 240, 397-399; source, period, transition and commencement context. | 2026-11-15 |

Not yet confirmed: A complete transfer-pricing or cross-border skill; client-specific special regimes; live form fields and financial-reporting framework. Headline rates and deadlines belong to the linked owning skills and are not duplicated here.

