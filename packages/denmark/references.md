---
name: denmark-references
jurisdiction: DK
last_updated: 2026-11-16
version: 1.1
description: Official source navigation for Danish investment, personal-tax and exchange-rate research, with unverified historical project leads.
tier: 2
type: router
tax_year: 2026
category: orchestrator
---

# Denmark source and skill routing v1.1

Built from the law. Not yet approved.

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

Use this index to choose the Danish investment, personal-tax or foreign-currency research task for income year 2026. It supplies source and skill navigation only. It does not calculate tax, establish a filing position or grant permission to reuse software. The historical project descriptions below are preserved research leads, not official authority or current-year rules.

## Ask the client first

Identify the taxpayer or entity, residence, income year, asset or employee-plan type, transaction dates and the output required. Obtain broker statements, acquisition and disposal records, employment-plan documents and actual currencies before choosing a method. A project name or calculator result does not establish these facts.

## The method, step by step

1. For investment disposals and portfolio income, load [dk-capital-gains](dk-capital-gains.md). Use Skattestyrelsen's [shares and securities index](https://skat.dk/en-us/individuals/shares-and-securities) to reach the relevant official investment, share-gain, departure or crypto guidance. Read the selected operative rules before using a rate, cost method or reporting condition.
2. For general personal-tax calculations, load [dk-income-tax](dk-income-tax.md). The official [individuals index](https://skat.dk/en-us/individuals) separates preliminary assessments from annual tax assessment notices and labels their years. Match the actual income and assessment year rather than treating a historical project threshold as current.
3. For employee share plans or foreign stock-plan transactions, select [dk-payroll](dk-payroll.md), [dk-capital-gains](dk-capital-gains.md) and, where relevant, [dk-cross-border](dk-cross-border.md) by the actual employment, asset and residence facts. Obtain the current official treatment before calculating. The archived E-Trade/FIFO description below does not establish an authorised cost method or reporting format.
4. For exchange-rate research, use [Danmarks Nationalbank's exchange-rate page](https://www.nationalbanken.dk/en/what-we-do/stable-prices-monetary-policy-and-the-danish-economy/exchange-rates), which links historical data and current feeds. Record the actual date, currency pair and quotation units. The publisher calls its rates indicative and informational; this index does not establish the tax rule selecting a conversion date, rate or method.
5. Handoff the selected skills, taxpayer facts, applicable year, actual official source passages, transaction records and unresolved questions. Obtain the specific legal rule, source access and any reuse permission before proceeding. Named accountant approval is separate from this routing index.

## When to refuse or refer

Do not file, pay, choose a rate or costing method, copy project code or claim accountant approval from this index. Stop the affected step where current official support, transaction evidence, legal scope or permission is missing. Do not adopt FIFO, a historical threshold, married-couple treatment or a claimed integration just because an archived project description says so. The selected substantive skill and applicable official rules must establish the actual conditions.

## Historical project leads, unverified and non-operative

Every statement in this archive, including the blanket licensing assertion, stars, languages, dates, formulas, married-couple treatment, FIFO description and proposed integrations, is an original unverified research claim. It has not been newly checked or adopted. Preserve it for research continuity only; do not use it as a current tax instruction, project endorsement or permission to copy. Current repository licences, file-level rights, versions, accuracy and compatibility must be established separately before reuse.

OpenAccountants is AGPL-3.0. MIT-licensed projects below can be incorporated with attribution.

### tesoro

- Repository: [libo/tesoro](https://github.com/libo/tesoro)
- License: MIT
- Stars: 24
- Language: Ruby
- Scope: Danish capital gains tax calculator for stock/investment portfolios. Implements the two-tier aktieindkomst (share income) taxation system with progressive rates: 27% up to progressionsgrænsen (DKK 58,900 in 2023) and 42% above. Supports married/unmarried filing with combined progressive threshold for married couples (2×).
- Why it matters: Clean implementation of SKAT's aktieindkomst progressive system with historical threshold data from 2014–2023. MIT license.
- Integration approach: Capital gains rate structure (27%/42% split) and progressive thresholds incorporated into the income tax skill.

### skattefar

- Repository: [ob-vest/skattefar](https://github.com/ob-vest/skattefar)
- License: MIT
- Stars: 0 (new, May 2026)
- Language: TypeScript
- Scope: Danish tax calculator "for mere mortals": aims to simplify SKAT's complex system into understandable components.
- Integration approach: Reference for Danish tax calculation UX and bracket structure.

### etrade-skat-tools

- Repository: [mpdn/etrade-skat-tools](https://github.com/mpdn/etrade-skat-tools)
- License: MIT
- Stars: 2
- Language: TypeScript
- Scope: Tooling for reporting stock plan sales from E-Trade to Danish SKAT. Handles currency conversion (USD→DKK) using Nationalbanken rates, calculates gains using FIFO, and formats for SKAT reporting.
- Integration approach: Reference for foreign stock income reporting to SKAT, FIFO methodology, and Nationalbanken FX rate sourcing.

## Sources

| Source and actual read scope | URL | Read on |
|---|---|---|
| Skattestyrelsen shares and securities: Read the index's links for investment guidance, share gains/losses, leaving Denmark and crypto. Navigation only; no linked tax rule or figure is adopted here. | https://skat.dk/en-us/individuals/shares-and-securities | 2026-11-16 |
| Skattestyrelsen individuals: Read the preliminary-assessment and annual-assessment headings, their separate year labels and the personal-tax, investments and cross-border navigation. No complete calculation or filing procedure read claimed. | https://skat.dk/en-us/individuals | 2026-11-16 |
| Danmarks Nationalbank exchange rates: Read the quotation-unit description, historical-data and current-feed links, and the indicative/information-only qualification. No dated exchange-rate value or tax conversion rule is adopted. | https://www.nationalbanken.dk/en/what-we-do/stable-prices-monetary-policy-and-the-danish-economy/exchange-rates | 2026-11-16 |

Not yet confirmed: All archived project licences, reuse and attribution permissions, repository stars, programming languages, maintenance, formula accuracy, claimed coverage and integrations, including the blanket AGPL/MIT incorporation assertion. The archived 2023 DKK 58,900 threshold, 27%/42% split, historical 2014-2023 coverage and married-couple doubling are not established as current rules here. The E-Trade/FIFO and FX/reporting-format claims are unverified and must not select a tax method. No current personal-tax, employee-plan or investment result follows from this index. It contains no operative rates, deadlines or worked tax cases, so the router shape requires no oa-check.
