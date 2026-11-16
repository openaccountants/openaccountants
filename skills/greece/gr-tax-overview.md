---
name: gr-tax-overview
description: "Routing map for Greek tax and accounting work in tax year 2026. Select the owner for individual and company income tax, residence and cross-border work, VAT, employee and self-employed insurance, payroll, gains, presumptions, transfer pricing, formation and invoicing. Former headline figures and return dates live with the relevant detailed skill, not in this map. Trigger phrases: Greek tax system, taxes in Greece overview, Greece tax rates 2026, how Greece taxes income."
version: 0.3
category: international
jurisdiction: GR
tax_year: 2026
last_updated: 2026-11-16
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
type: router
---

# Greece tax overview v0.3

## The method, step by step

Establish the tax year, taxpayer, transaction, residence and question first. Greek tax administration is AADE, with myAADE/TAXISnet for the relevant tax services; social insurance is administered by e-EFKA. Amounts in the country pack are in euro unless a particular source says otherwise.

| Question or former overview topic | Owner to load | Handoff |
|---|---|---|
| Tax year, employment, pension, business and rental income; parent/youth rates and the individual return window | [gr-income-tax](gr-income-tax.md) | Tax year and filing year, age, dependants, income categories and source documents; the owner holds the actual bands and deadlines |
| Company accounting year, corporation tax and company return window | [gr-corporate-income-tax](gr-corporate-income-tax.md) | Legal form, book category, year end and accounts; use [gr-partnerships-single-entry](gr-partnerships-single-entry.md) for that distinct job |
| Worldwide versus Greek-source taxation, residence, moving in/out, inbound regimes, treaty relief and withholding | [gr-cross-border](gr-cross-border.md) | Residence history, travel dates, source/type of income and counterpart country; do not treat an immigration permit as a tax election |
| VAT rates and reductions, registration/exemption, return frequency and filing/payment | [greece-vat-return](greece-vat-return.md) | Transaction/place of supply, period, book/start category and election; [gr-vat-return](gr-vat-return.md) is only an alias pointer |
| Employee/employer percentage contributions and APD | [gr-employee-contributions](gr-employee-contributions.md) | Pay period, earnings, coverage package and employment/posting status |
| Self-employed fixed monthly insurance categories | [gr-efka](gr-efka.md) | Occupation, selected category, parallel work and insured status |
| Payroll withholding and labour/payroll submissions | [gr-payroll](gr-payroll.md) | Gross pay, contributions, age/dependants, timing and employment records |
| Securities, business or property capital gains | [gr-capital-gains](gr-capital-gains.md) | Asset, dates, cost/proceeds, holding and residence |
| Deemed living expenses, asset purchases and coverage by prior capital | [gr-living-expense-presumptions](gr-living-expense-presumptions.md) | Household assets/spending and documentary sources of funds |
| Connected transactions and transfer-pricing obligations | [gr-transfer-pricing](gr-transfer-pricing.md) | Group relationships, transaction totals, turnover and reporting year |
| Incorporation and post-formation registration | [gr-company-formation](gr-company-formation.md) | Form, founders, contribution types and required notarial route |
| Invoice issue, mandatory channel, myDATA and reconciliation | [greece-einvoice](greece-einvoice.md) | Invoice date, counterparty, mandate phase and software/channel |

The former headline rate/band tables and individual/company filing dates are deliberately handed to the named owners above. This router does not independently maintain a second version of their figures. Read the owner's version, actual source scope and Not yet confirmed line before answering. Deliver a working paper with its evidence and unresolved facts, then seek professional sign-off for filing or taking a position.

## When to refuse or refer

Do not choose a tax residence, treaty result, entity/book category, VAT rate or professional approval from this map alone. Do not imply that a structural pass, contributor credit or automated calculation is accountant approval. Where a specialist regime or current official instruction is absent, identify that particular gap rather than inventing a treatment.

## Sources

| Source and actual scope read | URL | Read on |
|---|---|---|
| Ministry of Finance income-tax codification through Law 5264/2025: read arts. 3, 4, 8, 15, 58, 67 and 68 to locate the old overview's tax-base, tax-year, rate and return topics; figures are delegated to their owners | https://minfin.gov.gr/wp-content/uploads/2026/04/%CE%9A%CE%A9%CE%94%CE%99%CE%9A%CE%9F%CE%A0%CE%9F%CE%99%CE%97%CE%A3%CE%97-%CE%A4%CE%9F%CE%A5-%CE%9A%CE%A9%CE%94%CE%99%CE%9A%CE%91-%CE%A6%CE%9F%CE%A1%CE%9F%CE%9B%CE%9F%CE%93%CE%99%CE%91%CE%A3-%CE%95%CE%99%CE%A3%CE%9F%CE%94%CE%97%CE%9C%CE%91%CE%A4%CE%9F%CE%A3-%CE%9C%CE%95%CE%A7%CE%A1%CE%99-%CE%A4%CE%9F-%CE%9D-5264-2025.pdf | 2026-11-16 |
| Ministry of Finance VAT Code codification through Law 5313/2026: read arts. 26 and 43 to locate VAT rate and periodic-return topics | https://minfin.gov.gr/wp-content/uploads/2026/10/Κοινοποίηση-Διοικητικής-Κωδικοποίησης-του-ν.5144-2024-γι.pdf | 2026-11-16 |
| e-EFKA official site: read authority identity and entry points only, not a fresh audit of all contribution figures | https://www.efka.gov.gr | 2026-11-16 |
| Country repository skills: read all existing files for job routing and open coverage questions, without editing or reapproving the unchanged owners | https://github.com/openaccountants/openaccountants/blob/2844c309238b4fdb63be0a3d0ad9ae99a8ea89c8/skills/greece/README.md | 2026-11-16 |

Not yet confirmed: current transaction-specific answers and the unresolved source/filing items declared by each owner; the map supplies no new determination or blanket claim that the whole country is complete.
