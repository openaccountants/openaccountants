---
name: to-tax-overview
description: >
  Route Tonga 2026 individual/company tax, withholding, Consumption Tax, payroll/retirement and company-registration questions to their source-linked calculation owners. Establish actual taxpayer, period and activity facts; preserve unresolved domain and source limitations without duplicating rates or deadlines.
jurisdiction: TO
category: orchestrator
type: router
tax_year: 2026
last_updated: 2026-11-16
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
version: 0.1
---

# Tonga Tax Overview v0.1

**General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

Route a Tonga 2026 tax or business-registration question to the skill that owns its calculation. The authority is the Ministry of Revenue and Customs (MORC); monetary tax returns, financial statements and payments use Tongan currency (Tongan pa'anga, TOP/T$) under the Revenue Services Administration Regulations. Company registrations use the official Business Entities registry and have their own legal/licensing workflow.

This file carries no operative tax rates, threshold amounts, deadline values or computations. Use the current source-linked owner for those values and all conditions. Taxable residence, legal entity, source, year end and registration status determine the route; an old pack headline is not enough to select a filing date.

## Ask the client first

Obtain the actual legal/taxpayer type and question; individual home/presence/employment-source or company formation/management/partner-residence facts; actual fiscal/accounts period; activities and taxable/exempt sales/imports/foreign services; employee/retirement status; registrations, returns, receipts, notices and any purported exemption/election/treaty. Ask only for facts that change the relevant branch; do not request irrelevant payroll data for a simple company-name filing.

## The method, step by step

| Job | Load this owner | Route and limitation |
|---|---|---|
| Individual residence, ordinary employment tax, employee certificates/refund or business eligibility | [Individual income tax](to-income-tax.md) | Establish rolling/adjacent-year residence, source and exemptions; use its current marginal table and filing route. A fiscal year is not automatically a calendar year. |
| Company net-income tax, company fiscal year, PE/source or payment withholding | [Corporate income tax](to-corporate-income-tax.md) | Determine company tax classification and actual accounts year before rates, withholding categories, credits and filing dates. A qualifying individual small-business regime is not a company concession. |
| Consumption Tax registration, domestic supplies, exports, credits, imports or periodic return | [Consumption Tax](to-vat-gst.md) | Establish taxable activity, effective registration, period, place/time/value and credit documents; distinguish exempt/zero-rated and special classifications. |
| Employer PAYE, NRBF employee/employer amounts or payroll calendar | [Payroll and retirement](to-payroll-social.md), with the individual-tax owner | Separate tax gross from Fund earnings and employee cash deductions from employer costs. Retain unresolved Fund coverage/remittance questions. |
| Company/entity choice, local or overseas registration, registry costs or annual-return intake | [Company formation](to-company-formation.md) | Confirm legal form/ownership/activity and current online service; incorporation, foreign certification, business licence and tax registration are distinct. |
| Transfer pricing, detailed treaty or unsupported cross-border planning | [Pack coverage map](README.md) and the relevant existing owner’s referral | These dedicated domains remain missing; identify the actual law/relationship/transaction needed and refer rather than invent a complete route. |

Read the selected skill in full, including its Sources and Not yet confirmed line. Complete the required intake, apply the confirmed conditions, produce the owner’s working paper and use its current approved form/acceptance/payment checks. If a job crosses domains, link their results without copying the same rate into this router. A company with employees or taxable sales can need several owners, but each obligation remains separately classified and reconciled.

The old overview’s personal top rate/tax-free threshold, company rate, CT standard/export/import rates, annual filing date and CT frequency now live only with the responsible owner. The general worldwide-resident/Tonga-source-nonresident distinction is subject to actual exemptions, source tests and final-tax/PE branches in the income-tax owners. The company accounts period can differ from the ordinary individual fiscal period; obtain the actual period instead of imposing the historical headline.

## When to refuse or refer

Stop the affected computation when the owner’s required source, classification, period, registration, election or taxpayer document is unavailable. Do not replace an unresolved law with a vendor rate or the old approximate headline. Refer uncertain PE/treaty, TP, special-industry, entity-law and Fund timing/coverage positions to a qualified professional with the exact unresolved point and supporting records. A mechanically current skill is not accountant approval or complete jurisdiction coverage.

For filing handoff, provide entity/TIN and period, selected owner/version, source dates, calculation/reconciliation, actual form route, status of return acceptance/payment and open items. Leave unsupported applications pending. This router does not authorize submission, payment or a claim of completion from a saved draft.

## Sources

| Source and actual reading scope | Official URL | Read on |
|---|---|---|
| Income Tax Act, Cap.11.05, 2020 consolidation: Read for s 2 fiscal year, ss 4-11, Part 6 heading and ss 60-67(including both 65A headings), 68-69: period, residence, source, foreign/PE/associate/avoidance boundaries, ordinary filing and separate-tax branches | https://ago.gov.to/cms/images/LEGISLATION/PRINCIPAL/2007/2007-0010/IncomeTaxAct_3.pdf | 2026-11-15 |
| MORC company/partnership guidance: Read for complete current resident/non-resident company scope and published rate guidance | https://www.revenue.gov.to/company-partnership-corporative-society-trust | 2026-11-16 |
| MORC Consumption Tax Overview: Read for complete CT scope/import/value/credit overview | https://www.revenue.gov.to/consumption-tax-overview | 2026-11-15 |
| Revenue Services Administration Regulations 2021: Read for regs 14-16,24-26: currency, payment/receipt and actual procedural directions | https://www.revenue.gov.to/sites/default/files/inline-files/RevenueServicesAdministrationRegulations2021_FINAL_Eng_0.pdf | 2026-11-15 |

Not yet confirmed: This is a routing skill and does not supply a complete Tonga return or a comprehensive list of taxes. Follow each linked skill’s current limitations. The original universal July-to-June company-year, unqualified 30 April annual date and two-month CT-period assumptions have been replaced by the actual owner’s period analysis. Conditional 2020-amendment commencement and affected income exemption/CT certificate, receipt, refund-limit applications remain held in the income/CT owners. Specific unrecovered rate Orders, complete current CT special classifications, NRBF age/remittance conflicts, live form mapping, TP/treaty applications and entity-specific legal conditions remain open where stated in those owners. No accountant approval is claimed.
