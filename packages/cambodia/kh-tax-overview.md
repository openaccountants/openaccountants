---
name: kh-tax-overview
description: >
  Route a Cambodia 2026 tax question to the correct salary, physical-person
  business income, corporate income, VAT, payroll/social or formation skill.
  Use for Cambodian tax-system orientation, authority, tax-year/currency intake,
  tax residence, rate questions and filing-calendar questions. This is a routing
  overview: calculations and legal conditions live in the linked skills; unresolved
  core coverage remains explicit in the country README.
jurisdiction: KH
category: orchestrator
type: router
tax_year: 2026
last_updated: 2026-11-15
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
version: 0.1
---

# Cambodia Tax Overview and Routing v0.1

**General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

Route Cambodia tax work to the skill that owns its rules and calculation. The General Department of Taxation (GDT), Ministry of Economy and Finance, is the tax authority. Use the original Khmer legislation where a translation differs. This overview supplies no tax amount or filing deadline; open the destination before answering a rate or compliance question. The [pack README](README.md) identifies missing and partial coverage; current metadata does not mean accountant approval or complete jurisdiction coverage.

## Ask the client first

Identify the actual question, tax period/year, person or entity, employment versus business receipts, residence and source facts, tax registration/classification, activity/sector, currency and documents. Confirm whether the job is a rate estimate, working paper, filing, amendment, arrears or formation. A USD contract or bank descriptor does not determine tax residence, taxable income or a lawful KHR filing conversion.

## The method, step by step

| Question / original overview topic | Destination and boundary |
|---|---|
| Salary tax, personal top rate, employee residence or worldwide/source salary | [Income tax](kh-income-tax.md): establish employment, residence and source before using the resident/non-resident method; benefits are separate. |
| Physical-person business/professional income, tax year and annual return | [Income tax](kh-income-tax.md): annual TOI scope/base/credits and filing baseline; current special-classification detail remains held. |
| Company tax, standard/special corporate rate, company residence/source or approved financial year | [Corporate income tax](kh-corporate-income-tax.md): legal-person populations, base, minimum tax, credits and statutory calendar. A generic worldwide/source slogan does not replace those rules. |
| VAT/GST existence, ordinary rate or supply classification | [VAT](cambodia-vat.md): taxable person, place, taxable/zero/non-taxable supply, input eligibility and evidence before computation. |
| Salary-tax withholding calendar or social contributions | [Payroll/social](kh-payroll-social.md), with [income tax](kh-income-tax.md) for salary: distinguish salary-tax reporting from NSSF coverage/payment/declaration; current NSSF assessment remains incomplete. |
| Monthly VAT, prepayment or withholding deadline | Open [VAT](cambodia-vat.md) or [corporate income tax](kh-corporate-income-tax.md), as applicable: distinguish the statutory baseline from the actual period/channel GDT calendar. |
| Annual business return deadline or calendar-year question | Open [income tax](kh-income-tax.md) or [corporate income tax](kh-corporate-income-tax.md): apply the actual year-end/approved-year and current notice. |
| Patent-tax annual renewal or entity registration | [Company formation](kh-company-formation.md): patent scope/class/start date/activity/place rules; current amended formation-law conditions remain open. |
| Currency: KHR statutory tables, USD documents or conversion | Destination skill intake: identify actual currency and obtain the operative official conversion instruction and period rate; no USD approximation is a filing rule. |
| Tax administration / authority / submission evidence | [GDT](https://www.tax.gov.kh/en/) and the relevant destination: use the actual service/calendar, preserve return/payment acknowledgments and notices. |

Read the destination's complete scope, Ask section, method, exceptions and actual source-read dates. Carry its unconfirmed items into the output; do not turn a partial skill into a completed tax opinion. Keep employee, company, VAT and social liabilities separate even if the same bank account pays them. Return a routing brief identifying the destination, facts needed and unresolved condition before a calculation starts.

## Boundary and exception table

| Situation | Routing action |
|---|---|
| Residence, period, entity or tax uncertain | Hold the answer's amount/deadline and resolve the actual fact in the relevant destination. |
| NSSF assessment, amended company-law conditions or ordinary physical-person implementing detail missing | Retain the README partial-coverage warning and refer the unresolved application. |
| QIP/SEZ, treaty/foreign credit, special sector or enforcement | Use destination referral conditions with the actual certificate/contract/notice; ordinary examples do not decide the specialist application. |
| More than one tax applies | Use each relevant destination and reconcile the shared facts; do not substitute one calculation for the others. |

## When to refuse or refer

Do not compute, file or promise a deadline from this routing page. Refer any application beyond a destination's confirmed scope and state the missing instrument or fact. No tax is labelled absent merely because this pack lacks a complete skill.

## Sources

| Source | Official URL | Read for / actual date |
|---|---|---|
| Law on Taxation, original Khmer income/salary/VAT and patent sections, specified operative passages and neighboring exceptions | https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/816f7e7b-e4be-4d8f-a789-e587b92dbe2e | Tax distinctions and route ownership: original pages 3-19 and 25-32 read 2026-11-14; pages 20-24 and 38-39 read 2026-11-15; nowhole-statute-readclaim |
| Prakas575, all original Khmer pages | https://www.tax.gov.kh/u6rhf7ogbi6/gdtstream/fb78dfde-8342-4e3c-80e0-84ef81919c70 | Salary employment/residence/base/benefit/filing distinctions;2026-11-15 |
| GDT official authority site and actual calendar | https://www.tax.gov.kh/en/ | Authority/calendar route, actualperiodnotfutureextensions;2026-11-14 |

Not yet confirmed: current NSSF assessment/transition, full current amended company-law compliance, detailed current physical-person/small-taxpayer implementation, exact FX/rounding/filing boxes and specialist applications identified by the destinations. These remain partial/referral items, not rates or deadlines supplied by this router. Every original overview topic is retained as a destination above; calculation figures now have one owner in the linked skills.

Built from the law. Written by Codex. Not reviewed by an accountant.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.
