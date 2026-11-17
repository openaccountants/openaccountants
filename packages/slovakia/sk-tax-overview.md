---
name: sk-tax-overview
description: "Route a Slovakia 2026 question to the owning personal, company, VAT, payroll/social, cross-border, transfer-pricing or formation skill. Establish the period, residence, income/transaction and form before computing; preserves the owners' unresolved boundaries without duplicating their figures."
version: 0.3
jurisdiction: SK
category: international
tax_year: 2026
last_updated: 2026-11-15
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
type: router
---

# Slovakia Tax Overview

Load the skill for the person's job and facts before using any rate, threshold, deadline or form. This page routes the 2026 pack; it does not own a second set of tax figures. The Financial Administration is the official tax-authority entry point: [Finančná správa SR](https://www.financnasprava.sk/sk/titulna-stranka).

## Ask the client first

- Individual, company, partnership, employer or software user, and which task?
- Relevant tax/accounting period and actual registration/transaction dates?
- Residence, permanent home/seat, management, foreign work/income and treaty countries?
- Income categories, taxable revenue, taxable supplies, staff and connected transactions?
- Which records, registrations, return type and current form are available?
- Does the question fall within a stated unresolved boundary in the owning skill?

## The method, step by step

1. Establish residence and source before assuming worldwide or source-only taxation. Load [sk-cross-border](sk-cross-border.md) for individuals' permanent residence/home/day-count tests, companies' seat/effective-management tests, treaty restrictions and withholding. A domestic residence test alone does not settle a treaty conflict.
2. Select the income-tax owner. Use [slovakia-pit](slovakia-pit.md) for employment, business/SZČO, rent, capital/other income, progressive bands versus the small-business rate, allowances, flat-rate expenses, child bonus, losses, advances and the actual return. That owner carries the subsistence-minimum derivation and its period, rather than this router. Use [sk-corporate-income-tax](sk-corporate-income-tax.md) for company taxable-revenue rate selection, minimum tax, tax base, deductions, depreciation, losses, interest limitations, advances and the actual corporate return. The rate selector and the taxable base are different inputs.
3. Separate becoming a VAT payer from registering for a particular transaction. Load [slovakia-vat-registration-4-7-7a](slovakia-vat-registration-4-7-7a.md) for domestic turnover triggers and effective dates, acquisitions, incoming/outgoing services, limited registrations, deregistration and the actual registration form. Load [slovakia-vat-return](slovakia-vat-return.md) for standard/reduced classification, input tax, reverse charge, car restrictions, coefficients, tax periods, returns, control statements, refunds and the actual forms. A registration number alone does not establish full payer status or deduction rights.
4. For employees or self-employed insurance, load [sk-payroll-social](sk-payroll-social.md). It owns social/health contributions, bases and ceilings, payroll advances/allowances/bonus, registrations, reporting, payment cycles, reconciliation and cross-border employment checks. Establish the insured person's status and actual start date before using a contribution method.
5. For dependent persons or controlled dealings, add [sk-transfer-pricing](sk-transfer-pricing.md) for relationship/significance tests, methods, adjustments, documentation, return disclosure, CbCR and APAs. Add the cross-border skill where source, treaty or withholding facts also matter.
6. For choosing or registering a company, load [sk-company-formation](sk-company-formation.md): entity liability, founding routes, paid capital, register documents, court/notary route, fees and follow-up. It separates foundation from the company's effective register date and accounts deposit from return approval. Apply the tax owners after determining the vehicle's actual facts.
7. For return preparation, load the owner's filing section, current-year official form and instructions. The PIT/CIT owners carry their tax-year/return-form transition and notice-extension conditions; the VAT owners carry the return, payment and control-statement calendar. For bankruptcy or liquidation, do not apply the ordinary notice-extension route; use the separate statutory application procedure. [Income Tax Act § 49(3)(a)-(c)](https://www.slov-lex.sk/static/SK/ZZ/2003/595/20260101.html). Do not infer a fixed deadline or use an old XML schema from the tax year's label alone. The filing platform/access must match the actual official instructions; a generic “all returns use eDane” shortcut is insufficient.
8. Return the selected skill names, established inputs, source/period, calculation where relevant, form/portal and unresolved conditions. For external software, add [slovakia-references](references.md) to evaluate provenance and integration conditions; source code is not tax-law authority.

### Destination map

| Original overview topic | Current owner and handoff |
|---|---|
| Tax year and income categories; personal bands and subsistence-minimum multiples; business-rate revenue selector; capital-income treatment | [slovakia-pit](slovakia-pit.md), scope, base and computation sections |
| Company rate by taxable revenue, minimum tax, return/payment and extensions | [sk-corporate-income-tax](sk-corporate-income-tax.md), method and filing sections |
| Individual/company residence, worldwide/source basis, foreign income, dividends and withholding | [sk-cross-border](sk-cross-border.md), residence/source and payment methods; PIT/CIT owners for the return |
| VAT existence, rates and goods/services classification; monthly/quarterly periods; returns/payment and control statements | [slovakia-vat-return](slovakia-vat-return.md), rate classification and filing sections |
| Domestic VAT turnover triggers and payer-effective dates; other registration categories | [slovakia-vat-registration-4-7-7a](slovakia-vat-registration-4-7-7a.md), category decision and filing sections |
| Payroll and social/health rates, bases and payment/reporting obligations | [sk-payroll-social](sk-payroll-social.md) |
| Transfer pricing and entity formation | [sk-transfer-pricing](sk-transfer-pricing.md) and [sk-company-formation](sk-company-formation.md) |
| Currency and authority | Use EUR inputs in the relevant owner and the official authority link above. The old euro-adoption history is addressed below, outside any tax computation |

## When to refuse or refer

- Facts, period or jurisdiction do not identify an owner: establish them before computing. This router has no independent rates, deadline calculator or worked tax cases.
- Do not turn an unconfirmed sibling item into a confirmed answer. In particular, the VAT owners retain boundaries for a zero-turnover annual coefficient and a first control-statement breach; the registration owner retains the gross crossing-invoice circularity boundary. Refer those precise issues for resolution.
- The cross-border owner does not establish the operative suspension boundary for the Russia treaty; do not infer it from an old treaty list or replace it with a blanket punitive withholding rule. The transfer-pricing owner also has stated APA-office identity and foreign deemed-dividend boundaries.
- A software tool, old form, contribution credit or source-cited draft does not establish accountant approval of an actual filing.

## Sources

The tax-law passages, exact figures, read dates and worked cases live in the linked owners. These files were read for routing; this page does not claim fresh legal verification of every protected sibling. The narrow bankruptcy/liquidation extension boundary above was reread in the Income Tax Act, alongside the authority and historical-currency sources below.

| Source and scope | URL | Read on |
|---|---|---|
| Financial Administration, official authority entry point | https://www.financnasprava.sk/sk/titulna-stranka | 2026-11-15 |
| ECB, Slovakia cash-changeover page, read to resolve the old unsupported adoption-date item | https://www.ecb.europa.eu/euro/changeover/slovakia/html/index.en.html | 2026-11-15 |
| Income Tax Act § 49(3)(a)-(c), notice-extension exclusion and separate bankruptcy/liquidation application route | https://www.slov-lex.sk/static/SK/ZZ/2003/595/20260101.html | 2026-11-15 |

Not yet confirmed: a particular filer's portal access or suitability of an upstream software version for the current return; unresolved items in the linked owners remain unresolved. The old claim that the euro became legal tender on 1 January 2009 is confirmed by the ECB's dated changeover account, but is historical context and not an input to a current tax calculation.

> Contributed by Michael Cutajar.
